---
type: faction
name: Phản Loạn Long Tử
hantu: 反叛龙子
faction_type: Hội
alignment: -3
race: Long Tộc (Chân Long huyết mạch)
region: Vô Tận Hải
founded: Năm mươi năm trước thời điểm hiện tại
founder: Hắc Long
emblem: Nghich_Luan_Hac_Long.png
specialty: Ám Long Ẩn Tức Thuật, Gián điệp nội bộ Long Cung, Mật mã Long Ngâm
economy:
  - Tài trợ bí mật từ kho riêng các thành viên Long Tử
  - Trao đổi tin tức với Tạp Huyết Long Đàn để nhận vật tư bên ngoài
  - Chiếm đoạt nhỏ lẻ từ kho tàng Long Cung mà không bị phát hiện
arcs:
  - arc: 1
    status: Ẩn mình chờ thời
    rank: Không Xếp Hạng
    leader: Hắc Long (danh tính bí mật)
    population: 13
    territory:
      - Không cố định — luân chuyển địa điểm hội họp
    assets:
      - name: Ngọc Giản Mã Hóa
        type: Pháp Bảo
      - name: Ám Long Ẩn Tức Thuật
        type: Công Trình
    stats: [30, 25, 5, 13, 10, 40]
    divisions:
      - name: Hạch Tâm Tổ
        role: Lãnh đạo tối cao và hoạch định chiến lược
        headcount:
          hoi_truong: 1
          pho_hoi_truong: 2
          thanh_vien: 0
          tong_quan: 0
        members:
          - character: "[Hắc Long]"
            position: Hội Trưởng (Thủ Lĩnh)
            cultivation: Nguyên Anh Sơ Kỳ
            placeholder: true
          - character: "[Phó Thủ Lĩnh Nhất]"
            position: Phó Hội Trưởng
            cultivation: Kim Đan Hậu Kỳ
            placeholder: true
          - character: "[Phó Thủ Lĩnh Nhị]"
            position: Phó Hội Trưởng
            cultivation: Kim Đan Hậu Kỳ
            placeholder: true
      - name: Tế Bào Mạng
        role: Thành viên hoạt động gián điệp phân tán trong Long Cung
        headcount:
          hoi_truong: 0
          pho_hoi_truong: 0
          thanh_vien: 10
          tong_quan: 0
        members:
          - character: "[Long Tử Mật Viên]"
            position: Thành Viên
            cultivation: Kim Đan Sơ Kỳ
            placeholder: true
    relationships:
      - faction: Long Cung
        description: Mục tiêu cải cách từ bên trong, quan hệ tuyệt mật — nếu bị phát hiện sẽ bị xử tử toàn bộ dòng tộc.
        diplomacy:
          lien_minh: -100
          tin: -100
          uy_hiep: -80
          thuong_mai: 0
          on_oan: -90
          le_thuoc: 80
      - faction: Tạp Huyết Long Đàn
        description: Bí mật liên lạc, trao đổi thức ăn lấy tin tức bên ngoài Long Cung, đang cân nhắc liên minh.
        diplomacy:
          lien_minh: 40
          tin: 30
          uy_hiep: 0
          thuong_mai: 35
          on_oan: 50
          le_thuoc: 0
      - faction: Giao Long Lưu Vong
        description: Đã bí mật liên lạc với Ngạo Thiên, hai bên đang thăm dò lẫn nhau, chia sẻ mục tiêu chung lật đổ chế độ huyết mạch.
        diplomacy:
          lien_minh: 35
          tin: 25
          uy_hiep: 0
          thuong_mai: 10
          on_oan: 45
          le_thuoc: 0
---

# Phản Loạn Long Tử (反叛龙子)

## I. Tổng Quan (总览)
Phản Loạn Long Tử là tổ chức bí mật hoạt động ngầm bên trong Long Cung, tập hợp những Long Tử và Long Tôn bất mãn với chế độ phong kiến cứng nhắc dựa trên huyết mạch. Tổ chức gồm mười ba thành viên, tất cả đều là con cháu ruột thịt của các Long Vương, sở hữu huyết mạch thuần chủng nhưng mang tư tưởng cải cách. Dưới sự lãnh đạo của nhân vật bí ẩn mang bí danh "Hắc Long" — tu vi tương đương Nguyên Anh Sơ Kỳ — tổ chức này đã hoạt động bí mật suốt hơn năm mươi năm mà chưa bao giờ bị phát hiện. Mặc dù quy mô nhỏ bé và không xếp hạng chính thức, tiềm năng của Phản Loạn Long Tử là vô cùng khủng khiếp, bởi mỗi thành viên đều nắm giữ quyền lực thực sự bên trong Long Cung.

## II. Địa Lý & Tài Nguyên (地理 与 资源)
Phản Loạn Long Tử không có trụ sở cố định. Mỗi lần hội họp, địa điểm lại thay đổi — có thể là một hang động san hô bỏ hoang ở rìa lãnh thổ Long Cung, một vực sâu không ai thèm để ý, hoặc thậm chí bên trong chính điện Long Cung vào những đêm triều đình không họp. Tài nguyên của tổ chức hoàn toàn đến từ kho riêng của từng thành viên; là Long Tử, Long Tôn chính thống, họ không thiếu linh thạch hay pháp bảo, nhưng việc sử dụng phải hết sức thận trọng để không gây nghi ngờ. Liên lạc nội bộ thông qua Long Ngâm mật mã — một tần số đặc biệt trong tiếng gầm của rồng mà chỉ thành viên đã được huấn luyện mới có thể nhận biết, người ngoài nghe chỉ thấy tiếng vang bình thường của đại dương.

## III. Văn Hóa & Tín Ngưỡng (文化 与 信仰)
Thành viên Phản Loạn Long Tử đều là Long Tộc chính thống nhưng mang tư tưởng cách mạng. Họ cho rằng hệ thống phân chia đẳng cấp theo độ thuần chủng huyết mạch là lỗi thời, tàn nhẫn và đang dẫn Long Tộc đến chỗ diệt vong. Chứng kiến cảnh Giao Long bị đối xử như nô lệ, Tạp Huyết Long bị trục xuất không thương tiếc, họ tin rằng Long Cung cần thay đổi từ gốc rễ. Tuy nhiên, bên trong tổ chức vẫn tồn tại mâu thuẫn: một nhóm muốn cải cách ôn hòa từ bên trong, nhóm khác cho rằng chỉ có lật đổ hoàn toàn mới giải quyết được vấn đề. Nỗi sợ lớn nhất của mỗi thành viên không phải cái chết của bản thân, mà là sự liên lụy đến gia tộc nếu bị phát hiện — trong Long Cung, tội phản nghịch bị xử theo nguyên tắc "tru di cửu tộc."

## IV. Cơ Cấu Tổ Chức (组织结构)
Tổ chức hoạt động theo hệ thống tế bào nghiêm ngặt: mỗi thành viên chỉ biết danh tính của hai người khác, đảm bảo nếu một mắt xích bị lộ, toàn bộ mạng lưới vẫn an toàn. Đứng đầu là "Hắc Long" — thủ lĩnh tối cao mà danh tính thật chỉ có hai phó thủ lĩnh biết. Hai phó thủ lĩnh có tu vi Kim Đan Hậu Kỳ, đảm nhiệm việc truyền đạt mệnh lệnh và điều phối mười thành viên còn lại. Mười thành viên này là con cháu của các Long Vương khác nhau, phân bố rải rác trong các phủ đệ khắp Long Cung, đều có tu vi Kim Đan trở lên. Mọi giao tiếp thông qua ngọc giản mã hóa đặc biệt — nếu người ngoài cố đọc, ngọc giản sẽ tự hủy ngay lập tức mà không để lại dấu vết.

## V. Công Pháp & Trận Pháp (功法 与 阵法)
Mỗi thành viên tu luyện công pháp chính thống của Long Cung phù hợp với dòng tộc riêng — Chân Long Cửu Biến, Long Ngâm Chấn Thiên, hoặc các biến thể tùy theo chi nhánh Long Vương. Không ai dám tu luyện công pháp ngoại lai để tránh bị nghi ngờ. Tuy nhiên, Hắc Long đã bí mật sáng tạo ra Ám Long Ẩn Tức Thuật — bí thuật cho phép ẩn giấu hoàn toàn khí tức Long Tộc, biến người tu luyện thành "vô hình" trước cảm ứng của đồng loại. Kỹ thuật này tinh vi đến mức ngay cả Long Vương cũng khó phát hiện, và đây chính là lý do tổ chức tồn tại năm mươi năm mà chưa bị lộ. Hắc Long đã truyền thụ Ám Long Ẩn Tức Thuật cho tất cả thành viên, nhưng chia thành nhiều phiên bản khác nhau — nếu một phiên bản bị giải mã, các phiên bản khác vẫn hoạt động.

## VI. Đặc Sản Môn Phái (门派特产)
- **Ngọc Giản Mã Hóa:** Pháp bảo liên lạc tự chế, khắc rune bí mật lên ngọc giản Long Cung thông thường. Bên ngoài trông giống thư tín gia đình bình thường, nhưng bên trong chứa lớp thông tin ẩn chỉ hiện ra khi chủ nhân đích thân dùng Long Huyết kích hoạt. Nếu người ngoài cưỡng ép giải mã, ngọc giản lập tức biến thành bột, đồng thời phát ra tín hiệu cảnh báo đến Hắc Long.
- **Ám Long Ấn:** Dấu ấn bí mật khắc trên vảy ngược dưới cằm — vị trí mà Long Tộc hiếm khi kiểm tra. Mỗi thành viên mang một Ám Long Ấn khác biệt, dùng để xác nhận danh tính khi gặp mặt trực tiếp trong những tình huống khẩn cấp.

## VII. Cơ Sở Hạ Tầng (基础设施)
Phản Loạn Long Tử cố tình không xây dựng bất kỳ cơ sở hạ tầng nào để tránh để lại dấu vết. Mọi cuộc họp diễn ra tại địa điểm tạm thời — hang động san hô bỏ hoang, khe nứt dưới đáy biển, hoặc bên trong các phế tích cổ mà Long Cung đã quên lãng. Kho dự trữ duy nhất là một không gian lưu trữ chiều không — pháp bảo cá nhân của Hắc Long, chứa lương thực, ngọc giản ghi chép, và một bản sao bằng chứng về sự bất công trong hệ thống huyết mạch Long Cung. Không có nơi huấn luyện, không có thư viện, không có bất cứ thứ gì có thể bị tìm thấy.

## VIII. Kinh Tế (经济)
Tổ chức không có nền kinh tế riêng biệt. Mỗi thành viên tự trang trải chi phí hoạt động từ tài sản gia tộc — là Long Tử, Long Tôn chính thống, họ đều sống trong nhung lụa của Long Cung. Khi cần tài nguyên cho hoạt động chung, các thành viên đóng góp từ phần thưởng cá nhân hoặc lén lút trích một phần nhỏ từ kho tàng của phủ đệ gia tộc. Ngoài ra, tổ chức duy trì một kênh trao đổi bí mật với Tạp Huyết Long Đàn: cung cấp thức ăn và vật tư y tế từ Long Cung, đổi lấy tin tức về tình hình bên ngoài mà Long Cung cố tình bưng bít.

## IX. Lịch Sử Tóm Tắt (简史)
Phản Loạn Long Tử hình thành cách đây hơn năm mươi năm, khởi nguồn từ một sự kiện đau lòng: một Long Tử bị cha ruột — một trong các Long Vương — xử phạt tàn nhẫn chỉ vì dám kết bạn với một Giao Long. Hình phạt bao gồm giam cầm trong Hàn Ngục một năm và bóc mười hai vảy trên lưng trước mặt triều thần. Sự kiện này thức tỉnh những Long Tử có tư tưởng cải cách, từ đó dần tập hợp lại dưới sự dẫn dắt của một nhân vật bí ẩn tự xưng Hắc Long. Suốt năm mươi năm, tổ chức kiên nhẫn tuyển mộ thêm thành viên, nhưng quá trình cực kỳ thận trọng — mỗi ứng viên phải được quan sát ít nhất mười năm trước khi được tiếp cận. Cho đến nay, Phản Loạn Long Tử chưa bao giờ thực hiện hành động lớn, vẫn đang trong giai đoạn tập hợp lực lượng và chờ thời cơ chín muồi.

## X. Giai Thoại & Bí Mật (轶事 与 秘密)
"Hắc Long" được đồn đoán là con trai ruột của một trong Tứ Hải Long Vương — nếu điều này đúng, quyền lực tiềm ẩn của tổ chức là vô cùng lớn, bởi kẻ nằm vùng không phải tay chân nhỏ mà chính là hoàng tử Long Cung. Tổ chức đã bí mật liên lạc với cả Giao Long Lưu Vong và Tạp Huyết Long Đàn, đang cân nhắc thành lập một liên minh ngầm giữa ba thế lực bị Long Cung áp bức. Tuy nhiên, nội bộ vẫn chưa thống nhất về phương pháp: phe ôn hòa muốn gửi thỉnh nguyện thư trực tiếp đến Long Đế (Tổ Long đang ngủ), trong khi phe cấp tiến muốn chờ Long Đế tỉnh giấc rồi bày tỏ trước mặt — một canh bạc vô cùng nguy hiểm. Nếu bất kỳ thành viên nào bị phát hiện, không chỉ bản thân bị xử tử mà toàn bộ gia tộc trong Long Cung cũng sẽ bị liên lụy, có thể dẫn đến cuộc thanh trừng quy mô lớn làm rung chuyển nền tảng quyền lực Long Cung.

## XI. Quan Hệ Thế Lực (势力关系)
- **Long Cung:** Mối quan hệ phức tạp nhất — Phản Loạn Long Tử vừa là con cháu ruột thịt của Long Cung, vừa là kẻ thù tư tưởng từ bên trong. Mọi thành viên đều sống và hoạt động ngay giữa lòng Long Cung, khiến ranh giới giữa "đồng minh" và "phản nghịch" chỉ là một bước chân.
- **Tạp Huyết Long Đàn:** Mối quan hệ đồng cảm thận trọng. Phản Loạn Long Tử nhìn thấy ở Tạp Huyết Long Đàn bằng chứng sống về sự tàn nhẫn của hệ thống huyết mạch, và đã bí mật trao đổi vật tư lấy tin tức. Tuy nhiên, hai bên vẫn giữ khoảng cách vì sợ lộ danh tính.
- **Giao Long Lưu Vong:** Đã thiết lập liên lạc bí mật với cựu Tướng Quân Ngạo Thiên. Hai bên chia sẻ mục tiêu chung — thay đổi chế độ huyết mạch bất công của Long Cung — nhưng vẫn đang trong giai đoạn thăm dò, chưa cam kết chính thức.
