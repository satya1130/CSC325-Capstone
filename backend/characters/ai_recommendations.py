"""US-11: roster-grounded AI recommendations with deterministic offline fallback."""
import json
import os
import re
from pathlib import Path

PROMPT_PATH = Path(__file__).resolve().parents[2] / "prompts" / "recommend_v1.txt"


def clean(value):
    return re.sub(r"\s+", " ", str(value or "")).strip()[:400]


def rank_candidates(selected, roster):
    """Stable ranking using overlapping stored powers and category; no API required."""
    chosen_id = str(selected.get("id", ""))
    words = set(re.findall(r"[a-z]{4,}", clean(selected.get("powers")).lower()))
    results = []
    for item in roster:
        if str(item.get("id", "")) == chosen_id:
            continue
        other_words = set(re.findall(r"[a-z]{4,}", clean(item.get("powers")).lower()))
        overlap = len(words & other_words)
        same_category = int(bool(selected.get("category")) and selected.get("category") == item.get("category"))
        results.append((-(overlap * 3 + same_category), clean(item.get("name")).lower(), item))
    return [entry[2] for entry in sorted(results)[:3]]


def recommend(selected, roster, client=None):
    candidates = rank_candidates(selected, roster)
    fallback = {
        "recommendations": [{"id": str(c["id"]), "name": c["name"]} for c in candidates],
        "reason": "Suggested using recorded powers and character categories.",
        "source": "fallback",
        "prompt_version": "recommend_v1",
    }
    if not candidates or (not os.getenv("OPENAI_API_KEY") and client is None):
        return fallback
    try:
        if client is None:
            from openai import OpenAI
            client = OpenAI(timeout=8.0, max_retries=0)
        record = lambda c: {k: clean(c.get(k)) for k in ("name", "description", "powers", "category")}
        payload = {"selected": record(selected), "candidates": [record(c) for c in candidates]}
        response = client.responses.create(
            model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
            instructions=PROMPT_PATH.read_text(encoding="utf-8"),
            input=json.dumps(payload), max_output_tokens=220, store=False,
        )
        if getattr(response, "status", "completed") != "completed":
            return fallback
        result = json.loads(getattr(response, "output_text", "") or "")
        names = result.get("names")
        reason = result.get("reason")
        allowed = {c["name"]: c for c in candidates}
        if (not isinstance(names, list) or not 1 <= len(names) <= 3
                or any(not isinstance(n, str) or n not in allowed for n in names)
                or len(set(names)) != len(names)
                or not isinstance(reason, str) or not 15 <= len(reason.strip()) <= 300):
            return fallback
        return {
            "recommendations": [{"id": str(allowed[n]["id"]), "name": n} for n in names],
            "reason": reason.strip(), "source": "openai", "prompt_version": "recommend_v1",
        }
    except (Exception):
        return fallback
