#!/usr/bin/env python3
"""
Pipeline: Sync character files → relationship_data.js

Scans Đạo/Nhân_Vật/**/*.md, extracts YAML frontmatter,
and merges into scripts/relationship_data.js.

Usage:
    python scripts/sync_relationship_data.py [--region REGION] [--dry-run] [--batch N]
    python scripts/sync_relationship_data.py --status
"""

import os, sys, re, json, subprocess, argparse, unicodedata

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SCRIPT_DIR)
CHAR_DIR = os.path.join(ROOT, "Đạo", "Nhân_Vật")
REL_DATA = os.path.join(ROOT, "scripts", "relationship_data.js")

REGION_MAP = {
    "Bắc_Băng": "Bắc Băng", "Đông_Hoang": "Đông Hoang",
    "Nam_Cương": "Nam Cương", "Tây_Mạc": "Tây Mạc",
    "Thiên_Trụ": "Thiên Trụ", "Vô_Tận_Hải": "Vô Tận Hải", "Tán_Tu": "Tán Tu",
}

ROLE_KEYWORDS = {
    "chủ": "leader", "trưởng": "leader", "vương": "leader",
    "minh chủ": "leader", "tộc trưởng": "leader",
    "hộ pháp": "combat", "chiến": "combat", "sát": "combat", "vệ": "combat",
    "trưởng lão": "key_member", "phó": "key_member",
    "dược": "support", "y sư": "support",
    "trinh sát": "scout", "thám": "scout",
}

REL_TYPE_MAP = {
    "kẻ thù": "enemy", "thù": "enemy", "đối đầu": "enemy", "căm": "enemy",
    "hận": "enemy", "tử địch": "enemy", "địch": "enemy",
    "đồng minh": "ally", "liên minh": "ally", "hợp tác": "ally",
    "bạn": "ally", "thân": "ally",
    "sư phụ": "mentor", "dạy": "mentor", "truyền": "mentor",
    "đệ tử": "disciple", "học trò": "disciple",
    "thuộc hạ": "subordinate", "phục tùng": "subordinate", "trung thành": "subordinate",
    "chỉ huy": "master", "lãnh đạo": "master", "thượng cấp": "master",
    "tôn kính": "master", "kính trọng": "master", "bảo vệ": "master",
    "cha": "family", "mẹ": "family", "con": "family", "huynh": "family",
    "đệ": "family", "vợ": "family", "chồng": "family",
    "đối thủ": "rival", "cạnh tranh": "rival", "kình": "rival",
    "nghi ngờ": "neutral", "trung lập": "neutral",
}

REALM_COLORS = {
    "Phàm Nhân": "#9e9e9e", "Luyện Khí": "#8bc34a", "Trúc Cơ": "#4caf50",
    "Kim Đan": "#ff9800", "Nguyên Anh": "#f44336", "Hóa Thần": "#9c27b0",
    "Luyện Hư": "#673ab7", "Đại Thừa": "#3f51b5", "Độ Kiếp": "#e91e63",
}


def name_to_id(name):
    s = unicodedata.normalize('NFKD', name.strip())
    ascii_str = ''.join(c for c in s if not unicodedata.combining(c))
    ascii_str = ascii_str.replace('Đ', 'D').replace('đ', 'd')
    result = re.sub(r'[^a-z0-9]+', '_', ascii_str.lower().strip()).strip('_')
    return result


def guess_role(archetype):
    if not archetype: return "member"
    lower = archetype.lower()
    for kw, role in ROLE_KEYWORDS.items():
        if kw in lower: return role
    return "member"


def guess_rel_type(desc):
    if not desc: return "neutral"
    lower = desc.lower()
    for kw, rt in REL_TYPE_MAP.items():
        if kw in lower: return rt
    return "ally"


def get_color(cultivation):
    if cultivation:
        for realm, color in REALM_COLORS.items():
            if realm in cultivation: return color
    return "#888888"


def parse_yaml(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except: return None
    match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not match: return None
    yaml_text = match.group(1)
    data = {}
    rels = []
    current_rel = {}
    for line in yaml_text.split('\n'):
        stripped = line.strip()
        if not stripped or stripped.startswith('#'): continue
        top = re.match(r'^(\w+):\s*(.*)', line)
        if top and not line.startswith(' '):
            data[top.group(1)] = top.group(2).strip().strip("'\"") or None
            continue
        rc = re.match(r'\s+-\s+character:\s*(.*)', line)
        if rc:
            if current_rel.get('character'):
                rels.append(dict(current_rel))
            current_rel = {'character': rc.group(1).strip().strip("'\"")}
            continue
        rd = re.match(r'\s+description:\s*(.*)', line)
        if rd:
            current_rel['description'] = rd.group(1).strip().strip("'\"")
            continue
        iv = re.match(r'\s+(\w+):\s*(.*)', line)
        if iv:
            k, v = iv.group(1), iv.group(2).strip().strip("'\"")
            if k == 'cultivation' and v: data['cultivation'] = v
    if current_rel.get('character'):
        rels.append(dict(current_rel))
    data['relationships_list'] = rels
    return data


def load_existing():
    try:
        node_script = """
        const fs = require('fs');
        const code = fs.readFileSync('./scripts/relationship_data.js', 'utf8');
        const fn = new Function(code + '; return relationshipData;');
        const d = fn();
        process.stdout.write(JSON.stringify(d));
        """
        result = subprocess.run(
            ['node', '-e', node_script],
            capture_output=True, text=True, cwd=ROOT, encoding='utf-8'
        )
        if result.returncode == 0 and result.stdout:
            return json.loads(result.stdout)
    except: pass
    return {"characters": [], "relationships": [], "factions": []}


def save_data(data):
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    with open(REL_DATA, 'w', encoding='utf-8') as f:
        f.write(f"const relationshipData = {json_str};\n")


def scan_chars(region_filter=None):
    results = []
    for rf in sorted(os.listdir(CHAR_DIR)):
        rp = os.path.join(CHAR_DIR, rf)
        if not os.path.isdir(rp): continue
        if region_filter and rf != region_filter: continue
        rd = REGION_MAP.get(rf, rf.replace('_', ' '))
        for ff in sorted(os.listdir(rp)):
            fp = os.path.join(rp, ff)
            if not os.path.isdir(fp): continue
            fd = ff.replace('_', ' ')
            for cf in sorted(os.listdir(fp)):
                if not cf.endswith('.md') or cf == 'index.md': continue
                parsed = parse_yaml(os.path.join(fp, cf))
                if parsed and parsed.get('name'):
                    results.append({'parsed': parsed, 'region': rd, 'faction': fd})
    return results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--region', help='Region folder name')
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--batch', type=int, default=0)
    parser.add_argument('--status', action='store_true')
    args = parser.parse_args()

    existing = load_existing()
    existing_ids = {c['id'] for c in existing['characters']}

    if args.status:
        all_c = scan_chars()
        synced = sum(1 for c in all_c if name_to_id(c['parsed']['name']) in existing_ids)
        print(f"Characters: {len(existing['characters'])} in data / {len(all_c)} on disk / {len(all_c)-synced} missing")
        print(f"Relationships: {len(existing['relationships'])}")
        regions = {}
        for c in all_c:
            r = c['region']
            if r not in regions: regions[r] = {'total': 0, 'synced': 0}
            regions[r]['total'] += 1
            if name_to_id(c['parsed']['name']) in existing_ids: regions[r]['synced'] += 1
        for r in sorted(regions):
            s = regions[r]
            pct = s['synced']/s['total']*100 if s['total'] else 0
            print(f"  {r}: {s['synced']}/{s['total']} ({pct:.0f}%)")
        return

    all_c = scan_chars(args.region)
    existing_rel_keys = {(r.get('source',''), r.get('target','')) for r in existing['relationships']}
    new_chars, new_rels, count = [], [], 0

    for entry in all_c:
        p = entry['parsed']
        cid = name_to_id(p['name'])
        if cid in existing_ids: continue
        new_chars.append({
            "id": cid, "name": p['name'], "title": p.get('archetype',''),
            "realm": p.get('cultivation','') or '', "faction": entry['faction'],
            "region": entry['region'], "role": guess_role(p.get('archetype','')),
            "pov": False, "avatar_color": get_color(p.get('cultivation',''))
        })
        existing_ids.add(cid)
        for rel in p.get('relationships_list', []):
            tid = name_to_id(rel.get('character',''))
            desc = rel.get('description','')
            key = (cid, tid)
            if key not in existing_rel_keys and (tid, cid) not in existing_rel_keys:
                new_rels.append({"source": cid, "target": tid, "type": guess_rel_type(desc), "description": desc})
                existing_rel_keys.add(key)
        count += 1
        if args.batch > 0 and count >= args.batch: break

    if args.dry_run:
        print(f"Would add {len(new_chars)} characters and {len(new_rels)} relationships")
        return

    if not new_chars:
        print("No new characters to add."); return

    existing['characters'].extend(new_chars)
    all_ids = {c['id'] for c in existing['characters']}
    valid = [r for r in new_rels if r['source'] in all_ids and r['target'] in all_ids]
    existing['relationships'].extend(valid)
    save_data(existing)
    print(f"Added {len(new_chars)} chars, {len(valid)} rels → Total: {len(existing['characters'])} chars, {len(existing['relationships'])} rels")


if __name__ == '__main__':
    main()
