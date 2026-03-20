---
type: faction
name: Linh Hồ Tàn Tộc
hantu: 灵狐残族
faction_type: Gia Tộc
alignment: 1
race: Yêu Tộc (Hồ Yêu)
region: Vô Tận Hải
founded: 500 năm trước (tàn dư di cư)
founder: Hồ Tộc Trưởng đời đầu (thất truyền)
emblem: Bach_Ho_Nguyet_Quang.png
specialty: Huyễn thuật ẩn thân, Nguyệt Ảnh bẩm sinh, Che giấu tung tích
economy:
- Bán lông hồ rụng tự nhiên (luyện bút linh)
- Trao đổi nhỏ lẻ với thương nhân qua đường
- Hái quả dại và săn thú rừng tự cung
arcs:
  - arc: 1
    status: Ẩn nấp — sợ hãi sinh tồn
    rank: Hạng Năm
    leader: Tộc Trưởng Hồ Tuyết Nhi
    population: 47
    territory:
      - Hang đá sâu trong dãy Núi Độc Long (phía tây)
    assets:
      - name: Hang Ẩn Hồ Tộc
        type: Công Trình
      - name: Nguyệt Quang Thạch
        type: Pháp Bảo
    stats: [15, 10, 20, 47, 35, 10]
    divisions:
      - name: Hồ Tộc Chính Hội
        role: Toàn bộ sinh hoạt, phòng vệ và dạy dỗ thế hệ trẻ
        headcount:
          truong_lao: 2
          chinh_chi: 8
          thu_chi: 0
          gia_nhan: 0
        members:
          - character: Hồ Tuyết Nhi
            position: Tộc Trưởng
            cultivation: Trúc Cơ Viên Mãn
            placeholder: false
          - character: "[Trưởng Lão Hồ Yêu I]"
            position: Trưởng Lão
            cultivation: Trúc Cơ Trung Kỳ
            placeholder: true
          - character: "[Trưởng Lão Hồ Yêu II]"
            position: Trưởng Lão
            cultivation: Trúc Cơ Trung Kỳ
            placeholder: true
          - character: "[Hồ Non Cửu Vĩ]"
            position: Ấu Sinh
            cultivation: Chưa hóa hình
            placeholder: true
    relationships:
      - faction: Vạn Yêu Thành
        description: Mối đe dọa lớn nhất. Vạn Yêu Thành trưng binh mở rộng ảnh hưởng, nếu bị phát hiện Hồ Tộc sẽ bị đẩy ra tiền tuyến làm bia đỡ đạn.
        diplomacy:
          lien_minh: -20
          tin: -60
          uy_hiep: 70
          thuong_mai: -30
          on_oan: -40
          le_thuoc: 0
      - faction: Lục Mãng Hạ Tộc
        description: Cùng cư ngụ gần dãy Núi Độc Long, biết sự tồn tại của nhau nhưng giữ khoảng cách. Đôi khi trao đổi tin tức ngầm.
        diplomacy:
          lien_minh: 10
          tin: 15
          uy_hiep: 0
          thuong_mai: 5
          on_oan: 0
          le_thuoc: 0
      - faction: Bách Thú Sơn Trang
        description: Hồ Tuyết Nhi từng nghe danh Sơn Trang thu nhận yêu tộc, nhưng không dám tiếp cận vì sợ lộ tung tích.
        diplomacy:
          lien_minh: 5
          tin: 10
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 0
---

# Linh Hồ Tàn Tộc (灵狐残族)

## I. Tổng Quan (总览)
Linh Hồ Tàn Tộc là tàn dư của một chi nhánh Hồ Tộc phương Bắc, bị đánh tan trong chiến tranh yêu-nhân cách đây năm trăm năm và phải chạy đến vùng Núi Độc Long ẩn náu. Hiện tại chỉ còn bốn mươi bảy thành viên gồm hai mươi lăm hồ yêu đã hóa hình và mười hai ấu sinh, do Tộc Trưởng Hồ Tuyết Nhi — một bạch hồ hai trăm tuổi tu vi Trúc Cơ Viên Mãn — lãnh đạo. Đây là thế lực Hạng Năm, gần như không có sức mạnh quân sự, tồn tại hoàn toàn nhờ khả năng huyễn thuật ẩn thân bẩm sinh và triết lý "giấu mình là sống, lộ diện là chết."

## II. Địa Lý & Tài Nguyên (地理 与 资源)
Hang ổ của Linh Hồ Tàn Tộc nằm sâu trong khe núi phía tây dãy Núi Độc Long, được che phủ bởi huyễn thuật sơ khai khiến người ngoài chỉ thấy một vách đá bình thường. Bên trong hang khô ráo và ấm áp nhờ mạch địa nhiệt nhỏ chạy qua, chia thành nhiều ngách, mỗi gia đình hồ yêu chiếm một ngách riêng. Tài nguyên chính là lông hồ thoát rụng tự nhiên — có tác dụng luyện bút linh cấp thấp hoặc dùng trong huyễn thuật — và kỹ năng huyễn thuật bẩm sinh, tài sản quý nhất nhưng cũng chính là lý do khiến họ bị săn đuổi. Thức ăn chủ yếu là thịt thú rừng và quả dại, nguồn cung bấp bênh theo mùa.
Khu vực xung quanh ẩn chứa nhiều bí mật chưa được khám phá — hang động chưa ai đến, mạch khoáng chưa ai biết, dấu tích cổ đại mà thời gian chưa kịp xóa nhòa.

## III. Văn Hóa & Tín Ngưỡng (文化 与 信仰)
Văn hóa của Linh Hồ Tàn Tộc xoay quanh sinh tồn bằng ẩn nấp, không bằng chiến đấu. Quy tắc nghiêm ngặt nhất là cấm hóa hình ở nơi công cộng và cấm sử dụng huyễn thuật mê hoặc nhân tộc — vì bất kỳ dấu vết nào cũng có thể dẫn đường cho kẻ thù tìm đến. Nếu bị phát hiện, cả tộc lập tức bỏ hang di dời, không luyến tiếc. Phong tục quan trọng nhất là "Thí Luyện Giấu Mình" — hồ yêu non đủ năm mươi tuổi phải ẩn nấp gần khu dân cư nhân tộc bảy ngày mà không bị phát hiện để được công nhận trưởng thành. Tín ngưỡng mờ nhạt, chỉ còn lưu truyền truyền thuyết về Cửu Vĩ Thiên Hồ thời Thượng Cổ như một giấc mơ xa vời.
Mỗi thế hệ mới được truyền dạy không chỉ kỹ năng sinh tồn mà cả câu chuyện về nguồn cội, để ngọn lửa ký ức không bao giờ tắt dù hoàn cảnh khắc nghiệt đến đâu.

## IV. Cơ Cấu Tổ Chức (组织结构)
Cơ cấu gia tộc đơn giản phù hợp với quy mô nhỏ bé. Tộc Trưởng Hồ Tuyết Nhi nắm quyền quyết định mọi việc lớn, từ di dời hang ổ đến phân phối thức ăn. Hai Trưởng Lão Trúc Cơ Trung Kỳ phụ trách dạy dỗ hồ yêu non và canh phòng cảnh giới. Hai mươi lăm hồ yêu còn lại chia thành tám gia đình, tự quản nội bộ nhưng tuân theo mệnh lệnh Tộc Trưởng khi có biến. Mười hai ấu sinh chưa hóa hình được cả tộc bảo vệ cẩn thận, trong đó có một cá thể đặc biệt mà chỉ Hồ Tuyết Nhi biết rõ bí mật.

## V. Công Pháp & Trận Pháp (功法 与 阵法)
Công pháp duy nhất của tộc là "Nguyệt Ảnh Huyễn Hồ Quyết" — huyễn thuật bẩm sinh của Hồ Tộc, cho phép tạo ảo ảnh và ẩn thân. Cấp bậc thấp, chỉ đủ đánh lừa tu sĩ Trúc Cơ hoặc phàm nhân, gặp Kim Đan trở lên thì vô dụng. Công pháp này không có tác dụng tấn công, thuần túy phòng ngự và trốn chạy. Tàn Tộc không có bất kỳ trận pháp nào — phòng thủ hoàn toàn dựa vào việc ẩn giấu hang ổ và không để lại dấu vết. Đây là điểm yếu chí mạng: một khi bị phát hiện, họ gần như không có khả năng chống cự.

## VI. Đặc Sản Môn Phái (门派特产)
Lông hồ rụng tự nhiên là sản phẩm duy nhất có giá trị giao dịch, được dùng làm nguyên liệu luyện bút linh cấp thấp hoặc thêu vào y phục huyễn thuật để tăng hiệu quả ẩn thân. Ngoài ra, nước mắt hồ yêu có chứa vi lượng nguyệt lực, tương truyền có thể dùng trong đan dược trị tâm ma — nhưng Hồ Tuyết Nhi cấm tuyệt đối việc thu thập, vì đó là phẩm giá cuối cùng của tộc nhân.
Ngoài ra, Linh Hồ Tàn Tộc còn sở hữu vật phẩm có giá trị văn hóa hơn vật chất — thứ mà thương nhân bỏ qua nhưng nhà sử học trả bất cứ giá nào.

## VII. Cơ Sở Hạ Tầng (基础设施)
Hạ tầng tối giản vì bản chất du cư ẩn nấp. Hang chính rộng nhất là nơi họp tộc và cất giữ Nguyệt Quang Thạch — di vật tổ tiên. Mỗi ngách hang được trải cỏ khô và lông thú cho ấm, có lối thoát hiểm riêng dẫn ra ngoài khe núi. Không có công trình phòng thủ hay kiến trúc cố định — mọi thứ được thiết kế để có thể bỏ lại trong thời gian ngắn nhất nếu cần di dời.
Toàn bộ hạ tầng mang dấu ấn đặc trưng cộng đồng — không phải xa hoa mà là thực dụng đúc kết qua nhiều thế hệ thử nghiệm.

## VIII. Kinh Tế (经济)
Kinh tế tự cung tự cấp ở mức tối thiểu. Thu nhập gần như bằng không, chỉ thỉnh thoảng trao đổi lông hồ với thương nhân qua đường để lấy muối và vải. Mọi giao dịch đều do Hồ Tuyết Nhi đích thân thực hiện dưới hình dáng nhân tộc, tại các chợ phàm nhân xa hang ổ hàng trăm dặm. Thức ăn hoàn toàn dựa vào săn bắt và hái lượm, không có trồng trọt hay chăn nuôi. Đời sống vật chất rất khó khăn, nhưng Hồ Tuyết Nhi luôn ưu tiên an toàn hơn sung túc.
Tiềm năng kinh tế vượt xa những gì đang được khai thác — sự thiếu hụt nhân lực, kiến thức thương mại, và bảo hộ chính trị khiến phần lớn giá trị vẫn nằm yên.

## IX. Lịch Sử Tóm Tắt (简史)
Linh Hồ Tàn Tộc vốn là chi nhánh nhỏ của Hồ Tộc lớn ở phương Bắc, sở hữu huyễn thuật tinh xảo và sống ôn hòa với nhân tộc. Năm trăm năm trước, chiến tranh yêu-nhân bùng nổ, Hồ Tộc bị tàn sát gần hết vì nhân tộc nghi ngờ huyễn thuật của họ là tà pháp mê hoặc. Tàn dư chạy về phương Nam, lưu lạc qua nhiều vùng trước khi tìm được chỗ ẩn náu trong dãy Núi Độc Long. Gần đây, việc Vạn Yêu Thành mở rộng ảnh hưởng và trưng binh yêu tộc khiến Hồ Tuyết Nhi phải dẫn tộc nhân trốn sâu hơn vào khe núi, vì bị trưng binh đồng nghĩa với bị đẩy ra tiền tuyến làm bia đỡ đạn.
Mỗi thế hệ kế tiếp gánh di sản và gánh nặng thế hệ trước — nhưng cũng mang khả năng mới mà cha ông chưa từng tưởng tượng.

## X. Giai Thoại & Bí Mật (轶事 与 秘密)
Hồ Tuyết Nhi giữ một viên Nguyệt Quang Thạch — di vật cuối cùng của Hồ Tộc tổ tiên. Tương truyền viên đá có thể đánh thức huyết mạch Thiên Hồ nếu ai đó trong tộc đạt Kim Đan, nhưng hiện tại không hồ yêu nào đủ tu vi, và công pháp hiện có cũng không cho phép đột phá đến cảnh giới đó. Bí mật lớn nhất nằm ở một trong số ấu sinh — mỗi đêm trăng tròn, chín đuôi thoáng hiện rồi biến mất trên thân thể nó. Hồ Tuyết Nhi vừa mừng vừa sợ, vì Cửu Vĩ Thiên Hồ chưa xuất hiện kể từ Thượng Cổ. Nếu tin tức lộ ra, cả tu chân giới sẽ đổ xô tìm đến — có kẻ muốn chiêu mộ, kẻ khác muốn giết để đoạt huyết mạch.
Những bí mật này, nếu được tiết lộ, có thể khiến nhiều thế lực phải nhìn lại đánh giá của mình về cộng đồng nhỏ bé này — vừa là cơ hội vừa là mối nguy.

## XI. Quan Hệ Thế Lực (势力关系)
- **Vạn Yêu Thành:** Mối đe dọa sinh tồn lớn nhất. Vạn Yêu Thành trưng binh mở rộng thế lực, nếu phát hiện Hồ Tộc sẽ bắt ép phục vụ. Linh Hồ Tàn Tộc tránh xa bằng mọi giá.
- **Lục Mãng Hạ Tộc:** Cùng sống gần Núi Độc Long, biết sự tồn tại của nhau qua dấu vết. Quan hệ trung lập nhưng có tiềm năng hợp tác vì cùng cảnh ngộ bị áp bức.
- **Bách Thú Sơn Trang:** Nghe danh là nơi thu nhận yêu tộc, nhưng Hồ Tuyết Nhi không dám mạo hiểm tiếp cận vì lo sợ bẫy và phản bội.
Nhìn tổng thể, mạng lưới quan hệ tuy mỏng manh nhưng đủ duy trì sự tồn tại — trong thế giới tu chân tàn khốc, tồn tại đã là chiến thắng.
