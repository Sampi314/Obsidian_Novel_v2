import os
import re

def get_chapter_title(filepath):
    """
    Extracts the first H1 title from a markdown file.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
            # First pass: look for # Title
            for line in lines:
                if line.startswith("# "):
                    return line.strip()[2:]

            # Second pass: look for Title\n=== or similar if using setext style (less likely but possible)
            # or maybe it's inside metadata? The file we saw has YAML frontmatter then comments then content.
            # Let's look for the first line that looks like a title after YAML frontmatter

            in_yaml = False
            for line in lines:
                stripped = line.strip()
                if stripped == "---":
                    in_yaml = not in_yaml
                    continue
                if in_yaml:
                    continue

                # Ignore comments
                if stripped.startswith("<!--") or stripped.endswith("-->"):
                    continue

                # Ignore navigation block lines (which we inject)
                if "<div" in stripped or "<table" in stripped or "<td" in stripped or "<tr" in stripped:
                    continue

                # Check for standard markdown headers
                if stripped.startswith("# "):
                    return stripped[2:]

    except Exception as e:
        print(f"Error reading {filepath}: {e}")
    return "Không có tiêu đề"

def extract_chapter_number(filename):
    """
    Extracts the chapter number from the filename for sorting.
    Handles formats like Chương_00001_... -> 1.0
    and Chương_00001_5_... -> 1.5
    """
    match = re.search(r'Chương_(\d+)(?:_(\d+))?_', filename)
    if match:
        major = int(match.group(1))
        minor = int(match.group(2)) if match.group(2) else 0
        return major + (minor / 10.0)
    return float('inf') # Put non-matching files at the end

def get_html_header(title):
    return f"""
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f4f4f9;
        }}
        h1 {{
            color: #2c3e50;
            border-bottom: 2px solid #3498db;
            padding-bottom: 10px;
        }}
        h2 {{
            color: #2980b9;
            margin-top: 30px;
        }}
        ul {{
            list-style-type: none;
            padding: 0;
        }}
        li {{
            background: #fff;
            margin: 5px 0;
            padding: 10px;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            transition: transform 0.2s;
        }}
        li:hover {{
            transform: translateX(5px);
        }}
        a {{
            text-decoration: none;
            color: #34495e;
            font-weight: 500;
            display: block;
        }}
        a:hover {{
            color: #3498db;
        }}
        .footer {{
            margin-top: 50px;
            text-align: center;
            font-size: 0.9em;
            color: #7f8c8d;
        }}
        .back-link {{
            display: inline-block;
            margin-bottom: 20px;
            color: #7f8c8d;
            font-size: 0.9em;
        }}
    </style>
</head>
<body>
"""

def get_html_footer():
    return """
    <div class="footer">
        <p>Thế Giới Tiên Hiệp Cố Nguyên &copy; 2024</p>
    </div>
</body>
</html>
"""

def generate_pov_index_html(pov_dir, pov_name):
    """
    Generates an index.html file for a specific POV directory.
    """
    index_path = os.path.join(pov_dir, "index.html")

    html_content = [get_html_header(f"Mục Lục: {pov_name}")]

    html_content.append(f'    <a href="../../../index.html" class="back-link">← Quay lại Trang Chủ</a>')
    html_content.append(f'<h1>Mục Lục: {pov_name}</h1>')
    html_content.append('<ul>')

    files = []
    for filename in os.listdir(pov_dir):
        if filename.endswith(".md") and filename != "index.md" and filename != "MỤC_LỤC.md":
            files.append(filename)

    # Sort files numerically
    files.sort(key=extract_chapter_number)

    for filename in files:
        filepath = os.path.join(pov_dir, filename)
        title = get_chapter_title(filepath)
        # Link to .html file
        html_filename = filename.replace(".md", ".html")
        html_content.append(f'    <li><a href="{html_filename}">{title}</a></li>')

    html_content.append('</ul>')
    html_content.append(get_html_footer())

    with open(index_path, "w", encoding="utf-8") as f:
        f.write("\n".join(html_content))

    print(f"Generated HTML index for {pov_name} at {index_path}")

def generate_root_index_html(repo_root):
    """
    Generates the root index.html file.
    """
    index_path = os.path.join(repo_root, "index.html")

    html_content = [get_html_header("Mục Lục Tổng Hợp - Cố Nguyên Giới")]

    html_content.append('    <h1>Mục Lục Tổng Hợp</h1>')
    html_content.append('    <p>Chào mừng đến với trang mục lục tổng hợp của thế giới Tiên Hiệp \'Cố Nguyên\'.</p>')

    html_content.append('    <h2>📖 Cốt Truyện (Story)</h2>')
    html_content.append('    <p>Các chương truyện được phân loại theo góc nhìn nhân vật:</p>')
    html_content.append('    <ul>')

    # Story Section
    story_dir = os.path.join(repo_root, "Đạo", "Chương_Truyện")
    if os.path.exists(story_dir):
        pov_dirs = [d for d in os.listdir(story_dir) if os.path.isdir(os.path.join(story_dir, d))]
        pov_dirs.sort()

        for pov_dir_name in pov_dirs:
            # Human readable name
            display_name = pov_dir_name.replace("Góc_Nhìn_", "").replace("_", " ")
            link_path = f"Đạo/Chương_Truyện/{pov_dir_name}/index.html"
            html_content.append(f'        <li><a href="{link_path}">Góc Nhìn {display_name}</a></li>')

            # Generate the POV index while we are here
            full_pov_path = os.path.join(story_dir, pov_dir_name)
            generate_pov_index_html(full_pov_path, f"Góc Nhìn {display_name}")

    html_content.append('    </ul>')

    # Wiki Section
    html_content.append('    <h2>📚 Tra Cứu (Wiki)</h2>')
    html_content.append('    <p>Thông tin chi tiết về thế giới, nhân vật và hệ thống tu luyện:</p>')
    html_content.append('    <ul>')

    wiki_links = [
        ("Hồ Sơ Thế Giới (World Profile)", "Đạo/HỒ_SƠ_THẾ_GIỚI.md"),
        ("Nhân Vật (Characters)", "Đạo/Nhân_Vật/"),
        ("Công Pháp (Techniques)", "Đạo/Công_Pháp/"),
        ("Thế Lực (Factions)", "Đạo/Thế_Lực/"),
        ("Kỳ Vật (Artifacts & Beasts)", "Đạo/Kỳ_Vật/"),
        ("Chủng Tộc (Races)", "Đạo/Chủng_Tộc/"),
        ("Đan Dược (Alchemy)", "Đạo/Đan_Dược/"),
        ("Luyện Khí (Blacksmithing)", "Đạo/Luyện_Khí/"),
        ("Trận Pháp (Formations)", "Đạo/Trận_Pháp/"),
        ("Phù Lục (Talismans)", "Đạo/Phù_Lục/"),
        ("Thế Giới & Thời Gian (World & Timeline)", "Đạo/Thế_Giới_Và_Thời_Gian/"),
        ("Văn Hóa (Culture)", "Đạo/Văn_Hóa/")
    ]

    for title, path in wiki_links:
        html_content.append(f'        <li><a href="{path}">{title}</a></li>')

    html_content.append('    </ul>')

    html_content.append(get_html_footer())

    with open(index_path, "w", encoding="utf-8") as f:
        f.write("\n".join(html_content))

    print(f"Generated root HTML index at {index_path}")

if __name__ == "__main__":
    repo_root = os.getcwd()
    generate_root_index_html(repo_root)
