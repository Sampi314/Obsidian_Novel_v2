# 🌌 THIÊN ĐẠO TỰ VẬN — Cố Nguyên Thế Giới Tự Tiến Hóa 🔮

*~ Khi trời đất vận hành, vạn vật tự sinh ~*

## 🧿 THIÊN MỆNH

Bạn đang chạy như một tác vụ tự động theo lịch trình. Không có người dùng để hỏi. Bạn phải tự đọc, đánh giá, quyết định và hành động mỗi lần chạy.

**Bước đầu tiên luôn là:** Đọc `.jules/INSTRUCTIONS.md` — đây là nguồn sự thật duy nhất cho tất cả cấu hình, quy tắc, và hướng dẫn cụ thể. Mọi thông tin về agent, quy trình, thứ tự viết chương, cấu trúc dự án đều nằm trong đó.

---

## 🪷 GIAI ĐOẠN 1: KHỞI ĐỘNG

1. Đọc `.jules/INSTRUCTIONS.md` — đặc biệt phần **TRẠNG THÁI HIỆN TẠI** ở đầu file để biết chính xác phải làm gì.
2. Đọc `Đạo/HỒ_SƠ_THẾ_GIỚI.md` — nắm bắt trạng thái hiện tại của thế giới.
3. Đọc `.jules_memory/` — kiểm tra ghi chú phiên trước, TODO, và công việc dở dang.
4. Đọc `Đạo/BÁO_CÁO_CHẤT_LƯỢNG.md` — kiểm tra các vấn đề tồn đọng.

---

## 🔥 GIAI ĐOẠN 2: ĐÁNH GIÁ & ƯU TIÊN

Quét toàn bộ cây thư mục `Đạo/` và đánh giá những gì đã có so với những gì còn thiếu. Chấm điểm:

| Ưu Tiên | Điều Kiện |
|---------|-----------|
| 🔴 Nghiêm trọng | Ghi chú trong phần TRẠNG THÁI HIỆN TẠI của INSTRUCTIONS.md |
| 🟠 Cao | Tham chiếu lỗi — nội dung được nhắc đến nhưng file không tồn tại |
| 🟠 Cao | Hệ thống cốt lõi chỉ có file khung cần bổ sung chi tiết |
| 🟡 Trung bình | Nội dung hiện có nhưng thiếu chiều sâu hoặc tham chiếu chéo |
| 🟢 Thấp | Đánh bóng — nâng cao chất lượng văn phong, thêm văn vẻ |

**Quy tắc quyết định:**
- Nếu phiên trước để lại TODO trong `.jules_memory/` hoặc INSTRUCTIONS.md, tiếp tục công việc đó.
- Xử lý mục 🟠 Cao trước mục 🟡 Trung bình.
- Ưu tiên chiều sâu hơn chiều rộng — hoàn thiện một thứ tốt hơn là chạm vào năm thứ qua loa.
- **QUAN TRỌNG:** Không mặc định viết chương — xem Cây Quyết Định ở Giai Đoạn 3.

---

## ⚡ GIAI ĐOẠN 3: THỰC THI — CÂY QUYẾT ĐỊNH

**KHÔNG được mặc định viết chương.** Viết chương chỉ là MỘT trong nhiều loại công việc. Thực hiện theo đúng thứ tự ưu tiên sau:

### ƯU TIÊN 1: Kiểm tra Lỗ Hổng Thế Giới (World-Building Gaps)
Quét các thư mục sau và kiểm tra file nào chỉ có khung / thiếu nội dung:
- `Đạo/Nhân_Vật/` — Có nhân vật được nhắc đến trong chương nhưng chưa có hồ sơ?
- `Đạo/Thế_Lực/` — Có tông môn/gia tộc xuất hiện trong truyện nhưng chưa có file?
- `Đạo/Chủng_Tộc/` — Có chủng tộc được nhắc nhưng chưa được xây dựng?
- `Đạo/Công_Pháp/` — Có công pháp xuất hiện trong chương nhưng chưa có bí tịch?
- `Đạo/Tu_Luyện/` — Hệ thống cảnh giới có đầy đủ không?
- `Đạo/Thế_Giới_Và_Thời_Gian/` — Có địa điểm mới cần bổ sung?

**Nếu tìm thấy lỗ hổng** → Kích hoạt Agent tương ứng (đọc `.jules/[Agent].md`) → Tạo nội dung → DỪNG (không viết chương phiên này).

### ƯU TIÊN 2: Kiểm Soát Chất Lượng
Đọc `Đạo/BÁO_CÁO_CHẤT_LƯỢNG.md`. Nếu có vấn đề chưa giải quyết:
- Mâu thuẫn lore → Sửa file liên quan
- Nhân vật thiếu chiều sâu → Kích hoạt Agent Nhân Vật bổ sung
- Timeline lỗi → Kích hoạt Agent Thời Gian
- Chương chất lượng thấp → Viết lại chương đó (KHÔNG phải viết chương mới)

**Nếu có vấn đề chất lượng** → Sửa chữa → DỪNG.

### ƯU TIÊN 3: Cập Nhật Quan Hệ & Dữ Liệu
Kiểm tra `scripts/relationship_data.js`:
- Có nhân vật mới chưa được thêm vào?
- Có quan hệ mới hình thành trong các chương gần đây chưa được cập nhật?
- Biểu đồ Mermaid trong `Đạo/Nhân_Vật/Quan_Hệ/` có cần cập nhật?

**Nếu dữ liệu quan hệ lỗi thời** → Kích hoạt Agent Quan Hệ → Cập nhật → Có thể kết hợp với viết chương nếu còn thời gian.

### ƯU TIÊN 4: Viết Chương (CHỈ KHI CÁC ƯU TIÊN TRÊN ĐỀU ỔN)
Chỉ khi:
- ✅ Không có lỗ hổng thế giới
- ✅ Không có vấn đề chất lượng tồn đọng
- ✅ Dữ liệu quan hệ đã cập nhật

Thì mới viết chương theo quy tắc trong `.jules/INSTRUCTIONS.md` (Bước A-D: kiểm tra tiến độ → catch-up → vòng xoay).

### QUY TẮC KÍCH HOẠT AGENT
Mỗi Agent khi kích hoạt:
1. Đọc file skill từ `.jules/[Tên_Agent].md`
2. Đọc bộ nhớ từ `.jules_memory/` (nếu có)
3. Tuân thủ đúng quy trình nội bộ của Agent
4. Lưu kết quả vào đúng thư mục con trong `Đạo/`

### TỶ LỆ PHÂN BỔ CÔNG VIỆC KHUYẾN NGHỊ
Để đảm bảo thế giới được xây dựng song song với cốt truyện:
- **3/5 phiên:** Viết chương (nếu không có vấn đề tồn đọng)
- **1/5 phiên:** World-building (nhân vật, thế lực, công pháp, địa lý)
- **1/5 phiên:** Chất lượng & dữ liệu (kiểm duyệt, quan hệ, timeline)

Ghi nhớ phiên gần nhất đã làm gì vào `.jules_memory/` để đảm bảo xoay vòng đúng tỷ lệ.

---

## 📜 GIAI ĐOẠN 4: LƯU TRỮ & CẬP NHẬT

Sau khi hoàn thành công việc:

1. 💾 **Lưu kết quả** vào đúng thư mục con trong `Đạo/` với tên file Tiếng Việt có dấu (dấu + gạch_dưới).
2. 🌐 **Cập nhật `Đạo/HỒ_SƠ_THẾ_GIỚI.md`** — thêm/cập nhật mục tóm tắt cho mọi thứ đã tạo hoặc chỉnh sửa.
3. 📖 **Cập nhật `MỤC_LỤC.md`** — nếu tạo chương mới, thêm link vào `Đạo/Chương_Truyện/[Góc_Nhìn]/MỤC_LỤC.md`.
4. 🧠 **Ghi bộ nhớ Agent** vào `.jules_memory/` — ghi lại: công việc phiên này, TODO phiên sau.
5. 📋 **Cập nhật `Đạo/BÁO_CÁO_CHẤT_LƯỢNG.md`** — ghi log.
6. 📊 **Cập nhật frontend** — xem hướng dẫn trong INSTRUCTIONS.md (Bước 5: Cập Nhật Frontend).
7. 📌 **Cập nhật TRẠNG THÁI HIỆN TẠI** trong `.jules/INSTRUCTIONS.md` — BẮT BUỘC (xem Bước 6 trong INSTRUCTIONS).

---

## 🏮 GIAI ĐOẠN 5: BÁO CÁO PHIÊN

Tạo commit với thông điệp:

```
🌌 [Tổng Quản] <ngày> — <tóm tắt ngắn>

⚡ Agent đã kích hoạt: <danh sách>
📋 Loại công việc: <World-Building / Viết Chương / Chất Lượng / Dữ Liệu>
✨ Đã tạo mới: <file mới>
🔄 Đã cập nhật: <file chỉnh sửa>
🔮 Ưu tiên tiếp theo: <việc cần làm phiên sau>
```

---

## 🧹 TỰ ĐỘNG NÉN DỮ LIỆU (AUTO-COMPACT)

Để tránh tràn bộ nhớ, mỗi phiên PHẢI thực hiện:

### Nén `.jules_memory/`
- Mỗi file bộ nhớ Agent **KHÔNG được vượt quá 200 dòng**.
- Nếu file bộ nhớ dài hơn 200 dòng:
  1. Giữ lại 50 dòng gần nhất (phiên gần nhất)
  2. Tóm tắt tất cả nội dung cũ hơn thành **1 đoạn tổng hợp** (max 30 dòng) đặt ở đầu file
  3. Xóa chi tiết cũ — chỉ giữ bài học quan trọng và quyết định lớn
- Định dạng tóm tắt:
  ```
  ## TỔNG HỢP LỊCH SỬ (tự động nén)
  - [Ngày]: [Tóm tắt 1 dòng]
  - ...

  ## PHIÊN GẦN NHẤT
  [Chi tiết đầy đủ]
  ```

### Nén `Đạo/BÁO_CÁO_CHẤT_LƯỢNG.md`
- Giữ lại **10 báo cáo gần nhất**.
- Các báo cáo cũ hơn → tóm tắt thành 1 dòng mỗi báo cáo trong phần "Lịch Sử".
- Xóa các mục đã giải quyết hoàn toàn.

### Nén TRẠNG THÁI HIỆN TẠI (trong INSTRUCTIONS.md)
- Phần Ưu Tiên: chỉ giữ 3 mục, xóa mục đã hoàn thành.
- Phần Ghi Chú: xóa ghi chú đã xử lý.

---

## 🚫 THIÊN QUY CẤM LUẬT

1. **KHÔNG** xóa hoặc ghi đè nội dung hiện có mà không có lý do chính đáng.
2. **KHÔNG** mâu thuẫn với `HỒ_SƠ_THẾ_GIỚI.md`.
3. **KHÔNG** tạo nội dung nông cạn/chung chung.
4. **KHÔNG** lặp lại cùng một sai lầm.
5. **LUÔN** kiểm tra trạng thái thực tế của file trước khi hành động.
6. **GIỚI HẠN** mỗi lần chạy tối đa 2–3 nhiệm vụ tập trung. Chất lượng hơn số lượng.
7. **LUÔN** đọc `.jules/INSTRUCTIONS.md` trước mọi hành động — đó là nguồn cấu hình duy nhất.
8. **LUÔN** chạy auto-compact trước khi kết thúc phiên.
