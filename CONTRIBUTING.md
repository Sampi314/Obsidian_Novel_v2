# 🛠️ Hướng Dẫn Bảo Trì & Quy Chuẩn Nội Dung (Internal Maintenance Guide)

> [!CAUTION]
> **DỰ ÁN CÁ NHÂN - KHÔNG TIẾP NHẬN ĐÓNG GÓP CÔNG KHAI**
> Kho lưu trữ này được thiết lập cho mục đích cá nhân và phát triển thế giới với sự hỗ trợ của AI. Chúng tôi **KHÔNG** tiếp nhận Pull Requests hoặc Issues từ cộng đồng. Mọi đóng góp công khai sẽ bị từ chối hoặc bỏ qua.

---

## 🤖 Quy Trình Dành Cho Tác Nhân AI (AI Agent Workflow)

Để duy trì tính nhất quán của thế giới "Cố Nguyên", các tác nhân AI (Claude Code, Gemini, v.v.) khi thực hiện nhiệm vụ bảo trì hoặc sáng tạo phải tuân thủ nghiêm ngặt các bước sau:

### 1. Kiểm Tra Nhất Quán (Consistency Check)
- Trước khi thêm bất kỳ thực thể mới nào (Nhân vật, Tông môn, Công pháp), AI phải đọc tệp gốc `Đạo/HỒ_SƠ_THẾ_GIỚI.md`.
- Đảm bảo thực thể mới không mâu thuẫn với các thiết lập hiện có về cảnh giới, địa lý hoặc lịch sử.

### 2. Kỹ Năng Chuyên Biệt (Claude Code Skills)
Sử dụng các kỹ năng đã được thiết lập trong `.claude/skills/` để thực hiện các tác vụ cụ thể. Ví dụ:
- Sử dụng `/nhan-vat` để tạo hồ sơ nhân vật mới với YAML frontmatter chuẩn.
- Sử dụng `/kiem-duyet` sau khi viết chương truyện để đảm bảo chất lượng.
- Sử dụng `/quan-he` để cập nhật sơ đồ quan hệ khi có thay đổi về tình tiết.

### 3. Quy Tắc Đặt Tên & Lưu Trữ (Naming & Storage)
- **BẮT BUỘC**: Tên tệp tin phải là **Tiếng Việt có dấu**.
- **KHOẢNG TRẮNG**: Thay thế bằng dấu gạch dưới (`_`).
- **ĐƯỜNG DẪN**: Lưu đúng vào các thư mục chức năng trong `Đạo/`.
  - *Ví dụ chuẩn*: `Đạo/Công_Pháp/Thái_Cực_Kiếm_Phổ.md`
  - *Ví dụ sai*: `Dao/Cong_Phap/thai cuc kiem pho.md`

### 4. Cấu Trúc Metadata (YAML Frontmatter)
Mọi tệp tin nội dung phải có YAML frontmatter đầy đủ theo schema của loại thực thể đó.
- `type`: `character`, `faction`, `chapter`, `item`, v.v.
- `tags`: Các từ khóa phân loại.
- `status`: Tình trạng thực thể (Active, Deceased, Hidden).

---

## 🔧 Công Cụ Hỗ Trợ (Maintenance Scripts)

Sử dụng các script trong thư mục `scripts/` để tự động hóa việc bảo trì:

- `python3 scripts/update_chapter_data.py`: Cập nhật danh sách chương truyện và mục lục.
- `node scripts/generate_wiki_index.mjs`: Tái cấu trúc chỉ mục tìm kiếm cho wiki.
- `python3 scripts/check_links.py`: Kiểm tra tính toàn vẹn của các liên kết nội bộ.

---

## ⚙️ Cấu Hình Git (Git Configuration)

Để tránh lỗi hiển thị tên tệp tin tiếng Việt trong terminal:

```bash
git config core.quotePath false
```

---
*Tài liệu này phục vụ mục đích hướng dẫn quy trình vận hành nội bộ giữa Người dùng và AI.*
