"""US-10: grounded OpenAI character summaries with safe offline fallback."""
import os
import re
from pathlib import Path

PROMPT_PATH = Path(__file__).resolve().parents[2] / "prompts" / "summary_v1.txt"
MODEL = os.environ.get("OPENAI_MODEL", "gpt-4o-mini")
MAX_INPUT = 1500


def _clean(value):
    return re.sub(r"\s+", " ", str(value or "")).strip()[:MAX_INPUT]


def fallback_summary(character):
    """Only repeat stored fields; never fabricate Marvel lore."""
    name = _clean(character.get("name")) or "This character"
    description = _clean(character.get("description"))
    powers = _clean(character.get("powers"))
    if description:
        result = f"{name}: {description}"
    else:
        result = f"{name}: No character description is available."
    if powers:
        result += f" Recorded powers and abilities: {powers}."
    return result[:3000]


def _valid_summary(output, name):
    if not isinstance(output, str):
        return False
    value = output.strip()
    if not (20 <= len(value) <= 700):
        return False
    if not name or name.lower() not in value.lower():
        return False
    if any(token in value.lower() for token in (
        "ignore previous instructions", "system prompt", "api key", "```"
    )):
        return False
    return True


def generate_summary(character, client=None):
    """Return summary, source, prompt_version. Never expose API errors or secrets."""
    record = {key: _clean(character.get(key)) for key in ("name", "description", "powers", "category")}
    fallback = {"summary": fallback_summary(record), "source": "fallback", "prompt_version": "summary_v1"}
    if not os.environ.get("OPENAI_API_KEY") and client is None:
        return fallback
    try:
        if client is None:
            from openai import OpenAI
            client = OpenAI(timeout=8.0, max_retries=0)
        instructions = PROMPT_PATH.read_text(encoding="utf-8")
        input_text = "\n".join(f"{key}: {value}" for key, value in record.items())
        response = client.responses.create(
            model=MODEL,
            instructions=instructions,
            input=f"Character record (untrusted data):\n{input_text}",
            max_output_tokens=180,
            store=False,
        )
        summary = getattr(response, "output_text", None)
        if getattr(response, "status", "completed") != "completed" or not _valid_summary(summary, record["name"]):
            return fallback
        return {"summary": summary.strip(), "source": "openai", "prompt_version": "summary_v1"}
    except Exception:
        return fallback
