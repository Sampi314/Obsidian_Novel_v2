import os
import re

def to_proper_case(text):
    # Keep some parts like "(Mộc Linh Trận Địa)" intact if we just title case it.
    # Title casing can be tricky with Vietnamese. We will lower it first then title case,
    # but manually fix things like " (", ")", and "-".

    # We only want to convert text that is actually all-caps or mostly caps,
    # because some headers are already nicely formatted.
    # Let's just do a naive check: if more than 50% of letters are uppercase,
    # we convert it.

    letters = [c for c in text if c.isalpha()]
    if not letters:
        return text
    upper_count = sum(1 for c in letters if c.isupper())
    if upper_count / len(letters) < 0.5:
        return text

    words = text.split()
    proper_words = []
    for w in words:
        if len(w) > 0:
            proper_words.append(w.capitalize())
        else:
            proper_words.append(w)

    # For a string like "HIỆN TƯỢNG THIÊN NHIÊN: HẮC SA BÃO (黑沙暴)",
    # w.capitalize() will make "Hiện", "Tượng", "Thiên", "Nhiên:", "Hắc", "Sa", "Bão", "(黑沙暴)"
    # We need to make sure things attached to punctuation are handled okay.

    # Actually, a better approach for Vietnamese is:
    def cap_match(match):
        word = match.group(0)
        # Avoid messing with chinese characters by just capitalizing
        if len(word) > 0:
            return word[0].upper() + word[1:].lower()
        return word

    proper_text = re.sub(r'[\w\u00C0-\u1EF9]+', cap_match, text)
    return proper_text

def fix_headers_in_files():
    dirs_to_check = ['Đạo']
    updated_files = 0

    # Regex to find Markdown headers like "# BẢN ĐỒ SƠ BỘ"
    header_pattern = re.compile(r'^(#+)\s+(.+)$', re.MULTILINE)

    for d in dirs_to_check:
        for root, dirs, files in os.walk(d):
            if '.git' in root or 'scripts' in root:
                continue
            for file in files:
                if file.endswith('.md'):
                    filepath = os.path.join(root, file)
                    try:
                        with open(filepath, 'r', encoding='utf-8') as f:
                            content = f.read()

                        # Replace headers
                        def replace_header(match):
                            hashes = match.group(1)
                            title = match.group(2)
                            new_title = to_proper_case(title)
                            return f"{hashes} {new_title}"

                        new_content = header_pattern.sub(replace_header, content)

                        if content != new_content:
                            with open(filepath, 'w', encoding='utf-8') as f:
                                f.write(new_content)
                            updated_files += 1
                    except Exception as e:
                        print(f"Error reading {filepath}: {e}")

    print(f"\nUpdated headers in {updated_files} files.")

if __name__ == '__main__':
    fix_headers_in_files()
