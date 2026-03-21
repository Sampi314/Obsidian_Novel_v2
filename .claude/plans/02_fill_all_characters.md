# Plan: Fill All 1,670 Character Details

## Goal
Fill sections II-V for all 1,670 characters that still have `*(Chưa xác định)*` placeholder text.

## Current State (2026-03-16)
| Region | Unfilled | Total | Factions | Assigned To |
|--------|:--------:|:-----:|:--------:|:-----------:|
| Đông Hoang | 627 | 634 | 99 | **Claude** |
| Nam Cương | 85 | 133 | 12 | **Claude** |
| Tán Tu | 3 | 6 | 1 | **Claude** |
| Vô Tận Hải | 318 | 320 | 42 | **Gemini** |
| Bắc Băng | 274 | 277 | 45 | **Gemini** |
| Tây Mạc | 269 | 271 | 49 | **Gemini** |
| Thiên Trụ | 94 | 136 | 14 | **Gemini** |
| **Total** | **1,670** | **1,777** | **262** | |

## Task Split

### Claude Code — 715 characters (3 regions)
- **Đông Hoang** (627 unfilled, 99 factions) — largest region
- **Nam Cương** (85 unfilled, 12 factions)
- **Tán Tu** (3 unfilled, 1 faction)

### Gemini — 955 characters (4 regions)
- **Vô Tận Hải** (318 unfilled, 42 factions)
- **Bắc Băng** (274 unfilled, 45 factions)
- **Tây Mạc** (269 unfilled, 49 factions)
- **Thiên Trụ** (94 unfilled, 14 factions)

## IMPORTANT: No-Overlap Rule
- Claude ONLY touches files in: `Đạo/Nhân_Vật/Đông_Hoang/`, `Đạo/Nhân_Vật/Nam_Cương/`, `Đạo/Nhân_Vật/Tán_Tu/`
- Gemini ONLY touches files in: `Đạo/Nhân_Vật/Vô_Tận_Hải/`, `Đạo/Nhân_Vật/Bắc_Băng/`, `Đạo/Nhân_Vật/Tây_Mạc/`, `Đạo/Nhân_Vật/Thiên_Trụ/`
- Both can READ `Đạo/Thế_Lực/*.md` (faction files) for context — these are read-only references

---

## How To Fill Characters (Both Claude & Gemini)

### Step-by-Step Per Faction

1. **Find unfilled characters**: Look for files containing `*(Chưa xác định)*` in the assigned region folders
2. **Read faction context**: Read `Đạo/Thế_Lực/[Faction_Name].md` to understand culture, specialty, race, hierarchy
3. **Read filled examples** (if any): Check if any characters in the same faction folder already have sections II-V filled — match their style
4. **Fill sections II-V** for each unfilled character:

#### Section II — Ngoại Hình & Tính Cách (2-4 sentences)
- Physical appearance: build, face, hair, scars, clothing style
- Personality: temperament, habits, how others perceive them
- Must reflect the character's race and cultivation rank
- Example:
```
Thân hình cao lớn, vai rộng, mái tóc bạch kim buộc cao. Đôi mắt màu hổ phách luôn mang vẻ cảnh giác. Tính cách trầm mặc, ít nói, nhưng khi đã mở lời thì từng câu đều có trọng lượng. Đồng môn kính nể vì sự công bằng và kỷ luật nghiêm khắc.
```

#### Section III — Năng Lực & Chiến Đấu (2-3 sentences)
- Combat style tied to faction specialty
- At least 1 signature technique with Vietnamese name + Hán Tự (漢字)
- Mention strengths AND weaknesses
- Example:
```
Chuyên về kiếm pháp băng hàn, mỗi nhát chém mang theo sát khí đông cứng không khí. Tuyệt chiêu "Băng Thiên Nhất Kiếm" (冰天一劍) có thể đóng băng mọi thứ trong bán kính mười trượng. Điểm yếu: tốc độ thi triển chậm, dễ bị đối thủ nhanh nhẹn khai thác kẽ hở.
```

#### Section IV — Các Mối Quan Hệ (2-4 bullet points)
- Format: `- **[Tên Nhân Vật]:** [mô tả quan hệ]`
- At least 1 relationship within the same faction (use actual character names from the same folder)
- Cross-faction relationships are optional
- Example:
```
- **Hàn Tiêu:** Sư phụ truyền thụ kiếm pháp, người duy nhất hắn tuyệt đối tin tưởng.
- **Lang Bạch Sương:** Đồng môn sư muội, thường xuyên bất đồng quan điểm nhưng phối hợp chiến đấu ăn ý.
- **Băng Tuyết Nhi:** Đệ tử yêu quý nhất, nhìn thấy bóng dáng bản thân thời trẻ.
```

#### Section V — Tiểu Sử & Hành Trình (3-5 sentences)
- Origin: where they came from, how they joined the faction
- A defining event that shaped who they are
- Current goal or hidden secret
- Example:
```
Sinh ra trong một thôn nhỏ ở rìa Băng Nguyên, từ nhỏ đã chứng kiến gia đình bị yêu thú tấn công. Được Hàn Tiêu cứu mạng và thu nhận làm đồ đệ năm 8 tuổi. Trải qua mười năm khổ luyện, cuối cùng đột phá Kim Đan, trở thành kiếm tu trẻ nhất trong lịch sử môn phái. Hiện tại đang truy tìm tung tích bọn yêu thú năm xưa, nghi ngờ có thế lực tà đạo đứng sau điều khiển.
```

### Quality Rules (CRITICAL)
- **Vietnamese only** — absolutely no English in content
- Each character's personality MUST differ from faction-mates
- Combat abilities MUST match faction specialty (e.g., poison for Vạn Độc Môn, ice for Băng Lang)
- **YAML frontmatter and Section I must NOT be changed** — only edit sections II-V
- Every relationship must reference an actual character name (check the faction folder)
- Replace `*(Chưa xác định)*` completely — no placeholders should remain

### How to identify unfilled characters
A character is "unfilled" if their file contains the text `*(Chưa xác định)*` in any of sections II-V.

---

## Post-Fill Verification
After both Claude and Gemini finish:
```bash
python3 scripts/find_unfilled_chars.py 1
```
When output shows `"remaining": 0` → all done.

## Commit Convention
- Claude commits: `docs: fill character details for Đông Hoang/Nam Cương/Tán Tu`
- Gemini commits: `docs: fill character details for Vô Tận Hải/Bắc Băng/Tây Mạc/Thiên Trụ`
