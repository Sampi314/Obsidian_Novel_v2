<div align="right">[ [ 🇺🇸 View English Version ] ](./README.en.md)</div>

# 🌌 Hệ Thống Kiến Tạo Thế Giới Tiên Hiệp "Cố Nguyên"

> [!IMPORTANT]
> **TRẠNG THÁI: KHO LƯU TRỮ CÁ NHÂN (PRIVATE REFERENCE ARCHIVE)**
> Đây là dự án kiến tạo thế giới (world-building) cá nhân. Kho lưu trữ này đóng vai trò là cơ sở dữ liệu sống cho việc sáng tác và phát triển nội dung Tiên Hiệp với sự hỗ trợ của AI. **Chúng tôi không tiếp nhận đóng góp (Pull Requests/Issues) từ bên ngoài.**

---

## 📜 Giới Thiệu (Lore Summary)

"Cố Nguyên" là một đại thế giới tu chân cổ đại, nơi linh khí bắt nguồn từ thuở hỗn mang. Dự án này hệ thống hóa toàn bộ quy luật, thực thể và lịch sử của thế giới này, từ những cảnh giới tu luyện huyền vi đến những âm mưu tranh đấu giữa các đại tông môn. 

Mục tiêu của dự án là xây dựng một hệ sinh thái dữ liệu chặt chẽ, cho phép các tác nhân AI (AI Agents) và tác giả cùng phối hợp để tạo ra những chương truyện có tính nhất quán cao về logic thế giới.

---

## 📖 Trình Đọc Tương Tác (Interactive Reader)

Hệ thống sử dụng `reader.html` làm bộ engine hiển thị duy nhất. Dựa vào trường `type` trong YAML frontmatter của mỗi tệp tin Markdown, trình đọc sẽ tự động thay đổi giao diện:

- **`type: character`**: Hiển thị Hồ sơ nhân vật với biểu đồ radar tư chất, dòng thời gian đại cảnh và thanh trạng thái cảm xúc.
- **`type: faction`**: Hiển thị Hồ sơ thế lực với sơ đồ phân chia bộ viện, thanh quan hệ ngoại giao và bản đồ lãnh thổ.
- **Chapter files**: Trình đọc chương truyện chuyên dụng với hệ thống điều hướng thông minh và trình phát TTS (Text-to-Speech).

**Chủ đề (Themes):** Thủy Mạc (Ink), Huyết Nguyệt (Blood Moon), Thanh Trúc (Bamboo), Bạch Tuyết (Snow), Hắc Diện (Dark).

**[👉 Truy cập Mục Lục Tổng Hợp](https://sampi314.github.io/Obsidian_Novel_v2/index.html)**

---

## 🗂️ Phân Loại Dữ liệu (World Taxonomy)

Toàn bộ tri thức về thế giới được tổ chức trong thư mục `Đạo/`:

- **`Nhân_Vật/`**: Hồ sơ chi tiết về các tu sĩ, yêu ma và phàm nhân.
- **`Thế_Lực/`**: Hệ thống tông môn, gia tộc và triều đình (hơn 200 thực thể).
- **`Công_Pháp/`**: Bí kíp tu luyện, thần thông và chiêu thức.
- **`Thế_Giới_Và_Thời_Gian/`**: Địa lý, lịch sử và dòng thời gian vạn năm.
- **`Tu_Luyện/`**: Hệ thống cảnh giới và quy luật thiên đạo.
- ... và các hạng mục khác như Đan Dược, Luyện Khí, Trận Pháp, Phù Lục, Thơ Ca, Âm Nhạc.

---

## 🤖 Kỹ Năng Claude Code (AI Skills)

Dự án tích hợp 21 kỹ năng chuyên biệt dành cho AI (Claude Code Skills), giúp các tác nhân AI hiểu và sáng tạo nội dung đúng theo quy chuẩn của thế giới Cố Nguyên.

Các kỹ năng tiêu biểu:
- `/the-gioi`: Thiết kế địa lý và hệ sinh thái.
- `/nhan-vat`: Khởi tạo nhân vật với metadata YAML chuẩn hóa.
- `/chuong-truyen`: Sáng tác chương truyện dựa trên cốt truyện có sẵn.
- `/kiem-duyet`: Kiểm tra tính nhất quán và chất lượng nội dung.
- *(Xem chi tiết trong `.claude/skills/`)*

---

## 🛠️ Nền Tảng Kỹ Thuật (Technical Stack)

- **Ngôn ngữ chính**: Vietnamese (Tiếng Việt) cho nội dung thế giới.
- **Metadata**: YAML Frontmatter cho cấu trúc dữ liệu.
- **Frontend**: HTML/Vanilla JS, CSS (Custom Reader).
- **Automation**: Scripts Python & Node.js (`scripts/`) để đồng bộ dữ liệu, kiểm tra liên kết và quản lý mục lục.
- **AI Tooling**: Claude Code, Jules Agents.

---

## ⚠️ Lưu Ý Cho AI Bảo Trì

Khi thực hiện cập nhật dữ liệu, các tác nhân AI **BẮT BUỘC** tuân thủ:
1. Tên tệp tin phải sử dụng tiếng Việt có dấu, khoảng trắng thay bằng dấu gạch dưới (`_`).
2. Luôn kiểm tra tính nhất quán với `HỒ_SƠ_THẾ_GIỚI.md` trước khi thêm thực thể mới.
3. Cập nhật `public/wiki-index.json` sau khi thay đổi cấu trúc tệp tin.

---
© 2026 Cố Nguyên Project. All rights reserved.
