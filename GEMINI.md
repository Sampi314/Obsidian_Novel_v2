# Gemini Task: Populate Faction Rosters

## Your Assignment
Create NEW characters to fill population gaps for factions in **3 regions** (~410 characters total).

**Read the full plan at:** `.claude/plans/populate_factions.md`

## Your Regions (ONLY touch these)
| Region | Path | Characters Needed | Factions |
|--------|------|:-----------------:|:--------:|
| Vô Tận Hải | `Đạo/Nhân_Vật/Vô_Tận_Hải/` | ~116 | 14 |
| Bắc Băng | `Đạo/Nhân_Vật/Bắc_Băng/` | ~169 | 18 |
| Tây Mạc | `Đạo/Nhân_Vật/Tây_Mạc/` | ~125 | 15 |

## DO NOT touch these regions
- `Đạo/Nhân_Vật/Đông_Hoang/` (Claude's region)
- `Đạo/Nhân_Vật/Nam_Cương/` (Jules' region)
- `Đạo/Nhân_Vật/Thiên_Trụ/` (Jules' region)

## Quick Start
1. Run `python3 scripts/faction_population_gap.py [Region]` to see which factions need characters
2. Pick the faction with the BIGGEST gap (Hạng Nhất first)
3. Read the faction file: `Đạo/Thế_Lực/[Region]/[Faction].md`
4. Read the race file if not Nhân Tộc: `Đạo/Chủng_Tộc/[Race].md`
5. Create 5-10 new character files per session
6. Commit: `docs: populate [Faction] with [N] new characters`

## Character Targets by Rank
| Hạng | Named Characters Needed |
|------|------------------------|
| Nhất | 35 per faction |
| Nhì | 20 per faction |
| Ba | 12 per faction |
| Tư | 7 per faction |
| Năm | 4 per faction |
| KXH | 3 per faction |

## Character Types to Create
Mix these types for each faction:

### Tu Sĩ (Cultivators)
- Leadership: Trưởng Lão, Hộ Pháp, Phong Chủ
- Elite: Chân Truyền, Nội Môn
- Common: Ngoại Môn

### Phàm Nhân (Mortals) — QUAN TRỌNG
- cultivation: "Phàm Nhân" (no cultivation level)
- stats: [1-5 range for all 6 values]
- Types: Đầu bếp, Thợ rèn, Hầu cận, Thương nhân, Nông dân, Tạp dịch
- MUST have interesting backstories — not NPCs!

## YAML Template for New Characters
```yaml
---
type: character
name: [Tên Hán Việt]
hantu: [漢字]
archetype: [Vai trò]
race: [Chủng tộc]
age: [Tuổi]
avatar: [Tên_File.png]
arcs:
  - arc: 1
    status: Còn Sống
    cultivation: [Cảnh giới hoặc "Phàm Nhân"]
    methods: [Công pháp]
    inventory:
      - name: [Vật phẩm]
        type: [Loại]
    stats: [Sinh Lực, Công Lực, Thần Thức, Tốc Độ, Phòng Ngự, Đặc Biệt]
    relationships:
      - character: [Tên]
        description: [Mô tả]
        feelings: {yeu: 0, han: 0, kinh: 0, tin: 0, so: 0, on: 0}
---
```

## Naming Rules
- Nhân Tộc: Vietnamese surnames (Nguyễn, Trần, Lê, Phạm...)
- Yêu Tộc: Animal surnames (Hổ, Lang, Xà, Hồ...)
- Cự Tộc: Nham, Thạch, Sơn
- Hải Tộc: Sea creature surnames (Kình, Giải, Chương, Triều...)
- Vi Tộc: Micro surnames (Nấm, Bào, Khuẩn, Phấn...)
- Phàm nhân: Simple daily names (Tiểu X, Lão X, giản dị)
- NEVER use job titles as names (no Trưởng Lão, Vương, Chiến Sĩ in name)

## Key Rules
- Vietnamese only (no English in content)
- Each character needs unique personality
- Combat abilities must match faction specialty
- Relationships must reference real character names
- Include 2-3 phàm nhân per faction minimum
