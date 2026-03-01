import os
import re
from scripts.utils import get_chapter_title, extract_chapter_number

def get_html_header(title):
    return f"""
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        :root {{
            --bg-dark: #12100e;
            --bg-lighter: #1e1a17;
            --text-gold: #d4af37;
            --text-gold-hover: #f1c40f;
            --text-light: #e0d8c8;
            --text-muted: #9e917d;
            --accent-red: #8b0000;
            --accent-jade: #00a86b;
            --border-color: #4a3c31;
        }}

        body {{
            font-family: "Georgia", "Times New Roman", Times, serif;
            line-height: 1.8;
            color: var(--text-light);
            max-width: 900px;
            margin: 0 auto;
            padding: 40px 20px;
            background-color: var(--bg-dark);
            background-image: radial-gradient(circle at center, #1a1614 0%, #12100e 100%);
            border-left: 2px solid var(--border-color);
            border-right: 2px solid var(--border-color);
            min-height: 100vh;
        }}

        h1 {{
            color: var(--text-gold);
            text-align: center;
            font-size: 2.5em;
            margin-bottom: 20px;
            text-transform: uppercase;
            letter-spacing: 2px;
            border-bottom: 2px solid var(--accent-red);
            padding-bottom: 15px;
            text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.8);
            position: relative;
        }}

        h1::after {{
            content: "☯";
            display: block;
            font-size: 0.8em;
            color: var(--text-muted);
            margin-top: 10px;
            text-align: center;
            text-shadow: none;
        }}

        h2 {{
            color: var(--accent-jade);
            margin-top: 50px;
            font-size: 1.8em;
            border-bottom: 1px dashed var(--border-color);
            padding-bottom: 8px;
            text-align: center;
            letter-spacing: 1px;
        }}

        p {{
            font-size: 1.1em;
            color: var(--text-muted);
            text-align: center;
            font-style: italic;
            margin-bottom: 30px;
        }}

        ul {{
            list-style-type: none;
            padding: 0;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }}

        li {{
            background: var(--bg-lighter);
            padding: 15px 20px;
            border-radius: 4px;
            border: 1px solid var(--border-color);
            box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.5), 0 2px 4px rgba(0, 0, 0, 0.3);
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
            display: flex;
            align-items: center;
        }}

        li::before {{
            content: '';
            position: absolute;
            top: 0; left: 0;
            width: 4px; height: 100%;
            background-color: var(--accent-red);
            opacity: 0.7;
            transition: all 0.3s ease;
        }}

        li:hover {{
            transform: translateY(-3px);
            border-color: var(--text-gold);
            box-shadow: inset 0 0 15px rgba(212, 175, 55, 0.1), 0 4px 8px rgba(0, 0, 0, 0.5);
        }}

        li:hover::before {{
            width: 6px;
            opacity: 1;
        }}

        a {{
            text-decoration: none;
            color: var(--text-light);
            font-weight: bold;
            display: block;
            width: 100%;
            font-size: 1.1em;
            transition: color 0.3s ease;
            padding-left: 10px;
        }}

        a:hover {{
            color: var(--text-gold-hover);
        }}

        .footer {{
            margin-top: 80px;
            text-align: center;
            font-size: 0.9em;
            color: var(--text-muted);
            border-top: 1px solid var(--border-color);
            padding-top: 20px;
        }}

        .back-link {{
            display: inline-block;
            margin-bottom: 30px;
            color: var(--text-muted);
            font-size: 1em;
            border: 1px solid var(--border-color);
            padding: 8px 15px;
            border-radius: 3px;
            transition: all 0.3s ease;
            text-align: center;
            text-decoration: none;
        }}

        .back-link:hover {{
            color: var(--text-gold);
            border-color: var(--text-gold);
            background: rgba(212, 175, 55, 0.05);
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

    # Quy Hoạch Cốt Truyện Section
    html_content.append('    <h2>🗺️ Quy Hoạch Cốt Truyện (Story Arcs)</h2>')
    html_content.append('    <p>Các tuyến truyện chính trên toàn Cố Nguyên Giới:</p>')
    html_content.append('    <ul>')

    arcs_links = [
        ("Tuyến Truyện Nam Cương", "Đạo/Quy_Hoạch_Cốt_Truyện/Nam_Cương/Tuyến_Truyện_Nam_Cương.md", [
            ("Diệp Tĩnh Sương Chi Tiết", "Đạo/Quy_Hoạch_Cốt_Truyện/Nam_Cương/Diệp_Tĩnh_Sương_Chi_Tiết.md"),
            ("Lâm Phong", "Đạo/Quy_Hoạch_Cốt_Truyện/Nam_Cương/Lâm_Phong.md"),
            ("Lệ Vô Tâm Chi Tiết", "Đạo/Quy_Hoạch_Cốt_Truyện/Nam_Cương/Lệ_Vô_Tâm_Chi_Tiết.md"),
        ]),
        ("Tuyến Truyện Bắc Hàn", "Đạo/Quy_Hoạch_Cốt_Truyện/Bắc_Hàn/Tuyến_Truyện_Bắc_Hàn.md", []),
        ("Tuyến Truyện Đông Hoang", "Đạo/Quy_Hoạch_Cốt_Truyện/Đông_Hoang/Tuyến_Truyện_Đông_Hoang.md", []),
        ("Tuyến Truyện Thiên Trụ", "Đạo/Quy_Hoạch_Cốt_Truyện/Thiên_Trụ/Tuyến_Truyện_Thiên_Trụ.md", []),
        ("Tuyến Truyện Tây Mạc", "Đạo/Quy_Hoạch_Cốt_Truyện/Tây_Mạc/Tuyến_Truyện_Tây_Mạc.md", []),
        ("Quản Lý Arc Truyện", "Đạo/Quy_Hoạch_Cốt_Truyện/QUẢN_LÝ_ARC_TRUYỆN.md", [])
    ]

    for title, path, sub_links in arcs_links:
        html_content.append(f'        <li><a href="{path}">{title}</a>')
        if sub_links:
            html_content.append('            <ul>')
            for sub_title, sub_path in sub_links:
                html_content.append(f'                <li><a href="{sub_path}">{sub_title}</a></li>')
            html_content.append('            </ul>')
        html_content.append('        </li>')

    html_content.append('    </ul>')

    # Wiki Section
    html_content.append('    <h2>📚 Tra Cứu (Wiki)</h2>')
    html_content.append('    <p>Thông tin chi tiết về thế giới, nhân vật và hệ thống tu luyện:</p>')
    html_content.append('    <ul>')

    wiki_links = [
        ("Hồ Sơ Thế Giới (World Profile)", "Đạo/HỒ_SƠ_THẾ_GIỚI.html"),
        ("Nhân Vật (Characters)", "Đạo/Nhân_Vật/index.html"),
        ("Công Pháp (Techniques)", "Đạo/Công_Pháp/index.html"),
        ("Thế Lực (Factions)", "Đạo/Thế_Lực/index.html"),
        ("Kỳ Vật (Artifacts & Beasts)", "Đạo/Kỳ_Vật/index.html"),
        ("Chủng Tộc (Races)", "Đạo/Chủng_Tộc/index.html"),
        ("Đan Dược (Alchemy)", "Đạo/Đan_Dược/index.html"),
        ("Luyện Khí (Blacksmithing)", "Đạo/Luyện_Khí/index.html"),
        ("Trận Pháp (Formations)", "Đạo/Trận_Pháp/index.html"),
        ("Phù Lục (Talismans)", "Đạo/Phù_Lục/index.html"),
        ("Thế Giới & Thời Gian (World & Timeline)", "Đạo/Thế_Giới_Và_Thời_Gian/index.html"),
        ("Văn Hóa (Culture)", "Đạo/Văn_Hóa/index.html")
    ]

    for title, path in wiki_links:
        html_content.append(f'        <li><a href="{path}">{title}</a></li>')

        # Tạo index cho thư mục con (bỏ HỒ SƠ THẾ GIỚI ra vì là file md)
        if path.endswith("/index.html"):
            category_rel_dir = path.replace("/index.html", "")
            category_full_dir = os.path.join(repo_root, category_rel_dir)
            if os.path.exists(category_full_dir):
                # category_name từ title "Nhân Vật (Characters)"
                category_name = title.split("(")[0].strip()
                generate_wiki_category_index_html(category_full_dir, category_name, repo_root)

    html_content.append('    </ul>')

    html_content.append(get_html_footer())

    with open(index_path, "w", encoding="utf-8") as f:
        f.write("\n".join(html_content))

    print(f"Generated root HTML index at {index_path}")

def generate_wiki_category_index_html(category_dir, category_name, repo_root):
    """
    Generates an index.html file for a specific Wiki category directory (like Nhân_Vật).
    """
    index_path = os.path.join(category_dir, "index.html")
    rel_path = os.path.relpath(category_dir, repo_root)
    level_to_root = rel_path.count(os.sep)
    root_path = "../" * level_to_root

    html_content = [get_html_header(f"{category_name}")]

    html_content.append(f'    <a href="{root_path}index.html" class="back-link">← Quay lại Trang Chủ</a>')
    html_content.append(f'<h1>{category_name}</h1>')
    html_content.append('<ul>')

    files = []
    for filename in os.listdir(category_dir):
        if filename.endswith(".md") and filename != "index.md":
            files.append(filename)

    # Sort files alphabetically
    files.sort()

    for filename in files:
        filepath = os.path.join(category_dir, filename)
        title = get_chapter_title(filepath)
        # Link to .html file
        html_filename = filename.replace(".md", ".html")
        html_content.append(f'    <li><a href="{html_filename}">{title}</a></li>')

    html_content.append('</ul>')
    html_content.append(get_html_footer())

    with open(index_path, "w", encoding="utf-8") as f:
        f.write("\n".join(html_content))

    print(f"Generated HTML index for {category_name} at {index_path}")

if __name__ == "__main__":
    repo_root = os.getcwd()
    generate_root_index_html(repo_root)
