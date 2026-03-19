---
type: faction
name: Địa Tâm Thám Hiểm Đội
hantu: 地心探险队
faction_type: Hội
alignment: 3
race: Thạch Tộc
region: Tây Mạc
founded: Năm Khởi Nguyên 99.985
founder: Thâm Nham
emblem: Cuoc_Dao_Va_Hang_Sau.png
specialty: Thám hiểm hang ngầm, Thạch Dung Thuật, Khoáng vật học thâm tầng
economy:
- Bán khoáng vật hiếm tìm được ở tầng sâu
- Nhận hợp đồng thăm dò địa chất cho các tông môn
- Trao đổi nham thạch nguyên thủy với Hỏa Diễm Công Phường
arcs:
  - arc: 1
    status: Hoạt động — thăm dò tầng sâu Xích Nham Sơn Mạch
    rank: Không Xếp Hạng
    leader: Đội Trưởng Thâm Nham
    population: 20
    territory:
      - Hệ thống hang ngầm sâu nhất Xích Nham Sơn Mạch
    assets:
      - name: Bản Đồ Hang Ngầm Tam Tầng
        type: Tư Liệu
      - name: Khoáng Vật Phát Quang Thâm Tầng
        type: Nguyên Liệu
    stats: [30, 40, 15, 20, 25, 10]
    divisions:
      - name: Đội Thám Hiểm Chính
        role: Tiên phong đào sâu và khảo sát cấu trúc hang ngầm
        headcount:
          hoi_truong: 1
          pho_hoi_truong: 2
          thanh_vien: 15
          tong_quan: 2
        members:
          - character: Thâm Nham
            position: Đội Trưởng
            cultivation: Trúc Cơ Viên Mãn
          - character: "[Phó Đội Giáp]"
            position: Phó Đội — Bản Đồ
            cultivation: Trúc Cơ Trung Kỳ
            placeholder: true
          - character: "[Phó Đội Ất]"
            position: Phó Đội — An Toàn
            cultivation: Trúc Cơ Trung Kỳ
            placeholder: true
    relationships:
      - faction: Cổ Nham Bộ Lạc
        description: Mâu thuẫn tư tưởng nghiêm trọng — Cổ Nham coi việc đào sâu là xúc phạm Nham Thần, đã từ chối thẳng khi Thâm Nham xin phép khoan dưới đỉnh thiêng.
        diplomacy:
          lien_minh: -30
          tin: -40
          uy_hiep: 0
          thuong_mai: 10
          on_oan: -30
          le_thuoc: 0
      - faction: Hỏa Diễm Công Phường
        description: Đối tác trao đổi — Địa Tâm cung cấp nham thạch nguyên thủy, Hỏa Diễm đổi lại dụng cụ đào hầm bằng thép.
        diplomacy:
          lien_minh: 20
          tin: 40
          uy_hiep: 0
          thuong_mai: 60
          on_oan: 0
          le_thuoc: 0
      - faction: Cổ Sa Yêu Tộc
        description: Quan hệ mờ ám — Cổ Sa Yêu Tộc tỏ ra im lặng bất thường khi nghe tin về bức tường đá nhân tạo, có thể biết bí mật đằng sau.
        diplomacy:
          lien_minh: 0
          tin: -20
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 0
---

# Địa Tâm Thám Hiểm Đội (地心探险队)

## I. Tổng Quan (总览)
Địa Tâm Thám Hiểm Đội là một nhóm nhỏ gồm hai mươi Thạch Tộc trẻ tuổi chuyên thám hiểm tầng sâu nhất của Xích Nham Sơn Mạch, nơi ánh sáng không bao giờ chạm tới và nhiệt độ tăng dần theo từng tầng đá. Đứng đầu bởi Đội Trưởng Thâm Nham — một Thạch Tộc gan dạ với thân xác bằng hắc diệu thạch cứng — đội hoạt động theo tôn chỉ "Cội nguồn của Thạch Tộc nằm ở nơi sâu nhất — phải đào xuống mới tìm được câu trả lời". Dù quy mô nhỏ bé và đã mất ba thành viên trong các chuyến thám hiểm, Địa Tâm Thám Hiểm Đội vẫn kiên trì đào sâu hơn, bởi mỗi tầng mới đều mang đến những phát hiện kỳ lạ và nguy hiểm chưa từng thấy.

## II. Địa Lý & Tài Nguyên (地理与资源)
Đội hoạt động trong hệ thống hang động sâu nhất Xích Nham Sơn Mạch, một mê cung ngầm chằng chịt nơi mà ngay cả Cổ Nham Bộ Lạc cũng không dám bước chân tới. Hang ngầm trải dài theo chiều dọc qua nhiều tầng đá, nhiệt độ tăng dần theo độ sâu do gần mạch nham thạch nóng chảy vẫn còn hoạt động. Ở các tầng sâu nhất, đội phát hiện những loại khoáng vật chưa từng thấy trên bề mặt — đá phát quang tự nhiên, nham thạch nguyên thủy chứa linh lực đậm đặc, và những tinh thể kỳ lạ hình thành dưới áp suất cực cao. Tuy nhiên, nguy hiểm luôn rình rập: sập hầm bất ngờ, dòng nham thạch nóng chảy chuyển hướng không báo trước, và đặc biệt là những sinh vật ngầm chưa được phân loại ẩn nấp trong bóng tối.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
Khác với Cổ Nham Bộ Lạc thờ phụng Nham Thần và cấm khai thác đá thiêng, Địa Tâm Thám Hiểm Đội theo đuổi triết lý thực chứng: chỉ tin vào những gì tận mắt nhìn thấy dưới lòng đất. Thâm Nham thường nói "Nham Thần có thật hay không, đào xuống sẽ biết". Đội có quy tắc sinh tử nghiêm ngặt — không bao giờ đi một mình, luôn di chuyển theo nhóm ít nhất ba người. Trước khi đào sâu hơn một tầng mới, thành viên gõ nhịp đặc biệt vào vách đá và lắng nghe: nếu có tiếng vọng lại theo mẫu nhất định thì dừng ngay, vì điều đó báo hiệu cấu trúc đá phía trước không ổn định. Phong tục này đã cứu mạng đội nhiều lần, nhưng cũng có ba lần tiếng vọng đến quá chậm.

## IV. Cơ Cấu Tổ Chức (组织结构)
Đội chỉ gồm hai mươi thành viên, tổ chức đơn giản nhưng kỷ luật chặt chẽ. Đội Trưởng Thâm Nham nắm quyền quyết định mọi chuyến thám hiểm, từ hướng đào đến thời điểm rút lui. Hai Phó Đội tương đương Trúc Cơ Trung Kỳ chia nhau phụ trách bản đồ hang ngầm và an toàn — một người vẽ lại cấu trúc hang sau mỗi chuyến đi, người kia kiểm tra độ ổn định của vách đá trước khi đội tiến sâu. Mười lăm thành viên còn lại ở cấp Luyện Khí đến Trúc Cơ Sơ Kỳ, trong đó có hai Thạch Tộc đặc biệt chuyên "nghe đá" — cảm nhận cấu trúc bên trong qua rung động, đóng vai trò tai mắt cho toàn đội. Hai tổng quản phụ trách hậu cần và vận chuyển khoáng vật thu được lên bề mặt.

## V. Công Pháp & Trận Pháp (功法与阵法)
Địa Tâm Thám Hiểm Đội không tu luyện công pháp chiến đấu mà tập trung vào các kỹ thuật sinh tồn dưới lòng đất. Thạch Dung Thuật là kỹ thuật cốt lõi, cho phép thành viên hòa nhập thân xác vào đá để di chuyển qua tường đá mỏng — kỹ năng bẩm sinh của Thạch Tộc nhưng được Thâm Nham tinh chỉnh thành phương pháp có hệ thống. Đội sử dụng cảm nhận rung động trong lòng đất để tránh sập hầm và dò tìm mạch khoáng, kết hợp với khoáng vật phát quang tìm được ở tầng sâu để chiếu sáng đường đi. Khi gặp nguy hiểm, toàn đội có thể đồng loạt hòa vào vách đá ẩn náu, chờ nguy cơ qua đi rồi mới tiếp tục.

## VI. Đặc Sản Môn Phái (门派特产)
- **Khoáng Vật Phát Quang Thâm Tầng:** Loại đá tự phát sáng tìm được ở độ sâu kỷ lục, ánh sáng dịu nhẹ nhưng bền bỉ hàng chục năm, rất được các thương đoàn đi đêm ưa chuộng.
- **Bản Đồ Hang Ngầm Tam Tầng:** Bộ bản đồ chi tiết nhất về hệ thống hang động Xích Nham Sơn Mạch, vẽ trên phiến nham thạch mỏng, ghi chú cả vùng nguy hiểm và mạch khoáng.
- **Nham Thạch Nguyên Thủy:** Loại đá chỉ tồn tại ở tầng sâu nhất, chứa linh lực đậm đặc và cổ xưa, là nguyên liệu quý mà Hỏa Diễm Công Phường rất muốn có để rèn pháp khí đặc biệt.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Doanh Trại Tầng Một:** Căn cứ chính đặt ở tầng hang đầu tiên, nơi an toàn nhất, dùng làm kho chứa khoáng vật và chỗ nghỉ ngơi giữa các chuyến thám hiểm.
- **Trạm Trung Chuyển Tầng Hai:** Điểm dừng chân tạm thời ở độ sâu trung bình, được gia cố bằng nham thạch cứng để chống sập, có trữ nước và thực phẩm khô.
- **Hệ Thống Dây Dẫn Đường:** Dây linh bện từ sợi khoáng vật, căng dọc theo các tuyến hang đã khám phá, giúp thành viên không bị lạc trong mê cung ngầm.

## VIII. Kinh Tế (经济)
Kinh tế của Địa Tâm Thám Hiểm Đội dựa hoàn toàn vào những gì đào được từ lòng đất. Khoáng vật phát quang thâm tầng là mặt hàng bán chạy nhất, được thương đoàn trên Thiên Sa Thương Đạo thu mua đều đặn. Nham thạch nguyên thủy thì trao đổi trực tiếp với Hỏa Diễm Công Phường để lấy dụng cụ đào hầm và thực phẩm. Đôi khi đội nhận hợp đồng thăm dò địa chất từ các tông môn nhỏ muốn biết có mỏ khoáng dưới lãnh địa hay không. Thu nhập không ổn định nhưng đủ duy trì hoạt động, và Thâm Nham cũng không quan tâm đến tiền bạc — với ông, mỗi chuyến thám hiểm là phần thưởng tự thân.

## IX. Lịch Sử Tóm Tắt (简史)
Thâm Nham sinh ra trong Cổ Nham Bộ Lạc nhưng luôn bị ám ảnh bởi câu hỏi mà các trưởng lão không muốn trả lời: Thạch Tộc đến từ đâu? Cổ Nham nói từ Nham Thần, nhưng Thâm Nham muốn tự tìm câu trả lời bằng chứng cứ cụ thể. Ông tập hợp những Thạch Tộc trẻ cùng chí hướng, lặng lẽ rời bộ lạc và đào sâu vào lòng Xích Nham Sơn Mạch. Mỗi lần đi sâu hơn, đội phát hiện những cấu trúc địa chất kỳ lạ hơn — đá có vân xoắn ốc nhân tạo, khoáng vật không tuân theo quy luật tự nhiên, và tiếng vọng bất thường từ phía sâu hơn nữa. Đã mất ba thành viên trong các chuyến thám hiểm vì sập hầm và sinh vật ngầm tấn công, nhưng Thâm Nham không từ bỏ, vì ông tin rằng câu trả lời nằm ngay phía sau bức tường đá nhân tạo mà đội phát hiện ở độ sâu kỷ lục.

## X. Giai Thoại & Bí Mật (轶事与秘密)
Ở độ sâu kỷ lục, đội phát hiện một bức tường đá nhân tạo khổng lồ — bề mặt nhẵn bóng hoàn hảo, không thuộc bất kỳ loại nham thạch nào đã biết, và không ai trong đội phá nổi dù dùng hết sức. Thâm Nham khẳng định ông nghe thấy "nhịp đập" đều đặn từ phía sau bức tường, như thể có thứ gì đó đang sống và hô hấp ở sâu hơn nữa. Khi tin tức về bức tường lan đến tai Cổ Sa Yêu Tộc, phản ứng của họ là im lặng bất thường — không tò mò, không phủ nhận, chỉ im lặng, như thể đã biết từ lâu thứ gì đằng sau đó nhưng không muốn ai đến gần. Thâm Nham nghi ngờ bức tường có liên quan đến nguồn gốc thực sự của Thạch Tộc, và ông đang bí mật tìm cách liên lạc với Cổ Tích Thám Hiểm Đoàn để có thêm nhân lực và kiến thức giải mã cổ văn trên bề mặt tường.

## XI. Quan Hệ Thế Lực (势力关系)
- **Cổ Nham Bộ Lạc:** Mâu thuẫn tư tưởng sâu sắc. Cổ Nham coi việc đào sâu vào lòng đất là xúc phạm Nham Thần, đã từ chối thẳng khi Thâm Nham xin phép đào dưới đỉnh thiêng. Hai bên không thù địch nhưng quan hệ lạnh nhạt, và Đại Tế Tư Bàn Thạch nhiều lần cảnh báo Thâm Nham rằng "đào quá sâu sẽ đánh thức thứ không nên đánh thức".
- **Hỏa Diễm Công Phường:** Đối tác trao đổi ổn định. Địa Tâm cung cấp nham thạch nguyên thủy — nguyên liệu rèn pháp khí mà Hỏa Diễm không tìm được ở nơi khác — đổi lại dụng cụ đào hầm bằng thép gia cố và lương thực. Mối quan hệ đôi bên cùng có lợi, tuy không thân mật.
- **Cổ Sa Yêu Tộc:** Quan hệ mờ ám và đầy nghi hoặc. Cổ Sa Yêu Tộc tỏ ra biết nhiều hơn những gì họ nói về bức tường đá nhân tạo mà Địa Tâm phát hiện. Thâm Nham muốn tiếp cận nhưng chưa tìm được cách, vì Yêu Tộc cổ đại này không dễ dàng gặp mặt bất kỳ ai.
