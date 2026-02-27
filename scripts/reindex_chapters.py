import os
import re
from scripts.utils import extract_chapter_number

def reindex_chapters(repo_root):
    story_dir = os.path.join(repo_root, "Đạo", "Chương_Truyện")
    if not os.path.exists(story_dir):
        print(f"Directory not found: {story_dir}")
        return

    pov_dirs = [d for d in os.listdir(story_dir) if os.path.isdir(os.path.join(story_dir, d))]

    for pov in pov_dirs:
        pov_path = os.path.join(story_dir, pov)
        print(f"Processing {pov}...")
        files = []
        for filename in os.listdir(pov_path):
            if filename.endswith(".md") and filename not in ["index.md", "MỤC_LỤC.md"]:
                files.append(filename)

        # Separate numbered files from others (like templates)
        numbered_files = []
        for f in files:
            num = extract_chapter_number(f)
            if num != float('inf'):
                numbered_files.append((num, f))
            else:
                print(f"Skipping unnumbered file: {f}")

        # Sort files based on extracted chapter number
        numbered_files.sort(key=lambda x: x[0])

        if not numbered_files:
            continue

        # Rename to temporary names first to avoid collisions
        # We use a map to store the temporary name -> final name info
        temp_map = {}
        for i, (num, filename) in enumerate(numbered_files):
            temp_name = f"TEMP_REINDEX_{i}_{filename}"
            src = os.path.join(pov_path, filename)
            dst = os.path.join(pov_path, temp_name)
            try:
                os.rename(src, dst)
                temp_map[temp_name] = (i + 1, filename)
            except Exception as e:
                print(f"Error renaming {filename} to temp: {e}")

        # Rename to final names
        for temp_name, (new_index, original_filename) in temp_map.items():
            # Extract title part from original filename
            # Original: Chương_00001_Title.md or Chương_00001_5_Title.md
            match = re.search(r'Chương_\d+(?:_\d+)?_(.*)', original_filename)
            if match:
                title_part = match.group(1)
                new_filename = f"Chương_{new_index:05d}_{title_part}"
                src = os.path.join(pov_path, temp_name)
                dst = os.path.join(pov_path, new_filename)
                try:
                    os.rename(src, dst)
                    print(f"Renamed {original_filename} (Index {extract_chapter_number(original_filename)}) -> {new_filename} (Index {new_index})")
                except Exception as e:
                    print(f"Error renaming {temp_name} to {new_filename}: {e}")
            else:
                print(f"Error parsing title from {original_filename}")
                # Try to revert? Or just leave as temp?
                # This should match if extract_chapter_number matched.

if __name__ == "__main__":
    reindex_chapters(os.getcwd())
