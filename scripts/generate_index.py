import os

# Define a simple HTML template
HTML_TEMPLATE = """
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
    {content}
    <div class="footer">
        <p>Thế Giới Tiên Hiệp Cố Nguyên &copy; 2024</p>
    </div>
</body>
</html>
"""

def get_chapter_title(filepath):
    """
    Extracts the first H1 title from a markdown file.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith("# "):
                    return line.strip()[2:]
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
    return "Không có tiêu đề"

def generate_pov_index(pov_dir, pov_name, repo_root):
    """
    Generates an index.html file for a specific POV directory.
    """
    index_path = os.path.join(pov_dir, "index.html")

    # Calculate relative path to root for the back link
    rel_path_to_root = os.path.relpath(repo_root, pov_dir)
    back_link = f'<a href="{rel_path_to_root}/index.html" class="back-link">← Quay lại Trang Chủ</a>'

    body_content = f"{back_link}\n<h1>Mục Lục: {pov_name}</h1>\n<ul>\n"

    files = []
    for filename in os.listdir(pov_dir):
        if filename.endswith(".md") and filename != "index.md" and filename != "MỤC_LỤC.md":
            files.append(filename)

    files.sort()

    for filename in files:
        filepath = os.path.join(pov_dir, filename)
        title = get_chapter_title(filepath)
        # Link directly to the markdown file
        body_content += f'    <li><a href="{filename}">{title}</a></li>\n'

    body_content += "</ul>"

    full_html = HTML_TEMPLATE.format(title=f"Mục Lục: {pov_name}", content=body_content)

    with open(index_path, "w", encoding="utf-8") as f:
        f.write(full_html)

    print(f"Generated HTML index for {pov_name} at {index_path}")

def generate_root_index(repo_root):
    """
    Generates the root index.html file.
    """
    index_path = os.path.join(repo_root, "index.html")

    body_content = """
    <h1>Mục Lục Tổng Hợp</h1>
    <p>Chào mừng đến với trang mục lục tổng hợp của thế giới Tiên Hiệp 'Cố Nguyên'.</p>

    <h2>📖 Cốt Truyện (Story)</h2>
    <p>Các chương truyện được phân loại theo góc nhìn nhân vật:</p>
    <ul>
    """

    # Story Section
    story_dir = os.path.join(repo_root, "Đạo", "Chương_Truyện")
    if os.path.exists(story_dir):
        pov_dirs = [d for d in os.listdir(story_dir) if os.path.isdir(os.path.join(story_dir, d))]
        pov_dirs.sort()

        for pov_dir_name in pov_dirs:
            # Human readable name
            display_name = pov_dir_name.replace("Góc_Nhìn_", "").replace("_", " ")
            link_path = f"Đạo/Chương_Truyện/{pov_dir_name}/index.html"
            body_content += f'        <li><a href="{link_path}">Góc Nhìn {display_name}</a></li>\n'

            # Generate the POV index while we are here
            full_pov_path = os.path.join(story_dir, pov_dir_name)
            generate_pov_index(full_pov_path, f"Góc Nhìn {display_name}", repo_root)

    body_content += """
    </ul>

    <h2>📚 Tra Cứu (Wiki)</h2>
    <p>Thông tin chi tiết về thế giới, nhân vật và hệ thống tu luyện:</p>
    <ul>
        <li><a href="Đạo/HỒ_SƠ_THẾ_GIỚI.md">Hồ Sơ Thế Giới (World Profile)</a></li>
        <li><a href="Đạo/Nhân_Vật/">Nhân Vật (Characters)</a></li>
        <li><a href="Đạo/Công_Pháp/">Công Pháp (Techniques)</a></li>
        <li><a href="Đạo/Thế_Lực/">Thế Lực (Factions)</a></li>
        <li><a href="Đạo/Kỳ_Vật/">Kỳ Vật (Artifacts & Beasts)</a></li>
        <li><a href="Đạo/Chủng_Tộc/">Chủng Tộc (Races)</a></li>
        <li><a href="Đạo/Đan_Dược/">Đan Dược (Alchemy)</a></li>
        <li><a href="Đạo/Luyện_Khí/">Luyện Khí (Blacksmithing)</a></li>
        <li><a href="Đạo/Trận_Pháp/">Trận Pháp (Formations)</a></li>
        <li><a href="Đạo/Phù_Lục/">Phù Lục (Talismans)</a></li>
        <li><a href="Đạo/Thế_Giới_Và_Thời_Gian/">Thế Giới & Thời Gian (World & Timeline)</a></li>
        <li><a href="Đạo/Văn_Hóa/">Văn Hóa (Culture)</a></li>
    </ul>
    """

    full_html = HTML_TEMPLATE.format(title="Mục Lục Tổng Hợp - Cố Nguyên Giới", content=body_content)

    with open(index_path, "w", encoding="utf-8") as f:
        f.write(full_html)

    print(f"Generated root HTML index at {index_path}")

if __name__ == "__main__":
    repo_root = os.getcwd()
    generate_root_index(repo_root)
