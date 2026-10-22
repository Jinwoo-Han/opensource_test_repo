import tempfile
import unittest
from pathlib import Path

from campus_tool.catalog import Place, filter_places, load_catalog


class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.directory = Path(self.temp.name)

    def write(self, content, name="entries.csv", encoding="utf-8"):
        (self.directory / name).write_text(content, encoding=encoding)

    def test_korean_bom_and_quoted_comma(self):
        self.write('id,name,category,price\na,"가상, 식당",식사,5000\n', encoding="utf-8-sig")
        self.assertEqual(load_catalog(self.directory), [Place("a", "가상, 식당", "식사", 5000)])

    def test_multiple_files(self):
        self.write("id,name,category,price\nb,카페,음료,2000\n", "b.csv")
        self.write("id,name,category,price\na,도서관,공간,0\n", "a.csv")
        self.assertEqual([p.id for p in load_catalog(self.directory)], ["a", "b"])

    def test_header_only_is_empty_catalog(self):
        self.write("id,name,category,price\n")
        self.assertEqual(load_catalog(self.directory), [])

    def test_invalid_rows_are_rejected(self):
        contents = [
            "", "name,price\n카페,2000\n",
            "id,name,category,price\na,카페,음료\n",
            "id,name,category,price\na,카페,음료,2000,extra\n",
            "id,name,category,price\na, ,음료,2000\n",
            "id,name,category,price\na,카페,음료,not-a-number\n",
            "id,name,category,price\na,카페,음료,-1\n",
        ]
        for content in contents:
            with self.subTest(content=content):
                self.write(content)
                with self.assertRaises(ValueError):
                    load_catalog(self.directory)

    def test_duplicate_id_across_files(self):
        self.write("id,name,category,price\na,식당,식사,5000\n", "a.csv")
        self.write("id,name,category,price\na,카페,음료,2000\n", "b.csv")
        with self.assertRaisesRegex(ValueError, "중복 ID"):
            load_catalog(self.directory)

    def test_missing_directory_and_no_csv(self):
        with self.assertRaises(FileNotFoundError):
            load_catalog(self.directory / "missing")
        with self.assertRaisesRegex(ValueError, "CSV 파일"):
            load_catalog(self.directory)

    def test_filter_includes_price_boundary_without_mutation(self):
        places = [Place("a", "식당", "식사", 5000), Place("b", "카페", "음료", 2000)]
        self.assertEqual(filter_places(places, "식사", 5000), [places[0]])
        self.assertEqual(filter_places(places, "공간"), [])
        self.assertEqual(filter_places(places, max_price=0), [])
        self.assertEqual(len(places), 2)
        with self.assertRaises(ValueError):
            filter_places(places, max_price=-1)

    def test_contribution_csv_files_are_valid(self):
        # 새 기여 파일도 모두 읽는다. 특정 개수나 파일명을 강제하지 않는다.
        root = Path(__file__).resolve().parents[1]
        load_catalog(root / "examples" / "submissions")


if __name__ == "__main__":
    unittest.main()
