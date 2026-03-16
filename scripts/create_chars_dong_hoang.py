#!/usr/bin/env python3
"""
Generate character files for all Đông Hoang factions that currently have no characters.
"""
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHAR_DIR = os.path.join(BASE, "Đạo", "Nhân_Vật", "Đông_Hoang")

def make_char(name, hantu, archetype, race, cultivation, faction_name):
    """Generate character markdown content."""
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
- **Khu Vực:** Đông Hoang.
- **Thế Lực:** {faction_name}.
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

# All 69 factions with their characters
# Format: (faction_dir_name, faction_display_name, [(name, hantu, archetype, race, cultivation), ...])

FACTIONS = [
    # ============================================================
    # 1. Ảnh Nguyệt Uyển - Vi Tộc spy network, Hạng Nhất, pop 100k -> LARGE (10 chars)
    # ============================================================
    ("Ảnh_Nguyệt_Uyển", "Ảnh Nguyệt Uyển", [
        ("Vi Nguyệt Ảnh", "微月影", "Ảnh Chủ", "Vi Tộc", "Hóa Thần Sơ Kỳ"),
        ("Vi Ám Hà", "微暗荷", "Phó Ảnh Chủ", "Vi Tộc", "Luyện Hư Sơ Kỳ"),
        ("Tiểu Dạ Lan", "小夜蘭", "Thất Dạ Sứ", "Vi Tộc", "Nguyên Anh Hậu Kỳ"),
        ("Vi Sương Vân", "微霜雲", "Thất Dạ Sứ", "Vi Tộc", "Nguyên Anh Hậu Kỳ"),
        ("Linh Ảnh Điệp", "靈影蝶", "Thất Dạ Sứ", "Vi Tộc", "Nguyên Anh Trung Kỳ"),
        ("Vi Vô Thanh", "微無聲", "Sát Thủ Trưởng", "Vi Tộc", "Nguyên Anh Trung Kỳ"),
        ("Hoa Tiểu Yến", "花小燕", "Gián Điệp Trưởng", "Vi Tộc", "Nguyên Anh Sơ Kỳ"),
        ("Vi Minh Nguyệt", "微明月", "Trưởng Lão", "Vi Tộc", "Nguyên Anh Sơ Kỳ"),
        ("Tiểu Phong Linh", "小風鈴", "Trinh Sát Viên", "Vi Tộc", "Kim Đan Hậu Kỳ"),
        ("Vi Tiểu Hàn", "微小寒", "Liên Lạc Viên", "Vi Tộc", "Kim Đan Sơ Kỳ"),
    ]),

    # ============================================================
    # 2. Ảo Ảnh Lâm Tộc - Cursed Tinh Linh, Hạng Ba, pop 2000 -> SMALL (4 chars)
    # ============================================================
    ("Ảo_Ảnh_Lâm_Tộc", "Ảo Ảnh Lâm Tộc", [
        ("Nguyệt Yểm Ma", "月魘魔", "Trưởng Lão Yểm Ma", "Tinh Linh Tộc", "Nguyên Anh Hậu Kỳ"),
        ("Vân Huyễn Ảnh", "雲幻影", "Trưởng Lão", "Tinh Linh Tộc", "Nguyên Anh Sơ Kỳ"),
        ("Sương Mê Hồn", "霜迷魂", "Yểm Hồn Đội Trưởng", "Tinh Linh Tộc", "Kim Đan Hậu Kỳ"),
        ("Phong Ảo Mộng", "風幻夢", "Chiến Binh", "Tinh Linh Tộc", "Kim Đan Sơ Kỳ"),
    ]),

    # ============================================================
    # 3. Bách Hoa Cốc - Nhân Tộc female sect, Hạng Nhì, pop 3000 -> MEDIUM (6 chars)
    # ============================================================
    ("Bách_Hoa_Cốc", "Bách Hoa Cốc", [
        ("Lý Hoa Nguyệt", "李花月", "Cốc Chủ", "Nhân Tộc", "Luyện Hư Sơ Kỳ"),
        ("Trần Bách Liên", "陳百蓮", "Thái Thượng Trưởng Lão", "Nhân Tộc", "Nguyên Anh Đỉnh Phong"),
        ("Phạm Tú Lan", "范秀蘭", "Trưởng Lão Hoa Linh Đường", "Nhân Tộc", "Nguyên Anh Hậu Kỳ"),
        ("Nguyễn Vũ Cúc", "阮雨菊", "Trưởng Lão", "Nhân Tộc", "Nguyên Anh Trung Kỳ"),
        ("Lê Thanh Mai", "黎青梅", "Chưởng Quản Đệ Tử", "Nhân Tộc", "Kim Đan Hậu Kỳ"),
        ("Hoàng Tiểu Đào", "黃小桃", "Nội Môn Đệ Tử", "Nhân Tộc", "Trúc Cơ Hậu Kỳ"),
    ]),

    # ============================================================
    # 4. Bách Nghệ Phường Tổng Đàn - Nhân Tộc artisans, Hạng Năm, pop 305 -> SMALL (3 chars)
    # ============================================================
    ("Bách_Nghệ_Phường_Tổng_Đàn", "Bách Nghệ Phường Tổng Đàn", [
        ("Đặng Công Mẫu", "鄧工母", "Phường Chủ", "Nhân Tộc", "Kim Đan Trung Kỳ"),
        ("Vũ Thiết Chùy", "武鐵錘", "Phó Phường Chủ Đan Đường", "Nhân Tộc", "Trúc Cơ Hậu Kỳ"),
        ("Lý Tiểu Lô", "李小爐", "Tổng Quản", "Nhân Tộc", "Trúc Cơ Trung Kỳ"),
    ]),

    # ============================================================
    # 5. Bách Thú Sơn Trang - Nhân Tộc beast tamers, Hạng Nhì, pop 10000 -> MEDIUM (8 chars)
    # ============================================================
    ("Bách_Thú_Sơn_Trang", "Bách Thú Sơn Trang", [
        ("Trần Vạn Thú", "陳萬獸", "Trang Chủ", "Nhân Tộc", "Luyện Hư Sơ Kỳ"),
        ("Lý Thiên Mã", "李天馬", "Thái Thượng Trưởng Lão", "Nhân Tộc", "Nguyên Anh Đỉnh Phong"),
        ("Phạm Linh Ưng", "范靈鷹", "Hộ Pháp", "Nhân Tộc", "Nguyên Anh Hậu Kỳ"),
        ("Hoàng Mãnh Hổ", "黃猛虎", "Hộ Pháp", "Nhân Tộc", "Nguyên Anh Hậu Kỳ"),
        ("Nguyễn Kỳ Lân", "阮麒麟", "Trưởng Lão Ngự Thú Viện", "Nhân Tộc", "Nguyên Anh Trung Kỳ"),
        ("Đặng Xà Vương", "鄧蛇王", "Trưởng Lão", "Nhân Tộc", "Nguyên Anh Sơ Kỳ"),
        ("Vũ Tiểu Long", "武小龍", "Nội Môn Đệ Tử", "Nhân Tộc", "Kim Đan Sơ Kỳ"),
        ("Lê Phượng Nhi", "黎鳳兒", "Ngoại Môn Đệ Tử", "Nhân Tộc", "Trúc Cơ Hậu Kỳ"),
    ]),

    # ============================================================
    # 6. Cự Tộc Thợ Xây - Cự Tộc builders, Hạng Năm -> SMALL (3 chars)
    # ============================================================
    ("Cự_Tộc_Thợ_Xây", "Cự Tộc Thợ Xây", [
        ("Thạch Lực", "石力", "Phường Trưởng", "Cự Tộc", "Trúc Cơ Hậu Kỳ"),
        ("Nham Đại Chùy", "岩大錘", "Thợ Cả", "Cự Tộc", "Trúc Cơ Trung Kỳ"),
        ("Sơn Thiết Bích", "山鐵壁", "Thợ Xây", "Cự Tộc", "Trúc Cơ Sơ Kỳ"),
    ]),

    # ============================================================
    # 7. Cửu Hoa Kiếm Tông - Nhân Tộc sword sect, Hạng Nhất, pop 5000 -> LARGE (10 chars)
    # ============================================================
    ("Cửu_Hoa_Kiếm_Tông", "Cửu Hoa Kiếm Tông", [
        ("Lý Lục Trần", "李六塵", "Tông Chủ", "Nhân Tộc", "Luyện Hư Sơ Kỳ"),
        ("Trần Cửu Hoa", "陳九花", "Thái Thượng Trưởng Lão", "Nhân Tộc", "Luyện Hư Sơ Kỳ"),
        ("Phạm Kiếm Tâm", "范劍心", "Hộ Pháp", "Nhân Tộc", "Nguyên Anh Đỉnh Phong"),
        ("Hoàng Thiên Phong", "黃天鋒", "Hộ Pháp", "Nhân Tộc", "Nguyên Anh Đỉnh Phong"),
        ("Nguyễn Tĩnh Kiếm", "阮靜劍", "Trưởng Lão Thiên Hoa Phong", "Nhân Tộc", "Nguyên Anh Hậu Kỳ"),
        ("Lê Hàn Sương", "黎寒霜", "Trưởng Lão", "Nhân Tộc", "Nguyên Anh Hậu Kỳ"),
        ("Vũ Phi Kiếm", "武飛劍", "Trưởng Lão", "Nhân Tộc", "Nguyên Anh Trung Kỳ"),
        ("Đặng Minh Nguyệt", "鄧明月", "Chân Truyền Đệ Tử", "Nhân Tộc", "Kim Đan Hậu Kỳ"),
        ("Trần Tiểu Kiếm", "陳小劍", "Nội Môn Đệ Tử", "Nhân Tộc", "Kim Đan Sơ Kỳ"),
        ("Lý Thanh Phong", "李青風", "Ngoại Môn Đệ Tử", "Nhân Tộc", "Trúc Cơ Hậu Kỳ"),
    ]),

    # ============================================================
    # 8. Độc Đảo Lưu Dân - Community on toxic island, no rank -> SMALL (3 chars)
    # ============================================================
    ("Độc_Đảo_Lưu_Dân", "Độc Đảo Lưu Dân", [
        ("Mạc Lão Đầu", "莫老頭", "Trưởng Thôn", "Nhân Tộc", "Luyện Khí Đỉnh Phong"),
        ("Mạc Tiểu Ngư", "莫小魚", "Ngư Dân", "Nhân Tộc", "Luyện Khí Trung Kỳ"),
        ("Mạc Dược Nương", "莫藥娘", "Thầy Thuốc", "Nhân Tộc", "Luyện Khí Hậu Kỳ"),
    ]),

    # ============================================================
    # 9. Độc Trùng Trị Liệu Đường - Healing with poison bugs, Hạng Năm -> SMALL (3 chars)
    # ============================================================
    ("Độc_Trùng_Trị_Liệu_Đường", "Độc Trùng Trị Liệu Đường", [
        ("Trùng Thanh Châm", "蟲青針", "Đường Chủ", "Trùng Tộc", "Trúc Cơ Hậu Kỳ"),
        ("Khuẩn Tiểu Linh", "菌小靈", "Dược Sư", "Trùng Tộc", "Trúc Cơ Sơ Kỳ"),
        ("Bào Hoàng Ty", "胞黃絲", "Học Đồ", "Trùng Tộc", "Luyện Khí Hậu Kỳ"),
    ]),

    # ============================================================
    # 10. Giáp Xác Liên Minh - Shell alliance, Hạng Năm -> SMALL (3 chars)
    # ============================================================
    ("Giáp_Xác_Liên_Minh", "Giáp Xác Liên Minh", [
        ("Xà Cương Giáp", "蛇鋼甲", "Minh Chủ", "Yêu Tộc", "Trúc Cơ Hậu Kỳ"),
        ("Quy Thiết Bối", "龜鐵背", "Phó Minh Chủ", "Yêu Tộc", "Trúc Cơ Trung Kỳ"),
        ("Giải Kiên Xác", "蟹堅殼", "Chiến Binh", "Yêu Tộc", "Trúc Cơ Sơ Kỳ"),
    ]),

    # ============================================================
    # 11. Hoang Dã Thợ Săn Bang - Hunter gang, Hạng Tư -> SMALL (4 chars)
    # ============================================================
    ("Hoang_Dã_Thợ_Săn_Bang", "Hoang Dã Thợ Săn Bang", [
        ("Lang Liệp Phong", "狼獵風", "Bang Chủ", "Yêu Tộc", "Kim Đan Sơ Kỳ"),
        ("Hổ Thiết Trảo", "虎鐵爪", "Phó Bang Chủ", "Yêu Tộc", "Trúc Cơ Viên Mãn"),
        ("Ưng Lợi Nhãn", "鷹利眼", "Trinh Sát Trưởng", "Yêu Tộc", "Trúc Cơ Hậu Kỳ"),
        ("Báo Khoái Đao", "豹快刀", "Sát Thủ", "Yêu Tộc", "Trúc Cơ Trung Kỳ"),
    ]),

    # ============================================================
    # 12. Hoàng Tuyền Cứu Hộ Đội - Rescue team, Hạng Năm -> SMALL (3 chars)
    # ============================================================
    ("Hoàng_Tuyền_Cứu_Hộ_Đội", "Hoàng Tuyền Cứu Hộ Đội", [
        ("Lý Bạch Cứu", "李白救", "Đội Trưởng", "Nhân Tộc", "Trúc Cơ Viên Mãn"),
        ("Trần Thiện Tâm", "陳善心", "Phó Đội Trưởng", "Nhân Tộc", "Trúc Cơ Hậu Kỳ"),
        ("Phạm Nhân Từ", "范仁慈", "Cứu Hộ Viên", "Nhân Tộc", "Trúc Cơ Sơ Kỳ"),
    ]),

    # ============================================================
    # 13. Hợp Hoan Tông - Charming sect, Hạng Nhì, pop 4000 -> MEDIUM (6 chars)
    # ============================================================
    ("Hợp_Hoan_Tông", "Hợp Hoan Tông", [
        ("Hồ Mị Cơ", "狐媚姬", "Tông Chủ", "Yêu Tộc", "Luyện Hư Sơ Kỳ"),
        ("Hồ Huyễn Nương", "狐幻娘", "Thái Thượng Trưởng Lão", "Yêu Tộc", "Nguyên Anh Đỉnh Phong"),
        ("Lý Xuân Phong", "李春風", "Hộ Pháp", "Nhân Tộc", "Nguyên Anh Hậu Kỳ"),
        ("Hồ Nguyệt Nhi", "狐月兒", "Trưởng Lão Hồng Phấn Các", "Yêu Tộc", "Nguyên Anh Trung Kỳ"),
        ("Phạm Diễm Tình", "范豔情", "Trưởng Lão", "Nhân Tộc", "Nguyên Anh Sơ Kỳ"),
        ("Hồ Tiểu Mị", "狐小媚", "Nội Môn Đệ Tử", "Yêu Tộc", "Kim Đan Sơ Kỳ"),
    ]),

    # ============================================================
    # 14. Huyết Sát Minh - Evil org, Hạng Nhất -> LARGE (10 chars)
    # ============================================================
    ("Huyết_Sát_Minh", "Huyết Sát Minh", [
        ("Lý Huyết Thần", "李血神", "Minh Chủ", "Nhân Tộc", "Luyện Hư Hậu Kỳ"),
        ("Trần Huyết Ảnh", "陳血影", "Tả Sứ", "Nhân Tộc", "Hóa Thần Sơ Kỳ"),
        ("Phạm Huyết Đao", "范血刀", "Hữu Sứ", "Nhân Tộc", "Nguyên Anh Đỉnh Phong"),
        ("Lê Huyết La", "黎血羅", "Đường Chủ Sát Thủ Đường", "Nhân Tộc", "Nguyên Anh Hậu Kỳ"),
        ("Hoàng Huyết Yến", "黃血燕", "Đường Chủ Tình Báo Đường", "Nhân Tộc", "Nguyên Anh Hậu Kỳ"),
        ("Vũ Huyết Cuồng", "武血狂", "Đường Chủ Chiến Đấu Đường", "Nhân Tộc", "Nguyên Anh Trung Kỳ"),
        ("Đặng Huyết Linh", "鄧血靈", "Hộ Pháp", "Nhân Tộc", "Nguyên Anh Trung Kỳ"),
        ("Nguyễn Huyết Sát", "阮血煞", "Trưởng Lão", "Nhân Tộc", "Nguyên Anh Sơ Kỳ"),
        ("Lý Huyết Vũ", "李血雨", "Sát Thủ Tinh Nhuệ", "Nhân Tộc", "Kim Đan Hậu Kỳ"),
        ("Trần Tiểu Huyết", "陳小血", "Đệ Tử", "Nhân Tộc", "Kim Đan Sơ Kỳ"),
    ]),

    # ============================================================
    # 15. Huyết Thảo Đường - Blood herb hall, Hạng Năm -> SMALL (3 chars)
    # ============================================================
    ("Huyết_Thảo_Đường", "Huyết Thảo Đường", [
        ("Lý Thảo Tam", "李草三", "Đường Chủ", "Nhân Tộc", "Trúc Cơ Trung Kỳ"),
        ("Lý Huyết Dược", "李血藥", "Dược Sư", "Nhân Tộc", "Trúc Cơ Sơ Kỳ"),
        ("Trần Thảo Nhi", "陳草兒", "Học Đồ", "Nhân Tộc", "Luyện Khí Hậu Kỳ"),
    ]),

    # ============================================================
    # 16. Liệt Dương Tông - Fire sect, Hạng Nhì, pop 4500 -> MEDIUM (7 chars)
    # ============================================================
    ("Liệt_Dương_Tông", "Liệt Dương Tông", [
        ("Lê Dương Thiết", "黎陽鐵", "Tông Chủ", "Nhân Tộc", "Luyện Hư Sơ Kỳ"),
        ("Trần Viêm Đế", "陳炎帝", "Thái Thượng Trưởng Lão", "Nhân Tộc", "Nguyên Anh Đỉnh Phong"),
        ("Phạm Hỏa Liên", "范火蓮", "Hộ Pháp", "Nhân Tộc", "Nguyên Anh Hậu Kỳ"),
        ("Hoàng Dung Nham", "黃熔岩", "Hộ Pháp", "Nhân Tộc", "Nguyên Anh Hậu Kỳ"),
        ("Nguyễn Liệt Diễm", "阮烈焰", "Trưởng Lão Viêm Long Quân", "Nhân Tộc", "Nguyên Anh Trung Kỳ"),
        ("Đặng Xích Hỏa", "鄧赤火", "Trưởng Lão", "Nhân Tộc", "Nguyên Anh Sơ Kỳ"),
        ("Vũ Tiểu Viêm", "武小炎", "Chân Truyền Đệ Tử", "Nhân Tộc", "Kim Đan Hậu Kỳ"),
    ]),

    # ============================================================
    # 17. Linh Thú Mục Trường - Beast ranch, Hạng Năm -> SMALL (3 chars)
    # ============================================================
    ("Linh_Thú_Mục_Trường", "Linh Thú Mục Trường", [
        ("Ngưu Đại Lực", "牛大力", "Mục Trường Chủ", "Yêu Tộc", "Trúc Cơ Trung Kỳ"),
        ("Dương Tiểu Mục", "羊小牧", "Mục Đồng", "Yêu Tộc", "Trúc Cơ Sơ Kỳ"),
        ("Mã Phi Vân", "馬飛雲", "Thuần Thú Sư", "Yêu Tộc", "Luyện Khí Đỉnh Phong"),
    ]),

    # ============================================================
    # 18. Lông Vũ Phường - Feather workshop, Hạng Năm, Vũ Tộc -> SMALL (3 chars)
    # ============================================================
    ("Lông_Vũ_Phường", "Lông Vũ Phường", [
        ("Vũ Mao Nhi", "羽毛兒", "Phường Chủ", "Vũ Tộc", "Luyện Khí Đỉnh Phong"),
        ("Vũ Thái Vũ", "羽彩羽", "Thợ Dệt", "Vũ Tộc", "Luyện Khí Hậu Kỳ"),
        ("Vũ Tiểu Phong", "羽小風", "Học Đồ", "Vũ Tộc", "Luyện Khí Trung Kỳ"),
    ]),

    # ============================================================
    # 19. Lưu Vong Thuyền Đội - Exile fleet, Hạng Tư -> SMALL (4 chars)
    # ============================================================
    ("Lưu_Vong_Thuyền_Đội", "Lưu Vong Thuyền Đội", [
        ("Trần Vạn Lý", "陳萬里", "Thuyền Chủ", "Nhân Tộc", "Kim Đan Trung Kỳ"),
        ("Lý Hải Phong", "李海風", "Phó Thuyền Chủ", "Nhân Tộc", "Kim Đan Sơ Kỳ"),
        ("Phạm Ba Đào", "范波濤", "Hoa Tiêu Trưởng", "Nhân Tộc", "Trúc Cơ Hậu Kỳ"),
        ("Nguyễn Tiểu Ngư", "阮小魚", "Thủy Thủ", "Nhân Tộc", "Trúc Cơ Sơ Kỳ"),
    ]),

    # ============================================================
    # 20. Luyện Khí Đại Sư Hội (Thần Khí Phường) - Weapon forge, Hạng Nhất, pop 6000 -> MEDIUM (8 chars)
    # ============================================================
    ("Luyện_Khí_Đại_Sư_Hội", "Thần Khí Phường", [
        ("Lý Cơ Giới", "李機械", "Phường Chủ", "Nhân Tộc", "Luyện Hư Sơ Kỳ"),
        ("Trần Thiên Cơ", "陳天機", "Thái Thượng Trưởng Lão", "Nhân Tộc", "Nguyên Anh Đỉnh Phong"),
        ("Phạm Thiết Đúc", "范鐵鑄", "Trưởng Lão Cơ Giới Viện", "Nhân Tộc", "Nguyên Anh Hậu Kỳ"),
        ("Hoàng Thần Lô", "黃神爐", "Trưởng Lão", "Nhân Tộc", "Nguyên Anh Hậu Kỳ"),
        ("Nguyễn Đúc Kim", "阮鑄金", "Trưởng Lão", "Nhân Tộc", "Nguyên Anh Trung Kỳ"),
        ("Đặng Linh Cơ", "鄧靈機", "Trưởng Lão", "Nhân Tộc", "Nguyên Anh Sơ Kỳ"),
        ("Vũ Tiểu Đúc", "武小鑄", "Chân Truyền Đệ Tử", "Nhân Tộc", "Kim Đan Hậu Kỳ"),
        ("Lê Luyện Kim", "黎煉金", "Nội Môn Đệ Tử", "Nhân Tộc", "Kim Đan Sơ Kỳ"),
    ]),

    # ============================================================
    # 21. Mật Lâm Thợ Săn Hội - Forest hunter guild, Hạng Năm -> SMALL (3 chars)
    # ============================================================
    ("Mật_Lâm_Thợ_Săn_Hội", "Mật Lâm Thợ Săn Hội", [
        ("Lý Mã Lâm", "李馬林", "Hội Trưởng", "Nhân Tộc", "Trúc Cơ Hậu Kỳ"),
        ("Trần Sơn Cung", "陳山弓", "Phó Hội Trưởng", "Nhân Tộc", "Trúc Cơ Trung Kỳ"),
        ("Phạm Tiểu Liệp", "范小獵", "Thợ Săn", "Nhân Tộc", "Trúc Cơ Sơ Kỳ"),
    ]),

    # ============================================================
    # 22. Mật Ong Linh Đoàn - Bee spirit group, Hạng Năm -> SMALL (3 chars)
    # ============================================================
    ("Mật_Ong_Linh_Đoàn", "Mật Ong Linh Đoàn", [
        ("Trùng Mật Linh", "蟲蜜靈", "Ong Hậu", "Trùng Tộc", "Trúc Cơ Trung Kỳ"),
        ("Trùng Kim Phấn", "蟲金粉", "Ong Thợ Trưởng", "Trùng Tộc", "Trúc Cơ Sơ Kỳ"),
        ("Trùng Tiểu Mật", "蟲小蜜", "Ong Lính", "Trùng Tộc", "Luyện Khí Hậu Kỳ"),
    ]),

    # ============================================================
    # 23. Mật Phong Linh Đàn - Bee hive group, Hạng Năm -> SMALL (3 chars)
    # ============================================================
    ("Mật_Phong_Linh_Đàn", "Mật Phong Linh Đàn", [
        ("Trùng Kim Hoa", "蟲金花", "Ong Chúa", "Trùng Tộc", "Trúc Cơ Viên Mãn"),
        ("Trùng Hoàng Châm", "蟲黃針", "Ong Chiến Binh", "Trùng Tộc", "Trúc Cơ Sơ Kỳ"),
        ("Trùng Ngọt Sương", "蟲甜霜", "Ong Dưỡng Nhi", "Trùng Tộc", "Luyện Khí Hậu Kỳ"),
    ]),

    # ============================================================
    # 24. Mộc Diệp Thôn - Village community, Hạng Năm -> SMALL (4 chars)
    # ============================================================
    ("Mộc_Diệp_Thôn", "Mộc Diệp Thôn", [
        ("Lý Thanh Phong", "李清風", "Trưởng Lão", "Nhân Tộc", "Kim Đan Trung Kỳ"),
        ("Trần Mộc Diệp", "陳木葉", "Phó Trưởng Lão", "Nhân Tộc", "Trúc Cơ Viên Mãn"),
        ("Phạm Lâm Nhi", "范林兒", "Dược Sư", "Nhân Tộc", "Trúc Cơ Hậu Kỳ"),
        ("Nguyễn Tiểu Mộc", "阮小木", "Thôn Dân", "Nhân Tộc", "Luyện Khí Hậu Kỳ"),
    ]),

    # ============================================================
    # 25. Nam Cương Dược Sư Hội - Pharmacist guild, Hạng Năm -> SMALL (3 chars)
    # ============================================================
    ("Nam_Cương_Dược_Sư_Hội", "Nam Cương Dược Sư Hội", [
        ("Lê Dược Nương", "黎藥娘", "Hội Trưởng", "Nhân Tộc", "Trúc Cơ Hậu Kỳ"),
        ("Phạm Bách Thảo", "范百草", "Phó Hội Trưởng", "Nhân Tộc", "Trúc Cơ Trung Kỳ"),
        ("Hoàng Tiểu Dược", "黃小藥", "Dược Đồ", "Nhân Tộc", "Luyện Khí Đỉnh Phong"),
    ]),

    # ============================================================
    # 26. Ngoại Môn Đệ Tử Liên Minh - Secret alliance, no rank -> SMALL (3 chars)
    # ============================================================
    ("Ngoại_Môn_Đệ_Tử_Liên_Minh", "Ngoại Môn Đệ Tử Liên Minh", [
        ("Lý Ảnh Thủ", "李影首", "Minh Chủ", "Nhân Tộc", "Trúc Cơ Viên Mãn"),
        ("Trần Ám Vệ", "陳暗衛", "Phó Minh Chủ", "Nhân Tộc", "Trúc Cơ Hậu Kỳ"),
        ("Phạm Tiểu Ngạo", "范小傲", "Thành Viên", "Nhân Tộc", "Trúc Cơ Trung Kỳ"),
    ]),

    # ============================================================
    # 27. Ngọc Thạch Thợ Mỏ - Jade miners, Hạng Năm -> SMALL (3 chars)
    # ============================================================
    ("Ngọc_Thạch_Thợ_Mỏ", "Ngọc Thạch Thợ Mỏ", [
        ("Nham Ngọc Đục", "岩玉琢", "Phường Trưởng", "Cự Tộc", "Trúc Cơ Trung Kỳ"),
        ("Thạch Khoáng Sơn", "石礦山", "Thợ Mỏ Trưởng", "Cự Tộc", "Trúc Cơ Sơ Kỳ"),
        ("Sơn Tiểu Ngọc", "山小玉", "Thợ Mỏ", "Cự Tộc", "Luyện Khí Hậu Kỳ"),
    ]),

    # ============================================================
    # 28. Ngọc Trai Sâu Phường - Pearl worm workshop, no rank -> SMALL (3 chars)
    # ============================================================
    ("Ngọc_Trai_Sâu_Phường", "Ngọc Trai Sâu Phường", [
        ("Trùng Bạch", "蟲白", "Phường Chủ", "Trùng Tộc", "Trúc Cơ Trung Kỳ"),
        ("Trùng Ngọc Châu", "蟲玉珠", "Thợ Chế Tác", "Trùng Tộc", "Trúc Cơ Sơ Kỳ"),
        ("Trùng Tiểu Trai", "蟲小蚌", "Nuôi Trồng Viên", "Trùng Tộc", "Luyện Khí Hậu Kỳ"),
    ]),

    # ============================================================
    # 29. Ngự Kiếm Sơn Trang - Sword villa, Hạng Nhì, pop 2500 -> MEDIUM (6 chars)
    # ============================================================
    ("Ngự_Kiếm_Sơn_Trang", "Ngự Kiếm Sơn Trang", [
        ("Trần Kiếm Nam", "陳劍南", "Trang Chủ", "Nhân Tộc", "Luyện Hư Sơ Kỳ"),
        ("Lý Kiếm Hồn", "李劍魂", "Thái Thượng Trưởng Lão", "Nhân Tộc", "Nguyên Anh Đỉnh Phong"),
        ("Phạm Phi Kiếm", "范飛劍", "Trưởng Lão Kiếm Đúc Viện", "Nhân Tộc", "Nguyên Anh Hậu Kỳ"),
        ("Hoàng Thiên Hỏa", "黃天火", "Trưởng Lão", "Nhân Tộc", "Nguyên Anh Trung Kỳ"),
        ("Nguyễn Thanh Luyện", "阮青煉", "Chân Truyền Đệ Tử", "Nhân Tộc", "Kim Đan Hậu Kỳ"),
        ("Đặng Tiểu Kiếm", "鄧小劍", "Nội Môn Đệ Tử", "Nhân Tộc", "Trúc Cơ Hậu Kỳ"),
    ]),

    # ============================================================
    # 30. Nham Thạch Tiểu Đội - Rock squad, Hạng Năm, pop 18 -> SMALL (3 chars)
    # ============================================================
    ("Nham_Thạch_Tiểu_Đội", "Nham Thạch Tiểu Đội", [
        ("Nham Cương", "岩鋼", "Đội Trưởng", "Thạch Tộc", "Trúc Cơ Hậu Kỳ"),
        ("Thạch Trấn Sơn", "石鎮山", "Phó Đội Trưởng", "Thạch Tộc", "Trúc Cơ Trung Kỳ"),
        ("Nham Tiểu Đá", "岩小石", "Tuần Tra Viên", "Thạch Tộc", "Trúc Cơ Sơ Kỳ"),
    ]),

    # ============================================================
    # 31. Ốc Đảo Hộ Vệ Đội - Oasis guard, no rank -> SMALL (3 chars)
    # ============================================================
    ("Ốc_Đảo_Hộ_Vệ_Đội", "Ốc Đảo Hộ Vệ Đội", [
        ("Trần Sa Nghĩa", "陳沙義", "Tổng Đội Trưởng", "Nhân Tộc", "Trúc Cơ Viên Mãn"),
        ("Lý Hoang Lực", "李荒力", "Phó Đội Trưởng", "Nhân Tộc", "Trúc Cơ Hậu Kỳ"),
        ("Phạm Tiểu Vệ", "范小衛", "Hộ Vệ", "Nhân Tộc", "Trúc Cơ Sơ Kỳ"),
    ]),

    # ============================================================
    # 32. Ốc Đảo Vi Linh - Tiny oasis spirits, no rank -> SMALL (3 chars)
    # ============================================================
    ("Ốc_Đảo_Vi_Linh", "Ốc Đảo Vi Linh", [
        ("Vi Linh Mẫu", "微靈母", "Linh Mẫu", "Vi Tộc", "Trúc Cơ Trung Kỳ"),
        ("Vi Ngọc Tuyền", "微玉泉", "Thủ Hộ", "Vi Tộc", "Trúc Cơ Sơ Kỳ"),
        ("Vi Tiểu Sa", "微小沙", "Linh Tộc", "Vi Tộc", "Luyện Khí Hậu Kỳ"),
    ]),

    # ============================================================
    # 33. Phản Độc Minh - Anti-poison alliance, Hạng Năm -> SMALL (3 chars)
    # ============================================================
    ("Phản_Độc_Minh", "Phản Độc Minh", [
        ("Lê Thiết Tâm", "黎鐵心", "Minh Chủ", "Nhân Tộc", "Trúc Cơ Sơ Kỳ"),
        ("Trần Chính Khí", "陳正氣", "Phó Minh Chủ", "Nhân Tộc", "Luyện Khí Đỉnh Phong"),
        ("Phạm Giải Độc", "范解毒", "Dược Sư", "Nhân Tộc", "Luyện Khí Hậu Kỳ"),
    ]),

    # ============================================================
    # 34. Phản Sào Trùng Quần - Rebel bug tribe, Hạng Năm -> SMALL (3 chars)
    # ============================================================
    ("Phản_Sào_Trùng_Quần", "Phản Sào Trùng Quần", [
        ("Trùng Xích Giác", "蟲赤角", "Trùng Trưởng", "Trùng Tộc", "Trúc Cơ Hậu Kỳ"),
        ("Trùng Thanh Dực", "蟲青翼", "Chiến Binh Trưởng", "Trùng Tộc", "Trúc Cơ Sơ Kỳ"),
        ("Trùng Tiểu Phản", "蟲小反", "Trinh Sát", "Trùng Tộc", "Luyện Khí Hậu Kỳ"),
    ]),

    # ============================================================
    # 35. Pháo Đài Xanh Hội (Thanh Mộc Kỵ Sĩ Đoàn) - Green fort, Hạng Ba, pop 1200 -> SMALL (5 chars)
    # ============================================================
    ("Pháo_Đài_Xanh_Hội", "Thanh Mộc Kỵ Sĩ Đoàn", [
        ("Trần Đại Thạch", "陳大石", "Đoàn Trưởng", "Nhân Tộc", "Nguyên Anh Sơ Kỳ"),
        ("Lý Thanh Diệp", "李青葉", "Phó Đoàn Trưởng", "Nhân Tộc", "Kim Đan Hậu Kỳ"),
        ("Phạm Mộc Thuẫn", "范木盾", "Kỵ Sĩ Trưởng Khiên Xanh Đội", "Nhân Tộc", "Kim Đan Trung Kỳ"),
        ("Hoàng Lâm Vệ", "黃林衛", "Kỵ Sĩ", "Nhân Tộc", "Trúc Cơ Hậu Kỳ"),
        ("Nguyễn Tiểu Thảo", "阮小草", "Tân Binh", "Nhân Tộc", "Trúc Cơ Sơ Kỳ"),
    ]),

    # ============================================================
    # 36. Phế Độc Đường - Poison rebel hall, Hạng Tư -> SMALL (4 chars)
    # ============================================================
    ("Phế_Độc_Đường", "Phế Độc Đường", [
        ("Lê Vô Hận", "黎無恨", "Đường Chủ", "Nhân Tộc", "Kim Đan Sơ Kỳ"),
        ("Trần Độc Ảnh", "陳毒影", "Phó Đường Chủ", "Nhân Tộc", "Trúc Cơ Viên Mãn"),
        ("Phạm Huyền Châm", "范玄針", "Sát Thủ", "Nhân Tộc", "Trúc Cơ Hậu Kỳ"),
        ("Hoàng Tiểu Độc", "黃小毒", "Đệ Tử", "Nhân Tộc", "Trúc Cơ Sơ Kỳ"),
    ]),

    # ============================================================
    # 37. Phế Khí Luyện Đan Phường - Waste alchemy, Hạng Năm -> SMALL (3 chars)
    # ============================================================
    ("Phế_Khí_Luyện_Đan_Phường", "Phế Khí Luyện Đan Phường", [
        ("Lý Hoài Cựu", "李懷舊", "Phường Chủ", "Nhân Tộc", "Trúc Cơ Hậu Kỳ"),
        ("Trần Phế Lô", "陳廢爐", "Đan Sư", "Nhân Tộc", "Trúc Cơ Trung Kỳ"),
        ("Phạm Tiểu Đan", "范小丹", "Học Đồ", "Nhân Tộc", "Luyện Khí Đỉnh Phong"),
    ]),

    # ============================================================
    # 38. Phế Linh Các - Waste spirit pavilion, Hạng Năm, pop 200 -> SMALL (4 chars)
    # ============================================================
    ("Phế_Linh_Các", "Phế Linh Các", [
        ("Lạc Vô Danh", "洛無名", "Các Chủ", "Nhân Tộc", "Kim Đan Hậu Kỳ"),
        ("Trần Tàn Linh", "陳殘靈", "Đại Trưởng Lão", "Nhân Tộc", "Kim Đan Trung Kỳ"),
        ("Phạm Phế Căn", "范廢根", "Trưởng Lão", "Nhân Tộc", "Trúc Cơ Viên Mãn"),
        ("Lý Tiểu Phế", "李小廢", "Nội Môn Đệ Tử", "Nhân Tộc", "Trúc Cơ Sơ Kỳ"),
    ]),

    # ============================================================
    # 39. Phiêu Bạt Khách Sạn Liên Minh - Inn network, Hạng Năm -> SMALL (3 chars)
    # ============================================================
    ("Phiêu_Bạt_Khách_Sạn_Liên_Minh", "Phiêu Bạt Khách Sạn Liên Minh", [
        ("Trần Chưởng Quầy", "陳掌櫃", "Tổng Quản", "Nhân Tộc", "Trúc Cơ Viên Mãn"),
        ("Lý Túy Tiên", "李醉仙", "Chưởng Quầy Chi Nhánh", "Nhân Tộc", "Trúc Cơ Hậu Kỳ"),
        ("Phạm Tiểu Nhị", "范小二", "Tiểu Nhị", "Nhân Tộc", "Luyện Khí Hậu Kỳ"),
    ]),

    # ============================================================
    # 40. Quỷ Nhai Hội - Ghost cliff society, Hạng Ba -> MEDIUM (5 chars)
    # ============================================================
    ("Quỷ_Nhai_Hội", "Quỷ Nhai Hội", [
        ("Lý Quỷ Nhị", "李鬼二", "Quỷ Chủ", "Nhân Tộc", "Kim Đan Hậu Kỳ"),
        ("Trần Quỷ Diện", "陳鬼面", "Phó Quỷ Chủ", "Nhân Tộc", "Kim Đan Trung Kỳ"),
        ("Phạm Hắc Ảnh", "范黑影", "Đường Chủ Tình Báo", "Nhân Tộc", "Kim Đan Sơ Kỳ"),
        ("Hoàng Quỷ Thủ", "黃鬼手", "Sát Thủ Trưởng", "Nhân Tộc", "Trúc Cơ Viên Mãn"),
        ("Nguyễn Tiểu Quỷ", "阮小鬼", "Thành Viên", "Nhân Tộc", "Trúc Cơ Hậu Kỳ"),
    ]),

    # ============================================================
    # 41. Sơn Cốc Cự Tộc Ẩn Sĩ - Giant hermits, Hạng Ba -> SMALL (4 chars)
    # ============================================================
    ("Sơn_Cốc_Cự_Tộc_Ẩn_Sĩ", "Sơn Cốc Cự Tộc Ẩn Sĩ", [
        ("Thạch Tổ", "石祖", "Đại Trưởng Lão", "Cự Tộc", "Hóa Thần Trung Kỳ"),
        ("Nham Trường Lão", "岩長老", "Trưởng Lão", "Cự Tộc", "Nguyên Anh Hậu Kỳ"),
        ("Sơn Thiết Nhai", "山鐵崖", "Hộ Vệ", "Cự Tộc", "Nguyên Anh Sơ Kỳ"),
        ("Cương Tiểu Sơn", "鋼小山", "Thủ Vệ", "Cự Tộc", "Kim Đan Hậu Kỳ"),
    ]),

    # ============================================================
    # 42. Sương Khói Lữ Đoàn - Frost smoke brigade, Hạng Năm -> SMALL (3 chars)
    # ============================================================
    ("Sương_Khói_Lữ_Đoàn", "Sương Khói Lữ Đoàn", [
        ("Lý Vũ Hàn", "李雨寒", "Đoàn Trưởng", "Nhân Tộc", "Trúc Cơ Hậu Kỳ"),
        ("Trần Sương Phong", "陳霜風", "Phó Đoàn Trưởng", "Nhân Tộc", "Trúc Cơ Trung Kỳ"),
        ("Phạm Tiểu Sương", "范小霜", "Thành Viên", "Nhân Tộc", "Trúc Cơ Sơ Kỳ"),
    ]),

    # ============================================================
    # 43. Tằm Ti Dệt Phường - Silk weaving, Hạng Năm -> SMALL (3 chars)
    # ============================================================
    ("Tằm_Ti_Dệt_Phường", "Tằm Ti Dệt Phường", [
        ("Trùng Bạch Ti", "蟲白絲", "Tằm Mẫu", "Trùng Tộc", "Trúc Cơ Hậu Kỳ"),
        ("Trùng Kim Ti", "蟲金絲", "Thợ Dệt Trưởng", "Trùng Tộc", "Trúc Cơ Sơ Kỳ"),
        ("Trùng Tiểu Tằm", "蟲小蚕", "Thợ Dệt", "Trùng Tộc", "Luyện Khí Hậu Kỳ"),
    ]),

    # ============================================================
    # 44. Thạch Linh Đồng Tử Hội - Stone spirit kids, no rank -> SMALL (3 chars)
    # ============================================================
    ("Thạch_Linh_Đồng_Tử_Hội", "Thạch Linh Đồng Tử Hội", [
        ("Thạch Viên Viên", "石圓圓", "Đầu Lĩnh", "Cự Tộc", "Luyện Khí Trung Kỳ"),
        ("Nham Tiểu Đậu", "岩小豆", "Thành Viên", "Cự Tộc", "Luyện Khí Sơ Kỳ"),
        ("Sơn Tiểu Đá", "山小石", "Thành Viên", "Cự Tộc", "Luyện Khí Sơ Kỳ"),
    ]),

    # ============================================================
    # 45. Thạch Tâm Thủ Hộ Đoàn - Stone heart guardians, Hạng Năm -> SMALL (3 chars)
    # ============================================================
    ("Thạch_Tâm_Thủ_Hộ_Đoàn", "Thạch Tâm Thủ Hộ Đoàn", [
        ("Thạch Kiên", "石堅", "Đoàn Trưởng", "Cự Tộc", "Trúc Cơ Viên Mãn"),
        ("Nham Thiết Vệ", "岩鐵衛", "Phó Đoàn Trưởng", "Cự Tộc", "Trúc Cơ Hậu Kỳ"),
        ("Sơn Tiểu Hộ", "山小護", "Thủ Hộ", "Cự Tộc", "Trúc Cơ Sơ Kỳ"),
    ]),

    # ============================================================
    # 46. Thạch Tượng Thủ Vệ - Stone statue guards, Hạng Tư -> SMALL (4 chars)
    # ============================================================
    ("Thạch_Tượng_Thủ_Vệ", "Thạch Tượng Thủ Vệ", [
        ("Thạch Miên", "石眠", "Thủ Vệ Trưởng", "Cự Tộc", "Kim Đan Trung Kỳ"),
        ("Nham Tĩnh Lập", "岩靜立", "Phó Thủ Vệ", "Cự Tộc", "Trúc Cơ Viên Mãn"),
        ("Sơn Cổ Thạch", "山古石", "Thủ Vệ", "Cự Tộc", "Trúc Cơ Hậu Kỳ"),
        ("Thiết Tiểu Tượng", "鐵小像", "Thủ Vệ", "Cự Tộc", "Trúc Cơ Trung Kỳ"),
    ]),

    # ============================================================
    # 47. Thái Ất Môn - Top sect, Hạng Nhất, pop 12000 -> LARGE (10 chars)
    # ============================================================
    ("Thái_Ất_Môn", "Thái Ất Môn", [
        ("Lý Thanh Vân", "李青雲", "Chưởng Môn", "Nhân Tộc", "Luyện Hư Trung Kỳ"),
        ("Trần Thái Huyền", "陳太玄", "Thái Thượng Trưởng Lão", "Nhân Tộc", "Luyện Hư Sơ Kỳ"),
        ("Phạm Thiên Cơ", "范天機", "Thái Thượng Trưởng Lão", "Nhân Tộc", "Luyện Hư Sơ Kỳ"),
        ("Hoàng Bát Quái", "黃八卦", "Hộ Pháp", "Nhân Tộc", "Nguyên Anh Đỉnh Phong"),
        ("Nguyễn Tử Vi", "阮紫微", "Hộ Pháp", "Nhân Tộc", "Nguyên Anh Đỉnh Phong"),
        ("Đặng Huyền Thanh", "鄧玄清", "Trưởng Lão Thiên Cơ Các", "Nhân Tộc", "Nguyên Anh Hậu Kỳ"),
        ("Vũ Linh Bảo", "武靈寶", "Trưởng Lão", "Nhân Tộc", "Nguyên Anh Hậu Kỳ"),
        ("Lê Thái Ất", "黎太乙", "Trưởng Lão", "Nhân Tộc", "Nguyên Anh Trung Kỳ"),
        ("Trần Tiểu Quái", "陳小卦", "Chân Truyền Đệ Tử", "Nhân Tộc", "Kim Đan Hậu Kỳ"),
        ("Lý Minh Tinh", "李明星", "Nội Môn Đệ Tử", "Nhân Tộc", "Kim Đan Sơ Kỳ"),
    ]),

    # ============================================================
    # 48. Thần Mộc Ký Sinh Tộc - Parasitic tree tribe, no rank -> SMALL (3 chars)
    # ============================================================
    ("Thần_Mộc_Ký_Sinh_Tộc", "Thần Mộc Ký Sinh Tộc", [
        ("Vi Mộc", "微木", "Tộc Trưởng", "Vi Tộc", "Trúc Cơ Trung Kỳ"),
        ("Vi Ký Sinh", "微寄生", "Trưởng Lão", "Vi Tộc", "Trúc Cơ Sơ Kỳ"),
        ("Vi Tiểu Mộc", "微小木", "Tộc Dân", "Vi Tộc", "Luyện Khí Hậu Kỳ"),
    ]),

    # ============================================================
    # 49. Thanh Đế Cung - Top sect, Hạng Nhất, pop 8000 -> LARGE (10 chars)
    # ============================================================
    ("Thanh_Đế_Cung", "Thanh Đế Cung", [
        ("Lý Mộc Thanh", "李木青", "Cung Chủ", "Nhân Tộc", "Luyện Hư Trung Kỳ"),
        ("Trần Thanh Tiên", "陳青仙", "Thái Thượng Trưởng Lão", "Nhân Tộc", "Luyện Hư Sơ Kỳ"),
        ("Tinh Vạn Diệp", "星萬葉", "Thái Thượng Trưởng Lão", "Tinh Linh Tộc", "Luyện Hư Sơ Kỳ"),
        ("Phạm Thanh Hoa", "范青花", "Hộ Pháp", "Nhân Tộc", "Nguyên Anh Đỉnh Phong"),
        ("Hoàng Mộc Linh", "黃木靈", "Trưởng Lão Dược Tiên Viện", "Nhân Tộc", "Nguyên Anh Hậu Kỳ"),
        ("Nguyệt Thường Xuân", "月長春", "Trưởng Lão", "Tinh Linh Tộc", "Nguyên Anh Hậu Kỳ"),
        ("Nguyễn Thanh Trúc", "阮青竹", "Trưởng Lão", "Nhân Tộc", "Nguyên Anh Trung Kỳ"),
        ("Lê Dược Tiên", "黎藥仙", "Trưởng Lão", "Nhân Tộc", "Nguyên Anh Sơ Kỳ"),
        ("Đặng Thanh Liên", "鄧青蓮", "Chân Truyền Đệ Tử", "Nhân Tộc", "Kim Đan Hậu Kỳ"),
        ("Vũ Tiểu Thanh", "武小青", "Nội Môn Đệ Tử", "Nhân Tộc", "Trúc Cơ Hậu Kỳ"),
    ]),

    # ============================================================
    # 50. Thanh Vân Nghĩa Đoàn - Volunteer militia, Hạng Năm -> SMALL (3 chars)
    # ============================================================
    ("Thanh_Vân_Nghĩa_Đoàn", "Thanh Vân Nghĩa Đoàn", [
        ("Lý Thiết Trụ", "李鐵柱", "Đoàn Trưởng", "Nhân Tộc", "Trúc Cơ Viên Mãn"),
        ("Trần Nghĩa Sĩ", "陳義士", "Phó Đoàn Trưởng", "Nhân Tộc", "Trúc Cơ Hậu Kỳ"),
        ("Phạm Tiểu Dũng", "范小勇", "Nghĩa Quân", "Nhân Tộc", "Trúc Cơ Sơ Kỳ"),
    ]),

    # ============================================================
    # 51. Thiên Lý Truyền Thư Các - Messenger network, Hạng Năm -> SMALL (3 chars)
    # ============================================================
    ("Thiên_Lý_Truyền_Thư_Các", "Thiên Lý Truyền Thư Các", [
        ("Lý Phong Thư", "李風書", "Các Chủ", "Nhân Tộc", "Trúc Cơ Trung Kỳ"),
        ("Trần Phi Tín", "陳飛信", "Truyền Thư Sứ", "Nhân Tộc", "Trúc Cơ Sơ Kỳ"),
        ("Phạm Tiểu Nhạn", "范小雁", "Đưa Thư Viên", "Nhân Tộc", "Luyện Khí Hậu Kỳ"),
    ]),

    # ============================================================
    # 52. Thiên Trụ Hộ Vệ Đoàn - Military, Hạng Nhất, pop 50000 -> LARGE (10 chars)
    # ============================================================
    ("Thiên_Trụ_Hộ_Vệ_Đoàn", "Thiên Trụ Hộ Vệ Đoàn", [
        ("Lý Vô Nhai", "李無涯", "Đại Tướng Quân", "Nhân Tộc", "Luyện Hư Trung Kỳ"),
        ("Trần Thiên Giáp", "陳天甲", "Phó Tướng", "Nhân Tộc", "Luyện Hư Sơ Kỳ"),
        ("Phạm Thiết Thành", "范鐵城", "Tướng Quân Kiếm Trận", "Nhân Tộc", "Nguyên Anh Đỉnh Phong"),
        ("Hoàng Thạch Bích", "黃石壁", "Tướng Quân", "Nhân Tộc", "Nguyên Anh Đỉnh Phong"),
        ("Nham Cự Lực", "岩巨力", "Tướng Quân Cự Tộc", "Cự Tộc", "Nguyên Anh Hậu Kỳ"),
        ("Nguyễn Trấn Quan", "阮鎮關", "Uy Trưởng Cửa Ải", "Nhân Tộc", "Nguyên Anh Trung Kỳ"),
        ("Đặng Thiết Vệ", "鄧鐵衛", "Uy Trưởng", "Nhân Tộc", "Nguyên Anh Sơ Kỳ"),
        ("Vũ Phi Long", "武飛龍", "Hiệu Úy", "Nhân Tộc", "Kim Đan Hậu Kỳ"),
        ("Lê Trấn Sơn", "黎鎮山", "Hiệu Úy", "Nhân Tộc", "Kim Đan Trung Kỳ"),
        ("Trần Tiểu Binh", "陳小兵", "Binh Sĩ", "Nhân Tộc", "Trúc Cơ Hậu Kỳ"),
    ]),

    # ============================================================
    # 53. Thú Linh Sư Hội - Beast spirit teacher guild, Hạng Năm -> SMALL (3 chars)
    # ============================================================
    ("Thú_Linh_Sư_Hội", "Thú Linh Sư Hội", [
        ("Hổ Thú Ngữ", "虎獸語", "Hội Trưởng", "Yêu Tộc", "Trúc Cơ Viên Mãn"),
        ("Lang Linh Thông", "狼靈通", "Phó Hội Trưởng", "Yêu Tộc", "Trúc Cơ Hậu Kỳ"),
        ("Miêu Tiểu Linh", "貓小靈", "Thành Viên", "Yêu Tộc", "Trúc Cơ Sơ Kỳ"),
    ]),

    # ============================================================
    # 54. Thú Ngữ Thông Dịch Hội - Beast translator guild, Hạng Năm, pop 50 -> SMALL (3 chars)
    # ============================================================
    ("Thú_Ngữ_Thông_Dịch_Hội", "Thú Ngữ Thông Dịch Hội", [
        ("Ưng Đa Ngữ", "鷹多語", "Hội Trưởng", "Yêu Tộc", "Trúc Cơ Viên Mãn"),
        ("Xà Ngữ Âm", "蛇語音", "Dịch Giả Trưởng", "Yêu Tộc", "Trúc Cơ Hậu Kỳ"),
        ("Miêu Tiểu Dịch", "貓小譯", "Tập Sự", "Yêu Tộc", "Luyện Khí Đỉnh Phong"),
    ]),

    # ============================================================
    # 55. Thương Hội Bạch Lang - Wolf merchant guild, mid-tier -> MEDIUM (5 chars)
    # ============================================================
    ("Thương_Hội_Bạch_Lang", "Thương Hội Bạch Lang", [
        ("Trần Bạch Lang", "陳白狼", "Hội Trưởng (Đại Lang)", "Nhân Tộc", "Trúc Cơ Viên Mãn"),
        ("Lý Thiết Nha", "李鐵牙", "Quản Sự (Sói Đầu Đàn)", "Nhân Tộc", "Trúc Cơ Hậu Kỳ"),
        ("Phạm Bạch Vệ", "范白衛", "Hộ Vệ Cốt Cán (Sói Bạc)", "Nhân Tộc", "Trúc Cơ Trung Kỳ"),
        ("Hoàng Phong Hành", "黃風行", "Hộ Vệ Cốt Cán", "Nhân Tộc", "Trúc Cơ Sơ Kỳ"),
        ("Nguyễn Tiểu Sói", "阮小狼", "Hộ Vệ Ngoại Vi", "Nhân Tộc", "Luyện Khí Đỉnh Phong"),
    ]),

    # ============================================================
    # 56. Tiên Cầm Viện - Bird training, Hạng Ba, pop 2000 -> MEDIUM (5 chars)
    # ============================================================
    ("Tiên_Cầm_Viện", "Tiên Cầm Viện", [
        ("Lý Cầm Tiên", "李禽仙", "Viện Trưởng", "Nhân Tộc", "Nguyên Anh Đỉnh Phong"),
        ("Vũ Hạc Vũ", "羽鶴羽", "Hộ Pháp", "Vũ Tộc", "Nguyên Anh Hậu Kỳ"),
        ("Trần Ưng Phi", "陳鷹飛", "Trưởng Lão Linh Ca Đường", "Nhân Tộc", "Nguyên Anh Sơ Kỳ"),
        ("Phạm Phượng Ca", "范鳳歌", "Trưởng Lão", "Nhân Tộc", "Kim Đan Hậu Kỳ"),
        ("Ưng Tiểu Phi", "鷹小飛", "Đệ Tử", "Yêu Tộc", "Trúc Cơ Hậu Kỳ"),
    ]),

    # ============================================================
    # 57. Tiểu Cự Nhân Đoàn - Small giant group, Hạng Năm -> SMALL (3 chars)
    # ============================================================
    ("Tiểu_Cự_Nhân_Đoàn", "Tiểu Cự Nhân Đoàn", [
        ("Nham Tiểu Sơn", "岩小山", "Đoàn Trưởng", "Cự Tộc", "Trúc Cơ Viên Mãn"),
        ("Thạch Tiểu Lực", "石小力", "Phó Đoàn Trưởng", "Cự Tộc", "Trúc Cơ Hậu Kỳ"),
        ("Sơn Tiểu Nham", "山小岩", "Thành Viên", "Cự Tộc", "Trúc Cơ Sơ Kỳ"),
    ]),

    # ============================================================
    # 58. Tiểu Ngư Nhân Thôn - Small fish people village, no rank -> SMALL (3 chars)
    # ============================================================
    ("Tiểu_Ngư_Nhân_Thôn", "Tiểu Ngư Nhân Thôn", [
        ("Ngư Lão Vĩ", "魚老尾", "Thôn Trưởng", "Yêu Tộc", "Luyện Khí Hậu Kỳ"),
        ("Ngư Tiểu Lân", "魚小鱗", "Ngư Dân", "Yêu Tộc", "Luyện Khí Trung Kỳ"),
        ("Ngư Bạch San", "魚白珊", "Ngư Dân", "Yêu Tộc", "Luyện Khí Sơ Kỳ"),
    ]),

    # ============================================================
    # 59. Triều Tịch Quan Trắc Đài - Tide observatory, no rank -> SMALL (3 chars)
    # ============================================================
    ("Triều_Tịch_Quan_Trắc_Đài", "Triều Tịch Quan Trắc Đài", [
        ("Lý Vọng Nguyệt", "李望月", "Đài Trưởng", "Nhân Tộc", "Trúc Cơ Viên Mãn"),
        ("Trần Hải Triều", "陳海潮", "Quan Trắc Viên", "Nhân Tộc", "Trúc Cơ Trung Kỳ"),
        ("Phạm Tiểu Sóng", "范小浪", "Học Đồ", "Nhân Tộc", "Luyện Khí Hậu Kỳ"),
    ]),

    # ============================================================
    # 60. Trùng Cốc Tàn Binh - Bug valley remnants, Hạng Tư -> SMALL (4 chars)
    # ============================================================
    ("Trùng_Cốc_Tàn_Binh", "Trùng Cốc Tàn Binh", [
        ("Lê Thiết Giáp", "黎鐵甲", "Liên Minh Chủ", "Nhân Tộc", "Kim Đan Sơ Kỳ"),
        ("Trần Trùng Chiến", "陳蟲戰", "Phó Minh Chủ", "Nhân Tộc", "Trúc Cơ Viên Mãn"),
        ("Phạm Cương Binh", "范鋼兵", "Đội Trưởng", "Nhân Tộc", "Trúc Cơ Hậu Kỳ"),
        ("Hoàng Tiểu Giáp", "黃小甲", "Chiến Binh", "Nhân Tộc", "Trúc Cơ Sơ Kỳ"),
    ]),

    # ============================================================
    # 61. Tử Vong Chi Thung Lũng - Death valley, Hạng Nhì, pop 12500 -> LARGE (8 chars)
    # ============================================================
    ("Tử_Vong_Chi_Thung_Lũng", "Tử Vong Chi Thung Lũng", [
        ("Lý Thi Ma", "李屍魔", "Cốc Chủ", "Nhân Tộc", "Luyện Hư Sơ Kỳ"),
        ("Trần Thi Vương", "陳屍王", "Thái Thượng Trưởng Lão", "Thi Tộc", "Nguyên Anh Đỉnh Phong"),
        ("Phạm Hắc Cốt", "范黑骨", "Hộ Pháp", "Nhân Tộc", "Nguyên Anh Hậu Kỳ"),
        ("Hoàng Tử Linh", "黃死靈", "Hộ Pháp", "Thi Tộc", "Nguyên Anh Hậu Kỳ"),
        ("Nguyễn Vạn Thi", "阮萬屍", "Trưởng Lão Thi Khôi Đội", "Nhân Tộc", "Nguyên Anh Trung Kỳ"),
        ("Đặng Huyết Nhục", "鄧血肉", "Trưởng Lão", "Thi Tộc", "Nguyên Anh Sơ Kỳ"),
        ("Vũ Thi Khôi", "武屍傀", "Chân Truyền Đệ Tử", "Nhân Tộc", "Kim Đan Hậu Kỳ"),
        ("Lê Tiểu Thi", "黎小屍", "Nội Môn Đệ Tử", "Nhân Tộc", "Kim Đan Sơ Kỳ"),
    ]),

    # ============================================================
    # 62. Vạn Pháp Thư Quán - Library, Hạng Năm -> SMALL (3 chars)
    # ============================================================
    ("Vạn_Pháp_Thư_Quán", "Vạn Pháp Thư Quán", [
        ("Lý Thư Lão", "李書老", "Quán Chủ", "Nhân Tộc", "Kim Đan Trung Kỳ"),
        ("Trần Mặc Hương", "陳墨香", "Phó Quán Chủ", "Nhân Tộc", "Trúc Cơ Viên Mãn"),
        ("Phạm Tiểu Thư", "范小書", "Thủ Thư", "Nhân Tộc", "Trúc Cơ Hậu Kỳ"),
    ]),

    # ============================================================
    # 63. Vân Tông - Top sect, Hạng Nhất siêu cấp, pop 50000 -> LARGE (12 chars)
    # ============================================================
    ("Vân_Tông", "Vân Tông", [
        ("Lý Vân Thiên", "李雲天", "Tông Chủ", "Nhân Tộc", "Luyện Hư Hậu Kỳ"),
        ("Trần Thái Hư", "陳太虛", "Thái Thượng Trưởng Lão", "Nhân Tộc", "Luyện Hư Trung Kỳ"),
        ("Phạm Hạo Nhiên", "范浩然", "Thái Thượng Trưởng Lão", "Nhân Tộc", "Luyện Hư Sơ Kỳ"),
        ("Hoàng Vân Du", "黃雲遊", "Thái Thượng Trưởng Lão", "Nhân Tộc", "Luyện Hư Sơ Kỳ"),
        ("Nguyễn Thiên Kiếm", "阮天劍", "Hộ Pháp", "Nhân Tộc", "Hóa Thần Sơ Kỳ"),
        ("Đặng Vân Hải", "鄧雲海", "Hộ Pháp", "Nhân Tộc", "Nguyên Anh Đỉnh Phong"),
        ("Vũ Thanh Phong", "武清風", "Trưởng Lão Kiếm Đỉnh", "Nhân Tộc", "Nguyên Anh Đỉnh Phong"),
        ("Lê Vân Sơn", "黎雲山", "Trưởng Lão", "Nhân Tộc", "Nguyên Anh Hậu Kỳ"),
        ("Trần Thiên Vân", "陳天雲", "Trưởng Lão", "Nhân Tộc", "Nguyên Anh Trung Kỳ"),
        ("Phạm Vân Kiếm", "范雲劍", "Chân Truyền Đệ Tử", "Nhân Tộc", "Kim Đan Hậu Kỳ"),
        ("Hoàng Tiểu Vân", "黃小雲", "Nội Môn Đệ Tử", "Nhân Tộc", "Kim Đan Sơ Kỳ"),
        ("Lý Vân Phong", "李雲風", "Ngoại Môn Đệ Tử", "Nhân Tộc", "Trúc Cơ Hậu Kỳ"),
    ]),

    # ============================================================
    # 64. Vạn Trùng Cốc - Trùng Tộc hive, massive -> MEDIUM (6 chars)
    # ============================================================
    ("Vạn_Trùng_Cốc", "Vạn Trùng Cốc", [
        ("Trùng Mẫu", "蟲母", "Trùng Mẫu (Nữ Hoàng)", "Trùng Tộc", "Hóa Thần Trung Kỳ"),
        ("Trùng Nhện Chúa", "蟲蛛主", "Trùng Vương", "Trùng Tộc", "Nguyên Anh Đỉnh Phong"),
        ("Trùng Bọ Ngựa", "蟲螳螂", "Trùng Tướng", "Trùng Tộc", "Nguyên Anh Hậu Kỳ"),
        ("Trùng Cánh Cứng", "蟲甲蟲", "Trùng Tướng", "Trùng Tộc", "Nguyên Anh Trung Kỳ"),
        ("Trùng Độc Ong", "蟲毒蜂", "Trùng Tướng", "Trùng Tộc", "Nguyên Anh Sơ Kỳ"),
        ("Trùng Kiến Vương", "蟲蟻王", "Trùng Binh Trưởng", "Trùng Tộc", "Kim Đan Hậu Kỳ"),
    ]),

    # ============================================================
    # 65. Vạn Tượng Sâm La (Vạn Tượng La Bàn) - Assassin guild, Hạng Nhì, pop 3000 -> MEDIUM (6 chars)
    # ============================================================
    ("Vạn_Tượng_Sâm_La", "Vạn Tượng La Bàn", [
        ("Lý Chấp Kim", "李執金", "Hội Trưởng", "Nhân Tộc", "Luyện Hư Sơ Kỳ"),
        ("Trần Thiên Nhãn", "陳天眼", "Phó Hội Trưởng", "Nhân Tộc", "Nguyên Anh Đỉnh Phong"),
        ("Phạm Kim Đao", "范金刀", "Kim Đao Đội Trưởng", "Nhân Tộc", "Nguyên Anh Hậu Kỳ"),
        ("Hoàng Ám Ảnh", "黃暗影", "Ám Sát Trưởng", "Nhân Tộc", "Nguyên Anh Trung Kỳ"),
        ("Nguyễn Tầm Tung", "阮尋蹤", "Truy Tìm Chuyên Gia", "Nhân Tộc", "Nguyên Anh Sơ Kỳ"),
        ("Đặng Tiểu La", "鄧小羅", "Sát Thủ", "Nhân Tộc", "Kim Đan Hậu Kỳ"),
    ]),

    # ============================================================
    # 66. Vô Tranh Tự - Top temple, Hạng Nhất, pop 10000 -> LARGE (10 chars)
    # ============================================================
    ("Vô_Tranh_Tự", "Vô Tranh Tự", [
        ("Lý Vô Nhai", "李無崖", "Phương Trượng", "Nhân Tộc", "Luyện Hư Trung Kỳ"),
        ("Trần Vô Tướng", "陳無相", "Thái Thượng Trưởng Lão", "Nhân Tộc", "Luyện Hư Sơ Kỳ"),
        ("Phạm Vô Niệm", "范無念", "Thái Thượng Trưởng Lão", "Nhân Tộc", "Luyện Hư Sơ Kỳ"),
        ("Hoàng Kim Cương", "黃金剛", "Hộ Pháp La Hán Đường", "Nhân Tộc", "Nguyên Anh Đỉnh Phong"),
        ("Nguyễn Bát Nhã", "阮般若", "Hộ Pháp", "Nhân Tộc", "Nguyên Anh Đỉnh Phong"),
        ("Đặng Huệ Tâm", "鄧慧心", "Trưởng Lão", "Nhân Tộc", "Nguyên Anh Hậu Kỳ"),
        ("Vũ Giới Luật", "武戒律", "Giới Luật Viện Trưởng", "Nhân Tộc", "Nguyên Anh Hậu Kỳ"),
        ("Lê Thiền Định", "黎禪定", "Trưởng Lão", "Nhân Tộc", "Nguyên Anh Trung Kỳ"),
        ("Trần Tiểu Tăng", "陳小僧", "Đệ Tử", "Nhân Tộc", "Kim Đan Sơ Kỳ"),
        ("Lý Ngộ Không", "李悟空", "Tập Sự", "Nhân Tộc", "Trúc Cơ Hậu Kỳ"),
    ]),

    # ============================================================
    # 67. Vũ Hoàng Các - Sky clan, massive -> LARGE (8 chars)
    # ============================================================
    ("Vũ_Hoàng_Các", "Vũ Hoàng Các", [
        ("Vũ Thiên Hoàng", "羽天凰", "Vũ Hoàng", "Vũ Tộc", "Luyện Hư Hậu Kỳ"),
        ("Vũ Phong Dực", "羽風翼", "Dực Tướng Đông", "Vũ Tộc", "Luyện Hư Sơ Kỳ"),
        ("Vũ Lôi Vũ", "羽雷羽", "Dực Tướng Tây", "Vũ Tộc", "Hóa Thần Sơ Kỳ"),
        ("Vũ Quang Dực", "羽光翼", "Dực Tướng Nam", "Vũ Tộc", "Hóa Thần Sơ Kỳ"),
        ("Vũ Hàn Dực", "羽寒翼", "Dực Tướng Bắc", "Vũ Tộc", "Nguyên Anh Đỉnh Phong"),
        ("Vũ Thánh Phong", "羽聖風", "Thánh Phong Trưởng Lão", "Vũ Tộc", "Nguyên Anh Hậu Kỳ"),
        ("Vũ Thương Khung", "羽蒼穹", "Thương Khung Vệ Đội Trưởng", "Vũ Tộc", "Nguyên Anh Trung Kỳ"),
        ("Vũ Tiểu Vũ", "羽小羽", "Thường Dân", "Vũ Tộc", "Kim Đan Sơ Kỳ"),
    ]),

    # ============================================================
    # 68. Vu Tộc Chiếu Cáo (Vu Tộc Tế Đàn) - Shaman tribe, Hạng Ba, pop 3000 -> MEDIUM (5 chars)
    # ============================================================
    ("Vu_Tộc_Chiếu_Cáo", "Vu Tộc Tế Đàn", [
        ("Nham Vu Huyết", "岩巫血", "Đại Tế Tư", "Cự Tộc", "Nguyên Anh Đỉnh Phong"),
        ("Sơn Vu Cốt", "山巫骨", "Trưởng Lão", "Cự Tộc", "Nguyên Anh Trung Kỳ"),
        ("Thạch Vu Hỏa", "石巫火", "Trưởng Lão", "Cự Tộc", "Nguyên Anh Sơ Kỳ"),
        ("Cương Chiến Sĩ", "鋼戰士", "Chiến Vu Đội Trưởng", "Cự Tộc", "Kim Đan Hậu Kỳ"),
        ("Nham Tiểu Vu", "岩小巫", "Tập Sự Vu Sư", "Cự Tộc", "Trúc Cơ Hậu Kỳ"),
    ]),

    # ============================================================
    # 69. Vũ Tộc Lưu Dân Trại - Winged refugee camp, no rank -> SMALL (3 chars)
    # ============================================================
    ("Vũ_Tộc_Lưu_Dân_Trại", "Vũ Tộc Lưu Dân Trại", [
        ("Vũ Lạc Vũ", "羽落羽", "Trại Chủ", "Vũ Tộc", "Trúc Cơ Sơ Kỳ"),
        ("Vũ Đoạn Dực", "羽斷翼", "Phó Trại Chủ", "Vũ Tộc", "Luyện Khí Đỉnh Phong"),
        ("Vũ Tiểu Lạc", "羽小落", "Trại Dân", "Vũ Tộc", "Luyện Khí Trung Kỳ"),
    ]),
]


def main():
    total_created = 0
    for faction_dir, faction_name, characters in FACTIONS:
        faction_path = os.path.join(CHAR_DIR, faction_dir)
        os.makedirs(faction_path, exist_ok=True)
        for name, hantu, archetype, race, cultivation in characters:
            filename = name.replace(" ", "_") + ".md"
            filepath = os.path.join(faction_path, filename)
            content = make_char(name, hantu, archetype, race, cultivation, faction_name)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            total_created += 1
            print(f"  Created: {filepath}")
        print(f"[{faction_name}] -> {len(characters)} characters")
    print(f"\n=== TOTAL FILES CREATED: {total_created} ===")


if __name__ == "__main__":
    main()
