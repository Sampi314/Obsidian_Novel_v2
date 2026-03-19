---
type: faction
name: San Hô Thợ Lặn Đội
hantu: 珊瑚潜水队
faction_type: Hội
alignment: 2
race: Nhân Tộc
region: Tây Mạc
founded: Khoảng 30 năm trước khi truyện bắt đầu
founder: Cha của Nguyễn Thủy Tiên (phàm nhân)
emblem: San_Ho_Tho_Lan.png
specialty: Lặn thu hoạch san hô linh, Ngưng Tức Thuật, Khai thác ngọc trai hoang dã
economy:
- Thu hoạch san hô linh cấp thấp bán cho Thiên Sa Thương Hội
- Khai thác ngọc trai hoang dã và vỏ sò đặc biệt
- Nhận hợp đồng thăm dò vùng nước nông ven bờ
arcs:
  - arc: 1
    status: Hoạt động ổn định nhưng bị ép giá
    rank: Không Xếp Hạng
    leader: Đội Trưởng Nguyễn Thủy Tiên
    population: 26
    territory:
      - Bến cảng nhỏ ven bờ biển nam Vô Tận Hải
      - Vùng rạn san hô nước nông (dưới 20 trượng)
    assets:
      - name: Bến cảng nhỏ
        type: Công Trình
      - name: Đèn chiếu sáng dưới nước
        type: Pháp Khí
      - name: Dao cắt san hô
        type: Pháp Khí
    stats: [15, 20, 10, 26, 5, 8]
    divisions:
      - name: Tổ Lặn Kỳ Cựu
        role: Lặn sâu thu hoạch san hô linh và ngọc trai quý
        headcount:
          hoi_truong: 1
          pho_hoi_truong: 0
          thanh_vien: 5
          tong_quan: 0
        members:
          - character: Nguyễn Thủy Tiên
            position: Đội Trưởng
            cultivation: Trúc Cơ Viên Mãn
          - character: "[Thợ Lặn Kỳ Cựu]"
            position: Thợ Lặn Cấp Cao
            cultivation: Luyện Khí Trung Kỳ
            placeholder: true
      - name: Tổ Lặn Thường
        role: Thu hoạch san hô ở vùng nước nông và vận chuyển sản phẩm
        headcount:
          hoi_truong: 0
          pho_hoi_truong: 0
          thanh_vien: 20
          tong_quan: 0
        members:
          - character: "[Thợ Lặn Thường]"
            position: Thợ Lặn
            cultivation: Luyện Khí Sơ Kỳ
            placeholder: true
    relationships:
      - faction: Thiên Sa Thương Hội
        description: Bên mua duy nhất, ép giá thu mua sản phẩm san hô linh với giá rẻ mạt. Đội không có lựa chọn khác.
        diplomacy:
          lien_minh: -10
          tin: 20
          uy_hiep: 70
          thuong_mai: 80
          on_oan: -30
          le_thuoc: 80
      - faction: San Hô Thủ Hộ Đoàn
        description: Cùng hoạt động tại vùng rạn san hô, tôn trọng lẫn nhau. Thợ Lặn Đội tuân thủ quy tắc khai thác bền vững.
        diplomacy:
          lien_minh: 20
          tin: 40
          uy_hiep: 0
          thuong_mai: 10
          on_oan: 0
          le_thuoc: 0
      - faction: Hải Tộc (Tiểu Ngư Nhân Thôn)
        description: Hai bên tránh nhau, không xung đột nhưng cũng không giao tiếp. Vùng hoạt động bị giới hạn để tránh va chạm.
        diplomacy:
          lien_minh: 0
          tin: 10
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 0
---

# San Hô Thợ Lặn Đội (珊瑚潜水队)

## I. Tổng Quan (总览)
San Hô Thợ Lặn Đội là một đội thợ lặn nhỏ chuyên thu hoạch san hô linh cấp thấp tại vùng rạn san hô ven bờ biển nam Vô Tận Hải. Với chỉ hai mươi sáu thành viên, phần lớn là phàm nhân hoặc tu sĩ Luyện Khí sơ kỳ, đội tồn tại bằng nghề lặn truyền thống do cha của Đội Trưởng Nguyễn Thủy Tiên sáng lập. Dù sản phẩm thu hoạch có giá trị nhất định trên thị trường, đội bị Thiên Sa Thương Hội ép giá thu mua, khiến đời sống thành viên luôn trong cảnh chật vật. Nguyễn Thủy Tiên là người duy nhất trong đội đạt cảnh giới Trúc Cơ Viên Mãn, vừa là trụ cột chiến lực vừa là linh hồn của toàn đội.

## II. Địa Lý & Tài Nguyên (地理与资源)
Đội hoạt động tại vùng rạn san hô gần bờ biển nam Vô Tận Hải, nơi nước nông đủ để thợ lặn phàm nhân làm việc an toàn. Bến cảng nhỏ của đội nằm ẩn mình trong một vịnh đá tự nhiên, che chắn khỏi sóng lớn và gió biển. Tài nguyên chính bao gồm san hô linh cấp thấp, ngọc trai hoang dã, và các loại vỏ sò đặc biệt có thể dùng làm nguyên liệu luyện đan. Tuy nhiên, vùng hoạt động bị giới hạn nghiêm ngặt ở độ sâu dưới hai mươi trượng, bởi vượt quá ranh giới đó là lãnh địa của Hải Tộc. Đôi khi thợ lặn bắt gặp dấu hiệu của Tiểu Ngư Nhân Thôn ở rìa vùng hoạt động, hai bên ngầm tránh nhau mà không xảy ra xung đột.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
Thành viên San Hô Thợ Lặn Đội phần lớn là thợ lặn chuyên nghiệp, quen giữ hơi dưới nước lâu hơn người thường nhờ rèn luyện từ nhỏ. Đội tuân thủ nghiêm ngặt quy tắc "chỉ lấy đủ dùng" để không làm cạn kiệt rạn san hô, bởi họ hiểu rằng nếu rạn san hô chết đi, sinh kế của đội cũng chấm dứt. Trước mỗi lần lặn, toàn đội tập trung tại bến cảng làm lễ xin phép biển cả, thắp hương và rải cánh hoa xuống nước. Nghi lễ này mang tính mê tín nhưng không một ai dám bỏ qua, bởi những thợ lặn từng coi thường nghi thức đều gặp xui xẻo dưới nước. Tinh thần đoàn kết của đội rất cao, mỗi thành viên coi nhau như anh em ruột thịt, cùng chia sẻ gian khổ và thu nhập.

## IV. Cơ Cấu Tổ Chức (组织结构)
Cơ cấu của đội đơn giản và gọn nhẹ, không có hệ thống quan liêu phức tạp. Đội Trưởng Nguyễn Thủy Tiên đứng đầu, vừa điều phối hoạt động lặn vừa đàm phán giao dịch với bên ngoài. Dưới cô là năm thợ lặn kỳ cựu ở cảnh giới Luyện Khí trung kỳ, mỗi người phụ trách hướng dẫn một nhóm nhỏ thợ lặn thường. Hai mươi thợ lặn còn lại phần lớn ở Luyện Khí sơ kỳ hoặc là phàm nhân thuần túy, phụ trách thu hoạch ở vùng nước nông nhất. Mọi quyết định quan trọng đều do Thủy Tiên đưa ra sau khi tham khảo ý kiến các thợ lặn kỳ cựu, tạo nên bầu không khí dân chủ và gắn bó.

## V. Công Pháp & Trận Pháp (功法与阵法)
Công pháp duy nhất mà đội sử dụng là Ngưng Tức Thuật, một kỹ thuật hô hấp đặc biệt cho phép người luyện nín thở dưới nước lâu hơn phàm nhân rất nhiều. Thợ lặn lão luyện nhất có thể nín thở dưới nước một canh giờ liên tục, vẫn kém xa so với tu sĩ thủy hệ chân chính nhưng đã vượt trội hơn hẳn phàm nhân thông thường. Đội không sở hữu trận pháp nào, chỉ trang bị pháp khí cấp thấp bao gồm đèn chiếu sáng dưới nước và dao chuyên dụng để cắt san hô. Khả năng chiến đấu gần như không có, nếu gặp nguy hiểm, đội chỉ có thể dựa vào Nguyễn Thủy Tiên hoặc bỏ chạy lên bờ.

## VI. Đặc Sản Môn Phái (门派特产)
San hô linh cấp thấp là sản phẩm chủ lực của đội, được sử dụng làm nguyên liệu phụ trong luyện đan và trang trí linh khí. Ngọc trai hoang dã thu hoạch từ vùng rạn san hô tuy không quý hiếm bằng ngọc trai nuôi cấy của Hải Tộc, nhưng vẫn có giá trị nhất định trên thị trường dược liệu. Ngoài ra, đội còn thu gom các loại vỏ sò đặc biệt có chứa vi lượng linh lực, dùng làm nguyên liệu cho phù lục thủy hệ cấp thấp.

## VII. Cơ Sở Hạ Tầng (基础设施)
Bến cảng nhỏ của đội nằm trong vịnh đá tự nhiên, được gia cố bằng gỗ và đá san hô khô. Trên bến có một nhà kho chứa dụng cụ lặn và sản phẩm thu hoạch chờ giao dịch. Khu sinh hoạt chung gồm vài túp lều tranh sát bờ biển, nơi thành viên nghỉ ngơi giữa các ca lặn. Trang thiết bị nghèo nàn, không có kết giới phòng thủ hay trận pháp bảo vệ, toàn bộ an ninh phụ thuộc vào vị trí kín đáo của vịnh và sự cảnh giác của thợ lặn.

## VIII. Kinh Tế (经济)
Nền kinh tế của đội hoàn toàn phụ thuộc vào việc bán sản phẩm san hô linh cho Thiên Sa Thương Hội. Giá thu mua bị ép xuống mức rẻ mạt, nhưng đội không có kênh phân phối nào khác nên đành chấp nhận. Thu nhập chia đều cho toàn đội sau khi trừ chi phí dụng cụ và lương thực, mỗi thành viên chỉ đủ sống qua ngày. Nguyễn Thủy Tiên từng cố gắng tìm người mua khác nhưng đều bị Thương Hội ngăn cản, khiến đội rơi vào thế bị lệ thuộc kinh tế gần như hoàn toàn.

## IX. Lịch Sử Tóm Tắt (简史)
San Hô Thợ Lặn Đội được thành lập bởi cha của Nguyễn Thủy Tiên, một thợ lặn phàm nhân nổi tiếng trong vùng. Ông tập hợp những ngư dân nghèo ven biển, dạy họ kỹ thuật lặn sâu và nhận biết san hô linh, biến nghề lặn thành nguồn sinh kế ổn định. Sau khi ông mất vì tai nạn dưới nước khi lặn quá sâu vào vùng cấm, Nguyễn Thủy Tiên kế thừa vị trí đội trưởng khi còn rất trẻ. Cô tự mày mò tu luyện Ngưng Tức Thuật từ một cuốn bí kíp cũ và dần đạt đến Trúc Cơ Viên Mãn, trở thành trụ cột sức mạnh duy nhất của đội. Từng có hai thợ lặn bị hải thú tấn công khi lặn quá sâu và mất mạng, bài học đau thương đó khiến đội lập ra quy tắc giới hạn độ sâu nghiêm ngặt.

## X. Giai Thoại & Bí Mật (轶事与秘密)
Trong một lần lặn sâu hơn bình thường, đội phát hiện mảnh vỡ của một pháp khí cổ đại nằm sâu trong rạn san hô, tỏa ra ánh sáng mờ nhạt màu xanh lam. Tuy nhiên, không ai dám lấy vì sợ Hải Tộc phát hiện và trả thù. Nguyễn Thủy Tiên từng nghe một lão ngư kể rằng rạn san hô nơi đội hoạt động thực ra là xác hóa thạch của một con hải thú thượng cổ khổng lồ, và san hô linh hình thành chính là nhờ linh lực tàn dư trong xương cốt của nó. Ngoài ra, có một vùng san hô phát sáng kỳ dị vào lúc nửa đêm mỗi tháng một lần, thợ lặn trong đội coi đó là điềm xui và tuyệt đối không ai dám lặn xuống vào thời điểm đó.

## XI. Quan Hệ Thế Lực (势力关系)
- **Thiên Sa Thương Hội:** Bên mua duy nhất, ép giá thu mua san hô linh. Đội bị lệ thuộc kinh tế nhưng âm thầm bất mãn.
- **San Hô Thủ Hộ Đoàn:** Quan hệ hữu hảo, cùng bảo vệ hệ sinh thái rạn san hô. Thủy Tiên thi thoảng trao đổi thông tin về tình trạng rạn san hô với Thủy Linh Nhi.
- **Hải Tộc (Tiểu Ngư Nhân Thôn):** Trung lập, hai bên ngầm tránh nhau. Thợ Lặn Đội không xâm phạm vùng nước sâu, Hải Tộc không can thiệp vùng nước nông.
