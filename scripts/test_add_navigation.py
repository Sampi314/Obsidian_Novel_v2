import unittest
from scripts.add_navigation import extract_chapter_number

class TestExtractChapterNumber(unittest.TestCase):
    def test_standard_chapter(self):
        filename = "Chương_001_Tiêu_Đề.md"
        self.assertEqual(extract_chapter_number(filename), 1.0)

    def test_fractional_chapter(self):
        filename = "Chương_001_5_Tiêu_Đề.md"
        self.assertEqual(extract_chapter_number(filename), 1.5)

    def test_zero_padded_chapter(self):
        filename = "Chương_00005_Tiêu_Đề.md"
        self.assertEqual(extract_chapter_number(filename), 5.0)

    def test_large_chapter_number(self):
        filename = "Chương_1234_Tiêu_Đề.md"
        self.assertEqual(extract_chapter_number(filename), 1234.0)

    def test_complex_filename(self):
        filename = "Chương_100_Tên_Dài_Nhiều_Dấu_Gạch_Dưới.md"
        self.assertEqual(extract_chapter_number(filename), 100.0)

    def test_non_matching_filename_readme(self):
        filename = "README.md"
        self.assertEqual(extract_chapter_number(filename), float('inf'))

    def test_non_matching_filename_random(self):
        filename = "random_file.txt"
        self.assertEqual(extract_chapter_number(filename), float('inf'))

    def test_chapter_zero(self):
        filename = "Chương_000_Mở_Đầu.md"
        self.assertEqual(extract_chapter_number(filename), 0.0)

if __name__ == '__main__':
    unittest.main()
