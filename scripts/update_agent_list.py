import os
import re

JULES_DIR = ".jules/"
CHAR_DIR = "Đạo/Nhân_Vật/"
TECHNIQUE_DIR = "Đạo/Công_Pháp/"
README_FILE = "README.md"

MARKER_AGENT_START = "<!-- AGENT_LIST_START -->"
MARKER_AGENT_END = "<!-- AGENT_LIST_END -->"
MARKER_CHAR_START = "<!-- CHARACTER_LIST_START -->"
MARKER_CHAR_END = "<!-- CHARACTER_LIST_END -->"
MARKER_TECH_START = "<!-- TECHNIQUE_LIST_START -->"
MARKER_TECH_END = "<!-- TECHNIQUE_LIST_END -->"

CATEGORY_MAP = {
    "01_Kiến_Tạo_Thế_Giới.md": "Thế Giới",
    "14_Quản_Lý_Dòng_Thời_Gian.md": "Thế Giới",
    "04_Kiến_Tạo_Văn_Hóa.md": "Thế Giới",
    "02_Kiến_Tạo_Chủng_Tộc.md": "Nhân Sự",
    "03_Kiến_Tạo_Nhân_Vật.md": "Nhân Sự",
    "05_Xây_Dựng_Thế_Lực.md": "Nhân Sự",
    "06_Thiết_Kế_Hệ_Thống_Tu_Luyện.md": "Tu Luyện",
    "07_Sáng_Tạo_Công_Pháp.md": "Tu Luyện",
    "08_Viết_Sách_Công_Pháp.md": "Tu Luyện",
    "09_Đan_Dược_Sư.md": "Nghề Phụ",
    "10_Luyện_Khí_Sư.md": "Nghề Phụ",
    "11_Trận_Pháp_Sư.md": "Nghề Phụ",
    "12_Phù_Lục_Sư.md": "Nghề Phụ",
    "13_Bách_Khoa_Kỳ_Vật.md": "Tài Nguyên",
    "15_Sáng_Tác_Thơ_Ca.md": "Nghệ Thuật",
    "16_Sáng_Tác_Âm_Nhạc.md": "Nghệ Thuật",
    "20_Họa_Sĩ_Thế_Giới.md": "Nghệ Thuật",
    "17_Đạo_Diễn_Hành_Động.md": "Cốt Truyện",
    "18_Viết_Chương_Truyện.md": "Cốt Truyện",
    "19_Kiểm_Soát_Chất_Lượng.md": "QA",
}

CATEGORY_ORDER = [
    "Thế Giới",
    "Nhân Sự",
    "Tu Luyện",
    "Nghề Phụ",
    "Tài Nguyên",
    "Nghệ Thuật",
    "Cốt Truyện",
    "QA"
]

def read_file_content(filepath):
    if not os.path.exists(filepath):
        return ""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def extract_agent_info(filepath):
    filename = os.path.basename(filepath)
    content = read_file_content(filepath)

    skill_match = re.search(r'^# SKILL:\s*(.+)$', content, re.MULTILINE)
    skill_name = skill_match.group(1).strip() if skill_match else filename.replace(".md", "").replace("_", " ")

    role_match = re.search(r'## VAI TRÒ\s*(.*?)\n##', content, re.DOTALL)
    role_desc = ""
    if role_match:
        role_text = role_match.group(1).strip()
        role_desc = role_text.split('\n')[0]

    return {
        "filename": filename,
        "name": skill_name,
        "desc": role_desc,
        "category": CATEGORY_MAP.get(filename, "Khác")
    }

def extract_character_info(filepath):
    filename = os.path.basename(filepath)
    content = read_file_content(filepath)

    # Try multiple patterns for Name
    name_match = re.search(r'-\s*\*\*Tên Nhân Vật:\*\*\s*(.+)', content)
    name = name_match.group(1).strip() if name_match else filename.replace(".md", "").replace("_", " ")

    # Race
    race_match = re.search(r'-\s*\*\*Chủng Tộc:\*\*\s*(.+)', content)
    race = race_match.group(1).strip() if race_match else "N/A"

    # Realm (Cultivation Level)
    realm_match = re.search(r'-\s*\*\*Cảnh Giới:\*\*\s*(.+)', content)
    realm = realm_match.group(1).strip() if realm_match else "N/A"

    return {
        "filename": filename,
        "name": name,
        "race": race,
        "realm": realm
    }

def extract_technique_info(filepath):
    filename = os.path.basename(filepath)
    content = read_file_content(filepath)

    # Name from first header
    name_match = re.search(r'^#\s*(.+)', content)
    name = name_match.group(1).strip() if name_match else filename.replace(".md", "").replace("_", " ")

    # Rank
    rank_match = re.search(r'-\s*\*\*Phẩm Cấp:\*\*\s*(.+)', content)
    rank = rank_match.group(1).strip() if rank_match else "N/A"

    # Element
    element_match = re.search(r'-\s*\*\*Thuộc Tính:\*\*\s*(.+)', content)
    element = element_match.group(1).strip() if element_match else "N/A"

    return {
        "filename": filename,
        "name": name,
        "rank": rank,
        "element": element
    }

def generate_agent_table():
    agents = []
    if os.path.exists(JULES_DIR):
        for filename in os.listdir(JULES_DIR):
            # Check for the renamed instructions file (or old one if it existed)
            if filename.endswith(".md") and filename not in ["INSTRUCTIONS.md", "00_INSTRUCTIONS.md"]:
                filepath = os.path.join(JULES_DIR, filename)
                agents.append(extract_agent_info(filepath))

    agents.sort(key=lambda x: (CATEGORY_ORDER.index(x['category']) if x['category'] in CATEGORY_ORDER else 99, x['name']))

    table_lines = [
        "| Lĩnh Vực | Agent / Tài Liệu Hướng Dẫn | Mô Tả Nhiệm Vụ |",
        "| :--- | :--- | :--- |"
    ]
    current_category = ""
    for agent in agents:
        category_cell = f"**{agent['category']}**" if agent['category'] != current_category else ""
        current_category = agent['category']
        link = f"[{agent['name']}]({JULES_DIR}{agent['filename']})"
        desc = agent['desc'].replace("\n", " ").strip()
        table_lines.append(f"| {category_cell} | {link} | {desc} |")

    return "\n".join(table_lines)

def generate_character_table():
    chars = []
    if os.path.exists(CHAR_DIR):
        for filename in os.listdir(CHAR_DIR):
            if filename.endswith(".md"):
                filepath = os.path.join(CHAR_DIR, filename)
                chars.append(extract_character_info(filepath))

    chars.sort(key=lambda x: x['name'])

    table_lines = [
        "| Tên Nhân Vật | Chủng Tộc | Cảnh Giới | File |",
        "| :--- | :--- | :--- | :--- |"
    ]
    for char in chars:
        link = f"[Xem Chi Tiết]({CHAR_DIR}{char['filename']})"
        table_lines.append(f"| {char['name']} | {char['race']} | {char['realm']} | {link} |")

    return "\n".join(table_lines)

def generate_technique_table():
    techs = []
    if os.path.exists(TECHNIQUE_DIR):
        for filename in os.listdir(TECHNIQUE_DIR):
            if filename.endswith(".md"):
                filepath = os.path.join(TECHNIQUE_DIR, filename)
                techs.append(extract_technique_info(filepath))

    techs.sort(key=lambda x: x['name'])

    table_lines = [
        "| Tên Công Pháp | Phẩm Cấp | Thuộc Tính | File |",
        "| :--- | :--- | :--- | :--- |"
    ]
    for tech in techs:
        link = f"[Xem Chi Tiết]({TECHNIQUE_DIR}{tech['filename']})"
        table_lines.append(f"| {tech['name']} | {tech['rank']} | {tech['element']} | {link} |")

    return "\n".join(table_lines)

def replace_section(content, marker_start, marker_end, new_text):
    pattern = re.compile(f"{re.escape(marker_start)}.*?{re.escape(marker_end)}", re.DOTALL)
    if pattern.search(content):
        return pattern.sub(f"{marker_start}\n{new_text}\n{marker_end}", content)
    return content

def update_readme():
    if not os.path.exists(README_FILE):
        print(f"Error: {README_FILE} not found.")
        return

    with open(README_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update Agent List
    print("Updating Agent List...")
    agent_table = generate_agent_table()
    content = replace_section(content, MARKER_AGENT_START, MARKER_AGENT_END, agent_table)

    # Update Character List
    print("Updating Character List...")
    char_table = generate_character_table()
    content = replace_section(content, MARKER_CHAR_START, MARKER_CHAR_END, char_table)

    # Update Technique List
    print("Updating Technique List...")
    tech_table = generate_technique_table()
    content = replace_section(content, MARKER_TECH_START, MARKER_TECH_END, tech_table)

    with open(README_FILE, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Successfully updated {README_FILE}")

if __name__ == "__main__":
    update_readme()
