"""Sprint 3 offline golden-set evaluation: deterministic fixtures, no API calls.

Run: python evals/run_evals.py
The fixture results validate the pipeline and its detection rules, NOT live-model
accuracy. Re-evaluate and review real model outputs when changing provider/model.
"""
import json
import re
import sys
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "backend"))
from characters.ai_summary import generate_summary, fallback_summary
from characters.ai_recommendations import recommend
from characters.ai_questions import answer_question

DATASET = ROOT / "evals" / "golden_set.json"
THRESHOLDS = {"facts": 1.0, "grounding": 1.0, "consistency": 1.0}
ALLOWED = set(("is a an the and or with who has have can uses use known for his her their "
               "of in to as by from abilities ability recorded no available character "
               "description powers").split())


def words(value):
    return set(re.findall(r"[a-z0-9]+", str(value).lower()))


def grounding_check(character, output):
    """Lexical warning proxy; human review is still needed for semantic claims."""
    source = set().union(*(words(value) for value in character.values()))
    unknown = sorted(words(output) - source - ALLOWED)
    return not unknown, unknown


def mock_client(output, status="completed"):
    client = Mock()
    client.responses.create.return_value = SimpleNamespace(output_text=output, status=status)
    return client


def evaluate(case):
    record = case["character"]
    expected = case["expected_output"]
    first = generate_summary(record, client=mock_client(expected))
    second = generate_summary(record, client=mock_client(expected))
    facts = all(fact.lower() in first["summary"].lower() for fact in case["expected_facts"])
    grounded, unknown = grounding_check(record, first["summary"])
    consistent = first == second and first["source"] == "openai"
    return {"id": case["id"], "name": record["name"], "facts": facts,
            "grounding": grounded, "consistency": consistent, "unknown": unknown}


def safety_checks():
    record = {"name": "Iron Man", "description": "Uses advanced armored technology.",
              "powers": "Flight and repulsor blasts", "category": "Hero"}
    valid = "Iron Man: Uses advanced armored technology. Recorded powers and abilities: Flight and repulsor blasts."
    invented = valid + " Iron Man has teleportation."
    safe, _ = grounding_check(record, valid)
    invented_safe, unexpected = grounding_check(record, invented)
    bad = generate_summary(record, client=mock_client(invented))
    # A changed/mock provider response must be caught by the evaluation even if
    # the service itself accepts the output; otherwise the Eval gate is ineffective.
    provider_drift_caught = bad["source"] != "openai" or not grounding_check(record, bad["summary"])[0]
    timeout = Mock()
    timeout.responses.create.side_effect = TimeoutError("simulated")
    fallback = generate_summary(record, client=timeout)
    qa_fallback = answer_question(record, "What powers?", client=timeout)
    rec_fallback = recommend(record, [record, {
        "id": "2", "name": "War Machine", "description": "Armored hero",
        "powers": "Flight", "category": "Hero"}], client=timeout)
    return {
        "hallucination_detector": safe and not invented_safe and "teleportation" in unexpected,
        "changed_provider_output_detected": provider_drift_caught,
        "summary_timeout_fallback": fallback["source"] == "fallback"
            and fallback["summary"] == fallback_summary(record),
        "question_timeout_fallback": qa_fallback["source"] == "fallback",
        "recommendation_timeout_fallback": rec_fallback["source"] == "fallback",
    }


def main():
    cases = json.loads(DATASET.read_text(encoding="utf-8"))
    ids = [case.get("id") for case in cases]
    if len(cases) < 15 or len(set(ids)) != len(ids):
        print("FAIL: Need at least 15 unique golden examples")
        return 1
    results = [evaluate(case) for case in cases]
    scores = {metric: sum(r[metric] for r in results) / len(results)
              for metric in THRESHOLDS}
    checks = safety_checks()
    print("MARVEL CLASH SPRINT 3 OFFLINE EVAL (mocked responses, not live model quality)")
    for result in results:
        ok = all(result[metric] for metric in THRESHOLDS)
        print(f"{'PASS' if ok else 'FAIL'}: {result['id']:02d} {result['name']}"
              + (f" unsupported={result['unknown']}" if result["unknown"] else ""))
    print(f"Golden cases: {len(results)}")
    for metric, threshold in THRESHOLDS.items():
        print(f"{metric}: {scores[metric]:.0%} (minimum {threshold:.0%})")
    for name, passed in checks.items():
        print(f"{name}: {'PASS' if passed else 'FAIL'}")
    passed = all(scores[k] >= threshold for k, threshold in THRESHOLDS.items()) and all(checks.values())
    print("OVERALL:", "PASS" if passed else "FAIL")
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
