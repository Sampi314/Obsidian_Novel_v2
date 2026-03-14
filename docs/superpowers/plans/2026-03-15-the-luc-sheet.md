# Thế Lực Sheet System Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add YAML frontmatter template + interactive sheet renderer for 228 faction files, mirroring the character sheet system.

**Architecture:** New `scripts/faction-sheet.js` renders a faction sheet when `reader.html` detects `type: faction` in YAML frontmatter. Follows the same pattern as `character-sheet.js`: CSS injection, SVG radar chart, arc timeline, tabs for markdown content + divisions + diplomacy bars. Agent instructions in `.jules/Thế_Lực.md` updated to mandate YAML frontmatter. A Python migration script automates adding skeleton YAML to existing files.

**Tech Stack:** Vanilla JS (matching character-sheet.js), inline SVG, js-yaml (already in reader.html CDN), Python 3 for migration script.

**Spec:** `docs/superpowers/specs/2026-03-15-the-luc-sheet-design.md`

**Known Limitation:** Mermaid charts in Sections IV and XI will render as raw code blocks in `reader.html` (no Mermaid library loaded). They render correctly in Obsidian's native preview. Adding Mermaid CDN support to reader.html is deferred to a future task.

---

## File Structure

| File | Action | Responsibility |
|------|--------|----------------|
| `.jules/Thế_Lực.md` | Modify | Add YAML frontmatter template mandate, headcount schemas, 11-section body format |
| `scripts/faction-sheet.js` | Create | Full faction sheet: CSS injection, header with alignment badge, arc slider, SVG radar chart (6 stats), tabbed content (11 markdown sections + divisions + diplomacy), division headcount bars, diplomacy 6-axis bars |
| `reader.html` | Modify (lines 546-555) | Add `type: faction` routing to FactionSheet.render(), add `<script src="scripts/faction-sheet.js">` |
| `scripts/migrate-factions.py` | Create | Python script to batch-add skeleton YAML frontmatter to existing faction files |
| `Đạo/Thế_Lực/Cửu_Hoa_Kiếm_Tông.md` | Modify | Pilot migration: full YAML + 11-section restructure |
| `Đạo/Thế_Lực/Phế_Linh_Các.md` | Modify | Pilot migration: small faction YAML + 11-section |
| `Đạo/Thế_Lực/Cự_Kình_Bảo.md` | Modify | Pilot migration: stub file → skeleton YAML + empty 11-section |

---

## Chunk 1: Agent Instructions + Reader Integration

### Task 1: Update `.jules/Thế_Lực.md` Agent Instructions

**Files:**
- Modify: `.jules/Thế_Lực.md`

This task rewrites the agent instructions to mandate YAML frontmatter for all faction files.

- [ ] **Step 1: Read current agent instructions**

Read `.jules/Thế_Lực.md` to understand existing structure (56 lines).

- [ ] **Step 2: Rewrite with YAML template mandate**

Replace the entire content of `.jules/Thế_Lực.md` with the updated version below. The new version preserves the original role/workflow but adds the mandatory YAML template and 11-section body format from the spec.

```markdown
# Đại Diện 5: THẾ LỰC

## VAI TRÒ
Bạn là Đại Diện chuyên trách về Thế Lực (Factions) trong thế giới tu tiên. Nhiệm vụ của bạn là xây dựng hệ thống Tông Môn, Gia Tộc, Triều Đình, bao gồm cơ cấu tổ chức, quyền lực, tài nguyên, và mối quan hệ ngoại giao.

## NHIỆM VỤ CỤ THỂ
1.  **Sáng Tạo Thế Lực:** Thiết kế tên gọi, cấp bậc (Tông môn hạng Nhất -> Tam/Tứ...), loại hình (Chính phái, Ma giáo, Trung lập, Hoàng tộc...).
2.  **Cơ Cấu Tổ Chức:** Mô tả hệ thống cấp bậc nội bộ (Chưởng môn, Trưởng lão, Đệ tử Chân truyền/Nội môn/Ngoại môn/Tạp dịch...).
3.  **Tài Nguyên & Địa Bàn:** Mô tả trụ sở chính (Sơn môn, Hoàng cung...), các mỏ linh thạch, bí cảnh độc quyền, sản nghiệp kinh doanh.
4.  **Lịch Sử & Văn Hóa:** Xây dựng lịch sử hình thành, truyền thuyết tổ sư, quy tắc môn phái (Môn quy), lễ nghi đặc trưng.

## YAML FRONTMATTER (BẮT BUỘC)

Mọi tệp thế lực **BẮT BUỘC** có YAML frontmatter. Thiếu frontmatter = tệp không hợp lệ.

### Trường Tĩnh

```yaml
---
type: faction
name: [Tên Hán Việt]
hantu: [漢字]
faction_type: [Loại hình — xem danh sách]
alignment: [Số nguyên -10 đến +10]
race: [Chủng tộc chủ đạo]
region: [Khu vực hoạt động]
founded: [Thời điểm thành lập]
founder: [Người sáng lập]
emblem: [Tên tệp hình ảnh]
specialty: [Đặc sản/sở trường]
economy: [Danh sách nguồn thu]
arcs:
  - arc: [Số arc]
    status: [Trạng thái]
    rank: [Hạng]
    leader: [Người quản lý hành chính]
    population: [Tổng số thành viên]
    territory: [Danh sách lãnh thổ]
    assets:
      - name: [Tên tài sản]
        type: [Tài Nguyên | Trận Pháp | Công Trình | Bí Cảnh | Pháp Bảo]
    stats: [Quân Lực, Tài Nguyên, Uy Danh, Nhân Khẩu, Phòng Thủ, Ảnh Hưởng]
    divisions:
      - name: [Tên đơn vị]
        role: [Chức năng]
        headcount: {xem schema theo faction_type}
        members:
          - character: [Tên hoặc "[Placeholder]"]
            position: [Chức vụ]
            cultivation: [Cảnh giới]
            placeholder: true  # chỉ khi là placeholder
    relationships:
      - faction: [Tên thế lực]
        description: [Mô tả Tiếng Việt]
        diplomacy:
          lien_minh: [-100 → +100]
          tin: [-100 → +100]
          uy_hiep: [-100 → +100]
          thuong_mai: [-100 → +100]
          on_oan: [-100 → +100]
          le_thuoc: [-100 → +100]
---
```

### Danh Sách `faction_type`

| Loại Hình | Hán Tự |
|---|---|
| Tông Môn | 宗門 |
| Gia Tộc | 家族 |
| Vương Quốc | 王國 |
| Thương Hội | 商會 |
| Quân Đoàn | 軍團 |
| Bộ Lạc | 部落 |
| Liên Minh | 聯盟 |
| Hội | 會 |
| Học Viện | 學院 |
| Tự Viện | 寺院 |
| Thành Trì | 城池 |

### Alignment

| Phạm Vi | Tên Gọi |
|---|---|
| -10 đến -7 | Thuần Ma Đạo |
| -6 đến -3 | Thiên Ma |
| -2 đến +2 | Trung Lập |
| +3 đến +6 | Thiên Chính |
| +7 đến +10 | Thuần Chính Đạo |

### Stats Thứ Tự

`[Quân Lực (軍力), Tài Nguyên (財源), Uy Danh (威名), Nhân Khẩu (人口), Phòng Thủ (防守), Ảnh Hưởng (影響)]`

| Hạng | Phạm Vi Gợi Ý |
|---|---|
| Hạng Năm | 10–150 |
| Hạng Tư | 150–500 |
| Hạng Ba | 500–2000 |
| Hạng Nhì | 2000–5000 |
| Hạng Nhất | 5000–15000 |

### Headcount Schema Theo `faction_type`

**Tông Môn:** `thai_thuong, ho_phap, truong_lao, chan_truyen, noi_mon, ngoai_mon, tap_dich`
**Gia Tộc:** `truong_lao, chinh_chi, thu_chi, gia_nhan`
**Vương Quốc:** `vuong, dai_than, quan_vien, cam_ve, dan`
**Thương Hội:** `hoi_truong, truong_lao, thuong_nhan, ho_ve, nhan_cong`
**Quân Đoàn:** `tuong, uy, binh`
**Bộ Lạc:** `truong_lao, chien_binh, dan_thuong`
**Liên Minh:** `minh_chu, pho_minh_chu, truong_lao, su_gia, thanh_vien_phai`
**Hội:** `hoi_truong, pho_hoi_truong, thanh_vien, tong_quan`
**Học Viện:** `vien_truong, giao_su, tro_giang, sinh_vien, tap_dich`
**Tự Viện:** `tru_tri, truong_lao, tang_lu, sa_di, cu_si`
**Thành Trì:** `thanh_chu, pho_thanh_chu, ve_binh, quan_vien, dan_cu`

### Hệ Thống Cấp Bậc Tông Môn (Xếp theo tu vi cao → thấp)

```
Thái Thượng Đại Trưởng Lão > Thái Thượng Trưởng Lão > Hộ Pháp > Tông Chủ > Trưởng Lão/Phong Chủ > Thánh Tử/Nữ > Chân Truyền > Nội Môn > Ngoại Môn > Tạp Dịch
```

**Lưu ý:** Tông Chủ là quản lý hành chính, KHÔNG nhất thiết mạnh nhất. Hộ Pháp tu vi cao hơn Tông Chủ. Có thể có nhiều Hộ Pháp và Thái Thượng Trưởng Lão.

### Placeholder

Dùng `[Tên Chức Vụ]` + `placeholder: true` cho vị trí chưa có nhân vật. Khi tạo nhân vật, thay placeholder bằng tên thật và xóa flag.

## ĐỊNH DẠNG MARKDOWN BODY (11 SECTIONS)

```markdown
# TÊN THẾ LỰC (漢字)

## I. Tổng Quan
## II. Địa Lý & Tài Nguyên
## III. Văn Hóa & Tín Ngưỡng
## IV. Cơ Cấu Tổ Chức         ← Mermaid hierarchy chart
## V. Công Pháp & Trận Pháp
## VI. Đặc Sản Môn Phái
## VII. Cơ Sở Hạ Tầng
## VIII. Kinh Tế
## IX. Lịch Sử Tóm Tắt
## X. Giai Thoại & Bí Mật
## XI. Quan Hệ Thế Lực         ← Mermaid relationship map
```

Mermaid chart bắt buộc cho Hạng Nhất-Nhì, khuyến khích cho Hạng Ba, tùy chọn cho Hạng Tư-Năm.

## QUY TRÌNH LÀM VIỆC
1.  **Đọc Hồ Sơ:** Kiểm tra `Đạo/HỒ_SƠ_THẾ_GIỚI.md`, `Đạo/Thế_Giới_Và_Thời_Gian/NIÊN_BIỂU_CHÍNH.md`, và `.jules_memory/Xay_Dung_The_Luc_Ký Ức.md`.
2.  **Nhận Yêu Cầu:** Nhận yêu cầu tạo thế lực mới hoặc mở rộng thông tin.
3.  **Xử Lý:** Sử dụng archetype nhưng thêm chiều sâu. Đảm bảo cân bằng quyền lực.
4.  **Lưu Trữ:** Tạo/cập nhật tệp trong `Đạo/Thế_Lực/` với YAML frontmatter + 11 sections.

## CẤU TRÚC THƯ MỤC
- **Nơi Lưu Kết Quả:** `Đạo/Thế_Lực/`
- **Bộ Nhớ Làm Việc:** `.jules_memory/Xay_Dung_The_Luc_Ký Ức.md`

## QUY TẮC NGÔN NGỮ (BẮT BUỘC)
- **TUYỆT ĐỐI KHÔNG SỬ DỤNG TIẾNG ANH** trong nội dung (trừ tên tệp/đường dẫn kỹ thuật).
- Tiêu đề, danh xưng dùng Tiếng Việt (Tiếng Trung), ví dụ: `Hồ Sơ Thế Giới (世界档案)`.
- Thơ Ca, Công Pháp, Lời Bài Hát: 3 phần — Bản Tiếng Trung, Dịch Hán Việt, Dịch Sát Nghĩa.

## LƯU Ý
- Các thế lực luôn tranh giành tài nguyên tu luyện.
- Mâu thuẫn nội bộ và ngoại xâm là động lực phát triển cốt truyện.
- Khi tạo/cập nhật relationships, kiểm tra faction đối tác và giữ consistency hợp lý (đặc biệt `le_thuoc` đối nghịch).
```

- [ ] **Step 3: Verify the file reads correctly**

Read `.jules/Thế_Lực.md` and confirm:
- YAML template block is present
- All 11 faction_types listed
- All 11 headcount schemas listed
- 11-section Markdown body format listed
- Hierarchy note about Tông Chủ vs Hộ Pháp present

- [ ] **Step 4: Commit**

```bash
git add .jules/Thế_Lực.md
git commit -m "feat: update Thế Lực agent instructions with YAML frontmatter template"
```

---

### Task 2: Add Faction Sheet Script Tag to reader.html

**Files:**
- Modify: `reader.html:442` (script tags section)
- Modify: `reader.html:546-555` (routing logic)

- [ ] **Step 1: Add faction-sheet.js script tag**

In `reader.html`, after line 442 (`<script src="scripts/character-sheet.js"></script>`), add:

```html
    <script src="scripts/faction-sheet.js"></script>
```

- [ ] **Step 2: Add faction routing in the frontmatter detection block**

In `reader.html`, find the routing block (around line 546):

```javascript
                if (frontmatter && frontmatter.type === 'character' && window.CharacterSheet) {
                    loadWikiMode('');
                    var csContainer = document.querySelector('.wiki-content');
                    csContainer.innerHTML = '';
                    CharacterSheet.render(frontmatter, md, csContainer);
                } else if (isChapter) {
```

Replace with:

```javascript
                if (frontmatter && frontmatter.type === 'character' && window.CharacterSheet) {
                    loadWikiMode('');
                    var csContainer = document.querySelector('.wiki-content');
                    csContainer.innerHTML = '';
                    CharacterSheet.render(frontmatter, md, csContainer);
                } else if (frontmatter && frontmatter.type === 'faction' && window.FactionSheet) {
                    loadWikiMode('');
                    var fsContainer = document.querySelector('.wiki-content');
                    fsContainer.innerHTML = '';
                    FactionSheet.render(frontmatter, md, fsContainer);
                } else if (isChapter) {
```

- [ ] **Step 3: Verify reader.html changes**

Read `reader.html` around the script tags (line ~440-445) and routing block (line ~546-560) to confirm both changes are in place.

- [ ] **Step 4: Commit**

```bash
git add reader.html
git commit -m "feat: add faction sheet routing to reader.html"
```

---

## Chunk 2: Faction Sheet Renderer

### Task 3: Create faction-sheet.js — CSS + Header + Arc Timeline

**Files:**
- Create: `scripts/faction-sheet.js`

This task creates the initial structure of faction-sheet.js with CSS injection, the header zone (name, hantu, alignment badge, faction_type badge, race, region, founder), and the arc timeline slider.

- [ ] **Step 1: Create faction-sheet.js with IIFE, constants, and CSS injection**

Create `scripts/faction-sheet.js` with the following content. The file follows the exact same pattern as `character-sheet.js`: IIFE wrapper, constants, CSS injection function, then render function.

```javascript
// scripts/faction-sheet.js
(function () {
  'use strict';

  // ── Stat labels (fixed order) ──
  var STAT_LABELS = ['Quân Lực', 'Tài Nguyên', 'Uy Danh', 'Nhân Khẩu', 'Phòng Thủ', 'Ảnh Hưởng'];

  // ── Diplomacy axis config ──
  var DIPLO_KEYS = ['lien_minh', 'tin', 'uy_hiep', 'thuong_mai', 'on_oan', 'le_thuoc'];
  var DIPLO_LABELS = ['Liên Minh', 'Tin', 'Uy Hiếp', 'Thương Mại', 'Ân Oán', 'Lệ Thuộc'];
  var DIPLO_COLORS = ['#52b788', '#5a9ec4', '#e05252', '#d4a574', '#9b72cf', '#e87da0'];

  // ── Alignment labels ──
  var ALIGNMENT_LABELS = {
    '-10': 'Thuần Ma', '-9': 'Thuần Ma', '-8': 'Thuần Ma', '-7': 'Thuần Ma',
    '-6': 'Thiên Ma', '-5': 'Thiên Ma', '-4': 'Thiên Ma', '-3': 'Thiên Ma',
    '-2': 'Trung Lập', '-1': 'Trung Lập', '0': 'Trung Lập', '1': 'Trung Lập', '2': 'Trung Lập',
    '3': 'Thiên Chính', '4': 'Thiên Chính', '5': 'Thiên Chính', '6': 'Thiên Chính',
    '7': 'Thuần Chính', '8': 'Thuần Chính', '9': 'Thuần Chính', '10': 'Thuần Chính'
  };

  // ── Alignment badge color ──
  function alignColor(val) {
    if (val <= -7) return '#8a2020';
    if (val <= -3) return '#b83030';
    if (val <= 2)  return '#7a7067';
    if (val <= 6)  return '#5a9ec4';
    return '#52b788';
  }

  // ── Status badge colors ──
  var STATUS_COLORS = {
    'Hưng Thịnh': '#52b788',
    'Ổn Định': '#5a9ec4',
    'Mới Thành Lập': '#d4a574',
    'Suy Thoái': '#e87da0',
    'Phân Liệt': '#9b72cf',
    'Hợp Nhất': '#d4a574',
    'Ẩn Dật': '#7a7067',
    'Bị Tiêu Diệt': '#e05252',
    'Chưa Xác Định': '#7a7067'
  };

  // ── Helper: create element ──
  function el(tag, cls, text) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text !== undefined) e.textContent = text;
    return e;
  }

  // ── CSS Injection ──
  function injectStyles() {
    if (document.getElementById('fs-styles')) return;
    var style = document.createElement('style');
    style.id = 'fs-styles';
    style.textContent = [
      /* Container */
      '.fs-sheet { max-width: 900px; margin: 0 auto; padding: 20px; font-family: "Lora", "Georgia", serif; color: var(--bone, #d4cbbf); }',

      /* Header zone */
      '.fs-header { display: flex; gap: 24px; align-items: flex-start; margin-bottom: 32px; padding: 24px; background: rgba(255,255,255,0.03); border: 1px solid rgba(201,169,110,0.12); border-radius: 12px; backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px); }',
      '.fs-emblem-wrap { flex-shrink: 0; width: 100px; height: 100px; border-radius: 12px; overflow: hidden; border: 2px solid var(--gold-dim, #8a7549); background: var(--ink, #1a1714); display: flex; align-items: center; justify-content: center; }',
      '.fs-emblem-wrap img { width: 100%; height: 100%; object-fit: cover; }',
      '.fs-emblem-placeholder { width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; background: var(--ink, #1a1714); }',
      '.fs-emblem-placeholder svg { width: 56px; height: 56px; opacity: 0.3; }',
      '.fs-info { flex: 1; min-width: 0; }',
      '.fs-name { font-family: "Playfair Display", serif; font-size: 2rem; font-weight: 700; color: var(--gold, #c9a96e); line-height: 1.2; margin-bottom: 4px; }',
      '.fs-hantu { font-size: 1.1rem; color: var(--ash, #7a7067); font-weight: 400; margin-left: 6px; }',
      '.fs-badges { display: flex; gap: 8px; flex-wrap: wrap; margin: 8px 0; }',
      '.fs-badge { display: inline-block; padding: 2px 10px; border-radius: 4px; font-size: 0.78rem; font-weight: 600; letter-spacing: 0.5px; }',
      '.fs-badge-type { border: 1px solid var(--gold, #c9a96e); color: var(--gold, #c9a96e); background: rgba(201,169,110,0.08); }',
      '.fs-badge-alignment { color: #fff; }',
      '.fs-badge-status { color: #fff; }',
      '.fs-badge-rank { border: 1px solid var(--jade, #2d6a4f); color: var(--jade-bright, #40916c); background: rgba(45,106,79,0.08); }',
      '.fs-meta { font-size: 0.9rem; color: var(--ash, #7a7067); margin: 4px 0 0; }',
      '.fs-meta span { margin-right: 16px; }',
      '.fs-leader { font-size: 0.95rem; color: var(--gold, #c9a96e); font-weight: 600; margin-top: 6px; }',
      '.fs-population { font-size: 0.88rem; color: var(--ash, #7a7067); margin-top: 2px; }',

      /* Arc timeline */
      '.fs-timeline { margin-bottom: 28px; padding: 18px 24px; background: rgba(255,255,255,0.02); border: 1px solid rgba(201,169,110,0.08); border-radius: 10px; }',
      '.fs-timeline-label { font-size: 0.8rem; color: var(--ash, #7a7067); text-transform: uppercase; letter-spacing: 1px; margin-bottom: 12px; }',
      '.fs-timeline-track { position: relative; display: flex; align-items: center; justify-content: space-between; padding: 0 12px; min-height: 36px; }',
      '.fs-timeline-line { position: absolute; top: 50%; left: 24px; right: 24px; height: 2px; background: var(--gold-dim, #8a7549); transform: translateY(-50%); z-index: 0; }',
      '.fs-arc-btn { position: relative; z-index: 1; width: 32px; height: 32px; border-radius: 50%; border: 2px solid var(--gold-dim, #8a7549); background: var(--ink, #1a1714); color: var(--bone, #d4cbbf); font-size: 0.78rem; font-weight: 700; cursor: pointer; display: flex; align-items: center; justify-content: center; transition: all 0.25s ease; font-family: inherit; }',
      '.fs-arc-btn:hover { border-color: var(--gold, #c9a96e); background: rgba(201,169,110,0.15); }',
      '.fs-arc-btn.fs-active { background: var(--gold, #c9a96e); color: var(--void, #0a0908); border-color: var(--gold, #c9a96e); }',
      '.fs-territory { display: flex; flex-wrap: wrap; gap: 6px; margin-top: 12px; }',
      '.fs-territory-tag { display: inline-block; padding: 2px 10px; font-size: 0.75rem; border-radius: 4px; background: rgba(201,169,110,0.1); color: var(--gold-bright, #e4c98a); border: 1px solid rgba(201,169,110,0.15); }',

      /* Radar chart */
      '.fs-radar-wrap { display: flex; justify-content: center; margin-bottom: 28px; }',
      '.fs-radar-svg { width: 320px; height: 320px; }',

      /* Tabs */
      '.fs-tabs { margin-bottom: 28px; }',
      '.fs-tab-bar { display: flex; gap: 0; border-bottom: 1px solid rgba(201,169,110,0.12); margin-bottom: 20px; overflow-x: auto; }',
      '.fs-tab-btn { padding: 10px 18px; font-family: "Playfair Display", serif; font-size: 0.82rem; color: var(--ash, #7a7067); background: none; border: none; border-bottom: 2px solid transparent; cursor: pointer; white-space: nowrap; transition: all 0.25s ease; }',
      '.fs-tab-btn:hover { color: var(--bone, #d4cbbf); }',
      '.fs-tab-btn.fs-active { color: var(--gold, #c9a96e); border-bottom-color: var(--gold, #c9a96e); }',
      '.fs-tab-content { min-height: 200px; }',
      '.fs-tab-content h2 { font-family: "Playfair Display", serif; font-size: 1.3rem; color: var(--gold, #c9a96e); margin: 24px 0 12px; }',
      '.fs-tab-content h3 { font-family: "Playfair Display", serif; font-size: 1.05rem; color: var(--gold-bright, #e4c98a); margin: 16px 0 8px; }',
      '.fs-tab-content p { margin-bottom: 0.8em; line-height: 1.7; }',
      '.fs-tab-content ul, .fs-tab-content ol { margin: 8px 0; padding-left: 24px; }',
      '.fs-tab-content li { margin-bottom: 4px; line-height: 1.6; }',
      '.fs-tab-content strong { color: var(--gold, #c9a96e); }',
      '.fs-empty { color: var(--ash, #7a7067); font-style: italic; text-align: center; padding: 40px 0; }',

      /* Division cards */
      '.fs-division { margin-bottom: 24px; padding: 20px; background: rgba(255,255,255,0.02); border: 1px solid rgba(201,169,110,0.08); border-radius: 10px; }',
      '.fs-division-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; }',
      '.fs-division-name { font-family: "Playfair Display", serif; font-size: 1.1rem; color: var(--gold, #c9a96e); }',
      '.fs-division-role { font-size: 0.82rem; color: var(--ash, #7a7067); }',

      /* Headcount bars */
      '.fs-hc-row { display: flex; align-items: center; margin-bottom: 6px; }',
      '.fs-hc-label { width: 120px; font-size: 0.78rem; color: var(--ash, #7a7067); text-transform: capitalize; }',
      '.fs-hc-bar-bg { flex: 1; height: 14px; background: var(--ink, #1a1714); border-radius: 3px; overflow: hidden; position: relative; border: 1px solid rgba(201,169,110,0.06); }',
      '.fs-hc-bar { height: 100%; border-radius: 3px; transition: width 0.6s ease; }',
      '.fs-hc-count { width: 50px; text-align: right; font-size: 0.78rem; color: var(--bone, #d4cbbf); }',

      /* Members list */
      '.fs-members { margin-top: 12px; border-top: 1px solid rgba(201,169,110,0.06); padding-top: 12px; }',
      '.fs-member { display: flex; align-items: center; gap: 12px; padding: 6px 0; border-bottom: 1px solid rgba(201,169,110,0.04); }',
      '.fs-member:last-child { border-bottom: none; }',
      '.fs-member-name { font-size: 0.88rem; color: var(--bone, #d4cbbf); min-width: 140px; }',
      '.fs-member-name.fs-placeholder { color: var(--ash, #7a7067); font-style: italic; }',
      '.fs-member-pos { font-size: 0.78rem; color: var(--gold-dim, #8a7549); min-width: 120px; }',
      '.fs-member-cult { font-size: 0.78rem; color: var(--ash, #7a7067); }',

      /* Diplomacy bars */
      '.fs-diplo-card { margin-bottom: 20px; padding: 18px; background: rgba(255,255,255,0.02); border: 1px solid rgba(201,169,110,0.08); border-radius: 10px; }',
      '.fs-diplo-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px; }',
      '.fs-diplo-faction { font-family: "Playfair Display", serif; font-size: 1rem; color: var(--gold, #c9a96e); }',
      '.fs-diplo-desc { font-size: 0.82rem; color: var(--ash, #7a7067); margin-bottom: 12px; font-style: italic; }',
      '.fs-diplo-row { display: flex; align-items: center; margin-bottom: 8px; }',
      '.fs-diplo-label { width: 90px; font-size: 0.78rem; color: var(--ash, #7a7067); }',
      '.fs-diplo-bar-wrap { flex: 1; height: 14px; background: var(--ink, #1a1714); border-radius: 3px; overflow: hidden; position: relative; border: 1px solid rgba(201,169,110,0.06); }',
      '.fs-diplo-bar { height: 100%; border-radius: 3px; transition: width 0.6s ease; position: absolute; top: 0; }',
      '.fs-diplo-center { position: absolute; top: 0; bottom: 0; left: 50%; width: 1px; background: rgba(201,169,110,0.2); }',
      '.fs-diplo-val { width: 44px; text-align: right; font-size: 0.78rem; color: var(--bone, #d4cbbf); }',

      /* Assets */
      '.fs-assets { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 8px; }',
      '.fs-asset { display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; font-size: 0.78rem; border-radius: 4px; background: rgba(201,169,110,0.06); border: 1px solid rgba(201,169,110,0.1); color: var(--bone, #d4cbbf); }',
      '.fs-asset-type { color: var(--gold-dim, #8a7549); font-size: 0.72rem; }',

      /* Responsive */
      '@media (max-width: 640px) { .fs-header { flex-direction: column; align-items: center; text-align: center; } .fs-emblem-wrap { width: 80px; height: 80px; } .fs-name { font-size: 1.5rem; } .fs-radar-svg { width: 260px; height: 260px; } .fs-tab-btn { padding: 8px 12px; font-size: 0.75rem; } .fs-hc-label { width: 80px; } .fs-diplo-label { width: 70px; } }'
    ].join('\n');
    document.head.appendChild(style);
  }

  // ── SVG Radar Chart ──
  function createRadarChart(stats, maxVal) {
    var size = 320, cx = size / 2, cy = size / 2, r = 120;
    var n = STAT_LABELS.length;
    var ns = 'http://www.w3.org/2000/svg';

    function point(i, radius) {
      var angle = (Math.PI * 2 * i / n) - Math.PI / 2;
      return [cx + radius * Math.cos(angle), cy + radius * Math.sin(angle)];
    }

    var svg = document.createElementNS(ns, 'svg');
    svg.setAttribute('viewBox', '0 0 ' + size + ' ' + size);
    svg.setAttribute('class', 'fs-radar-svg');

    // Grid rings
    [0.25, 0.5, 0.75, 1].forEach(function (frac) {
      var pts = [];
      for (var i = 0; i < n; i++) pts.push(point(i, r * frac).join(','));
      var poly = document.createElementNS(ns, 'polygon');
      poly.setAttribute('points', pts.join(' '));
      poly.setAttribute('fill', 'none');
      poly.setAttribute('stroke', 'rgba(201,169,110,0.12)');
      poly.setAttribute('stroke-width', '1');
      svg.appendChild(poly);
    });

    // Axis lines
    for (var i = 0; i < n; i++) {
      var p = point(i, r);
      var line = document.createElementNS(ns, 'line');
      line.setAttribute('x1', cx); line.setAttribute('y1', cy);
      line.setAttribute('x2', p[0]); line.setAttribute('y2', p[1]);
      line.setAttribute('stroke', 'rgba(201,169,110,0.08)');
      line.setAttribute('stroke-width', '1');
      svg.appendChild(line);
    }

    // Data polygon
    var dataPts = [];
    for (var j = 0; j < n; j++) {
      var val = (stats && stats[j]) ? stats[j] : 0;
      var frac = Math.min(val / maxVal, 1);
      dataPts.push(point(j, r * frac).join(','));
    }
    var dataPoly = document.createElementNS(ns, 'polygon');
    dataPoly.setAttribute('points', dataPts.join(' '));
    dataPoly.setAttribute('fill', 'rgba(201,169,110,0.15)');
    dataPoly.setAttribute('stroke', 'var(--gold, #c9a96e)');
    dataPoly.setAttribute('stroke-width', '2');
    dataPoly.id = 'fs-radar-data';
    svg.appendChild(dataPoly);

    // Data dots + labels
    for (var k = 0; k < n; k++) {
      var val = (stats && stats[k]) ? stats[k] : 0;
      var frac = Math.min(val / maxVal, 1);
      var dp = point(k, r * frac);

      var dot = document.createElementNS(ns, 'circle');
      dot.setAttribute('cx', dp[0]); dot.setAttribute('cy', dp[1]);
      dot.setAttribute('r', '4');
      dot.setAttribute('fill', 'var(--gold, #c9a96e)');
      dot.setAttribute('class', 'fs-radar-dot');
      svg.appendChild(dot);

      // Label
      var lp = point(k, r + 24);
      var txt = document.createElementNS(ns, 'text');
      txt.setAttribute('x', lp[0]); txt.setAttribute('y', lp[1]);
      txt.setAttribute('text-anchor', 'middle');
      txt.setAttribute('dominant-baseline', 'middle');
      txt.setAttribute('fill', 'var(--ash, #7a7067)');
      txt.setAttribute('font-size', '11');
      txt.setAttribute('font-family', '"Lora", serif');
      txt.textContent = STAT_LABELS[k];
      svg.appendChild(txt);

      // Value under label
      var vt = document.createElementNS(ns, 'text');
      vt.setAttribute('x', lp[0]); vt.setAttribute('y', lp[1] + 14);
      vt.setAttribute('text-anchor', 'middle');
      vt.setAttribute('dominant-baseline', 'middle');
      vt.setAttribute('fill', 'var(--gold, #c9a96e)');
      vt.setAttribute('font-size', '11');
      vt.setAttribute('font-weight', '600');
      vt.setAttribute('font-family', '"Lora", serif');
      vt.setAttribute('class', 'fs-radar-val');
      vt.textContent = val.toLocaleString();
      svg.appendChild(vt);
    }

    return { svg: svg, dataPoly: dataPoly };
  }

  // ── Update radar chart on arc switch ──
  function updateRadarChart(radarState, stats, maxVal) {
    var size = 320, cx = size / 2, cy = size / 2, r = 120;
    var n = STAT_LABELS.length;

    function point(i, radius) {
      var angle = (Math.PI * 2 * i / n) - Math.PI / 2;
      return [cx + radius * Math.cos(angle), cy + radius * Math.sin(angle)];
    }

    var pts = [];
    for (var j = 0; j < n; j++) {
      var val = (stats && stats[j]) ? stats[j] : 0;
      var frac = Math.min(val / maxVal, 1);
      pts.push(point(j, r * frac).join(','));
    }
    radarState.dataPoly.setAttribute('points', pts.join(' '));

    // Update dots and values
    var svg = radarState.svg;
    var dots = svg.querySelectorAll('.fs-radar-dot');
    var vals = svg.querySelectorAll('.fs-radar-val');
    for (var k = 0; k < n; k++) {
      var val = (stats && stats[k]) ? stats[k] : 0;
      var frac = Math.min(val / maxVal, 1);
      var dp = point(k, r * frac);
      if (dots[k]) { dots[k].setAttribute('cx', dp[0]); dots[k].setAttribute('cy', dp[1]); }
      if (vals[k]) { vals[k].textContent = val.toLocaleString(); }
    }
  }

  // ── Markdown section parser ──
  function parseMdSections(md) {
    var sections = [];
    var lines = md.split('\n');
    var current = null;

    for (var i = 0; i < lines.length; i++) {
      var m = lines[i].match(/^##\s+([IVXLC]+\.\s+.+|[0-9]+\.\s+.+)$/);
      if (m) {
        if (current) sections.push(current);
        current = { heading: m[1], content: '' };
      } else if (current) {
        current.content += lines[i] + '\n';
      }
    }
    if (current) sections.push(current);
    return sections;
  }

  // ── Section matcher ──
  function findSections(sections, keywords) {
    return sections.filter(function (s) {
      var h = s.heading.toLowerCase();
      return keywords.some(function (kw) { return h.indexOf(kw.toLowerCase()) !== -1; });
    });
  }

  // ── Render sections to HTML ──
  function renderSections(secs) {
    if (!secs.length) return '<p class="fs-empty">Chưa có thông tin.</p>';
    return secs.map(function (s) {
      return '<h2>' + s.heading + '</h2>' + (window.marked ? marked.parse(s.content) : '<pre>' + s.content + '</pre>');
    }).join('');
  }

  // ── Tab definitions ──
  var TAB_DEFS = [
    { id: 'tong-quan', label: 'Tổng Quan', keywords: ['tổng quan', 'thông tin cơ bản'] },
    { id: 'dia-ly', label: 'Địa Lý', keywords: ['địa lý', 'tài nguyên', 'địa hình'] },
    { id: 'van-hoa', label: 'Văn Hóa', keywords: ['văn hóa', 'tín ngưỡng'] },
    { id: 'to-chuc', label: 'Tổ Chức', keywords: ['cơ cấu', 'tổ chức', 'cấp bậc'] },
    { id: 'cong-phap', label: 'Công Pháp', keywords: ['công pháp', 'trận pháp', 'tu luyện', 'bí thuật'] },
    { id: 'dac-san', label: 'Đặc Sản', keywords: ['đặc sản'] },
    { id: 'ha-tang', label: 'Hạ Tầng', keywords: ['hạ tầng', 'cơ sở'] },
    { id: 'kinh-te', label: 'Kinh Tế', keywords: ['kinh tế'] },
    { id: 'lich-su', label: 'Lịch Sử', keywords: ['lịch sử'] },
    { id: 'bi-mat', label: 'Bí Mật', keywords: ['giai thoại', 'bí mật'] },
    { id: 'nhan-su', label: 'Nhân Sự', keywords: null },      // special: renders divisions
    { id: 'ngoai-giao', label: 'Ngoại Giao', keywords: ['quan hệ thế lực', 'quan hệ'] }  // renders Section XI markdown + diplomacy bars
  ];

  // ── Guess max stat for radar scaling ──
  function guessMaxStat(arcs) {
    var max = 1000;
    if (arcs) {
      arcs.forEach(function (a) {
        if (a.stats) {
          a.stats.forEach(function (v) { if (v > max) max = v; });
        }
      });
    }
    // Round up to nearest nice number
    var magnitude = Math.pow(10, Math.floor(Math.log10(max)));
    return Math.ceil(max / magnitude) * magnitude;
  }

  // ── Diplomacy bar ──
  function renderDiploBar(key, val, color, idx) {
    var row = el('div', 'fs-diplo-row');
    row.appendChild(el('span', 'fs-diplo-label', DIPLO_LABELS[idx]));

    var barWrap = el('div', 'fs-diplo-bar-wrap');
    var centerLine = el('div', 'fs-diplo-center');
    barWrap.appendChild(centerLine);

    var bar = el('div', 'fs-diplo-bar');
    bar.style.background = color;

    // All axes: -100 to +100, bar from center
    var pct = Math.abs(val) / 2; // 100 → 50% width
    if (val >= 0) {
      bar.style.left = '50%';
      bar.style.width = pct + '%';
    } else {
      bar.style.right = '50%';
      bar.style.left = (50 - pct) + '%';
      bar.style.width = pct + '%';
    }

    barWrap.appendChild(bar);
    row.appendChild(barWrap);
    row.appendChild(el('span', 'fs-diplo-val', (val >= 0 ? '+' : '') + val));
    return row;
  }

  // ── Headcount bar ──
  function renderHcBar(label, count, maxCount, color) {
    var row = el('div', 'fs-hc-row');
    var lbl = label.replace(/_/g, ' ');
    row.appendChild(el('span', 'fs-hc-label', lbl));

    var barBg = el('div', 'fs-hc-bar-bg');
    var bar = el('div', 'fs-hc-bar');
    var pct = maxCount > 0 ? Math.min(count / maxCount * 100, 100) : 0;
    bar.style.width = pct + '%';
    bar.style.background = color || 'var(--gold, #c9a96e)';
    barBg.appendChild(bar);
    row.appendChild(barBg);
    row.appendChild(el('span', 'fs-hc-count', count.toLocaleString()));
    return row;
  }

  // ════════════════════════════════════════════
  //  MAIN RENDER
  // ════════════════════════════════════════════
  function render(frontmatter, md, container) {
    injectStyles();

    var fm = frontmatter;
    var arcs = fm.arcs || [];
    var currentArcKey = arcs.length ? arcs[0].arc : 1;
    var mdSections = parseMdSections(md);
    var maxVal = guessMaxStat(arcs);

    function currentArc() {
      for (var i = 0; i < arcs.length; i++) {
        if (arcs[i].arc === currentArcKey) return arcs[i];
      }
      return arcs[0] || {};
    }

    var sheet = el('div', 'fs-sheet');

    // ════════════════════════════════
    //  1. HEADER
    // ════════════════════════════════
    var header = el('div', 'fs-header');

    // Emblem
    var emblemWrap = el('div', 'fs-emblem-wrap');
    if (fm.emblem) {
      var img = document.createElement('img');
      img.src = 'Đạo/Ảnh/Thế_Lực/' + fm.emblem;
      img.alt = fm.name || '';
      img.onerror = function () {
        emblemWrap.innerHTML = '';
        var ph = el('div', 'fs-emblem-placeholder');
        ph.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M3 21V5a2 2 0 012-2h14a2 2 0 012 2v16l-4-3-3 3-3-3-3 3-3-3z"/></svg>';
        emblemWrap.appendChild(ph);
      };
      emblemWrap.appendChild(img);
    } else {
      var ph = el('div', 'fs-emblem-placeholder');
      ph.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M3 21V5a2 2 0 012-2h14a2 2 0 012 2v16l-4-3-3 3-3-3-3 3-3-3z"/></svg>';
      emblemWrap.appendChild(ph);
    }
    header.appendChild(emblemWrap);

    // Info block
    var info = el('div', 'fs-info');

    // Name + hantu
    var nameEl = el('div', 'fs-name');
    nameEl.textContent = fm.name || '???';
    if (fm.hantu) {
      var hantu = el('span', 'fs-hantu', '(' + fm.hantu + ')');
      nameEl.appendChild(hantu);
    }
    info.appendChild(nameEl);

    // Badges row
    var badges = el('div', 'fs-badges');

    if (fm.faction_type) {
      badges.appendChild(el('span', 'fs-badge fs-badge-type', fm.faction_type));
    }

    if (fm.alignment !== undefined) {
      var alignBadge = el('span', 'fs-badge fs-badge-alignment');
      var label = ALIGNMENT_LABELS[String(fm.alignment)] || 'Trung Lập';
      alignBadge.textContent = label + ' (' + fm.alignment + ')';
      alignBadge.style.background = alignColor(fm.alignment);
      badges.appendChild(alignBadge);
    }

    // Status badge (from current arc)
    var statusBadge = el('span', 'fs-badge fs-badge-status');
    function updateStatusBadge(arc) {
      var s = (arc && arc.status) || '—';
      statusBadge.textContent = s;
      statusBadge.style.background = STATUS_COLORS[s] || '#7a7067';
    }
    updateStatusBadge(currentArc());
    badges.appendChild(statusBadge);

    // Rank badge
    var rankBadge = el('span', 'fs-badge fs-badge-rank');
    function updateRankBadge(arc) {
      rankBadge.textContent = (arc && arc.rank) || '—';
    }
    updateRankBadge(currentArc());
    badges.appendChild(rankBadge);

    info.appendChild(badges);

    // Meta line: race, region, founded
    var meta = el('div', 'fs-meta');
    if (fm.race) meta.appendChild(el('span', null, '🏷 ' + fm.race));
    if (fm.region) meta.appendChild(el('span', null, '📍 ' + fm.region));
    if (fm.founded) meta.appendChild(el('span', null, '📜 ' + fm.founded));
    if (fm.founder) meta.appendChild(el('span', null, '👤 ' + fm.founder));
    info.appendChild(meta);

    // Leader
    var leaderEl = el('div', 'fs-leader');
    function updateLeader(arc) {
      leaderEl.textContent = (arc && arc.leader) ? 'Lãnh Đạo: ' + arc.leader : '';
    }
    updateLeader(currentArc());
    info.appendChild(leaderEl);

    // Population
    var popEl = el('div', 'fs-population');
    function updatePop(arc) {
      popEl.textContent = (arc && arc.population) ? 'Thành viên: ' + arc.population.toLocaleString() : '';
    }
    updatePop(currentArc());
    info.appendChild(popEl);

    header.appendChild(info);
    sheet.appendChild(header);

    // ════════════════════════════════
    //  2. ARC TIMELINE
    // ════════════════════════════════
    var arcButtons = [];
    if (arcs.length > 0) {
      var timeline = el('div', 'fs-timeline');
      timeline.appendChild(el('div', 'fs-timeline-label', 'Arc Timeline'));

      var track = el('div', 'fs-timeline-track');
      track.appendChild(el('div', 'fs-timeline-line'));

      arcs.forEach(function (a) {
        var btn = el('button', 'fs-arc-btn', String(a.arc));
        btn.setAttribute('data-arc', a.arc);
        if (a.arc === currentArcKey) btn.classList.add('fs-active');
        btn.addEventListener('click', function () { switchArc(a.arc); });
        track.appendChild(btn);
        arcButtons.push(btn);
      });

      timeline.appendChild(track);

      // Territory tags
      var territoryWrap = el('div', 'fs-territory');
      function updateTerritory(arc) {
        territoryWrap.innerHTML = '';
        if (arc && arc.territory) {
          arc.territory.forEach(function (t) {
            territoryWrap.appendChild(el('span', 'fs-territory-tag', t));
          });
        }
      }
      updateTerritory(currentArc());
      timeline.appendChild(territoryWrap);

      // Assets
      var assetsWrap = el('div', 'fs-assets');
      function updateAssets(arc) {
        assetsWrap.innerHTML = '';
        if (arc && arc.assets) {
          arc.assets.forEach(function (a) {
            var tag = el('span', 'fs-asset');
            tag.textContent = a.name;
            if (a.type) {
              tag.appendChild(el('span', 'fs-asset-type', ' [' + a.type + ']'));
            }
            assetsWrap.appendChild(tag);
          });
        }
      }
      updateAssets(currentArc());
      timeline.appendChild(assetsWrap);

      sheet.appendChild(timeline);
    }

    // ════════════════════════════════
    //  3. RADAR CHART
    // ════════════════════════════════
    var radarWrap = el('div', 'fs-radar-wrap');
    var radarState = createRadarChart(currentArc().stats, maxVal);
    radarWrap.appendChild(radarState.svg);
    sheet.appendChild(radarWrap);

    // ════════════════════════════════
    //  4. TABS
    // ════════════════════════════════
    var tabsContainer = el('div', 'fs-tabs');
    var tabBar = el('div', 'fs-tab-bar');
    var tabContent = el('div', 'fs-tab-content');
    var tabButtons = [];
    var activeTabId = TAB_DEFS[0].id;

    TAB_DEFS.forEach(function (def) {
      var btn = el('button', 'fs-tab-btn', def.label);
      btn.setAttribute('data-tab', def.id);
      if (def.id === activeTabId) btn.classList.add('fs-active');
      btn.addEventListener('click', function () { switchTab(def.id); });
      tabBar.appendChild(btn);
      tabButtons.push(btn);
    });

    tabsContainer.appendChild(tabBar);
    tabsContainer.appendChild(tabContent);
    sheet.appendChild(tabsContainer);

    function switchTab(tabId) {
      activeTabId = tabId;
      tabButtons.forEach(function (b) {
        b.classList.toggle('fs-active', b.getAttribute('data-tab') === tabId);
      });
      renderTabContent(tabId);
    }

    function renderTabContent(tabId) {
      tabContent.innerHTML = '';
      var inner;

      if (tabId === 'nhan-su') {
        inner = renderDivisionsTab(currentArc());
      } else if (tabId === 'ngoai-giao') {
        inner = el('div');
        // Show Section XI markdown (Mermaid chart etc.) above diplomacy bars
        var def = TAB_DEFS.filter(function (d) { return d.id === tabId; })[0];
        if (def && def.keywords) {
          var matched = findSections(mdSections, def.keywords);
          if (matched.length) inner.innerHTML = renderSections(matched);
        }
        inner.appendChild(renderDiplomacyTab(currentArc()));
      } else {
        var def = TAB_DEFS.filter(function (d) { return d.id === tabId; })[0];
        if (def && def.keywords) {
          var matched = findSections(mdSections, def.keywords);
          inner = el('div');
          inner.innerHTML = renderSections(matched);
        } else {
          inner = el('div');
          inner.innerHTML = '<p class="fs-empty">Chưa có thông tin.</p>';
        }
      }

      tabContent.appendChild(inner);
    }

    // ── Divisions tab ──
    function renderDivisionsTab(arc) {
      var wrap = el('div');
      if (!arc || !arc.divisions || !arc.divisions.length) {
        wrap.innerHTML = '<p class="fs-empty">Chưa có thông tin cơ cấu.</p>';
        return wrap;
      }

      arc.divisions.forEach(function (div) {
        var card = el('div', 'fs-division');

        // Header
        var dh = el('div', 'fs-division-header');
        dh.appendChild(el('span', 'fs-division-name', div.name));
        if (div.role) dh.appendChild(el('span', 'fs-division-role', div.role));
        card.appendChild(dh);

        // Headcount bars
        if (div.headcount) {
          var keys = Object.keys(div.headcount);
          var maxHc = 0;
          keys.forEach(function (k) { if (div.headcount[k] > maxHc) maxHc = div.headcount[k]; });

          var hcColors = ['#9b72cf', '#e87da0', '#d4a574', '#52b788', '#5a9ec4', '#e05252', '#7a7067'];
          keys.forEach(function (k, i) {
            card.appendChild(renderHcBar(k, div.headcount[k], maxHc, hcColors[i % hcColors.length]));
          });
        }

        // Members
        if (div.members && div.members.length) {
          var membersWrap = el('div', 'fs-members');
          div.members.forEach(function (m) {
            var row = el('div', 'fs-member');
            var nameSpan = el('span', 'fs-member-name' + (m.placeholder ? ' fs-placeholder' : ''), m.character);
            row.appendChild(nameSpan);
            if (m.position) row.appendChild(el('span', 'fs-member-pos', m.position));
            if (m.cultivation) row.appendChild(el('span', 'fs-member-cult', m.cultivation));
            membersWrap.appendChild(row);
          });
          card.appendChild(membersWrap);
        }

        wrap.appendChild(card);
      });

      return wrap;
    }

    // ── Diplomacy tab ──
    function renderDiplomacyTab(arc) {
      var wrap = el('div');
      if (!arc || !arc.relationships || !arc.relationships.length) {
        wrap.innerHTML = '<p class="fs-empty">Chưa có thông tin ngoại giao.</p>';
        return wrap;
      }

      arc.relationships.forEach(function (rel) {
        var card = el('div', 'fs-diplo-card');

        var dh = el('div', 'fs-diplo-header');
        dh.appendChild(el('span', 'fs-diplo-faction', rel.faction));
        card.appendChild(dh);

        if (rel.description) {
          card.appendChild(el('div', 'fs-diplo-desc', rel.description));
        }

        if (rel.diplomacy) {
          DIPLO_KEYS.forEach(function (key, idx) {
            var val = rel.diplomacy[key] || 0;
            card.appendChild(renderDiploBar(key, val, DIPLO_COLORS[idx], idx));
          });
        }

        wrap.appendChild(card);
      });

      return wrap;
    }

    // Render default tab
    renderTabContent(activeTabId);

    // ════════════════════════════════
    //  5. ARC SWITCHING
    // ════════════════════════════════
    function switchArc(key) {
      currentArcKey = key;
      var arc = currentArc();

      arcButtons.forEach(function (btn) {
        btn.classList.toggle('fs-active', Number(btn.getAttribute('data-arc')) === key);
      });

      updateStatusBadge(arc);
      updateRankBadge(arc);
      updateLeader(arc);
      updatePop(arc);
      updateTerritory(arc);
      updateAssets(arc);
      updateRadarChart(radarState, arc.stats, maxVal);

      // Re-render arc-dependent tabs
      if (activeTabId === 'nhan-su' || activeTabId === 'ngoai-giao') {
        renderTabContent(activeTabId);
      }
    }

    // ── Mount ──
    container.appendChild(sheet);
  }

  // ── Public API ──
  window.FactionSheet = {
    render: render
  };
})();
```

- [ ] **Step 2: Verify file was created correctly**

Read `scripts/faction-sheet.js` and confirm:
- IIFE wrapper present
- STAT_LABELS array has 6 faction stats in correct order
- DIPLO_KEYS array has 6 diplomacy axes
- CSS injection function with `fs-` prefixed class names (not `cs-`)
- `createRadarChart` function present
- `render` function present with 5 sections (header, timeline, radar, tabs, arc switching)
- `FactionSheet.render` exposed as public API
- Tab definitions include all 12 tabs (10 markdown + nhan-su + ngoai-giao)

- [ ] **Step 3: Commit**

```bash
git add scripts/faction-sheet.js
git commit -m "feat: create faction-sheet.js renderer with radar chart, divisions, and diplomacy bars"
```

---

## Chunk 3: Pilot Migration + Migration Script

### Task 4: Pilot Migration — Cửu Hoa Kiếm Tông (Large Faction)

**Files:**
- Modify: `Đạo/Thế_Lực/Cửu_Hoa_Kiếm_Tông.md`

This task adds the full YAML frontmatter from the spec's example to the largest, most-detailed faction file. The existing 7-section Roman content is restructured to 11 sections.

- [ ] **Step 1: Read current file**

Read `Đạo/Thế_Lực/Cửu_Hoa_Kiếm_Tông.md` to understand existing content structure.

- [ ] **Step 2: Add YAML frontmatter + restructure to 11 sections**

Prepend the YAML frontmatter from the spec (the full Cửu Hoa Kiếm Tông example in Section "Ví Dụ Hoàn Chỉnh"). Then restructure the existing markdown body:

- Keep existing sections I–V, renumber if needed
- Add empty sections VI (Đặc Sản), VII (Hạ Tầng), VIII (Kinh Tế) with `<!-- Cần bổ sung -->`
- Existing VI → new IX (Lịch Sử)
- Existing VII → new X (Giai Thoại)
- Add Section XI (Quan Hệ Thế Lực) with Mermaid relationship map
- Add Mermaid hierarchy chart to Section IV

Use the exact YAML from the spec's "Ví Dụ Hoàn Chỉnh: Cửu Hoa Kiếm Tông" section (lines 474-595 of the spec).

- [ ] **Step 3: Verify the file**

Read the modified file and confirm:
- YAML frontmatter parses correctly (all required fields present)
- 11 sections numbered I–XI with correct headings
- Existing content preserved in correct sections
- Mermaid charts present in sections IV and XI

- [ ] **Step 4: Test in browser**

Open `reader.html?file=Đạo/Thế_Lực/Cửu_Hoa_Kiếm_Tông.md` in browser. Verify:
- Faction sheet renders (not raw markdown)
- Header shows name, hantu, badges (Tông Môn, Thuần Chính, Hưng Thịnh, Hạng Nhất)
- Radar chart displays 6 stats
- Tabs work: Tổng Quan, Tổ Chức, Nhân Sự (divisions), Ngoại Giao (diplomacy bars)
- Arc timeline shows arc 1

- [ ] **Step 5: Commit**

```bash
git add "Đạo/Thế_Lực/Cửu_Hoa_Kiếm_Tông.md"
git commit -m "feat: pilot migration — add YAML frontmatter to Cửu Hoa Kiếm Tông"
```

---

### Task 5: Pilot Migration — Phế Linh Các (Small Faction)

**Files:**
- Modify: `Đạo/Thế_Lực/Phế_Linh_Các.md`

- [ ] **Step 1: Read current file**

Read `Đạo/Thế_Lực/Phế_Linh_Các.md` to understand existing content.

- [ ] **Step 2: Add YAML frontmatter + restructure**

Use the spec's Phế Linh Các example (lines 602-660 of spec) for frontmatter. Restructure existing content to 11 sections, adding empty sections where content doesn't exist.

- [ ] **Step 3: Verify and test in browser**

Read the file. Open in browser and verify faction sheet renders correctly for a small faction (simple layout, no Mermaid charts required for Hạng Năm).

- [ ] **Step 4: Commit**

```bash
git add "Đạo/Thế_Lực/Phế_Linh_Các.md"
git commit -m "feat: pilot migration — add YAML frontmatter to Phế Linh Các"
```

---

### Task 6: Pilot Migration — Cự Kình Bảo (Stub File)

**Files:**
- Modify: `Đạo/Thế_Lực/Cự_Kình_Bảo.md`

- [ ] **Step 1: Read current file**

Read `Đạo/Thế_Lực/Cự_Kình_Bảo.md` — this is a stub file (~2 lines).

- [ ] **Step 2: Add skeleton YAML frontmatter + 11 empty sections**

Since this is a stub, create a minimal but valid YAML frontmatter:

```yaml
---
type: faction
name: Cự Kình Bảo
hantu: 巨鯨堡
faction_type: Thành Trì
alignment: 0
race: Nhân Tộc
region: Vô Tận Hải
founded: ""
founder: ""
emblem: ""
specialty: ""
economy: []
arcs:
  - arc: 1
    status: Chưa Xác Định
    rank: ""
    leader: ""
    population: 0
    territory: []
    assets: []
    stats: [0, 0, 0, 0, 0, 0]
    divisions: []
    relationships: []
---
```

Then add the 11-section skeleton:

```markdown
# CỰ KÌNH BẢO (巨鯨堡)

## I. Tổng Quan
<!-- Cần bổ sung -->

## II. Địa Lý & Tài Nguyên
<!-- Cần bổ sung -->

... (all 11 sections with <!-- Cần bổ sung -->)
```

Fill in `name`, `hantu`, `faction_type`, `region` from whatever data exists in the stub. Leave other fields empty/zero.

- [ ] **Step 3: Verify and test**

Read the file. Verify YAML is valid. Open in browser — faction sheet should render with placeholder data (empty radar chart, no divisions, no diplomacy).

- [ ] **Step 4: Commit**

```bash
git add "Đạo/Thế_Lực/Cự_Kình_Bảo.md"
git commit -m "feat: pilot migration — add skeleton YAML to stub file Cự Kình Bảo"
```

---

### Task 7: Create Batch Migration Script

**Files:**
- Create: `scripts/migrate-factions.py`

This Python script automates adding skeleton YAML frontmatter to the remaining ~225 faction files. It reads existing content, extracts what data it can (name, hantu from H1 heading), and prepends a skeleton frontmatter.

- [ ] **Step 1: Create the migration script**

```python
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

# Region guesses from directory/filename patterns
REGION_DEFAULTS = {
    'Băng': 'Bắc Băng', 'Tuyết': 'Bắc Băng', 'Hàn': 'Bắc Băng',
    'Sa': 'Tây Mạc', 'Mạc': 'Tây Mạc', 'Viêm': 'Tây Mạc',
    'Hải': 'Vô Tận Hải', 'Long': 'Vô Tận Hải', 'Kình': 'Vô Tận Hải',
}


def has_frontmatter(content):
    """Check if file already has YAML frontmatter."""
    return content.strip().startswith('---')


def extract_h1(content):
    """Extract name and hantu from H1 heading like '# TÊN (漢字)'."""
    m = re.search(r'^#\s+(.+?)(?:\s*\(([^)]+)\))?\s*$', content, re.MULTILINE)
    if m:
        return m.group(1).strip(), (m.group(2) or '').strip()
    return '', ''


def guess_region(name, content):
    """Guess region from name keywords."""
    for keyword, region in REGION_DEFAULTS.items():
        if keyword in name or keyword in content[:200]:
            return region
    return 'Đông Hoang'  # default


def build_skeleton_yaml(name, hantu, region):
    """Build minimal YAML frontmatter dict."""
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
    """Add skeleton YAML frontmatter to a single file."""
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
```

- [ ] **Step 2: Test dry run**

Run: `cd /Users/sampi_wu/Documents/GitHub/Obsidian_Novel_v2 && python3 scripts/migrate-factions.py`

Expected: Output listing ~225 files as "WOULD MIGRATE" and 3 as "skip" (the pilot files already migrated).

- [ ] **Step 3: Test single file apply**

Run: `python3 scripts/migrate-factions.py --apply --file Bạch_Cốt_Hội.md`

Expected: 1 file migrated. Read the file to verify YAML frontmatter was added correctly, existing content preserved.

- [ ] **Step 4: Revert the test migration**

Run: `git checkout -- "Đạo/Thế_Lực/Bạch_Cốt_Hội.md"`

This reverts the test migration so the file is clean for the actual batch run.

- [ ] **Step 5: Commit the migration script**

```bash
git add scripts/migrate-factions.py
git commit -m "feat: add batch migration script for faction YAML frontmatter"
```

---

### Task 8: Run Batch Migration

**Files:**
- Modify: All ~225 remaining files in `Đạo/Thế_Lực/`

- [ ] **Step 1: Run batch migration**

Run: `python3 scripts/migrate-factions.py --apply`

Expected: ~225 files migrated, 3 skipped (pilot files).

- [ ] **Step 2: Verify sample of migrated files**

Read 3 random migrated files to confirm:
- YAML frontmatter present and parseable
- Original content preserved below the frontmatter
- H1 name/hantu correctly extracted

- [ ] **Step 3: Test a migrated file in browser**

Open a recently migrated file (e.g., `reader.html?file=Đạo/Thế_Lực/Bạch_Cốt_Hội.md`). Verify:
- Faction sheet renders (even with skeleton data)
- No JavaScript errors in console
- Tabs display existing markdown content correctly

- [ ] **Step 4: Commit all migrated files**

```bash
git add Đạo/Thế_Lực/
git commit -m "feat: batch migrate 225 faction files with skeleton YAML frontmatter"
```

---

### Task 9: Update Faction Index

**Files:**
- Modify: `Đạo/Thế_Lực/index.md` (if needed — verify it still works after migration)

- [ ] **Step 1: Verify index.md**

Read `Đạo/Thế_Lực/index.md` and confirm all 228 faction links still work. The index references H1 headings, which should be preserved after migration.

- [ ] **Step 2: Commit if changes needed**

If index needs updating:
```bash
git add "Đạo/Thế_Lực/index.md"
git commit -m "fix: update faction index after migration"
```

---

## Summary

| Task | Description | Chunk |
|------|-------------|-------|
| 1 | Update `.jules/Thế_Lực.md` agent instructions | 1 |
| 2 | Add faction routing to `reader.html` | 1 |
| 3 | Create `scripts/faction-sheet.js` (full renderer) | 2 |
| 4 | Pilot: Cửu Hoa Kiếm Tông (large faction) | 3 |
| 5 | Pilot: Phế Linh Các (small faction) | 3 |
| 6 | Pilot: Cự Kình Bảo (stub file) | 3 |
| 7 | Create `scripts/migrate-factions.py` | 3 |
| 8 | Run batch migration (~225 files) | 3 |
| 9 | Verify faction index | 3 |
