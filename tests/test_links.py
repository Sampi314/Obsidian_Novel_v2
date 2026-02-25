import os
import re
import pytest

def test_ho_so_the_gioi_links():
    """
    Parses Đạo/HỒ_SƠ_THẾ_GIỚI.md and checks if all local links (starting with `Đạo/`) exist.
    """
    # Get the repo root based on this test file's location
    # tests/test_links.py -> repo_root/tests/test_links.py
    current_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(current_dir)

    index_file = os.path.join(repo_root, "Đạo", "HỒ_SƠ_THẾ_GIỚI.md")
    assert os.path.exists(index_file), f"{index_file} does not exist!"

    with open(index_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Regex to find links like [Text](Path) or `Path`
    # Focusing on the specific format used in the file: `Đạo/...`
    # The file uses `...` for paths.

    # Pattern for markdown links [text](path)
    md_links = re.findall(r'\[.*?\]\((.*?)\)', content)

    # Pattern for inline code paths `path`
    code_paths = re.findall(r'`(.*?)`', content)

    all_paths = md_links + code_paths

    missing_files = []

    for path in all_paths:
        # Filter for local paths starting with Đạo/ or relative paths
        if path.startswith("Đạo/"):
            # The path is relative to the repo root
            full_path = os.path.join(repo_root, path)
            if not os.path.exists(full_path):
                missing_files.append(path)
        elif path.startswith("http"):
            continue

    assert not missing_files, f"Found broken links in {index_file}: {missing_files}"
