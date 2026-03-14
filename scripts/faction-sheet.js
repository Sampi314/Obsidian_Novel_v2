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
      '.fs-sheet { max-width: 900px; margin: 0 auto; padding: 20px; font-family: "Lora", "Georgia", serif; color: var(--bone, #d4cbbf); }',
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
      '.fs-timeline { margin-bottom: 28px; padding: 18px 24px; background: rgba(255,255,255,0.02); border: 1px solid rgba(201,169,110,0.08); border-radius: 10px; }',
      '.fs-timeline-label { font-size: 0.8rem; color: var(--ash, #7a7067); text-transform: uppercase; letter-spacing: 1px; margin-bottom: 12px; }',
      '.fs-timeline-track { position: relative; display: flex; align-items: center; justify-content: space-between; padding: 0 12px; min-height: 36px; }',
      '.fs-timeline-line { position: absolute; top: 50%; left: 24px; right: 24px; height: 2px; background: var(--gold-dim, #8a7549); transform: translateY(-50%); z-index: 0; }',
      '.fs-arc-btn { position: relative; z-index: 1; width: 32px; height: 32px; border-radius: 50%; border: 2px solid var(--gold-dim, #8a7549); background: var(--ink, #1a1714); color: var(--bone, #d4cbbf); font-size: 0.78rem; font-weight: 700; cursor: pointer; display: flex; align-items: center; justify-content: center; transition: all 0.25s ease; font-family: inherit; }',
      '.fs-arc-btn:hover { border-color: var(--gold, #c9a96e); background: rgba(201,169,110,0.15); }',
      '.fs-arc-btn.fs-active { background: var(--gold, #c9a96e); color: var(--void, #0a0908); border-color: var(--gold, #c9a96e); }',
      '.fs-territory { display: flex; flex-wrap: wrap; gap: 6px; margin-top: 12px; }',
      '.fs-territory-tag { display: inline-block; padding: 2px 10px; font-size: 0.75rem; border-radius: 4px; background: rgba(201,169,110,0.1); color: var(--gold-bright, #e4c98a); border: 1px solid rgba(201,169,110,0.15); }',
      '.fs-radar-wrap { display: flex; justify-content: center; margin-bottom: 28px; }',
      '.fs-radar-svg { width: 320px; height: 320px; }',
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
      '.fs-division { margin-bottom: 24px; padding: 20px; background: rgba(255,255,255,0.02); border: 1px solid rgba(201,169,110,0.08); border-radius: 10px; }',
      '.fs-division-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; }',
      '.fs-division-name { font-family: "Playfair Display", serif; font-size: 1.1rem; color: var(--gold, #c9a96e); }',
      '.fs-division-role { font-size: 0.82rem; color: var(--ash, #7a7067); }',
      '.fs-hc-row { display: flex; align-items: center; margin-bottom: 6px; }',
      '.fs-hc-label { width: 120px; font-size: 0.78rem; color: var(--ash, #7a7067); text-transform: capitalize; }',
      '.fs-hc-bar-bg { flex: 1; height: 14px; background: var(--ink, #1a1714); border-radius: 3px; overflow: hidden; position: relative; border: 1px solid rgba(201,169,110,0.06); }',
      '.fs-hc-bar { height: 100%; border-radius: 3px; transition: width 0.6s ease; }',
      '.fs-hc-count { width: 50px; text-align: right; font-size: 0.78rem; color: var(--bone, #d4cbbf); }',
      '.fs-members { margin-top: 12px; border-top: 1px solid rgba(201,169,110,0.06); padding-top: 12px; }',
      '.fs-member { display: flex; align-items: center; gap: 12px; padding: 6px 0; border-bottom: 1px solid rgba(201,169,110,0.04); }',
      '.fs-member:last-child { border-bottom: none; }',
      '.fs-member-name { font-size: 0.88rem; color: var(--bone, #d4cbbf); min-width: 140px; }',
      '.fs-member-name.fs-placeholder { color: var(--ash, #7a7067); font-style: italic; }',
      '.fs-member-pos { font-size: 0.78rem; color: var(--gold-dim, #8a7549); min-width: 120px; }',
      '.fs-member-cult { font-size: 0.78rem; color: var(--ash, #7a7067); }',
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
      '.fs-assets { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 8px; }',
      '.fs-asset { display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; font-size: 0.78rem; border-radius: 4px; background: rgba(201,169,110,0.06); border: 1px solid rgba(201,169,110,0.1); color: var(--bone, #d4cbbf); }',
      '.fs-asset-type { color: var(--gold-dim, #8a7549); font-size: 0.72rem; }',
      '@media (max-width: 640px) { .fs-header { flex-direction: column; align-items: center; text-align: center; } .fs-emblem-wrap { width: 80px; height: 80px; } .fs-name { font-size: 1.5rem; } .fs-radar-svg { width: 260px; height: 260px; } .fs-tab-btn { padding: 8px 12px; font-size: 0.75rem; } .fs-hc-label { width: 80px; } .fs-diplo-label { width: 70px; } }'
    ].join('\n');
    document.head.appendChild(style);
  }

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
    for (var i = 0; i < n; i++) {
      var p = point(i, r);
      var line = document.createElementNS(ns, 'line');
      line.setAttribute('x1', cx); line.setAttribute('y1', cy);
      line.setAttribute('x2', p[0]); line.setAttribute('y2', p[1]);
      line.setAttribute('stroke', 'rgba(201,169,110,0.08)');
      line.setAttribute('stroke-width', '1');
      svg.appendChild(line);
    }
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

  function findSections(sections, keywords) {
    return sections.filter(function (s) {
      var h = s.heading.toLowerCase();
      return keywords.some(function (kw) { return h.indexOf(kw.toLowerCase()) !== -1; });
    });
  }

  function renderSections(secs) {
    if (!secs.length) return '<p class="fs-empty">Chưa có thông tin.</p>';
    return secs.map(function (s) {
      return '<h2>' + s.heading + '</h2>' + (window.marked ? marked.parse(s.content) : '<pre>' + s.content + '</pre>');
    }).join('');
  }

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
    { id: 'nhan-su', label: 'Nhân Sự', keywords: null },
    { id: 'ngoai-giao', label: 'Ngoại Giao', keywords: ['quan hệ thế lực', 'quan hệ'] }
  ];

  function guessMaxStat(arcs) {
    var max = 1000;
    if (arcs) {
      arcs.forEach(function (a) {
        if (a.stats) {
          a.stats.forEach(function (v) { if (v > max) max = v; });
        }
      });
    }
    var magnitude = Math.pow(10, Math.floor(Math.log10(max)));
    return Math.ceil(max / magnitude) * magnitude;
  }

  function renderDiploBar(key, val, color, idx) {
    var row = el('div', 'fs-diplo-row');
    row.appendChild(el('span', 'fs-diplo-label', DIPLO_LABELS[idx]));
    var barWrap = el('div', 'fs-diplo-bar-wrap');
    var centerLine = el('div', 'fs-diplo-center');
    barWrap.appendChild(centerLine);
    var bar = el('div', 'fs-diplo-bar');
    bar.style.background = color;
    var pct = Math.abs(val) / 2;
    if (val >= 0) {
      bar.style.left = '50%';
      bar.style.width = pct + '%';
    } else {
      bar.style.left = (50 - pct) + '%';
      bar.style.width = pct + '%';
    }
    barWrap.appendChild(bar);
    row.appendChild(barWrap);
    row.appendChild(el('span', 'fs-diplo-val', (val >= 0 ? '+' : '') + val));
    return row;
  }

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

    // 1. HEADER
    var header = el('div', 'fs-header');
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

    var info = el('div', 'fs-info');
    var nameEl = el('div', 'fs-name');
    nameEl.textContent = fm.name || '???';
    if (fm.hantu) {
      var hantu = el('span', 'fs-hantu', '(' + fm.hantu + ')');
      nameEl.appendChild(hantu);
    }
    info.appendChild(nameEl);

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
    var statusBadge = el('span', 'fs-badge fs-badge-status');
    function updateStatusBadge(arc) {
      var s = (arc && arc.status) || '—';
      statusBadge.textContent = s;
      statusBadge.style.background = STATUS_COLORS[s] || '#7a7067';
    }
    updateStatusBadge(currentArc());
    badges.appendChild(statusBadge);
    var rankBadge = el('span', 'fs-badge fs-badge-rank');
    function updateRankBadge(arc) {
      rankBadge.textContent = (arc && arc.rank) || '—';
    }
    updateRankBadge(currentArc());
    badges.appendChild(rankBadge);
    info.appendChild(badges);

    var meta = el('div', 'fs-meta');
    if (fm.race) meta.appendChild(el('span', null, fm.race));
    if (fm.region) meta.appendChild(el('span', null, fm.region));
    if (fm.founded) meta.appendChild(el('span', null, fm.founded));
    if (fm.founder) meta.appendChild(el('span', null, fm.founder));
    info.appendChild(meta);

    var leaderEl = el('div', 'fs-leader');
    function updateLeader(arc) {
      leaderEl.textContent = (arc && arc.leader) ? 'Lãnh Đạo: ' + arc.leader : '';
    }
    updateLeader(currentArc());
    info.appendChild(leaderEl);

    var popEl = el('div', 'fs-population');
    function updatePop(arc) {
      popEl.textContent = (arc && arc.population) ? 'Thành viên: ' + arc.population.toLocaleString() : '';
    }
    updatePop(currentArc());
    info.appendChild(popEl);

    header.appendChild(info);
    sheet.appendChild(header);

    // 2. ARC TIMELINE
    var arcButtons = [];
    var territoryWrap, assetsWrap;
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

      territoryWrap = el('div', 'fs-territory');
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

      assetsWrap = el('div', 'fs-assets');
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

    // 3. RADAR CHART
    var radarWrap = el('div', 'fs-radar-wrap');
    var radarState = createRadarChart(currentArc().stats, maxVal);
    radarWrap.appendChild(radarState.svg);
    sheet.appendChild(radarWrap);

    // 4. TABS
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

    function renderDivisionsTab(arc) {
      var wrap = el('div');
      if (!arc || !arc.divisions || !arc.divisions.length) {
        wrap.innerHTML = '<p class="fs-empty">Chưa có thông tin cơ cấu.</p>';
        return wrap;
      }
      arc.divisions.forEach(function (div) {
        var card = el('div', 'fs-division');
        var dh = el('div', 'fs-division-header');
        dh.appendChild(el('span', 'fs-division-name', div.name));
        if (div.role) dh.appendChild(el('span', 'fs-division-role', div.role));
        card.appendChild(dh);
        if (div.headcount) {
          var keys = Object.keys(div.headcount);
          var maxHc = 0;
          keys.forEach(function (k) { if (div.headcount[k] > maxHc) maxHc = div.headcount[k]; });
          var hcColors = ['#9b72cf', '#e87da0', '#d4a574', '#52b788', '#5a9ec4', '#e05252', '#7a7067'];
          keys.forEach(function (k, i) {
            card.appendChild(renderHcBar(k, div.headcount[k], maxHc, hcColors[i % hcColors.length]));
          });
        }
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

    renderTabContent(activeTabId);

    // 5. ARC SWITCHING
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
      if (typeof updateTerritory === 'function') updateTerritory(arc);
      if (typeof updateAssets === 'function') updateAssets(arc);
      updateRadarChart(radarState, arc.stats, maxVal);
      if (activeTabId === 'nhan-su' || activeTabId === 'ngoai-giao') {
        renderTabContent(activeTabId);
      }
    }

    container.appendChild(sheet);
  }

  window.FactionSheet = {
    render: render
  };
})();
