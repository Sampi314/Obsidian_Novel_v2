# NHẬT KÝ KIỂM SOÁT CHẤT LƯỢNG

## Quy Trình Kiểm Tra
1. **Nhất quán lore** — Kiểm tra tên, cảnh giới, thế lực, sự kiện chéo giữa các file
2. **Tham chiếu lỗi** — File được nhắc nhưng không tồn tại, link hỏng
3. **Trùng lặp** — Nội dung giống nhau ở nhiều file
4. **Thiếu sót** — Nhân vật/thế lực/kỳ vật được nhắc nhưng chưa có hồ sơ riêng
5. **Hệ thống 3 ngôn ngữ** — Kiểm tra 漢字 → Hán Việt → Tiếng Việt đầy đủ

## Phiên Kiểm Tra
- *(Chưa có phiên kiểm tra nào được ghi nhận)*

## Các Vấn Đề Phổ Biến
- **"Không có tiêu đề"** trong chapter_data.js — Chương thiếu dòng H1 `# Chương N: Tên`
- **Mâu thuẫn cảnh giới** — Nhân vật được ghi cảnh giới khác nhau ở hồ sơ vs chương truyện
- **Link hỏng** — MỤC_LỤC tham chiếu file không tồn tại hoặc tên file sai dấu

## Danh Sách Kiểm Tra Nhanh
- [ ] Tất cả chương có H1 đúng format `# Chương N: Tên`
- [ ] chapter_data.js không còn "Không có tiêu đề"
- [ ] MỤC_LỤC.md khớp với file thực tế trong thư mục
- [ ] HỒ_SƠ_THẾ_GIỚI.md được cập nhật khi có nội dung mới
- [ ] Không có file .html dư thừa trong Đạo/

## TODO Cho Phiên Sau
- Chạy kiểm tra toàn diện cross-reference giữa nhân vật và chương truyện
- Kiểm tra tính nhất quán timeline sự kiện
- Xác minh tất cả công pháp/kỹ năng được ghi nhận đúng cảnh giới
