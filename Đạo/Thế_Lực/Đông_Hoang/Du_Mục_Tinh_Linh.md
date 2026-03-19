---
type: faction
name: Du Mục Tinh Linh
hantu: 游牧精灵
faction_type: Bộ Lạc
alignment: 4
race: Tinh Linh Tộc
region: Đông Hoang
founded: 40 năm trước
founder: Phong Diệp
emblem: La_Xanh_Bay_Trong_Gio.png
specialty: Bản đồ rừng Đông Hoang, Thu hái dược thảo hoang dã, Trinh sát địa hình
economy:
- Thu hái và bán dược thảo hoang dã dọc đường
- Cung cấp dịch vụ hướng đạo rừng
- Trao đổi tin tức và hàng hóa giữa các cộng đồng hẻo lánh
arcs:
  - arc: 1
    status: Lang thang tự do
    rank: Không Xếp Hạng
    leader: Trưởng Đoàn Phong Diệp
    population: 30
    territory:
      - Không cố định (Lang thang giữa các khu rừng Đông Hoang)
    assets:
      - name: Bản Đồ Rừng Đông Hoang (Bí mật)
        type: Tài Nguyên
      - name: Bộ Sưu Tập Hạt Giống Dược Thảo
        type: Tài Nguyên
    stats: [20, 15, 10, 30, 5, 15]
    divisions:
      - name: Đoàn Du Mục
        role: Di chuyển, thu hái, trao đổi, sinh tồn tập thể
        headcount:
          truong_lao: 3
          chien_binh: 7
          dan_thuong: 20
        members:
          - character: Phong Diệp
            position: Trưởng Đoàn
            cultivation: Trúc Cơ Viên Mãn
          - character: "[Tinh Linh Hướng Đạo]"
            position: Hướng Đạo
            cultivation: Trúc Cơ Trung Kỳ
            placeholder: true
          - character: "[Dược Thảo Sư]"
            position: Thầy Thuốc
            cultivation: Trúc Cơ Sơ Kỳ
            placeholder: true
    relationships:
      - faction: Tinh Linh Vương Đình
        description: Quan hệ căng thẳng, Vương Đình coi Đoàn là kẻ phản bội rời bỏ cộng đồng nhưng không đáng để truy đuổi. Phong Diệp từ chối quay về.
        diplomacy:
          lien_minh: -20
          tin: -30
          uy_hiep: 20
          thuong_mai: 0
          on_oan: -30
          le_thuoc: 0
      - faction: Lạc Diệp Tinh Linh
        description: Đồng cảm sâu sắc, Lạc Diệp Tinh Linh cũng là nhóm Tinh Linh rời bỏ Vương Đình. Hai bên thỉnh thoảng gặp nhau và trao đổi tin tức.
        diplomacy:
          lien_minh: 40
          tin: 50
          uy_hiep: 0
          thuong_mai: 30
          on_oan: 10
          le_thuoc: 0
      - faction: Hoang Dã Thợ Săn Bang
        description: Quan hệ thân thiện, Thợ Săn Bang đôi khi thuê Đoàn làm hướng đạo trong rừng sâu. Hai bên trao đổi dược thảo lấy thịt thú.
        diplomacy:
          lien_minh: 20
          tin: 40
          uy_hiep: 0
          thuong_mai: 50
          on_oan: 0
          le_thuoc: 0
---

# DU MỤC TINH LINH (游牧精灵)

## I. Tổng Quan (总览)
Du Mục Tinh Linh là một nhóm nhỏ gồm khoảng ba mươi Tinh Linh chọn lối sống lang thang giữa các khu rừng Đông Hoang, từ chối hệ thống giai cấp cứng nhắc của Tinh Linh Vương Đình. Với triết lý "Rừng là nhà, gió là đường", Đoàn di chuyển liên tục, không bao giờ ở đâu quá một mùa. Không có trụ sở, không có lãnh thổ, không có quy tắc ràng buộc — ai muốn đi thì tự do đi, ai muốn gia nhập chỉ cần bước theo. Đây là cộng đồng Tinh Linh tự do nhất Đông Hoang, và cũng là mong manh nhất.

## II. Địa Lý & Tài Nguyên (地理与资源)
Đoàn không có lãnh thổ cố định mà di chuyển theo mùa giữa các khu rừng Đông Hoang, từ Vĩnh Hằng Sâm Lâm đến rừng phía nam, từ rìa đông gần biển đến biên giới tây giáp sa mạc. Mỗi nơi dừng chân là một bãi trống tự nhiên trong rừng, dựng lều tạm từ cành lá và dây leo. Sau khi rời đi, dấu vết duy nhất còn lại là một cây non mới trồng — phong tục đánh dấu hành trình. Tài nguyên đến từ việc thu hái dược thảo hoang dã dọc đường — nhờ di chuyển liên tục, Đoàn tiếp cận được nhiều loại dược thảo quý chỉ mọc ở những vùng rừng hẻo lánh mà người định cư không bao giờ tìm tới. Ngoài ra, Đoàn trao đổi hàng hóa với các cộng đồng nhỏ gặp trên đường, đóng vai trò thương nhân lưu động bất đắc dĩ.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
Du Mục Tinh Linh tin rằng tự do là giá trị cao nhất — cao hơn cả tu vi, cao hơn cả sự an toàn. Họ từ chối mọi hệ thống phân cấp: không có mệnh lệnh, chỉ có thảo luận; không có quy tắc cứng, chỉ có nguyên tắc tự nguyện. Phong Diệp là "Trưởng Đoàn" nhưng thực tế chỉ là người đề xuất hướng đi — mọi quyết định lớn đều bàn bạc tập thể bên đống lửa. Phong tục quan trọng nhất là trồng cây tại mỗi nơi dừng chân: mỗi Tinh Linh chọn một hạt giống, dùng chút linh lực mộc hệ thúc đẩy nó nảy mầm, rồi lên đường. Qua bốn mươi năm, hàng ngàn cây non do Đoàn trồng đã mọc rải rác khắp Đông Hoang — bản đồ sống ghi lại hành trình lang thang.

## IV. Cơ Cấu Tổ Chức (组织结构)
Trưởng Đoàn Phong Diệp là Tinh Linh trẻ (theo chuẩn Tinh Linh, mới hơn hai trăm tuổi), mái tóc xanh lá cắt ngắn bất thường so với Tinh Linh truyền thống, mắt màu hổ phách luôn nhìn về phía chân trời. Tu vi Trúc Cơ Viên Mãn, đủ sức đột phá Kim Đan nhưng không muốn — nàng cho rằng Kim Đan đòi hỏi ổn định tu luyện, mâu thuẫn với lối sống du mục. Ba Trưởng Lão không phải cấp bậc chính thức mà chỉ là ba Tinh Linh lớn tuổi nhất được tôn trọng vì kinh nghiệm. Bảy "chiến binh" là những Tinh Linh biết chiến đấu, tự nguyện bảo vệ Đoàn khi gặp nguy hiểm. Hai mươi thành viên còn lại là Tinh Linh Luyện Khí và Trúc Cơ Sơ Kỳ, phần lớn gia nhập vì bất mãn với Vương Đình hoặc đơn giản là muốn xem thế giới. Thành phần biến động liên tục — người đến, người đi, không ai bị giữ lại.

## V. Công Pháp & Trận Pháp (功法与阵法)
- **Công Pháp:** Đoàn tu luyện thuật mộc hệ tự do, không theo khuôn mẫu cứng nhắc của Vương Đình. Phong Diệp tự sáng tạo bộ "Phong Lâm Du Mục Quyết" — công pháp lấy cảm hứng từ gió thổi qua rừng, nhấn mạnh sự linh hoạt và thích ứng hơn là sức mạnh thuần túy. Người tu luyện có thể hấp thụ linh khí từ bất kỳ loại cây nào chứ không chỉ cổ thụ thiêng, phù hợp với lối sống di chuyển liên tục.
- **Trận Pháp:** Không có trận pháp phòng thủ. Đoàn dựa vào sự di chuyển liên tục để tránh nguy hiểm — không ở đâu đủ lâu để kẻ thù kịp tập hợp lực lượng. Khi gặp đe dọa, chiến thuật duy nhất là "tản mác và hội tụ" — mọi người chạy tán loạn vào rừng, dùng khả năng hòa mình vào cây cối bẩm sinh của Tinh Linh để ẩn nấp, rồi tập hợp lại tại điểm hẹn bí mật.

## VI. Đặc Sản Môn Phái (门派特产)
- **Dược Thảo Hoang Dã Quý Hiếm:** Nhờ di chuyển liên tục qua nhiều vùng rừng hẻo lánh, Đoàn thu hái được nhiều loại dược thảo cực hiếm chỉ mọc ở những nơi xa xôi. Đây là hàng hóa trao đổi chính.
- **Bản Đồ Rừng Đông Hoang:** Bản đồ tay do Phong Diệp vẽ suốt bốn mươi năm — chi tiết nhất từng tồn tại, ghi cả vị trí dược thảo quý, nguồn nước, khu vực nguy hiểm, và lãnh thổ các thế lực. Bản đồ này nếu lọt ra ngoài sẽ có giá trị vô cùng lớn.
- **Hạt Giống Lai Tạo:** Qua việc trồng cây ở nhiều vùng sinh thái khác nhau, Đoàn vô tình tạo ra một số giống cây lai tạo tự nhiên có đặc tính độc đáo — chịu hạn, kháng độc, hoặc sinh trưởng nhanh bất thường.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Lều Tạm Di Động:** Mỗi gia đình hoặc nhóm nhỏ có một bộ lều tạm gọn nhẹ, làm từ vỏ cây và dây leo, dựng lên trong nửa canh giờ và thu gọn còn nhanh hơn. Tổng cộng khoảng mười chiếc lều xếp thành vòng tròn quanh đống lửa trung tâm.
- **Đống Lửa Hội Đồng:** Nơi cả Đoàn tập hợp mỗi tối để ăn, kể chuyện và thảo luận. Đây không phải cơ sở vật chất mà là biểu tượng tinh thần — ở đâu có đống lửa của Đoàn, ở đó là nhà.
- **Điểm Hẹn Bí Mật:** Phong Diệp đánh dấu khoảng hai mươi điểm hẹn bí mật rải rác khắp các khu rừng Đông Hoang, nơi Đoàn tập hợp lại sau khi tản mác tránh nguy hiểm. Mỗi điểm hẹn được đánh dấu bằng ký hiệu khắc trên cây mà chỉ Tinh Linh trong Đoàn mới nhận ra.

## VIII. Kinh Tế (经济)
Kinh tế của Đoàn dựa vào trao đổi trực tiếp, không dùng tiền tệ. Dược thảo hoang dã thu hái dọc đường là hàng hóa chính, đổi lấy thực phẩm, vải vóc, và đôi khi linh thạch hạ phẩm từ các cộng đồng gặp trên đường. Phong Diệp cũng nhận làm hướng đạo rừng cho các nhóm thợ săn hoặc thương đoàn nhỏ — dẫn đường qua những khu rừng nguy hiểm để lấy phí. Thu nhập bấp bênh nhưng Đoàn không cần nhiều — Tinh Linh có thể hấp thụ linh khí từ cây cối để bổ sung năng lượng, nhu cầu ăn uống thấp hơn hẳn nhân tộc.

## IX. Lịch Sử Tóm Tắt (简史)
Bốn mươi năm trước, Phong Diệp rời Vĩnh Hằng Sâm Lâm vì không chấp nhận hệ thống giai cấp cứng nhắc — nơi Tinh Linh bị phân loại từ lúc sinh ra theo huyết thống, ai ở đâu thì ở đó suốt đời. Nàng không muốn nổi loạn hay lật đổ, chỉ đơn giản muốn đi. Vài Tinh Linh cùng chí hướng bước theo nàng ra khỏi rừng thiêng, bắt đầu cuộc sống du mục. Dọc đường, Đoàn thu nhận thêm Tinh Linh lạc lõng — kẻ bị trục xuất, kẻ tự nguyện rời đi, kẻ mất nhà. Vương Đình ban đầu gửi người đuổi theo nhưng nhanh chóng bỏ cuộc, coi nhóm nhỏ ba mươi Tinh Linh du mục là không đáng để phí sức truy đuổi. Bốn mươi năm qua, Đoàn đã đi qua gần như mọi ngóc ngách Đông Hoang, chứng kiến nhiều thứ mà cả Vương Đình lẫn các đại phái đều không biết đến.

## X. Giai Thoại & Bí Mật (轶事与秘密)
Phong Diệp bí mật vẽ bản đồ tất cả các khu rừng Đông Hoang suốt bốn mươi năm — bản đồ chi tiết nhất từng tồn tại, ghi chép vị trí dược thảo quý, nguồn nước bí mật, hang động ẩn giấu, lãnh thổ các thế lực, và cả những khu vực nguy hiểm mà không ai dám bước vào. Nếu bản đồ này lọt vào tay bất kỳ thế lực nào — Thiên Yêu Đình, Huyết Sát Minh, hay thậm chí Tinh Linh Vương Đình — hậu quả sẽ khôn lường. Phong Diệp cất bản đồ bằng phương pháp mộc hệ đặc biệt: cuộn giấu trong thân một cây sống, chỉ có thể mở bằng linh lực của nàng.

Đoàn đôi khi vô tình đi qua lãnh thổ của thế lực mạnh mà không biết — đã từng dựng trại ngay rìa hang ổ của Ảo Ảnh Lâm Tộc mà không hay, chỉ rời đi vì "cảm giác không thoải mái". Sự ngây thơ này vừa là điểm yếu chí mạng vừa là lý do họ còn sống — kẻ mạnh thường không thèm để ý đến nhóm nhỏ vô hại qua đường.

Gần đây, Phong Diệp phát hiện nhiều khu rừng phía nam đang chết dần — cây cối héo úa không rõ nguyên nhân, linh khí loãng dần. Nàng ghi chép hiện tượng này vào bản đồ nhưng chưa tìm ra giải thích, chỉ biết rằng phạm vi ảnh hưởng đang mở rộng mỗi năm.

## XI. Quan Hệ Thế Lực (势力关系)
- **Tinh Linh Vương Đình:** Quan hệ căng thẳng nhưng không thù địch. Vương Đình coi Đoàn là kẻ phản bội nhưng không đáng để truy đuổi. Phong Diệp thi thoảng nghe tin tức về Vương Đình qua các Tinh Linh khác và thầm lo lắng.
- **Lạc Diệp Tinh Linh:** Đồng cảm sâu sắc, cũng là nhóm Tinh Linh rời bỏ Vương Đình. Hai bên thỉnh thoảng gặp nhau trong rừng, chia sẻ tin tức và dược thảo.
- **Hoang Dã Thợ Săn Bang:** Quan hệ thân thiện thực tế — Thợ Săn Bang thuê Đoàn làm hướng đạo, đổi lại cung cấp thịt thú và tin tức thế giới bên ngoài rừng.
