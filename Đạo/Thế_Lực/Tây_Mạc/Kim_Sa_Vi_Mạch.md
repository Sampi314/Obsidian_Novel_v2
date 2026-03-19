---
type: faction
name: Kim Sa Vi Mạch
hantu: 金沙微脉
faction_type: Bộ Lạc
alignment: -2
race: Vi Tộc (Kim Linh Vi Thể)
region: Tây Mạc
founded: Hồng Hoang (tồn tại từ thuở khai thiên)
founder: Không có (hình thành tự nhiên)
emblem: Mach_Vang_Ngam.png
specialty: Cảm ứng mạch khoáng, Điều khiển kim linh vi lượng, Thông tin địa chất
economy:
- Không có kinh tế theo nghĩa thông thường
- Hấp thu vi lượng kim linh từ mạch vàng để duy trì sự sống
- Sở hữu thông tin về toàn bộ mỏ vàng và mạch khoáng sa mạc (giá trị vô hạn nhưng không ai biết)
arcs:
  - arc: 1
    status: Di tản — Mạch Chủ dẫn toàn tộc rút về phía tây
    rank: Không Xếp Hạng
    leader: Mạch Chủ
    population: 5
    territory:
      - Mạch vàng và mạch khoáng ngầm dưới Hoàng Kim Sa Hải
    assets:
      - name: Bản Đồ Mạch Khoáng Toàn Sa Mạc (trong trí nhớ tập thể)
        type: Tư Liệu
    stats: [5, 50, 5, 5, 10, 5]
    divisions:
      - name: Quần Thể Vi Mạch
        role: Duy trì sự sống trong mạch vàng, thăm dò mạch mới, di tản khi bị đe dọa
        headcount:
          truong_lao: 1
          chien_binh: 0
          dan_thuong: 4
        members:
          - character: "[Mạch Chủ]"
            position: Mạch Chủ — Cá thể sáng nhất
            cultivation: Trúc Cơ Sơ Kỳ (tương đương)
            placeholder: true
    relationships:
      - faction: Kim Sa Thợ Mỏ Hội
        description: Kẻ thù tự nhiên một chiều — thợ mỏ khai thác phá hủy mạch ngầm là nhà của Vi Mạch, nhưng thợ mỏ hoàn toàn không biết sự tồn tại của Vi Tộc.
        diplomacy:
          lien_minh: 0
          tin: 0
          uy_hiep: 0
          thuong_mai: 0
          on_oan: -50
          le_thuoc: 0
      - faction: Sa Thạch Du Mục
        description: Chủng tộc duy nhất nhận ra sự tồn tại của Vi Mạch — đôi khi họ "nghe" thấy Vi Mạch di chuyển qua rung động trong đá, nhưng không can thiệp.
        diplomacy:
          lien_minh: 0
          tin: 10
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 0
      - faction: Thiên Sa Thương Hội
        description: Kẻ thù gián tiếp — thương hội tài trợ và điều phối khai thác mỏ trên quy mô lớn, gây ra sự phá hủy mạch ngầm có hệ thống mà Vi Mạch không thể chống lại.
        diplomacy:
          lien_minh: 0
          tin: 0
          uy_hiep: 0
          thuong_mai: 0
          on_oan: -30
          le_thuoc: 0
---

# Kim Sa Vi Mạch (金沙微脉)

> *"Cát vàng khắp Hoàng Kim Sa Hải — ai cũng thấy, ai cũng giẫm lên, nhưng không ai biết đó là máu của chúng tôi."*
> — Rung động của Mạch Chủ, được Sa Thạch Du Mục ghi nhận nhưng không giải mã nổi

> *"Mỏ Ngủ là mỏ có hồn — ta không biết hồn gì, nhưng ta biết: đào đến khi nó thức, thì muộn rồi."*
> — Đội Trưởng Mỏ Trần Kim Cương, ghi trong nhật ký khai thác
> *"Cát vàng dưới chân ta không phải cát — đó là lịch sử của một chủng tộc mà ta giẫm lên mỗi ngày."*
> — Trưởng Lão Nham Phong, nói khi dạy tộc nhân về "tiếng đá hát"



## I. Tổng Quan (总览)

Kim Sa Vi Mạch là một chủng tộc vi thể bí ẩn sống trong mạch vàng và mạch khoáng ngầm dưới toàn bộ Hoàng Kim Sa Hải, tồn tại từ thuở hồng hoang trước khi bất kỳ chủng tộc nào đặt chân lên sa mạc. Mỗi cá thể nhỏ bằng hạt cát vàng, di chuyển bên trong mạch khoáng như máu chảy trong huyết quản, và chính chúng là lý do sa mạc mang tên "Hoàng Kim" — cát vàng óng ánh khắp Hoàng Kim Sa Hải là sản phẩm bài tiết của Vi Mạch qua hàng triệu năm. Mạch Chủ — cá thể sáng nhất, to bằng hạt cát lớn — dẫn dắt toàn tộc bằng tín hiệu rung động, và hiện đang lãnh đạo cuộc di tản lớn về phía tây để tránh xa các mỏ đang bị Nhân Tộc khai thác. Triết lý sống giản đơn: "Mạch vàng là nhà — ai phá nhà, là kẻ thù." Trong toàn bộ Tây Mạc, không một tu sĩ hay thương nhân nào ngờ rằng dưới chân mình tồn tại cả một dân tộc đang chạy nạn.

## II. Địa Lý & Tài Nguyên (地理 与 资源)

Kim Sa Vi Mạch phân bố khắp hệ thống mạch vàng và mạch khoáng ngầm dưới Hoàng Kim Sa Hải, từ lớp cát gần bề mặt đến các mạch sâu hàng trăm trượng. Hệ thống mạch ngầm chằng chịt như mạng lưới huyết quản, nối liền mọi mỏ vàng, mỏ linh thạch, và mạch khoáng trong toàn sa mạc — trong đó ba nút giao lớn nhất được Vi Mạch gọi là Trung Huyết Điểm, Bắc Huyết Điểm và Nam Huyết Điểm. Trung Huyết Điểm — nơi Mạch Chủ từng cư trú — nằm ngay dưới khu mỏ lớn nhất của Kim Sa Thợ Mỏ Hội, buộc Mạch Chủ phải bỏ đi cách đây năm mươi năm. Vi Mạch biết chính xác vị trí của mọi nguồn tài nguyên ngầm — thông tin có thể đáng giá hơn bất kỳ kho báu nào nếu có ai biết cách khai thác, nhưng Vi Mạch không có phương tiện giao tiếp với chủng tộc khác. Tuy nhiên, sự mở rộng khai thác mỏ của Nhân Tộc đang phá hủy mạch ngầm với tốc độ ngày càng nhanh, buộc Vi Mạch phải liên tục di tản, mất dần lãnh thổ và nguồn kim linh nuôi sống toàn tộc. Vùng mạch cổ nhất — Thái Sơ Mạch — nằm sâu ba trăm trượng dưới rìa tây Hoàng Kim Sa Hải, vẫn nguyên vẹn vì chưa ai đào sâu đến thế, là nơi mà Vi Mạch coi như "thánh địa" cuối cùng.

## III. Văn Hóa & Tín Ngưỡng (文化 与 信仰)
> *"Kim Chấn Hoan Ca vang lên, cát lấp lánh — Kim Ai Bi Minh vang lên, đá khóc."*
> — Sa Thạch Du Mục miêu tả hai hiện tượng mà họ cảm nhận nhưng không hiểu


Vi Mạch không có văn hóa theo nghĩa thông thường mà vận hành theo bản năng tập thể, nhưng qua hàng triệu năm, một số hành vi đã trở thành "truyền thống" bất biến. Quy tắc cốt lõi là không bao giờ tiết lộ vị trí mạch vàng cho chủng tộc khác — dù thực tế chúng không có cách giao tiếp với bên ngoài, quy tắc này vẫn được duy trì như bản năng phòng vệ sâu nhất. Khi phát hiện mạch khoáng mới, toàn tộc rung động ăn mừng trong nghi thức được gọi là "Kim Chấn Hoan Ca" — tạo ra hiện tượng mặt cát phía trên hơi lấp lánh mà đôi khi lữ khách nhầm tưởng là ảo giác sa mạc, nhưng thực ra là hàng triệu vi thể cùng rung lên trong niềm vui. Khi một mạch cổ bị phá hủy, Vi Mạch phát ra rung động trầm buồn kéo dài nhiều ngày — "Kim Ai Bi Minh" — mà Sa Thạch Du Mục đôi khi cảm nhận được và gọi là "tiếng đá khóc." Phản ứng khi mạch bị khai thác rất nhất quán: Vi Mạch di tản trước khi cuốc mỏ chạm đến, để lại mạch rỗng cho thợ mỏ — và trước khi rời đi, chúng "vắt" hết kim linh ra khỏi mạch như một hành vi vừa là sinh tồn vừa là trả thù thầm lặng. Vì thế, Kim Sa Thợ Mỏ Hội thường xuyên đào trúng các mạch khoáng "trống không" mà không hiểu lý do.

## IV. Cơ Cấu Tổ Chức (组织结构)

Tổ chức của Kim Sa Vi Mạch hoàn toàn khác biệt với mọi thế lực khác, phản ánh bản chất vi thể của chủng tộc. Mạch Chủ là cá thể sáng nhất và to nhất — hiện đang cư trú tại một nút giao mạch nhỏ gần Tây Huyết Điểm — đóng vai trò trung tâm phát tín hiệu điều phối. Bốn cá thể "Mạch Phụ" lớn thứ hai đến thứ năm phân bố ở bốn hướng, đóng vai trò trạm trung chuyển tín hiệu. Hàng ngàn cá thể trinh sát nhỏ bé liên tục thăm dò mạch mới, báo cáo về Mạch Chủ qua rung động — tốc độ truyền tin đạt ba trăm dặm mỗi ngày, nhanh hơn bất kỳ hệ thống liên lạc nào trên mặt đất. Hàng triệu cá thể quần thể phân bố khắp mạch ngầm, mỗi cá thể hấp thu vi lượng kim linh để tồn tại. Không có hệ thống cấp bậc rõ ràng ngoài Mạch Chủ — toàn tộc hành động như một cơ thể thống nhất, trong đó Mạch Chủ là "bộ não" và các cá thể khác là "tế bào". Tổng quần thể lên đến hàng triệu nhưng xét về sức mạnh cá thể thì gần như bằng không. Khi Mạch Chủ già đi và sáng yếu dần, cá thể sáng nhất trong bốn Mạch Phụ sẽ tự động thay thế — quá trình kế vị diễn ra tự nhiên qua hàng trăm năm mà không có bất kỳ xung đột nào.

## V. Công Pháp & Trận Pháp (功法 与 阵法)

Kim Sa Vi Mạch không tu luyện theo nghĩa truyền thống mà hấp thu vi lượng kim linh từ mạch vàng để duy trì sự sống — một dạng tu luyện thụ động tự nhiên, chậm chạp nhưng không ngừng nghỉ qua hàng triệu năm. Khả năng bẩm sinh nổi bật nhất là "Địa Mạch Cảm Ứng": phát hiện mọi mạch vàng, mỏ linh thạch, và nguồn khoáng sản trong phạm vi cực rộng — Mạch Chủ có thể cảm ứng toàn bộ mạch ngầm trong bán kính năm trăm dặm — đồng thời cảm nhận ngay lập tức khi bất kỳ mạch nào bị khai thác. Khi bị đe dọa, Mạch Chủ có thể ra lệnh "Kim Mạch Tức Diệt" — làm mạch khoáng "tắt" tạm thời, ngưng phát linh lực, khiến mỏ trở nên vô giá trị trong mắt kẻ khai thác. Đây là cơ chế phòng vệ duy nhất, và cũng giải thích tại sao nhiều mỏ ở Tây Mạc bỗng dưng cạn kiệt rồi lại hồi phục sau vài năm — hiện tượng mà thợ mỏ gọi là "Mỏ Ngủ." Ngoài ra, khi toàn tộc tập trung tại một mạch lớn, sự hiện diện của hàng triệu vi thể kim linh tạo ra "Kim Quang Ức Chế Trường" — vùng không gian mà la bàn và thiên hướng thuật đều mất hiệu, khiến thợ mỏ không thể xác định chính xác vị trí mạch. Đội Trưởng Mỏ Trần Kim Cương gọi hiện tượng này là "Quỷ La Bàn" và coi đó là lời nguyền của sa mạc.

## VI. Đặc Sản Môn Phái (门派特产)

- **Cát Vàng Hoàng Kim:** Sản phẩm bài tiết tự nhiên qua hàng triệu năm, chính là thứ tạo nên màu vàng óng ánh đặc trưng của Hoàng Kim Sa Hải. Mỗi hạt cát vàng chứa vi lượng kim linh có giá trị trong luyện đan kim hệ — đan sư Phế Khí Luyện Đan Phường từng phát hiện rằng một nghìn cân cát Hoàng Kim có thể chiết xuất được một giọt "Kim Linh Tinh Lộ" dùng trong đan dược cường hóa kinh mạch kim hệ, nhưng chi phí chiết xuất cao hơn giá trị thu được.
- **Bản Đồ Mạch Khoáng Sống:** Trí nhớ tập thể của toàn tộc chứa vị trí chính xác của mọi mỏ vàng, mỏ linh thạch và mạch khoáng trong sa mạc — thông tin vô giá nhưng không thể trích xuất. Nếu ai tìm cách giao tiếp với Vi Mạch, sẽ nắm trong tay chìa khóa kinh tế của toàn Tây Mạc — Thiên Sa Thương Hội sẵn sàng trả bất kỳ giá nào cho thông tin này.
- **Hiệu Ứng Lấp Lánh (Kim Chấn Quang):** Khi toàn tộc rung động trong Kim Chấn Hoan Ca, mặt cát phía trên hiện tượng lấp lánh kỳ ảo, đôi khi bị nhầm là dấu hiệu của mỏ vàng gần bề mặt — đã có không ít thợ mỏ đào bới điên cuồng tại những điểm này chỉ để tìm thấy cát trống, và đôi khi mất mạng vì say nắng.

## VII. Cơ Sở Hạ Tầng (基础设施)

- **Nút Giao Mạch Chủ (Tây Huyết Điểm):** Điểm giao nhau hiện tại của hệ thống mạch ngầm phía tây, nơi Mạch Chủ đang tạm cư trú sau cuộc di tản từ Trung Huyết Điểm. Nằm sâu bảy mươi trượng dưới mặt cát, được bao quanh bởi quặng vàng thuần tịnh chưa bị phát hiện — một mỏ tiềm năng khổng lồ mà nếu lộ ra, sẽ khiến cả Tây Mạc chấn động.
- **Mạng Lưới Mạch Ngầm:** Hệ thống mạch vàng và khoáng tự nhiên trải khắp sa mạc, tổng chiều dài ước tính hàng vạn dặm, đóng vai trò vừa là nhà ở, vừa là đường giao thông, vừa là nguồn thức ăn cho Vi Mạch. Mạch chính có đường kính từ một đến ba thước, mạch phụ nhỏ chỉ bằng ngón tay.
- **Trạm Trinh Sát (Đoan Mạch):** Các điểm cuối của mạch ngầm nơi cá thể trinh sát đóng quân, cảm nhận mọi rung động từ bề mặt. Có tổng cộng khoảng ba trăm Đoan Mạch rải khắp Hoàng Kim Sa Hải, tạo thành mạng lưới giám sát toàn diện mà không ai trên mặt đất ngờ tới.
- **Thái Sơ Mạch:** Mạch cổ nhất và sâu nhất, ba trăm trượng dưới rìa tây sa mạc, chứa kim linh nguyên thủy đậm đặc gấp mười lần mạch thường — nơi Vi Mạch coi là "thánh địa," nguồn sống cuối cùng nếu mọi mạch khác bị phá hủy.
- **Mạch Cổ Hồ Tàng:** Những đoạn mạch đã cạn kiệt kim linh nhưng được Vi Mạch giữ lại làm nơi ẩn náu khẩn cấp khi mạch chính bị khai thác, giống như boongke phòng thủ tự nhiên.

## VIII. Kinh Tế (经济)

Kim Sa Vi Mạch không có kinh tế theo nghĩa thông thường. Chúng không giao dịch, không trao đổi, và không tích lũy tài sản — khái niệm "sở hữu" hoàn toàn xa lạ với chủng tộc này. Nguồn sống duy nhất là vi lượng kim linh hấp thu từ mạch vàng — quá trình tự nhiên không cần nỗ lực, chỉ cần mạch còn tồn tại. Tuy nhiên, xét ở góc độ rộng hơn, Vi Mạch gián tiếp ảnh hưởng đến nền kinh tế khai thác khoáng sản toàn Tây Mạc: khi chúng rời khỏi một mạch, mạch đó dần mất linh lực và trở nên kém giá trị — hiện tượng "Mỏ Ngủ"; khi chúng đến mạch mới, mạch đó bỗng trở nên giàu có — hiện tượng "Mỏ Thức." Điều này tạo ra chu kỳ "mỏ phồn thịnh rồi tàn lụi" mà các thợ mỏ và thương nhân quy cho thiên ý nhưng thực ra do Vi Mạch di cư. Thiên Sa Thương Hội đã mất không ít tiền vì đầu tư vào các mỏ bỗng dưng "tàn lụi" mà không hiểu nguyên nhân — riêng năm trước, ba mỏ phía đông đồng loạt "ngủ" khiến thương hội lỗ hơn năm ngàn linh thạch trung phẩm.

## IX. Lịch Sử Tóm Tắt (简史)
> *"Mỏ có ý chí riêng — ta tin chắc điều đó, dù không ai tin ta."*
> — Trần Kim Cương, ghi trong nhật ký khai thác, mục cuối cùng trước khi nghỉ hưu


Kim Sa Vi Mạch tồn tại từ thuở hồng hoang, trước khi bất kỳ chủng tộc có linh trí nào đặt chân lên Tây Mạc. Chúng là sinh vật nguyên thủy nhất của sa mạc, và sự hiện diện của chúng qua hàng triệu năm đã tạo ra Hoàng Kim Sa Hải — lớp cát vàng óng là sản phẩm bài tiết kim linh tích lũy từ đời này sang đời khác. Suốt thời gian dài, Vi Mạch sống yên bình vì không ai biết đến sự tồn tại của chúng. Bi kịch bắt đầu cách đây khoảng hai nghìn năm khi Nhân Tộc phát hiện mỏ vàng đầu tiên tại Trung Huyết Điểm — cuộc khai thác đó phá hủy hàng chục dặm mạch ngầm và giết chết vô số vi thể. Kim Sa Thợ Mỏ Hội ra đời năm trăm năm trước, biến khai thác mỏ thành ngành công nghiệp có hệ thống, đẩy nhanh sự tàn phá. Một trăm năm trước, Thiên Sa Thương Hội bắt đầu tài trợ khai thác quy mô lớn, và tốc độ mất mạch ngầm tăng vọt. Mạch Chủ hiện tại đang dẫn toàn tộc dần rút về phía tây, hướng tới rìa Vĩnh Tịch Chi Địa — nơi không ai dám đào — như là nơi trú ẩn cuối cùng.

## X. Giai Thoại & Bí Mật (轶事 与 秘密)

Kim Sa Thợ Mỏ Hội không biết rằng mỗi khi đào trúng mạch khoáng "trống không", thực ra là Vi Mạch đã cảm nhận rung động bước chân thợ mỏ từ xa — chính xác từ khoảng cách năm dặm — và di tản toàn bộ trước khi cuốc chạm đến. Đội Trưởng Mỏ Trần Kim Cương đã ghi nhận hiện tượng "Mỏ Ngủ" hơn ba mươi lần trong sự nghiệp và vẫn không tìm ra lời giải, lão viết trong nhật ký: "Mỏ có ý chí riêng — ta tin chắc điều đó, dù không ai tin ta." Hiện tượng nhiều mỏ ở Tây Mạc bỗng dưng cạn kiệt rồi lại hồi phục sau vài năm cũng do Vi Mạch rời đi rồi quay lại khi nguy hiểm qua đi. Mạch Chủ đang dẫn toàn tộc tiến gần hơn đến Vĩnh Tịch Chi Địa, nơi mà ngay cả Sa Thạch Du Mục cũng không dám bước vào — điều này đặt ra câu hỏi rúng động: liệu Vi Mạch biết gì về bản chất thực sự của vùng đất chết đó? Tại sao chúng dám đến nơi mọi sinh vật đều sợ hãi? Sa Thạch Du Mục là chủng tộc duy nhất nhận ra sự tồn tại của Vi Mạch, đôi khi họ "nghe" thấy tiếng rung vi tế trong đá khi Vi Mạch di chuyển — Trưởng Lão Du Mục Nham Phong gọi đó là "mạch đá hát" và coi là điềm báo tốt lành, nhưng không ngờ rằng đó là cả một chủng tộc đang sống dưới chân họ. Bí ẩn lớn nhất: gần đây Mạch Chủ phát ra một tín hiệu rung động chưa từng có — "Kim Cảm Dị Ba" — hướng về phía Vĩnh Tịch Chi Địa, như thể đang giao tiếp với thứ gì đó bên trong vùng đất chết. Và đáng lo ngại hơn: thứ bên trong Vĩnh Tịch Chi Địa đã đáp lại.

## XI. Quan Hệ Thế Lực (势力关系)

- **Kim Sa Thợ Mỏ Hội:** Kẻ thù tự nhiên một chiều và tàn khốc nhất. Thợ mỏ khai thác phá hủy mạch ngầm — nhà của Vi Mạch — nhưng hoàn toàn không biết Vi Tộc tồn tại. Vi Mạch không đủ sức phản kháng, chỉ có thể di tản trước khi bị ảnh hưởng. Mỗi cuốc đào là một ngôi nhà bị phá hủy, và kẻ phá nhà không hề biết mình đang làm gì.
- **Cổ Thạch Linh Mạch:** Những mạch khoáng cổ đại nằm sâu dưới lòng đất vẫn giữ nguyên trạng thái nguyên thủy từ thuở hồng hoang. Vi Mạch coi đây là "vùng cấm" không ai được xâm phạm — ngay cả khi mạch mới cạn kiệt, chúng cũng không khai thác Cổ Thạch Linh Mạch trừ khi sự sống còn của toàn tộc bị đe dọa.


- **Sa Thạch Du Mục:** Chủng tộc duy nhất cảm nhận được sự hiện diện của Vi Mạch qua rung động trong đá, nhưng không hiểu bản chất. Quan hệ trung lập — Sa Thạch Du Mục không khai thác mỏ nên không gây hại cho Vi Mạch. Trưởng Lão Nham Phong dạy tộc nhân tôn trọng "tiếng đá hát" — vô tình bảo vệ Vi Mạch mà không hề hay biết.
- **Thiên Sa Thương Hội:** Kẻ thù gián tiếp nhưng nguy hiểm bậc nhất. Thương hội tài trợ và điều phối hoạt động khai thác mỏ trên quy mô lớn khắp Tây Mạc, gây ra sự phá hủy mạch ngầm có hệ thống với tốc độ mà Vi Mạch không thể chạy kịp. Nếu Thiên Sa Thương Hội mở rộng khai thác sang phía tây — nơi Vi Mạch đang trú ẩn — toàn tộc sẽ đứng trước nguy cơ diệt vong thực sự.