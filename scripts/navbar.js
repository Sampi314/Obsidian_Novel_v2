/* ═══════════════════════════════════════════
   MYSTIC INK — Site-Wide Navigation Bar
   "Floating Jade Tablet" — Ancient Sect Banner
   ═══════════════════════════════════════════ */

(function () {
  'use strict';

  // ── Inject Styles ──
  var css = document.createElement('style');
  css.textContent = [
    /* ── Base Bar ── */
    '.mn-bar{',
      'position:fixed;top:0;left:0;width:100%;z-index:8000;',
      'padding:0 clamp(16px,3vw,48px);',
      'display:flex;align-items:center;justify-content:space-between;',
      'height:64px;',
      'background:transparent;',
      'transition:background .5s cubic-bezier(.25,.46,.45,.94),',
        'box-shadow .5s ease,height .4s ease,backdrop-filter .5s ease;',
      'font-family:"Playfair Display","Georgia",serif;',
    '}',

    /* Scrolled state */
    '.mn-bar.mn-scrolled{',
      'background:rgba(10,9,8,.92);',
      'backdrop-filter:blur(12px) saturate(1.3);',
      '-webkit-backdrop-filter:blur(12px) saturate(1.3);',
      'box-shadow:0 1px 0 rgba(201,169,110,.08),0 4px 24px rgba(0,0,0,.4);',
      'height:52px;',
    '}',

    /* Bottom accent line */
    '.mn-bar::after{',
      'content:"";position:absolute;bottom:0;left:0;',
      'width:100%;height:1px;',
      'background:linear-gradient(to right,transparent,rgba(201,169,110,.12),transparent);',
      'opacity:0;transition:opacity .5s ease;',
    '}',
    '.mn-bar.mn-scrolled::after{opacity:1;}',

    /* ── Logo ── */
    '.mn-logo{',
      'display:flex;align-items:center;gap:12px;',
      'text-decoration:none;color:#c9a96e;',
      'flex-shrink:0;',
    '}',

    '.mn-logo-symbol{',
      'font-size:1.5rem;',
      'filter:drop-shadow(0 0 8px rgba(201,169,110,.25));',
      'transition:filter .4s ease,transform .4s ease;',
      'line-height:1;',
    '}',
    '.mn-logo:hover .mn-logo-symbol{',
      'filter:drop-shadow(0 0 16px rgba(201,169,110,.5));',
      'transform:rotate(180deg);',
    '}',

    '.mn-logo-text{',
      'font-size:1.05rem;font-weight:500;',
      'letter-spacing:.12em;',
      'color:#d4cbbf;',
      'transition:color .3s ease;',
    '}',
    '.mn-bar.mn-scrolled .mn-logo-text{font-size:.95rem;}',
    '.mn-logo:hover .mn-logo-text{color:#e4c98a;}',

    /* ── Desktop Links ── */
    '.mn-links{',
      'display:flex;align-items:center;gap:6px;',
      'list-style:none;margin:0;padding:0;',
    '}',

    '.mn-links li{position:relative;}',

    '.mn-links a{',
      'display:block;padding:8px 16px;',
      'text-decoration:none;',
      'color:#7a7067;',
      'font-size:.82rem;font-weight:500;',
      'letter-spacing:.1em;',
      'transition:color .3s ease;',
      'position:relative;',
    '}',

    '.mn-links a:hover,.mn-links a.mn-active{color:#e4c98a;}',

    /* Brush-stroke underline */
    '.mn-links a::after{',
      'content:"";position:absolute;',
      'bottom:2px;left:16px;right:16px;height:2px;',
      'background:linear-gradient(to right,transparent,#c9a96e,transparent);',
      'transform:scaleX(0);transform-origin:center;',
      'transition:transform .35s cubic-bezier(.25,.46,.45,.94);',
      'border-radius:1px;',
    '}',
    '.mn-links a:hover::after,.mn-links a.mn-active::after{transform:scaleX(1);}',

    /* Separator dot between links */
    '.mn-links li+li::before{',
      'content:"·";position:absolute;left:-3px;top:50%;',
      'transform:translateY(-50%);',
      'color:rgba(201,169,110,.15);font-size:.9rem;',
      'pointer-events:none;',
    '}',

    /* ── Hamburger (mobile) ── */
    '.mn-hamburger{',
      'display:none;',
      'flex-direction:column;justify-content:center;align-items:center;',
      'width:40px;height:40px;',
      'cursor:pointer;border:none;background:none;',
      'padding:0;position:relative;z-index:8010;',
    '}',

    '.mn-hamburger span{',
      'display:block;width:22px;height:1.5px;',
      'background:#c9a96e;',
      'transition:all .35s cubic-bezier(.25,.46,.45,.94);',
      'position:absolute;',
    '}',
    '.mn-hamburger span:nth-child(1){transform:translateY(-6px);}',
    '.mn-hamburger span:nth-child(2){opacity:1;}',
    '.mn-hamburger span:nth-child(3){transform:translateY(6px);}',

    /* Open state */
    '.mn-hamburger.mn-open span:nth-child(1){transform:rotate(45deg);}',
    '.mn-hamburger.mn-open span:nth-child(2){opacity:0;}',
    '.mn-hamburger.mn-open span:nth-child(3){transform:rotate(-45deg);}',

    /* ── Mobile Overlay ── */
    '.mn-overlay{',
      'position:fixed;top:0;left:0;width:100%;height:100%;',
      'background:rgba(10,9,8,.97);',
      'backdrop-filter:blur(20px);',
      '-webkit-backdrop-filter:blur(20px);',
      'z-index:8005;',
      'display:flex;flex-direction:column;',
      'justify-content:center;align-items:center;gap:8px;',
      'opacity:0;visibility:hidden;',
      'transition:opacity .4s ease,visibility .4s ease;',
    '}',
    '.mn-overlay.mn-open{opacity:1;visibility:visible;}',

    /* Decorative circles in overlay */
    '.mn-overlay::before{',
      'content:"";position:absolute;',
      'width:300px;height:300px;border-radius:50%;',
      'border:1px solid rgba(201,169,110,.04);',
      'top:50%;left:50%;transform:translate(-50%,-50%);',
      'pointer-events:none;',
    '}',
    '.mn-overlay::after{',
      'content:"";position:absolute;',
      'width:450px;height:450px;border-radius:50%;',
      'border:1px solid rgba(201,169,110,.025);',
      'top:50%;left:50%;transform:translate(-50%,-50%);',
      'pointer-events:none;',
    '}',

    '.mn-overlay a{',
      'text-decoration:none;color:#7a7067;',
      'font-family:"Playfair Display","Georgia",serif;',
      'font-size:1.3rem;font-weight:400;',
      'letter-spacing:.18em;',
      'padding:16px 32px;',
      'transition:color .3s ease,transform .3s ease,letter-spacing .4s ease;',
      'position:relative;',
      'opacity:0;transform:translateY(20px);',
    '}',
    '.mn-overlay.mn-open a{opacity:1;transform:translateY(0);}',

    '.mn-overlay a:hover{',
      'color:#e4c98a;',
      'letter-spacing:.25em;',
    '}',

    /* Stagger animation for mobile links */
    '.mn-overlay a:nth-child(1){transition-delay:.05s;}',
    '.mn-overlay a:nth-child(2){transition-delay:.1s;}',
    '.mn-overlay a:nth-child(3){transition-delay:.15s;}',
    '.mn-overlay a:nth-child(4){transition-delay:.2s;}',
    '.mn-overlay a:nth-child(5){transition-delay:.25s;}',

    /* Mobile overlay divider */
    '.mn-overlay-divider{',
      'width:60px;height:1px;',
      'background:linear-gradient(to right,transparent,rgba(201,169,110,.2),transparent);',
      'margin:8px 0;',
      'opacity:0;',
      'transition:opacity .4s ease .15s;',
    '}',
    '.mn-overlay.mn-open .mn-overlay-divider{opacity:1;}',

    /* ── Responsive ── */
    '@media(max-width:768px){',
      '.mn-links{display:none;}',
      '.mn-hamburger{display:flex;}',
      '.mn-logo-text{font-size:.9rem;letter-spacing:.08em;}',
      '.mn-logo-symbol{font-size:1.3rem;}',
    '}',

    /* Prevent body scroll when menu open */
    'body.mn-menu-open{overflow:hidden;}',

  ].join('\n');
  document.head.appendChild(css);

  // ── Navigation Data ──
  var isIndex = /index\.html$/.test(window.location.pathname) ||
                window.location.pathname.endsWith('/');
  var isReader = /reader\.html/.test(window.location.pathname);

  var links = [
    { label: 'Trang Chủ', href: 'index.html', icon: '🏠' },
    { label: 'Cốt Truyện', href: 'index.html#cot-truyen', icon: '📖' },
    { label: 'Tra Cứu', href: 'index.html#tra-cuu', icon: '📚' },
    { label: 'Quan Hệ', href: 'relationship.html', icon: '🔗' },
  ];

  // ── Build DOM ──
  var bar = document.createElement('nav');
  bar.className = 'mn-bar';
  bar.setAttribute('aria-label', 'Site navigation');

  // Logo
  var logo = document.createElement('a');
  logo.className = 'mn-logo';
  logo.href = 'index.html';
  logo.setAttribute('aria-label', 'Trang chủ Cố Nguyên Giới');
  logo.innerHTML =
    '<span class="mn-logo-symbol">☯</span>' +
    '<span class="mn-logo-text">Cố Nguyên Giới</span>';
  bar.appendChild(logo);

  // Desktop links
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

    // Active state
    if (links[i].href === 'index.html' && isIndex) {
      a.classList.add('mn-active');
    } else if (links[i].href === 'relationship.html' &&
               /relationship\.html/.test(window.location.pathname)) {
      a.classList.add('mn-active');
    }

    li.appendChild(a);
    ul.appendChild(li);
  }
  bar.appendChild(ul);

  // Hamburger
  var hamburger = document.createElement('button');
  hamburger.className = 'mn-hamburger';
  hamburger.setAttribute('aria-label', 'Menu');
  hamburger.setAttribute('aria-expanded', 'false');
  for (var s = 0; s < 3; s++) {
    hamburger.appendChild(document.createElement('span'));
  }
  bar.appendChild(hamburger);

  // Mobile overlay
  var overlay = document.createElement('div');
  overlay.className = 'mn-overlay';
  overlay.setAttribute('role', 'dialog');
  overlay.setAttribute('aria-label', 'Navigation menu');

  for (var j = 0; j < links.length; j++) {
    if (j === 2) {
      // Divider before "Tra Cứu"
      var divider = document.createElement('div');
      divider.className = 'mn-overlay-divider';
      overlay.appendChild(divider);
    }
    var ma = document.createElement('a');
    ma.href = links[j].href;
    ma.textContent = links[j].label;
    overlay.appendChild(ma);
  }

  // ── Insert into DOM ──
  document.body.prepend(overlay);
  document.body.prepend(bar);

  // ── Scroll Logic ──
  var scrolled = false;
  var ticking = false;

  function onScroll() {
    var sy = window.pageYOffset || document.documentElement.scrollTop;
    var shouldMark = sy > 40;
    if (shouldMark !== scrolled) {
      scrolled = shouldMark;
      if (scrolled) {
        bar.classList.add('mn-scrolled');
      } else {
        bar.classList.remove('mn-scrolled');
      }
    }
    ticking = false;
  }

  window.addEventListener('scroll', function () {
    if (!ticking) {
      requestAnimationFrame(onScroll);
      ticking = true;
    }
  }, { passive: true });

  // Initial check
  onScroll();

  // ── Mobile Menu Toggle ──
  function toggleMenu() {
    var isOpen = hamburger.classList.toggle('mn-open');
    overlay.classList.toggle('mn-open');
    document.body.classList.toggle('mn-menu-open');
    hamburger.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
  }

  hamburger.addEventListener('click', toggleMenu);

  // Close on overlay link click
  overlay.addEventListener('click', function (e) {
    if (e.target.tagName === 'A') {
      toggleMenu();
    }
  });

  // Close on Escape
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && overlay.classList.contains('mn-open')) {
      toggleMenu();
    }
  });

  // ── Smooth scroll for hash links on same page ──
  bar.addEventListener('click', function (e) {
    var target = e.target.closest('a[href*="#"]');
    if (!target) return;

    var href = target.getAttribute('href');
    var hashIdx = href.indexOf('#');
    if (hashIdx === -1) return;

    var page = href.substring(0, hashIdx);
    var hash = href.substring(hashIdx + 1);

    // Only smooth-scroll if we're already on the target page
    var onTargetPage = (page === '' || page === 'index.html') && isIndex;
    if (!onTargetPage) return;

    var el = document.getElementById(hash);
    if (!el) return;

    e.preventDefault();
    el.scrollIntoView({ behavior: 'smooth', block: 'start' });
  });

})();
