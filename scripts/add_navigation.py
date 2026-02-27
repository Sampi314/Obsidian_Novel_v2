import os
import re
import html
from scripts.utils import get_chapter_title, extract_chapter_number

# Regex for existing navigation block
NAV_PATTERN = re.compile(r"<!-- NAVIGATION_START -->.*?<!-- NAVIGATION_END -->\s*", re.DOTALL)

# Regex for YAML Front Matter
# Matches start of file, ---, content, ---
FRONT_MATTER_PATTERN = re.compile(r"^---\n.*?\n---\n", re.DOTALL)

def generate_navigation(repo_root):
    story_dir = os.path.join(repo_root, "Đạo", "Chương_Truyện")
    if not os.path.exists(story_dir):
        print(f"Directory not found: {story_dir}")
        return

    pov_dirs = [d for d in os.listdir(story_dir) if os.path.isdir(os.path.join(story_dir, d))]

    for pov in pov_dirs:
        pov_path = os.path.join(story_dir, pov)
        files = []
        for filename in os.listdir(pov_path):
            if filename.endswith(".md") and filename not in ["index.md", "MỤC_LỤC.md"]:
                files.append(filename)

        # Sort files based on extracted chapter number
        files.sort(key=extract_chapter_number)

        # Pre-calculate titles for the dropdown
        chapter_list = []
        for filename in files:
            filepath = os.path.join(pov_path, filename)
            title = get_chapter_title(filepath)
            chapter_list.append({"filename": filename, "title": title})

        # Generate navigation for each file
        for i, current_chapter in enumerate(chapter_list):
            prev_chapter = chapter_list[i-1] if i > 0 else None
            next_chapter = chapter_list[i+1] if i < len(chapter_list) - 1 else None

            nav_html = []
            nav_html.append("<!-- NAVIGATION_START -->")
            nav_html.append('<div id="chapter-navigation" style="text-align: center; margin-bottom: 20px;">')

            # Use a table for layout to mimic a button bar
            nav_html.append('<table style="width: 100%; text-align: center; border: none;">')
            nav_html.append('<tr>')

            # Previous Button
            if prev_chapter:
                nav_html.append(f'<td style="border: none; padding: 5px;"><a href="{prev_chapter["filename"].replace(".md", ".html")}">⬅️ Chương Trước</a></td>')
            else:
                nav_html.append('<td style="border: none; padding: 5px; color: #adb5bd;">⬅️ Chương Trước</td>')

            # Home & TOC
            nav_html.append('<td style="border: none; padding: 5px;"><a href="../../../index.html">🏠 Trang Chủ</a></td>')
            nav_html.append('<td style="border: none; padding: 5px;"><a href="index.html">📖 Mục Lục</a></td>')

            # Next Button
            next_link_url = next_chapter["filename"].replace(".md", ".html") if next_chapter else "#"
            if next_chapter:
                nav_html.append(f'<td style="border: none; padding: 5px;"><a id="next-chapter-link" href="{next_link_url}">Chương Sau ➡️</a></td>')
            else:
                nav_html.append('<td style="border: none; padding: 5px; color: #adb5bd;">Chương Sau ➡️</td>')

            nav_html.append('</tr>')
            nav_html.append('</table>')

            # Dropdown
            nav_html.append('<details style="margin-top: 10px;">')
            nav_html.append('<summary style="cursor: pointer; font-weight: bold;">Chọn Chương</summary>')
            nav_html.append('<ul style="max-height: 200px; overflow-y: auto; list-style: none; padding: 0; text-align: left;">')

            for chap in chapter_list:
                is_active = 'font-weight: bold; background-color: #f0f0f0;' if chap["filename"] == current_chapter["filename"] else ''
                nav_html.append(f'<li style="padding: 5px; {is_active}"><a href="{chap["filename"].replace(".md", ".html")}">{html.escape(chap["title"])}</a></li>')

            nav_html.append('</ul>')
            nav_html.append('</details>')

            # Audio Player Controls
            nav_html.append('<div style="margin-top: 15px; border-top: 1px solid #ccc; padding-top: 10px;">')
            nav_html.append('  <strong>🎧 Nghe Chương Này:</strong>')
            nav_html.append('  <br>')
            nav_html.append('  <button id="btn-play" onclick="startReading()" style="cursor: pointer; padding: 5px 10px; margin: 5px;">▶️ Đọc</button>')
            nav_html.append('  <button id="btn-pause" onclick="pauseReading()" style="cursor: pointer; padding: 5px 10px; margin: 5px; display: none;">⏸️ Tạm Dừng</button>')
            nav_html.append('  <button id="btn-resume" onclick="resumeReading()" style="cursor: pointer; padding: 5px 10px; margin: 5px; display: none;">⏯️ Tiếp Tục</button>')
            nav_html.append('  <button id="btn-stop" onclick="stopReading()" style="cursor: pointer; padding: 5px 10px; margin: 5px; display: none;">⏹️ Dừng</button>')
            nav_html.append('</div>')

            # JavaScript for Advanced TTS
            # This script handles chunking, highlighting, auto-play, and auto-advance.
            script_content = """
<script>
    var synth = window.speechSynthesis;
    var currentUtterance = null;
    var readingQueue = [];
    var currentIndex = 0;
    var isPaused = false;
    var isStopped = false;

    // Elements to read
    var contentElements = [];

    // Next chapter URL
    var nextChapterUrl = "%s";

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
        document.getElementById("btn-play").style.display = "none";
        document.getElementById("btn-pause").style.display = "inline-block";
        document.getElementById("btn-resume").style.display = "none";
        document.getElementById("btn-stop").style.display = "inline-block";

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
            document.getElementById("btn-pause").style.display = "none";
            document.getElementById("btn-resume").style.display = "inline-block";
        }
    }

    function resumeReading() {
        if (isPaused) {
            synth.resume();
            isPaused = false;
            document.getElementById("btn-pause").style.display = "inline-block";
            document.getElementById("btn-resume").style.display = "none";
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

        document.getElementById("btn-play").style.display = "inline-block";
        document.getElementById("btn-pause").style.display = "none";
        document.getElementById("btn-resume").style.display = "none";
        document.getElementById("btn-stop").style.display = "none";
    }

    // Auto-play check
    window.onload = function() {
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
</script>
""" % (next_link_url)

            nav_html.append(script_content)

            nav_html.append('</div>')
            nav_html.append("<!-- NAVIGATION_END -->")
            nav_html.append("") # Empty line after

            nav_block = "\n".join(nav_html)

            # Update file content
            filepath = os.path.join(pov_path, current_chapter["filename"])
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()

                # Remove existing navigation first
                content_without_nav = NAV_PATTERN.sub("", content)

                match = FRONT_MATTER_PATTERN.match(content_without_nav)

                if match:
                    # Insert after front matter
                    end_pos = match.end()
                    new_content = content_without_nav[:end_pos] + nav_block + content_without_nav[end_pos:]
                else:
                    # Prepend to top
                    new_content = nav_block + content_without_nav

                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(new_content)

                print(f"Updated navigation for {current_chapter['filename']}")

            except Exception as e:
                print(f"Error updating {filepath}: {e}")

if __name__ == "__main__":
    repo_root = os.getcwd()
    generate_navigation(repo_root)
