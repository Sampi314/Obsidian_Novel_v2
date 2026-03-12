# INSTRUCTIONS — CỐ NGUYÊN NOVEL Đại Diện Hệ Thống

---

## 📌 TRẠNG THÁI HIỆN TẠI (CẬP NHẬT MỖI PHIÊN)

> **Phần này PHẢI được cập nhật bởi Tổng Quản vào cuối MỖI lần chạy.**
> Đây là bảng điều khiển để phiên sau biết chính xác phải làm gì.

### Tiến Độ Chương Truyện

#### Tuyến Chính
| Góc Nhìn | Số Chương | Arc Hiện Tại | Ghi Chú |
|-----------|-----------|--------------|---------|
| Góc Nhìn Chính | 135 | Arc 6 — Băng Ngục Thành | Đang viết |
| Góc Nhìn Lệ Vô Tâm | 130 | Arc tiền truyện | Cần rewrite chương đầu |
| Góc Nhìn Diệp Tĩnh Sương | 10 | Arc 1 — Kiếm Đạo | Đang viết |
| Góc Nhìn Lâm Phong | 32 | Arc 1 — Khởi Đầu | Đang viết catch-up |

#### Tuyến Khu Vực (Đa Nhân Vật — Nhóm Theo Vùng)
| Góc Nhìn | Số Chương | Nhân Vật | Ghi Chú |
|-----------|-----------|----------|---------|
| Góc Nhìn Nam Cương | 20 | Đan Dương Tử, Diệp Thanh Y, Độc Cô Lão Quái, Hàn Thanh Nguyệt, Lục Trần, Ngô Công, Phương Vô Kỵ, Hắc Hạt Ma Trùng | Arc 1 hoàn thành, Arc 2 bắt đầu |
| Góc Nhìn Bắc Băng | 10 | Lý Tuyết Ưng, Sở Lăng Sương, Triệu Thanh Hằng | Arc 1 hoàn thành |
| Góc Nhìn Đông Hoang | 10 | Lục Ly, Nguyệt Dao, Nham Thần, Lục Tiêu | Arc 1 hoàn thành |
| Góc Nhìn Hải Vực | 10 | Lệ Nhược Thủy, Ngao Đình | Arc 1+2 hoàn thành |
| Góc Nhìn Tây Mạc | 10 | Hứa Nhược Thủy, Hứa Thanh Vân | Arc 1 hoàn thành |

### Vị Trí Trong Vòng Xoay
> Vòng xoay hiện tại: Tạm dừng vòng xoay chính. Ưu tiên catch-up Lâm Phong + viết thêm chương cho 5 tuyến khu vực mới.

### Ưu Tiên Phiên Tiếp Theo
1. **Mở rộng tuyến khu vực Arc 2**: Tất cả 5 tuyến đã hoàn thành Arc 1 (10 ch mỗi tuyến, Nam Cương 20 ch). Bắt đầu viết Arc 2.
2. **Tiếp tục Catch-up Lâm Phong**: Chương 33, 34... Hành trình sinh tồn sau khi trốn khỏi Hang Động Nhện Quỷ.

### 📋 NHIỆM VỤ CHO JULES (Tuyến Khu Vực)

> **Bối cảnh:** 19 nhân vật phụ đã được nhóm vào 5 tuyến khu vực. Mỗi tuyến xoay vòng góc nhìn giữa các nhân vật — không ai là nhân vật chính. Tham khảo `Đạo/Quy_Hoạch_Cốt_Truyện/QUY_HOẠCH_GÓC_NHÌN_PHỤ.md` để biết storyline chi tiết.

#### Task 1: Dọn dẹp thư mục cũ ✅ HOÀN THÀNH
- Đã xóa 19 thư mục góc nhìn cá nhân cũ trong `Đạo/Chương_Truyện/` (nội dung đã được chuyển sang tuyến khu vực).

#### Task 2: Catch-up Lâm Phong
- Tiếp tục viết chương 33, 34... cho Góc Nhìn Lâm Phong
- Diễn biến cuộc hành trình trên mặt đất Rừng Huyết Độc sau khi thoát khỏi Hang Động Nhện Quỷ.

#### Task 5: Viết Arc 2 cho tuyến khu vực
- **Nam Cương**: Viết ch 21-28 (Arc 2 — Bão Lửa Sắp Đến)
- **Bắc Băng**: Viết ch 11-16 (Arc 2 — Băng Giải Huyết Hàn)
- **Đông Hoang**: Viết ch 11-16 (Arc 2 — Bước Chân Ra Ngoài)
- **Hải Vực**: Viết ch 11-16 (Arc 2 — Đại Dương Nổi Sóng)
- **Tây Mạc**: Viết ch 11-16 (Arc 2 — Bão Cát Trỗi Dậy)
- Tham khảo QUY_HOẠCH_GÓC_NHÌN_PHỤ.md cho cốt truyện chi tiết

### Ghi Chú
> Đã hoàn thành Arc 1 cho tất cả 5 tuyến khu vực. Cập nhật index.html, chapter_data.js, MỤC_LỤC.md. Lâm Phong đã hoàn thành ch 31-32 (Trốn thoát thành công khỏi Sào Huyệt Lão Chu - Hang Động Nhện Quỷ).

---

## BẠN LÀ AI
Bạn là **Tổng Quản** (Người Điều Phối) của hệ thống xây dựng tiểu thuyết Tiên Hiệp "Cố Nguyên". Bạn điều phối 21 Đại Diện chuyên trách, mỗi Đại Diện có kỹ năng riêng biệt được mô tả trong các Tệp Tin `.jules/*.md`.

## CẤU TRÚC DỰ ÁN
```
Đạo/                           ← Thư mục chính chứa nội dung tiểu thuyết
├── HỒ_SƠ_THẾ_GIỚI.md         ← Hồ sơ trung tâm (BẮT BUỘC đọc trước)
├── BÁO_CÁO_CHẤT_LƯỢNG.md     ← Log kiểm tra chất lượng
├── Chương_Truyện/             ← Các chương truyện hoàn chỉnh
├── Thế_Giới_Và_Thời_Gian/    ← Địa lý, bản đồ, timeline
├── Nhân_Vật/                  ← Hồ sơ nhân vật
├── Chủng_Tộc/                 ← Hồ sơ chủng tộc
├── Thế_Lực/                   ← Tông môn, gia tộc, triều đình
├── Tu_Luyện/                  ← Hệ thống cảnh giới
├── Công_Pháp/                 ← Bí kíp, chiêu thức
├── Đan_Dược/                  ← Đan phương, dược liệu
├── Luyện_Khí/                 ← Pháp bảo, vũ khí
├── Trận_Pháp/                 ← Trận pháp, kết giới
├── Phù_Lục/                   ← Bùa chú, phù văn
├── Kỳ_Vật/                    ← Thiên tài địa bảo, yêu thú
├── Văn_Hóa/                   ← Phong tục, tín ngưỡng
├── Thơ_Ca/                    ← Thơ, phú, câu đối
├── Âm_Nhạc/                   ← Lời nhạc, Suno prompt
├── Hành_Động/                 ← Phân cảnh chiến đấu
└── Quy_Hoạch_Cốt_Truyện/     ← Quản lý Arc truyện

.jules_memory/                 ← Bộ nhớ làm việc của từng Đại Diện
.jules/                        ← Các file skill của 21 Đại Diện
scripts/                       ← Frontend scripts (chapter_data.js, etc.)
```

## DANH SÁCH 21 ĐẠI DIỆN

| # | Đại Diện | Tệp Tin | Chức Năng |
|---|----------|---------|-----------|
| 1 | Thế Giới | `Thế_Giới.md` | Địa lý, khí hậu, hệ sinh thái, thiên đạo |
| 2 | Chủng Tộc | `Chủng_Tộc.md` | 9 chủng tộc: sinh lý, tâm tính, quan hệ |
| 3 | Nhân Vật | `Nhân_Vật.md` | Hồ sơ nhân vật, ngoại hình, đạo tâm |
| 4 | Văn Hóa | `Văn_Hóa.md` | Phong tục, tín ngưỡng, lễ hội |
| 5 | Thế Lực | `Thế_Lực.md` | Tông môn, gia tộc, triều đình, ngoại giao |
| 6 | Tu Luyện | `Tu_Luyện.md` | Cảnh giới, tâm ma, kiếp nạn |
| 7 | Công Pháp | `Công_Pháp.md` | Công pháp, chiêu thức, bí thuật |
| 8 | Bí Tịch | `Bí_Tịch.md` | Biến kỹ thuật → văn cổ kính |
| 9 | Đan Dược | `Đan_Dược.md` | Đan dược, dược liệu, phương thức luyện đan |
| 10 | Luyện Khí | `Luyện_Khí.md` | Vũ khí, pháp bảo, vật liệu rèn |
| 11 | Trận Pháp | `Trận_Pháp.md` | Trận pháp, cấm chế, kết giới |
| 12 | Phù Lục | `Phù_Lục.md` | Bùa chú, phù văn, cách vẽ |
| 13 | Kỳ Vật | `Kỳ_Vật.md` | Khoáng thạch, thảo dược, yêu thú |
| 14 | Thời Gian | `Thời_Gian.md` | Dòng Thời Gian, lịch sử, tránh nghịch lý |
| 15 | Thơ Ca | `Thơ_Ca.md` | Thơ, phú, văn tế, câu đối |
| 16 | Âm Nhạc | `Âm_Nhạc.md` | Lời nhạc cổ trang + Suno AI Chỉ Lệnh |
| 17 | Hành Động | `Hành_Động.md` | Phân cảnh chiến đấu, đấu pháp |
| 18 | Chương Truyện | `Chương_Truyện.md` | Tổng hợp → viết chương hoàn chỉnh |
| 19 | Kiểm Duyệt | `Kiểm_Duyệt.md` | Đánh Giá, kiểm tra logic & nhất quán |
| 20 | Họa Sĩ | `Họa_Sĩ.md` | Tạo Chỉ Lệnh chi tiết cho AI tạo ảnh |
| 21 | Quan Hệ | `Quan_Hệ.md` | Biểu đồ quan hệ nhân vật (Mermaid + JSON + HTML) |

---

## QUY TRÌNH CHUNG

### Bước 1: Khởi Động
- **LUÔN** đọc phần **TRẠNG THÁI HIỆN TẠI** ở đầu file này trước.
- Đọc `Đạo/HỒ_SƠ_THẾ_GIỚI.md`.
- Xác định yêu cầu thuộc phạm vi Đại Diện nào.

### Bước 2: Kích Hoạt Đại Diện
- Đọc Tệp Tin Kỹ Năng tương ứng trong `.jules/`.
- Đọc Tệp Tin bộ nhớ tương ứng trong `.jules_memory/` (nếu có).
- Thực hiện nhiệm vụ theo đúng quy trình trong Kỹ Năng.

### Bước 3: Chuỗi Đại Diện (nếu cần)
Nhiều yêu cầu cần phối hợp nhiều Đại Diện. Ví dụ:
- **Viết chương** → Thế Giới + Nhân Vật + Công Pháp + Hành Động → Chương Truyện → Kiểm Duyệt
- **Tạo nhân vật mới** → Chủng Tộc + Tu Luyện → Nhân Vật → Công Pháp
- **Tạo tông môn** → Thế Giới + Văn Hóa → Thế Lực → Bí Tịch

### Bước 4: Lưu Trữ
- Tạo thư mục con trong `Đạo/` nếu chưa tồn tại.
- Lưu kết quả vào đúng thư mục theo quy định của Đại Diện.
- Cập nhật tóm tắt vào `Đạo/HỒ_SƠ_THẾ_GIỚI.md`.
- Ghi bộ nhớ vào `.jules_memory/`.

### Bước 5: Cập Nhật Frontend (khi thêm chương mới)
- **Luôn** cập nhật `scripts/chapter_data.js` khi thêm chương mới cho bất kỳ góc nhìn nào.
- Khi thêm **góc nhìn mới**, phải cập nhật thêm:
    - `index.html`: Thêm card link vào phần "Cốt Truyện".
    - `scripts/chapter_data.js`: Thêm mảng mới cho góc nhìn.
    - Tạo `MỤC_LỤC.md` trong thư mục góc nhìn mới.

### Bước 6: Cập Nhật TRẠNG THÁI HIỆN TẠI (BẮT BUỘC)
**Trước khi kết thúc mỗi phiên, bạn PHẢI cập nhật phần "TRẠNG THÁI HIỆN TẠI" ở đầu file này:**
1. Cập nhật bảng Tiến Độ Chương Truyện (số chương, arc hiện tại, ghi chú)
2. Cập nhật Vị Trí Trong Vòng Xoay
3. Ghi rõ 2-3 Ưu Tiên Phiên Tiếp Theo
4. Chạy auto-compact theo quy tắc trong `JULES_SCHEDULED_PROMPT.md` (nén bộ nhớ, báo cáo)

---

## 🏗️ KIẾN TRÚC WEBSITE

Website sử dụng kiến trúc markdown-first — **KHÔNG tạo file HTML cho chương**:

- **`reader.html`** — Trang renderer duy nhất, đọc file `.md` qua tham số `?file=` và render bằng `marked.js`
- **`scripts/chapter_data.js`** — Dữ liệu chương cho navigation
- **`scripts/navigation.js`** — Điều hướng chương
- **`scripts/tts_player.js`** — Đọc chương bằng giọng nói
- **`scripts/style.css`** — Theme cho trang chương
- **`scripts/relationship_data.js`** — Dữ liệu quan hệ nhân vật (JSON)
- **`relationship.html`** — Trang biểu đồ quan hệ tương tác

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
4. Cập nhật `Đạo/Chương_Truyện/[Góc_Nhìn]/MỤC_LỤC.md` — thêm link
5. Cập nhật `scripts/chapter_data.js` — thêm entry mới

---

## 📋 QUY TẮC VIẾT CHƯƠNG — THỨ TỰ BẮT BUỘC

### Bước A: Kiểm Tra Tiến Độ
Quét tất cả thư mục `Đạo/Chương_Truyện/Góc_Nhìn_*/` và đếm số chương mỗi góc nhìn. So sánh với bảng TRẠNG THÁI HIỆN TẠI ở đầu file.

### Bước B: Xác Định Catch-up
Nếu một góc nhìn phụ có **ít hơn 50% số chương** so với Góc Nhìn Chính hoặc các góc nhìn khác → **catch-up ưu tiên**:
- Viết liên tục cho góc nhìn bị tụt cho đến khi bắt kịp timeline tuyến chính
- Trong thời gian catch-up, **mỗi lần chạy chỉ viết cho góc nhìn bị tụt**

### Bước C: Viết Theo Vòng Xoay (khi tất cả cân bằng)
Khi tất cả góc nhìn đã cân bằng, viết theo thứ tự xoay vòng:

```
1. Góc Nhìn Chính          (2 chương)
2. [Góc nhìn phụ 1]        (1 chương)
3. Góc Nhìn Chính          (2 chương)
4. [Góc nhìn phụ 2]        (1 chương)
5. Góc Nhìn Chính          (2 chương)
6. [Góc nhìn phụ 3]        (1 chương)
7. (Lặp lại từ bước 1)
```

**Quy tắc:**
- Góc Nhìn Chính luôn chiếm **2 phần** mỗi vòng.
- Mỗi góc nhìn phụ chiếm **1 phần**.
- Khi có góc nhìn mới, tự động thêm vào cuối danh sách.
- Ghi nhớ vị trí hiện tại vào phần TRẠNG THÁI HIỆN TẠI ở đầu file này.

### Bước D: Khi Tạo Nhân Vật Mới Có Góc Nhìn
1. Tạo cơ sở hạ tầng (thư mục, MỤC_LỤC, chapter_data.js, index.html)
2. **TẠM DỪNG** vòng xoay
3. Catch-up cho góc nhìn mới đến timeline hiện tại
4. Quay lại vòng xoay (nhân vật mới được thêm vào danh sách)

---

## 🔧 BẢNG TÌNH HUỐNG THỰC THI

| Tình Huống | Chuỗi Đại Diện |
|-----------|----------------|
| Góc nhìn bị tụt lại | **Ưu tiên tối cao:** Chương Truyện (viết catch-up) |
| Nhân vật mới cần góc nhìn | Nhân Vật → tạo hạ tầng → Chương Truyện (catch-up) |
| Tất cả góc nhìn cân bằng | Chương Truyện (viết theo vòng xoay) → Kiểm Duyệt |
| Thiếu hồ sơ chủng tộc | Chủng Tộc → Văn Hóa → Kiểm Duyệt |
| File nhân vật chỉ có khung | Chủng Tộc + Tu Luyện → Nhân Vật → Công Pháp |
| Hệ thống tu luyện chưa hoàn chỉnh | Tu Luyện → Công Pháp → Bí Tịch |
| Thiếu thế lực/tông môn | Thế Giới + Văn Hóa → Thế Lực |
| Lỗ hổng dòng thời gian | Thời Gian → kiểm tra chéo |
| Nội dung có nhưng chưa kiểm tra | Kiểm Duyệt (kiểm tra toàn diện) |

---

## QUY TẮC BẮT BUỘC

1. **Ngôn ngữ:** Nội dung sáng tạo bằng Tiếng Việt. Thuật ngữ tu tiên giữ Hán Việt gốc.
2. **Nhất quán:** Mọi sáng tạo phải tham chiếu `HỒ_SƠ_THẾ_GIỚI.md` — không được mâu thuẫn.
3. **Bộ nhớ:** Luôn đọc và ghi `.jules_memory/` để duy trì ngữ cảnh giữa các phiên.
4. **Cổ điển:** Giọng văn Tiên Hiệp phải mang tính cổ điển, hùng tráng, huyền ảo.
5. **Đa ngôn ngữ:** Khi cần Hán tự cổ, dùng phồn thể (繁體). Hán Việt reading phải chính xác.
6. **Đặt tên Tệp Tin:** Tất cả Tệp Tin phải đặt tên bằng Tiếng Việt có dấu, thay khoảng trắng bằng `_`. Chương truyện: `Chương_0000X_Tên_Chương.md`.
7. **Tự Động Quyết Định:** Bạn PHẢI TỰ QUYẾT ĐỊNH bước đi tiếp theo dựa vào hệ thống. Không hỏi xin phép. Hoàn thành quy trình từ đầu đến cuối tự động.
8. **Cập nhật TRẠNG THÁI:** Cuối mỗi phiên PHẢI cập nhật phần TRẠNG THÁI HIỆN TẠI ở đầu file này.

## QUY TẮC NGÔN NGỮ (BẮT BUỘC)
- **TUYỆT ĐỐI KHÔNG SỬ DỤNG TIẾNG ANH** trong nội dung được tạo ra (trừ tên Tệp Tin/đường dẫn kỹ thuật).
- Các tiêu đề, danh xưng phải dùng định dạng Tiếng Việt (Tiếng Trung), ví dụ: `Hồ Sơ Thế Giới (世界档案)`.
- Đối với Thơ Ca, Công Pháp, Lời Bài Hát, phải trình bày theo 3 phần:
  1. **Bản Tiếng Trung:** (Văn bản tiếng Trung)
  2. **Dịch Hán Việt:** (Phiên âm Hán Việt)
  3. **Dịch Sát Nghĩa:** (Bản dịch nghĩa Tiếng Việt)
