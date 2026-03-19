---
type: faction
name: Cổ Thụ Tế Tự Đoàn
hantu: 古树祭祀团
faction_type: Tự Viện
alignment: 5
race: Tinh Linh Tộc
region: Đông Hoang
founded: Thượng Cổ Kỷ Nguyên
founder: Không rõ (truyền thống tự phát)
emblem: Co_Thu_Linh_Moc.png
specialty: Thụ Tâm Dung Hợp Thuật, Tế tự cổ thụ linh thiêng, Cảm ứng rừng thiêng
economy:
- Thu hoạch nhựa cổ thụ có dược tính
- Trao đổi lá linh cấp cao với dược sư bên ngoài
- Nhận cúng dường từ Tinh Linh hành hương
arcs:
  - arc: 1
    status: Suy tàn yên tĩnh
    rank: Hạng Năm
    leader: Thụ Linh Mộc Tâm
    population: 18
    territory:
      - Khu Cổ Thụ Thiêng (Sâu trong Vĩnh Hằng Sâm Lâm)
    assets:
      - name: Sáu Cổ Thụ Linh Thiêng
        type: Tài Nguyên
      - name: Bàn Tế Đại Thụ
        type: Công Trình
      - name: Mạng Lưới Rễ Cảm Ứng
        type: Trận Pháp
    stats: [30, 120, 140, 18, 100, 80]
    divisions:
      - name: Tế Tự Đường
        role: Chăm sóc và tế tự sáu cổ thụ linh thiêng, duy trì liên kết linh hồn
        headcount:
          hoi_truong: 1
          pho_hoi_truong: 0
          thanh_vien: 6
          tong_quan: 1
        members:
          - character: Mộc Tâm
            position: Thụ Linh
            cultivation: Kim Đan Trung Kỳ
          - character: "[Tế Tự Trưởng]"
            position: Tế Tự Trưởng
            cultivation: Trúc Cơ Viên Mãn
            placeholder: true
      - name: Hộ Vệ Đội
        role: Tuần tra bảo vệ khu vực cổ thụ và mang tin ra ngoài
        headcount:
          hoi_truong: 0
          pho_hoi_truong: 0
          thanh_vien: 10
          tong_quan: 0
        members:
          - character: "[Hộ Vệ Trưởng]"
            position: Đội Trưởng
            cultivation: Trúc Cơ Hậu Kỳ
            placeholder: true
    relationships:
      - faction: Tinh Linh Vương Đình
        description: Quan hệ xa cách, Vương Đình coi Đoàn là tàn dư cực đoan nhưng không can thiệp vì tôn trọng truyền thống Thượng Cổ.
        diplomacy:
          lien_minh: 10
          tin: 20
          uy_hiep: 0
          thuong_mai: 10
          on_oan: -10
          le_thuoc: 0
      - faction: Cổ Thụ Thủ Hộ Đoàn
        description: Cùng tôn thờ cổ thụ nhưng triết lý khác biệt — Tế Tự Đoàn hòa nhập vào cây, Thủ Hộ Đoàn bảo vệ cây từ bên ngoài.
        diplomacy:
          lien_minh: 40
          tin: 50
          uy_hiep: 0
          thuong_mai: 20
          on_oan: 10
          le_thuoc: 0
      - faction: Dược Thảo Tinh Linh Viện
        description: Đối tác trao đổi nhựa cổ thụ và lá linh, Viện cung cấp dược phẩm cho Đoàn.
        diplomacy:
          lien_minh: 20
          tin: 40
          uy_hiep: 0
          thuong_mai: 60
          on_oan: 0
          le_thuoc: 0
---

# CỔ THỤ TẾ TỰ ĐOÀN (古树祭祀团)

## I. Tổng Quan (总览)
Cổ Thụ Tế Tự Đoàn là một tổ chức tín ngưỡng cổ xưa nhất của Tinh Linh Tộc, tồn tại từ trước khi Tinh Linh Vương Đình hình thành. Đoàn tọa lạc sâu trong Vĩnh Hằng Sâm Lâm, quanh những cổ thụ ngàn năm tuổi, nơi mà ngay cả Vương Đình cũng hiếm khi đặt chân đến. Với triết lý "Cổ thụ là tổ tiên, hòa vào cây là trở về cội nguồn", Đoàn xem việc dung hợp linh hồn với cổ thụ là con đường tu luyện tối cao — một phương thức cực đoan khiến họ bị gạt ra rìa xã hội Tinh Linh hiện đại. Ngày nay chỉ còn chưa đến hai chục thành viên, phần lớn là Tinh Linh già đã tự nguyện gắn bó phần đời còn lại với những gốc cây thiêng.

## II. Địa Lý & Tài Nguyên (地理与资源)
Khu vực cổ thụ linh thiêng nằm ở tầng sâu nhất của Vĩnh Hằng Sâm Lâm, nơi ánh sáng mặt trời gần như không chạm tới mặt đất mà chỉ lọc qua vô số tầng tán lá, tạo nên cảnh sắc huyền ảo với những vệt sáng xanh vàng nhảy múa giữa bóng tối. Sáu cổ thụ khổng lồ mọc thành vòng tròn, rễ nổi trên mặt đất đan xen tạo thành mê cung tự nhiên cao đến ngực người. Linh khí tại đây cực kỳ dồi dào nhờ cổ thụ tích tụ hàng ngàn năm, đậm đặc đến mức có thể nhìn thấy bằng mắt thường dưới dạng sương mỏng xanh lục. Nhựa cổ thụ tiết ra có dược tính mạnh, có thể trị nội thương và bồi bổ linh lực. Lá linh từ tầng cao nhất của cổ thụ là nguyên liệu luyện đan quý hiếm mà các dược sư bên ngoài sẵn sàng trả giá cao.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
Tế Tự Đoàn tin rằng cổ thụ ngàn năm chính là hiện thân của tổ tiên Tinh Linh Tộc — mỗi cây là một vị tiền bối đã chọn con đường hòa nhập vào thiên nhiên. Hàng tháng vào ngày trăng tròn, toàn Đoàn tổ chức đại lễ tế tự, các Tế Tự xếp quanh gốc cây, hát khúc cổ ca bằng Tinh Linh Ngữ cổ đại — ngôn ngữ mà ngay cả Vương Đình ngày nay cũng đã quên gần hết. Quy tắc nghiêm nhất của Đoàn là tuyệt đối cấm chặt phá bất kỳ cổ thụ nào, dù chỉ một cành nhỏ. Tinh Linh già khi cảm thấy thời khắc đã đến sẽ chọn một cổ thụ để tiến hành nghi lễ "Quy Căn" — dần dần hòa nhập thể xác và linh hồn vào thân cây, trở thành một phần vĩnh viễn của cổ thụ. Đây được Đoàn coi là vinh dự tối cao, nhưng bên ngoài lại xem là hành vi tự hủy.

## IV. Cơ Cấu Tổ Chức (组织结构)
Đoàn có cơ cấu đơn giản do quy mô nhỏ. Đứng đầu là Thụ Linh Mộc Tâm — Tinh Linh 2.000 tuổi, nửa thân đã hóa vỏ cây, không thể rời khỏi cổ thụ gốc mà bà đã liên kết. Mộc Tâm giao tiếp bằng thần thức truyền qua rễ cây, giọng nói vang vọng trong tâm trí người nghe như tiếng gió xào xạc giữa tán lá. Dưới Thụ Linh là sáu Tế Tự — mỗi người phụ trách chăm sóc và duy trì liên kết với một cổ thụ linh thiêng, đều là Tinh Linh lớn tuổi đã bắt đầu quá trình dung hợp. Mười Hộ Vệ trẻ hơn đảm nhận việc tuần tra bảo vệ khu vực và là cầu nối duy nhất giữa Đoàn với thế giới bên ngoài.

## V. Công Pháp & Trận Pháp (功法与阵法)
- **Công Pháp:** "Thụ Tâm Dung Hợp Thuật" — công pháp cổ đại cho phép Tinh Linh kết nối thần thức với cổ thụ, dần dần đồng hóa thể xác và linh hồn vào thân cây. Người tu luyện sẽ dần mất đi khả năng di chuyển và cảm giác vật lý, nhưng đổi lại mở rộng thần thức ra toàn bộ hệ rễ cổ thụ, cảm nhận được mọi sự sống trong phạm vi rừng thiêng. Đây là công pháp một chiều — không có cách đảo ngược sau khi đã dung hợp quá sâu.
- **Trận Pháp:** "Vạn Căn Cảm Ứng Trận" — rễ cổ thụ ngàn năm tạo thành mạng lưới cảm ứng tự nhiên trải rộng khắp khu vực. Bất kỳ sinh vật nào đặt chân lên vùng đất có rễ cây đều bị Mộc Tâm phát hiện ngay tức khắc, xác định được vị trí, tu vi và thậm chí cảm xúc của kẻ xâm nhập.

## VI. Đặc Sản Môn Phái (门派特产)
- **Nhựa Cổ Thụ Ngàn Năm:** Nhựa cây tiết ra từ thân cổ thụ linh thiêng, có màu hổ phách trong suốt, mang dược tính cực mạnh. Uống một giọt có thể trị nội thương nặng, bôi ngoài da thì chữa lành vết thương nhanh gấp mười lần bình thường. Sản lượng cực hiếm vì Đoàn chỉ thu hoạch khi cổ thụ tự tiết ra, không bao giờ khoan lấy.
- **Lá Linh Đại Thụ:** Lá cây từ tầng cao nhất của cổ thụ, chứa linh khí cô đọng qua hàng trăm năm quang hợp linh lực. Là nguyên liệu quý cho các đan phương cấp cao liên quan đến mộc hệ.
- **Hạt Giống Thiêng:** Hạt giống từ cổ thụ ngàn năm, cực kỳ hiếm và gần như không bao giờ được trao đổi. Nếu gieo đúng nơi có linh mạch, có thể phát triển thành cổ thụ linh trong vài trăm năm.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Bàn Tế Đại Thụ:** Khu vực tế lễ trung tâm nằm giữa vòng tròn sáu cổ thụ, xây bằng đá linh cổ đại phủ đầy rêu và dây leo. Bàn tế khắc những rune Tinh Linh Thượng Cổ đã mờ theo thời gian nhưng vẫn phát ra ánh sáng nhẹ khi trăng tròn.
- **Hốc Cây Cư Ngụ:** Mỗi thành viên sống trong hốc tự nhiên của cổ thụ, không cần xây dựng gì thêm. Hốc cây rộng đủ cho một người nằm nghỉ, ấm áp vào mùa đông và mát mẻ vào mùa hè nhờ thân cây tự điều hòa.
- **Tuyến Rễ Liên Lạc:** Hệ thống rễ cây nối liền sáu cổ thụ cho phép truyền tin tức giữa các Tế Tự mà không cần di chuyển, hoạt động như một mạng lưới thông tin nội bộ nguyên thủy nhưng hiệu quả.

## VIII. Kinh Tế (经济)
Cổ Thụ Tế Tự Đoàn gần như không tham gia hoạt động kinh tế. Nguồn thu nhỏ giọt đến từ việc trao đổi nhựa cổ thụ và lá linh với Dược Thảo Tinh Linh Viện, đổi lấy dược phẩm cần thiết và vật dụng sinh hoạt cơ bản. Thỉnh thoảng, Tinh Linh hành hương đến khu cổ thụ thiêng sẽ mang theo cúng dường — nhưng số lượng khách hành hương ngày càng ít đi theo sự lãng quên của truyền thống cổ đại.

## IX. Lịch Sử Tóm Tắt (简史)
Cổ Thụ Tế Tự Đoàn tồn tại từ trước khi Tinh Linh Vương Đình hình thành, là truyền thống tín ngưỡng cổ xưa nhất của Tinh Linh Tộc. Thời Thượng Cổ, gần như mọi Tinh Linh đều thực hành nghi lễ tế tự cổ thụ và xem việc quy căn vào cây là quy luật tự nhiên. Khi Vương Đình lên nắm quyền và phát triển hệ thống tu luyện mới, Tế Tự Đoàn bị gạt ra rìa vì cách tu luyện quá cực đoan — xã hội Tinh Linh hiện đại coi việc hòa nhập vào cây là tự hủy vô nghĩa. Qua hàng ngàn năm, thành viên ngày càng giảm, chỉ còn những Tinh Linh già cỗi nhất vẫn kiên trì con đường tổ tiên.

## X. Giai Thoại & Bí Mật (轶事与秘密)
Mộc Tâm đã kết nối với cổ thụ ngàn năm đến mức có thể cảm nhận được toàn bộ Vĩnh Hằng Sâm Lâm — mỗi cái cây, mỗi con suối, mỗi sinh vật bò trên đất. Tuy nhiên, thần thức của bà đang dần tan vào cây, và trong vài chục năm nữa, Mộc Tâm sẽ mất hoàn toàn ý thức cá nhân, trở thành một phần vô tri của cổ thụ. Bà biết điều này nhưng không hề sợ hãi — với bà, đó là sự hoàn thành.

Có tin đồn rằng cổ thụ lớn nhất trong khu vực — cây ở trung tâm vòng tròn, gốc rộng đến mức ba mươi người ôm không hết — thực ra là một Tinh Linh Hóa Thần đã hoàn toàn hóa thụ từ thời Thượng Cổ. Nếu đúng vậy, đây có thể là sinh vật sống lâu nhất còn tồn tại ở Đông Hoang, và ký ức của vị Hóa Thần này có thể chứa đựng bí mật về thời đại trước Đại Chiến.

## XI. Quan Hệ Thế Lực (势力关系)
- **Tinh Linh Vương Đình:** Quan hệ xa cách nhưng không thù địch. Vương Đình coi Đoàn là tàn dư cổ hủ nhưng tôn trọng truyền thống Thượng Cổ nên không can thiệp.
- **Cổ Thụ Thủ Hộ Đoàn:** Cùng tôn thờ cổ thụ nhưng phương thức khác biệt — Tế Tự Đoàn hòa nhập, Thủ Hộ Đoàn bảo vệ. Hai bên tôn trọng nhau và thỉnh thoảng trao đổi tin tức về tình trạng rừng thiêng.
- **Dược Thảo Tinh Linh Viện:** Đối tác thương mại nhỏ, Viện mua nhựa cổ thụ và lá linh, đổi lại cung cấp dược phẩm cho Đoàn.
