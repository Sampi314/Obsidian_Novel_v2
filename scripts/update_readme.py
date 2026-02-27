import os
import re

def get_file_info(filepath):
    """
    Extracts relevant info from a character/technique file.
    Returns a dict with: name, type/realm, file_link
    """
    filename = os.path.basename(filepath)
    name = filename.replace(".md", "").replace("_", " ")

    info = {
        "name": name,
        "detail": "N/A",
        "filename": filename,
        "path": filepath
    }

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

            # Try to find "Cảnh Giới" or "Phẩm Cấp"
            # We look for lines starting with "- **Cảnh Giới:**" or similar

            realm_match = re.search(r'-\s*\*\*Cảnh Giới:\*\*\s*(.*)', content)
            rank_match = re.search(r'-\s*\*\*Phẩm Cấp:\*\*\s*(.*)', content)
            race_match = re.search(r'-\s*\*\*Chủng Tộc:\*\*\s*(.*)', content)
            attr_match = re.search(r'-\s*\*\*Thuộc Tính:\*\*\s*(.*)', content)

            details = []

            if race_match:
                details.append(race_match.group(1).strip().rstrip('.'))

            if realm_match:
                details.append(realm_match.group(1).strip().rstrip('.'))

            if rank_match:
                details.append(rank_match.group(1).strip().rstrip('.'))

            if attr_match:
                details.append(attr_match.group(1).strip().rstrip('.'))

            if details:
                info["detail"] = ". ".join(details) + "."

    except Exception as e:
        print(f"Error reading {filepath}: {e}")

    return info

def generate_table(directory, col1_title, col2_title):
    """
    Generates a Markdown table from files in a directory.
    """
    if not os.path.exists(directory):
        return []

    files = [f for f in os.listdir(directory) if f.endswith(".md") and f != "index.md"]
    files.sort()

    lines = []
    lines.append(f"| {col1_title} | {col2_title} | File |")
    lines.append(f"| :--- | :--- | :--- |")

    for f in files:
        filepath = os.path.join(directory, f)
        info = get_file_info(filepath)

        # Link to the file
        # Assuming README is at root, and directory is relative to root
        link = f"[Xem Chi Tiết]({directory}/{f})"

        lines.append(f"| {info['name']} | {info['detail']} | {link} |")

    return lines

def update_readme(repo_root):
    readme_path = os.path.join(repo_root, "README.md")
    if not os.path.exists(readme_path):
        print("README.md not found!")
        return

    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Define sections to update
    sections = [
        {
            "start": "<!-- CHARACTER_LIST_START -->",
            "end": "<!-- CHARACTER_LIST_END -->",
            "dir": "Đạo/Nhân_Vật",
            "col1": "Tên Nhân Vật",
            "col2": "Thông Tin (Chủng Tộc / Cảnh Giới)"
        },
        {
            "start": "<!-- TECHNIQUE_LIST_START -->",
            "end": "<!-- TECHNIQUE_LIST_END -->",
            "dir": "Đạo/Công_Pháp",
            "col1": "Tên Công Pháp",
            "col2": "Thông Tin (Phẩm Cấp / Thuộc Tính)"
        }
    ]

    new_content = content

    for section in sections:
        start_marker = section["start"]
        end_marker = section["end"]

        start_pos = new_content.find(start_marker)
        end_pos = new_content.find(end_marker)

        if start_pos != -1 and end_pos != -1:
            print(f"Updating section: {section['dir']}")
            table_lines = generate_table(section["dir"], section["col1"], section["col2"])

            # Construct replacement block
            block = f"{start_marker}\n" + "\n".join(table_lines) + "\n"

            # Replace
            new_content = new_content[:start_pos] + block + new_content[end_pos:]
        else:
            print(f"Warning: Markers {start_marker} ... {end_marker} not found.")

    if new_content != content:
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("README.md updated successfully.")
    else:
        print("No changes needed for README.md.")

if __name__ == "__main__":
    update_readme(os.getcwd())
