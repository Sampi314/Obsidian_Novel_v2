#!/usr/bin/env python3
"""
Batch migration script for Thế Lực files.
Adds skeleton YAML frontmatter to faction files that don't have one.

Usage:
    python scripts/migrate-factions.py                    # dry run (preview)
    python scripts/migrate-factions.py --apply            # apply changes
    python scripts/migrate-factions.py --apply --file X   # apply to single file
"""

import os
import re
import sys
import yaml

THE_LUC_DIR = os.path.join(os.path.dirname(__file__), '..', 'Đạo', 'Thế_Lực')

REGION_DEFAULTS = {
    'Băng': 'Bắc Băng', 'Tuyết': 'Bắc Băng', 'Hàn': 'Bắc Băng',
    'Sa': 'Tây Mạc', 'Mạc': 'Tây Mạc', 'Viêm': 'Tây Mạc',
    'Hải': 'Vô Tận Hải', 'Long': 'Vô Tận Hải', 'Kình': 'Vô Tận Hải',
}


def has_frontmatter(content):
    return content.strip().startswith('---')


def extract_h1(content):
    m = re.search(r'^#\s+(.+?)(?:\s*[\(（]([^)）]+)[\)）])?\s*$', content, re.MULTILINE)
    if m:
        return m.group(1).strip(), (m.group(2) or '').strip()
    return '', ''


def guess_region(name, content):
    for keyword, region in REGION_DEFAULTS.items():
        if keyword in name or keyword in content[:200]:
            return region
    return 'Đông Hoang'


def build_skeleton_yaml(name, hantu, region):
    return {
        'type': 'faction',
        'name': name or '???',
        'hantu': hantu or '',
        'faction_type': '',
        'alignment': 0,
        'race': '',
        'region': region,
        'founded': '',
        'founder': '',
        'emblem': '',
        'specialty': '',
        'economy': [],
        'arcs': [{
            'arc': 1,
            'status': 'Chưa Xác Định',
            'rank': '',
            'leader': '',
            'population': 0,
            'territory': [],
            'assets': [],
            'stats': [0, 0, 0, 0, 0, 0],
            'divisions': [],
            'relationships': [],
        }],
    }


def migrate_file(filepath, dry_run=True):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if has_frontmatter(content):
        return 'skip', 'already has frontmatter'

    name, hantu = extract_h1(content)
    region = guess_region(name, content)
    fm = build_skeleton_yaml(name, hantu, region)

    yaml_str = yaml.dump(fm, allow_unicode=True, default_flow_style=False, sort_keys=False)
    new_content = '---\n' + yaml_str + '---\n\n' + content

    if dry_run:
        return 'would_migrate', name
    else:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return 'migrated', name


def main():
    apply_mode = '--apply' in sys.argv
    single_file = None
    if '--file' in sys.argv:
        idx = sys.argv.index('--file')
        if idx + 1 < len(sys.argv):
            single_file = sys.argv[idx + 1]

    the_luc_dir = os.path.normpath(THE_LUC_DIR)
    files = sorted([
        os.path.join(the_luc_dir, f)
        for f in os.listdir(the_luc_dir)
        if f.endswith('.md') and f != 'index.md'
    ])

    if single_file:
        files = [f for f in files if os.path.basename(f) == single_file]
        if not files:
            print(f"File not found: {single_file}")
            sys.exit(1)

    stats = {'skip': 0, 'migrated': 0, 'would_migrate': 0}

    for filepath in files:
        status, info = migrate_file(filepath, dry_run=not apply_mode)
        stats[status] = stats.get(status, 0) + 1
        if status != 'skip':
            mode = 'MIGRATED' if status == 'migrated' else 'WOULD MIGRATE'
            print(f"  [{mode}] {os.path.basename(filepath)} — {info}")

    print(f"\n{'DRY RUN' if not apply_mode else 'APPLIED'}:")
    print(f"  Skipped (already has FM): {stats['skip']}")
    if apply_mode:
        print(f"  Migrated: {stats['migrated']}")
    else:
        print(f"  Would migrate: {stats['would_migrate']}")
    print(f"  Total files: {len(files)}")


if __name__ == '__main__':
    main()
