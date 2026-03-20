---
type: faction
name: Lưu Vong Thuyền Đội
hantu: 流亡船队
faction_type: Liên Minh
alignment: -2
race: Đa chủng (Nhân Tộc chủ yếu)
region: Đông Hoang
founded: Cách đây 100 năm
founder: Vạn Lý Phong
emblem: Thuyen_Buom_Tren_Song.png
specialty: Hàng hải và sinh tồn trên biển, Ẩn mê thuật hải dương, Mạng lưới tình báo hải lưu
economy:
- Đánh bắt hải sản và lọc nước biển
- Trao đổi hàng hóa với thương thuyền đi ngang
- Dịch vụ vận chuyển bí mật cho kẻ đào vong
arcs:
  - arc: 1
    status: Trôi nổi ổn định
    rank: Hạng Tư
    leader: Thuyền Chủ Vạn Lý Phong
    population: 800
    territory:
      - Vô Tận Hải (không cố định, di chuyển theo hải lưu)
    assets:
      - name: Đội Thuyền (40+ chiếc)
        type: Hạm Đội
      - name: Ẩn Mê Phù
        type: Pháp Khí
      - name: Ngọc Giản Bí Ẩn
        type: Bí Bảo
    stats: [300, 200, 150, 800, 250, 180]
    divisions:
      - name: Hội Đồng Biển
        role: Cơ quan quyết sách tối cao, gồm bảy trưởng thuyền lớn nhất, họp khi có chuyện quan trọng
        headcount:
          tuong: 1
          uy: 7
          binh: 792
        members:
          - character: Vạn Lý Phong
            position: Thuyền Chủ
            cultivation: Kim Đan Trung Kỳ
          - character: "[Hải Vân Nương]"
            position: Trưởng Thuyền Nhị
            cultivation: Trúc Cơ Viên Mãn
            placeholder: true
          - character: "[Lão Mỏ Neo]"
            position: Trưởng Thuyền Tam
            cultivation: Trúc Cơ Hậu Kỳ
            placeholder: true
    relationships:
      - faction: Hắc Hải Hải Tặc
        description: Kẻ thù truyền kiếp — Hắc Hải từng suýt nuốt trọn thuyền đội khi Vạn Lý Phong chưa đột phá Kim Đan. Hai bên chạm mặt trên biển là đánh, không có đàm phán.
        diplomacy:
          lien_minh: -60
          tin: 0
          uy_hiep: 50
          thuong_mai: 0
          on_oan: -80
          le_thuoc: 0
      - faction: Hải Thần Cung
        description: Tránh mặt — Lưu Vong Thuyền Đội luôn đi vòng quanh lãnh hải Hải Thần Cung, không dám xâm phạm. Đổi lại, Hải Thần Cung coi thuyền đội quá nhỏ bé để bận tâm.
        diplomacy:
          lien_minh: 0
          tin: 10
          uy_hiep: 30
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 0
      - faction: Phong Bạo Thương Đội
        description: Đối tác thương mại chính trên biển — Phong Bạo Thương Đội là một trong số ít thế lực sẵn sàng giao dịch với thuyền đội đào vong mà không hỏi xuất xứ hàng hóa.
        diplomacy:
          lien_minh: 20
          tin: 30
          uy_hiep: 0
          thuong_mai: 50
          on_oan: 10
          le_thuoc: 10
---

# Lưu Vong Thuyền Đội (流亡船队)

## I. Tổng Quan (总览)
Lưu Vong Thuyền Đội là một "thành phố nổi" gồm hơn bốn mươi chiếc thuyền lớn nhỏ buộc lại với nhau, trôi theo hải lưu trên vùng biển sâu Vô Tận Hải. Thành viên là những kẻ đào vong từ khắp đại lục — tội phạm trốn án, con nợ bỏ trốn, kẻ bị tông phái truy sát, hoặc đơn giản là những người không còn nơi nào trên đất liền dung thân. Dẫn dắt bởi Thuyền Chủ Vạn Lý Phong — một cựu thương nhân phá sản tu đến Kim Đan Trung Kỳ — thuyền đội không bao giờ cập bến, tồn tại hoàn toàn trên mặt biển và duy trì sự sống bằng đánh cá, lọc nước, cùng trao đổi hàng hóa với thương thuyền đi ngang. Với tám trăm người sống chen chúc trên những con thuyền cũ kỹ, đây là nơi trú ẩn cuối cùng của những kẻ bị thế giới từ bỏ.

## II. Địa Lý & Tài Nguyên (地理与资源)
Lưu Vong Thuyền Đội không có lãnh thổ cố định — đội thuyền di chuyển liên tục theo hải lưu ấm, tránh bão và tránh va chạm với các thế lực hải dương lớn. Khi buộc lại với nhau, đội thuyền trải dài gần nửa dặm trên mặt biển, tạo thành một quần thể nổi với cầu ván nối giữa các thuyền. Thuyền chính của Vạn Lý Phong là chiếc lớn nhất, dài mười lăm trượng, đóng vai trò trung tâm mà các thuyền nhỏ xoay quanh. Tài nguyên hoàn toàn phụ thuộc vào biển: cá và hải sản là nguồn thực phẩm chính, nước biển được lọc qua trận pháp đơn giản, và gỗ tốt — thứ quý giá nhất — chỉ có được khi gặp xác thuyền đắm hoặc trao đổi với thương thuyền. Mọi thứ trên thuyền đội đều cũ kỹ, vá víu, và sử dụng đến khi không thể sửa được nữa.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
Luật duy nhất của thuyền đội là: "Không hỏi quá khứ, không phản bội thuyền đội." Mọi thành viên, dù xuất thân từ đâu hay mang tội gì, đều được đối xử bình đẳng kể từ khi bước lên thuyền. Quá khứ bị xóa sạch — không ai được phép tra hỏi người khác về lý do họ ra biển. Đổi lại, phản bội thuyền đội là tội chết duy nhất: kẻ phản bội bị trói vào mảnh ván và thả xuống biển cho sóng cuốn đi. Trẻ em sinh ra trên thuyền chưa bao giờ thấy đất liền, gọi biển là "nhà" và coi tiếng sóng là nhạc ru. Chúng lớn lên biết bơi trước khi biết đi, biết đọc hải lưu trước khi biết đọc chữ. Văn hóa thuyền đội rất thực dụng và bình đẳng — không phân biệt chủng tộc, giới tính hay tu vi, chỉ cần có ích cho cộng đồng là được chấp nhận.

## IV. Cơ Cấu Tổ Chức (组织结构)
Vạn Lý Phong là Thuyền Chủ, nắm quyền quyết định hướng đi và các vấn đề sống còn của thuyền đội. Dưới ông là Hội Đồng Biển gồm bảy trưởng thuyền lớn nhất, mỗi người tự quản lý con thuyền và thành viên trên đó. Hội Đồng họp khi có chuyện quan trọng: thay đổi tuyến đường, đối phó hải tặc, hoặc quyết định nhận thành viên mới. Mỗi thuyền lớn có từ ba mươi đến sáu mươi người, hoạt động như một "khu phố" tự trị với người đánh cá, thợ sửa thuyền, và vài tu sĩ cấp thấp canh gác. Tổng dân số khoảng tám trăm người, đa phần phàm nhân và Luyện Khí, chỉ vài chục Trúc Cơ và duy nhất Vạn Lý Phong đạt Kim Đan. Quy trình nhận thành viên mới rất đơn giản: kẻ xin gia nhập được hỏi một câu duy nhất — "Có chỗ nào quay về không?" Nếu trả lời "không" thì được nhận.

## V. Công Pháp & Trận Pháp (功法与阵法)
Vạn Lý Phong tu luyện "Thuận Phong Quyết" — công pháp phong hệ cho phép điều khiển gió đẩy thuyền, đồng thời cảm nhận biến đổi thời tiết trước cả ngày. Nhờ công pháp này, thuyền đội có thể tránh bão hiệu quả và di chuyển nhanh hơn thuyền thông thường. Ngoài ra, mỗi thuyền trong đội đều được gắn "Ẩn Mê Phù" — loại phù lục đơn giản tạo ra ảo giác khiến thuyền đội khó bị phát hiện từ xa. Từ ngoài nhìn vào, đội thuyền trông như một đám sương mù trôi trên biển, không thu hút sự chú ý. Ẩn Mê Phù không đủ mạnh để qua mắt tu sĩ Kim Đan, nhưng đủ để tránh hải tặc Trúc Cơ và các đội tuần tra thông thường.

## VI. Đặc Sản Môn Phái (门派特产)
- **Hải Vật Hiếm:** Thuyền đội đánh bắt được nhiều loại hải sản linh hiếm mà thuyền thương mại không tìm thấy vì đội hoạt động ở vùng biển sâu ít ai dám đến. Nội đan hải thú, ngọc trai linh, và tảo biển linh dược là những mặt hàng có giá trị nhất.
- **Bản Đồ Hải Lưu:** Một trăm năm trôi nổi trên biển tích lũy kiến thức đồ sộ về hải lưu, vùng bão, và lãnh hải các thế lực hải dương. Bản đồ này là tài sản bí mật tối quan trọng, chỉ Vạn Lý Phong và các trưởng thuyền biết.
- **Dịch Vụ Đào Vong:** Đôi khi thuyền đội nhận tiền để chở kẻ trốn chạy ra biển, giúp họ biến mất khỏi tầm truy sát của kẻ thù trên đất liền.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Thuyền Chính "Vạn Lý Hào":** Chiếc thuyền lớn nhất dài mười lăm trượng, đóng vai trò trung tâm hành chính và nơi ở của Vạn Lý Phong. Khoang sâu nhất bị khóa kín, không ai được phép vào ngoài Thuyền Chủ.
- **Cầu Ván Liên Thuyền:** Hệ thống cầu ván và dây thừng nối các thuyền lại với nhau, cho phép cư dân di chuyển giữa các "khu phố" mà không cần xuống nước.
- **Chợ Nổi:** Khu vực trung tâm nơi các thuyền nhỏ nhất tập trung, hoạt động như chợ trao đổi hàng hóa nội bộ và nơi tiếp đón thương thuyền bên ngoài.
- **Xưởng Sửa Thuyền:** Một chiếc thuyền phẳng chuyên dùng để kéo thuyền hỏng lên sửa chữa, trang bị dụng cụ thủ công thô sơ nhưng đủ dùng.

## VIII. Kinh Tế (经济)
Kinh tế thuyền đội vận hành theo mô hình tự cung tự cấp kết hợp trao đổi hàng hóa. Bảy mươi phần trăm thực phẩm đến từ đánh cá và thu hoạch tảo biển, phần còn lại trao đổi với thương thuyền đi ngang. Thuyền đội bán hải vật hiếm, nội đan hải thú, và đôi khi cả thông tin tình báo về tuyến đường biển để đổi lấy gỗ, vải, dược liệu, và linh thạch. Không có tiền tệ nội bộ — mọi giao dịch trong thuyền đội dùng hệ thống ghi nợ do Hội Đồng Biển quản lý. Kinh tế không giàu có nhưng đủ duy trì sự sống, và Vạn Lý Phong luôn ưu tiên an toàn hơn lợi nhuận — nếu giao dịch nào có nguy cơ lộ vị trí, ông sẵn sàng từ chối dù giá cao.

## IX. Lịch Sử Tóm Tắt (简史)
Một trăm năm trước, Vạn Lý Phong vốn là thương nhân khá giả ở lục địa, nhưng bị đối tác phản bội dẫn đến phá sản và mang nợ lớn với một thế lực ngầm. Không còn đường sống trên đất liền, ông dẫn gia đình lên thuyền ra biển trốn nợ. Trên biển, ông dần thu nhận thêm những kẻ lang thang tương tự — cựu binh đào ngũ, tội phạm bị truy nã, tu sĩ thất bại — từ một thuyền thành ba, rồi mười, rồi cả đội. Bước ngoặt lớn nhất xảy ra hai mươi năm trước khi Hắc Hải Hải Tặc phát hiện thuyền đội và đem quân tấn công, suýt nuốt trọn. Trong lúc tuyệt vọng, Vạn Lý Phong đột phá Kim Đan, triệu hồi cuồng phong đánh chìm ba thuyền hải tặc, cứu sống cả đội. Từ đó uy tín của ông không ai dám nghi ngờ, và Lưu Vong Thuyền Đội chính thức trở thành một thế lực được các hải phường công nhận.

## X. Giai Thoại & Bí Mật (轶事与秘密)
Có tin đồn thuyền đội từng đi qua "Vùng Biển Chết" — một khu vực trên Vô Tận Hải mà ngay cả Hải Thần Cung cũng tránh xa. Nơi đó nước biển chuyển đen, la bàn quay loạn, và mọi thuyền đi vào đều không trở ra. Lưu Vong Thuyền Đội tuyên bố đã vô tình lạc vào và sống sót, nhưng không ai giải thích được bằng cách nào — Vạn Lý Phong từ chối nói về chuyện này.

Khoang thuyền chính bị khóa kín của Vạn Lý Phong chứa một thứ bí mật mà không ai biết. Một vài trưởng thuyền cũ từng nghe thấy tiếng vo vo kỳ lạ phát ra từ đó vào những đêm trăng tròn, nhưng không dám hỏi. Ngoài ra, đội thuyền từng cứu được một tu sĩ trọng thương trôi dạt trên biển — người đó để lại một cuốn ngọc giản trước khi chết, nội dung chưa ai giải mã được dù đã thử nhiều cách.

Gần đây, một thuyền nhỏ ở rìa đội phát hiện xác một sinh vật biển lạ trôi nổi — thân dài hơn mười trượng, vảy đen bóng, và mang trên mình vết thương sâu như bị vũ khí linh lực gây ra. Không ai trong thuyền đội nhận ra đây là sinh vật gì, nhưng Vạn Lý Phong đích thân ra xem và lập tức ra lệnh đẩy xác ra xa, không ai được chạm vào. Ông nhận ra rằng vết thương trên thân sinh vật mang dấu vết của công pháp Long Cung — nghĩa là gần đây Long Cung đã giao chiến với thứ gì đó ở vùng biển sâu, và chiến trường ấy không xa thuyền đội. Ông lặng lẽ ra lệnh thay đổi hướng đi, rời xa khu vực đó càng nhanh càng tốt.

## XI. Quan Hệ Thế Lực (势力关系)
- **Hắc Hải Hải Tặc:** Kẻ thù sinh tử — hai mươi năm trước suýt bị tiêu diệt, hiện tại hai bên vẫn đánh nhau khi chạm mặt trên biển. Hắc Hải muốn trả thù vụ mất ba thuyền.
- **Hải Thần Cung:** Tránh mặt hoàn toàn — thuyền đội luôn đi vòng quanh lãnh hải Hải Thần Cung, không dám xâm phạm. Hải Thần Cung coi họ quá nhỏ để bận tâm.
- **Phong Bạo Thương Đội:** Đối tác thương mại chính, một trong số ít thế lực sẵn sàng giao dịch mà không hỏi xuất xứ hàng hóa hay thân phận người bán.
- **Độc Đảo Lưu Dân:** Đôi khi trao đổi hàng hóa khi thuyền đội trôi qua gần các hòn đảo có lưu dân cư trú, quan hệ trung lập và thận trọng.
