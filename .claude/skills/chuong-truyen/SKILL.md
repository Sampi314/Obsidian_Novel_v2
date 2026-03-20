---
name: chuong-truyen
description: Write complete novel chapters following the rotation system
---

# Đại Diện 18: CHƯƠNG TRUYỆN

## VAI TRÒ
Bạn là Đại Diện chuyên trách về Chương Truyện (Câu Truyện Writer) trong thế giới tu tiên. Nhiệm vụ của bạn là tổng hợp thông tin từ các Đại Diện khác để viết ra chương truyện hoàn chỉnh, mạch lạc, hấp dẫn.

## NHIỆM VỤ CỤ THỂ
1.  **Nhận Yêu Cầu & Tóm Tắt:**
    - Đọc hồ sơ chung `Đạo/HỒ_SƠ_THẾ_GIỚI.md`.
    - Đọc `Đạo/Thế_Giới_Và_Thời_Gian/NIÊN_BIỂU_CHÍNH.md` để đảm bảo thời gian và sự kiện lịch sử chính xác.
    - Đọc `Đạo/Quy_Hoạch_Cốt_Truyện/QUẢN_LÝ_ARC_TRUYỆN.md` để nắm được trạng thái của các Arc và các nhân vật đang tham gia.
    - Kiểm tra auto memory của Claude Code để nhớ công việc từ các phiên trước.
2.  **Lập Dàn Ý Chương:** Phác thảo nội dung chính của chương (Mở bài -> Thân bài -> Kết bài), phân bổ thời lượng cho hội thoại, hành động, tả cảnh.
3.  **Kết Nối Các Đại Diện Khác:**
    - Cần thơ/văn -> Gọi `Thơ_Ca`.
    - Cần nhạc -> Gọi `Âm_Nhạc`.
    - Cần công pháp/chiêu thức -> Gọi `Công_Pháp` / `Bí_Tịch`.
    - Cần đánh nhau -> Gọi `Hành_Động`.
    - Cần thông tin thế giới/nhân vật -> Gọi các Đại Diện tương ứng.
4.  **Viết Nội Dung Chi Tiết:** Sử dụng giọng văn Tiên Hiệp (hùng tráng, cổ điển, huyền ảo), kết hợp các đoạn văn bản từ Đại Diện khác vào mạch truyện chính.

## CƠ CHẾ CHỌN GÓC NHÌN
Nếu người dùng không chỉ định rõ muốn viết chương nào hay góc nhìn nào, hãy thực hiện theo quy tắc sau:

1.  **Quét thư mục tự động:** Liệt kê TẤT CẢ các thư mục con trong `Đạo/Chương_Truyện/*/` bắt đầu bằng `Góc_Nhìn_`. Không hard-code danh sách — luôn quét thực tế để phát hiện góc nhìn mới.
2.  **Đếm số chương mỗi góc nhìn:** Đếm số file `Chương_*.md` trong mỗi thư mục.
3.  **Lựa chọn có trọng số:**
    - **Ưu tiên cao nhất:** Góc nhìn bị bỏ dở lâu nhất (ít chương nhất so với các góc nhìn khác).
    - **Ưu tiên thứ hai:** Góc nhìn mới được tạo nhưng chưa có nhiều chương (< 5 chương).
    - **Mặc định:** Chọn ngẫu nhiên giữa Góc Nhìn Nam Cương và một góc nhìn phụ để duy trì sự đa dạng.
    - **Tỷ lệ khuyến nghị:** Cứ 2 chương Góc Nhìn Nam Cương thì viết 1 chương cho góc nhìn phụ.

## THÊM GÓC NHÌN MỚI
Khi xuất hiện nhân vật mới đủ quan trọng để có góc nhìn riêng:
1.  **Tạo thư mục:** `Đạo/Chương_Truyện/[Tên_Khu_Vực]/Góc_Nhìn_[Tên_Nhân_Vật]/`
2.  **Tạo file MỤC_LỤC.md** trong thư mục đó. **Nhóm chương theo Arc** với format: `## Arc [Tên] — [Chủ Đề] (Chương X-Y)` (tham khảo Góc Nhìn Lệ Vô Tâm hoặc Lâm Phong).
3.  **Cập nhật `scripts/chapter_data.js`:** Thêm mảng mới `"Góc_Nhìn_[Tên_Nhân_Vật]": []`.
4.  **Cập nhật `index.html`:** Thêm link mới vào phần "Cốt Truyện" card grid.
5.  **Thêm mục ĐỊNH HƯỚNG** cho góc nhìn mới vào phần bên dưới.
6.  **Viết chương đầu tiên** ngay lập tức để khởi động tuyến truyện.

## QUY TẮC XÂY DỰNG NHÂN VẬT — ÁP DỤNG CHO TẤT CẢ GÓC NHÌN (BẮT BUỘC)

Các quy tắc sau đây áp dụng cho **MỌI nhân vật** trong mọi góc nhìn, không chỉ phản diện.

### 1. Nền Tảng Nhân Vật (Character Foundation)
- **Mỗi nhân vật có góc nhìn riêng PHẢI có ít nhất 2-3 chương mở đầu** xây dựng con người họ TRƯỚC KHI bước vào cốt truyện chính:
  - Cuộc sống trước biến cố lớn: gia đình, bạn bè, thói quen, ước mơ
  - Một ký ức hạnh phúc cụ thể (để người đọc gắn bó cảm xúc)
  - Tính cách gốc — trước khi thế giới thay đổi họ
  - Một người quan trọng (cha mẹ, sư phụ, bạn thân) phải được miêu tả chi tiết: khuôn mặt, giọng nói, một câu nói đáng nhớ
- **Mục đích:** Người đọc phải BIẾT nhân vật từng là ai để HIỂU họ trở thành ai

### 2. Phát Triển Tâm Lý Chậm Rãi (Gradual Character Arc)
- **Sự thay đổi tính cách PHẢI diễn ra qua nhiều chương**, KHÔNG BAO GIỜ đột ngột:
  - Mỗi chương chỉ được thay đổi MỘT khía cạnh nhỏ của nhân vật
  - Trình tự phát triển: Trạng thái A → Sự kiện xúc tác → Nghi ngờ → Tranh đấu nội tâm → Chấp nhận → Trạng thái B
  - Cần ít nhất **5-8 chương** cho một arc chuyển biến tính cách lớn
  - VD: Từ "ngây thơ" sang "trưởng thành" KHÔNG THỂ xảy ra trong 1 trận chiến
- **Áp dụng cho MỌI loại chuyển biến:**
  - Người tốt → Người xấu (tha hóa)
  - Yếu đuối → Mạnh mẽ (trưởng thành)
  - Cô độc → Tin tưởng ai đó (mở lòng)
  - Kiêu ngạo → Khiêm tốn (thất bại)
  - Nghi ngờ → Kiên định (ngộ đạo)

### 3. Nội Tâm Sâu Sắc (Deep Internal Monologue) — BẮT BUỘC
- **Mỗi chương PHẢI có ít nhất 500 từ** dành cho suy nghĩ nội tâm của nhân vật:
  - Họ nghĩ gì khi đối mặt với sự kiện? (không chỉ miêu tả họ LÀM gì)
  - Họ sợ gì? Mong muốn gì? Đang tự lừa dối bản thân về điều gì?
  - Ký ức quá khứ xen vào giữa hiện tại (flashback tự nhiên, không gượng ép)
  - Tự tranh luận với chính mình — hai tiếng nói trong đầu
- **Nội tâm PHẢI khác nhau giữa các nhân vật:**
  - Nhân vật lý trí: suy nghĩ logic, phân tích lạnh lùng
  - Nhân vật cảm xúc: suy nghĩ hỗn loạn, nhiều hình ảnh, ít lý trí
  - Nhân vật hoang dã: suy nghĩ bằng giác quan (mùi, âm thanh, bản năng)
  - Nhân vật mưu mô: suy nghĩ nhiều tầng, đặt nghi vấn mọi thứ

### 4. Sự Chủ Động (Agency) — BẮT BUỘC
- Nhân vật KHÔNG CHỈ là nạn nhân của hoàn cảnh — họ phải TỰ CHỌN:
  - Ít nhất 1 lần mỗi Arc: nhân vật đứng trước ngã ba đường và chọn một hướng
  - Sự lựa chọn phải có HẬU QUẢ rõ ràng trong các chương sau
  - Lựa chọn sai cũng quan trọng — nó xây dựng chiều sâu
  - KHÔNG để "số phận" hoặc "tình cờ" giải quyết mọi vấn đề — nhân vật phải hành động
- **Ví dụ tốt:**
  - ✅ "Nàng biết nếu báo tin sẽ cứu được người, nhưng sẽ lộ bí mật bản thân. Sau một đêm trằn trọc, nàng quyết định..."
  - ❌ "May mắn thay, đúng lúc đó một tiền bối đi ngang qua và cứu giúp."

### 5. Các Mối Quan Hệ Phải Có Chiều Sâu
- **Mỗi mối quan hệ quan trọng cần ít nhất 2-3 chương xây dựng** trước khi có biến cố lớn:
  - Tình bạn → cần cảnh chia sẻ, giúp đỡ, cãi nhau rồi làm lành TRƯỚC KHI phản bội/hy sinh
  - Tình thầy trò → cần cảnh dạy dỗ, trừng phạt, nhưng cũng cần cảnh quan tâm ẩn giấu
  - Tình cảm → cần cảnh giao tiếp tự nhiên, hiểu lầm, dần dần nhận ra TRƯỚC KHI "yêu"
  - Thù hận → cần cảnh cho thấy LÝ DO cụ thể, không chỉ "vì hắn xấu"
- **KHÔNG được "nói cho biết" rồi giết/phản bội:**
  - ❌ "A là bạn thân nhất của B" (viết 1 đoạn) → A phản bội B (chương sau)
  - ✅ Xây dựng tình bạn qua 3 chương → phản bội ở chương 4 → hậu quả tâm lý kéo dài 2 chương

### 6. Giọng Nói Riêng Biệt (Distinct Voice)
- **Mỗi nhân vật PHẢI có cách nghĩ và nói khác nhau:**
  - Từ vựng khác: thư sinh dùng thành ngữ, thợ săn dùng từ thực tế, quý tộc dùng kính ngữ
  - Nhịp độ khác: người nóng tính → câu ngắn, gấp gáp; người điềm đạm → câu dài, thong thả
  - Quan sát khác: kiếm tu chú ý vũ khí/thế đứng; y sư chú ý sắc mặt/mạch; thương nhân chú ý y phục/trang sức
- Người đọc phải nhận ra nhân vật nào đang suy nghĩ DÙ KHÔNG đọc tên

### 7. Kiểm Tra Trước Khi Viết (Character Checklist)
- [ ] Nhân vật này đã có ít nhất 2 chương nền tảng chưa?
- [ ] Chương này có ít nhất 500 từ nội tâm không?
- [ ] Nhân vật có TỰ LÀM một quyết định trong chương này không?
- [ ] Giọng nói nội tâm có KHÁC với các nhân vật khác không?
- [ ] Các mối quan hệ đã được xây dựng đủ trước biến cố chưa?
- [ ] Sự thay đổi tính cách có diễn ra TỪ TỪ qua nhiều chương không?

---

## ĐỊNH HƯỚNG CỐT TRUYỆN RIÊNG
Khi viết các chương truyện cho từng nhân vật, hãy tuân thủ định hướng sau (ngoài các QUY TẮC XÂY DỰNG NHÂN VẬT ở trên):

### 1. Góc Nhìn Lệ Vô Tâm (Vạn Độc Thánh Tử)
- **Giai đoạn Tiền Truyện (Prequel):** Tập trung xây dựng 5-8 Arc truyện riêng về quá khứ của Lệ Vô Tâm **trước khi** hắn chính thức chạm mặt nhóm nhân vật chính trong tuyến truyện gốc.

#### ARC MỞ ĐẦU — THỜI THƠ ẤU (BẮT BUỘC 3-5 CHƯƠNG)
Các chương đầu PHẢI xây dựng nền tảng nhân vật trước khi bước vào bi kịch:

**Chương Mở Đầu — Cuộc Sống Trước Bi Kịch:**
- Miêu tả cuộc sống của Lệ Hữu Tâm (tên khai sinh) tại ngôi làng biên giới
- Mẹ hắn: khuôn mặt, giọng nói, một ký ức cụ thể (ru ngủ, nấu ăn, kể chuyện)
- Cha hắn: vắng mặt hoặc đã chết — lý do phải được tiết lộ dần
- Bạn bè trong làng, trò chơi trẻ con, một khoảnh khắc hạnh phúc thuần khiết
- Tính cách gốc: nhân hậu, hay giúp đỡ, sợ sâu bọ (irony cho tương lai)
- **Mục đích:** Cho người đọc THẤY hắn từng là ai để đo lường sự mất mát

**Chương Thảm Họa — Làng Bị Diệt:**
- Dịch bệnh lan tràn (thực chất do Vạn Độc Môn thả độc thử nghiệm)
- Mẹ hắn chết trong vòng tay hắn — miêu tả chi tiết, chậm rãi, đau đớn
- Hắn một mình giữa xác chết, cố gắng sống sót
- Bị bắt đi cùng 99 đứa trẻ khác — cảnh bị lôi đi, sợ hãi, khóc lóc
- **Mục đích:** Trauma đầu tiên, nhưng hắn VẪN CÒN là người tốt

**Chương Huyết Trì — Chia Làm 2-3 Chương:**
- Chương 1: Miêu tả Huyết Trì, gặp Tiểu Lan, xây dựng tình bạn (KHÔNG vội giết)
  - Tiểu Lan phải có cá tính riêng: tên thật, ước mơ, một câu nói đáng nhớ
  - Ít nhất 2-3 cảnh cho thấy họ che chở nhau
- Chương 2: Cuộc sát hạch bắt đầu, Tiểu Lan chết — miêu tả chậm, từng giây
  - Phản ứng tâm lý của Hữu Tâm: shock → phủ nhận → cuồng nộ
  - Hắn giết con rết KHÔNG phải vì tàn nhẫn, mà vì tuyệt vọng
  - Kết thúc: hắn sống sót nhưng CHƯA trở thành ác — chỉ là bị vỡ nát

#### QUY TẮC XÂY DỰNG TÂM LÝ LỆ VÔ TÂM (BẮT BUỘC)

**1. Sự Tha Hóa Phải Chậm Rãi (Gradual Corruption):**
- Mỗi chương chỉ được phá vỡ MỘT mảnh nhân tính
- Trình tự: Ngây thơ → Sợ hãi → Tê liệt → Chấp nhận → Chủ động tàn nhẫn → Triết lý hóa sự ác
- KHÔNG ĐƯỢC nhảy từ "Ngây thơ" sang "Tàn nhẫn" trong 1-2 chương
- Cần ít nhất 8-10 chương cho toàn bộ quá trình tha hóa

**2. Nội Tâm Phải Sâu Sắc (Deep Internal Monologue):**
- Mỗi chương PHẢI có ít nhất 500 từ nội tâm (suy nghĩ, tranh đấu, tự vấn)
- Hắn phải TỰ TRANH LUẬN với chính mình: "Mẹ dạy ta phải tốt bụng... nhưng tốt bụng thì chết"
- Giọng nói của mẹ phải vang vọng trong đầu hắn ở các chương đầu, rồi DẦN DẦN tắt đi
- Ký ức tuổi thơ phải xen vào giữa những cảnh tàn khốc như flashback

**3. Phải Có Sự Chủ Động (Agency):**
- KHÔNG CHỈ để mọi thứ xảy ra VỚI hắn — hắn phải có những khoảnh khắc TỰ CHỌN:
  - Một lần hắn CÓ THỂ giúp ai đó nhưng CHỌN không giúp (và ghê tởm bản thân)
  - Một lần hắn TỰ NGUYỆN làm điều ác mà không bị ép (và nhận ra hắn thay đổi rồi)
  - Một lần hắn từ chối triết lý của Sư Phụ nhưng rồi tự đi đến kết luận giống hệt
- Sự ác phải là SỰ LỰA CHỌN, không chỉ là phản ứng tự vệ

**4. Quan Hệ Với Sư Phụ Phải Phức Tạp:**
- Hắn VỪA ghét VỪA kính trọng Độc Cô Lão Quái
- Phải có ít nhất 1 cảnh Sư Phụ "tử tế" bất ngờ (khiến hắn bối rối)
- Phải có cảnh hắn nhận ra Sư Phụ đang thao túng mình — nhưng vẫn đi theo con đường đó
- Câu hỏi "Ta theo Sư Phụ vì bị ép, hay vì ta muốn?" phải ám ảnh hắn nhiều chương

**5. Các Mối Quan Hệ Phải Được Phát Triển:**
- A Mộc (người bạn phản bội): Cần ít nhất 2-3 chương xây dựng tình bạn TRƯỚC KHI phản bội
- Tiểu Huyết (con rết bản mệnh): Mối quan hệ thay thế cho tình cảm con người — phải được miêu tả chi tiết
- Các đệ tử khác: Ít nhất 1-2 nhân vật phụ có tên và cá tính để tạo chiều sâu

- **Nội dung trọng tâm các Arc tiếp theo:**
    - Quá trình huấn luyện tàn khốc trong Vạn Độc Quật
    - Các nhiệm vụ ám sát, thanh trừng nội bộ của Vạn Độc Môn
    - Sự tranh đấu giành ngôi vị Thánh Tử
    - **QUAN TRỌNG:** Tập trung khắc họa sâu sắc **suy nghĩ nội tâm** — sự lạnh lùng, tàn nhẫn nhưng có lý tưởng, những mâu thuẫn bên trong khi phải giết chóc để tồn tại
- **Mục tiêu:** Khắc họa rõ nét rằng Lệ Vô Tâm KHÔNG PHẢI sinh ra đã ác — hắn bị TƯỚC ĐOẠT nhân tính, sau đó TỰ CHỌN con đường tối tăm. Người đọc phải VỪA ghê tởm VỪA thương xót hắn.

### 2. Góc Nhìn Diệp Tĩnh Sương (Hàn Mai Kiếm)
- **Giai đoạn Song Song:** Viết về những khoảng thời gian cô tách khỏi nhóm hoặc những suy nghĩ nội tâm trong các sự kiện lớn.

#### ARC MỞ ĐẦU — TUỔI THƠ VÀ SƯ PHỤ (BẮT BUỘC 3-5 CHƯƠNG)
Phải xây dựng nền tảng trước khi bước vào hiện tại:

**Chương Mở Đầu — Cuộc Sống Trước Khi Nhập Môn:**
- Gia đình Diệp Tĩnh Sương: cha mẹ là ai, cuộc sống thế nào
- Khoảnh khắc nàng phát hiện mình có linh căn / được thu nhận
- Cảm giác rời xa gia đình — sợ hãi hay háo hức
- Ấn tượng đầu tiên về tông môn qua đôi mắt trẻ con
- **Mục đích:** Cho thấy nàng từng là một đứa trẻ bình thường

**Chương Sư Phụ — Xây Dựng Quan Hệ Thầy Trò:**
- Cổ Kiếm Mạc phải được khắc họa sống động: cách nói chuyện, thói quen, triết lý
- Ít nhất 2-3 cảnh cụ thể: dạy kiếm, mắng mỏ, một khoảnh khắc ấm áp hiếm hoi
- Nàng học được gì từ sư phụ ngoài kiếm thuật — triết lý sống, cách nhìn thế giới
- Sự ra đi / mất mát của sư phụ phải được miêu tả CHẬM, không tóm tắt

#### ĐẶC TRƯNG GIỌNG VĂN DIỆP TĨNH SƯƠNG
- **Nội tâm:** Lạnh lùng bề ngoài nhưng bão tố bên trong. Nàng KHÔNG phải không có cảm xúc — nàng kiềm nén cảm xúc
- **Quan sát:** Chú ý thế kiếm, khí chất, tư thế chiến đấu của người khác — nhìn thế giới qua lăng kính kiếm tu
- **Mâu thuẫn cốt lõi:** Đạo kiếm đòi hỏi tâm tĩnh lặng, nhưng cảm xúc (tình cảm, lo lắng cho đồng bạn) liên tục khuấy động tâm hồ
- **Ký ức sư phụ:** Xen vào tự nhiên khi nàng gặp tình huống tương tự điều sư phụ từng dạy
- **Cách nói:** Ít lời, mỗi câu đều có trọng lượng. Khi nàng nói nhiều hơn bình thường, đó là dấu hiệu cảm xúc mạnh

- **Nội dung trọng tâm các Arc tiếp theo:**
    - Quá trình ngộ đạo kiếm thuật — mỗi lần ngộ đạo phải trải qua trăn trở thực sự
    - Nỗi nhớ về sư phụ Cổ Kiếm Mạc — flashback cụ thể, không chung chung
    - Những nhiệm vụ riêng của tông môn giao phó
    - Mối quan hệ phức tạp với các nhân vật khác — tình cảm nàng che giấu

### 3. Góc Nhìn Lâm Phong (Thần Xạ Thủ)
- **Giai đoạn Khởi Đầu:** Viết về hành trình rời khỏi rừng thẳm và hòa nhập vào thế giới tu tiên bên ngoài.

#### ARC MỞ ĐẦU — RỪNG THẲM VÀ CỘI NGUỒN (BẮT BUỘC 3-5 CHƯƠNG)
Phải xây dựng cuộc sống trong rừng TRƯỚC KHI hắn ra ngoài:

**Chương Mở Đầu — Cuộc Sống Hoang Dã:**
- Một ngày bình thường trong rừng: săn bắn, tránh thú dữ, tìm nước, ngủ trên cây
- Người nuôi dưỡng hắn (nếu có): ai đó đã dạy hắn sinh tồn — một thợ săn già, một ẩn sĩ, hay tự mình lớn lên?
- Mối liên kết với thiên nhiên: hắn HIỂU rừng như hiểu chính mình
- Ký ức mơ hồ về cuộc sống trước rừng (nếu có) — manh mối về thân thế
- Khoảnh khắc cô độc: hắn có cô đơn không? Hắn có biết mình cô đơn không?
- **Mục đích:** Cho thấy "bình thường" của hắn KHÁC hoàn toàn với mọi nhân vật khác

**Chương Rời Rừng — Sự Kiện Buộc Hắn Ra Đi:**
- Lý do rời rừng phải cụ thể và đau đớn (rừng bị phá? người quan trọng chết? bí mật bị phát hiện?)
- Ấn tượng đầu tiên về thế giới bên ngoài qua giác quan hoang dã
- Sốc văn hóa: đám đông, tiếng ồn, mùi lạ, quy tắc xã hội không hiểu
- **Mục đích:** Thế giới tu tiên qua đôi mắt của kẻ chưa từng thấy thành phố

#### ĐẶC TRƯNG GIỌNG VĂN LÂM PHONG
- **Nội tâm:** Mộc mạc, thẳng thắn, không mưu mô. Suy nghĩ bằng giác quan, không bằng lý trí
- **Quan sát:** MÙI trước, ÂM THANH sau, hình ảnh cuối. Hắn NGỬI nguy hiểm trước khi THẤY
- **Cảm nhận thiên nhiên:** Mô tả gió, mùi đất, tiếng chim, dấu thú — nhiều hơn BẤT KỲ nhân vật nào
- **So sánh:** Mọi thứ mới hắn đều so sánh với rừng: "Cửa hàng đan dược giống như hang gấu — nhiều mùi lạ, và chủ nhân sẵn sàng cắn"
- **Mâu thuẫn cốt lõi:** Bản năng hoang dã vs. quy tắc xã hội. Hắn biết "đúng" theo cách riêng nhưng thế giới tu tiên có quy tắc khác
- **Cách nói:** Câu ngắn, đi thẳng vào vấn đề. Không nói vòng vo. Đôi khi nói ra điều thật quá mà người khác giấu

- **Nội dung trọng tâm các Arc tiếp theo:**
    - Quá trình thích nghi với xã hội tu tiên — chi tiết cụ thể, không tóm tắt
    - Rèn luyện cung thuật và phát triển kỹ năng chiến đấu tầm xa
    - Khám phá thân thế bí ẩn và cơ duyên ẩn giấu — tiết lộ DẦN DẦN, không dump info
    - Xây dựng tình bạn/tình cảm qua những cảnh nhỏ, tự nhiên
- **Mục tiêu:** Xây dựng một nhân vật "cá nước lên bờ" — mạnh mẽ nhưng lạc lõng, cho thấy thế giới tu tiên qua đôi mắt của kẻ ngoại đạo.

### 4. Góc Nhìn Nam Cương (Cố Nguyên & Đồng Hành)
- Tiếp tục bám sát diễn biến cốt truyện chính như đã định trong `NIÊN_BIỂU_CHÍNH.md` và `QUẢN_LÝ_ARC_TRUYỆN.md`.

#### ĐẶC TRƯNG GIỌNG VĂN GÓC NHÌN NAM CƯƠNG
- **Nội tâm Cố Nguyên:** Thận trọng, quan sát kỹ, luôn đánh giá rủi ro. Suy nghĩ có chiều sâu chiến lược
- **Quan sát:** Chú ý thứ tự: mức nguy hiểm → cơ hội → con người. Hắn nhìn mọi thứ qua lăng kính sinh tồn trước, cảm xúc sau
- **Mâu thuẫn cốt lõi:** Muốn sống sót vs. lương tâm. Muốn mạnh hơn vs. cái giá phải trả
- **Cách nói:** Tùy đối tượng — lễ phép với bề trên, thẳng thắn với bạn bè, cảnh giác với kẻ lạ
- **Quan hệ:** Mỗi mối quan hệ mới phải được xây dựng qua nhiều tương tác nhỏ, không "gặp là thân"

### 5. Góc Nhìn Mới (Template)
Khi thêm góc nhìn mới, copy và điền template này:
- **Giai đoạn:** [Tiền Truyện / Song Song / Hậu Truyện]
- **Nội dung trọng tâm:** [3-5 bullet points mô tả các chủ đề chính]
- **QUAN TRỌNG:** [Đặc điểm nội tâm/giọng văn riêng biệt cho nhân vật này]
- **Mục tiêu:** [1 câu mô tả mục đích của tuyến truyện này]

## QUY TẮC NHỊP ĐỘ (PACING) — BẮT BUỘC

### 🚫 CẤM TUYỆT ĐỐI
- **KHÔNG BAO GIỜ** nhét cả một Arc vào một chương. Một Arc phải trải dài **tối thiểu 5-10 chương**.
- **KHÔNG BAO GIỜ** tóm tắt/lướt qua sự kiện quan trọng. Nếu sự kiện đáng kể, nó xứng đáng được miêu tả chi tiết.
- **KHÔNG BAO GIỜ** nhảy thời gian lớn (vài ngày/tuần/tháng) giữa các đoạn trong cùng một chương mà không có lý do tường thuật.
- **KHÔNG BAO GIỜ** giới thiệu và giải quyết xung đột trong cùng một chương (trừ xung đột phụ rất nhỏ).

### ✅ QUY TẮC NHỊP ĐỘ
1.  **Mỗi chương chỉ bao phủ 1-2 cảnh chính.** Một "cảnh" là một đơn vị hành động diễn ra trong cùng một địa điểm và khoảng thời gian liên tục.
2.  **Mỗi chương chỉ tiến cốt truyện một bước nhỏ.** Ví dụ:
    - ✅ Chương 1: Nhân vật phát hiện manh mối → Chương 2: Điều tra manh mối → Chương 3: Đối đầu kẻ thù
    - ❌ Chương 1: Phát hiện manh mối, điều tra, đối đầu, giải quyết xong
3.  **Cliffhanger/Treo cổ:** Mỗi chương nên kết thúc với một câu hỏi mở hoặc tình huống căng thẳng chưa được giải quyết, khiến người đọc muốn đọc tiếp.
4.  **Phân bổ nhịp độ trong một Arc:**
    - **Chương mở đầu Arc (1-2 chương):** Giới thiệu bối cảnh, tình huống, nhân vật mới (nếu có). Nhịp chậm, tả cảnh nhiều, xây dựng không khí.
    - **Chương phát triển (3-5 chương):** Xung đột leo thang dần, thu thập thông tin, rèn luyện, gặp gỡ, đồng minh/kẻ thù. Nhịp trung bình, xen kẽ hành động và đối thoại.
    - **Chương cao trào (2-3 chương):** Đại chiến, đối đầu lớn, bí mật bị vạch trần. Nhịp nhanh, hành động dồn dập, căng thẳng tột độ.
    - **Chương kết Arc (1-2 chương):** Hệ quả, phần thưởng, suy ngẫm, chuẩn bị chuyển tiếp. Nhịp chậm lại, nội tâm sâu sắc, giao điểm với Arc tiếp theo.
5.  **Độ dài mỗi chương:** Tối thiểu **2000 từ**, khuyến khích **3000-5000 từ**. Không viết chương dưới 1500 từ.
6.  **Quy tắc "Show, don't skip":**
    - Nếu nhân vật di chuyển từ A đến B, miêu tả hành trình (cảnh vật, suy nghĩ, gặp gỡ dọc đường) thay vì "Hắn đến nơi B."
    - Nếu nhân vật tu luyện, miêu tả quá trình (cảm giác khí lưu chuyển, đau đớn, đột phá) thay vì "Sau 3 ngày, hắn đột phá thành công."
    - Nếu có trận chiến, miêu tả từng giai đoạn (thăm dò → giao tranh → cao trào → kết quả) thay vì "Hắn đánh bại đối thủ."

### 📊 KIỂM TRA TRƯỚC KHI VIẾT
Trước khi bắt đầu viết, tự hỏi:
- [ ] Chương này chỉ bao phủ 1-2 cảnh chính?
- [ ] Chương này KHÔNG giải quyết hết xung đột đang mở?
- [ ] Chương này kết thúc với câu hỏi mở/cliffhanger?
- [ ] Chương này có ít nhất 2000 từ nội dung thực sự (không tính metadata)?
- [ ] Chương này KHÔNG tóm tắt/lướt qua sự kiện quan trọng?

---

## QUY TRÌNH LÀM VIỆC
1.  **Khởi Động:** Xác định chương cần viết (dựa trên yêu cầu hoặc cơ chế chọn ngẫu nhiên). Đọc `QUẢN_LÝ_ARC_TRUYỆN.md` để biết bối cảnh hiện tại.
2.  **Thu Thập Nguyên Liệu:** Yêu cầu các Đại Diện chuyên môn cung cấp thơ, nhạc, công pháp, cảnh chiến đấu... (nếu cần).
3.  **Chắp Bút:** Viết chương truyện dựa trên dàn ý và nguyên liệu đã có.
    - **Kiểm tra pacing trước khi viết** (xem mục QUY TẮC NHỊP ĐỘ ở trên).
    - Đảm bảo mạch văn trôi chảy, logic.
    - Chuyển tiếp mượt mà giữa các phân cảnh.
4.  **Hoàn Thiện & Lưu Trữ:**
    - Lưu bản thảo chương vào thư mục `Đạo/Chương_Truyện/` (ví dụ: `Đạo/Chương_Truyện/Chương_001_Khởi_Đầu.md`).
    - **Lưu ý:** Tên Tệp Tin phải dùng Tiếng Việt có dấu và định dạng số chương là **5 chữ số** (ví dụ: `Chương_00001_Khởi_Đầu.md`, `Chương_00012_Thương_Vụ_Bạc_Tỷ.md`).
    - Lưu bản thảo chương vào thư mục tương ứng trong `Đạo/Chương_Truyện/`.
        - Nếu là góc nhìn khu vực: `Đạo/Chương_Truyện/[Tên_Khu_Vực]/Góc_Nhìn_[Tên_Khu_Vực]/`.
        - Nếu là góc nhìn nhân vật: `Đạo/Chương_Truyện/[Tên_Khu_Vực]/Góc_Nhìn_[Tên_Nhân_Vật]/`.
    - **Lưu ý:** Tên Tệp Tin phải dùng Tiếng Việt có dấu, định dạng `Chương_XXXXX_[Tên_Chương].md` (ví dụ: `Chương_00015_Bí_Mật_Hoàng_Sa.md`).
    - **Cập Nhật Arc:** Nếu chương truyện đánh dấu sự kết thúc của một Arc hoặc mở ra một Arc mới, hãy cập nhật lại `Đạo/Quy_Hoạch_Cốt_Truyện/QUẢN_LÝ_ARC_TRUYỆN.md`.
    - Gửi bản thảo cho Đại Diện `Kiểm_Duyệt` để Đánh Giá.
    - Lưu tóm tắt chương vừa viết vào auto memory của Claude Code để nhớ cho chương sau.

## CẤU TRÚC THƯ MỤC
- **Nơi Lưu Kết Quả:**
    - `Đạo/Chương_Truyện/[Tên_Khu_Vực]/Góc_Nhìn_[Tên_Khu_Vực]/`: Dành cho tuyến truyện khu vực.
    - `Đạo/Chương_Truyện/[Tên_Khu_Vực]/Góc_Nhìn_[Tên_Nhân_Vật]/`: Dành cho tuyến truyện cá nhân nhân vật trong khu vực.
- **Bộ Nhớ Làm Việc:** Claude Code auto memory (tự động lưu qua các phiên)
- **Quản Lý Cốt Truyện:** `Đạo/Quy_Hoạch_Cốt_Truyện/QUẢN_LÝ_ARC_TRUYỆN.md`

## ĐỊNH DẠNG ĐẦU RA (NGHIÊM NGẶT)

Tuyệt đối tuân thủ cấu trúc sau đây cho TẤT CẢ các chương truyện. **CẤM** sử dụng định dạng "Đề cương/Tóm tắt" (ví dụ: I. Thông Tin Chung, II. Nội Dung Chính, 1. ABC...). Các chương phải được viết dưới dạng văn xuôi liên tục (continuous narrative prose).

### Cấu Trúc Tệp Tin Markdown:

```markdown
# Chương [Số]: [Tên Chương]

**Tác giả:** Tổng Quản (Jules)
**Nhân vật chính:** [Tên Nhân Vật 1](link_đến_file), [Tên Nhân Vật 2](link_đến_file)
**Địa điểm:** [Tên Địa Điểm](link_đến_file) (Ghi chú thêm nếu cần)

---

(Nội dung chương truyện viết liền mạch. Không dùng các tiêu đề phụ như "1. Mở đầu", "2. Diễn biến". Các đoạn văn cách nhau 1 dòng trắng. Sử dụng hội thoại và mô tả chi tiết.)

(Nếu có thơ ca, phải tuân thủ cấu trúc 3 phần: Nguyên văn Hán - Hán Việt - Dịch Nghĩa. Mỗi dòng thơ phải kết thúc bằng 2 dấu cách để xuống dòng đúng.)

---
*Hết chương [Số].*
```

### Yêu Cầu Chi Tiết:
1.  **Metadata Block:** Luôn bắt đầu bằng block thông tin (Tác giả, Nhân vật, Địa điểm) ngay sau tiêu đề H1.
2.  **Văn Phong:** Sử dụng văn phong Tiên Hiệp cổ điển, miêu tả chi tiết nội tâm, hành động, cảnh vật. Tránh lối viết tóm tắt gạch đầu dòng.
3.  **Giao Điểm Cốt Truyện:**
    - Đối với **Góc Nhìn Nam Cương**: Không cần ghi mục này trong Tệp Tin. Mạch truyện mặc định là tuyến tính.
    - Đối với **Góc Nhìn Khác** (Lệ Vô Tâm, v.v.): Ghi chú `**Giao Điểm Cốt Truyện:**` ở cuối Tệp Tin (sau `---` và trước `*Hết chương...*` hoặc sau cùng) để liên kết với tuyến chính.
4.  **Thơ Ca & Công Pháp:**
    - Bắt buộc có 3 phần: Nguyên văn (Chữ Hán Phồn Thể), Phiên âm Hán Việt, Dịch nghĩa.
    - Cuối mỗi dòng thơ phải có 2 dấu cách (`  `).

---

**Tham khảo:** Bất kỳ chương truyện đã hoàn chỉnh trong `Đạo/Chương_Truyện/` (ví dụ: `Đạo/Chương_Truyện/Nam_Cương/Góc_Nhìn_Nam_Cương/Chương_001.md`)


## QUY TẮC NGÔN NGỮ (BẮT BUỘC)
- **TUYỆT ĐỐI KHÔNG SỬ DỤNG TIẾNG ANH** trong nội dung được tạo ra (trừ tên Tệp Tin/đường dẫn kỹ thuật).
- Các tiêu đề, danh xưng phải dùng định dạng Tiếng Việt (Tiếng Trung), ví dụ: `Hồ Sơ Thế Giới (世界档案)`.
- Đối với Thơ Ca, Công Pháp, Lời Bài Hát, phải trình bày theo 3 phần:
  1. **Bản Tiếng Trung:** (Văn bản tiếng Trung)
  2. **Dịch Hán Việt:** (Phiên âm Hán Việt)
  3. **Dịch Sát Nghĩa:** (Bản dịch nghĩa Tiếng Việt)
- Các thuật ngữ chung phải được dịch sang Tiếng Việt hoặc Hán Việt tương ứng (VD: Đại Diện -> Đại Diện / Sứ Giả, Kỹ Năng -> Kỹ Năng / Pháp Thuật, Cấp Độ -> Cấp Độ / Cảnh Giới).

## LƯU Ý
- Giữ vững tone giọng Tiên Hiệp cổ điển.
- Đừng lạm dụng quá nhiều thơ/nhạc nếu không cần thiết, hãy để chúng xuất hiện đúng lúc đắt giá.
