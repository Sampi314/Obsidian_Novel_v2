---
type: faction
name: Sa Mạc Yêu Hồ
hantu: 沙漠妖狐
faction_type: Gia Tộc
alignment: -3
race: Yêu Tộc (Hồ Yêu)
region: Tây Mạc
founded: Năm Khởi Nguyên 97.800
founder: Hồ Nguyệt Nhi
emblem: Ho_Ngu_Duoi_Duoi_Trang.png
specialty: Mê Hồn Thuật, Biến Hóa Thuật, Tình báo và gián điệp
economy:
  - Kinh doanh quán trọ và cửa hàng tạp hóa trên Thiên Sa Thương Đạo
  - Buôn bán thông tin (thật lẫn giả)
  - Bán bản đồ và dịch vụ tư vấn đường đi
arcs:
  - arc: 1
    status: Hoạt động bí mật (Ngụy trang thành thương nhân)
    rank: Hạng Tư
    leader: Tộc Trưởng Hồ Nguyệt Nhi
    population: 40
    territory:
      - Các cửa hàng rải rác trên Thiên Sa Thương Đạo
      - Hang bí mật (điểm tụ họp đêm trăng tròn)
    assets:
      - name: Mạng lưới gián điệp trên Thương Đạo
        type: Tình Báo
      - name: Ảo Ảnh Trận
        type: Trận Pháp
    stats: [150, 200, 300, 40, 180, 400]
    divisions:
      - name: Gián Điệp Ngụy Trang
        role: Ngụy trang thành thương nhân tại các trạm dừng, thu thập và bán thông tin
        headcount:
          truong_lao: 5
          chinh_chi: 10
          thu_chi: 20
          gia_nhan: 5
        members:
          - character: Hồ Nguyệt Nhi
            position: Tộc Trưởng
            cultivation: Kim Đan Sơ Kỳ
          - character: "[Gián Điệp Nằm Vùng Thương Hội]"
            position: Nội Ứng
            cultivation: Trúc Cơ Trung Kỳ
            placeholder: true
          - character: "[Hồ Yêu Trạm Bắc]"
            position: Chưởng Quầy
            cultivation: Trúc Cơ Sơ Kỳ
            placeholder: true
    relationships:
      - faction: Thiên Sa Thương Hội
        description: Bán thông tin cho Thương Hội trong khi có gián điệp nằm vùng bên trong hơn mười năm. Quan hệ một chiều, Thương Hội không biết bản chất thật của đối tác.
        diplomacy:
          lien_minh: 20
          tin: -30
          uy_hiep: 0
          thuong_mai: 50
          on_oan: 0
          le_thuoc: 0
      - faction: Sa Tặc Liên Minh
        description: Đồng thời bán thông tin cho Sa Tặc, hai mặt hai tay. Sa Tặc coi Yêu Hồ là nguồn tin đáng giá nhưng không biết Hồ Nguyệt Nhi cũng bán cho cả phe đối lập.
        diplomacy:
          lien_minh: 10
          tin: -20
          uy_hiep: 0
          thuong_mai: 40
          on_oan: 0
          le_thuoc: 0
      - faction: Cổ Sa Yêu Tộc
        description: Hồ Nguyệt Nhi biết về sự tồn tại của Cổ Sa Yêu Tộc nhưng chưa bao giờ tiếp xúc. Bà ta sợ yêu tộc cổ đại này hơn bất kỳ tông môn Nhân Tộc nào.
        diplomacy:
          lien_minh: 0
          tin: -50
          uy_hiep: -80
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 0
---

# Sa Mạc Yêu Hồ (沙漠妖狐)

## I. Tổng Quan (总览)

Sa Mạc Yêu Hồ là một gia tộc Hồ yêu khoảng bốn mươi thành viên, sống ngụy trang hoàn hảo giữa cộng đồng Nhân Tộc trên Thiên Sa Thương Đạo. Dưới sự lãnh đạo của Tộc Trưởng Hồ Nguyệt Nhi, một Hồ yêu năm đuôi tu vi Kim Đan Sơ Kỳ, gia tộc đã xây dựng mạng lưới tình báo và thương mại tinh vi dọc toàn tuyến Thương Đạo. Họ điều hành quán trọ, cửa hàng tạp hóa, quầy bản đồ, tất cả đều do Hồ yêu biến hóa thành Nhân Tộc vận hành. Rất ít ai nghi ngờ rằng cô chủ quán xinh đẹp hay ông lão bán bản đồ thực chất là yêu thú.

## II. Địa Lý & Tài Nguyên (地理与资源)

Sa Mạc Yêu Hồ không sở hữu lãnh địa cố định theo nghĩa truyền thống. Các thành viên rải rác trên toàn tuyến Thiên Sa Thương Đạo, hòa lẫn hoàn hảo vào dòng thương nhân và lữ khách. Mỗi Hồ yêu cấp cao phụ trách một trạm dừng, đóng vai thương nhân thường trú, trong khi các Hồ yêu cấp thấp đóng vai người hầu, phu khuân hay ca nữ. Điểm tụ họp duy nhất của cả tộc là một hang động bí mật nằm sâu dưới lòng đất, nơi mỗi đêm trăng tròn các Hồ yêu trở về hình dạng thật để họp mặt và trao đổi thông tin. Tài nguyên quý giá nhất của họ không phải vàng bạc hay linh thạch, mà là thông tin, thứ được thu thập mỗi ngày từ miệng khách hàng và đồng nghiệp không hề biết họ đang nói chuyện với yêu hồ.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)

Triết lý sống của Sa Mạc Yêu Hồ gói gọn trong câu: "Lừa dối không xấu — chỉ xấu khi bị bắt." Đây không phải tà đạo mù quáng mà là phương thức sinh tồn của một chủng tộc yếu thế buộc phải sống ẩn giữa kẻ mạnh hơn. Tuy nhiên, Hồ Nguyệt Nhi đặt ra những ranh giới rõ ràng: không bao giờ lừa đến mức giết chết con mồi vì "khách hàng chết thì không có lần sau", và tuyệt đối không lừa trẻ con cùng người già. Ai vi phạm sẽ bị Tộc Trưởng trừng phạt nặng nề, từ đánh đòn đến trục xuất khỏi tộc. Phong tục quan trọng nhất là đêm trăng tròn, khi toàn tộc tề tựu trong hang bí mật, trút bỏ lớp ngụy trang Nhân Tộc và sống thật với bản chất Hồ yêu của mình trong vài canh giờ ngắn ngủi.

## IV. Cơ Cấu Tổ Chức (组织结构)

Đứng đầu gia tộc là Tộc Trưởng Hồ Nguyệt Nhi, Hồ yêu năm đuôi tu vi Kim Đan Sơ Kỳ, bề ngoài ngụy trang thành nữ thương nhân trung niên xinh đẹp. Dưới bà là năm Hồ yêu cấp cao tu vi tương đương Trúc Cơ, mỗi con đóng vai thương nhân tại một trạm dừng trọng yếu trên Thiên Sa Thương Đạo, vừa kinh doanh vừa thu thập tình báo. Khoảng ba mươi lăm Hồ yêu cấp thấp còn lại đóng vai người hầu, phu khuân, ca nữ và các nghề nghiệp bình dân khác, mắt tai rải khắp nơi. Đặc biệt, một Hồ yêu đã nằm vùng bên trong Thiên Sa Thương Hội hơn mười năm, leo đến vị trí trung cấp mà không hề bị phát hiện.

## V. Công Pháp & Trận Pháp (功法与阵法)

Sa Mạc Yêu Hồ sở hữu ba kỹ thuật cốt lõi truyền thừa trong tộc. Thứ nhất là Mê Hồn Thuật, ảo thuật tinh thần làm con mồi tin vào thông tin giả, mua hàng giả với giá thật, ký hợp đồng bất lợi mà không hay biết. Thứ hai là Biến Hóa Thuật, bẩm sinh của Hồ yêu, cho phép ngụy trang thành Nhân Tộc gần như hoàn hảo, chỉ có tu sĩ Kim Đan trở lên mới có thể nhìn thấu. Thứ ba là Ảo Ảnh Trận, trận pháp phòng thân: khi bị lộ thân phận, Hồ yêu kích hoạt trận pháp tạo ra hàng chục phân thân giả, lợi dụng hỗn loạn để bỏ chạy. Ba kỹ thuật này không mạnh về sát thương nhưng cực kỳ hiệu quả cho mục đích sinh tồn và tình báo.

## VI. Đặc Sản Môn Phái (门派特产)

- **Hồ Hương Mê Điệp:** Loại hương liệu do Hồ yêu tiết ra tự nhiên, khi pha vào rượu hoặc trà sẽ khiến người uống trở nên cởi mở và dễ nói thật hơn. Không gây hại sức khỏe nhưng cực kỳ hữu ích trong việc khai thác thông tin.
- **Bản Đồ Giả:** Bản đồ sa mạc trông rất tinh xảo nhưng cố tình sai lệch vài chi tiết quan trọng, bán cho những kẻ mà Hồ Nguyệt Nhi muốn dẫn dụ đi lạc hoặc rơi vào bẫy.

## VII. Cơ Sở Hạ Tầng (基础设施)

- **Chuỗi Quán Trọ Nguyệt Nhi:** Ba quán trọ nhỏ đặt dọc Thiên Sa Thương Đạo, mỗi quán do một Hồ yêu cấp cao điều hành. Bề ngoài là quán trọ bình thường phục vụ lữ khách, bên trong là trạm thu thập và trung chuyển thông tin.
- **Hang Mật Nguyệt:** Hang động ngầm nằm sâu dưới một đụn cát lớn, lối vào được ngụy trang bằng Ảo Ảnh Trận. Đây là nơi họp mặt đêm trăng tròn, kho chứa tài sản thật và nơi trú ẩn khẩn cấp khi bị phát hiện.

## VIII. Kinh Tế (经济)

Kinh tế của Sa Mạc Yêu Hồ xoay quanh hai trụ cột chính: kinh doanh hợp pháp và buôn bán thông tin. Chuỗi quán trọ, cửa hàng tạp hóa và quầy bán bản đồ mang lại thu nhập ổn định từ lữ khách và thương nhân. Nhưng nguồn lợi lớn nhất đến từ việc bán thông tin tình báo cho nhiều phía cùng lúc. Hồ Nguyệt Nhi tinh quái ở chỗ bà ta bán thông tin thật xen lẫn thông tin giả, đảm bảo không bên nào có được bức tranh toàn cảnh, chỉ có tộc Yêu Hồ mới nắm giữ toàn bộ sự thật.

## IX. Lịch Sử Tóm Tắt (简史)

Hồ yêu sa mạc từng bị Nhân Tộc truy sát vì lừa đảo lộ liễu. Nhiều đời trước, Hồ yêu sống hoang dã, lừa gạt lữ khách trắng trợn, gây ra thù hận sâu sắc. Hồ Nguyệt Nhi, con cháu của những Hồ yêu sống sót, nhận ra phương thức cũ không bền vững. Bà dẫn tộc nhân chuyển sang chiến lược tinh vi hơn: ngụy trang hoàn hảo thành thương nhân Nhân Tộc, kinh doanh hợp pháp bên ngoài, thu thập và buôn bán thông tin bên trong.

Qua hơn hai trăm năm, mạng lưới của Yêu Hồ đã phủ kín Thiên Sa Thương Đạo. Thậm chí Sa Mạc Hướng Đạo Hội cũng không biết rằng một số hướng đạo mà họ hợp tác thực ra là Hồ yêu ngụy trang. Giờ đây, bất kỳ ai muốn nắm bắt tình hình trên Thương Đạo đều phải mua tin từ mạng lưới của Hồ Nguyệt Nhi, dù không hề biết người bán tin thực chất là ai.

## X. Giai Thoại & Bí Mật (轶事与秘密)

Bí mật lớn nhất của Hồ Nguyệt Nhi là bà ta đồng thời bán thông tin cho cả Thiên Sa Thương Hội lẫn Sa Tặc Liên Minh, hai thế lực thù địch nhất Tây Mạc. Cả hai bên đều coi bà là nguồn tin đáng tin cậy mà không hề biết đối phương cũng đang nhận tin từ cùng một người. Đây là canh bạc cực kỳ nguy hiểm: nếu một trong hai bên phát hiện sự thật, cả gia tộc sẽ bị tiêu diệt.

Trong nội bộ tộc, một Hồ yêu trẻ đã phải lòng thật sự một thương nhân Nhân Tộc và muốn rời bỏ tộc để sống đời thường. Hồ Nguyệt Nhi đang đắn đo chưa quyết định nên cho phép hay phải giết để bảo toàn bí mật. Ngoài ra, Hồ Nguyệt Nhi biết về sự tồn tại của Cổ Sa Yêu Tộc, thế lực yêu tộc cổ đại bí ẩn sâu trong sa mạc, nhưng bà chưa bao giờ dám tiếp xúc vì sợ hãi sức mạnh không thể đo lường của họ.

## XI. Quan Hệ Thế Lực (势力关系)

- **Thiên Sa Thương Hội:** Khách hàng mua tin quan trọng nhất. Hồ Nguyệt Nhi duy trì hình ảnh "thương nhân bán tin đáng tin" trong mắt Thương Hội, đồng thời cài gián điệp nằm vùng bên trong hơn mười năm. Quan hệ bề ngoài hữu hảo, bên trong đầy rẫy lừa dối.
- **Sa Tặc Liên Minh:** Cũng là khách hàng mua tin, nhưng bên Sa Tặc. Hồ Nguyệt Nhi bán cho Sa Tặc thông tin về lịch trình thương đoàn, đổi lại nhận được tin tức về hoạt động cướp bóc. Hai mặt hai tay, nguy hiểm vô cùng.
- **Cổ Sa Yêu Tộc:** Mối quan hệ đơn phương, chỉ có Hồ Nguyệt Nhi biết về sự tồn tại của Cổ Sa Yêu Tộc. Bà sợ họ hơn bất kỳ thế lực Nhân Tộc nào và tuyệt đối tránh xa lãnh địa của họ.
