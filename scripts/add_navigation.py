import os
import re

# Regex for existing navigation block
NAV_PATTERN = re.compile(r"<!-- NAVIGATION_START -->.*?<!-- NAVIGATION_END -->\s*", re.DOTALL)

# Regex for YAML Front Matter
# Matches start of file, ---, content, ---
FRONT_MATTER_PATTERN = re.compile(r"^---\n.*?\n---\n", re.DOTALL)

def get_chapter_title(filepath):
    """
    Extracts the first H1 title from a markdown file.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
            # First pass: look for # Title
            for line in lines:
                if line.startswith("# "):
                    return line.strip()[2:]

            # Second pass: look for Title\n=== or similar if using setext style (less likely but possible)
            # or maybe it's inside metadata? The file we saw has YAML frontmatter then comments then content.
            # Let's look for the first line that looks like a title after YAML frontmatter

            in_yaml = False
            for line in lines:
                stripped = line.strip()
                if stripped == "---":
                    in_yaml = not in_yaml
                    continue
                if in_yaml:
                    continue

                # Ignore comments
                if stripped.startswith("<!--") or stripped.endswith("-->"):
                    continue

                # Ignore navigation block lines (which we inject)
                if "<div" in stripped or "<table" in stripped or "<td" in stripped or "<tr" in stripped:
                    continue

                # Check for standard markdown headers
                if stripped.startswith("# "):
                    return stripped[2:]

    except Exception as e:
        print(f"Error reading {filepath}: {e}")
    return "Không có tiêu đề"

def extract_chapter_number(filename):
    """
    Extracts the chapter number from the filename for sorting.
    Handles formats like Chương_00001_... -> 1.0
    and Chương_00001_5_... -> 1.5
    """
    match = re.search(r'Chương_(\d+)(?:_(\d+))?_', filename)
    if match:
        major = int(match.group(1))
        minor = int(match.group(2)) if match.group(2) else 0
        return major + (minor / 10.0)
    return float('inf') # Put non-matching files at the end

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
            nav_html.append('<div style="text-align: center; margin-bottom: 20px;">')

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
                nav_html.append(f'<li style="padding: 5px; {is_active}"><a href="{chap["filename"].replace(".md", ".html")}">{chap["title"]}</a></li>')

            nav_html.append('</ul>')
            nav_html.append('</details>')
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
