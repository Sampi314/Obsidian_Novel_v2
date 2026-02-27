import os
import re

mapping = {
    'Chương_00021_Huyết_Độc_Phiến.md': 'Chương_00031_Huyết_Độc_Phiến.md',
    'Chương_00022_Bẫy_Rập_Rừng_Sương.md': 'Chương_00033_Bẫy_Rập_Rừng_Sương.md',
    'Chương_00023_Diệt_Môn_Chi_Họa.md': 'Chương_00036_Diệt_Môn_Chi_Họa.md',
    'Chương_00024_Thanh_Trừng_Nội_Bộ.md': 'Chương_00039_Thanh_Trừng_Nội_Bộ.md',
    'Chương_00025_Mệnh_Lệnh_Bóng_Tối.md': 'Chương_00061_Mệnh_Lệnh_Bóng_Tối.md',
    'Chương_00026_Thí_Nghiệm_Máu.md': 'Chương_00062_Thí_Nghiệm_Máu.md',
    'Chương_00027_Ván_Cờ_Huyết_Độc.md': 'Chương_00063_Ván_Cờ_Huyết_Độc.md',
    'Chương_00028_Truy_Vết_Tử_Thần.md': 'Chương_00064_Truy_Vết_Tử_Thần.md',
    'Chương_00029_Dưới_Bóng_Hắc_Sa.md': 'Chương_00065_Dưới_Bóng_Hắc_Sa.md',
    'Chương_00030_Huyết_Tế_Sa_Mạc.md': 'Chương_00066_Huyết_Tế_Sa_Mạc.md',
    'Chương_00031_Sát_Ý_Rừng_Gai.md': 'Chương_00067_Sát_Ý_Rừng_Gai.md',
    'Chương_00032_Mạng_Lưới_Tử_Thần.md': 'Chương_00068_Mạng_Lưới_Tử_Thần.md',
    'Chương_00033_Con_Mồi_Vào_Rọ.md': 'Chương_00069_Con_Mồi_Vào_Rọ.md'
}

base_dir = 'Đạo/Chương_Truyện/Góc_Nhìn_Lệ_Vô_Tâm'

for old_name, new_name in mapping.items():
    old_path = os.path.join(base_dir, old_name)
    new_path = os.path.join(base_dir, new_name)

    if not os.path.exists(old_path):
        print(f"Skipping {old_name}: File not found.")
        continue

    # Extract new chapter number from new filename
    match = re.search(r'Chương_(\d+)_', new_name)
    if not match:
        print(f"Skipping {old_name}: Could not extract chapter number from {new_name}.")
        continue

    new_chapter_num = int(match.group(1))

    with open(old_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update header
    # Regex looks for # Chương X: or # Chương X
    # It replaces it with # Chương <new_chapter_num>:

    # Check if the title has a colon or not
    header_pattern = re.compile(r'^#\s*Chương\s*\d+\s*(:?)', re.MULTILINE)

    def replace_header(m):
        colon = m.group(1) if m.group(1) else ":" # Default to colon if missing, or keep it
        return f"# Chương {new_chapter_num}{colon}"

    new_content = header_pattern.sub(replace_header, content)

    # Write to new file
    with open(new_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    # Verify new file exists before deleting old one
    if os.path.exists(new_path):
        os.remove(old_path)
        print(f"Migrated {old_name} -> {new_name}")
    else:
        print(f"Error migrating {old_name}: New file not created.")

print("Migration complete.")
