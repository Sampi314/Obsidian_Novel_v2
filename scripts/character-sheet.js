// scripts/character-sheet.js
(function () {
  'use strict';

  // ── Stat labels (fixed order) ──
  var STAT_LABELS = ['Thể Lực', 'Linh Lực', 'Trí Tuệ', 'Tốc Độ', 'Phòng Ngự', 'Tâm Tính'];
  // Stats are stored as arrays: [Thể Lực, Linh Lực, Trí Tuệ, Tốc Độ, Phòng Ngự, Tâm Tính]

  // ── Feeling bar config ──
  var FEELING_KEYS = ['yeu', 'han', 'kinh', 'tin', 'so', 'on'];
  var FEELING_LABELS = ['Yêu', 'Hận', 'Kính', 'Tin', 'Sợ', 'Ơn'];
  var FEELING_COLORS = ['#e87da0', '#e05252', '#d4a574', '#52b788', '#9b72cf', '#5a9ec4'];

  // ── Status badge colors ──
  var STATUS_COLORS = {
    'Sống': '#52b788',
    'Vong': '#e05252', 'Chết': '#e05252',
    'Hồn': '#5a9ec4', 'Ý Chí': '#5a9ec4',
    'Xá': '#9b72cf', 'Sinh': '#9b72cf'
  };

  // ── CSS Injection ──
  function injectStyles() {
    if (document.getElementById('cs-styles')) return;
    var style = document.createElement('style');
    style.id = 'cs-styles';
    style.textContent = [
      /* Entry animation */
      '@keyframes cs-enter { from { opacity: 0; transform: translateY(16px); } to { opacity: 1; transform: translateY(0); } }',
      '@keyframes cs-fade { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: translateY(0); } }',
      '@keyframes cs-radar-draw { from { stroke-dashoffset: 800; opacity: 0; } to { stroke-dashoffset: 0; opacity: 1; } }',
      '@keyframes cs-glow-pulse { 0%, 100% { filter: drop-shadow(0 0 6px rgba(201,169,110,0.25)); } 50% { filter: drop-shadow(0 0 12px rgba(201,169,110,0.4)); } }',

      /* Container */
      '.cs-sheet { max-width: 880px; margin: 0 auto; padding: 24px; font-family: "Lora", "Georgia", serif; color: var(--bone, #d4cbbf); animation: cs-enter 0.6s ease-out; }',

      /* Header zone */
      '.cs-header { display: flex; gap: 28px; align-items: flex-start; margin-bottom: 36px; padding: 28px 32px; background: linear-gradient(135deg, rgba(201,169,110,0.05) 0%, rgba(255,255,255,0.02) 50%, rgba(201,169,110,0.03) 100%); border: 1px solid rgba(201,169,110,0.14); border-radius: 16px; backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px); position: relative; overflow: hidden; }',
      '.cs-header::before { content: ""; position: absolute; top: -1px; left: 0; right: 0; height: 2px; background: linear-gradient(90deg, transparent, var(--gold-dim, #8a7549), transparent); opacity: 0.5; }',
      '.cs-header::after { content: ""; position: absolute; top: 0; right: 0; width: 120px; height: 120px; background: radial-gradient(circle at 100% 0%, rgba(201,169,110,0.06) 0%, transparent 70%); pointer-events: none; }',
      '.cs-avatar-wrap { flex-shrink: 0; width: 160px; height: 160px; border-radius: 12px; overflow: hidden; border: 2px solid var(--gold-dim, #8a7549); box-shadow: 0 0 0 4px rgba(201,169,110,0.06), 0 8px 32px rgba(0,0,0,0.35); background: var(--ink, #1a1714); display: flex; align-items: center; justify-content: center; transition: box-shadow 0.3s ease, border-color 0.3s ease; }',
      '.cs-avatar-wrap:hover { box-shadow: 0 0 0 4px rgba(201,169,110,0.12), 0 8px 32px rgba(0,0,0,0.45); border-color: var(--gold, #c9a96e); }',
      '.cs-avatar-wrap img { width: 100%; height: 100%; object-fit: cover; }',
      '.cs-avatar-placeholder { width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; background: var(--ink, #1a1714); }',
      '.cs-avatar-placeholder svg { width: 72px; height: 72px; opacity: 0.25; }',
      '.cs-info { flex: 1; min-width: 0; }',
      '.cs-name { font-family: "Playfair Display", serif; font-size: 2.3rem; font-weight: 700; color: var(--gold, #c9a96e); line-height: 1.15; margin-bottom: 0; text-shadow: 0 0 40px rgba(201,169,110,0.12); }',
      '.cs-hantu { font-size: 1.3rem; color: var(--ash, #7a7067); font-weight: 400; letter-spacing: 3px; margin-top: 4px; margin-bottom: 4px; }',
      '.cs-badges { display: flex; gap: 10px; flex-wrap: wrap; margin: 12px 0; }',
      '.cs-badge { display: inline-block; padding: 3px 14px; border-radius: 6px; font-size: 0.76rem; font-weight: 600; letter-spacing: 0.8px; text-transform: uppercase; }',
      '.cs-badge-archetype { border: 1px solid var(--gold, #c9a96e); color: var(--gold, #c9a96e); background: rgba(201,169,110,0.08); }',
      '.cs-badge-status { color: #fff; box-shadow: 0 2px 8px rgba(0,0,0,0.25); }',
      '.cs-meta { font-size: 0.9rem; color: var(--ash, #7a7067); margin: 6px 0 2px; }',
      '.cs-tong-luc { font-size: 1rem; color: var(--gold, #c9a96e); font-weight: 600; margin-top: 10px; padding-top: 10px; border-top: 1px solid rgba(201,169,110,0.08); letter-spacing: 0.5px; }',

      /* Arc timeline */
      '.cs-timeline { margin-bottom: 32px; padding: 22px 28px; background: rgba(255,255,255,0.02); border: 1px solid rgba(201,169,110,0.1); border-radius: 14px; }',
      '.cs-timeline-label { font-size: 0.7rem; color: var(--ash, #7a7067); text-transform: uppercase; letter-spacing: 2.5px; margin-bottom: 14px; font-weight: 600; }',
      '.cs-timeline-track { position: relative; display: flex; align-items: center; justify-content: space-between; padding: 0 12px; min-height: 42px; }',
      '.cs-timeline-line { position: absolute; top: 50%; left: 24px; right: 24px; height: 2px; background: linear-gradient(90deg, var(--gold-dim, #8a7549), var(--gold, #c9a96e), var(--gold-dim, #8a7549)); transform: translateY(-50%); z-index: 0; opacity: 0.6; }',
      '.cs-arc-btn { position: relative; z-index: 1; width: 38px; height: 38px; border-radius: 50%; border: 2px solid var(--gold-dim, #8a7549); background: var(--ink, #1a1714); color: var(--bone, #d4cbbf); font-size: 0.82rem; font-weight: 700; cursor: pointer; display: flex; align-items: center; justify-content: center; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); font-family: inherit; }',
      '.cs-arc-btn:hover { border-color: var(--gold, #c9a96e); background: rgba(201,169,110,0.12); transform: scale(1.1); }',
      '.cs-arc-btn.cs-active { background: var(--gold, #c9a96e); color: var(--void, #0a0908); border-color: var(--gold, #c9a96e); box-shadow: 0 0 16px rgba(201,169,110,0.3); transform: scale(1.05); }',
      '.cs-methods { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 14px; }',
      '.cs-method-tag { display: inline-block; padding: 4px 14px; font-size: 0.75rem; border-radius: 20px; background: rgba(201,169,110,0.07); color: var(--gold-bright, #e4c98a); border: 1px solid rgba(201,169,110,0.14); transition: all 0.2s ease; letter-spacing: 0.3px; }',
      '.cs-method-tag:hover { background: rgba(201,169,110,0.14); border-color: rgba(201,169,110,0.25); }',

      /* Radar chart */
      '.cs-radar-wrap { display: flex; justify-content: center; margin-bottom: 32px; }',
      '.cs-radar-svg { width: 320px; height: 320px; filter: drop-shadow(0 0 20px rgba(201,169,110,0.04)); }',
      '.cs-radar-grid { fill: none; stroke: var(--gold-dim, #8a7549); stroke-width: 0.5; opacity: 0.35; }',
      '.cs-radar-axis { stroke: var(--gold-dim, #8a7549); stroke-width: 0.5; opacity: 0.25; }',
      '.cs-radar-poly { fill: var(--gold, #c9a96e); fill-opacity: 0.15; stroke: var(--gold, #c9a96e); stroke-width: 2; stroke-dasharray: 800; animation: cs-radar-draw 1s ease-out forwards; filter: drop-shadow(0 0 6px rgba(201,169,110,0.25)); transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1); }',
      '.cs-radar-dot { fill: var(--gold-bright, #e4c98a); stroke: var(--void, #0a0908); stroke-width: 2; transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1); }',
      '.cs-radar-label { fill: var(--bone, #d4cbbf); font-size: 11px; font-family: "Lora", serif; text-anchor: middle; }',
      '.cs-radar-value { fill: var(--gold-bright, #e4c98a); font-size: 10.5px; font-family: "Lora", serif; text-anchor: middle; font-weight: 700; }',

      /* Tabs */
      '.cs-tabs { margin-bottom: 8px; }',
      '.cs-tab-bar { display: flex; gap: 2px; border-bottom: 1px solid rgba(201,169,110,0.1); overflow-x: auto; -webkit-overflow-scrolling: touch; scrollbar-width: none; }',
      '.cs-tab-bar::-webkit-scrollbar { display: none; }',
      '.cs-tab-btn { background: none; border: none; border-bottom: 2px solid transparent; color: var(--ash, #7a7067); font-family: "Playfair Display", serif; font-size: 0.9rem; padding: 12px 20px; cursor: pointer; white-space: nowrap; transition: all 0.3s ease; letter-spacing: 0.3px; }',
      '.cs-tab-btn:hover { color: var(--bone, #d4cbbf); background: rgba(201,169,110,0.04); }',
      '.cs-tab-btn.cs-active { color: var(--gold, #c9a96e); border-bottom-color: var(--gold, #c9a96e); background: rgba(201,169,110,0.06); }',
      '.cs-tab-content { padding: 24px 8px; min-height: 140px; animation: cs-fade 0.35s ease; }',
      '.cs-tab-content .cs-empty { color: var(--ash, #7a7067); font-style: italic; }',

      /* Markdown rendered content in tabs */
      '.cs-tab-content h1, .cs-tab-content h2, .cs-tab-content h3 { color: var(--gold, #c9a96e); font-family: "Playfair Display", serif; margin: 20px 0 10px; }',
      '.cs-tab-content h2 { font-size: 1.35rem; border-bottom: 1px solid rgba(201,169,110,0.08); padding-bottom: 8px; }',
      '.cs-tab-content h3 { font-size: 1.1rem; }',
      '.cs-tab-content p { margin: 10px 0; line-height: 1.85; }',
      '.cs-tab-content ul, .cs-tab-content ol { margin: 8px 0 8px 20px; }',
      '.cs-tab-content li { margin: 4px 0; line-height: 1.7; }',
      '.cs-tab-content strong { color: var(--gold-bright, #e4c98a); }',
      '.cs-tab-content blockquote { border-left: 3px solid var(--gold-dim, #8a7549); padding: 10px 18px; margin: 14px 0; color: var(--ash, #7a7067); font-style: italic; background: rgba(201,169,110,0.03); border-radius: 0 8px 8px 0; }',

      /* Inventory tab */
      '.cs-inv-list { list-style: none; padding: 0; margin: 0; }',
      '.cs-inv-item { display: flex; align-items: center; gap: 12px; padding: 12px 16px; border-bottom: 1px solid rgba(201,169,110,0.06); transition: background 0.2s ease; border-radius: 6px; }',
      '.cs-inv-item:hover { background: rgba(201,169,110,0.04); }',
      '.cs-inv-item:last-child { border-bottom: none; }',
      '.cs-inv-name { flex: 1; color: var(--bone, #d4cbbf); font-weight: 500; }',
      '.cs-inv-type { display: inline-block; padding: 2px 10px; font-size: 0.72rem; border-radius: 12px; background: rgba(201,169,110,0.1); color: var(--gold, #c9a96e); border: 1px solid rgba(201,169,110,0.15); }',

      /* Relationships tab */
      '.cs-rel-list { display: flex; flex-direction: column; gap: 20px; }',
      '.cs-rel-card { padding: 20px; background: linear-gradient(135deg, rgba(255,255,255,0.03) 0%, rgba(255,255,255,0.01) 100%); border: 1px solid rgba(201,169,110,0.1); border-radius: 12px; transition: all 0.3s ease; }',
      '.cs-rel-card:hover { border-color: rgba(201,169,110,0.2); box-shadow: 0 4px 20px rgba(0,0,0,0.15); }',
      '.cs-rel-name { font-family: "Playfair Display", serif; font-weight: 700; color: var(--gold, #c9a96e); font-size: 1.1rem; margin-bottom: 4px; }',
      '.cs-rel-desc { color: var(--ash, #7a7067); font-size: 0.85rem; margin-bottom: 14px; font-style: italic; }',
      '.cs-feel-row { display: flex; align-items: center; gap: 10px; margin: 7px 0; }',
      '.cs-feel-label { width: 36px; font-size: 0.75rem; color: var(--ash, #7a7067); text-align: right; flex-shrink: 0; }',
      '.cs-feel-track { flex: 1; height: 12px; background: rgba(255,255,255,0.04); border-radius: 6px; position: relative; overflow: hidden; }',
      '.cs-feel-center { position: absolute; left: 50%; top: 0; bottom: 0; width: 1px; background: rgba(255,255,255,0.1); }',
      '.cs-feel-fill { position: absolute; top: 1px; bottom: 1px; border-radius: 5px; transition: width 0.5s cubic-bezier(0.4, 0, 0.2, 1); }',
      '.cs-feel-val { width: 42px; font-size: 0.75rem; text-align: right; flex-shrink: 0; font-weight: 700; }',

      /* Responsive */
      '@media (max-width: 768px) {',
      '  .cs-header { flex-direction: column; align-items: center; text-align: center; padding: 20px; gap: 20px; }',
      '  .cs-avatar-wrap { width: 140px; height: 140px; }',
      '  .cs-badges { justify-content: center; }',
      '  .cs-radar-svg { width: 280px; height: 280px; }',
      '  .cs-tab-bar { overflow-x: auto; }',
      '  .cs-sheet { padding: 12px; }',
      '  .cs-name { font-size: 1.8rem; }',
      '  .cs-hantu { font-size: 1.1rem; }',
      '}'
    ].join('\n');
    document.head.appendChild(style);
  }

  // ── Helpers ──

  function el(tag, cls, text) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text !== undefined) e.textContent = text;
    return e;
  }

  function svgEl(tag, attrs) {
    var e = document.createElementNS('http://www.w3.org/2000/svg', tag);
    if (attrs) {
      Object.keys(attrs).forEach(function (k) { e.setAttribute(k, attrs[k]); });
    }
    return e;
  }

  /** Get stat values array from an arc object */
  function getStats(arc) {
    if (!arc || !arc.stats) return [0, 0, 0, 0, 0, 0];
    if (Array.isArray(arc.stats)) return arc.stats.map(function (v) { return Number(v) || 0; });
    return [0, 0, 0, 0, 0, 0];
  }

  /** Compute Tổng Lực from stats array */
  function tongLuc(stats) {
    return stats.reduce(function (a, b) { return a + b; }, 0);
  }

  /** Get status color by keyword substring match */
  function statusColor(status) {
    if (!status) return '#7a7067';
    var s = status.toLowerCase();
    var keys = Object.keys(STATUS_COLORS);
    for (var i = 0; i < keys.length; i++) {
      if (s.indexOf(keys[i].toLowerCase()) !== -1) return STATUS_COLORS[keys[i]];
    }
    return '#7a7067';
  }

  /** Parse markdown body into sections keyed by heading text */
  function parseMdSections(md) {
    var sections = [];
    var lines = md.split('\n');
    var currentHeading = null;
    var currentContent = [];

    for (var i = 0; i < lines.length; i++) {
      var headingMatch = lines[i].match(/^##\s+(.+)$/);
      if (headingMatch) {
        if (currentHeading !== null) {
          sections.push({ heading: currentHeading, content: currentContent.join('\n') });
        }
        currentHeading = headingMatch[1];
        currentContent = [];
      } else if (currentHeading !== null) {
        currentContent.push(lines[i]);
      }
    }
    if (currentHeading !== null) {
      sections.push({ heading: currentHeading, content: currentContent.join('\n') });
    }
    return sections;
  }

  /** Find sections matching any of the given keywords (case-insensitive) */
  function findSections(sections, keywords) {
    var result = [];
    sections.forEach(function (sec) {
      var upper = sec.heading.toUpperCase();
      for (var i = 0; i < keywords.length; i++) {
        if (upper.indexOf(keywords[i]) !== -1) {
          result.push(sec);
          break;
        }
      }
    });
    return result;
  }

  /** Render matched sections as HTML via marked */
  function renderSections(matchedSections) {
    if (!matchedSections.length) return '<p class="cs-empty">Chưa có thông tin.</p>';
    var combined = matchedSections.map(function (s) {
      return '## ' + s.heading + '\n' + s.content;
    }).join('\n\n');
    return marked.parse(combined);
  }

  // ── SVG Silhouette Placeholder ──
  function createAvatarPlaceholder() {
    var wrap = el('div', 'cs-avatar-placeholder');
    var svg = svgEl('svg', { viewBox: '0 0 64 64', fill: 'none' });
    var circle = svgEl('circle', { cx: '32', cy: '22', r: '12', fill: 'var(--ash, #7a7067)' });
    var body = svgEl('ellipse', { cx: '32', cy: '54', rx: '20', ry: '14', fill: 'var(--ash, #7a7067)' });
    svg.appendChild(circle);
    svg.appendChild(body);
    wrap.appendChild(svg);
    return wrap;
  }

  // ── Radar Chart ──
  function buildRadarChart(stats) {
    var size = 300;
    var cx = size / 2;
    var cy = size / 2;
    var maxR = 110;

    var svg = svgEl('svg', {
      viewBox: '0 0 ' + size + ' ' + size,
      class: 'cs-radar-svg'
    });

    var maxVal = Math.max.apply(null, stats);
    if (maxVal === 0) maxVal = 1; // avoid division by zero

    // Compute vertex positions for a hexagon (start from top)
    function vertex(i, r) {
      var angle = (Math.PI * 2 * i / 6) - Math.PI / 2;
      return {
        x: cx + r * Math.cos(angle),
        y: cy + r * Math.sin(angle)
      };
    }

    function hexPoints(r) {
      var pts = [];
      for (var i = 0; i < 6; i++) {
        var v = vertex(i, r);
        pts.push(v.x.toFixed(2) + ',' + v.y.toFixed(2));
      }
      return pts.join(' ');
    }

    // Grid: 4 concentric hexagons
    var levels = [0.25, 0.5, 0.75, 1.0];
    levels.forEach(function (frac) {
      var poly = svgEl('polygon', {
        points: hexPoints(maxR * frac),
        class: 'cs-radar-grid'
      });
      svg.appendChild(poly);
    });

    // Axis lines
    for (var i = 0; i < 6; i++) {
      var v = vertex(i, maxR);
      var line = svgEl('line', {
        x1: cx, y1: cy,
        x2: v.x.toFixed(2), y2: v.y.toFixed(2),
        class: 'cs-radar-axis'
      });
      svg.appendChild(line);
    }

    // Data polygon
    var dataPts = [];
    for (var j = 0; j < 6; j++) {
      var norm = stats[j] / maxVal;
      var dv = vertex(j, maxR * norm);
      dataPts.push(dv.x.toFixed(2) + ',' + dv.y.toFixed(2));
    }
    var dataPoly = svgEl('polygon', {
      points: dataPts.join(' '),
      class: 'cs-radar-poly'
    });
    svg.appendChild(dataPoly);

    // Data dots at vertices
    var dots = [];
    for (var dd = 0; dd < 6; dd++) {
      var normD = stats[dd] / maxVal;
      var dvD = vertex(dd, maxR * normD);
      var dot = svgEl('circle', {
        cx: dvD.x.toFixed(2), cy: dvD.y.toFixed(2), r: '4',
        class: 'cs-radar-dot'
      });
      svg.appendChild(dot);
      dots.push(dot);
    }

    // Labels & values
    var labelOffset = 26;
    for (var k = 0; k < 6; k++) {
      var lv = vertex(k, maxR + labelOffset);
      var lbl = svgEl('text', {
        x: lv.x.toFixed(2), y: lv.y.toFixed(2),
        class: 'cs-radar-label'
      });
      lbl.textContent = STAT_LABELS[k];
      svg.appendChild(lbl);

      var vv = vertex(k, maxR + labelOffset + 14);
      var val = svgEl('text', {
        x: vv.x.toFixed(2), y: vv.y.toFixed(2),
        class: 'cs-radar-value'
      });
      val.textContent = String(stats[k]);
      svg.appendChild(val);
    }

    return { svg: svg, polygon: dataPoly, dots: dots, valueTexts: svg.querySelectorAll('.cs-radar-value') };
  }

  function updateRadarChart(radarState, stats) {
    var maxVal = Math.max.apply(null, stats);
    if (maxVal === 0) maxVal = 1;
    var cx = 150, cy = 150, maxR = 110;

    function vertex(i, r) {
      var angle = (Math.PI * 2 * i / 6) - Math.PI / 2;
      return {
        x: cx + r * Math.cos(angle),
        y: cy + r * Math.sin(angle)
      };
    }

    var pts = [];
    for (var j = 0; j < 6; j++) {
      var norm = stats[j] / maxVal;
      var v = vertex(j, maxR * norm);
      pts.push(v.x.toFixed(2) + ',' + v.y.toFixed(2));
    }
    radarState.polygon.setAttribute('points', pts.join(' '));

    // Update dots
    if (radarState.dots) {
      for (var d = 0; d < 6; d++) {
        var normD = stats[d] / maxVal;
        var vd = vertex(d, maxR * normD);
        radarState.dots[d].setAttribute('cx', vd.x.toFixed(2));
        radarState.dots[d].setAttribute('cy', vd.y.toFixed(2));
      }
    }

    var valueEls = radarState.svg.querySelectorAll('.cs-radar-value');
    for (var k = 0; k < 6; k++) {
      if (valueEls[k]) valueEls[k].textContent = String(stats[k]);
    }
  }

  // ── Feeling Bars ──
  function buildFeelingBar(idx, value) {
    var row = el('div', 'cs-feel-row');

    var label = el('span', 'cs-feel-label', FEELING_LABELS[idx]);
    row.appendChild(label);

    var track = el('div', 'cs-feel-track');
    var center = el('div', 'cs-feel-center');
    track.appendChild(center);

    var fill = el('div', 'cs-feel-fill');
    var color = FEELING_COLORS[idx];
    var width = Math.abs(value) / 2; // percentage of bar width
    if (value >= 0) {
      fill.style.left = '50%';
      fill.style.width = width + '%';
      fill.style.background = color;
      fill.style.opacity = '0.8';
    } else {
      fill.style.right = '50%';
      fill.style.width = width + '%';
      fill.style.background = color;
      fill.style.opacity = '0.4';
    }
    track.appendChild(fill);
    row.appendChild(track);

    var valText = el('span', 'cs-feel-val');
    valText.textContent = (value >= 0 ? '+' : '') + value;
    valText.style.color = color;
    row.appendChild(valText);

    return row;
  }

  // ── Tab Content Renderers ──

  function renderInventoryTab(arc) {
    var wrap = el('div');
    if (!arc || !arc.inventory || !arc.inventory.length) {
      wrap.innerHTML = '<p class="cs-empty">Không có vật phẩm.</p>';
      return wrap;
    }
    var list = el('ul', 'cs-inv-list');
    arc.inventory.forEach(function (item) {
      var li = el('li', 'cs-inv-item');
      li.appendChild(el('span', 'cs-inv-name', item.name || item));
      if (item.type) {
        li.appendChild(el('span', 'cs-inv-type', item.type));
      }
      list.appendChild(li);
    });
    wrap.appendChild(list);
    return wrap;
  }

  function renderRelationshipsTab(arc) {
    var wrap = el('div');
    if (!arc || !arc.relationships || !arc.relationships.length) {
      wrap.innerHTML = '<p class="cs-empty">Chưa có thông tin quan hệ.</p>';
      return wrap;
    }
    var list = el('div', 'cs-rel-list');
    arc.relationships.forEach(function (rel) {
      var card = el('div', 'cs-rel-card');
      card.appendChild(el('div', 'cs-rel-name', rel.character || '???'));
      if (rel.description) {
        card.appendChild(el('div', 'cs-rel-desc', rel.description));
      }
      // Feeling bars
      FEELING_KEYS.forEach(function (key, idx) {
        var val = (rel.feelings && rel.feelings[key] !== undefined && rel.feelings[key] !== null) ? Number(rel.feelings[key]) : 0;
        card.appendChild(buildFeelingBar(idx, val));
      });
      list.appendChild(card);
    });
    wrap.appendChild(list);
    return wrap;
  }

  // ══════════════════════════════════════════════
  //  Main render function
  // ══════════════════════════════════════════════
  function render(data, md, container) {
    injectStyles();

    // ── Resolve arcs ──
    var arcs = data.arcs || [];
    var arcKeys = [];
    var arcMap = {};
    arcs.forEach(function (a) {
      var key = Number(a.arc);
      if (!isNaN(key)) {
        arcKeys.push(key);
        arcMap[key] = a;
      }
    });
    arcKeys.sort(function (a, b) { return a - b; });
    var currentArcKey = arcKeys.length ? arcKeys[arcKeys.length - 1] : null;

    function currentArc() {
      return currentArcKey !== null ? arcMap[currentArcKey] : null;
    }

    // ── Parse markdown sections ──
    var mdSections = parseMdSections(md);

    // ── Sheet container ──
    var sheet = el('div', 'cs-sheet');

    // ════════════════════════════════
    //  1. HEADER ZONE
    // ════════════════════════════════
    var header = el('div', 'cs-header');

    // Avatar
    var avatarWrap = el('div', 'cs-avatar-wrap');
    if (data.avatar) {
      var img = document.createElement('img');
      img.src = 'Đạo/Ảnh/Nhân_Vật/' + data.avatar;
      img.alt = data.name || 'Avatar';
      img.onerror = function () {
        avatarWrap.innerHTML = '';
        avatarWrap.appendChild(createAvatarPlaceholder());
      };
      avatarWrap.appendChild(img);
    } else {
      avatarWrap.appendChild(createAvatarPlaceholder());
    }
    header.appendChild(avatarWrap);

    // Info column
    var info = el('div', 'cs-info');

    // Name + hantu (displayed separately for dramatic effect)
    var nameEl = el('h1', 'cs-name', data.name || 'Không tên');
    info.appendChild(nameEl);
    if (data.hantu) {
      var hantuEl = el('div', 'cs-hantu', data.hantu);
      info.appendChild(hantuEl);
    }

    // Badges
    var badges = el('div', 'cs-badges');
    if (data.archetype) {
      badges.appendChild(el('span', 'cs-badge cs-badge-archetype', data.archetype));
    }
    var statusBadge = el('span', 'cs-badge cs-badge-status');
    function updateStatusBadge(arc) {
      var st = (arc && arc.status) ? arc.status : (data.status || 'Sống');
      statusBadge.textContent = st;
      statusBadge.style.background = statusColor(st);
    }
    updateStatusBadge(currentArc());
    badges.appendChild(statusBadge);
    info.appendChild(badges);

    // Meta: race · cultivation
    var metaEl = el('div', 'cs-meta');
    function updateMeta(arc) {
      var race = data.race || '';
      var cult = (arc && arc.cultivation) ? arc.cultivation : (data.cultivation || '');
      metaEl.textContent = race + (race && cult ? ' · ' : '') + cult;
    }
    updateMeta(currentArc());
    info.appendChild(metaEl);

    // Tổng Lực
    var tongLucEl = el('div', 'cs-tong-luc');
    function updateTongLuc(arc) {
      var stats = getStats(arc);
      tongLucEl.textContent = '\u2694 Tổng Lực: ' + tongLuc(stats);
    }
    updateTongLuc(currentArc());
    info.appendChild(tongLucEl);

    header.appendChild(info);
    sheet.appendChild(header);

    // ════════════════════════════════
    //  2. ARC TIMELINE
    // ════════════════════════════════
    var timelineWrap = null;
    var methodsWrap = null;
    var arcButtons = [];

    if (arcKeys.length > 1) {
      timelineWrap = el('div', 'cs-timeline');
      timelineWrap.appendChild(el('div', 'cs-timeline-label', 'Arc'));

      var track = el('div', 'cs-timeline-track');
      var line = el('div', 'cs-timeline-line');
      track.appendChild(line);

      arcKeys.forEach(function (key) {
        var btn = el('button', 'cs-arc-btn', String(key));
        if (key === currentArcKey) btn.classList.add('cs-active');
        btn.setAttribute('data-arc', key);
        btn.addEventListener('click', function () { switchArc(key); });
        track.appendChild(btn);
        arcButtons.push(btn);
      });
      timelineWrap.appendChild(track);

      // Methods
      methodsWrap = el('div', 'cs-methods');
      function updateMethods(arc) {
        methodsWrap.innerHTML = '';
        if (arc && arc.methods && arc.methods.length) {
          arc.methods.forEach(function (m) {
            methodsWrap.appendChild(el('span', 'cs-method-tag', m));
          });
        }
      }
      updateMethods(currentArc());
      timelineWrap.appendChild(methodsWrap);

      sheet.appendChild(timelineWrap);
    }

    // ════════════════════════════════
    //  3. RADAR CHART
    // ════════════════════════════════
    var currentStats = getStats(currentArc());
    var radarWrap = el('div', 'cs-radar-wrap');
    var radarState = buildRadarChart(currentStats);
    radarWrap.appendChild(radarState.svg);
    sheet.appendChild(radarWrap);

    // ════════════════════════════════
    //  4. TABS
    // ════════════════════════════════
    var TAB_DEFS = [
      { id: 'ngoai-hinh', label: 'Ngoại Hình', keywords: ['NGOẠI HÌNH', 'TÍNH CÁCH', 'KHÍ CHẤT'] },
      { id: 'nang-luc', label: 'Năng Lực', keywords: ['NĂNG LỰC', 'CÔNG PHÁP', 'SỨC MẠNH', 'KỸ NĂNG', 'SỞ TRƯỜNG'] },
      { id: 'cot-truyen', label: 'Cốt Truyện', keywords: ['CỐT TRUYỆN', 'SỰ KIỆN', 'LỊCH SỬ'] },
      { id: 'trang-bi', label: 'Trang Bị', arcDependent: true },
      { id: 'quan-he', label: 'Quan Hệ', arcDependent: true }
    ];

    var tabsContainer = el('div', 'cs-tabs');
    var tabBar = el('div', 'cs-tab-bar');
    var tabContent = el('div', 'cs-tab-content');
    var activeTabId = TAB_DEFS[0].id;
    var tabButtons = [];

    TAB_DEFS.forEach(function (def) {
      var btn = el('button', 'cs-tab-btn', def.label);
      if (def.id === activeTabId) btn.classList.add('cs-active');
      btn.setAttribute('data-tab', def.id);
      btn.addEventListener('click', function () {
        activateTab(def.id);
      });
      tabBar.appendChild(btn);
      tabButtons.push(btn);
    });
    tabsContainer.appendChild(tabBar);
    tabsContainer.appendChild(tabContent);
    sheet.appendChild(tabsContainer);

    function activateTab(tabId) {
      activeTabId = tabId;
      tabButtons.forEach(function (b) {
        b.classList.toggle('cs-active', b.getAttribute('data-tab') === tabId);
      });
      renderTabContent(tabId);
    }

    function renderTabContent(tabId) {
      tabContent.innerHTML = '';
      var inner;

      if (tabId === 'trang-bi') {
        inner = renderInventoryTab(currentArc());
      } else if (tabId === 'quan-he') {
        inner = renderRelationshipsTab(currentArc());
      } else {
        // Markdown-based tab
        var def = TAB_DEFS.filter(function (d) { return d.id === tabId; })[0];
        if (def && def.keywords) {
          var matched = findSections(mdSections, def.keywords);
          inner = el('div');
          inner.innerHTML = renderSections(matched);
        } else {
          inner = el('div');
          inner.innerHTML = '<p class="cs-empty">Chưa có thông tin.</p>';
        }
      }

      tabContent.appendChild(inner);
    }

    // Render default tab
    renderTabContent(activeTabId);

    // ════════════════════════════════
    //  5. ARC SWITCHING
    // ════════════════════════════════
    function switchArc(key) {
      currentArcKey = key;
      var arc = currentArc();

      // Update arc buttons
      arcButtons.forEach(function (btn) {
        btn.classList.toggle('cs-active', Number(btn.getAttribute('data-arc')) === key);
      });

      // Update header
      updateStatusBadge(arc);
      updateMeta(arc);
      updateTongLuc(arc);

      // Update methods
      if (methodsWrap) {
        methodsWrap.innerHTML = '';
        if (arc && arc.methods && arc.methods.length) {
          arc.methods.forEach(function (m) {
            methodsWrap.appendChild(el('span', 'cs-method-tag', m));
          });
        }
      }

      // Update radar chart
      var newStats = getStats(arc);
      updateRadarChart(radarState, newStats);

      // Re-render arc-dependent tab if active
      if (activeTabId === 'trang-bi' || activeTabId === 'quan-he') {
        renderTabContent(activeTabId);
      }
    }

    // ── Mount ──
    container.appendChild(sheet);
  }

  // ── Public API ──
  window.CharacterSheet = {
    render: render
  };
})();
