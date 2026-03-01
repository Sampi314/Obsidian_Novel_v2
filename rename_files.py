import os
import re

def to_proper_case_filename(filename):
    """
    Converts a filename like 'Hồ_Sơ_Thế_Giới.md' to 'Hồ_Sơ_Thế_Giới.md'.
    Keeps the extension lowercase.
    """
    name, ext = os.path.splitext(filename)

    # Check if the name contains at least one alphabetic character and is entirely uppercase
    # or mostly uppercase (we'll just apply proper case to words that are fully uppercase).
    # To be safe, let's just properly case any word in the name.

    # Split by underscore
    words = name.split('_')
    proper_words = []

    changed = False
    for word in words:
        if word.isupper() and len(word) > 0:
            changed = True

        # Capitalize the first letter, lower the rest
        if word:
            # Handle special cases like 'BẢN' -> 'Bản' correctly with Vietnamese characters
            proper_word = word.capitalize()
            # str.capitalize() works well for standard unicode, but to be sure:
            # We will use lower() then title() which handles hyphens/etc better,
            # but for our simple underscore separated words, capitalize() is usually fine.
            proper_words.append(word.capitalize())
        else:
            proper_words.append('')

    if not changed:
        return filename

    new_name = '_'.join(proper_words) + ext
    return new_name

def rename_files_in_dir(directory):
    renamed_map = {}

    # Collect all files first to avoid modifying the directory while iterating
    files_to_rename = []
    for root, dirs, files in os.walk(directory):
        if '.git' in root or 'scripts' in root:
            continue
        for file in files:
            if file.endswith('.md') or file.endswith('.html'):
                # Also apply to html if there are generated ones we track
                filepath = os.path.join(root, file)
                new_filename = to_proper_case_filename(file)
                if new_filename != file:
                    new_filepath = os.path.join(root, new_filename)
                    files_to_rename.append((filepath, new_filepath, file, new_filename))

    # Rename them using git mv
    for old_path, new_path, old_name, new_name in files_to_rename:
        print(f"Renaming: {old_path} -> {new_path}")
        # Use git mv to preserve history
        os.system(f'git mv "{old_path}" "{new_path}"')
        renamed_map[old_name] = new_name

        # also add without extension to map
        old_base = os.path.splitext(old_name)[0]
        new_base = os.path.splitext(new_name)[0]
        renamed_map[old_base] = new_base

    return renamed_map

if __name__ == '__main__':
    mapping = rename_files_in_dir('Đạo')
    mapping.update(rename_files_in_dir('.')) # For things like Mục_Lục.md -> Mục_Lục.md
    print(f"\nTotal files renamed: {len(mapping)//2}")

    # Save the mapping so we can update links later
    import json
    with open('rename_map.json', 'w', encoding='utf-8') as f:
        json.dump(mapping, f, ensure_ascii=False, indent=2)
