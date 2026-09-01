"""Tests for the participant codebook validator."""

from pathlib import Path
import sys
import unittest


STARTER_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(STARTER_DIR))

from validate_codebook import find_cycle, find_unmapped_candidate_codes


class ValidateCodebookTests(unittest.TestCase):
    def test_find_cycle_returns_closed_path(self):
        self.assertEqual(find_cycle({"D1": "F1", "F1": "D1"}), ["D1", "F1", "D1"])

    def test_find_cycle_returns_empty_list_for_tree(self):
        self.assertEqual(find_cycle({"D1": "F1", "F1": "S1", "S1": ""}), [])

    @unittest.skip("Ćwiczenie: poproś Codexa o implementację i usuń dekorator skip.")
    def test_unmapped_candidates_exclude_theoretical_and_needs_review(self):
        rows = [
            {"code_id": "D1", "code_level": "descriptive", "parent_code_id": "", "review_status": "candidate"},
            {"code_id": "F1", "code_level": "focused", "parent_code_id": "S1", "review_status": "candidate"},
            {"code_id": "S2", "code_level": "synthetic", "parent_code_id": "", "review_status": "needs_review"},
            {"code_id": "T1", "code_level": "theoretical", "parent_code_id": "", "review_status": "candidate"},
        ]
        self.assertEqual(find_unmapped_candidate_codes(rows), ["D1"])


if __name__ == "__main__":
    unittest.main()
