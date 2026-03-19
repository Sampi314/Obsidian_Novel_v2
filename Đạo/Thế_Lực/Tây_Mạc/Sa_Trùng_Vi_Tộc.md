---
type: faction
name: Sa Trùng Vi Tộc
hantu: 沙虫微族
faction_type: Bộ Lạc
alignment: 5
race: Yêu Tộc (Sa Trùng)
region: Tây Mạc
founded: Thượng Cổ (Tồn tại từ trước ký ức của Thạch Tộc)
founder: Không rõ (Loài sinh vật nguyên thủy)
emblem: Song_Rung_Trong_Dat.png
specialty: Cảm biến rung động, Cảnh báo sớm tự nhiên, Giao tiếp bằng sóng rung
economy:
  - Không có kinh tế (Sinh vật nguyên thủy, tự cung tự cấp)
  - Giá trị gián tiếp: Hệ thống cảnh báo sớm cho ốc đảo
arcs:
  - arc: 1
    status: Tồn tại tự nhiên (Cộng sinh với ốc đảo, bất an vì tín hiệu lạ)
    rank: Không Xếp Hạng
    leader: Trùng Mẫu
    population: 10000
    territory:
      - Lớp đất ẩm quanh mọi ốc đảo lớn nhỏ trong Tây Mạc
    assets:
      - name: Hệ thống cảnh báo rung động tự nhiên
        type: Khả Năng Bẩm Sinh
    stats: [5, 10, 5, 10000, 5, 30]
    divisions:
      - name: Quần Thể Ốc Đảo
        role: Toàn bộ quần thể hoạt động tập thể theo tín hiệu rung động, không có phân cấp phức tạp
        headcount:
          truong_lao: 1
          chien_binh: 0
          dan_thuong: 9999
        members:
          - character: Trùng Mẫu
            position: Cá thể chỉ huy
            cultivation: Luyện Khí (tương đương)
    relationships:
      - faction: Sa Mãng Tộc
        description: Sa Mãng coi Sa Trùng là "bà con xa" và có cấm kỵ không ăn thịt. Hai bên cùng sống dưới đất nhưng hiếm khi tiếp xúc trực tiếp.
        diplomacy:
          lien_minh: 20
          tin: 10
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 0
      - faction: Thủy Nguồn Bảo Vệ Đoàn
        description: Ốc đảo là môi trường sống của Sa Trùng, Thủy Nguồn Bảo Vệ Đoàn bảo vệ ốc đảo cũng là gián tiếp bảo vệ Sa Trùng. Quan hệ cộng sinh tự nhiên.
        diplomacy:
          lien_minh: 30
          tin: 20
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 10
      - faction: Vi Trùng Trinh Sát Đội
        description: Vi Trùng Trinh Sát Đội nghiên cứu và tận dụng tín hiệu rung động của Sa Trùng cho mục đích trinh sát quân sự. Sa Trùng không chủ động hợp tác nhưng tín hiệu của chúng bị khai thác.
        diplomacy:
          lien_minh: 0
          tin: 0
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 0
---

# Sa Trùng Vi Tộc (沙虫微族)

## I. Tổng Quan (总览)

Sa Trùng Vi Tộc là loài sinh vật nguyên thủy cực nhỏ sống trong lớp đất ẩm quanh các ốc đảo trên toàn Tây Mạc, mỗi cá thể chỉ dài bằng ngón tay. Tuy mỗi cá thể cực kỳ yếu ớt, quần thể tại mỗi ốc đảo lên đến hàng ngàn, thậm chí hàng vạn, hoạt động tập thể như một sinh vật duy nhất thông qua hệ thống tín hiệu rung động phức tạp. Trùng Mẫu, cá thể lớn nhất và phát tín hiệu mạnh nhất, đóng vai trò điều phối toàn bộ quần thể. Sa Trùng Vi Tộc tồn tại từ trước ký ức của cả Thạch Tộc, có thể là một trong những loài sống lâu đời nhất Tây Mạc. Giá trị lớn nhất của chúng nằm ở khả năng cảnh báo sớm tự nhiên: phát hiện mọi chuyển động dưới mặt đất, từ bão cát, yêu thú đến kẻ xâm nhập, trước khi bất kỳ ai khác nhận ra.

## II. Địa Lý & Tài Nguyên (地理与资源)

Sa Trùng Vi Tộc phân bố trong lớp đất ẩm xung quanh mọi ốc đảo lớn nhỏ khắp Tây Mạc. Chúng sống trong đất, hiếm khi lên mặt đất, tạo nên mạng lưới cảm biến rung động tự nhiên bao phủ rộng lớn mà không ai nhìn thấy. Tài nguyên duy nhất của Sa Trùng chính là thân thể chúng: khả năng cảm nhận rung động trong bán kính vài dặm, phân biệt được các loại nguồn rung khác nhau như bước chân người, bò trườn của yêu thú, hay rung chấn địa tầng báo hiệu bão cát. Đất ẩm quanh ốc đảo là điều kiện sống bắt buộc, nếu ốc đảo khô cạn thì Sa Trùng cũng chết theo. Vì vậy, sự tồn tại của Sa Trùng gắn liền với sức khỏe của ốc đảo.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)

Gọi "văn hóa" cho Sa Trùng Vi Tộc thì hơi gượng, vì chúng hoạt động chủ yếu theo bản năng tập thể. Tuy nhiên, hành vi của chúng thể hiện một dạng "triết lý" nguyên thủy: "Đất rung — nguy hiểm đến. Đất yên — bình an ở." Khi phát hiện rung động lạ, toàn bộ quần thể phải phát tín hiệu cảnh báo đồng loạt, không có ngoại lệ. Hệ thống giao tiếp bằng rung động trong đất cực kỳ phức tạp mà Nhân Tộc không thể nghe trực tiếp: mỗi loại rung động có tần số, nhịp điệu và cường độ khác nhau, biểu thị bão cát, yêu thú lớn, người lạ, mạch nước ngầm, hay thậm chí cảm xúc của quần thể. Đây là ngôn ngữ nguyên thủy nhất và cũng tinh vi nhất Tây Mạc.

## IV. Cơ Cấu Tổ Chức (组织结构)

Cơ cấu tổ chức của Sa Trùng Vi Tộc đơn giản đến mức gần như không có. Toàn bộ quần thể hoạt động tập thể, không phân chia thành nhóm hay cấp bậc rõ ràng. Cá thể duy nhất có vai trò đặc biệt là Trùng Mẫu, con lớn nhất trong quần thể, có khả năng phát tín hiệu rung động mạnh nhất và phối hợp hành vi của toàn bộ quần thể. Trùng Mẫu không "ra lệnh" theo nghĩa thông thường mà phát ra tín hiệu định hướng, các cá thể khác phản ứng theo bản năng. Khi Trùng Mẫu chết, cá thể lớn thứ nhì tự động trở thành Trùng Mẫu mới. Hàng ngàn cá thể còn lại đều bình đẳng về vai trò, cùng cảm nhận và cùng phát tín hiệu.

## V. Công Pháp & Trận Pháp (功法与阵法)

Sa Trùng Vi Tộc không tu luyện theo bất kỳ nghĩa nào. Sức mạnh duy nhất của chúng là khả năng bẩm sinh cảm nhận rung động trong bán kính vài dặm, phát hiện mọi chuyển động dưới mặt đất với độ chính xác cao. Chúng có thể phân biệt bước chân của một người với bước chân của mười người, phân biệt rung chấn tự nhiên với rung chấn nhân tạo, và cảm nhận được sự thay đổi của mạch nước ngầm. Khi toàn bộ quần thể rung động đồng loạt, chúng tạo ra "sóng cảnh báo" lan xa hàng dặm, đủ mạnh để Nhân Tộc cảm nhận qua hệ thống ống tre đặt trong đất. Đây không phải vũ khí tấn công mà là hệ thống cảnh báo sớm tự nhiên hiệu quả nhất Tây Mạc.

## VI. Đặc Sản Môn Phái (门派特产)

- **Tín Hiệu Rung Động:** Không phải vật phẩm hữu hình mà là dịch vụ tự nhiên. Ốc đảo nào có quần thể Sa Trùng khỏe mạnh sẽ có hệ thống cảnh báo sớm miễn phí, phát hiện bão cát và kẻ xâm nhập trước khi chúng đến nơi. Giá trị chiến lược cực lớn cho phòng thủ ốc đảo.
- **Dịch Sa Trùng:** Chất dịch do Sa Trùng tiết ra khi rung động mạnh, có tác dụng nhẹ trong việc kích hoạt linh lực hệ Thổ. Hiếm khi được thu thập vì Sa Trùng quá nhỏ, nhưng một số dược sư biết cách gom góp từ đất quanh ốc đảo.

## VII. Cơ Sở Hạ Tầng (基础设施)

- **Mạng Lưới Hang Ngầm Vi Mô:** Sa Trùng đào hàng triệu đường hầm nhỏ xíu trong lớp đất ẩm quanh ốc đảo, tạo thành mạng lưới kết nối toàn bộ quần thể. Mạng lưới này cũng giúp thoát nước và thông khí cho đất, gián tiếp duy trì sức khỏe ốc đảo.
- **Hệ Thống Ống Tre (Do Nhân Tộc Xây):** Ốc Đảo Hộ Vệ Đội là thế lực đầu tiên đặt ống tre xuống đất để "nghe" tín hiệu rung động của Sa Trùng. Hệ thống này không thuộc về Sa Trùng nhưng phụ thuộc hoàn toàn vào sự tồn tại của chúng.

## VIII. Kinh Tế (经济)

Sa Trùng Vi Tộc không có kinh tế theo nghĩa thông thường. Chúng là sinh vật nguyên thủy, sống bằng cách hấp thu vi lượng linh khí từ đất ẩm và nước ngầm quanh ốc đảo, hoàn toàn tự cung tự cấp. Tuy nhiên, giá trị kinh tế gián tiếp mà chúng mang lại cho dân cư ốc đảo là rất lớn: hệ thống cảnh báo sớm giúp tránh thiệt hại do bão cát, yêu thú và Sa Tặc, tiết kiệm chi phí phòng thủ và giảm tổn thất nhân mạng. Một số thế lực như Ốc Đảo Hộ Vệ Đội và Vi Trùng Trinh Sát Đội đã nhận ra giá trị này và tìm cách khai thác, tạo nên mối quan hệ cộng sinh đơn phương: Nhân Tộc hưởng lợi, Sa Trùng không biết mình đang "phục vụ."

## IX. Lịch Sử Tóm Tắt (简史)

Sa Trùng Vi Tộc tồn tại từ rất lâu đời, lâu hơn cả ký ức của Thạch Tộc, có thể là một trong những loài nguyên thủy nhất trên đất Tây Mạc. Chúng sống ký sinh quanh ốc đảo, vô hại với mọi sinh vật lớn hơn, và trong phần lớn lịch sử hoàn toàn bị bỏ qua vì quá nhỏ bé.

Dân cư ốc đảo dần nhận ra một hiện tượng kỳ lạ: mỗi khi Sa Trùng phát tín hiệu bất thường, bão cát, yêu thú tấn công hoặc Sa Tặc đến gần luôn xảy ra sau đó. Từ quan sát này, một số ốc đảo bắt đầu "nghe" tín hiệu Sa Trùng để phòng bị. Ốc Đảo Hộ Vệ Đội là thế lực đầu tiên chính thức hợp tác với Sa Trùng bằng hệ thống ống tre cắm xuống đất, biến tín hiệu rung động thành âm thanh mà tai người có thể nghe. Từ đó, Sa Trùng từ loài sinh vật bị bỏ quên trở thành tài sản chiến lược của nhiều ốc đảo.

## X. Giai Thoại & Bí Mật (轶事与秘密)

Bí mật đáng lo ngại nhất hiện tại là gần đây Sa Trùng ở nhiều ốc đảo đồng loạt phát tín hiệu cực mạnh hướng về phía Vĩnh Tịch Chi Địa. Không ai hiểu được nghĩa cụ thể của tín hiệu này, nhưng cường độ chưa từng có tiền lệ, và Trùng Mẫu tại nhiều ốc đảo bắt đầu dẫn quần thể rời xa, di chuyển theo hướng ngược lại với Vĩnh Tịch Chi Địa. Đây là lần đầu tiên trong ký ức dân cư ốc đảo mà Sa Trùng chủ động di cư.

Ốc Đảo Hộ Vệ Đội đã ghi nhận hiện tượng này qua hệ thống ống tre và đang lo lắng sâu sắc, vì mất Sa Trùng đồng nghĩa với mất hệ thống cảnh báo sớm. Ngoài ra, có một học giả tán tu đưa ra giả thuyết gây chấn động: Sa Trùng Vi Tộc thực ra là mảnh vỡ của một linh thể cổ đại. Nếu tất cả quần thể trên toàn Tây Mạc hợp nhất, sức mạnh sẽ không thể tưởng tượng. Giả thuyết này chưa được chứng minh nhưng khiến nhiều thế lực bắt đầu nhìn Sa Trùng bằng con mắt khác.

## XI. Quan Hệ Thế Lực (势力关系)

- **Sa Mãng Tộc:** Sa Mãng coi Sa Trùng là "bà con xa" cùng sống dưới đất và có cấm kỵ không ăn thịt. Đôi khi Sa Mãng cảm nhận tín hiệu rung động của Sa Trùng và dùng làm tham khảo. Quan hệ hòa bình tự nhiên.
- **Thủy Nguồn Bảo Vệ Đoàn:** Bảo vệ ốc đảo cũng là gián tiếp bảo vệ môi trường sống của Sa Trùng. Mối quan hệ cộng sinh tự nhiên: ốc đảo khỏe thì Sa Trùng sống, Sa Trùng sống thì ốc đảo có hệ thống cảnh báo.
- **Vi Trùng Trinh Sát Đội:** Tổ chức chuyên nghiên cứu và khai thác tín hiệu rung động của Sa Trùng cho mục đích trinh sát quân sự. Sa Trùng không chủ động hợp tác, tín hiệu của chúng bị thu thập một chiều. Quan hệ khai thác đơn phương.
