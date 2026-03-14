# Chapter Lock System Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a chapter lock system where the author can mark chapters as approved from the index/reader pages, persisting lock state to GitHub via OAuth, with agent and CI protection.

**Architecture:** A shared `scripts/chapter-lock.js` module handles GitHub OAuth, lock file CRUD, and UI injection. Both `index.html` and `reader.html` load this module. A Cloudflare Worker handles the OAuth token exchange. A GitHub Action + branch protection rule blocks PRs that touch locked chapters.

**Tech Stack:** Vanilla JS (no frameworks), GitHub REST API, Cloudflare Workers, GitHub Actions

**Spec:** `docs/superpowers/specs/2026-03-14-chapter-lock-system-design.md`

---

## Chunk 1: Cloudflare Worker + Shared Auth Module

### Task 1: Create the Cloudflare Worker OAuth proxy

**Files:**
- Create: `workers/oauth-proxy/worker.js`
- Create: `workers/oauth-proxy/wrangler.toml`

- [ ] **Step 1: Create worker.js**

```javascript
// workers/oauth-proxy/worker.js
export default {
  async fetch(request, env) {
    const ALLOWED_ORIGIN = 'https://sampi314.github.io';

    // Handle CORS preflight
    if (request.method === 'OPTIONS') {
      return new Response(null, {
        status: 204,
        headers: {
          'Access-Control-Allow-Origin': ALLOWED_ORIGIN,
          'Access-Control-Allow-Methods': 'POST, OPTIONS',
          'Access-Control-Allow-Headers': 'Content-Type',
        },
      });
    }

    if (request.method !== 'POST') {
      return new Response('Method not allowed', { status: 405 });
    }

    const { code } = await request.json();
    if (!code) {
      return new Response(JSON.stringify({ error: 'Missing code' }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    const tokenResponse = await fetch('https://github.com/login/oauth/access_token', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
      },
      body: JSON.stringify({
        client_id: env.CLIENT_ID,
        client_secret: env.CLIENT_SECRET,
        code: code,
      }),
    });

    const tokenData = await tokenResponse.json();

    return new Response(JSON.stringify(tokenData), {
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': ALLOWED_ORIGIN,
      },
    });
  },
};
```

- [ ] **Step 2: Create wrangler.toml**

```toml
# workers/oauth-proxy/wrangler.toml
name = "co-nguyen-oauth-proxy"
main = "worker.js"
compatibility_date = "2024-01-01"

# Set these via: wrangler secret put CLIENT_ID / CLIENT_SECRET
# [vars]
# CLIENT_ID = "set-via-secret"
# CLIENT_SECRET = "set-via-secret"
```

- [ ] **Step 3: Commit**

```bash
git add workers/oauth-proxy/worker.js workers/oauth-proxy/wrangler.toml
git commit -m "feat: add Cloudflare Worker OAuth proxy for chapter lock system"
```

---

### Task 2: Create the shared chapter-lock.js module

**Files:**
- Create: `scripts/chapter-lock.js`

This module handles: OAuth flow, session management, lock file CRUD via GitHub API, and UI injection (login button, checkmarks).

- [ ] **Step 1: Create chapter-lock.js with config and session management**

```javascript
// scripts/chapter-lock.js
(function () {
  'use strict';

  // ── Config ──
  // TODO: Replace these after creating the GitHub OAuth App and Cloudflare Worker
  var CONFIG = {
    GITHUB_CLIENT_ID: 'YOUR_CLIENT_ID',
    OAUTH_PROXY_URL: 'https://YOUR_WORKER.workers.dev',
    REPO_OWNER: 'Sampi314',
    REPO_NAME: 'Obsidian_Novel_v2',
    ALLOWED_USER: 'Sampi314',
    SESSION_DURATION_MS: 3 * 60 * 60 * 1000, // 3 hours
    LOCK_FILE_PATH: 'locked_chapters.json',
  };

  var STORAGE_KEYS = {
    TOKEN: 'co-nguyen-gh-token',
    TIMESTAMP: 'co-nguyen-gh-ts',
    AVATAR: 'co-nguyen-gh-avatar',
    USERNAME: 'co-nguyen-gh-user',
  };

  // ── Session Management ──
  function getToken() {
    var token = localStorage.getItem(STORAGE_KEYS.TOKEN);
    var ts = parseInt(localStorage.getItem(STORAGE_KEYS.TIMESTAMP), 10);
    if (!token || !ts) return null;
    if (Date.now() - ts > CONFIG.SESSION_DURATION_MS) {
      clearSession();
      return null;
    }
    return token;
  }

  function saveSession(token, avatar, username) {
    localStorage.setItem(STORAGE_KEYS.TOKEN, token);
    localStorage.setItem(STORAGE_KEYS.TIMESTAMP, String(Date.now()));
    localStorage.setItem(STORAGE_KEYS.AVATAR, avatar || '');
    localStorage.setItem(STORAGE_KEYS.USERNAME, username || '');
  }

  function clearSession() {
    Object.keys(STORAGE_KEYS).forEach(function (k) {
      localStorage.removeItem(STORAGE_KEYS[k]);
    });
  }

  function getSessionInfo() {
    return {
      avatar: localStorage.getItem(STORAGE_KEYS.AVATAR) || '',
      username: localStorage.getItem(STORAGE_KEYS.USERNAME) || '',
    };
  }

  // Start in-page expiry timer
  function startExpiryTimer() {
    var ts = parseInt(localStorage.getItem(STORAGE_KEYS.TIMESTAMP), 10);
    if (!ts) return;
    var remaining = CONFIG.SESSION_DURATION_MS - (Date.now() - ts);
    if (remaining <= 0) {
      clearSession();
      renderAuthUI();
      return;
    }
    setTimeout(function () {
      clearSession();
      renderAuthUI();
    }, remaining);
  }

  // ── OAuth Flow ──
  function startOAuthLogin() {
    // Always redirect back to index.html (matches the registered OAuth callback URL)
    var redirectUri = window.location.origin + '/Obsidian_Novel_v2/index.html';
    var url = 'https://github.com/login/oauth/authorize'
      + '?client_id=' + encodeURIComponent(CONFIG.GITHUB_CLIENT_ID)
      + '&redirect_uri=' + encodeURIComponent(redirectUri)
      + '&scope=public_repo';
    window.location.href = url;
  }

  async function handleOAuthCallback() {
    var params = new URLSearchParams(window.location.search);
    var code = params.get('code');
    if (!code) return false;

    // Clean URL
    var cleanUrl = window.location.pathname + window.location.hash;
    window.history.replaceState({}, document.title, cleanUrl);

    try {
      // Exchange code for token
      var resp = await fetch(CONFIG.OAUTH_PROXY_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ code: code }),
      });
      var data = await resp.json();
      if (!data.access_token) {
        console.error('OAuth failed:', data);
        return false;
      }

      // Verify user is the repo owner
      var userResp = await fetch('https://api.github.com/user', {
        headers: { 'Authorization': 'Bearer ' + data.access_token },
      });
      var user = await userResp.json();
      if (user.login !== CONFIG.ALLOWED_USER) {
        alert('Access denied. Only the repo owner can lock chapters.');
        return false;
      }

      saveSession(data.access_token, user.avatar_url, user.login);
      return true;
    } catch (err) {
      console.error('OAuth error:', err);
      return false;
    }
  }

  // ── Lock File CRUD ──
  var _lockCache = { chapters: null, sha: null };

  async function fetchLockFile(token) {
    var url = 'https://api.github.com/repos/' + CONFIG.REPO_OWNER + '/' + CONFIG.REPO_NAME
      + '/contents/' + CONFIG.LOCK_FILE_PATH + '?ref=main&t=' + Date.now();
    var headers = { 'Accept': 'application/vnd.github.v3+json' };
    if (token) headers['Authorization'] = 'Bearer ' + token;

    var resp = await fetch(url, { headers: headers });
    if (resp.status === 404) {
      _lockCache = { chapters: [], sha: null };
      return [];
    }
    if (!resp.ok) throw new Error('Failed to fetch lock file: ' + resp.status);

    var data = await resp.json();
    var bytes = Uint8Array.from(atob(data.content.replace(/\s/g, '')), function(c) { return c.charCodeAt(0); });
    var content = JSON.parse(new TextDecoder().decode(bytes));
    _lockCache = { chapters: content.locked_chapters || [], sha: data.sha };
    return _lockCache.chapters;
  }

  async function toggleChapterLock(chapterPath) {
    var token = getToken();
    if (!token) return false;

    var maxRetries = 3;
    for (var attempt = 0; attempt < maxRetries; attempt++) {
      try {
        // Fetch latest
        await fetchLockFile(token);
        var chapters = _lockCache.chapters.slice();
        var idx = chapters.indexOf(chapterPath);
        var isLocking = idx === -1;
        if (isLocking) {
          chapters.push(chapterPath);
          chapters.sort();
        } else {
          chapters.splice(idx, 1);
        }

        var newContent = JSON.stringify({
          locked_chapters: chapters,
          last_updated: new Date().toISOString(),
          updated_by: getSessionInfo().username,
        }, null, 2);

        var body = {
          message: (isLocking ? 'lock' : 'unlock') + ': ' + chapterPath.split('/').pop(),
          content: btoa(unescape(encodeURIComponent(newContent))),
          branch: 'main',
        };
        if (_lockCache.sha) body.sha = _lockCache.sha;

        var url = 'https://api.github.com/repos/' + CONFIG.REPO_OWNER + '/' + CONFIG.REPO_NAME
          + '/contents/' + CONFIG.LOCK_FILE_PATH;
        var resp = await fetch(url, {
          method: 'PUT',
          headers: {
            'Authorization': 'Bearer ' + token,
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(body),
        });

        if (resp.status === 409) continue; // SHA conflict, retry
        if (resp.status === 401 || resp.status === 403) {
          clearSession();
          renderAuthUI();
          return false;
        }
        if (!resp.ok) throw new Error('PUT failed: ' + resp.status);

        var result = await resp.json();
        _lockCache.sha = result.content.sha;
        _lockCache.chapters = chapters;
        return true;
      } catch (err) {
        if (attempt === maxRetries - 1) {
          console.error('toggleChapterLock failed:', err);
          return false;
        }
      }
    }
    return false;
  }

  function isChapterLocked(chapterPath) {
    return _lockCache.chapters ? _lockCache.chapters.indexOf(chapterPath) !== -1 : false;
  }

  // ── Auth UI ──
  function renderAuthUI() {
    // Render into all auth containers (desktop navbar + mobile overlay)
    var containers = document.querySelectorAll('[id^="chapter-lock-auth"]');
    if (!containers.length) return;

    var token = getToken();

    containers.forEach(function (container) {
      container.innerHTML = '';

      if (token) {
        var info = getSessionInfo();
        var wrapper = document.createElement('div');
        wrapper.className = 'cl-auth-logged-in';

        if (info.avatar) {
          var img = document.createElement('img');
          img.src = info.avatar;
          img.alt = info.username;
          img.className = 'cl-avatar';
          img.width = 24;
          img.height = 24;
          wrapper.appendChild(img);
        }

        var logoutBtn = document.createElement('button');
        logoutBtn.className = 'cl-logout-btn';
        logoutBtn.textContent = 'Logout';
        logoutBtn.addEventListener('click', function () {
          clearSession();
          renderAuthUI();
          renderAllCheckmarks();
        });
        wrapper.appendChild(logoutBtn);
        container.appendChild(wrapper);
      } else {
        var loginBtn = document.createElement('button');
        loginBtn.className = 'cl-login-btn';
        loginBtn.textContent = 'Login with GitHub';
        loginBtn.addEventListener('click', startOAuthLogin);
        container.appendChild(loginBtn);
      }
    });
  }

  // ── Checkmark UI ──
  var _checkmarkElements = [];

  function createCheckmark(chapterPath, parentEl) {
    var token = getToken();
    var locked = isChapterLocked(chapterPath);

    var btn = document.createElement('span');
    btn.className = 'cl-checkmark' + (locked ? ' cl-locked' : '');
    btn.textContent = locked ? '\u2713' : '';
    btn.title = locked ? 'Locked for publish' : (token ? 'Click to lock' : '');
    btn.setAttribute('data-chapter-path', chapterPath);

    if (token) {
      btn.classList.add('cl-clickable');
      btn.addEventListener('click', async function (e) {
        e.preventDefault();
        e.stopPropagation();
        btn.classList.add('cl-loading');

        var success = await toggleChapterLock(chapterPath);
        btn.classList.remove('cl-loading');

        if (success) {
          var nowLocked = isChapterLocked(chapterPath);
          btn.className = 'cl-checkmark' + (nowLocked ? ' cl-locked' : '') + ' cl-clickable';
          btn.textContent = nowLocked ? '\u2713' : '';
          btn.title = nowLocked ? 'Locked for publish' : 'Click to lock';
          // Update all other checkmarks for the same chapter
          _checkmarkElements.forEach(function (el) {
            if (el !== btn && el.getAttribute('data-chapter-path') === chapterPath) {
              el.className = 'cl-checkmark' + (nowLocked ? ' cl-locked' : '') + ' cl-clickable';
              el.textContent = nowLocked ? '\u2713' : '';
            }
          });
        }
      });
    }

    _checkmarkElements.push(btn);
    parentEl.appendChild(btn);
    return btn;
  }

  function renderAllCheckmarks() {
    _checkmarkElements.forEach(function (el) {
      var path = el.getAttribute('data-chapter-path');
      var locked = isChapterLocked(path);
      var token = getToken();
      el.className = 'cl-checkmark' + (locked ? ' cl-locked' : '') + (token ? ' cl-clickable' : '');
      el.textContent = locked ? '\u2713' : '';
    });
  }

  // ── CSS ──
  function injectStyles() {
    var style = document.createElement('style');
    style.textContent = [
      '.cl-checkmark { display: inline-flex; align-items: center; justify-content: center;',
      '  width: 20px; height: 20px; font-size: 14px; border-radius: 3px;',
      '  border: 1px solid var(--muted, #6a7080); color: transparent;',
      '  transition: all 0.2s ease; flex-shrink: 0; margin-left: 8px; }',
      '.cl-checkmark.cl-locked { color: var(--accent, #d4a574);',
      '  border-color: var(--accent, #d4a574); }',
      '.cl-checkmark.cl-clickable { cursor: pointer; }',
      '.cl-checkmark.cl-clickable:hover { border-color: var(--accent-bright, #e8be8e);',
      '  background: rgba(212,165,116,0.1); }',
      '.cl-checkmark.cl-loading { opacity: 0.5; pointer-events: none;',
      '  animation: cl-pulse 0.8s ease-in-out infinite; }',
      '@keyframes cl-pulse { 0%,100% { opacity: 0.5; } 50% { opacity: 1; } }',
      '.cl-login-btn { background: none; border: 1px solid var(--accent-dim, #9b7a52);',
      '  color: var(--text, #e8e0d4); padding: 4px 12px; border-radius: 4px;',
      '  cursor: pointer; font-size: 13px; font-family: inherit;',
      '  transition: all 0.2s ease; }',
      '.cl-login-btn:hover { border-color: var(--accent, #d4a574);',
      '  background: rgba(212,165,116,0.1); }',
      '.cl-logout-btn { background: none; border: none;',
      '  color: var(--muted, #6a7080); cursor: pointer; font-size: 12px;',
      '  font-family: inherit; padding: 2px 6px; }',
      '.cl-logout-btn:hover { color: var(--text, #e8e0d4); }',
      '.cl-auth-logged-in { display: flex; align-items: center; gap: 8px; }',
      '.cl-avatar { border-radius: 50%; border: 1px solid var(--accent-dim, #9b7a52); }',
      '.cl-chapter-list { list-style: none; padding: 0; margin: 8px 0 0 0; }',
      '.cl-chapter-item { display: flex; align-items: center; padding: 6px 12px;',
      '  font-size: 14px; color: var(--text, #e8e0d4); }',
      '.cl-chapter-item a { color: var(--text, #e8e0d4); text-decoration: none;',
      '  flex: 1; transition: color 0.2s; }',
      '.cl-chapter-item a:hover { color: var(--accent, #d4a574); }',
      '.cl-expand-btn { background: none; border: none; color: var(--muted, #6a7080);',
      '  cursor: pointer; font-size: 12px; padding: 4px 8px; margin-top: 4px;',
      '  font-family: inherit; transition: color 0.2s; }',
      '.cl-expand-btn:hover { color: var(--text, #e8e0d4); }',
      '.cl-chapter-panel { max-height: 0; overflow: hidden;',
      '  transition: max-height 0.3s ease; }',
      '.cl-chapter-panel.cl-expanded { max-height: 2000px; }',
      '.cl-card-chapter-wrapper { width: 100%; margin: 4px 0 12px; }',
    ].join('\n');
    document.head.appendChild(style);
  }

  // ── Public API ──
  window.ChapterLock = {
    init: async function () {
      injectStyles();

      // Handle OAuth callback if present
      var wasCallback = await handleOAuthCallback();

      // Load lock data (public read, no token needed)
      try {
        await fetchLockFile(getToken());
      } catch (err) {
        console.error('Failed to load lock file:', err);
        _lockCache = { chapters: [], sha: null };
      }

      renderAuthUI();
      startExpiryTimer();

      if (wasCallback) {
        renderAllCheckmarks();
      }
    },
    getToken: getToken,
    isChapterLocked: isChapterLocked,
    createCheckmark: createCheckmark,
    fetchLockFile: fetchLockFile,
    renderAuthUI: renderAuthUI,
    renderAllCheckmarks: renderAllCheckmarks,
  };
})();
```

- [ ] **Step 2: Verify the file was created correctly**

Open `scripts/chapter-lock.js` in a text editor and confirm no syntax errors. Search for `YOUR_CLIENT_ID` to confirm the placeholder is present.

- [ ] **Step 3: Commit**

```bash
git add scripts/chapter-lock.js
git commit -m "feat: add shared chapter-lock module (OAuth, lock CRUD, UI)"
```

---

## Chunk 2: Index Page Integration

### Task 3: Add auth UI container and script to index.html

**Files:**
- Modify: `index.html`

The navbar is generated by `scripts/navbar.js`. We need to add the auth container after the navbar generates, and load `chapter-lock.js` + `chapter_data.js`.

- [ ] **Step 1: Add the chapter-lock auth container to the navbar**

In `index.html`, find the line that loads `scripts/navbar.js` (line 645). After the navbar script tag, add a small inline script that injects the auth container into the navbar:

```html
<script src="scripts/chapter-lock.js"></script>
<script src="scripts/chapter_data.js"></script>
```

Add these two script tags right after the `<script src="scripts/navbar.js"></script>` line.

- [ ] **Step 2: Add initialization code to the main inline script**

At the beginning of the main inline IIFE (line 646, inside `(function() { 'use strict';`), add the auth UI container injection and ChapterLock initialization. Add this code right after the `'use strict';` line:

```javascript
// ── Chapter Lock System ──
(function initChapterLock() {
    // Inject auth container into navbar
    var navLinks = document.querySelector('.mn-links');
    if (navLinks) {
        var authLi = document.createElement('li');
        authLi.id = 'chapter-lock-auth';
        authLi.style.cssText = 'display:flex;align-items:center;';
        navLinks.appendChild(authLi);
    }
    // Also inject into mobile overlay (before theme section)
    var overlay = document.querySelector('.mn-overlay');
    if (overlay) {
        var mobileAuth = document.createElement('div');
        mobileAuth.id = 'chapter-lock-auth-mobile';
        mobileAuth.style.cssText = 'display:flex;align-items:center;justify-content:center;padding:12px;';
        var themeLabel = overlay.querySelector('[style*="Theme"]') || overlay.lastElementChild;
        if (themeLabel) {
            overlay.insertBefore(mobileAuth, themeLabel);
        } else {
            overlay.appendChild(mobileAuth);
        }
    }

    if (window.ChapterLock) {
        window.ChapterLock.init().then(function () {
            // Init expandable chapters AFTER lock data is loaded
            if (typeof initExpandableChapters === 'function') {
                initExpandableChapters();
            }
        });
    }
})();
```

- [ ] **Step 3: Verify in browser**

Open `index.html` locally. Confirm:
- "Login with GitHub" button appears in the navbar (desktop)
- Button appears in the hamburger menu (mobile view, resize to < 768px)
- No JS console errors

- [ ] **Step 4: Commit**

```bash
git add index.html
git commit -m "feat: integrate chapter-lock auth UI into index page navbar"
```

---

### Task 4: Add expandable chapter lists to index page POV cards

**Files:**
- Modify: `index.html` (main inline script)

- [ ] **Step 1: Add chapter list expansion logic**

In the main inline IIFE in `index.html`, after the chapter lock initialization code from Task 3, add the following function that creates expandable chapter lists under POV cards:

```javascript
// ── Expandable Chapter Lists ──
// NOTE: This function is called from ChapterLock.init().then() above,
// NOT called synchronously, to ensure lock data is loaded first.
function initExpandableChapters() {
    if (typeof chapterData === 'undefined') return;

    var cards = document.querySelectorAll('a.card[data-card]');
    cards.forEach(function (card) {
        var href = card.getAttribute('href');
        if (!href || href.indexOf('MỤC_LỤC.md') === -1) return;

        // Extract POV key and directory path from href
        // href format: reader.html?file=Đạo/Chương_Truyện/Bắc_Băng/Góc_Nhìn_Bắc_Băng/MỤC_LỤC.md
        var fileParam = href.split('file=')[1];
        if (!fileParam) return;
        var dirPath = decodeURIComponent(fileParam).replace(/MỤC_LỤC\.md$/, '');
        var povKey = dirPath.split('/').filter(Boolean).pop(); // e.g., "Góc_Nhìn_Bắc_Băng"

        var chapters = chapterData[povKey];
        if (!chapters || chapters.length === 0) return;

        // Find the card-grid parent to insert AFTER the grid (not inside it)
        var cardGrid = card.closest('.card-grid');
        if (!cardGrid) return;

        // Create a wrapper that goes after the card-grid
        var wrapper = document.createElement('div');
        wrapper.className = 'cl-card-chapter-wrapper';
        wrapper.setAttribute('data-pov', povKey);

        // Create expand button
        var expandBtn = document.createElement('button');
        expandBtn.className = 'cl-expand-btn';
        expandBtn.textContent = '\u25B6 ' + povKey.replace(/Góc_Nhìn_/,'').replace(/_/g,' ') + ' — ' + chapters.length + ' chapters';

        // Create chapter panel
        var panel = document.createElement('div');
        panel.className = 'cl-chapter-panel';

        var list = document.createElement('ul');
        list.className = 'cl-chapter-list';

        chapters.forEach(function (ch) {
            var li = document.createElement('li');
            li.className = 'cl-chapter-item';

            var link = document.createElement('a');
            link.href = 'reader.html?file=' + encodeURIComponent(dirPath + ch.filename);
            link.textContent = ch.title;
            li.appendChild(link);

            // Add checkmark
            var chapterPath = dirPath + ch.filename;
            if (window.ChapterLock) {
                window.ChapterLock.createCheckmark(chapterPath, li);
            }

            list.appendChild(li);
        });

        panel.appendChild(list);

        // Toggle behavior
        expandBtn.addEventListener('click', function (e) {
            e.preventDefault();
            e.stopPropagation();
            var expanded = panel.classList.toggle('cl-expanded');
            expandBtn.textContent = (expanded ? '\u25BC ' : '\u25B6 ') + povKey.replace(/Góc_Nhìn_/,'').replace(/_/g,' ') + ' — ' + chapters.length + ' chapters';
        });

        wrapper.appendChild(expandBtn);
        wrapper.appendChild(panel);

        // Insert the wrapper after the card-grid (outside the grid layout)
        // Check if a wrapper for this POV already exists to avoid duplicates
        if (!cardGrid.parentNode.querySelector('.cl-card-chapter-wrapper[data-pov="' + povKey + '"]')) {
            cardGrid.parentNode.insertBefore(wrapper, cardGrid.nextSibling);
        }
    });
}
```

- [ ] **Step 2: Verify in browser**

Open `index.html` locally. Confirm:
- Each POV card with chapters has a "▶ N chapters" button below it
- Clicking the button expands the chapter list with slide animation
- Each chapter has a checkmark area (empty since not logged in)
- Chapter titles link to `reader.html?file=...`
- Clicking again collapses the list
- No JS console errors

- [ ] **Step 3: Commit**

```bash
git add index.html
git commit -m "feat: add expandable chapter lists with lock checkmarks to index page"
```

---

## Chunk 3: Reader Page Integration

### Task 5: Add chapter lock to reader.html MỤC_LỤC view

**Files:**
- Modify: `reader.html`

- [ ] **Step 1: Load chapter-lock.js in reader.html**

In `reader.html`, find the line that loads `scripts/navbar.js` (line 396). Add after it:

```html
<script src="scripts/chapter-lock.js"></script>
```

- [ ] **Step 2: Add auth container injection and initialization**

In the main IIFE of `reader.html` (starts around line 398), add code after the navbar is loaded to inject the auth container and initialize ChapterLock. Find the section where the file is loaded and rendered. After the HTML is inserted into the DOM (after `marked.parse(md)` is applied), add code to inject checkmarks into MỤC_LỤC links.

Two changes are needed:

**Change A:** Add this code at the end of the main IIFE, before the closing `})();`:

```javascript
// ── Chapter Lock Integration ──
function initReaderChapterLock() {
    // Inject auth container into navbar
    var navLinks = document.querySelector('.mn-links');
    if (navLinks) {
        var authLi = document.createElement('li');
        authLi.id = 'chapter-lock-auth';
        authLi.style.cssText = 'display:flex;align-items:center;';
        navLinks.appendChild(authLi);
    }

    if (window.ChapterLock) {
        window.ChapterLock.init();
    }
}

// This function is called AFTER markdown content is rendered (see Change B below)
function injectMucLucCheckmarks() {
    if (!window.ChapterLock) return;

    // Only inject on MỤC_LỤC pages
    var filePath = new URLSearchParams(window.location.search).get('file');
    if (!filePath || filePath.indexOf('MỤC_LỤC') === -1) return;

    var dirPath = filePath.replace(/MỤC_LỤC\.md$/, '');

    // Find all chapter links in the rendered content
    var contentArea = document.querySelector('.wiki-page') || document.body;
    var links = contentArea.querySelectorAll('a[href*="reader.html?file="]');

    links.forEach(function (link) {
        var href = link.getAttribute('href');
        var fileMatch = href.match(/file=([^&]+)/);
        if (!fileMatch) return;
        var chapterFile = decodeURIComponent(fileMatch[1]);

        // Only add checkmarks for chapter files (not other MỤC_LỤC links)
        if (!/Chương_\d+/.test(chapterFile)) return;

        // Wrap link and checkmark in a flex container
        var wrapper = document.createElement('span');
        wrapper.style.cssText = 'display:inline-flex;align-items:center;';
        link.parentNode.insertBefore(wrapper, link);
        wrapper.appendChild(link);

        window.ChapterLock.createCheckmark(chapterFile, wrapper);
    });
}

initReaderChapterLock();
```

**Change B:** Find the `loadWikiMode` function in reader.html (the function that sets `body.className = 'wiki-page'` and inserts rendered HTML). At the END of that function, after the content is in the DOM, add:

```javascript
// Inject chapter lock checkmarks after content is rendered
if (typeof injectMucLucCheckmarks === 'function') {
    injectMucLucCheckmarks();
}
```

This ensures checkmarks are injected only after the markdown links exist in the DOM.

- [ ] **Step 3: Verify in browser**

Open `reader.html?file=Đạo/Chương_Truyện/Nam_Cương/Góc_Nhìn_Lâm_Phong/MỤC_LỤC.md` locally. Confirm:
- Login button appears in navbar
- Each chapter link has a checkmark area next to it
- Checkmarks are read-only (not logged in)
- Opening an individual chapter (not MỤC_LỤC) does NOT show checkmarks
- No JS console errors

- [ ] **Step 4: Commit**

```bash
git add reader.html
git commit -m "feat: add chapter lock checkmarks to reader MỤC_LỤC view"
```

---

## Chunk 4: Agent & CI Protection

### Task 6: Create CLAUDE.md

**Files:**
- Create: `CLAUDE.md`

- [ ] **Step 1: Create CLAUDE.md**

```markdown
# Cố Nguyên Giới — Agent Instructions

## Locked Chapters

Before editing any chapter file in `Đạo/Chương_Truyện/`, check `locked_chapters.json` in the repo root.
If the chapter's file path is listed in `locked_chapters`, DO NOT modify it.
These chapters are approved for publication and must not be changed.
Do NOT modify `locked_chapters.json` itself — it is managed exclusively by the author through the web UI.
```

- [ ] **Step 2: Commit**

```bash
git add CLAUDE.md
git commit -m "feat: add CLAUDE.md with locked chapter instructions for agents"
```

---

### Task 7: Create GitHub Action to protect locked chapters

**Files:**
- Create: `.github/workflows/protect-locked-chapters.yml`

- [ ] **Step 1: Create the workflow**

```yaml
name: Protect Locked Chapters

on:
  pull_request:
    paths:
      - "Đạo/Chương_Truyện/**"

jobs:
  check-locked-chapters:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout base branch
        uses: actions/checkout@v4
        with:
          ref: ${{ github.event.pull_request.base.ref }}

      - name: Check for locked chapter modifications
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          # Get the lock file from the base branch
          if [ ! -f locked_chapters.json ]; then
            echo "No locked_chapters.json found. Skipping check."
            exit 0
          fi

          # Get list of changed files in the PR
          CHANGED_FILES=$(gh pr diff "${{ github.event.pull_request.number }}" --name-only)

          # Check each changed file against locked chapters
          VIOLATIONS=""
          while IFS= read -r locked_path; do
            if echo "$CHANGED_FILES" | grep -qF "$locked_path"; then
              VIOLATIONS="${VIOLATIONS}\n  - ${locked_path}"
            fi
          done < <(python3 -c "
          import json
          with open('locked_chapters.json') as f:
              data = json.load(f)
          for ch in data.get('locked_chapters', []):
              print(ch)
          ")

          if [ -n "$VIOLATIONS" ]; then
            echo "::error::This PR modifies locked chapters that are approved for publication:"
            echo -e "$VIOLATIONS"
            echo ""
            echo "These chapters are locked in locked_chapters.json and must not be changed."
            exit 1
          fi

          echo "No locked chapters were modified. Check passed."
```

- [ ] **Step 2: Commit**

```bash
git add .github/workflows/protect-locked-chapters.yml
git commit -m "feat: add GitHub Action to block PRs modifying locked chapters"
```

---

### Task 8: Update auto-merge.yml to respect status checks

**Files:**
- Modify: `.github/workflows/auto-merge.yml`

- [ ] **Step 1: Update auto-merge to use --auto flag**

Replace the current `auto-merge.yml` content. Change `gh pr merge --merge` to `gh pr merge --auto --merge` so it waits for required status checks (including the locked chapters check) before merging:

```yaml
name: Auto Merge

on:
  pull_request:
    types: [opened, synchronize, reopened]

permissions:
  contents: write
  pull-requests: write

jobs:
  auto-merge:
    runs-on: ubuntu-latest
    if: github.actor == 'google-labs-jules[bot]'
    steps:
      - name: Enable auto-merge for Jules PRs
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: gh pr merge --auto --merge "${{ github.event.pull_request.html_url }}"
```

- [ ] **Step 2: Commit**

```bash
git add .github/workflows/auto-merge.yml
git commit -m "feat: update auto-merge to wait for status checks before merging"
```

---

### Task 9: Manual setup — Branch protection rule

This step requires manual configuration in GitHub Settings.

- [ ] **Step 1: Add branch protection rule**

Go to: GitHub repo → Settings → Branches → Add rule
- Branch name pattern: `main`
- Enable: "Require status checks to pass before merging"
- Add required check: `check-locked-chapters`
- Save

---

### Task 10: Manual setup — GitHub OAuth App + Cloudflare Worker

- [ ] **Step 1: Create GitHub OAuth App**

Go to: GitHub → Settings → Developer Settings → OAuth Apps → New OAuth App
- Application name: `Cố Nguyên Giới Chapter Lock`
- Homepage URL: `https://sampi314.github.io/Obsidian_Novel_v2/`
- Authorization callback URL: `https://sampi314.github.io/Obsidian_Novel_v2/`
- Note the **Client ID**

- [ ] **Step 2: Deploy Cloudflare Worker**

```bash
cd workers/oauth-proxy
npx wrangler login
npx wrangler secret put CLIENT_ID    # paste the Client ID from step 1
npx wrangler secret put CLIENT_SECRET # paste the Client Secret from step 1
npx wrangler deploy
```

Note the Worker URL (e.g., `https://co-nguyen-oauth-proxy.YOUR_ACCOUNT.workers.dev`)

- [ ] **Step 3: Update chapter-lock.js config**

In `scripts/chapter-lock.js`, replace the placeholder values:
- `YOUR_CLIENT_ID` → the actual Client ID from step 1
- `https://YOUR_WORKER.workers.dev` → the actual Worker URL from step 2

- [ ] **Step 4: Commit and push**

```bash
git add scripts/chapter-lock.js
git commit -m "feat: configure OAuth credentials for chapter lock system"
git push origin main
```

- [ ] **Step 5: End-to-end test**

1. Visit `https://sampi314.github.io/Obsidian_Novel_v2/`
2. Click "Login with GitHub" → authorize → redirected back
3. Expand a POV card → click a checkmark → confirm it commits to `locked_chapters.json`
4. Verify the checkmark shows ✓ after commit
5. Refresh page → confirm lock state persists
6. Visit a MỤC_LỤC page in the reader → confirm checkmarks appear there too
7. Wait 3 hours (or manually change the timestamp in localStorage) → confirm session expires
8. Create a test PR that modifies a locked chapter → confirm the GitHub Action blocks it
