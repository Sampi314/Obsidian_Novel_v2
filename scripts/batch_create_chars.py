#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Batch-create 189 character files for Nam Cương and Thiên Trụ factions."""

import os

BASE = os.path.join(os.path.dirname(__file__), '..', 'Đạo', 'Nhân_Vật')

def make_char(name, hantu, archetype, race, cultivation, region, faction, position, desc=""):
    """Create a character .md file if it doesn't already exist."""
    fname = name.replace(' ', '_') + '.md'
    fpath = os.path.join(BASE, fname)
    if os.path.exists(fpath):
        print(f"  SKIP (exists): {fname}")
        return False

    content = f"""---
type: character
name: {name}
hantu: {hantu}
archetype: {position}
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
- **Khu Vực:** {region}.
- **Thế Lực:** {faction}.
- **Chức Vụ:** {position}.

## II. NGOẠI HÌNH & TÍNH CÁCH
{desc if desc else '*(Chưa xác định)*'}

## III. NĂNG LỰC & CHIẾN ĐẤU
*(Chưa xác định)*

## IV. CÁC MỐI QUAN HỆ
*(Chưa xác định)*

## V. TIỂU SỬ & HÀNH TRÌNH
*(Chưa xác định)*
"""
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  CREATED: {fname}")
    return True

# ============================================================
# NAM CƯƠNG CHARACTERS
# ============================================================

def create_van_doc_mon():
    """Vạn Độc Môn — 18 new characters"""
    F = "Vạn Độc Môn"
    R = "Nam Cương"
    chars = [
        ("Âu Dương Vô Tích", "歐陽無跡", "Thái Thượng Trưởng Lão", "Nhân Tộc", "Hóa Thần Trung Kỳ"),
        ("Liễu Lãnh Huyết", "柳冷血", "Xà Chi Hộ Pháp", "Nhân Tộc", "Nguyên Anh Hậu Kỳ"),
        ("Mạc Thiên Túc", "莫千足", "Rết Chi Hộ Pháp", "Nhân Tộc", "Nguyên Anh Sơ Kỳ"),
        ("Hạ Thiên Châm", "夏天針", "Yết Chi Hộ Pháp", "Nhân Tộc", "Nguyên Anh Trung Kỳ"),
        ("Đàm Trầm Thủy", "譚沈水", "Thiềm Chi Hộ Pháp", "Nhân Tộc", "Nguyên Anh Sơ Kỳ"),
        ("La Vân Ti", "羅雲絲", "Nhện Chi Hộ Pháp", "Nhân Tộc", "Kim Đan Viên Mãn"),
        ("Hàn Phong", "韓鋒", "Nhất Sát", "Nhân Tộc", "Kim Đan Viên Mãn"),
        ("Đinh Huyết Mi", "丁血眉", "Nhị Sát", "Nhân Tộc", "Kim Đan Đỉnh Phong"),
        ("Bạch Vô Ảnh", "白無影", "Tam Sát", "Nhân Tộc", "Kim Đan Hậu Kỳ"),
        ("Hắc Dạ", "黑夜", "Tứ Sát", "Nhân Tộc", "Kim Đan Hậu Kỳ"),
        ("Diệp Thanh Trúc", "葉青竹", "Ngũ Sát", "Nhân Tộc", "Kim Đan Trung Kỳ"),
        ("Phùng Tiêu", "馮蕭", "Lục Sát", "Nhân Tộc", "Kim Đan Trung Kỳ"),
        ("Tiêu Vô Hận", "蕭無恨", "Thất Sát", "Nhân Tộc", "Kim Đan Sơ Kỳ"),
        ("Ân Mộc Thanh", "殷木青", "Mộc Độc Sư Đường Chủ", "Nhân Tộc", "Nguyên Anh Sơ Kỳ"),
        ("Cổ Hàn Sương", "古寒霜", "Luyện Tà Đường Chủ", "Nhân Tộc", "Nguyên Anh Sơ Kỳ"),
        ("A Mộc", "阿木", "Chân Truyền Đệ Tử", "Nhân Tộc", "Kim Đan Sơ Kỳ"),
        ("Hồ Nguyệt Nhi", "胡月兒", "Nội Môn Đệ Tử", "Nhân Tộc", "Trúc Cơ Hậu Kỳ"),
        ("Ân Tiểu Độc", "殷小毒", "Nội Môn Đệ Tử", "Nhân Tộc", "Trúc Cơ Trung Kỳ"),
    ]
    for name, hantu, pos, race, cult in chars:
        make_char(name, hantu, pos, race, cult, R, F, pos)

def create_dan_ha_coc():
    """Đan Hà Cốc — 19 new characters"""
    F = "Đan Hà Cốc"
    R = "Nam Cương"
    chars = [
        ("Hạ Viêm", "夏炎", "Thái Thượng Trưởng Lão", "Nhân Tộc", "Hóa Thần Trung Kỳ"),
        ("Lư Hỏa", "盧火", "Tả Hộ Pháp", "Nhân Tộc", "Nguyên Anh Viên Mãn"),
        ("Phùng Đan Thanh", "馮丹青", "Hữu Hộ Pháp", "Nhân Tộc", "Nguyên Anh Hậu Kỳ"),
        ("Dương Linh Hỏa", "楊靈火", "Đệ Nhất Tháp Chủ", "Nhân Tộc", "Nguyên Anh Trung Kỳ"),
        ("Trần Hỏa Nham", "陳火岩", "Đệ Nhị Tháp Chủ", "Nhân Tộc", "Nguyên Anh Sơ Kỳ"),
        ("Tôn Đan Tâm", "孫丹心", "Đệ Tam Tháp Chủ", "Nhân Tộc", "Nguyên Anh Hậu Kỳ"),
        ("Lâm Thanh Hà", "林清河", "Đệ Tứ Tháp Chủ", "Nhân Tộc", "Nguyên Anh Sơ Kỳ"),
        ("Mã Hồng Lô", "馬紅爐", "Đệ Ngũ Tháp Chủ", "Nhân Tộc", "Kim Đan Viên Mãn"),
        ("Hoàng Thiên Hỏa", "黃天火", "Đệ Lục Tháp Chủ", "Nhân Tộc", "Kim Đan Đỉnh Phong"),
        ("Châu Ngọc Yên", "周玉煙", "Đệ Thất Tháp Chủ", "Nhân Tộc", "Kim Đan Đỉnh Phong"),
        ("Hứa Luyện", "許煉", "Đệ Bát Tháp Chủ", "Nhân Tộc", "Kim Đan Hậu Kỳ"),
        ("Tiêu Hỏa Nhi", "蕭火兒", "Đệ Cửu Tháp Chủ", "Nhân Tộc", "Kim Đan Trung Kỳ"),
        ("Thạch Hổ", "石虎", "Hộ Pháp Đường Chủ", "Nhân Tộc", "Nguyên Anh Trung Kỳ"),
        ("Lưu Thiết Giáp", "劉鐵甲", "Đệ Nhất Hộ Pháp", "Nhân Tộc", "Nguyên Anh Sơ Kỳ"),
        ("Ngô Lôi", "吳雷", "Đệ Nhị Hộ Pháp", "Nhân Tộc", "Kim Đan Viên Mãn"),
        ("Vương Cương", "王鋼", "Đệ Tam Hộ Pháp", "Nhân Tộc", "Kim Đan Đỉnh Phong"),
        ("Dương Tiểu Lô", "楊小爐", "Đại Đệ Tử", "Nhân Tộc", "Kim Đan Sơ Kỳ"),
        ("Phùng Lô Hỏa", "馮爐火", "Nội Môn Đệ Tử", "Nhân Tộc", "Trúc Cơ Viên Mãn"),
        ("Lâm Ngọc Yên", "林玉煙", "Nội Môn Đệ Tử", "Nhân Tộc", "Trúc Cơ Hậu Kỳ"),
    ]
    for name, hantu, pos, race, cult in chars:
        make_char(name, hantu, pos, race, cult, R, F, pos)

def create_co_nguyet_than_giao():
    """Cổ Nguyệt Thần Giáo — 16 new characters"""
    F = "Cổ Nguyệt Thần Giáo"
    R = "Nam Cương"
    chars = [
        ("Tuyết Nguyệt", "雪月", "Đại Tư Tế", "Nhân Tộc", "Nguyên Anh Hậu Kỳ"),
        ("Nguyệt Ảnh", "月影", "Đệ Nhất Phó Tư Tế", "Nhân Tộc", "Nguyên Anh Trung Kỳ"),
        ("Vu Huyền Nương", "巫玄娘", "Đệ Nhị Phó Tư Tế", "Nhân Tộc", "Nguyên Anh Sơ Kỳ"),
        ("Bạch Vọng Nguyệt", "白望月", "Đệ Tam Phó Tư Tế", "Nhân Tộc", "Nguyên Anh Sơ Kỳ"),
        ("Lam Nguyệt Nhi", "藍月兒", "Thánh Nữ", "Nhân Tộc", "Kim Đan Viên Mãn"),
        ("Vu Thiên Hương", "巫天香", "Đại Trưởng Lão Tế Tư", "Nhân Tộc", "Kim Đan Đỉnh Phong"),
        ("Linh Nguyệt Hà", "靈月河", "Trưởng Lão Tế Tư", "Nhân Tộc", "Kim Đan Hậu Kỳ"),
        ("Mộng Yểm", "夢魘", "Trưởng Lão Tế Tư", "Nhân Tộc", "Kim Đan Hậu Kỳ"),
        ("Cổ Lan", "古蘭", "Trưởng Lão Tế Tư", "Nhân Tộc", "Kim Đan Trung Kỳ"),
        ("Nguyệt Trầm", "月沈", "Trưởng Lão Tế Tư", "Nhân Tộc", "Kim Đan Trung Kỳ"),
        ("Đằng Thiết Sơn", "藤鐵山", "Thống Lĩnh Đồ Đằng", "Nhân Tộc", "Nguyên Anh Sơ Kỳ"),
        ("Đằng Hổ", "藤虎", "Phó Trưởng Lão Đồ Đằng", "Nhân Tộc", "Kim Đan Đỉnh Phong"),
        ("Sơn Mãng", "山莽", "Chiến Sĩ Đồ Đằng", "Nhân Tộc", "Kim Đan Hậu Kỳ"),
        ("Vu Tiểu Linh", "巫小靈", "Đệ Tử Tế Tư", "Nhân Tộc", "Trúc Cơ Viên Mãn"),
        ("Nguyệt Nhi", "月兒", "Đệ Tử Tế Tư", "Nhân Tộc", "Trúc Cơ Hậu Kỳ"),
        ("Đằng Thanh", "藤青", "Đệ Tử Đồ Đằng", "Nhân Tộc", "Trúc Cơ Hậu Kỳ"),
    ]
    for name, hantu, pos, race, cult in chars:
        make_char(name, hantu, pos, race, cult, R, F, pos)

def create_huyet_ma_tong():
    """Huyết Ma Tông — 10 new characters"""
    F = "Huyết Ma Tông"
    R = "Nam Cương"
    chars = [
        ("Huyết Tôn", "血尊", "Tông Chủ", "Nhân Tộc", "Nguyên Anh Hậu Kỳ"),
        ("Mộ Dung Huyết Thiên", "慕容血天", "Thái Thượng Trưởng Lão", "Nhân Tộc", "Nguyên Anh Viên Mãn"),
        ("Cừu Thiên", "仇天", "Đệ Nhất Huyết Tướng", "Nhân Tộc", "Nguyên Anh Sơ Kỳ"),
        ("Hà Minh Phong", "何明風", "Đệ Nhị Huyết Tướng", "Nhân Tộc", "Kim Đan Viên Mãn"),
        ("Lý Ám", "李暗", "Đệ Tam Huyết Tướng", "Nhân Tộc", "Kim Đan Đỉnh Phong"),
        ("Tôn Hàn Thiết", "孫寒鐵", "Đệ Tứ Huyết Tướng", "Nhân Tộc", "Kim Đan Đỉnh Phong"),
        ("Trương Phách", "張魄", "Huyết Nô Viện Chủ", "Nhân Tộc", "Kim Đan Đỉnh Phong"),
        ("Cừu Tiểu Đao", "仇小刀", "Chân Truyền Đệ Tử", "Nhân Tộc", "Kim Đan Sơ Kỳ"),
        ("Hà Linh", "何靈", "Nội Môn Đệ Tử", "Nhân Tộc", "Trúc Cơ Viên Mãn"),
        ("Ân Thiết", "殷鐵", "Nội Môn Đệ Tử", "Nhân Tộc", "Trúc Cơ Hậu Kỳ"),
    ]
    for name, hantu, pos, race, cult in chars:
        make_char(name, hantu, pos, race, cult, R, F, pos)

def create_quy_thi_nam_cuong():
    """Quỷ Thị Nam Cương — 6 new characters"""
    F = "Quỷ Thị Nam Cương"
    R = "Nam Cương"
    chars = [
        ("Mạc Vô Diện", "莫無面", "Quỷ Chủ", "Nhân Tộc", "Nguyên Anh Viên Mãn"),
        ("Chu Thiết Diện", "朱鐵面", "Trưởng Lão Chấp Pháp", "Nhân Tộc", "Nguyên Anh Sơ Kỳ"),
        ("Vương Cổ Thuyền", "王古船", "Đưa Đò Trưởng", "Nhân Tộc", "Kim Đan Viên Mãn"),
        ("Hồ Vô Thanh", "胡無聲", "Tổng Quản", "Nhân Tộc", "Kim Đan Hậu Kỳ"),
        ("Ám Nhị", "暗二", "Tổng Quản", "Nhân Tộc", "Kim Đan Trung Kỳ"),
        ("Lệ Tam", "厲三", "Đấu Giá Sư", "Nhân Tộc", "Kim Đan Sơ Kỳ"),
    ]
    for name, hantu, pos, race, cult in chars:
        make_char(name, hantu, pos, race, cult, R, F, pos)

def create_hac_bao_trai():
    """Hắc Báo Trại — 7 new characters"""
    F = "Hắc Báo Trại"
    R = "Nam Cương"
    chars = [
        ("Đỗ Môn", "杜門", "Trại Chủ", "Nhân Tộc", "Trúc Cơ Hậu Kỳ"),
        ("Đỗ Hải", "杜海", "Phó Trại Chủ", "Nhân Tộc", "Trúc Cơ Trung Kỳ"),
        ("Đỗ Hùng", "杜雄", "Báo Ảnh Đội Trưởng", "Nhân Tộc", "Trúc Cơ Sơ Kỳ"),
        ("Lý Sơn Đao", "李山刀", "Hắc Đao Trưởng Lão", "Nhân Tộc", "Trúc Cơ Trung Kỳ"),
        ("Vương Thiết Nha", "王鐵牙", "Hắc Đao Trưởng Lão", "Nhân Tộc", "Trúc Cơ Sơ Kỳ"),
        ("Đỗ Tiểu Hổ", "杜小虎", "Cơ Sở Đệ Tử", "Nhân Tộc", "Luyện Khí Đỉnh Phong"),
        ("Lý Sơn Nhi", "李山兒", "Ngoại Cơ Sở Đệ Tử", "Nhân Tộc", "Luyện Khí Hậu Kỳ"),
    ]
    for name, hantu, pos, race, cult in chars:
        make_char(name, hantu, pos, race, cult, R, F, pos)

def create_doc_long_bao():
    """Độc Long Bảo — 8 new characters"""
    F = "Độc Long Bảo"
    R = "Nam Cương"
    chars = [
        ("Độc Nhãn", "獨眼", "Bảo Chủ", "Nhân Tộc", "Kim Đan Trung Kỳ"),
        ("Lưu Ám Ảnh", "劉暗影", "Long Ảnh Đội Trưởng", "Nhân Tộc", "Kim Đan Sơ Kỳ"),
        ("Trần Phục Long", "陳伏龍", "Phục Thú Viện Chủ", "Nhân Tộc", "Kim Đan Sơ Kỳ"),
        ("Hoàng Thạch", "黃石", "Trưởng Lão", "Nhân Tộc", "Trúc Cơ Viên Mãn"),
        ("Triệu Long Hổ", "趙龍虎", "Trưởng Lão", "Nhân Tộc", "Trúc Cơ Hậu Kỳ"),
        ("Mạc Vân", "莫雲", "Trưởng Lão", "Nhân Tộc", "Trúc Cơ Trung Kỳ"),
        ("Lưu Tiểu Long", "劉小龍", "Nội Môn Đệ Tử", "Nhân Tộc", "Trúc Cơ Sơ Kỳ"),
        ("Hoàng Nhi", "黃兒", "Nội Môn Đệ Tử", "Nhân Tộc", "Luyện Khí Đỉnh Phong"),
    ]
    for name, hantu, pos, race, cult in chars:
        make_char(name, hantu, pos, race, cult, R, F, pos)

def create_ban_yeu_thon():
    """Bán Yêu Thôn — 3 new characters"""
    F = "Bán Yêu Thôn"
    R = "Nam Cương"
    chars = [
        ("Lý Bán Huyền", "李半玄", "Trưởng Lão", "Bán Yêu", "Trúc Cơ Viên Mãn"),
        ("Lý Bán Sơn", "李半山", "Trưởng Lão", "Bán Yêu", "Trúc Cơ Hậu Kỳ"),
        ("Thượng Quan Yêu Nhi", "上官妖兒", "Đội Trưởng Tuần Tra", "Bán Yêu", "Trúc Cơ Sơ Kỳ"),
    ]
    for name, hantu, pos, race, cult in chars:
        make_char(name, hantu, pos, race, cult, R, F, pos)

def create_dia_mach_tham_hiem():
    """Địa Mạch Thám Hiểm Đội — 5 new characters"""
    F = "Địa Mạch Thám Hiểm Đội"
    R = "Nam Cương"
    chars = [
        ("Thạch Vạn Lý", "石萬里", "Đội Trưởng", "Nhân Tộc", "Trúc Cơ Viên Mãn"),
        ("Lý Ám Dạ", "李暗夜", "Phó Đội Trưởng", "Nhân Tộc", "Trúc Cơ Hậu Kỳ"),
        ("Châu Hàn Dạ", "周寒夜", "Bản Đồ Sư", "Nhân Tộc", "Trúc Cơ Sơ Kỳ"),
        ("Trần Thạch Nham", "陳石岩", "Khai Khoáng Sư", "Nhân Tộc", "Trúc Cơ Sơ Kỳ"),
        ("Lâm Tiểu Đăng", "林小燈", "Thám Hiểm Viên", "Nhân Tộc", "Luyện Khí Đỉnh Phong"),
    ]
    for name, hantu, pos, race, cult in chars:
        make_char(name, hantu, pos, race, cult, R, F, pos)

def create_small_nam_cuong():
    """Small Nam Cương factions — 3 new characters"""
    make_char("Tằm Dạ Quang", "蠶夜光", "Cố Vấn Đệ Tử", "Trùng Tộc", "Trúc Cơ Viên Mãn",
              "Nam Cương", "Cổ Kén Tu Luyện Xã", "Cố Vấn Đệ Tử")
    make_char("Phấn Vũ", "粉羽", "Phấn Sư", "Vi Tộc", "Luyện Khí Trung Kỳ",
              "Nam Cương", "Bụi Phấn Hội", "Phấn Sư")
    make_char("Phấn Thanh Lộ", "粉清露", "Phấn Sư", "Vi Tộc", "Luyện Khí Sơ Kỳ",
              "Nam Cương", "Bụi Phấn Hội", "Phấn Sư")

# ============================================================
# THIÊN TRỤ CHARACTERS
# ============================================================

def create_dai_can_hoang_trieu():
    """Đại Càn Hoàng Triều — 16 new characters"""
    F = "Đại Càn Hoàng Triều"
    R = "Thiên Trụ"
    chars = [
        ("Lý Thiên Vũ", "李天武", "Càn Đế", "Nhân Tộc", "Hóa Thần Trung Kỳ"),
        ("Trần Bách Tài", "陳百財", "Hộ Bộ Thượng Thư", "Nhân Tộc", "Nguyên Anh Viên Mãn"),
        ("Khổng Minh Đức", "孔明德", "Lễ Bộ Thượng Thư", "Nhân Tộc", "Nguyên Anh Hậu Kỳ"),
        ("Vương Thiết Kỵ", "王鐵騎", "Binh Bộ Thượng Thư", "Nhân Tộc", "Nguyên Anh Viên Mãn"),
        ("Bao Chính", "包正", "Hình Bộ Thượng Thư", "Nhân Tộc", "Nguyên Anh Hậu Kỳ"),
        ("Lỗ Thiên Kiều", "魯天橋", "Công Bộ Thượng Thư", "Nhân Tộc", "Nguyên Anh Sơ Kỳ"),
        ("Tôn Hiền", "孫賢", "Lại Bộ Thượng Thư", "Nhân Tộc", "Nguyên Anh Sơ Kỳ"),
        ("Mộ Dung Chiến", "慕容戰", "Thần Sách Đại Tướng", "Nhân Tộc", "Hóa Thần Sơ Kỳ"),
        ("Triệu Vạn Quân", "趙萬軍", "Phó Tướng Thần Sách", "Nhân Tộc", "Nguyên Anh Viên Mãn"),
        ("Tư Mã Tinh Vân", "司馬星雲", "Khâm Thiên Giám Chính", "Nhân Tộc", "Nguyên Anh Viên Mãn"),
        ("Hà Thiên Chiêu", "何天昭", "Phó Giám Khâm Thiên", "Nhân Tộc", "Nguyên Anh Hậu Kỳ"),
        ("Lý Thiên Long", "李天龍", "Thái Tử", "Nhân Tộc", "Nguyên Anh Sơ Kỳ"),
        ("Lý Thiên Phượng", "李天鳳", "Nhị Hoàng Tử", "Nhân Tộc", "Kim Đan Viên Mãn"),
        ("Lý Nguyệt Nhi", "李月兒", "Công Chúa", "Nhân Tộc", "Kim Đan Sơ Kỳ"),
        ("Trương Văn Hàn", "張文翰", "Hàn Lâm Học Sĩ", "Nhân Tộc", "Kim Đan Đỉnh Phong"),
        ("Lưu Phong Thành", "劉風城", "Tướng Quân Thị Vệ", "Nhân Tộc", "Kim Đan Đỉnh Phong"),
    ]
    for name, hantu, pos, race, cult in chars:
        make_char(name, hantu, pos, race, cult, R, F, pos)

def create_cuu_u_ma_tong():
    """Cửu U Ma Tông — 14 new characters"""
    F = "Cửu U Ma Tông"
    R = "Thiên Trụ"
    chars = [
        ("Ma Chủ Vô Tên", "魔主無名", "Ma Chủ", "Nhân Tộc", "Luyện Hư Trung Kỳ"),
        ("Cừu Huyết Thiên", "仇血天", "Đệ Nhất Ma Vương", "Nhân Tộc", "Hóa Thần Hậu Kỳ"),
        ("Âm Phong", "陰風", "Đệ Nhị Ma Vương", "Nhân Tộc", "Hóa Thần Sơ Kỳ"),
        ("Hồn Diệt", "魂滅", "Đệ Tam Ma Vương", "Nhân Tộc", "Nguyên Anh Viên Mãn"),
        ("Nạp Lan U Minh", "納蘭幽冥", "Đệ Tứ Ma Vương", "Nhân Tộc", "Nguyên Anh Viên Mãn"),
        ("Lý Cửu Âm", "李九陰", "Đệ Ngũ Ma Vương", "Nhân Tộc", "Nguyên Anh Hậu Kỳ"),
        ("Mạc U Hồn", "莫幽魂", "Đệ Lục Ma Vương", "Nhân Tộc", "Nguyên Anh Hậu Kỳ"),
        ("Bạch Cốt", "白骨", "Đệ Thất Ma Vương", "Nhân Tộc", "Nguyên Anh Trung Kỳ"),
        ("Diệp Huyền Minh", "葉玄冥", "Đệ Bát Ma Vương", "Nhân Tộc", "Nguyên Anh Trung Kỳ"),
        ("Quỷ Diện", "鬼面", "Đệ Cửu Ma Vương", "Nhân Tộc", "Nguyên Anh Sơ Kỳ"),
        ("Lý Vô Ảnh", "李無影", "Ảnh Ma Viện Chủ", "Nhân Tộc", "Nguyên Anh Viên Mãn"),
        ("Nạp Lan Tiểu U", "納蘭小幽", "Chân Truyền Đệ Tử", "Nhân Tộc", "Kim Đan Đỉnh Phong"),
        ("Cừu Huyết Nhi", "仇血兒", "Nội Môn Đệ Tử", "Nhân Tộc", "Kim Đan Sơ Kỳ"),
        ("Mạc Ám", "莫暗", "Nội Môn Đệ Tử", "Nhân Tộc", "Trúc Cơ Viên Mãn"),
    ]
    for name, hantu, pos, race, cult in chars:
        make_char(name, hantu, pos, race, cult, R, F, pos)

def create_thien_kieu_hoc_vien():
    """Thiên Kiêu Học Viện — 11 new characters"""
    F = "Thiên Kiêu Học Viện"
    R = "Thiên Trụ"
    chars = [
        ("Hạo Nhiên", "浩然", "Viện Trưởng", "Nhân Tộc", "Hóa Thần Hậu Kỳ"),
        ("Lý Học Hải", "李學海", "Phó Viện Trưởng Học Thuật", "Nhân Tộc", "Nguyên Anh Viên Mãn"),
        ("Vương Chiến", "王戰", "Phó Viện Trưởng Chiến Đấu", "Nhân Tộc", "Nguyên Anh Viên Mãn"),
        ("Tôn Thiên Cơ", "孫天機", "Trận Chư Viện Chủ", "Nhân Tộc", "Nguyên Anh Hậu Kỳ"),
        ("Triệu Phong Vân", "趙風雲", "Chiến Đấu Viện Chủ", "Nhân Tộc", "Nguyên Anh Hậu Kỳ"),
        ("Lỗ Bách Nghệ", "魯百藝", "Bách Nghệ Viện Chủ", "Nhân Tộc", "Nguyên Anh Sơ Kỳ"),
        ("Khổng Thư", "孔書", "Giáo Sư", "Nhân Tộc", "Nguyên Anh Sơ Kỳ"),
        ("Hoàng Phủ Lạc Thiên", "皇甫落天", "Giáo Sư", "Nhân Tộc", "Kim Đan Viên Mãn"),
        ("Lâm Tĩnh", "林靜", "Giáo Sư", "Nhân Tộc", "Kim Đan Đỉnh Phong"),
        ("Trương Tinh Thần", "張星辰", "Sinh Viên", "Nhân Tộc", "Kim Đan Sơ Kỳ"),
        ("Tiêu Mộng Dao", "蕭夢遥", "Nữ Sinh Viên", "Nhân Tộc", "Trúc Cơ Viên Mãn"),
    ]
    for name, hantu, pos, race, cult in chars:
        make_char(name, hantu, pos, race, cult, R, F, pos)

def create_bach_bao_cac():
    """Bách Bảo Các — 7 new characters"""
    F = "Bách Bảo Các"
    R = "Thiên Trụ"
    chars = [
        ("Tiền Đa Đa", "錢多多", "Các Chủ", "Nhân Tộc", "Nguyên Anh Hậu Kỳ"),
        ("Lý Minh Châu", "李明珠", "Giám Định Viện Chủ", "Nhân Tộc", "Nguyên Anh Sơ Kỳ"),
        ("Thiết Quân", "鐵軍", "Kỵ Giáp Thống Lĩnh", "Nhân Tộc", "Nguyên Anh Sơ Kỳ"),
        ("Châu Thương", "周商", "Đấu Giá Đường Chủ", "Nhân Tộc", "Kim Đan Viên Mãn"),
        ("Tiền Bảo", "錢寶", "Đại Chưởng Quỹ", "Nhân Tộc", "Kim Đan Đỉnh Phong"),
        ("Mã Vạn Kim", "馬萬金", "Thương Nhân", "Nhân Tộc", "Kim Đan Hậu Kỳ"),
        ("Hứa Ngọc", "許玉", "Giám Định Sư", "Nhân Tộc", "Kim Đan Trung Kỳ"),
    ]
    for name, hantu, pos, race, cult in chars:
        make_char(name, hantu, pos, race, cult, R, F, pos)

def create_thien_moc_thanh():
    """Thiên Mộc Thành — 8 new characters"""
    F = "Thiên Mộc Thành"
    R = "Thiên Trụ"
    chars = [
        ("Mộc Thiên Hào", "木天浩", "Thành Chủ", "Nhân Tộc", "Nguyên Anh Viên Mãn"),
        ("Mộc Vân", "木雲", "Phó Thành Chủ Quân Sự", "Nhân Tộc", "Nguyên Anh Hậu Kỳ"),
        ("Lâm Thương", "林商", "Phó Thành Chủ Thương Mại", "Nhân Tộc", "Nguyên Anh Sơ Kỳ"),
        ("Mộc Thiên Quân", "木天軍", "Tướng Quân Thị Vệ", "Nhân Tộc", "Nguyên Anh Sơ Kỳ"),
        ("Lâm Vạn Hóa", "林萬貨", "Thương Hội Chủ Tịch", "Nhân Tộc", "Kim Đan Viên Mãn"),
        ("Trần Thiết", "陳鐵", "Đại Sư Rèn Đúc", "Nhân Tộc", "Kim Đan Trung Kỳ"),
        ("Vương Lương", "王良", "Nông Trưởng", "Nhân Tộc", "Trúc Cơ Viên Mãn"),
        ("Hồ Thương", "胡商", "Thương Nhân", "Nhân Tộc", "Trúc Cơ Hậu Kỳ"),
    ]
    for name, hantu, pos, race, cult in chars:
        make_char(name, hantu, pos, race, cult, R, F, pos)

def create_thach_linh_cung():
    """Thạch Linh Cung — 19 new characters"""
    F = "Thạch Linh Cung"
    R = "Thiên Trụ"
    chars = [
        ("Thạch Chùy", "石錘", "Cung Chủ", "Thạch Tộc", "Nguyên Anh Viên Mãn"),
        ("Thạch Vạn Niên", "石萬年", "Thái Thượng Trưởng Lão", "Thạch Tộc", "Hóa Thần Sơ Kỳ"),
        ("Thạch Hỏa Long", "石火龍", "Đệ Nhất Hỏa Sư", "Thạch Tộc", "Nguyên Anh Hậu Kỳ"),
        ("Thạch Kim Quang", "石金光", "Đệ Nhị Hỏa Sư", "Thạch Tộc", "Nguyên Anh Sơ Kỳ"),
        ("Thạch Thiên", "石天", "Đệ Tam Hỏa Sư", "Thạch Tộc", "Nguyên Anh Sơ Kỳ"),
        ("Thạch Nham", "石岩", "Đệ Tứ Hỏa Sư", "Thạch Tộc", "Kim Đan Viên Mãn"),
        ("Thạch Linh Quang", "石靈光", "Đệ Ngũ Hỏa Sư", "Thạch Tộc", "Kim Đan Đỉnh Phong"),
        ("Thạch Bàn", "石盤", "Đệ Lục Hỏa Sư", "Thạch Tộc", "Kim Đan Đỉnh Phong"),
        ("Sơn Cương", "山鋼", "Đệ Thất Hỏa Sư", "Lai Cự Tộc", "Kim Đan Hậu Kỳ"),
        ("Mã Thiết Sơn", "馬鐵山", "Đệ Bát Hỏa Sư", "Lai Cự Tộc", "Kim Đan Hậu Kỳ"),
        ("Lý Ngọc Nham", "李玉岩", "Đệ Cửu Hỏa Sư", "Nhân Tộc", "Kim Đan Trung Kỳ"),
        ("Hồ Vân", "胡雲", "Đệ Thập Hỏa Sư", "Nhân Tộc", "Kim Đan Trung Kỳ"),
        ("Trần Phong", "陳鋒", "Đệ Thập Nhất Hỏa Sư", "Nhân Tộc", "Kim Đan Sơ Kỳ"),
        ("Sơn Tiểu Thạch", "山小石", "Đệ Thập Nhị Hỏa Sư", "Lai Cự Tộc", "Kim Đan Sơ Kỳ"),
        ("Sơn Thiết", "山鐵", "Hộ Pháp", "Lai Cự Tộc", "Nguyên Anh Sơ Kỳ"),
        ("Thạch Hùng", "石雄", "Hộ Pháp", "Thạch Tộc", "Kim Đan Viên Mãn"),
        ("Sơn Vạn", "山萬", "Quân Trưởng Thạch Mạch", "Lai Cự Tộc", "Kim Đan Đỉnh Phong"),
        ("Thạch Tiểu Sơn", "石小山", "Nội Môn Đệ Tử", "Thạch Tộc", "Trúc Cơ Viên Mãn"),
        ("Sơn Lực", "山力", "Nội Môn Đệ Tử", "Lai Cự Tộc", "Trúc Cơ Hậu Kỳ"),
    ]
    for name, hantu, pos, race, cult in chars:
        make_char(name, hantu, pos, race, cult, R, F, pos)

def create_loi_tri_thanh_dia():
    """Lôi Trì Thánh Địa — 8 new characters"""
    F = "Lôi Trì Thánh Địa"
    R = "Thiên Trụ"
    chars = [
        ("Lôi Thiên Nộ", "雷天怒", "Lôi Tôn", "Nhân Tộc", "Hóa Thần Sơ Kỳ"),
        ("Lôi Chấn", "雷震", "Đệ Nhất Hộ Pháp", "Nhân Tộc", "Nguyên Anh Hậu Kỳ"),
        ("Lôi Phong", "雷風", "Đệ Nhị Hộ Pháp", "Nhân Tộc", "Nguyên Anh Sơ Kỳ"),
        ("Lôi Vân", "雷雲", "Đệ Tam Hộ Pháp", "Nhân Tộc", "Nguyên Anh Sơ Kỳ"),
        ("Lôi Cương", "雷鋼", "Viện Chủ Lôi Pháp", "Nhân Tộc", "Nguyên Anh Trung Kỳ"),
        ("Lôi Tiểu Chấn", "雷小震", "Chân Truyền Đệ Tử", "Nhân Tộc", "Kim Đan Sơ Kỳ"),
        ("Tôn Lôi Ưng", "孫雷鷹", "Nội Môn Đệ Tử", "Nhân Tộc", "Trúc Cơ Viên Mãn"),
        ("Trần Lôi Hỏa", "陳雷火", "Nội Môn Đệ Tử", "Nhân Tộc", "Trúc Cơ Hậu Kỳ"),
    ]
    for name, hantu, pos, race, cult in chars:
        make_char(name, hantu, pos, race, cult, R, F, pos)

def create_trich_tinh_lau():
    """Trích Tinh Lâu — 5 new characters"""
    F = "Trích Tinh Lâu"
    R = "Thiên Trụ"
    chars = [
        ("Tinh Hà", "星河", "Lâu Chủ", "Nhân Tộc", "Nguyên Anh Viên Mãn"),
        ("Nguyệt Quang", "月光", "Thủ Các Trưởng Lão", "Nhân Tộc", "Nguyên Anh Hậu Kỳ"),
        ("Khắc Minh", "刻明", "Viện Chủ", "Nhân Tộc", "Nguyên Anh Sơ Kỳ"),
        ("Tinh Thần", "星辰", "Thiên Hà Học Giả", "Nhân Tộc", "Kim Đan Đỉnh Phong"),
        ("Bạch Quang Niên", "白光年", "Không Gian Học Giả", "Nhân Tộc", "Kim Đan Hậu Kỳ"),
    ]
    for name, hantu, pos, race, cult in chars:
        make_char(name, hantu, pos, race, cult, R, F, pos)

def create_thien_mon_kinh_dai():
    """Thiên Môn Kính Đài — 6 new characters"""
    F = "Thiên Môn Kính Đài"
    R = "Thiên Trụ"
    chars = [
        ("Cảnh Thiên Minh", "景天明", "Đài Chủ / Kính Lão", "Nhân Tộc", "Hóa Thần Sơ Kỳ"),
        ("Triệu Kính Vệ", "趙鏡衛", "Kính Vệ Thống Lĩnh", "Nhân Tộc", "Nguyên Anh Hậu Kỳ"),
        ("Sử Thiên Thư", "史天書", "Đại Sử Quan", "Nhân Tộc", "Nguyên Anh Sơ Kỳ"),
        ("Cảnh Tiểu Minh", "景小明", "Chấp Pháp Trưởng Sứ", "Nhân Tộc", "Kim Đan Đỉnh Phong"),
        ("Lý Thư", "李書", "Sử Quan", "Nhân Tộc", "Kim Đan Hậu Kỳ"),
        ("Hà Quan Tinh", "何觀星", "Chấp Pháp Trưởng Sứ", "Nhân Tộc", "Kim Đan Trung Kỳ"),
    ]
    for name, hantu, pos, race, cult in chars:
        make_char(name, hantu, pos, race, cult, R, F, pos)

# ============================================================
# MAIN
# ============================================================

if __name__ == '__main__':
    created = 0
    skipped = 0

    print("=== NAM CƯƠNG ===")
    fns_nc = [
        create_van_doc_mon, create_dan_ha_coc, create_co_nguyet_than_giao,
        create_huyet_ma_tong, create_quy_thi_nam_cuong, create_hac_bao_trai,
        create_doc_long_bao, create_ban_yeu_thon, create_dia_mach_tham_hiem,
        create_small_nam_cuong,
    ]
    for fn in fns_nc:
        print(f"\n--- {fn.__doc__} ---")
        fn()

    print("\n=== THIÊN TRỤ ===")
    fns_tt = [
        create_dai_can_hoang_trieu, create_cuu_u_ma_tong, create_thien_kieu_hoc_vien,
        create_bach_bao_cac, create_thien_moc_thanh, create_thach_linh_cung,
        create_loi_tri_thanh_dia, create_trich_tinh_lau, create_thien_mon_kinh_dai,
    ]
    for fn in fns_tt:
        print(f"\n--- {fn.__doc__} ---")
        fn()

    # Count results
    total_files = len([f for f in os.listdir(BASE) if f.endswith('.md')])
    print(f"\n{'='*50}")
    print(f"Total character files in Nhân_Vật: {total_files}")
    print("Done!")
