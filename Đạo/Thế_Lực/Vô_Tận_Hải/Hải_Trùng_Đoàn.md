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

## I. Tổng Quan (总览)
Hải Trùng Đoàn là tập hợp hàng triệu sinh vật đáy biển cấp thấp — bọ giáp biển, giun biển, và các loài giáp xác nhỏ — đóng vai trò "đội vệ sinh" vĩnh cửu của Vô Tận Hải. Với dân số ước tính ba triệu cá thể nhưng không xếp hạng trong bảng thế lực, đoàn tồn tại từ thuở sơ khai của đại dương, chuyên phân hủy xác chết và tái chế dinh dưỡng cho hệ sinh thái biển sâu. Đứng đầu là Trùng Vương Giáp Xác, con bọ biển linh lớn nhất với kích thước bằng con chó, tu vi tương đương Trúc Cơ Sơ Kỳ. Dù bị mọi chủng tộc khác ghê tởm và coi thường, đoàn đóng vai trò sinh thái không thể thay thế — nếu không có chúng, đáy biển sẽ chìm trong xác chết thối rữa và hệ sinh thái sẽ sụp đổ.

## II. Địa Lý & Tài Nguyên (地理 与 资源)
Hải Trùng Đoàn hoạt động chủ yếu trên bề mặt đáy biển bằng phẳng vùng phía tây, nơi xác sinh vật chết từ tầng nước trên chìm xuống tích tụ theo thời gian. Khu vực rộng lớn nhưng nghèo linh khí — đáy biển phẳng không có linh mạch, ánh sáng không tới, nhiệt độ thấp và áp suất cao. Tài nguyên chính là xác chết hải thú, cá, thực vật biển — nguồn dinh dưỡng duy nhất nuôi sống cả đàn. Sau mỗi trận chiến lớn giữa Hải Thần Cung và Hắc Hải Hải Tặc, hàng nghìn xác chết trôi xuống đáy biển — đó là lúc Hải Trùng Đoàn được "bữa tiệc" lớn nhất, số lượng cá thể bùng nổ trong vài tuần. Gần đây, số lượng xác chết tăng vọt ở vùng biển nam, khiến đoàn đang mở rộng lãnh thổ về phía đó với tốc độ đáng lo ngại.

## III. Văn Hóa & Tín Ngưỡng (文化 与 信仰)
Hải Trùng Đoàn gồm các sinh vật cấp thấp — bọ giáp biển, giun biển, và giáp xác nhỏ chuyên phân hủy xác chết, phần lớn hành động theo bản năng ăn, ngủ, sinh sản mà không có văn hóa hay tín ngưỡng phức tạp. Chỉ có Trùng Vương Giáp Xác và vài chục cá thể lớn nhất đã khai mở linh trí ở mức tối thiểu, có thể giao tiếp đơn giản bằng tín hiệu mùi hương và rung động. Vai trò sinh thái của đoàn cực kỳ quan trọng: dọn sạch xác chết, tái chế dinh dưỡng, ngăn chặn dịch bệnh và ô nhiễm đáy biển. Các Hải Tộc khác ghê tởm chúng — không ai muốn nhìn cảnh hàng triệu con bọ đang gặm xác đồng loại — nhưng thầm biết ơn vì không ai muốn tự tay dọn dẹp chiến trường. Trong thế giới Hải Tộc, "bị so sánh với Hải Trùng" là lời sỉ nhục nặng nề nhất.

## IV. Cơ Cấu Tổ Chức (组织结构)
Đoàn không có hệ thống tổ chức chính thức theo nghĩa thông thường. Trùng Vương Giáp Xác là cá thể lớn nhất và duy nhất có linh trí đủ cao để ra quyết định, phát tín hiệu mùi hương đặc biệt để dẫn đàn đến nguồn thức ăn mới. Khoảng một trăm cá thể cỡ lớn đóng vai trò "chiến binh" — bảo vệ Trùng Vương và thăm dò vùng mới, nhưng bản chất vẫn là hành động bản năng chứ không phải mệnh lệnh có ý thức. Phần còn lại — gần ba triệu cá thể — là đàn trùng phổ thông, di chuyển theo mùi hương của Trùng Vương như một dòng sông sống, bao phủ đáy biển và phân hủy mọi thứ hữu cơ trên đường đi. Khi Trùng Vương chết, cá thể lớn nhất tiếp theo sẽ tự động thay thế — quá trình chuyển giao quyền lực đơn giản và tàn nhẫn.

## V. Công Pháp & Trận Pháp (功法 与 阵法)
Hải Trùng Đoàn không có công pháp — mọi khả năng đều là bản năng sinh học tiến hóa qua hàng triệu năm. Khả năng phân hủy là sức mạnh cốt lõi: axit tiêu hóa mà chúng tiết ra có thể ăn mòn pháp khí cấp thấp, hòa tan xương cốt hải thú chỉ trong vài ngày, và thậm chí làm suy yếu trận pháp nếu có đủ số lượng tập trung. Khi bị đe dọa, cả đàn cuộn lại thành hình cầu khổng lồ — hàng triệu lớp giáp xác chồng lên nhau tạo thành tường phòng thủ dày đặc, axit tiết ra từ bên trong khiến bất kỳ kẻ nào xuyên qua đều bị ăn mòn. Đây không phải trận pháp mà là phản xạ bầy đàn, nhưng hiệu quả phòng thủ đáng kinh ngạc — ngay cả Kim Đan tu sĩ cũng ngại đối đầu với quả cầu giáp xác ba triệu con.

## VI. Đặc Sản Môn Phái (门派特产)
- **Axit Tiêu Hóa Linh Tính:** Chất lỏng do Hải Trùng tiết ra, có khả năng ăn mòn hầu hết vật liệu hữu cơ và pháp khí cấp thấp. Luyện khí sư thu thập (thông qua trung gian) để dùng trong quá trình luyện chế, đặc biệt hữu ích khi cần hòa tan nguyên liệu cứng.
- **Giáp Xác Trùng Phiến:** Mảnh giáp rụng tự nhiên từ những cá thể lớn, cứng hơn thép thường và kháng axit tốt. Thợ thủ công biển thu gom để chế tạo áo giáp cấp thấp hoặc dụng cụ chống ăn mòn.
- **Trùng Phấn:** Phân của Hải Trùng sau khi phân hủy xác chết, giàu dinh dưỡng linh tính, là loại phân bón tốt nhất cho tảo linh và linh thực vật thủy sinh.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Bãi Trầm Tích Cổ Đại:** Vùng đáy biển phẳng nơi đoàn cư trú chính, tích tụ hàng nghìn năm xác sinh vật phân hủy tạo thành lớp trầm tích dày hàng trượng. Bên dưới lớp trầm tích có thể chứa hóa thạch và di vật từ các kỷ nguyên trước.
- **Tổ Trùng Vương:** Khu vực nhỏ nơi Trùng Vương Giáp Xác thường trú ngụ, bao quanh bởi một vòng tròn cá thể lớn canh gác. Không phải kiến trúc mà là một vùng trầm tích dày nhất, ấm nhất, giàu dinh dưỡng nhất.
- **Dòng Sông Trùng:** Khi di chuyển đến nguồn thức ăn mới, hàng triệu cá thể tạo thành một "dòng sông" sống chảy trên đáy biển, dài có khi hàng dặm — cảnh tượng vừa hùng vĩ vừa kinh hoàng đối với bất kỳ Hải Tộc nào chứng kiến.

## VIII. Kinh Tế (经济)
Hải Trùng Đoàn không có khái niệm kinh tế theo nghĩa thông thường — chúng không mua bán, không tích trữ, không hiểu giá trị của linh thạch. Tuy nhiên, hoạt động của đoàn tạo ra giá trị kinh tế gián tiếp đáng kể cho toàn bộ Vô Tận Hải. Axit tiêu hóa linh tính được các thương nhân thu thập và bán cho luyện khí sư trên đất liền. Trùng phấn là loại phân bón tốt nhất cho tảo linh, được Hải Tảo Nông Dân Hội và Hải Thảo Dược Sư sử dụng. Giáp xác rụng được thợ thủ công biển thu gom để chế tạo. Tất cả những giao dịch này đều diễn ra mà Hải Trùng Đoàn không hay biết — chúng chỉ ăn, phân hủy, và để lại sản phẩm phụ cho người khác lợi dụng.

## IX. Lịch Sử Tóm Tắt (简史)
Hải Trùng Đoàn tồn tại từ thuở sơ khai của Vô Tận Hải, là một trong những dạng sống cổ xưa nhất còn tồn tại trên đáy biển. Qua hàng triệu năm, đoàn đã âm thầm dọn dẹp mọi thứ chết chóc — từ xác cá nhỏ đến xương cốt hải thú thượng cổ, từ tàn tích chiến trường đến di vật văn minh đã diệt vong. Trong lịch sử, sau mỗi đại chiến lớn, các thế lực thắng cuộc thường bắt Hải Trùng Đoàn làm "nô lệ dọn dẹp" — xua đàn trùng đến chiến trường để xóa sạch dấu vết. Mỗi lần như vậy, số lượng cá thể bùng nổ nhờ nguồn thức ăn dồi dào, khiến đoàn ngày càng lớn mạnh hơn. Gần đây, số lượng xác chết ở vùng biển nam tăng vọt bất thường — Hải Trùng Đoàn đang mở rộng lãnh thổ về phía đó, điều mà các thế lực tinh ý coi là điềm báo chiến tranh sắp đến.

## X. Giai Thoại & Bí Mật (轶事 与 秘密)
Trùng Vương Giáp Xác đã sống hơn nghìn năm — tuổi thọ bất thường cho một sinh vật cấp thấp — bởi vì nó từng ăn xác một con hải thú thượng cổ chứa tinh hoa cổ đại. Chính bữa ăn đó đã khai mở linh trí cho nó và nâng tu vi lên Trúc Cơ, biến nó từ một con bọ biển bình thường thành Trùng Vương. Trong lịch sử, mỗi lần Hải Trùng Đoàn bùng nổ số lượng bất thường, một đại chiến sẽ xảy ra sau đó — hoặc ngược lại, đại chiến vừa xảy ra. Có người cho rằng chúng "biết trước" chiến tranh, nhưng thực tế có thể là bản năng sinh tồn phát hiện tín hiệu xung đột sớm hơn bất kỳ hệ thống trinh sát nào. Dù bị coi thường, nếu Hải Trùng Đoàn biến mất, đáy biển sẽ chìm trong xác chết thối rữa, dịch bệnh tràn lan, và hệ sinh thái Vô Tận Hải sẽ sụp đổ trong vài thập kỷ — sự phụ thuộc này lớn hơn bất kỳ ai muốn thừa nhận.

## XI. Quan Hệ Thế Lực (势力关系)
Hải Trùng Đoàn ở vị trí đặc biệt trong hệ thống thế lực Vô Tận Hải: bị coi thường nhất nhưng cũng không thể thiếu nhất. Hải Thần Cung lợi dụng đoàn như công cụ dọn dẹp miễn phí sau chiến trận, không bao giờ trả công hay công nhận đóng góp. Hắc Hải Hải Tặc ghê tởm chúng nhưng không đánh vì không có lý do — xác chết do hải tặc tạo ra lại nuôi sống đàn trùng, tạo thành mối quan hệ gián tiếp kỳ lạ. Hải Quy Trưởng Lão Hội, đặc biệt là Huyền Quy, là một trong số ít thế lực hiểu và tôn trọng vai trò sinh thái của Hải Trùng Đoàn — dù hai bên không giao thiệp trực tiếp, sự tôn trọng ngầm đó là mối quan hệ tích cực duy nhất mà đoàn có.
