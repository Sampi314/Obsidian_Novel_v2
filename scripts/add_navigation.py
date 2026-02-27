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
            if next_chapter:
                nav_html.append(f'<td style="border: none; padding: 5px;"><a href="{next_chapter["filename"].replace(".md", ".html")}">Chương Sau ➡️</a></td>')
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
            nav_html.append('  <button onclick="speakChapter()" style="cursor: pointer; padding: 5px 10px; margin: 5px;">▶️ Đọc</button>')
            nav_html.append('  <button onclick="pauseSpeech()" style="cursor: pointer; padding: 5px 10px; margin: 5px;">⏸️ Tạm Dừng</button>')
            nav_html.append('  <button onclick="resumeSpeech()" style="cursor: pointer; padding: 5px 10px; margin: 5px;">⏯️ Tiếp Tục</button>')
            nav_html.append('  <button onclick="stopSpeech()" style="cursor: pointer; padding: 5px 10px; margin: 5px;">⏹️ Dừng</button>')
            nav_html.append('</div>')

            # JavaScript for TTS
            nav_html.append('<script>')
            nav_html.append('var synth = window.speechSynthesis;')
            nav_html.append('var utterance = null;')
            nav_html.append('')
            nav_html.append('function speakChapter() {')
            nav_html.append('  if (synth.speaking) {')
            nav_html.append('    console.error("speechSynthesis.speaking");')
            nav_html.append('    return;')
            nav_html.append('  }')
            nav_html.append('  // Clone body to remove navigation before reading')
            nav_html.append('  var content = document.body.cloneNode(true);')
            nav_html.append('  var nav = content.querySelector("#chapter-navigation");')
            nav_html.append('  if (nav) {')
            nav_html.append('    nav.remove();')
            nav_html.append('  }')
            nav_html.append('  var text = content.innerText;')
            nav_html.append('  utterance = new SpeechSynthesisUtterance(text);')
            nav_html.append('  utterance.lang = "vi-VN";')
            nav_html.append('  synth.speak(utterance);')
            nav_html.append('}')
            nav_html.append('')
            nav_html.append('function pauseSpeech() {')
            nav_html.append('  if (synth.speaking && !synth.paused) {')
            nav_html.append('    synth.pause();')
            nav_html.append('  }')
            nav_html.append('}')
            nav_html.append('')
            nav_html.append('function resumeSpeech() {')
            nav_html.append('  if (synth.paused) {')
            nav_html.append('    synth.resume();')
            nav_html.append('  }')
            nav_html.append('}')
            nav_html.append('')
            nav_html.append('function stopSpeech() {')
            nav_html.append('  if (synth.speaking) {')
            nav_html.append('    synth.cancel();')
            nav_html.append('  }')
            nav_html.append('}')
            nav_html.append('</script>')

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
