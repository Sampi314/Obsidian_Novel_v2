import json
import re

with open('scripts/chapter_data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# The script update_chapter_data.py likely recreated the file based on the filesystem,
# so Chương_Mẫu_Huyền_Băng.md might have been ignored if it doesn't match the regex.
# Let's check if the file contains the sample chapter.
if 'Chương_Mẫu_Huyền_Băng' not in content:
    print("Sample chapter missing. The generator script might have skipped it because it doesn't match the regex.")
else:
    print("Sample chapter is present.")
