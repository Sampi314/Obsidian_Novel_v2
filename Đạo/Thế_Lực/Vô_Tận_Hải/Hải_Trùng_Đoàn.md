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

> *"Biển sâu có kẻ không ngủ, không nghỉ, chỉ ăn. Ăn hết cái chết để biển tiếp tục sống. Ngươi gọi chúng là sâu bọ — ta gọi chúng là ân nhân."*
> — Một lão ngư dân vô danh, nói với đệ tử Hải Thần Cung đang nhăn mặt khi nhìn thấy Dòng Sông Trùng

## I. Tổng Quan (总览)
Hải Trùng Đoàn là tập hợp hàng triệu sinh vật đáy biển cấp thấp — bọ giáp biển, giun biển, và các loài giáp xác nhỏ — đóng vai trò "đội vệ sinh" vĩnh cửu của Vô Tận Hải. Với dân số ước tính ba triệu cá thể nhưng không xếp hạng trong bảng thế lực, đoàn tồn tại từ thuở sơ khai của đại dương, chuyên phân hủy xác chết và tái chế dinh dưỡng cho hệ sinh thái biển sâu.

Đứng đầu là Trùng Vương Giáp Xác, con bọ biển linh lớn nhất với kích thước bằng con chó, tu vi tương đương Trúc Cơ Sơ Kỳ — sinh vật duy nhất trong đoàn có linh trí đủ cao để nhận thức bản thân là "ta" chứ không phải "đàn." Dù bị mọi chủng tộc khác ghê tởm và coi thường, đoàn đóng vai trò sinh thái không thể thay thế — nếu không có chúng, đáy biển sẽ chìm trong xác chết thối rữa và hệ sinh thái sẽ sụp đổ.

Trong ngữ cảnh Hải Tộc, câu "đi gặp Hải Trùng" đồng nghĩa với "chết" — một cách nói vừa ghê tởm vừa chính xác đến đáng sợ. Nhưng có một sự thật mà ít ai muốn đối mặt: mọi sinh vật biển, từ cá bé đến hải thú vĩ đại, từ ngư dân đến Hải Thần — cuối cùng đều "gặp" Hải Trùng.

> *"Biển cả bình đẳng hơn mọi vương quốc — vì sau khi chết, Long Vương hay cá rô đều thành bữa ăn của bọ giáp."*
> — Câu nói lưu truyền trong giới tán tu biển sâu

## II. Địa Lý & Tài Nguyên (地理 与 资源)
Hải Trùng Đoàn hoạt động chủ yếu trên bề mặt đáy biển bằng phẳng vùng phía tây, tại khu vực mà Hải Tộc gọi là "Trùng Nguyên" — vùng trầm tích rộng hàng trăm dặm vuông, nơi xác sinh vật chết từ tầng nước trên chìm xuống tích tụ theo thời gian. Khu vực rộng lớn nhưng nghèo linh khí — đáy biển phẳng không có linh mạch, ánh sáng không tới, nhiệt độ thấp và áp suất cao, mùi thối rữa nồng nặc đến mức sinh vật thông thường không thể tồn tại quá một ngày.

Tài nguyên chính là xác chết hải thú, cá, thực vật biển — nguồn dinh dưỡng duy nhất nuôi sống cả đàn. Sau mỗi trận chiến lớn giữa Hải Thần Cung và Hắc Hải Hải Tặc, hàng nghìn xác chết trôi xuống đáy biển — đó là lúc Hải Trùng Đoàn được "bữa tiệc" lớn nhất, số lượng cá thể bùng nổ trong vài tuần, mật độ dày đến mức đáy biển dường như chuyển động như một tấm thảm sống.

Trùng Nguyên chia thành ba vùng mà ngư dân biển sâu ghi nhận: **Bạch Cốt Bãi** phía bắc — nơi xương cốt hải thú lớn tích tụ thành đống trắng xóa dưới đáy, xương đã bị bọ giáp gặm sạch thịt nhưng quá cứng để phân hủy hoàn toàn, tạo thành cảnh quan ma mị dưới ánh lân quang; **Hắc Nê Trầm** ở trung tâm — lớp bùn đen dày hàng trượng do xác chết phân hủy tích tụ nghìn năm, mềm đến mức bất kỳ vật nặng nào rơi xuống đều bị nuốt chửng; và **Tân Trùng Nguyên** phía nam — khu vực mới hình thành chỉ trong vài năm do số lượng xác chết ở vùng biển nam tăng vọt bất thường vì Huyết Độc, đoàn đang mở rộng lãnh thổ về phía đó với tốc độ đáng lo ngại.

> *"Trùng Nguyên phía nam mới hình thành rộng ngang Trùng Nguyên cũ đã tích lũy hàng ngàn năm — điều đó nghĩa là lượng xác chết ở biển nam trong vài năm qua bằng cả nghìn năm trước. Ngươi có hiểu điều đó đáng sợ đến mức nào không?"*
> — Huyền Quy, cảnh báo các thế lực Hải Tộc trong cuộc họp mùa thu

## III. Văn Hóa & Tín Ngưỡng (文化 与 信仰)
Hải Trùng Đoàn gồm các sinh vật cấp thấp — bọ giáp biển, giun biển, và giáp xác nhỏ chuyên phân hủy xác chết, phần lớn hành động theo bản năng ăn, ngủ, sinh sản mà không có văn hóa hay tín ngưỡng phức tạp. Chỉ có Trùng Vương Giáp Xác và vài chục cá thể lớn nhất — gọi là "Trùng Giáp" — đã khai mở linh trí ở mức tối thiểu, có thể giao tiếp đơn giản bằng tín hiệu mùi hương và rung động mặt đáy biển.

Vai trò sinh thái của đoàn cực kỳ quan trọng: dọn sạch xác chết, tái chế dinh dưỡng, ngăn chặn dịch bệnh và ô nhiễm đáy biển — Huyền Quy gọi chúng là "Hải Dương Tịnh Cốt Sư." Các Hải Tộc khác ghê tởm chúng — không ai muốn nhìn cảnh hàng triệu con bọ đang gặm xác đồng loại — nhưng thầm biết ơn vì không ai muốn tự tay dọn dẹp chiến trường.

Trong thế giới Hải Tộc, "bị so sánh với Hải Trùng" là lời sỉ nhục nặng nề nhất, nhưng mỉa mai thay, chính Hải Trùng lại là loài không bao giờ sỉ nhục ai. Giáp Xác — Trùng Vương — là cá thể duy nhất có đủ linh trí để hiểu mình bị khinh miệt, nhưng cũng là cá thể duy nhất không quan tâm. Huyền Quy kể rằng lần duy nhất giao tiếp được với Giáp Xác, lão đã hỏi: "Ngươi có tức giận khi bị coi thường không?" Giáp Xác chỉ quay đầu nhìn lão rồi tiếp tục gặm xương — câu trả lời rõ ràng nhất có thể.

> *"Ta hỏi Trùng Vương có buồn không khi bị ghê tởm. Nó nhìn ta bằng đôi mắt nghìn năm — đôi mắt đã nhìn thấy xác của vạn vạn sinh linh — rồi quay đi. Ta hiểu: nó đã thấy quá nhiều để còn biết buồn."*
> — Huyền Quy, kể lại trong hồi ký

## IV. Cơ Cấu Tổ Chức (组织结构)
Đoàn không có hệ thống tổ chức chính thức theo nghĩa thông thường. Trùng Vương Giáp Xác là cá thể lớn nhất và duy nhất có linh trí đủ cao để ra quyết định, phát tín hiệu mùi hương đặc biệt gọi là "Trùng Lệnh" để dẫn đàn đến nguồn thức ăn mới — mùi hương này có thể truyền xa hàng dặm trong nước biển. Khoảng một trăm cá thể cỡ lớn đóng vai trò "chiến binh" — bảo vệ Trùng Vương và thăm dò vùng mới, nhưng bản chất vẫn là hành động bản năng chứ không phải mệnh lệnh có ý thức.

Phó Trùng Giáp là con bọ lớn thứ hai, luôn đi phía trước đoàn để dò đường — nếu Phó Trùng gặp nguy, cả đoàn biết phải chuyển hướng. Phó Trùng hiện tại — cá thể mà tán tu biển đặt tên là "Nhị Giáp" — có vỏ giáp đen bóng với ba vết sẹo dài trên lưng, dấu tích từ lần bị cá mập linh tấn công nhưng sống sót, và kể từ đó đàn trùng tự động tránh xa mọi cá mập trong phạm vi mười dặm.

Phần còn lại — gần ba triệu cá thể — là đàn trùng phổ thông, di chuyển theo mùi hương của Trùng Vương như một dòng sông sống, bao phủ đáy biển và phân hủy mọi thứ hữu cơ trên đường đi. Khi Trùng Vương chết, cá thể lớn nhất tiếp theo sẽ tự động thay thế — quá trình chuyển giao quyền lực đơn giản và tàn nhẫn: bầy đàn ăn luôn xác Trùng Vương cũ, không một chút do dự. Giáp Xác biết điều này — nó biết rằng bầy đàn mà nó dẫn dắt sẽ là bầy đàn ăn thịt nó khi nó chết — nhưng đó là quy luật đáy biển, không cần thay đổi và cũng không thể thay đổi.

## V. Công Pháp & Trận Pháp (功法 与 阵法)
Hải Trùng Đoàn không có công pháp — mọi khả năng đều là bản năng sinh học tiến hóa qua hàng triệu năm. Khả năng phân hủy là sức mạnh cốt lõi: axit tiêu hóa mà chúng tiết ra — gọi là "Trùng Toan" — có thể ăn mòn pháp khí cấp thấp, hòa tan xương cốt hải thú chỉ trong vài ngày, và thậm chí làm suy yếu trận pháp nếu có đủ số lượng tập trung.

Khi bị đe dọa, cả đàn cuộn lại thành hình cầu khổng lồ — hàng triệu lớp giáp xác chồng lên nhau tạo thành tường phòng thủ dày đặc gọi là "Trùng Cầu Trận," axit tiết ra từ bên trong khiến bất kỳ kẻ nào xuyên qua đều bị ăn mòn — trong chiến sử Vô Tận Hải, có ghi chép rằng một tu sĩ Trúc Cơ hải tặc từng cố xuyên qua Trùng Cầu và ra ngoài chỉ còn bộ xương trắng ở trong bộ giáp đã tan một nửa. Đây không phải trận pháp mà là phản xạ bầy đàn, nhưng hiệu quả phòng thủ đáng kinh ngạc — ngay cả Kim Đan tu sĩ cũng ngại đối đầu với quả cầu giáp xác ba triệu con, không phải vì không phá nổi mà vì kinh tởm.

Ngoài Trùng Cầu Trận, Giáp Xác còn phát triển một chiến thuật mà Huyền Quy gọi là "Trùng Triều" — khi đánh hơi được nguồn thức ăn khổng lồ (thường là chiến trường mới), Giáp Xác phát Trùng Lệnh đặc biệt khiến toàn bộ ba triệu cá thể đồng loạt di chuyển cùng lúc, tạo thành "cơn sóng thần" sinh vật trên đáy biển, nuốt chửng mọi thứ hữu cơ trên đường đi trong vài canh giờ. Tốc độ phân hủy khi Trùng Triều hoạt động nhanh gấp mười lần bình thường — một xác hải thú lớn bằng chiếc thuyền bị gặm sạch chỉ trong nửa ngày.

> *"Ta từng chứng kiến Trùng Triều một lần — ba triệu con bọ di chuyển cùng lúc, đáy biển rung chuyển như động đất. Khi chúng đi qua, chỉ còn cát trắng và xương."*
> — Lão thủy thủ Hắc Hải, kể tại quán rượu Hải Khẩu

## VI. Đặc Sản Môn Phái (门派特产)
**Axit Tiêu Hóa Linh Tính (Trùng Toan):** Chất lỏng do Hải Trùng tiết ra, có khả năng ăn mòn hầu hết vật liệu hữu cơ và pháp khí cấp thấp, màu vàng nâu với mùi chua khẳn đặc trưng. Luyện khí sư thu thập thông qua trung gian — thường là tán tu dùng bình ngọc hứng ở rìa đàn trùng — để dùng trong quá trình luyện chế, đặc biệt hữu ích khi cần hòa tan nguyên liệu cứng như vảy hải thú hay xương rồng biển. Một bình Trùng Toan bán được ba linh thạch hạ phẩm, nhưng quá trình thu thập nguy hiểm vì phải tiếp cận rìa đàn — tán tu tên Hải Phệ chuyên thu Trùng Toan tại Trùng Nguyên, cả hai tay phủ đầy sẹo ăn mòn, gọi đó là "giá phải trả cho nghề."

**Giáp Xác Trùng Phiến:** Mảnh giáp rụng tự nhiên từ những cá thể lớn khi lột xác, cứng hơn thép thường và kháng axit tốt — thợ thủ công biển thu gom để chế tạo áo giáp cấp thấp hoặc dụng cụ chống ăn mòn, một bộ giáp Trùng Phiến đầy đủ bán được năm mươi linh thạch hạ phẩm. Mảnh giáp từ Trùng Vương hoặc Trùng Giáp — lớn hơn và cứng hơn gấp ba — được coi là vật liệu quý, nhưng gần như không thể thu được vì chúng chìm vào Hắc Nê Trầm ngay sau khi rụng.

**Trùng Phấn:** Phân của Hải Trùng sau khi phân hủy xác chết, giàu dinh dưỡng linh tính, là loại phân bón tốt nhất cho tảo linh và linh thực vật thủy sinh — Hải Tảo Nông Dân Hội mua một sọt Trùng Phấn với giá mười linh thạch hạ phẩm, rẻ hơn phân bón linh thông thường một nửa nhưng hiệu quả gấp ba. Mùi của Trùng Phấn khó chịu đến mức thương nhân phải vận chuyển trong hộp đá biển niêm phong, và ngay cả vậy vẫn có lần khiến cả sọt hàng liền kề bị trả lại vì "mùi Trùng Nguyên bám vào."

## VII. Cơ Sở Hạ Tầng (基础设施)
**Bãi Trầm Tích Cổ Đại (Trùng Nguyên):** Vùng đáy biển phẳng nơi đoàn cư trú chính, tích tụ hàng nghìn năm xác sinh vật phân hủy tạo thành lớp trầm tích dày hàng trượng — lớp trầm tích này mềm xốp, ấm hơn đáy biển xung quanh, và phát ra mùi hương phân hủy đặc trưng mà Hải Tộc gọi là "Mùi Trùng Nguyên." Bên dưới lớp trầm tích có thể chứa hóa thạch và di vật từ các kỷ nguyên trước, nhưng không ai muốn đào xuống kiểm tra vì phải đi qua ba triệu con bọ giáp.

**Tổ Trùng Vương:** Khu vực nhỏ ở trung tâm Trùng Nguyên nơi Trùng Vương Giáp Xác thường trú ngụ, bao quanh bởi một vòng tròn cá thể lớn canh gác — trầm tích ở đây dày nhất, ấm nhất, giàu dinh dưỡng nhất, và được nén chặt thành một dạng "ngai" tự nhiên mà Trùng Vương nằm trên suốt ngày. Ngai Trùng Vương — khối trầm tích nén cứng hình tròn, đường kính ba trượng — phát ra ánh lân quang xanh nhạt do hàm lượng khoáng chất cao, là điểm sáng duy nhất trong đáy biển tối tăm mênh mông, có thể nhìn thấy từ khoảng cách mười dặm.

**Dòng Sông Trùng:** Khi di chuyển đến nguồn thức ăn mới, hàng triệu cá thể tạo thành một "dòng sông" sống chảy trên đáy biển, dài có khi hàng chục dặm — cảnh tượng vừa hùng vĩ vừa kinh hoàng đối với bất kỳ Hải Tộc nào chứng kiến, ai nhìn thấy Dòng Sông Trùng đều biết rằng ở đầu kia có chiến trường hoặc thảm họa. Dòng sông để lại "rãnh" trên đáy biển — vết lõm dài nơi trầm tích bị xới tung, mất nhiều tháng mới lấp đầy — ngư dân dùng rãnh này như bản đồ để tránh vùng nguy hiểm.

## VIII. Kinh Tế (经济)
Hải Trùng Đoàn không có khái niệm kinh tế theo nghĩa thông thường — chúng không mua bán, không tích trữ, không hiểu giá trị của linh thạch. Tuy nhiên, hoạt động của đoàn tạo ra giá trị kinh tế gián tiếp đáng kể cho toàn bộ Vô Tận Hải.

Axit tiêu hóa linh tính được các thương nhân thu thập và bán cho luyện khí sư trên đất liền với giá ba linh thạch hạ phẩm một bình. Trùng phấn là loại phân bón tốt nhất cho tảo linh, được Hải Tảo Nông Dân Hội và Hải Thảo Dược Sư sử dụng rộng rãi. Giáp xác rụng được thợ thủ công biển thu gom để chế tạo — một nghề riêng gọi là "Trùng Giáp Sư" đã hình thành quanh việc thu hoạch và chế tác vảy giáp. Tại chợ biển sâu Hải Khẩu, có hẳn một dãy hàng chuyên bán sản phẩm từ Hải Trùng — Trùng Toan, Trùng Phấn, Trùng Phiến — do tán tu thu gom và thương nhân phân phối. Dãy hàng này nằm ở góc xa nhất chợ vì mùi, nhưng không bao giờ vắng khách.

Tất cả những giao dịch này đều diễn ra mà Hải Trùng Đoàn không hay biết — chúng chỉ ăn, phân hủy, và để lại sản phẩm phụ cho người khác lợi dụng, là "nhà sản xuất" lớn nhất Vô Tận Hải mà không nhận được một xu thù lao. Một thương nhân tên Thủy Tài từng tính toán: tổng giá trị thương mại từ sản phẩm phụ Hải Trùng mỗi năm vượt hai vạn linh thạch hạ phẩm — trong khi Hải Trùng Đoàn nhận được chính xác số không.

## IX. Lịch Sử Tóm Tắt (简史)
Hải Trùng Đoàn tồn tại từ thuở sơ khai của Vô Tận Hải, là một trong những dạng sống cổ xưa nhất còn tồn tại trên đáy biển — Huyền Quy nói rằng khi lão mới sinh ra cách đây mười vạn năm, Hải Trùng đã ở đó. Qua hàng triệu năm, đoàn đã âm thầm dọn dẹp mọi thứ chết chóc — từ xác cá nhỏ đến xương cốt hải thú thượng cổ, từ tàn tích chiến trường đến di vật văn minh đã diệt vong.

Trong lịch sử, sau mỗi đại chiến lớn, các thế lực thắng cuộc thường bắt Hải Trùng Đoàn làm "nô lệ dọn dẹp" — xua đàn trùng đến chiến trường bằng cách ném xác chết dọc đường làm mồi nhử. Mỗi lần như vậy, số lượng cá thể bùng nổ nhờ nguồn thức ăn dồi dào, khiến đoàn ngày càng lớn mạnh hơn. Theo ghi chép của Hải Quy trưởng lão, dân số hiện tại ba triệu là lớn nhất trong lịch sử, gấp ba lần thời kỳ trước Đại Chiến Hải Yêu một trăm năm trước.

Sự kiện đáng nhớ nhất là "Đại Dọn Chiến Trường" sau Đại Chiến Hải Yêu — Hải Thần Cung xua Hải Trùng Đoàn dọn dẹp chiến trường kéo dài hàng trăm dặm, nơi hàng vạn xác chết Hải Tộc và hải thú chồng chất. Dòng Sông Trùng kéo dài suốt ba mươi dặm, mất mười bảy ngày để dọn sạch — khi kết thúc, số lượng cá thể tăng từ một triệu lên gần ba triệu, và Trùng Nguyên mở rộng thêm hai mươi dặm về phía nam. Hải Thần Cung không nói cảm ơn, chỉ ra lệnh "xong thì biến."

Gần đây, số lượng xác chết ở vùng biển nam tăng vọt bất thường — Hải Trùng Đoàn đang mở rộng lãnh thổ về phía đó, điều mà các thế lực tinh ý coi là điềm báo chiến tranh sắp đến hoặc thảm họa sinh thái đang diễn ra.

## X. Giai Thoại & Bí Mật (轶事 与 秘密)
Trùng Vương Giáp Xác đã sống hơn nghìn năm — tuổi thọ bất thường cho một sinh vật cấp thấp — bởi vì nó từng ăn xác một con hải thú thượng cổ tên Ám Hải Cự Giáp chứa tinh hoa cổ đại. Chính bữa ăn đó đã khai mở linh trí cho nó và nâng tu vi lên Trúc Cơ, biến nó từ một con bọ biển bình thường thành Trùng Vương — đây cũng là lý do nó lớn bất thường so với đồng loại. Trong bụng Trùng Vương vẫn còn một mảnh vỏ giáp từ Ám Hải Cự Giáp chưa tiêu hóa được, toàn bộ linh lực của nó đều đến từ mảnh vỏ đó — nếu ai lấy được mảnh vỏ này, Trùng Vương sẽ thoái hóa về thành bọ biển thường ngay lập tức.

Trong lịch sử, mỗi lần Hải Trùng Đoàn bùng nổ số lượng bất thường, một đại chiến sẽ xảy ra sau đó — hoặc ngược lại, đại chiến vừa xảy ra. Có người cho rằng chúng "biết trước" chiến tranh, nhưng thực tế có thể là bản năng sinh tồn phát hiện tín hiệu xung đột sớm hơn bất kỳ hệ thống trinh sát nào — xác chết phát ra "mùi chết" trước khi chìm xuống đáy biển, và Hải Trùng đánh hơi mùi đó từ rất xa. Huyền Quy gọi hiện tượng này là "Trùng Triệu" — điềm báo của bọ giáp — và từng cảnh báo: "Khi Trùng Nguyên mở rộng, hãy chuẩn bị cho chiến tranh."

Dù bị coi thường, nếu Hải Trùng Đoàn biến mất, đáy biển sẽ chìm trong xác chết thối rữa, dịch bệnh tràn lan, và hệ sinh thái Vô Tận Hải sẽ sụp đổ trong vài thập kỷ — sự phụ thuộc này lớn hơn bất kỳ ai muốn thừa nhận. Có một bí mật mà chỉ Huyền Quy biết: Trùng Vương Giáp Xác gần đây bắt đầu từ chối ăn xác chết bị nhiễm Huyết Độc — phát Trùng Lệnh đặc biệt khiến toàn đàn tránh xa. Đây là lần đầu tiên trong lịch sử Hải Trùng từ chối thức ăn — dấu hiệu cho thấy Huyết Độc nguy hiểm đến mức ngay cả "đội vệ sinh vĩnh cửu" của đại dương cũng không dám chạm vào.

> *"Hải Trùng từ chối ăn. Ngươi hiểu điều đó nghĩa là gì không? Nghĩa là thứ đang giết biển nam còn tệ hơn cả cái chết — vì ngay cả sinh vật chuyên ăn cái chết cũng sợ."*
> — Huyền Quy, nói với riêng một trưởng lão San Hô Đảo Quốc trong đêm khuya

## XI. Quan Hệ Thế Lực (势力关系)
Hải Trùng Đoàn ở vị trí đặc biệt trong hệ thống thế lực Vô Tận Hải: bị coi thường nhất nhưng cũng không thể thiếu nhất.

**Hải Thần Cung** lợi dụng đoàn như công cụ dọn dẹp miễn phí sau chiến trận, không bao giờ trả công hay công nhận đóng góp — Tả Tướng Quân từng nói: "Trùng dọn rác là bản năng, trả công cho bản năng là ngu." Hải Thần Cung cũng thỉnh thoảng dùng Hải Trùng như vũ khí — xua đàn trùng vào lãnh thổ kẻ thù, để mùi thối rữa và cảnh tượng kinh hoàng phá vỡ tinh thần đối phương. Chiến thuật này bị coi là hèn hạ ngay cả trong giới Hải Tộc, nhưng hiệu quả không thể phủ nhận.

**Hắc Hải Hải Tặc** ghê tởm chúng nhưng không đánh vì không có lý do — xác chết do hải tặc tạo ra lại nuôi sống đàn trùng, tạo thành mối quan hệ gián tiếp kỳ lạ mà cả hai bên đều không muốn thừa nhận. Thủ lĩnh hải tặc Hắc Phong từng nói đùa: "Hải Trùng là đồng minh trung thành nhất của hải tặc — vì hải tặc tạo xác, Trùng ăn xác, không ai bị bắt."

**Hải Quy Trưởng Lão Hội**, đặc biệt là Huyền Quy, là một trong số ít thế lực hiểu và tôn trọng vai trò sinh thái của Hải Trùng Đoàn — dù hai bên không giao thiệp trực tiếp, sự tôn trọng ngầm đó là mối quan hệ tích cực duy nhất mà đoàn có. Huyền Quy từng cảnh báo Hải Thần Cung: "Ngày nào các ngươi xua hết Trùng đi, ngày đó đáy biển sẽ chôn vùi cả cung điện các ngươi." Và gần đây, với việc Trùng Vương từ chối ăn xác nhiễm Huyết Độc, Huyền Quy bắt đầu lo lắng thực sự — nếu Hải Trùng Đoàn không thể dọn dẹp xác chết ở biển nam, dịch bệnh sẽ bùng phát nhanh hơn bất kỳ ai tưởng.

> *"Ngày Hải Trùng ngừng ăn là ngày biển bắt đầu chết. Và ngày đó đã đến."*
> — Huyền Quy, ghi chú cá nhân, mùa đông năm nay
