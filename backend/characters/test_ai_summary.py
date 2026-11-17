"""Offline tests: no real AI network requests or API key required."""
import unittest
from types import SimpleNamespace
from unittest.mock import Mock, patch
from .ai_summary import generate_summary, fallback_summary, PROMPT_PATH


CHARACTER = {"name": "Iron Man", "description": "Uses advanced armor.", "powers": "Flight", "category": "Hero"}


class SummaryTests(unittest.TestCase):
    def test_valid_mocked_api_response(self):
        client = Mock()
        client.responses.create.return_value = SimpleNamespace(
            status="completed", output_text="Iron Man uses advanced armor and can fly."
        )
        result = generate_summary(CHARACTER, client=client)
        self.assertEqual(result["source"], "openai")
        self.assertEqual(result["prompt_version"], "summary_v1")
        client.responses.create.assert_called_once()

    def test_summary_prompt_has_three_sections_and_grounding(self):
        instructions = PROMPT_PATH.read_text(encoding="utf-8")
        for heading in ("Character Overview", "Key Abilities", "What Makes Them Unique"):
            self.assertIn(heading, instructions)
        self.assertIn("Use ONLY the provided character record", instructions)

    def test_structured_mocked_summary_is_accepted(self):
        client = Mock()
        client.responses.create.return_value = SimpleNamespace(
            status="completed",
            output_text=(
                "Character Overview\\nIron Man uses advanced armor.\\n\\n"
                "Key Abilities\\nHis armor supports flight.\\n\\n"
                "What Makes Them Unique\\nHis armor could offer mobility in a fight."
            ),
        )
        result = generate_summary(CHARACTER, client=client)
        self.assertEqual(result["source"], "openai")
        self.assertIn("What Makes Them Unique", result["summary"])
        self.assertEqual(client.responses.create.call_args.kwargs["max_output_tokens"], 260)

    def test_timeout_falls_back(self):
        client = Mock()
        client.responses.create.side_effect = TimeoutError("timeout")
        self.assertEqual(generate_summary(CHARACTER, client=client)["source"], "fallback")

    def test_invalid_output_falls_back(self):
        client = Mock()
        client.responses.create.return_value = SimpleNamespace(status="completed", output_text="ok")
        self.assertEqual(generate_summary(CHARACTER, client=client)["summary"], fallback_summary(CHARACTER))

    def test_incomplete_output_falls_back(self):
        client = Mock()
        client.responses.create.return_value = SimpleNamespace(status="incomplete", output_text="Iron Man uses armor.")
        self.assertEqual(generate_summary(CHARACTER, client=client)["source"], "fallback")

    def test_missing_key_falls_back(self):
        with patch.dict("os.environ", {"OPENAI_API_KEY": ""}):
            self.assertEqual(generate_summary(CHARACTER)["source"], "fallback")

    def test_no_record_does_not_invent(self):
        result = fallback_summary({"name": "Unknown"})
        self.assertIn("No character description is available", result)


if __name__ == "__main__":
    unittest.main()
