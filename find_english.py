import os
import re

def is_english_word(word):
    # This is a basic check. We are looking for typical English technical terms often found in markdown files
    english_terms = [
        "Agent", "Skill", "Level", "System", "Name", "Memory", "Background",
        "Story", "Character", "Chapter", "World", "Building", "Timeline",
        "Action", "Director", "Quality", "Control", "Review", "Plot", "Hole",
        "Bug", "Profile", "File", "Folder", "Path", "Title", "Heading",
        "Content", "Description", "Role", "Task", "Process", "Structure",
        "Format", "Output", "Note", "Detail", "Summary", "Report", "Update",
        "Create", "Edit", "Delete", "Add", "Remove", "Fix", "Check", "Test"
    ]
    word_lower = word.lower()
    for term in english_terms:
        if term.lower() == word_lower:
            return True
    return False

def check_file(filepath):
    found = False
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            words = re.findall(r'\b[A-Za-z]+\b', content)
            for word in words:
                if is_english_word(word):
                    print(f"File: {filepath} contains English term: {word}")
                    found = True
                    break # Just log the file once for now
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
    return found

def main():
    dirs_to_check = ['.', '.jules', '.jules_memory', 'Đạo']
    files_with_english = []

    for d in dirs_to_check:
        for root, _, files in os.walk(d):
            if '.git' in root or 'scripts' in root:
                continue
            for file in files:
                if file.endswith('.md'):
                    filepath = os.path.join(root, file)
                    if check_file(filepath):
                        files_with_english.append(filepath)

    print(f"\nTotal files with potential English: {len(files_with_english)}")

if __name__ == '__main__':
    main()
