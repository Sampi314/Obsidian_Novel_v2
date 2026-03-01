import os
import re
import glob

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Remove YAML frontmatter wrapped in <p> tags
    content = re.sub(r'<p>---</p>\s*<p>title:\s*".*?"</p>\s*<p>---</p>\s*', '', content)

    # Un-wrap navigation div
    content = re.sub(r'<p><!-- NAVIGATION_START --></p>\s*<p><div class="navigation"></p>\s*<p>(.*?)</p>\s*<p></div></p>\s*<p><!-- NAVIGATION_END --></p>', r'<!-- NAVIGATION_START -->\n<div class="navigation">\n\1\n</div>\n<!-- NAVIGATION_END -->', content)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

for root, _, files in os.walk('Đạo HTML/Chương_Truyện/'):
    for file in files:
        if file.endswith('.html'):
            process_file(os.path.join(root, file))
