import os
import re
from scripts.utils import extract_chapter_index

def update_headers(repo_root):
    story_dir = os.path.join(repo_root, "Đạo", "Chương_Truyện")
    if not os.path.exists(story_dir):
        print(f"Directory not found: {story_dir}")
        return

    pov_dirs = [d for d in os.listdir(story_dir) if os.path.isdir(os.path.join(story_dir, d))]

    # Pattern matches: Start of line, # Chương, space, number/dots, colon, space, rest of line
    header_pattern = re.compile(r'^(# Chương )[\d\.]+(: .*)$', re.MULTILINE)

    for pov in pov_dirs:
        pov_path = os.path.join(story_dir, pov)
        print(f"Processing {pov}...")
        for filename in os.listdir(pov_path):
            if filename.endswith(".md") and filename not in ["index.md", "MỤC_LỤC.md"]:
                index = extract_chapter_index(filename)
                if index is None:
                    continue

                filepath = os.path.join(pov_path, filename)
                try:
                    with open(filepath, "r", encoding="utf-8") as f:
                        content = f.read()

                    # Use \g<1> to explicitly refer to group 1, avoiding ambiguity with the following number
                    new_content = header_pattern.sub(f'\\g<1>{index}\\g<2>', content)

                    if new_content != content:
                        with open(filepath, "w", encoding="utf-8") as f:
                            f.write(new_content)
                        print(f"Updated header in {filename} to Chapter {index}")
                    else:
                         # It might have failed silently or didn't match?
                         # Or it was already correct.
                         pass
                except Exception as e:
                    print(f"Error updating {filename}: {e}")

if __name__ == "__main__":
    update_headers(os.getcwd())
