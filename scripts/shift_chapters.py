import os
import re
import argparse

def extract_chapter_index(filename):
    """
    Extracts the integer chapter index from the filename.
    Chương_00001_Title.md -> 1
    """
    match = re.search(r'Chương_(\d+)_', filename)
    if match:
        return int(match.group(1))
    return None

def shift_chapters(directory, start_index, offset):
    """
    Shifts chapter indices in filenames by a given offset.
    Only shifts chapters with index >= start_index.
    """
    if not os.path.exists(directory):
        print(f"Directory not found: {directory}")
        return

    print(f"Shifting chapters in {directory} starting from {start_index} by {offset}...")

    files = []
    for filename in os.listdir(directory):
        if filename.endswith(".md") and filename not in ["index.md", "MỤC_LỤC.md"]:
            index = extract_chapter_index(filename)
            if index is not None and index >= start_index:
                files.append((index, filename))

    # Sort files in descending order to avoid overwriting (e.g., 9->10 before 8->9)
    files.sort(key=lambda x: x[0], reverse=True)

    for index, filename in files:
        new_index = index + offset

        # Extract title part
        match = re.search(r'Chương_\d+_(.*)', filename)
        if match:
            title_part = match.group(1)
            new_filename = f"Chương_{new_index:05d}_{title_part}"

            src = os.path.join(directory, filename)
            dst = os.path.join(directory, new_filename)

            try:
                os.rename(src, dst)
                print(f"Renamed {filename} -> {new_filename}")
            except Exception as e:
                print(f"Error renaming {filename}: {e}")
        else:
            print(f"Could not parse title from {filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Shift chapter indices.")
    parser.add_argument("--directory", required=True, help="Directory containing chapter files")
    parser.add_argument("--start", type=int, required=True, help="Starting chapter index to shift")
    parser.add_argument("--offset", type=int, required=True, help="Number of positions to shift")

    args = parser.parse_args()

    # Resolve absolute path for directory
    directory = os.path.abspath(args.directory)

    shift_chapters(directory, args.start, args.offset)
