---
type: faction
name: Vạn Yêu Thành Ngoại Vi
hantu: 万妖城外围
faction_type: Bộ Lạc
alignment: -1
race: Yêu Tộc cấp thấp (Đa chủng loài)
region: Đông Hoang
founded: Khoảng vài trăm năm trước (hình thành tự nhiên)
founder: Không có (cộng đồng tự phát)
emblem: Ngoai_Vi_Van_Yeu.png
specialty: Lao động rẻ, Buôn bán vặt vãnh, Trung gian giữa trong và ngoài thành
economy:
- Buôn bán hàng hóa cấp thấp và đồ phế thải
- Cung cấp lao động rẻ cho Nội Thành
- Chợ phiên ba ngày một lần
arcs:
  - arc: 1
    status: Tồn tại bấp bênh
    rank: Không Xếp Hạng
    leader: Hồ Tiểu Nương (không chính thức)
    population: 500
    territory:
      - Vành đai bên ngoài tường thành Vạn Yêu Thành (khoảng 5 dặm)
    assets:
      - name: Chợ Phiên Ngoại Vi
        type: Công Trình
    stats: [10, 5, 5, 500, 8, 10]
    divisions:
      - name: Cộng Đồng Ngoại Vi
        role: Sinh hoạt cộng đồng, trao đổi hàng hóa, trung gian với Nội Thành
        headcount:
          truong_lao: 1
          chien_binh: 15
          dan_thuong: 484
        members:
          - character: Hồ Tiểu Nương
            position: Người có tiếng nói nhất (không chính thức)
            cultivation: Trúc Cơ Hậu Kỳ
          - character: "[Lang Yêu Thủ Lĩnh]"
            position: Thủ lĩnh Khu Lang Yêu
            cultivation: Luyện Khí Viên Mãn
            placeholder: true
    relationships:
      - faction: Vạn Yêu Thành
        description: Bị coi thường nhưng không thể thiếu — Ngoại Vi cung cấp lao động rẻ và dịch vụ tạp vụ cho Nội Thành.
        diplomacy:
          lien_minh: 10
          tin: -10
          uy_hiep: -50
          thuong_mai: 40
          on_oan: -30
          le_thuoc: 70
      - faction: Hoang Dã Yêu Liên
        description: Yêu tộc hoang dã thỉnh thoảng ghé Ngoại Vi trao đổi hàng hóa và tin tức.
        diplomacy:
          lien_minh: 20
          tin: 20
          uy_hiep: 0
          thuong_mai: 30
          on_oan: 0
          le_thuoc: 0
      - faction: Hỗn Huyết Yêu Đoàn
        description: Nhiều yêu tộc hỗn huyết bị cả trong thành lẫn ngoài thành khinh bỉ, tìm đến nhau để nương tựa.
        diplomacy:
          lien_minh: 30
          tin: 30
          uy_hiep: 0
          thuong_mai: 20
          on_oan: 0
          le_thuoc: 0
---

# Vạn Yêu Thành Ngoại Vi (万妖城外围)

## I. Tổng Quan (总览)
Vạn Yêu Thành Ngoại Vi là cộng đồng tự phát của những yêu tộc cấp thấp không đủ tư cách bước qua cổng thành Vạn Yêu Thành. Không Xếp Hạng về sức mạnh — không có cường giả, không có trận pháp, không có tài nguyên đáng kể — nhưng cộng đồng này lại là mắt xích không thể thiếu trong bộ máy vận hành của Vạn Yêu Thành: nguồn lao động rẻ, dịch vụ tạp vụ, và lớp đệm giữa thành trì kiên cố bên trong với thế giới hoang dã bên ngoài. Người có tiếng nói nhất là Hồ Tiểu Nương — một yêu hồ già khôn ngoan ở cảnh giới Trúc Cơ Hậu Kỳ, không mang danh hiệu chính thức nào nhưng được mọi yêu tộc ngoại vi tôn trọng.

## II. Địa Lý & Tài Nguyên (地理与资源)
Ngoại Vi trải dài trên vành đai khoảng năm dặm bên ngoài tường thành Vạn Yêu Thành, nơi đất đai bằng phẳng nhưng không được bảo vệ bởi trận pháp hay phù văn nào. Lều lán tạm bợ dựng bằng gỗ mục và da thú rải rác không trật tự, quầy hàng rong lộ thiên bày bán đồ linh tinh, đường đi bùn lầy khi mưa và bụi mù khi nắng. Tài nguyên gần như không có — hàng hóa chủ yếu là đồ phế thải từ trong thành bị vứt ra, dược thảo tạp loại hái bên đường, và chiến lợi phẩm cấp thấp nhặt nhạnh từ yêu thú hoang dã xung quanh.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
Triết lý sống của Ngoại Vi là "sống được ngày nào hay ngày đó" — không có lý tưởng cao xa, không có ước mơ lớn lao, chỉ cần tồn tại qua ngày là đủ. Không có quy tắc chính thức — luật rừng chi phối, kẻ mạnh hơn nói to hơn. Tuy nhiên, cộng đồng có một ranh giới ngầm: ai quá hung hãn, giết đồng loại vô cớ hoặc cướp phá quá mức sẽ bị toàn bộ cộng đồng tẩy chay — không ai buôn bán, không ai giúp đỡ, tương đương với bản án tử ở nơi mà sự tương trợ là điều kiện sống còn.

Chợ phiên mỗi ba ngày là sự kiện quan trọng nhất — yêu tộc cấp thấp từ khắp nơi tụ tập trao đổi hàng hóa, tin tức, và đôi khi cả câu chuyện phiếm. Chợ phiên là lúc duy nhất Ngoại Vi có chút sinh khí giống một cộng đồng thực sự.

## IV. Cơ Cấu Tổ Chức (组织结构)
Không có hệ thống tổ chức chính thức. Hồ Tiểu Nương đóng vai trò trung gian và người giải quyết tranh chấp — bà không ra lệnh ai mà dùng sự khôn ngoan và quan hệ để thuyết phục. Cộng đồng tự nhiên chia thành nhiều khu nhỏ theo chủng loại yêu: khu hồ yêu, khu lang yêu, khu thỏ yêu, khu điểu yêu... Mỗi khu có một "thủ lĩnh" tự phong — thường là cá thể mạnh nhất hoặc già nhất — nhưng quyền lực chỉ giới hạn trong khu nhỏ của mình. Dân số khoảng năm trăm, biến động theo mùa — mùa đông giảm vì yêu tộc yếu chết rét, mùa hè tăng vì lưu dân mới đến.

## V. Công Pháp & Trận Pháp (功法与阵法)
Không có công pháp hay trận pháp. Tuyệt đại đa số yêu tộc ngoại vi là phàm yêu hoặc Luyện Khí Sơ Kỳ, dựa hoàn toàn vào bản năng huyết mạch để sinh tồn — móng vuốt, răng nanh, và giác quan nhạy bén là "vũ khí" duy nhất. Vài cá thể may mắn có huyết mạch tốt hơn có thể tự mò mẫm hấp thu linh khí từ môi trường, nhưng không có người dẫn dắt nên hiệu quả cực kỳ thấp và nguy hiểm.

## VI. Đặc Sản Môn Phái (门派特产)
- **Lao Động Rẻ:** "Đặc sản" lớn nhất của Ngoại Vi — yêu tộc cấp thấp sẵn sàng làm mọi việc nặng nhọc, bẩn thỉu cho Nội Thành để đổi lấy thức ăn hoặc vài viên linh thạch hạ phẩm.
- **Tin Tức Ngoài Thành:** Yêu tộc ngoại vi tiếp xúc với thế giới bên ngoài nhiều hơn cư dân Nội Thành, nên đôi khi nắm được thông tin về di chuyển của các thế lực, bí cảnh mở cửa, hoặc yêu thú lạ xuất hiện.
- **Dược Thảo Tạp Loại:** Thảo dược cấp thấp hái từ vùng hoang địa xung quanh, không đủ tinh thuần để vào Chợ Đen nhưng vẫn có giá trị cho yêu tộc nghèo.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Chợ Phiên Ngoại Vi:** Khu đất trống giữa cộng đồng, ba ngày một lần biến thành chợ tạm với hàng chục quầy hàng lộ thiên.
- **Lều Lán Cộng Đồng:** Không có kiến trúc kiên cố — toàn bộ là lều lán tạm bợ bằng gỗ, da thú, và vải rách, có thể dựng lên hoặc dỡ bỏ trong vài giờ.
- **Giếng Chung:** Một giếng nước do Hồ Tiểu Nương vận động đào cách đây năm mươi năm — nguồn nước sạch duy nhất, được coi là "tài sản" quý giá nhất của cộng đồng.

## VIII. Kinh Tế (经济)
Kinh tế Ngoại Vi ở mức sinh tồn — không có tích lũy, không có thặng dư. Đa số yêu tộc sống qua ngày bằng cách săn bắt côn trùng và thú nhỏ hoang dã, hái dược thảo tạp loại bán cho khách vãng lai, hoặc vào Nội Thành làm lao động tạp dịch đổi lấy thức ăn thừa. Chợ phiên là hoạt động kinh tế duy nhất có tổ chức, nhưng quy mô nhỏ bé — toàn bộ giá trị giao dịch trong một phiên chợ có lẽ không bằng một giao dịch nhỏ nhất trong Chợ Đen Nội Thành. Tiền tệ chủ yếu là trao đổi hiện vật, linh thạch hạ phẩm cực hiếm.

## IX. Lịch Sử Tóm Tắt (简史)
Ngoại Vi hình thành tự nhiên khi Vạn Yêu Thành xây tường thành và thiết lập tiêu chuẩn để phân biệt yêu tộc "đủ tư cách" vào trong và "không đủ" ở ngoài. Tiêu chuẩn đơn giản và tàn nhẫn: phải đạt ít nhất Trúc Cơ, hoặc có huyết mạch quý hiếm, hoặc sở hữu tài nguyên có giá trị. Những yêu tộc cấp thấp không đáp ứng được — phàm yêu, huyết mạch loãng, tu vi thấp — bị từ chối ở cổng thành, tụ tập bên ngoài buôn bán vặt vãnh và chờ đợi một cơ hội có lẽ không bao giờ đến.

Ngoại Vi đã tồn tại hàng trăm năm, bị coi thường bởi cả Nội Thành lẫn thế giới bên ngoài. Nhưng nó không thể bị xóa sổ vì một lý do thực dụng: Nội Thành cần lao động rẻ, cần người làm việc bẩn thỉu mà yêu tộc cấp cao không thèm đụng tay — và Ngoại Vi cung cấp chính xác điều đó.

## X. Giai Thoại & Bí Mật (轶事与秘密)
Hồ Tiểu Nương thực ra có đủ tư cách vào Nội Thành — tu vi Trúc Cơ Hậu Kỳ và huyết mạch hồ yêu đủ chuẩn. Bà chọn ở ngoài vì có lý do riêng mà không ai biết. Có giả thuyết rằng bà đang canh giữ ai đó trong cộng đồng Ngoại Vi — một yêu tộc ẩn giấu huyết mạch cổ đại dưới vỏ bọc phàm yêu, và nhiệm vụ của bà là bảo vệ kẻ đó cho đến khi thời cơ chín muồi.

Trong cộng đồng ngoại vi có vài yêu tộc cố tình giả yếu để tránh bị chú ý — huyết mạch thực sự của chúng có thể truy ngược về những dòng tộc cổ đại đã tuyệt chủng. Lý do chúng ẩn mình ở nơi tận cùng đáy xã hội vẫn là bí ẩn — có thể chạy trốn kẻ thù, có thể chờ đợi điều gì đó, hoặc đơn giản là đã mệt mỏi với cuộc chiến sinh tồn của kẻ mạnh.

## XI. Quan Hệ Thế Lực (势力关系)
- **Vạn Yêu Thành:** Mối quan hệ bất bình đẳng — Ngoại Vi phụ thuộc hoàn toàn vào Nội Thành về kinh tế nhưng bị đối xử như tầng lớp thấp nhất.
- **Hoang Dã Yêu Liên:** Yêu tộc hoang dã thỉnh thoảng ghé chợ phiên trao đổi tin tức và hàng hóa.
- **Hỗn Huyết Yêu Đoàn:** Chia sẻ cảnh ngộ bị khinh bỉ, thỉnh thoảng giúp đỡ lẫn nhau.
