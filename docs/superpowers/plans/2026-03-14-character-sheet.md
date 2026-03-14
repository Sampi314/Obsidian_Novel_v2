# Character Sheet System Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace raw markdown rendering of character profiles in `reader.html` with a DnD-inspired character sheet featuring SVG radar chart, arc timeline slider, tabbed content, inventory, and relationship feeling bars.

**Architecture:** New `scripts/character-sheet.js` renders a character sheet when `reader.html` detects `type: character` in YAML frontmatter. js-yaml (CDN) parses frontmatter. All CSS injected via JS. reader.html gets multi-theme support via `data-theme` CSS variables copied from index.html.

**Tech Stack:** Vanilla JS, inline SVG for radar chart, js-yaml via CDN, CSS variables for theming.

---

## File Structure

| File | Action | Responsibility |
|------|--------|----------------|
| `scripts/character-sheet.js` | Create | Full character sheet: CSS injection, header, avatar, arc slider, SVG radar, tabs (markdown + inventory + relationships), feeling bars |
| `reader.html` | Modify | Add js-yaml CDN, add character-sheet.js script, add theme variables for all 5 themes, replace frontmatter regex with YAML parsing, route `type: character` to CharacterSheet |
| `Đạo/Nhân_Vật/Diệp_Tĩnh_Sương.md` | Modify | Add sample YAML frontmatter (proof-of-concept character) |

---

### Task 1: Add multi-theme CSS variables to reader.html

**Files:**
- Modify: `reader.html:10-44`

Currently reader.html has hardcoded Cổ Thư-only CSS variables in `:root`. We need to add `data-theme` selectors for all 5 themes (matching index.html) and add a script to apply the saved theme on page load.

- [ ] **Step 1: Add theme init script to reader.html head**

Add after line 6 (before the marked.js script tag) in `reader.html`:

```html
<script>
    (function(){
        var t=localStorage.getItem('co-nguyen-theme')||'thuy-mac';
        document.documentElement.setAttribute('data-theme',t);
    })();
</script>
```

- [ ] **Step 2: Replace `:root` CSS variables with themed versions**

Replace the existing `:root` block (lines 16-44) with themed variable sets. Keep the existing variable names (`--void`, `--abyss`, `--ink`, `--gold`, `--bone`, `--ash`, etc.) as aliases that map from the theme system. The approach: add `[data-theme]` selectors that override the reader's own variables.

Add these theme selectors **before** the existing `:root` block:

```css
/* ── Multi-Theme Support ── */
:root, [data-theme="co-thu"] {
    --void: #0a0908; --ink: #1a1714;
    --gold: #c9a96e; --gold-bright: #e4c98a; --gold-dim: #8a7549;
    --bone: #d4cbbf; --ash: #7a7067;
    --crimson: #6b1c23; --crimson-bright: #9b2c3a;
    --jade: #2d6a4f; --jade-bright: #40916c;
}
[data-theme="thuy-mac"] {
    --void: #0c0f14; --ink: #151a22;
    --gold: #d4a574; --gold-bright: #e8be8e; --gold-dim: #9b7a52;
    --bone: #e8e0d4; --ash: #6a7080;
    --crimson: #7a3040; --crimson-bright: #a64458;
    --jade: #6b8f71; --jade-bright: #82ab88;
}
[data-theme="huyet-nguyet"] {
    --void: #100808; --ink: #1c1212;
    --gold: #c4746c; --gold-bright: #e09088; --gold-dim: #8a524c;
    --bone: #e8dcd8; --ash: #7a6468;
    --crimson: #8a2020; --crimson-bright: #b83030;
    --jade: #6b8f71; --jade-bright: #82ab88;
}
[data-theme="thanh-truc"] {
    --void: #080f0c; --ink: #121c16;
    --gold: #7ab88a; --gold-bright: #96d4a6; --gold-dim: #5a8a66;
    --bone: #dce8e0; --ash: #607a68;
    --crimson: #7a3040; --crimson-bright: #a64458;
    --jade: #4a9a6a; --jade-bright: #60b880;
}
[data-theme="bach-tuyet"] {
    --void: #f5f0e8; --ink: #faf6ef;
    --gold: #8a6020; --gold-bright: #a07428; --gold-dim: #b8a06a;
    --bone: #2a2420; --ash: #7a7068;
    --crimson: #8a3545; --crimson-bright: #a64458;
    --jade: #4a7a52; --jade-bright: #5a9060;
}
```

Then remove the duplicate color definitions from the existing `:root` block, keeping only layout variables (`--bg-color`, `--text-color`, `--font-family`, `--line-height`, `--font-size`, `--max-width`) that reference the themed variables.

- [ ] **Step 3: Verify theme switching works**

Open `reader.html` in the browser, switch themes via the navbar dropdown, and confirm colors change across the page.

- [ ] **Step 4: Commit**

```bash
git add reader.html
git commit -m "feat: add multi-theme support to reader.html"
```

---

### Task 2: Add js-yaml CDN and frontmatter parsing to reader.html

**Files:**
- Modify: `reader.html:7` (add script tag)
- Modify: `reader.html:451-493` (fetch/render flow)

- [ ] **Step 1: Add js-yaml CDN script tag**

Add after the marked.js script tag (line 7):

```html
<script src="https://cdn.jsdelivr.net/npm/js-yaml@4.1.0/dist/js-yaml.min.js"></script>
```

- [ ] **Step 2: Add character-sheet.js script tag**

Add after the chapter-lock.js script tag (near end of file, before closing `</body>`):

```html
<script src="scripts/character-sheet.js"></script>
```

- [ ] **Step 3: Replace frontmatter stripping with YAML parsing**

Replace lines 455-456 (the frontmatter regex strip):

```javascript
// Strip YAML frontmatter
md = md.replace(/^---\n[\s\S]*?\n---\n/, '');
```

With:

```javascript
// Parse YAML frontmatter
var frontmatter = null;
var fmMatch = md.match(/^---\n([\s\S]*?)\n---\n([\s\S]*)$/);
if (fmMatch && window.jsyaml) {
    try {
        frontmatter = jsyaml.load(fmMatch[1]);
        md = fmMatch[2];
    } catch (e) {
        console.warn('YAML parse error, rendering as plain markdown:', e);
        md = md.replace(/^---\n[\s\S]*?\n---\n/, '');
    }
} else if (fmMatch) {
    md = fmMatch[2]; // js-yaml not loaded, just strip
}
```

- [ ] **Step 4: Route character type to CharacterSheet renderer**

Replace lines 489-493 (the isChapter routing):

```javascript
if (isChapter) {
    loadChapterMode(html);
} else {
    loadWikiMode(html);
}
```

With:

```javascript
if (frontmatter && frontmatter.type === 'character' && window.CharacterSheet) {
    loadWikiMode(''); // set up wiki page shell (back link, footer)
    var container = document.querySelector('.wiki-content');
    container.innerHTML = '';
    CharacterSheet.render(frontmatter, md, container);
} else if (isChapter) {
    loadChapterMode(html);
} else {
    loadWikiMode(html);
}
```

- [ ] **Step 5: Verify non-character pages still render normally**

Open `reader.html?file=Đạo/Nhân_Vật/index.md` and confirm it renders as before (plain markdown).

- [ ] **Step 6: Commit**

```bash
git add reader.html
git commit -m "feat: add YAML frontmatter parsing and character sheet routing"
```

---

### Task 3: Create character-sheet.js — CSS injection and header

**Files:**
- Create: `scripts/character-sheet.js`

Build the foundation: IIFE, CSS injection, header rendering (avatar, name, badges, Tổng Lực).

- [ ] **Step 1: Create character-sheet.js with IIFE, config, CSS, and header**

Create `scripts/character-sheet.js`:

```javascript
// scripts/character-sheet.js
(function () {
  'use strict';

  var STAT_LABELS = ['Thể Lực', 'Linh Lực', 'Trí Tuệ', 'Tốc Độ', 'Phòng Ngự', 'Tâm Tính'];
  var FEELING_KEYS = ['yeu', 'han', 'kinh', 'tin', 'so', 'on'];
  var FEELING_LABELS = ['Yêu', 'Hận', 'Kính', 'Tin', 'Sợ', 'Ơn'];
  var FEELING_COLORS = ['#e87da0', '#e05252', '#d4a574', '#52b788', '#9b72cf', '#5a9ec4'];
  var AVATAR_BASE = 'Đạo/Ảnh/Nhân_Vật/';

  function getStatusColor(status) {
    if (!status) return 'var(--ash)';
    var s = status.toLowerCase();
    if (s.indexOf('sống') !== -1) return '#52b788';
    if (s.indexOf('vong') !== -1 || s.indexOf('chết') !== -1) return '#e05252';
    if (s.indexOf('hồn') !== -1 || s.indexOf('ý chí') !== -1) return '#5a9ec4';
    if (s.indexOf('xá') !== -1 || s.indexOf('sinh') !== -1) return '#9b72cf';
    return 'var(--ash)';
  }

  function sumStats(stats) {
    if (!stats || !stats.length) return 0;
    var s = 0;
    for (var i = 0; i < stats.length; i++) s += (stats[i] || 0);
    return s;
  }

  function getArc(data, arcNum) {
    if (!data.arcs || !data.arcs.length) return null;
    for (var i = 0; i < data.arcs.length; i++) {
      if (data.arcs[i].arc === arcNum) return data.arcs[i];
    }
    return data.arcs[data.arcs.length - 1];
  }

  function latestArc(data) {
    if (!data.arcs || !data.arcs.length) return null;
    return data.arcs[data.arcs.length - 1];
  }

  // ── CSS ──
  function injectStyles() {
    if (document.getElementById('cs-styles')) return;
    var style = document.createElement('style');
    style.id = 'cs-styles';
    style.textContent = [
      '.cs-sheet { max-width: 900px; margin: 0 auto; font-family: "Lora", "Georgia", serif; }',

      // Header
      '.cs-header { display: flex; gap: 20px; align-items: flex-start; padding: 24px; background: var(--ink); border: 1px solid var(--gold-dim, var(--ash)); border-radius: 8px; margin-bottom: 2px; }',
      '.cs-avatar-wrap { width: 120px; height: 120px; border-radius: 8px; overflow: hidden; flex-shrink: 0; border: 2px solid var(--gold-dim, var(--ash)); background: var(--void); display: flex; align-items: center; justify-content: center; }',
      '.cs-avatar-wrap img { width: 100%; height: 100%; object-fit: cover; }',
      '.cs-avatar-placeholder { color: var(--ash); font-size: 48px; opacity: 0.4; }',
      '.cs-info { flex: 1; min-width: 0; }',
      '.cs-name { font-family: "Playfair Display", serif; font-size: 1.8rem; font-weight: 600; color: var(--gold); margin-bottom: 4px; }',
      '.cs-hantu { color: var(--ash); font-size: 1rem; margin-left: 8px; }',
      '.cs-badges { display: flex; gap: 8px; flex-wrap: wrap; margin: 8px 0; }',
      '.cs-badge { padding: 2px 10px; border-radius: 4px; font-size: 0.75rem; letter-spacing: 0.05em; border: 1px solid; }',
      '.cs-badge-archetype { color: var(--gold); border-color: var(--gold-dim); }',
      '.cs-badge-status { border-color: currentColor; }',
      '.cs-meta { color: var(--ash); font-size: 0.9rem; margin: 4px 0; }',
      '.cs-tong-luc { color: var(--gold); font-size: 1.1rem; font-weight: 600; margin-top: 6px; }',

      // Arc slider
      '.cs-arc-slider { display: flex; align-items: center; gap: 0; padding: 12px 24px; background: var(--ink); border: 1px solid var(--gold-dim, var(--ash)); border-top: none; border-radius: 0; }',
      '.cs-arc-label { color: var(--ash); font-size: 0.8rem; margin-right: 12px; white-space: nowrap; }',
      '.cs-arc-track { display: flex; gap: 0; flex: 1; position: relative; }',
      '.cs-arc-line { position: absolute; top: 50%; left: 0; right: 0; height: 2px; background: var(--ash); opacity: 0.3; transform: translateY(-50%); }',
      '.cs-arc-btn { position: relative; z-index: 1; width: 36px; height: 36px; border-radius: 50%; border: 2px solid var(--ash); background: var(--void); color: var(--bone, var(--ash)); font-size: 0.8rem; font-family: inherit; cursor: pointer; transition: all 0.2s; display: flex; align-items: center; justify-content: center; }',
      '.cs-arc-btn:hover { border-color: var(--gold); color: var(--gold); }',
      '.cs-arc-btn.cs-active { border-color: var(--gold); background: var(--gold); color: var(--void); font-weight: 700; }',
      '.cs-methods { padding: 8px 24px 12px; background: var(--ink); border: 1px solid var(--gold-dim, var(--ash)); border-top: none; border-radius: 0 0 8px 8px; margin-bottom: 16px; }',
      '.cs-methods-list { display: flex; gap: 8px; flex-wrap: wrap; }',
      '.cs-method-tag { color: var(--gold-bright, var(--gold)); font-size: 0.8rem; padding: 2px 8px; border: 1px solid var(--gold-dim); border-radius: 3px; }',

      // Radar chart
      '.cs-radar-wrap { display: flex; justify-content: center; padding: 20px; background: var(--ink); border: 1px solid var(--gold-dim, var(--ash)); border-radius: 8px; margin-bottom: 16px; }',
      '.cs-radar-svg { width: 300px; height: 300px; }',
      '.cs-radar-grid { fill: none; stroke: var(--ash); stroke-width: 0.5; opacity: 0.3; }',
      '.cs-radar-axis { stroke: var(--ash); stroke-width: 0.5; opacity: 0.3; }',
      '.cs-radar-poly { fill: var(--gold); fill-opacity: 0.2; stroke: var(--gold); stroke-width: 2; transition: all 0.4s ease; }',
      '.cs-radar-label { fill: var(--bone, var(--ash)); font-size: 11px; font-family: "Lora", serif; }',
      '.cs-radar-value { fill: var(--gold); font-size: 10px; font-family: "Lora", serif; font-weight: 600; }',

      // Tabs
      '.cs-tabs { display: flex; gap: 0; border-bottom: 2px solid var(--gold-dim, var(--ash)); margin-bottom: 0; overflow-x: auto; }',
      '.cs-tab { padding: 10px 16px; background: none; border: none; color: var(--ash); font-family: inherit; font-size: 0.85rem; cursor: pointer; border-bottom: 2px solid transparent; margin-bottom: -2px; transition: all 0.2s; white-space: nowrap; }',
      '.cs-tab:hover { color: var(--gold); }',
      '.cs-tab.cs-active { color: var(--gold); border-bottom-color: var(--gold); }',
      '.cs-tab-content { padding: 20px 0; min-height: 100px; }',
      '.cs-tab-content .wiki-content { max-width: none; }',
      '.cs-tab-empty { color: var(--ash); font-style: italic; }',

      // Inventory
      '.cs-inv-list { list-style: none; padding: 0; }',
      '.cs-inv-item { display: flex; align-items: center; gap: 10px; padding: 8px 12px; border-bottom: 1px solid rgba(127,127,127,0.1); }',
      '.cs-inv-name { flex: 1; color: var(--bone, var(--ash)); }',
      '.cs-inv-type { font-size: 0.75rem; padding: 2px 8px; border-radius: 3px; color: var(--gold); border: 1px solid var(--gold-dim); }',

      // Relationships
      '.cs-rel-entry { padding: 16px 0; border-bottom: 1px solid rgba(127,127,127,0.1); }',
      '.cs-rel-name { font-weight: 600; color: var(--gold); font-size: 1rem; }',
      '.cs-rel-desc { color: var(--ash); font-size: 0.85rem; margin: 4px 0 10px; }',
      '.cs-feeling-row { display: flex; align-items: center; gap: 8px; margin: 4px 0; }',
      '.cs-feeling-label { width: 36px; font-size: 0.75rem; color: var(--ash); text-align: right; }',
      '.cs-feeling-bar-wrap { flex: 1; height: 14px; background: rgba(127,127,127,0.1); border-radius: 3px; position: relative; overflow: hidden; }',
      '.cs-feeling-center { position: absolute; left: 50%; top: 0; bottom: 0; width: 1px; background: var(--ash); opacity: 0.5; }',
      '.cs-feeling-fill { position: absolute; top: 1px; bottom: 1px; border-radius: 2px; transition: all 0.3s; }',
      '.cs-feeling-val { width: 32px; font-size: 0.7rem; color: var(--ash); }',

      // Responsive
      '@media (max-width: 768px) {',
      '  .cs-header { flex-direction: column; align-items: center; text-align: center; }',
      '  .cs-badges { justify-content: center; }',
      '  .cs-radar-svg { width: 260px; height: 260px; }',
      '  .cs-tabs { gap: 0; }',
      '  .cs-tab { padding: 8px 10px; font-size: 0.78rem; }',
      '}',
    ].join('\n');
    document.head.appendChild(style);
  }

  // ── Header ──
  function renderHeader(data, arc, container) {
    var header = document.createElement('div');
    header.className = 'cs-header';
    header.id = 'cs-header';

    // Avatar
    var avatarWrap = document.createElement('div');
    avatarWrap.className = 'cs-avatar-wrap';
    if (data.avatar) {
      var img = document.createElement('img');
      img.src = AVATAR_BASE + data.avatar;
      img.alt = data.name;
      img.onerror = function () {
        avatarWrap.innerHTML = '<svg class="cs-avatar-placeholder" viewBox="0 0 48 48" width="48" height="48"><circle cx="24" cy="18" r="10" fill="currentColor"/><ellipse cx="24" cy="44" rx="18" ry="14" fill="currentColor"/></svg>';
      };
      avatarWrap.appendChild(img);
    } else {
      avatarWrap.innerHTML = '<svg class="cs-avatar-placeholder" viewBox="0 0 48 48" width="48" height="48"><circle cx="24" cy="18" r="10" fill="currentColor"/><ellipse cx="24" cy="44" rx="18" ry="14" fill="currentColor"/></svg>';
    }
    header.appendChild(avatarWrap);

    // Info
    var info = document.createElement('div');
    info.className = 'cs-info';
    info.id = 'cs-info';

    var nameEl = document.createElement('div');
    nameEl.className = 'cs-name';
    nameEl.textContent = data.name || 'Unknown';
    if (data.hantu) {
      var hantu = document.createElement('span');
      hantu.className = 'cs-hantu';
      hantu.textContent = '(' + data.hantu + ')';
      nameEl.appendChild(hantu);
    }
    info.appendChild(nameEl);

    var badges = document.createElement('div');
    badges.className = 'cs-badges';
    if (data.archetype) {
      var ab = document.createElement('span');
      ab.className = 'cs-badge cs-badge-archetype';
      ab.textContent = data.archetype;
      badges.appendChild(ab);
    }
    if (arc && arc.status) {
      var sb = document.createElement('span');
      sb.className = 'cs-badge cs-badge-status';
      sb.textContent = arc.status;
      sb.style.color = getStatusColor(arc.status);
      badges.appendChild(sb);
    }
    info.appendChild(badges);

    var meta = document.createElement('div');
    meta.className = 'cs-meta';
    meta.id = 'cs-meta';
    var parts = [];
    if (data.race) parts.push(data.race);
    if (arc && arc.cultivation) parts.push(arc.cultivation);
    meta.textContent = parts.join(' · ');
    info.appendChild(meta);

    var tl = document.createElement('div');
    tl.className = 'cs-tong-luc';
    tl.id = 'cs-tong-luc';
    tl.textContent = '⚔ Tổng Lực: ' + sumStats(arc ? arc.stats : []);
    info.appendChild(tl);

    header.appendChild(info);
    container.appendChild(header);
  }

  // placeholder for remaining sections
  window.CharacterSheet = {
    render: function (data, markdownBody, container) {
      injectStyles();
      container.innerHTML = '';
      var arc = latestArc(data);
      renderHeader(data, arc, container);
      // TODO: arc slider, radar, tabs
    }
  };
})();
```

- [ ] **Step 2: Test header rendering**

Add temporary frontmatter to `Đạo/Nhân_Vật/Diệp_Tĩnh_Sương.md` (just name + archetype + one arc) and open in browser. Verify header renders with placeholder avatar, name, badges, Tổng Lực.

- [ ] **Step 3: Commit**

```bash
git add scripts/character-sheet.js
git commit -m "feat: create character-sheet.js with CSS and header rendering"
```

---

### Task 4: Add arc timeline slider

**Files:**
- Modify: `scripts/character-sheet.js`

- [ ] **Step 1: Add renderArcSlider function**

Add after `renderHeader` function:

```javascript
function renderArcSlider(data, currentArc, container, onArcChange) {
    var slider = document.createElement('div');
    slider.className = 'cs-arc-slider';

    var label = document.createElement('span');
    label.className = 'cs-arc-label';
    label.textContent = 'Arc';
    slider.appendChild(label);

    var track = document.createElement('div');
    track.className = 'cs-arc-track';

    var line = document.createElement('div');
    line.className = 'cs-arc-line';
    track.appendChild(line);

    data.arcs.forEach(function (arcEntry) {
      var btn = document.createElement('button');
      btn.className = 'cs-arc-btn' + (arcEntry.arc === currentArc.arc ? ' cs-active' : '');
      btn.textContent = arcEntry.arc;
      btn.addEventListener('click', function () {
        track.querySelectorAll('.cs-arc-btn').forEach(function (b) { b.classList.remove('cs-active'); });
        btn.classList.add('cs-active');
        onArcChange(arcEntry);
      });
      track.appendChild(btn);
    });

    slider.appendChild(track);
    container.appendChild(slider);

    // Methods display
    var methodsDiv = document.createElement('div');
    methodsDiv.className = 'cs-methods';
    methodsDiv.id = 'cs-methods';
    renderMethods(currentArc, methodsDiv);
    container.appendChild(methodsDiv);
}

function renderMethods(arc, container) {
    container.innerHTML = '';
    var list = document.createElement('div');
    list.className = 'cs-methods-list';
    var methods = (arc && arc.methods) || [];
    if (methods.length === 0) {
      list.innerHTML = '<span class="cs-tab-empty">Không có</span>';
    } else {
      methods.forEach(function (m) {
        var tag = document.createElement('span');
        tag.className = 'cs-method-tag';
        tag.textContent = m;
        list.appendChild(tag);
      });
    }
    container.appendChild(list);
}
```

- [ ] **Step 2: Wire slider into render function**

Update the `render` function to call `renderArcSlider` and store state for arc switching:

```javascript
render: function (data, markdownBody, container) {
    injectStyles();
    container.innerHTML = '';
    var currentArc = latestArc(data);

    renderHeader(data, currentArc, container);

    if (data.arcs && data.arcs.length > 1) {
      renderArcSlider(data, currentArc, container, function (newArc) {
        currentArc = newArc;
        updateForArc(data, currentArc);
      });
    } else {
      // Single arc — show methods only
      var methodsDiv = document.createElement('div');
      methodsDiv.className = 'cs-methods';
      methodsDiv.id = 'cs-methods';
      methodsDiv.style.borderRadius = '0 0 8px 8px';
      methodsDiv.style.borderTop = 'none';
      renderMethods(currentArc, methodsDiv);
      container.appendChild(methodsDiv);
    }
}
```

- [ ] **Step 3: Add updateForArc function**

This function updates all arc-dependent sections when the slider changes:

```javascript
function updateForArc(data, arc) {
    // Update header badges and meta
    var badges = document.querySelector('.cs-badges');
    var statusBadge = badges.querySelector('.cs-badge-status');
    if (statusBadge && arc.status) {
      statusBadge.textContent = arc.status;
      statusBadge.style.color = getStatusColor(arc.status);
    }

    var meta = document.getElementById('cs-meta');
    if (meta) {
      var parts = [];
      if (data.race) parts.push(data.race);
      if (arc.cultivation) parts.push(arc.cultivation);
      meta.textContent = parts.join(' · ');
    }

    var tl = document.getElementById('cs-tong-luc');
    if (tl) tl.textContent = '⚔ Tổng Lực: ' + sumStats(arc.stats);

    // Update methods
    var methodsDiv = document.getElementById('cs-methods');
    if (methodsDiv) renderMethods(arc, methodsDiv);

    // Update radar (will be added in Task 5)
    if (window._csUpdateRadar) window._csUpdateRadar(arc.stats);

    // Update inventory tab (will be added in Task 6)
    if (window._csUpdateInventory) window._csUpdateInventory(arc);

    // Update relationships tab (will be added in Task 6)
    if (window._csUpdateRelationships) window._csUpdateRelationships(arc);
}
```

- [ ] **Step 4: Test arc slider**

Add a second arc entry to the test frontmatter. Click between arcs and verify header info updates.

- [ ] **Step 5: Commit**

```bash
git add scripts/character-sheet.js
git commit -m "feat: add arc timeline slider with methods display"
```

---

### Task 5: Add SVG radar chart

**Files:**
- Modify: `scripts/character-sheet.js`

- [ ] **Step 1: Add renderRadar function**

Add after `renderMethods`:

```javascript
function renderRadar(stats, container) {
    var wrap = document.createElement('div');
    wrap.className = 'cs-radar-wrap';

    var size = 300;
    var cx = size / 2, cy = size / 2;
    var radius = 110;
    var n = 6;

    var svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    svg.setAttribute('class', 'cs-radar-svg');
    svg.setAttribute('viewBox', '0 0 ' + size + ' ' + size);

    // Grid circles (25%, 50%, 75%, 100%)
    [0.25, 0.5, 0.75, 1].forEach(function (pct) {
      var pts = [];
      for (var i = 0; i < n; i++) {
        var angle = (Math.PI * 2 * i / n) - Math.PI / 2;
        pts.push((cx + radius * pct * Math.cos(angle)).toFixed(1) + ',' + (cy + radius * pct * Math.sin(angle)).toFixed(1));
      }
      var poly = document.createElementNS('http://www.w3.org/2000/svg', 'polygon');
      poly.setAttribute('points', pts.join(' '));
      poly.setAttribute('class', 'cs-radar-grid');
      svg.appendChild(poly);
    });

    // Axis lines
    for (var i = 0; i < n; i++) {
      var angle = (Math.PI * 2 * i / n) - Math.PI / 2;
      var line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
      line.setAttribute('x1', cx);
      line.setAttribute('y1', cy);
      line.setAttribute('x2', cx + radius * Math.cos(angle));
      line.setAttribute('y2', cy + radius * Math.sin(angle));
      line.setAttribute('class', 'cs-radar-axis');
      svg.appendChild(line);
    }

    // Data polygon
    var dataPoly = document.createElementNS('http://www.w3.org/2000/svg', 'polygon');
    dataPoly.setAttribute('class', 'cs-radar-poly');
    dataPoly.id = 'cs-radar-poly';
    svg.appendChild(dataPoly);

    // Labels and values
    var labelOffset = 24;
    for (var i = 0; i < n; i++) {
      var angle = (Math.PI * 2 * i / n) - Math.PI / 2;
      var lx = cx + (radius + labelOffset) * Math.cos(angle);
      var ly = cy + (radius + labelOffset) * Math.sin(angle);

      var text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
      text.setAttribute('x', lx);
      text.setAttribute('y', ly);
      text.setAttribute('class', 'cs-radar-label');
      text.setAttribute('text-anchor', 'middle');
      text.setAttribute('dominant-baseline', 'central');
      text.textContent = STAT_LABELS[i];
      svg.appendChild(text);

      // Value text (closer to axis)
      var vx = cx + (radius + 10) * Math.cos(angle);
      var vy = cy + (radius + 10) * Math.sin(angle);
      var valText = document.createElementNS('http://www.w3.org/2000/svg', 'text');
      valText.setAttribute('x', vx);
      valText.setAttribute('y', vy + 12);
      valText.setAttribute('class', 'cs-radar-value');
      valText.setAttribute('text-anchor', 'middle');
      valText.id = 'cs-radar-val-' + i;
      svg.appendChild(valText);
    }

    wrap.appendChild(svg);
    container.appendChild(wrap);

    // Update function
    function updateRadar(newStats) {
      var s = newStats || [];
      var maxVal = 0;
      for (var i = 0; i < n; i++) {
        if ((s[i] || 0) > maxVal) maxVal = s[i] || 0;
      }
      if (maxVal === 0) maxVal = 1;

      var pts = [];
      for (var i = 0; i < n; i++) {
        var val = (s[i] || 0) / maxVal;
        var angle = (Math.PI * 2 * i / n) - Math.PI / 2;
        pts.push((cx + radius * val * Math.cos(angle)).toFixed(1) + ',' + (cy + radius * val * Math.sin(angle)).toFixed(1));
      }
      dataPoly.setAttribute('points', pts.join(' '));

      // Update value texts
      for (var i = 0; i < n; i++) {
        var el = document.getElementById('cs-radar-val-' + i);
        if (el) el.textContent = (s[i] || 0);
      }
    }

    updateRadar(stats);
    window._csUpdateRadar = updateRadar;
}
```

- [ ] **Step 2: Wire radar into render function**

Add `renderRadar(currentArc.stats, container);` call in the `render` function, after the slider.

- [ ] **Step 3: Test radar chart**

Open the test character in browser. Verify 6-axis radar renders with labels and values. Switch arcs and verify polygon shape animates.

- [ ] **Step 4: Commit**

```bash
git add scripts/character-sheet.js
git commit -m "feat: add SVG radar chart with arc-based animation"
```

---

### Task 6: Add tabs system (markdown tabs + inventory + relationships)

**Files:**
- Modify: `scripts/character-sheet.js`

- [ ] **Step 1: Add markdown section parser**

```javascript
function parseMarkdownSections(mdBody) {
    var sections = { ngoaihinh: '', nangluc: '', cottruyen: '' };
    var parts = mdBody.split(/^(##\s+.+)$/m);
    var current = null;

    for (var i = 0; i < parts.length; i++) {
      var part = parts[i].trim();
      if (/^##\s+/.test(part)) {
        var heading = part.toUpperCase();
        if (/NGOẠI HÌNH|TÍNH CÁCH|KHÍ CHẤT/.test(heading)) {
          current = 'ngoaihinh';
        } else if (/NĂNG LỰC|CÔNG PHÁP|SỨC MẠNH|KỸ NĂNG|SỞ TRƯỜNG/.test(heading)) {
          current = 'nangluc';
        } else if (/CỐT TRUYỆN|SỰ KIỆN|LỊCH SỬ/.test(heading)) {
          current = 'cottruyen';
        } else {
          // Append to whichever current section, or skip
          if (current) sections[current] += part + '\n';
          current = null;
        }
      } else if (current && part) {
        sections[current] += part + '\n';
      }
    }

    // Render markdown for each section
    marked.setOptions({ breaks: true, gfm: true });
    for (var key in sections) {
      sections[key] = sections[key].trim() ? marked.parse(sections[key]) : '';
    }
    return sections;
}
```

- [ ] **Step 2: Add renderTabs function**

```javascript
function renderTabs(data, currentArc, mdBody, container) {
    var sections = parseMarkdownSections(mdBody);
    var tabDefs = [
      { id: 'ngoaihinh', label: 'Ngoại Hình', type: 'markdown' },
      { id: 'nangluc', label: 'Năng Lực', type: 'markdown' },
      { id: 'cottruyen', label: 'Cốt Truyện', type: 'markdown' },
      { id: 'trangbi', label: 'Trang Bị', type: 'inventory' },
      { id: 'quanhe', label: 'Quan Hệ', type: 'relationships' },
    ];

    var tabBar = document.createElement('div');
    tabBar.className = 'cs-tabs';

    var contentArea = document.createElement('div');
    contentArea.className = 'cs-tab-content';
    contentArea.id = 'cs-tab-content';

    var activeTab = 'ngoaihinh';

    function showTab(tabId) {
      activeTab = tabId;
      tabBar.querySelectorAll('.cs-tab').forEach(function (t) {
        t.classList.toggle('cs-active', t.getAttribute('data-tab') === tabId);
      });

      contentArea.innerHTML = '';
      var def = tabDefs.find(function (d) { return d.id === tabId; });
      if (!def) return;

      if (def.type === 'markdown') {
        var html = sections[tabId];
        if (html) {
          contentArea.innerHTML = html;
        } else {
          contentArea.innerHTML = '<p class="cs-tab-empty">Chưa có thông tin.</p>';
        }
      } else if (def.type === 'inventory') {
        renderInventoryTab(currentArc, contentArea);
      } else if (def.type === 'relationships') {
        renderRelationshipsTab(currentArc, contentArea);
      }
    }

    tabDefs.forEach(function (def) {
      var tab = document.createElement('button');
      tab.className = 'cs-tab' + (def.id === activeTab ? ' cs-active' : '');
      tab.textContent = def.label;
      tab.setAttribute('data-tab', def.id);
      tab.addEventListener('click', function () { showTab(def.id); });
      tabBar.appendChild(tab);
    });

    container.appendChild(tabBar);
    container.appendChild(contentArea);
    showTab(activeTab);

    // Expose update functions for arc changes
    window._csUpdateInventory = function (arc) {
      currentArc = arc;
      if (activeTab === 'trangbi') showTab('trangbi');
    };
    window._csUpdateRelationships = function (arc) {
      currentArc = arc;
      if (activeTab === 'quanhe') showTab('quanhe');
    };
}
```

- [ ] **Step 3: Add renderInventoryTab function**

```javascript
function renderInventoryTab(arc, container) {
    var items = (arc && arc.inventory) || [];
    if (items.length === 0) {
      container.innerHTML = '<p class="cs-tab-empty">Không có vật phẩm.</p>';
      return;
    }
    var list = document.createElement('ul');
    list.className = 'cs-inv-list';
    items.forEach(function (item) {
      var li = document.createElement('li');
      li.className = 'cs-inv-item';
      var nameSpan = document.createElement('span');
      nameSpan.className = 'cs-inv-name';
      nameSpan.textContent = item.name;
      li.appendChild(nameSpan);
      if (item.type) {
        var typeSpan = document.createElement('span');
        typeSpan.className = 'cs-inv-type';
        typeSpan.textContent = item.type;
        li.appendChild(typeSpan);
      }
      list.appendChild(li);
    });
    container.appendChild(list);
}
```

- [ ] **Step 4: Add renderRelationshipsTab function with feeling bars**

```javascript
function renderRelationshipsTab(arc, container) {
    var rels = (arc && arc.relationships) || [];
    if (rels.length === 0) {
      container.innerHTML = '<p class="cs-tab-empty">Không có quan hệ.</p>';
      return;
    }

    rels.forEach(function (rel) {
      var entry = document.createElement('div');
      entry.className = 'cs-rel-entry';

      var name = document.createElement('div');
      name.className = 'cs-rel-name';
      name.textContent = rel.character || '';
      entry.appendChild(name);

      if (rel.description) {
        var desc = document.createElement('div');
        desc.className = 'cs-rel-desc';
        desc.textContent = rel.description;
        entry.appendChild(desc);
      }

      if (rel.feelings) {
        FEELING_KEYS.forEach(function (key, idx) {
          var val = rel.feelings[key] || 0;
          var row = document.createElement('div');
          row.className = 'cs-feeling-row';

          var label = document.createElement('span');
          label.className = 'cs-feeling-label';
          label.textContent = FEELING_LABELS[idx];
          row.appendChild(label);

          var barWrap = document.createElement('div');
          barWrap.className = 'cs-feeling-bar-wrap';

          var center = document.createElement('div');
          center.className = 'cs-feeling-center';
          barWrap.appendChild(center);

          var fill = document.createElement('div');
          fill.className = 'cs-feeling-fill';
          fill.style.background = FEELING_COLORS[idx];
          if (val >= 0) {
            fill.style.left = '50%';
            fill.style.width = (val / 2) + '%';
            fill.style.opacity = '0.8';
          } else {
            var w = Math.abs(val) / 2;
            fill.style.left = (50 - w) + '%';
            fill.style.width = w + '%';
            fill.style.opacity = '0.4';
          }
          barWrap.appendChild(fill);
          row.appendChild(barWrap);

          var valSpan = document.createElement('span');
          valSpan.className = 'cs-feeling-val';
          valSpan.textContent = (val > 0 ? '+' : '') + val;
          row.appendChild(valSpan);

          entry.appendChild(row);
        });
      }

      container.appendChild(entry);
    });
}
```

- [ ] **Step 5: Wire tabs into render function**

Update `render` to call `renderTabs(data, currentArc, markdownBody, container)` after the radar chart.

- [ ] **Step 6: Test all tabs**

Open the test character and verify all 5 tabs render correctly. Switch arcs and verify inventory/relationships update.

- [ ] **Step 7: Commit**

```bash
git add scripts/character-sheet.js
git commit -m "feat: add tabs with markdown parsing, inventory, and relationship feeling bars"
```

---

### Task 7: Add sample frontmatter to Diệp Tĩnh Sương

**Files:**
- Modify: `Đạo/Nhân_Vật/Diệp_Tĩnh_Sương.md`

- [ ] **Step 1: Add YAML frontmatter to Diệp Tĩnh Sương**

Prepend this frontmatter to the file (before the existing `# HỒ SƠ NHÂN VẬT` heading):

```yaml
---
type: character
name: Diệp Tĩnh Sương
hantu: 葉靜霜
archetype: Kiếm Tu
race: Nhân Tộc
avatar: Diệp_Tĩnh_Sương.png
arcs:
  - arc: 1
    status: Còn Sống
    cultivation: Luyện Khí Tầng 5
    methods: [Hàn Mai Kiếm Quyết]
    inventory:
      - name: Tuyết Ảnh Kiếm
        type: Vũ Khí
    stats: [12, 18, 22, 20, 10, 25]
    relationships:
      - character: Cổ Kiếm Mạc
        description: Sư phụ, người cứu mạng
        feelings:
          yeu: 60
          han: 0
          kinh: 90
          tin: 85
          so: 5
          on: 95
  - arc: 5
    status: Còn Sống
    cultivation: Trúc Cơ Sơ Kỳ
    methods: [Hàn Mai Kiếm Quyết, Lạc Tuyết Vô Ngân]
    inventory:
      - name: Tuyết Ảnh Kiếm
        type: Vũ Khí
      - name: Hàn Ngọc Bội
        type: Pháp Bảo
    stats: [55, 90, 45, 85, 40, 70]
    relationships:
      - character: Lâm Phong
        description: Đồng hành đáng tin cậy
        feelings:
          yeu: 15
          han: 0
          kinh: 30
          tin: 55
          so: 0
          on: 20
      - character: Huyết Sát Minh
        description: Kẻ thù huyết hải thâm thù
        feelings:
          yeu: -80
          han: 95
          kinh: -40
          tin: -90
          so: 20
          on: -100
---
```

- [ ] **Step 2: Full integration test**

Open `reader.html?file=Đạo/Nhân_Vật/Diệp_Tĩnh_Sương.md` in browser. Verify:
1. Header: name, Hán Tự, Kiếm Tu badge, Còn Sống (green) badge, cultivation, Tổng Lực
2. Arc slider: two buttons (1, 5). Clicking switches all data.
3. Radar chart: 6-axis polygon with values. Shape changes on arc switch.
4. Ngoại Hình tab: renders appearance content from markdown
5. Năng Lực tab: renders abilities content
6. Cốt Truyện tab: renders plot history
7. Trang Bị tab: shows inventory items with type badges
8. Quan Hệ tab: shows relationship entries with feeling bars (negative bars dimmed left, positive bright right)
9. Theme switching: change themes, verify colors adapt
10. Mobile: resize to <768px, verify stacked layout

- [ ] **Step 3: Verify non-character pages unaffected**

Open `reader.html?file=Đạo/Nhân_Vật/index.md` — should render as normal markdown.
Open any chapter file — should render as normal chapter mode.

- [ ] **Step 4: Commit**

```bash
git add scripts/character-sheet.js reader.html "Đạo/Nhân_Vật/Diệp_Tĩnh_Sương.md"
git commit -m "feat: complete character sheet system with sample data"
```
