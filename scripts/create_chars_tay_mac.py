#!/usr/bin/env python3
"""
Generate character files for all Tây Mạc factions that currently have no characters.
"""

import os

BASE = "/Users/sampi_wu/Documents/GitHub/Obsidian_Novel_v2"
CHAR_DIR = os.path.join(BASE, "Đạo/Nhân_Vật/Tây_Mạc")


def make_char(name, hantu, archetype, race, cultivation, faction, faction_dir):
    """Create a character markdown file."""
    filename = name.replace(" ", "_") + ".md"
    filepath = os.path.join(CHAR_DIR, faction_dir, filename)
    name_upper = name.upper()

    content = f"""---
type: character
name: {name}
hantu: {hantu}
archetype: {archetype}
race: {race}
avatar: ''
arcs:
  - arc: 1
    status: Chưa Xác Định
    cultivation: {cultivation}
    methods: []
    inventory: []
    stats: [0, 0, 0, 0, 0, 0]
    relationships: []
---

# HỒ SƠ NHÂN VẬT: {name_upper} ({hantu})

## I. THÔNG TIN CƠ BẢN
- **Họ Tên:** {name} ({hantu}).
- **Chủng Tộc:** {race}.
- **Tu Vi:** {cultivation}.
- **Khu Vực:** Tây Mạc.
- **Thế Lực:** {faction}.
- **Chức Vụ:** {archetype}.

## II. NGOẠI HÌNH & TÍNH CÁCH
*(Chưa xác định)*

## III. NĂNG LỰC & CHIẾN ĐẤU
*(Chưa xác định)*

## IV. CÁC MỐI QUAN HỆ
*(Chưa xác định)*

## V. TIỂU SỬ & HÀNH TRÌNH
*(Chưa xác định)*
"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    return filepath


# ============================================================
# FACTION DATA
# ============================================================

factions = {}

# ---- 1. Bán Thạch Cự Nhân (pop 50, small) -> 3-4 chars ----
factions["Bán_Thạch_Cự_Nhân"] = {
    "faction_name": "Bán Thạch Cự Nhân",
    "chars": [
        ("Thạch Cương", "石刚", "Trưởng Lão", "Hỗn huyết (Cự Tộc, Thạch Tộc)", "Trúc Cơ Viên Mãn"),
        ("Thạch Huyết Nham", "石血岩", "Trưởng Lão", "Hỗn huyết (Cự Tộc, Thạch Tộc)", "Trúc Cơ Trung Kỳ"),
        ("Thạch Chùy", "石锤", "Đội Trưởng Vệ Binh", "Hỗn huyết (Cự Tộc, Thạch Tộc)", "Trúc Cơ Sơ Kỳ"),
        ("Nham Liệt", "岩裂", "Chiến Binh", "Hỗn huyết (Cự Tộc, Thạch Tộc)", "Luyện Khí Hậu Kỳ"),
    ],
}

# ---- 2. Cổ Nham Bộ Lạc (pop ~200, Thạch Tộc, medium) -> 5-6 chars ----
factions["Cổ_Nham_Bộ_Lạc"] = {
    "faction_name": "Cổ Nham Bộ Lạc",
    "chars": [
        ("Bàn Thạch", "磐石", "Đại Tế Tư", "Thạch Tộc", "Kim Đan Sơ Kỳ"),
        ("Nham Cốt", "岩骨", "Tế Tư", "Thạch Tộc", "Trúc Cơ Viên Mãn"),
        ("Nham Linh", "岩灵", "Tế Tư", "Thạch Tộc", "Trúc Cơ Viên Mãn"),
        ("Xích Nham", "赤岩", "Thủ Vệ Trưởng", "Thạch Tộc", "Trúc Cơ Hậu Kỳ"),
        ("Nham Tĩnh", "岩静", "Tế Tư", "Thạch Tộc", "Trúc Cơ Trung Kỳ"),
    ],
}

# ---- 3. Cổ Thạch Bộ Lạc (pop ~few hundred to thousands, Thạch Tộc, medium) -> 5-6 chars ----
factions["Cổ_Thạch_Bộ_Lạc"] = {
    "faction_name": "Cổ Thạch Bộ Lạc",
    "chars": [
        ("Vạn Cổ Thạch", "万古石", "Thạch Tổ", "Thạch Tộc", "Luyện Hư Sơ Kỳ"),
        ("Nham Trầm", "岩沉", "Trưởng Lão", "Thạch Tộc", "Nguyên Anh Sơ Kỳ"),
        ("Thạch Uy", "石威", "Chiến Thạch Thần", "Thạch Tộc", "Kim Đan Hậu Kỳ"),
        ("Nham Phong", "岩峰", "Trưởng Lão", "Thạch Tộc", "Kim Đan Trung Kỳ"),
        ("Thạch Lôi", "石雷", "Chiến Thạch Thần", "Thạch Tộc", "Kim Đan Sơ Kỳ"),
        ("Ngọc Thạch", "玉石", "Trưởng Lão", "Thạch Tộc", "Nguyên Anh Trung Kỳ"),
    ],
}

# ---- 4. Cổ Tích Cự Nhân Thức Tỉnh (pop 25, small) -> 3-4 chars ----
factions["Cổ_Tích_Cự_Nhân_Thức_Tỉnh"] = {
    "faction_name": "Cổ Tích Cự Nhân Thức Tỉnh",
    "chars": [
        ("Cổ Mộng", "古梦", "Trưởng Lão", "Cự Tộc", "Kim Đan Sơ Kỳ"),
        ("Cổ Sơn", "古山", "Chiến Binh Cổ Đại", "Cự Tộc", "Trúc Cơ Viên Mãn"),
        ("Cổ Nham Hồn", "古岩魂", "Chiến Binh Cổ Đại", "Cự Tộc", "Trúc Cơ Hậu Kỳ"),
    ],
}

# ---- 5. Cổ Tích Thám Hiểm Đoàn (pop 40, small) -> 4-5 chars ----
factions["Cổ_Tích_Thám_Hiểm_Đoàn"] = {
    "faction_name": "Cổ Tích Thám Hiểm Đoàn",
    "chars": [
        ("Lý Cổ Trần", "李古尘", "Đoàn Trưởng", "Nhân Tộc", "Kim Đan Sơ Kỳ"),
        ("Trần Phá Bẫy", "陈破陷", "Phó Đoàn", "Nhân Tộc", "Trúc Cơ Viên Mãn"),
        ("Nguyễn Dịch Cổ", "阮译古", "Phó Đoàn", "Nhân Tộc", "Trúc Cơ Viên Mãn"),
        ("Hoàng Thổ Đạo", "黄土道", "Thám Hiểm Viên", "Nhân Tộc", "Trúc Cơ Hậu Kỳ"),
    ],
}

# ---- 6. Cự Tộc Phu Khuân Vác (pop 60, small-medium) -> 4-5 chars ----
factions["Cự_Tộc_Phu_Khuân_Vác"] = {
    "faction_name": "Cự Tộc Phu Khuân Vác",
    "chars": [
        ("Sa Lực", "沙力", "Công Đầu", "Cự Tộc", "Trúc Cơ Sơ Kỳ"),
        ("Sa Mặc", "沙默", "Phu Khuân Vác", "Cự Tộc", "Luyện Khí Hậu Kỳ"),
        ("Sa Trọng", "沙重", "Tổ Trưởng", "Cự Tộc", "Luyện Khí Hậu Kỳ"),
        ("Sa Kiên", "沙坚", "Tổ Trưởng", "Cự Tộc", "Luyện Khí Hậu Kỳ"),
    ],
}

# ---- 7. Hoàng Sa Di Dân (pop 300, phàm nhân, small) -> 4-5 chars ----
factions["Hoàng_Sa_Di_Dân"] = {
    "faction_name": "Hoàng Sa Di Dân",
    "chars": [
        ("Hoàng Cổ Nham", "黄古岩", "Trưởng Lão", "Nhân Tộc", "Phàm Nhân"),
        ("Hoàng Minh Nguyệt", "黄明月", "Bô Lão", "Nhân Tộc", "Phàm Nhân"),
        ("Hoàng Thiếu Quang", "黄少光", "Thanh Niên", "Nhân Tộc", "Phàm Nhân"),
        ("Hoàng Ngọc Dương", "黄玉阳", "Huyết Mạch Thức Tỉnh", "Nhân Tộc", "Luyện Khí Sơ Kỳ"),
    ],
}

# ---- 8. Hỏa Diễm Công Phường (pop 25, small) -> 3-4 chars ----
factions["Hỏa_Diễm_Công_Phường"] = {
    "faction_name": "Hỏa Diễm Công Phường",
    "chars": [
        ("Hỏa Thiết Tâm", "火铁心", "Phường Chủ", "Nhân Tộc", "Trúc Cơ Viên Mãn"),
        ("Hỏa Giáp Trụ", "火甲柱", "Thợ Cả", "Nhân Tộc", "Trúc Cơ Sơ Kỳ"),
        ("Hỏa Tiểu Viêm", "火小炎", "Học Việc", "Nhân Tộc", "Luyện Khí Trung Kỳ"),
    ],
}

# ---- 9. Kim Sa Tự (pop 5000, Hạng Nhất, large) -> 10-12 chars ----
factions["Kim_Sa_Tự"] = {
    "faction_name": "Kim Sa Tự",
    "chars": [
        ("Không Độ", "空度", "Trụ Trì", "Nhân Tộc", "Hóa Thần Sơ Kỳ"),
        ("Pháp Không", "法空", "Đại Trưởng Lão", "Nhân Tộc", "Nguyên Anh Hậu Kỳ"),
        ("Giới Trần", "戒尘", "Trưởng Lão", "Nhân Tộc", "Nguyên Anh Trung Kỳ"),
        ("Huệ Minh", "慧明", "Thủ Các Kinh Diệu", "Nhân Tộc", "Nguyên Anh Trung Kỳ"),
        ("Kim Cương", "金刚", "Hộ Pháp", "Nhân Tộc", "Nguyên Anh Sơ Kỳ"),
        ("Phổ Tế", "普济", "Trưởng Lão Phổ Độ", "Nhân Tộc", "Nguyên Anh Sơ Kỳ"),
        ("Thiện Nhẫn", "善忍", "Trưởng Lão Đạt Ma", "Nhân Tộc", "Kim Đan Đỉnh Phong"),
        ("Minh Ngộ", "明悟", "Khổ Hạnh Tăng", "Nhân Tộc", "Kim Đan Hậu Kỳ"),
        ("Tịnh Tâm", "净心", "Tăng Lữ", "Nhân Tộc", "Kim Đan Sơ Kỳ"),
        ("Viên Thông", "圆通", "Sa Di Trưởng", "Nhân Tộc", "Trúc Cơ Hậu Kỳ"),
    ],
}

# ---- 10. Ký Sinh Liên Minh (tiny parasites, small) -> 3 chars ----
factions["Ký_Sinh_Liên_Minh"] = {
    "faction_name": "Ký Sinh Liên Minh",
    "chars": [
        ("Khuẩn Ám", "菌暗", "Ký Sinh Trưởng", "Vi Tộc", "Luyện Khí Hậu Kỳ"),
        ("Khuẩn Tiềm", "菌潜", "Ký Sinh Trưởng", "Vi Tộc", "Luyện Khí Trung Kỳ"),
        ("Bào Ẩn", "胞隐", "Ký Sinh Trưởng", "Vi Tộc", "Luyện Khí Trung Kỳ"),
    ],
}

# ---- 11. Lưu Sa Huyễn Ảo (Lưu Sa Huyễn Cung) (pop 1200, Hạng Nhì, large) -> 8-10 chars ----
factions["Lưu_Sa_Huyễn_Ảo"] = {
    "faction_name": "Lưu Sa Huyễn Cung",
    "chars": [
        ("Linh Cơ", "灵机", "Cung Chủ", "Nhân Tộc", "Nguyên Anh Hậu Kỳ"),
        ("Hồ Huyễn Yên", "狐幻烟", "Viện Chủ Huyễn Ảnh", "Yêu Tộc (Hồ Ly)", "Nguyên Anh Sơ Kỳ"),
        ("Hồ Mộng Điệp", "狐梦蝶", "Đội Trưởng Sa Hồ", "Yêu Tộc (Hồ Ly)", "Kim Đan Viên Mãn"),
        ("Vân Ảo", "云幻", "Trưởng Lão", "Nhân Tộc", "Kim Đan Hậu Kỳ"),
        ("Hồ Tuyết Lạc", "狐雪落", "Huyễn Thuật Sư", "Yêu Tộc (Hồ Ly)", "Kim Đan Trung Kỳ"),
        ("Linh Mộng", "灵梦", "Chân Truyền Đệ Tử", "Nhân Tộc", "Kim Đan Sơ Kỳ"),
        ("Hồ Sương Nhi", "狐霜儿", "Linh Hồ Trinh Sát", "Yêu Tộc (Hồ Ly)", "Trúc Cơ Hậu Kỳ"),
        ("Mộng Hà", "梦霞", "Nội Môn Đệ Tử", "Nhân Tộc", "Trúc Cơ Trung Kỳ"),
    ],
}

# ---- 12. Phong Hóa Giả Hội (pop 30 Thạch Tộc, small) -> 3-4 chars ----
factions["Phong_Hóa_Giả_Hội"] = {
    "faction_name": "Phong Hóa Giả Hội",
    "chars": [
        ("Tàn Nham", "残岩", "Hội Trưởng", "Thạch Tộc", "Kim Đan Sơ Kỳ"),
        ("Bạc Thạch", "薄石", "Thành Viên", "Thạch Tộc", "Trúc Cơ Hậu Kỳ"),
        ("Mạt Nham", "末岩", "Thành Viên", "Thạch Tộc", "Trúc Cơ Trung Kỳ"),
    ],
}

# ---- 13. Phong Sát Cốc (pop 3500, Hạng Nhì, large) -> 8-10 chars ----
factions["Phong_Sát_Cốc"] = {
    "faction_name": "Phong Sát Cốc",
    "chars": [
        ("Hắc Phong", "黑风", "Cốc Chủ", "Nhân Tộc", "Nguyên Anh Hậu Kỳ"),
        ("Phong Cuồng", "风狂", "Hộ Pháp", "Nhân Tộc", "Nguyên Anh Sơ Kỳ"),
        ("Phong Ảnh", "风影", "Đội Trưởng Ảnh Phong", "Nhân Tộc", "Kim Đan Đỉnh Phong"),
        ("Sa Quỷ", "沙鬼", "Đội Trưởng Sa Quỷ", "Nhân Tộc", "Kim Đan Hậu Kỳ"),
        ("Huyết Phong", "血风", "Hộ Pháp", "Yêu Tộc", "Nguyên Anh Sơ Kỳ"),
        ("Tử Bão", "紫暴", "Trưởng Lão", "Nhân Tộc", "Kim Đan Viên Mãn"),
        ("Phong Nha", "风牙", "Trưởng Lão", "Yêu Tộc", "Kim Đan Hậu Kỳ"),
        ("Hắc Sa", "黑沙", "Nội Môn Đệ Tử", "Nhân Tộc", "Kim Đan Sơ Kỳ"),
        ("Lý Cuồng Phong", "李狂风", "Chân Truyền Đệ Tử", "Nhân Tộc", "Kim Đan Trung Kỳ"),
        ("Phong Liệt", "风烈", "Ngoại Môn Đệ Tử", "Nhân Tộc", "Trúc Cơ Hậu Kỳ"),
    ],
}

# ---- 14. Sa Cự Nhân Bộ Lạc (pop 80, small-medium) -> 5 chars ----
factions["Sa_Cự_Nhân_Bộ_Lạc"] = {
    "faction_name": "Sa Cự Nhân Bộ Lạc",
    "chars": [
        ("Sa Cương", "沙刚", "Tộc Trưởng", "Cự Tộc", "Kim Đan Sơ Kỳ"),
        ("Sa Trầm", "沙沉", "Trưởng Lão", "Cự Tộc", "Trúc Cơ Viên Mãn"),
        ("Sa Hùng", "沙雄", "Trưởng Lão", "Cự Tộc", "Trúc Cơ Viên Mãn"),
        ("Lão Sa", "老沙", "Thợ Đào Giếng", "Cự Tộc", "Trúc Cơ Hậu Kỳ"),
        ("Sa Thiết", "沙铁", "Chiến Binh", "Cự Tộc", "Trúc Cơ Trung Kỳ"),
    ],
}

# ---- 15. Sa Mãng Tộc (pop 200, Yêu Tộc xà, small-medium) -> 4-5 chars ----
factions["Sa_Mãng_Tộc"] = {
    "faction_name": "Sa Mãng Tộc",
    "chars": [
        ("Huyền Sa", "玄沙", "Tộc Trưởng", "Yêu Tộc (Xà)", "Trúc Cơ Hậu Kỳ"),
        ("Xà Độc Nha", "蛇毒牙", "Trưởng Lão", "Yêu Tộc (Xà)", "Trúc Cơ Trung Kỳ"),
        ("Xà Ám Lân", "蛇暗鳞", "Trưởng Lão", "Yêu Tộc (Xà)", "Trúc Cơ Sơ Kỳ"),
        ("Xà Linh Vĩ", "蛇灵尾", "Trinh Sát", "Yêu Tộc (Xà)", "Luyện Khí Hậu Kỳ"),
    ],
}

# ---- 16. Sa Mạc Hướng Đạo Hội (pop 80, small) -> 4-5 chars ----
factions["Sa_Mạc_Hướng_Đạo_Hội"] = {
    "faction_name": "Sa Mạc Hướng Đạo Hội",
    "chars": [
        ("Phong Sa Lão Nhân", "风沙老人", "Hội Trưởng", "Nhân Tộc", "Trúc Cơ Trung Kỳ"),
        ("Lê Thuận Phong", "黎顺风", "Trưởng Lão", "Nhân Tộc", "Trúc Cơ Sơ Kỳ"),
        ("Đặng Sa Đạo", "邓沙道", "Trưởng Lão", "Nhân Tộc", "Trúc Cơ Sơ Kỳ"),
        ("Phạm Hướng Tây", "范向西", "Hướng Đạo", "Nhân Tộc", "Luyện Khí Hậu Kỳ"),
        ("Vũ Sa Lộ", "武沙路", "Hướng Đạo", "Nhân Tộc", "Luyện Khí Trung Kỳ"),
    ],
}

# ---- 17. Sa Mạc Sinh Tồn Đoàn (pop 50, small) -> 4-5 chars ----
factions["Sa_Mạc_Sinh_Tồn_Đoàn"] = {
    "faction_name": "Sa Mạc Sinh Tồn Đoàn",
    "chars": [
        ("Hạ Thiên Lý", "夏千里", "Đoàn Trưởng", "Nhân Tộc", "Trúc Cơ Sơ Kỳ"),
        ("Trần Cát Phong", "陈喝风", "Phó Đoàn", "Nhân Tộc", "Luyện Khí Đỉnh Phong"),
        ("Lê Hoang Sa", "黎荒沙", "Phó Đoàn", "Nhân Tộc", "Luyện Khí Đỉnh Phong"),
        ("Nguyễn Sinh Tồn", "阮生存", "Thành Viên", "Nhân Tộc", "Luyện Khí Hậu Kỳ"),
    ],
}

# ---- 18. Sa Thạch Du Mục (pop 100, Thạch Tộc, small-medium) -> 5 chars ----
factions["Sa_Thạch_Du_Mục"] = {
    "faction_name": "Sa Thạch Du Mục",
    "chars": [
        ("Nham Lưu", "岩流", "Tộc Trưởng", "Thạch Tộc", "Trúc Cơ Viên Mãn"),
        ("Nham Tầm", "岩寻", "Trưởng Lão Thăm Dò", "Thạch Tộc", "Trúc Cơ Trung Kỳ"),
        ("Nham Hậu", "岩厚", "Trưởng Lão", "Thạch Tộc", "Trúc Cơ Trung Kỳ"),
        ("Thạch Sa", "石沙", "Trinh Sát Trưởng", "Thạch Tộc", "Trúc Cơ Sơ Kỳ"),
        ("Nham Tiểu Lộ", "岩小路", "Trinh Sát", "Thạch Tộc", "Luyện Khí Hậu Kỳ"),
    ],
}

# ---- 19. Sa Thạch Lưu Dân (pop ~40, small) -> 3-4 chars ----
factions["Sa_Thạch_Lưu_Dân"] = {
    "faction_name": "Sa Thạch Lưu Dân",
    "chars": [
        ("Sa Tàn", "沙残", "Trưởng Đoàn", "Thạch Tộc", "Trúc Cơ Sơ Kỳ"),
        ("Nham Thương", "岩伤", "Hộ Vệ", "Thạch Tộc", "Luyện Khí Hậu Kỳ"),
        ("Nham Nghịch", "岩逆", "Lưu Dân Đặc Biệt", "Thạch Tộc", "Luyện Khí Trung Kỳ"),
    ],
}

# ---- 20. Sa Tặc Liên Minh (pop 5000, Hạng Ba, large) -> 8-10 chars ----
factions["Sa_Tặc_Liên_Minh"] = {
    "faction_name": "Sa Tặc Liên Minh",
    "chars": [
        ("Hắc Phong Đại Vương", "黑风大王", "Minh Chủ", "Nhân Tộc", "Trúc Cơ Hậu Kỳ"),
        ("Đào Cuồng Sa", "陶狂沙", "Phó Minh Chủ", "Nhân Tộc", "Trúc Cơ Trung Kỳ"),
        ("Lang Ảnh Sa", "狼影沙", "Đội Trưởng Ảnh Sa", "Nhân Tộc", "Trúc Cơ Trung Kỳ"),
        ("Lý Huyết Lang", "李血狼", "Đội Trưởng Huyết Lang", "Nhân Tộc", "Trúc Cơ Sơ Kỳ"),
        ("Phong Tàn Nhẫn", "风残忍", "Trưởng Lão", "Nhân Tộc", "Trúc Cơ Trung Kỳ"),
        ("Trần Độc Nhãn", "陈独眼", "Thủ Lĩnh Băng Đảng", "Nhân Tộc", "Trúc Cơ Sơ Kỳ"),
        ("Sa Đồ", "沙屠", "Sát Thủ", "Sa Tộc", "Trúc Cơ Sơ Kỳ"),
        ("Lưu Cát Đạo", "刘割盗", "Thủ Lĩnh Băng Đảng", "Nhân Tộc", "Luyện Khí Đỉnh Phong"),
    ],
}

# ---- 21. San Hô Thợ Lặn Đội (pop ~25, small) -> 3-4 chars ----
factions["San_Hô_Thợ_Lặn_Đội"] = {
    "faction_name": "San Hô Thợ Lặn Đội",
    "chars": [
        ("Nguyễn Thủy Tiên", "阮水仙", "Đội Trưởng", "Nhân Tộc", "Trúc Cơ Viên Mãn"),
        ("Trần Hải Sâm", "陈海参", "Thợ Lặn Kỳ Cựu", "Nhân Tộc", "Luyện Khí Trung Kỳ"),
        ("Lê Ngọc Trai", "黎玉珠", "Thợ Lặn Kỳ Cựu", "Nhân Tộc", "Luyện Khí Trung Kỳ"),
    ],
}

# ---- 22. San Hô Vi Trùng (colony organisms, very small) -> 3 chars ----
factions["San_Hô_Vi_Trùng"] = {
    "faction_name": "San Hô Vi Trùng",
    "chars": [
        ("Trùng Mẫu", "虫母", "San Hô Mẫu Trùng", "Vi Tộc", "Luyện Khí Hậu Kỳ"),
        ("Trùng Cổ Sinh", "虫古生", "Vi Trùng Cổ Đại", "Vi Tộc", "Luyện Khí Trung Kỳ"),
        ("Trùng Tân Nha", "虫新芽", "Vi Trùng Kế Thừa", "Vi Tộc", "Luyện Khí Sơ Kỳ"),
    ],
}

# ---- 23. Thiên Sa Thương Hội (pop 20000, Hạng Nhất, large) -> 10-12 chars ----
factions["Thiên_Sa_Thương_Hội"] = {
    "faction_name": "Thiên Sa Thương Hội",
    "chars": [
        ("Cổ Thiên Lý", "古千里", "Gia Chủ Sa Thương", "Nhân Tộc", "Nguyên Anh Trung Kỳ"),
        ("Hứa Nhược Thủy", "许若水", "Gia Chủ Sa Dược", "Nhân Tộc", "Nguyên Anh Sơ Kỳ"),
        ("Trần Khoáng Sơn", "陈矿山", "Gia Chủ Khai Khoáng", "Nhân Tộc", "Nguyên Anh Sơ Kỳ"),
        ("Lâm Thiên Mục", "林千目", "Gia Chủ Tình Báo", "Nhân Tộc", "Nguyên Anh Sơ Kỳ"),
        ("Vô Danh", "无名", "Thủ Lĩnh Sa Ảnh", "Nhân Tộc", "Nguyên Anh Hậu Kỳ"),
        ("Phạm Thương Đạo", "范商道", "Tổng Quản Vận Tải", "Nhân Tộc", "Kim Đan Viên Mãn"),
        ("Lý Sa Kim", "李沙金", "Tổng Quản Thương Phường", "Nhân Tộc", "Kim Đan Hậu Kỳ"),
        ("Đặng Thiên Hà", "邓天河", "Đội Trưởng Hộ Thương", "Nhân Tộc", "Kim Đan Trung Kỳ"),
        ("Hoàng Sa Nhạn", "黄沙雁", "Sát Thủ Sa Ảnh", "Nhân Tộc", "Kim Đan Sơ Kỳ"),
        ("Nguyễn Bảo Tháp", "阮宝塔", "Quản Lý Bảo Tháp", "Nhân Tộc", "Trúc Cơ Viên Mãn"),
        ("Vũ Thương Vân", "武商云", "Thương Nhân", "Nhân Tộc", "Trúc Cơ Hậu Kỳ"),
    ],
}

# ---- 24. Thiết Giáp Yêu Thú Đàn (pop ~100, small-medium) -> 4-5 chars ----
factions["Thiết_Giáp_Yêu_Thú_Đàn"] = {
    "faction_name": "Thiết Giáp Yêu Thú Đàn",
    "chars": [
        ("Thiết Giáp Vương", "铁甲王", "Đàn Chủ", "Yêu Tộc (Trùng)", "Trúc Cơ Viên Mãn"),
        ("Thiết Nha", "铁牙", "Cận Vệ", "Yêu Tộc (Trùng)", "Trúc Cơ Trung Kỳ"),
        ("Thiết Lân", "铁鳞", "Cận Vệ", "Yêu Tộc (Trùng)", "Trúc Cơ Trung Kỳ"),
        ("Thiết Ấu", "铁幼", "Ấu Trùng Đặc Biệt", "Yêu Tộc (Trùng)", "Luyện Khí Sơ Kỳ"),
    ],
}

# ---- 25. Thần Cung Bắn Sa (Thần Cung Môn) (pop 2000, Hạng Ba, medium-large) -> 8 chars ----
factions["Thần_Cung_Bắn_Sa"] = {
    "faction_name": "Thần Cung Môn",
    "chars": [
        ("Tiễn Vô Song", "箭无双", "Môn Chủ", "Nhân Tộc", "Nguyên Anh Hậu Kỳ"),
        ("Tiễn Phá Không", "箭破空", "Đại Trưởng Lão", "Nhân Tộc", "Nguyên Anh Sơ Kỳ"),
        ("Lý Xuyên Vân", "李穿云", "Trưởng Lão", "Nhân Tộc", "Kim Đan Viên Mãn"),
        ("Cung Tuyệt Trần", "弓绝尘", "Viện Chủ Chế Khí", "Nhân Tộc", "Kim Đan Viên Mãn"),
        ("Tiễn Linh Phong", "箭灵风", "Trưởng Lão", "Nhân Tộc", "Kim Đan Hậu Kỳ"),
        ("Phạm Nhất Tiễn", "范一箭", "Xạ Thủ Chân Truyền", "Nhân Tộc", "Kim Đan Sơ Kỳ"),
        ("Đặng Truy Phong", "邓追风", "Đội Trưởng Trinh Sát", "Nhân Tộc", "Trúc Cơ Viên Mãn"),
        ("Lê Thiên Mục", "黎天目", "Nội Môn Đệ Tử", "Nhân Tộc", "Trúc Cơ Hậu Kỳ"),
    ],
}

# ---- 26. Thủy Nguồn Bảo Vệ Đoàn (Thanh Lương Thủ Vệ) (pop 800, Hạng Ba, medium-large) -> 7-8 chars ----
factions["Thủy_Nguồn_Bảo_Vệ_Đoàn"] = {
    "faction_name": "Thanh Lương Thủ Vệ",
    "chars": [
        ("Hàn Thủy", "寒水", "Đoàn Trưởng", "Nhân Tộc", "Nguyên Anh Sơ Kỳ"),
        ("Trần Thanh Lương", "陈清凉", "Thống Lĩnh Tuần Tra", "Nhân Tộc", "Kim Đan Trung Kỳ"),
        ("Lý Thủy Nguyên", "李水源", "Viện Chủ Thủy Nguyên", "Nhân Tộc", "Kim Đan Sơ Kỳ"),
        ("Phạm Tụ Thủy", "范聚水", "Thủy Sư", "Nhân Tộc", "Trúc Cơ Viên Mãn"),
        ("Đặng Tuần Sa", "邓巡沙", "Đội Phó Tuần Tra", "Nhân Tộc", "Trúc Cơ Hậu Kỳ"),
        ("Nguyễn Hướng Tuyền", "阮向泉", "Hướng Đạo", "Nhân Tộc", "Trúc Cơ Trung Kỳ"),
        ("Sơn Thủ Hộ", "山守护", "Hộ Pháp Cự Nhân", "Cự Tộc", "Trúc Cơ Viên Mãn"),
    ],
}

# ---- 27. Thủy Tinh Thạch Phường (pop 45, Thạch Tộc, small) -> 4 chars ----
factions["Thủy_Tinh_Thạch_Phường"] = {
    "faction_name": "Thủy Tinh Thạch Phường",
    "chars": [
        ("Tinh Minh", "晶明", "Phường Chủ", "Thạch Tộc", "Trúc Cơ Hậu Kỳ"),
        ("Tinh Thấu", "晶透", "Thợ Cả", "Thạch Tộc", "Trúc Cơ Sơ Kỳ"),
        ("Tinh Sắc", "晶色", "Thợ Cả", "Thạch Tộc", "Trúc Cơ Sơ Kỳ"),
        ("Tinh Tiểu Quang", "晶小光", "Thợ Phụ", "Thạch Tộc", "Luyện Khí Hậu Kỳ"),
    ],
}

# ---- 28. Trục Khách Đường (pop ~40+, Hạng Tư, small-medium) -> 5-6 chars ----
factions["Trục_Khách_Đường"] = {
    "faction_name": "Trục Khách Đường",
    "chars": [
        ("Đoạn Kiếm Sinh", "断剑生", "Đường Chủ", "Nhân Tộc", "Nguyên Anh Sơ Kỳ"),
        ("Lâm Tàn Kiếm", "林残剑", "Giáo Tập", "Nhân Tộc", "Kim Đan Hậu Kỳ"),
        ("Phong Bạch Nhận", "风白刃", "Giáo Tập", "Nhân Tộc", "Kim Đan Trung Kỳ"),
        ("Vũ Loạn Kiếm", "武乱剑", "Giáo Tập", "Nhân Tộc", "Kim Đan Sơ Kỳ"),
        ("Lý Trúc Phong", "李逐风", "Đệ Tử", "Nhân Tộc", "Trúc Cơ Hậu Kỳ"),
        ("Trần Vô Danh", "陈无名", "Đệ Tử", "Nhân Tộc", "Trúc Cơ Trung Kỳ"),
    ],
}

# ---- 29. Đại Mạc Gác Đêm (pop 18, very small) -> 3-4 chars ----
factions["Đại_Mạc_Gác_Đêm"] = {
    "faction_name": "Đại Mạc Gác Đêm",
    "chars": [
        ("Dạ Cương", "夜刚", "Đội Trưởng", "Cự Tộc (Sa Cự Nhân)", "Trúc Cơ Viên Mãn"),
        ("Dạ Ảnh", "夜影", "Vệ Binh", "Cự Tộc (Sa Cự Nhân)", "Trúc Cơ Trung Kỳ"),
        ("Dạ Hỏa", "夜火", "Thợ Đuốc", "Cự Tộc (Sa Cự Nhân)", "Trúc Cơ Sơ Kỳ"),
        ("Dạ Trầm", "夜沉", "Vệ Binh", "Cự Tộc (Sa Cự Nhân)", "Luyện Khí Hậu Kỳ"),
    ],
}

# ---- 30. Địa Tâm Thám Hiểm Đội (pop 20, Thạch Tộc, small) -> 4 chars ----
factions["Địa_Tâm_Thám_Hiểm_Đội"] = {
    "faction_name": "Địa Tâm Thám Hiểm Đội",
    "chars": [
        ("Thâm Nham", "深岩", "Đội Trưởng", "Thạch Tộc", "Trúc Cơ Viên Mãn"),
        ("Nham Đào", "岩掘", "Phó Đội", "Thạch Tộc", "Trúc Cơ Trung Kỳ"),
        ("Nham Thính", "岩听", "Thạch Tộc Nghe Đá", "Thạch Tộc", "Trúc Cơ Sơ Kỳ"),
        ("Nham Quang", "岩光", "Thành Viên", "Thạch Tộc", "Luyện Khí Hậu Kỳ"),
    ],
}


# ============================================================
# MAIN
# ============================================================

def main():
    total = 0
    for faction_dir, data in factions.items():
        dirpath = os.path.join(CHAR_DIR, faction_dir)
        os.makedirs(dirpath, exist_ok=True)
        faction_name = data["faction_name"]
        for name, hantu, archetype, race, cultivation in data["chars"]:
            filepath = make_char(name, hantu, archetype, race, cultivation, faction_name, faction_dir)
            print(f"  Created: {filepath}")
            total += 1
        print(f"[{faction_dir}] -> {len(data['chars'])} characters")
    print(f"\n=== Total files created: {total} ===")


if __name__ == "__main__":
    main()
