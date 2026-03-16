#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Find characters that still have placeholder text and need details filled in.
Usage: python3 scripts/find_unfilled_chars.py [count]
  count: number of characters to return (default: 3)
Outputs JSON array of {path, name, faction, region, faction_file} for unfilled chars.
"""

import os
import re
import json
import sys
import random

BASE = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'Đạo', 'Nhân_Vật'))
FACTIONS_DIR = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'Đạo', 'Thế_Lực'))

def find_faction_file(faction_name):
    """Find the faction .md file matching a faction name (searches region subdirs)."""
    target = faction_name.replace(' ', '_') + '.md'
    # Search in region subdirectories
    for entry in os.listdir(FACTIONS_DIR):
        subdir = os.path.join(FACTIONS_DIR, entry)
        if not os.path.isdir(subdir):
            continue
        candidate = os.path.join(subdir, target)
        if os.path.exists(candidate):
            return candidate
        # Try fuzzy match within subdir
        for f in os.listdir(subdir):
            if not f.endswith('.md'):
                continue
            name_part = f[:-3].replace('_', ' ')
            if name_part.lower() == faction_name.lower():
                return os.path.join(subdir, f)
    return None

def extract_field(content, field):
    """Extract a **Field:** value from content."""
    m = re.search(rf'\*\*{field}:\*\*\s*(.+?)\.?\s*$', content, re.MULTILINE)
    return m.group(1).strip().rstrip('.') if m else None

def is_unfilled(content):
    """Check if a character file still has placeholder text."""
    return '*(Chưa xác định)*' in content

def main():
    count = int(sys.argv[1]) if len(sys.argv) > 1 else 3

    unfilled = []
    regions = ['Nam_Cương', 'Thiên_Trụ', 'Đông_Hoang', 'Vô_Tận_Hải', 'Bắc_Băng', 'Tây_Mạc', 'Tán_Tu']

    for region in regions:
        region_path = os.path.join(BASE, region)
        if not os.path.isdir(region_path):
            continue
        for faction_folder in sorted(os.listdir(region_path)):
            faction_path = os.path.join(region_path, faction_folder)
            if not os.path.isdir(faction_path):
                continue
            for fname in sorted(os.listdir(faction_path)):
                if not fname.endswith('.md'):
                    continue
                fpath = os.path.join(faction_path, fname)
                with open(fpath, 'r', encoding='utf-8') as f:
                    content = f.read()
                if is_unfilled(content):
                    name = extract_field(content, 'Họ Tên') or fname[:-3].replace('_', ' ')
                    faction = extract_field(content, 'Thế Lực') or faction_folder.replace('_', ' ')
                    faction_file = find_faction_file(faction)
                    unfilled.append({
                        'path': fpath,
                        'name': name,
                        'faction': faction,
                        'faction_folder': faction_folder,
                        'region': region,
                        'faction_file': faction_file,
                    })

    # Group by faction and pick from same faction when possible
    # This ensures the agent can read one faction file and fill multiple chars
    by_faction = {}
    for c in unfilled:
        key = f"{c['region']}/{c['faction_folder']}"
        by_faction.setdefault(key, []).append(c)

    # Pick a faction group with unfilled chars, prefer groups with more chars
    faction_keys = list(by_faction.keys())
    if not faction_keys:
        print(json.dumps({"remaining": 0, "chars": []}, ensure_ascii=False, indent=2))
        return

    # Weight by count (bigger factions get picked more often)
    weights = [len(by_faction[k]) for k in faction_keys]
    chosen_key = random.choices(faction_keys, weights=weights, k=1)[0]
    chosen = by_faction[chosen_key][:count]

    result = {
        "remaining": len(unfilled),
        "total_factions_remaining": len(faction_keys),
        "chosen_faction": chosen_key,
        "chars": chosen,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
