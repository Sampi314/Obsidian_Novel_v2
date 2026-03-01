# Hướng Dẫn Đóng Góp (Contributing Guidelines)

Cảm ơn bạn đã quan tâm đến việc đóng góp cho dự án "Cố Nguyên"! Chúng tôi hoan nghênh mọi sự đóng góp từ cộng đồng để xây dựng thế giới Tiên Hiệp này ngày càng phong phú.

Vui lòng dành chút thời gian đọc qua các hướng dẫn sau đây để quá trình đóng góp diễn ra thuận lợi.

## ⚙️ Quy Trình Đóng Góp (Contribution Workflow)

Để đảm bảo tính nhất quán và chất lượng của dự án, vui lòng tuân thủ quy trình sau:

1.  **Đọc Hồ Sơ Thế Giới:**
    *   Trước khi bắt đầu, hãy đọc kỹ **[Hồ Sơ Thế Giới (World Profile)](Đạo/Hồ_Sơ_Thế_Giới.md)** để nắm vững bối cảnh, lịch sử và các quy tắc của thế giới "Cố Nguyên". Điều này giúp tránh các mâu thuẫn trong cốt truyện hoặc thiết lập.

2.  **Thực Thi (Execute):**
    *   Sử dụng các công cụ có sẵn để tạo nội dung mới hoặc chỉnh sửa nội dung hiện có.
    *   Đảm bảo nội dung mới phù hợp với văn phong Tiên Hiệp và logic của thế giới.

3.  **Lưu Trữ (Store):**
    *   Lưu Tệp Tin vào đúng thư mục con trong `Đạo/` tương ứng với loại nội dung:
        *   `Đạo/Nhân_Vật/`: Hồ sơ nhân vật.
        *   `Đạo/Thế_Lực/`: Tông môn, tổ chức.
        *   `Đạo/Công_Pháp/`: Bí kíp, công pháp.
        *   `Đạo/Chủng_Tộc/`: Các chủng tộc.
        *   `Đạo/Kỳ_Vật/`, `Đạo/Đan_Dược/`, `Đạo/Luyện_Khí/`: Vật phẩm, tài nguyên.
        *   `Đạo/Chương_Truyện/`: Bản thảo chương truyện.

4.  **Quy Tắc Đặt Tên Tệp Tin:**
    *   Tên Tệp Tin **bắt buộc** phải là **Tiếng Việt có dấu**.
    *   Thay thế tất cả khoảng trắng (spaces) bằng dấu gạch dưới `_`.
    *   Ví dụ: `Đạo/Nhân_Vật/Lâm_Phong.md`, `Đạo/Công_Pháp/Băng_Tâm_Quyết.md`.

5.  **Cập Nhật (Cập Nhật):**
    *   Sau khi thêm Tệp Tin mới, hãy cập nhật tóm tắt nội dung hoặc liên kết vào `Đạo/Hồ_Sơ_Thế_Giới.md` nếu cần thiết để mọi người dễ dàng theo dõi.

## 🔧 Cài Đặt Môi Trường (Setup)

Dự án sử dụng tên Tệp Tin tiếng Việt, điều này có thể gây ra lỗi hiển thị trên một số cấu hình Git (ví dụ: tên Tệp Tin bị mã hóa thành `\\304\\220...`).

Để khắc phục, hãy chạy lệnh sau trong thư mục gốc của dự án:

```bash
bash scripts/setup_git.sh
```

Hoặc cấu hình thủ công:

```bash
git config core.quotePath false
```

## 🐛 Báo Cáo Lỗi (Reporting Issues)

Nếu bạn phát hiện lỗi logic, sai sót chính tả, hoặc vấn đề kỹ thuật:
*   Hãy mở một **Issue** trên GitHub.
*   Mô tả rõ ràng vấn đề và vị trí (tên Tệp Tin, dòng) để chúng tôi dễ dàng khắc phục.

## 📝 Pull Requests

*   Chúng tôi khuyến khích các Pull Request (PR) nhỏ và tập trung vào một vấn đề cụ thể.
*   Mô tả chi tiết những thay đổi bạn đã thực hiện trong PR.
*   Đảm bảo các liên kết trong bài viết hoạt động chính xác.

Cảm ơn sự đóng góp của bạn!
