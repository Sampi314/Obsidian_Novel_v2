---
type: faction
name: Vũ Tộc Lưu Dân Trại
hantu: 羽族流民寨
faction_type: Bộ Lạc
alignment: 2
race: Vũ Tộc (Huyết mạch loãng, cánh nhỏ)
region: Đông Hoang
founded: Khoảng 30 năm trước
founder: Vũ Lạc Phong (Trại Chủ đời đầu, cha Vũ Lạc Vũ)
emblem: Canh_Nho_Van_La_Canh.png
specialty: Trinh sát trên không cấp thấp, Sinh tồn hoang dã, Kể chuyện truyền miệng
economy:
- Săn bắt trứng chim tuyết và côn trùng chịu lạnh
- Bán lông vũ rụng cho Lông Vũ Phường
- Cung cấp nhân lực cho Phong Vũ Trinh Sát Đội
arcs:
  - arc: 1
    status: Tồn tại bấp bênh
    rank: Không Xếp Hạng
    leader: Trại Chủ Vũ Lạc Vũ
    population: 90
    territory:
      - Vách đá trên tundra giữa Bắc Băng
    assets:
      - name: Tổ Phượng Hoàng Băng Bỏ Hoang
        type: Bí Cảnh
    stats: [8, 5, 10, 90, 5, 5]
    divisions:
      - name: Toàn Trại
        role: Sinh tồn, săn bắt, bảo vệ cộng đồng
        headcount:
          truong_lao: 1
          chien_binh: 15
          dan_thuong: 74
        members:
          - character: Vũ Lạc Vũ
            position: Trại Chủ
            cultivation: Trúc Cơ Sơ Kỳ
          - character: "[Bà Lão Cánh Bạc]"
            position: Trưởng Lão (không chính thức)
            cultivation: Kim Đan Sơ Kỳ (ẩn giấu)
            placeholder: true
    relationships:
      - faction: Vũ Hoàng Các
        description: Bị khinh bỉ và phủ nhận — Vũ Hoàng Các coi lưu dân như bụi trần không xứng mang danh Vũ Tộc.
        diplomacy:
          lien_minh: -50
          tin: -60
          uy_hiep: 0
          thuong_mai: -100
          on_oan: -30
          le_thuoc: 0
      - faction: Lông Vũ Phường
        description: Mối quan hệ thương mại duy nhất — Trại bán lông vũ rụng đổi lấy thức ăn và vật dụng thiết yếu.
        diplomacy:
          lien_minh: 10
          tin: 20
          uy_hiep: 0
          thuong_mai: 50
          on_oan: 0
          le_thuoc: 20
      - faction: Phong Vũ Trinh Sát Đội
        description: Trẻ con Vũ Tộc trong Trại gia nhập Đội để kiếm sống, đổi lại Đội bảo vệ Trại khỏi yêu thú.
        diplomacy:
          lien_minh: 30
          tin: 30
          uy_hiep: 0
          thuong_mai: 20
          on_oan: 0
          le_thuoc: 30
---

# Vũ Tộc Lưu Dân Trại (羽族流民寨)

## I. Tổng Quan (总览)
Vũ Tộc Lưu Dân Trại là trại tị nạn nhỏ bé của những Vũ Tộc bị Vũ Hoàng Các trục xuất vì huyết mạch không đủ thuần khiết hoặc cánh không đủ lớn. Không Xếp Hạng về sức mạnh, với chưa đầy một trăm người — đa số là phàm nhân hoặc Luyện Khí Sơ Kỳ — Trại tồn tại bấp bênh trên vách đá tundra giữa Bắc Băng, nơi gió rít qua khe đá tạo âm thanh ai oán. Trại Chủ Vũ Lạc Vũ — Vũ Tộc trung niên ở cảnh giới Trúc Cơ Sơ Kỳ, cánh nhỏ bay thấp, tính tình chất phác — là người duy nhất có tu vi đáng kể và gánh vác trách nhiệm bảo vệ toàn Trại. Dù nghèo khổ đến cùng cực, triết lý sống của Trại vẫn là "cánh nhỏ vẫn là cánh" — dù bị cả thế giới phủ nhận, họ vẫn tự hào là Vũ Tộc.

## II. Địa Lý & Tài Nguyên (地理与资源)
Trại đóng trên vách đá lởm chởm giữa vùng tundra Bắc Băng, xa cả Vũ Hoàng Các trên trời lẫn các tông môn lớn dưới đất. Vị trí hiểm trở — vách đá dốc đứng, gió lạnh thổi liên tục — là lợi thế phòng thủ duy nhất, vì yêu thú lớn khó leo lên. Hốc đá tự nhiên được mở rộng thành nơi trú ẩn, vừa đủ che mưa tuyết nhưng không đủ ấm. Tài nguyên cực kỳ nghèo nàn: trứng chim tuyết — nguồn protein chính, rêu đá — loại thực vật duy nhất mọc ở đây, và côn trùng chịu lạnh — thức ăn bổ sung. Nước uống từ tuyết tan, củi đốt từ gỗ trôi dạt — mọi thứ đều thiếu thốn và phải tiết kiệm từng chút.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
Trại không có tín ngưỡng chính thức, nhưng duy trì một truyền thống thiêng liêng: mỗi tối, lão nhân trong Trại kể chuyện về vinh quang xưa của Vũ Tộc cho trẻ nhỏ nghe — những câu chuyện về thời Vũ Tộc tự do bay khắp bầu trời, về những trận chiến hào hùng trên tầng mây. Đây không chỉ là giải trí mà là cách giữ cho ngọn lửa tự hào của Vũ Tộc không tắt, dù cánh nhỏ không bay cao.

Quy tắc trong Trại đơn giản và nghiêm ngặt: không ăn cắp của đồng tộc, bảo vệ trẻ con và người già trước tiên, chia sẻ thức ăn khi có và cùng nhịn khi thiếu. Ai vi phạm sẽ bị đuổi khỏi Trại — tương đương với bản án tử trong vùng tundra khắc nghiệt.

## IV. Cơ Cấu Tổ Chức (组织结构)
Cơ cấu cực kỳ đơn giản theo mô hình bộ lạc nhỏ. Trại Chủ Vũ Lạc Vũ đứng đầu, phụ trách mọi quyết định lớn — từ phân phối thức ăn đến quyết định di chuyển khi cần. Dưới trướng có mười đến mười lăm thợ săn trẻ — những Vũ Tộc trẻ còn bay được, dù thấp và chậm — phụ trách kiếm thức ăn hàng ngày. Bà Lão Cánh Bạc — cựu nội môn đệ tử Vũ Hoàng Các bị trục xuất — đóng vai trò trưởng lão không chính thức, âm thầm hướng dẫn và bảo vệ cộng đồng bằng kiến thức và kinh nghiệm mà không ai trong Trại biết là bà còn giữ được tu vi Kim Đan.

## V. Công Pháp & Trận Pháp (功法与阵法)
Trại không có công pháp chính thức. Vài Vũ Tộc trẻ tự mò mẫm hấp thu Phong linh khí từ môi trường nhưng không có phương pháp bài bản nên hiệu quả cực thấp và đôi khi gây thương tích. Không có trận pháp — phòng thủ hoàn toàn dựa vào địa hình vách đá hiểm trở tự nhiên.

Tuy nhiên, bà lão cánh bạc âm thầm dạy trẻ con vài bài Phong công pháp cơ bản — không phải công pháp chiến đấu mà là kỹ thuật cảm nhận gió và tăng cường khả năng bay. Bà dạy rất cẩn thận, chỉ từng chút một, để không ai nghi ngờ bà còn giữ tu vi cao hơn vẻ bề ngoài.

## VI. Đặc Sản Môn Phái (门派特产)
- **Lông Vũ Rụng:** "Đặc sản" duy nhất có giá trị thương mại — lông vũ Vũ Tộc dù huyết mạch loãng vẫn mang chút linh lực phong hệ, được Lông Vũ Phường thu mua để chế tạo quạt phong và bút lông.
- **Trứng Chim Tuyết Muối:** Món ăn bảo quản đặc trưng — trứng chim tuyết ướp muối đá, có vị mặn đắng nhưng giàu dinh dưỡng, thỉnh thoảng bán cho thương nhân qua đường.
- **Câu Chuyện Cổ:** Bà lão cánh bạc và các lão nhân trong Trại là kho tàng truyện kể sống về lịch sử Vũ Tộc thượng cổ — những câu chuyện mà Vũ Hoàng Các đã cố tình xóa bỏ khỏi sử sách.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Hốc Đá Trú Ẩn:** Khoảng hai mươi hốc đá tự nhiên được mở rộng bằng tay, mỗi hốc chứa từ ba đến năm người, che được gió tuyết nhưng không kín hoàn toàn.
- **Bếp Chung:** Một khoảng đá bằng phẳng giữa Trại, nơi đốt lửa nấu ăn chung — cũng là nơi tụ tập nghe kể chuyện mỗi tối.
- **Điểm Canh Gác:** Hai hốc đá ở vị trí cao nhất, nơi thợ săn thay phiên canh gác — quan sát yêu thú và cảnh báo nguy hiểm.
- **Tổ Phượng Hoàng Băng Bỏ Hoang:** Nằm dưới vách đá nơi Trại đóng — bên trong có trứng hóa thạch mang linh lực tàn dư, chưa ai trong Trại biết giá trị thực sự.

## VIII. Kinh Tế (经济)
Kinh tế Trại ở mức sinh tồn tuyệt đối — không có tích lũy, không có thặng dư, mỗi ngày là một cuộc chiến giành thức ăn. Nguồn sống chính từ săn bắt trứng chim tuyết và côn trùng chịu lạnh, bổ sung bằng rêu đá khi thời tiết quá xấu để bay. Thu nhập tiền mặt gần như bằng không — nguồn duy nhất là bán lông vũ rụng cho Lông Vũ Phường đổi lấy vải, muối, và dầu đèn. Ngoài ra, trẻ con Vũ Tộc gia nhập Phong Vũ Trinh Sát Đội kiếm được chút lương thực gửi về Trại — đây là mối quan hệ cộng sinh quan trọng nhất giúp Trại tồn tại.

## IX. Lịch Sử Tóm Tắt (简史)
Vũ Hoàng Các có tiêu chuẩn khắt khe — chỉ thu nhận Vũ Tộc có huyết mạch thuần và cánh đủ lớn. Những Vũ Tộc không đạt chuẩn bị từ chối ở cổng đảo bay, hoặc tệ hơn, bị trục xuất sau Lễ Thử Cánh lúc năm tuổi. Phiêu bạt khắp nơi, bị khinh bỉ bởi cả đồng tộc trên trời lẫn các chủng tộc dưới đất, họ trở thành lưu dân không nơi nương tựa.

Ba mươi năm trước, Vũ Lạc Phong — cha của Trại Chủ hiện tại — tập hợp những lưu dân Vũ Tộc lập Trại trên vách đá tundra, nơi không ai muốn sống nhưng ít nhất không ai đuổi đi. Vũ Lạc Phong qua đời mười năm sau đó vì kiệt sức trong mùa đông khắc nghiệt, con trai Vũ Lạc Vũ kế nhiệm ở tuổi hai mươi — trẻ, yếu, nhưng chất phác và kiên cường. Vũ Hoàng Các biết Trại tồn tại nhưng coi như bụi trần không đáng nhìn — không giúp đỡ, cũng không tiêu diệt.

## X. Giai Thoại & Bí Mật (轶事与秘密)
Trong Trại có bà lão Vũ Tộc cánh bạc — bà từng là nội môn đệ tử Vũ Hoàng Các, bị trục xuất vì yêu một Nhân Tộc. Thực tế, tu vi thật của bà là Kim Đan Sơ Kỳ — bà cố tình ẩn giấu, chỉ lộ ra chút ít khi dạy trẻ con vài bài Phong công pháp cơ bản. Bà lão biết một bí mật về Vũ Hoàng hiện tại — liên quan đến nghi lễ đạt sáu đôi cánh ánh sáng — và bà thề sẽ chỉ kể cho người xứng đáng trước khi chết.

Dưới vách đá nơi Trại đóng có tổ phượng hoàng băng bỏ hoang — bên trong chứa trứng hóa thạch mang linh lực tàn dư. Nếu ai đó có đủ kiến thức để kích hoạt linh lực trong trứng hóa thạch, nó có thể hồi sinh thành Phượng Hoàng Băng — linh thú cổ đại có sức mạnh ngang Nguyên Anh. Điều trớ trêu là bà lão cánh bạc biết tổ phượng hoàng tồn tại nhưng không có đủ linh lực để kích hoạt, và cũng không dám tiết lộ vì sợ thu hút sự chú ý của Vũ Hoàng Các.

## XI. Quan Hệ Thế Lực (势力关系)
- **Vũ Hoàng Các:** Bị khinh bỉ và phủ nhận — Vũ Hoàng Các coi Trại như bụi trần.
- **Lông Vũ Phường:** Mối quan hệ thương mại duy nhất — bán lông vũ rụng đổi lấy nhu yếu phẩm.
- **Phong Vũ Trinh Sát Đội:** Trẻ con Trại gia nhập Đội để kiếm sống, Đội bảo vệ Trại khỏi yêu thú đổi lại.
- **Đoản Dực Lạc Đoàn:** Chia sẻ thức ăn khi cả hai bên đều thiếu thốn.
