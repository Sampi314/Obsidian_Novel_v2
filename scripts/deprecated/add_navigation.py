import os
import re
import html
import json
from scripts.utils import get_chapter_title, extract_chapter_number

# Regex for existing navigation block
NAV_PATTERN = re.compile(r"<!-- NAVIGATION_START -->.*?<!-- NAVIGATION_END -->\s*", re.DOTALL)

# Regex for YAML Front Matter
FRONT_MATTER_PATTERN = re.compile(r"^---\n.*?\n---\n", re.DOTALL)

def collect_chapter_data(repo_root):
    story_dir = os.path.join(repo_root, "Đạo", "Chương_Truyện")
    if not os.path.exists(story_dir):
        print(f"Directory not found: {story_dir}")
        return {}

    pov_dirs = [d for d in os.listdir(story_dir) if os.path.isdir(os.path.join(story_dir, d))]

    all_chapters = {}

    for pov in pov_dirs:
        pov_path = os.path.join(story_dir, pov)
        files = []
        for filename in os.listdir(pov_path):
            if filename.endswith(".md") and filename not in ["index.md", "MỤC_LỤC.md"]:
                files.append(filename)

        # Sort files based on extracted chapter number
        files.sort(key=extract_chapter_number)

        chapter_list = []
        for filename in files:
            filepath = os.path.join(pov_path, filename)
            title = get_chapter_title(filepath)
            chapter_list.append({
                "filename": filename,
                "title": title
            })

        all_chapters[pov] = chapter_list

    return all_chapters

def generate_chapter_data_js(repo_root, data):
    js_content = f"window.chapterData = {json.dumps(data, ensure_ascii=False, indent=2)};"
    js_path = os.path.join(repo_root, "scripts", "chapter_data.js")
    with open(js_path, "w", encoding="utf-8") as f:
        f.write(js_content)
    print(f"Generated {js_path}")

def generate_navigation(repo_root):
    # 1. Collect all chapter data
    print("Collecting chapter data...")
    all_data = collect_chapter_data(repo_root)

    # 2. Generate the JS data file
    generate_chapter_data_js(repo_root, all_data)

    # 3. Update individual files with minimal placeholder and script tags
    story_dir = os.path.join(repo_root, "Đạo", "Chương_Truyện")

    for pov, chapter_list in all_data.items():
        pov_path = os.path.join(story_dir, pov)

        for current_chapter in chapter_list:

            nav_html = []
            nav_html.append("<!-- NAVIGATION_START -->")
            nav_html.append('<div id="chapter-navigation" style="text-align: center; margin-bottom: 20px;"></div>')

            # Script injections
            # Path is relative from Đạo/Chương_Truyện/POV/Chapter.md to scripts/
            # POV is 3 levels deep (Đạo/Chương_Truyện/POV), so ../../../ takes us to root
            nav_html.append('<script src="../../../scripts/chapter_data.js"></script>')
            nav_html.append('<script src="../../../scripts/navigation.js"></script>')
            nav_html.append('<script src="../../../scripts/tts_player.js"></script>')

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

                # print(f"Updated navigation for {current_chapter['filename']}") # Reduce spam

            except Exception as e:
                print(f"Error updating {filepath}: {e}")

    print("Navigation injection complete.")

if __name__ == "__main__":
    repo_root = os.getcwd()
    generate_navigation(repo_root)
