import os
import re

HO_SO_PATH = "Đạo/HỒ_SƠ_THẾ_GIỚI.md"
FACTIONS_DIR = "Đạo/Thế_Lực"

def main():
    with open(HO_SO_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the "## VI. THẾ LỰC CHÍNH" section
    match = re.search(r"## VI\. THẾ LỰC CHÍNH.*", content, re.DOTALL)
    if not match:
        print("Could not find ## VI. THẾ LỰC CHÍNH")
        return

    prefix_content = content[:match.start()]

    # We will just generate the entire new section based on files in the directory.
    # We'll try to guess the region based on filenames or just list them.
    # To be precise, we know the regions from our creation scripts.

    nam_cuong = ["Vạn_Độc_Môn", "Đan_Hà_Cốc", "Vạn_Trùng_Cốc", "Tinh_Linh_Vương_Đình", "Hắc_Báo_Trại", "Thiên_Mộc_Thành", "Cổ_Nguyệt_Thần_Giáo", "Huyết_Ma_Tông", "Quỷ_Thị_Nam_Cương", "Bách_Thú_Sơn_Trang"]
    thien_tru = ["Long_Cung", "Vũ_Hoàng_Các", "Thiên_Môn_Kính_Đài", "Thạch_Linh_Cung", "Vân_Tông", "Tiên_Cầm_Viện", "Lôi_Trì_Thánh_Địa", "Vô_Tranh_Tự", "Thiên_Trụ_Hộ_Vệ_Đoàn", "Trích_Tinh_Lâu"]
    bac_bang = ["Huyền_Băng_Cung", "Cự_Linh_Tông", "Băng_Lang_Bộ_Lạc", "Cực_Quang_Thần_Điện", "Sương_Ma_Uyển", "Băng_Ngục_Thành", "Hàn_Kiếm_Cốc", "Tuyết_Cự_Nhân_Đảo", "Phiêu_Miễu_Băng_Hải", "Thiên_Sơn_Đông_Cốc"]
    vo_tan_hai = ["Hải_Thần_Cung", "Hắc_Hải_Hải_Tặc", "San_Hô_Đảo_Quốc", "Vực_Thẳm_Ma_Cung", "Cự_Kình_Bảo", "Hải_Yêu_Mê_Cung", "Giao_Nhân_Tộc_Liên_Minh", "Thủy_Kiếm_Đảo", "Bắc_Hải_Cự_Yêu_Hang", "Phong_Bạo_Thương_Đội"]
    dong_hoang = ["Thiên_Yêu_Đình", "Cổ_Thạch_Bộ_Lạc", "Vạn_Yêu_Thành", "Thanh_Đế_Cung", "Vu_Tộc_Chiếu_Cáo", "Liệt_Dương_Tông", "Ngự_Kiếm_Sơn_Trang", "Tử_Vong_Chi_Thung_Lũng", "Bách_Hoa_Cốc", "Ảo_Ảnh_Lâm_Tộc"]
    tay_mac = ["Thiên_Sa_Thương_Hội", "Sa_Tặc_Liên_Minh", "Kim_Sa_Tự", "Độc_Long_Bảo", "Lưu_Sa_Huyễn_Ảo", "Hoàng_Sa_Cổ_Quốc", "Thần_Cung_Bắn_Sa", "Thủy_Nguồn_Bảo_Vệ_Đoàn", "Phong_Sát_Cốc", "Pháo_Đài_Xanh_Hội"]
    trung_tam = ["Cửu_Hoa_Kiếm_Tông", "Dược_Vương_Cốc", "Ảnh_Nguyệt_Uyển", "Đại_Càn_Hoàng_Triều", "Thái_Ất_Môn", "Ma_Đạo_Minh", "Thiên_Kiêu_Học_Viện", "Bách_Bảo_Các", "Luyện_Khí_Đại_Sư_Hội", "Hợp_Hoan_Tông", "Vạn_Tượng_Sâm_La"]

    new_section = "## VI. THẾ LỰC CHÍNH\n\n"

    def add_category(title, lst):
        nonlocal new_section
        new_section += f"- **{title}:**\n"
        for item in lst:
            filename = item + ".md"
            filepath = os.path.join(FACTIONS_DIR, filename)
            if os.path.exists(filepath):
                name = item.replace("_", " ")
                new_section += f"    - [{name}](Thế_Lực/{filename})\n"
            else:
                print(f"Warning: {filepath} not found.")

    add_category("Nam Cương (Southern Border)", nam_cuong)
    add_category("Thiên Trụ Sơn (World Pillar)", thien_tru)
    add_category("Bắc Băng (Northern Ice)", bac_bang)
    add_category("Đông Hoang (Eastern Wilderness)", dong_hoang)
    add_category("Tây Mạc (Western Desert)", tay_mac)
    add_category("Trung Tâm (Central)", trung_tam)
    add_category("Vô Tận Hải (Endless Sea)", vo_tan_hai)

    # Any others not listed?
    listed = set(nam_cuong + thien_tru + bac_bang + vo_tan_hai + dong_hoang + tay_mac + trung_tam)
    others = []
    for f in os.listdir(FACTIONS_DIR):
        if f.endswith('.md'):
            base = f[:-3]
            if base not in listed:
                others.append(base)

    if others:
        add_category("Khác (Others)", others)

    with open(HO_SO_PATH, 'w', encoding='utf-8') as f:
        f.write(prefix_content + new_section)

    print("Updated HỒ_SƠ_THẾ_GIỚI.md")

if __name__ == "__main__":
    main()
