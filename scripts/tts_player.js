(function() {
    var synth = window.speechSynthesis;
    var currentUtterance = null;
    var currentIndex = 0;
    var isPaused = false;
    var isStopped = true; // start as true until play is hit
    var currentSpeed = 1.0;

    // Elements to read
    var contentElements = [];

    // Configuration from global scope or data attribute
    // We expect window.nextChapterUrl to be set in the HTML
    var nextChapterUrl = window.nextChapterUrl || "#";

    // Original HTML backup for highlighting
    var originalHTMLs = {};

    function getReadableElements() {
        // Collect all paragraph-like elements in the body
        // Filter out navigation, headers, footers, and specific unwanted text
        var all = document.body.querySelectorAll('p, h1, h2, h3, h4, h5, h6, li, blockquote');
        var readable = [];

        for (var i = 0; i < all.length; i++) {
            var el = all[i];

            // Skip navigation block
            if (el.closest('#chapter-navigation')) continue;

            // Skip invisible elements
            if (el.offsetParent === null) continue;

            var text = el.innerText.trim();
            if (text.length === 0) continue;

            // Skip specific unwanted text
            if (text.includes("Obsidian_Novel_v2")) continue;
            if (text.includes("Mục Lục Tổng Hợp")) continue;

            readable.push(el);
        }
        // Setup click listeners for each readable element
        for (var j = 0; j < readable.length; j++) {
            (function(index) {
                readable[index].style.cursor = "pointer";
                readable[index].title = "Nhấn để đọc từ đây";
                readable[index].addEventListener('click', function() {
                    if (isStopped) {
                        currentIndex = index;
                        startReading();
                    }
                });
            })(j);
        }

        return readable;
    }

    function updateSpeedDisplay() {
        var display = document.getElementById('speed-display');
        if (display) {
            display.textContent = currentSpeed.toFixed(1) + 'x';
        }
    }

    function increaseSpeed() {
        if (currentSpeed < 2.5) {
            currentSpeed += 0.1;
            updateSpeedDisplay();
            restartCurrentUtteranceIfPlaying();
        }
    }

    function decreaseSpeed() {
        if (currentSpeed > 0.5) {
            currentSpeed -= 0.1;
            updateSpeedDisplay();
            restartCurrentUtteranceIfPlaying();
        }
    }

    function restartCurrentUtteranceIfPlaying() {
        if (!isStopped && !isPaused) {
            // Need to restart the current chunk to apply the new speed
            synth.cancel(); // This will trigger onend/onerror, we must handle carefully
            // Actually, canceling triggers onend? Let's stop and restart carefully
            isPaused = true;
            setTimeout(function() {
                isPaused = false;
                // If we were highlighting, we should clean up
                var el = contentElements[currentIndex];
                if (el && originalHTMLs[currentIndex]) {
                    el.innerHTML = originalHTMLs[currentIndex];
                }
                readNextChunk();
            }, 100);
        }
    }

    function startReading() {
        if (synth.speaking && !isPaused) return;

        isStopped = false;

        // Reset controls
        toggleControls('playing');

        if (contentElements.length === 0) {
            contentElements = getReadableElements();
        }

        if (currentIndex >= contentElements.length) {
            currentIndex = 0; // Restart if finished
        }

        readNextChunk();
    }

    function readNextChunk() {
        if (isStopped) return;

        if (currentIndex >= contentElements.length) {
            // Finished reading the chapter
            stopReading();

            // Auto-advance to next chapter if available
            var currentNextChapterUrl = window.nextChapterUrl || "#";
            if (currentNextChapterUrl && currentNextChapterUrl !== "#") {
                // Add autoplay param
                var separator = currentNextChapterUrl.includes('?') ? '&' : '?';
                window.location.href = currentNextChapterUrl + separator + 'autoplay=true';
            }
            return;
        }

        var el = contentElements[currentIndex];

        // Save original HTML
        if (!originalHTMLs[currentIndex]) {
            originalHTMLs[currentIndex] = el.innerHTML;
        }

        el.scrollIntoView({behavior: "smooth", block: "center"});

        var text = el.innerText;

        // Wrap words in spans for highlighting
        var words = text.split(/\s+/);
        var spansHTML = words.map(function(word, idx) {
            return '<span id="tts-word-' + idx + '">' + word + '</span>';
        }).join(' ');

        el.innerHTML = spansHTML;

        var utterance = new SpeechSynthesisUtterance(text);
        utterance.lang = "vi-VN";
        utterance.rate = currentSpeed;

        // Map character index to word index
        var charIndexToWordIndex = [];
        var charCount = 0;
        for (var i = 0; i < words.length; i++) {
            var wordLen = words[i].length;
            for (var c = 0; c < wordLen + 1; c++) { // +1 for space
                charIndexToWordIndex[charCount + c] = i;
            }
            charCount += wordLen + 1;
        }

        var currentWordIndex = -1;

        utterance.onboundary = function(event) {
            if (event.name === 'word') {
                var wordIndex = charIndexToWordIndex[event.charIndex];
                if (wordIndex !== undefined && wordIndex !== currentWordIndex) {
                    // Remove highlight from previous word
                    if (currentWordIndex >= 0) {
                        var prevSpan = document.getElementById('tts-word-' + currentWordIndex);
                        if (prevSpan) {
                            prevSpan.style.backgroundColor = "";
                            prevSpan.style.color = "";
                        }
                    }

                    // Add highlight to current word
                    var currSpan = document.getElementById('tts-word-' + wordIndex);
                    if (currSpan) {
                        currSpan.style.backgroundColor = "#d4af37"; // text-gold
                        currSpan.style.color = "#12100e"; // bg-dark
                        currSpan.style.borderRadius = "2px";
                    }
                    currentWordIndex = wordIndex;
                }
            }
        };

        utterance.onend = function() {
            // Restore original HTML
            el.innerHTML = originalHTMLs[currentIndex];

            if (isStopped || isPaused) return;

            currentIndex++;
            // Small timeout to allow synth status to update
            setTimeout(function() {
                if (!isPaused && !isStopped) {
                     readNextChunk();
                }
            }, 50);
        };

        utterance.onerror = function(event) {
            // Cancel events are normal when we manually cancel
            if (event.error === 'canceled') return;

            if (isStopped) return;

            console.error("Speech error", event);
            el.innerHTML = originalHTMLs[currentIndex];
            currentIndex++;
            readNextChunk();
        };

        currentUtterance = utterance;
        synth.speak(utterance);
    }

    function pauseReading() {
        if (synth.speaking && !isPaused) {
            synth.pause();
            isPaused = true;
            toggleControls('paused');
        }
    }

    function resumeReading() {
        if (isPaused) {
            synth.resume();
            isPaused = false;
            toggleControls('playing');
        } else if (!synth.speaking && currentIndex < contentElements.length) {
            // Resume from stop or clean state
            startReading();
        }
    }

    function stopReading() {
        isStopped = true;
        synth.cancel();
        isPaused = false;

        // Clean up highlights
        if (contentElements.length > 0 && currentIndex < contentElements.length) {
            var el = contentElements[currentIndex];
            if (el && originalHTMLs[currentIndex]) {
                el.innerHTML = originalHTMLs[currentIndex];
            }
        }

        currentIndex = 0;
        toggleControls('stopped');
    }

    function toggleControls(state) {
        var btnPlay = document.getElementById("btn-play");
        var btnPause = document.getElementById("btn-pause");
        var btnResume = document.getElementById("btn-resume");
        var btnStop = document.getElementById("btn-stop");

        if (!btnPlay) return; // Controls not found

        btnPlay.style.display = "none";
        btnPause.style.display = "none";
        btnResume.style.display = "none";
        btnStop.style.display = "none";

        if (state === 'playing') {
            btnPause.style.display = "inline-block";
            btnStop.style.display = "inline-block";
        } else if (state === 'paused') {
            btnResume.style.display = "inline-block";
            btnStop.style.display = "inline-block";
        } else { // stopped
            btnPlay.style.display = "inline-block";
        }
    }

    // Expose functions globally for button onclick handlers
    window.startReading = startReading;
    window.pauseReading = pauseReading;
    window.resumeReading = resumeReading;
    window.stopReading = stopReading;
    window.increaseSpeed = increaseSpeed;
    window.decreaseSpeed = decreaseSpeed;

    // Auto-play check
    window.onload = function() {
        contentElements = getReadableElements(); // Initialize elements early so click works

        // Initial control state
        toggleControls('stopped');

        var urlParams = new URLSearchParams(window.location.search);
        if (urlParams.get('autoplay') === 'true') {
            // Delay slightly to ensure voices are loaded
            setTimeout(startReading, 1000);
        }
    };

    // Handle page unload to stop speech
    window.onbeforeunload = function() {
        isStopped = true;
        synth.cancel();
    };
})();
