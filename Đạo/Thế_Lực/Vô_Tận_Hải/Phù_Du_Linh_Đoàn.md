---
type: faction
name: Phù Du Linh Đoàn
hantu: 浮游灵团
faction_type: Bộ Lạc
alignment: 0
race: Vi Tộc (Phù Du Linh — sinh vật phù du phát sáng)
region: Vô Tận Hải
founded: Từ khi Vô Tận Hải hình thành (Thượng Cổ)
founder: Không có (hình thành tự nhiên)
emblem: Quan_The_Anh_Sang.png
specialty: Quần Thể Ý Thức, Phát sáng chiếu sáng vùng biển tối, Giao tiếp hình ảnh ánh sáng
economy:
  - Không có nền kinh tế (tồn tại bằng hấp thu linh khí vi lượng)
arcs:
  - arc: 1
    status: Tồn tại tự nhiên
    rank: Không Xếp Hạng
    leader: Linh Quang Mẫu
    population: Hàng triệu cá thể
    territory:
      - Vùng biển sâu phía tây Vô Tận Hải (tầng nước tối)
    assets:
      - name: Quần Thể Ý Thức
        type: Bí Cảnh
      - name: Ánh Sáng Chói Lòa (bản năng phòng thủ)
        type: Trận Pháp
    stats: [5, 5, 5, 50, 10, 8]
    divisions:
      - name: Linh Quang Mẫu
        role: Cá thể trung tâm, "mẹ" của cả đoàn, phát sáng mạnh nhất và duy trì Quần Thể Ý Thức
        headcount:
          truong_lao: 1
          chien_binh: 0
          dan_thuong: 0
        members:
          - character: "[Linh Quang Mẫu]"
            position: Trưởng Lão (Mẫu Thể)
            cultivation: Luyện Khí (tương đương)
            placeholder: true
      - name: Quần Thể Phù Du
        role: Hàng triệu cá thể hành động theo bản năng tập thể, tạo thành thực thể ý thức chung
        headcount:
          truong_lao: 0
          chien_binh: 0
          dan_thuong: 0
        members:
          - character: "[Phù Du Linh cá thể]"
            position: Thành viên quần thể
            cultivation: Không có
            placeholder: true
    relationships:
      - faction: Thâm Hải Thám Hiểm Đoàn
        description: Thâm Hải Thám Hiểm Đoàn là tổ chức duy nhất từng tiếp cận gần Phù Du Linh Đoàn đủ lâu để ghi nhận Quần Thể Ý Thức. Phù Du Linh không chủ động giao tiếp nhưng cũng không thù địch.
        diplomacy:
          lien_minh: 0
          tin: 5
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 0
      - faction: Hải Thần Cung
        description: Hải Thần Cung từng bắt Phù Du Linh làm đèn chiếu sáng nhưng chúng rời biển sâu thì chết nhanh. Hiện Hải Thần Cung coi chúng là hiện tượng tự nhiên, không can thiệp.
        diplomacy:
          lien_minh: 0
          tin: 0
          uy_hiep: -10
          thuong_mai: 0
          on_oan: -15
          le_thuoc: 0
      - faction: Sóng Vi Ba Liên Lạc
        description: Hai Vi Tộc cùng tồn tại trong vùng biển sâu, không cạnh tranh tài nguyên. Phù Du Linh phát sáng, Vi Ba Linh truyền sóng — hai hệ sinh thái bổ sung cho nhau.
        diplomacy:
          lien_minh: 0
          tin: 0
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 0
---

# Phù Du Linh Đoàn (浮游灵团)

> *"Trong vực sâu không ánh sáng, chúng là những ngôi sao cuối cùng — và có lẽ là ký ức cuối cùng của một thế giới đã chìm."*
> — Trích nhật ký thám hiểm của Đoàn Trưởng Thâm Hải Thám Hiểm Đoàn, lần lặn thứ mười ba

## I. Tổng Quan (总览)
Phù Du Linh Đoàn là một tập hợp hàng triệu sinh vật cực nhỏ thuộc Vi Tộc — những thực thể phù du phát sáng tồn tại trong vùng biển sâu phía tây Vô Tận Hải, nơi ánh sáng mặt trời không bao giờ chạm tới. Mỗi cá thể Phù Du Linh gần như không có ý thức riêng biệt, nhưng khi tập hợp đủ số lượng, chúng hình thành "Quần Thể Ý Thức" — một dạng trí tuệ tập thể nguyên thủy nhưng kỳ bí. Đứng đầu — nếu có thể gọi là đứng đầu — là Linh Quang Mẫu, cá thể lớn nhất và phát sáng mạnh nhất, đóng vai trò "mẹ" và hạt nhân duy trì sự gắn kết của cả đoàn. Phù Du Linh Đoàn không xếp hạng trong bất kỳ hệ thống thế lực nào, bởi chúng không phải một tổ chức theo nghĩa thông thường mà là một hiện tượng sinh thái kỳ lạ, tồn tại từ khi Vô Tận Hải hình thành — một trong những sinh vật cổ xưa nhất trên đời.

## II. Địa Lý & Tài Nguyên (地理与资源)
Phù Du Linh Đoàn sống ở tầng nước sâu nơi ánh sáng mặt trời không thể lọt xuống — vùng tối vĩnh cửu của Vô Tận Hải, phía tây, nơi áp suất nước nghiền nát mọi sinh vật thông thường. Vùng nước này được các nhà hải dương học gọi là "Hắc Uyên Đới" — dải nước đen bắt đầu từ độ sâu hơn ba nghìn trượng, nơi nhiệt độ gần bằng không và linh khí loãng đến mức thần thức tu sĩ Kim Đan cũng khó duy trì quá một canh giờ. Chúng không có tài nguyên vật chất — sự tồn tại hoàn toàn dựa vào việc hấp thu linh khí vi lượng hòa tan trong nước biển sâu, một lượng nhỏ đến mức ngay cả tu sĩ cũng không thèm để ý. Ánh sáng phát ra từ cơ thể Phù Du Linh là nguồn sáng duy nhất trong vùng biển tối, tạo nên những dải sáng lung linh uốn lượn giữa lòng đại dương đen thẫm — cảnh tượng mà rất ít sinh vật có cơ hội chứng kiến. Phù Du Linh di chuyển theo hải lưu sâu, đặc biệt là dòng "Huyền Lưu" — hải lưu lạnh chảy ngầm từ Bắc Băng xuống phía nam, trôi dạt vô định giữa bóng tối vĩnh hằng nhưng luôn quay trở lại khu vực "Tĩnh Uyên" — vùng nước tĩnh lặng nơi Huyền Lưu tạo thành vòng xoáy chậm, là nơi Linh Quang Mẫu thường cư trú.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
Phù Du Linh không có văn hóa hay tín ngưỡng theo cách hiểu thông thường. Mỗi cá thể chỉ sống vài ngày rồi tan biến, nhưng Quần Thể Ý Thức tồn tại liên tục qua hàng triệu thế hệ, như một dòng sông ý thức không bao giờ ngừng chảy. Khi Quần Thể Ý Thức đạt đến mật độ cao, chúng thể hiện những hành vi kỳ lạ không thể giải thích bằng bản năng đơn thuần: xếp thành hình dáng có ý nghĩa, phát sáng theo nhịp điệu nhất định giống như một bài hát không có âm thanh, hoặc thay đổi hướng di chuyển đột ngột như đang "quyết định" điều gì đó. Thâm Hải Thám Hiểm Đoàn từng ghi nhận rằng vào những đêm không trăng, Phù Du Linh xếp thành hình dáng mặt trăng tròn — như thể chúng nhớ về ánh sáng mà tầng nước sâu không bao giờ chạm tới. Vai trò sinh thái của chúng là vô cùng quan trọng — ánh sáng của Phù Du Linh chiếu sáng vùng biển tối, giúp các sinh vật biển sâu khác di chuyển và tìm thức ăn, bao gồm loài Sâm San Hô Sâu — loại dược liệu biển quý hiếm chỉ sinh trưởng dưới ánh sáng Phù Du Linh. Không có chúng, tầng nước sâu của Vô Tận Hải sẽ là bóng tối tuyệt đối, một thế giới câm điếc.

## IV. Cơ Cấu Tổ Chức (组织结构)
Phù Du Linh Đoàn không có hệ thống cấp bậc rõ ràng — cả đoàn di chuyển và phản ứng như một sinh vật đơn lẻ khổng lồ. Linh Quang Mẫu là cá thể lớn nhất, đóng vai trò hạt nhân trung tâm của Quần Thể Ý Thức, phát ra tần số ánh sáng đặc biệt để đồng bộ hóa hành vi của hàng triệu cá thể xung quanh. Khi Linh Quang Mẫu chết — do tuổi thọ tự nhiên hoặc bị hải thú ăn — Quần Thể Ý Thức tan rã tạm thời, cả đoàn trở thành những cá thể rời rạc vô tri, cho đến khi một Phù Du Linh mới phát triển đủ lớn để trở thành Mẫu Thể kế tiếp. Quá trình này có thể mất từ vài tuần đến vài tháng, trong thời gian đó đoàn Phù Du Linh trôi dạt vô hồn theo hải lưu, mất đi mọi hành vi có tổ chức.

## V. Công Pháp & Trận Pháp (功法与阵法)
Phù Du Linh không tu luyện bất kỳ công pháp nào — khả năng phát sáng là bản năng tự nhiên do cơ thể chuyển hóa linh khí vi lượng trong nước thành quang năng. Mỗi cá thể chỉ phát ra ánh sáng yếu ớt, nhưng khi hàng triệu cá thể cùng tỏa sáng, hiệu ứng tổng hợp đủ để chiếu sáng một vùng biển rộng hàng dặm. Cơ chế phòng vệ duy nhất của chúng là phát sáng chói lòa khi bị đe dọa — toàn bộ Quần Thể Ý Thức cùng lúc tập trung toàn bộ năng lượng vào một đợt sáng bùng nổ, đủ mạnh để làm mù tạm thời hải thú cấp thấp và gây choáng váng cho sinh vật cấp trung trong vài giây. Tuy nhiên, sau mỗi lần bùng nổ, cả đoàn kiệt sức nghiêm trọng và phải mất nhiều ngày mới hồi phục.

## VI. Đặc Sản Môn Phái (门派特产)
- **Phù Du Linh Dịch:** Khi Phù Du Linh chết, cơ thể tan thành một giọt dịch phát quang cực nhỏ, nếu thu thập đủ số lượng lớn có thể dùng làm nguyên liệu luyện đan chiếu sáng hoặc mực vẽ phù lục đặc biệt. Mực Phù Du được giới phù lục sư săn tìm vì có khả năng phát sáng trong bóng tối, cho phép đọc phù lục mà không cần đèn — đặc biệt hữu ích trong chiến đấu ban đêm. Tuy nhiên, việc thu thập cực kỳ khó khăn vì Phù Du Linh sống ở tầng nước sâu và dịch phát quang tan vào nước chỉ trong vài phút.
- **Quần Thể Ý Thức:** Bản thân hiện tượng Quần Thể Ý Thức là một bí ẩn có giá trị nghiên cứu vô cùng lớn. Nếu ai đó có thể giải mã cơ chế hoạt động của nó, tri thức thu được có thể ứng dụng vào trận pháp liên kết tâm thức hoặc kỹ thuật điều khiển hàng loạt — nhưng cho đến nay chưa ai thành công. Trận Sư Lương Hải Vân của Hải Thần Cung từng dành ba mươi năm nghiên cứu nhưng chỉ thu được một bản ghi chép dở dang trước khi qua đời vì tuổi già.
- **Ánh Sáng Tĩnh Uyên:** Vùng nước quanh nơi Linh Quang Mẫu cư trú phát ra thứ ánh sáng dịu nhẹ không dao động — các thợ lặn gọi là "Ánh Sáng Tĩnh Uyên." Tu sĩ thiền định trong vùng ánh sáng này cho biết thần thức trở nên ổn định bất thường, như thể đang được bao bọc bởi một ý thức mênh mông và bình yên. Hiệu ứng này chưa được giải thích nhưng đã trở thành truyền thuyết trong giới thâm hải thám hiểm.

## VII. Cơ Sở Hạ Tầng (基础设施)
Phù Du Linh Đoàn không xây dựng bất kỳ cơ sở hạ tầng nào. Chúng không có nhà cửa, hang động, hay bất kỳ cấu trúc cố định nào — sự tồn tại hoàn toàn là trôi dạt trong lòng nước. Nếu phải kể một thứ gần giống "cơ sở hạ tầng," thì đó là chính bản thân đoàn Phù Du Linh: khi tập hợp đông đủ, chúng tạo thành một cấu trúc sống di động, một đám mây sáng khổng lồ dưới lòng biển tối, đóng vai trò vừa là nơi ở vừa là phương tiện di chuyển vừa là hệ thống phòng thủ. Vùng nước xung quanh Linh Quang Mẫu có nồng độ linh khí cao hơn bình thường — kết quả của hàng triệu cá thể cùng hô hấp linh khí — tạo thành một "ốc đảo" vi mô thu hút các sinh vật biển sâu nhỏ bé khác.

## VIII. Kinh Tế (经济)
Phù Du Linh Đoàn không có khái niệm kinh tế. Chúng không sản xuất, không trao đổi, không tích lũy. Sự tồn tại hoàn toàn dựa vào việc hấp thu linh khí vi lượng trong nước biển — một nguồn tài nguyên gần như vô tận nhưng cũng gần như vô giá trị đối với bất kỳ sinh vật nào khác. Mỗi cá thể Phù Du Linh tiêu thụ một lượng linh khí nhỏ đến mức không thể đo lường, nhưng hàng triệu cá thể cộng lại tạo ra một vùng "hút linh khí" nhẹ xung quanh đoàn, ảnh hưởng không đáng kể đến môi trường xung quanh. Giá trị kinh tế duy nhất mà Phù Du Linh mang lại là gián tiếp: ánh sáng của chúng duy trì hệ sinh thái vùng biển tối, nơi nhiều loại hải sản và dược liệu quý hiếm sinh sống.

## IX. Lịch Sử Tóm Tắt (简史)
Phù Du Linh tồn tại từ khi Vô Tận Hải hình thành — một trong những sinh vật cổ nhất trong thế giới tu tiên, có lẽ còn lâu đời hơn cả Long Tộc. Trong suốt hàng triệu năm, chúng trôi dạt âm thầm trong bóng tối, không ai biết đến sự tồn tại của chúng ngoài các sinh vật biển sâu. Khoảng hai nghìn năm trước, một nhóm Giao Nhân đánh cá sâu lần đầu chứng kiến "đám mây sáng dưới đáy biển" và mang câu chuyện về kể lại, nhưng bị coi là ảo giác do áp suất nước gây ra. Không ai coi chúng là Vi Tộc cho đến khi một nhóm nghiên cứu của Thâm Hải Thám Hiểm Đoàn do Thám Hiểm Gia Trần Huyền Thâm dẫn đầu phát hiện hiện tượng Quần Thể Ý Thức — lần đầu tiên xác nhận rằng những sinh vật nhỏ bé này có dạng trí tuệ tập thể. Phát hiện này gây chấn động giới học thuật biển sâu nhưng nhanh chóng bị lãng quên vì không ai có thể lặn đủ sâu để nghiên cứu thêm. Từng có thời kỳ Hải Thần Cung ra lệnh cho binh sĩ bắt Phù Du Linh bằng bình ngọc chuyên dụng để làm đèn chiếu sáng cung điện, nhưng chúng chết rất nhanh khi rời khỏi môi trường biển sâu, khiến nỗ lực khai thác thất bại hoàn toàn và bị Hải Đế cấm tiếp tục.

## X. Giai Thoại & Bí Mật (轶事与秘密)
Có giả thuyết rằng Phù Du Linh không phải sinh vật tự nhiên mà là tàn dư linh hồn của một thế lực cổ đại bị hủy diệt — hàng triệu mảnh vụn linh hồn bị nghiền nát đến mức mất đi mọi ký ức và cá tính, chỉ còn lại bản năng phát sáng và xu hướng tụ lại với nhau. Giả thuyết này do Trận Sư Lương Hải Vân đề xuất sau khi phân tích cấu trúc năng lượng của Phù Du Linh và nhận ra rằng tần số dao động của chúng giống một cách kỳ lạ với tần số linh hồn nhân tộc ở trạng thái tan rã. Nếu giả thuyết này đúng, Quần Thể Ý Thức có thể là nỗ lực vô thức của những linh hồn đó để "ghép lại" thành một thể thống nhất.

Thâm Hải Thám Hiểm Đoàn từng chứng kiến Phù Du Linh xếp thành hình dáng một tòa thành cổ đại hoàn chỉnh — tường thành, cổng vòm, tháp canh, thậm chí cả quảng trường trung tâm với đài phun nước — rồi tan biến trong chớp mắt, như thể đó là ký ức cuối cùng của một nền văn minh đã chết. Thám Hiểm Gia Trần Huyền Thâm ghi lại rằng kiến trúc đó không giống bất kỳ nền văn minh nào hiện tồn tại, gợi ý về một thế lực đã hoàn toàn bị xóa khỏi lịch sử.

Khi Quần Thể Ý Thức đạt đến mật độ cực đại — điều chỉ xảy ra vài lần trong hàng nghìn năm — chúng có thể giao tiếp bằng hình ảnh ánh sáng phức tạp, chiếu lên lòng nước những cảnh tượng mà người chứng kiến mô tả như "giấc mơ của đại dương."

## XI. Quan Hệ Thế Lực (势力关系)
- **Thâm Hải Thám Hiểm Đoàn:** Tổ chức duy nhất từng tiếp cận gần và nghiên cứu Phù Du Linh Đoàn. Mối quan hệ đơn phương — Thâm Hải quan sát, Phù Du Linh không phản ứng. Tuy nhiên, có ghi chép rằng trong một lần thám hiểm, Phù Du Linh đã chủ động xếp thành mũi tên chỉ hướng, giúp đoàn thám hiểm tránh được một vực sâu nguy hiểm.
- **Hải Thần Cung:** Hải Thần Cung từng thử bắt Phù Du Linh làm nguồn sáng trang trí cho cung điện, nhưng thất bại vì chúng chết nhanh khi rời môi trường tự nhiên. Hiện tại, Hải Thần Cung xếp Phù Du Linh Đoàn vào danh mục "hiện tượng tự nhiên" và không can thiệp.
- **Sóng Vi Ba Liên Lạc:** Hai Vi Tộc cùng tồn tại trong vùng biển sâu mà không cạnh tranh — Phù Du Linh phát sáng ở tầng nước tối, Vi Ba Linh truyền sóng khắp mọi tầng. Không có tương tác trực tiếp nhưng sự tồn tại song song của chúng cho thấy vùng biển sâu của Vô Tận Hải phong phú hơn nhiều so với những gì các thế lực trên mặt nước biết đến.
