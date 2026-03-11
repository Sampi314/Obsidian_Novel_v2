import os
import re

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Remove YAML frontmatter wrapped in <p> tags
    content = re.sub(r'<p>---</p>\s*<p>title:\s*".*?"</p>\s*<p>---</p>\s*', '', content)

    # Clean up navigation wrapper
    content = content.replace('<p><!-- NAVIGATION_START --></p>', '<!-- NAVIGATION_START -->')
    content = content.replace('<p><div id="chapter-navigation" style="text-align: center; margin-bottom: 20px;"></div></p>', '<div id="chapter-navigation" style="text-align: center; margin-bottom: 20px;"></div>')
    content = content.replace('<p><script src="../../../scripts/chapter_data.js"></script></p>', '<script src="../../../scripts/chapter_data.js"></script>')
    content = content.replace('<p><script src="../../../scripts/navigation.js"></script></p>', '<script src="../../../scripts/navigation.js"></script>')
    content = content.replace('<p><script src="../../../scripts/tts_player.js"></script></p>', '<script src="../../../scripts/tts_player.js"></script>')
    content = content.replace('<p><!-- NAVIGATION_END --></p>', '<!-- NAVIGATION_END -->')

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

for root, _, files in os.walk('Đạo HTML/Chương_Truyện/'):
    for file in files:
        if file.endswith('.html'):
            process_file(os.path.join(root, file))
