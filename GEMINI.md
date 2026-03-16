# Gemini Task: Fill Character Details

## Your Assignment
Fill sections II-V for all unfilled characters in **4 regions** (955 characters total).

**Read the full plan at:** `.claude/plans/fill_all_characters.md`

## Your Regions (ONLY touch these)
| Region | Path | Unfilled | Factions |
|--------|------|:--------:|:--------:|
| Vô Tận Hải | `Đạo/Nhân_Vật/Vô_Tận_Hải/` | 318 | 42 |
| Bắc Băng | `Đạo/Nhân_Vật/Bắc_Băng/` | 274 | 45 |
| Tây Mạc | `Đạo/Nhân_Vật/Tây_Mạc/` | 269 | 49 |
| Thiên Trụ | `Đạo/Nhân_Vật/Thiên_Trụ/` | 94 | 14 |

## DO NOT touch these (Claude's regions)
- `Đạo/Nhân_Vật/Đông_Hoang/`
- `Đạo/Nhân_Vật/Nam_Cương/`
- `Đạo/Nhân_Vật/Tán_Tu/`

## Quick Start
1. Read `.claude/plans/fill_all_characters.md` for full instructions, templates, and examples
2. For each faction in your regions:
   - Read the faction file: `Đạo/Thế_Lực/[Faction_Name].md` (for context)
   - Find unfilled chars: files containing `*(Chưa xác định)*`
   - Fill sections II-V using the templates in the plan
3. Verify: `python3 scripts/find_unfilled_chars.py 1`
4. Commit: `docs: fill character details for [Region]`

## Key Rules
- Vietnamese only (no English in content)
- NEVER modify YAML frontmatter or Section I
- Each character needs unique personality
- Combat abilities must match faction specialty
- Relationships must reference real character names from the same faction folder
