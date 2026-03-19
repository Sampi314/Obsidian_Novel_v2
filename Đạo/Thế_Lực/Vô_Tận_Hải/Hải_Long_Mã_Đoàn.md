---
type: faction
name: Hải Long Mã Đoàn
hantu: 海龙马团
faction_type: Quân Đoàn
alignment: 1
race: Hải Tộc (Á Long, Long Tộc huyết mạch thấp)
region: Vô Tận Hải
founded: Từ khi Long Cung thành lập
founder: Không rõ (do Long Cung chỉ định)
emblem: Hai_Long_Ma_Doan.png
specialty: Thuần hóa Hải Long Mã, Vận chuyển biển sâu, Chăm sóc linh thú
economy:
- Cung cấp dịch vụ vận chuyển cho Long Cung
- Nhân giống và thuần hóa Hải Long Mã
arcs:
  - arc: 1
    status: Phục dịch Long Cung
    rank: Không Xếp Hạng
    leader: Mã Phu Trưởng Lão Hoàng Lân
    population: 60
    territory:
      - Chuồng Ngựa Biển (rìa lãnh thổ Long Cung)
    assets:
      - name: Đồng Cỏ Biển (Tảo biển lớn)
        type: Tài Nguyên
      - name: Hải Long Mã Bạc Mao
        type: Pháp Bảo
    stats: [10, 10, 5, 60, 10, 5]
    divisions:
      - name: Mã Phu Đội
        role: Chăm sóc, thuần hóa và điều khiển đàn Hải Long Mã phục vụ Long Cung
        headcount:
          tuong: 1
          uy: 0
          binh: 10
        members:
          - character: Hoàng Lân
            position: Mã Phu Trưởng
            cultivation: Trúc Cơ Trung Kỳ
          - character: "[Mã Phu Phó]"
            position: Phó Đội Trưởng
            cultivation: Luyện Khí Viên Mãn
            placeholder: true
    relationships:
      - faction: Long Cung
        description: Hoàn toàn lệ thuộc. Hải Long Mã Đoàn tồn tại chỉ để phục vụ Long Cung, không có quyền tự quyết hay tài nguyên riêng. Bị coi là tầng đáy xã hội Long Tộc.
        diplomacy:
          lien_minh: 10
          tin: 20
          uy_hiep: 80
          thuong_mai: 0
          on_oan: -30
          le_thuoc: 100
      - faction: Tạp Huyết Long Đàn
        description: Cùng cảnh ngộ bị Long Cung coi thường vì huyết mạch thấp. Có sự đồng cảm ngầm nhưng mã phu không dám công khai liên lạc vì sợ bị trừng phạt.
        diplomacy:
          lien_minh: 10
          tin: 20
          uy_hiep: 0
          thuong_mai: 5
          on_oan: 15
          le_thuoc: 0
      - faction: Ấu Long Học Viện
        description: Thỉnh thoảng Hải Long Mã Đoàn cung cấp ngựa biển cho học viện dùng trong huấn luyện, là dịp hiếm hoi được đối xử tương đối tử tế.
        diplomacy:
          lien_minh: 15
          tin: 25
          uy_hiep: 10
          thuong_mai: 20
          on_oan: 0
          le_thuoc: 30
---

# HẢI LONG MÃ ĐOÀN (海龙马团)

> *"Ba trăm năm ta chăm ngựa cho Long Cung, chưa một Chân Long nào nói 'cảm ơn.' Nhưng Ngân Phong hiểu — mỗi sáng nó dụi đầu vào tay ta, thế là đủ."*
> — Hoàng Lân, Mã Phu Trưởng, thì thầm với đàn ngựa trong đêm khuya

## I. Tổng Quan (总览)
Hải Long Mã Đoàn là đơn vị chăm sóc và thuần hóa Hải Long Mã — giống lai giữa Long Tộc cấp thấp và ngựa biển linh — phục vụ nhu cầu di chuyển và vận chuyển của Long Cung. Dẫn đầu bởi Mã Phu Trưởng Lão Hoàng Lân, một Á Long già đã trung thành phục vụ Long Cung suốt hơn ba trăm năm mà chưa một lần được Chân Long nói lời cảm ơn. Với chỉ mười mã phu và năm mươi con Hải Long Mã, đây là thế lực nhỏ nhất và bị coi thường nhất trong hệ thống Long Cung, nhưng lại đóng vai trò không thể thiếu — nếu mã phu đình công, các Chân Long quý tộc sẽ phải tự mình di chuyển. Sự tồn tại của Hải Long Mã Đoàn là bức tranh thu nhỏ về phân tầng xã hội trong Long Cung: huyết mạch quyết định số phận, và những ai sinh ra ở đáy thì mãi mãi ở đáy.

## II. Địa Lý & Tài Nguyên (地理 与 资源)
Chuồng Ngựa Biển nằm ở rìa ngoài cùng lãnh thổ Long Cung — vùng biển mà linh khí dư thừa nhưng không Chân Long nào thèm ở vì vị trí hẻo lánh và "mùi ngựa," người trong Long Cung gọi nơi này là Tanh Vực. Phía đông là Tảo Dã — đồng cỏ biển rộng lớn gồm các loại tảo biển lớn dùng làm thức ăn cho Hải Long Mã, trong đó có giống Thanh Mao Tảo mọc cao đến ba trượng, uốn lượn theo hải lưu như đồng lúa trên cạn. Phía tây là Hàn Nham Tường — bức tường đá tự nhiên ngăn cách chuồng ngựa với khu vực sinh sống của Chân Long, vừa là ranh giới địa lý vừa là ranh giới giai cấp. Ngoài đồng cỏ biển, khu vực không có bất kỳ tài nguyên đáng kể nào — mọi vật tư từ linh thạch đến thức ăn cho mã phu đều phụ thuộc hoàn toàn vào Long Cung phân phát, luôn ở mức tối thiểu. Chuồng nuôi bốc mùi tanh nồng đặc trưng, khiến các Chân Long không bao giờ đích thân đến gần — chỉ sai người gọi mã phu mang ngựa đến nơi cần.

## III. Văn Hóa & Tín Ngưỡng (文化 与 信仰)
Hải Long Mã là giống lai đặc biệt — hình dáng ngựa nhưng có vảy rồng mờ nhạt trên thân, bờm là các sợi tảo linh phát sáng nhạt, bốn chân có màng bơi và đuôi mang hình đuôi cá. Chúng bị Long Cung coi như gia súc, dùng để kéo xe cho Chân Long đi lại giữa các cung điện dưới đáy biển. Mã phu đều là Á Long hoặc Long Tộc huyết mạch cực thấp — bị phân công làm công việc "hạ đẳng" mà không ai trong Long Cung muốn đảm nhận. Văn hóa trong đoàn mang đậm sự cam chịu và nhẫn nhục, nhưng cũng ẩn chứa lòng tự trọng bị đè nén. Hoàng Lân dạy các mã phu rằng "chăm sóc sinh linh là việc cao quý, dù thế gian không công nhận" — triết lý giúp họ duy trì phẩm giá trong hoàn cảnh bị khinh miệt. Mỗi khi có ngựa biển chết, mã phu tổ chức "Tống Mã Lễ" giản dị — thả xác ngựa vào dòng hải lưu ấm hướng nam, hát bài "Tảo Dã Ca" mà Hoàng Lân sáng tác, giai điệu buồn vang vọng trong đêm biển. Chân Long không bao giờ biết đến nghi lễ này, và nếu biết có lẽ sẽ cười nhạo.

## IV. Cơ Cấu Tổ Chức (组织结构)
Cấu trúc cực kỳ đơn giản, phản ánh quy mô nhỏ bé của đoàn. Hoàng Lân là Mã Phu Trưởng, chịu trách nhiệm toàn bộ công việc thuần hóa, chăm sóc và điều phối Hải Long Mã cho Long Cung, đồng thời là người duy nhất trong đoàn có tu vi đạt Trúc Cơ. Mã Phu Phó — một Á Long trẻ tên Hoàng Vân, cháu gọi Hoàng Lân bằng ông — phụ trách quản lý kho tảo và phân công ca trực. Bên dưới là tám mã phu, toàn bộ ở cảnh giới Luyện Khí hoặc thấp hơn, chia nhau chăm sóc năm mươi con Hải Long Mã, mỗi người phụ trách năm đến sáu con. Công việc đơn điệu, lặp đi lặp lại mỗi ngày: cho ăn, tắm rửa, thuần hóa ngựa mới, và mang ngựa đến khi Chân Long có nhu cầu — bất kể giờ giấc. Mã phu không có cơ hội thăng tiến hay tu luyện chính thức — mọi tài nguyên tu luyện của Long Cung đều dành cho Chân Long và Giao Long, không bao giờ phân bổ đến tầng đáy.

## V. Công Pháp & Trận Pháp (功法 与 阵法)
Hải Long Mã Đoàn không sở hữu bất kỳ công pháp chiến đấu nào — Long Cung không cho phép và cũng không cần mã phu biết đánh. Kỹ năng duy nhất đáng kể là "Nhu Long Thuần Thú Thuật" mà Hoàng Lân tự mày mò phát triển qua ba trăm năm kinh nghiệm, cho phép giao tiếp và kiểm soát đàn Hải Long Mã thông qua sóng thần thức nhẹ hòa quyện với âm thanh trầm — một dạng kết hợp giữa thần thức và ca thuật mà không tông phái nào dạy. Đây không phải pháp thuật cao cấp, mà là kỹ thuật tích lũy qua kinh nghiệm thực tế, hiệu quả bất ngờ đến mức ngay cả Thuần Thú Sư chuyên nghiệp cũng khó bắt chước. Ngoài ra, Hoàng Lân phát triển được khả năng cảm nhận tâm trạng và sức khỏe của Hải Long Mã qua biểu hiện nhỏ nhất — ánh mắt, cách vỗ đuôi, nhịp thở — một năng lực mà không ai khác trong Long Cung có được, nhưng cũng không ai coi trọng. Mã phu trẻ Hoàng Vân gần đây bắt đầu lén tập "Cơ Bản Long Tộc Thể Luyện Công" — bộ công pháp cấp thấp nhặt được từ một cuốn sách vứt đi trong bãi rác Long Cung.

## VI. Đặc Sản Môn Phái (门派特产)
Sản phẩm chính của Hải Long Mã Đoàn là chính bản thân Hải Long Mã — những con ngựa biển đã được thuần hóa, có thể kéo xe và chở người di chuyển dưới đáy biển với tốc độ nhanh hơn bơi thông thường gấp năm lần. **Ngân Phong** — con Hải Long Mã lông bạc nhanh nhất đàn — được coi là "bảo mã" của Long Cung, các Chân Long tranh nhau sử dụng mỗi khi cần di chuyển gấp. **Long Mã Phân** tuy bốc mùi nhưng là phân bón tuyệt vời cho tảo biển và san hô, chứa vi lượng long khí giúp thực vật biển phát triển mạnh mẽ; thỉnh thoảng được một số Hải Tộc nông nghiệp như Hải Tảo Nông Dân Hội tìm mua. **Nguyệt Quang Ti** — lông bờm Hải Long Mã, những sợi tảo linh phát sáng — có thể dùng làm nguyên liệu dệt vải dạ quang cấp thấp hoặc bện thành dây buộc pháp khí có tính kháng nước, nhưng sản lượng quá ít để trở thành thương phẩm đáng kể.

## VII. Cơ Sở Hạ Tầng (基础设施)
Chuồng Ngựa Biển là toàn bộ cơ sở hạ tầng của đoàn — một khu vực rộng được rào bằng san hô cứng và trận pháp đơn giản, chia thành năm chuồng lớn mang tên Giáp, Ất, Bính, Đinh, Mậu, mỗi chuồng chứa mười con Hải Long Mã. **Mã Phu Xá** — khu ở của mã phu nằm liền kề, gồm mười phòng nhỏ xây bằng đá biển, chật chội và ẩm ướt nhưng được Hoàng Lân trang trí bằng vỏ sò và san hô nhỏ, tạo chút ấm cúng trong hoàn cảnh tồi tàn. **Thuần Mã Trường** — bãi huấn luyện ngoài trời dùng để thuần hóa Hải Long Mã mới sinh, đáy lót cát mịn để ngựa con không bị thương khi ngã. **Tảo Khố** — kho tảo biển dự trữ đủ thức ăn cho đàn ngựa trong một tháng, quản lý bởi Hoàng Vân. Tất cả đều thô sơ, tối giản, và được duy trì bằng sức lao động của mã phu thay vì pháp thuật — Long Cung không lãng phí linh thạch cho "chuồng ngựa."

## VIII. Kinh Tế (经济)
Hải Long Mã Đoàn không có kinh tế độc lập. Toàn bộ chi phí hoạt động — từ thức ăn cho ngựa đến lương thực cho mã phu — đều do Long Cung cung cấp, ở mức tối thiểu vừa đủ để duy trì sự sống và hoạt động, không hơn không kém. Mã phu không nhận bổng lộc hay linh thạch, chỉ được cấp phát thực phẩm và nơi ở — điều kiện sống thua cả tù nhân trong ngục Long Cung. Đổi lại, đoàn phải đảm bảo Hải Long Mã luôn sẵn sàng phục vụ mọi nhu cầu di chuyển của Chân Long, bất kể ngày đêm, bất kể thời tiết. Thỉnh thoảng Hoàng Lân bán lén một ít Long Mã Phân cho nông dân biển qua trung gian tại Tảo Dã, thu được chút linh thạch lẻ để mua thuốc chữa thương cho mã phu bị thương — bốn mươi ba linh thạch hạ phẩm tích lũy suốt năm năm, đó là toàn bộ "quỹ đen" của đoàn. Long Cung không biết hoặc không thèm quan tâm đến hoạt động này.

## IX. Lịch Sử Tóm Tắt (简史)
Hải Long Mã Đoàn tồn tại từ thuở khai thiên lập cung của Long Cung, luôn ở tầng đáy xã hội Long Tộc suốt hàng vạn năm. Không ai nhớ đội trưởng đầu tiên là ai, cũng không có sử sách ghi lại lịch sử của đoàn — bởi trong mắt Long Cung, mã phu không xứng đáng được ghi vào sử. Hoàng Lân đã phục vụ hơn ba trăm năm, chứng kiến ba đời Long Vương, vô số cuộc tranh giành quyền lực, và biết bao biến cố lớn nhỏ — từ "Loạn Giao Long" hai trăm năm trước đến cuộc thanh trừng Tạp Huyết Long Đàn gần đây. Từng có một mã phu trẻ tên Thanh Lân — em trai của Hoàng Lân — cố gắng tu luyện vượt bậc, đạt được Trúc Cơ Sơ Kỳ, nhưng bị một Chân Long tên Xích Viêm đánh trọng thương vì "mã phu hạ đẳng không biết phận mình." Thanh Lân từ đó tàn phế, sống nốt quãng đời trong chuồng ngựa, và Hoàng Lân mang theo nỗi hận này suốt hai trăm năm. Kể từ đó không mã phu nào dám tu luyện công khai nữa — cho đến khi Hoàng Vân xuất hiện.

## X. Giai Thoại & Bí Mật (轶事 与 秘密)
Trong đàn năm mươi Hải Long Mã, Ngân Phong — con lông bạc tốc độ nhanh gấp ba lần bình thường — được các Chân Long tranh nhau sử dụng, nhưng chỉ nghe lời Hoàng Lân. Bí mật hơn, trong đàn còn có một con tên "Mặc Ảnh" thể hiện trí tuệ bất thường — có thể hiểu tiếng nói và biểu cảm của người, đôi khi tự tìm đường về chuồng mà không cần mã phu dẫn. Hoàng Lân nghi ngờ Mặc Ảnh đã kế thừa ký ức từ tổ tiên Long Tộc thuần chủng qua hiện tượng "Huyết Mạch Hồi Tố," và nếu đúng vậy, nó có tiềm năng hóa long — điều chưa từng xảy ra với Hải Long Mã trong lịch sử. Ông giấu kín phát hiện này vì biết rõ Long Cung sẽ giết Mặc Ảnh ngay nếu biết — một con "gia súc" hóa long là sỉ nhục đối với Chân Long. Bí mật lớn nhất của Hoàng Lân là cuốn nhật ký bọc da cá mập mà ông âm thầm ghi chép suốt ba trăm năm — ghi lại mọi chuyện diễn ra trong Long Cung mà ông tai nghe mắt thấy khi mang ngựa đến các cung điện: cuộc mật đàm giữa trưởng lão, âm mưu tranh đoạt ngôi vị, giao dịch bí mật với thế lực bên ngoài. Cuốn nhật ký đó chứa đựng bí mật triều chính, âm mưu, và tình báo về lực lượng Long Cung — giá trị tình báo khổng lồ nếu rơi vào tay bất kỳ thế lực nào, và Hoàng Lân biết điều đó. Ông giấu nó dưới tảng đá ở góc chuồng Mậu, nơi không ai thèm nhìn đến.

## XI. Quan Hệ Thế Lực (势力关系)
Hải Long Mã Đoàn tồn tại hoàn toàn trong bóng tối quyền lực của Long Cung, không có tiếng nói và không có lựa chọn. Mối quan hệ với Long Cung là lệ thuộc tuyệt đối — mã phu phục vụ không công, không được quyền từ chối bất kỳ yêu cầu nào, và bất kỳ sự bất tuân nào dù nhỏ nhất đều có thể bị trừng phạt bằng bạo lực. Với Tạp Huyết Long Đàn, hai bên chia sẻ nỗi khổ chung của những Long Tộc huyết mạch thấp bị khinh miệt — Hoàng Lân từng lén gặp một trưởng lão Tạp Huyết Long tên Hắc Giác tại Tảo Dã vào đêm trăng mới, trao đổi tin tức và an ủi nhau, nhưng cả hai đều không dám liên lạc công khai vì sợ bị trừng phạt. Ấu Long Học Viện là nơi duy nhất đối xử tương đối tử tế khi cần Hải Long Mã cho huấn luyện — Lam Nguyệt luôn gửi linh cá dư thừa cho mã phu, và Hoàng Lân coi bà là người bạn duy nhất trong hệ thống Long Cung. Nếu có một ngày Long Cung biến động, cuốn nhật ký ba trăm năm của Hoàng Lân sẽ là quân cờ thay đổi cục diện — nhưng lão mã phu chưa quyết định sẽ trao nó cho ai.
