import os

files_to_check = []
for root, _, files in os.walk('Đạo'):
    for f in files:
        if f.endswith('.md'):
            files_to_check.append(os.path.join(root, f))

replacements = {
    "(Poison Mushroom Forest)": "(Độc Khuẩn Lâm)",
    "(MOONLIGHT RUINS)": "(Nguyệt Quang Phế Tích)",
    "(Moonlight Ruins)": "(Nguyệt Quang Phế Tích)",
    "MOONLIGHT RUINS": "Nguyệt Quang Phế Tích",
    "Poison Mushroom Forest": "Độc Khuẩn Lâm"
}

for filepath in files_to_check:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        new_content = content
        for k, v in replacements.items():
            new_content = new_content.replace(k, v)

        if content != new_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed specific english in {filepath}")
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
