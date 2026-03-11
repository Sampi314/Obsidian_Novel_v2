import re

filepath = 'Đạo/BÁO_CÁO_CHẤT_LƯỢNG.md'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# find the table headers
header_match = re.search(r'(\| Ngày \| Đại Diện \| Nội Dung \| Trạng Thái \| Ghi Chú \|.*?)(?:---|===)\n', content, re.DOTALL)
if not header_match:
    print("Could not find table headers")
    exit(1)

header_pos = header_match.end()
lines_after_header = content[header_pos:].split('\n')

table_lines = []
other_lines = []
for line in lines_after_header:
    if line.strip().startswith('|'):
        table_lines.append(line)
    else:
        other_lines.append(line)

if len(table_lines) > 10:
    history = table_lines[:-10]
    recent = table_lines[-10:]

    summary_lines = []
    for h_line in history:
        # extract date and short content
        cols = [col.strip() for col in h_line.split('|')]
        if len(cols) >= 4:
            date = cols[1]
            content_desc = cols[3]
            summary_lines.append(f"- {date}: {content_desc}")

    new_content = content[:header_match.end()]
    new_content += "## LỊCH SỬ\n" + "\n".join(summary_lines) + "\n\n"
    new_content += "## PHIÊN GẦN NHẤT\n" + "\n".join(recent) + "\n"
    new_content += "\n".join(other_lines)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Compacted successfully.")
else:
    print("No compaction needed.")
