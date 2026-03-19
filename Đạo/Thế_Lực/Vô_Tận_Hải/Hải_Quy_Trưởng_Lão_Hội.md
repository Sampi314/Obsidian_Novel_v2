---
type: faction
name: Hải Quy Trưởng Lão Hội
hantu: 海龟长老会
faction_type: Hội
alignment: 5
race: Hải Tộc (Rùa Biển Linh Thú)
region: Vô Tận Hải
founded: Viễn Cổ Kỷ Nguyên
founder: Huyền Quy (tự phát tập hợp)
emblem: Quy_Giap_Co_Tu.png
specialty: Ký ức thủy cảnh, Trường sinh thiền định, Cổ sử biển sâu
economy:
- Bán thông tin lịch sử và tiên tri cho các thế lực
- Cho phép tu sĩ đến thiền định trong Quy Giáp Đường (thu phí linh thạch)
- Đổi ký ức cổ đại lấy tài nguyên dưỡng sinh
arcs:
  - arc: 1
    status: Ẩn cư quan sát
    rank: Hạng Tư
    leader: Đại Trưởng Lão Huyền Quy
    population: 18
    territory:
      - Quy Giáp Đường (đáy biển trung tâm Vô Tận Hải)
      - Tĩnh Tức Hải Vực (vùng biển yên lặng xung quanh hang)
    assets:
      - name: Quy Giáp Đường
        type: Công Trình
      - name: Ký Ức Thủy Cảnh Trận
        type: Trận Pháp
      - name: Thiên Đạo Quy Giáp
        type: Pháp Bảo
    stats: [160, 200, 450, 180, 400, 350]
    divisions:
      - name: Trưởng Lão Đường
        role: Nghị sự và lưu trữ ký ức cổ đại
        headcount:
          hoi_truong: 1
          pho_hoi_truong: 0
          thanh_vien: 7
          tong_quan: 0
        members:
          - character: Huyền Quy
            position: Đại Trưởng Lão
            cultivation: Kim Đan Hậu Kỳ
            placeholder: false
          - character: "[Bạch Quy]"
            position: Trưởng Lão
            cultivation: Kim Đan Trung Kỳ
            placeholder: true
      - name: Thiếu Niên Quy Đường
        role: Đào tạo thế hệ rùa biển trẻ, ghi chép sự kiện hiện tại
        headcount:
          hoi_truong: 0
          pho_hoi_truong: 1
          thanh_vien: 10
          tong_quan: 0
        members:
          - character: "[Ấu Quy Đầu Lĩnh]"
            position: Giám Hộ
            cultivation: Trúc Cơ Hậu Kỳ
            placeholder: true
    relationships:
      - faction: Hải Thần Cung
        description: Từng cung cấp thông tin nhưng bị phớt lờ vì tốc độ truyền đạt quá chậm. Hải Thần Cung vẫn tôn trọng Huyền Quy nhưng không coi trọng ý kiến của hội.
        diplomacy:
          lien_minh: 10
          tin: 30
          uy_hiep: 0
          thuong_mai: 15
          on_oan: -10
          le_thuoc: 5
      - faction: Hải Tảo Nông Dân Hội
        description: Quan hệ láng giềng hòa hảo. Nông dân thỉnh thoảng mang tảo linh đến cúng dường các trưởng lão để đổi lấy lời khuyên.
        diplomacy:
          lien_minh: 20
          tin: 40
          uy_hiep: 0
          thuong_mai: 25
          on_oan: 0
          le_thuoc: 0
      - faction: Thâm Hải Thám Hiểm Đoàn
        description: Các nhà thám hiểm thường tìm đến Huyền Quy để hỏi về địa hình cổ đại và vị trí di tích, sẵn sàng trả giá cao cho thông tin.
        diplomacy:
          lien_minh: 15
          tin: 50
          uy_hiep: 0
          thuong_mai: 60
          on_oan: 0
          le_thuoc: 0
---

# HẢI QUY TRƯỞNG LÃO HỘI (海龟长老会)

## I. Tổng Quan (总览)
Hải Quy Trưởng Lão Hội là một tập hợp tự nhiên của những con rùa biển linh thú già nhất Vô Tận Hải, lấy trí tuệ và ký ức làm sức mạnh cốt lõi. Với tổng cộng mười tám thành viên, hội không có quân đội, không có lãnh thổ rộng lớn, nhưng sở hữu kho tàng kiến thức trải dài hàng nghìn năm lịch sử đại dương. Đứng đầu là Đại Trưởng Lão Huyền Quy, một con rùa biển hơn năm nghìn tuổi với tu vi tương đương Kim Đan Hậu Kỳ, đặt trụ sở tại Quy Giáp Đường dưới đáy biển trung tâm Vô Tận Hải. Hội giữ thái độ trung lập tuyệt đối, không tham gia tranh chấp giữa các thế lực, chỉ quan sát và ghi nhớ — coi đó là sứ mệnh tối thượng của mình.

## II. Địa Lý & Tài Nguyên (地理 与 资源)
Quy Giáp Đường nằm trong một hang động rộng lớn dưới đáy biển, lối vào hẹp chỉ vừa một con rùa, khiến kẻ thù khó lòng xâm nhập. Bên trong hang có linh khí trung bình và một hồ nước ngọt tự nhiên — điều cực kỳ hiếm có dưới đáy biển sâu. Xung quanh Quy Giáp Đường là Tĩnh Tức Hải Vực, một vùng biển yên lặng kỳ lạ nơi hải lưu dừng lại và mọi âm thanh đều bị triệt tiêu, tạo môi trường lý tưởng cho thiền định và hồi tưởng. Tài nguyên lớn nhất của hội không phải là linh thạch hay khoáng vật, mà là trí nhớ — các trưởng lão sống hàng nghìn năm, chứng kiến và ghi nhớ mọi biến cố đã xảy ra trên đại dương. Đáy hang còn có mạch nước ấm ngầm cung cấp nhiệt độ ổn định, giúp các rùa biển già yếu duy trì sức khỏe.

## III. Văn Hóa & Tín Ngưỡng (文化 与 信仰)
Thành viên đều là rùa biển linh thú già, đã tu luyện đủ lâu để khai mở linh trí và có khả năng giao tiếp bằng thần thức. Hội coi trọng sự kiên nhẫn và trí tuệ hơn sức mạnh vũ lực — triết lý cốt lõi là "Sống lâu hơn kẻ thù là chiến thắng vĩ đại nhất." Các trưởng lão tin rằng đại dương có ý chí riêng, mỗi đợt sóng đều mang thông điệp từ thiên đạo, và nhiệm vụ của rùa biển là lắng nghe, ghi nhớ, rồi truyền lại cho thế hệ sau. Mỗi năm vào ngày triều cường lớn nhất, cả hội tập trung tại trung tâm Quy Giáp Đường để thực hiện Đại Ký Ức Lễ — mỗi trưởng lão chia sẻ một ký ức quan trọng nhất trong năm, khắc lên mai rùa bằng linh lực để lưu giữ vĩnh viễn.

## IV. Cơ Cấu Tổ Chức (组织结构)
Hội có cơ cấu đơn giản, chia thành hai bộ phận chính. Trưởng Lão Đường gồm Đại Trưởng Lão Huyền Quy và bảy trưởng lão có tuổi từ một nghìn đến ba nghìn năm, tu vi từ Kim Đan Sơ Kỳ đến Kim Đan Trung Kỳ, phụ trách nghị sự và lưu trữ ký ức cổ đại. Thiếu Niên Quy Đường gồm mười con rùa dưới năm trăm tuổi, tu vi ở cảnh giới Trúc Cơ, đang trong giai đoạn học hỏi và được giao nhiệm vụ ghi chép các sự kiện hiện tại. Mỗi cuộc họp của hội kéo dài hàng tháng trời vì tốc độ nói chuyện cực chậm — bất kỳ ai nóng tính đến dự họp đều sẽ phát điên trước khi cuộc họp kết thúc. Huyền Quy nói chậm rãi đến mức cần cả ngày mới xong một câu hoàn chỉnh, nhưng mỗi lời ông nói đều mang trọng lượng ngàn cân.

## V. Công Pháp & Trận Pháp (功法 与 阵法)
Công pháp trấn hội là Quy Tức Trường Sinh Quyết, một pháp môn đặc thù giúp kéo dài tuổi thọ vượt xa giới hạn bình thường của cảnh giới tương ứng, nhưng đổi lại tốc độ tu luyện cực kỳ chậm chạp. Huyền Quy còn nắm giữ Ký Ức Thủy Cảnh — một thần thông cho phép chiếu lại cảnh tượng đã chứng kiến trong quá khứ lên mặt nước, tái hiện rõ ràng như thể đang xảy ra trước mắt. Ngoài ra, tám trưởng lão cùng triển khai Bát Quy Hộ Giáp Trận, dùng mai rùa liên kết thành vòng tròn phòng thủ gần như bất khả xâm phạm. Nhược điểm lớn nhất là khả năng tấn công gần như bằng không — hội hoàn toàn dựa vào phòng ngự và trốn tránh.

## VI. Đặc Sản Môn Phái (门派特产)
- **Quy Giáp Ký Ức Phiến:** Mảnh mai rùa rụng tự nhiên, bên trong chứa một đoạn ký ức lịch sử. Tu sĩ có thể dùng thần thức để xem lại cảnh tượng quá khứ, là vật phẩm quý giá cho các sử gia và nhà khảo cổ.
- **Tĩnh Tức Thủy:** Nước lấy từ hồ nước ngọt trong Quy Giáp Đường, có tác dụng an thần và ổn định tâm cảnh, đặc biệt hữu ích cho tu sĩ bị tẩu hỏa nhập ma hoặc tâm cảnh bất ổn.
- **Trường Sinh Tảo:** Loại tảo linh mọc trên mai rùa trưởng lão, hấp thu tinh hoa trường sinh qua hàng trăm năm, có tác dụng kéo dài tuổi thọ khi sắc thành trà.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Quy Giáp Đường:** Hang động chính rộng lớn, trần hang phủ đầy thạch nhũ phát quang, tạo ánh sáng dịu nhẹ. Tám vị trí ngồi bằng đá tự nhiên xếp thành vòng tròn ở trung tâm, dành cho các trưởng lão nghị sự.
- **Hồ Tĩnh Tâm:** Hồ nước ngọt tự nhiên nằm sâu trong hang, mặt nước phẳng lặng như gương. Đây là nơi Huyền Quy triển khai Ký Ức Thủy Cảnh, chiếu lại quá khứ cho người cần xem.
- **Thiếu Niên Quy Sào:** Khu vực riêng dành cho mười con rùa trẻ nghỉ ngơi và luyện tập, nằm ở nhánh hang phía đông với dòng nước ấm chảy qua liên tục.

## VIII. Kinh Tế (经济)
Kinh tế của Hải Quy Trưởng Lão Hội quy mô nhỏ, chủ yếu dựa trên việc trao đổi thông tin và ký ức lịch sử. Các thế lực lớn như Hải Thần Cung hay Thâm Hải Thám Hiểm Đoàn thỉnh thoảng gửi linh thạch hoặc dược liệu dưỡng sinh để đổi lấy thông tin về địa hình cổ đại, vị trí di tích, hoặc sự kiện lịch sử quan trọng. Ngoài ra, một số tu sĩ tìm đến Tĩnh Tức Hải Vực để thiền định, trả phí bằng linh thạch hoặc thảo dược quý. Thu nhập không lớn nhưng đủ để duy trì cuộc sống giản dị của mười tám thành viên.

## IX. Lịch Sử Tóm Tắt (简史)
Hội hình thành tự nhiên khi các rùa biển già nhất Vô Tận Hải tìm đến nhau để chia sẻ ký ức, không có ngày thành lập chính thức. Huyền Quy, con rùa cổ nhất, trở thành trung tâm quy tụ do tuổi thọ và trí tuệ vượt trội. Trong lịch sử, hội từng cung cấp thông tin chiến lược cho Hải Thần Cung, nhưng bị phớt lờ vì tốc độ truyền đạt quá chậm — một cảnh báo về cuộc tấn công của Hắc Hải Hải Tặc đến nơi khi trận chiến đã kết thúc từ lâu. Huyền Quy là một trong số ít sinh vật còn sống từng chứng kiến trận Đại Chiến cổ đại giữa Hải Thần và Ma Thần, ký ức này được khắc sâu trên mai ông và trở thành bảo vật lịch sử vô giá. Dù bị coi thường vì chậm chạp, hội vẫn kiên nhẫn tồn tại, tin rằng thời gian sẽ chứng minh giá trị của sự bền bỉ.

## X. Giai Thoại & Bí Mật (轶事 与 秘密)
Huyền Quy biết vị trí chính xác của một phong ấn cổ đại dưới đáy biển — nơi giam giữ một sinh vật khổng lồ từ kỷ nguyên trước. Ông chưa từng tiết lộ cho ai vì lo sợ các thế lực sẽ cố giải phong ấn để chiếm đoạt sức mạnh. Mai rùa của Đại Trưởng Lão khắc đầy cổ tự tự nhiên hình thành qua hàng nghìn năm — các học giả và phù văn sư tin rằng đó là ký tự của Thiên Đạo, nhưng chưa ai giải mã được hết. Huyền Quy từng nói một câu mất ba ngày mới xong: "Ta... đã... thấy... biển... này... chết... một... lần... rồi." Câu nói này khiến toàn bộ Vô Tận Hải chấn động, vì nó ám chỉ rằng đại dương hiện tại không phải là đại dương nguyên thủy — một sự kiện hủy diệt đã từng xảy ra và bị lãng quên.

## XI. Quan Hệ Thế Lực (势力关系)
Hải Quy Trưởng Lão Hội giữ thái độ trung lập với hầu hết các thế lực, không chủ động gây thù chuốc oán nhưng cũng không kết minh chính thức với ai. Hải Thần Cung tôn trọng tuổi tác của Huyền Quy nhưng không coi trọng ý kiến của hội vì sự chậm chạp đáng bực mình. Hải Tảo Nông Dân Hội là láng giềng thân thiện nhất, thường xuyên mang tảo linh đến cúng dường. Thâm Hải Thám Hiểm Đoàn là đối tác thương mại quan trọng, sẵn sàng trả giá cao cho thông tin về di tích và địa hình cổ đại.
