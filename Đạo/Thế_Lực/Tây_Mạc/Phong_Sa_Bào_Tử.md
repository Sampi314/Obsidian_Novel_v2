---
type: faction
name: Phong Sa Bào Tử
hantu: 风沙孢子
faction_type: Liên Minh
alignment: 0
race: Vi Tộc (Bào Tử loại)
region: Tây Mạc
founded: Tự nhiên (Tồn tại song hành cùng bão cát Tây Mạc)
founder: Không có (Hình thành tự nhiên)
emblem: Phong_Sa_Bao_Tu.png
specialty: Hấp thu khoáng linh vi mô, Phát sáng tín hiệu, Dự báo hướng gió
economy:
- Không có hoạt động kinh tế chủ động
- Khoáng linh vi mô bị thu gom bởi đan sư
arcs:
  - arc: 1
    status: Tồn tại ổn định (Trôi nổi cùng bão cát)
    rank: Không Xếp Hạng
    leader: Bào Tử Vương (Bản năng điều phối)
    population: 10
    territory:
      - Hoàng Kim Sa Hải (Bất kỳ nơi nào có bão cát)
    assets:
      - name: Bào Tử Vương
        type: Sinh Vật
      - name: Khoáng linh vi mô
        type: Tài Nguyên
    stats: [5, 20, 5, 10, 10, 15]
    divisions:
      - name: Đoàn Bào Tử
        role: Bay cùng bão cát, thu khoáng linh vi mô, phân phối tập thể
        headcount:
          truong_lao: 1
          chien_binh: 0
          dan_thuong: 9
        members:
          - character: "[Bào Tử Vương]"
            position: Cá thể lớn nhất (Điều phối đoàn)
            cultivation: Luyện Khí (Tương đương)
            placeholder: true
    relationships:
      - faction: Sa Mạc Hướng Đạo Hội
        description: Hướng Đạo Hội là số ít biết về Bào Tử, sử dụng vệt sáng sau bão để xác định hướng gió và dự báo thời tiết.
        diplomacy:
          lien_minh: 0
          tin: 10
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 10
          le_thuoc: 0
      - faction: Phế Khí Luyện Đan Phường
        description: Từng thu gom Bào Tử rơi sau bão, phát hiện chứa khoáng linh tinh khiết nhưng lượng quá ít để sử dụng thương mại.
        diplomacy:
          lien_minh: 0
          tin: 0
          uy_hiep: 0
          thuong_mai: 10
          on_oan: 0
          le_thuoc: 0
      - faction: Linh Sa Khuẩn Đoàn
        description: Cùng là Vi Tộc trong Hoàng Kim Sa Hải nhưng không tương tác. Khuẩn Đoàn sống dưới đất, Bào Tử sống trên không — hai hệ sinh thái song song.
        diplomacy:
          lien_minh: 0
          tin: 0
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 0
---

# Phong Sa Bào Tử (风沙孢子)

> *"Gió đưa đi đâu — đi đó. Bão cho gì — nhận đó. Không chọn, không từ chối, chỉ bay."*
> — Triết lý sinh tồn của Bào Tử, được Phong Sa Lão Nhân ghi lại sau lần chứng kiến Mưa Linh Quang

## I. Tổng Quan (总览)
Phong Sa Bào Tử là Vi Tộc cổ xưa sống lơ lửng trong các trận bão cát của Hoàng Kim Sa Hải — chủng tộc duy nhất trong toàn Tây Mạc sinh tồn trên không trung thay vì dưới đất hay trong nước. Mỗi đoàn gồm hàng triệu bào tử bay cùng nhau như một đám mây sống, hấp thu khoáng linh vi mô phân tán trong bão cát mà không sinh vật nào khác có khả năng thu thập. Dưới sự điều phối của Bào Tử Vương — cá thể lớn nhất, to bằng hạt gạo — đoàn bào tử hoạt động hoàn toàn tập thể, giao tiếp bằng ánh sáng và sống chết cùng bão. Rất ít chủng tộc biết đến sự tồn tại của chúng, và đối với phần lớn cư dân sa mạc, vệt sáng nhạt trên cát sau bão chỉ là hiện tượng tự nhiên bình thường. Nhưng đối với những ai hiểu, Phong Sa Bào Tử là minh chứng rằng ngay cả trong cơn bão tàn khốc nhất, sự sống vẫn tìm ra cách tồn tại.

## II. Địa Lý & Tài Nguyên (地理 与 资源)
Phong Sa Bào Tử xuất hiện ở bất kỳ nơi nào có bão cát trong Hoàng Kim Sa Hải, không có lãnh địa cố định — nhà của chúng là chính cơn bão. Khi bão hoạt động, chúng bay lơ lửng trong tầng không khí cao nhất của cơn bão — "Phong Nhãn Tầng" — nơi gió xoáy mạnh nhất nhưng khoáng linh vi mô cũng dày đặc nhất, hấp thu những hạt khoáng chất siêu nhỏ mà mắt thường không thấy nhưng chứa linh lực thuần khiết. Khi bão tạnh, toàn bộ đoàn "rơi" xuống cát cùng nhau, tạo thành vệt sáng nhạt lung linh trên mặt sa mạc — hiện tượng mà Sa Mạc Hướng Đạo Hội gọi là "Bão Dư Quang" — đây là khoảnh khắc duy nhất có thể quan sát được sự tồn tại của chúng. Các vệt sáng thường xuất hiện ở ba khu vực bão tập trung: **Cuồng Phong Hẻm** phía đông, **Bão Mắt Sa Trường** ở trung tâm, và **Thiên Lý Phong Đạo** phía bắc. Khoáng linh vi mô là tài nguyên bẩm sinh của Bào Tử, tinh khiết đến mức đan sư phải kinh ngạc, nhưng lượng thu được từ mỗi đoàn quá ít để khai thác thương mại.

## III. Văn Hóa & Tín Ngưỡng (文化 与 信仰)
Triết lý sinh tồn của Bào Tử đơn giản đến thuần khiết, thể hiện qua hành vi tập thể: "Gió đưa đi đâu — đi đó. Bão cho gì — nhận đó." Chúng không chống lại gió, không chọn hướng, hoàn toàn thuận theo bão cát để di chuyển — một dạng "vô vi" tự nhiên nhất mà ngay cả Vô Tranh Tự cũng phải ngưỡng mộ nếu biết đến. Khi bão tạnh và đoàn rơi xuống, tất cả cùng nghỉ ngơi trong im lặng — "Tịch Miên" — trước khi cơn bão tiếp theo nâng chúng lên lại. Giao tiếp bằng phương thức phát sáng theo nhịp điệu — "Quang Ngữ" — mỗi tần số ánh sáng mang một ý nghĩa khác nhau: sáng nhanh nghĩa là nguy hiểm, sáng chậm nghĩa là an toàn, sáng nhấp nháy nghĩa là "tập trung về phía Bào Tử Vương." Ngôn ngữ ánh sáng này tinh tế đến mức Phong Sa Lão Nhân — hướng đạo kỳ cựu nhất sa mạc — nghiên cứu suốt hai mươi năm vẫn chỉ giải mã được ba tín hiệu. Không có phân chia vai trò — tất cả cùng bay, cùng thu khoáng linh, cùng phân phối đều cho nhau.

## IV. Cơ Cấu Tổ Chức (组织结构)
Cơ cấu của Bào Tử cực kỳ đơn giản và bình đẳng tuyệt đối — một "xã hội không giai cấp" tự nhiên nhất thế gian. Bào Tử Vương là cá thể lớn nhất trong đoàn, to bằng hạt gạo trong khi các cá thể khác nhỏ như hạt bụi, phát tín hiệu Quang Ngữ mạnh nhất để điều phối toàn đoàn bay theo cùng hướng và tập trung hấp thu khoáng linh. Vai trò của Bào Tử Vương không phải "vua" mà giống "ngọn hải đăng" — chỉ phát sáng dẫn đường, không ra lệnh. Hàng triệu bào tử còn lại hành động tập thể, không có phân chia nhóm hay nhiệm vụ riêng biệt, mỗi cá thể đều bình đẳng trong quyền lợi và trách nhiệm. Khi Bào Tử Vương chết — thường do kiệt sức sau bão lớn — cá thể lớn thứ hai tự động thay thế mà không có bất kỳ tranh chấp hay nghi thức nào — quá trình chuyển giao diễn ra trong tích tắc, hoàn toàn theo bản năng, không có tang lễ vì Bào Tử không biết buồn. Hiện tại có ít nhất năm đoàn Bào Tử hoạt động độc lập trong Hoàng Kim Sa Hải, mỗi đoàn theo một hệ thống bão riêng.

## V. Công Pháp & Trận Pháp (功法 与 阵法)
Bào Tử không tu luyện — khả năng hấp thu khoáng linh vi mô là bẩm sinh, một phần của chu kỳ sinh tồn tự nhiên không cần rèn luyện. Khi bị đe dọa bởi yêu thú hay sinh vật khác, toàn đoàn đồng loạt phát sáng chói lòa trong kỹ năng phòng thủ duy nhất — "Linh Quang Bạo Phát" — tạo ra vụ nổ ánh sáng làm lóa mắt và nhiễu loạn thần thức kẻ tấn công trong khoảnh khắc, đủ để đoàn tản mát và thoát thân theo gió. Cường độ ánh sáng tương đương pháp thuật cấp Luyện Khí, không đủ gây thương tích cho tu sĩ Trúc Cơ nhưng hiệu quả tuyệt vời với yêu thú và sinh vật thông thường. Ngoài ra, khi đoàn rơi xuống cát sau bão, chúng tạo ra hiện tượng "Mưa Linh Quang" — hàng triệu điểm sáng nhỏ li ti rơi xuống như mưa sao, vô cùng đẹp mắt nhưng hoàn toàn vô hại, kéo dài từ nửa khắc đến một khắc. Phong Sa Lão Nhân mô tả đây là "cảnh tượng đẹp nhất sa mạc mà ta từng thấy" — nhưng trong suốt bốn mươi năm lang thang, lão chỉ chứng kiến bảy lần.

## VI. Đặc Sản Môn Phái (门派特产)
- **Khoáng Linh Vi Mô (Tinh Trần):** Hạt khoáng chất siêu nhỏ chứa linh lực thuần khiết đặc biệt, do Bào Tử hấp thu từ bão cát và tích lũy trong cơ thể suốt đời. Tinh khiết hơn bất kỳ loại linh thạch nào — đan sư Hồng Luyện xác nhận rằng một lạng Tinh Trần có giá trị ngang mười cân linh thạch trung phẩm về mặt thuần độ, nhưng thu thập một lạng cần lượm nhặt hàng nghìn xác Bào Tử, khiến việc khai thác thương mại gần như bất khả thi.
- **Bão Dư Quang (Vệt Sáng Bào Tử):** Dấu vết lung linh trên cát sau khi đoàn Bào Tử rơi xuống, chứa một lượng nhỏ khoáng linh và thông tin về hướng gió chủ đạo. Sa Mạc Hướng Đạo Hội sử dụng Bão Dư Quang như la bàn tự nhiên — hướng mà vệt sáng kéo dài nhất cho biết gió chính sẽ thổi về đâu trong ba ngày tới, phương pháp dự báo chính xác hơn bất kỳ pháp khí nào.
- **Hắc Tinh Phấn:** Bụi phấn cực hiếm rơi từ Bào Tử Vương đen (Hắc Tinh) — nếu thu được, có tính chất kỳ dị: hấp thu và triệt tiêu linh lực trong phạm vi nhỏ. Chưa ai thu thập đủ lượng để nghiên cứu nghiêm túc.

## VII. Cơ Sở Hạ Tầng (基础设施)
Phong Sa Bào Tử không xây dựng bất kỳ cơ sở hạ tầng nào — chúng là sinh vật trôi nổi hoàn toàn, sống và chết trong không trung, tự do hơn bất kỳ chủng tộc nào trên Cố Nguyên Giới. Khi bão hoạt động, Phong Nhãn Tầng — tầng không khí cao nhất trong lòng bão — chính là "nhà" của chúng, một ngôi nhà luôn di chuyển với tốc độ hàng trăm dặm mỗi ngày. Khi bão tạnh, mặt cát nơi đoàn rơi xuống tạm thời trở thành nơi nghỉ ngơi — "Tịch Miên Địa" — nhưng không bao giờ cố định vì bão tiếp theo sẽ nâng chúng lên lại trong vài ngày đến vài tuần. Điều đáng chú ý là những khu vực Bào Tử thường xuyên rơi xuống — đặc biệt là ba khu vực Cuồng Phong Hẻm, Bão Mắt Sa Trường, và Thiên Lý Phong Đạo — có nồng độ khoáng linh trong cát cao hơn bình thường từ mười đến hai mươi phần trăm, vô tình tạo ra những "điểm phì nhiêu" giữa lòng sa mạc mà không ai giải thích được nguồn gốc, thu hút thực vật và côn trùng linh đến cư ngụ.

## VIII. Kinh Tế (经济)
Bào Tử không có khái niệm kinh tế hay giao dịch — chúng tồn tại ngoài mọi hệ thống thương mại của Tây Mạc. Giá trị kinh tế gián tiếp của chúng nằm ở hai khía cạnh. Thứ nhất, khoáng linh vi mô Tinh Trần — Phế Khí Luyện Đan Phường từng cử đệ tử Vân Sa ra bão thu gom Bào Tử rơi trên cát sau bão, phát hiện chúng chứa khoáng linh tinh khiết đặc biệt, nhưng sau ba năm thu gom mới được nửa lạng, Phường Chủ Hồng Luyện quyết định ngừng vì "công sức không xứng đáng." Thứ hai, Bão Dư Quang có giá trị gián tiếp với Sa Mạc Hướng Đạo Hội như một công cụ dự báo thời tiết và xác định hướng gió — thứ mà không pháp khí nào có thể thay thế, giúp hướng đạo cứu sống vô số thương đoàn và lữ khách mỗi năm. Phong Sa Lão Nhân từng nói: "Bão Dư Quang đáng giá hơn vàng — nó cho ta biết bão tiếp theo đến từ đâu."

## IX. Lịch Sử Tóm Tắt (简史)
Phong Sa Bào Tử tồn tại từ thời cổ đại, song hành cùng các trận bão cát đầu tiên của Tây Mạc — khi sa mạc mới hình thành và gió bắt đầu cuốn cát bay, Bào Tử nguyên thủy đã ở đó, bay lên cùng những cơn bão đầu tiên. Chúng không có lịch sử theo nghĩa thông thường — không có sự kiện trọng đại, không có biến cố, chỉ có chu kỳ bất tận của bay lên và rơi xuống, đơn giản và vĩnh cửu. Rất ít chủng tộc từng nhận ra sự tồn tại của chúng. Cách đây khoảng hai trăm năm, Sa Mạc Hướng Đạo Hội đời thứ ba — dưới sự lãnh đạo của Hướng Đạo Trưởng Phong Vũ Lão — là thế lực đầu tiên ghi nhận Bào Tử như hiện tượng tự nhiên có quy luật, và phát triển phương pháp đọc Bão Dư Quang để dự báo thời tiết, truyền lại cho các thế hệ hướng đạo sau. Ngoài ra, Bào Tử tồn tại trong im lặng, không gây ảnh hưởng và cũng không bị ảnh hưởng bởi bất kỳ cuộc chiến hay biến cố nào trên sa mạc — cho đến khi xảy ra sự kiện Hắc Tinh.

## X. Giai Thoại & Bí Mật (轶事 与 秘密)
- Phế Khí Luyện Đan Phường từng thu gom Bào Tử rơi trên cát sau bão — đệ tử Vân Sa phát hiện Tinh Trần chứa khoáng linh tinh khiết vượt xa linh thạch thông thường gấp mười lần, nhưng lượng quá ít để sử dụng thương mại. Dù vậy, Hồng Luyện vẫn giữ nửa lạng Tinh Trần thu được trong hộp ngọc bí mật, tin rằng một ngày nào đó sẽ tìm ra cách sử dụng xứng đáng. Một số đan sư lang thang vẫn lặng lẽ tìm kiếm vệt sáng Bào Tử sau mỗi trận bão lớn, hy vọng thu được thêm.
- Sự kiện Hắc Tinh xảy ra cách đây khoảng bảy mươi năm: một trận bão khổng lồ tên "Thiên La Phong" — lớn nhất trong ba trăm năm — đưa một đoàn Bào Tử đến tận rìa Vĩnh Tịch Chi Địa. Toàn bộ đoàn chết sạch trong khoảnh khắc như bị hút cạn sinh lực, chỉ Bào Tử Vương sống sót nhưng từ đó biến đổi hoàn toàn — phát sáng đen thay vì trắng, to gấp đôi bình thường, và bay ngược gió thay vì thuận gió. Bào Tử Vương đen — "Hắc Tinh" — giờ bay một mình, không theo bão nào nữa, lang thang như bóng ma giữa sa mạc.
- Sa Mạc Hướng Đạo Hội gọi Hắc Tinh là "Tử Diệt Tinh" và coi mỗi lần nhìn thấy nó là điềm xấu — nơi nào Hắc Tinh xuất hiện, bão cát bất thường sẽ đến trong vòng ba ngày, mạnh gấp đôi bão thông thường. Phong Sa Lão Nhân từng cố theo dõi Hắc Tinh suốt mười bảy ngày nhưng nó biến mất mỗi khi có người đến gần mười trượng, như thể cảm nhận được thần thức — điều mà Bào Tử thông thường không thể làm. Lão Nhân ghi trong nhật ký: "Thứ đó không còn là Bào Tử nữa — nó đã trở thành thứ gì đó khác, thứ gì đó mà Vĩnh Tịch Chi Địa đã biến nó thành."

## XI. Quan Hệ Thế Lực (势力关系)
- **Sa Mạc Hướng Đạo Hội:** Thế lực duy nhất nhận ra và ghi nhận Bào Tử như hiện tượng tự nhiên có quy luật, có giá trị sinh tồn thực tế. Hướng đạo sử dụng Bão Dư Quang để dự báo hướng gió và cảnh báo bão cát, biến sự tồn tại vô hình của Bào Tử thành công cụ cứu sống. Phong Sa Lão Nhân — hướng đạo kỳ cựu nhất — là người nghiên cứu Bào Tử sâu nhất và coi chúng là "thầy giáo vô hình của sa mạc."
- **Phế Khí Luyện Đan Phường:** Từng nghiên cứu Bào Tử vì Tinh Trần khoáng linh tinh khiết, nhưng đã ngừng thu gom do lượng quá ít. Hồng Luyện vẫn coi Bào Tử là đề tài nghiên cứu tiềm năng và giữ nửa lạng Tinh Trần như "bảo vật chờ ngày."
- **Linh Sa Khuẩn Đoàn:** Cùng là Vi Tộc cổ đại trong Hoàng Kim Sa Hải nhưng chiếm hai hệ sinh thái hoàn toàn khác biệt — Khuẩn Đoàn dưới đất phân giải cái chết, Bào Tử trên không thu gom tinh hoa gió — hai mặt đối lập của cùng một sa mạc, không tương tác và không cạnh tranh, nhưng cùng duy trì sự cân bằng cho Hoàng Kim Sa Hải.
