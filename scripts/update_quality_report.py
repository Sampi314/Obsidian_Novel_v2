import datetime

with open('/app/Đạo/BÁO_CÁO_CHẤT_LƯỢNG.md', 'r', encoding='utf-8') as f:
    content = f.read()

now = datetime.datetime.now().strftime("%Y-%m-%d")

new_report = f"""
## [{now}] - Cập Nhật Nhân Vật Sương Ma Uyển (Bắc Băng)
- **Nội Dung:** Bổ sung chi tiết (Ngoại hình, Tính cách, Năng lực, Quan hệ, Tiểu sử) cho Hắc Sương Quỷ, Lãnh Vô Hồn, Sương Nô Vương.
- **Đánh Giá:** Các nhân vật đã được điền đủ 4 mục II-V, mang đặc trưng tàn bạo, độc ác của Ma Tộc phương Bắc, phù hợp với tông chỉ của Sương Ma Uyển.
- **Trạng Thái:** Đã hoàn thành và thêm vào dữ liệu quan hệ (`relationship_data.js`).
"""

# Insert at the beginning of the "## PHIÊN GẦN NHẤT" section or just after the title if it exists
insert_point = content.find("## ")
if insert_point != -1:
    content = content[:insert_point] + new_report + content[insert_point:]
else:
    content = new_report + content

with open('/app/Đạo/BÁO_CÁO_CHẤT_LƯỢNG.md', 'w', encoding='utf-8') as f:
    f.write(content)
