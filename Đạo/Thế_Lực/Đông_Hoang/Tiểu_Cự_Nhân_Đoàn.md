---
type: faction
name: Tiểu Cự Nhân Đoàn
hantu: 小巨人团
faction_type: Bộ Lạc
alignment: 3
race: Cự Tộc (thế hệ mới)
region: Đông Hoang
founded: 20 năm trước
founder: Tiểu Sơn
emblem: Tieu_Cu_Nhan_Doan.png
specialty: Sức mạnh thể phách vượt trội, Khai thác khoáng đá, Xây dựng quy mô lớn
economy:
- Khai thác khoáng đá và linh thạch thô cấp thấp
- Săn thú rừng lớn
- Làm thuê khuân vác và xây dựng cho nhân tộc
arcs:
  - arc: 1
    status: Đang phát triển
    rank: Hạng Năm
    leader: Đoàn Trưởng Tiểu Sơn
    population: 28
    territory:
      - Vùng núi đá phía bắc Đông Hoang
      - Hang động mở rộng trong vách đá
    assets:
      - name: Hang Động Cự Nhân
        type: Công Trình
      - name: Mỏ linh thạch thô cấp thấp
        type: Tài Nguyên
    stats: [80, 60, 30, 28, 70, 20]
    divisions:
      - name: Toàn Đoàn
        role: Sinh tồn, khai thác và hòa nhập với thế giới bên ngoài
        headcount:
          truong_lao: 0
          chien_binh: 8
          dan_thuong: 20
        members:
          - character: "[Tiểu Sơn]"
            position: Đoàn Trưởng
            cultivation: Trúc Cơ Viên Mãn (tương đương)
            placeholder: true
          - character: "[Nham Tý]"
            position: Phó Đoàn
            cultivation: Trúc Cơ Trung Kỳ (tương đương)
            placeholder: true
          - character: "[Thạch Quyền]"
            position: Phó Đoàn
            cultivation: Trúc Cơ Trung Kỳ (tương đương)
            placeholder: true
    relationships:
      - faction: Sơn Cốc Cự Tộc Ẩn Sĩ
        description: Nguồn cội huyết thống. Tiểu Sơn bí mật thăm viếng và được Trưởng Lão kể về Thạch Tổ, nhưng hai bên có quan điểm đối lập về tương lai chủng tộc.
        diplomacy:
          lien_minh: 20
          tin: 30
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 10
          le_thuoc: 20
      - faction: Cửu Hoa Kiếm Tông
        description: Quan hệ thận trọng. Nhân tộc vùng lân cận dần chấp nhận Cự Nhân Đoàn nhờ sự hòa nhã của Tiểu Sơn, nhưng các tông môn lớn vẫn xem họ như dị tộc.
        diplomacy:
          lien_minh: 0
          tin: 10
          uy_hiep: 5
          thuong_mai: 15
          on_oan: 0
          le_thuoc: 0
      - faction: Cự Tộc Thợ Xây
        description: Đồng tộc làm thuê cho nhân tộc. Hai bên chia sẻ kinh nghiệm hòa nhập và đôi khi hợp tác trong các dự án xây dựng lớn.
        diplomacy:
          lien_minh: 40
          tin: 50
          uy_hiep: 0
          thuong_mai: 30
          on_oan: 0
          le_thuoc: 0
---

# Tiểu Cự Nhân Đoàn (小巨人团)

## I. Tổng Quan (总览)

Tiểu Cự Nhân Đoàn là một cộng đồng nhỏ bé gồm 28 Cự Tộc thế hệ mới — những người sinh ra với thân hình chỉ cao 8 đến 10 mét, nhỏ hơn rất nhiều so với tổ tiên 30-50 mét trước đây. Dưới sự dẫn dắt của Đoàn Trưởng Tiểu Sơn, một Cự Tộc trẻ tuổi thông minh và hòa nhã, Đoàn lựa chọn con đường hòa nhập với thế giới bên ngoài thay vì ẩn cư như tổ tiên. Với triết lý "Nhỏ hơn tổ tiên, nhưng linh hoạt hơn", Tiểu Cự Nhân Đoàn đang cố gắng chứng minh rằng sự thu nhỏ không phải dấu hiệu suy tàn mà là bước tiến hóa mới của chủng tộc Cự Tộc.

## II. Địa Lý & Tài Nguyên (地理与资源)

Đoàn cư trú trong vùng núi đá hoang vu phía bắc Đông Hoang, nơi ít người qua lại vì địa hình hiểm trở. Nơi ở chính là một hệ thống hang động tự nhiên trong vách đá, được các thành viên Cự Tộc dùng sức mạnh thể phách mở rộng thủ công cho phù hợp với thân hình 8-10 mét. Vùng núi này sở hữu nguồn khoáng đá phong phú và một vài mạch linh thạch thô cấp thấp — đủ để duy trì cuộc sống nhưng không có giá trị chiến lược lớn. Xung quanh hang động là rừng rậm với nhiều thú rừng lớn, cung cấp nguồn thực phẩm dồi dào cho chế độ ăn uống đặc thù của Cự Tộc. Địa hình hiểm trở vô hình trung trở thành lá chắn tự nhiên, khiến các thế lực bên ngoài ít quan tâm đến vùng đất này.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)

Văn hóa Tiểu Cự Nhân Đoàn mang đậm tinh thần cải cách và thích nghi. Quy tắc quan trọng nhất là "Không được xấu hổ vì chiều cao" — mỗi thành viên phải học cách tự hào về bản thân và tìm cách sống chung với các chủng tộc nhỏ hơn. Đây là sự đối lập rõ rệt với Sơn Cốc Cự Tộc Ẩn Sĩ, nơi các Cự Tộc già coi sự thu nhỏ là dấu hiệu suy tàn đáng xấu hổ. Mỗi năm, Đoàn tổ chức thi ném đá — truyền thống thể thao duy nhất còn lại từ thời Cự Tộc cổ đại — vừa để rèn luyện sức mạnh vừa để giữ gìn bản sắc chủng tộc. Ngoài ra, Tiểu Sơn đang cố gắng xây dựng một bộ nghi lễ mới kết hợp giữa truyền thống Cự Tộc và phong tục nhân tộc, nhằm tạo cầu nối văn hóa giữa hai bên.

## IV. Cơ Cấu Tổ Chức (组织结构)

Cơ cấu tổ chức đơn giản, phẳng và dựa trên sự tín nhiệm cá nhân thay vì thứ bậc cứng nhắc.

- **Đoàn Trưởng — Tiểu Sơn:** Cự Tộc trẻ cao 9 mét, thông minh và hòa nhã, có tu vi tương đương Trúc Cơ Viên Mãn. Là người sáng lập và linh hồn của Đoàn, luôn cố gắng xây dựng quan hệ hữu hảo với nhân tộc.
- **Phó Đoàn (2 người):** Hai Cự Tộc có tu vi tương đương Trúc Cơ Trung Kỳ, hỗ trợ Tiểu Sơn trong việc quản lý sinh hoạt hàng ngày và huấn luyện chiến đấu.
- **Chiến Binh (8 người):** Những Cự Tộc khỏe mạnh nhất, phụ trách bảo vệ hang động, săn bắn và khai thác khoáng đá.
- **Dân Thường (18 người):** Cự Tộc trẻ em, phụ nữ và những thành viên đang trong giai đoạn tu luyện cơ bản.

## V. Công Pháp & Trận Pháp (功法与阵法)

Tiểu Cự Nhân Đoàn tu luyện một biến thể giản lược của cổ pháp Cự Tộc, được điều chỉnh để thích ứng với thân hình nhỏ hơn. Công pháp này tập trung vào việc nén sức mạnh thể phách thay vì phân tán như tổ tiên — nhờ thân hình nhỏ hơn, mật độ linh lực trong cơ thể thực tế cao hơn, cho phép bùng phát sức mạnh tức thời đáng kinh ngạc. Đoàn không có trận pháp chính thức, hoàn toàn dựa vào sức mạnh thể phách tự nhiên vượt trội so với nhân tộc. Tuy nhiên, Tiểu Sơn đã bắt đầu nghiên cứu cách phối hợp chiến đấu theo nhóm — điều mà Cự Tộc cổ đại chưa bao giờ cần vì mỗi cá thể đã đủ mạnh để chiến đấu một mình.

## VI. Đặc Sản Môn Phái (门派特产)

- **Thạch Nha Khí Cụ:** Các công cụ chế tạo từ đá và khoáng thạch bằng sức mạnh thể phách thuần túy, không cần lò rèn. Tuy thô sơ nhưng cực kỳ bền chắc, được một số thợ rèn nhân tộc thu mua làm nguyên liệu.
- **Thú Nhục Sấy Khô:** Cự Tộc săn bắn thú rừng lớn mà nhân tộc không thể hạ được, thịt sấy khô theo phương pháp cổ truyền, giàu linh khí và dinh dưỡng.
- **Dịch Vụ Khuân Vác & Xây Dựng:** Nhờ thân hình khổng lồ, Cự Nhân Đoàn nhận làm thuê các công việc nặng nhọc cho nhân tộc — khuân đá, dựng cột, đào kênh — đổi lấy lương thực và vật tư sinh hoạt.

## VII. Cơ Sở Hạ Tầng (基础设施)

- **Hang Động Cự Nhân:** Hệ thống hang động mở rộng bao gồm khu sinh hoạt chung, kho lương thực, khu rèn luyện thể phách và một hang động lớn dùng làm nơi hội họp. Trần hang cao trên 15 mét, đủ cho Cự Tộc đứng thẳng.
- **Bãi Thi Ném Đá:** Một bãi đất trống trên đỉnh núi, nơi tổ chức lễ hội ném đá hàng năm và cũng là khu vực huấn luyện chiến đấu hàng ngày.
- **Mỏ Thạch Khoáng:** Một mỏ đá nhỏ nằm sâu trong lòng núi, khai thác khoáng thạch và linh thạch thô cấp thấp bằng phương pháp thủ công.

## VIII. Kinh Tế (经济)

Kinh tế Tiểu Cự Nhân Đoàn ở mức tự cung tự cấp với một ít trao đổi thương mại. Nguồn thu chính đến từ ba hoạt động: khai thác khoáng đá bán cho thương nhân nhân tộc, săn thú rừng lớn lấy thịt và da, và nhận làm thuê các công việc nặng nhọc như khuân vác đá, xây dựng công trình cho các làng nhân tộc lân cận. Thu nhập khiêm tốn nhưng đủ để đổi lấy những vật tư mà Cự Tộc không thể tự sản xuất — vải vóc, dược liệu cơ bản và dụng cụ tinh xảo. Tiểu Sơn đang tìm cách mở rộng quan hệ thương mại, đặc biệt là nhận thầu các dự án xây dựng lớn cho tông môn và thành bang.

## IX. Lịch Sử Tóm Tắt (简史)

Cự Tộc thế hệ mới sinh ra ngày càng nhỏ — từ 30-50 mét xuống còn 8-10 mét. Các Cự Tộc già trong Sơn Cốc coi đây là dấu hiệu suy tàn của chủng tộc, nhưng Tiểu Sơn tin rằng đây là một dạng tiến hóa mới. Hai mươi năm trước, hắn tập hợp các Cự Tộc trẻ có cùng chí hướng, rời khỏi Sơn Cốc và thành lập Tiểu Cự Nhân Đoàn với mục tiêu hòa nhập với thế giới bên ngoài thay vì ẩn cư chờ chết. Ban đầu, Đoàn bị cả hai phía kỳ thị — Cự Tộc già coi họ là phản bội truyền thống, nhân tộc sợ hãi vì thân hình khổng lồ. Nhưng nhờ sự kiên nhẫn và thái độ hòa nhã của Tiểu Sơn, Đoàn dần được các làng nhân tộc vùng lân cận chấp nhận, thậm chí được thuê làm công việc khuân vác và xây dựng.

## X. Giai Thoại & Bí Mật (轶事与秘密)

- Tiểu Sơn bí mật đến thăm Sơn Cốc Cự Tộc Ẩn Sĩ và được Trưởng Lão kể về Thạch Tổ — vị Cự Tộc Hóa Thần đang ngủ sâu. Hắn chưa biết nên vui hay sợ trước sự thật này.
- Thân hình nhỏ đi có thể không phải suy tàn mà là dấu hiệu của đột biến — vài Cự Tộc trẻ trong Đoàn bắt đầu thể hiện khả năng mà tổ tiên không có, bao gồm khả năng cảm ứng linh khí tinh tế hơn và tốc độ di chuyển nhanh hơn đáng kể.
- Có tin đồn rằng Tiểu Sơn đã phát hiện một hang động cổ đại sâu trong núi, bên trong có bích họa ghi lại lịch sử thật sự của Cự Tộc — bao gồm cả lý do tại sao chủng tộc này ngày càng thu nhỏ.

## XI. Quan Hệ Thế Lực (势力关系)

- **Sơn Cốc Cự Tộc Ẩn Sĩ:** Nguồn cội huyết thống nhưng quan điểm đối lập. Cự Tộc già coi Tiểu Sơn là kẻ phản bội truyền thống, trong khi Tiểu Sơn vẫn giữ thái độ kính trọng và bí mật viếng thăm.
- **Cự Tộc Thợ Xây:** Đồng tộc cùng chọn con đường hòa nhập nhân tộc. Hai bên chia sẻ kinh nghiệm thích nghi và đôi khi hợp tác trong các dự án lớn.
- **Nhân Tộc Vùng Lân Cận:** Quan hệ dần cải thiện từ sợ hãi sang chấp nhận. Các làng nhân tộc thuê Cự Nhân Đoàn làm công việc nặng nhọc, tạo nền tảng cho sự tin tưởng lẫn nhau.
