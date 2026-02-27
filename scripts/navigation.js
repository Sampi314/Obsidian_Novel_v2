(function() {

    function injectStyles() {
        // Main style sheet
        var link = document.createElement('link');
        link.rel = 'stylesheet';
        link.href = '../../../scripts/style.css';
        document.head.appendChild(link);

        // Google Fonts
        var fontLink = document.createElement('link');
        fontLink.rel = 'stylesheet';
        fontLink.href = 'https://fonts.googleapis.com/css2?family=Merriweather:ital,wght@0,300;0,400;0,700;1,400&display=swap';
        document.head.appendChild(fontLink);
    }

    function createProgressBar() {
        var progressContainer = document.createElement('div');
        progressContainer.id = 'progress-container';

        var progressBar = document.createElement('div');
        progressBar.id = 'progress-bar';

        progressContainer.appendChild(progressBar);
        document.body.prepend(progressContainer);

        window.addEventListener('scroll', function() {
            var scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
            var scrollHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
            var scrolled = (scrollTop / scrollHeight) * 100;
            document.getElementById('progress-bar').style.width = scrolled + "%";
        });
    }

    function generateNavigation() {
        var container = document.getElementById('chapter-navigation');
        if (!container) return;

        // Clean up container
        container.innerHTML = '';
        container.className = 'nav-container';

        // Add class to body for styling hook
        document.body.classList.add('chapter-page');

        // Determine current chapter and POV
        var path = window.location.pathname;
        var pathParts = path.split('/').filter(function(p) { return p !== ""; });
        var currentFilename = decodeURIComponent(pathParts.pop() || "index.html");
        var currentPov = decodeURIComponent(pathParts.pop());

        if (!window.chapterData || !window.chapterData[currentPov]) {
            console.error("Chapter data not found for POV: " + currentPov);
            return;
        }

        var chapters = window.chapterData[currentPov];
        var currentIndex = -1;
        var currentMdFilename = currentFilename.replace('.html', '.md');

        for (var i = 0; i < chapters.length; i++) {
            if (chapters[i].filename === currentMdFilename) {
                currentIndex = i;
                break;
            }
        }

        var prevChapter = (currentIndex > 0) ? chapters[currentIndex - 1] : null;
        var nextChapter = (currentIndex < chapters.length - 1) ? chapters[currentIndex + 1] : null;

        // --- Navigation Bar (Flexbox) ---
        var navBar = document.createElement('div');
        navBar.className = 'nav-bar';

        // Prev Button
        var prevBtn = document.createElement('a');
        prevBtn.className = 'nav-btn';
        if (prevChapter) {
            prevBtn.href = prevChapter.filename.replace('.md', '.html');
            prevBtn.innerHTML = '⬅️ Chương Trước';
        } else {
            prevBtn.className += ' disabled';
            prevBtn.innerHTML = '⬅️ Chương Trước';
        }
        navBar.appendChild(prevBtn);

        // Home Button
        var homeBtn = document.createElement('a');
        homeBtn.href = '../../../index.html';
        homeBtn.className = 'nav-btn';
        homeBtn.innerHTML = '🏠 Trang Chủ';
        navBar.appendChild(homeBtn);

        // TOC Button
        var tocBtn = document.createElement('a');
        tocBtn.href = 'index.html';
        tocBtn.className = 'nav-btn';
        tocBtn.innerHTML = '📖 Mục Lục';
        navBar.appendChild(tocBtn);

        // Next Button
        var nextBtn = document.createElement('a');
        nextBtn.className = 'nav-btn';
        var nextUrl = "#";
        if (nextChapter) {
            nextUrl = nextChapter.filename.replace('.md', '.html');
            nextBtn.href = nextUrl;
            nextBtn.id = 'next-chapter-link';
            nextBtn.innerHTML = 'Chương Sau ➡️';
        } else {
            nextBtn.className += ' disabled';
            nextBtn.innerHTML = 'Chương Sau ➡️';
        }
        navBar.appendChild(nextBtn);

        container.appendChild(navBar);

        // Set global nextChapterUrl for TTS player
        window.nextChapterUrl = nextUrl;

        // --- Dropdown ---
        var details = document.createElement('details');
        var summary = document.createElement('summary');
        summary.textContent = '📚 Chọn Chương';
        details.appendChild(summary);

        var ul = document.createElement('ul');

        // Render chapters for dropdown
        for (var i = 0; i < chapters.length; i++) {
            var chap = chapters[i];
            var li = document.createElement('li');
            var a = document.createElement('a');

            a.href = chap.filename.replace('.md', '.html');
            a.textContent = chap.title;

            if (i === currentIndex) {
                li.className = 'active';
            }

            li.appendChild(a);
            ul.appendChild(li);
        }

        details.appendChild(ul);
        container.appendChild(details);

        // --- Audio Player Controls ---
        var audioDiv = document.createElement('div');
        audioDiv.className = 'audio-player';

        var audioTitle = document.createElement('strong');
        audioTitle.textContent = '🎧 Nghe Chương Này';
        audioDiv.appendChild(audioTitle);

        var controlsDiv = document.createElement('div');
        controlsDiv.className = 'audio-controls';

        // We need to create buttons with IDs that match what tts_player.js expects
        // tts_player.js toggles display:none on elements with IDs btn-play, btn-pause, etc.

        function createAudioBtn(id, text, actionName) {
            var btn = document.createElement('button');
            btn.id = id;
            btn.textContent = text;
            btn.className = 'audio-btn';

            // tts_player.js defines global functions like startReading()
            btn.addEventListener('click', function() {
                if (typeof window[actionName] === 'function') {
                    window[actionName]();
                }
            });

            // Default visibility
            if (id !== 'btn-play') {
                btn.style.display = 'none';
            }

            return btn;
        }

        controlsDiv.appendChild(createAudioBtn('btn-play', '▶️ Đọc', 'startReading'));
        controlsDiv.appendChild(createAudioBtn('btn-pause', '⏸️ Tạm Dừng', 'pauseReading'));
        controlsDiv.appendChild(createAudioBtn('btn-resume', '⏯️ Tiếp Tục', 'resumeReading'));
        controlsDiv.appendChild(createAudioBtn('btn-stop', '⏹️ Dừng', 'stopReading'));

        audioDiv.appendChild(controlsDiv);
        container.appendChild(audioDiv);
    }

    // Initialize
    function init() {
        injectStyles();
        createProgressBar();
        generateNavigation();
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

})();
