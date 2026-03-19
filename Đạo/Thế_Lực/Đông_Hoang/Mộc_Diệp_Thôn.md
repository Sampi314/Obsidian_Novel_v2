---
type: faction
name: Mộc Diệp Thôn
hantu: 木叶村
faction_type: Bộ Lạc
alignment: 3
race: Nhân Tộc
region: Đông Hoang
founded: 200 năm trước
founder: Mộc Thanh Phong
emblem: Moc_Diep_Thon.png
specialty: Mộc hệ dưỡng sinh, Trồng trọt linh thảo, Ẩn tu tự cung tự cấp
economy:
- Trồng dược thảo cấp thấp tự tiêu dùng
- Khai thác gỗ linh mộc nhỏ lẻ
- Trao đổi lương thực nội bộ
arcs:
  - arc: 1
    status: Ẩn cư ổn định
    rank: Hạng Năm
    leader: Trưởng Lão Mộc Thanh Phong
    population: 150
    territory:
      - Thung lũng kín phía tây Đông Hoang
      - Rừng cổ thụ bao quanh thung lũng
    assets:
      - name: Long mạch nhỏ dưới thung lũng
        type: Tài Nguyên
      - name: Trận pháp che giấu cấp thấp
        type: Trận Pháp
      - name: Vườn dược thảo cộng đồng
        type: Công Trình
    stats: [30, 80, 10, 150, 90, 15]
    divisions:
      - name: Hội Đồng Trưởng Lão
        role: Quyết định mọi việc lớn nhỏ trong Thôn thông qua bỏ phiếu
        headcount:
          truong_lao: 6
          chien_binh: 15
          dan_thuong: 129
        members:
          - character: Mộc Thanh Phong
            position: Trưởng Lão
            cultivation: Kim Đan Trung Kỳ
          - character: "[Trưởng Lão Nhị]"
            position: Trưởng Lão
            cultivation: Trúc Cơ Hậu Kỳ
            placeholder: true
          - character: "[Trưởng Lão Tam]"
            position: Trưởng Lão
            cultivation: Trúc Cơ Trung Kỳ
            placeholder: true
    relationships:
      - faction: Dược Vương Cốc
        description: Không có liên hệ chính thức, nhưng đôi khi tán tu mang dược thảo từ Thôn ra bán cho Cốc mà Thôn không hay biết.
        diplomacy:
          lien_minh: 0
          tin: 5
          uy_hiep: 0
          thuong_mai: 10
          on_oan: 0
          le_thuoc: 0
      - faction: Cửu Hoa Kiếm Tông
        description: Không qua lại, nhưng Thôn luôn lo sợ nếu bị phát hiện sẽ bị tông phái lớn nhòm ngó long mạch.
        diplomacy:
          lien_minh: 0
          tin: 0
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 0
      - faction: Mật Lâm Thợ Săn Hội
        description: Thợ săn đôi khi đi lạc gần thung lũng nhưng bị trận pháp đánh lạc hướng, chưa phát hiện Thôn.
        diplomacy:
          lien_minh: 0
          tin: 0
          uy_hiep: 5
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 0
---

# Mộc Diệp Thôn (木叶村)

## I. Tổng Quan (总览)
Mộc Diệp Thôn là một cộng đồng ẩn cư nhỏ bé nằm sâu trong thung lũng kín phía tây Đông Hoang, được bao bọc bởi rừng cổ thụ ngàn năm. Thôn do Mộc Thanh Phong — một tu sĩ mộc hệ Kim Đan — sáng lập cách đây 200 năm khi ông chọn rời bỏ thế giới tu luyện đầy tranh đoạt. Với triết lý "sống thuận theo tự nhiên, không tranh đoạt với đời", Mộc Diệp Thôn là nơi cư ngụ của những tán tu chán nản chiến tranh, phàm nhân tìm kiếm bình yên, và các gia đình hỗn hợp tu sĩ - phàm nhân. Dù quy mô nhỏ và gần như vô danh trên bản đồ thế lực Đông Hoang, bí mật ẩn giấu bên dưới thung lũng khiến Thôn tiềm ẩn giá trị vượt xa vẻ ngoài khiêm tốn của nó.

## II. Địa Lý & Tài Nguyên (地理与资源)
Thung lũng nơi Mộc Diệp Thôn tọa lạc được che chắn bởi dãy núi thấp bốn phía và lớp rừng cổ thụ dày đặc bên ngoài. Lối vào duy nhất là một khe núi hẹp bị rễ cây và dây leo phủ kín, rất khó phát hiện nếu không có người dẫn đường. Bên trong thung lũng, địa hình bằng phẳng với đất phì nhiêu, suối nước trong chảy từ khe đá, và khí hậu ôn hòa quanh năm nhờ địa thế che chắn gió lạnh từ phía bắc. Tài nguyên chính là dược thảo trồng tại vườn cộng đồng, lương thực tự cung tự cấp từ ruộng linh điền, và một lượng nhỏ gỗ linh mộc cấp thấp từ rừng xung quanh. Đặc biệt, bên dưới thung lũng ẩn chứa một long mạch nhỏ — nguồn linh khí âm thầm nuôi dưỡng đất đai và cây cối, khiến mọi thứ ở đây tươi tốt bất thường.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
Cư dân Mộc Diệp Thôn sống theo nguyên tắc giản dị và hòa hợp với thiên nhiên. Mọi tranh chấp nội bộ được giải quyết thông qua bỏ phiếu tại Hội Đồng Trưởng Lão, không ai được dùng vũ lực. Quy tắc nghiêm ngặt nhất là cấm tiết lộ vị trí Thôn cho người ngoài — bất kỳ ai vi phạm sẽ bị trục xuất vĩnh viễn. Vũ khí không được mang vào khu dân cư, chỉ được cất giữ tại nhà kho chung ở rìa Thôn. Mỗi mùa thu, toàn thể dân làng tổ chức Lễ Tạ Thụ — buổi lễ tạ ơn rừng cổ thụ đã che chở cộng đồng, trong đó mỗi gia đình trồng thêm một cây non và cầu nguyện cho sự bình yên tiếp tục. Đây là nghi thức mang tính tâm linh sâu sắc, thể hiện lòng biết ơn đối với thiên nhiên thay vì thần linh hay tổ sư.

## IV. Cơ Cấu Tổ Chức (组织结构)
Mộc Diệp Thôn không có hệ thống tôn ti phức tạp. Trưởng Lão Mộc Thanh Phong giữ vai trò lãnh đạo tinh thần và là người có tu vi cao nhất, nhưng quyền hành thực tế được chia sẻ đều cho Hội Đồng gồm 5 vị Trúc Cơ kỳ cựu cùng ông. Mọi quyết định lớn — từ phân chia đất canh tác đến tiếp nhận cư dân mới — đều phải qua bỏ phiếu đa số. Dân cư khoảng 150 người, bao gồm tu sĩ cấp thấp (Luyện Khí đến Trúc Cơ), phàm nhân, và gia đình hỗn hợp. Một đội tuần tra nhỏ gồm 15 tu sĩ Luyện Khí luân phiên canh gác rìa thung lũng, nhưng nhiệm vụ chính của họ là duy trì trận pháp che giấu chứ không phải chiến đấu.

## V. Công Pháp & Trận Pháp (功法与阵法)
Mộc Diệp Thôn không có công pháp chiến đấu. Dân làng tu luyện các loại công pháp mộc hệ nhẹ nhàng, tập trung vào việc trồng trọt, dưỡng sinh và cảm ứng linh khí tự nhiên. Phương pháp tu luyện chính là "Mộc Diệp Sinh Cơ Công" — một bộ công pháp cấp thấp giúp tăng cường sinh lực, kéo dài tuổi thọ và thúc đẩy cây cối phát triển. Về trận pháp, xung quanh thung lũng được bố trí một lớp trận pháp che giấu cấp thấp do Mộc Thanh Phong đích thân thiết lập. Trận pháp này không có sát thương mà hoạt động bằng cách gây nhiễu loạn phương hướng — bất kỳ ai đi vào vùng ảnh hưởng sẽ vô thức đi lòng vòng rồi quay ra mà không biết đã bỏ lỡ lối vào. Chỉ người mang "Mộc Diệp Lệnh" — một chiếc lá cây đặc biệt do Trưởng Lão ban — mới không bị ảnh hưởng.

## VI. Đặc Sản Môn Phái (门派特产)
- **Mộc Diệp Linh Trà:** Trà pha từ lá cây cổ thụ bao quanh thung lũng, có tác dụng thanh tâm tĩnh thần và tăng tốc hồi phục linh lực nhẹ. Hương vị thanh ngọt đặc trưng, chỉ có thể trồng tại vùng đất được long mạch nuôi dưỡng.
- **Dược Thảo Cấp Thấp:** Các loại linh thảo phổ thông như Thanh Linh Thảo, Dưỡng Khí Hoa được trồng trong vườn cộng đồng, chất lượng cao hơn bình thường nhờ đất đai phì nhiêu.
- **Gỗ Linh Mộc Thôn:** Gỗ từ cành cây rụng tự nhiên, được thu gom và sử dụng làm công cụ canh tác hoặc đồ gia dụng, có chứa một lượng nhỏ linh khí.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Quảng Trường Cổ Thụ:** Trung tâm Thôn, nơi cây cổ thụ lớn nhất mọc — dân làng họp mặt và tổ chức Lễ Tạ Thụ tại đây.
- **Vườn Dược Thảo Cộng Đồng:** Khu vườn được chia thành lô cho mỗi gia đình, trồng dược thảo và lương thực, tưới bằng nước suối tự nhiên.
- **Nhà Kho Chung:** Nơi cất giữ lương thực dự trữ, vũ khí, và vật tư của toàn Thôn.
- **Trạm Tuần Tra:** Bốn trạm nhỏ ở bốn hướng rìa thung lũng, nơi đội tuần tra luân phiên kiểm tra trận pháp che giấu.

## VIII. Kinh Tế (经济)
Kinh tế Mộc Diệp Thôn hoàn toàn dựa trên tự cung tự cấp. Dân làng trồng lương thực và dược thảo trên linh điền được long mạch ngầm nuôi dưỡng, thu hoạch gỗ linh mộc từ cành rụng tự nhiên, và đánh bắt cá suối. Không có hoạt động thương mại với bên ngoài — đây vừa là nguyên tắc sống vừa là biện pháp bảo vệ bí mật vị trí. Thỉnh thoảng, một vài tán tu có nhu cầu đặc biệt sẽ bí mật rời Thôn để mua nhu yếu phẩm ở thị trấn xa, nhưng họ không bao giờ tiết lộ mình đến từ đâu. Mức sống trong Thôn giản dị nhưng đủ đầy, không ai thiếu ăn nhờ đất đai màu mỡ.

## IX. Lịch Sử Tóm Tắt (简史)
Hai trăm năm trước, Mộc Thanh Phong — khi ấy là một tu sĩ mộc hệ Kim Đan — lui về thung lũng này sau khi thất bại đột phá Nguyên Anh. Ban đầu ông chỉ một mình ẩn cư, tìm kiếm sự thanh tĩnh để tĩnh tâm tu dưỡng. Dần dần, những tán tu chán nản với cuộc sống tranh đoạt bên ngoài tìm đến xin ở. Mộc Thanh Phong không từ chối, chỉ yêu cầu họ giữ bí mật và sống hòa thuận. Thôn từ một túp lều phát triển thành cộng đồng nhỏ với vài chục hộ, rồi dần ổn định ở mức 150 người. Trong suốt 200 năm, Thôn chưa từng bị phát hiện bởi bất kỳ thế lực nào bên ngoài nhờ trận pháp che giấu và vị trí địa lý hiểm trở.

## X. Giai Thoại & Bí Mật (轶事与秘密)
Mộc Thanh Phong thất bại đột phá Nguyên Anh không phải vì thiếu tài năng hay tài nguyên. Theo lời đồn thầm trong Hội Đồng Trưởng Lão, ông cố tình dừng lại giữa chừng — lý do thực sự chỉ mình ông biết. Một số người đoán rằng ông nhìn thấy điều gì đó trong quá trình đột phá khiến ông chọn từ bỏ sức mạnh để giữ lại thứ quan trọng hơn. Bí mật lớn nhất của Thôn nằm ngay dưới chân: một long mạch nhỏ chạy xuyên qua lòng đất thung lũng, là nguồn cội khiến đất đai phì nhiêu và linh khí dồi dào bất thường. Nếu tin tức về long mạch này lọt ra ngoài, các tông phái lớn như Cửu Hoa Kiếm Tông hay Thanh Đế Cung chắc chắn sẽ nhòm ngó, và cộng đồng nhỏ bé này không có khả năng chống cự.

## XI. Quan Hệ Thế Lực (势力关系)
Mộc Diệp Thôn gần như không có quan hệ với bất kỳ thế lực nào — đây là chủ đích chứ không phải sự cô lập bất đắc dĩ. Thôn tồn tại trong trạng thái "vô hình" trên bản đồ quyền lực Đông Hoang. Dược Vương Cốc đôi khi nhận được dược thảo chất lượng cao từ các tán tu không rõ xuất xứ — trên thực tế là từ Thôn, nhưng không bên nào biết mối liên hệ gián tiếp này. Mật Lâm Thợ Săn Hội thỉnh thoảng có thợ săn đi lạc gần thung lũng, nhưng trận pháp che giấu luôn đánh lạc hướng họ thành công. Mối đe dọa lớn nhất không đến từ kẻ thù mà từ khả năng bí mật long mạch bị vô tình tiết lộ.
