---
type: faction
name: Hải Trùng Đoàn
hantu: 海虫团
faction_type: Bộ Lạc
alignment: 0
race: Hải Tộc (Giáp xác, giun biển, bọ biển cấp thấp)
region: Vô Tận Hải
founded: Thượng Cổ Kỷ Nguyên (tồn tại từ thuở sơ khai)
founder: Không rõ (tự phát sinh thái)
emblem: Giap_Xac_Quan.png
specialty: Phân hủy sinh học, Tái chế dinh dưỡng đại dương, Chiến thuật bầy đàn
economy:
- "Hợp đồng dọn dẹp" sau các trận chiến lớn (bị ép buộc)
- Bán axit phân hủy cho luyện khí sư (thông qua trung gian)
- Khai thác tinh hoa xác chết hải thú (vô ý thức)
arcs:
  - arc: 1
    status: Mở rộng lãnh thổ
    rank: Không Xếp Hạng
    leader: Trùng Vương Giáp Xác
    population: 3000000
    territory:
      - Vùng trầm tích phía tây đáy biển Vô Tận Hải
      - Các bãi xác chết sau chiến trận (tạm thời)
    assets:
      - name: Bãi Trầm Tích Cổ Đại
        type: Tài Nguyên
      - name: Axit Tiêu Hóa Linh Tính
        type: Tài Nguyên
    stats: [35, 10, 5, 50, 30, 8]
    divisions:
      - name: Đàn Trùng Chính
        role: Phân hủy xác chết, tái chế dinh dưỡng, mở rộng lãnh thổ
        headcount:
          truong_lao: 1
          chien_binh: 100
          dan_thuong: 2999899
        members:
          - character: Giáp Xác
            position: Trùng Vương
            cultivation: Trúc Cơ Sơ Kỳ
            placeholder: false
          - character: "[Phó Trùng Giáp]"
            position: Phó Trùng Vương
            cultivation: Luyện Khí Đỉnh Phong
            placeholder: true
    relationships:
      - faction: Hải Thần Cung
        description: Bị Hải Thần Cung coi thường nhưng lợi dụng. Sau mỗi trận chiến lớn, Hải Thần Cung ép Hải Trùng Đoàn dọn dẹp chiến trường, coi như "nô lệ dọn dẹp" không cần trả công.
        diplomacy:
          lien_minh: -20
          tin: -10
          uy_hiep: 60
          thuong_mai: 0
          on_oan: -30
          le_thuoc: 40
      - faction: Hắc Hải Hải Tặc
        description: Mối quan hệ gián tiếp — mỗi cuộc tấn công của hải tặc tạo ra xác chết, và Hải Trùng Đoàn đến dọn dẹp. Hải tặc ghê tởm chúng nhưng không đánh vì không có lý do.
        diplomacy:
          lien_minh: 0
          tin: -30
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 0
      - faction: Hải Quy Trưởng Lão Hội
        description: Huyền Quy là một trong số ít sinh vật hiểu vai trò sinh thái quan trọng của Hải Trùng Đoàn. Đôi bên không giao thiệp trực tiếp nhưng tồn tại sự tôn trọng ngầm.
        diplomacy:
          lien_minh: 5
          tin: 20
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 0
---

# HẢI TRÙNG ĐOÀN (海虫团)

> *"Chúng ăn cái chết để nuôi sự sống — đó là đạo lý giản đơn nhất mà các thế lực hùng mạnh luôn quên."*
> — Huyền Quy, Hải Quy Trưởng Lão Hội

## I. Tổng Quan (总览)
Hải Trùng Đoàn là tập hợp hàng triệu sinh vật đáy biển cấp thấp — bọ giáp biển, giun biển, và các loài giáp xác nhỏ — đóng vai trò "đội vệ sinh" vĩnh cửu của Vô Tận Hải. Với dân số ước tính ba triệu cá thể nhưng không xếp hạng trong bảng thế lực, đoàn tồn tại từ thuở sơ khai của đại dương, chuyên phân hủy xác chết và tái chế dinh dưỡng cho hệ sinh thái biển sâu. Đứng đầu là Trùng Vương Giáp Xác, con bọ biển linh lớn nhất với kích thước bằng con chó, tu vi tương đương Trúc Cơ Sơ Kỳ — sinh vật duy nhất trong đoàn có linh trí đủ cao để nhận thức bản thân là "ta" chứ không phải "đàn." Dù bị mọi chủng tộc khác ghê tởm và coi thường, đoàn đóng vai trò sinh thái không thể thay thế — nếu không có chúng, đáy biển sẽ chìm trong xác chết thối rữa và hệ sinh thái sẽ sụp đổ. Trong ngữ cảnh Hải Tộc, câu "đi gặp Hải Trùng" đồng nghĩa với "chết" — một cách nói vừa ghê tởm vừa chính xác đến đáng sợ.

## II. Địa Lý & Tài Nguyên (地理 与 资源)
Hải Trùng Đoàn hoạt động chủ yếu trên bề mặt đáy biển bằng phẳng vùng phía tây, tại khu vực mà Hải Tộc gọi là "Trùng Nguyên" — vùng trầm tích rộng hàng trăm dặm vuông, nơi xác sinh vật chết từ tầng nước trên chìm xuống tích tụ theo thời gian. Khu vực rộng lớn nhưng nghèo linh khí — đáy biển phẳng không có linh mạch, ánh sáng không tới, nhiệt độ thấp và áp suất cao, mùi thối rữa nồng nặc đến mức sinh vật thông thường không thể tồn tại quá một ngày. Tài nguyên chính là xác chết hải thú, cá, thực vật biển — nguồn dinh dưỡng duy nhất nuôi sống cả đàn. Sau mỗi trận chiến lớn giữa Hải Thần Cung và Hắc Hải Hải Tặc, hàng nghìn xác chết trôi xuống đáy biển — đó là lúc Hải Trùng Đoàn được "bữa tiệc" lớn nhất, số lượng cá thể bùng nổ trong vài tuần, mật độ dày đến mức đáy biển dường như chuyển động như một tấm thảm sống. Gần đây, số lượng xác chết tăng vọt ở vùng biển nam do ảnh hưởng của Huyết Độc giết chết sinh vật hàng loạt, khiến đoàn đang mở rộng lãnh thổ về phía đó với tốc độ đáng lo ngại — Trùng Nguyên phía nam mới hình thành chỉ trong vài năm, rộng ngang với Trùng Nguyên cũ đã tích lũy hàng ngàn năm.

## III. Văn Hóa & Tín Ngưỡng (文化 与 信仰)
Hải Trùng Đoàn gồm các sinh vật cấp thấp — bọ giáp biển, giun biển, và giáp xác nhỏ chuyên phân hủy xác chết, phần lớn hành động theo bản năng ăn, ngủ, sinh sản mà không có văn hóa hay tín ngưỡng phức tạp. Chỉ có Trùng Vương Giáp Xác và vài chục cá thể lớn nhất — gọi là "Trùng Giáp" — đã khai mở linh trí ở mức tối thiểu, có thể giao tiếp đơn giản bằng tín hiệu mùi hương và rung động mặt đáy biển. Vai trò sinh thái của đoàn cực kỳ quan trọng: dọn sạch xác chết, tái chế dinh dưỡng, ngăn chặn dịch bệnh và ô nhiễm đáy biển — Huyền Quy gọi chúng là "Hải Dương Tịnh Cốt Sư." Các Hải Tộc khác ghê tởm chúng — không ai muốn nhìn cảnh hàng triệu con bọ đang gặm xác đồng loại — nhưng thầm biết ơn vì không ai muốn tự tay dọn dẹp chiến trường. Trong thế giới Hải Tộc, "bị so sánh với Hải Trùng" là lời sỉ nhục nặng nề nhất, nhưng mỉa mai thay, chính Hải Trùng lại là loài không bao giờ sỉ nhục ai.

## IV. Cơ Cấu Tổ Chức (组织结构)
Đoàn không có hệ thống tổ chức chính thức theo nghĩa thông thường. Trùng Vương Giáp Xác là cá thể lớn nhất và duy nhất có linh trí đủ cao để ra quyết định, phát tín hiệu mùi hương đặc biệt gọi là "Trùng Lệnh" để dẫn đàn đến nguồn thức ăn mới — mùi hương này có thể truyền xa hàng dặm trong nước biển. Khoảng một trăm cá thể cỡ lớn đóng vai trò "chiến binh" — bảo vệ Trùng Vương và thăm dò vùng mới, nhưng bản chất vẫn là hành động bản năng chứ không phải mệnh lệnh có ý thức. Phó Trùng Giáp là con bọ lớn thứ hai, luôn đi phía trước đoàn để dò đường — nếu Phó Trùng gặp nguy, cả đoàn biết phải chuyển hướng. Phần còn lại — gần ba triệu cá thể — là đàn trùng phổ thông, di chuyển theo mùi hương của Trùng Vương như một dòng sông sống, bao phủ đáy biển và phân hủy mọi thứ hữu cơ trên đường đi. Khi Trùng Vương chết, cá thể lớn nhất tiếp theo sẽ tự động thay thế — quá trình chuyển giao quyền lực đơn giản và tàn nhẫn: bầy đàn ăn luôn xác Trùng Vương cũ, không một chút do dự.

## V. Công Pháp & Trận Pháp (功法 与 阵法)
Hải Trùng Đoàn không có công pháp — mọi khả năng đều là bản năng sinh học tiến hóa qua hàng triệu năm. Khả năng phân hủy là sức mạnh cốt lõi: axit tiêu hóa mà chúng tiết ra — gọi là "Trùng Toan" — có thể ăn mòn pháp khí cấp thấp, hòa tan xương cốt hải thú chỉ trong vài ngày, và thậm chí làm suy yếu trận pháp nếu có đủ số lượng tập trung. Khi bị đe dọa, cả đàn cuộn lại thành hình cầu khổng lồ — hàng triệu lớp giáp xác chồng lên nhau tạo thành tường phòng thủ dày đặc gọi là "Trùng Cầu Trận," axit tiết ra từ bên trong khiến bất kỳ kẻ nào xuyên qua đều bị ăn mòn — trong chiến sử Vô Tận Hải, có ghi chép rằng một tu sĩ Trúc Cơ hải tặc từng cố xuyên qua Trùng Cầu và ra ngoài chỉ còn bộ xương trắng ở trong bộ giáp đã tan một nửa. Đây không phải trận pháp mà là phản xạ bầy đàn, nhưng hiệu quả phòng thủ đáng kinh ngạc — ngay cả Kim Đan tu sĩ cũng ngại đối đầu với quả cầu giáp xác ba triệu con, không phải vì không phá nổi mà vì kinh tởm.

## VI. Đặc Sản Môn Phái (门派特产)
**Axit Tiêu Hóa Linh Tính (Trùng Toan):** Chất lỏng do Hải Trùng tiết ra, có khả năng ăn mòn hầu hết vật liệu hữu cơ và pháp khí cấp thấp, màu vàng nâu với mùi chua khẳn đặc trưng. Luyện khí sư thu thập thông qua trung gian — thường là tán tu dùng bình ngọc hứng ở rìa đàn trùng — để dùng trong quá trình luyện chế, đặc biệt hữu ích khi cần hòa tan nguyên liệu cứng như vảy hải thú hay xương rồng biển. **Giáp Xác Trùng Phiến:** Mảnh giáp rụng tự nhiên từ những cá thể lớn khi lột xác, cứng hơn thép thường và kháng axit tốt — thợ thủ công biển thu gom để chế tạo áo giáp cấp thấp hoặc dụng cụ chống ăn mòn, một bộ giáp Trùng Phiến đầy đủ bán được năm mươi linh thạch hạ phẩm. **Trùng Phấn:** Phân của Hải Trùng sau khi phân hủy xác chết, giàu dinh dưỡng linh tính, là loại phân bón tốt nhất cho tảo linh và linh thực vật thủy sinh — Hải Tảo Nông Dân Hội mua một sọt Trùng Phấn với giá mười linh thạch hạ phẩm, rẻ hơn phân bón linh thông thường một nửa nhưng hiệu quả gấp ba.

## VII. Cơ Sở Hạ Tầng (基础设施)
**Bãi Trầm Tích Cổ Đại (Trùng Nguyên):** Vùng đáy biển phẳng nơi đoàn cư trú chính, tích tụ hàng nghìn năm xác sinh vật phân hủy tạo thành lớp trầm tích dày hàng trượng — lớp trầm tích này mềm xốp, ấm hơn đáy biển xung quanh, và phát ra mùi hương phân hủy đặc trưng mà Hải Tộc gọi là "Mùi Trùng Nguyên." Bên dưới lớp trầm tích có thể chứa hóa thạch và di vật từ các kỷ nguyên trước, nhưng không ai muốn đào xuống kiểm tra vì phải đi qua ba triệu con bọ giáp. **Tổ Trùng Vương:** Khu vực nhỏ ở trung tâm Trùng Nguyên nơi Trùng Vương Giáp Xác thường trú ngụ, bao quanh bởi một vòng tròn cá thể lớn canh gác — trầm tích ở đây dày nhất, ấm nhất, giàu dinh dưỡng nhất, và được nén chặt thành một dạng "ngai" tự nhiên mà Trùng Vương nằm trên suốt ngày. **Dòng Sông Trùng:** Khi di chuyển đến nguồn thức ăn mới, hàng triệu cá thể tạo thành một "dòng sông" sống chảy trên đáy biển, dài có khi hàng chục dặm — cảnh tượng vừa hùng vĩ vừa kinh hoàng đối với bất kỳ Hải Tộc nào chứng kiến, ai nhìn thấy Dòng Sông Trùng đều biết rằng ở đầu kia có chiến trường hoặc thảm họa.

## VIII. Kinh Tế (经济)
Hải Trùng Đoàn không có khái niệm kinh tế theo nghĩa thông thường — chúng không mua bán, không tích trữ, không hiểu giá trị của linh thạch. Tuy nhiên, hoạt động của đoàn tạo ra giá trị kinh tế gián tiếp đáng kể cho toàn bộ Vô Tận Hải. Axit tiêu hóa linh tính được các thương nhân thu thập và bán cho luyện khí sư trên đất liền với giá ba linh thạch hạ phẩm một bình. Trùng phấn là loại phân bón tốt nhất cho tảo linh, được Hải Tảo Nông Dân Hội và Hải Thảo Dược Sư sử dụng rộng rãi. Giáp xác rụng được thợ thủ công biển thu gom để chế tạo — một nghề riêng gọi là "Trùng Giáp Sư" đã hình thành quanh việc thu hoạch và chế tác vảy giáp. Tất cả những giao dịch này đều diễn ra mà Hải Trùng Đoàn không hay biết — chúng chỉ ăn, phân hủy, và để lại sản phẩm phụ cho người khác lợi dụng, là "nhà sản xuất" lớn nhất Vô Tận Hải mà không nhận được một xu thù lao.

## IX. Lịch Sử Tóm Tắt (简史)
Hải Trùng Đoàn tồn tại từ thuở sơ khai của Vô Tận Hải, là một trong những dạng sống cổ xưa nhất còn tồn tại trên đáy biển — Huyền Quy nói rằng khi lão mới sinh ra cách đây mười vạn năm, Hải Trùng đã ở đó. Qua hàng triệu năm, đoàn đã âm thầm dọn dẹp mọi thứ chết chóc — từ xác cá nhỏ đến xương cốt hải thú thượng cổ, từ tàn tích chiến trường đến di vật văn minh đã diệt vong. Trong lịch sử, sau mỗi đại chiến lớn, các thế lực thắng cuộc thường bắt Hải Trùng Đoàn làm "nô lệ dọn dẹp" — xua đàn trùng đến chiến trường bằng cách ném xác chết dọc đường làm mồi nhử. Mỗi lần như vậy, số lượng cá thể bùng nổ nhờ nguồn thức ăn dồi dào, khiến đoàn ngày càng lớn mạnh hơn — theo ghi chép của Hải Quy trưởng lão, dân số hiện tại ba triệu là lớn nhất trong lịch sử, gấp ba lần thời kỳ trước Đại Chiến Hải Yêu một trăm năm trước. Gần đây, số lượng xác chết ở vùng biển nam tăng vọt bất thường — Hải Trùng Đoàn đang mở rộng lãnh thổ về phía đó, điều mà các thế lực tinh ý coi là điềm báo chiến tranh sắp đến hoặc thảm họa sinh thái đang diễn ra.

## X. Giai Thoại & Bí Mật (轶事 与 秘密)
Trùng Vương Giáp Xác đã sống hơn nghìn năm — tuổi thọ bất thường cho một sinh vật cấp thấp — bởi vì nó từng ăn xác một con hải thú thượng cổ tên Ám Hải Cự Giáp chứa tinh hoa cổ đại. Chính bữa ăn đó đã khai mở linh trí cho nó và nâng tu vi lên Trúc Cơ, biến nó từ một con bọ biển bình thường thành Trùng Vương — đây cũng là lý do nó lớn bất thường so với đồng loại. Trong bụng Trùng Vương vẫn còn một mảnh vỏ giáp từ Ám Hải Cự Giáp chưa tiêu hóa được, toàn bộ linh lực của nó đều đến từ mảnh vỏ đó — nếu ai lấy được mảnh vỏ này, Trùng Vương sẽ thoái hóa về thành bọ biển thường ngay lập tức. Trong lịch sử, mỗi lần Hải Trùng Đoàn bùng nổ số lượng bất thường, một đại chiến sẽ xảy ra sau đó — hoặc ngược lại, đại chiến vừa xảy ra. Có người cho rằng chúng "biết trước" chiến tranh, nhưng thực tế có thể là bản năng sinh tồn phát hiện tín hiệu xung đột sớm hơn bất kỳ hệ thống trinh sát nào — xác chết phát ra "mùi chết" trước khi chìm xuống đáy biển, và Hải Trùng đánh hơi mùi đó từ rất xa. Dù bị coi thường, nếu Hải Trùng Đoàn biến mất, đáy biển sẽ chìm trong xác chết thối rữa, dịch bệnh tràn lan, và hệ sinh thái Vô Tận Hải sẽ sụp đổ trong vài thập kỷ — sự phụ thuộc này lớn hơn bất kỳ ai muốn thừa nhận.

## XI. Quan Hệ Thế Lực (势力关系)
Hải Trùng Đoàn ở vị trí đặc biệt trong hệ thống thế lực Vô Tận Hải: bị coi thường nhất nhưng cũng không thể thiếu nhất. Hải Thần Cung lợi dụng đoàn như công cụ dọn dẹp miễn phí sau chiến trận, không bao giờ trả công hay công nhận đóng góp — Tả Tướng Quân từng nói: "Trùng dọn rác là bản năng, trả công cho bản năng là ngu." Hắc Hải Hải Tặc ghê tởm chúng nhưng không đánh vì không có lý do — xác chết do hải tặc tạo ra lại nuôi sống đàn trùng, tạo thành mối quan hệ gián tiếp kỳ lạ mà cả hai bên đều không muốn thừa nhận. Hải Quy Trưởng Lão Hội, đặc biệt là Huyền Quy, là một trong số ít thế lực hiểu và tôn trọng vai trò sinh thái của Hải Trùng Đoàn — dù hai bên không giao thiệp trực tiếp, sự tôn trọng ngầm đó là mối quan hệ tích cực duy nhất mà đoàn có. Huyền Quy từng cảnh báo Hải Thần Cung: "Ngày nào các ngươi xua hết Trùng đi, ngày đó đáy biển sẽ chôn vùi cả cung điện các ngươi."
