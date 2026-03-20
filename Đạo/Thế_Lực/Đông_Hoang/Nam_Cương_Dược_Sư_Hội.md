---
type: faction
name: Nam Cương Dược Sư Hội
hantu: 南疆药师会
faction_type: Hội
alignment: 4
race: Nhân Tộc
region: Đông Hoang
founded: 80 năm trước
founder: Nhóm dược sư lang thang vùng Nam Cương
emblem: Nam_Cuong_Duoc_Su_Hoi.png
specialty: Bào chế đan dược cấp thấp, Thu mua dược liệu, Chữa trị thương tật
economy:
- Thu mua dược liệu từ vùng rìa Nam Cương
- Bán lẻ đan dược thành phẩm từ Đan Hà Cốc
- Bào chế đan dược cấp thấp (Luyện Khí Đan, Trúc Cơ Đan)
- Tổ chức Dược Hội mùa xuân hàng năm
arcs:
  - arc: 1
    status: Hoạt động ổn định
    rank: Hạng Năm
    leader: Hội Trưởng Lâm Dược Nương
    population: 60
    territory:
      - Khu chợ dược liệu Trạm Biên Nam Cương
      - Kho bảo quản dược liệu
    assets:
      - name: Khu Chợ Dược Liệu (30+ quầy hàng)
        type: Công Trình
      - name: Kho Bảo Quản Đá Lạnh
        type: Công Trình
      - name: Mạng lưới thu mua dược liệu Nam Cương
        type: Tài Nguyên
    stats: [20, 100, 90, 60, 30, 70]
    divisions:
      - name: Ban Bào Chế & Buôn Bán
        role: Bào chế đan dược, quản lý quầy hàng, và thu mua dược liệu
        headcount:
          hoi_truong: 1
          pho_hoi_truong: 1
          thanh_vien: 15
          tong_quan: 43
        members:
          - character: Lâm Dược Nương
            position: Hội Trưởng
            cultivation: Trúc Cơ Hậu Kỳ
          - character: Tôn Bách Dược
            position: Phó Hội Trưởng
            cultivation: Trúc Cơ Trung Kỳ
    relationships:
      - faction: Dược Vương Cốc
        description: Đối tác thương mại chính, mua đan dược thành phẩm về bán lẻ. Phải bán dược liệu giá rẻ cho Cốc để đổi lấy sự bảo hộ.
        diplomacy:
          lien_minh: 30
          tin: 40
          uy_hiep: 20
          thuong_mai: 70
          on_oan: 10
          le_thuoc: 50
      - faction: Huyết Thảo Đường
        description: Đối thủ cạnh tranh trong lĩnh vực dược liệu, nhưng Huyết Thảo Đường chuyên dược liệu tà thuật khiến hai bên ít chồng chéo.
        diplomacy:
          lien_minh: -10
          tin: -20
          uy_hiep: 10
          thuong_mai: -30
          on_oan: -15
          le_thuoc: 0
      - faction: Hoang Dã Thợ Săn Bang
        description: Thợ săn thường mang dược liệu hiếm từ vùng hoang dã về bán cho Hội, đồng thời mua thuốc trị thương trước khi lên đường.
        diplomacy:
          lien_minh: 10
          tin: 20
          uy_hiep: 0
          thuong_mai: 50
          on_oan: 5
          le_thuoc: 0
---

# Nam Cương Dược Sư Hội (南疆药师会)

## I. Tổng Quan (总览)
> *"Thuốc không chọn bệnh nhân, dược sư không chọn khách — ai trả tiền, ta bán thuốc. Ai cần cứu, ta cứu."*
> — Lâm Dược Nương, phát biểu tại Dược Hội mùa xuân

> *"Bách Dược lão nhân biết nhiều bí phương hơn số tóc trên đầu — nhưng bí phương nào cũng đáng giá một mạng người."*
> — Lời đồn trong giới tán tu Trạm Biên


Nam Cương Dược Sư Hội là tổ chức nghề nghiệp quy tụ các dược sư hoạt động tại Trạm Biên Nam Cương — vùng biên giới phía nam Đông Hoang. Với triết lý "Dược sư không chọn bệnh nhân", Hội chữa trị cho mọi chủng tộc kể cả yêu tộc nếu trả tiền, và kiên quyết giữ tiêu chuẩn chất lượng dược phẩm. Dù chỉ là tổ chức Hạng Năm với khoảng 60 thành viên, Hội nắm vai trò quan trọng trong mạng lưới cung ứng dược liệu vùng rìa, đồng thời tổ chức Dược Hội mùa xuân — sự kiện thương mại lớn nhất khu vực Trạm Biên hàng năm. Hội Trưởng Lâm Dược Nương điều hành với phong cách ôn hòa nhưng cứng rắn, biến một nhóm dược sư lang thang thành tổ chức có uy tín và tiếng nói tại vùng biên.

## II. Địa Lý & Tài Nguyên (地理与资源)

Trụ sở của Hội nằm tại khu chợ dược liệu lớn nhất Trạm Biên Nam Cương, gồm hơn 30 quầy hàng gỗ xếp dọc con đường chính. Khu chợ ngoài trời được che bằng mái lá dừa, tạo bóng mát cho cả người mua lẫn dược liệu nhạy cảm với ánh nắng. Phía sau khu chợ là kho bảo quản dược liệu xây bằng đá lạnh — loại đá khoáng đặc biệt của vùng Nam Cương có khả năng duy trì nhiệt độ thấp tự nhiên, giúp bảo quản dược liệu tươi lâu hơn gấp nhiều lần. Tài nguyên chính của Hội bao gồm mạng lưới thu mua dược liệu rộng khắp vùng rìa Nam Cương, kỹ thuật bào chế đan dược cấp thấp (Luyện Khí Đan, Trúc Cơ Đan phẩm chất trung bình), và quan hệ thương mại ổn định với Dược Vương Cốc — nguồn cung cấp đan dược thành phẩm chất lượng cao để bán lẻ.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)

Nguyên tắc tối cao của Hội là "không bán thuốc giả, không trộn độc vào thuốc" — bất kỳ ai vi phạm sẽ bị khai trừ và thông báo cho toàn Trạm Biên. Sự nghiêm khắc này xuất phát từ kinh nghiệm đau thương: chồng của Hội Trưởng Lâm Dược Nương từng chết vì trúng độc khi hái dược liệu, có thể do dược liệu giả trộn lẫn gây nhầm lẫn. Văn hóa Hội đề cao tính thực dụng và trung lập — dược sư phục vụ mọi khách hàng, không phân biệt chính tà, miễn là trả tiền và không gây rối tại khu chợ. Mỗi mùa xuân, Hội tổ chức Dược Hội — hội chợ dược liệu kéo dài ba ngày, thu hút tán tu từ khắp nơi đến mua bán, trao đổi kiến thức bào chế, và thậm chí cả đấu giá dược liệu hiếm. Đây là sự kiện được chờ đợi nhất năm tại Trạm Biên.

## IV. Cơ Cấu Tổ Chức (组织结构)

Hội có cơ cấu đơn giản nhưng rõ ràng. Đứng đầu là Hội Trưởng Lâm Dược Nương — nữ dược sư trung niên, ôn hòa trong giao tiếp nhưng cứng rắn trong chuyện buôn bán và tiêu chuẩn chất lượng. Phó Hội Trưởng Tôn Bách Dược là lão dược sư kỳ cựu, nắm giữ nhiều bí phương gia truyền và là người có kiến thức sâu rộng nhất về dược liệu Nam Cương. Dưới hai người là 15 dược sư chính thức ở trình độ Luyện Khí Hậu Kỳ đến Trúc Cơ Sơ Kỳ, mỗi người sở hữu và vận hành một quầy hàng riêng trong khu chợ. Tầng thấp nhất là 40 học đồ — phàm nhân và tu sĩ Luyện Khí Sơ Kỳ — phụ việc bào chế, bán hàng, và thu mua dược liệu tại các vùng xa.

## V. Công Pháp & Trận Pháp (功法与阵法)

Nam Cương Dược Sư Hội không có công pháp chiến đấu. Kỹ thuật tu luyện duy nhất là "Dược Hỏa Khống Chế Thuật" — phương pháp kiểm soát ngọn lửa khi luyện đan, cho phép dược sư điều chỉnh nhiệt độ chính xác đến từng mức nhỏ nhất. Thuật này hoàn toàn không có tác dụng chiến đấu, nhưng là nền tảng để bào chế đan dược chất lượng ổn định. Ngoài ra, một số dược sư thâm niên nắm vững "Dược Lý Cảm Ứng" — khả năng dùng linh lực để phân tích thành phần dược liệu bằng cách chạm tay, phát hiện tạp chất hoặc thuốc giả ngay lập tức. Hội không có trận pháp phòng thủ, phải dựa vào sự bảo hộ của Dược Vương Cốc khi gặp mối đe dọa vũ lực.

## VI. Đặc Sản Môn Phái (门派特产)

- **Luyện Khí Đan (Phẩm Chất Trung Bình):** Đan dược cơ bản hỗ trợ tu sĩ Luyện Khí kỳ hồi phục và tích lũy linh lực. Chất lượng không bằng sản phẩm của Dược Vương Cốc nhưng giá rẻ hơn nhiều, phù hợp với tán tu nghèo.
- **Trúc Cơ Đan (Phẩm Chất Kém):** Đan dược hỗ trợ đột phá Trúc Cơ, tỷ lệ thành công thấp nhưng vẫn tốt hơn không có. Sản phẩm "giá rẻ" bán chạy nhất Hội.
- **Dược Liệu Nam Cương:** Các loại dược liệu đặc hữu vùng biên giới phía nam, bao gồm Hỏa Trùng Thảo, Nam Sương Hoa, và Độc Khí Nhựa — nguyên liệu quý cho nhiều bài thuốc giải độc.
- **Dịch Vụ Chữa Trị:** Dược sư Hội cung cấp dịch vụ chữa thương tại chỗ cho tán tu và thương nhân qua đường, từ vết thương ngoài da đến trúng độc cấp thấp.

## VII. Cơ Sở Hạ Tầng (基础设施)

- **Khu Chợ Dược Liệu:** Hơn 30 quầy hàng gỗ dọc đường chính Trạm Biên, mỗi quầy do một dược sư chính thức vận hành, bày bán đủ loại dược liệu và đan dược.
- **Kho Bảo Quản Đá Lạnh:** Kho ngầm xây bằng đá lạnh tự nhiên, duy trì nhiệt độ thấp để bảo quản dược liệu nhạy cảm. Đây là tài sản giá trị nhất của Hội.
- **Phòng Luyện Đan Chung:** Hai phòng luyện đan nhỏ phía sau khu chợ, trang bị lò luyện cấp thấp, dùng chung cho các dược sư và học đồ.
- **Lều Y Liệu:** Lều lớn ở đầu khu chợ, nơi dược sư luân phiên trực để chữa trị khẩn cấp cho khách qua đường.

## VIII. Kinh Tế (经济)

Kinh tế của Hội xoay quanh ba trụ cột: thu mua dược liệu thô từ vùng rìa Nam Cương, bào chế đan dược cấp thấp tại chỗ, và bán lẻ đan dược thành phẩm chất lượng cao nhập từ Dược Vương Cốc. Mô hình này đảm bảo nguồn thu ổn định nhưng cũng tạo ra sự phụ thuộc đáng kể vào Dược Vương Cốc — Hội phải bán dược liệu thô giá rẻ cho Cốc để đổi lấy sự bảo hộ khỏi cướp bóc. Dược Hội mùa xuân là nguồn thu lớn nhất trong năm, khi lượng giao dịch tăng gấp mười lần ngày thường. Hoang Dã Thợ Săn Bang là nhóm khách hàng trung thành — họ mua thuốc trị thương trước khi lên đường và mang dược liệu hiếm từ vùng hoang dã về bán lại cho Hội.

## IX. Lịch Sử Tóm Tắt (简史)

Hội thành lập hơn 80 năm trước bởi một nhóm dược sư lang thang muốn tạo ra tiêu chuẩn chung cho dược liệu Nam Cương. Trước đó, thị trường dược liệu vùng biên hỗn loạn — thuốc giả tràn lan, giá cả biến động thất thường, và dược sư bị thương nhân bất lương lừa đảo. Nhóm sáng lập đề ra quy tắc "không thuốc giả, không trộn độc", dần thu hút thêm dược sư uy tín gia nhập. Trong 80 năm hoạt động, Hội đã hai lần bị Hắc Báo Trại cướp sạch kho hàng, buộc phải cầu viện Dược Vương Cốc bảo hộ với cái giá là phải bán dược liệu giá rẻ cho Cốc. Dưới sự điều hành của Lâm Dược Nương — người kế nhiệm vị trí Hội Trưởng 20 năm trước — Dược Hội mùa xuân ngày càng phát triển, trở thành sự kiện quan trọng nhất Trạm Biên và đưa uy tín Hội lên tầm cao mới.

## X. Giai Thoại & Bí Mật (轶事与秘密)

Phó Hội Trưởng Tôn Bách Dược thực ra sở hữu một bí phương luyện "Tẩy Tủy Đan" — loại đan dược cực kỳ quý hiếm có khả năng cải thiện linh căn cấp thấp, giúp tu sĩ đột phá giới hạn tư chất bẩm sinh. Lão giấu kín bí phương này suốt đời vì hiểu rằng nếu lộ ra, cường giả từ khắp Đông Hoang sẽ kéo đến cướp đoạt, và Hội nhỏ bé không thể chống đỡ. Bên cạnh đó, ít ai biết rằng Hội bí mật ghi chép lại mọi giao dịch dược liệu khả nghi — từ ai mua số lượng lớn Huyết Linh Thảo (nguyên liệu luyện độc) đến ai thường xuyên mua Hồi Dương Đan (thường dùng sau khi tẩu hỏa nhập ma). Cơ sở dữ liệu này vô tình trở thành công cụ theo dõi hoạt động tà đạo qua mô hình tiêu thụ nguyên liệu, nhưng Hội chưa biết cách khai thác triệt để giá trị tình báo này.

## XI. Quan Hệ Thế Lực (势力关系)

Dược Vương Cốc là đối tác thương mại quan trọng nhất và cũng là người bảo hộ của Hội. Mối quan hệ này mang tính phụ thuộc rõ rệt — Hội phải bán dược liệu giá rẻ và ưu tiên cung cấp nguyên liệu quý cho Cốc để đổi lấy sự bảo vệ khỏi cướp bóc vùng biên. Hoang Dã Thợ Săn Bang là nhóm khách hàng và đối tác cung ứng trung thành, mang lại nguồn dược liệu hiếm từ vùng hoang dã. Huyết Thảo Đường là đối thủ cạnh tranh tiềm ẩn trong lĩnh vực dược liệu, nhưng do Huyết Thảo Đường chuyên về dược liệu tà thuật nên hai bên ít chồng chéo thị trường. Hội duy trì thái độ trung lập với hầu hết các thế lực — kinh doanh không phân biệt chính tà, nhưng cũng âm thầm cảnh giác trước những khách hàng đáng ngờ.

Gần đây, Hội phát hiện một xu hướng đáng lo: lượng mua Huyết Linh Thảo tăng gấp ba lần trong năm qua, phần lớn từ những người mua giấu mặt. Lâm Dược Nương đã ra lệnh ghi chép kỹ hơn và thông báo cho Thanh Vân Nghĩa Đoàn, nhưng chưa dám hành động công khai vì sợ mất khách hàng và gây thù oán với kẻ mạnh hơn.


