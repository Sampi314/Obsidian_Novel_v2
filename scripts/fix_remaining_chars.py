#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Move remaining unfiled characters to their correct faction subfolders."""

import os
import shutil

BASE = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'Đạo', 'Nhân_Vật'))

# Manual mapping: (region, filename) -> faction_folder
MANUAL_MAP = {
    # Nam Cương
    ('Nam_Cương', 'Độc_Cô_Lão_Quái.md'): 'Vạn_Độc_Môn',
    ('Nam_Cương', 'Lệ_Vô_Tâm.md'): 'Vạn_Độc_Môn',
    ('Nam_Cương', 'Mặc_Dơi.md'): 'Vạn_Độc_Môn',
    ('Nam_Cương', 'Ngô_Công_Trưởng_Lão.md'): 'Vạn_Độc_Môn',
    ('Nam_Cương', 'Hắc_Hạt_Ma_Trùng.md'): 'Vạn_Độc_Môn',
    ('Nam_Cương', 'Đan_Dương_Tử.md'): 'Đan_Hà_Cốc',
    # Đông Hoang
    ('Đông_Hoang', 'Diệp_Thanh_Y.md'): 'Dược_Vương_Cốc',
    ('Đông_Hoang', 'Diệp_Tĩnh_Sương.md'): 'Tán_Tu',
    ('Đông_Hoang', 'Lâm_Phong.md'): 'Tán_Tu',
    ('Đông_Hoang', 'Lục_Ly.md'): 'Tinh_Linh_Vương_Đình',
    ('Đông_Hoang', 'Nham_Thần.md'): 'Độc_Lập',
    # Bắc Băng
    ('Bắc_Băng', 'Sở_Lăng_Sương.md'): 'Tán_Tu',
    ('Bắc_Băng', 'Triệu_Thanh_Hằng.md'): 'Tán_Tu',
    # Tây Mạc
    ('Tây_Mạc', 'Hứa_Nhược_Thủy.md'): 'San_Hô_Đảo_Quốc',
    ('Tây_Mạc', 'Hứa_Thanh_Vân.md'): 'San_Hô_Đảo_Quốc',
    # Vô Tận Hải
    ('Vô_Tận_Hải', 'Lệ_Nhược_Thủy.md'): 'Hải_Thần_Cung',
    ('Vô_Tận_Hải', 'Ngao_Đình.md'): 'Long_Cung',
    # Tán Tu (keep in region root or create Tán_Tu subfolder)
    ('Tán_Tu', 'A_Ngốc.md'): 'Tán_Tu',
    ('Tán_Tu', 'Hàn_Thanh_Nguyệt.md'): 'Tán_Tu',
    ('Tán_Tu', 'Phương_Vô_Kỵ.md'): 'Tán_Tu',
}

def main():
    moved = 0
    for (region, fname), faction_folder in MANUAL_MAP.items():
        src = os.path.join(BASE, region, fname)
        if not os.path.exists(src):
            print(f"  NOT FOUND: {region}/{fname}")
            continue

        dest_dir = os.path.join(BASE, region, faction_folder)
        os.makedirs(dest_dir, exist_ok=True)
        dest = os.path.join(dest_dir, fname)

        if os.path.exists(dest):
            print(f"  SKIP: {region}/{faction_folder}/{fname} exists")
            continue

        shutil.move(src, dest)
        print(f"  MOVED: {region}/{fname} -> {faction_folder}/")
        moved += 1

    # Also handle "Không" folders - rename to "Không_Rõ"
    # And clean up empty "Không" folders
    for region in os.listdir(BASE):
        region_path = os.path.join(BASE, region)
        if not os.path.isdir(region_path):
            continue
        khong_path = os.path.join(region_path, 'Không')
        if os.path.isdir(khong_path):
            files = os.listdir(khong_path)
            if files:
                # Move to Tán_Tu or Độc_Lập
                dest = os.path.join(region_path, 'Độc_Lập')
                os.makedirs(dest, exist_ok=True)
                for f in files:
                    src_f = os.path.join(khong_path, f)
                    dst_f = os.path.join(dest, f)
                    if not os.path.exists(dst_f):
                        shutil.move(src_f, dst_f)
                        print(f"  MOVED: {region}/Không/{f} -> Độc_Lập/")
                        moved += 1
            # Remove empty Không folder
            try:
                os.rmdir(khong_path)
                print(f"  REMOVED empty folder: {region}/Không/")
            except OSError:
                pass

    print(f"\nTotal moved: {moved}")

if __name__ == '__main__':
    main()
