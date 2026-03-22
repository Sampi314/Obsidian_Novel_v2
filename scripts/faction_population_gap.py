#!/usr/bin/env python3
"""Identify factions that need more named characters based on rank."""
import os, sys, re, yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Target named characters by rank
TARGETS = {
    'Hạng Nhất': 70,
    'Hạng Nhì': 35,
    'Hạng Ba': 18,
    'Hạng Tư': 10,
    'Hạng Năm': 6,
    'Không Xếp Hạng': 3,
}

def get_rank(text):
    for key in TARGETS:
        if key in text:
            return key
    return 'Không Xếp Hạng'

def count_chars(faction_name, region_dirs):
    """Count character files for a faction across all region directories."""
    total = 0
    safe_name = faction_name.replace(' ', '_')
    for rdir in region_dirs:
        char_dir = ROOT / 'Đạo' / 'Nhân_Vật' / rdir / safe_name
        if char_dir.is_dir():
            total += len([f for f in char_dir.glob('*.md')])
    return total

def scan_factions(region_filter=None):
    the_luc = ROOT / 'Đạo' / 'Thế_Lực'
    results = []

    # Map regions to character dirs
    region_map = {
        'Đông Hoang': ['Đông_Hoang'],
        'Nam Cương': ['Nam_Cương'],
        'Bắc Băng': ['Bắc_Băng'],
        'Tây Mạc': ['Tây_Mạc'],
        'Vô Tận Hải': ['Vô_Tận_Hải'],
        'Thiên Trụ': ['Thiên_Trụ'],
    }

    for region_dir in sorted(the_luc.iterdir()):
        if not region_dir.is_dir() or region_dir.name == '.git':
            continue
        region_name = region_dir.name.replace('_', ' ')
        if region_filter and region_filter.replace('_', ' ') != region_name:
            continue

        char_dirs = region_map.get(region_name, [region_dir.name])

        for f in sorted(region_dir.glob('*.md')):
            if f.name == 'index.md':
                continue
            try:
                text = f.read_text(encoding='utf-8')
                # Extract YAML
                if text.startswith('---'):
                    end = text.index('---', 3)
                    yml = yaml.safe_load(text[3:end])
                else:
                    continue

                name = yml.get('name', f.stem.replace('_', ' '))
                arcs = yml.get('arcs', [])
                rank_str = ''
                if arcs and isinstance(arcs, list) and len(arcs) > 0:
                    rank_str = str(arcs[0].get('rank', ''))

                rank = get_rank(rank_str)
                target = TARGETS.get(rank, 3)
                current = count_chars(name, char_dirs)
                gap = max(0, target - current)

                if gap > 0:
                    results.append({
                        'name': name,
                        'region': region_name,
                        'rank': rank,
                        'target': target,
                        'current': current,
                        'gap': gap,
                    })
            except Exception as e:
                pass

    # Sort by rank priority then gap size
    rank_order = list(TARGETS.keys())
    results.sort(key=lambda x: (rank_order.index(x['rank']), -x['gap']))
    return results

def main():
    region = sys.argv[1] if len(sys.argv) > 1 else None
    if region == 'all':
        region = None

    results = scan_factions(region)

    total_gap = sum(r['gap'] for r in results)
    print(f"{'Thế Lực':<35} {'Khu Vực':<15} {'Hạng':<20} {'Có':>4} {'Cần':>4} {'Thiếu':>5}")
    print('-' * 90)
    for r in results:
        print(f"{r['name']:<35} {r['region']:<15} {r['rank']:<20} {r['current']:>4} {r['target']:>4} {r['gap']:>5}")
    print('-' * 90)
    print(f"Tổng cần tạo: {total_gap} nhân vật | {len(results)} thế lực thiếu người")

if __name__ == '__main__':
    main()
