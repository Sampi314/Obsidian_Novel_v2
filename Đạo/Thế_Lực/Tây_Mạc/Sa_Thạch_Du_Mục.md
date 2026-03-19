---
type: faction
name: Sa Thạch Du Mục
hantu: 砂石游牧
faction_type: Bộ Lạc
alignment: 2
race: Thạch Tộc
region: Tây Mạc
founded: Thượng Cổ (Bộ lạc du mục lâu đời nhất Xích Nham Sơn Mạch)
founder: Không rõ (Truyền thừa từ đời Thạch Tộc nguyên thủy)
emblem: Vien_Da_Do_Khac_Dau.png
specialty: Nham Giáp Thuật, Thăm dò mạch khoáng, Cường hóa thân xác bằng khoáng linh
economy:
  - Khai thác khoáng linh từ mạch ngầm (tự cung tự cấp)
  - Trao đổi nham thạch quý với các bộ lạc Thạch Tộc khác
arcs:
  - arc: 1
    status: Du mục (Di chuyển theo mạch khoáng, nguồn sống cạn dần)
    rank: Không Xếp Hạng
    leader: Tộc Trưởng Nham Lưu
    population: 100
    territory:
      - Xích Nham Sơn Mạch (di chuyển theo mùa khoáng linh)
    assets:
      - name: Bản đồ mạch khoáng bí mật
        type: Bí Tịch
      - name: Viên đá khắc dấu bộ lạc
        type: Di Vật
    stats: [30, 20, 5, 100, 40, 10]
    divisions:
      - name: Bộ Lạc Du Mục
        role: Toàn bộ bộ lạc di chuyển cùng nhau, thăm dò và khai thác mạch khoáng
        headcount:
          truong_lao: 3
          chien_binh: 10
          dan_thuong: 87
        members:
          - character: Nham Lưu
            position: Tộc Trưởng
            cultivation: Trúc Cơ Viên Mãn (tương đương)
          - character: "[Trưởng Lão Thăm Dò]"
            position: Trưởng Lão
            cultivation: Trúc Cơ Trung Kỳ (tương đương)
            placeholder: true
          - character: "[Thủ Lĩnh Trinh Sát]"
            position: Đội Trưởng Trinh Sát
            cultivation: Trúc Cơ Sơ Kỳ (tương đương)
            placeholder: true
    relationships:
      - faction: Kim Sa Thợ Mỏ Hội
        description: Quan hệ căng thẳng ngày càng tăng. Nhân Tộc khai thác mỏ quy mô lớn khiến nguồn khoáng linh cạn kiệt, đe dọa sự sinh tồn của bộ lạc. Cả hai đều là kẻ yếu nhưng xung đột lợi ích không thể hòa giải.
        diplomacy:
          lien_minh: -30
          tin: -20
          uy_hiep: 10
          thuong_mai: -50
          on_oan: -30
          le_thuoc: 0
      - faction: Cổ Nham Bộ Lạc
        description: Cùng là Thạch Tộc nhưng khác biệt về lối sống. Cổ Nham coi Sa Thạch Du Mục là "người anh em lạc lối" không thờ Nham Thần. Sa Thạch Du Mục tôn trọng Cổ Nham nhưng từ chối quay về núi thiêng.
        diplomacy:
          lien_minh: 20
          tin: 30
          uy_hiep: 0
          thuong_mai: 10
          on_oan: 0
          le_thuoc: 0
      - faction: Kim Sa Vi Mạch
        description: Mối liên hệ bí ẩn. Sa Thạch Du Mục là chủng tộc duy nhất nhận ra sự tồn tại của Vi Mạch qua rung động trong đá. Gần đây, cả hai đang di chuyển cùng hướng như thể cùng chạy trốn khỏi thứ gì đó.
        diplomacy:
          lien_minh: 0
          tin: 10
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 0
---

# Sa Thạch Du Mục (砂石游牧)

## I. Tổng Quan (总览)

Sa Thạch Du Mục là bộ lạc Thạch Tộc du mục lâu đời nhất Xích Nham Sơn Mạch, gồm khoảng một trăm cá thể sống bằng cách di chuyển theo các mạch khoáng linh trong vùng núi đá đỏ. Tộc Trưởng Nham Lưu, một Thạch Tộc già có thân xác bằng sa thạch đỏ với tu vi tương đương Trúc Cơ Viên Mãn, dẫn dắt bộ lạc duy trì lối sống du mục truyền thống đã tồn tại từ thuở thượng cổ. Tuy không xếp hạng về thế lực, bộ lạc sở hữu kiến thức vô giá về hệ thống mạch khoáng ngầm trong lòng đất, bao gồm cả những mạch chưa ai biết đến. Họ đang đối mặt với khủng hoảng sinh tồn khi nguồn khoáng linh ngày càng cạn kiệt do hoạt động khai thác quy mô lớn của Nhân Tộc.

## II. Địa Lý & Tài Nguyên (地理与资源)

Lãnh thổ của Sa Thạch Du Mục không cố định mà thay đổi theo mùa khoáng linh, rải rác khắp Xích Nham Sơn Mạch. Vùng núi đá đỏ này có nhiều hang động tự nhiên và mạch khoáng chạy ngầm dưới lòng đất, tạo nên môi trường sống lý tưởng cho Thạch Tộc. Tài nguyên sống còn của bộ lạc là linh thạch thô khai thác từ mạch khoáng, vì Thạch Tộc "ăn" khoáng linh để duy trì thân xác đá. Tuy nhiên, từ khi Nhân Tộc, đặc biệt là Kim Sa Thợ Mỏ Hội, bắt đầu khai thác mỏ quy mô lớn, mạch khoáng ngày càng cạn kiệt, buộc bộ lạc phải di chuyển xa hơn và thường xuyên hơn để tìm nguồn sống. Bộ lạc giữ bí mật về một mạch khoáng ngầm khổng lồ chưa ai biết, bảo vật cuối cùng đảm bảo sự sinh tồn.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)

Triết lý cốt lõi của Sa Thạch Du Mục là: "Đá sinh ra từ đất, trở về đất — Thạch Tộc cũng vậy." Khác với Cổ Nham Bộ Lạc thờ Nham Thần, Sa Thạch Du Mục không tôn thờ thần linh cụ thể mà kính trọng đất đai và khoáng mạch như nguồn sống. Quy tắc tối thượng là không bao giờ khai thác cạn kiệt một mạch khoáng, luôn để lại phần cho đất phục hồi, dù đang thiếu thốn cũng không được tham lam. Mỗi khi di chuyển đến nơi mới, bộ lạc để lại một viên đá khắc dấu hiệu riêng tại nơi cũ, đánh dấu rằng họ đã từng sống ở đây và sẽ trở lại khi mạch khoáng phục hồi. Cấm kỵ lớn nhất là không bán khoáng linh cho Nhân Tộc, dù đói cũng không phá vỡ nguyên tắc này.

## IV. Cơ Cấu Tổ Chức (组织结构)

Bộ lạc tổ chức đơn giản, phù hợp với lối sống du mục. Đứng đầu là Tộc Trưởng Nham Lưu, Thạch Tộc già có thân xác sa thạch đỏ, di chuyển chậm chạp nhưng ý chí cứng rắn và kinh nghiệm sâu rộng. Dưới Tộc Trưởng là ba Trưởng Lão tu vi tương đương Trúc Cơ Trung Kỳ, phụ trách thăm dò mạch khoáng mới và quyết định hướng di chuyển. Mười Thạch Tộc trinh sát trẻ, nhanh nhẹn nhất bộ lạc, chuyên đi trước tìm mạch khoáng và dò xét xem khu vực mới có an toàn không. Tám mươi bảy Thạch Tộc còn lại là dân thường, đa phần tu vi tương đương Luyện Khí, di chuyển cùng đoàn và tham gia khai thác khoáng linh.

## V. Công Pháp & Trận Pháp (功法与阵法)

Thạch Tộc không tu luyện theo cách Nhân Tộc mà hấp thu khoáng linh trực tiếp từ đá để cường hóa thân xác. Kỹ thuật đặc trưng nhất của Sa Thạch Du Mục là Nham Giáp Thuật, cho phép cứng hóa lớp ngoài thân thể thành giáp đá cứng khi bị tấn công, tạo lớp phòng thủ vật lý gần như bất khả xâm phạm đối với vũ khí thường. Khi toàn bộ bộ lạc phối hợp, họ có thể tạo ra rung chấn nhỏ trên mặt đất, vừa làm vũ khí phòng thủ vừa dùng để giao tiếp đường dài với các Thạch Tộc khác. Ngoài ra, Thạch Tộc có khả năng cảm nhận rung động qua đá và đất, cho phép phát hiện sự di chuyển ngầm của sinh vật khác, kể cả Kim Sa Vi Mạch mà không ai khác nhận ra.

## VI. Đặc Sản Môn Phái (门派特产)

- **Nham Thạch Khắc Ký:** Những viên đá khắc dấu bộ lạc, tuy đơn giản nhưng chứa vi lượng linh lực của Thạch Tộc. Qua thời gian, những viên đá này trở thành mốc dẫn đường trong Xích Nham Sơn Mạch cho bất kỳ ai biết đọc dấu hiệu.
- **Sa Thạch Tinh Hoa:** Loại đá đỏ đặc biệt do Thạch Tộc bài tiết khi hấp thu quá nhiều khoáng linh, có chứa năng lượng địa mạch cô đọng. Hiếm hoi và cực kỳ quý giá nếu dùng trong luyện khí hệ Thổ.

## VII. Cơ Sở Hạ Tầng (基础设施)

- **Doanh Trại Di Động:** Bộ lạc không xây dựng công trình cố định. Mỗi khi đến nơi mới, Thạch Tộc tận dụng hang động tự nhiên hoặc tạo ra hốc đá tạm thời bằng cách đào vào vách núi. Khi rời đi, mọi dấu vết đều bị xóa.
- **Kho Khoáng Linh:** Một "chiếc túi" bằng đá rỗng do Tộc Trưởng mang theo, chứa khoáng linh dự trữ cho cả bộ lạc trong trường hợp không tìm được mạch mới kịp thời. Lượng dự trữ hiện tại đang giảm dần.

## VIII. Kinh Tế (经济)

Kinh tế của Sa Thạch Du Mục hoàn toàn tự cung tự cấp, không tham gia vào hệ thống thương mại của Nhân Tộc. Nguồn sống duy nhất là khoáng linh khai thác từ mạch ngầm, dùng để "ăn" và duy trì thân xác đá. Đôi khi bộ lạc trao đổi nham thạch quý với các bộ lạc Thạch Tộc khác như Cổ Nham Bộ Lạc, nhưng quy mô rất nhỏ. Tình trạng kinh tế hiện tại đáng lo ngại: mạch khoáng cạn kiệt dần do khai thác công nghiệp của Nhân Tộc, bộ lạc phải di chuyển xa hơn và thường xuyên hơn, tiêu hao nhiều khoáng linh hơn cho việc di chuyển, tạo ra vòng xoáy suy thoái.

## IX. Lịch Sử Tóm Tắt (简史)

Sa Thạch Du Mục là bộ lạc Thạch Tộc du mục lâu đời nhất Xích Nham Sơn Mạch, tồn tại từ thời thượng cổ khi mạch khoáng linh còn dồi dào và Nhân Tộc chưa đến Tây Mạc. Thuở ấy, bộ lạc di chuyển chậm rãi theo vòng tròn lớn quanh sơn mạch, mỗi mạch khoáng đều có đủ thời gian phục hồi trước khi họ quay lại.

Từng có thời kỳ hưng thịnh khi số lượng lên đến vài trăm, nhưng tình hình thay đổi khi Nhân Tộc bắt đầu khai thác mỏ quy mô lớn. Mạch khoáng bị đào sạch, đất đai bị xáo trộn, và Thạch Tộc buộc phải di chuyển xa hơn vào vùng hiểm trở hơn. Mối quan hệ với Kim Sa Thợ Mỏ Hội ngày càng căng thẳng, dù cả hai đều là kẻ yếu trong cục diện thế lực Tây Mạc. Tộc Trưởng Nham Lưu đang tìm kiếm giải pháp dài hạn cho cuộc khủng hoảng sinh tồn này.

## X. Giai Thoại & Bí Mật (轶事与秘密)

Tộc Trưởng Nham Lưu tin rằng sâu trong lòng Xích Nham Sơn Mạch có "Nham Mẫu", một khối đá cổ đại khổng lồ là nguồn gốc của mọi Thạch Tộc. Đây là truyền thuyết được truyền miệng qua nhiều đời Tộc Trưởng, nhưng chưa ai tìm thấy Nham Mẫu. Nham Lưu tin rằng nếu tìm được Nham Mẫu, Thạch Tộc sẽ không cần phụ thuộc vào mạch khoáng nữa.

Bí mật lớn nhất mà bộ lạc giữ kín là vị trí của một mạch khoáng ngầm khổng lồ chưa ai biết, đủ cung cấp khoáng linh cho cả trăm Thạch Tộc trong hàng ngàn năm. Nếu thông tin lộ ra, chắc chắn Nhân Tộc sẽ tranh đoạt bằng mọi giá. Gần đây, trinh sát báo cáo một hiện tượng kỳ lạ: Kim Sa Vi Mạch đang di chuyển cùng hướng với bộ lạc, như thể cả hai đều đang chạy trốn khỏi thứ gì đó đang đến từ phía đông.

## XI. Quan Hệ Thế Lực (势力关系)

- **Kim Sa Thợ Mỏ Hội:** Xung đột lợi ích trực tiếp. Hoạt động khai thác mỏ quy mô lớn của Thợ Mỏ Hội là nguyên nhân chính khiến nguồn khoáng linh cạn kiệt, đe dọa sự sinh tồn của bộ lạc. Hai bên đều yếu nhưng mâu thuẫn không thể hòa giải.
- **Cổ Nham Bộ Lạc:** Cùng là Thạch Tộc, có mối liên hệ huyết thống xa. Cổ Nham coi Sa Thạch Du Mục là "người anh em lạc lối" không chịu thờ Nham Thần. Sa Thạch Du Mục tôn trọng Cổ Nham nhưng kiên quyết giữ lối sống du mục tự do, từ chối quay về núi thiêng.
- **Kim Sa Vi Mạch:** Mối liên hệ bí ẩn và đơn phương. Sa Thạch Du Mục là chủng tộc duy nhất nhận ra sự tồn tại của Vi Mạch qua rung động trong đá. Hai bên chưa bao giờ giao tiếp trực tiếp, nhưng dường như đang bị cùng một thế lực bí ẩn đẩy về phía tây.
