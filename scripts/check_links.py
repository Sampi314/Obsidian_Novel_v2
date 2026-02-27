import os
import re
import sys

def check_links(index_file="Đạo/HỒ_SƠ_THẾ_GIỚI.md"):
    repo_root = os.getcwd()
    file_path = os.path.join(repo_root, index_file)
    base_dir = os.path.dirname(file_path)

    if not os.path.exists(file_path):
        print(f"Error: Index file {index_file} not found at {file_path}")
        return False

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Regex to find links like [Text](Path) or `Path`
    md_links = re.findall(r'\[.*?\]\((.*?)\)', content)
    code_paths = re.findall(r'`(Đạo/.*?)`', content) # Only check `Đạo/...` inside backticks

    all_paths = md_links + code_paths
    missing_files = []
    checked_count = 0

    print(f"Checking links in {index_file}...")

    for path in all_paths:
        path = path.strip()
        # Clean up path if it has query params or anchors
        if '#' in path:
            path = path.split('#')[0]

        if not path:
            continue

        if path.startswith("http") or path.startswith("https"):
            continue

        if path.startswith("mailto:"):
            continue

        # Determine full path
        if path.startswith("Đạo/"):
            # Path relative to repo root
            full_path = os.path.join(repo_root, path)
        elif path.startswith("/"):
             # If it starts with /, assume it's relative to repo root (GitHub style)
            # Remove leading slash
            full_path = os.path.join(repo_root, path.lstrip("/"))
        else:
            # Relative path to the file location
            full_path = os.path.join(base_dir, path)

        checked_count += 1
        if not os.path.exists(full_path):
            missing_files.append(path)

    if missing_files:
        print(f"\n❌ Found {len(missing_files)} broken links:")
        for p in missing_files:
            print(f"  - {p}")
        return False
    else:
        print(f"\n✅ All {checked_count} links are valid.")
        return True

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target_file = sys.argv[1]
        success = check_links(target_file)
    else:
        success = check_links()

    if not success:
        sys.exit(1)
