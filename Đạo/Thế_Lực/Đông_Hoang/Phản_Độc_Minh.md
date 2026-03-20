---
type: faction
name: Phản Độc Minh
hantu: 反毒盟
faction_type: Liên Minh
alignment: 6
race: Nhân Tộc
region: Đông Hoang
founded: 30 năm trước
founder: Hứa Thiết Tâm
emblem: Phan_Doc_Minh.png
specialty: Thu thập tình báo về Vạn Độc Môn, Giải độc thực chiến, Cứu trợ nạn nhân
economy:
- Quyên góp từ nạn nhân và đồng tình viên
- Bán thuốc giải độc thô sơ cho dân biên giới
- Trao đổi thông tin tình báo lấy vật tư
arcs:
  - arc: 1
    status: Hoạt động bí mật
    rank: Hạng Năm
    leader: Minh Chủ Hứa Thiết Tâm
    population: 120
    territory:
      - Trạm Biên Nam Cương (khu lều trại phía tây chợ)
    assets:
      - name: Sổ Ghi Chép 300 Loại Độc
        type: Bảo Vật
      - name: Kho Dược Liệu Giải Độc
        type: Tài Nguyên
      - name: Mạng lưới trinh sát biên giới
        type: Tài Nguyên
    stats: [40, 30, 50, 120, 20, 60]
    divisions:
      - name: Ban Tình Báo
        role: Thu thập thông tin về Vạn Độc Môn và theo dõi hoạt động của Vạn Độc Thất Sát
        headcount:
          minh_chu: 1
          pho_minh_chu: 0
          truong_lao: 3
          su_gia: 10
          thanh_vien_phai: 30
        members:
          - character: Hứa Thiết Tâm
            position: Minh Chủ
            cultivation: Trúc Cơ Sơ Kỳ
          - character: "[Trưởng Lão Tình Báo]"
            position: Trưởng Lão
            cultivation: Luyện Khí Hậu Kỳ
            placeholder: true
      - name: Ban Giải Độc & Cứu Trợ
        role: Sơ cứu giải độc cho nạn nhân và bào chế thuốc giải
        headcount:
          minh_chu: 0
          pho_minh_chu: 0
          truong_lao: 0
          su_gia: 20
          thanh_vien_phai: 56
        members:
          - character: "[Đội Trưởng Giải Độc]"
            position: Trưởng Lão
            cultivation: Luyện Khí Hậu Kỳ
            placeholder: true
    relationships:
      - faction: Phế Độc Đường
        description: Hợp tác bí mật, Phế Độc Đường cung cấp thông tin nội bộ Vạn Độc Môn, đổi lại Phản Độc Minh cung cấp mạng lưới trinh sát biên giới.
        diplomacy:
          lien_minh: 60
          tin: 50
          uy_hiep: 0
          thuong_mai: 30
          on_oan: 20
          le_thuoc: 0
      - faction: Vạn Độc Môn
        description: Tử địch, Phản Độc Minh tồn tại chỉ để chống lại Vạn Độc Môn, bị Vạn Độc Thất Sát truy kích nhiều lần.
        diplomacy:
          lien_minh: -100
          tin: -100
          uy_hiep: 80
          thuong_mai: -100
          on_oan: -100
          le_thuoc: 0
      - faction: Nam Cương Dược Sư Hội
        description: Quan hệ thân thiện, Dược Sư Hội ngầm cung cấp dược liệu giá rẻ cho Phản Độc Minh.
        diplomacy:
          lien_minh: 30
          tin: 40
          uy_hiep: 0
          thuong_mai: 50
          on_oan: 10
          le_thuoc: 0
---

# PHẢN ĐỘC MINH (反毒盟)

## I. Tổng Quan (总览)

Phản Độc Minh là liên minh bí mật quy tụ những nạn nhân sống sót sau các thí nghiệm tàn bạo của Vạn Độc Môn. Với khoảng 120 thành viên, hầu hết là phàm nhân và tu sĩ cấp Luyện Khí, liên minh này không có sức mạnh quân sự đáng kể nhưng sở hữu tài sản vô giá: kiến thức giải độc tích lũy từ kinh nghiệm đau thương của hàng trăm nạn nhân. Dưới sự lãnh đạo của Minh Chủ Hứa Thiết Tâm — nông dân mất cả gia tộc vì thí nghiệm Dược Nhân, tự học đến Trúc Cơ — Phản Độc Minh hoạt động như một tổ chức phản kháng ngầm, kết hợp giữa thu thập tình báo, cứu trợ nạn nhân và tìm kiếm đồng minh để một ngày phá hủy Vạn Độc Môn.

## II. Địa Lý & Tài Nguyên (地理与资源)

Trụ sở hiện tại của Phản Độc Minh nằm ở rìa Trạm Biên Nam Cương, gần cổng ra vào phía tây hướng về Vạn Độc Cốc. Vị trí này tuy nguy hiểm nhưng cho phép theo dõi những kẻ ra vào vùng lãnh thổ Vạn Độc Môn. Dãy lều tạm bợ dựng trên nền đất cao tránh ngập, xung quanh là hào nhỏ chứa dung dịch giải độc thô sơ ngăn côn trùng độc xâm nhập. Tài nguyên quan trọng nhất là cuốn sổ ghi chép hơn 300 loại độc của Vạn Độc Môn, do các nạn nhân sống sót đóng góp qua ba thập kỷ. Ngoài ra, dược liệu tầm thường hái ven rừng Nam Cương — không đủ luyện đan nhưng đủ để bào chế thuốc giải cứu mạng tạm thời.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)

Triết lý cốt lõi của Phản Độc Minh gói gọn trong câu: "Kẻ từng nếm độc sẽ nhận ra vị thuốc." Liên minh tin rằng nỗi đau là thầy dạy tốt nhất — những ai từng chịu đựng độc tố của Vạn Độc Môn sẽ có hiểu biết sâu sắc nhất về cách giải độc. Mỗi thành viên mới phải kể lại câu chuyện bị Vạn Độc Môn hại trước mặt toàn minh — nước mắt là lễ gia nhập, không cần nghi thức phức tạp. Quy tắc tối cao là không bỏ rơi đồng minh bị trúng độc; ai phản bội sẽ bị trục xuất và thông tin bí mật bị xóa khỏi trí nhớ bằng thuật phong ấn thô sơ.

## IV. Cơ Cấu Tổ Chức (组织结构)

Phản Độc Minh tổ chức theo mô hình liên minh lỏng lẻo, chia thành hai ban chính. Minh Chủ Hứa Thiết Tâm — nông dân mất cả gia tộc vì thí nghiệm Dược Nhân của Vạn Độc Môn, tự mò mẫm tu luyện đến Trúc Cơ Sơ Kỳ — nắm quyền quyết định tối cao. Tam Trưởng Lão gồm ba nạn nhân lâu năm nhất, đều Luyện Khí Hậu Kỳ, phụ trách ba mảng: tình báo, hậu cần và huấn luyện. Ban Giải Độc có khoảng 20 Giải Độc Sư Luyện Khí biết sơ cứu giải độc. Phần còn lại là hơn 70 thành viên thường — phàm nhân và Luyện Khí Sơ Kỳ — làm trinh sát, hậu cần và chăm sóc nạn nhân mới.

## V. Công Pháp & Trận Pháp (功法与阵法)

Phản Độc Minh không có công pháp chính thức. Thành viên tu luyện tạp công pháp nhặt nhạnh từ nhiều nguồn, không hệ thống. Tuy nhiên, sở hữu một số phương thuốc giải độc hiệu quả bất ngờ — được tổng hợp từ kinh nghiệm thực chiến chứ không phải lý thuyết. Những phương thuốc này tuy thô sơ nhưng đã cứu sống hàng trăm mạng người trong ba thập kỷ. Đặc biệt, liên minh phát triển được "Ngũ Độc Biện Sắc Thuật" — kỹ năng nhận diện loại độc chỉ bằng quan sát triệu chứng, do những người từng trải qua đủ loại độc truyền dạy.

## VI. Đặc Sản Môn Phái (门派特产)

- **Bách Độc Giải Phương Lục:** Cuốn sổ ghi chép hơn 300 loại độc của Vạn Độc Môn kèm phương pháp giải độc tương ứng. Không phải sách lý thuyết mà là kinh nghiệm xương máu của nạn nhân sống sót. Mỗi trang đều thấm mồ hôi và nước mắt.
- **Cấp Cứu Giải Độc Hoàn:** Đan dược thô sơ bào chế từ dược liệu ven rừng, hiệu quả chỉ bằng 30% thuốc giải chính hãng nhưng đủ giữ mạng nạn nhân trong vài giờ chờ cứu viện. Giá rẻ và dễ sản xuất.

## VII. Cơ Sở Hạ Tầng (基础设施)

- **Khu Lều Trại:** Dãy lều tạm bợ phía tây chợ Trạm Biên Nam Cương, bề ngoài trông như lều tị nạn nhưng bên trong có hệ thống liên lạc bằng tín hiệu khói và mật mã.
- **Phòng Giải Độc:** Một lều lớn trung tâm trang bị dụng cụ sơ cứu và dược liệu cơ bản, nơi tiếp nhận và cứu chữa nạn nhân mới.
- **Hào Giải Độc:** Hào nhỏ bao quanh khu trại chứa dung dịch hỗn hợp thảo dược, ngăn côn trùng độc và tạo vùng đệm an toàn.
- **Kho Bí Mật:** Hầm nhỏ dưới lều Minh Chủ, cất giấu cuốn Bách Độc Giải Phương Lục và các mẫu độc thu thập được.

## VIII. Kinh Tế (经济)

Kinh tế của Phản Độc Minh phụ thuộc chủ yếu vào quyên góp và trao đổi. Nạn nhân được cứu sống thường quay lại đóng góp lương thực hoặc vật tư; đồng tình viên ở chợ Trạm Biên thỉnh thoảng giúp đỡ bằng hiện vật. Một phần nhỏ thu nhập đến từ việc bán Cấp Cứu Giải Độc Hoàn cho dân biên giới với giá rẻ. Phản Độc Minh cũng trao đổi thông tin tình báo với Phế Độc Đường để nhận vật tư y tế chất lượng cao hơn. Nhìn chung, liên minh luôn trong tình trạng thiếu thốn, hoạt động bằng ý chí nhiều hơn tiền bạc.

## IX. Lịch Sử Tóm Tắt (简史)

Phản Độc Minh thành lập cách đây 30 năm, ngay sau vụ Vạn Độc Môn thử nghiệm "Huyết Lệ Tán" trên dân làng biên giới. Hứa Thiết Tâm — lúc đó chỉ là nông dân bình thường — mất vợ, con và toàn bộ gia tộc trong cuộc thí nghiệm đó. Từ nỗi đau và phẫn nộ, ông tập hợp những nạn nhân sống sót, thề nguyện sẽ đấu tranh cho đến khi Vạn Độc Môn bị tiêu diệt.

Ba thập kỷ qua, Phản Độc Minh bị Vạn Độc Thất Sát truy kích nhiều lần, phải di chuyển trụ sở tổng cộng 7 lần, mất không ít thành viên. Hứa Thiết Tâm tự mò mẫm tu luyện từ phàm nhân đến Trúc Cơ Sơ Kỳ — tiến bộ đáng kinh ngạc cho một người không có sư phụ. Gần đây, liên minh bắt đầu hợp tác ngầm với Phế Độc Đường — cựu đệ tử Vạn Độc Môn đào thoát — tạo nên mối liên kết tình báo nguy hiểm nhưng đầy tiềm năng.

## X. Giai Thoại & Bí Mật (轶事与秘密)

- Cuốn sổ ghi chép 300 loại độc thực ra có một trang ẩn, ghi lại phương pháp phá giải Vạn Độc Phệ Tâm Trận — đại trận bảo vệ cốt lõi Vạn Độc Cốc. Tuy nhiên, phương pháp này cần ít nhất tu vi Kim Đan mới thực hiện được, nên hiện tại chỉ là hy vọng hão — trừ khi tìm được đồng minh đủ mạnh.
- Có tin đồn Hứa Thiết Tâm thực ra đã lén luyện một biến thể độc công từ chính những độc tố thu thập được. Ông tin rằng chỉ có "dùng độc trị độc" mới đánh bại được Vạn Độc Môn, nhưng phương pháp này đang ăn mòn kinh mạch của ông, rút ngắn tuổi thọ. Đây là bí mật mà ngay cả Tam Trưởng Lão cũng không biết.
- Mạng lưới trinh sát của Phản Độc Minh phát hiện rằng Vạn Độc Môn gần đây gia tăng thu mua "Dược Nhân" — dấu hiệu cho thấy một thí nghiệm quy mô lớn đang được chuẩn bị.

## XI. Quan Hệ Thế Lực (势力关系)

| Thế Lực | Quan Hệ | Mô Tả |
|---------|---------|-------|
| Phế Độc Đường | Đồng minh bí mật | Trao đổi tình báo và vật tư chống Vạn Độc Môn |
| Vạn Độc Môn | Tử địch | Mục tiêu tồn tại duy nhất của liên minh |
| Nam Cương Dược Sư Hội | Thân thiện | Cung cấp dược liệu giá rẻ ngầm |
