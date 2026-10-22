import contextlib
import io
import tempfile
import unittest
from pathlib import Path

from campus_tool.__main__ import main


class CliTests(unittest.TestCase):
    def run_cli(self, args):
        output, errors = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(output), contextlib.redirect_stderr(errors):
            code = main(args)
        return code, output.getvalue(), errors.getvalue()

    def test_packaged_examples_and_combined_filter(self):
        code, output, errors = self.run_cli(["--category", "식사", "--max-price", "5500"])
        self.assertEqual(code, 0)
        self.assertIn("예시 학생식당", output)
        self.assertNotIn("예시 카페", output)
        self.assertEqual(errors, "")

    def test_no_matches_is_success(self):
        code, output, _ = self.run_cli(["--category", "없는종류"])
        self.assertEqual(code, 0)
        self.assertIn("조건에 맞는 항목이 없습니다", output)

    def test_negative_price_is_error(self):
        code, _, errors = self.run_cli(["--max-price", "-1"])
        self.assertEqual(code, 2)
        self.assertIn("0 이상", errors)

    def test_missing_data_is_error(self):
        with tempfile.TemporaryDirectory() as directory:
            code, _, errors = self.run_cli(["--data-dir", str(Path(directory) / "missing")])
        self.assertEqual(code, 2)
        self.assertIn("데이터 폴더", errors)


if __name__ == "__main__":
    unittest.main()
