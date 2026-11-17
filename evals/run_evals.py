
"""Marvel Clash Sprint 3 offline AI evaluation runner.

Run from the project root:
    python evals/run_evals.py

Uses mocked OpenAI responses.
No API key or network required.
"""

import json
import re
import sys
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock, patch

ROOT = Path(__file__).resolve().parents[1]
BACKEND = ROOT / "backend"
sys.path.insert(0, str(BACKEND))

from characters.ai_summary import generate_summary, fallback_summary

DATASET = ROOT / "evals" / "golden_set.json"

MIN_CASES = 15
FACT_THRESHOLD = 1.00
GROUNDING_THRESHOLD = 1.00
CONSISTENCY_THRESHOLD = 1.00


def normalize(text):
    return re.sub(r"\s+", " ", str(text).lower()).strip()


def expected_facts_present(summary, expected_facts):
    """Check required keywords in a generated summary."""
    output = normalize(summary)
    return all(
        normalize(fact) in output
        for fact in expected_facts
    )


def grounding_check(character, summary):
    """Conservative lexical grounding proxy.

    Detects unfamiliar words, but cannot prove that
    every statement is factually supported.
    """
    source = " ".join(
        str(value or "") for value in character.values()
    )

    source_words = set(
        re.findall(r"[a-z0-9]+", source.lower())
    )
    output_words = set(
        re.findall(r"[a-z0-9]+", summary.lower())
    )

    allowed = {
        "is", "a", "an", "the", "and", "or", "with",
        "who", "has", "have", "can", "uses", "use",
        "known", "for", "his", "her", "their", "of",
        "in", "to", "as", "by", "from", "abilities",
        "ability", "recorded", "no", "available",
        "character", "description", "powers",
    }

    unsupported_words = (
        output_words - source_words - allowed
    )

    return (
        len(unsupported_words) == 0,
        sorted(unsupported_words),
    )


def make_mock_client(summary):
    client = Mock()
    client.responses.create.return_value = SimpleNamespace(
        status="completed",
        output_text=summary,
    )
    return client


def evaluate_case(case):
    character = case["character"]
    expected_facts = case["expected_facts"]

    summary = fallback_summary(character)

    result = generate_summary(
        character,
        client=make_mock_client(summary),
    )

    facts_ok = expected_facts_present(
        result["summary"], expected_facts
    )

    grounded, unsupported = grounding_check(
        character, result["summary"]
    )

    second = generate_summary(
        character,
        client=make_mock_client(summary),
    )

    consistent = (
        result["summary"] == second["summary"]
        and result["source"] == second["source"]
    )

    return {
        "id": case["id"],
        "name": character["name"],
        "facts_ok": facts_ok,
        "grounded": grounded,
        "unsupported_words": unsupported,
        "consistent": consistent,
        "source": result["source"],
    }


def test_hallucination_detection():
    """Prove the grounding proxy catches an invented power."""
    character = {
        "name": "Iron Man",
        "description": "Uses advanced armored technology.",
        "powers": "Flight and repulsor blasts",
        "category": "Hero",
    }

    valid_summary = fallback_summary(character)

    invented_summary = (
        valid_summary
        + " Iron Man also has teleportation powers."
    )

    valid_grounded, _ = grounding_check(
        character, valid_summary
    )

    invented_grounded, unsupported = grounding_check(
        character, invented_summary
    )

    passed = (
        valid_grounded
        and not invented_grounded
        and "teleportation" in unsupported
    )

    return passed, unsupported


def test_fallback_detection():
    """Prove a failed AI request returns stored facts."""
    character = {
        "name": "Iron Man",
        "description": "Uses advanced armored technology.",
        "powers": "Flight and repulsor blasts",
        "category": "Hero",
    }

    client = Mock()
    client.responses.create.side_effect = TimeoutError(
        "Simulated API timeout"
    )

    result = generate_summary(
        character, client=client
    )

    return (
        result["source"] == "fallback"
        and result["summary"] == fallback_summary(character)
    )


def main():
    with DATASET.open(encoding="utf-8") as file:
        cases = json.load(file)

    if len(cases) < MIN_CASES:
        print(
            f"FAIL: Expected at least {MIN_CASES} cases, "
            f"found {len(cases)}."
        )
        return 1

    results = []

    with patch.dict(
        "os.environ", {"OPENAI_API_KEY": ""}
    ):
        for case in cases:
            results.append(evaluate_case(case))

        hallucination_passed, unsupported = (
            test_hallucination_detection()
        )

        fallback_passed = test_fallback_detection()

    print("\nMARVEL CLASH - SPRINT 3 AI EVALUATION")
    print("=" * 60)

    for result in results:
        passed = (
            result["facts_ok"]
            and result["grounded"]
            and result["consistent"]
        )

        status = "PASS" if passed else "FAIL"

        print(
            f"{status}: {result['id']:02d} "
            f"{result['name']}"
        )

        if not result["facts_ok"]:
            print("  Missing expected facts")

        if not result["grounded"]:
            print(
                "  Unsupported words:",
                ", ".join(result["unsupported_words"])
            )

        if not result["consistent"]:
            print("  Inconsistent outputs")

    total = len(results)

    fact_score = sum(
        result["facts_ok"] for result in results
    ) / total

    grounding_score = sum(
        result["grounded"] for result in results
    ) / total

    consistency_score = sum(
        result["consistent"] for result in results
    ) / total

    print("\nRESULTS")
    print("-" * 60)
    print(f"Cases:       {total}")
    print(f"Fact recall: {fact_score:.0%}")
    print(f"Grounding:   {grounding_score:.0%}")
    print(f"Consistency: {consistency_score:.0%}")

    print("\nSAFETY CHECKS")
    print("-" * 60)

    print(
        "Hallucination detection:",
        "PASS" if hallucination_passed else "FAIL"
    )

    print(
        "Invented words detected:",
        ", ".join(unsupported) or "None"
    )

    print(
        "API timeout fallback:",
        "PASS" if fallback_passed else "FAIL"
    )

    passed = (
        fact_score >= FACT_THRESHOLD
        and grounding_score >= GROUNDING_THRESHOLD
        and consistency_score >= CONSISTENCY_THRESHOLD
        and hallucination_passed
        and fallback_passed
    )

    print("\nOVERALL:", "PASS" if passed else "FAIL")

    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
