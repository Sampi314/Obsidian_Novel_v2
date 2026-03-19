---
type: faction
name: Thần Mộc Ký Sinh Tộc
hantu: 神木寄生族
faction_type: Bộ Lạc
alignment: 7
race: Vi Tộc
region: Đông Hoang
founded: Thượng Cổ (cùng thời với Thần Mộc)
founder: Không rõ (Tổ tiên Vi Tộc đầu tiên)
emblem: Than_Moc_Ky_Sinh_Toc.png
specialty: Chăm sóc Thần Mộc, Dược học bào tử, Giao tiếp với cây
economy:
  - Thu hoạch nhựa Thần Mộc (sử dụng nội bộ)
  - Thu thập phấn hoa linh và bào tử dược tính
  - Không có giao thương với bên ngoài
arcs:
  - arc: 1
    status: Ổn định (Cộng sinh với Thần Mộc)
    rank: Không Xếp Hạng
    leader: Tộc Trưởng Vi Mộc
    population: 5000
    territory:
      - Thân, cành và rễ Thần Mộc (Thế Giới Thụ)
      - Các khe nứt và nốt sần trên vỏ cây
    assets:
      - name: Thần Mộc (Thế Giới Thụ)
        type: Tài Nguyên (cộng sinh)
      - name: Kho Nhựa Thần Mộc
        type: Tài Nguyên
      - name: Vườn Bào Tử Linh
        type: Tài Nguyên
    stats: [5, 40, 5, 5000, 10, 5]
    divisions:
      - name: Bộ Lạc Chính
        role: Sinh hoạt, chăm sóc và bảo vệ Thần Mộc
        headcount:
          truong_lao: 5
          chien_binh: 200
          dan_thuong: 4795
        members:
          - character: Vi Mộc
            position: Tộc Trưởng
            cultivation: Trúc Cơ (hấp thụ tự nhiên)
          - character: "[Trưởng Nhánh Đông]"
            position: Trưởng Nhánh
            cultivation: Luyện Khí Hậu Kỳ
            placeholder: true
    relationships:
      - faction: Tinh Linh Vương Đình
        description: Tinh Linh biết Vi Tộc tồn tại trên Thần Mộc nhưng coi như côn trùng vô hại, không quan tâm.
        diplomacy:
          lien_minh: 0
          tin: 5
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 30
      - faction: Nấm Linh Mạng Lưới
        description: Mạng lưới nấm linh dưới gốc Thần Mộc là hàng xóm tự nhiên, đôi khi cung cấp dưỡng chất qua rễ cây.
        diplomacy:
          lien_minh: 10
          tin: 10
          uy_hiep: 0
          thuong_mai: 5
          on_oan: 0
          le_thuoc: 0
      - faction: Dược Thảo Tinh Linh Viện
        description: Nếu biết Vi Tộc sở hữu kiến thức về bào tử và nhựa Thần Mộc, Dược Viện sẽ rất muốn hợp tác, nhưng Vi Tộc quá nhỏ bé để ai chú ý.
        diplomacy:
          lien_minh: 0
          tin: 0
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 0
---

# Thần Mộc Ký Sinh Tộc (神木寄生族)

## I. Tổng Quan (总览)

Thần Mộc Ký Sinh Tộc là một bộ lạc Vi Tộc gồm khoảng 5000 cá thể siêu nhỏ (mỗi cá thể chỉ lớn bằng ngón tay), sống cộng sinh trên Thần Mộc — cây vĩ đại nhất Vĩnh Hằng Sâm Lâm, còn được gọi là Thế Giới Thụ. Với kích thước quá nhỏ bé, Vi Tộc gần như vô hình đối với thế giới tu luyện bên ngoài, không được xếp hạng trong bất kỳ bảng xếp hạng thế lực nào. Tuy nhiên, vai trò thực sự của họ vô cùng quan trọng — Vi Tộc là "bác sĩ" của Thần Mộc, giữ cho cây khỏe mạnh bằng cách tiêu diệt sâu bọ, dọn dẹp mô chết và điều tiết luồng nhựa cây. Nếu không có Vi Tộc, sức khỏe Thần Mộc sẽ suy giảm nghiêm trọng.

## II. Địa Lý & Tài Nguyên (地理与资源)

Vi Tộc xây dựng "thành phố" bên trong vỏ cây, khe nứt và nốt sần trên Thần Mộc, tạo thành một hệ thống cư trú phức tạp trải dài từ rễ đến ngọn. Mỗi nhánh lớn của Thần Mộc là một "quận" riêng biệt với cư dân và trưởng nhánh riêng. Tài nguyên chính là nhựa Thần Mộc — vừa là thức ăn, vừa là vật liệu xây dựng và dược liệu. Phấn hoa linh từ hoa Thần Mộc có đặc tính chữa lành mạnh mẽ, trong khi bào tử từ nấm ký sinh trên vỏ cây chứa dược tính đa dạng mà Vi Tộc đã nghiên cứu hàng vạn năm.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)

Toàn bộ văn hóa Vi Tộc xoay quanh Thần Mộc với triết lý cốt lõi: "Thần Mộc cho ta sự sống, ta trả ơn bằng sự chăm sóc." Mối quan hệ cộng sinh này không phải ký sinh một chiều mà là hợp tác đôi bên — Vi Tộc nhận nhựa cây làm thức ăn, đổi lại tiêu diệt sâu bọ hại cây và dọn dẹp các mô chết trên vỏ. Nghi lễ quan trọng nhất là "Lễ Kết Nối" — mỗi thế hệ mới sinh ra được nhúng vào nhựa Thần Mộc ngay sau khi chào đời, tạo mối liên kết linh hồn vĩnh viễn với cây. Quy tắc nghiêm ngặt nhất là cấm rời Thần Mộc quá lâu, vì xa cây quá 7 ngày thì Vi Tộc sẽ suy yếu dần rồi chết.

## IV. Cơ Cấu Tổ Chức (组织结构)

Tộc Trưởng Vi Mộc là cá thể duy nhất có khả năng giao tiếp với Thần Mộc qua rung động, đóng vai trò "phiên dịch" giữa cây và tộc. Mỗi nhánh lớn của Thần Mộc có một Trưởng Nhánh phụ trách khu vực đó, quản lý dân cư và phân công nhiệm vụ chăm sóc vỏ cây. "Chiến binh" của tộc (khoảng 200 cá thể) chuyên tiêu diệt sâu bọ và ký sinh trùng hại cây — dù nhỏ bé, họ sử dụng vũ khí tẩm nhựa Thần Mộc có tính sát trùng mạnh. Phần lớn dân số (4795 cá thể) là dân thường, làm công việc thu hoạch nhựa, dọn dẹp vỏ cây và nuôi dạy thế hệ mới.

## V. Công Pháp & Trận Pháp (功法与阵法)

Vi Tộc không có công pháp tu luyện chính thống — họ hấp thụ linh khí từ Thần Mộc một cách tự nhiên qua mối liên kết cộng sinh, nên tu vi tăng trưởng rất chậm nhưng ổn định. Tộc Trưởng Vi Mộc đạt tương đương Trúc Cơ sau hàng vạn năm tích lũy tự nhiên. Về phòng thủ, Vi Tộc hoàn toàn dựa vào Thần Mộc — cây tự bảo vệ bằng linh khí mạnh mẽ, và bất kỳ kẻ địch nào đủ sức đe dọa Vi Tộc thì cũng phải đối mặt với phản ứng phòng ngự của cả Thần Mộc. Không có trận pháp riêng.

## VI. Đặc Sản Môn Phái (门派特产)

Nhựa Thần Mộc tinh chế là sản phẩm quý giá nhất của Vi Tộc — một giọt nhựa nguyên chất có thể chữa lành vết thương cấp Trúc Cơ trong vài giờ. Phấn hoa linh từ hoa Thần Mộc có tác dụng an thần và ổn định tâm thức, cực kỳ quý hiếm vì Thần Mộc chỉ ra hoa mỗi 100 năm. Bào tử dược tính từ nấm ký sinh trên vỏ cây được Vi Tộc nghiên cứu và phân loại qua hàng vạn năm, tạo thành kho kiến thức dược liệu mà không tông phái nào trên thế giới sở hữu. Tuy nhiên, tất cả sản phẩm chỉ dùng nội bộ vì Vi Tộc không giao thương với bên ngoài.

## VII. Cơ Sở Hạ Tầng (基础设施)

"Thành phố" của Vi Tộc là mạng lưới đường hầm và phòng ốc bên trong vỏ cây Thần Mộc, được xây dựng bằng nhựa cây đông cứng và sợi gỗ vi mô. Hệ thống bao gồm khu cư trú trên mỗi nhánh lớn, kho nhựa dự trữ ở gốc cây, vườn bào tử chuyên nuôi trồng nấm dược liệu, và đền thờ trung tâm — nơi Tộc Trưởng giao tiếp với Thần Mộc. Giao thông giữa các nhánh dựa vào hệ thống dây nhựa kéo dài theo thân cây, cho phép Vi Tộc di chuyển nhanh chóng từ rễ đến ngọn.

## VIII. Kinh Tế (经济)

Kinh tế của Vi Tộc hoàn toàn tự cung tự cấp trong phạm vi Thần Mộc. Nhựa cây là "đồng tiền" và thức ăn chính; phấn hoa linh được phân phối đều cho toàn tộc; bào tử dược tính được kho trữ cho mục đích y tế. Không có khái niệm buôn bán, lợi nhuận hay tích lũy tài sản — mọi thứ thuộc về tập thể. Hệ thống kinh tế này ổn định vì Thần Mộc cung cấp dồi dào, nhưng cũng cực kỳ mong manh — nếu Thần Mộc suy yếu, toàn bộ nền kinh tế sụp đổ ngay lập tức.

## IX. Lịch Sử Tóm Tắt (简史)

Thần Mộc Ký Sinh Tộc đã sống trên Thần Mộc từ khi cây còn non — hàng vạn năm trước, khi Vĩnh Hằng Sâm Lâm mới bắt đầu hình thành. Tổ tiên Vi Tộc là những sinh vật vi mô đầu tiên bám vào vỏ cây non, dần dần tiến hóa thành chủng tộc có ý thức nhờ hấp thụ linh khí từ cây. Qua hàng vạn năm cộng sinh, mối liên kết giữa Vi Tộc và Thần Mộc trở nên không thể tách rời — cây cần Vi Tộc để duy trì sức khỏe, Vi Tộc cần cây để tồn tại. Tinh Linh Vương Đình biết có Vi Tộc trên Thần Mộc nhưng luôn coi họ là "côn trùng vô hại," không đáng để ý — một sự hiểu lầm mà Vi Tộc rất vui lòng duy trì.

## X. Giai Thoại & Bí Mật (轶事与秘密)

Thần Mộc có ý thức riêng, và Vi Mộc là người duy nhất có thể nghe được "tiếng nói" của nó. Nhưng nội dung Thần Mộc truyền đạt khiến Vi Mộc sợ hãi đến mức không dám kể cho bất kỳ ai — hắn biết điều gì đó về bản chất thật sự của Thần Mộc, về lý do cây tồn tại, và về thứ gì đó đang ngủ sâu trong lõi gốc cây. Nỗi sợ này đè nặng lên hắn mỗi ngày, nhưng hắn không dám ngừng lắng nghe vì đó là trách nhiệm của Tộc Trưởng.

Nếu Thần Mộc chết, toàn bộ 5000 Vi Tộc trên cây cũng diệt vong trong vài ngày — mối liên kết cộng sinh sâu đến mức không thể tách rời. Đây là mối nguy hiểm sinh tử thường trực mà không ai bên ngoài quan tâm, vì trong mắt thế giới tu luyện, Vi Tộc quá nhỏ bé để đáng được chú ý.

## XI. Quan Hệ Thế Lực (势力关系)

- **Tinh Linh Vương Đình:** Tinh Linh là "chủ nhà" danh nghĩa của Vĩnh Hằng Sâm Lâm, biết Vi Tộc tồn tại nhưng coi là côn trùng không đáng bận tâm. Vi Tộc lợi dụng sự thờ ơ này để sống yên ổn, không muốn thu hút sự chú ý.
- **Nấm Linh Mạng Lưới:** Mạng lưới nấm linh dưới gốc Thần Mộc là hàng xóm tự nhiên, đôi khi cung cấp khoáng chất qua rễ cây. Quan hệ trung lập, cả hai đều là thành phần của hệ sinh thái Thần Mộc.
- **Dược Thảo Tinh Linh Viện:** Nếu Dược Viện biết về kiến thức dược liệu vạn năm của Vi Tộc, họ sẽ rất muốn hợp tác — nhưng Vi Tộc quá nhỏ bé để ai chú ý, và họ cũng không muốn bị chú ý.
