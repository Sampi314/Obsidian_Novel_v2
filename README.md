# 🌌 Hệ Thống Kiến Tạo Thế Giới Tiên Hiệp "Cố Nguyên"

> [!IMPORTANT]
> **TRẠNG THÁI: KHO LƯU TRỮ CÁ NHÂN (PRIVATE REFERENCE ARCHIVE)**
> Đây là dự án kiến tạo thế giới (world-building) cá nhân. Kho lưu trữ này đóng vai trò là cơ sở dữ liệu sống cho việc sáng tác và phát triển nội dung Tiên Hiệp với sự hỗ trợ của AI. **Chúng tôi không tiếp nhận đóng góp (Pull Requests/Issues) từ bên ngoài.**

---

## 📜 Giới Thiệu (Lore Summary)

"Cố Nguyên" là một đại thế giới tu chân cổ đại, nơi linh khí bắt nguồn từ thuở hỗn mang. Dự án này hệ thống hóa toàn bộ quy luật, thực thể và lịch sử của thế giới này, từ những cảnh giới tu luyện huyền vi đến những âm mưu tranh đấu giữa các đại tông môn.

Mục tiêu của dự án là xây dựng một hệ sinh thái dữ liệu chặt chẽ, cho phép các tác nhân AI (AI Agents) và tác giả cùng phối hợp để tạo ra những chương truyện có tính nhất quán cao về logic thế giới.

### 📊 Quy Mô Hiện Tại

| Hạng mục | Số lượng |
|----------|----------|
| Chương truyện | 700+ |
| Hồ sơ nhân vật | 600+ |
| Thế lực / Tổ chức | 200+ |
| Góc nhìn (POV) | 21+ nhân vật trải dài 5 khu vực + Thiên Trụ |
| AI Skills | 21 kỹ năng chuyên biệt |

**5 khu vực chính:** Nam Cương · Bắc Băng · Đông Hoang · Vô Tận Hải · Tây Mạc — cùng Thiên Trụ trung tâm.

---

## 📖 Trình Đọc Tương Tác (Interactive Reader)

Hệ thống sử dụng kiến trúc **Markdown-first** — không có tệp HTML chương truyện. Mọi nội dung được viết dưới dạng Markdown với YAML frontmatter, và `reader.html` là bộ engine hiển thị duy nhất, render trực tiếp từ file `.md`.

Dựa vào trường `type` trong YAML frontmatter, trình đọc tự động thay đổi giao diện:

- **`type: character`**: Hồ sơ nhân vật với biểu đồ radar tư chất, dòng thời gian đại cảnh và thanh trạng thái cảm xúc.
- **`type: faction`**: Hồ sơ thế lực với sơ đồ phân chia bộ viện, thanh quan hệ ngoại giao và bản đồ lãnh thổ.
- **Chapter files**: Trình đọc chương truyện chuyên dụng với hệ thống điều hướng thông minh và trình phát TTS.

### 🔊 Text-to-Speech (TTS)

- **Web Speech API** (`window.speechSynthesis`) — có sẵn trong trình duyệt, không cần cài đặt.
- **Edge TTS Server** (tùy chọn) — `python3 scripts/edge_tts_server.py` trên port 5050, tự động phát hiện khi khởi tạo. 2 giọng đọc: HoaiMy (Nữ), NamMinh (Nam).

### 🎨 Chủ đề (Themes)

5 themes: **Thủy Mạc** (Ink) · **Huyết Nguyệt** (Blood Moon) · **Thanh Trúc** (Bamboo) · **Bạch Tuyết** (Snow) · **Cổ Thư** (Ancient Tome).

### 🔗 Biểu Đồ Quan Hệ

`relationship.html` — Trình xem đồ thị quan hệ nhân vật tương tác, hiển thị mạng lưới liên kết giữa các nhân vật trong thế giới Cố Nguyên.

**[👉 Truy cập Mục Lục Tổng Hợp](https://sampi314.github.io/Obsidian_Novel_v2/index.html)**

---

## 🗂️ Phân Loại Dữ liệu (World Taxonomy)

Toàn bộ tri thức về thế giới được tổ chức trong thư mục `Đạo/`:

- **`Nhân_Vật/`**: Hồ sơ chi tiết về các tu sĩ, yêu ma và phàm nhân (600+ hồ sơ).
- **`Thế_Lực/`**: Hệ thống tông môn, gia tộc và triều đình (200+ thực thể).
- **`Công_Pháp/`**: Bí kíp tu luyện, thần thông và chiêu thức.
- **`Thế_Giới_Và_Thời_Gian/`**: Địa lý, lịch sử và dòng thời gian vạn năm.
- **`Tu_Luyện/`**: Hệ thống cảnh giới và quy luật thiên đạo.
- **`Chương_Truyện/`**: 700+ chương truyện chia theo góc nhìn nhân vật.
- ... và các hạng mục khác như Đan Dược, Luyện Khí, Trận Pháp, Phù Lục, Thơ Ca, Âm Nhạc.

---

## 🤖 Kỹ Năng Claude Code (AI Skills)

Dự án tích hợp **21 kỹ năng chuyên biệt** dành cho AI (Claude Code Skills), giúp các tác nhân AI hiểu và sáng tạo nội dung đúng theo quy chuẩn của thế giới Cố Nguyên.

| Lệnh | Chức năng |
|-------|-----------|
| `/the-gioi` | Thiết kế địa lý, khí hậu, hệ sinh thái và thiên đạo |
| `/chung-toc` | Quản lý 9 chủng tộc trong thế giới |
| `/nhan-vat` | Khởi tạo và phát triển hồ sơ nhân vật (YAML frontmatter) |
| `/van-hoa` | Thiết kế phong tục, tín ngưỡng, lễ hội và truyền thống |
| `/the-luc` | Thiết kế tông môn, gia tộc và tổ chức chính trị |
| `/tu-luyen` | Thiết kế cảnh giới tu luyện, kiếp nạn và tâm ma |
| `/cong-phap` | Thiết kế công pháp, võ thuật và bí thuật |
| `/bi-tich` | Chuyển đổi nội dung sang văn phong cổ tịch |
| `/dan-duoc` | Tạo đan phương, dược liệu và công thức luyện đan |
| `/luyen-khi` | Thiết kế vũ khí, linh bảo và hệ thống đúc rèn |
| `/tran-phap` | Thiết kế trận pháp, kết giới và phong ấn |
| `/phu-luc` | Thiết kế phù lục, phù văn và ấn ký |
| `/ky-vat` | Thiết kế linh vật, thần thú và kỳ vật |
| `/thoi-gian` | Quản lý dòng thời gian tổng và ngăn ngừa nghịch lý |
| `/tho-ca` | Sáng tác thơ cổ phong, phú, từ và văn chương |
| `/am-nhac` | Sáng tác lời nhạc và prompt Suno AI cho nhạc tiên hiệp |
| `/hanh-dong` | Biên đạo cảnh chiến đấu và hành động chi tiết |
| `/chuong-truyen` | Sáng tác chương truyện theo hệ thống vòng xoay |
| `/kiem-duyet` | Kiểm tra logic, tính nhất quán và liên tục |
| `/hoa-si` | Tạo prompt hình ảnh AI cho nhân vật, cảnh và pháp khí |
| `/quan-he` | Xây dựng biểu đồ quan hệ (Mermaid, JSON, HTML) |

---

## 🛠️ Nền Tảng Kỹ Thuật (Technical Stack)

- **Kiến trúc**: Markdown-first — nội dung sáng tác hoàn toàn bằng Markdown, render bởi `reader.html`.
- **Ngôn ngữ chính**: Vietnamese (Tiếng Việt) cho nội dung thế giới.
- **Metadata**: YAML Frontmatter cho cấu trúc dữ liệu.
- **Frontend**: HTML / Vanilla JS / CSS (Custom Reader, 5 themes).
- **TTS**: Web Speech API + Edge TTS server tùy chọn (port 5050).
- **Automation**: Scripts Python & Node.js (`scripts/`) để đồng bộ dữ liệu, kiểm tra liên kết và quản lý mục lục.
- **AI Tooling**: Claude Code (21 skills), Jules Agents.
- **Deployment**: GitHub Pages — [sampi314.github.io/Obsidian_Novel_v2](https://sampi314.github.io/Obsidian_Novel_v2/).

---

## ⚠️ Lưu Ý Cho AI Bảo Trì

Khi thực hiện cập nhật dữ liệu, các tác nhân AI **BẮT BUỘC** tuân thủ:
1. Tên tệp tin phải sử dụng tiếng Việt có dấu, khoảng trắng thay bằng dấu gạch dưới (`_`).
2. Luôn kiểm tra tính nhất quán với `HỒ_SƠ_THẾ_GIỚI.md` trước khi thêm thực thể mới.
3. Kiểm tra `locked_chapters.json` trước khi chỉnh sửa bất kỳ chương truyện nào trong `Đạo/Chương_Truyện/`.

---
© 2026 Cố Nguyên Project. All rights reserved.
