"""US-11 offline tests; all API responses are mocked."""
import json
import unittest
from types import SimpleNamespace
from unittest.mock import Mock, patch

from .ai_recommendations import recommend, rank_candidates, PROMPT_PATH

ROSTER = [
    {"id": "1", "name": "Iron Man", "description": "Uses armor", "powers": "Flight. Armor", "category": "Hero"},
    {"id": "2", "name": "Falcon", "description": "Flying hero", "powers": "Flight", "category": "Hero"},
    {"id": "3", "name": "Thor", "description": "Thunder hero", "powers": "Lightning", "category": "Hero"},
    {"id": "4", "name": "Loki", "description": "Trickster", "powers": "Magic", "category": "Villain"},
]


class RecommendationTests(unittest.TestCase):
    def test_rank_excludes_selected_and_is_stable(self):
        result = rank_candidates(ROSTER[0], ROSTER)
        self.assertEqual(result[0]["name"], "Falcon")
        self.assertNotIn("Iron Man", [c["name"] for c in result])

    def test_valid_mocked_ai(self):
        client = Mock()
        client.responses.create.return_value = SimpleNamespace(
            status="completed", output_text=json.dumps({
                "names": ["Falcon", "Thor"],
                "reason": "Falcon shares flight while Thor is also a recorded hero.",
            })
        )
        result = recommend(ROSTER[0], ROSTER, client=client)
        self.assertEqual(result["source"], "openai")
        self.assertEqual([x["name"] for x in result["recommendations"]], ["Falcon", "Thor"])

    def test_invalid_hallucinated_name_falls_back(self):
        client = Mock()
        client.responses.create.return_value = SimpleNamespace(
            status="completed", output_text=json.dumps({
                "names": ["Not In Roster"], "reason": "A completely invented recommendation."
            })
        )
        self.assertEqual(recommend(ROSTER[0], ROSTER, client=client)["source"], "fallback")

    def test_timeout_falls_back(self):
        client = Mock()
        client.responses.create.side_effect = TimeoutError()
        self.assertEqual(recommend(ROSTER[0], ROSTER, client=client)["source"], "fallback")

    def test_missing_key_falls_back(self):
        with patch.dict("os.environ", {"OPENAI_API_KEY": ""}):
            self.assertEqual(recommend(ROSTER[0], ROSTER)["source"], "fallback")

    def test_prompt_grounding(self):
        self.assertIn("untrusted DATA", PROMPT_PATH.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
