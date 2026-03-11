import os
import re

def fix_html_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove YAML frontmatter
    content = re.sub(r'<p>---</p>\n<p>title: ".*?"</p>\n<p>---</p>\n', '', content)

    # Fix navigation div being wrapped in <p>
    content = re.sub(r'<p><!-- NAVIGATION_START --></p>\n<p><div class="navigation"></p>\n<p>\[< (.*?)\]\((.*?)\) \| \[Mục Lục\]\((.*?)\) \| (.*?) ></p>\n<p></div></p>\n<p><!-- NAVIGATION_END --></p>', r'<!-- NAVIGATION_START -->\n<div class="navigation">\n[< \1](\2) | [Mục Lục](\3) | \4 >\n</div>\n<!-- NAVIGATION_END -->', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

fix_html_file('Đạo HTML/Chương_Truyện/Góc_Nhìn_Chính/Chương_00097_Khắc_Phục_Hậu_Quả.html')
fix_html_file('Đạo HTML/Chương_Truyện/Góc_Nhìn_Lệ_Vô_Tâm/Chương_00091_Báo_Cáo_Thất_Bại.html')
