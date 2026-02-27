import os

def get_chapter_title(filepath):
    """
    Extracts the first H1 title from a markdown file.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith("# "):
                    return line.strip()[2:]
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
    return "Không có tiêu đề"

def generate_pov_index(pov_dir, pov_name):
    """
    Generates an index.md file for a specific POV directory.
    """
    index_path = os.path.join(pov_dir, "index.md")
    content = [f"# Mục Lục: {pov_name}\n"]

    files = []
    for filename in os.listdir(pov_dir):
        if filename.endswith(".md") and filename != "index.md" and filename != "MỤC_LỤC.md":
            files.append(filename)

    files.sort()

    for filename in files:
        filepath = os.path.join(pov_dir, filename)
        title = get_chapter_title(filepath)
        content.append(f"- [{title}]({filename})")

    with open(index_path, "w", encoding="utf-8") as f:
        f.write("\n".join(content))

    print(f"Generated index for {pov_name} at {index_path}")

def generate_root_index(repo_root):
    """
    Generates the root index.md file.
    """
    index_path = os.path.join(repo_root, "index.md")

    content = [
        "# Mục Lục Tổng Hợp\n",
        "Chào mừng đến với trang mục lục tổng hợp của thế giới Tiên Hiệp 'Cố Nguyên'.\n",
        "## 📖 Cốt Truyện (Story)\n",
        "Các chương truyện được phân loại theo góc nhìn nhân vật:\n"
    ]

    # Story Section
    story_dir = os.path.join(repo_root, "Đạo", "Chương_Truyện")
    if os.path.exists(story_dir):
        pov_dirs = [d for d in os.listdir(story_dir) if os.path.isdir(os.path.join(story_dir, d))]
        pov_dirs.sort()

        for pov_dir_name in pov_dirs:
            # Human readable name
            display_name = pov_dir_name.replace("Góc_Nhìn_", "").replace("_", " ")
            link_path = f"Đạo/Chương_Truyện/{pov_dir_name}/index.md"
            content.append(f"- [Góc Nhìn {display_name}]({link_path})")

            # Generate the POV index while we are here
            full_pov_path = os.path.join(story_dir, pov_dir_name)
            generate_pov_index(full_pov_path, f"Góc Nhìn {display_name}")

    # Wiki Section
    content.extend([
        "\n## 📚 Tra Cứu (Wiki)\n",
        "Thông tin chi tiết về thế giới, nhân vật và hệ thống tu luyện:\n",
        "- [Hồ Sơ Thế Giới (World Profile)](Đạo/HỒ_SƠ_THẾ_GIỚI.md)",
        "- [Nhân Vật (Characters)](Đạo/Nhân_Vật/)",
        "- [Công Pháp (Techniques)](Đạo/Công_Pháp/)",
        "- [Thế Lực (Factions)](Đạo/Thế_Lực/)",
        "- [Kỳ Vật (Artifacts & Beasts)](Đạo/Kỳ_Vật/)",
        "- [Chủng Tộc (Races)](Đạo/Chủng_Tộc/)",
        "- [Đan Dược (Alchemy)](Đạo/Đan_Dược/)",
        "- [Luyện Khí (Blacksmithing)](Đạo/Luyện_Khí/)",
        "- [Trận Pháp (Formations)](Đạo/Trận_Pháp/)",
        "- [Phù Lục (Talismans)](Đạo/Phù_Lục/)",
        "- [Thế Giới & Thời Gian (World & Timeline)](Đạo/Thế_Giới_Và_Thời_Gian/)",
        "- [Văn Hóa (Culture)](Đạo/Văn_Hóa/)"
    ])

    with open(index_path, "w", encoding="utf-8") as f:
        f.write("\n".join(content))

    print(f"Generated root index at {index_path}")

if __name__ == "__main__":
    repo_root = os.getcwd()
    generate_root_index(repo_root)
