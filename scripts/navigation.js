(function() {

    // Detect reader mode: running inside reader.html with ?file= param
    var params = new URLSearchParams(window.location.search);
    var readerFile = params.get('file');
    var isReaderMode = !!readerFile;

    function injectStyles() {
        // Main style sheet — path depends on mode
        var link = document.createElement('link');
        link.rel = 'stylesheet';
        link.href = isReaderMode ? 'scripts/style.css' : '../../../scripts/style.css';
        document.head.appendChild(link);

        // Google Fonts
        var fontLink = document.createElement('link');
        fontLink.rel = 'stylesheet';
        fontLink.href = 'https://fonts.googleapis.com/css2?family=Merriweather:ital,wght@0,300;0,400;0,700;1,400&display=swap';
        document.head.appendChild(fontLink);
    }

    function createProgressBar() {
        // Skip if already exists
        if (document.getElementById('progress-container')) return;

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

    // Build a chapter link URL depending on mode
    function makeChapterUrl(chapterFilename) {
        if (isReaderMode) {
            // Extract directory from current file path
            var dir = readerFile.substring(0, readerFile.lastIndexOf('/') + 1);
            return 'reader.html?file=' + encodeURIComponent(dir + chapterFilename);
        } else {
            return chapterFilename.replace('.md', '.html');
        }
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
        var currentFilename, currentPov;

        if (isReaderMode) {
            // Reader mode: parse from ?file= param
            // e.g. "Đạo/Chương_Truyện/Góc_Nhìn_Chính/Chương_00001_Dấu_Hiệu_Tai_Ương.md"
            // Let's decode until there are no more percent signs
            var parsedFile = readerFile;
            var maxLoops = 5;
            while(parsedFile.indexOf('%') !== -1 && maxLoops > 0) {
                try {
                    parsedFile = decodeURIComponent(parsedFile);
                } catch(e) {
                    break;
                }
                maxLoops--;
            }
            // Some paths might include an extra area folder, e.g. Đạo/Chương_Truyện/Nam_Cương/Góc_Nhìn_Lâm_Phong/Chương_...
            // We want currentPov to be "Góc_Nhìn_..." and currentFilename to be "Chương_..."
            var parts = parsedFile.split('/').filter(function(p) { return p !== ''; });
            currentFilename = parts.pop() || '';
            currentPov = parts.pop() || '';
            if (currentPov && currentPov.indexOf('Góc_Nhìn_') === -1) {
                // Sometimes the path has an extra nesting, let's pop again if we didn't find "Góc_Nhìn_"
                var potentialPov = parts.pop();
                if (potentialPov && potentialPov.indexOf('Góc_Nhìn_') !== -1) {
                    currentPov = potentialPov;
                }
            }
            console.log("Parsed from URL - POV:", currentPov, "Filename:", currentFilename);
        } else {
            // Legacy mode: parse from pathname
            var path = window.location.pathname;
            var pathParts = path.split('/').filter(function(p) { return p !== ""; });
            currentFilename = decodeURIComponent(pathParts.pop() || "index.html");
            currentPov = decodeURIComponent(pathParts.pop());
        }

        // Ensure chapterData uses correct variable name
        var dataObj = window.chapterData;

        // Wait, if module.exports is used in chapterData for node, the structure might be different?
        console.log("dataObj keys: ", Object.keys(dataObj || {}));

        // Handle both possible structures depending on how it was loaded
        if (dataObj && dataObj.chapterData) {
            dataObj = dataObj.chapterData;
        }

        if (!dataObj || !dataObj[currentPov]) {
            console.error("Chapter data not found for POV: " + currentPov);
            return;
        }

        var chapters = dataObj[currentPov];
        var currentIndex = -1;
        // In reader mode, filename already ends with .md
        // In legacy mode, convert .html to .md for lookup
        var currentMdFilename = isReaderMode ? currentFilename : currentFilename.replace('.html', '.md');

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
            prevBtn.href = makeChapterUrl(prevChapter.filename);
            prevBtn.innerHTML = '⬅️ Chương Trước';
        } else {
            prevBtn.className += ' disabled';
            prevBtn.innerHTML = '⬅️ Chương Trước';
        }
        navBar.appendChild(prevBtn);

        // Home Button
        var homeBtn = document.createElement('a');
        homeBtn.href = isReaderMode ? 'index.html' : '../../../index.html';
        homeBtn.className = 'nav-btn';
        homeBtn.innerHTML = '🏠 Trang Chủ';
        navBar.appendChild(homeBtn);

        // TOC Button — links to the MỤC_LỤC.md for the current POV
        var tocBtn = document.createElement('a');
        if (isReaderMode) {
            var dir = readerFile.substring(0, readerFile.lastIndexOf('/') + 1);
            tocBtn.href = 'reader.html?file=' + encodeURIComponent(dir + 'MỤC_LỤC.md');
        } else {
            tocBtn.href = 'index.html';
        }
        tocBtn.className = 'nav-btn';
        tocBtn.innerHTML = '📖 Mục Lục';
        navBar.appendChild(tocBtn);

        // Next Button
        var nextBtn = document.createElement('a');
        nextBtn.className = 'nav-btn';
        var nextUrl = "#";
        if (nextChapter) {
            nextUrl = makeChapterUrl(nextChapter.filename);
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

            a.href = makeChapterUrl(chap.filename);
            a.textContent = chap.title;

            if (i === currentIndex) {
                li.className = 'active';
            }

            li.appendChild(a);
            ul.appendChild(li);
        }

        details.appendChild(ul);
        container.appendChild(details);

        // Audio player is now handled by tts_player.js (floating sticky bar)
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
