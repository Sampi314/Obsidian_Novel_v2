---
type: faction
name: Hỏa Yêu Tàn Đoàn
hantu: 火妖残团
faction_type: Bộ Lạc
alignment: -1
race: Hỏa Yêu
region: Tây Mạc
founded: Không rõ (tàn dư của bộ tộc cổ đại)
founder: Không rõ (bộ tộc nguyên thủy)
emblem: Ngon_Lua_Chap_Chon.png
specialty: Tàn Hỏa Thuật, Nấu chảy đá thành dung nham, Lưu hoàng linh
economy:
- Trao đổi lưu hoàng linh lấy than linh từ Hỏa Diễm Công Phường
- Cung cấp dịch vụ nấu chảy đá cho Thạch Tộc
- Khai thác nhiệt lượng từ miệng núi lửa bán hoạt động
arcs:
  - arc: 1
    status: Suy tàn — bám víu quanh núi lửa bán hoạt động
    rank: Không Xếp Hạng
    leader: Đoàn Trưởng Tàn Viêm
    population: 30
    territory:
      - Vùng núi lửa bán hoạt động phía đông Xích Nham Sơn Mạch
    assets:
      - name: Ngọn Lửa Trung Tâm
        type: Linh Vật
      - name: Hỏa Hạch Truyền Thuyết
        type: Truyền Thuyết
    stats: [20, 15, 10, 30, 15, 5]
    divisions:
      - name: Đoàn Chính
        role: Duy trì ngọn lửa trung tâm và bảo vệ vùng núi lửa
        headcount:
          truong_lao: 1
          chien_binh: 5
          dan_thuong: 24
        members:
          - character: Tàn Viêm
            position: Đoàn Trưởng
            cultivation: Trúc Cơ Sơ Kỳ
          - character: "[Lão Hỏa]"
            position: Trưởng Lão — Người nhớ thời hoàng kim
            cultivation: Luyện Khí Đỉnh Phong
            placeholder: true
          - character: "[Phó Đoàn Giáp]"
            position: Phó Đoàn
            cultivation: Luyện Khí Đỉnh Phong
            placeholder: true
    relationships:
      - faction: Hỏa Diễm Công Phường
        description: Mối quan hệ cộng sinh bí mật — Hỏa Diễm lén mang than linh đến đổi lấy lưu hoàng linh, giúp cả hai bên tồn tại mà không ai ngoài cuộc biết.
        diplomacy:
          lien_minh: 30
          tin: 50
          uy_hiep: 0
          thuong_mai: 60
          on_oan: 0
          le_thuoc: 20
      - faction: Cổ Nham Bộ Lạc
        description: Láng giềng cùng sống trên Xích Nham Sơn Mạch, Cổ Nham thỉnh thoảng cho phép Hỏa Yêu dùng mạch nhiệt gần đỉnh thiêng nhưng không chính thức liên minh.
        diplomacy:
          lien_minh: 10
          tin: 30
          uy_hiep: 0
          thuong_mai: 20
          on_oan: 0
          le_thuoc: 0
      - faction: Thiên Sa Thương Hội
        description: Thương hội không quan tâm đến Hỏa Yêu vì họ quá yếu và nghèo, nhưng đôi khi mua lưu hoàng linh với giá rẻ mạt qua trung gian.
        diplomacy:
          lien_minh: 0
          tin: 10
          uy_hiep: 30
          thuong_mai: 20
          on_oan: 0
          le_thuoc: 0
---

# Hỏa Yêu Tàn Đoàn (火妖残团)

## I. Tổng Quan (总览)
> *"Lửa tàn không phải lửa chết — chỉ cần một tia, ngọn lửa lại bùng."*
> — Tàn Viêm, nói với toàn đoàn mỗi đêm trước khi ngủ

> *"Ta nhớ thời xưa, ngọn lửa của bộ tộc thắp sáng cả chân trời — bây giờ, ngọn lửa trên thân ta chỉ đủ soi mặt mình."*
> — Lão Hỏa, kể cho thế hệ trẻ nghe bên Hỏa Đàn Trung Tâm


Hỏa Yêu Tàn Đoàn là tàn dư cuối cùng của một bộ tộc Hỏa Yêu từng hùng mạnh, nay chỉ còn khoảng ba mươi cá thể yếu ớt bám víu quanh các miệng núi lửa bán hoạt động phía đông Xích Nham Sơn Mạch. Đoàn Trưởng Tàn Viêm — một Hỏa Yêu nhỏ bé với ngọn lửa trên thân chập chờn — dẫn dắt đoàn bằng ý chí kiên cường hơn là sức mạnh thực sự. Triết lý sống của toàn đoàn gói gọn trong câu "Lửa tàn không phải lửa chết — chỉ cần một tia, ngọn lửa lại bùng". Dù biết rõ tộc đang trên bờ diệt vong vì nguồn hỏa linh cạn kiệt, mỗi Hỏa Yêu vẫn giữ ngọn lửa nhỏ bé của mình cháy từng ngày, chờ đợi phép màu có thể không bao giờ đến.

## II. Địa Lý & Tài Nguyên (地理与资源)

Hỏa Yêu Tàn Đoàn cư trú trong vùng núi lửa bán hoạt động phía đông Xích Nham Sơn Mạch, nơi dung nham nguội từ hàng ngàn năm trước tạo thành những hang động nóng bức và suối nước nóng chứa lưu hoàng linh. Địa hình xung quanh là đá đen nứt nẻ, hơi nóng bốc lên từ các kẽ đá, và mùi lưu huỳnh nồng nặc bao phủ cả vùng. Tài nguyên duy nhất có giá trị là nhiệt lượng từ lõi núi lửa — nguồn năng lượng cuối cùng duy trì sự sống cho toàn đoàn. Lưu hoàng linh trong suối nước nóng là mặt hàng trao đổi duy nhất, nhưng trữ lượng đang giảm dần. Nguy cơ lớn nhất là nếu núi lửa ngừng hoạt động hoàn toàn, toàn bộ đoàn sẽ chết vì thiếu hỏa linh trong vòng vài tháng.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)

Văn hóa của Hỏa Yêu Tàn Đoàn thấm đẫm nỗi buồn của một chủng tộc đang dần tắt. Quy tắc tối cao là không bao giờ để ngọn lửa trung tâm — ngọn lửa chung duy nhất của cả đoàn — tắt đi, vì đó là biểu tượng sống còn và niềm hy vọng cuối cùng. Mỗi Hỏa Yêu khi sinh ra phải nuốt một viên than linh để "giữ lửa" bên trong cơ thể, nghi thức này gọi là Hỏa Chủng Lễ. Đoàn không thờ thần linh nào cụ thể, nhưng tôn kính ngọn lửa như tổ tiên — họ tin rằng mỗi ngọn lửa tắt đi là một linh hồn Hỏa Yêu mất vĩnh viễn. Lão Hỏa, cá thể già nhất trong đoàn, thường kể cho thế hệ trẻ nghe về thời hoàng kim khi bộ tộc thắp sáng cả sa mạc, nhưng ngày càng ít Hỏa Yêu trẻ còn đủ kiên nhẫn lắng nghe.

## IV. Cơ Cấu Tổ Chức (组织结构)

Tổ chức của Hỏa Yêu Tàn Đoàn đơn giản đến mức thương tâm. Đoàn Trưởng Tàn Viêm đứng đầu, ngọn lửa trên thân ông là ngọn sáng nhất trong đoàn — dù chỉ bằng ngọn nến. Hai Phó Đoàn tương đương Luyện Khí Đỉnh Phong hỗ trợ canh giữ ngọn lửa trung tâm và phân chia nhiệt lượng cho các thành viên yếu nhất. Lão Hỏa giữ vai trò trưởng lão duy nhất, không còn sức chiến đấu nhưng là kho tàng ký ức sống về lịch sử bộ tộc. Năm Hỏa Yêu khỏe nhất đảm nhiệm vai trò chiến binh, tuần tra vùng núi lửa và xua đuổi sinh vật xâm nhập. Hai mươi bốn cá thể còn lại là dân thường, ngọn lửa mờ nhạt, nhiều cá thể phải quây quần sát ngọn lửa trung tâm suốt ngày đêm để không bị tắt.

## V. Công Pháp & Trận Pháp (功法与阵法)

Hỏa Yêu Tàn Đoàn sở hữu Tàn Hỏa Thuật — kỹ thuật tuyệt vọng cho phép dồn toàn bộ lửa lực vào một đòn duy nhất, cực kỳ mạnh mẽ trong khoảnh khắc nhưng sau đó người sử dụng kiệt sức hoàn toàn, thậm chí có nguy cơ tắt vĩnh viễn. Ngoài ra, khi hợp lực mười Hỏa Yêu có thể tạo ra một bức tường lửa tạm thời đủ để chặn kẻ tấn công trong vài phút. Kỹ năng quý giá nhất của đoàn là khả năng nấu chảy đá thành dung nham tạm thời — kỹ thuật mà Thạch Tộc rất cần nhưng không tự làm được, và đây cũng là lý do Thạch Tộc đôi khi tìm đến Hỏa Yêu để nhờ giúp đỡ. Tuy nhiên, mỗi lần sử dụng kỹ năng này đều tiêu hao hỏa linh đáng kể, khiến Tàn Viêm phải cân nhắc rất kỹ trước khi đồng ý.

## VI. Đặc Sản Môn Phái (门派特产)

- **Lưu Hoàng Linh:** Khoáng chất quý kết tinh trong suối nước nóng núi lửa, có tác dụng xúc tác trong luyện đan hỏa hệ và gia cố pháp khí chống nhiệt, là mặt hàng trao đổi duy nhất của đoàn.
- **Than Linh:** Viên than đặc biệt chứa hỏa linh cô đọng, Hỏa Yêu dùng để giữ lửa bên trong cơ thể, cũng có thể dùng làm nhiên liệu cho lò luyện đan cấp cao.
- **Dung Nham Đúc:** Dịch vụ nấu chảy đá thành dung nham theo yêu cầu, phục vụ Thạch Tộc cần tạo hình hoặc hàn gắn thân xác bằng đá.

## VII. Cơ Sở Hạ Tầng (基础设施)

- **Hỏa Đàn Trung Tâm:** Bệ đá tự nhiên giữa hang lớn nhất, nơi ngọn lửa trung tâm cháy không ngừng. Mọi Hỏa Yêu luân phiên tiếp lửa lực để duy trì.
- **Hang Lưu Hoàng:** Hệ thống hang nhỏ chứa suối nước nóng lưu hoàng linh, nơi thu hoạch khoáng chất trao đổi.
- **Ổ Hỏa Yêu:** Các hốc đá ấm dọc theo mạch nhiệt, mỗi Hỏa Yêu chọn một hốc gần nguồn nhiệt nhất có thể.

## VIII. Kinh Tế (经济)

Nền kinh tế của Hỏa Yêu Tàn Đoàn gần như không tồn tại theo nghĩa thông thường. Mặt hàng trao đổi chính là lưu hoàng linh, đổi lấy than linh từ Hỏa Diễm Công Phường qua mối quan hệ bí mật giữa hai bên. Đôi khi đoàn nhận yêu cầu nấu chảy đá từ Thạch Tộc, đổi lại thực phẩm khoáng chất hoặc nham thạch đặc biệt. Thiên Sa Thương Hội thỉnh thoảng mua lưu hoàng linh qua trung gian với giá rẻ mạt, nhưng Tàn Viêm không có vị thế để đàm phán. Toàn bộ thu nhập chỉ đủ để duy trì sự tồn tại ở mức tối thiểu — không có tích lũy, không có phát triển.

## IX. Lịch Sử Tóm Tắt (简史)

Hỏa Yêu Tàn Đoàn là tàn dư cuối cùng của một bộ tộc Hỏa Yêu hùng mạnh từng cai quản toàn bộ vùng núi lửa Xích Nham Sơn Mạch. Thời hoàng kim, ngọn lửa của họ chiếu rọi khắp Thiên Sa Thương Đạo suốt đêm, và Hoàng Sa Cổ Quốc từng mời họ thắp sáng các con đường sa mạc. Khi núi lửa chính ngừng hoạt động cách đây hàng trăm năm, nguồn hỏa linh cạn kiệt dần, bộ tộc suy tàn nhanh chóng. Những cá thể mạnh nhất rời đi tìm nguồn lửa mới và không bao giờ trở lại. Những cá thể còn lại quá yếu để di cư, chỉ có thể bám víu quanh các miệng núi lửa bán hoạt động cuối cùng. Tàn Viêm trở thành đoàn trưởng một cách tự nhiên khi ngọn lửa trên thân ông là ngọn sáng nhất — một danh hiệu buồn hơn vinh quang.

## X. Giai Thoại & Bí Mật (轶事与秘密)

Tàn Viêm tin rằng sâu trong lõi núi lửa chính — ngọn núi đã ngừng phun trào — vẫn còn "Hỏa Hạch", nguồn hỏa linh nguyên thủy có thể hồi phục toàn bộ tộc về thời hoàng kim. Nhưng đoàn không đủ sức đào xuống lõi núi, và Cổ Nham Bộ Lạc kiểm soát vùng đỉnh thiêng nơi miệng núi lửa tọa lạc. Lão Hỏa kể rằng thời xưa, bộ tộc sở hữu một bí thuật gọi là "Hỏa Nguyên Quy" — cho phép mọi Hỏa Yêu dồn lửa lực thành một ngọn lửa duy nhất mạnh đến mức thiêu tan núi đá, nhưng bí thuật đã thất truyền cùng với thế hệ trưởng lão cuối cùng. Mối quan hệ bí mật với Hỏa Diễm Công Phường là sợi dây sinh tồn mong manh nhất — nếu Thiên Sa Thương Hội phát hiện, cả hai bên đều gặp rắc rối.

## XI. Quan Hệ Thế Lực (势力关系)

- **Hỏa Diễm Công Phường:** Đối tác cộng sinh bí mật và quan trọng nhất. Hỏa Diễm lén mang than linh đến đổi lấy lưu hoàng linh, giúp cả hai tồn tại. Mối quan hệ này được giữ kín tuyệt đối vì Thiên Sa Thương Hội không cho phép giao dịch ngoài luồng trên lãnh thổ thương đạo.
- **Cổ Nham Bộ Lạc:** Quan hệ trung lập thiên tích cực. Cổ Nham thỉnh thoảng cho phép Hỏa Yêu tiếp cận mạch nhiệt gần đỉnh thiêng nhưng không chính thức liên minh, và cũng không cho phép đào xuống lõi núi lửa — nơi Tàn Viêm tin có Hỏa Hạch.
- **Thiên Sa Thương Hội:** Thương hội hầu như không quan tâm đến sự tồn tại của Hỏa Yêu Tàn Đoàn vì họ quá yếu và nghèo để có giá trị thương mại. Tuy nhiên, nếu phát hiện mối giao dịch bí mật với Hỏa Diễm, thương hội sẽ can thiệp vì lý do kiểm soát thương mại.

Một chi tiết nhỏ nhưng đau lòng: Hỏa Yêu khi chết không để lại xác — ngọn lửa trên thân tắt, cơ thể hóa thành tro trong khoảnh khắc. Tàn Viêm giữ tro của mỗi thành viên đã mất trong một chiếc bình đá nhỏ đặt quanh Hỏa Đàn Trung Tâm, và mỗi đêm khi tiếp lửa cho ngọn lửa trung tâm, ông đều nhìn những chiếc bình và thì thầm: "Chờ thêm chút nữa — ta sẽ tìm thấy Hỏa Hạch."


