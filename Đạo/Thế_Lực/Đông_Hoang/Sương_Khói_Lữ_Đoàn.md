---
type: faction
name: Sương Khói Lữ Đoàn
hantu: 霜烟旅团
faction_type: Hội
alignment: 4
race: Tinh Linh (có hỗn huyết)
region: Đông Hoang
founded: 120 năm trước
founder: Sương Vũ Hàn
emblem: Suong_Khoi_Lu_Doan.png
specialty: Khám phá phế tích, Ghi chép tri thức cổ, Giải mã ký tự cổ, Bản đồ học
economy:
- Bán bản đồ vẽ tay và ghi chép địa hình
- Giải mã ký tự cổ thuê cho các thế lực
- Trao đổi tri thức lấy vật tư và lương thực
arcs:
  - arc: 1
    status: Hoạt động (đang tạm dừng tại Trạm Biên)
    rank: Hạng Năm
    leader: Đoàn Trưởng Sương Vũ Hàn
    population: 10
    territory:
      - Trạm Biên Nam Cương (tạm trú)
      - Không có lãnh thổ cố định (du mục)
    assets:
      - name: Bộ sưu tập ghi chép phế tích
        type: Tài Nguyên
      - name: Cổ Ngữ Từ Điển tự biên
        type: Tài Nguyên
      - name: Bản đồ vẽ tay Nam Cương
        type: Tài Nguyên
    stats: [15, 30, 40, 10, 10, 50]
    divisions:
      - name: Lữ Đoàn Thám Hiểm
        role: Đội thám hiểm nhỏ chuyên khám phá phế tích, ghi chép tri thức, và vẽ bản đồ
        headcount:
          hoi_truong: 1
          pho_hoi_truong: 1
          thanh_vien: 8
          tong_quan: 0
        members:
          - character: Sương Vũ Hàn
            position: Hội Trưởng (Đoàn Trưởng)
            cultivation: Trúc Cơ Hậu Kỳ
          - character: Nguyệt Phong Linh
            position: Phó Hội Trưởng (Phó Đoàn)
            cultivation: Trúc Cơ Sơ Kỳ
          - character: "[Thành Viên Hỗn Huyết 1]"
            position: Thành Viên
            cultivation: Luyện Khí Viên Mãn
            placeholder: true
          - character: "[Thành Viên Hỗn Huyết 2]"
            position: Thành Viên
            cultivation: Luyện Khí Hậu Kỳ
            placeholder: true
    relationships:
      - faction: Tinh Linh Vương Đình
        description: Sương Vũ Hàn bị Vương Đình trục xuất 120 năm trước vì tự ý tiếp xúc với nhân tộc trao đổi sách cổ. Quan hệ hoàn toàn cắt đứt — Vương Đình coi Lữ Đoàn như nhóm phản nghịch, còn Sương Vũ Hàn không oán hận nhưng cũng không có ý quay về.
        diplomacy:
          lien_minh: -40
          tin: -50
          uy_hiep: 20
          thuong_mai: 0
          on_oan: -30
          le_thuoc: 0
      - faction: Vạn Pháp Thư Quán
        description: Lữ Đoàn đôi khi trao đổi ghi chép với Thư Quán, bán bản sao tri thức cổ để lấy vật tư. Quan hệ hữu hảo giữa những kẻ cùng yêu kiến thức.
        diplomacy:
          lien_minh: 10
          tin: 30
          uy_hiep: 0
          thuong_mai: 40
          on_oan: 0
          le_thuoc: 0
      - faction: Phiêu Bạt Khách Sạn Liên Minh
        description: Lữ Đoàn thường xuyên lưu trú tại các chi nhánh khách sạn trong quá trình di chuyển. Sương Vũ Hàn là khách quen sở hữu Phiêu Bạt Lệnh, và đôi khi đổi bản đồ lấy giảm giá phòng.
        diplomacy:
          lien_minh: 5
          tin: 20
          uy_hiep: 0
          thuong_mai: 30
          on_oan: 0
          le_thuoc: 0
---

# Sương Khói Lữ Đoàn (霜烟旅团)

## I. Tổng Quan (总览)
Sương Khói Lữ Đoàn là đội thám hiểm nhỏ gồm mười Tinh Linh (trong đó ba hỗn huyết), chuyên khám phá phế tích, ghi chép tri thức cổ đại, và vẽ bản đồ những vùng đất chưa ai biết đến ở Nam Cương. Dưới sự dẫn dắt của Đoàn Trưởng Sương Vũ Hàn — Tinh Linh tóc bạc mắt xám bị Vương Đình trục xuất vì tội tự ý giao du với nhân tộc — Lữ Đoàn đã đi qua hầu hết Nam Cương trong một trăm hai mươi năm, ghi chép được bảy phế tích chưa ai biết đến. Tuy chỉ xếp Hạng Năm về quy mô, tri thức mà Lữ Đoàn tích lũy có giá trị vượt xa hạng bậc — đặc biệt cuốn "Cổ Ngữ Từ Điển" tự biên của Sương Vũ Hàn, khả năng giải mã ký tự cổ tốt hơn bất kỳ ai ở Nam Cương.

## II. Địa Lý & Tài Nguyên (地理与资源)
Lữ Đoàn không có lãnh thổ cố định — đó vừa là bản chất vừa là triết lý sống. Hiện đang tạm trú tại Trạm Biên Nam Cương, thuê một kho hàng cũ làm nơi nghỉ chân giữa các chuyến phiêu bạt, nhưng có thể rời đi bất kỳ lúc nào. Trong một trăm hai mươi năm, Lữ Đoàn đã di chuyển liên tục giữa các vùng Nam Cương: từ rìa rừng rậm đến biên giới đầm lầy, từ chân núi Hỏa Vân Sơn đến bờ sông cổ đã cạn. Tài nguyên chính là tri thức tích lũy — bộ sưu tập ghi chép khổng lồ về phế tích, trận pháp cổ, ký tự lạ trên đá, và truyền thuyết địa phương, cùng bộ bản đồ vẽ tay chi tiết nhất về địa hình Nam Cương. Ngoài ra, kỹ năng sinh tồn và ngoại giao đa chủng tộc giúp Lữ Đoàn sống sót ở mọi nơi và giao tiếp với mọi chủng tộc.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
"Tri thức là bất tử, thể xác rồi sẽ tàn." Đây là câu nói Sương Vũ Hàn lặp lại mỗi khi có ai hỏi tại sao gã chấp nhận cuộc sống nguy hiểm thay vì ẩn cư an nhàn. Thu thập và bảo tồn kiến thức cổ đại là sứ mệnh thiêng liêng mà mọi thành viên Lữ Đoàn tự nguyện gánh vác. Quy tắc nghiêm ngặt nhất: ghi chép phải trung thực tuyệt đối, không thêm bớt một ký tự — vì sai lệch một chữ có thể biến tri thức thành rác. Quy tắc thứ hai: không bán tri thức cho kẻ sẽ dùng nó gây hại, dù trả giá bao nhiêu. Truyền thống đáng quý nhất là "Đêm Chuyện Kể" — mỗi tối bên lửa trại, thành viên kể lại câu chuyện hay nhất nghe được trong ngày, biến mỗi đêm thành buổi chia sẻ tri thức và giải trí duy nhất trong cuộc sống du mục khắc khổ.

## IV. Cơ Cấu Tổ Chức (组织结构)
Cơ cấu đơn giản phù hợp với đội nhỏ mười người. Sương Vũ Hàn giữ vai trò Đoàn Trưởng — nam Tinh Linh tóc bạc, mắt xám, dáng gầy gò nhưng bước chân không bao giờ mỏi, cảnh giới Trúc Cơ Hậu Kỳ, bị Vương Đình trục xuất một trăm hai mươi năm trước. Phó Đoàn là Nguyệt Phong Linh — nữ Tinh Linh trẻ cảnh giới Trúc Cơ Sơ Kỳ, giỏi vẽ bản đồ và giải mã ký tự cổ, được Sương Vũ Hàn truyền dạy. Tám thành viên còn lại gồm năm Tinh Linh thuần chủng và ba hỗn huyết, cảnh giới từ Luyện Khí đến Trúc Cơ Sơ Kỳ, mỗi người có sở trường riêng từ nấu ăn đến y thuật dã chiến. Khi đi vào vùng xa lạ, Lữ Đoàn thường thuê thêm tu sĩ nhân tộc hoặc yêu tộc bản địa làm hướng dẫn viên tạm thời.

## V. Công Pháp & Trận Pháp (功法与阵法)
Lữ Đoàn sở hữu "Phong Sương Bộ Pháp" — kỹ thuật di chuyển nhanh trong mọi địa hình, kết hợp phong hệ và thủy hệ linh lực. Bộ pháp này không mạnh trong chiến đấu nhưng cho phép di chuyển qua rừng rậm, đầm lầy, và núi đá với tốc độ gấp đôi người thường, đồng thời giảm tiêu hao thể lực đáng kể. Sương Vũ Hàn sáng tạo bộ pháp này qua hàng chục năm thực chiến với địa hình, và truyền dạy cho mọi thành viên. Lữ Đoàn không có trận pháp và không có chiến thuật tấn công — chiến thuật chính là tránh chiến đấu bằng mọi giá. Sương Vũ Hàn tự hào rằng gã biết lúc nào nên chạy và chạy đi đâu, và điều đó giá trị hơn bất kỳ kiếm pháp nào.

## VI. Đặc Sản Môn Phái (门派特产)
- **Bản Đồ Sương Khói:** Bản đồ vẽ tay chi tiết do Nguyệt Phong Linh thực hiện, ghi chép địa hình, nguồn nước, linh mạch, và vùng nguy hiểm dọc đường. Là bộ bản đồ chính xác nhất về Nam Cương, được các thương nhân và thám hiểm gia săn đón.
- **Cổ Ngữ Từ Điển:** Cuốn từ điển do Sương Vũ Hàn tự biên soạn suốt một trăm hai mươi năm, ghi chép hàng nghìn ký tự cổ cùng cách giải mã. Tài sản vô giá không thể sao chép, vì nhiều mục từ dựa trên trực giác và kinh nghiệm cá nhân.
- **Ghi Chép Phế Tích:** Bộ sưu tập chi tiết về bảy phế tích chưa ai biết đến, bao gồm vị trí, cấu trúc, bẫy trận, và nội dung bia đá. Giá trị nghiên cứu cực cao.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Kho Hàng Tạm Trú (Trạm Biên):** Kho hàng cũ thuê tại Trạm Biên, dùng làm nơi nghỉ chân và sao chép ghi chép phòng mất. Tạm bợ nhưng đủ dùng.
- **Túi Bảo Quản Ghi Chép:** Bộ túi đặc biệt chống ẩm và chống lửa chứa toàn bộ ghi chép và bản đồ, do Lữ Đoàn tự chế. Mất túi này đồng nghĩa mất toàn bộ thành quả một trăm hai mươi năm.
- **Bộ Dụng Cụ Giải Mã:** Công cụ thô sơ gồm bút, mực linh, giấy đặc biệt, và kính phóng đại cấp thấp, dùng để sao chép và phân tích ký tự cổ trên bia đá.

## VIII. Kinh Tế (经济)
Kinh tế Lữ Đoàn rất đơn giản và khiêm tốn. Nguồn thu chính là bán bản sao bản đồ cho thương nhân và tán tu cần nắm địa hình Nam Cương — không bán bản gốc, chỉ bán bản sao với thông tin giới hạn. Nguồn thu thứ hai là dịch vụ giải mã ký tự cổ: đôi khi tông phái hoặc cá nhân phát hiện bia đá cổ nhưng không đọc được, họ thuê Sương Vũ Hàn giải mã với giá không rẻ. Nguồn thu thứ ba là trao đổi trực tiếp — đổi tri thức lấy lương thực, vật tư, và trang bị cần thiết cho chuyến đi tiếp theo. Tổng thu nhập đủ sống nhưng không dư dả, phù hợp với lối sống khổ hạnh mà Lữ Đoàn tự nguyện chọn.

## IX. Lịch Sử Tóm Tắt (简史)
Một trăm hai mươi năm trước, Sương Vũ Hàn bị trục xuất khỏi Tinh Linh Vương Đình vì tội tự ý tiếp xúc với nhân tộc để trao đổi sách cổ — hành vi bị coi là phản bội lập trường cô lập của Vương Đình. Thay vì buồn bã, Sương Vũ Hàn coi đây là cơ hội khám phá thế giới mà gã luôn khao khát. Gã bắt đầu lang thang một mình qua Nam Cương, ghi chép mọi thứ gặp trên đường. Dần dần, những Tinh Linh có cùng đam mê tri thức — bao gồm cả hỗn huyết bị Vương Đình khinh miệt — tìm đến gia nhập, hình thành Lữ Đoàn. Trong suốt một trăm hai mươi năm, Lữ Đoàn đã đi qua hầu hết Nam Cương, phát hiện bảy phế tích chưa ai biết, và hiện đang tạm dừng ở Trạm Biên để bổ sung lương thực và sao chép ghi chép phòng trường hợp bị mất.

## X. Giai Thoại & Bí Mật (轶事与秘密)
Sương Vũ Hàn sở hữu khả năng giải mã ký tự cổ vượt xa bất kỳ ai ở Nam Cương, kể cả trưởng lão Tinh Linh Vương Đình — điều trớ trêu khi chính Vương Đình đã trục xuất gã. Cuốn Cổ Ngữ Từ Điển gã biên soạn là tài sản vô giá mà nếu bị mất, tri thức bên trong sẽ thất truyền vĩnh viễn vì phần lớn dựa trên kinh nghiệm cá nhân không thể truyền đạt bằng lời. Bí mật đáng lo ngại nhất nằm ở chuyến thám hiểm gần nhất: Lữ Đoàn phát hiện một phế tích có bia đá ghi lại sự kiện xảy ra trước cả Kỷ Nguyên Khởi Nguyên — nội dung vượt ngoài mọi lịch sử đã biết, đề cập đến những thực thể và sự kiện mà sử sách hiện tại không hề nhắc đến. Sương Vũ Hàn đang bí mật giải mã, nhưng càng đọc càng bất an, vì nội dung dần hé lộ rằng thế giới hiện tại có thể không phải là "phiên bản đầu tiên."

## XI. Quan Hệ Thế Lực (势力关系)
- **Tinh Linh Vương Đình:** Quan hệ hoàn toàn cắt đứt. Vương Đình coi Lữ Đoàn như nhóm phản nghịch, còn Sương Vũ Hàn không oán hận nhưng cũng không có ý quay về. Ba thành viên hỗn huyết trong Lữ Đoàn càng khiến Vương Đình khinh miệt.
- **Vạn Pháp Thư Quán:** Quan hệ hữu hảo giữa những kẻ cùng yêu kiến thức. Lữ Đoàn trao đổi bản sao ghi chép với Thư Quán để lấy vật tư, cả hai bên đều tôn trọng lẫn nhau.
- **Phiêu Bạt Khách Sạn Liên Minh:** Sương Vũ Hàn là khách quen sở hữu Phiêu Bạt Lệnh, Lữ Đoàn thường xuyên lưu trú tại các chi nhánh trong quá trình di chuyển. Đôi khi đổi bản đồ lấy giảm giá phòng.
