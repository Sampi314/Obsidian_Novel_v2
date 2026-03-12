#!/usr/bin/env python3
"""
update_chapter_data.py
----------------------
Quét thư mục Đạo/Chương_Truyện/ để tự động sinh scripts/chapter_data.js.

Cách dùng (chạy từ gốc repo):
    python scripts/update_chapter_data.py
"""

import json
import os
import re

# ---------------------------------------------------------------------------
# Cấu hình
# ---------------------------------------------------------------------------
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHAPTER_BASE = os.path.join(REPO_ROOT, "Đạo", "Chương_Truyện")
OUTPUT_FILE = os.path.join(REPO_ROOT, "scripts", "chapter_data.js")

CHAPTER_FILE_RE = re.compile(r"^Chương_(\d+)_.+\.md$")
H1_TITLE_RE = re.compile(r"^#\s+Chương\s+\d+\s*:\s*(.+)$")


def extract_chapter_number(filename: str) -> int:
    """Trích số chương từ tên file, ví dụ Chương_00041_... -> 41."""
    m = CHAPTER_FILE_RE.match(filename)
    if m:
        return int(m.group(1))
    return 0


def read_title_from_file(filepath: str, filename: str) -> str:
    """Đọc dòng H1 đầu tiên khớp '# Chương N: Tiêu đề'.

    Nếu không tìm thấy, suy ra tiêu đề từ tên file.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                m = H1_TITLE_RE.match(line)
                if m:
                    chapter_num = extract_chapter_number(filename)
                    return f"Chương {chapter_num}: {m.group(1).strip()}"
    except OSError:
        pass

    # Fallback: suy từ tên file
    # Chương_00041_Mê_Cung_Tơ_Độc.md -> Mê Cung Tơ Độc
    name_no_ext = os.path.splitext(filename)[0]  # bỏ .md
    # Bỏ phần "Chương_NNNNN_"
    parts = name_no_ext.split("_", 2)  # ["Chương", "00041", "Mê_Cung_Tơ_Độc"]
    chapter_num = extract_chapter_number(filename)
    if len(parts) >= 3:
        title_part = parts[2].replace("_", " ")
    else:
        title_part = name_no_ext.replace("_", " ")
    return f"Chương {chapter_num}: {title_part}"


def scan_pov_directory(pov_path: str) -> list[dict]:
    """Quét 1 thư mục POV, trả về danh sách {filename, title} đã sắp xếp."""
    entries: list[dict] = []
    for fname in os.listdir(pov_path):
        if not CHAPTER_FILE_RE.match(fname):
            continue
        filepath = os.path.join(pov_path, fname)
        if not os.path.isfile(filepath):
            continue
        title = read_title_from_file(filepath, fname)
        entries.append({"filename": fname, "title": title})

    # Sắp xếp theo số chương
    entries.sort(key=lambda e: extract_chapter_number(e["filename"]))
    return entries


def main() -> None:
    if not os.path.isdir(CHAPTER_BASE):
        print(f"Lỗi: Không tìm thấy thư mục {CHAPTER_BASE}")
        return

    chapter_data: dict[str, list[dict]] = {}
    total = 0

    # Duyệt các thư mục khu vực, sau đó duyệt các thư mục POV bên trong
    for region_name in sorted(os.listdir(CHAPTER_BASE)):
        region_path = os.path.join(CHAPTER_BASE, region_name)
        if not os.path.isdir(region_path):
            continue
        for pov_name in sorted(os.listdir(region_path)):
            pov_path = os.path.join(region_path, pov_name)
            if not os.path.isdir(pov_path):
                continue
            entries = scan_pov_directory(pov_path)
            if not entries:
                continue
            chapter_data[pov_name] = entries
            total += len(entries)
            print(f"  {region_name}/{pov_name}: {len(entries)} chương")

    # Ghi ra file JS
    json_str = json.dumps(chapter_data, ensure_ascii=False, indent=2)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write('const chapterData = (typeof window !== "undefined" && window.chapterData) ? window.chapterData : {};\n')
        f.write(f'Object.assign(chapterData, {json_str});\n\n')
        f.write("if (typeof window !== 'undefined') {\n")
        f.write("  window.chapterData = chapterData;\n")
        f.write("}\n")
        f.write("export { chapterData };\n")

    print(f"\nTổng cộng: {total} chương ({len(chapter_data)} POV)")
    print(f"Đã ghi: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
