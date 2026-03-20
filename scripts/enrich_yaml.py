#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Enrich character YAML frontmatter by extracting info from markdown content.

Adds these fields (after 'race', before 'avatar'):
  - lingan: Linh Căn (spiritual root)
  - dao_tam: Đạo Tâm (core philosophy)
  - aliases: List of nicknames/titles
  - origin: Birth/home location
  - age: Current age (number or string)
  - faction_rank: Position in faction

Usage:
  python scripts/enrich_yaml.py [--dry-run] [--limit N] [--file PATH]
"""

import os
import re
import sys
import yaml

BASE = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'Đạo', 'Nhân_Vật'))
REGIONS = ['Bắc_Băng', 'Nam_Cương', 'Thiên_Trụ', 'Đông_Hoang', 'Vô_Tận_Hải', 'Tây_Mạc', 'Tán_Tu']


def split_frontmatter(content):
    """Split YAML frontmatter from markdown content."""
    if not content.startswith('---'):
        return None, content
    end = content.find('\n---', 3)
    if end == -1:
        return None, content
    fm_str = content[4:end]
    body = content[end + 4:]
    return fm_str, body


def extract_from_markdown(body):
    """Extract enrichment fields from markdown content."""
    info = {}

    # Extract aliases (Biệt Danh / Danh Hiệu)
    aliases = []
    for pattern in [
        r'\*\*Biệt Danh:\*\*\s*(.+)',
        r'\*\*Danh Hiệu:\*\*\s*(.+)',
        r'\*\*Tên Khai Sinh:\*\*\s*(.+)',
    ]:
        m = re.search(pattern, body)
        if m:
            raw = m.group(1).strip().rstrip('.')
            # Split by comma or 、
            parts = re.split(r'[,，、;]', raw)
            for p in parts:
                p = p.strip()
                if p and p != '*(Chưa xác định)*':
                    # Truncate at em-dash explanation
                    p = re.sub(r'\s*—\s*.{20,}$', '', p).strip()
                    # Clean surrounding quotes and markdown
                    p = p.strip('"').strip('"').strip('"').strip("'").strip('*').strip()
                    # Remove leading quote marks
                    p = re.sub(r'^[""\']+', '', p).strip()
                    if p and 2 < len(p) < 80 and p not in aliases:
                        aliases.append(p)
    if aliases:
        info['aliases'] = aliases

    # Extract age (Tuổi)
    m = re.search(r'\*\*Tuổi[^:]*:\*\*\s*[Kk]?hoảng\s*(\d+)', body)
    if not m:
        m = re.search(r'\*\*Tuổi[^:]*:\*\*\s*(\d+)', body)
    if not m:
        m = re.search(r'\*\*Tuổi/Thọ Nguyên:\*\*\s*(\d+)', body)
    if m:
        info['age'] = int(m.group(1))

    # Extract origin (Khu Vực / quê quán)
    m = re.search(r'\*\*Khu Vực:\*\*\s*(.+?)\.?\s*$', body, re.MULTILINE)
    if m:
        raw = m.group(1).strip().rstrip('.')
        # Remove very long descriptions, keep just the location name
        if len(raw) > 80:
            raw = raw.split('—')[0].split('–')[0].strip()
        if raw and raw != '*(Chưa xác định)*':
            info['origin'] = raw

    # Extract faction_rank (Chức Vụ / Thân Phận)
    m = re.search(r'\*\*Chức Vụ:\*\*\s*(.+?)\.?\s*$', body, re.MULTILINE)
    if not m:
        m = re.search(r'\*\*Thân Phận:\*\*\s*(.+?)\.?\s*$', body, re.MULTILINE)
    if m:
        raw = m.group(1).strip().rstrip('.')
        # Truncate at first sentence boundary or parenthetical
        for sep in [',', '，', '—', '–']:
            idx = raw.find(sep)
            if 0 < idx < 60:
                raw = raw[:idx].strip()
                break
        # Remove parenthetical Chinese if still too long
        if len(raw) > 60:
            raw = re.sub(r'\s*[\(（].*?[\)）]', '', raw).strip()
        if raw and raw != '*(Chưa xác định)*':
            info['faction_rank'] = raw

    # Extract Linh Căn
    m = re.search(r'\*\*Linh Căn:\*\*\s*(.+?)\.?\s*$', body, re.MULTILINE)
    if m:
        raw = m.group(1).strip().rstrip('.')
        # Truncate at em-dash or comma explanation
        raw = re.sub(r'\s*—\s*.{30,}$', '', raw).strip()
        if len(raw) > 60:
            for sep in [',', '，', '—', '–']:
                idx = raw.find(sep)
                if 0 < idx < 60:
                    raw = raw[:idx].strip()
                    break
        if raw and raw != '*(Chưa xác định)*' and 'Không có' not in raw and 'Không áp dụng' not in raw:
            info['lingan'] = raw

    # Extract Đạo Tâm
    m = re.search(r'\*\*Đạo Tâm:\*\*\s*\*?\*?"?(.+?)"?\*?\*?\s*$', body, re.MULTILINE)
    if not m:
        m = re.search(r'\*\*Đạo Tâm:\*\*\s*\*?\*?\s*"([^"]+)"', body)
    if not m:
        # Try finding the section header pattern
        m = re.search(r'Đạo Tâm.*?[""「]([^""」]+)[""」]', body)
    if m:
        raw = m.group(1).strip().strip('*').strip('"').strip('"').strip('"').strip()
        # Clean trailing punctuation and parenthetical
        raw = re.sub(r'[\.\s]*[\(（].*$', '', raw).strip().rstrip('.')
        # Clean all residual markdown formatting
        raw = raw.strip('*').strip('"').strip('"').strip('"').strip("'").strip('.').strip()
        if raw and 5 < len(raw) < 100 and raw != '*(Chưa xác định)*':
            info['dao_tam'] = raw

    return info


def enrich_yaml_str(fm_str, enrichment):
    """Insert new fields into YAML frontmatter string, preserving formatting."""
    lines = fm_str.split('\n')
    new_lines = []
    inserted = False

    # Fields to insert (in order)
    fields_to_add = []
    for key in ['lingan', 'dao_tam', 'aliases', 'origin', 'age', 'faction_rank']:
        if key in enrichment:
            fields_to_add.append((key, enrichment[key]))

    if not fields_to_add:
        return fm_str  # Nothing to add

    for line in lines:
        new_lines.append(line)
        # Insert after 'race:' line (before 'avatar:')
        if not inserted and line.startswith('race:'):
            for key, val in fields_to_add:
                if key == 'aliases' and isinstance(val, list):
                    new_lines.append(f'aliases:')
                    for a in val:
                        new_lines.append(f'  - "{a}"')
                elif isinstance(val, int):
                    new_lines.append(f'{key}: {val}')
                elif isinstance(val, str):
                    # Escape quotes in YAML
                    if ':' in val or '"' in val or "'" in val or '#' in val:
                        val_escaped = val.replace('"', '\\"')
                        new_lines.append(f'{key}: "{val_escaped}"')
                    else:
                        new_lines.append(f'{key}: {val}')
            inserted = True

    return '\n'.join(new_lines)


def process_file(fpath, dry_run=False):
    """Process a single character file."""
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    fm_str, body = split_frontmatter(content)
    if fm_str is None:
        return None, 'no frontmatter'

    # Check if already enriched
    if 'lingan:' in fm_str or 'dao_tam:' in fm_str or 'aliases:' in fm_str:
        return None, 'already enriched'

    # Extract info from markdown
    enrichment = extract_from_markdown(body)
    if not enrichment:
        return None, 'nothing to extract'

    # Enrich YAML
    new_fm = enrich_yaml_str(fm_str, enrichment)
    if new_fm == fm_str:
        return None, 'no changes'

    new_content = '---\n' + new_fm + '\n---' + body

    if not dry_run:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)

    return enrichment, 'updated'


def main():
    dry_run = '--dry-run' in sys.argv
    limit = None
    single_file = None

    for i, arg in enumerate(sys.argv):
        if arg == '--limit' and i + 1 < len(sys.argv):
            limit = int(sys.argv[i + 1])
        if arg == '--file' and i + 1 < len(sys.argv):
            single_file = sys.argv[i + 1]

    if single_file:
        enrichment, status = process_file(single_file, dry_run)
        print(f'{status}: {single_file}')
        if enrichment:
            for k, v in enrichment.items():
                print(f'  {k}: {v}')
        return

    count = 0
    updated = 0
    skipped = 0
    errors = 0

    for region in REGIONS:
        region_path = os.path.join(BASE, region)
        if not os.path.isdir(region_path):
            continue
        for faction in sorted(os.listdir(region_path)):
            fp = os.path.join(region_path, faction)
            if not os.path.isdir(fp):
                continue
            for fname in sorted(os.listdir(fp)):
                if not fname.endswith('.md'):
                    continue
                fpath = os.path.join(fp, fname)
                count += 1
                if limit and count > limit:
                    break

                try:
                    enrichment, status = process_file(fpath, dry_run)
                    if status == 'updated':
                        updated += 1
                        fields = list(enrichment.keys()) if enrichment else []
                        print(f'  ✓ {region}/{faction}/{fname}: +{", ".join(fields)}')
                    else:
                        skipped += 1
                except Exception as e:
                    errors += 1
                    print(f'  ✗ {region}/{faction}/{fname}: {e}')

    prefix = '[DRY RUN] ' if dry_run else ''
    print(f'\n{prefix}Done: {updated} updated, {skipped} skipped, {errors} errors (of {count} files)')


if __name__ == '__main__':
    main()
