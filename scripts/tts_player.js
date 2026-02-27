(function() {
    var synth = window.speechSynthesis;
    var currentUtterance = null;
    var readingQueue = [];
    var currentIndex = 0;
    var isPaused = false;
    var isStopped = false;

    // Elements to read
    var contentElements = [];

    // Configuration from global scope or data attribute
    // We expect window.nextChapterUrl to be set in the HTML
    var nextChapterUrl = window.nextChapterUrl || "#";

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
        return readable;
    }

    function startReading() {
        if (synth.speaking && !isPaused) return;

        isStopped = false;

        // Reset controls
        toggleControls('playing');

        contentElements = getReadableElements();

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
            if (nextChapterUrl && nextChapterUrl !== "#") {
                // Add autoplay param
                var separator = nextChapterUrl.includes('?') ? '&' : '?';
                window.location.href = nextChapterUrl + separator + 'autoplay=true';
            }
            return;
        }

        var el = contentElements[currentIndex];

        // Highlight current element
        el.style.backgroundColor = "#e6f7ff";
        el.style.borderLeft = "4px solid #1890ff";
        el.style.paddingLeft = "10px";
        el.scrollIntoView({behavior: "smooth", block: "center"});

        var text = el.innerText;
        var utterance = new SpeechSynthesisUtterance(text);
        utterance.lang = "vi-VN";

        utterance.onend = function() {
            if (isStopped) return;

            // Remove highlight
            el.style.backgroundColor = "";
            el.style.borderLeft = "";
            el.style.paddingLeft = "";

            currentIndex++;
            if (!isPaused && synth.speaking === false) {
                 readNextChunk();
            }
        };

        utterance.onerror = function(event) {
            if (isStopped) return;

            console.error("Speech error", event);
            // Try to skip to next chunk on error
            el.style.backgroundColor = "";
            el.style.borderLeft = "";
            el.style.paddingLeft = "";
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
            if (el) {
                el.style.backgroundColor = "";
                el.style.borderLeft = "";
                el.style.paddingLeft = "";
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

    // Auto-play check
    window.onload = function() {
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
