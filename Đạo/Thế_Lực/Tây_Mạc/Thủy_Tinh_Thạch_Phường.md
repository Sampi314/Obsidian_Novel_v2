---
type: faction
name: Thủy Tinh Thạch Phường
hantu: 水晶石坊
faction_type: Hội
alignment: 2
race: Thạch Tộc
region: Tây Mạc
founded: Khoảng 150 năm trước (khi Thiên Sa Thương Hội phát hiện mạch thủy tinh linh)
founder: Trưởng lão Thạch Tộc đời trước (không rõ tên)
emblem: Thuy_Tinh_Lap_Lanh.png
specialty: Tinh Luyện Thuật, Khai thác thủy tinh linh, Chế tạo gương linh và bình chứa đan dược
economy:
- Khai thác và chế tác thủy tinh linh thô
- Sản xuất gương linh, bình chứa đan dược
- Bán sản phẩm cho Thiên Sa Thương Hội (bị ép giá)
arcs:
  - arc: 1
    status: Hoạt động ổn định nhưng bị Thiên Sa Thương Hội ép giá
    rank: Hạng Năm
    leader: Phường Chủ Tinh Minh
    population: 45
    territory:
      - Sườn tây Xích Nham Sơn Mạch (gần mạch thủy tinh linh)
      - Hang động thủy tinh
    assets:
      - name: Mạch thủy tinh linh tự nhiên
        type: Tài Nguyên
      - name: Lò luyện thủy tinh địa nhiệt
        type: Công Trình
    stats: [30, 120, 40, 45, 60, 20]
    divisions:
      - name: Ban Thợ Cả
        role: Chế tác thủy tinh linh thành sản phẩm tinh xảo
        headcount:
          hoi_truong: 1
          pho_hoi_truong: 0
          thanh_vien: 4
          tong_quan: 0
        members:
          - character: Tinh Minh
            position: Phường Chủ
            cultivation: Trúc Cơ Hậu Kỳ (tương đương)
          - character: "[Thợ Cả Gương Linh]"
            position: Thợ Cả
            cultivation: Trúc Cơ Sơ Kỳ (tương đương)
            placeholder: true
      - name: Ban Thợ Phụ
        role: Khai thác thủy tinh linh thô và phụ việc luyện chế
        headcount:
          hoi_truong: 0
          pho_hoi_truong: 0
          thanh_vien: 40
          tong_quan: 0
        members:
          - character: "[Thợ Phụ Thạch Tộc]"
            position: Thợ Phụ
            cultivation: Luyện Khí (tương đương)
            placeholder: true
    relationships:
      - faction: Thiên Sa Thương Hội
        description: Quan hệ bất bình đẳng. Thương Hội ép giá thu mua thủy tinh linh, không cho phường tự do bán trên thị trường. Phường quá yếu để phản kháng.
        diplomacy:
          lien_minh: -20
          tin: 20
          uy_hiep: 80
          thuong_mai: 90
          on_oan: -40
          le_thuoc: 80
      - faction: Hỏa Diễm Công Phường
        description: Đề nghị hợp tác trực tiếp, bỏ qua Thương Hội. Tinh Minh đang cân nhắc nhưng sợ bị trả thù nếu bị phát hiện.
        diplomacy:
          lien_minh: 20
          tin: 30
          uy_hiep: 0
          thuong_mai: 40
          on_oan: 0
          le_thuoc: 0
      - faction: Cổ Thạch Bộ Lạc
        description: Đồng tộc Thạch Tộc, có mối liên hệ huyết thống. Thi thoảng trao đổi vật liệu và kỹ thuật gia công đá.
        diplomacy:
          lien_minh: 30
          tin: 40
          uy_hiep: 0
          thuong_mai: 30
          on_oan: 0
          le_thuoc: 0
---

# Thủy Tinh Thạch Phường (水晶石坊)

## I. Tổng Quan (总览)
Thủy Tinh Thạch Phường là một phường thợ chế tác thủy tinh linh do Thạch Tộc vận hành, nằm tại sườn tây Xích Nham Sơn Mạch gần mạch thủy tinh linh tự nhiên. Với bốn mươi lăm thành viên Thạch Tộc, phường chuyên khai thác thủy tinh linh thô và chế tác thành các sản phẩm có giá trị như gương linh, bình chứa đan dược, và đồ trang sức linh lực. Phường Chủ Tinh Minh, một Thạch Tộc trẻ tuổi với thân xác trong suốt một phần và tay nghề tinh xảo, đang nỗ lực tìm cách thoát khỏi sự lệ thuộc kinh tế đối với Thiên Sa Thương Hội, nơi ép giá thu mua sản phẩm của phường với giá rẻ mạt suốt nhiều thế hệ.

## II. Địa Lý & Tài Nguyên (地理与资源)
Phường đặt trụ sở tại sườn tây Xích Nham Sơn Mạch, nơi có mạch thủy tinh linh tự nhiên duy nhất trong vùng. Hệ thống hang động lấp lánh ánh thủy tinh trải dài sâu vào lòng núi, nhiệt độ cao do mạch nhiệt ngầm chạy bên dưới, tạo điều kiện lý tưởng cho quá trình luyện chế thủy tinh. Thủy tinh linh thô khai thác từ mạch này là nguyên liệu quý dùng chế tạo gương linh cho tu sĩ, bình chứa đan dược chịu được nhiệt linh lực cao, và nhiều sản phẩm tinh xảo khác. Tuy nhiên, mạch thủy tinh nằm trong vùng ảnh hưởng của Thiên Sa Thương Hội, khiến phường không thể tự do bán sản phẩm trên thị trường mở mà phải giao cho Thương Hội với giá bị ép xuống rất thấp.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
Phường theo triết lý "Thủy tinh trong suốt như lòng Thạch Tộc, không giấu giếm, không lừa dối", phản ánh bản chất chân thật và ngay thẳng của Thạch Tộc. Mỗi thành viên Thạch Tộc khi gia nhập phường phải tự tay luyện một viên thủy tinh cầm tay, thể hiện tay nghề và thành ý. Sản phẩm giao cho Thiên Sa Thương Hội luôn đảm bảo đúng số lượng và chất lượng, dù bị ép giá, bởi danh dự Thạch Tộc không cho phép giao hàng kém. Tuy nhiên, thế hệ trẻ trong phường ngày càng bất mãn với hợp đồng bất bình đẳng, muốn phá vỡ thế cục hiện tại để phường có thể phát triển xứng đáng với giá trị sản phẩm.

## IV. Cơ Cấu Tổ Chức (组织结构)
Phường Chủ Tinh Minh đứng đầu, là Thạch Tộc trẻ tuổi nhất từng giữ chức phường chủ nhưng lại có tay nghề tinh xảo nhất trong nhiều thế hệ. Dưới Tinh Minh là bốn thợ cả tương đương Trúc Cơ Sơ Kỳ, mỗi người phụ trách một loại sản phẩm chuyên biệt: gương linh, bình chứa đan dược, đồ trang sức linh lực, và thủy tinh kiến trúc. Bốn mươi thợ phụ Thạch Tộc tương đương Luyện Khí đảm nhiệm công việc khai thác thủy tinh linh thô từ mạch và phụ việc trong quá trình luyện chế. Cơ cấu tổ chức gọn nhẹ, mọi quyết định kỹ thuật do thợ cả đưa ra, quyết định đối ngoại do Tinh Minh nắm giữ.

## V. Công Pháp & Trận Pháp (功法与阵法)
Công pháp cốt lõi của phường là Tinh Luyện Thuật, một kỹ thuật đặc biệt của Thạch Tộc cho phép sử dụng nhiệt nội thân để nấu chảy và tạo hình thủy tinh linh mà không cần lò nung bên ngoài. Chỉ Thạch Tộc mới có thể sử dụng kỹ thuật này vì đòi hỏi cơ thể chịu được nhiệt độ cực cao mà sinh vật bằng thịt xương không thể chống chọi. Phường không có trận pháp phòng thủ, hoàn toàn phụ thuộc vào Thiên Sa Thương Hội bảo vệ. Tinh Minh đang bí mật nghiên cứu cách luyện thủy tinh linh thành vũ khí phòng thân, hy vọng một ngày phường có thể tự bảo vệ mình.

## VI. Đặc Sản Môn Phái (门派特产)
Gương linh là sản phẩm tiêu biểu nhất của phường, được chế tạo từ thủy tinh linh tinh khiết, có khả năng phản chiếu linh lực và phát hiện ảo thuật. Bình chứa đan dược bằng thủy tinh linh chịu được nhiệt linh lực cao, giúp bảo quản đan dược tốt hơn nhiều so với bình gốm thông thường, được các dược sư săn đón. Ngoài ra, phường còn chế tác đồ trang sức thủy tinh linh phát sáng nhẹ, vừa mang giá trị thẩm mỹ vừa có tác dụng chiếu sáng trong bóng tối, rất được lữ khách sa mạc ưa chuộng.

## VII. Cơ Sở Hạ Tầng (基础设施)
Trụ sở chính của phường nằm trong hệ thống hang động thủy tinh tự nhiên, được Thạch Tộc cải tạo thành xưởng chế tác và khu sinh hoạt. Lò luyện thủy tinh tận dụng mạch nhiệt ngầm từ Xích Nham Sơn Mạch, cung cấp nguồn nhiệt ổn định mà không tốn linh thạch. Kho chứa sản phẩm nằm sâu trong hang, nơi nhiệt độ và độ ẩm được duy trì ổn định nhờ cấu trúc đá tự nhiên. Không có kết giới phòng thủ hay trận pháp bảo vệ, an ninh hoàn toàn phụ thuộc vào vị trí hẻo lánh của hang động và sự bảo hộ gián tiếp của Thiên Sa Thương Hội.

## VIII. Kinh Tế (经济)
Nền kinh tế của phường phụ thuộc gần như hoàn toàn vào Thiên Sa Thương Hội. Toàn bộ sản phẩm thủy tinh linh phải giao cho Thương Hội theo hợp đồng ép buộc với giá thu mua rất thấp so với giá trị thực trên thị trường. Dù chất lượng thủy tinh linh của phường là không thể thay thế và được giới luyện đan, luyện khí đánh giá cao, phường vẫn không có quyền tự do định giá hay tìm khách hàng riêng. Tinh Minh coi đây là bất công lớn nhất mà phường phải chịu đựng và đang âm thầm tìm kiếm đối tác thay thế.

## IX. Lịch Sử Tóm Tắt (简史)
Phường được thành lập khi Thiên Sa Thương Hội phát hiện mạch thủy tinh linh tại sườn tây Xích Nham Sơn Mạch và cần lực lượng khai thác. Thạch Tộc địa phương, vốn sống gần mạch thủy tinh từ lâu đời, được Thương Hội thuê với giá rẻ mạt. Hợp đồng bất bình đẳng ký kết từ thế hệ trước trói buộc phường suốt nhiều đời, bởi Thạch Tộc không có lựa chọn khác khi mạch thủy tinh nằm hoàn toàn trong vùng ảnh hưởng của Thương Hội. Tinh Minh là thế hệ phường chủ mới, mang theo tư duy đàm phán và khát vọng tự do kinh tế. Anh muốn đàm phán lại hợp đồng công bằng hơn, nhưng phường quá yếu để có tiếng nói trước Thương Hội hùng mạnh.

## X. Giai Thoại & Bí Mật (轶事与秘密)
Sâu trong mạch thủy tinh, tại vị trí mà chưa ai khai thác tới, tồn tại một khối thủy tinh linh khổng lồ tự nhiên, trong suốt hoàn hảo. Bên trong khối thủy tinh dường như có hình bóng mờ ảo của một sinh vật bị đóng băng từ thời cổ đại, nhưng không ai dám đến gần vì nhiệt độ xung quanh khối thủy tinh cao đến mức ngay cả Thạch Tộc cũng khó chịu đựng. Tinh Minh âm thầm giữ lại những viên thủy tinh linh đẹp nhất thay vì giao cho Thương Hội, tích trữ chúng trong một hốc đá bí mật với hy vọng một ngày có đủ vốn để thoát khỏi sự lệ thuộc. Hỏa Diễm Công Phường gần đây chủ động đề nghị hợp tác trực tiếp, bỏ qua Thương Hội, nhưng Tinh Minh vẫn đang do dự vì sợ bị Thương Hội phát hiện và trả thù.

## XI. Quan Hệ Thế Lực (势力关系)
- **Thiên Sa Thương Hội:** Quan hệ bất bình đẳng, Thương Hội ép giá thu mua và kiểm soát quyền bán sản phẩm. Phường âm thầm bất mãn nhưng chưa đủ sức phản kháng.
- **Hỏa Diễm Công Phường:** Đối tác tiềm năng, đề nghị hợp tác trực tiếp. Nếu thành công, có thể mở ra con đường thoát khỏi sự lệ thuộc Thương Hội.
- **Cổ Thạch Bộ Lạc:** Đồng tộc Thạch Tộc, có mối liên hệ huyết thống và trao đổi kỹ thuật gia công đá.
