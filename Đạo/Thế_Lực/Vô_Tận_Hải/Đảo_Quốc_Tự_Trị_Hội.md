---
type: faction
name: Đảo Quốc Tự Trị Hội
hantu: 岛国自治会
faction_type: Hội
alignment: 3
race: Nhân Tộc
region: Vô Tận Hải
founded: Một trăm năm trước
founder: Phạm Dân Chủ
emblem: Dao_Quoc_Tu_Tri.png
specialty: Bầu cử dân chủ, Tự trị cộng đồng, Nông ngư kết hợp
economy:
- Đánh bắt hải sản ven đảo
- Trồng trọt lúa linh phẩm chất thấp
- Khai thác linh thạch mỏ nhỏ (gần cạn kiệt)
arcs:
  - arc: 1
    status: Tự trị ổn định
    rank: Hạng Năm
    leader: Hội Trưởng Phạm Dân Chủ
    population: 300
    territory:
      - Quần đảo Bình An (năm hòn đảo nhỏ, ven bờ tây Vô Tận Hải)
    assets:
      - name: Ngũ Đảo Liên Hoàn Trận
        type: Trận Pháp
      - name: Bia Khắc Cổ Tự (dưới lòng đảo)
        type: Bí Cảnh
    stats: [20, 30, 15, 300, 25, 10]
    divisions:
      - name: Hội Đồng Dân Cử
        role: Cơ quan lập pháp và giám sát Hội Trưởng, đại diện cho năm đảo
        headcount:
          hoi_truong: 1
          pho_hoi_truong: 1
          thanh_vien: 15
          tong_quan: 0
        members:
          - character: Phạm Dân Chủ
            position: Hội Trưởng
            cultivation: Trúc Cơ Viên Mãn
          - character: "[Phó Hội Trưởng]"
            position: Phó Hội Trưởng
            cultivation: Trúc Cơ Sơ Kỳ
            placeholder: true
      - name: Dân Binh Đội
        role: Lực lượng phòng thủ và tuần tra ven đảo
        headcount:
          hoi_truong: 0
          pho_hoi_truong: 0
          thanh_vien: 20
          tong_quan: 1
        members:
          - character: "[Dân Binh Đội Trưởng]"
            position: Đội Trưởng
            cultivation: Luyện Khí Viên Mãn
            placeholder: true
    relationships:
      - faction: Phiêu Lưu Đảo Liên Minh
        description: Đồng minh thân cận, hai bên hỗ trợ lẫn nhau khi bị hải tặc tấn công. Thường xuyên trao đổi lương thực và tin tức.
        diplomacy:
          lien_minh: 70
          tin: 75
          uy_hiep: 0
          thuong_mai: 60
          on_oan: 10
          le_thuoc: 0
      - faction: Hắc Hải Hải Tặc
        description: Từng bị hải tặc nhỏ cướp phá nhiều lần, quan hệ thù địch nhưng quá yếu để trả thù.
        diplomacy:
          lien_minh: -80
          tin: -90
          uy_hiep: 60
          thuong_mai: -100
          on_oan: -70
          le_thuoc: 0
      - faction: Ngư Dân Tu Luyện Hội
        description: Trao đổi kinh nghiệm đánh bắt và kỹ thuật trồng trọt ven biển, quan hệ bình đẳng giữa hai tổ chức nhỏ.
        diplomacy:
          lien_minh: 40
          tin: 50
          uy_hiep: 0
          thuong_mai: 55
          on_oan: 0
          le_thuoc: 0
---

# ĐẢO QUỐC TỰ TRỊ HỘI (岛国自治会)

## I. Tổng Quan (总览)
Đảo Quốc Tự Trị Hội là một tổ chức tự trị nhỏ bé nằm trên quần đảo Bình An, ven bờ tây Vô Tận Hải. Với dân số chỉ khoảng ba trăm người, đây là một trong những thế lực nhỏ nhất vùng biển, nhưng lại sở hữu hệ thống chính trị độc đáo nhất — chế độ bầu cử dân chủ do Hội Trưởng Phạm Dân Chủ sáng lập cách đây một trăm năm. Mặc dù tự hào tuyên bố "độc lập" khỏi mọi vương triều và tông môn, thực tế không ai thèm công nhận lẫn phủ nhận quyền tự trị của họ, bởi quần đảo quá nhỏ bé và nghèo nàn để bất kỳ thế lực nào bận tâm.

## II. Địa Lý & Tài Nguyên (地理 与 资源)
Quần đảo Bình An gồm năm hòn đảo nhỏ nằm rải rác trên vùng biển nông ven bờ tây Vô Tận Hải. Mỗi đảo chỉ rộng vừa đủ cho vài chục hộ gia đình, với địa hình tương đối bằng phẳng và khí hậu ôn hòa quanh năm. Đất đai tuy hạn chế nhưng phì nhiêu cho vùng đảo, cho phép trồng được một ít lúa linh phẩm chất thấp. Nguồn cá xung quanh dồi dào, là nguồn thực phẩm chính của cư dân. Dưới lòng đảo thứ ba có một mỏ linh thạch phẩm chất thấp, nhưng sau nhiều thập kỷ khai thác đã gần cạn kiệt. Vị trí xa bờ đủ để tránh sự chú ý của các thế lực đất liền, tạo nên một vùng an toàn tương đối cho cộng đồng nhỏ bé này.

## III. Văn Hóa & Tín Ngưỡng (文化 与 信仰)
Đảo Quốc Tự Trị Hội lấy tinh thần "tự do" và "dân chủ" làm giá trị cốt lõi, tuyên bố độc lập khỏi mọi vương triều và tông môn — dù không ai thèm công nhận. Hệ thống bầu cử dân chủ là niềm tự hào lớn nhất: Hội Trưởng được bầu mỗi mười năm bởi tất cả cư dân trưởng thành, bất kể tu vi hay giới tính. Mỗi kỳ bầu cử là dịp lễ hội lớn nhất đảo, khi cả năm hòn đảo tranh luận ồn ào suốt một tháng trước ngày bỏ phiếu. Cư dân tuy đa phần là phàm nhân và tu sĩ cấp thấp, nhưng mang theo lòng tự trọng kỳ lạ về quyền tự quyết. Họ tin rằng "dù nhỏ bé, vẫn có quyền tự định đoạt vận mệnh" — một triết lý khiến các tu sĩ mạnh hơn đi ngang qua thường mỉm cười hoặc cười nhạo.

## IV. Cơ Cấu Tổ Chức (组织结构)
Hội Trưởng là người đứng đầu, được bầu bởi toàn dân mỗi mười năm, nhưng quyền hạn bị giới hạn bởi Hội Đồng Dân Cử gồm mười lăm đại diện cho năm đảo, mỗi đảo ba người. Hội Đồng có quyền phủ quyết các quyết định lớn của Hội Trưởng, tạo nên cơ chế kiểm soát quyền lực hiếm thấy trong thế giới tu luyện. Lực lượng vũ trang chỉ gồm hai mươi Dân Binh trang bị vũ khí thô sơ, đa phần là phàm nhân hoặc tu sĩ Luyện Khí, đủ để xua đuổi thú biển nhỏ nhưng hoàn toàn bất lực trước bất kỳ tu sĩ nào từ Kim Đan trở lên. Phạm Dân Chủ ở cảnh giới Trúc Cơ Viên Mãn là tu sĩ mạnh nhất trên đảo, và ông đã giữ chức Hội Trưởng liên tục qua nhiều kỳ bầu cử — không phải vì gian lận, mà vì không ai đủ năng lực thay thế.

## V. Công Pháp & Trận Pháp (功法 与 阵法)
Đảo Quốc Tự Trị Hội không có công pháp riêng. Phạm Dân Chủ tu luyện tạp công mua được từ thương nhân đi ngang, chắp vá từ nhiều nguồn khác nhau nên tu vi tuy đạt Trúc Cơ Viên Mãn nhưng nền tảng không vững, khó có thể đột phá Kim Đan. Trận pháp duy nhất đáng kể là Ngũ Đảo Liên Hoàn Trận, một hệ thống trận pháp cảnh báo kết nối năm hòn đảo. Khi có kẻ xâm nhập, trận pháp sẽ phát ra tiếng chuông cảnh báo trên tất cả các đảo. Tuy nhiên, năng lượng duy trì trận pháp ngày càng yếu do mỏ linh thạch cạn kiệt, và không ai trên đảo đủ trình độ để sửa chữa hay nâng cấp.

## VI. Đặc Sản Môn Phái (门派特产)
Dù không phải tông môn hay thương hội, Đảo Quốc Tự Trị Hội vẫn có một số sản phẩm đặc trưng. Lúa linh phẩm chất thấp trồng trên đảo tuy không quý giá nhưng có hương vị đặc biệt nhờ khí hậu biển, được ngư dân vùng lân cận ưa chuộng. Muối biển tinh luyện từ nước biển quanh đảo chứa một lượng nhỏ linh khí, dùng ướp hải sản giúp bảo quản lâu hơn. Ngoài ra, cư dân còn sản xuất rượu tảo biển lên men — thứ đồ uống mà thương nhân đi ngang đôi khi mua vui vì tò mò, nhưng chất lượng thực ra cũng tạm được.

## VII. Cơ Sở Hạ Tầng (基础设施)
Cơ sở hạ tầng của quần đảo đơn sơ nhưng đầy đủ cho cuộc sống tự cung tự cấp. Nhà ở xây bằng đá san hô và gỗ trôi dạt, chắc chắn trước gió biển. Trung tâm đảo Bình An có Hội Trường — một tòa nhà đá lớn nhất, nơi diễn ra bầu cử và họp Hội Đồng Dân Cử. Bến thuyền chung phục vụ cả năm đảo, với khoảng mười chiếc thuyền nhỏ dùng đánh cá và vận chuyển giữa các đảo. Hệ thống hứng nước mưa và giếng nước ngọt phân bố trên mỗi đảo, đảm bảo nhu cầu sinh hoạt tối thiểu.

## VIII. Kinh Tế (经济)
Kinh tế Đảo Quốc Tự Trị Hội hoàn toàn dựa trên tự cung tự cấp và trao đổi nhỏ lẻ. Nguồn thu chính đến từ đánh bắt hải sản ven đảo, một phần được đem trao đổi với thương nhân đi ngang để lấy vật tư cần thiết. Lúa linh và muối biển tinh luyện là hai mặt hàng trao đổi chủ lực. Mỏ linh thạch gần cạn kiệt khiến nguồn cung cấp năng lượng cho trận pháp ngày càng thiếu hụt, và đảo không có đủ tài nguyên để mua linh thạch từ bên ngoài. Nhìn chung, kinh tế chỉ đủ duy trì cuộc sống ổn định ở mức tối thiểu, không có tích lũy đáng kể.

## IX. Lịch Sử Tóm Tắt (简史)
Quần đảo Bình An ban đầu chỉ là nơi trú ẩn của một nhóm nông dân chạy nạn chiến tranh trên đất liền. Họ ra đảo sinh sống, dần dần hình thành cộng đồng nhỏ tự cung tự cấp. Một trăm năm trước, Phạm Dân Chủ — khi đó còn trẻ và đầy nhiệt huyết — đề xuất hệ thống tự trị dân chủ, được toàn dân ủng hộ. Từ đó, cứ mười năm một lần, cả đảo lại tổ chức bầu cử long trọng. Trong lịch sử, quần đảo từng bị hải tặc nhỏ cướp phá nhiều lần, phải nhờ Phiêu Lưu Đảo Liên Minh hỗ trợ đẩy lùi. Cư dân tự hào về lịch sử "không ai cai trị" của mình — dù trên thực tế, chưa bao giờ có thế lực nào thèm cai trị họ cả.

## X. Giai Thoại & Bí Mật (轶事 与 秘密)
Phạm Dân Chủ thực ra là con trai thứ của một quan lại nhỏ trên đất liền, bỏ trốn ra đảo vì bất mãn sâu sắc với chế độ quân chủ chuyên quyền. Ông giấu kín thân thế suốt trăm năm, chỉ tự nhận là "nông dân phiêu bạt." Dưới một trong năm hòn đảo có một động đá tự nhiên chứa bia khắc cổ tự — không ai trên đảo đọc được, nhưng nhiều người cảm nhận rõ ràng linh lực rò rỉ từ đó. Có thể đây là di tích của một thế lực cổ đại đã tuyệt diệt, và nếu được giải mã, giá trị có thể vượt xa mọi tài sản hiện có của đảo. Hệ thống bầu cử đặc biệt này từng khiến một tu sĩ Kim Đan đi ngang cười nhạo rằng: "Phàm nhân bầu ai làm chủ cũng vô nghĩa nếu một tu sĩ Kim Đan muốn chiếm đảo." Câu nói ấy ám ảnh Phạm Dân Chủ suốt nhiều năm, trở thành nỗi lo lớn nhất của ông về tương lai quần đảo.

## XI. Quan Hệ Thế Lực (势力关系)
Đảo Quốc Tự Trị Hội duy trì quan hệ thân thiết nhất với Phiêu Lưu Đảo Liên Minh — hai tổ chức nhỏ bé cùng cảnh ngộ, thường xuyên hỗ trợ lẫn nhau khi bị hải tặc quấy phá. Với Ngư Dân Tu Luyện Hội, hai bên trao đổi kinh nghiệm đánh bắt và kỹ thuật trồng trọt trên tinh thần bình đẳng. Mối đe dọa lớn nhất đến từ Hắc Hải Hải Tặc — những kẻ đã nhiều lần cướp phá quần đảo trong quá khứ, khiến cư dân sống trong nỗi sợ hãi thường trực. Đối với các thế lực lớn như Hải Thần Cung hay Long Cung, Đảo Quốc Tự Trị Hội đơn giản là quá nhỏ bé để được chú ý, và đó lại chính là lợi thế lớn nhất của họ.
