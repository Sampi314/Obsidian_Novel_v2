import os
import json

def fix_links():
    with open('rename_map.json', 'r', encoding='utf-8') as f:
        mapping = json.load(f)

    # Sort mapping by length of old name descending to avoid partial matches
    # e.g., mapping['A_B_C.md'] must be replaced before mapping['A_B.md']
    sorted_map = sorted(mapping.items(), key=lambda x: len(x[0]), reverse=True)

    files_to_check = []
    dirs_to_check = ['.', '.jules', '.jules_memory', 'Đạo']
    for d in dirs_to_check:
        for root, dirs, files in os.walk(d):
            if '.git' in root or 'scripts' in root:
                continue
            for file in files:
                if file.endswith('.md') or file.endswith('.py') or file.endswith('.html'):
                    files_to_check.append(os.path.join(root, file))

    updated_files = 0
    for filepath in files_to_check:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            new_content = content
            for old_name, new_name in sorted_map:
                # We want to replace occurrences of old_name with new_name
                # We must be careful to avoid double replacement if a name was unchanged
                if old_name != new_name and len(old_name) > 2:
                    new_content = new_content.replace(old_name, new_name)

            if content != new_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                updated_files += 1
        except Exception as e:
            print(f"Error reading {filepath}: {e}")

    print(f"\nUpdated links in {updated_files} files.")

if __name__ == '__main__':
    fix_links()
