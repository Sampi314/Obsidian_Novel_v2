---
type: faction
name: Ngọc Thạch Thợ Mỏ
hantu: 玉石矿工
faction_type: Hội
alignment: 2
race: Thạch Tộc
region: Đông Hoang
founded: Hàng trăm năm trước (chính thức thành Phường 50 năm trước)
founder: Ngọc Đục
emblem: Ngoc_Thach_Tho_Mo.png
specialty: Khai thác ngọc linh, Phân loại ngọc thạch, Đào hầm mỏ
economy:
- Khai thác ngọc linh các loại
- Bán ngọc thô cho thương nhân trung gian
- Gia công ngọc thô cấp thấp
arcs:
  - arc: 1
    status: Bị ép giá, cầm cự
    rank: Hạng Năm
    leader: Phường Trưởng Ngọc Đục
    population: 36
    territory:
      - Mỏ ngọc linh trong dãy núi Đông Hoang
      - Hệ thống hầm mỏ nhiều tầng
    assets:
      - name: Mỏ ngọc linh (ngọc thường đến ngọc chứa linh khí)
        type: Tài Nguyên
      - name: Hệ thống hầm mỏ đa thế hệ
        type: Công Trình
      - name: Lớp Tâm Thạch bí ẩn
        type: Bí Cảnh
    stats: [40, 120, 30, 36, 80, 20]
    divisions:
      - name: Phường Khai Thác
        role: Khai thác, phân loại, và bảo quản ngọc linh từ hầm mỏ
        headcount:
          hoi_truong: 1
          pho_hoi_truong: 0
          thanh_vien: 5
          tong_quan: 30
        members:
          - character: Ngọc Đục
            position: Phường Trưởng
            cultivation: Trúc Cơ Trung Kỳ (tương đương)
          - character: "[Thợ Cả Nhất]"
            position: Thợ Cả
            cultivation: Luyện Khí Đỉnh Phong (tương đương)
            placeholder: true
          - character: "[Thợ Cả Nhị]"
            position: Thợ Cả
            cultivation: Luyện Khí Đỉnh Phong (tương đương)
            placeholder: true
    relationships:
      - faction: Bách Nghệ Phường Tổng Đàn
        description: Đang cố thiết lập quan hệ thương mại trực tiếp, bỏ qua thương nhân trung gian. Nếu thành công sẽ cải thiện đời sống Thạch Tộc đáng kể.
        diplomacy:
          lien_minh: 20
          tin: 30
          uy_hiep: 0
          thuong_mai: 40
          on_oan: 10
          le_thuoc: 0
      - faction: Thương Hội Bạch Lang
        description: Thương nhân Bạch Lang là nhóm ép giá ngọc thô thảm hại nhất, lợi dụng Thạch Tộc thiếu hiểu biết thương mại.
        diplomacy:
          lien_minh: -30
          tin: -40
          uy_hiep: 50
          thuong_mai: -60
          on_oan: -50
          le_thuoc: 40
      - faction: Cự_Tộc_Thợ_Xây
        description: Cùng là Thạch Tộc, có sự đồng cảm chủng tộc. Đôi khi trao đổi ngọc lấy vật liệu xây dựng hoặc công cụ.
        diplomacy:
          lien_minh: 30
          tin: 40
          uy_hiep: 0
          thuong_mai: 30
          on_oan: 15
          le_thuoc: 0
---

# Ngọc Thạch Thợ Mỏ (玉石矿工)

## I. Tổng Quan (总览)
Ngọc Thạch Thợ Mỏ là phường khai thác ngọc linh nhỏ bé của Thạch Tộc, hoạt động tại mỏ ngọc sâu trong dãy núi Đông Hoang. Với chỉ 36 thành viên — toàn bộ đều là Thạch Tộc — phường sống nhờ việc khai thác và bán ngọc linh các loại, từ ngọc thường đến ngọc chứa linh khí quý hiếm. Dù sản phẩm của họ có giá trị không nhỏ trên thị trường, Thạch Tộc liên tục bị thương nhân nhân tộc ép giá thảm hại do thiếu hiểu biết về thương mại và không có sức mạnh chính trị để thương lượng. Phường Trưởng Ngọc Đục — một lão Thạch Tộc giàu kinh nghiệm — cố gắng tổ chức đồng bào thành Phường để có tiếng nói chung, nhưng tình thế vẫn chưa cải thiện đáng kể. Triết lý "Ngọc nằm trong đá, phải đục mới thấy" thể hiện sự kiên nhẫn và hy vọng bền bỉ của họ.

## II. Địa Lý & Tài Nguyên (地理与资源)
Mỏ ngọc linh nằm sâu trong dãy núi Đông Hoang, lối vào hẹp và tối, khó tiếp cận đối với người thường. Bên trong là hệ thống hầm mỏ chằng chịt do Thạch Tộc đào qua nhiều thế hệ, tường hầm lấp lánh ngọc thô chưa khai thác. Hầm mỏ có nhiều tầng: các tầng trên đã khai thác gần hết, tầng giữa đang khai thác hiện tại, và tầng sâu nhất chưa ai dám xuống vì phát hiện lớp đá cứng bất thường. Tài nguyên chính là ngọc linh các loại — từ ngọc thường dùng làm trang sức đến ngọc chứa linh khí có thể dùng trong luyện khí và chế tạo pháp khí cấp thấp. Ngoài ra, Thạch Tộc sống trực tiếp trong hầm mỏ, sử dụng hang động tự nhiên làm nhà ở — điều kiện mà nhân tộc coi là khắc nghiệt nhưng hoàn toàn phù hợp với thể chất Thạch Tộc.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
Thạch Tộc sống theo triết lý giản dị: "Ngọc nằm trong đá, phải đục mới thấy" — chấp nhận lao động nặng nhọc như cách tìm kiếm giá trị ẩn giấu trong cuộc sống. Họ tôn kính đá như một dạng sự sống, tin rằng mỗi viên ngọc đều mang "hồn đá" — linh khí tích tụ qua hàng vạn năm. Quy tắc của Phường đề cao sự công bằng nội bộ: khai thác đều đặn theo phân công, không được tham lam đào quá sâu gây nguy hiểm, và mọi sản phẩm phải bán qua Phường chứ không được bán riêng. Phong tục đặc biệt nhất là khoảnh khắc khi tìm được viên ngọc đặc biệt đẹp — cả Phường dừng lại, xếp vòng tròn xung quanh, im lặng ngắm nhìn trước khi tiếp tục làm việc. Đây là khoảnh khắc hiếm hoi được trân trọng, nhắc nhở rằng lao động vất vả đôi khi mang lại phần thưởng xứng đáng.

## IV. Cơ Cấu Tổ Chức (组织结构)
Phường có cơ cấu đơn giản theo truyền thống Thạch Tộc. Phường Trưởng Ngọc Đục là lão Thạch Tộc già nhất và giàu kinh nghiệm nhất, có khả năng phân biệt chất lượng ngọc từ xa chỉ bằng cách gõ vào bề mặt đá và nghe âm thanh vọng lại. Dưới ông là 5 Thợ Cả kỳ cựu, mỗi người dẫn dắt một nhóm khai thác 5-6 thợ mỏ tại các khu vực khác nhau trong hầm. 30 thợ mỏ còn lại đều là Thạch Tộc, hầu hết có sức mạnh thể chất tương đương Luyện Khí — không phải do tu luyện mà là bẩm sinh của chủng tộc đá. Phường không có bộ phận thương mại riêng, và đây chính là điểm yếu chí mạng: mọi giao dịch bán ngọc đều do Ngọc Đục tự đàm phán, nhưng lão không am hiểu thương mại nên thường xuyên bị thương nhân lừa ép.

## V. Công Pháp & Trận Pháp (功法与阵法)
Ngọc Thạch Thợ Mỏ không có công pháp tu luyện — Thạch Tộc dựa vào sức mạnh bẩm sinh của thể chất đá để đào đục. Năng lực đặc biệt của Thạch Tộc bao gồm "Thạch Cảm" — khả năng cảm nhận cấu trúc bên trong đá qua rung động khi gõ, cho phép phát hiện vị trí ngọc mà không cần phá hủy đá xung quanh — và "Thạch Kiên" — lớp da đá tự nhiên cứng hơn sắt thường, bảo vệ họ khỏi mảnh đá văng khi khai thác. Về trận pháp, hầm mỏ chằng chịt nhiều tầng chính là hệ thống phòng thủ tự nhiên — kẻ xâm nhập sẽ lạc trong mê cung đường hầm, trong khi Thạch Tộc thuộc nằm lòng mọi ngõ ngách và có thể di chuyển nhanh chóng trong bóng tối hoàn toàn.

## VI. Đặc Sản Môn Phái (门派特产)
- **Ngọc Linh Thô:** Ngọc khai thác từ mỏ với nhiều cấp chất lượng — ngọc thường dùng làm trang sức, ngọc trung bình có thể dùng trong trận pháp cấp thấp, và ngọc thượng hạng chứa linh khí dùng trong luyện khí.
- **Ngọc Điêu Khắc Thạch Tộc:** Một số thợ mỏ khéo tay điêu khắc ngọc thành các vật phẩm nhỏ — con giống linh thú, hoa văn may mắn — sử dụng kỹ thuật đục bẩm sinh chính xác đến mức không công cụ kim loại nào sánh được.
- **Bản Đồ Hầm Mỏ:** Kiến thức về cấu trúc địa chất khu vực, tích lũy qua nhiều thế hệ đào hầm, có giá trị lớn cho bất kỳ ai muốn khai thác khoáng sản trong dãy núi.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Hầm Mỏ Đa Tầng:** Hệ thống hầm mỏ chằng chịt được đào qua nhiều thế hệ, gồm ít nhất 5 tầng. Tầng trên đã khai thác cạn dùng làm nơi ở, tầng giữa đang khai thác, tầng dưới chưa khám phá hết.
- **Khu Ở Hang Động:** Các hang động tự nhiên và nhân tạo được Thạch Tộc mở rộng làm nơi sinh sống, giản dị nhưng chắc chắn, phù hợp với thể chất chủng tộc.
- **Kho Ngọc Tập Kết:** Khu vực cất giữ ngọc đã khai thác và phân loại, nằm ở tầng giữa hầm mỏ, do Phường Trưởng trực tiếp quản lý.
- **Cửa Hầm Canh Gác:** Lối vào hầm mỏ duy nhất, luôn có 2 Thạch Tộc luân phiên canh gác để đề phòng trộm cắp và kẻ xâm nhập.

## VIII. Kinh Tế (经济)
Kinh tế của Phường hoàn toàn dựa vào việc bán ngọc linh thô. Ban đầu, Thạch Tộc tự bán ngọc theo giá mà họ cho là hợp lý, nhưng khi thương nhân nhân tộc phát hiện nguồn cung ổn định, họ bắt đầu ép giá xuống mức thảm hại — lợi dụng Thạch Tộc thiếu hiểu biết thương mại và không có thế lực chính trị nào chống lưng. Hiện tại, Phường bán ngọc cho thương nhân trung gian với giá chỉ bằng 1/5 đến 1/10 giá trị thực trên thị trường. Thương Hội Bạch Lang là nhóm ép giá tệ nhất, thậm chí đe dọa bằng vũ lực khi Thạch Tộc cố tăng giá. Hy vọng lớn nhất là Bách Nghệ Phường Tổng Đàn đang cố gắng thiết lập quan hệ thương mại trực tiếp, bỏ qua thương nhân trung gian — nếu thành công, Thạch Tộc sẽ nhận được giá công bằng hơn nhiều.

## IX. Lịch Sử Tóm Tắt (简史)
Thạch Tộc khai thác mỏ ngọc linh này từ hàng trăm năm, khi cả khu vực còn hoang vắng và ít ai biết đến. Thời kỳ đầu, họ tự khai thác và sử dụng ngọc trong sinh hoạt hàng ngày, trao đổi với các bộ tộc lân cận theo giá công bằng. Mọi thứ thay đổi khi thương nhân nhân tộc phát hiện nguồn ngọc linh chất lượng cao — họ ồ ạt kéo đến, ban đầu mua bán tử tế nhưng dần dần ép giá khi nhận ra Thạch Tộc không biết giá trị thực của sản phẩm mình làm ra. Khoảng 50 năm trước, Ngọc Đục — Thạch Tộc già nhất hiện còn sống — quyết định tổ chức đồng bào thành Phường với hy vọng có tiếng nói chung khi đàm phán. Tình thế cải thiện đôi chút nhưng vẫn bất công, vì Thạch Tộc thiếu sức mạnh quân sự và chính trị để đối trọng.

## X. Giai Thoại & Bí Mật (轶事与秘密)
Sâu nhất trong mỏ — nơi chưa thợ mỏ nào dám xuống quá lâu — ẩn chứa một lớp ngọc mà Thạch Tộc gọi là "Tâm Thạch". Đây là loại ngọc đã ngưng tụ hàng vạn năm, cứng đến mức ngay cả Thạch Tộc với thể chất đá cũng không thể đục nổi. Khi chạm tay vào Tâm Thạch, nó phát ra âm thanh kỳ lạ — giống tiếng tim đập chậm rãi, đều đặn, như thể lớp đá đang sống. Ngọc Đục tin rằng Tâm Thạch có thể là một thực thể cổ đại đang ngủ hoặc một dạng linh mạch đã kết tinh, nhưng lão không dám khám phá thêm vì sợ đánh thức thứ gì đó mà Phường không kiểm soát nổi. Bí mật này chỉ Ngọc Đục và hai Thợ Cả thân tín biết — họ không nói cho thương nhân vì hiểu rằng nếu tin tức về Tâm Thạch lọt ra ngoài, mỏ ngọc sẽ bị thế lực lớn chiếm đoạt ngay lập tức.

## XI. Quan Hệ Thế Lực (势力关系)
Thương Hội Bạch Lang là đối tác thương mại chính nhưng cũng là kẻ bóc lột lớn nhất — thương nhân của họ ép giá ngọc thô xuống mức tối thiểu và đe dọa vũ lực khi Thạch Tộc phản kháng. Bách Nghệ Phường Tổng Đàn đang cố gắng thiết lập kênh thương mại trực tiếp với Phường, mang lại hy vọng thoát khỏi vòng xoáy ép giá. Cự Tộc Thợ Xây — cùng là Thạch Tộc — chia sẻ sự đồng cảm chủng tộc, đôi khi trao đổi ngọc lấy công cụ và vật liệu xây dựng, nhưng cả hai đều quá nhỏ bé để bảo vệ nhau trước thế lực lớn. Về tổng thể, Ngọc Thạch Thợ Mỏ đang ở thế yếu trên bàn cờ quyền lực, và tương lai của Phường phụ thuộc lớn vào việc liệu Bách Nghệ Phường Tổng Đàn có thành công trong việc thiết lập kênh thương mại công bằng hay không.
