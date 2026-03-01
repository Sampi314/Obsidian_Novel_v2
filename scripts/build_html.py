import os
import re

def markdown_to_html(md_text):
    """
    Very basic Markdown to HTML converter.
    Handles headers, bold, italic, lists, and links.
    """
    lines = md_text.split('\n')
    html_lines = []
    in_list = False

    for line in lines:
        stripped = line.strip()

        # Headers
        if stripped.startswith('# '):
            html_lines.append(f"<h1>{stripped[2:]}</h1>")
            continue
        elif stripped.startswith('## '):
            html_lines.append(f"<h2>{stripped[3:]}</h2>")
            continue
        elif stripped.startswith('### '):
            html_lines.append(f"<h3>{stripped[4:]}</h3>")
            continue

        # Lists
        if stripped.startswith('- ') or stripped.startswith('* '):
            if not in_list:
                html_lines.append("<ul>")
                in_list = True
            html_lines.append(f"<li>{stripped[2:]}</li>")
            continue
        elif in_list and not stripped:
            html_lines.append("</ul>")
            in_list = False
            continue
        elif in_list and stripped:
             html_lines.append(f"<li>{stripped}</li>")
             continue

        # Empty lines
        if not stripped:
            if in_list:
                html_lines.append("</ul>")
                in_list = False
            html_lines.append("<br>")
            continue

        # Paragraphs
        html_lines.append(f"<p>{stripped}</p>")

    if in_list:
        html_lines.append("</ul>")

    html = '\n'.join(html_lines)

    # Bold
    html = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html)

    # Italic
    html = re.sub(r'\*(.*?)\*', r'<em>\1</em>', html)

    # Links
    # Convert .md links to .html
    # First, handle explicit .md links
    html = re.sub(r'\[([^\]]+)\]\(([^)]+)\.md\)', r'<a href="\2.html">\1</a>', html)
    # Then handle other links
    html = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', html)

    # Clean up multiple <br> tags
    html = re.sub(r'(<br>\n)+', '<br>\n', html)

    return html

def get_html_header(title, level_to_root):
    # Adjust path to root based on folder depth
    # e.g. Đạo/HỒ_SƠ_THẾ_GIỚI.md -> depth 1 -> ../
    # e.g. Đạo/Nhân_Vật/Diệp_Thanh_Y.md -> depth 2 -> ../../
    root_path = "../" * level_to_root
    if level_to_root == 0:
        root_path = "./"

    return f"""<!DOCTYPE html>
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

        h2, h3 {{
            color: var(--accent-jade);
            margin-top: 50px;
            font-size: 1.8em;
            border-bottom: 1px dashed var(--border-color);
            padding-bottom: 8px;
            text-align: left;
            letter-spacing: 1px;
        }}

        h3 {{
            font-size: 1.4em;
            margin-top: 30px;
            border-bottom: none;
        }}

        p {{
            font-size: 1.1em;
            color: var(--text-light);
            text-align: justify;
            margin-bottom: 20px;
        }}

        ul {{
            list-style-type: disc;
            padding-left: 40px;
            margin-top: 20px;
            color: var(--text-light);
            font-size: 1.1em;
        }}

        li {{
            margin-bottom: 10px;
        }}

        a {{
            text-decoration: none;
            color: var(--text-gold);
            font-weight: bold;
            transition: color 0.3s ease;
        }}

        a:hover {{
            color: var(--text-gold-hover);
            text-decoration: underline;
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

        /* Table styles for character/technique lists */
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
            margin-bottom: 30px;
            color: var(--text-light);
        }}

        th, td {{
            padding: 12px 15px;
            border: 1px solid var(--border-color);
            text-align: left;
        }}

        th {{
            background-color: var(--bg-lighter);
            color: var(--text-gold);
            font-weight: bold;
        }}

        tr:nth-child(even) {{
            background-color: rgba(30, 26, 23, 0.5);
        }}

        tr:hover {{
            background-color: rgba(212, 175, 55, 0.05);
        }}
    </style>
</head>
<body>
    <a href="{root_path}index.html" class="back-link">← Quay lại Trang Chủ</a>
"""

def get_html_footer():
    return """
    <div class="footer">
        <p>Thế Giới Tiên Hiệp Cố Nguyên &copy; 2024</p>
    </div>
</body>
</html>
"""

def process_markdown_file(filepath, repo_root):
    # Calculate level_to_root for linking back
    rel_path = os.path.relpath(filepath, repo_root)
    # subtract 1 because index.html is in root
    level_to_root = rel_path.count(os.sep)

    # Read markdown
    with open(filepath, 'r', encoding='utf-8') as f:
        md_text = f.read()

    # Extract title from first line or filename
    title = os.path.basename(filepath).replace('.md', '').replace('_', ' ')
    first_line = md_text.split('\n')[0].strip()
    if first_line.startswith('# '):
        title = first_line[2:]

    # Convert content
    html_content = markdown_to_html(md_text)

    # Special handling for tables (basic)
    html_content = process_markdown_tables(html_content)

    # Remove YAML Front Matter if any
    html_content = re.sub(r'^<p>---</p>.*?<p>---</p><br>', '', html_content, flags=re.DOTALL)

    # Wrap in template
    full_html = get_html_header(title, level_to_root) + html_content + get_html_footer()

    # Save as .html
    html_filepath = filepath.replace('.md', '.html')
    with open(html_filepath, 'w', encoding='utf-8') as f:
        f.write(full_html)

def process_markdown_tables(html_text):
    """
    Very basic converter for markdown tables embedded in the parsed HTML.
    """
    lines = html_text.split('\n')
    new_lines = []
    in_table = False

    for line in lines:
        if '<p>|' in line and '|</p>' in line:
            # It's a table row
            row_content = line.replace('<p>|', '').replace('|</p>', '').strip()
            cells = [c.strip() for c in row_content.split('|')]

            # Check if it's a separator row (---)
            if all(c.replace('-', '').replace(':', '').strip() == '' for c in cells if c):
                continue

            if not in_table:
                new_lines.append('<table>')
                new_lines.append('<thead><tr>')
                for cell in cells:
                    if cell:
                        new_lines.append(f'<th>{cell}</th>')
                new_lines.append('</tr></thead>')
                new_lines.append('<tbody>')
                in_table = True
            else:
                new_lines.append('<tr>')
                for cell in cells:
                    if cell:
                        new_lines.append(f'<td>{cell}</td>')
                new_lines.append('</tr>')
        else:
            if in_table:
                new_lines.append('</tbody>')
                new_lines.append('</table>')
                in_table = False
            new_lines.append(line)

    if in_table:
        new_lines.append('</tbody>')
        new_lines.append('</table>')

    return '\n'.join(new_lines)

def convert_all_markdowns(repo_root):
    dao_dir = os.path.join(repo_root, "Đạo")
    if not os.path.exists(dao_dir):
        print("Đạo directory not found!")
        return

    for root, dirs, files in os.walk(dao_dir):
        for file in files:
            if file.endswith('.md') and file != "MỤC_LỤC.md" and file != "index.md":
                process_markdown_file(os.path.join(root, file), repo_root)

if __name__ == "__main__":
    repo_root = os.getcwd()
    convert_all_markdowns(repo_root)
    print("Done building HTML files.")
