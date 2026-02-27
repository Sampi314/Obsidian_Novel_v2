import re

# Pre-compile chapter number regex for better performance
CHAPTER_NUM_PATTERN = re.compile(r'Chương_(\d+)(?:_(\d+))?_')

def get_chapter_title(filepath):
    """
    Extracts the first H1 title from a markdown file.
    Optimized to read line by line instead of loading the whole file.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            in_yaml = False
            in_comment = False

            for line in f:
                stripped = line.strip()
                if not stripped:
                    continue

                # Handle YAML Frontmatter
                if stripped == "---":
                    in_yaml = not in_yaml
                    continue
                if in_yaml:
                    continue

                # Handle HTML Comments
                # If line starts with <!--, it might be a single line or start of a block
                if stripped.startswith("<!--"):
                    if "-->" not in stripped:
                        in_comment = True
                    continue

                # If we are inside a comment block, look for the closing tag
                if in_comment:
                    if "-->" in stripped:
                        in_comment = False
                    continue

                # Ignore navigation block lines (which we inject)
                # These might not be wrapped in <!-- comments --> in older versions,
                # or we just want to be extra safe ignoring raw HTML nav elements.
                if "<div" in stripped or "<table" in stripped or "<td" in stripped or "<tr" in stripped:
                    continue

                # Check for standard markdown headers (indented or otherwise)
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
    match = CHAPTER_NUM_PATTERN.search(filename)
    if match:
        major = int(match.group(1))
        minor = int(match.group(2)) if match.group(2) else 0
        return major + (minor / 10.0)
    return float('inf') # Put non-matching files at the end
