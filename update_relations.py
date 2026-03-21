import os
import yaml
import json
import glob

files = glob.glob('Đạo/Nhân_Vật/Đông_Hoang/Cửu_Hoa_Kiếm_Tông/*.md')
new_files = [
    'Kiều_Thanh_Phong.md', 'Kiều_Tử_Dương.md', 'Kiều_Nguyệt_Bạch.md',
    'Tống_Tiểu_Vân.md', 'Tống_Thiên_Kiếm.md', 'Tống_Hải_Triều.md',
    'Tạ_Hồng_Diệp.md', 'Tạ_Thanh_Thủy.md', 'Tạ_Phi_Vũ.md',
    'Lương_Bạch_Hạc.md', 'Lương_Ngọc_Thạch.md', 'Lương_Tử_Đằng.md',
    'Dư_Tiểu_Băng.md', 'Dư_Thanh_Sơn.md', 'Dư_Thiết_Hán.md'
]

new_relations = []

for file_path in files:
    filename = os.path.basename(file_path)
    if filename in new_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            if content.startswith('---'):
                end_idx = content.find('---', 3)
                if end_idx != -1:
                    yaml_str = content[3:end_idx]
                    try:
                        data = yaml.safe_load(yaml_str)
                        source_name = data.get('name')
                        if source_name and 'arcs' in data:
                            for arc in data['arcs']:
                                if 'relationships' in arc:
                                    for rel in arc['relationships']:
                                        new_rel = {
                                            "source": source_name,
                                            "target": rel.get('character', ''),
                                            "description": rel.get('description', ''),
                                            "feelings": rel.get('feelings', {})
                                        }
                                        new_relations.append(new_rel)
                    except Exception as e:
                        print(f"Error parsing {file_path}: {e}")

if new_relations:
    with open('scripts/relationship_data.js', 'r', encoding='utf-8') as f:
        js_content = f.read()

    start_str = "const relationshipData = "
    if js_content.startswith(start_str):
        json_str = js_content[len(start_str):].strip()
        if json_str.endswith(';'):
            json_str = json_str[:-1]

        try:
            rel_data = json.loads(json_str)
            if 'relationships' in rel_data:
                rel_data['relationships'].extend(new_relations)

                updated_json = json.dumps(rel_data, ensure_ascii=False, indent=2)
                updated_js = start_str + updated_json + ";\n\nexport default relationshipData;\n"

                with open('scripts/relationship_data.js', 'w', encoding='utf-8') as f:
                    f.write(updated_js)
                print(f"Added {len(new_relations)} relationships to scripts/relationship_data.js")
            else:
                print("Error: 'relationships' key not found in relationship_data.js JSON data.")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from relationship_data.js: {e}")
    else:
        print("Error: relationship_data.js does not start with expected export statement.")
