# Character Sheet System — Design Spec

## Goal

Replace the raw markdown rendering of character profiles (`Đạo/Nhân_Vật/*.md`) in `reader.html` with a DnD-inspired character sheet featuring an avatar, SVG radar chart, arc-based stat tracking with a timeline slider, tabbed content panels, inventory, and relationship tracking with feeling bars.

## Data Format

Character markdown files gain YAML frontmatter. The `type: character` field signals `reader.html` to render the character sheet instead of plain markdown.

```yaml
---
type: character
name: Diệp Tĩnh Sương
hantu: 葉靜霜
archetype: Kiếm Tu
race: Người
avatar: Diệp_Tĩnh_Sương.png
arcs:
  - arc: 1
    status: Còn Sống
    cultivation: Luyện Khí Tầng 5
    methods: [Hàn Băng Kiếm Quyết]
    inventory:
      - name: Phổ Thông Kiếm
        type: Vũ Khí
    stats: [15, 20, 10, 25, 15, 15]
    relationships:
      - character: Lâm Phong
        description: Bạn đồng hành mới quen
        feelings:
          yeu: 10
          han: 0
          kinh: 20
          tin: 30
          so: 0
          on: 15
  - arc: 5
    status: Còn Sống
    cultivation: Trúc Cơ Trung Kỳ
    methods: [Hàn Băng Kiếm Quyết, Băng Tâm Quyết]
    inventory:
      - name: Hàn Băng Kiếm
        type: Vũ Khí
      - name: Hộ Thân Ngọc Bội
        type: Pháp Bảo
      - name: Băng Tâm Đan
        type: Đan Dược
    stats: [80, 120, 60, 90, 70, 80]
    relationships:
      - character: Lâm Phong
        description: Đồng hành đáng tin cậy
        feelings:
          yeu: 30
          han: 0
          kinh: 40
          tin: 70
          so: 0
          on: 50
---

## Ngoại Hình
...markdown content (header text varies per file)...

## Năng Lực
...

## Cốt Truyện
...
```

### Frontmatter Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `type` | string | Yes | Must be `"character"` to trigger sheet rendering |
| `name` | string | Yes | Character's Vietnamese name |
| `hantu` | string | No | Chinese characters for the name |
| `archetype` | string | Yes | Character class (Kiếm Tu, Cung Thủ, Đan Sư, etc.) |
| `race` | string | Yes | Race/species |
| `avatar` | string | No | Filename in `Đạo/Ảnh/Nhân_Vật/`. If missing, show placeholder silhouette |
| `arcs` | array | Yes | Array of arc entries (see below) |

### Arc Entry Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `arc` | number | Yes | Arc number |
| `status` | string | Yes | Free text (Còn Sống, Tử Vong, Hồn Phách, Đoạt Xá, etc.) |
| `cultivation` | string | Yes | Current cultivation level (e.g. "Trúc Cơ Trung Kỳ") |
| `methods` | string[] | Yes | List of cultivation methods |
| `inventory` | object[] | No | Items: `{name, type}`. Types: Vũ Khí, Đan Dược, Pháp Bảo, etc. |
| `stats` | number[6] | Yes | `[Thể Lực, Linh Lực, Trí Tuệ, Tốc Độ, Phòng Ngự, Tâm Tính]`. Uncapped absolute values. |
| `relationships` | object[] | No | See Relationship fields below |

### Relationship Fields

| Field | Type | Description |
|-------|------|-------------|
| `character` | string | Name of the related character |
| `description` | string | Short description of the relationship |
| `feelings` | object | Six axes, each -100 to +100 |
| `feelings.yeu` | number | Love/Affection (-100 = disgust, 0 = neutral, +100 = absolute devotion) |
| `feelings.han` | number | Hate/Resentment (-100 = forgiveness, 0 = neutral, +100 = murderous hatred) |
| `feelings.kinh` | number | Respect/Admiration (-100 = contempt, 0 = neutral, +100 = reverence) |
| `feelings.tin` | number | Trust (-100 = total distrust, 0 = neutral, +100 = absolute trust) |
| `feelings.so` | number | Fear (-100 = fearless/bold toward them, 0 = neutral, +100 = terrified) |
| `feelings.on` | number | Gratitude/Debt (-100 = resentment/feels owed, 0 = neutral, +100 = life debt) |

Each axis ranges from **-100 to +100**. Negative = opposite sentiment, 0 = neutral, positive = strong feeling. A character can simultaneously have high Yêu and high Hận toward the same person. The feeling bars display as horizontal bars from a center line — negative extends left (dimmed), positive extends right (bright). Each axis has its own color: Yêu (pink), Hận (red), Kính (gold), Tin (green), Sợ (purple), Ơn (blue).

### Stats

Six uncapped absolute values. Order: `[Thể Lực, Linh Lực, Trí Tuệ, Tốc Độ, Phòng Ngự, Tâm Tính]`.

- **Thể Lực** — Physical power
- **Linh Lực** — Spiritual energy
- **Trí Tuệ** — Wisdom/knowledge (accumulates with experience)
- **Tốc Độ** — Speed/agility
- **Phòng Ngự** — Defense/durability
- **Tâm Tính** — Mental fortitude/willpower

**Tổng Lực** = sum of all 6 stats. Displayed prominently. Communicates absolute power scale at a glance.

Values scale with cultivation level. A Luyện Khí character might total ~100, a Trúc Cơ ~500, a Nguyên Anh ~5000+. Agents update stats at the beginning of each arc.

## Sheet Layout

```
┌─────────────────────────────────────────────┐
│  ┌──────┐   Name (Hán Tự)                  │
│  │Avatar│   Archetype Badge    Status Badge  │
│  │      │   Race · Cultivation Level         │
│  └──────┘   ⚔ Tổng Lực: 500                │
├─────────────────────────────────────────────┤
│         ◄━━ Arc Timeline Slider ━━►          │
├─────────────────────────────────────────────┤
│                                             │
│         ┌─ SVG Radar Chart ──┐              │
│         │    ╱╲              │              │
│         │   ╱  ╲             │              │
│         │  ╱    ╲            │              │
│         │  ╲    ╱            │              │
│         │   ╲  ╱             │              │
│         │    ╲╱              │              │
│         └────────────────────┘              │
│                                             │
├─────────────────────────────────────────────┤
│  [Ngoại Hình] [Năng Lực] [Cốt Truyện]      │
│  [Trang Bị]   [Quan Hệ]                    │
├─────────────────────────────────────────────┤
│  Tab content area                           │
│                                             │
└─────────────────────────────────────────────┘
```

### Header Zone

- **Avatar** (left): Image from `Đạo/Ảnh/Nhân_Vật/{avatar}`. If no avatar file, display a CSS-only placeholder — a rounded rectangle with a generic silhouette icon (using a simple SVG person outline) in `--muted` color on `--ink` background.
- **Info** (right of avatar):
  - Character name + Hán Tự in parentheses
  - Archetype badge (e.g. "Kiếm Tu")
  - Status badge — color-coded by keyword in the status string: contains "Sống" → green, contains "Vong" or "Death" → red, contains "Hồn" or "Ý Chí" → blue, contains "Xá" or "Sinh" → purple, default → `--muted` gray
  - Race + Cultivation level text (e.g. "Người · Trúc Cơ Trung Kỳ")
  - Tổng Lực: sum displayed with ⚔ icon prefix

### Arc Timeline Slider

- Custom div-based slider with clickable arc number buttons (not `<input type="range">`).
- Only shows arc numbers that have data (e.g. if a character has arcs [1, 3, 5], only those 3 are shown — no gaps).
- Sliding updates: header (status, cultivation, Tổng Lực), radar chart, Trang Bị tab, Quan Hệ tab.
- Default position: latest arc.
- Radar chart polygon animates (CSS transition on SVG points) when arc changes.
- Also shows the `methods` list for the selected arc below the slider.

### SVG Radar Chart

- 6-axis radar chart using inline SVG.
- Axes labeled: Thể Lực, Linh Lực, Trí Tuệ, Tốc Độ, Phòng Ngự, Tâm Tính.
- Values are absolute but the chart normalizes to the character's own max stat for that arc (so the shape shows relative strengths).
- Normalization formula: `value / max(stats)`. If all stats are 0, render an empty chart. If all stats are equal, render a full hexagon.
- Uses CSS variables for colors — auto-adapts to all 5 themes.
- Grid lines at 25%, 50%, 75%, 100% of max.
- Filled polygon with semi-transparent accent color.
- Smooth CSS transition when arc slider changes.

### Tabs

5 tabs with content area below:

1. **Ngoại Hình** — Appearance & Personality. Static (does not change with arc).
2. **Năng Lực** — Abilities & Cultivation. Static.
3. **Cốt Truyện** — Plot history. Static.

Tabs 1-3 are parsed from the markdown body below the frontmatter. Existing character files use inconsistent header formats (e.g. `## NGOẠI HÌNH`, `## II. NGOẠI HÌNH & TÍNH CÁCH`, `## III. NGOẠI HÌNH & KHÍ CHẤT`). The parser should match sections by **keyword search** in the heading text:
- Ngoại Hình tab: heading contains "NGOẠI HÌNH" or "TÍNH CÁCH"
- Năng Lực tab: heading contains "NĂNG LỰC" or "CÔNG PHÁP" or "SỨC MẠNH" or "KỸ NĂNG"
- Cốt Truyện tab: heading contains "CỐT TRUYỆN" or "SỰ KIỆN" or "LỊCH SỬ"

Content from the heading until the next `##` heading is captured. Sections not found render as "Chưa có thông tin." (No information yet).
4. **Trang Bị** — Inventory. From frontmatter `inventory` array, filtered by current arc. Each item displays name + type badge. Arc-dependent.
5. **Quan Hệ** — Relationships. From frontmatter `relationships` array, filtered by current arc. Arc-dependent.

### Relationship Display

Each relationship entry shows:
- Character name (bold)
- Short description text
- 6 horizontal feeling bars:
  - Each bar: label on left, horizontal bar from center, value on right
  - Center line = 0. Negative extends left (dimmed color), positive extends right (bright color)
  - Range: -100 to +100
  - Each axis has its own color: Yêu (pink), Hận (red), Kính (gold), Tin (green), Sợ (purple), Ơn (blue)

## Detection & Rendering Logic

1. `reader.html` fetches the markdown file (existing behavior).
2. Replace the existing frontmatter-stripping regex (`md.replace(/^---\n[\s\S]*?\n---\n/, '')`) with proper YAML parsing using `js-yaml`.
3. If content starts with `---`, extract frontmatter via `jsyaml.load()` and separate the markdown body.
4. If `frontmatter.type === 'character'`, call `CharacterSheet.render(frontmatter, markdownBody)` instead of normal markdown rendering.
5. Otherwise, pass the markdown body (without frontmatter) to `marked.js` as before.
6. If `js-yaml` CDN fails to load, fall back to the old regex stripping and render as plain markdown.
7. If YAML is malformed or required fields are missing, render as plain markdown with a console warning.
8. The file `Đạo/Nhân_Vật/index.md` is a directory listing, not a character — it will not have `type: character` frontmatter, so it renders normally.

## Dependencies

- **js-yaml** (~30kb minified, ~10kb gzipped) via CDN for YAML frontmatter parsing.
- No other new dependencies.

## Files

| File | Action | Description |
|------|--------|-------------|
| `scripts/character-sheet.js` | Create | Character sheet renderer: SVG radar, slider, tabs, relationship bars. CSS injected via JS (same pattern as `chapter-lock.js`). |
| `reader.html` | Modify | Add js-yaml CDN script tag, add character-sheet.js script tag, replace frontmatter regex with YAML parsing, add theme variable system (adopt `data-theme` from index.html). |
| `Đạo/Nhân_Vật/*.md` | Modify | Add YAML frontmatter to character files (can be done incrementally) |
| `Đạo/Ảnh/Nhân_Vật/` | Existing | Avatar images stored here. Placeholder used when no image exists. |

## Theming

All styling uses CSS variables from the existing theme system. The character sheet auto-adapts to all 5 themes:
- Thủy Mặc (default), Huyết Nguyệt, Thanh Trúc, Cổ Thư, Bạch Tuyết.

reader.html currently has its own hardcoded CSS variables (Cổ Thư palette only) and does not respond to `data-theme`. As a prerequisite, reader.html must be updated to adopt the multi-theme variable system from index.html so the character sheet (and the rest of the reader) can theme-switch.

Key variables used: `--void`, `--deep`, `--ink`, `--text`, `--accent`, `--accent-dim`, `--accent-bright`, `--muted`, `--card-bg`, `--card-border`.

## Responsive Design

- On desktop (>768px): avatar and info side by side, radar chart centered.
- On mobile (<768px): avatar above info (stacked), radar chart full width, tabs scroll horizontally if needed.

## UI Defaults

- **Default tab:** Ngoại Hình (first tab) is active on page load.
- **Default arc:** Latest arc (last in the `arcs` array) is selected on page load.
- **Inventory item types** are open-ended (free text). Common types: Vũ Khí, Đan Dược, Pháp Bảo, Trận Kỳ, Linh Thảo. Unknown types render with default `--muted` badge color.

## Agent Instructions

Agents (Jules, Claude, Gemini) should update character frontmatter at the beginning of each new arc:
1. Add a new arc entry with updated stats, cultivation, status, inventory, and relationships.
2. Do not modify previous arc entries (they are historical).
3. Stats should reflect the character's power at the start of the arc.
4. Feeling values range from -100 to +100 (negative = opposite sentiment, 0 = neutral, positive = strong feeling).
