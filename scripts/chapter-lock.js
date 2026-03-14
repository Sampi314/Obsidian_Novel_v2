// scripts/chapter-lock.js
(function () {
  'use strict';

  // ── Config ──
  var CONFIG = {
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

  // ── PAT Login ──
  async function promptForToken() {
    var token = prompt(
      'Enter your GitHub Personal Access Token\n'
      + '(Settings → Developer Settings → Personal Access Tokens → Generate)\n'
      + 'Needs "public_repo" scope.'
    );
    if (!token || !token.trim()) return;
    token = token.trim();

    try {
      var resp = await fetch('https://api.github.com/user', {
        headers: { 'Authorization': 'Bearer ' + token },
      });
      if (!resp.ok) {
        alert('Invalid token. Please check and try again.');
        return;
      }
      var user = await resp.json();
      if (user.login !== CONFIG.ALLOWED_USER) {
        alert('Access denied. Only the repo owner can lock chapters.');
        return;
      }

      saveSession(token, user.avatar_url, user.login);
      renderAuthUI();
      renderAllCheckmarks();
    } catch (err) {
      console.error('Token validation error:', err);
      alert('Failed to validate token. Check your network connection.');
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
        loginBtn.textContent = 'Login (PAT)';
        loginBtn.addEventListener('click', promptForToken);
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

      // Load lock data (public read, no token needed)
      try {
        await fetchLockFile(getToken());
      } catch (err) {
        console.error('Failed to load lock file:', err);
        _lockCache = { chapters: [], sha: null };
      }

      renderAuthUI();
      startExpiryTimer();
    },
    getToken: getToken,
    isChapterLocked: isChapterLocked,
    createCheckmark: createCheckmark,
    fetchLockFile: fetchLockFile,
    renderAuthUI: renderAuthUI,
    renderAllCheckmarks: renderAllCheckmarks,
  };
})();
