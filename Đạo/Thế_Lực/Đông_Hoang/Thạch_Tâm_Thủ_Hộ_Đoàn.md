---
type: faction
name: Thạch Tâm Thủ Hộ Đoàn
hantu: 石心守护团
faction_type: Hội
alignment: 6
race: Cự Tộc
region: Đông Hoang
founded: 15 năm trước
founder: Thạch Kiên
emblem: Thach_Tam_Thu_Ho_Doan.png
specialty: Bảo vệ mỏ linh thạch, Phòng ngự hang động, Chiến thuật Cự Tộc
economy:
  - Không khai thác linh thạch (bảo vệ là chính)
  - Trao đổi sức lao động lấy lương thực
  - Thu nhặt linh thạch vụn rơi tự nhiên để đổi vật tư
arcs:
  - arc: 1
    status: Hoạt động (Bảo vệ mỏ)
    rank: Hạng Năm
    leader: Đoàn Trưởng Thạch Kiên
    population: 12
    territory:
      - Mỏ linh thạch cổ đại trong dãy núi Đông Hoang
      - Hệ thống hang động xung quanh mỏ
    assets:
      - name: Mỏ Linh Thạch Thiêng
        type: Tài Nguyên
      - name: Hệ Thống Phòng Ngự Đá Tự Nhiên
        type: Công Sự
    stats: [30, 80, 15, 12, 120, 10]
    divisions:
      - name: Thủ Hộ Đội
        role: Tuần tra và bảo vệ mỏ linh thạch
        headcount:
          hoi_truong: 1
          pho_hoi_truong: 0
          thanh_vien: 8
          tong_quan: 3
        members:
          - character: Thạch Kiên
            position: Đoàn Trưởng
            cultivation: Trúc Cơ Viên Mãn
          - character: "[Phó Đoàn Trưởng]"
            position: Phó Đoàn Trưởng
            cultivation: Trúc Cơ Trung Kỳ
            placeholder: true
    relationships:
      - faction: Đại Địa Hành Giả
        description: Đại Địa Hành Giả biết về mỏ và âm thầm ủng hộ Đoàn, nhưng không can thiệp trực tiếp.
        diplomacy:
          lien_minh: 30
          tin: 50
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 20
          le_thuoc: 10
      - faction: Thạch Tượng Thủ Vệ
        description: Cùng là Cự Tộc / Thạch Tộc canh giữ di sản, có sự đồng cảm ngầm dù chưa giao tiếp trực tiếp.
        diplomacy:
          lien_minh: 10
          tin: 15
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 0
      - faction: Tán tu khai thác trộm
        description: Thường xuyên đẩy lùi các nhóm tán tu đến khai thác linh thạch trái phép, mối đe dọa liên tục.
        diplomacy:
          lien_minh: -80
          tin: -70
          uy_hiep: 40
          thuong_mai: -100
          on_oan: -50
          le_thuoc: 0
---

# Thạch Tâm Thủ Hộ Đoàn (石心守护团)

## I. Tổng Quan (总览)

Thạch Tâm Thủ Hộ Đoàn là một tổ chức nhỏ gồm 12 Cự Tộc trẻ, do Thạch Kiên thành lập cách đây 15 năm với mục đích duy nhất: bảo vệ mỏ linh thạch thiêng trong dãy núi Đông Hoang khỏi sự khai thác bừa bãi. Dù quy mô khiêm tốn và chỉ thuộc Hạng Năm, Đoàn sở hữu ý chí kiên cường đáng kinh ngạc — mỗi thành viên đều sẵn sàng hy sinh tính mạng để bảo vệ mỏ, coi linh thạch là máu của đại địa chứ không phải tài nguyên để khai thác. Triết lý này khiến Đoàn trở thành một sự tồn tại đặc biệt giữa thế giới tu luyện tham lam vô độ, nơi linh thạch là đồng tiền cứng có giá trị nhất.

## II. Địa Lý & Tài Nguyên (地理与资源)

Mỏ linh thạch cổ đại nằm sâu trong dãy núi Đông Hoang, được bao bọc bởi địa hình hiểm trở với các vách đá dựng đứng và khe núi hẹp. Lối vào chính chỉ vừa đủ cho Cự Tộc nhỏ (khoảng 8 mét) đi qua, tạo thành nút thắt cổ chai tự nhiên dễ phòng thủ. Bên trong là hệ thống hang động tự nhiên rộng lớn, tường hang lấp lánh ánh quang từ các mạch linh thạch thô cấp trung. Tuy giá trị kinh tế rất lớn, Đoàn kiên quyết không khai thác mà chỉ thu nhặt những mảnh vụn rơi tự nhiên để đổi lương thực, duy trì cuộc sống tối thiểu.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)

Triết lý cốt lõi của Đoàn được đúc kết trong câu nói truyền miệng: "Linh thạch là máu của đại địa, lấy quá nhiều thì đất chết." Thạch Kiên tin rằng Cự Tộc sinh ra từ đất đá, nên có trách nhiệm bảo vệ đại địa như bảo vệ mẹ. Mỗi mùa, Đoàn tổ chức lễ Tạ Địa, đặt một tảng linh thạch đẹp nhất lên bàn thờ đá trong hang sâu, thắp hương bằng rêu khô và cầu nguyện đại địa không bị tổn thương thêm. Quy tắc tuyệt đối là cấm khai thác linh thạch trừ trường hợp sinh tồn khẩn cấp, và cấm tiết lộ vị trí mỏ cho bất kỳ người ngoài nào, kể cả đồng tộc không thuộc Đoàn.

## IV. Cơ Cấu Tổ Chức (组织结构)

Cơ cấu rất đơn giản, phản ánh quy mô nhỏ của Đoàn. Đoàn Trưởng Thạch Kiên là người ra mọi quyết định lớn, bên dưới có 8 Thủ Vệ (Cự Tộc trẻ tương đương Trúc Cơ các cấp) luân phiên tuần tra mỏ, và 3 Trinh Sát (Cự Tộc nhỏ nhất, khoảng 8 mét) đảm nhận vai trò ra ngoài thu thập tin tức và trao đổi vật tư. Không có hệ thống quan liêu hay thứ bậc phức tạp — mọi người đều ngang hàng trước mỏ, chỉ Thạch Kiên có quyền chỉ huy trong tình huống chiến đấu.

## V. Công Pháp & Trận Pháp (功法与阵法)

Đoàn sử dụng cổ pháp thể phách Cự Tộc, thiên về phòng ngự và sức chịu đựng hơn là tấn công. Da đá của Cự Tộc kết hợp với cổ pháp tạo thành lớp giáp tự nhiên có thể chịu được công kích Trúc Cơ thông thường. Về trận pháp, Đoàn không có trận pháp chính thống mà sử dụng chiến thuật bố trí đá lớn tại các điểm chiến lược trong hang động — lợi dụng kích thước cơ thể và địa hình hẹp để tạo thành phòng tuyến gần như bất khả xâm phạm đối với kẻ địch cỡ người thường. Tuy đơn giản, chiến thuật này đã nhiều lần đẩy lùi nhóm tán tu có tu vi ngang hoặc cao hơn.

## VI. Đặc Sản Môn Phái (门派特产)

Đoàn không sản xuất hay buôn bán bất kỳ sản phẩm nào vì triết lý không khai thác. Tuy nhiên, trong quá trình bảo vệ mỏ, các thành viên đã tích lũy được kiến thức sâu rộng về linh thạch — phân biệt được phẩm cấp, tuổi thọ và trạng thái của mạch linh thạch chỉ bằng cách chạm tay vào tường hang. Kiến thức này vô cùng quý giá nhưng Đoàn không truyền ra ngoài, coi đó là bí mật của đại địa.

## VII. Cơ Sở Hạ Tầng (基础设施)

Cơ sở hạ tầng của Đoàn hết sức thô sơ, hoàn toàn dựa vào hang động tự nhiên. Khu sinh hoạt là các hốc đá rộng bên ngoài vùng mỏ chính, được kê bằng đá phẳng làm giường. Bàn thờ đại địa nằm ở hang sâu nhất, là nơi linh thiêng nhất của Đoàn. Lối vào chính có các tảng đá khổng lồ được đặt sẵn, khi cần thiết Cự Tộc có thể đẩy xuống để bịt kín, tạo thành lớp phòng thủ cuối cùng.

## VIII. Kinh Tế (经济)

Kinh tế của Đoàn gần như không tồn tại theo nghĩa truyền thống. Thành viên sống nhờ săn bắt thú rừng, hái lượm dược thảo hoang dại, và đôi khi trao đổi sức lao động với các bộ lạc Cự Tộc lân cận. Nguồn "thu nhập" duy nhất là những mảnh linh thạch vụn rơi tự nhiên từ vách hang — Đoàn thu gom chúng không thường xuyên để đổi lấy vật tư cần thiết. Sự nghèo khó về vật chất tương phản hoàn toàn với giá trị khổng lồ của mỏ mà họ bảo vệ, và đây là một nghịch lý mà Thạch Kiên chấp nhận như cái giá của lý tưởng.

## IX. Lịch Sử Tóm Tắt (简史)

Mỏ linh thạch trong dãy núi Đông Hoang là nơi thiêng liêng đối với Cự Tộc từ thời Thượng Cổ, được coi là mạch máu của đại địa. Hàng vạn năm qua, mỏ không bị khai thác vì nằm quá sâu và địa hình hiểm trở. Nhưng khi các tông phái nhân tộc bành trướng và nhu cầu linh thạch tăng vọt, nhiều nhóm tán tu bắt đầu dòm ngó. 15 năm trước, Thạch Kiên — một Cự Tộc trẻ 10 mét với tính cách kiên định bướng bỉnh — tập hợp 11 đồng tộc trẻ cùng chí hướng, thề bảo vệ mỏ bằng mọi giá. Kể từ đó, Đoàn đã đẩy lùi hàng chục nhóm tán tu xâm nhập, dù luôn trong tình trạng thiếu thốn và quân số ít ỏi.

## X. Giai Thoại & Bí Mật (轶事与秘密)

Sâu nhất trong mỏ có một vỉa linh thạch phát ra ánh sáng kỳ lạ — không phải ánh quang bình thường của linh thạch cấp trung mà là thứ ánh sáng có nhịp đập như tim đang đập. Thạch Kiên tin rằng đó không phải linh thạch thường mà là thứ gì đó cổ đại hơn nhiều, có thể là di sản Thượng Cổ hoặc cốt lõi của mạch linh khí toàn khu vực. Hắn không dám tiến vào sâu hơn, vì mỗi lần đến gần, cơ thể đá của hắn bắt đầu cộng hưởng mãnh liệt đến mức mất kiểm soát.

Đại Địa Hành Giả — vị du hành giả Cự Tộc bí ẩn — biết về mỏ này và âm thầm ủng hộ Đoàn, nhưng không can thiệp trực tiếp. Lý do vị ấy giữ khoảng cách không ai hiểu, nhưng Thạch Kiên nghi rằng Đại Địa Hành Giả biết bí mật về vỉa linh thạch sâu nhất mà không muốn tiết lộ.

## XI. Quan Hệ Thế Lực (势力关系)

- **Đại Địa Hành Giả:** Người bảo trợ ngầm, biết về mỏ và ủng hộ từ xa. Quan hệ đơn phương — Đoàn kính trọng nhưng không thể liên lạc chủ động.
- **Thạch Tượng Thủ Vệ:** Cùng là Cự Tộc / Thạch Tộc có sứ mệnh canh giữ, nhưng chưa từng giao tiếp trực tiếp vì cả hai đều hoạt động bí mật. Nếu biết nhau tồn tại, có thể trở thành đồng minh tự nhiên.
- **Các nhóm tán tu khai thác trộm:** Kẻ thù thường trực. Đoàn đã đẩy lùi nhiều lần nhưng nếu tin tức về mỏ lan rộng, sẽ có thêm nhiều nhóm mạnh hơn kéo đến, và Đoàn không đủ sức chống lại tông phái lớn.
