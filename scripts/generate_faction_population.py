#!/usr/bin/env python3
"""Generate stub character files for an entire faction population."""
import os, random, yaml, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# ── Vietnamese name components ──
SURNAMES = [
    'Nguyễn', 'Trần', 'Lê', 'Phạm', 'Hoàng', 'Đặng', 'Vương', 'Lý',
    'Chu', 'Mã', 'Vũ', 'Đoàn', 'Hà', 'Lâm', 'Tống', 'Đinh',
    'Bùi', 'Dương', 'Tạ', 'Hồ', 'Lưu', 'Tăng', 'Cao', 'Triệu',
    'Giang', 'Tô', 'Diệp', 'Từ', 'Quách', 'Thẩm', 'Nghiêm', 'La',
    'Tiêu', 'Hứa', 'Quan', 'Viên', 'Kiều', 'Tần', 'Mạc', 'Liễu',
]

GIVEN_FIRST = [
    'Thiên', 'Minh', 'Thanh', 'Hải', 'Phong', 'Vân', 'Tuyết', 'Ngọc',
    'Kim', 'Thiết', 'Huyền', 'Linh', 'Tĩnh', 'Kiếm', 'Hoa', 'Lan',
    'Xuân', 'Thu', 'Đông', 'Hạ', 'Sơn', 'Thủy', 'Hỏa', 'Mộc',
    'Thổ', 'Quang', 'Nguyệt', 'Tinh', 'Vũ', 'Phượng', 'Long', 'Hổ',
    'Bạch', 'Hắc', 'Hồng', 'Lam', 'Tử', 'Hoàng', 'Lục', 'Xích',
    'Trúc', 'Tùng', 'Mai', 'Liên', 'Cúc', 'Đào', 'Phúc', 'Đức',
    'Nhân', 'Nghĩa', 'Trí', 'Tín', 'Dũng', 'Cương', 'Nhu', 'Hiền',
    'Tuệ', 'An', 'Bình', 'Lạc', 'Khải', 'Chí', 'Viễn', 'Trường',
    'Đại', 'Tiểu', 'Ấu', 'Lão', 'Trung', 'Chính', 'Thuần', 'Nhã',
]

GIVEN_SECOND = [
    'Phong', 'Vân', 'Nguyệt', 'Hà', 'Sương', 'Tuyết', 'Vũ', 'Linh',
    'Đức', 'Tâm', 'Nhi', 'Hoa', 'Kiếm', 'Quang', 'Minh', 'Thanh',
    'Hải', 'Sơn', 'Thiên', 'Địa', 'Long', 'Phượng', 'Hổ', 'Lan',
    'Liên', 'Cúc', 'Trúc', 'Mai', 'Tùng', 'Bách', 'Ngọc', 'Châu',
    'Tín', 'Nghĩa', 'Nhân', 'Chí', 'An', 'Bình', 'Lạc', 'Hiền',
    'Dung', 'Diệu', 'Huy', 'Cường', 'Dũng', 'Vinh', 'Thịnh', 'Phúc',
    'Lộc', 'Thọ', 'Tài', 'Lương', 'Hùng', 'Anh', 'Kiệt', 'Tuấn',
    'Khôi', 'Hào', 'Trí', 'Tuệ', 'Định', 'Thái', 'Lôi', 'Điện',
]

# Phàm nhân simple names
PHAM_NHAN_PREFIXES = ['Tiểu', 'Lão', 'A', 'Bé']
PHAM_NHAN_NAMES = [
    'Đậu', 'Gạo', 'Mì', 'Muối', 'Đường', 'Cá', 'Tôm', 'Gà',
    'Bò', 'Lợn', 'Mèo', 'Chó', 'Ngựa', 'Dê', 'Trâu', 'Vịt',
    'Hoa', 'Lá', 'Cỏ', 'Cây', 'Đá', 'Sắt', 'Đồng', 'Bạc',
    'Sáng', 'Tối', 'Nắng', 'Mưa', 'Gió', 'Sương', 'Tuyết', 'Mây',
    'Núi', 'Sông', 'Suối', 'Biển', 'Ao', 'Hồ', 'Ruộng', 'Vườn',
    'Rèn', 'Búa', 'Dao', 'Kéo', 'Kim', 'Chỉ', 'Vải', 'Gỗ',
    'Lửa', 'Nước', 'Đất', 'Khói', 'Chổi', 'Nồi', 'Bếp', 'Chén',
    'Thùng', 'Gánh', 'Quang', 'Xe', 'Thuyền', 'Cầu', 'Đường', 'Phố',
]

PHAM_NHAN_JOBS = [
    'Tạp Dịch', 'Đầu Bếp', 'Phụ Bếp', 'Thợ Rèn', 'Thợ Mộc',
    'Giặt Giũ', 'Quét Dọn', 'Gánh Nước', 'Chăn Ngựa', 'Canh Cổng',
    'Trồng Rau', 'Nuôi Gà', 'Khuân Vác', 'Dệt Vải', 'Nấu Rượu',
    'Bán Hàng', 'Kế Toán', 'Truyền Tin', 'Quản Kho', 'Sửa Chữa',
    'Hái Thuốc', 'Phơi Dược Liệu', 'Đốn Củi', 'Xay Bột', 'Nấu Đan Lò',
    'Khâu Vá', 'Thêu Thùa', 'Chăm Vườn', 'Nuôi Linh Thú', 'Giao Hàng',
]

CULTIVATION_LEVELS = {
    'ngoai_mon': [
        ('Luyện Khí Sơ Kỳ', 14, 18),
        ('Luyện Khí Trung Kỳ', 16, 22),
        ('Luyện Khí Hậu Kỳ', 18, 25),
        ('Trúc Cơ Sơ Kỳ', 20, 30),
        ('Trúc Cơ Trung Kỳ', 22, 35),
    ],
    'tap_dich': [
        ('Phàm Nhân', 10, 80),
    ],
}


def generate_name(used_names, is_pham_nhan=False):
    """Generate a unique Vietnamese name."""
    for _ in range(1000):
        if is_pham_nhan and random.random() < 0.3:
            prefix = random.choice(PHAM_NHAN_PREFIXES)
            simple = random.choice(PHAM_NHAN_NAMES)
            name = f"{prefix} {simple}"
        else:
            surname = random.choice(SURNAMES)
            first = random.choice(GIVEN_FIRST)
            if random.random() < 0.6:
                second = random.choice(GIVEN_SECOND)
                name = f"{surname} {first} {second}"
            else:
                name = f"{surname} {first}"
        if name not in used_names:
            used_names.add(name)
            return name
    return None


def create_stub(filepath, name, cultivation, age, archetype, faction, division, job=None):
    """Write a stub character file."""
    hantu = ''  # Auto-fill later
    filename_safe = name.replace(' ', '_')

    if cultivation == 'Phàm Nhân':
        section3 = "## III. KỸ NĂNG & ĐỜI SỐNG\n*(Chưa xác định)*"
    else:
        section3 = "## III. NĂNG LỰC & CHIẾN ĐẤU\n*(Chưa xác định)*"

    position = job if job else archetype
    content = f"""---
type: character
name: {name}
hantu: ''
archetype: {archetype}
race: Nhân Tộc
dao_tam: ''
age: {age}
avatar: ''
arcs:
  - arc: 1
    status: Còn Sống
    cultivation: {cultivation}
    methods: []
    inventory: []
    stats: [0, 0, 0, 0, 0, 0]
    relationships: []
---

# {name}

## I. THÔNG TIN CƠ BẢN
- **Tên:** {name}
- **Chức Vụ:** {position} — {division}
- **Tu Vi:** {cultivation}
- **Phe Phái:** {faction}

## II. NGOẠI HÌNH & TÍNH CÁCH
*(Chưa xác định)*

{section3}

## IV. CÁC MỐI QUAN HỆ
*(Chưa xác định)*

## V. TIỂU SỬ & HÀNH TRÌNH
*(Chưa xác định)*
"""
    filepath.parent.mkdir(parents=True, exist_ok=True)
    filepath.write_text(content.strip() + '\n', encoding='utf-8')


def populate_faction(faction_name, region, output_dir, counts, faction_full_name=None):
    """
    counts = {
        'ngoai_mon': 800,
        'tap_dich': 8000,
    }
    """
    if faction_full_name is None:
        faction_full_name = faction_name

    out = ROOT / output_dir
    out.mkdir(parents=True, exist_ok=True)

    # Collect existing names
    used_names = set()
    for f in out.glob('*.md'):
        used_names.add(f.stem.replace('_', ' '))

    created = 0

    # Generate ngoại môn
    ngoai_count = counts.get('ngoai_mon', 0)
    for i in range(ngoai_count):
        name = generate_name(used_names, is_pham_nhan=False)
        if not name:
            break
        cult_level, age_min, age_max = random.choice(CULTIVATION_LEVELS['ngoai_mon'])
        age = random.randint(age_min, age_max)
        fpath = out / f"{name.replace(' ', '_')}.md"
        create_stub(fpath, name, cult_level, age, 'Ngoại Môn Đệ Tử', faction_full_name, 'Ngoại Môn Viện')
        created += 1

    # Generate tạp dịch / phàm nhân
    tap_count = counts.get('tap_dich', 0)
    for i in range(tap_count):
        name = generate_name(used_names, is_pham_nhan=True)
        if not name:
            break
        age = random.randint(10, 75)
        job = random.choice(PHAM_NHAN_JOBS)
        fpath = out / f"{name.replace(' ', '_')}.md"
        create_stub(fpath, name, 'Phàm Nhân', age, 'Phàm Nhân', faction_full_name, 'Hậu Cần Đường', job=job)
        created += 1

    return created


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 generate_faction_population.py <faction_config>")
        print("Example: python3 generate_faction_population.py cuu_hoa")
        sys.exit(1)

    config = sys.argv[1]

    if config == 'cuu_hoa':
        n = populate_faction(
            faction_name='Cửu Hoa Kiếm Tông',
            region='Đông_Hoang',
            output_dir='Đạo/Nhân_Vật/Đông_Hoang/Cửu_Hoa_Kiếm_Tông',
            counts={
                'ngoai_mon': 800,
                'tap_dich': 8000,
            },
            faction_full_name='Cửu Hoa Kiếm Tông',
        )
        print(f"Created {n} character stubs for Cửu Hoa Kiếm Tông")
    else:
        print(f"Unknown config: {config}")
        sys.exit(1)
