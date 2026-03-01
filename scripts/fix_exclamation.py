import os
import re

def fix_exclamation(directory):
    pattern = re.compile(r'!{2,}')
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                filepath = os.path.join(root, file)
                if "BÁO_CÁO_CHẤT_LƯỢNG.md" in file:
                    continue
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                new_content = pattern.sub('!', content)
                if content != new_content:
                    print(f"Fixed {filepath}")
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(new_content)

if __name__ == "__main__":
    fix_exclamation("Đạo/")
