# 🛡️ Chính Sách Bảo Mật — Dự Án Cố Nguyên

Đây là dự án sáng tạo nội dung văn học Tiên Hiệp "Cố Nguyên Giới", được triển khai dưới dạng GitHub Pages với hệ thống frontend (HTML/JS), script tự động hóa (Python/Node.js), và AI agent skills. Mặc dù không phải ứng dụng web truyền thống, dự án vẫn có bề mặt tấn công cần được bảo vệ.

---

## 📞 Báo Cáo Vấn Đề Bảo Mật

Nếu bạn phát hiện bất kỳ vấn đề nào liên quan đến bảo mật (ví dụ: lộ thông tin cá nhân, script có hành vi bất thường, XSS trong reader, lỗ hổng trong workflow), vui lòng thực hiện các bước sau:

1.  **KHÔNG** mở Issue công khai trên GitHub để tránh rủi ro.
2.  Gửi báo cáo chi tiết trực tiếp đến quản trị viên qua email: **nkhoihue@gmail.com**.
3.  Chúng tôi sẽ phản hồi và xử lý vấn đề trong thời gian sớm nhất có thể.

---

## 🤖 An Toàn AI Agent

Dự án sử dụng nhiều AI agent (Claude Code, Jules) để hỗ trợ viết và bảo trì nội dung. Các biện pháp bảo vệ:

### Hệ thống khóa chương (`locked_chapters.json`)
*   Các chương đã xuất bản được đánh dấu trong `locked_chapters.json` — AI agent **KHÔNG ĐƯỢC** chỉnh sửa những chương này.
*   File `locked_chapters.json` chỉ được quản lý bởi tác giả thông qua web UI (chapter-lock system).
*   GitHub Actions workflow `protect-locked-chapters.yml` kiểm tra và chặn mọi PR cố gắng sửa đổi chương đã khóa.

### AI agent skills (`.claude/skills/`)
*   Các skill file định nghĩa hành vi của agent khi tạo nội dung mới (nhân vật, chương truyện, thế lực, v.v.).
*   Skill output phải tuân theo template chuẩn — đảm bảo tính nhất quán dữ liệu.
*   Tất cả skill nằm trong `.claude/skills/` và được version control cùng repo.

### Quy tắc agent
*   Agent phải kiểm tra `locked_chapters.json` trước khi chỉnh sửa bất kỳ file nào trong `Đạo/Chương_Truyện/`.
*   Agent không được tự ý thay đổi `CLAUDE.md`, `locked_chapters.json`, hoặc GitHub Actions workflows.

---

## 🌐 Frontend & XSS

Dự án triển khai trên GitHub Pages với các file HTML tĩnh (`index.html`, `reader.html`, `relationship.html`).

### Xử lý Markdown (`reader.html`)
*   `reader.html` sử dụng thư viện [marked.js](https://github.com/markedjs/marked) (v12.0.2) để render Markdown thành HTML.
*   Nội dung Markdown được load từ chính repo (fetch nội bộ) — không nhận input trực tiếp từ người dùng.
*   HTML được chèn qua `innerHTML` — do nguồn dữ liệu là file `.md` trong repo (do tác giả kiểm soát), rủi ro XSS thấp.
*   **Khuyến nghị:** Nếu mở rộng để nhận nội dung từ bên ngoài trong tương lai, cần bổ sung sanitizer (ví dụ: DOMPurify).

### Dữ liệu frontend
*   `scripts/chapter_data.js` — dữ liệu chương, được tự động sinh bởi `update_chapter_data.py`.
*   `scripts/relationship_data.js` — dữ liệu quan hệ nhân vật.
*   `scripts/navigation.js` — điều hướng reader.
*   Các file JS này là dữ liệu tĩnh, không xử lý input người dùng.

---

## 🔊 TTS Server (Edge TTS)

*   Script `scripts/edge_tts_server.py` chạy server HTTP cục bộ trên **port 5050**.
*   Server này **chỉ dành cho môi trường phát triển local** — không có cơ chế xác thực (authentication).
*   **KHÔNG triển khai TTS server lên môi trường public** — nó được thiết kế để chạy trên `localhost` duy nhất.
*   2 giọng đọc Edge: HoaiMy (Nữ), NamMinh (Nam).
*   Nếu TTS server không chạy, hệ thống tự động fallback sang Web Speech API của trình duyệt.

---

## 🚀 GitHub Pages & Deployment

*   Dự án được triển khai tĩnh qua GitHub Pages — không có backend, database, hay API server.
*   GitHub Actions workflows:
    *   `update-chapter-data.yml` — tự động cập nhật `chapter_data.js` khi có thay đổi chương.
    *   `protect-locked-chapters.yml` — chặn PR chỉnh sửa chương đã khóa.
    *   `auto-merge.yml` — tự động merge PR đủ điều kiện.
*   **Không lưu trữ secret hay credentials trong repo.** Mọi biến nhạy cảm (nếu có) sử dụng GitHub Secrets.
*   Tất cả nội dung trên GitHub Pages là **công khai** — không đặt thông tin cá nhân hoặc nhạy cảm trong các file Markdown.

---

## ⚠️ Cảnh Báo Về Script Tự Động

Kho lưu trữ chứa nhiều script hỗ trợ bảo trì trong `scripts/`:

### Python scripts
*   Quản lý chương: `migrate_chapters.py`, `reindex_chapters.py`, `shift_chapters.py`, `update_chapter_data.py`
*   Quản lý nhân vật: `batch_create_chars.py`, `create_chars_*.py`, `fill_chars_*.py`
*   Kiểm tra chất lượng: `check_links.py`, `find_english.py`, `compact_quality.py`
*   Sửa lỗi hàng loạt: `fix_html.py`, `fix_english_terms.py`, `fix_exclamation.py`

### Node.js scripts
*   `chapter_data.js`, `navigation.js`, `tts_player.js` — frontend scripts chạy trong trình duyệt.
*   `chapter-lock.js`, `character-sheet.js`, `faction-sheet.js` — UI components.
*   `generate_wiki_index.mjs` — sinh dữ liệu wiki index.

### ⚠️ Lưu ý khi thực thi
*   Các script được thiết kế để chạy trong **môi trường phát triển nội bộ**.
*   Người dùng bên ngoài **nên kiểm tra kỹ nội dung script** trước khi thực thi trên hệ thống cá nhân.
*   Chỉ sử dụng các script được cung cấp chính thức trong nhánh `main` của kho lưu trữ này.
*   Một số script Python thao tác trực tiếp lên file system (đọc/ghi/di chuyển file `.md`) — chạy sai tham số có thể gây mất dữ liệu.

---

## 📚 Toàn Vẹn Dữ Liệu

### Nguồn sự thật duy nhất (Single Source of Truth)
*   `Đạo/HỒ_SƠ_THẾ_GIỚI.md` là **nguồn sự thật duy nhất** cho toàn bộ worldbuilding của Cố Nguyên Giới.
*   Mọi nội dung khác (chương truyện, hồ sơ nhân vật, thế lực) phải nhất quán với file này.
*   AI agent và tác giả đều phải tham chiếu `HỒ_SƠ_THẾ_GIỚI.md` khi tạo hoặc kiểm tra nội dung.

### Quy trình bảo vệ nội dung
*   Chương truyện đã xuất bản → khóa qua `locked_chapters.json` → bảo vệ bởi GitHub Actions.
*   Dữ liệu frontend (`chapter_data.js`) được sinh tự động — không chỉnh sửa thủ công.
*   Mọi thay đổi lớn nên đi qua Pull Request để có lịch sử kiểm tra.

---

Cảm ơn bạn đã quan tâm đến sự an toàn của dự án! 🙏
