import os
import re

# Directory containing the files
base_dir = 'Đạo/Chương_Truyện/Góc_Nhìn_Lệ_Vô_Tâm'

# Mapping of old filenames (which might be the target of a rename) to expected new headers
# But since I'm fixing *existing* files, I should just iterate the files in the directory
# and update their headers based on their filenames.

def update_chapter_headers():
    if not os.path.exists(base_dir):
        print(f"Directory {base_dir} not found.")
        return

    files = os.listdir(base_dir)
    pattern = re.compile(r'Chương_(\d+)_')

    for filename in files:
        if not filename.endswith('.md'):
            continue

        match = pattern.search(filename)
        if not match:
            continue

        chapter_num = int(match.group(1))
        filepath = os.path.join(base_dir, filename)

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Regex to find the header line. It might be # Chương X: Title or # Chương X Title
        # We want to force it to be # Chương <chapter_num>:

        # This regex matches the start of the file or a newline, followed by #, space(s), Chương, space(s), digits, optional colon
        header_regex = re.compile(r'^(#\s*Chương\s*)(\d+)(\s*:?)', re.MULTILINE)

        def replace_header(m):
            prefix = m.group(1)
            # old_num = m.group(2)
            suffix = m.group(3)
            # Ensure colon is present if it was there, or add it if standard format requires it.
            # The prompt says "update to match new filename number".
            # Let's standardize to "# Chương <num>:"
            return f"# Chương {chapter_num}:"

        new_content = header_regex.sub(replace_header, content)

        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated header in {filename} to Chương {chapter_num}")
        else:
            # Check if it already matches
            if f"# Chương {chapter_num}:" in content:
                print(f"Header in {filename} already correct.")
            else:
                print(f"Header in {filename} NOT updated (regex mismatch?).")

if __name__ == "__main__":
    update_chapter_headers()
