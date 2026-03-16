#!/usr/bin/env python3
"""
Generate character files for all Bắc Băng factions that currently have NO characters.
"""
import os

BASE = "/Users/sampi_wu/Documents/GitHub/Obsidian_Novel_v2"
CHAR_DIR = os.path.join(BASE, "Đạo", "Nhân_Vật", "Bắc_Băng")

def make_char(name, hantu, archetype, race, cultivation, faction_name, role):
    """Generate the full markdown content for a character file."""
    return f"""---
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

# HỒ SƠ NHÂN VẬT: {name.upper()} ({hantu})

## I. THÔNG TIN CƠ BẢN
- **Họ Tên:** {name} ({hantu}).
- **Chủng Tộc:** {race}.
- **Tu Vi:** {cultivation}.
- **Khu Vực:** Bắc Băng.
- **Thế Lực:** {faction_name}.
- **Chức Vụ:** {role}.

## II. NGOẠI HÌNH & TÍNH CÁCH
*(Chưa xác định)*

## III. NĂNG LỰC & CHIẾN ĐẤU
*(Chưa xác định)*

## IV. CÁC MỐI QUAN HỆ
*(Chưa xác định)*

## V. TIỂU SỬ & HÀNH TRÌNH
*(Chưa xác định)*
"""

# ============================================================
# FACTION DEFINITIONS - characters per faction
# ============================================================

factions = {}

# ---- 1. Hàn Tinh Quan Trắc Đài (pop 15, Hạng Năm, Nhân Tộc) → Small: 3-5 ----
factions["Hàn_Tinh_Quan_Trắc_Đài"] = {
    "faction_name": "Hàn Tinh Quan Trắc Đài",
    "characters": [
        ("Tinh Hàn Tử", "星寒子", "Đài Trưởng", "Nhân Tộc", "Trúc Cơ Viên Mãn", "Đài Trưởng"),
        ("Lý Tinh Vân", "李星云", "Giáo Sư", "Nhân Tộc", "Trúc Cơ Sơ Kỳ", "Giáo Sư Thiên Văn"),
        ("Trần Quang Minh", "陈光明", "Trợ Giảng", "Nhân Tộc", "Luyện Khí Hậu Kỳ", "Quan Trắc Viên"),
        ("Hoàng Tinh Nguyệt", "黄星月", "Họa Sĩ", "Nhân Tộc", "Luyện Khí Trung Kỳ", "Họa Sĩ Thiên Văn"),
    ],
}

# ---- 2. Hàn Phong Truyền Tin Đội (pop 12, Hạng Năm, Vũ Tộc) → Small: 3-5 ----
factions["Hàn_Phong_Truyền_Tin_Đội"] = {
    "faction_name": "Hàn Phong Truyền Tin Đội",
    "characters": [
        ("Vũ Tốc Vân", "羽速云", "Đội Trưởng", "Vũ Tộc", "Trúc Cơ Trung Kỳ", "Đội Trưởng"),
        ("Vũ Khinh Hồng", "羽轻鸿", "Truyền Tin Viên", "Vũ Tộc", "Luyện Khí Đỉnh Phong", "Phó Đội Trưởng"),
        ("Vũ Phiêu Linh", "羽飘零", "Truyền Tin Viên", "Vũ Tộc", "Luyện Khí Hậu Kỳ", "Truyền Tin Viên"),
        ("Vũ Tật Phong", "羽疾风", "Khí Tượng Viên", "Vũ Tộc", "Luyện Khí Trung Kỳ", "Chuyên Viên Khí Tượng"),
    ],
}

# ---- 3. Hàn Dân Hộ Vệ Đội (pop 215, Hạng Năm, Nhân Tộc) → Medium: 5-8 ----
factions["Hàn_Dân_Hộ_Vệ_Đội"] = {
    "faction_name": "Hàn Dân Hộ Vệ Đội",
    "characters": [
        ("Vương Thiết Nha", "王铁牙", "Đội Trưởng", "Nhân Tộc", "Luyện Khí Đỉnh Phong", "Đội Trưởng"),
        ("Vương Tiểu Nhị", "王小二", "Phó Đội", "Nhân Tộc", "Luyện Khí Trung Kỳ", "Phó Đội Trưởng"),
        ("Đỗ Sơn Hổ", "杜山虎", "Trinh Sát", "Nhân Tộc", "Luyện Khí Sơ Kỳ", "Trinh Sát Viên"),
        ("Lê Thạch Bàn", "黎石磐", "Thợ Bẫy", "Nhân Tộc", "Phàm Nhân", "Trưởng Nhóm Đặt Bẫy"),
        ("Phạm Hỏa Nương", "范火娘", "Y Sư", "Nhân Tộc", "Phàm Nhân", "Y Sư Dân Quân"),
        ("Nguyễn Đại Lực", "阮大力", "Chiến Binh", "Nhân Tộc", "Phàm Nhân", "Tổ Trưởng Tuần Tra"),
    ],
}

# ---- 4. Đoản Dực Lạc Đoàn (pop 30, Hạng Năm, Vũ Tộc bị trục xuất) → Small: 3-5 ----
factions["Đoản_Dực_Lạc_Đoàn"] = {
    "faction_name": "Đoản Dực Lạc Đoàn",
    "characters": [
        ("Vũ Tàn Phong", "羽残风", "Đoàn Trưởng", "Vũ Tộc", "Trúc Cơ Hậu Kỳ", "Đoàn Trưởng"),
        ("Vũ Lạc Vũ", "羽落羽", "Phó Đoàn Trưởng", "Vũ Tộc", "Luyện Khí Đỉnh Phong", "Phó Đoàn Trưởng"),
        ("Vũ Chiết Dực", "羽折翼", "Thợ Thủ Công", "Vũ Tộc", "Luyện Khí Hậu Kỳ", "Thợ Chế Tác Lông Vũ"),
        ("Vũ Vô Thiên", "羽无天", "Đệ Tử", "Vũ Tộc", "Luyện Khí Sơ Kỳ", "Ấu Đồ Phong Linh Căn"),
    ],
}

# ---- 5. Đại Bàng Tuyết Đàn (pop 26, Hạng Năm, Yêu Tộc Ưng) → Small: 3-5 ----
factions["Đại_Bàng_Tuyết_Đàn"] = {
    "faction_name": "Đại Bàng Tuyết Đàn",
    "characters": [
        ("Ưng Liệt", "鹰烈", "Đàn Trưởng", "Yêu Tộc", "Trúc Cơ Trung Kỳ", "Đàn Trưởng"),
        ("Ưng Hàn Ảnh", "鹰寒影", "Đội Trưởng Trinh Sát", "Yêu Tộc", "Luyện Khí Đỉnh Phong", "Đội Trưởng Trinh Sát"),
        ("Ưng Bạch Vũ", "鹰白羽", "Sứ Giả", "Yêu Tộc", "Luyện Khí Hậu Kỳ", "Sứ Giả Giao Thương"),
        ("Ưng Tiểu Phong", "鹰小风", "Ấu Ưng", "Yêu Tộc", "Luyện Khí Sơ Kỳ", "Học Viên Ấu Ưng"),
    ],
}

# ---- 6. Băng Nguyên Tán Tu Hội (pop 500, Hạng Năm, Nhân Tộc) → Medium: 5-8 ----
factions["Băng_Nguyên_Tán_Tu_Hội"] = {
    "faction_name": "Băng Nguyên Tán Tu Hội",
    "characters": [
        ("Trần Hàn Phong", "陈寒风", "Hội Trưởng", "Nhân Tộc", "Kim Đan Sơ Kỳ", "Hội Trưởng"),
        ("Lý Tuyết Phong", "李雪峰", "Phó Hội Trưởng", "Nhân Tộc", "Trúc Cơ Viên Mãn", "Trưởng Trại Hàn Phong"),
        ("Hoàng Đại Sơn", "黄大山", "Trưởng Trại", "Nhân Tộc", "Trúc Cơ Hậu Kỳ", "Trưởng Trại Tuyết Thưa"),
        ("Vũ Thiên Hàn", "武天寒", "Trưởng Trại", "Nhân Tộc", "Trúc Cơ Trung Kỳ", "Trưởng Trại Đá Ngầm"),
        ("Phạm Lệ Nương", "范丽娘", "Trưởng Trại", "Nhân Tộc", "Trúc Cơ Sơ Kỳ", "Trưởng Trại Gió Hú"),
        ("Đặng Thiết Ngưu", "邓铁牛", "Trưởng Trại", "Nhân Tộc", "Trúc Cơ Sơ Kỳ", "Trưởng Trại Suối Lạnh"),
        ("Nguyễn Hàn Sương", "阮寒霜", "Quản Sự", "Nhân Tộc", "Luyện Khí Đỉnh Phong", "Quản Sự Sàn Giao Dịch"),
    ],
}

# ---- 7. Băng Nguyên Khai Hoang Đội (pop 12, Hạng Năm, Cự Tộc) → Small: 3-5 ----
factions["Băng_Nguyên_Khai_Hoang_Đội"] = {
    "faction_name": "Băng Nguyên Khai Hoang Đội",
    "characters": [
        ("Thạch Khai Sơn", "石开山", "Đội Trưởng", "Cự Tộc", "Trúc Cơ Viên Mãn", "Đội Trưởng"),
        ("Thạch Thiết Chùy", "石铁锤", "Uy Trấn", "Cự Tộc", "Trúc Cơ Sơ Kỳ", "Uy Trấn"),
        ("Nham Cự Lực", "岩巨力", "Chiến Binh", "Cự Tộc", "Luyện Khí Đỉnh Phong", "Tiên Phong"),
    ],
}

# ---- 8. Băng Ngục Đào Vong Giả (pop 47, Hạng Năm, Đa chủng tộc) → Medium: 5-8 ----
factions["Băng_Ngục_Đào_Vong_Giả"] = {
    "faction_name": "Băng Ngục Đào Vong Giả",
    "characters": [
        ("Mạc Vô Danh", "莫无名", "Minh Chủ", "Nhân Tộc", "Nguyên Anh Sơ Kỳ", "Minh Chủ"),
        ("Hắc Diện Nhân", "黑面人", "Phó Minh Chủ", "Nhân Tộc", "Kim Đan Hậu Kỳ", "Phó Minh Chủ"),
        ("Xà Ám Ảnh", "蛇暗影", "Trinh Sát", "Yêu Tộc", "Kim Đan Sơ Kỳ", "Trinh Sát Trưởng"),
        ("Thiết Toả Nhân", "铁锁人", "Chiến Binh", "Nhân Tộc", "Trúc Cơ Viên Mãn", "Đội Trưởng Chiến Đấu"),
        ("Lãnh Vô Tâm", "冷无心", "Sát Thủ", "Nhân Tộc", "Trúc Cơ Hậu Kỳ", "Ám Sát Thủ"),
        ("Cương Thạch Nữ", "钢石女", "Chiến Binh", "Cự Tộc", "Trúc Cơ Trung Kỳ", "Hộ Vệ"),
    ],
}

# ---- 9. Bán Cự Nhân Hội (pop 63, Hạng Năm, Hỗn Huyết) → Medium: 5-8 ----
factions["Bán_Cự_Nhân_Hội"] = {
    "faction_name": "Bán Cự Nhân Hội",
    "characters": [
        ("Thạch Bán Nhân", "石半人", "Hội Trưởng", "Hỗn huyết (Cự Tộc, Nhân Tộc)", "Trúc Cơ Trung Kỳ", "Hội Trưởng"),
        ("Sơn Đại Nham", "山大岩", "Đội Trưởng Vệ Binh", "Hỗn huyết (Cự Tộc, Nhân Tộc)", "Trúc Cơ Sơ Kỳ", "Đội Trưởng Vệ Binh"),
        ("Thạch Nhu Nhi", "石柔儿", "Quản Sự", "Hỗn huyết (Cự Tộc, Nhân Tộc)", "Luyện Khí Hậu Kỳ", "Quản Sự Chăn Nuôi"),
        ("Nham Thiết Bích", "岩铁臂", "Chiến Binh", "Hỗn huyết (Cự Tộc, Nhân Tộc)", "Luyện Khí Trung Kỳ", "Vệ Binh"),
        ("Lê Bán Sơn", "黎半山", "Trưởng Lão", "Hỗn huyết (Cự Tộc, Nhân Tộc)", "Trúc Cơ Sơ Kỳ", "Trưởng Lão Cố Vấn"),
    ],
}

# ---- 10. Bạch Hồ Ẩn Tộc (pop 43, Hạng Tư, Yêu Tộc Bạch Hồ) → Medium: 5-8 ----
factions["Bạch_Hồ_Ẩn_Tộc"] = {
    "faction_name": "Bạch Hồ Ẩn Tộc",
    "characters": [
        ("Hồ Bạch Liên", "狐白莲", "Tộc Trưởng", "Yêu Tộc", "Kim Đan Sơ Kỳ", "Tộc Trưởng"),
        ("Hồ Tuyết Nhi", "狐雪儿", "Trưởng Lão", "Yêu Tộc", "Trúc Cơ Viên Mãn", "Trưởng Lão"),
        ("Hồ Thanh Nguyệt", "狐青月", "Chiến Binh", "Yêu Tộc", "Trúc Cơ Hậu Kỳ", "Hộ Vệ Trưởng"),
        ("Hồ Ngọc Châu", "狐玉珠", "Thợ Lặn", "Yêu Tộc", "Trúc Cơ Sơ Kỳ", "Thợ Lặn Ngọc Trai"),
        ("Hồ Ẩn Phong", "狐隐风", "Giám Sát", "Yêu Tộc", "Trúc Cơ Trung Kỳ", "Giám Sát Yêu Khí"),
        ("Hồ Tiểu Bạch", "狐小白", "Đệ Tử", "Yêu Tộc", "Luyện Khí Trung Kỳ", "Đệ Tử Huyễn Thuật"),
    ],
}

# ---- 11. Bạch Cốt Hội (pop 64, Hạng Tư, Nhân Tộc) → Medium: 5-8 ----
factions["Bạch_Cốt_Hội"] = {
    "faction_name": "Bạch Cốt Hội",
    "characters": [
        ("Đoạn Vô Tình", "断无情", "Hội Chủ", "Nhân Tộc", "Kim Đan Trung Kỳ", "Hội Chủ"),
        ("Trần Cốt Lão", "陈骨老", "Đội Trưởng", "Nhân Tộc", "Trúc Cơ Viên Mãn", "Đội Trưởng Thu Nhặt"),
        ("Lý Hắc Thổ", "李黑土", "Nghệ Nhân", "Nhân Tộc", "Trúc Cơ Hậu Kỳ", "Nghệ Nhân Cốt Pháp"),
        ("Phạm U Linh", "范幽灵", "Trinh Sát", "Nhân Tộc", "Trúc Cơ Sơ Kỳ", "Trinh Sát Phế Tích"),
        ("Hoàng Mộ Dạ", "黄暮夜", "Giám Định Viên", "Nhân Tộc", "Trúc Cơ Trung Kỳ", "Giám Định Di Vật"),
        ("Đặng Tàn Cốt", "邓残骨", "Chiến Binh", "Nhân Tộc", "Luyện Khí Đỉnh Phong", "Hộ Vệ Hang Ổ"),
    ],
}

# ---- 12. Tuyết Cự Nhân Đảo (pop 300, Hạng Ba, Cự Tộc) → Large: 8-12 ----
factions["Tuyết_Cự_Nhân_Đảo"] = {
    "faction_name": "Tuyết Cự Nhân Đảo",
    "characters": [
        ("Tuyết Sơn", "雪山", "Trưởng Lão", "Cự Tộc", "Nguyên Anh Viên Mãn", "Lão Cự Nhân Trưởng Lão"),
        ("Tuyết Nham Cốt", "雪岩骨", "Tướng Quân", "Cự Tộc", "Nguyên Anh Trung Kỳ", "Thống Lĩnh Dũng Sĩ"),
        ("Tuyết Băng Nha", "雪冰牙", "Trưởng Lão", "Cự Tộc", "Nguyên Anh Sơ Kỳ", "Trưởng Lão Tuyết Vu Các"),
        ("Sơn Đại Địa", "山大地", "Chiến Binh", "Cự Tộc", "Kim Đan Hậu Kỳ", "Dũng Sĩ Ném Băng"),
        ("Thạch Vĩnh Đông", "石永冬", "Tuyết Vu", "Cự Tộc", "Kim Đan Trung Kỳ", "Tuyết Vu"),
        ("Nham Cương Thể", "岩刚体", "Chiến Binh", "Cự Tộc", "Kim Đan Sơ Kỳ", "Dũng Sĩ Phòng Thủ"),
        ("Tuyết Nhu Sương", "雪柔霜", "Tuyết Vu", "Cự Tộc", "Kim Đan Sơ Kỳ", "Tuyết Vu Chữa Thương"),
        ("Sơn Thiết Quyền", "山铁拳", "Chiến Binh", "Cự Tộc", "Trúc Cơ Viên Mãn", "Chiến Binh Tuần Tra"),
        ("Tuyết Tiểu Phong", "雪小峰", "Ấu Cự Nhân", "Cự Tộc", "Trúc Cơ Sơ Kỳ", "Học Đồ Tuyết Vu"),
    ],
}

# ---- 13. Thiên Sơn Đông Cốc (pop 5000, Hạng Nhì, Nhân Tộc + Yêu Tộc) → Large: 8-12 ----
factions["Thiên_Sơn_Đông_Cốc"] = {
    "faction_name": "Thiên Sơn Đông Cốc",
    "characters": [
        ("Hàn Đan", "寒丹", "Cốc Chủ", "Nhân Tộc", "Hóa Thần Sơ Kỳ", "Cốc Chủ"),
        ("Lý Băng Diễm", "李冰焰", "Viện Chủ", "Nhân Tộc", "Nguyên Anh Hậu Kỳ", "Viện Chủ Lửa Lạnh Viện"),
        ("Trần Tuyết Liên", "陈雪莲", "Đội Trưởng", "Nhân Tộc", "Kim Đan Viên Mãn", "Đội Trưởng Hái Thuốc"),
        ("Phạm Hàn Ngọc", "范寒玉", "Đan Sư", "Nhân Tộc", "Nguyên Anh Sơ Kỳ", "Trưởng Lão Đan Sư"),
        ("Hoàng Đông Tuyền", "黄冬泉", "Trưởng Lão", "Nhân Tộc", "Nguyên Anh Sơ Kỳ", "Trưởng Lão Trường Sinh Viện"),
        ("Miêu Tuyết Ngọc", "猫雪玉", "Dược Sư", "Yêu Tộc", "Kim Đan Hậu Kỳ", "Dược Sư Thú Bạn"),
        ("Lê Hàn Sương", "黎寒霜", "Chân Truyền", "Nhân Tộc", "Kim Đan Trung Kỳ", "Chân Truyền Đệ Tử"),
        ("Nguyễn Băng Tâm", "阮冰心", "Chân Truyền", "Nhân Tộc", "Kim Đan Sơ Kỳ", "Chân Truyền Đệ Tử"),
        ("Thỏ Linh Nhi", "兔灵儿", "Hái Thuốc", "Yêu Tộc", "Trúc Cơ Viên Mãn", "Thợ Hái Tuyết Liên"),
        ("Đặng Tiểu Hàn", "邓小寒", "Nội Môn", "Nhân Tộc", "Trúc Cơ Hậu Kỳ", "Nội Môn Đệ Tử"),
    ],
}

# ---- 14. Sương Ma Uyển (pop 8000, Hạng Nhì, Băng Tộc/Ma Tộc) → Large: 8-12 ----
factions["Sương_Ma_Uyển"] = {
    "faction_name": "Sương Ma Uyển",
    "characters": [
        ("Sương Vô Tình", "霜无情", "Cốc Chủ", "Băng Tộc", "Hóa Thần Trung Kỳ", "Sương Ma Cốc Chủ"),
        ("Hắc Sương Quỷ", "黑霜鬼", "Hộ Pháp", "Băng Tộc", "Nguyên Anh Hậu Kỳ", "Đệ Nhất Sát Sương Quỷ"),
        ("Bạch Thi Nương", "白尸娘", "Đường Chủ", "Ma Tộc", "Kim Đan Viên Mãn", "Đường Chủ Băng Thi Đội"),
        ("Huyết Băng Tử", "血冰子", "Hộ Pháp", "Băng Tộc", "Nguyên Anh Sơ Kỳ", "Đệ Nhị Sát Sương Quỷ"),
        ("Ám Sương Ảnh", "暗霜影", "Sát Thủ", "Băng Tộc", "Nguyên Anh Sơ Kỳ", "Đệ Tam Sát Sương Quỷ"),
        ("Lãnh Vô Hồn", "冷无魂", "Ma Tu", "Ma Tộc", "Kim Đan Hậu Kỳ", "Luyện Tà Đường Chủ"),
        ("Hàn Độc Cốt", "寒毒骨", "Ma Tu", "Băng Tộc", "Kim Đan Trung Kỳ", "Hộ Pháp"),
        ("Sương Nô Vương", "霜奴王", "Băng Nô Thủ Lĩnh", "Băng Tộc", "Kim Đan Sơ Kỳ", "Thống Lĩnh Băng Nô"),
        ("Tuyệt Tình Hàn", "绝情寒", "Chân Truyền", "Băng Tộc", "Trúc Cơ Viên Mãn", "Chân Truyền Ma Đồ"),
        ("Ám Băng Nhi", "暗冰儿", "Nội Môn", "Băng Tộc", "Trúc Cơ Hậu Kỳ", "Nội Môn Ma Đồ"),
    ],
}

# ---- 15. Phiêu Miễu Băng Hải (pop 2000, Hạng Nhì, Nhân Tộc Nữ + Hải Yêu) → Large: 8-12 ----
factions["Phiêu_Miễu_Băng_Hải"] = {
    "faction_name": "Phiêu Miễu Băng Hải",
    "characters": [
        ("Hải Cung", "海宫", "Cung Chủ", "Nhân Tộc", "Hóa Thần Sơ Kỳ", "Cung Chủ"),
        ("Thủy Nguyệt Tiên", "水月仙", "Viện Chủ", "Nhân Tộc", "Nguyên Anh Hậu Kỳ", "Viện Chủ Ảo Vũ Viện"),
        ("Mộng Hàn Yên", "梦寒烟", "Đường Chủ", "Nhân Tộc", "Nguyên Anh Sơ Kỳ", "Đường Chủ Tâm Trí Đường"),
        ("Lam Tịnh Thủy", "蓝净水", "Trưởng Lão", "Hải Yêu", "Nguyên Anh Sơ Kỳ", "Trưởng Lão Thủy Hoa Viện"),
        ("Sương Vũ Nữ", "霜舞女", "Chân Truyền", "Nhân Tộc", "Kim Đan Hậu Kỳ", "Chân Truyền Vũ Nữ"),
        ("Băng San Hô", "冰珊瑚", "Dược Sư", "Hải Yêu", "Kim Đan Trung Kỳ", "Dược Sư Biển Băng"),
        ("Hàn Thanh Âm", "寒清音", "Nhạc Sư", "Nhân Tộc", "Kim Đan Sơ Kỳ", "Nhạc Sư Huyễn Âm"),
        ("Nguyệt Ảnh Hồ", "月影湖", "Chân Truyền", "Nhân Tộc", "Trúc Cơ Viên Mãn", "Chân Truyền Đệ Tử"),
        ("Thủy Linh Nhi", "水灵儿", "Nội Môn", "Hải Yêu", "Trúc Cơ Hậu Kỳ", "Nội Môn Đệ Tử"),
    ],
}

# ---- 16. Hàn Kiếm Cốc (pop 3000, Hạng Nhì, Nhân Tộc) → Large: 8-12 ----
factions["Hàn_Kiếm_Cốc"] = {
    "faction_name": "Hàn Kiếm Cốc",
    "characters": [
        ("Hàn Tiêu", "寒萧", "Cốc Chủ", "Nhân Tộc", "Nguyên Anh Viên Mãn", "Cốc Chủ"),
        ("Lý Băng Kiếm", "李冰剑", "Viện Chủ", "Nhân Tộc", "Nguyên Anh Hậu Kỳ", "Viện Chủ Chân Ngôn Kiếm Viện"),
        ("Trần Tuyết Phong", "陈雪锋", "Hộ Pháp", "Nhân Tộc", "Nguyên Anh Sơ Kỳ", "Hộ Pháp Khổ Tu Đoàn"),
        ("Phương Hàn Sương", "方寒霜", "Trưởng Lão", "Nhân Tộc", "Nguyên Anh Sơ Kỳ", "Trưởng Lão Kiếm Đạo"),
        ("Hoàng Đoạn Tuyết", "黄断雪", "Trưởng Lão", "Nhân Tộc", "Kim Đan Viên Mãn", "Trưởng Lão Tiếp Tế Viện"),
        ("Vũ Hàn Thiết", "武寒铁", "Chân Truyền", "Nhân Tộc", "Kim Đan Hậu Kỳ", "Chân Truyền Đệ Tử"),
        ("Lê Kiếm Tâm", "黎剑心", "Chân Truyền", "Nhân Tộc", "Kim Đan Trung Kỳ", "Chân Truyền Đệ Tử"),
        ("Nguyễn Phá Tuyết", "阮破雪", "Nội Môn", "Nhân Tộc", "Kim Đan Sơ Kỳ", "Nội Môn Đệ Tử"),
        ("Đặng Hàn Phong", "邓寒风", "Nội Môn", "Nhân Tộc", "Trúc Cơ Viên Mãn", "Nội Môn Đệ Tử"),
        ("Trần Tiểu Kiếm", "陈小剑", "Ngoại Môn", "Nhân Tộc", "Trúc Cơ Sơ Kỳ", "Ngoại Môn Đệ Tử"),
    ],
}

# ---- 17. Cực Quang Thần Điện (pop 10000, Hạng Nhì tiềm lực Nhất, Băng Tộc) → Large: 8-12 ----
factions["Cực_Quang_Thần_Điện"] = {
    "faction_name": "Cực Quang Thần Điện",
    "characters": [
        ("Cực Quang Thánh Nữ", "极光圣女", "Thánh Nữ", "Băng Tộc", "Hóa Thần Hậu Kỳ", "Thánh Nữ Lãnh Đạo"),
        ("Quang Minh Đại Tế", "光明大祭", "Đại Tế Tư", "Băng Tộc", "Nguyên Anh Viên Mãn", "Đại Tế Tư Ánh Sáng"),
        ("Băng Lăng Tướng Quân", "冰棱将军", "Tướng Quân", "Băng Tộc", "Nguyên Anh Hậu Kỳ", "Thống Lĩnh Hiệp Sĩ Băng Lăng"),
        ("Quang Hàn Chấp Sự", "光寒执事", "Chấp Sự", "Băng Tộc", "Nguyên Anh Trung Kỳ", "Phó Viện Chủ Tế Tư Viện"),
        ("Thánh Quang Linh", "圣光灵", "Linh Mục", "Băng Tộc", "Nguyên Anh Sơ Kỳ", "Đại Linh Mục"),
        ("Băng Lăng Vệ", "冰棱卫", "Hiệp Sĩ", "Băng Tộc", "Kim Đan Viên Mãn", "Hiệp Sĩ Băng Lăng Trưởng"),
        ("Quang Ảnh Tử", "光影子", "Mật Thám", "Băng Tộc", "Kim Đan Hậu Kỳ", "Thủ Lĩnh Chấp Đạo Đội"),
        ("Băng Tịnh Liên", "冰净莲", "Nữ Tế", "Băng Tộc", "Kim Đan Trung Kỳ", "Nữ Tế Tư"),
        ("Hàn Quang Kiếm", "寒光剑", "Hiệp Sĩ", "Băng Tộc", "Kim Đan Sơ Kỳ", "Hiệp Sĩ Băng Lăng"),
        ("Cực Quang Đồng Tử", "极光童子", "Đồng Tử", "Băng Tộc", "Trúc Cơ Viên Mãn", "Thị Vệ Thánh Nữ"),
    ],
}

# ---- 18. Băng Ngục Thành (pop 200000, Hạng Nhì, Đa chủng tộc) → Large: 8-12 ----
factions["Băng_Ngục_Thành"] = {
    "faction_name": "Băng Ngục Thành",
    "characters": [
        ("Ngục Vô Tình", "狱无情", "Thành Chủ", "Nhân Tộc", "Hóa Thần Sơ Kỳ", "Ngục Trưởng"),
        ("Hắc Giáp Thống Lĩnh", "黑甲统领", "Tướng Quân", "Nhân Tộc", "Nguyên Anh Hậu Kỳ", "Thống Lĩnh Hắc Giáp"),
        ("Độc Vương Lão Ngũ", "毒王老五", "Tù Trưởng", "Nhân Tộc", "Nguyên Anh Trung Kỳ", "Thủ Lĩnh Tầng Một"),
        ("Huyết Đồ Tàn Phong", "血屠残风", "Tù Trưởng", "Yêu Tộc", "Nguyên Anh Sơ Kỳ", "Thủ Lĩnh Tầng Hai"),
        ("Thiết Quyền Lão Ma", "铁拳老魔", "Tù Trưởng", "Nhân Tộc", "Nguyên Anh Sơ Kỳ", "Thủ Lĩnh Tầng Ba"),
        ("Băng Cốt Yêu Nữ", "冰骨妖女", "Tù Trưởng", "Yêu Tộc", "Kim Đan Viên Mãn", "Thủ Lĩnh Tầng Bốn"),
        ("Lý Tham Quan", "李贪官", "Cai Ngục", "Nhân Tộc", "Kim Đan Hậu Kỳ", "Phó Ngục Trưởng"),
        ("Trần Hắc Tâm", "陈黑心", "Cai Ngục", "Nhân Tộc", "Kim Đan Trung Kỳ", "Cai Ngục Trưởng Tầng Một"),
        ("Vương Đấu Trường", "王斗场", "Quản Lý", "Nhân Tộc", "Kim Đan Sơ Kỳ", "Quản Lý Đấu Trường Máu"),
        ("Mạc Lão Bà", "莫老婆", "Tù Nhân Cổ", "Nhân Tộc", "Luyện Hư Sơ Kỳ", "Tù Nhân Tầng Bốn"),
    ],
}

# ---- 19. Đại Địa Hành Giả (pop ~10, Hạng Tư, Cự Tộc) → Small: 3-5 ----
factions["Đại_Địa_Hành_Giả"] = {
    "faction_name": "Đại Địa Hành Giả",
    "characters": [
        ("Địa Tâm", "地心", "Hành Giả Trưởng", "Cự Tộc", "Kim Đan Sơ Kỳ", "Hành Giả Trưởng"),
        ("Nham Thâm Căn", "岩深根", "Hành Giả", "Cự Tộc", "Trúc Cơ Viên Mãn", "Hành Giả"),
        ("Thạch Mạch Nhi", "石脉儿", "Học Đồ", "Cự Tộc", "Luyện Khí Hậu Kỳ", "Học Đồ"),
    ],
}

# ---- 20. Yêu Thú Đông Miên Hội (pop ~35, Hạng Năm, Yêu Tộc) → Small: 3-5 ----
factions["Yêu_Thú_Đông_Miên_Hội"] = {
    "faction_name": "Yêu Thú Đông Miên Hội",
    "characters": [
        ("Hùng Đông", "熊冬", "Hội Trưởng", "Yêu Tộc", "Trúc Cơ Sơ Kỳ", "Hội Trưởng"),
        ("Xà Hàn Thân", "蛇寒身", "Canh Gác", "Yêu Tộc", "Luyện Khí Hậu Kỳ", "Đội Trưởng Canh Gác"),
        ("Thỏ Nhung Bạch", "兔绒白", "Thành Viên", "Yêu Tộc", "Luyện Khí Trung Kỳ", "Quản Kho Thực Phẩm"),
        ("Nhím Khoai Nhi", "刺球儿", "Thành Viên", "Yêu Tộc", "Luyện Khí Sơ Kỳ", "Canh Gác"),
    ],
}

# ---- 21. Tuyết Trung Cô Viện (pop ~80, Hạng Năm, Nhân Tộc) → Small: 3-5 ----
factions["Tuyết_Trung_Cô_Viện"] = {
    "faction_name": "Tuyết Trung Cô Viện",
    "characters": [
        ("Lý Mộ Tuyết", "李慕雪", "Viện Trưởng", "Nhân Tộc", "Kim Đan Trung Kỳ", "Viện Trưởng"),
        ("Trần Nhu Tâm", "陈柔心", "Quản Sự", "Nhân Tộc", "Trúc Cơ Trung Kỳ", "Quản Sự Nấu Ăn"),
        ("Phạm Thư Sinh", "范书生", "Quản Sự", "Nhân Tộc", "Trúc Cơ Sơ Kỳ", "Quản Sự Dạy Chữ"),
        ("Lê Dược Nương", "黎药娘", "Quản Sự", "Nhân Tộc", "Trúc Cơ Sơ Kỳ", "Quản Sự Chữa Bệnh"),
    ],
}

# ---- 22. Tuyết Liên Dược Phường (pop ~30, Hạng Năm, Nhân Tộc) → Small: 3-5 ----
factions["Tuyết_Liên_Dược_Phường"] = {
    "faction_name": "Tuyết Liên Dược Phường",
    "characters": [
        ("Liên Tuyết Nhi", "莲雪儿", "Phường Chủ", "Nhân Tộc", "Trúc Cơ Hậu Kỳ", "Phường Chủ"),
        ("Hoàng Dược Sư", "黄药师", "Dược Sư", "Nhân Tộc", "Luyện Khí Đỉnh Phong", "Dược Sư Trưởng"),
        ("Trần Sơn Nhi", "陈山儿", "Hái Dược", "Nhân Tộc", "Luyện Khí Trung Kỳ", "Trưởng Nhóm Hái Dược"),
        ("Lý Tiểu Liên", "李小莲", "Dược Sư", "Nhân Tộc", "Luyện Khí Sơ Kỳ", "Dược Sư Học Việc"),
    ],
}

# ---- 23. Tuyết Cự Nhân Lạc Đoàn (pop ~25, Hạng Năm, Cự Tộc) → Small: 3-5 ----
factions["Tuyết_Cự_Nhân_Lạc_Đoàn"] = {
    "faction_name": "Tuyết Cự Nhân Lạc Đoàn",
    "characters": [
        ("Thạch Tiểu Sơn", "石小山", "Đoàn Trưởng", "Cự Tộc", "Trúc Cơ Viên Mãn", "Đoàn Trưởng"),
        ("Nham Bán Thân", "岩半身", "Phó Đoàn", "Cự Tộc", "Trúc Cơ Sơ Kỳ", "Phó Đoàn Trưởng"),
        ("Thạch Nói Đá", "石语石", "Đặc Biệt", "Cự Tộc", "Luyện Khí Hậu Kỳ", "Cự Tộc Trẻ Thạch Linh"),
        ("Sơn Tiểu Nhi", "山小儿", "Ấu Cự Nhân", "Cự Tộc", "Luyện Khí Sơ Kỳ", "Ấu Cự Nhân"),
    ],
}

# ---- 24. Phá Băng Thương Đội (pop ~50, Hạng Năm, Nhân Tộc) → Medium: 5-8 ----
factions["Phá_Băng_Thương_Đội"] = {
    "faction_name": "Phá Băng Thương Đội",
    "characters": [
        ("Châu Phá Thiên", "周破天", "Đội Trưởng", "Nhân Tộc", "Trúc Cơ Viên Mãn", "Đội Trưởng"),
        ("Lý Thiết Kế", "李铁计", "Phó Đội", "Nhân Tộc", "Trúc Cơ Trung Kỳ", "Phó Đội Trưởng"),
        ("Nguyễn Đại Xa", "阮大车", "Phu Khuân Vác", "Nhân Tộc", "Phàm Nhân", "Trưởng Nhóm Khuân Vác"),
        ("Đặng Hỏa Nhi", "邓火儿", "Hộ Vệ", "Nhân Tộc", "Luyện Khí Hậu Kỳ", "Hộ Vệ Trưởng"),
        ("Phạm Linh Kế", "范灵计", "Kế Toán", "Nhân Tộc", "Luyện Khí Sơ Kỳ", "Quản Lý Tài Vụ"),
    ],
}

# ---- 25. Phong Vũ Trinh Sát Đội (pop ~14, Hạng Năm, Vũ Tộc) → Small: 3-5 ----
factions["Phong_Vũ_Trinh_Sát_Đội"] = {
    "faction_name": "Phong Vũ Trinh Sát Đội",
    "characters": [
        ("Vũ Tiểu Vũ", "羽小雨", "Đội Trưởng", "Vũ Tộc", "Luyện Khí Hậu Kỳ", "Đội Trưởng"),
        ("Vũ Thanh Phong", "羽清风", "Phó Đội", "Vũ Tộc", "Luyện Khí Trung Kỳ", "Phó Đội Trưởng"),
        ("Vũ Nhạn Nhi", "羽雁儿", "Trinh Sát", "Vũ Tộc", "Luyện Khí Sơ Kỳ", "Trinh Sát Viên"),
        ("Vũ Lão Cốt", "羽老骨", "Cố Vấn", "Vũ Tộc", "Trúc Cơ Sơ Kỳ", "Cố Vấn Khí Tượng"),
    ],
}

# ---- 26. Lưu Vong Kiếm Khách Đoàn (pop ~20, Hạng Tư, Nhân Tộc) → Medium: 5-8 ----
factions["Lưu_Vong_Kiếm_Khách_Đoàn"] = {
    "faction_name": "Lưu Vong Kiếm Khách Đoàn",
    "characters": [
        ("Phương Hàn", "方寒", "Đoàn Trưởng", "Nhân Tộc", "Kim Đan Sơ Kỳ", "Đoàn Trưởng"),
        ("Lý Tàn Kiếm", "李残剑", "Phó Đoàn", "Nhân Tộc", "Trúc Cơ Viên Mãn", "Phó Đoàn Trưởng"),
        ("Trần Đoạn Phong", "陈断锋", "Kiếm Khách", "Nhân Tộc", "Trúc Cơ Hậu Kỳ", "Kiếm Khách"),
        ("Hoàng Vô Niệm", "黄无念", "Kiếm Khách", "Nhân Tộc", "Trúc Cơ Trung Kỳ", "Kiếm Khách"),
        ("Vũ Hàn Kiếm", "武寒剑", "Kiếm Khách", "Nhân Tộc", "Trúc Cơ Sơ Kỳ", "Kiếm Khách"),
        ("Nguyễn Tiểu Phong", "阮小锋", "Tân Nhân", "Nhân Tộc", "Luyện Khí Đỉnh Phong", "Tân Nhân"),
    ],
}

# ============================================================
# Generate files
# ============================================================
total = 0
for dir_name, info in factions.items():
    faction_dir = os.path.join(CHAR_DIR, dir_name)
    os.makedirs(faction_dir, exist_ok=True)

    for char in info["characters"]:
        name, hantu, archetype, race, cultivation, role = char
        filename = name.replace(" ", "_") + ".md"
        filepath = os.path.join(faction_dir, filename)

        content = make_char(name, hantu, archetype, race, cultivation, info["faction_name"], role)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        total += 1
        print(f"  Created: {filepath}")

print(f"\n{'='*60}")
print(f"Total character files created: {total}")
print(f"Total factions populated: {len(factions)}")
