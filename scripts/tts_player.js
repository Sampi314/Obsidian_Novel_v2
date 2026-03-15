/* ═══════════════════════════════════════════
   CỐ NGUYÊN GIỚI — Floating TTS Player
   Web Speech API (browser-native, always works)
   + optional Edge TTS local server for HQ voices
   Sticky bottom bar with voice selection
   ═══════════════════════════════════════════ */

(function() {
    'use strict';

    // ── Configuration ──
    var EDGE_TTS_API = 'http://127.0.0.1:5050/tts';
    var edgeAvailable = false; // probed on init

    var EDGE_VOICES = [
        { id: 'vi-VN-HoaiMyNeural',  name: 'HoaiMy (Nữ)' },
        { id: 'vi-VN-NamMinhNeural', name: 'NamMinh (Nam)' },
    ];

    // ── State ──
    var state = {
        elements: [],
        currentIndex: 0,
        playing: false,
        paused: false,
        speed: parseFloat(localStorage.getItem('tts_speed') || '1.0'),
        voiceId: localStorage.getItem('tts_voice') || 'vi-VN-HoaiMyNeural',
        audioEl: null,
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
            '  <button class="tts-btn tts-btn-close" id="tts-close" title="Đóng">',
            '    <svg width="12" height="12" viewBox="0 0 12 12" fill="currentColor"><path d="M1 1l10 10M11 1L1 11" stroke="currentColor" stroke-width="2" fill="none"/></svg>',
            '  </button>',
            '</div>',
        ].join('\n');

        document.body.appendChild(bar);

        // Voice select populated later by populateVoices()
        var sel = document.getElementById('tts-voice-select');

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

        return bar;
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
            /* Highlight */
            '.tts-reading{',
            '  border-left:3px solid var(--accent,#d4a574) !important;',
            '  padding-left:12px !important;',
            '  transition:border-color .3s ease,padding .3s ease;',
            '}',
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
            state.audioEl.removeAttribute('src');
            state.audioEl = null;
        }
        if (window.speechSynthesis) {
            window.speechSynthesis.cancel();
        }
    }

    // Populate the voice dropdown with available browser voices + Edge voices
    function populateVoices() {
        var sel = document.getElementById('tts-voice-select');
        if (!sel) return;

        var prev = state.voiceId;
        sel.innerHTML = '';

        // Add browser Vietnamese voices
        if (window.speechSynthesis) {
            var allVoices = window.speechSynthesis.getVoices();
            for (var i = 0; i < allVoices.length; i++) {
                var v = allVoices[i];
                if (v.lang && v.lang.indexOf('vi') === 0) {
                    var opt = document.createElement('option');
                    opt.value = 'ws:' + v.name;
                    opt.textContent = v.name;
                    if (opt.value === prev) opt.selected = true;
                    sel.appendChild(opt);
                }
            }
        }

        // Add Edge TTS voices (only useful when server is running)
        if (edgeAvailable) {
            EDGE_VOICES.forEach(function(v) {
                var opt = document.createElement('option');
                opt.value = 'edge:' + v.id;
                opt.textContent = v.name + ' ✦';
                if (opt.value === prev) opt.selected = true;
                sel.appendChild(opt);
            });
        }

        // If saved voice not found, select first available
        if (sel.selectedIndex === -1 && sel.options.length > 0) {
            sel.selectedIndex = 0;
            state.voiceId = sel.value;
            localStorage.setItem('tts_voice', state.voiceId);
        }
    }

    // Probe whether the local Edge TTS server is reachable
    function probeEdgeServer() {
        var ctrl = new AbortController();
        var timer = setTimeout(function() { ctrl.abort(); }, 2000);
        fetch(EDGE_TTS_API + '?text=test&voice=vi-VN-HoaiMyNeural', {
            method: 'HEAD', mode: 'cors', signal: ctrl.signal
        }).then(function() {
            clearTimeout(timer);
            edgeAvailable = true;
            console.log('[TTS] Edge TTS server detected — using high-quality voices');
            populateVoices();
        }).catch(function() {
            clearTimeout(timer);
            edgeAvailable = false;
            console.log('[TTS] Edge TTS server not available — using browser voices');
        });
    }

    // Edge TTS: fetch audio from local server
    function edgeTTSSpeak(text) {
        return new Promise(function(resolve, reject) {
            var edgeVoice = state.voiceId.indexOf('edge:') === 0 ? state.voiceId.slice(5) : state.voiceId;
            var url = EDGE_TTS_API + '?' +
                'text=' + encodeURIComponent(text) +
                '&voice=' + encodeURIComponent(edgeVoice) +
                '&rate=' + encodeURIComponent(((state.speed - 1) * 100).toFixed(0) + '%');

            var audio = new Audio();
            audio.crossOrigin = 'anonymous';

            var timeout = setTimeout(function() {
                audio.removeAttribute('src');
                reject(new Error('Edge TTS timeout'));
            }, 10000);

            audio.addEventListener('canplaythrough', function() {
                clearTimeout(timeout);
                resolve(audio);
            }, { once: true });

            audio.addEventListener('error', function() {
                clearTimeout(timeout);
                reject(new Error('Edge TTS failed'));
            }, { once: true });

            audio.src = url;
            audio.load();
        });
    }

    // Web Speech API: works in all browsers, no server needed
    function webSpeechSpeak(text) {
        return new Promise(function(resolve, reject) {
            if (!window.speechSynthesis) {
                reject(new Error('speechSynthesis not supported'));
                return;
            }

            var utter = new SpeechSynthesisUtterance(text);
            utter.lang = 'vi-VN';
            utter.rate = state.speed;

            // Use selected browser voice, or first Vietnamese voice as fallback
            var voices = window.speechSynthesis.getVoices();
            var targetName = state.voiceId.indexOf('ws:') === 0 ? state.voiceId.slice(3) : '';
            var found = false;
            for (var i = 0; i < voices.length; i++) {
                if (targetName && voices[i].name === targetName) {
                    utter.voice = voices[i];
                    found = true;
                    break;
                }
            }
            if (!found) {
                for (var j = 0; j < voices.length; j++) {
                    if (voices[j].lang && voices[j].lang.indexOf('vi') === 0) {
                        utter.voice = voices[j];
                        found = true;
                        break;
                    }
                }
            }

            if (!found && voices.length === 0) {
                reject(new Error('No voices available — check System Settings → Accessibility → Spoken Content'));
                return;
            }

            var started = false;
            utter.onstart = function() { started = true; };
            utter.onend = function() {
                if (started) {
                    resolve('ended');
                } else {
                    reject(new Error('Speech ended without starting'));
                }
            };
            utter.onerror = function(e) {
                if (e.error === 'canceled') { resolve('canceled'); return; }
                reject(new Error('Speech error: ' + e.error));
            };

            window.speechSynthesis.speak(utter);
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

        var useEdge = edgeAvailable && state.voiceId.indexOf('edge:') === 0;

        function onSpeechFail(err) {
            console.error('[TTS] Failed:', err.message);
            handleStop();
            var pt = document.getElementById('tts-progress-text');
            if (pt) pt.textContent = 'Không có giọng đọc';
        }

        if (useEdge) {
            // Edge TTS with fallback to Web Speech
            edgeTTSSpeak(text).then(function(audio) {
                state.audioEl = audio;
                audio.addEventListener('ended', onChunkEnd);
                audio.play();
            }).catch(function() {
                webSpeechSpeak(text).then(onChunkEnd).catch(onSpeechFail);
            });
        } else {
            // Web Speech API
            webSpeechSpeak(text).then(onChunkEnd).catch(onSpeechFail);
        }
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
            } else if (window.speechSynthesis.paused) {
                window.speechSynthesis.resume();
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
        window.speechSynthesis.pause();
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

    // ── Double-click to read from any paragraph ──
    function setupClickToRead() {
        state.elements = getReadableElements();
        state.elements.forEach(function(el, idx) {
            el.style.cursor = 'pointer';
            el.title = 'Nhấn đúp để đọc từ đây';
            el.addEventListener('dblclick', function() {
                // Stop current playback if any, then start from this paragraph
                if (state.playing) {
                    cancelCurrentAudio();
                    state.playing = false;
                    state.paused = false;
                }
                state.currentIndex = idx;
                var bar = document.getElementById('tts-bar');
                var fab = document.getElementById('tts-fab');
                if (bar) bar.classList.add('tts-bar-visible');
                if (fab) fab.classList.add('tts-fab-hidden');
                handlePlay();
            });
        });
    }

    // ── Global API for navigation.js ──
    window.startReading = handlePlay;
    window.pauseReading = handlePause;
    window.resumeReading = function() { if (state.paused) handlePlay(); };
    window.stopReading = handleStop;
    window.increaseSpeed = function() { changeSpeed(0.1); };
    window.decreaseSpeed = function() { changeSpeed(-0.1); };

    // ── Initialize ──
    function init() {
        // Preload browser voices (some browsers load async)
        if (window.speechSynthesis) {
            window.speechSynthesis.getVoices();
            window.speechSynthesis.onvoiceschanged = function() {
                populateVoices();
            };
        }

        // Probe local Edge TTS server (non-blocking)
        probeEdgeServer();

        injectCSS();
        buildPlayer();
        populateVoices();
        buildFab();
        setupClickToRead();
        updateUI();

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
