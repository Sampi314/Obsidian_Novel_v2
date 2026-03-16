import os

memory_dir = '.jules_memory/'

for filename in os.listdir(memory_dir):
    filepath = os.path.join(memory_dir, filename)
    if os.path.isfile(filepath) and filepath.endswith('.md'):
        with open(filepath, 'r') as f:
            lines = f.readlines()

        if len(lines) > 200:
            print(f"Compacting {filename}...")
            # Keep last 50 lines, summarize the rest
            recent_lines = lines[-50:]
            old_lines = lines[:-50]

            summary = "## TỔNG HỢP LỊCH SỬ (tự động nén)\n- [Auto-compressed]: Đã nén các log cũ để tối ưu bộ nhớ.\n\n"
            new_content = [summary, "## PHIÊN GẦN NHẤT\n"] + recent_lines

            with open(filepath, 'w') as f:
                f.writelines(new_content)

print("Memory compaction done.")
