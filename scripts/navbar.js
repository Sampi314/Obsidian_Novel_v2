/* ═══════════════════════════════════════════
   CỐ NGUYÊN GIỚI — Site-Wide Navigation Bar
   Multi-Theme · Integrated Theme Picker
   ═══════════════════════════════════════════ */

(function () {
  'use strict';

  var themes = [
    { id: 'thuy-mac', name: 'Thủy Mặc', icon: '🌑' },
    { id: 'huyet-nguyet', name: 'Huyết Nguyệt', icon: '🔴' },
    { id: 'thanh-truc', name: 'Thanh Trúc', icon: '🌿' },
    { id: 'co-thu', name: 'Cổ Thư', icon: '📜' },
    { id: 'bach-tuyet', name: 'Bạch Tuyết', icon: '⬜' },
  ];

  var css = document.createElement('style');
  css.textContent = [
    /* ── Base Bar ── */
    '.mn-bar{',
      'position:fixed;top:0;left:0;width:100%;z-index:8000;',
      'padding:0 clamp(16px,3vw,48px);',
      'display:flex;align-items:center;justify-content:space-between;',
      'height:60px;',
      'background:transparent;',
      'transition:background .5s cubic-bezier(.25,.46,.45,.94),',
        'box-shadow .5s ease,height .4s ease,backdrop-filter .5s ease;',
      'font-family:"Cormorant Garamond","Georgia",serif;',
    '}',

    '.mn-bar.mn-scrolled{',
      'background:rgba(12,15,20,.92);',
      'backdrop-filter:blur(12px) saturate(1.2);',
      '-webkit-backdrop-filter:blur(12px) saturate(1.2);',
      'box-shadow:0 1px 0 rgba(212,165,116,.06),0 4px 20px rgba(0,0,0,.35);',
      'height:50px;',
    '}',

    '.mn-bar::after{',
      'content:"";position:absolute;bottom:0;left:0;',
      'width:100%;height:1px;',
      'background:linear-gradient(to right,transparent,rgba(212,165,116,.1),transparent);',
      'opacity:0;transition:opacity .5s ease;',
    '}',
    '.mn-bar.mn-scrolled::after{opacity:1;}',

    /* ── Logo ── */
    '.mn-logo{',
      'display:flex;align-items:center;gap:10px;',
      'text-decoration:none;color:var(--accent,#d4a574);',
      'flex-shrink:0;',
    '}',

    '.mn-logo-symbol{',
      'font-size:1.4rem;',
      'filter:drop-shadow(0 0 6px rgba(212,165,116,.2));',
      'transition:filter .4s ease,transform .4s ease;',
      'line-height:1;',
    '}',
    '.mn-logo:hover .mn-logo-symbol{',
      'filter:drop-shadow(0 0 12px rgba(212,165,116,.4));',
      'transform:rotate(180deg);',
    '}',

    '.mn-logo-text{',
      'font-size:1rem;font-weight:500;',
      'letter-spacing:.1em;',
      'color:var(--text,#e8e0d4);',
      'transition:color .3s ease;',
    '}',
    '.mn-bar.mn-scrolled .mn-logo-text{font-size:.92rem;}',
    '.mn-logo:hover .mn-logo-text{color:var(--accent-bright,#e8be8e);}',

    /* ── Desktop Links + Right Section ── */
    '.mn-right{',
      'display:flex;align-items:center;gap:4px;',
    '}',

    '.mn-links{',
      'display:flex;align-items:center;gap:4px;',
      'list-style:none;margin:0;padding:0;',
    '}',

    '.mn-links li{position:relative;}',

    '.mn-links a,.mn-links button{',
      'display:block;padding:8px 14px;',
      'text-decoration:none;',
      'color:var(--muted,#6a7080);',
      'font-size:.8rem;font-weight:500;',
      'letter-spacing:.08em;',
      'transition:color .3s ease;',
      'position:relative;background:none;border:none;cursor:pointer;',
      'font-family:"Cormorant Garamond","Georgia",serif;',
    '}',

    '.mn-links a:hover,.mn-links a.mn-active,.mn-links button:hover{color:var(--accent-bright,#e8be8e);}',

    '.mn-links a::after{',
      'content:"";position:absolute;',
      'bottom:2px;left:14px;right:14px;height:1.5px;',
      'background:linear-gradient(to right,transparent,var(--accent,#d4a574),transparent);',
      'transform:scaleX(0);transform-origin:center;',
      'transition:transform .35s cubic-bezier(.25,.46,.45,.94);',
      'border-radius:1px;',
    '}',
    '.mn-links a:hover::after,.mn-links a.mn-active::after{transform:scaleX(1);}',

    '.mn-links li+li::before{',
      'content:"·";position:absolute;left:-2px;top:50%;',
      'transform:translateY(-50%);',
      'color:rgba(212,165,116,.12);font-size:.85rem;',
      'pointer-events:none;',
    '}',

    /* ── Theme Picker (integrated in navbar) ── */
    '.mn-theme-wrap{position:relative;}',

    '.mn-theme-btn{',
      'display:flex;align-items:center;gap:5px;',
      'padding:6px 12px !important;',
      'font-size:.75rem !important;letter-spacing:.06em;',
    '}',
    '.mn-theme-btn .mn-theme-icon{font-size:.9rem;line-height:1;}',
    '.mn-theme-btn .mn-theme-arrow{',
      'font-size:.5rem;transition:transform .3s ease;',
    '}',
    '.mn-theme-wrap.mn-open .mn-theme-arrow{transform:rotate(180deg);}',

    '.mn-theme-dropdown{',
      'position:absolute;top:calc(100% + 8px);right:0;',
      'min-width:160px;',
      'background:var(--ink,#151a22);',
      'border:1px solid rgba(212,165,116,.08);',
      'border-radius:4px;',
      'box-shadow:0 8px 32px rgba(0,0,0,.4);',
      'opacity:0;visibility:hidden;',
      'transform:translateY(-6px);',
      'transition:opacity .25s ease,visibility .25s ease,transform .25s ease;',
      'overflow:hidden;z-index:8020;',
    '}',
    '.mn-theme-wrap.mn-open .mn-theme-dropdown{',
      'opacity:1;visibility:visible;transform:translateY(0);',
    '}',

    '.mn-theme-option{',
      'display:flex;align-items:center;gap:10px;',
      'width:100%;padding:10px 16px;',
      'background:none;border:none;cursor:pointer;',
      'color:var(--muted,#6a7080);',
      'font-family:"Cormorant Garamond","Georgia",serif;',
      'font-size:.82rem;letter-spacing:.04em;',
      'transition:all .25s ease;text-align:left;',
    '}',
    '.mn-theme-option:hover{',
      'background:rgba(212,165,116,.04);',
      'color:var(--accent-bright,#e8be8e);',
    '}',
    '.mn-theme-option.mn-active-theme{',
      'color:var(--accent,#d4a574);',
      'background:rgba(212,165,116,.06);',
    '}',
    '.mn-theme-option-icon{font-size:1rem;flex-shrink:0;}',
    '.mn-theme-option-check{',
      'margin-left:auto;font-size:.7rem;color:var(--accent,#d4a574);opacity:0;',
    '}',
    '.mn-theme-option.mn-active-theme .mn-theme-option-check{opacity:1;}',

    /* ── Hamburger ── */
    '.mn-hamburger{',
      'display:none;',
      'flex-direction:column;justify-content:center;align-items:center;',
      'width:38px;height:38px;',
      'cursor:pointer;border:none;background:none;',
      'padding:0;position:relative;z-index:8010;',
    '}',

    '.mn-hamburger span{',
      'display:block;width:20px;height:1.5px;',
      'background:var(--accent,#d4a574);',
      'transition:all .35s cubic-bezier(.25,.46,.45,.94);',
      'position:absolute;',
    '}',
    '.mn-hamburger span:nth-child(1){transform:translateY(-5px);}',
    '.mn-hamburger span:nth-child(2){opacity:1;}',
    '.mn-hamburger span:nth-child(3){transform:translateY(5px);}',

    '.mn-hamburger.mn-open span:nth-child(1){transform:rotate(45deg);}',
    '.mn-hamburger.mn-open span:nth-child(2){opacity:0;}',
    '.mn-hamburger.mn-open span:nth-child(3){transform:rotate(-45deg);}',

    /* ── Mobile Overlay ── */
    '.mn-overlay{',
      'position:fixed;top:0;left:0;width:100%;height:100%;',
      'background:rgba(12,15,20,.97);',
      'backdrop-filter:blur(20px);',
      '-webkit-backdrop-filter:blur(20px);',
      'z-index:8005;',
      'display:flex;flex-direction:column;',
      'justify-content:center;align-items:center;gap:8px;',
      'opacity:0;visibility:hidden;',
      'transition:opacity .4s ease,visibility .4s ease;',
    '}',
    '.mn-overlay.mn-open{opacity:1;visibility:visible;}',

    '.mn-overlay::before{',
      'content:"";position:absolute;',
      'width:280px;height:280px;border-radius:50%;',
      'border:1px solid rgba(212,165,116,.03);',
      'top:50%;left:50%;transform:translate(-50%,-50%);',
      'pointer-events:none;',
    '}',
    '.mn-overlay::after{',
      'content:"";position:absolute;',
      'width:420px;height:420px;border-radius:50%;',
      'border:1px solid rgba(212,165,116,.02);',
      'top:50%;left:50%;transform:translate(-50%,-50%);',
      'pointer-events:none;',
    '}',

    '.mn-overlay a,.mn-overlay .mn-overlay-theme-label{',
      'text-decoration:none;color:var(--muted,#6a7080);',
      'font-family:"Cormorant Garamond","Georgia",serif;',
      'font-size:1.25rem;font-weight:400;',
      'letter-spacing:.15em;',
      'padding:14px 28px;',
      'transition:color .3s ease,transform .3s ease,letter-spacing .4s ease;',
      'position:relative;',
      'opacity:0;transform:translateY(18px);',
    '}',
    '.mn-overlay.mn-open a,.mn-overlay.mn-open .mn-overlay-theme-label{opacity:1;transform:translateY(0);}',

    '.mn-overlay a:hover{',
      'color:var(--accent-bright,#e8be8e);',
      'letter-spacing:.22em;',
    '}',

    '.mn-overlay-divider{',
      'width:50px;height:1px;',
      'background:linear-gradient(to right,transparent,rgba(212,165,116,.15),transparent);',
      'margin:6px 0;',
      'opacity:0;',
      'transition:opacity .4s ease .15s;',
    '}',
    '.mn-overlay.mn-open .mn-overlay-divider{opacity:1;}',

    /* ── Mobile Theme Picker ── */
    '.mn-overlay-themes{',
      'display:flex;gap:12px;margin-top:4px;',
      'opacity:0;transform:translateY(18px);',
      'transition:opacity .4s ease .3s,transform .4s ease .3s;',
    '}',
    '.mn-overlay.mn-open .mn-overlay-themes{opacity:1;transform:translateY(0);}',

    '.mn-overlay-theme-dot{',
      'width:32px;height:32px;border-radius:50%;',
      'border:2px solid rgba(212,165,116,.12);',
      'background:none;cursor:pointer;',
      'font-size:.85rem;line-height:32px;text-align:center;',
      'transition:all .3s ease;',
    '}',
    '.mn-overlay-theme-dot:hover,.mn-overlay-theme-dot.mn-active-theme{',
      'border-color:var(--accent,#d4a574);',
      'box-shadow:0 0 12px rgba(212,165,116,.15);',
      'transform:scale(1.15);',
    '}',

    /* ── Bạch Tuyết (light theme) overrides ── */
    '[data-theme="bach-tuyet"] .mn-bar.mn-scrolled{',
      'background:rgba(245,240,232,.92);',
      'box-shadow:0 1px 0 rgba(138,96,32,.06),0 4px 20px rgba(42,36,32,.08);',
    '}',
    '[data-theme="bach-tuyet"] .mn-overlay{background:rgba(245,240,232,.97);}',
    '[data-theme="bach-tuyet"] .mn-overlay::before{border-color:rgba(138,96,32,.04);}',
    '[data-theme="bach-tuyet"] .mn-overlay::after{border-color:rgba(138,96,32,.03);}',
    '[data-theme="bach-tuyet"] .mn-overlay-divider{background:linear-gradient(to right,transparent,rgba(138,96,32,.12),transparent);}',
    '[data-theme="bach-tuyet"] .mn-bar::after{background:linear-gradient(to right,transparent,rgba(138,96,32,.08),transparent);}',
    '[data-theme="bach-tuyet"] .mn-theme-dropdown{',
      'background:var(--ink,#faf6ef);',
      'border-color:rgba(138,96,32,.1);',
      'box-shadow:0 8px 32px rgba(42,36,32,.15);',
    '}',

    /* ── Responsive ── */
    '@media(max-width:768px){',
      '.mn-links{display:none;}',
      '.mn-hamburger{display:flex;}',
      '.mn-logo-text{font-size:.88rem;letter-spacing:.07em;}',
      '.mn-logo-symbol{font-size:1.2rem;}',
    '}',

    'body.mn-menu-open{overflow:hidden;}',

  ].join('\n');
  document.head.appendChild(css);

  // ── Navigation Data ──
  var isIndex = /index\.html$/.test(window.location.pathname) ||
                window.location.pathname.endsWith('/');

  var links = [
    { label: 'Trang Chủ', href: 'index.html' },
    { label: 'Cốt Truyện', href: 'index.html#cot-truyen' },
    { label: 'Tra Cứu', href: 'index.html#tra-cuu' },
    { label: 'Quan Hệ', href: 'relationship.html' },
  ];

  // ── Build DOM ──
  var bar = document.createElement('nav');
  bar.className = 'mn-bar';
  bar.setAttribute('aria-label', 'Site navigation');

  var logo = document.createElement('a');
  logo.className = 'mn-logo';
  logo.href = 'index.html';
  logo.setAttribute('aria-label', 'Trang chủ Cố Nguyên Giới');
  logo.innerHTML =
    '<span class="mn-logo-symbol">\u262F</span>' +
    '<span class="mn-logo-text">Cố Nguyên Giới</span>';
  bar.appendChild(logo);

  // Right section: links + theme picker + hamburger
  var rightSection = document.createElement('div');
  rightSection.className = 'mn-right';

  var ul = document.createElement('ul');
  ul.className = 'mn-links';
  ul.setAttribute('role', 'menubar');

  for (var i = 0; i < links.length; i++) {
    var li = document.createElement('li');
    li.setAttribute('role', 'none');
    var a = document.createElement('a');
    a.href = links[i].href;
    a.textContent = links[i].label;
    a.setAttribute('role', 'menuitem');

    if (links[i].href === 'index.html' && isIndex) {
      a.classList.add('mn-active');
    } else if (links[i].href === 'relationship.html' &&
               /relationship\.html/.test(window.location.pathname)) {
      a.classList.add('mn-active');
    }

    li.appendChild(a);
    ul.appendChild(li);
  }

  // Theme picker in navbar (as a list item)
  var themeLi = document.createElement('li');
  themeLi.setAttribute('role', 'none');
  var themeWrap = document.createElement('div');
  themeWrap.className = 'mn-theme-wrap';

  var currentTheme = localStorage.getItem('co-nguyen-theme') || 'thuy-mac';
  var currentThemeObj = themes.find(function(t) { return t.id === currentTheme; }) || themes[0];

  var themeBtn = document.createElement('button');
  themeBtn.className = 'mn-theme-btn';
  themeBtn.setAttribute('aria-label', 'Chọn giao diện');
  themeBtn.innerHTML = '<span class="mn-theme-icon">' + currentThemeObj.icon + '</span>' +
                        '<span class="mn-theme-arrow">&#9660;</span>';

  var themeDropdown = document.createElement('div');
  themeDropdown.className = 'mn-theme-dropdown';

  themes.forEach(function(t) {
    var opt = document.createElement('button');
    opt.className = 'mn-theme-option' + (t.id === currentTheme ? ' mn-active-theme' : '');
    opt.innerHTML = '<span class="mn-theme-option-icon">' + t.icon + '</span>' +
                    '<span>' + t.name + '</span>' +
                    '<span class="mn-theme-option-check">&#10003;</span>';
    opt.addEventListener('click', function() {
      applyTheme(t.id);
    });
    themeDropdown.appendChild(opt);
  });

  themeWrap.appendChild(themeBtn);
  themeWrap.appendChild(themeDropdown);
  themeLi.appendChild(themeWrap);
  ul.appendChild(themeLi);

  rightSection.appendChild(ul);

  var hamburger = document.createElement('button');
  hamburger.className = 'mn-hamburger';
  hamburger.setAttribute('aria-label', 'Menu');
  hamburger.setAttribute('aria-expanded', 'false');
  for (var s = 0; s < 3; s++) {
    hamburger.appendChild(document.createElement('span'));
  }
  rightSection.appendChild(hamburger);

  bar.appendChild(rightSection);

  // ── Mobile Overlay ──
  var overlay = document.createElement('div');
  overlay.className = 'mn-overlay';
  overlay.setAttribute('role', 'dialog');
  overlay.setAttribute('aria-label', 'Navigation menu');

  for (var j = 0; j < links.length; j++) {
    if (j === 2) {
      var divider = document.createElement('div');
      divider.className = 'mn-overlay-divider';
      overlay.appendChild(divider);
    }
    var ma = document.createElement('a');
    ma.href = links[j].href;
    ma.textContent = links[j].label;
    overlay.appendChild(ma);
  }

  // Mobile theme dots
  var mobileDivider = document.createElement('div');
  mobileDivider.className = 'mn-overlay-divider';
  overlay.appendChild(mobileDivider);

  var mobileThemeLabel = document.createElement('div');
  mobileThemeLabel.className = 'mn-overlay-theme-label';
  mobileThemeLabel.textContent = 'Giao Diện';
  mobileThemeLabel.style.cssText = 'font-size:0.85rem;letter-spacing:.3em;color:var(--accent-dim,#9b7a52);cursor:default;';
  overlay.appendChild(mobileThemeLabel);

  var mobileThemes = document.createElement('div');
  mobileThemes.className = 'mn-overlay-themes';
  themes.forEach(function(t) {
    var dot = document.createElement('button');
    dot.className = 'mn-overlay-theme-dot' + (t.id === currentTheme ? ' mn-active-theme' : '');
    dot.textContent = t.icon;
    dot.title = t.name;
    dot.addEventListener('click', function() {
      applyTheme(t.id);
    });
    mobileThemes.appendChild(dot);
  });
  overlay.appendChild(mobileThemes);

  document.body.prepend(overlay);
  document.body.prepend(bar);

  // ── Theme Switching ──
  function applyTheme(id) {
    localStorage.setItem('co-nguyen-theme', id);
    document.documentElement.setAttribute('data-theme', id);

    var obj = themes.find(function(t) { return t.id === id; }) || themes[0];
    themeBtn.querySelector('.mn-theme-icon').textContent = obj.icon;

    // Update desktop dropdown
    themeDropdown.querySelectorAll('.mn-theme-option').forEach(function(opt, idx) {
      opt.classList.toggle('mn-active-theme', themes[idx].id === id);
    });

    // Update mobile dots
    mobileThemes.querySelectorAll('.mn-overlay-theme-dot').forEach(function(dot, idx) {
      dot.classList.toggle('mn-active-theme', themes[idx].id === id);
    });

    // Close dropdown
    themeWrap.classList.remove('mn-open');
  }

  // Toggle theme dropdown
  themeBtn.addEventListener('click', function(e) {
    e.stopPropagation();
    themeWrap.classList.toggle('mn-open');
  });

  // Close dropdown on outside click
  document.addEventListener('click', function(e) {
    if (!themeWrap.contains(e.target)) {
      themeWrap.classList.remove('mn-open');
    }
  });

  // ── Scroll Logic ──
  var scrolled = false;
  var ticking = false;

  function onScroll() {
    var sy = window.pageYOffset || document.documentElement.scrollTop;
    var shouldMark = sy > 40;
    if (shouldMark !== scrolled) {
      scrolled = shouldMark;
      if (scrolled) bar.classList.add('mn-scrolled');
      else bar.classList.remove('mn-scrolled');
    }
    ticking = false;
  }

  window.addEventListener('scroll', function () {
    if (!ticking) {
      requestAnimationFrame(onScroll);
      ticking = true;
    }
  }, { passive: true });

  if (!isIndex) bar.classList.add('mn-scrolled');
  onScroll();

  // ── Mobile Menu ──
  function toggleMenu() {
    var isOpen = hamburger.classList.toggle('mn-open');
    overlay.classList.toggle('mn-open');
    document.body.classList.toggle('mn-menu-open');
    hamburger.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
  }

  hamburger.addEventListener('click', toggleMenu);

  overlay.addEventListener('click', function (e) {
    if (e.target.tagName === 'A') toggleMenu();
  });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
      if (overlay.classList.contains('mn-open')) toggleMenu();
      themeWrap.classList.remove('mn-open');
    }
  });

  // ── Smooth scroll for same-page hash links ──
  bar.addEventListener('click', function (e) {
    var target = e.target.closest('a[href*="#"]');
    if (!target) return;

    var href = target.getAttribute('href');
    var hashIdx = href.indexOf('#');
    if (hashIdx === -1) return;

    var page = href.substring(0, hashIdx);
    var hash = href.substring(hashIdx + 1);

    var onTargetPage = (page === '' || page === 'index.html') && isIndex;
    if (!onTargetPage) return;

    var el = document.getElementById(hash);
    if (!el) return;

    e.preventDefault();
    el.scrollIntoView({ behavior: 'smooth', block: 'start' });
  });

})();
