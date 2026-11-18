"""Offline tests proving the model configuration sanity gate works."""
import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from run_evals import model_contract_check


class ModelContractTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.baseline = Path(self.directory.name) / "approved_model.json"
        self.baseline.write_text(json.dumps({"model": "gpt-4o-mini"}), encoding="utf-8")

    def tearDown(self):
        self.directory.cleanup()

    def test_approved_model_passes(self):
        self.assertTrue(model_contract_check("gpt-4o-mini", self.baseline)[0])

    def test_unapproved_model_fails(self):
        self.assertFalse(model_contract_check("different-model", self.baseline)[0])

    def test_environment_change_is_detected(self):
        with patch.dict(os.environ, {"OPENAI_MODEL": "different-model"}):
            self.assertFalse(model_contract_check(baseline_path=self.baseline)[0])

    def test_missing_model_baseline_fails_closed(self):
        self.baseline.write_text("{}", encoding="utf-8")
        with self.assertRaises(KeyError):
            model_contract_check("gpt-4o-mini", self.baseline)


if __name__ == "__main__":
    unittest.main()
