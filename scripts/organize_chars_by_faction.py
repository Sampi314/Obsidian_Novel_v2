#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Move character files into faction subfolders within each region folder."""

import os
import re
import shutil

BASE = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'Đạo', 'Nhân_Vật'))

REGIONS = ['Bắc_Băng', 'Đông_Hoang', 'Nam_Cương', 'Tán_Tu', 'Tây_Mạc', 'Thiên_Trụ', 'Vô_Tận_Hải']

def extract_faction(filepath):
    """Extract Thế Lực value from a character .md file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    m = re.search(r'\*\*Thế Lực:\*\*\s*(.+?)\.?\s*$', content, re.MULTILINE)
    if m:
        return m.group(1).strip().rstrip('.')
    return None

def faction_to_folder(faction):
    """Convert faction name to folder-safe name (replace spaces with underscores)."""
    if not faction:
        return None
    return faction.replace(' ', '_')

def main():
    total_moved = 0
    total_skipped = 0
    no_faction = []

    for region in REGIONS:
        region_path = os.path.join(BASE, region)
        if not os.path.isdir(region_path):
            continue

        print(f"\n{'='*50}")
        print(f"REGION: {region}")
        print(f"{'='*50}")

        files = [f for f in sorted(os.listdir(region_path))
                 if f.endswith('.md') and os.path.isfile(os.path.join(region_path, f))]

        # First pass: collect all factions
        faction_map = {}  # filename -> faction folder name
        for fname in files:
            fpath = os.path.join(region_path, fname)
            faction = extract_faction(fpath)
            folder = faction_to_folder(faction)
            if folder:
                faction_map[fname] = folder
            else:
                no_faction.append(f"{region}/{fname}")

        # Create faction folders and move files
        created_folders = set()
        for fname, folder in faction_map.items():
            folder_path = os.path.join(region_path, folder)
            if folder not in created_folders:
                os.makedirs(folder_path, exist_ok=True)
                created_folders.add(folder)

            src = os.path.join(region_path, fname)
            dst = os.path.join(folder_path, fname)
            if os.path.exists(dst):
                print(f"  SKIP (exists): {fname}")
                total_skipped += 1
                continue
            shutil.move(src, dst)
            total_moved += 1

        # Print summary for this region
        for folder in sorted(created_folders):
            folder_path = os.path.join(region_path, folder)
            count = len([f for f in os.listdir(folder_path) if f.endswith('.md')])
            print(f"  {folder}: {count}")

    # Handle files with no faction
    if no_faction:
        print(f"\n{'='*50}")
        print(f"NO FACTION FOUND ({len(no_faction)} files left in region root):")
        for f in no_faction:
            print(f"  {f}")

    print(f"\n{'='*50}")
    print(f"Total moved: {total_moved}")
    print(f"Total skipped: {total_skipped}")
    print(f"No faction: {len(no_faction)}")

if __name__ == '__main__':
    main()
