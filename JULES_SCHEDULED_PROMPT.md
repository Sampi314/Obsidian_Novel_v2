# 🌌 THIÊN ĐẠO TỰ VẬN — Cố Nguyên Thế Giới Tự Tiến Hóa 🔮

*~ Khi trời đất vận hành, vạn vật tự sinh ~*

## 🧿 THIÊN MỆNH

Bạn đang chạy như một tác vụ tự động theo lịch trình. Không có người dùng để hỏi. Bạn phải tự đọc, đánh giá, quyết định và hành động mỗi lần chạy.

Bắt đầu bằng cách đọc `.jules/INSTRUCTIONS.md` để hiểu vai trò Tổng Quản và hệ thống 19 Agent.

⚠️ **LƯU Ý QUAN TRỌNG:** Giữa các lần chạy, người dùng có thể đã:
- Xóa file mà họ không hài lòng — điều này có nghĩa là nội dung đó cần được làm lại tốt hơn
- Chỉnh sửa file trực tiếp — những thay đổi của người dùng là ưu tiên tối cao, luôn tôn trọng
- Thêm ghi chú/comment vào file — đây là chỉ dẫn trực tiếp cần thực hiện
- Đổi tên hoặc di chuyển file — cập nhật tham chiếu cho phù hợp

Bạn **KHÔNG BAO GIỜ** ghi đè những thay đổi của người dùng. Bản sửa của người dùng luôn đúng.

---

## 🏗️ KIẾN TRÚC HỆ THỐNG (CẬP NHẬT)

Website sử dụng kiến trúc mới — **KHÔNG CÒN tạo file HTML**:

- **`reader.html`** — Trang renderer duy nhất, đọc file `.md` qua tham số `?file=` và render bằng `marked.js`
- **`scripts/chapter_data.js`** — Dữ liệu chương, tự động cập nhật bởi GitHub Actions khi push `.md` mới
- **`scripts/navigation.js`** — Điều hướng chương, hỗ trợ cả reader mode và legacy mode
- **`scripts/tts_player.js`** — Đọc chương bằng giọng nói
- **`scripts/style.css`** — Theme cho trang chương

### ⚠️ KHÔNG BAO GIỜ:
- Tạo file `.html` cho chương hoặc wiki — `reader.html` xử lý tất cả
- Chạy `build_html.py`, `generate_index.py`, `add_navigation.py` — đã deprecated
- Tạo hoặc sửa file trong `Đạo HTML/` — thư mục này đã bị xóa

### ✅ KHI TẠO CHƯƠNG MỚI:
1. Tạo file `.md` trong `Đạo/Chương_Truyện/[Góc_Nhìn]/Chương_NNNNN_Tên_Chương.md`
2. Bắt đầu file với block NAVIGATION:
   ```
   <!-- NAVIGATION_START -->
   <div id="chapter-navigation" style="text-align: center; margin-bottom: 20px;"></div>
   <script src="../../../scripts/chapter_data.js"></script>
   <script src="../../../scripts/navigation.js"></script>
   <script src="../../../scripts/tts_player.js"></script>
   <!-- NAVIGATION_END -->
   ```
3. Tiếp theo là H1: `# Chương N: Tên Chương`
4. Cập nhật `Đạo/Chương_Truyện/[Góc_Nhìn]/MỤC_LỤC.md` — thêm link đến chương mới
5. `scripts/chapter_data.js` sẽ tự động cập nhật bởi GitHub Actions sau khi push

---

## 🪷 GIAI ĐOẠN 1: ĐỊNH HƯỚNG (Mỗi Lần Chạy)

1. Đọc `Đạo/HỒ_SƠ_THẾ_GIỚI.md` — nắm bắt trạng thái hiện tại của thế giới.
2. Đọc `.jules_memory/` — kiểm tra tất cả file bộ nhớ Agent để xem ghi chú phiên trước, TODO, và công việc dở dang.
3. Đọc `Đạo/BÁO_CÁO_CHẤT_LƯỢNG.md` — kiểm tra các vấn đề tồn đọng do Kiểm Soát Chất Lượng ghi nhận.

### 🔍 Phát Hiện Thay Đổi Của Người Dùng

Sau khi đọc bộ nhớ, so sánh trạng thái thực tế với trạng thái ghi nhớ:

- **File bị xóa:** Nếu `.jules_memory/` ghi rằng file X đã được tạo nhưng file X không còn tồn tại → người dùng đã xóa vì không hài lòng. Ghi nhận vào bộ nhớ, phân tích nguyên nhân có thể (nội dung nông cạn? sai lore? không đúng giọng văn?), và tạo lại với chất lượng cao hơn nếu nội dung đó vẫn cần thiết.

- **File bị chỉnh sửa:** Nếu nội dung file khác với những gì bộ nhớ ghi nhận → người dùng đã sửa. Lấy phiên bản hiện tại của người dùng làm chuẩn. Cập nhật bộ nhớ cho phù hợp. Học hỏi từ các thay đổi để hiểu gu và tiêu chuẩn của người dùng.

- **File có ghi chú/comment:** Tìm kiếm các dấu hiệu người dùng để lại chỉ dẫn trong file:
  - Comment HTML: `<!-- TODO: ... -->` hoặc `<!-- FIX: ... -->`
  - Dấu hiệu trong text: `[TODO]`, `[SỬA]`, `[CẦN LÀM LẠI]`, `[THÊM]`, `???`, `!!!`
  - Đoạn text bị gạch ngang hoặc highlight
  - Bất kỳ ghi chú nào bằng Tiếng Việt hoặc Tiếng Anh mang tính chỉ dẫn
  → Thực hiện theo chỉ dẫn đó như một nhiệm vụ ưu tiên cao.

- **File mới xuất hiện:** Nếu có file mới mà bộ nhớ không ghi nhận → người dùng tự tạo. Đọc, ghi nhận vào `HỒ_SƠ_THẾ_GIỚI.md` nếu chưa có, và đảm bảo các nội dung khác nhất quán với file mới này.

---

## 🔥 GIAI ĐOẠN 2: ĐÁNH GIÁ & ƯU TIÊN

Quét toàn bộ cây thư mục `Đạo/` và đánh giá những gì đã có so với những gì còn thiếu hoặc chưa phát triển. Chấm điểm từng mảng:

| Ưu Tiên | Điều Kiện |
|---------|-----------|
| 🔴 Nghiêm trọng | Chỉ dẫn trực tiếp từ người dùng (comment, ghi chú, TODO trong file) |
| 🔴 Nghiêm trọng | File bị người dùng xóa cần làm lại tốt hơn |
| 🟠 Cao | Tham chiếu lỗi — nội dung được nhắc đến nhưng file không tồn tại |
| 🟠 Cao | Hệ thống cốt lõi chỉ có file khung cần bổ sung chi tiết |
| 🟡 Trung bình | Nội dung hiện có nhưng thiếu chiều sâu, chi tiết, hoặc tham chiếu chéo |
| 🟢 Thấp | Đánh bóng — nâng cao chất lượng văn phong, thêm văn vẻ, thơ ca, âm nhạc đi kèm |

**Quy tắc quyết định:**
- Chỉ dẫn của người dùng luôn là ưu tiên số 1 — bất kể mức độ nghiêm trọng của các vấn đề khác.
- Nếu người dùng xóa file, hiểu đó là phản hồi tiêu cực và cải thiện khi tạo lại.
- Nếu không có chỉ dẫn người dùng, xử lý mục 🟠 Cao trước.
- Nếu phiên trước để lại TODO trong `.jules_memory/`, tiếp tục công việc đó (trừ khi người dùng đã xóa kết quả liên quan).
- Nếu mọi thứ đều ổn, chạy Kiểm Soát Chất Lượng (Agent 19) để kiểm tra toàn diện.
- Ưu tiên chiều sâu hơn chiều rộng — hoàn thiện một thứ tốt hơn là chạm vào năm thứ qua loa.

---

## ⚡ GIAI ĐOẠN 3: THỰC THI

### 📋 QUY TẮC VIẾT CHƯƠNG — THỨ TỰ BẮT BUỘC

Khi viết chương truyện, **PHẢI** tuân thủ quy trình sau:

#### Bước 3.1: Kiểm tra tiến độ tất cả góc nhìn

Quét tất cả thư mục `Đạo/Chương_Truyện/Góc_Nhìn_*/` và đếm số chương mỗi góc nhìn:

```
Ví dụ:
  Góc_Nhìn_Chính:           134 chương
  Góc_Nhìn_Diệp_Tĩnh_Sương: 42 chương (từ chương main 90)
  Góc_Nhìn_Lâm_Phong:         3 chương (BỊ TỤT LẠI)
  Góc_Nhìn_Lệ_Vô_Tâm:      128 chương
```

#### Bước 3.2: Xác định góc nhìn bị tụt lại (CATCH-UP)

Nếu một góc nhìn phụ có **ít hơn 50% số chương** so với Góc Nhìn Chính hoặc các góc nhìn phụ khác → đó là góc nhìn cần **catch-up ưu tiên**.

**Quy tắc catch-up:**
- Góc nhìn bị tụt lại **PHẢI được viết trước** cho đến khi bắt kịp timeline hiện tại của tuyến truyện chính.
- "Bắt kịp" nghĩa là: câu chuyện của nhân vật đó đã phát triển đến mốc thời gian tương đương với tuyến chính hiện tại (kiểm tra qua `QUẢN_LÝ_ARC_TRUYỆN.md`).
- Trong thời gian catch-up, **mỗi lần chạy chỉ viết cho góc nhìn bị tụt**, không viết góc nhìn khác.

#### Bước 3.3: Sau khi tất cả góc nhìn đã cân bằng — Viết theo danh sách xoay vòng

Khi tất cả góc nhìn đã cân bằng (timeline tương đương), viết chương theo thứ tự **xoay vòng cố định**:

```
1. Góc Nhìn Chính          (2 chương)
2. Góc Nhìn Lệ Vô Tâm     (1 chương)
3. Góc Nhìn Chính          (2 chương)
4. Góc Nhìn Diệp Tĩnh Sương (1 chương)
5. Góc Nhìn Chính          (2 chương)
6. Góc Nhìn Lâm Phong      (1 chương)
7. (Lặp lại từ bước 1)
```

**Quy tắc xoay vòng:**
- Góc Nhìn Chính luôn chiếm **2 phần** trong mỗi vòng (vì là tuyến chính).
- Mỗi góc nhìn phụ chiếm **1 phần** trong vòng xoay.
- Khi có góc nhìn mới, tự động thêm vào cuối danh sách xoay vòng.
- Ghi nhớ vị trí hiện tại trong vòng xoay vào `.jules_memory/Viet_Chuong_Truyen_Ký Ức.md`.

#### Bước 3.4: Khi tạo nhân vật mới có góc nhìn riêng

Khi Agent Nhân Vật tạo nhân vật mới đủ quan trọng (xem `.jules/Nhân_Vật.md`):
1. **Tạo cơ sở hạ tầng:** Thư mục, MỤC_LỤC.md, chapter_data.js, index.html.
2. **TẠM DỪNG** vòng xoay chương hiện tại.
3. **Catch-up toàn bộ:** Viết liên tục cho góc nhìn mới cho đến khi bắt kịp timeline tuyến chính.
4. **Quay lại** vòng xoay bình thường (nhân vật mới được thêm vào danh sách xoay vòng).

---

### 🔧 Bảng Tình Huống Thực Thi

Dựa trên đánh giá, kích hoạt chuỗi Agent phù hợp:

| Tình Huống | Chuỗi Agent |
|-----------|------------|
| Góc nhìn bị tụt lại | **Ưu tiên tối cao:** Chương Truyện (viết catch-up cho góc nhìn đó) |
| Nhân vật mới cần góc nhìn | Nhân Vật → tạo cơ sở hạ tầng → Chương Truyện (catch-up) |
| Tất cả góc nhìn cân bằng | Chương Truyện (viết theo vòng xoay) → Kiểm Soát Chất Lượng |
| Người dùng để TODO/comment trong file | Agent phù hợp với nội dung file → Kiểm Soát Chất Lượng |
| Người dùng xóa file nhân vật | Phân tích lỗi cũ → Kiến Tạo Nhân Vật (làm lại tốt hơn) |
| Người dùng sửa file thế giới | Đọc bản sửa → cập nhật mọi file liên quan cho nhất quán |
| Thiếu hồ sơ chủng tộc | Kiến Tạo Chủng Tộc → Kiến Tạo Văn Hóa → Kiểm Soát Chất Lượng |
| File nhân vật chỉ có khung | Kiến Tạo Chủng Tộc + Hệ Thống Tu Luyện → Kiến Tạo Nhân Vật → Sáng Tạo Công Pháp |
| Hệ thống tu luyện chưa hoàn chỉnh | Thiết Kế Hệ Thống Tu Luyện → Sáng Tạo Công Pháp → Viết Sách Công Pháp |
| Thiếu thế lực/tông môn | Kiến Tạo Thế Giới + Văn Hóa → Xây Dựng Thế Lực |
| Lỗ hổng dòng thời gian | Quản Lý Dòng Thời Gian → kiểm tra chéo toàn bộ nội dung |
| Chưa có thơ cho vùng/sự kiện | Sáng Tác Thơ Ca |
| Chưa có nhạc cho cảnh/thời đại | Sáng Tác Âm Nhạc |
| Nội dung có nhưng chưa kiểm tra | Kiểm Soát Chất Lượng (kiểm tra toàn diện) |

Mỗi Agent khi kích hoạt:
1. Đọc file skill từ `.jules/[Tên_Agent].md`
2. Đọc bộ nhớ từ `.jules_memory/` (nếu có)
3. Tuân thủ đúng quy trình nội bộ của Agent
4. Lưu kết quả vào đúng thư mục con trong `Đạo/`

---

## 📜 GIAI ĐOẠN 4: LƯU TRỮ & CẬP NHẬT

Sau khi hoàn thành công việc:

1. 💾 **Lưu kết quả** vào đúng thư mục con trong `Đạo/` với tên file Tiếng Việt có dấu (dấu + gạch_dưới).
2. 🌐 **Cập nhật `Đạo/HỒ_SƠ_THẾ_GIỚI.md`** — thêm/cập nhật mục tóm tắt cho mọi thứ đã tạo hoặc chỉnh sửa.
3. 📖 **Cập nhật `MỤC_LỤC.md`** — nếu tạo chương mới, thêm link vào `Đạo/Chương_Truyện/[Góc_Nhìn]/MỤC_LỤC.md`.
4. 🧠 **Ghi bộ nhớ Agent** vào `.jules_memory/` — ghi lại:
   - Những gì đã làm phiên này
   - Các thay đổi của người dùng đã phát hiện và cách xử lý
   - Bài học rút ra từ file bị xóa/sửa (gu của người dùng, tiêu chuẩn chất lượng)
   - TODO cho phiên sau
5. 📋 **Cập nhật `Đạo/BÁO_CÁO_CHẤT_LƯỢNG.md`** — ghi log những gì đã tạo/chỉnh sửa và các vấn đề phát hiện.
6. 🧹 **Dọn dẹp chỉ dẫn người dùng** — nếu đã hoàn thành TODO/comment của người dùng trong file, xóa comment đó để đánh dấu đã xong.

---

## 🏮 GIAI ĐOẠN 5: BÁO CÁO PHIÊN

Tạo commit với thông điệp rõ ràng tóm tắt công việc đã thực hiện:

```
🌌 [Tổng Quản] <ngày> — <tóm tắt ngắn>

👤 Phát hiện thay đổi người dùng: <mô tả nếu có, "Không có" nếu không>
⚡ Agent đã kích hoạt: <danh sách>
✨ Đã tạo mới: <file mới>
🔄 Đã cập nhật: <file chỉnh sửa>
🗑️ Đã tạo lại (bị xóa trước đó): <file nếu có>
🔮 Ưu tiên tiếp theo: <việc cần làm phiên sau>
```

---

## 🚫 THIÊN QUY CẤM LUẬT

1. **KHÔNG BAO GIỜ** ghi đè thay đổi của người dùng. Bản sửa của người dùng là chân lý tuyệt đối.
2. **KHÔNG** xóa hoặc ghi đè nội dung hiện có mà không có lý do chính đáng. Ưu tiên mở rộng và làm phong phú thêm.
3. **KHÔNG** mâu thuẫn với `HỒ_SƠ_THẾ_GIỚI.md`. Nếu phát hiện mâu thuẫn trong các file hiện có, ghi nhận vào `BÁO_CÁO_CHẤT_LƯỢNG.md` và sửa chữa.
4. **KHÔNG** tạo nội dung nông cạn/chung chung. Mọi phần phải mang đậm chất Tiên Hiệp — cổ điển, hùng tráng, huyền ảo.
5. **KHÔNG** lặp lại cùng một sai lầm. Nếu người dùng xóa file, rút kinh nghiệm và làm khác đi.
6. **KHÔNG** tạo file `.html` — website sử dụng `reader.html` để render `.md` trực tiếp.
7. **KHÔNG** chạy `build_html.py`, `generate_index.py`, hoặc `add_navigation.py` — đã deprecated.
8. **LUÔN** duy trì hệ thống ba ngôn ngữ: 漢字 (phồn thể) → Hán Việt → Tiếng Việt khi cần thiết.
9. **LUÔN** kiểm tra trạng thái thực tế của file trước khi hành động — đừng tin bộ nhớ mù quáng.
10. **GIỚI HẠN** mỗi lần chạy tối đa 2–3 nhiệm vụ tập trung. Chất lượng hơn số lượng.
11. Tên file Tiếng Việt có dấu và gạch dưới. Không ngoại lệ.
