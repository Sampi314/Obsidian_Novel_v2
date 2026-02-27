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
            # First pass: look for # Title
            for line in f:
                if line.startswith("# "):
                    return line.strip()[2:]

            # Second pass: look for the first line that looks like a title after YAML frontmatter
            f.seek(0)
            in_yaml = False
            for line in f:
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
