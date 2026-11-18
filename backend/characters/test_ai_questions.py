"""Offline US-12 tests. Never call the real AI API."""
import unittest
from types import SimpleNamespace
from unittest.mock import Mock, patch
from .ai_questions import answer_question, fallback_answer, PROMPT_PATH

CHARACTER = {"name": "Ant-Man", "description": "Uses Pym technology to shrink or grow.",
             "powers": "Size manipulation. Ant communication", "category": "Hero"}


class CharacterQuestionsTests(unittest.TestCase):
    def test_valid_mocked_answer(self):
        client = Mock()
        client.responses.create.return_value = SimpleNamespace(
            status="completed",
            output_text="Ant-Man can change size using the recorded Pym technology.",
        )
        result = answer_question(CHARACTER, "What can Ant-Man do?", client=client)
        self.assertEqual(result["source"], "openai")
        self.assertEqual(result["prompt_version"], "character_qa_v1")
        client.responses.create.assert_called_once()

    def test_timeout_fallback(self):
        client = Mock()
        client.responses.create.side_effect = TimeoutError("provider timed out")
        self.assertEqual(answer_question(CHARACTER, "What powers?", client=client)["source"], "fallback")

    def test_invalid_output_fallback(self):
        client = Mock()
        client.responses.create.return_value = SimpleNamespace(status="completed", output_text="OK")
        self.assertEqual(answer_question(CHARACTER, "What powers?", client=client)["source"], "fallback")

    def test_incomplete_output_fallback(self):
        client = Mock()
        client.responses.create.return_value = SimpleNamespace(
            status="incomplete", output_text="Ant-Man can shrink and grow."
        )
        self.assertEqual(answer_question(CHARACTER, "What powers?", client=client)["source"], "fallback")

    def test_missing_key_fallback(self):
        with patch.dict("os.environ", {"OPENAI_API_KEY": ""}):
            self.assertEqual(answer_question(CHARACTER, "Who is this?")["source"], "fallback")

    def test_unknown_question_does_not_invent(self):
        answer = fallback_answer(CHARACTER, "Who is his father?")
        self.assertIn("can't verify", answer)

    def test_prompt_grounding(self):
        prompt = PROMPT_PATH.read_text(encoding="utf-8")
        self.assertIn("ONLY the supplied character record", prompt)


if __name__ == "__main__":
    unittest.main()
