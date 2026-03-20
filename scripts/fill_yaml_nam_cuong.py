#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fill YAML frontmatter for unfilled Nam Cương characters.
Reads existing markdown body content and generates appropriate YAML values.
"""

import os
import re
import random

BASE = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'Đạo', 'Nhân_Vật', 'Nam_Cương'))

# Stats ranges by cultivation level
STATS_RANGES = {
    'Luyện Khí Sơ Kỳ': (10, 60),
    'Luyện Khí Trung Kỳ': (30, 90),
    'Luyện Khí Hậu Kỳ': (50, 120),
    'Luyện Khí Đỉnh Phong': (80, 150),
    'Luyện Khí Viên Mãn': (100, 150),
    'Trúc Cơ Sơ Kỳ': (150, 300),
    'Trúc Cơ Trung Kỳ': (200, 350),
    'Trúc Cơ Hậu Kỳ': (250, 400),
    'Trúc Cơ Đỉnh Phong': (300, 450),
    'Trúc Cơ Viên Mãn': (350, 500),
    'Giả Đan Cảnh': (450, 600),
    'Kim Đan Sơ Kỳ': (600, 1000),
    'Kim Đan Trung Kỳ': (800, 1400),
    'Kim Đan Hậu Kỳ': (1000, 1600),
    'Kim Đan Đỉnh Phong': (1200, 1800),
    'Kim Đan Viên Mãn': (1400, 2000),
    'Nguyên Anh Sơ Kỳ': (2000, 3000),
    'Nguyên Anh Trung Kỳ': (2500, 3800),
    'Nguyên Anh Hậu Kỳ': (3000, 4500),
    'Nguyên Anh Đỉnh Phong': (3500, 5000),
    'Hóa Thần Sơ Kỳ': (5000, 8000),
    'Hóa Thần Trung Kỳ': (7000, 11000),
    'Hóa Thần Hậu Kỳ': (9000, 13000),
    'Hóa Thần Đỉnh Phong': (11000, 15000),
}


def get_cultivation(content):
    m = re.search(r'\*\*Tu Vi:\*\*\s*(.+?)\.?\s*$', content, re.MULTILINE)
    if m:
        return m.group(1).strip().rstrip('.')
    return None


def get_stat_range(cultivation):
    if not cultivation:
        return (100, 300)
    if cultivation in STATS_RANGES:
        return STATS_RANGES[cultivation]
    for key, val in STATS_RANGES.items():
        if key in cultivation or cultivation in key:
            return val
    for key, val in STATS_RANGES.items():
        parts = key.split()
        if len(parts) >= 2 and parts[0] in cultivation:
            return val
    return (100, 300)


def extract_section(content, section_num_start, section_num_end):
    """Extract content between two section headers"""
    pattern = rf'## {section_num_start}\..+?\n(.*?)(?=\n## {section_num_end}\.)'
    m = re.search(pattern, content, re.DOTALL)
    if m:
        return m.group(1).strip()
    return ''


def extract_methods_from_section3(content):
    """Extract cultivation methods from Section III only"""
    sec3 = extract_section(content, 'III', 'IV')
    if not sec3:
        return []

    methods = []
    # Find all occurrences of Chinese characters in parentheses
    # Then look backwards to find the Vietnamese technique name
    for match in re.finditer(r'[（(]([\u4e00-\u9fff]+)[)）]', sec3):
        han_chars = match.group(1)
        # Get the text before the parenthesis
        before = sec3[:match.start()].rstrip()
        # Extract the last few words (the technique name)
        # Split by common separators and take the technique name portion
        # Technique names are typically 3-6 Vietnamese words
        words = before.split()
        if len(words) < 2:
            continue

        # Try to find the technique name by looking for capitalized words
        # Vietnamese technique names start with capital letters
        technique_words = []
        for word in reversed(words):
            # Stop if we hit a non-technique word (lowercase, common words)
            if word[0].isupper() or (len(word) <= 2 and word[0].islower()):
                technique_words.insert(0, word)
            else:
                break
            if len(technique_words) >= 6:
                break

        viet_name = ' '.join(technique_words).strip()

        # Strip common prefixes
        prefixes = ['Tuyệt chiêu ', 'Chiêu thức ', 'Sở trường ',
                     'Kỹ thuật ', 'Công pháp ', 'Bí thuật ']
        for prefix in prefixes:
            if viet_name.startswith(prefix):
                viet_name = viet_name[len(prefix):]
                break

        # Validate
        if len(viet_name) >= 3 and ':' not in viet_name and len(viet_name) <= 40:
            methods.append(viet_name)

    # Deduplicate
    seen = set()
    unique = []
    for m_item in methods:
        if m_item not in seen:
            seen.add(m_item)
            unique.append(m_item)
    return unique[:3]


def extract_relationships_from_section4(content):
    """Extract relationships from Section IV"""
    sec4 = extract_section(content, 'IV', 'V')
    if not sec4:
        return []

    rels = []
    # Multiple patterns to handle different formatting styles:
    # 1. - **Name:** description
    # 2. - **[[Name]]** — description
    # 3. - **Name** — description
    patterns = [
        # Pattern for **Name:** desc (colon inside or outside bold)
        r'[-\*]\s*\*\*(?:\[\[)?([^\]\*\n]+?)(?:\]\])?\*\*:?\s*[—:\-]+\s*(.+?)(?:\n|$)',
        # Pattern for **Name:** desc (colon right after **)
        r'[-\*]\s*\*\*(?:\[\[)?([^\]\*\n]+?)(?:\]\])?:\*\*\s*(.+?)(?:\n|$)',
    ]
    for pattern in patterns:
        for match in re.finditer(pattern, sec4):
            char_name = match.group(1).strip().rstrip(':')
            desc = match.group(2).strip().rstrip('.')
            if char_name and desc and len(char_name) > 1 and len(desc) > 3:
                if not any(r['character'] == char_name for r in rels):
                    feelings = generate_feelings(desc)
                    rels.append({
                        'character': char_name,
                        'description': desc,
                        'feelings': feelings
                    })
        if rels:
            break  # Use first pattern that finds matches
    return rels


def generate_feelings(desc):
    """Generate feelings dict based on description keywords"""
    feelings = {'yeu': 0, 'han': 0, 'kinh': 0, 'tin': 0, 'so': 0, 'on': 0}
    desc_lower = desc.lower()

    # Family/protection bonds
    if any(w in desc_lower for w in ['em trai', 'em gái', 'bảo vệ', 'thân thiết', 'yêu thương', 'con trai', 'con gái', 'cha', 'mẹ', 'như con']):
        feelings['yeu'] = random.randint(50, 80)
        feelings['tin'] = random.randint(40, 70)
        feelings['on'] = random.randint(20, 50)
    # Respect
    if any(w in desc_lower for w in ['kính trọng', 'tôn kính', 'kính phục', 'ngưỡng mộ', 'tiền bối', 'tôn kính nhất']):
        feelings['kinh'] = random.randint(40, 80)
        feelings['tin'] = max(feelings['tin'], random.randint(30, 60))
    # Master-disciple
    if any(w in desc_lower for w in ['sư phụ', 'thầy', 'dạy dỗ', 'truyền thụ', 'truyền dạy', 'đào tạo']):
        feelings['kinh'] = max(feelings['kinh'], random.randint(50, 80))
        feelings['on'] = max(feelings['on'], random.randint(30, 60))
        feelings['tin'] = max(feelings['tin'], random.randint(20, 50))
    # Peers
    if any(w in desc_lower for w in ['đồng liêu', 'chiến hữu', 'đồng đội', 'sư huynh', 'sư tỷ', 'sư đệ', 'sư muội', 'đồng môn']):
        feelings['yeu'] = max(feelings['yeu'], random.randint(20, 50))
        feelings['tin'] = max(feelings['tin'], random.randint(20, 50))
    # Trust
    if any(w in desc_lower for w in ['trung thành', 'tín nhiệm', 'tin tưởng', 'đáng tin', 'đắc lực', 'cánh tay phải']):
        feelings['tin'] = max(feelings['tin'], random.randint(50, 80))
    # Friendship
    if any(w in desc_lower for w in ['bạn', 'tình bạn', 'kết bạn', 'bạn bè']):
        feelings['yeu'] = max(feelings['yeu'], random.randint(30, 60))
        feelings['tin'] = max(feelings['tin'], random.randint(20, 50))
    # Pride
    if any(w in desc_lower for w in ['tự hào', 'niềm tự hào', 'hy vọng']):
        feelings['yeu'] = max(feelings['yeu'], random.randint(50, 80))

    # Fear
    if any(w in desc_lower for w in ['sợ', 'khiếp sợ', 'sợ hãi', 'e ngại', 'sợ hãi tuyệt đối']):
        feelings['so'] = random.randint(40, 80)
    # Hatred
    if any(w in desc_lower for w in ['ghét', 'căm ghét', 'thù hận', 'kẻ thù', 'đối thủ']):
        feelings['han'] = random.randint(30, 70)
        feelings['yeu'] = min(feelings['yeu'], random.randint(-70, -30))
    # Suspicion
    if any(w in desc_lower for w in ['đề phòng', 'cảnh giác', 'nghi ngờ', 'tham vọng']):
        feelings['tin'] = min(feelings['tin'], random.randint(-50, -20))
    # Contempt
    if any(w in desc_lower for w in ['coi thường', 'khinh', 'bắt nạt']):
        feelings['kinh'] = min(feelings['kinh'], random.randint(-50, -20))
    # Authority
    if any(w in desc_lower for w in ['cấp trên', 'phục tùng', 'tuân lệnh', 'phục vụ']):
        feelings['kinh'] = max(feelings['kinh'], random.randint(20, 50))
    # Competition
    if any(w in desc_lower for w in ['ganh đua', 'cạnh tranh']):
        feelings['han'] = max(feelings['han'], random.randint(10, 30))
    # Cooperation
    if any(w in desc_lower for w in ['hợp tác', 'bổ sung', 'chỉ dạy']):
        feelings['tin'] = max(feelings['tin'], random.randint(20, 50))
        feelings['yeu'] = max(feelings['yeu'], random.randint(10, 30))
    # Shared burden
    if any(w in desc_lower for w in ['chia sẻ', 'gánh nặng']):
        feelings['tin'] = max(feelings['tin'], random.randint(40, 70))
        feelings['yeu'] = max(feelings['yeu'], random.randint(30, 60))
    # Appreciation
    if any(w in desc_lower for w in ['đánh giá cao', 'trọng dụng', 'tài năng']):
        feelings['kinh'] = max(feelings['kinh'], random.randint(20, 50))
        feelings['tin'] = max(feelings['tin'], random.randint(20, 40))

    return feelings


def generate_stats(cultivation, content):
    """Generate appropriate stats based on cultivation and character description"""
    lo, hi = get_stat_range(cultivation)
    content_lower = content.lower()

    mid = (lo + hi) // 2
    spread = (hi - lo) // 4
    stats = [
        random.randint(mid - spread, mid + spread),
        random.randint(mid - spread, mid + spread),
        random.randint(mid - spread, mid + spread),
        random.randint(mid - spread, mid + spread),
        random.randint(mid - spread, mid + spread),
        random.randint(mid - spread, mid + spread),
    ]

    # Physical fighters
    if any(w in content_lower for w in ['vạm vỡ', 'to lớn', 'chắc nịch', 'rắn rỏi', 'cận chiến', 'luyện thể', 'cơ bắp', 'mạnh mẽ']):
        stats[0] = min(hi, int(stats[0] * 1.3))
        stats[4] = min(hi, int(stats[4] * 1.2))
    # Strategists
    if any(w in content_lower for w in ['mưu trí', 'thông minh', 'quân sư', 'chiến thuật', 'tính toán', 'sắc sảo', 'tỉ mỉ']):
        stats[2] = min(hi, int(stats[2] * 1.3))
    # Speed
    if any(w in content_lower for w in ['nhanh', 'tốc độ', 'chớp nhoáng', 'ẩn thân', 'do thám', 'đánh lén']):
        stats[3] = min(hi, int(stats[3] * 1.3))
    # Alchemists
    if any(w in content_lower for w in ['đan sư', 'luyện đan', 'đan dược', 'dược']):
        stats[1] = min(hi, int(stats[1] * 1.2))
        stats[2] = min(hi, int(stats[2] * 1.2))
    # Strong will
    if any(w in content_lower for w in ['uy nghiêm', 'kiên định', 'bất khuất', 'ý chí', 'đạo tâm', 'lạnh lùng', 'tàn nhẫn']):
        stats[5] = min(hi, int(stats[5] * 1.3))
    # Weak physically
    if any(w in content_lower for w in ['gầy', 'mảnh mai', 'thể chất yếu', 'yếu ớt']):
        stats[0] = max(lo, int(stats[0] * 0.7))
    # Timid
    if any(w in content_lower for w in ['nhút nhát', 'sợ hãi', 'lo sợ', 'non nớt']):
        stats[5] = max(lo, int(stats[5] * 0.7))
    # Spirit users
    if any(w in content_lower for w in ['cổ trùng', 'độc', 'linh lực', 'nguyệt quang', 'huyết', 'vu thuật', 'hỏa']):
        stats[1] = min(hi, int(stats[1] * 1.2))
    # Defense
    if any(w in content_lower for w in ['phòng ngự', 'hộ pháp', 'kiên cố']):
        stats[4] = min(hi, int(stats[4] * 1.3))
    # Leaders
    if any(w in content_lower for w in ['lãnh đạo', 'trại chủ', 'bảo chủ', 'cốc chủ', 'đại tư tế', 'tông chủ', 'môn chủ']):
        stats[5] = min(hi, int(stats[5] * 1.2))
        stats[2] = min(hi, int(stats[2] * 1.1))

    stats = [max(lo, min(hi, s)) for s in stats]
    return stats


def rebuild_yaml_section(content, cultivation, stats, methods, relationships):
    """Rebuild the entire YAML arc section with proper data"""
    # Find the YAML frontmatter
    yaml_match = re.match(r'^---\n(.*?\n)---\n', content, re.DOTALL)
    if not yaml_match:
        return content

    yaml_text = yaml_match.group(1)
    after_yaml = content[yaml_match.end():]

    # Replace status
    yaml_text = yaml_text.replace('status: Chưa Xác Định', 'status: Còn Sống')

    # Fix methods - replace any existing methods line (possibly multi-line due to bug)
    # First, find and remove the old methods line(s)
    yaml_text = re.sub(r'    methods: \[.*?\]\n', '', yaml_text, flags=re.DOTALL)
    yaml_text = re.sub(r'    methods:.*?\n(?:.*?\n)*?(?=    inventory:)', '', yaml_text)

    # Fix stats
    yaml_text = re.sub(r'    stats: \[[\d, ]+\]', f'    stats: {stats}', yaml_text)

    # Fix relationships
    if relationships:
        rel_yaml = build_relationships_yaml(relationships)
        yaml_text = re.sub(r'    relationships: \[\]', rel_yaml, yaml_text)
        # Also handle existing relationships that were partially filled
        # (don't replace already-filled relationships)

    # Re-insert methods in the right place (after cultivation line)
    if methods:
        methods_str = '[' + ', '.join(methods) + ']'
        yaml_text = yaml_text.replace(
            f'    cultivation: {cultivation}\n',
            f'    cultivation: {cultivation}\n    methods: {methods_str}\n'
        )
    else:
        yaml_text = yaml_text.replace(
            f'    cultivation: {cultivation}\n',
            f'    cultivation: {cultivation}\n    methods: []\n'
        )

    return f'---\n{yaml_text}---\n{after_yaml}'


def build_relationships_yaml(relationships):
    """Build YAML string for relationships"""
    if not relationships:
        return '    relationships: []'

    lines = ['    relationships:']
    for rel in relationships:
        lines.append(f'      - character: {rel["character"]}')
        lines.append(f'        description: {rel["description"]}')
        lines.append(f'        feelings:')
        lines.append(f'          yeu: {rel["feelings"]["yeu"]}')
        lines.append(f'          han: {rel["feelings"]["han"]}')
        lines.append(f'          kinh: {rel["feelings"]["kinh"]}')
        lines.append(f'          tin: {rel["feelings"]["tin"]}')
        lines.append(f'          so: {rel["feelings"]["so"]}')
        lines.append(f'          on: {rel["feelings"]["on"]}')
    return '\n'.join(lines)


def process_character(path):
    """Process a single character file"""
    with open(path, 'r', encoding='utf-8') as fh:
        original_content = fh.read()

    # Force re-process: check if file has arc section with any of these markers
    # We want to re-process all files that were previously auto-filled
    has_arc = 'arcs:' in original_content and '  - arc: 1' in original_content
    if not has_arc:
        return False

    # Skip files that are manually crafted main characters (like Lệ Vô Tâm)
    # These have non-empty inventory and carefully tuned stats
    if 'inventory:\n      - name:' in original_content:
        return False

    cultivation = get_cultivation(original_content)
    if not cultivation:
        return False

    # Use the markdown body (after ---) for extraction
    body_match = re.search(r'^---\n.*?\n---\n(.*)$', original_content, re.DOTALL)
    if not body_match:
        return False
    body = body_match.group(1)

    # Generate stats
    stats = generate_stats(cultivation, body)

    # Extract methods from Section III
    methods = extract_methods_from_section3(body)

    # Extract relationships from Section IV
    relationships = extract_relationships_from_section4(body)

    # Rebuild the file
    new_content = rebuild_yaml_section(original_content, cultivation, stats, methods, relationships)

    if new_content != original_content:
        with open(path, 'w', encoding='utf-8') as fh:
            fh.write(new_content)
        return True
    return False


def main():
    count = 0
    for root, dirs, files in os.walk(BASE):
        for f in sorted(files):
            if not f.endswith('.md') or f == 'index.md':
                continue
            path = os.path.join(root, f)
            if process_character(path):
                count += 1
                faction = os.path.basename(root)
                print(f'  Updated: {faction}/{f}')

    print(f'\nTotal updated: {count} characters')


if __name__ == '__main__':
    main()
