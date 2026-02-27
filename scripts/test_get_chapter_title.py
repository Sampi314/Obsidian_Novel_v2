import unittest
import os
import tempfile
from scripts.utils import get_chapter_title

class TestGetChapterTitle(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        import shutil
        shutil.rmtree(self.test_dir)

    def create_test_file(self, filename, content):
        filepath = os.path.join(self.test_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return filepath

    def test_standard_title(self):
        content = "# Chương 1: Mở Đầu\n\nNội dung chương..."
        filepath = self.create_test_file("standard.md", content)
        self.assertEqual(get_chapter_title(filepath), "Chương 1: Mở Đầu")

    def test_title_after_frontmatter(self):
        content = "---\ntitle: Test\n---\n\n# Chương 2: Tiếp Theo\n"
        filepath = self.create_test_file("frontmatter.md", content)
        self.assertEqual(get_chapter_title(filepath), "Chương 2: Tiếp Theo")

    def test_title_after_comments(self):
        content = "<!-- Comment -->\n# Chương 3: Bí Mật\n"
        filepath = self.create_test_file("comments.md", content)
        self.assertEqual(get_chapter_title(filepath), "Chương 3: Bí Mật")

    def test_no_title(self):
        content = "Nội dung không có tiêu đề.\n"
        filepath = self.create_test_file("no_title.md", content)
        self.assertEqual(get_chapter_title(filepath), "Không có tiêu đề")

    def test_indented_title(self):
        # This triggers the second pass logic in the current implementation
        content = "  # Chương 4: Thử Thách\n"
        filepath = self.create_test_file("indented.md", content)
        self.assertEqual(get_chapter_title(filepath), "Chương 4: Thử Thách")

    def test_vietnamese_title(self):
        content = "# Chương 5: Đêm Trăng Máu\n"
        filepath = self.create_test_file("vietnamese.md", content)
        self.assertEqual(get_chapter_title(filepath), "Chương 5: Đêm Trăng Máu")

    def test_ignore_navigation_block(self):
        content = "<!-- NAVIGATION_START -->\n<div style='...'>...</div>\n<!-- NAVIGATION_END -->\n# Chương 6: Kết Thúc\n"
        filepath = self.create_test_file("nav_block.md", content)
        self.assertEqual(get_chapter_title(filepath), "Chương 6: Kết Thúc")

if __name__ == '__main__':
    unittest.main()
