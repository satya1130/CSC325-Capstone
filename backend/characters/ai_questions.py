"""US-12: grounded character questions, with safe deterministic offline fallback."""
import os
import re
from pathlib import Path

PROMPT_PATH = Path(__file__).resolve().parents[2] / "prompts" / "character_qa_v1.txt"
MAX_QUESTION_LENGTH = 300


def clean(value, limit=1200):
    return re.sub(r"\s+", " ", str(value or "")).strip()[:limit]


def fallback_answer(character, question):
    """Never invent facts when the AI provider is unavailable."""
    name = clean(character.get("name"), 100) or "This character"
    description = clean(character.get("description"))
    powers = clean(character.get("powers"))
    q = question.casefold()
    if any(word in q for word in ("power", "abilit", "skill", "do", "fight", "strong")):
        return f"{name}'s recorded powers and abilities: {powers}." if powers else f"No powers or abilities are recorded for {name}."
    if (q.startswith(("who is this character", "who is "+name.casefold(), "describe ", "tell me about ", "what is "+name.casefold())) or q in ("who is this?", "who is this character?", "describe this character")):
        return f"{name}: {description}" if description else f"No description is recorded for {name}."
    return f"I can't verify that from {name}'s stored character profile. The available description is: {description}" if description else f"I can't verify that from {name}'s stored character profile."


def answer_question(character, question, client=None):
    """Return answer, source and prompt version. Provider failures never reach the user."""
    name = clean(character.get("name"), 100)
    record = {key: clean(character.get(key)) for key in ("name", "description", "powers", "category")}
    fallback = {"answer": fallback_answer(record, question), "source": "fallback", "prompt_version": "character_qa_v1"}
    if not os.getenv("OPENAI_API_KEY") and client is None:
        return fallback
    try:
        if client is None:
            from openai import OpenAI
            client = OpenAI(timeout=8.0, max_retries=0)
        import json
        response = client.responses.create(
            model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
            instructions=PROMPT_PATH.read_text(encoding="utf-8"),
            input=json.dumps({"character_record_untrusted": record, "visitor_question_untrusted": question}),
            max_output_tokens=180,
            store=False,
        )
        answer = getattr(response, "output_text", None)
        if (getattr(response, "status", "completed") != "completed"
                or not isinstance(answer, str)
                or not 15 <= len(answer.strip()) <= 900
                or not name or name.casefold() not in answer.casefold()
                or any(term in answer.casefold() for term in (
                    "system prompt", "api key", "ignore previous instructions", "```"
                ))):
            return fallback
        return {"answer": answer.strip(), "source": "openai", "prompt_version": "character_qa_v1"}
    except Exception:
        return fallback
