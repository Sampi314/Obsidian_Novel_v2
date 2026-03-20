#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audit character relationships for bidirectionality and consistency.

Scans all 1777+ character files, builds a directed relationship graph,
and detects:
  1. ONE_DIRECTIONAL: A→B exists but B→A doesn't
  2. MARKDOWN_ONLY: relationship in markdown Section VI but not in YAML
  3. NO_FEELINGS: YAML relationship exists but has no feelings values
  4. NAME_NOT_FOUND: referenced character doesn't match any known name

Usage:
  python scripts/audit_relationships.py [--summary] [--verbose] [--output FILE]
"""

import os
import re
import sys
import json
import yaml
from collections import defaultdict

BASE = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'Đạo', 'Nhân_Vật'))
REGIONS = ['Bắc_Băng', 'Nam_Cương', 'Thiên_Trụ', 'Đông_Hoang', 'Vô_Tận_Hải', 'Tây_Mạc', 'Tán_Tu']


def split_frontmatter(content):
    if not content.startswith('---'):
        return None, content
    end = content.find('\n---', 3)
    if end == -1:
        return None, content
    return content[4:end], content[end + 4:]


def normalize_name(name):
    """Normalize a character name for matching."""
    name = name.strip()
    # Remove parenthetical Chinese/explanations
    name = re.sub(r'\s*[\(（].*?[\)）]', '', name)
    # Remove quotes
    name = name.strip('"').strip('"').strip('"').strip("'").strip('*')
    # Remove trailing punctuation
    name = name.rstrip('.,:;—–')
    return name.strip()


def build_name_registry():
    """Walk all character files and build name→file mapping."""
    registry = {}  # canonical_name → {file, region, faction}
    alias_map = {}  # alias → canonical_name

    for region in REGIONS:
        region_path = os.path.join(BASE, region)
        if not os.path.isdir(region_path):
            continue
        for faction in sorted(os.listdir(region_path)):
            faction_path = os.path.join(region_path, faction)
            if not os.path.isdir(faction_path):
                continue
            for fname in sorted(os.listdir(faction_path)):
                if not fname.endswith('.md'):
                    continue
                fpath = os.path.join(faction_path, fname)
                try:
                    with open(fpath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    fm_str, _ = split_frontmatter(content)
                    if fm_str is None:
                        continue
                    data = yaml.safe_load(fm_str)
                    if not data or data.get('type') != 'character':
                        continue
                    name = data.get('name', fname[:-3].replace('_', ' '))
                    registry[name] = {
                        'file': fpath,
                        'region': region,
                        'faction': faction,
                    }
                    # Register aliases
                    aliases = data.get('aliases', [])
                    if isinstance(aliases, list):
                        for alias in aliases:
                            clean = normalize_name(str(alias))
                            if clean and clean != name:
                                alias_map[clean] = name
                except Exception:
                    continue

    return registry, alias_map


def resolve_name(name, registry, alias_map):
    """Try to resolve a relationship target name to a registered character."""
    clean = normalize_name(name)
    # Exact match
    if clean in registry:
        return clean
    # Alias match
    if clean in alias_map:
        return alias_map[clean]
    # Fuzzy: try without diacritics normalization (just strip extra spaces)
    for reg_name in registry:
        if reg_name.lower() == clean.lower():
            return reg_name
    return None


def extract_yaml_relationships(data):
    """Extract relationships from parsed YAML data."""
    rels = []
    arcs = data.get('arcs', [])
    if not arcs:
        return rels
    arc = arcs[0]
    yaml_rels = arc.get('relationships', [])
    if not yaml_rels:
        return rels
    for r in yaml_rels:
        if not isinstance(r, dict):
            continue
        target = r.get('character', '')
        desc = r.get('description', '')
        feelings = r.get('feelings', {})
        has_feelings = bool(feelings and any(v != 0 for v in feelings.values())) if isinstance(feelings, dict) else False
        rels.append({
            'target': normalize_name(target),
            'description': desc,
            'feelings': feelings if isinstance(feelings, dict) else {},
            'has_feelings': has_feelings,
            'source': 'yaml',
        })
    return rels


def extract_markdown_relationships(body):
    """Extract relationships from markdown Section VI or Section IV."""
    rels = []
    # Find Section VI (QUAN HỆ) or Section IV (CÁC MỐI QUAN HỆ)
    section_match = re.search(
        r'^## (?:VI|IV)\.?\s*(?:QUAN HỆ|CÁC MỐI QUAN HỆ)',
        body, re.MULTILINE
    )
    if not section_match:
        return rels

    # Get text from section start to next ## section
    start = section_match.end()
    next_section = re.search(r'^## ', body[start:], re.MULTILINE)
    section_text = body[start:start + next_section.start()] if next_section else body[start:]

    # Parse relationship entries: "- **Name...:**" or "- **Name** (Type):"
    pattern = r'-\s*\*\*([^*]+?)(?:\s*—[^:]*)?(?:\s*[\(（][^)）]*[\)）])?\s*:\*\*'
    alt_pattern = r'-\s*\*\*\[?([^\]]*?)\]?\*\*\s*(?:[\(（]([^)）]*)[\)）])?\s*:\s*(.+)'

    for m in re.finditer(pattern, section_text):
        name = normalize_name(m.group(1))
        if name and len(name) > 1:
            rels.append({
                'target': name,
                'description': '',
                'source': 'markdown',
            })

    if not rels:
        for m in re.finditer(alt_pattern, section_text):
            name = normalize_name(m.group(1))
            if name and len(name) > 1:
                rels.append({
                    'target': name,
                    'description': m.group(3).strip() if m.group(3) else '',
                    'source': 'markdown',
                })

    return rels


def main():
    verbose = '--verbose' in sys.argv
    summary_only = '--summary' in sys.argv
    output_file = None
    for i, arg in enumerate(sys.argv):
        if arg == '--output' and i + 1 < len(sys.argv):
            output_file = sys.argv[i + 1]

    print("Phase 1: Building name registry...")
    registry, alias_map = build_name_registry()
    print(f"  {len(registry)} characters registered, {len(alias_map)} aliases")

    print("Phase 2: Extracting all relationships...")
    # graph[source_name] = [{ target, description, feelings, source }]
    graph = defaultdict(list)
    yaml_edges = 0
    md_edges = 0

    for name, info in registry.items():
        try:
            with open(info['file'], 'r', encoding='utf-8') as f:
                content = f.read()
            fm_str, body = split_frontmatter(content)
            if fm_str is None:
                continue
            data = yaml.safe_load(fm_str)

            # YAML relationships
            yaml_rels = extract_yaml_relationships(data)
            yaml_targets = {r['target'] for r in yaml_rels}
            for r in yaml_rels:
                graph[name].append(r)
                yaml_edges += 1

            # Markdown relationships (only if not already in YAML)
            md_rels = extract_markdown_relationships(body)
            for r in md_rels:
                if r['target'] not in yaml_targets:
                    graph[name].append(r)
                    md_edges += 1

        except Exception as e:
            if verbose:
                print(f"  Error processing {name}: {e}")

    print(f"  {yaml_edges} YAML edges, {md_edges} markdown-only edges")

    print("Phase 3: Detecting issues...")
    issues = {
        'one_directional': [],
        'markdown_only': [],
        'no_feelings': [],
        'name_not_found': [],
    }

    all_edges = set()
    for source, rels in graph.items():
        for r in rels:
            target = r['target']
            resolved = resolve_name(target, registry, alias_map)

            if resolved is None:
                # Skip generic references (factions, "dân bảy thôn", etc.)
                if len(target) > 2 and not any(kw in target.lower() for kw in ['dân', 'thôn', 'tộc', 'hội', 'cung', 'môn', 'đoàn', 'đội', 'phường']):
                    issues['name_not_found'].append({
                        'character': source,
                        'references': target,
                        'source': r['source'],
                    })
                continue

            all_edges.add((source, resolved))

            if r['source'] == 'markdown':
                issues['markdown_only'].append({
                    'character': source,
                    'target': resolved,
                    'file': registry[source]['file'],
                })

            if r['source'] == 'yaml' and not r.get('has_feelings', False):
                issues['no_feelings'].append({
                    'character': source,
                    'target': resolved,
                })

    # Check bidirectionality
    for (a, b) in all_edges:
        if (b, a) not in all_edges:
            # Find the edge data
            edge_data = None
            for r in graph[a]:
                resolved = resolve_name(r['target'], registry, alias_map)
                if resolved == b:
                    edge_data = r
                    break
            issues['one_directional'].append({
                'from': a,
                'to': b,
                'from_region': registry[a]['region'],
                'to_region': registry[b]['region'] if b in registry else '?',
                'source': edge_data['source'] if edge_data else '?',
                'description': edge_data.get('description', '') if edge_data else '',
            })

    bidirectional = sum(1 for (a, b) in all_edges if (b, a) in all_edges) // 2
    stats = {
        'total_characters': len(registry),
        'total_edges': len(all_edges),
        'bidirectional_pairs': bidirectional,
        'one_directional': len(issues['one_directional']),
        'markdown_only': len(issues['markdown_only']),
        'no_feelings': len(issues['no_feelings']),
        'name_not_found': len(issues['name_not_found']),
    }

    report = {'stats': stats, 'issues': issues}

    # Print summary
    print(f"\n{'='*50}")
    print(f"RELATIONSHIP AUDIT REPORT")
    print(f"{'='*50}")
    print(f"  Characters scanned: {stats['total_characters']}")
    print(f"  Total relationship edges: {stats['total_edges']}")
    print(f"  Bidirectional pairs: {stats['bidirectional_pairs']}")
    print(f"  ONE-DIRECTIONAL (missing reciprocal): {stats['one_directional']}")
    print(f"  MARKDOWN-ONLY (not in YAML): {stats['markdown_only']}")
    print(f"  NO FEELINGS (YAML but no values): {stats['no_feelings']}")
    print(f"  NAME NOT FOUND: {stats['name_not_found']}")

    if not summary_only:
        if issues['one_directional']:
            print(f"\n--- ONE-DIRECTIONAL (top 30) ---")
            for item in issues['one_directional'][:30]:
                print(f"  {item['from']} → {item['to']}  [{item['source']}]  {item['description'][:60]}")

        if issues['name_not_found']:
            print(f"\n--- NAME NOT FOUND (top 20) ---")
            for item in issues['name_not_found'][:20]:
                print(f"  {item['character']} references '{item['references']}' [{item['source']}]")

    # Save report
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        print(f"\nFull report saved to: {output_file}")


if __name__ == '__main__':
    main()
