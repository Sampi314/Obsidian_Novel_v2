/* ═══════════════════════════════════════════
   CỐ NGUYÊN GIỚI — Floating TTS Player
   VieNeu-TTS with Voice Cloning
   Sticky bottom bar with voice selection & settings
   ═══════════════════════════════════════════ */

(function() {
    'use strict';

    // ── Configuration ──
    var DEFAULT_VIENEU_URL = 'http://127.0.0.1:8001';

    // VieNeu-TTS voices
    var VIENEU_VOICES = [
        { id: 'Binh',  name: 'Bình (Nam Bắc)' },
        { id: 'Tuyen', name: 'Tuyên (Nam Bắc)' },
        { id: 'Vinh',  name: 'Vĩnh (Nam Nam)' },
        { id: 'Doan',  name: 'Đoan (Nữ Nam)' },
        { id: 'Ly',    name: 'Ly (Nữ Bắc)' },
        { id: 'Ngoc',  name: 'Ngọc (Nữ Bắc)' },
    ];

    // ── State ──
    var state = {
        elements: [],
        originalHTMLs: {},
        currentIndex: 0,
        playing: false,
        paused: false,
        speed: parseFloat(localStorage.getItem('tts_speed') || '1.0'),
        voiceId: localStorage.getItem('tts_voice') || 'Binh',
        vieneuUrl: localStorage.getItem('tts_vieneu_url') || DEFAULT_VIENEU_URL,
        audioEl: null,
        vieneuAvailable: null,   // null = untested
        settingsOpen: false,
        clonedVoices: JSON.parse(localStorage.getItem('tts_cloned_voices') || '[]'),
        pendingCloneAudio: null, // temp: holds FileReader result before save
    };

    // ── Build Floating Player UI ──
    function buildPlayer() {
        var bar = document.createElement('div');
        bar.id = 'tts-bar';
        bar.className = 'tts-bar';

        bar.innerHTML = [
            '<div class="tts-bar-inner">',
            '  <div class="tts-controls">',
            '    <button class="tts-btn tts-btn-play" id="tts-play" title="Phát">',
            '      <svg width="16" height="16" viewBox="0 0 16 16" fill="currentColor"><polygon points="3,1 13,8 3,15"/></svg>',
            '    </button>',
            '    <button class="tts-btn tts-btn-pause" id="tts-pause" title="Tạm dừng" style="display:none">',
            '      <svg width="16" height="16" viewBox="0 0 16 16" fill="currentColor"><rect x="2" y="1" width="4" height="14"/><rect x="10" y="1" width="4" height="14"/></svg>',
            '    </button>',
            '    <button class="tts-btn tts-btn-stop" id="tts-stop" title="Dừng" style="display:none">',
            '      <svg width="14" height="14" viewBox="0 0 14 14" fill="currentColor"><rect x="1" y="1" width="12" height="12" rx="1"/></svg>',
            '    </button>',
            '  </div>',
            '  <div class="tts-progress">',
            '    <div class="tts-progress-bar" id="tts-progress-bar"></div>',
            '    <span class="tts-progress-text" id="tts-progress-text">---</span>',
            '  </div>',
            '  <div class="tts-speed">',
            '    <button class="tts-btn-sm" id="tts-speed-down" title="Giảm tốc">-</button>',
            '    <span class="tts-speed-val" id="tts-speed-val">' + state.speed.toFixed(1) + 'x</span>',
            '    <button class="tts-btn-sm" id="tts-speed-up" title="Tăng tốc">+</button>',
            '  </div>',
            '  <div class="tts-voice-wrap">',
            '    <select class="tts-voice-select" id="tts-voice-select"></select>',
            '  </div>',
            '  <button class="tts-btn tts-btn-settings" id="tts-settings" title="Cài đặt VieNeu-TTS">',
            '    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83-2.83l.06-.06A1.65 1.65 0 0 0 4.68 15a1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 2.83-2.83l.06.06A1.65 1.65 0 0 0 9 4.68a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 2.83l-.06.06A1.65 1.65 0 0 0 19.4 9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>',
            '  </button>',
            '  <button class="tts-btn tts-btn-close" id="tts-close" title="Đóng">',
            '    <svg width="12" height="12" viewBox="0 0 12 12" fill="currentColor"><path d="M1 1l10 10M11 1L1 11" stroke="currentColor" stroke-width="2" fill="none"/></svg>',
            '  </button>',
            '</div>',
            // Settings panel (hidden by default)
            '<div class="tts-settings-panel" id="tts-settings-panel">',
            '  <div class="tts-settings-inner">',
            '    <div class="tts-settings-header">',
            '      <span class="tts-settings-title">Cài Đặt VieNeu-TTS</span>',
            '      <span class="tts-settings-badge" id="tts-vieneu-status"></span>',
            '    </div>',
            '    <div class="tts-settings-row">',
            '      <label class="tts-settings-label">Server URL</label>',
            '      <input class="tts-settings-input" id="tts-vieneu-url" type="text" ',
            '        value="' + state.vieneuUrl + '" placeholder="http://127.0.0.1:8001"/>',
            '    </div>',
            '    <div class="tts-settings-row">',
            '      <button class="tts-settings-btn" id="tts-vieneu-test">Kiểm Tra Kết Nối</button>',
            '      <button class="tts-settings-btn tts-settings-btn-save" id="tts-vieneu-save">Lưu</button>',
            '    </div>',
            '    <div class="tts-settings-help">',
            '      Chạy VieNeu-TTS local: <code>uv run vieneu-web</code><br>',
            '      Repo: <a href="https://github.com/pnnbao97/VieNeu-TTS" target="_blank">github.com/pnnbao97/VieNeu-TTS</a>',
            '    </div>',
            '    <div class="tts-clone-divider"></div>',
            '    <div class="tts-clone-section">',
            '      <div class="tts-settings-header">',
            '        <span class="tts-settings-title">Giọng Nhân Vật — Voice Cloning</span>',
            '        <span class="tts-clone-hint">(3-5 giây mẫu giọng)</span>',
            '      </div>',
            '      <div class="tts-settings-row">',
            '        <label class="tts-settings-label">Tên Nhân Vật</label>',
            '        <input class="tts-settings-input" id="tts-clone-name" type="text" placeholder="VD: Diệp Thanh Y"/>',
            '      </div>',
            '      <div class="tts-settings-row">',
            '        <label class="tts-settings-label">Mẫu Giọng</label>',
            '        <input type="file" id="tts-clone-audio" accept="audio/*" class="tts-settings-file"/>',
            '      </div>',
            '      <div class="tts-settings-row">',
            '        <label class="tts-settings-label">Lời Mẫu</label>',
            '        <input class="tts-settings-input" id="tts-clone-text" type="text" placeholder="Nội dung lời nói trong đoạn mẫu giọng"/>',
            '      </div>',
            '      <div class="tts-settings-row">',
            '        <button class="tts-settings-btn tts-settings-btn-save" id="tts-clone-save">Tạo Giọng Nhân Vật</button>',
            '        <span class="tts-clone-status" id="tts-clone-status"></span>',
            '      </div>',
            '      <div id="tts-clone-list" class="tts-clone-list"></div>',
            '    </div>',
            '  </div>',
            '</div>',
        ].join('\n');

        document.body.appendChild(bar);

        // Populate voice select
        var sel = document.getElementById('tts-voice-select');
        var optgroup = document.createElement('optgroup');
        optgroup.label = 'VieNeu-TTS';
        VIENEU_VOICES.forEach(function(v) {
            var opt = document.createElement('option');
            opt.value = v.id;
            opt.textContent = v.name;
            if (v.id === state.voiceId) opt.selected = true;
            optgroup.appendChild(opt);
        });
        sel.appendChild(optgroup);

        // Add cloned character voices optgroup
        populateClonedVoicesInSelect();

        // ── Event Listeners ──
        document.getElementById('tts-play').addEventListener('click', handlePlay);
        document.getElementById('tts-pause').addEventListener('click', handlePause);
        document.getElementById('tts-stop').addEventListener('click', handleStop);
        document.getElementById('tts-speed-down').addEventListener('click', function() { changeSpeed(-0.1); });
        document.getElementById('tts-speed-up').addEventListener('click', function() { changeSpeed(0.1); });
        document.getElementById('tts-close').addEventListener('click', function() {
            handleStop();
            bar.classList.remove('tts-bar-visible');
        });
        sel.addEventListener('change', function() {
            state.voiceId = sel.value;
            localStorage.setItem('tts_voice', state.voiceId);
            if (state.playing && !state.paused) {
                cancelCurrentAudio();
                readCurrentChunk();
            }
        });

        // Settings panel
        document.getElementById('tts-settings').addEventListener('click', toggleSettings);
        document.getElementById('tts-vieneu-test').addEventListener('click', testVieneuConnection);
        document.getElementById('tts-vieneu-save').addEventListener('click', saveVieneuSettings);

        // Voice cloning
        document.getElementById('tts-clone-save').addEventListener('click', saveClonedVoice);
        document.getElementById('tts-clone-audio').addEventListener('change', handleCloneAudioSelect);

        // Render existing cloned voices
        renderClonedVoiceList();

        return bar;
    }

    // ── Settings Panel ──

    function toggleSettings() {
        var panel = document.getElementById('tts-settings-panel');
        state.settingsOpen = !state.settingsOpen;
        panel.classList.toggle('tts-settings-visible', state.settingsOpen);
    }

    function testVieneuConnection() {
        var urlInput = document.getElementById('tts-vieneu-url');
        var badge = document.getElementById('tts-vieneu-status');
        var testBtn = document.getElementById('tts-vieneu-test');
        var testUrl = urlInput.value.replace(/\/+$/, '');

        badge.textContent = 'Đang kiểm tra...';
        badge.className = 'tts-settings-badge tts-badge-pending';
        testBtn.disabled = true;

        fetch(testUrl + '/voices', { mode: 'cors' })
            .then(function(r) {
                if (!r.ok) throw new Error('HTTP ' + r.status);
                return r.json();
            })
            .then(function(data) {
                badge.textContent = 'Kết nối thành công';
                badge.className = 'tts-settings-badge tts-badge-ok';
                state.vieneuAvailable = true;
                // Update voice list if server returned voices
                if (data && data.voices) {
                    updateVieneuVoicesFromServer(data.voices);
                }
            })
            .catch(function() {
                badge.textContent = 'Không kết nối được';
                badge.className = 'tts-settings-badge tts-badge-error';
                state.vieneuAvailable = false;
            })
            .finally(function() {
                testBtn.disabled = false;
            });
    }

    function saveVieneuSettings() {
        var urlInput = document.getElementById('tts-vieneu-url');
        state.vieneuUrl = urlInput.value.replace(/\/+$/, '');
        localStorage.setItem('tts_vieneu_url', state.vieneuUrl);

        var badge = document.getElementById('tts-vieneu-status');
        badge.textContent = 'Đã lưu';
        badge.className = 'tts-settings-badge tts-badge-ok';
        setTimeout(function() {
            badge.textContent = '';
            badge.className = 'tts-settings-badge';
        }, 2000);
    }

    function updateVieneuVoicesFromServer(serverVoices) {
        // serverVoices is an array of voice objects from VieNeu-TTS /voices endpoint
        // Update the dropdown if we got new voices
        if (!Array.isArray(serverVoices) || serverVoices.length === 0) return;

        var sel = document.getElementById('tts-voice-select');
        var vieneuGroup = sel.querySelector('optgroup[label*="VieNeu"]');
        if (!vieneuGroup) return;

        // Clear existing options
        while (vieneuGroup.firstChild) vieneuGroup.removeChild(vieneuGroup.firstChild);

        // Re-populate from server
        serverVoices.forEach(function(v) {
            var opt = document.createElement('option');
            opt.value = v.id || v.name;
            opt.textContent = v.label || v.name || v.id;
            if (opt.value === state.voiceId) opt.selected = true;
            vieneuGroup.appendChild(opt);
        });
    }

    // ── Voice Cloning ──

    function handleCloneAudioSelect(e) {
        var file = e.target.files && e.target.files[0];
        if (!file) { state.pendingCloneAudio = null; return; }

        var reader = new FileReader();
        reader.onload = function() {
            // Store as base64 (strip data URL prefix)
            var base64 = reader.result.split(',')[1];
            state.pendingCloneAudio = {
                base64: base64,
                type: file.type || 'audio/wav',
                name: file.name,
                size: file.size,
            };
        };
        reader.readAsDataURL(file);
    }

    function saveClonedVoice() {
        var nameInput = document.getElementById('tts-clone-name');
        var textInput = document.getElementById('tts-clone-text');
        var statusEl = document.getElementById('tts-clone-status');

        var voiceName = nameInput.value.trim();
        var refText = textInput.value.trim();

        if (!voiceName) {
            statusEl.textContent = 'Cần nhập tên nhân vật';
            statusEl.className = 'tts-clone-status tts-badge-error';
            return;
        }
        if (!state.pendingCloneAudio) {
            statusEl.textContent = 'Cần chọn file mẫu giọng';
            statusEl.className = 'tts-clone-status tts-badge-error';
            return;
        }
        if (!refText) {
            statusEl.textContent = 'Cần nhập lời mẫu';
            statusEl.className = 'tts-clone-status tts-badge-error';
            return;
        }

        var voiceId = 'clone_' + Date.now();
        var profile = {
            id: voiceId,
            name: voiceName,
            audioBase64: state.pendingCloneAudio.base64,
            audioType: state.pendingCloneAudio.type,
            refText: refText,
            createdAt: new Date().toISOString(),
        };

        state.clonedVoices.push(profile);
        localStorage.setItem('tts_cloned_voices', JSON.stringify(state.clonedVoices));

        // Clear inputs
        nameInput.value = '';
        textInput.value = '';
        document.getElementById('tts-clone-audio').value = '';
        state.pendingCloneAudio = null;

        statusEl.textContent = 'Đã tạo: ' + voiceName;
        statusEl.className = 'tts-clone-status tts-badge-ok';
        setTimeout(function() {
            statusEl.textContent = '';
            statusEl.className = 'tts-clone-status';
        }, 3000);

        renderClonedVoiceList();
        populateClonedVoicesInSelect();
    }

    function deleteClonedVoice(voiceId) {
        state.clonedVoices = state.clonedVoices.filter(function(v) { return v.id !== voiceId; });
        localStorage.setItem('tts_cloned_voices', JSON.stringify(state.clonedVoices));

        // Reset voice selection if deleted voice was active
        if (state.voiceId === voiceId) {
            state.voiceId = 'Binh';
            localStorage.setItem('tts_voice', state.voiceId);
            var sel = document.getElementById('tts-voice-select');
            if (sel) sel.value = state.voiceId;
        }

        renderClonedVoiceList();
        populateClonedVoicesInSelect();
    }

    function renderClonedVoiceList() {
        var listEl = document.getElementById('tts-clone-list');
        if (!listEl) return;

        if (state.clonedVoices.length === 0) {
            listEl.innerHTML = '<span class="tts-clone-empty">Chưa có giọng nhân vật nào</span>';
            return;
        }

        var html = state.clonedVoices.map(function(v) {
            return '<div class="tts-clone-item" data-id="' + v.id + '">' +
                '<span class="tts-clone-item-name">' + v.name + '</span>' +
                '<span class="tts-clone-item-ref">' + v.refText.substring(0, 30) + (v.refText.length > 30 ? '…' : '') + '</span>' +
                '<button class="tts-clone-item-del" data-id="' + v.id + '" title="Xóa">×</button>' +
                '</div>';
        }).join('');

        listEl.innerHTML = html;

        // Attach delete handlers
        listEl.querySelectorAll('.tts-clone-item-del').forEach(function(btn) {
            btn.addEventListener('click', function(e) {
                e.stopPropagation();
                deleteClonedVoice(btn.getAttribute('data-id'));
            });
        });
    }

    function populateClonedVoicesInSelect() {
        var sel = document.getElementById('tts-voice-select');
        if (!sel) return;

        // Remove existing clone optgroup if any
        var existing = sel.querySelector('optgroup[label*="Nhân Vật"]');
        if (existing) sel.removeChild(existing);

        if (state.clonedVoices.length === 0) return;

        var optgroup = document.createElement('optgroup');
        optgroup.label = 'Giọng Nhân Vật (Clone)';

        state.clonedVoices.forEach(function(v) {
            var opt = document.createElement('option');
            opt.value = v.id;
            opt.textContent = v.name;
            if (v.id === state.voiceId) opt.selected = true;
            optgroup.appendChild(opt);
        });

        // Append after VieNeu voices
        sel.appendChild(optgroup);
    }

    // ── Inject CSS ──
    function injectCSS() {
        var style = document.createElement('style');
        style.textContent = [
            '.tts-bar{',
            '  position:fixed;bottom:0;left:0;width:100%;z-index:7500;',
            '  transform:translateY(100%);',
            '  transition:transform .4s cubic-bezier(.25,.46,.45,.94);',
            '  pointer-events:none;',
            '}',
            '.tts-bar.tts-bar-visible{transform:translateY(0);pointer-events:auto;}',
            '.tts-bar-inner{',
            '  display:flex;align-items:center;gap:10px;',
            '  padding:10px clamp(12px,3vw,24px);',
            '  background:rgba(12,15,20,.95);',
            '  backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);',
            '  border-top:1px solid rgba(212,165,116,.08);',
            '  box-shadow:0 -4px 24px rgba(0,0,0,.4);',
            '  font-family:"Cormorant Garamond","Georgia",serif;',
            '}',
            '[data-theme="bach-tuyet"] .tts-bar-inner{',
            '  background:rgba(245,240,232,.95);',
            '  border-top-color:rgba(138,96,32,.1);',
            '  box-shadow:0 -4px 24px rgba(42,36,32,.1);',
            '}',
            /* Controls */
            '.tts-controls{display:flex;gap:6px;flex-shrink:0;}',
            '.tts-btn{',
            '  width:36px;height:36px;border-radius:50%;border:1px solid rgba(212,165,116,.15);',
            '  background:rgba(212,165,116,.06);color:var(--accent,#d4a574);',
            '  cursor:pointer;display:flex;align-items:center;justify-content:center;',
            '  transition:all .25s ease;',
            '}',
            '.tts-btn:hover{background:rgba(212,165,116,.14);border-color:var(--accent,#d4a574);transform:scale(1.08);}',
            '.tts-btn-play{background:rgba(212,165,116,.12);}',
            '.tts-btn-close{width:28px;height:28px;border:none;background:none;color:var(--muted,#6a7080);flex-shrink:0;}',
            '.tts-btn-close:hover{color:var(--accent,#d4a574);}',
            '.tts-btn-settings{width:30px;height:30px;border:none;background:none;color:var(--muted,#6a7080);flex-shrink:0;}',
            '.tts-btn-settings:hover{color:var(--accent,#d4a574);}',
            '.tts-btn-settings.tts-settings-active{color:var(--accent,#d4a574);}',
            /* Progress */
            '.tts-progress{',
            '  flex:1;min-width:0;display:flex;align-items:center;gap:10px;',
            '}',
            '.tts-progress-bar{',
            '  flex:1;height:3px;background:rgba(212,165,116,.08);border-radius:2px;position:relative;overflow:hidden;',
            '}',
            '.tts-progress-bar::after{',
            '  content:"";position:absolute;top:0;left:0;height:100%;width:var(--pct,0%);',
            '  background:linear-gradient(to right,var(--accent-dim,#9b7a52),var(--accent,#d4a574));',
            '  border-radius:2px;transition:width .3s ease;',
            '}',
            '.tts-progress-text{',
            '  font-size:.72rem;color:var(--muted,#6a7080);white-space:nowrap;min-width:50px;text-align:center;',
            '}',
            /* Speed */
            '.tts-speed{display:flex;align-items:center;gap:4px;flex-shrink:0;}',
            '.tts-btn-sm{',
            '  width:26px;height:26px;border-radius:4px;border:1px solid rgba(212,165,116,.1);',
            '  background:none;color:var(--accent-dim,#9b7a52);cursor:pointer;',
            '  font-size:.9rem;font-weight:700;display:flex;align-items:center;justify-content:center;',
            '  transition:all .2s ease;font-family:monospace;',
            '}',
            '.tts-btn-sm:hover{background:rgba(212,165,116,.08);color:var(--accent,#d4a574);}',
            '.tts-speed-val{font-size:.75rem;color:var(--accent,#d4a574);min-width:32px;text-align:center;font-weight:600;}',
            /* Voice Select */
            '.tts-voice-wrap{flex-shrink:0;}',
            '.tts-voice-select{',
            '  padding:5px 8px;border-radius:3px;',
            '  border:1px solid rgba(212,165,116,.12);',
            '  background:rgba(21,26,34,.9);color:var(--text,#e8e0d4);',
            '  font-family:"Cormorant Garamond","Georgia",serif;font-size:.75rem;',
            '  cursor:pointer;outline:none;',
            '}',
            '[data-theme="bach-tuyet"] .tts-voice-select{background:rgba(238,231,220,.9);color:#2a2420;}',
            '.tts-voice-select:focus{border-color:var(--accent,#d4a574);}',
            '.tts-voice-select optgroup{font-style:normal;font-weight:700;color:var(--accent-dim,#9b7a52);font-size:.7rem;}',
            /* Highlight */
            '.tts-highlight{',
            '  background:rgba(212,165,116,.15) !important;',
            '  color:var(--accent-bright,#e8be8e) !important;',
            '  border-radius:2px;padding:0 2px;',
            '  transition:background .15s ease;',
            '}',
            '.tts-reading{',
            '  border-left:3px solid var(--accent,#d4a574) !important;',
            '  padding-left:12px !important;',
            '  transition:border-color .3s ease,padding .3s ease;',
            '}',
            /* Settings Panel */
            '.tts-settings-panel{',
            '  max-height:0;overflow:hidden;',
            '  transition:max-height .3s ease;',
            '  background:rgba(8,10,14,.98);',
            '  border-top:1px solid rgba(212,165,116,.06);',
            '}',
            '[data-theme="bach-tuyet"] .tts-settings-panel{background:rgba(240,234,224,.98);}',
            '.tts-settings-panel.tts-settings-visible{max-height:520px;}',
            '.tts-settings-inner{',
            '  padding:12px clamp(12px,3vw,24px);',
            '  display:flex;flex-direction:column;gap:8px;',
            '}',
            '.tts-settings-header{display:flex;align-items:center;gap:10px;}',
            '.tts-settings-title{font-size:.8rem;color:var(--accent,#d4a574);font-weight:600;font-family:"Cormorant Garamond","Georgia",serif;}',
            '.tts-settings-badge{font-size:.65rem;padding:2px 8px;border-radius:10px;}',
            '.tts-badge-ok{background:rgba(80,200,120,.15);color:#50c878;}',
            '.tts-badge-error{background:rgba(220,60,60,.15);color:#dc3c3c;}',
            '.tts-badge-pending{background:rgba(212,165,116,.1);color:var(--accent,#d4a574);}',
            '.tts-settings-row{display:flex;gap:8px;align-items:center;}',
            '.tts-settings-label{font-size:.72rem;color:var(--muted,#6a7080);min-width:70px;font-family:"Cormorant Garamond","Georgia",serif;}',
            '.tts-settings-input{',
            '  flex:1;padding:5px 8px;border-radius:3px;font-size:.72rem;',
            '  border:1px solid rgba(212,165,116,.12);',
            '  background:rgba(21,26,34,.9);color:var(--text,#e8e0d4);',
            '  font-family:monospace;outline:none;',
            '}',
            '[data-theme="bach-tuyet"] .tts-settings-input{background:rgba(238,231,220,.9);color:#2a2420;}',
            '.tts-settings-input:focus{border-color:var(--accent,#d4a574);}',
            '.tts-settings-btn{',
            '  padding:4px 12px;border-radius:3px;font-size:.7rem;cursor:pointer;',
            '  border:1px solid rgba(212,165,116,.15);',
            '  background:rgba(212,165,116,.06);color:var(--accent,#d4a574);',
            '  font-family:"Cormorant Garamond","Georgia",serif;transition:all .2s ease;',
            '}',
            '.tts-settings-btn:hover{background:rgba(212,165,116,.14);}',
            '.tts-settings-btn:disabled{opacity:.5;cursor:default;}',
            '.tts-settings-btn-save{background:rgba(212,165,116,.15);font-weight:600;}',
            '.tts-settings-help{font-size:.65rem;color:var(--muted,#6a7080);line-height:1.5;}',
            '.tts-settings-help code{',
            '  background:rgba(212,165,116,.08);padding:1px 4px;border-radius:2px;',
            '  font-family:monospace;font-size:.62rem;',
            '}',
            '.tts-settings-help a{color:var(--accent-dim,#9b7a52);text-decoration:none;}',
            '.tts-settings-help a:hover{text-decoration:underline;}',
            /* Voice Cloning Section */
            '.tts-clone-divider{height:1px;background:rgba(212,165,116,.1);margin:8px 0;}',
            '.tts-clone-hint{font-size:.6rem;color:var(--muted,#6a7080);font-style:italic;}',
            '.tts-settings-file{',
            '  font-size:.68rem;color:var(--muted,#6a7080);',
            '  font-family:"Cormorant Garamond","Georgia",serif;',
            '}',
            '.tts-settings-file::file-selector-button{',
            '  padding:3px 10px;border-radius:3px;font-size:.65rem;cursor:pointer;',
            '  border:1px solid rgba(212,165,116,.15);margin-right:8px;',
            '  background:rgba(212,165,116,.06);color:var(--accent,#d4a574);',
            '  font-family:"Cormorant Garamond","Georgia",serif;',
            '}',
            '.tts-clone-status{font-size:.65rem;padding:2px 8px;border-radius:10px;}',
            '.tts-clone-list{margin-top:6px;display:flex;flex-direction:column;gap:4px;}',
            '.tts-clone-empty{font-size:.62rem;color:var(--muted,#6a7080);font-style:italic;}',
            '.tts-clone-item{',
            '  display:flex;align-items:center;gap:8px;padding:4px 8px;border-radius:3px;',
            '  background:rgba(212,165,116,.04);border:1px solid rgba(212,165,116,.08);',
            '}',
            '.tts-clone-item-name{font-size:.72rem;color:var(--accent,#d4a574);font-weight:600;min-width:80px;}',
            '.tts-clone-item-ref{font-size:.6rem;color:var(--muted,#6a7080);flex:1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;}',
            '.tts-clone-item-del{',
            '  width:20px;height:20px;border:none;background:none;color:var(--muted,#6a7080);',
            '  cursor:pointer;font-size:.9rem;display:flex;align-items:center;justify-content:center;',
            '  border-radius:50%;transition:all .2s ease;flex-shrink:0;',
            '}',
            '.tts-clone-item-del:hover{background:rgba(220,60,60,.15);color:#dc3c3c;}',
            /* Fab trigger button (when bar is hidden) */
            '.tts-fab{',
            '  position:fixed;bottom:20px;right:20px;z-index:7499;',
            '  width:48px;height:48px;border-radius:50%;',
            '  border:1px solid rgba(212,165,116,.15);',
            '  background:rgba(12,15,20,.9);color:var(--accent,#d4a574);',
            '  backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);',
            '  cursor:pointer;display:flex;align-items:center;justify-content:center;',
            '  font-size:1.2rem;',
            '  box-shadow:0 4px 16px rgba(0,0,0,.3);',
            '  transition:all .3s ease;',
            '}',
            '[data-theme="bach-tuyet"] .tts-fab{background:rgba(245,240,232,.9);border-color:rgba(138,96,32,.15);}',
            '.tts-fab:hover{transform:scale(1.1);box-shadow:0 6px 24px rgba(212,165,116,.15);}',
            '.tts-fab.tts-fab-hidden{opacity:0;pointer-events:none;transform:scale(0.8);}',
            /* Responsive */
            '@media(max-width:640px){',
            '  .tts-bar-inner{gap:6px;padding:8px 10px;}',
            '  .tts-btn{width:32px;height:32px;}',
            '  .tts-voice-wrap{display:none;}',
            '  .tts-progress-text{font-size:.65rem;min-width:40px;}',
            '  .tts-speed-val{font-size:.68rem;min-width:28px;}',
            '  .tts-btn-settings{display:none;}',
            '}',
        ].join('\n');
        document.head.appendChild(style);
    }

    // ── Collect Readable Elements ──
    function getReadableElements() {
        var all = document.body.querySelectorAll('p, h1, h2, h3, h4, h5, h6, li, blockquote');
        var readable = [];
        for (var i = 0; i < all.length; i++) {
            var el = all[i];
            if (el.closest('#chapter-navigation')) continue;
            if (el.closest('.tts-bar')) continue;
            if (el.closest('.mn-bar')) continue;
            if (el.offsetParent === null) continue;
            var text = el.innerText.trim();
            if (text.length === 0) continue;
            if (text.includes("Obsidian_Novel_v2")) continue;
            if (text.includes("Mục Lục Tổng Hợp")) continue;
            readable.push(el);
        }
        return readable;
    }

    // ── UI State Updates ──
    function updateUI() {
        var bar = document.getElementById('tts-bar');
        var fab = document.getElementById('tts-fab');
        var btnPlay = document.getElementById('tts-play');
        var btnPause = document.getElementById('tts-pause');
        var btnStop = document.getElementById('tts-stop');

        if (state.playing) {
            bar.classList.add('tts-bar-visible');
            fab.classList.add('tts-fab-hidden');

            if (state.paused) {
                btnPlay.style.display = 'flex';
                btnPause.style.display = 'none';
            } else {
                btnPlay.style.display = 'none';
                btnPause.style.display = 'flex';
            }
            btnStop.style.display = 'flex';
        } else {
            btnPlay.style.display = 'flex';
            btnPause.style.display = 'none';
            btnStop.style.display = 'none';
        }

        // Progress
        var total = state.elements.length || 1;
        var current = Math.min(state.currentIndex + 1, total);
        var pct = (current / total * 100).toFixed(0);
        document.getElementById('tts-progress-text').textContent = current + '/' + total;
        document.getElementById('tts-progress-bar').style.setProperty('--pct', pct + '%');

        // Speed
        document.getElementById('tts-speed-val').textContent = state.speed.toFixed(1) + 'x';
    }

    function highlightElement(el) {
        document.querySelectorAll('.tts-reading').forEach(function(e) {
            e.classList.remove('tts-reading');
        });
        if (el) {
            el.classList.add('tts-reading');
            el.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
    }

    // ── Audio Playback ──

    function cancelCurrentAudio() {
        if (state.audioEl) {
            state.audioEl.pause();
            // Revoke blob URL if exists
            if (state.audioEl._blobUrl) {
                URL.revokeObjectURL(state.audioEl._blobUrl);
            }
            state.audioEl.removeAttribute('src');
            state.audioEl = null;
        }
    }

    // VieNeu-TTS: fetch audio from local server (supports voice cloning)
    function vieneuTTSSpeak(text) {
        return new Promise(function(resolve, reject) {
            var cloneVoice = state.clonedVoices.find(function(v) { return v.id === state.voiceId; });

            var fetchPromise;
            if (cloneVoice) {
                // Voice cloning: POST with FormData (ref_audio + ref_text)
                var formData = new FormData();
                formData.append('text', text);
                formData.append('ref_text', cloneVoice.refText);

                // Convert base64 back to Blob for file upload
                var byteChars = atob(cloneVoice.audioBase64);
                var byteArray = new Uint8Array(byteChars.length);
                for (var i = 0; i < byteChars.length; i++) {
                    byteArray[i] = byteChars.charCodeAt(i);
                }
                var audioBlob = new Blob([byteArray], { type: cloneVoice.audioType || 'audio/wav' });
                formData.append('ref_audio', audioBlob, 'ref.wav');

                fetchPromise = fetch(state.vieneuUrl + '/stream', {
                    method: 'POST',
                    body: formData,
                    mode: 'cors',
                });
            } else {
                // Standard voice: GET request
                var url = state.vieneuUrl + '/stream?' +
                    'text=' + encodeURIComponent(text) +
                    '&voice_id=' + encodeURIComponent(state.voiceId);
                fetchPromise = fetch(url, { mode: 'cors' });
            }

            // Both paths return WAV audio — handle identically
            fetchPromise
                .then(function(response) {
                    if (!response.ok) throw new Error('VieNeu HTTP ' + response.status);
                    return response.blob();
                })
                .then(function(blob) {
                    var blobUrl = URL.createObjectURL(blob);
                    var audio = new Audio();
                    audio._blobUrl = blobUrl; // store for cleanup

                    audio.addEventListener('canplaythrough', function() {
                        resolve(audio);
                    }, { once: true });

                    audio.addEventListener('error', function() {
                        URL.revokeObjectURL(blobUrl);
                        reject(new Error('VieNeu audio playback failed'));
                    }, { once: true });

                    audio.src = blobUrl;
                    audio.load();
                })
                .catch(function(err) {
                    reject(err);
                });
        });
    }

    function readCurrentChunk() {
        if (!state.playing || state.paused) return;
        if (state.currentIndex >= state.elements.length) {
            handleStop();
            var nextUrl = window.nextChapterUrl || '#';
            if (nextUrl && nextUrl !== '#') {
                var sep = nextUrl.includes('?') ? '&' : '?';
                window.location.href = nextUrl + sep + 'autoplay=true';
            }
            return;
        }

        var el = state.elements[state.currentIndex];
        var text = el.innerText.trim();

        highlightElement(el);
        updateUI();

        vieneuTTSSpeak(text).then(function(audio) {
            state.vieneuAvailable = true;
            state.audioEl = audio;
            audio.addEventListener('ended', onChunkEnd);
            audio.play();
        }).catch(function(err) {
            console.error('VieNeu-TTS error:', err.message);
            state.vieneuAvailable = false;
            // Skip chunk on error rather than silently stall
            onChunkEnd();
        });
    }

    function onChunkEnd() {
        if (!state.playing || state.paused) return;
        var el = state.elements[state.currentIndex];
        if (el) el.classList.remove('tts-reading');

        state.currentIndex++;
        state.audioEl = null;

        setTimeout(function() {
            if (state.playing && !state.paused) {
                readCurrentChunk();
            }
        }, 80);
    }

    // ── Handlers ──

    function handlePlay() {
        if (state.paused) {
            state.paused = false;
            if (state.audioEl) {
                state.audioEl.play();
            } else {
                readCurrentChunk();
            }
            updateUI();
            return;
        }

        if (state.elements.length === 0) {
            state.elements = getReadableElements();
        }
        if (state.currentIndex >= state.elements.length) {
            state.currentIndex = 0;
        }

        state.playing = true;
        state.paused = false;
        updateUI();
        readCurrentChunk();
    }

    function handlePause() {
        state.paused = true;
        if (state.audioEl) {
            state.audioEl.pause();
        }
        updateUI();
    }

    function handleStop() {
        state.playing = false;
        state.paused = false;
        cancelCurrentAudio();

        document.querySelectorAll('.tts-reading').forEach(function(e) {
            e.classList.remove('tts-reading');
        });

        state.currentIndex = 0;

        var bar = document.getElementById('tts-bar');
        var fab = document.getElementById('tts-fab');
        if (bar) bar.classList.remove('tts-bar-visible');
        if (fab) fab.classList.remove('tts-fab-hidden');

        // Close settings if open
        var panel = document.getElementById('tts-settings-panel');
        if (panel) panel.classList.remove('tts-settings-visible');
        state.settingsOpen = false;

        updateUI();
    }

    function changeSpeed(delta) {
        state.speed = Math.max(0.5, Math.min(2.5, state.speed + delta));
        state.speed = Math.round(state.speed * 10) / 10;
        localStorage.setItem('tts_speed', state.speed.toFixed(1));
        updateUI();

        if (state.playing && !state.paused) {
            cancelCurrentAudio();
            readCurrentChunk();
        }
    }

    // ── FAB (Floating Action Button) ──
    function buildFab() {
        var fab = document.createElement('button');
        fab.id = 'tts-fab';
        fab.className = 'tts-fab';
        fab.title = 'Nghe Chương';
        fab.innerHTML = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="5,3 19,12 5,21" fill="currentColor"/></svg>';
        fab.addEventListener('click', function() {
            var bar = document.getElementById('tts-bar');
            bar.classList.add('tts-bar-visible');
            fab.classList.add('tts-fab-hidden');
            handlePlay();
        });
        document.body.appendChild(fab);
    }

    // ── Expose for click-to-read on paragraphs ──
    function setupClickToRead() {
        state.elements = getReadableElements();
        state.elements.forEach(function(el, idx) {
            el.style.cursor = 'pointer';
            el.title = 'Nhấn để đọc từ đây';
            el.addEventListener('click', function(e) {
                if (!state.playing) {
                    state.currentIndex = idx;
                    var bar = document.getElementById('tts-bar');
                    var fab = document.getElementById('tts-fab');
                    if (bar) bar.classList.add('tts-bar-visible');
                    if (fab) fab.classList.add('tts-fab-hidden');
                    handlePlay();
                }
            });
        });
    }

    // ── Also expose globally for navigation.js backward compat ──
    window.startReading = handlePlay;
    window.pauseReading = handlePause;
    window.resumeReading = function() { if (state.paused) handlePlay(); };
    window.stopReading = handleStop;
    window.increaseSpeed = function() { changeSpeed(0.1); };
    window.decreaseSpeed = function() { changeSpeed(-0.1); };

    // ── Initialize ──
    function init() {
        // Clean up stale voice IDs from removed engines (Edge/native)
        var validIds = VIENEU_VOICES.map(function(v) { return v.id; })
            .concat(state.clonedVoices.map(function(v) { return v.id; }));
        if (validIds.indexOf(state.voiceId) === -1) {
            state.voiceId = 'Binh';
            localStorage.setItem('tts_voice', 'Binh');
        }

        injectCSS();
        buildPlayer();
        buildFab();
        setupClickToRead();
        updateUI();

        // Probe VieNeu-TTS availability silently on load
        fetch(state.vieneuUrl + '/voices', { mode: 'cors' })
            .then(function(r) { return r.ok ? r.json() : Promise.reject(); })
            .then(function() { state.vieneuAvailable = true; })
            .catch(function() { state.vieneuAvailable = null; }); // null = unknown, will try on first use

        // Auto-play if param present
        var urlParams = new URLSearchParams(window.location.search);
        if (urlParams.get('autoplay') === 'true') {
            setTimeout(function() {
                var bar = document.getElementById('tts-bar');
                var fab = document.getElementById('tts-fab');
                bar.classList.add('tts-bar-visible');
                fab.classList.add('tts-fab-hidden');
                handlePlay();
            }, 1000);
        }
    }

    if (document.readyState === 'complete') {
        init();
    } else {
        window.addEventListener('load', init);
    }

    // Cleanup on leave
    window.addEventListener('beforeunload', function() {
        state.playing = false;
        cancelCurrentAudio();
    });
})();
