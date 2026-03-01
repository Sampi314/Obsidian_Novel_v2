import re
import os

with open('Đạo/Hồ_Sơ_Thế_Giới.md', 'r') as f:
    content = f.read()

links = re.findall(r'\]\(([^)]+)\)', content)
missing = []
for link in links:
    if link.startswith('http'): continue
    path = os.path.join('Đạo', link)
    if not os.path.exists(path):
        missing.append(link)

print("Missing links in Hồ_Sơ_Thế_Giới.md:")
for m in set(missing):
    print(m)
