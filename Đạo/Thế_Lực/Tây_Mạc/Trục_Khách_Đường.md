---
type: faction
name: Trục Khách Đường
hantu: 逐客堂
faction_type: Tông Môn
alignment: -2
race: Nhân Tộc
region: Tây Mạc
founded: 80 năm trước
founder: Đoạn Kiếm Sinh
emblem: Thanh_Kiem_Gay.png
specialty: Trục Khách Bách Kiếm Quyết, Thu nhận kiếm tu bị trục xuất, Dung hợp kiếm pháp đa tông phái
economy:
- Nhận hợp đồng hộ tống và bảo vệ từ thương đoàn nhỏ
- Đệ tử bán phế kiếm và vật liệu thu lượm từ phế tích
- Nhận thù lao từ các nhiệm vụ truy sát yêu thú
arcs:
  - arc: 1
    status: Đang phát triển âm thầm
    rank: Hạng Tư
    leader: Đường Chủ Đoạn Kiếm Sinh
    population: 200
    territory:
      - Phế tích cổ giữa ranh giới Đông Hoang và Tây Mạc
    assets:
      - name: Phế tích cổ (tàn tích tông phái đã diệt vong)
        type: Công Trình
      - name: Bộ sưu tập bí kíp kiếm pháp tàn khuyết
        type: Bí Kíp
      - name: Thanh kiếm cổ Cửu Hoa (ẩn giấu)
        type: Pháp Bảo
    stats: [400, 200, 300, 200, 250, 180]
    divisions:
      - name: Ban Giáo Tập
        role: Giảng dạy kiếm pháp tổng hợp và hướng dẫn đệ tử dung hợp sở học
        headcount:
          hoi_truong: 1
          pho_hoi_truong: 3
          thanh_vien: 0
          tong_quan: 0
        members:
          - character: Đoạn Kiếm Sinh
            position: Đường Chủ
            cultivation: Nguyên Anh Sơ Kỳ
          - character: "[Giáo Tập Giáp]"
            position: Giáo Tập
            cultivation: Kim Đan
            placeholder: true
          - character: "[Giáo Tập Ất]"
            position: Giáo Tập
            cultivation: Kim Đan
            placeholder: true
          - character: "[Giáo Tập Bính]"
            position: Giáo Tập
            cultivation: Kim Đan
            placeholder: true
      - name: Đệ Tử Đường
        role: Tu luyện kiếm pháp mới và thực hiện nhiệm vụ bên ngoài
        headcount:
          hoi_truong: 0
          pho_hoi_truong: 0
          thanh_vien: 40
          tong_quan: 3
        members:
          - character: "[Đệ Tử Trúc Cơ]"
            position: Đệ Tử
            cultivation: Trúc Cơ
            placeholder: true
      - name: Ngoại Môn Đệ Tử
        role: Mới gia nhập, đang trong giai đoạn thử thách và đoạn tuyệt quá khứ
        headcount:
          hoi_truong: 0
          pho_hoi_truong: 0
          thanh_vien: 150
          tong_quan: 5
        members:
          - character: "[Ngoại Môn Đệ Tử]"
            position: Ngoại Môn
            cultivation: Luyện Khí - Trúc Cơ Sơ Kỳ
            placeholder: true
    relationships:
      - faction: Cửu Hoa Kiếm Tông
        description: Mối quan hệ phức tạp và nguy hiểm. Đoạn Kiếm Sinh bị Cửu Hoa trục xuất, Cửu Hoa biết Trục Khách Đường tồn tại nhưng chưa ra tay vì chưa chạm đến lợi ích cốt lõi.
        diplomacy:
          lien_minh: -60
          tin: -50
          uy_hiep: 40
          thuong_mai: 0
          on_oan: -70
          le_thuoc: 0
      - faction: Sa Tặc Liên Minh
        description: Thường xuyên đụng độ khi đệ tử Trục Khách Đường thực hiện nhiệm vụ hộ tống trên sa mạc. Hai bên coi nhau là mối phiền hà.
        diplomacy:
          lien_minh: -30
          tin: -20
          uy_hiep: 20
          thuong_mai: 0
          on_oan: -20
          le_thuoc: 0
      - faction: Thiên Sa Thương Hội
        description: Nhận hợp đồng hộ tống từ các thương đoàn nhỏ thuộc Thương Hội. Quan hệ thuần túy thương mại, không thân thiết nhưng không thù địch.
        diplomacy:
          lien_minh: 0
          tin: 30
          uy_hiep: 0
          thuong_mai: 40
          on_oan: 0
          le_thuoc: 0
---

# Trục Khách Đường (逐客堂)

## I. Tổng Quan (总览)
Trục Khách Đường là một tông môn kiếm pháp đặc biệt nằm tại phế tích cổ giữa ranh giới Đông Hoang và Tây Mạc, chuyên thu nhận những kiếm tu bị trục xuất hoặc tự rời bỏ tông phái cũ. Dưới sự lãnh đạo của Đường Chủ Đoạn Kiếm Sinh, một Nguyên Anh Sơ Kỳ nguyên là chân truyền đệ tử Cửu Hoa Kiếm Tông bị khai trừ, Trục Khách Đường theo đuổi triết lý "Kiếm không phân tông phái, chỉ phân mạnh yếu". Với khoảng hai trăm thành viên, tông môn này thu thập và dung hợp tinh hoa kiếm pháp từ nhiều nguồn khác nhau, tạo nên một hệ thống kiếm đạo tổng hợp độc nhất vô nhị trong Cố Nguyên Giới.

## II. Địa Lý & Tài Nguyên (地理与资源)
Trụ sở đặt tại phế tích kiến trúc cổ nửa chìm trong cát, tàn tích của một tông phái đã diệt vong từ lâu, nằm ở vùng hoang vu giữa Đông Hoang và Tây Mạc. Khí hậu nơi đây khắc nghiệt, gió cát quanh năm, nhưng chính sự hẻo lánh là lá chắn bảo vệ tốt nhất cho tông môn. Phòng ốc đổ nát được tu sửa tạm bợ bằng vật liệu thu lượm, đủ để che mưa nắng nhưng không đáng gọi là kiến trúc. Tài nguyên khan hiếm, chủ yếu là phế kiếm thu lượm được từ phế tích và bí kíp kiếm pháp tàn khuyết từ nhiều tông phái khác nhau mà đệ tử mang theo khi gia nhập. Địa hình phế tích phức tạp với nhiều hành lang đổ nát và tầng hầm bí mật, tạo lợi thế phòng thủ tự nhiên.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
Triết lý cốt lõi của Trục Khách Đường là "Kiếm không phân tông phái, chỉ phân mạnh yếu", thể hiện tinh thần khai phóng và phản kháng đối với sự cứng nhắc của các tông phái truyền thống. Quy tắc quan trọng nhất: sau khi vào Đường, không được nhắc đến tông phái cũ, bỏ lại quá khứ hoàn toàn. Cấm quay lại trả thù tông phái cũ khi chưa đủ mạnh để tránh mang họa cho cả Đường. Nghi lễ gia nhập yêu cầu đệ tử mới gãy một thanh kiếm trước mặt mọi người, tượng trưng cho việc đoạn tuyệt con đường kiếm cũ và sẵn sàng tiếp nhận kiếm đạo mới. Bầu không khí trong Đường vừa nghiêm khắc vừa bình đẳng, không ai bị phán xét vì quá khứ, chỉ được đánh giá qua kiếm thuật hiện tại.

## IV. Cơ Cấu Tổ Chức (组织结构)
Đường Chủ Đoạn Kiếm Sinh nắm quyền tối cao, là người sáng tạo ra Trục Khách Bách Kiếm Quyết và trực tiếp giảng dạy đệ tử cốt cán. Ba vị Giáo Tập cảnh giới Kim Đan, mỗi người từng là đệ tử của một tông kiếm khác nhau trước khi bị trục xuất hoặc tự rời đi, phụ trách giảng dạy và hướng dẫn đệ tử dung hợp sở học cũ thành kiếm pháp mới. Bốn mươi đệ tử chính thức đa số ở cảnh giới Trúc Cơ, là những người đã hoàn thành quá trình đoạn tuyệt quá khứ và bắt đầu tu luyện kiếm pháp tổng hợp. Một trăm năm mươi ngoại môn đệ tử mới gia nhập đang trong giai đoạn thử thách, vừa rèn luyện kiếm thuật vừa thích nghi với văn hóa mới.

## V. Công Pháp & Trận Pháp (功法与阵法)
Công pháp chủ đạo là Trục Khách Bách Kiếm Quyết, hệ thống kiếm pháp tổng hợp do Đoạn Kiếm Sinh sáng tạo dựa trên việc phân tích, giải cấu và tái kết hợp sở trường kiếm pháp từ hàng chục tông phái khác nhau. Mỗi đệ tử được khuyến khích phát triển biến thể riêng dựa trên sở học cũ, không có khuôn mẫu cứng nhắc. Đoạn Kiếm Sinh tin rằng kiếm đạo chân chính nằm ở sự thích ứng và sáng tạo, không phải sự tuân thủ mù quáng. Tông môn không có trận pháp cố định, dựa vào địa hình phức tạp của phế tích để phòng thủ. Khi chiến đấu tập thể, đệ tử phối hợp kiếm pháp đa phong cách tạo nên sự biến ảo khó lường cho đối thủ.

## VI. Đặc Sản Môn Phái (门派特产)
Sản phẩm đặc trưng nhất của Trục Khách Đường là bộ sưu tập bí kíp kiếm pháp tàn khuyết từ hàng chục tông phái, được Đoạn Kiếm Sinh biên tập và chú giải thành tài liệu giảng dạy. Tuy mỗi bí kíp đều không hoàn chỉnh, nhưng khi kết hợp lại tạo nên kho tàng kiến thức kiếm đạo đa dạng bậc nhất. Ngoài ra, đệ tử Trục Khách Đường thường sở hữu phế kiếm được tái rèn, những thanh kiếm cũ bị gãy được hàn lại và khắc thêm phù văn mới, mang ý nghĩa tượng trưng "từ đổ nát tái sinh".

## VII. Cơ Sở Hạ Tầng (基础设施)
Trụ sở là phế tích cổ được tu sửa tối thiểu, bao gồm đại sảnh chính nơi Đường Chủ giảng dạy kiếm pháp, các phòng tu luyện cá nhân trong tầng hầm, và sân luyện kiếm ngoài trời giữa các bức tường đổ nát. Hệ thống hành lang ngầm phức tạp dưới phế tích cung cấp đường thoát hiểm và kho chứa bí mật. Không có kết giới phòng thủ chính quy, nhưng Đoạn Kiếm Sinh đã bố trí nhiều bẫy kiếm khí tại các lối vào chính, kết hợp với địa hình đổ nát để tạo thành hệ thống phòng thủ tự nhiên khá hiệu quả.

## VIII. Kinh Tế (经济)
Kinh tế của Trục Khách Đường dựa trên ba nguồn thu chính: hợp đồng hộ tống và bảo vệ từ các thương đoàn nhỏ đi qua vùng ranh giới Đông Hoang và Tây Mạc, bán phế kiếm và vật liệu thu lượm từ phế tích, và thù lao từ các nhiệm vụ truy sát yêu thú sa mạc. Thu nhập đủ để duy trì hoạt động nhưng không dư dả, đệ tử sống khổ hạnh và tự cung tự cấp phần lớn. Đoạn Kiếm Sinh không quan tâm đến giàu có, coi kiếm đạo là mục tiêu duy nhất, nên tông môn giữ phong cách giản dị và thực dụng.

## IX. Lịch Sử Tóm Tắt (简史)
Tám mươi năm trước, Đoạn Kiếm Sinh vốn là thiên tài kiếm đạo của Cửu Hoa Kiếm Tông, được kỳ vọng trở thành chưởng môn thế hệ tiếp theo. Tuy nhiên, hắn bị trục xuất khi bị phát hiện lén nghiên cứu kiếm pháp Ma Đạo Minh, một hành vi cấm kỵ tuyệt đối trong Cửu Hoa. Sau khi lang bạt khắp nơi, chiến đấu với vô số kiếm tu từ nhiều tông phái khác nhau, Đoạn Kiếm Sinh ngộ ra rằng kiếm đạo chân chính không nên bị giới hạn bởi ranh giới tông phái. Hắn lập Trục Khách Đường tại phế tích giữa sa mạc, chuyên thu nhận những kiếm tu bị trục xuất hoặc bất mãn với tông phái cũ, dạy họ phá bỏ khuôn khổ và kết hợp sở học thành kiếm pháp mới. Qua tám mươi năm âm thầm phát triển, tông môn từ vài người trở thành hai trăm thành viên.

## X. Giai Thoại & Bí Mật (轶事与秘密)
Đoạn Kiếm Sinh vẫn giữ một thanh kiếm cổ của Cửu Hoa Kiếm Tông. Hắn nói với mọi người rằng thanh kiếm đã gãy trong ngày bị trục xuất, nhưng thực ra thanh kiếm vẫn nguyên vẹn, được ẩn giấu sâu trong tầng hầm bí mật nhất của phế tích. Đó là thanh kiếm hắn từng dùng suốt thời niên thiếu tại Cửu Hoa, và dù miệng nói đã đoạn tuyệt, hắn chưa bao giờ thực sự buông bỏ. Cửu Hoa Kiếm Tông biết rõ Trục Khách Đường tồn tại và đang thu nhận đệ tử bị trục xuất từ các tông kiếm, nhưng chưa ra tay vì Đoạn Kiếm Sinh chưa chạm đến lợi ích cốt lõi của họ. Tuy nhiên, nếu Trục Khách Bách Kiếm Quyết lan rộng và đe dọa uy tín kiếm đạo chính thống, Cửu Hoa sẽ không tiếp tục im lặng.

## XI. Quan Hệ Thế Lực (势力关系)
- **Cửu Hoa Kiếm Tông:** Mối quan hệ nguy hiểm nhất. Đoạn Kiếm Sinh bị Cửu Hoa trục xuất, Cửu Hoa đang theo dõi nhưng chưa ra tay. Bom nổ chậm có thể bùng phát bất cứ lúc nào.
- **Sa Tặc Liên Minh:** Thường xuyên đụng độ khi đệ tử thực hiện nhiệm vụ hộ tống. Hai bên coi nhau là phiền phức nhưng không phải tử thù.
- **Thiên Sa Thương Hội:** Quan hệ thương mại thuần túy, nhận hợp đồng hộ tống từ thương đoàn nhỏ. Không thân thiết nhưng cũng không thù địch.
