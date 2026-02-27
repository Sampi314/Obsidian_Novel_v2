import os
import re

def get_html_header(title):
    return f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        :root {{
            --primary-color: #3498db;
            --secondary-color: #2c3e50;
            --bg-color: #f4f4f9;
            --card-bg: #ffffff;
            --text-color: #333333;
            --border-color: #e0e0e0;
        }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            line-height: 1.6;
            color: var(--text-color);
            background-color: var(--bg-color);
            margin: 0;
            padding: 20px;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
        }}
        h1 {{
            color: var(--secondary-color);
            text-align: center;
            border-bottom: 2px solid var(--primary-color);
            padding-bottom: 10px;
            margin-bottom: 30px;
        }}
        h2 {{
            color: var(--primary-color);
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 5px;
            margin-top: 40px;
        }}
        .back-link {{
            display: inline-block;
            margin-bottom: 20px;
            color: #7f8c8d;
            text-decoration: none;
            font-weight: 500;
        }}
        .back-link:hover {{
            color: var(--primary-color);
        }}
        .arcs-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-bottom: 40px;
        }}
        .arc-card {{
            background: var(--card-bg);
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            padding: 20px;
            border-left: 5px solid var(--primary-color);
            transition: transform 0.2s;
        }}
        .arc-card:hover {{
            transform: translateY(-5px);
        }}
        .arc-title {{
            font-size: 1.2em;
            font-weight: bold;
            color: var(--secondary-color);
            margin-bottom: 10px;
        }}
        .arc-meta {{
            font-size: 0.9em;
            color: #555;
            margin-bottom: 15px;
        }}
        .arc-meta strong {{
            color: var(--secondary-color);
        }}
        .arc-tasks {{
            margin: 0;
            padding-left: 20px;
            font-size: 0.95em;
        }}
        .arc-tasks li {{
            margin-bottom: 8px;
        }}
        .completed {{
            color: #27ae60;
            text-decoration: line-through;
            opacity: 0.8;
        }}
        .in-progress {{
            color: #e67e22;
            font-weight: 500;
        }}
        .future {{
            color: #2980b9;
        }}
        .table-wrapper {{
            overflow-x: auto;
            background: var(--card-bg);
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            padding: 20px;
            margin-top: 20px;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
        }}
        th, td {{
            padding: 12px 15px;
            text-align: left;
            border-bottom: 1px solid var(--border-color);
        }}
        th {{
            background-color: var(--bg-color);
            color: var(--secondary-color);
            font-weight: 600;
        }}
        tr:hover {{
            background-color: var(--bg-color);
        }}
        .footer {{
            margin-top: 50px;
            text-align: center;
            font-size: 0.9em;
            color: #7f8c8d;
        }}
    </style>
</head>
<body>
    <div class="container">
        <a href="index.html" class="back-link">← Quay lại Trang Chủ</a>
        <h1>Tuyến Truyện & Kế Hoạch (Story Planner)</h1>
"""

def get_html_footer():
    return """
        <div class="footer">
            <p>Thế Giới Tiên Hiệp Cố Nguyên &copy; 2024</p>
        </div>
    </div>
</body>
</html>
"""

def parse_markdown_file(filepath):
    if not os.path.exists(filepath):
        return [], [], []

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract Current Arcs
    current_arcs = []
    current_arcs_section = re.search(r'## ARC HIỆN TẠI\n(.*?)(?=\n## |\Z)', content, re.DOTALL)
    if current_arcs_section:
        arcs_text = current_arcs_section.group(1)
        arc_blocks = re.split(r'\n### \d+\. ', arcs_text)

        for block in arc_blocks:
            if not block.strip(): continue

            lines = block.strip().split('\n')
            title = lines[0].strip()

            arc_data = {
                'title': title,
                'status': '',
                'arc_name': '',
                'main_char': '',
                'sub_char': '',
                'tasks': []
            }

            in_tasks = False
            for line in lines[1:]:
                line = line.strip()
                if line.startswith('*   **Trạng Thái:**'):
                    arc_data['status'] = line.replace('*   **Trạng Thái:**', '').strip()
                elif line.startswith('*   **Tên Arc:**'):
                    arc_data['arc_name'] = line.replace('*   **Tên Arc:**', '').strip()
                elif line.startswith('*   **Nhân Vật Chính:**'):
                    arc_data['main_char'] = line.replace('*   **Nhân Vật Chính:**', '').strip()
                elif line.startswith('*   **Nhân Vật Phụ:**'):
                    arc_data['sub_char'] = line.replace('*   **Nhân Vật Phụ:**', '').strip()
                elif line.startswith('*   **Mục Tiêu:**'):
                    in_tasks = True
                elif in_tasks and line.startswith('- '):
                    task = line[2:].strip()
                    arc_data['tasks'].append(task)
                elif line == '':
                    continue

            current_arcs.append(arc_data)

    # Extract Future Arcs
    future_arcs = []
    future_arcs_section = re.search(r'## CÁC ARC DỰ KIẾN \(FUTURE ARCS\)\n(.*?)(?=\n## |\Z)', content, re.DOTALL)
    if future_arcs_section:
        arcs_text = future_arcs_section.group(1)
        arc_blocks = re.split(r'\n### \d+\. ', arcs_text)

        for block in arc_blocks:
            if not block.strip(): continue

            lines = block.strip().split('\n')
            title = lines[0].strip()

            arc_data = {
                'title': title,
                'description': '',
                'characters': ''
            }

            for line in lines[1:]:
                line = line.strip()
                if line.startswith('*   **Mô Tả:**'):
                    arc_data['description'] = line.replace('*   **Mô Tả:**', '').strip()
                elif line.startswith('*   **Nhân Vật Tham Gia:**') or line.startswith('- '):
                    if line.startswith('*   **Nhân Vật Tham Gia:**'):
                        arc_data['characters'] += line.replace('*   **Nhân Vật Tham Gia:**', '').strip() + ' '
                    else:
                        arc_data['characters'] += line.replace('- ', '').strip() + ', '

            arc_data['characters'] = arc_data['characters'].strip().rstrip(',')
            future_arcs.append(arc_data)

    # Extract Character Status
    character_status = []
    char_section = re.search(r'## HỒ SƠ NHÂN VẬT & TIẾN ĐỘ\n(.*?)(\n## |\Z)', content, re.DOTALL)
    if char_section:
        table_text = char_section.group(1)
        lines = table_text.strip().split('\n')
        for line in lines:
            if line.startswith('|') and not line.startswith('| :---') and 'Nhân Vật' not in line:
                parts = [p.strip() for p in line.split('|') if p.strip()]
                if len(parts) >= 4:
                    character_status.append({
                        'name': parts[0].replace('**', ''),
                        'pov': parts[1],
                        'status': parts[2],
                        'note': parts[3]
                    })

    return current_arcs, future_arcs, character_status

def format_task(task):
    if '(Đã hoàn thành' in task or '(Hoàn thành' in task:
        return f'<li class="completed">{task}</li>'
    elif 'Hiện Tại' in task or 'Đang diễn ra' in task or '**Mới:**' in task or '**Sự Kiện Mới:**' in task:
        return f'<li class="in-progress">{task}</li>'
    else:
        return f'<li class="future">{task}</li>'

def generate_story_planner_html(repo_root):
    filepath = os.path.join(repo_root, "Đạo", "Quy_Hoạch_Cốt_Truyện", "QUẢN_LÝ_ARC_TRUYỆN.md")
    output_path = os.path.join(repo_root, "story_planner.html")

    current_arcs, future_arcs, char_status = parse_markdown_file(filepath)

    html = [get_html_header("Tuyến Truyện & Kế Hoạch - Cố Nguyên Giới")]

    # Current Arcs
    if current_arcs:
        html.append("<h2>Arc Hiện Tại</h2>")
        html.append('<div class="arcs-grid">')
        for arc in current_arcs:
            html.append('   <div class="arc-card">')
            html.append(f'       <div class="arc-title">{arc["title"]}</div>')
            html.append('       <div class="arc-meta">')
            if arc['arc_name']: html.append(f'           <div><strong>Tên Arc:</strong> {arc["arc_name"]}</div>')
            if arc['status']: html.append(f'           <div><strong>Trạng Thái:</strong> {arc["status"]}</div>')
            if arc['main_char']: html.append(f'           <div><strong>NV Chính:</strong> {arc["main_char"]}</div>')
            if arc['sub_char']: html.append(f'           <div><strong>NV Phụ:</strong> {arc["sub_char"]}</div>')
            html.append('       </div>')
            html.append('       <strong>Mục Tiêu & Tiến Độ:</strong>')
            html.append('       <ul class="arc-tasks">')
            for task in arc['tasks']:
                html.append(f'           {format_task(task)}')
            html.append('       </ul>')
            html.append('   </div>')
        html.append('</div>')

    # Future Arcs
    if future_arcs:
        html.append("<h2>Các Arc Dự Kiến</h2>")
        html.append('<div class="arcs-grid">')
        for arc in future_arcs:
            html.append('   <div class="arc-card" style="border-left-color: #9b59b6;">')
            html.append(f'       <div class="arc-title">{arc["title"]}</div>')
            if arc['description']:
                html.append(f'       <p style="font-size: 0.95em; margin-bottom: 10px;">{arc["description"]}</p>')
            if arc['characters']:
                html.append(f'       <div class="arc-meta"><strong>Nhân vật:</strong> {arc["characters"]}</div>')
            html.append('   </div>')
        html.append('</div>')

    # Character Status
    if char_status:
        html.append("<h2>Trạng Thái Nhân Vật</h2>")
        html.append('<div class="table-wrapper">')
        html.append('   <table>')
        html.append('       <thead>')
        html.append('           <tr>')
        html.append('               <th>Nhân Vật</th>')
        html.append('               <th>Góc Nhìn</th>')
        html.append('               <th>Trạng Thái</th>')
        html.append('               <th>Ghi Chú</th>')
        html.append('           </tr>')
        html.append('       </thead>')
        html.append('       <tbody>')
        for char in char_status:
            html.append('           <tr>')
            html.append(f'               <td><strong>{char["name"]}</strong></td>')
            html.append(f'               <td>{char["pov"]}</td>')
            status_color = "#27ae60" if "Hoạt động" in char["status"] else "#e74c3c" if "Hy Sinh" in char["status"] else "#f39c12"
            html.append(f'               <td style="color: {status_color}; font-weight: 500;">{char["status"]}</td>')
            html.append(f'               <td>{char["note"]}</td>')
            html.append('           </tr>')
        html.append('       </tbody>')
        html.append('   </table>')
        html.append('</div>')

    html.append(get_html_footer())

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(html))

    print(f"Generated Story Planner at {output_path}")

if __name__ == "__main__":
    generate_story_planner_html(os.getcwd())
