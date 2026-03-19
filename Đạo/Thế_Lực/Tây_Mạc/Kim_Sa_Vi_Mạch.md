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

## I. Tổng Quan (总览)
Kim Sa Vi Mạch là một chủng tộc vi thể bí ẩn sống trong mạch vàng và mạch khoáng ngầm dưới toàn bộ Hoàng Kim Sa Hải, tồn tại từ thuở hồng hoang trước khi bất kỳ chủng tộc nào đặt chân lên sa mạc. Mỗi cá thể nhỏ bằng hạt cát vàng, di chuyển bên trong mạch khoáng như máu chảy trong huyết quản, và chính chúng là lý do sa mạc mang tên "Hoàng Kim" — cát vàng óng ánh khắp Hoàng Kim Sa Hải là sản phẩm bài tiết của Vi Mạch qua hàng triệu năm. Mạch Chủ — cá thể sáng nhất, to bằng hạt cát lớn — dẫn dắt toàn tộc bằng tín hiệu rung động, và hiện đang lãnh đạo cuộc di tản lớn về phía tây để tránh xa các mỏ đang bị Nhân Tộc khai thác. Triết lý sống giản đơn: "Mạch vàng là nhà — ai phá nhà, là kẻ thù".

## II. Địa Lý & Tài Nguyên (地理与资源)
Kim Sa Vi Mạch phân bố khắp hệ thống mạch vàng và mạch khoáng ngầm dưới Hoàng Kim Sa Hải, từ lớp cát gần bề mặt đến các mạch sâu hàng trăm trượng. Hệ thống mạch ngầm chằng chịt như mạng lưới huyết quản, nối liền mọi mỏ vàng, mỏ linh thạch, và mạch khoáng trong toàn sa mạc. Vi Mạch biết chính xác vị trí của mọi nguồn tài nguyên ngầm — thông tin có thể đáng giá hơn bất kỳ kho báu nào nếu có ai biết cách khai thác. Tuy nhiên, sự mở rộng khai thác mỏ của Nhân Tộc đang phá hủy mạch ngầm với tốc độ ngày càng nhanh, buộc Vi Mạch phải liên tục di tản, mất dần lãnh thổ và nguồn kim linh nuôi sống toàn tộc.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
Vi Mạch không có văn hóa theo nghĩa thông thường mà vận hành theo bản năng tập thể. Quy tắc cốt lõi là không bao giờ tiết lộ vị trí mạch vàng cho chủng tộc khác — dù thực tế chúng không có cách giao tiếp với bên ngoài. Khi phát hiện mạch khoáng mới, toàn tộc rung động ăn mừng, tạo ra hiện tượng mặt cát phía trên hơi lấp lánh mà đôi khi lữ khách nhầm tưởng là ảo giác sa mạc. Phản ứng khi mạch bị khai thác rất nhất quán: Vi Mạch di tản trước khi cuốc mỏ chạm đến, để lại mạch rỗng cho thợ mỏ. Vì thế, Kim Sa Thợ Mỏ Hội thường xuyên đào trúng các mạch khoáng "trống không" mà không hiểu lý do.

## IV. Cơ Cấu Tổ Chức (组织结构)
Tổ chức của Kim Sa Vi Mạch hoàn toàn khác biệt với mọi thế lực khác. Mạch Chủ là cá thể sáng nhất và to nhất, sống ở nút giao lớn nhất của mạch ngầm, đóng vai trò trung tâm phát tín hiệu điều phối. Hàng ngàn cá thể trinh sát nhỏ bé liên tục thăm dò mạch mới, báo cáo về Mạch Chủ qua rung động. Hàng triệu cá thể quần thể phân bố khắp mạch ngầm, mỗi cá thể hấp thu vi lượng kim linh để tồn tại. Không có hệ thống cấp bậc rõ ràng ngoài Mạch Chủ — toàn tộc hành động như một cơ thể thống nhất, trong đó Mạch Chủ là "bộ não" và các cá thể khác là "tế bào". Tổng quần thể lên đến hàng triệu nhưng xét về sức mạnh cá thể thì gần như bằng không.

## V. Công Pháp & Trận Pháp (功法与阵法)
Kim Sa Vi Mạch không tu luyện theo nghĩa truyền thống mà hấp thu vi lượng kim linh từ mạch vàng để duy trì sự sống — một dạng tu luyện thụ động tự nhiên. Khả năng bẩm sinh nổi bật nhất là cảm ứng mạch khoáng: phát hiện mọi mạch vàng, mỏ linh thạch, và nguồn khoáng sản trong phạm vi cực rộng, đồng thời cảm nhận ngay lập tức khi bất kỳ mạch nào bị khai thác. Khi bị đe dọa, Mạch Chủ có thể ra lệnh làm mạch khoáng "tắt" — ngưng phát linh lực tạm thời, khiến mỏ trở nên vô giá trị trong mắt kẻ khai thác. Đây là cơ chế phòng vệ duy nhất, và cũng giải thích tại sao nhiều mỏ ở Tây Mạc bỗng dưng cạn kiệt rồi lại hồi phục sau vài năm.

## VI. Đặc Sản Môn Phái (门派特产)
- **Cát Vàng Hoàng Kim:** Sản phẩm bài tiết tự nhiên qua hàng triệu năm, chính là thứ tạo nên màu vàng óng ánh đặc trưng của Hoàng Kim Sa Hải, chứa vi lượng kim linh có giá trị trong luyện đan kim hệ.
- **Bản Đồ Mạch Khoáng Sống:** Trí nhớ tập thể của toàn tộc chứa vị trí chính xác của mọi mỏ vàng, mỏ linh thạch và mạch khoáng trong sa mạc — thông tin vô giá nhưng không thể trích xuất.
- **Hiệu Ứng Lấp Lánh:** Khi toàn tộc rung động, mặt cát phía trên hiện tượng lấp lánh kỳ ảo, đôi khi bị nhầm là dấu hiệu của mỏ vàng gần bề mặt.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Nút Giao Mạch Chủ:** Điểm giao nhau lớn nhất của hệ thống mạch ngầm, nơi Mạch Chủ cư trú và phát tín hiệu điều phối toàn tộc. Vị trí liên tục thay đổi theo cuộc di tản về phía tây.
- **Mạng Lưới Mạch Ngầm:** Hệ thống mạch vàng và khoáng tự nhiên trải khắp sa mạc, đóng vai trò vừa là nhà ở, vừa là đường giao thông, vừa là nguồn thức ăn cho Vi Mạch.
- **Trạm Trinh Sát:** Các điểm cuối của mạch ngầm nơi cá thể trinh sát đóng quân, cảm nhận mọi rung động từ bề mặt.

## VIII. Kinh Tế (经济)
Kim Sa Vi Mạch không có kinh tế theo nghĩa thông thường. Chúng không giao dịch, không trao đổi, và không tích lũy tài sản. Nguồn sống duy nhất là vi lượng kim linh hấp thu từ mạch vàng — quá trình tự nhiên không cần nỗ lực. Tuy nhiên, xét ở góc độ rộng hơn, Vi Mạch gián tiếp ảnh hưởng đến nền kinh tế khai thác khoáng sản toàn Tây Mạc: khi chúng rời khỏi một mạch, mạch đó dần mất linh lực và trở nên kém giá trị; khi chúng đến mạch mới, mạch đó bỗng trở nên giàu có. Điều này tạo ra hiện tượng "mỏ phồn thịnh rồi tàn lụi" mà các thợ mỏ và thương nhân quy cho thiên ý nhưng thực ra do Vi Mạch di cư.

## IX. Lịch Sử Tóm Tắt (简史)
Kim Sa Vi Mạch tồn tại từ thuở hồng hoang, trước khi bất kỳ chủng tộc có linh trí nào đặt chân lên Tây Mạc. Chúng là sinh vật nguyên thủy nhất của sa mạc, và sự hiện diện của chúng qua hàng triệu năm đã tạo ra Hoàng Kim Sa Hải — lớp cát vàng óng là sản phẩm bài tiết kim linh tích lũy từ đời này sang đời khác. Suốt thời gian dài, Vi Mạch sống yên bình vì không ai biết đến sự tồn tại của chúng. Khi Nhân Tộc và các chủng tộc khác bắt đầu khai thác mỏ, mạch ngầm bị phá hủy dần, và Kim Sa Thợ Mỏ Hội — dù vô tình — trở thành kẻ thù lớn nhất. Mạch Chủ hiện tại đang dẫn toàn tộc dần rút về phía tây, hướng tới Vĩnh Tịch Chi Địa — nơi không ai dám đào — như là nơi trú ẩn cuối cùng.

## X. Giai Thoại & Bí Mật (轶事与秘密)
Kim Sa Thợ Mỏ Hội không biết rằng mỗi khi đào trúng mạch khoáng "trống không", thực ra là Vi Mạch đã cảm nhận rung động bước chân thợ mỏ từ xa và di tản toàn bộ trước khi cuốc chạm đến. Hiện tượng nhiều mỏ ở Tây Mạc bỗng dưng cạn kiệt rồi lại hồi phục sau vài năm cũng là do Vi Mạch rời đi rồi quay lại khi nguy hiểm qua đi. Mạch Chủ đang dẫn toàn tộc tiến gần hơn đến Vĩnh Tịch Chi Địa, nơi mà ngay cả Sa Thạch Du Mục cũng không dám bước vào — điều này đặt ra câu hỏi liệu Vi Mạch biết gì về bản chất thực sự của vùng đất chết đó. Sa Thạch Du Mục là chủng tộc duy nhất nhận ra sự tồn tại của Vi Mạch, đôi khi họ "nghe" thấy tiếng rung vi tế trong đá khi Vi Mạch di chuyển, nhưng coi đó là hiện tượng tự nhiên chứ không ngờ rằng đó là cả một chủng tộc đang sống dưới chân họ.

## XI. Quan Hệ Thế Lực (势力关系)
- **Kim Sa Thợ Mỏ Hội:** Kẻ thù tự nhiên một chiều. Thợ mỏ khai thác phá hủy mạch ngầm — nhà của Vi Mạch — nhưng hoàn toàn không biết Vi Tộc tồn tại. Vi Mạch không đủ sức phản kháng, chỉ có thể di tản trước khi bị ảnh hưởng.
- **Sa Thạch Du Mục:** Chủng tộc duy nhất cảm nhận được sự hiện diện của Vi Mạch qua rung động trong đá, nhưng không hiểu bản chất. Quan hệ trung lập — Sa Thạch Du Mục không khai thác mỏ nên không gây hại cho Vi Mạch.
- **Thiên Sa Thương Hội:** Kẻ thù gián tiếp. Thương hội tài trợ và điều phối hoạt động khai thác mỏ trên quy mô lớn khắp Tây Mạc, gây ra sự phá hủy mạch ngầm có hệ thống. Vi Mạch không biết thương hội tồn tại, chỉ cảm nhận được sự phá hủy ngày càng tăng.
