#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Move character files into region subfolders inside Đạo/Nhân_Vật/."""

import os
import re
import shutil

BASE = os.path.join(os.path.dirname(__file__), '..', 'Đạo', 'Nhân_Vật')
BASE = os.path.normpath(BASE)

# Map raw Khu Vực values to folder names
REGION_MAP = {
    'Đông Hoang': 'Đông_Hoang',
    'Vô Tận Hải': 'Vô_Tận_Hải',
    'Thiên Trụ': 'Thiên_Trụ',
    'Nam Cương': 'Nam_Cương',
    'Bắc Băng': 'Bắc_Băng',
    'Tây Mạc': 'Tây_Mạc',
    'Trung Tâm': 'Thiên_Trụ',  # Merge into Thiên Trụ
    'Lang thang': 'Tán_Tu',
}

def extract_region(filepath):
    """Extract Khu Vực value from a character .md file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    # Try to find **Khu Vực:** pattern
    m = re.search(r'\*\*Khu Vực:\*\*\s*(.+?)\.?\s*$', content, re.MULTILINE)
    if m:
        return m.group(1).strip().rstrip('.')
    return None

def main():
    # Create region folders
    for folder in set(REGION_MAP.values()):
        folder_path = os.path.join(BASE, folder)
        os.makedirs(folder_path, exist_ok=True)
        print(f"  Folder: {folder}")

    # Also create an "Khác" folder for unmatched
    os.makedirs(os.path.join(BASE, 'Khác'), exist_ok=True)

    moved = 0
    skipped = 0
    unknown = 0
    errors = []

    for fname in sorted(os.listdir(BASE)):
        if not fname.endswith('.md'):
            continue
        fpath = os.path.join(BASE, fname)
        if os.path.isdir(fpath):
            continue

        region = extract_region(fpath)
        if region and region in REGION_MAP:
            dest_folder = REGION_MAP[region]
        elif region:
            # Unknown region — put in Khác
            dest_folder = 'Khác'
            errors.append(f"  Unknown region '{region}' for {fname}")
            unknown += 1
        else:
            # No region found — put in Khác
            dest_folder = 'Khác'
            errors.append(f"  No region found for {fname}")
            unknown += 1

        dest_path = os.path.join(BASE, dest_folder, fname)
        if os.path.exists(dest_path):
            print(f"  SKIP (exists at dest): {fname}")
            skipped += 1
            continue

        shutil.move(fpath, dest_path)
        moved += 1

    print(f"\n{'='*50}")
    print(f"Moved: {moved}")
    print(f"Skipped: {skipped}")
    print(f"Unknown/No region: {unknown}")
    if errors:
        print("\nWarnings:")
        for e in errors:
            print(e)

    # Print counts per folder
    print(f"\nFiles per region folder:")
    for folder in sorted(os.listdir(BASE)):
        folder_path = os.path.join(BASE, folder)
        if os.path.isdir(folder_path):
            count = len([f for f in os.listdir(folder_path) if f.endswith('.md')])
            print(f"  {folder}: {count}")

if __name__ == '__main__':
    main()
