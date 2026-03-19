---
type: faction
name: Phiêu Phấn Trinh Sát
hantu: 飘粉侦察
faction_type: Hội
alignment: -1
race: Vi Tộc (Phấn Hoa)
region: Đông Hoang
founded: 10 năm trước
founder: Phấn Phiêu
emblem: Phieu_Phan_Trinh_Sat.png
specialty: Trinh sát, Theo dõi mục tiêu, Thu thập thông tin, Tình báo
economy:
- Hợp đồng trinh sát từ tán tu và thương nhân
- Bán tin tình báo cho các thế lực nhỏ
- Thu thập phấn hoa linh cấp thấp trao đổi
arcs:
  - arc: 1
    status: Hoạt động
    rank: Không Xếp Hạng
    leader: Đội Trưởng Phấn Phiêu
    population: 50
    territory:
      - Rừng hoa dại phía đông Đông Hoang
      - Các tuyến đường thương mại ven rừng
    assets:
      - name: Mạng lưới trinh sát phấn hoa
        type: Tài Nguyên
      - name: Kho thông tin tình báo
        type: Tài Nguyên
      - name: Bụi hoa dại căn cứ
        type: Công Trình
    stats: [5, 10, 5, 50, 5, 20]
    divisions:
      - name: Đội Trinh Sát Phấn Hoa
        role: Thu thập thông tin bằng cách bay theo mục tiêu, giao tiếp qua thay đổi màu sắc phấn hoa
        headcount:
          hoi_truong: 1
          pho_hoi_truong: 0
          thanh_vien: 45
          tong_quan: 4
        members:
          - character: Phấn Phiêu
            position: Hội Trưởng (Đội Trưởng)
            cultivation: Tương đương Luyện Khí
          - character: "[Phấn Vũ]"
            position: Tổng Quản (Phó Đội)
            cultivation: Tương đương Luyện Khí
            placeholder: true
          - character: "[Phấn Sương]"
            position: Tổng Quản (Trinh Sát Trưởng)
            cultivation: Tương đương Luyện Khí
            placeholder: true
    relationships:
      - faction: Hoang Dã Thợ Săn Bang
        description: Khách hàng lớn nhất của Đội. Thợ săn bang thường xuyên thuê Phiêu Phấn theo dõi lộ trình linh thú hoặc trinh sát mục tiêu trước khi ra tay. Tuy nhiên, Đội đôi khi bí mật bán tin cho đối thủ của Bang mà Bang không biết.
        diplomacy:
          lien_minh: 10
          tin: 10
          uy_hiep: 0
          thuong_mai: 50
          on_oan: -10
          le_thuoc: 20
      - faction: Linh Trần Vi Tộc
        description: Cùng là Vi Tộc nhưng khác bản chất — Linh Trần tồn tại thụ động trong khi Phiêu Phấn chủ động kiếm sống. Đôi khi Phiêu Phấn bay qua vùng Linh Trần cư trú và trao đổi tin tức về biến động linh khí.
        diplomacy:
          lien_minh: 5
          tin: 10
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 0
      - faction: Phiêu Bạt Khách Sạn Liên Minh
        description: Đội thường trinh sát quanh các khách sạn để thu thập tin tức miễn phí từ lữ khách qua lại. Chưởng Quầy không biết những hạt bụi bay quanh cửa sổ thực ra là gián điệp.
        diplomacy:
          lien_minh: 0
          tin: 0
          uy_hiep: 0
          thuong_mai: 5
          on_oan: 0
          le_thuoc: 0
---

# Phiêu Phấn Trinh Sát (飘粉侦察)

## I. Tổng Quan (总览)
Phiêu Phấn Trinh Sát là đội trinh sát đặc biệt gồm năm mươi Vi Tộc phấn hoa, mỗi cá thể nhỏ như hạt bụi, chuyên thu thập thông tin bằng cách bay theo mục tiêu mà không ai phát hiện. Dưới sự dẫn dắt của Phấn Phiêu — Vi Tộc phấn hoa thông minh nhất đội, biết cách giao tiếp với tu sĩ nhân tộc cấp thấp — đội đã hoạt động suốt mười năm qua, nhận hợp đồng trinh sát từ tán tu và thương nhân. Không xếp hạng trên bất kỳ bảng thế lực nào vì quá nhỏ bé, nhưng chính sự vô hình lại là vũ khí mạnh nhất: không ai nghi ngờ hạt phấn hoa bay trong gió lại đang ghi nhớ mọi lời nói và hành động của mục tiêu.

## II. Địa Lý & Tài Nguyên (地理与资源)
Căn cứ chính của Đội nằm trong rừng hoa dại phía đông Đông Hoang, gần các tuyến đường thương mại chính. Khu vực này mọc đầy bụi hoa dại nhiều màu sắc, tạo môi trường hoàn hảo cho Vi Tộc phấn hoa ẩn nấp — hàng triệu hạt phấn hoa tự nhiên bay trong không khí, không ai phân biệt được đâu là phấn thường, đâu là Vi Tộc đang theo dõi. Tài nguyên chính là phấn hoa linh cấp thấp do chính Vi Tộc tạo ra trong quá trình sinh sống, có thể trao đổi với tu sĩ nhỏ làm nguyên liệu phụ trợ. Tuy nhiên, tài sản giá trị nhất là sự vô hình — khả năng bay theo gió đến bất kỳ đâu mà không bị phát hiện, biến mỗi hạt phấn thành một mắt thần di động.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
Triết lý cốt lõi của Phiêu Phấn Trinh Sát gói gọn trong câu: "Nhỏ bé là lợi thế, vô hình là sức mạnh." Trong thế giới tu luyện nơi kẻ mạnh thống trị, Vi Tộc phấn hoa đã biến điểm yếu lớn nhất — kích thước siêu nhỏ — thành lợi thế sinh tồn vượt trội. Quy tắc nghề nghiệp rất rõ ràng: không được để mục tiêu phát hiện đang bị theo dõi, thông tin thu thập phải chính xác tuyệt đối, và cấm bán tin cho hai bên đối lập cùng lúc (dù quy tắc cuối cùng thỉnh thoảng bị Phấn Phiêu lờ đi khi lợi nhuận quá hấp dẫn). Trinh sát hoàn thành nhiệm vụ được thưởng hạt phấn vàng — loại phấn hoa hiếm nhất rừng, tương đương huân chương chiến công trong thế giới Vi Tộc.

## IV. Cơ Cấu Tổ Chức (组织结构)
Đội có cơ cấu đơn giản phù hợp với quy mô nhỏ. Phấn Phiêu giữ vai trò Đội Trưởng, là Vi Tộc phấn hoa duy nhất có khả năng giao tiếp với tu sĩ nhân tộc cấp thấp thông qua việc sắp xếp phấn hoa thành hình chữ đơn giản trên mặt phẳng. Dưới Phấn Phiêu là bốn Tổng Quản — những Vi Tộc có kinh nghiệm nhất — mỗi cá thể phụ trách một hướng trinh sát. Bốn mươi lăm thành viên còn lại là trinh sát viên, mỗi cá thể nhỏ như hạt bụi, bay theo gió và quan sát. Giao tiếp nội bộ bằng cách thay đổi màu sắc phấn hoa: vàng là an toàn, đỏ là nguy hiểm, xanh là có tin mới. Khi cần báo cáo cho khách hàng, Phấn Phiêu tập hợp đội viên liên quan lại, cùng nhau sắp phấn thành bản đồ hoặc chữ viết trên mặt đá phẳng.

## V. Công Pháp & Trận Pháp (功法与阵法)
Phiêu Phấn Trinh Sát không có công pháp — Vi Tộc phấn hoa sử dụng bản năng tự nhiên để bay và ẩn nấp, hấp thụ linh khí loãng từ hoa dại để duy trì sự sống. Khả năng chiến đấu gần như bằng không đối với bất kỳ tu sĩ nào, kể cả Luyện Khí thấp nhất. Biện pháp tự vệ duy nhất là "Phấn Mê Trận" — khi bị đe dọa, cả đội đồng loạt tung phấn hoa gây dị ứng mạnh: hắt hơi liên tục, chảy nước mắt, ngứa da. Không gây hại thực sự nhưng tạo cơ hội thoát thân hiệu quả. Ngoài ra, khả năng phân tán theo gió khiến việc truy đuổi Vi Tộc phấn hoa gần như bất khả thi — chúng tan vào không khí và biến mất trong tích tắc.

## VI. Đặc Sản Môn Phái (门派特产)
- **Báo Cáo Phấn Hoa:** Bản đồ và thông tin trinh sát được Vi Tộc sắp xếp bằng phấn hoa trên mặt phẳng, chi tiết đến từng bước chân mục tiêu đi trong ngày. Độ chính xác cao vì trinh sát viên theo sát mà không bị phát hiện.
- **Phấn Hoa Linh:** Loại phấn do Vi Tộc tạo ra trong quá trình sinh sống, chứa linh khí cấp thấp, dùng làm nguyên liệu phụ trợ trong một số đan phương đơn giản hoặc hương liệu an thần.
- **Dịch Vụ Cảnh Báo Sớm:** Rải Vi Tộc dọc tuyến đường để phát hiện kẻ lạ tiếp cận, cảnh báo khách hàng trước khi nguy hiểm đến gần.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Bụi Hoa Dại Căn Cứ:** Khu rừng hoa dại mọc dày, nơi Vi Tộc phấn hoa cư trú và tập hợp. Bên ngoài chỉ là bụi hoa bình thường, bên trong là hàng chục Vi Tộc đang trao đổi tin tức.
- **Trạm Quan Sát Ven Đường:** Những bụi hoa nhỏ được Vi Tộc "trồng" dọc tuyến đường thương mại, đóng vai trò trạm gác và điểm trung chuyển tin tức.
- **Đá Phẳng Báo Cáo:** Vài tảng đá phẳng gần rìa rừng nơi Phấn Phiêu sắp xếp phấn hoa thành báo cáo cho khách hàng đến nhận.

## VIII. Kinh Tế (经济)
Kinh tế của Đội hoàn toàn dựa vào hợp đồng trinh sát. Phấn Phiêu nhận yêu cầu từ khách hàng — thường là tán tu hoặc thương nhân muốn biết tình hình đường đi, theo dõi đối thủ, hoặc xác nhận vị trí mục tiêu — rồi phân công trinh sát viên thực hiện. Phí hợp đồng thường rất rẻ so với mặt bằng chung vì Vi Tộc không cần nhiều để sống, nhưng lại đắt so với khả năng chi trả của đội: vài viên linh thạch cấp thấp hoặc vật phẩm trao đổi. Hoang Dã Thợ Săn Bang là khách hàng lớn nhất, chiếm gần một nửa thu nhập. Phấn Phiêu cũng bí mật bán tin cho những bên khác mà khách hàng chính không biết — nguồn thu phụ rủi ro nhưng béo bở.

## IX. Lịch Sử Tóm Tắt (简史)
Mười năm trước, Phấn Phiêu phát hiện rằng tu sĩ nhân tộc sẵn sàng trả linh thạch để mua thông tin mà đối với Vi Tộc phấn hoa chỉ cần bay theo gió vài ngày là có. Vi Tộc phấn hoa quá nhỏ để ai phát hiện, có thể bám theo mục tiêu hàng ngày mà không bị chú ý — kỹ năng sinh tồn tự nhiên bỗng trở thành nghề nghiệp có lời. Phấn Phiêu bắt đầu nhận hợp đồng đơn lẻ, rồi dần tổ chức các Vi Tộc phấn hoa đồng loại thành đội trinh sát chuyên nghiệp. Từ nhóm năm cá thể ban đầu, Đội mở rộng lên năm mươi thành viên, hoạt động phủ khắp các tuyến đường chính trong khu vực.

## X. Giai Thoại & Bí Mật (轶事与秘密)
Phiêu Phấn Trinh Sát đã vô tình thu thập được thông tin về một âm mưu lớn giữa hai thế lực đáng gờm ở Đông Hoang. Tuy nhiên, Vi Tộc phấn hoa quá nhỏ bé và nhận thức hạn chế nên không hiểu hết ý nghĩa của những gì chúng nghe được — chỉ biết ghi nhớ các từ khóa mà không thể ghép thành bức tranh toàn cảnh. Phấn Phiêu linh cảm rằng thông tin này cực kỳ giá trị hoặc cực kỳ nguy hiểm, nhưng không biết nên bán cho ai hay giấu đi. Ngoài ra, Đội giữ bí mật rằng đôi khi bán tin cho cả hai bên đối lập cùng lúc — vi phạm quy tắc do chính mình đặt ra — vì lợi nhuận quá hấp dẫn so với rủi ro bị phát hiện.

## XI. Quan Hệ Thế Lực (势力关系)
- **Hoang Dã Thợ Săn Bang:** Khách hàng lớn nhất và nguồn thu nhập chính. Thợ săn bang thuê Đội trinh sát lộ trình linh thú và theo dõi mục tiêu. Quan hệ thương mại ổn định nhưng có vết nứt ngầm — Đội đôi khi bán tin cho đối thủ của Bang.
- **Linh Trần Vi Tộc:** Quan hệ đồng tộc lỏng lẻo. Cùng là Vi Tộc nhưng Linh Trần tồn tại thụ động còn Phiêu Phấn chủ động kinh doanh. Đôi khi trao đổi thông tin về biến động linh khí trong khu vực.
- **Phiêu Bạt Khách Sạn Liên Minh:** Quan hệ một chiều — Đội thường trinh sát quanh các khách sạn để thu thập tin tức miễn phí từ lữ khách mà Chưởng Quầy hoàn toàn không hay biết.
