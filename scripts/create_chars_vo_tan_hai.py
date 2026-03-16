#!/usr/bin/env python3
"""
Create character files for all Vô Tận Hải factions that currently have NO characters.
Ma_Đạo_Minh (Trung Tâm -> Thiên Trụ) was checked and already has characters as Cửu_U_Ma_Tông.
"""
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NHAN_VAT_VTH = os.path.join(BASE, "Đạo", "Nhân_Vật", "Vô_Tận_Hải")


def make_char_content(name, hantu, archetype, race, cultivation, region, faction, chuc_vu):
    name_upper = name.upper()
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

# HỒ SƠ NHÂN VẬT: {name_upper} ({hantu})

## I. THÔNG TIN CƠ BẢN
- **Họ Tên:** {name} ({hantu}).
- **Chủng Tộc:** {race}.
- **Tu Vi:** {cultivation}.
- **Khu Vực:** {region}.
- **Thế Lực:** {faction}.
- **Chức Vụ:** {chuc_vu}.

## II. NGOẠI HÌNH & TÍNH CÁCH
*(Chưa xác định)*

## III. NĂNG LỰC & CHIẾN ĐẤU
*(Chưa xác định)*

## IV. CÁC MỐI QUAN HỆ
*(Chưa xác định)*

## V. TIỂU SỬ & HÀNH TRÌNH
*(Chưa xác định)*
"""


# ── Faction definitions ──────────────────────────────────────────────
# Each faction: (folder_name, faction_display, region, characters_list)
# characters_list: [(name, hantu, archetype, race, cultivation, chuc_vu), ...]

FACTIONS = []

# ═══════════════════════════════════════════════════════════════════════
# 1. Ấu Long Học Viện — pop 21, Hạng Năm, small → 3-5 chars
# ═══════════════════════════════════════════════════════════════════════
FACTIONS.append(("Ấu_Long_Học_Viện", "Ấu Long Học Viện", "Vô Tận Hải", [
    ("Lam Nguyệt", "蓝月", "Bảo Mẫu Trưởng", "Long Tộc", "Trúc Cơ Viên Mãn", "Viện Trưởng / Bảo Mẫu Trưởng"),
    ("Long Vân Nhi", "龙云儿", "Giáo Sư", "Long Tộc", "Trúc Cơ Sơ Kỳ", "Giáo Sư Giao Long"),
    ("Ngao Tiểu Lôi", "鳌小雷", "Trợ Giảng", "Long Tộc", "Luyện Khí Đỉnh Phong", "Trợ Giảng"),
    ("Long Ngọc", "龙玉", "Học Viên", "Long Tộc", "Luyện Khí Sơ Kỳ", "Ấu Long Học Viên"),
]))

# ═══════════════════════════════════════════════════════════════════════
# 2. Cự Kình Bảo — pop 5000, Hạng Nhì, large → 8-12 chars
# ═══════════════════════════════════════════════════════════════════════
FACTIONS.append(("Cự_Kình_Bảo", "Cự Kình Bảo", "Vô Tận Hải", [
    ("Kình Thiên", "鲸天", "Thành Chủ", "Nhân Tộc", "Nguyên Anh Viên Mãn", "Thành Chủ"),
    ("Kình Hải Vân", "鲸海云", "Phó Thành Chủ", "Nhân Tộc", "Nguyên Anh Sơ Kỳ", "Phó Thành Chủ"),
    ("Ba Thiết Phong", "波铁锋", "Thống Lĩnh", "Hải Tộc", "Nguyên Anh Sơ Kỳ", "Thống Lĩnh Kình Vệ Quân"),
    ("Triều Ngọc Hà", "潮玉荷", "Đại Chưởng Quỹ", "Nhân Tộc", "Kim Đan Hậu Kỳ", "Quản Sự Giao Thương Viện"),
    ("Hải Đại Mộc", "海大木", "Kỹ Sư", "Nhân Tộc", "Kim Đan Trung Kỳ", "Kỹ Sư Trưởng Hậu Mãnh Viện"),
    ("Thủy Bạch Liên", "水白莲", "Dược Sư", "Hải Tộc", "Kim Đan Sơ Kỳ", "Dược Sư"),
    ("Kình Tiểu Ngư", "鲸小鱼", "Vệ Binh", "Nhân Tộc", "Trúc Cơ Viên Mãn", "Đội Trưởng Vệ Binh"),
    ("Lang Hải Phong", "浪海枫", "Thương Nhân", "Nhân Tộc", "Trúc Cơ Hậu Kỳ", "Chưởng Quầy Đấu Giá"),
    ("Ba Tiểu Vũ", "波小雨", "Hướng Đạo", "Hải Tộc", "Trúc Cơ Trung Kỳ", "Hướng Đạo Sư Hải Lưu"),
    ("Kình Lão Ngư", "鲸老渔", "Trưởng Lão", "Nhân Tộc", "Nguyên Anh Sơ Kỳ", "Trưởng Lão Hội Đồng"),
]))

# ═══════════════════════════════════════════════════════════════════════
# 3. Đảo Quốc Tự Trị Hội — pop ~300, Hạng Năm, small → 3-5 chars
# ═══════════════════════════════════════════════════════════════════════
FACTIONS.append(("Đảo_Quốc_Tự_Trị_Hội", "Đảo Quốc Tự Trị Hội", "Vô Tận Hải", [
    ("Phạm Dân Chủ", "范民主", "Hội Trưởng", "Nhân Tộc", "Trúc Cơ Viên Mãn", "Hội Trưởng"),
    ("Phạm Hải Thanh", "范海清", "Phó Hội Trưởng", "Nhân Tộc", "Trúc Cơ Sơ Kỳ", "Phó Hội Trưởng / Đại Diện Đảo"),
    ("Lê Tĩnh Ngư", "黎静渔", "Dân Binh Trưởng", "Nhân Tộc", "Luyện Khí Đỉnh Phong", "Dân Binh Trưởng"),
    ("Nguyễn Hải Nông", "阮海农", "Nông Dân", "Nhân Tộc", "Luyện Khí Trung Kỳ", "Trưởng Thôn Đảo Phía Nam"),
]))

# ═══════════════════════════════════════════════════════════════════════
# 4. Giao Nhân Tộc Liên Minh — pop 3000, Hạng Ba, medium-large → 8 chars
# ═══════════════════════════════════════════════════════════════════════
FACTIONS.append(("Giao_Nhân_Tộc_Liên_Minh", "Giao Nhân Tộc Liên Minh", "Vô Tận Hải", [
    ("Lệ Cơ", "泪姬", "Minh Chủ", "Hải Tộc (Giao Nhân)", "Nguyên Anh Sơ Kỳ", "Minh Chủ"),
    ("Lệ Vân Trường", "泪云长", "Phó Minh Chủ", "Hải Tộc (Giao Nhân)", "Kim Đan Đỉnh Phong", "Phó Minh Chủ"),
    ("Ba Nguyệt Hà", "波月荷", "Viện Chủ", "Hải Tộc (Giao Nhân)", "Kim Đan Viên Mãn", "Viện Chủ Vân Khâu Viện"),
    ("Thủy Lan Nhi", "水兰儿", "Tướng Quân", "Hải Tộc (Giao Nhân)", "Kim Đan Đỉnh Phong", "Tướng Quân Hải Ba Vệ"),
    ("Ba Thiên Lệ", "波千泪", "Trưởng Lão", "Hải Tộc (Giao Nhân)", "Kim Đan Hậu Kỳ", "Trưởng Lão"),
    ("Hải Minh Châu", "海明珠", "Nghệ Nhân", "Hải Tộc (Giao Nhân)", "Kim Đan Sơ Kỳ", "Đại Sư Dệt Lụa Vân"),
    ("Triều Tiểu Ca", "潮小歌", "Sứ Giả", "Hải Tộc (Giao Nhân)", "Trúc Cơ Viên Mãn", "Sứ Giả Giao Thương"),
    ("Ba Ngọc Hàn", "波玉寒", "Chiến Binh", "Hải Tộc (Giao Nhân)", "Trúc Cơ Hậu Kỳ", "Đội Trưởng Hải Ba Vệ"),
]))

# ═══════════════════════════════════════════════════════════════════════
# 5. Lục Mãng Hạ Tộc — pop ~80, Hạng Năm, small → 4 chars
# ═══════════════════════════════════════════════════════════════════════
FACTIONS.append(("Lục_Mãng_Hạ_Tộc", "Lục Mãng Hạ Tộc", "Vô Tận Hải", [
    ("Thanh Lân", "青鳞", "Tộc Trưởng", "Yêu Tộc (Xà Tộc)", "Trúc Cơ Hậu Kỳ", "Tộc Trưởng"),
    ("Hắc Vĩ", "黑尾", "Phó Tộc Trưởng", "Yêu Tộc (Xà Tộc)", "Trúc Cơ Sơ Kỳ", "Phó Tộc Trưởng / Hình Phạt"),
    ("Xà Bạch Linh", "蛇白灵", "Bạch Xà", "Yêu Tộc (Xà Tộc)", "Luyện Khí Đỉnh Phong", "Thành Viên (Bí Mật)"),
    ("Thanh Vĩ Nhi", "青尾儿", "Chiến Sĩ", "Yêu Tộc (Xà Tộc)", "Luyện Khí Hậu Kỳ", "Đội Trưởng Tuần Tra"),
]))

# ═══════════════════════════════════════════════════════════════════════
# 6. Ngư Dân Tu Luyện Hội — pop ~200, unranked, small → 4 chars
# ═══════════════════════════════════════════════════════════════════════
FACTIONS.append(("Ngư_Dân_Tu_Luyện_Hội", "Ngư Dân Tu Luyện Hội", "Vô Tận Hải", [
    ("Lý Đại Hải", "李大海", "Lão Ngư Ông", "Nhân Tộc", "Luyện Khí Đỉnh Phong", "Hội Trưởng / Lão Ngư Ông"),
    ("Lý Tiểu Ba", "李小波", "Ngư Đội Trưởng", "Nhân Tộc", "Luyện Khí Trung Kỳ", "Ngư Đội Trưởng"),
    ("Trần Hải Yến", "陈海燕", "Ngư Dân", "Nhân Tộc", "Luyện Khí Tam Tầng", "Ngư Dân / Đệ Tử Trẻ"),
    ("Lý Vạn Triều", "李万潮", "Trưởng Thôn", "Nhân Tộc", "Luyện Khí Sơ Kỳ", "Phó Hội Trưởng"),
]))

# ═══════════════════════════════════════════════════════════════════════
# 7. Phản Loạn Long Tử — pop ~12, unranked/secret, small → 4 chars
# ═══════════════════════════════════════════════════════════════════════
FACTIONS.append(("Phản_Loạn_Long_Tử", "Phản Loạn Long Tử", "Vô Tận Hải", [
    ("Long Hắc Dạ", "龙黑夜", "Thủ Lĩnh", "Long Tộc", "Nguyên Anh Sơ Kỳ", "Thủ Lĩnh / Hắc Long"),
    ("Long Tử Vân", "龙紫云", "Phó Thủ Lĩnh", "Long Tộc", "Kim Đan Hậu Kỳ", "Phó Thủ Lĩnh"),
    ("Long Ngọc Hàn", "龙玉寒", "Phó Thủ Lĩnh", "Long Tộc", "Kim Đan Hậu Kỳ", "Phó Thủ Lĩnh"),
    ("Long Thanh Phong", "龙青风", "Thành Viên", "Long Tộc", "Kim Đan Trung Kỳ", "Liên Lạc Viên"),
]))

# ═══════════════════════════════════════════════════════════════════════
# 8. Phiêu Lưu Đảo Liên Minh — pop ~500, Hạng Năm, small → 5 chars
# ═══════════════════════════════════════════════════════════════════════
FACTIONS.append(("Phiêu_Lưu_Đảo_Liên_Minh", "Phiêu Lưu Đảo Liên Minh", "Vô Tận Hải", [
    ("Trần Hải Phong", "陈海风", "Tổng Đảo Chủ", "Nhân Tộc", "Kim Đan Sơ Kỳ", "Tổng Đảo Chủ"),
    ("Lê Bạch Ngư", "黎白鱼", "Đảo Chủ", "Nhân Tộc", "Trúc Cơ Viên Mãn", "Đảo Chủ Đảo Số Ba"),
    ("Hoàng Hải Triều", "黄海潮", "Đội Trưởng", "Nhân Tộc", "Trúc Cơ Hậu Kỳ", "Đội Trưởng Hải Tuần Đội"),
    ("Phạm Sóng", "范浪", "Thuyền Trưởng", "Nhân Tộc", "Trúc Cơ Sơ Kỳ", "Thuyền Trưởng Thương Thuyền"),
    ("Trần Tiểu Đăng", "陈小灯", "Ngư Dân", "Nhân Tộc", "Luyện Khí Hậu Kỳ", "Đại Diện Đảo Thứ Mười Ba"),
]))

# ═══════════════════════════════════════════════════════════════════════
# 9. Phong Bạo Thương Đội — pop 3000, Hạng Nhì, large → 8-10 chars
# ═══════════════════════════════════════════════════════════════════════
FACTIONS.append(("Phong_Bạo_Thương_Đội", "Phong Bạo Thương Đội", "Vô Tận Hải", [
    ("Hải Phong", "海风", "Tổng Quản", "Nhân Tộc", "Nguyên Anh Trung Kỳ", "Tổng Quản"),
    ("Lôi Vạn Lý", "雷万里", "Hạm Đội Trưởng", "Nhân Tộc", "Nguyên Anh Sơ Kỳ", "Hạm Đội Trưởng"),
    ("Phong Thiết Nha", "风铁牙", "Hộ Pháp", "Nhân Tộc", "Nguyên Anh Trung Kỳ", "Hộ Pháp Phong Lôi Hộ Vệ"),
    ("Vân Hải Đồ", "云海图", "Hướng Đạo Sư", "Nhân Tộc", "Kim Đan Viên Mãn", "Hướng Đạo Sư Trưởng"),
    ("Đặng Thương Hà", "邓商荷", "Thương Nhân", "Nhân Tộc", "Kim Đan Hậu Kỳ", "Đại Chưởng Quỹ"),
    ("Lôi Tiểu Vũ", "雷小雨", "Thuyền Trưởng", "Nhân Tộc", "Kim Đan Sơ Kỳ", "Thuyền Trưởng Kỳ Hạm"),
    ("Phong Cuồng Ba", "风狂波", "Hộ Vệ", "Nhân Tộc", "Trúc Cơ Viên Mãn", "Đội Trưởng Hộ Vệ"),
    ("Vũ Hải Yến", "武海燕", "Thuyền Viên", "Nhân Tộc", "Trúc Cơ Hậu Kỳ", "Phó Thuyền Trưởng"),
    ("Lôi Thiên Phong", "雷天风", "Trưởng Lão", "Nhân Tộc", "Nguyên Anh Sơ Kỳ", "Trưởng Lão Hội Đồng"),
]))

# ═══════════════════════════════════════════════════════════════════════
# 10. Phù Du Linh Đoàn — pop millions (vi tộc), unranked, small → 3 chars
# ═══════════════════════════════════════════════════════════════════════
FACTIONS.append(("Phù_Du_Linh_Đoàn", "Phù Du Linh Đoàn", "Vô Tận Hải", [
    ("Linh Quang Mẫu", "灵光母", "Đoàn Mẫu", "Vi Tộc (Phù Du)", "Luyện Khí Đỉnh Phong", "Linh Quang Mẫu / Quần Thể Ý Thức"),
    ("Linh Tiểu Quang", "灵小光", "Phù Du Tiên Phong", "Vi Tộc (Phù Du)", "Luyện Khí Sơ Kỳ", "Tiên Phong Chiếu Sáng"),
    ("Linh Bích Hải", "灵碧海", "Phù Du Cổ", "Vi Tộc (Phù Du)", "Luyện Khí Trung Kỳ", "Hạch Tâm Quần Thể"),
]))

# ═══════════════════════════════════════════════════════════════════════
# 11. San Hô Đảo Quốc — pop 5000, Hạng Nhì, large → 8-10 chars
# ═══════════════════════════════════════════════════════════════════════
FACTIONS.append(("San_Hô_Đảo_Quốc", "San Hô Đảo Quốc", "Vô Tận Hải", [
    ("Thủy Tinh", "水晶", "Nữ Vương", "Hải Tộc (Nhân Ngư)", "Nguyên Anh Đỉnh Phong", "Nữ Vương"),
    ("Hải Nguyệt Ca", "海月歌", "Viện Chủ", "Hải Tộc (Nhân Ngư)", "Nguyên Anh Hậu Kỳ", "Viện Chủ Linh Ca Viện"),
    ("Triều Thiên Vệ", "潮天卫", "Tướng Quân", "Hải Tộc (Nhân Ngư)", "Nguyên Anh Sơ Kỳ", "Thống Lĩnh Hải Vệ Quân"),
    ("San Bạch Ngọc", "珊白玉", "Trưởng Lão", "Hải Tộc (Tiên Cá)", "Nguyên Anh Sơ Kỳ", "Trưởng Lão Hội Đồng Linh San"),
    ("Hải Vân Dao", "海云瑶", "Nhạc Sư", "Hải Tộc (Nhân Ngư)", "Kim Đan Viên Mãn", "Đại Sư Linh Ca"),
    ("San Hồng Diệp", "珊红叶", "Thương Nhân", "Hải Tộc (Tiên Cá)", "Kim Đan Hậu Kỳ", "Đoàn Trưởng Thương Hồ Đoàn"),
    ("Triều Bích Hải", "潮碧海", "Chiến Binh", "Hải Tộc (Nhân Ngư)", "Kim Đan Trung Kỳ", "Đội Trưởng Hải Vệ"),
    ("Hải Tiểu Loa", "海小螺", "Nghệ Nhân", "Hải Tộc (Tiên Cá)", "Trúc Cơ Viên Mãn", "Nghệ Nhân Điêu Khắc San Hô"),
    ("San Ngọc Lan", "珊玉兰", "Dược Sư", "Hải Tộc (Nhân Ngư)", "Kim Đan Sơ Kỳ", "Dược Sư Tảo Biển"),
]))

# ═══════════════════════════════════════════════════════════════════════
# 12. Tạp Huyết Long Đàn — pop ~40, Hạng Tư, small → 5 chars
# ═══════════════════════════════════════════════════════════════════════
FACTIONS.append(("Tạp_Huyết_Long_Đàn", "Tạp Huyết Long Đàn", "Vô Tận Hải", [
    ("Xích Giác", "赤角", "Đàn Chủ", "Long Tộc (Tạp Huyết)", "Kim Đan Sơ Kỳ", "Đàn Chủ"),
    ("Long Hôi Vĩ", "龙灰尾", "Trưởng Lão", "Long Tộc (Tạp Huyết)", "Trúc Cơ Hậu Kỳ", "Trưởng Lão"),
    ("Long Bạch Lân", "龙白鳞", "Trưởng Lão", "Long Tộc (Tạp Huyết)", "Trúc Cơ Hậu Kỳ", "Trưởng Lão"),
    ("Giao Hàn Băng", "蛟寒冰", "Chiến Binh", "Long Tộc (Tạp Huyết)", "Trúc Cơ Trung Kỳ", "Chiến Binh (Phun Băng)"),
    ("Long Thiết Trảo", "龙铁爪", "Trưởng Lão", "Long Tộc (Tạp Huyết)", "Trúc Cơ Hậu Kỳ", "Trưởng Lão"),
]))

# ═══════════════════════════════════════════════════════════════════════
# 13. Thủy Kiếm Đảo — pop 1800, Hạng Ba, medium-large → 8 chars
# ═══════════════════════════════════════════════════════════════════════
FACTIONS.append(("Thủy_Kiếm_Đảo", "Thủy Kiếm Đảo", "Vô Tận Hải", [
    ("Thủy Vô Trần", "水无尘", "Đảo Chủ", "Nhân Tộc", "Nguyên Anh Trung Kỳ", "Đảo Chủ"),
    ("Hải Triều Kiếm", "海潮剑", "Trưởng Lão", "Nhân Tộc", "Kim Đan Viên Mãn", "Đội Trưởng Triều Tịch Đội"),
    ("Lý Thanh Lãng", "李清浪", "Hộ Pháp", "Nhân Tộc", "Kim Đan Đỉnh Phong", "Hộ Pháp Hải Ngự Đoàn"),
    ("Trần Kiếm Ngư", "陈剑鱼", "Trưởng Lão", "Nhân Tộc", "Kim Đan Hậu Kỳ", "Trưởng Lão"),
    ("Thủy Nguyệt Hàn", "水月寒", "Chân Truyền", "Nhân Tộc", "Kim Đan Sơ Kỳ", "Chân Truyền Đệ Tử"),
    ("Lý Hải Đào", "李海涛", "Dược Sư", "Nhân Tộc", "Kim Đan Sơ Kỳ", "Dược Sư Trưởng Lưu Thủy Viện"),
    ("Vũ Sóng Triều", "武浪潮", "Nội Môn", "Nhân Tộc", "Trúc Cơ Viên Mãn", "Đội Trưởng Nội Môn"),
    ("Trần Tiểu Kiếm", "陈小剑", "Ngoại Môn", "Nhân Tộc", "Trúc Cơ Sơ Kỳ", "Ngoại Môn Đệ Tử Ưu Tú"),
]))

# ═══════════════════════════════════════════════════════════════════════
# 14. Thủy Mẫu Trùng Đàn — pop thousands (Trùng Tộc), unranked, small → 3 chars
# ═══════════════════════════════════════════════════════════════════════
FACTIONS.append(("Thủy_Mẫu_Trùng_Đàn", "Thủy Mẫu Trùng Đàn", "Vô Tận Hải", [
    ("Nguyệt Quang", "月光", "Đàn Mẫu", "Trùng Tộc (Sứa Linh)", "Trúc Cơ Sơ Kỳ", "Đàn Mẫu"),
    ("Trùng Bạch Quang", "虫白光", "Sứa Linh Lớn", "Trùng Tộc (Sứa Linh)", "Luyện Khí Đỉnh Phong", "Phó Đàn"),
    ("Trùng Hồng Diệm", "虫红焰", "Sứa Linh Đỏ", "Trùng Tộc (Sứa Linh)", "Luyện Khí Hậu Kỳ", "Tiên Phong Dẫn Đường"),
]))

# ═══════════════════════════════════════════════════════════════════════
# 15. Thuyền Nhân Hộ Vệ Đội — pop ~37, Hạng Năm, small → 5 chars
# ═══════════════════════════════════════════════════════════════════════
FACTIONS.append(("Thuyền_Nhân_Hộ_Vệ_Đội", "Thuyền Nhân Hộ Vệ Đội", "Vô Tận Hải", [
    ("Trương Hải Bằng", "张海鹏", "Đội Trưởng", "Nhân Tộc", "Trúc Cơ Viên Mãn", "Đội Trưởng"),
    ("Vũ Thiết Sơn", "武铁山", "Phó Đội", "Nhân Tộc", "Trúc Cơ Trung Kỳ", "Phó Đội Trưởng"),
    ("Lê Hải Yến", "黎海燕", "Phó Đội", "Nhân Tộc", "Trúc Cơ Trung Kỳ", "Phó Đội Trưởng"),
    ("Đặng Tiểu Ngư", "邓小鱼", "Hộ Vệ", "Nhân Tộc", "Luyện Khí Đỉnh Phong", "Hộ Vệ Viên / Linh Căn Thủy"),
    ("Hoàng Lão Cẩu", "黄老狗", "Hộ Vệ", "Nhân Tộc", "Trúc Cơ Sơ Kỳ", "Hộ Vệ Kỳ Cựu"),
]))

# ═══════════════════════════════════════════════════════════════════════
# 16. Vực Thẳm Ma Cung — pop 4000, Hạng Nhì, large → 8-10 chars
# ═══════════════════════════════════════════════════════════════════════
FACTIONS.append(("Vực_Thẳm_Ma_Cung", "Vực Thẳm Ma Cung", "Vô Tận Hải", [
    ("Thâm Hải", "深海", "Cung Chủ", "Hải Tộc (Biến Dị)", "Hóa Thần Sơ Kỳ", "Ma Cung Chủ"),
    ("Ám Lưu", "暗流", "Hộ Pháp", "Thủy Ma", "Nguyên Anh Hậu Kỳ", "Đại Hộ Pháp"),
    ("Hắc Triều", "黑潮", "Thống Lĩnh", "Hải Tộc (Biến Dị)", "Nguyên Anh Hậu Kỳ", "Thống Lĩnh Thâm Hải Ma Quân"),
    ("Ngư Quỷ Diện", "鱼鬼面", "Đội Trưởng", "Thủy Ma", "Kim Đan Đỉnh Phong", "Đội Trưởng Ám Ảnh Ngư Đội"),
    ("Huyết Trùng", "血虫", "Trưởng Lão", "Hải Tộc (Biến Dị)", "Nguyên Anh Sơ Kỳ", "Trưởng Lão Ma Quân"),
    ("Thâm Uyên Nữ", "深渊女", "Ma Sư", "Thủy Ma", "Nguyên Anh Sơ Kỳ", "Trưởng Lão Thi Ma Các"),
    ("Hắc Nha", "黑牙", "Ma Binh", "Hải Tộc (Biến Dị)", "Kim Đan Hậu Kỳ", "Phó Thống Lĩnh"),
    ("Ám Ảnh Ngư", "暗影鱼", "Sát Thủ", "Thủy Ma", "Kim Đan Trung Kỳ", "Sát Thủ Tinh Nhuệ"),
    ("Thâm Hải Trùng", "深海虫", "Ma Binh", "Hải Tộc (Biến Dị)", "Kim Đan Sơ Kỳ", "Đội Trưởng Xung Kích"),
    ("Huyết Ba", "血波", "Ma Tu", "Thủy Ma", "Trúc Cơ Viên Mãn", "Ngoại Môn Đệ Tử"),
]))

# ═══════════════════════════════════════════════════════════════════════
# 17. Yêu Thú Cứu Hộ Đoàn — pop ~15+, Hạng Năm, small → 4 chars
# ═══════════════════════════════════════════════════════════════════════
FACTIONS.append(("Yêu_Thú_Cứu_Hộ_Đoàn", "Yêu Thú Cứu Hộ Đoàn", "Vô Tận Hải", [
    ("Hùng Từ Bi", "熊慈悲", "Đoàn Trưởng", "Yêu Tộc (Gấu Yêu)", "Trúc Cơ Hậu Kỳ", "Đoàn Trưởng"),
    ("Yến Thanh", "燕青", "Phó Đoàn", "Yêu Tộc (Yến Yêu)", "Trúc Cơ Sơ Kỳ", "Phó Đoàn Trưởng / Trinh Sát"),
    ("Hổ Thiết Chưởng", "虎铁掌", "Cứu Hộ Viên", "Yêu Tộc (Hổ Yêu)", "Luyện Khí Đỉnh Phong", "Cứu Hộ Viên Chính"),
    ("Miêu Nhược Nhược", "猫弱弱", "Dược Sư", "Yêu Tộc (Miêu Yêu)", "Luyện Khí Hậu Kỳ", "Dược Sư / Chăm Sóc Linh Thú"),
]))


# ── Generate files ───────────────────────────────────────────────────
def main():
    total = 0
    for folder_name, faction_display, region, chars in FACTIONS:
        faction_dir = os.path.join(NHAN_VAT_VTH, folder_name)
        os.makedirs(faction_dir, exist_ok=True)
        for name, hantu, archetype, race, cultivation, chuc_vu in chars:
            filename = name.replace(" ", "_") + ".md"
            filepath = os.path.join(faction_dir, filename)
            content = make_char_content(
                name, hantu, archetype, race, cultivation,
                region, faction_display, chuc_vu
            )
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            total += 1
            print(f"  Created: {os.path.relpath(filepath, BASE)}")
        print(f"  [{folder_name}] {len(chars)} characters")
        print()

    print(f"=== TOTAL: {total} character files created across {len(FACTIONS)} factions ===")


if __name__ == "__main__":
    main()
