---
type: faction
name: Thuyền Nhân Hộ Vệ Đội
hantu: 船人護衛隊
faction_type: Quân Đoàn
alignment: 5
race: Nhân Tộc
region: Vô Tận Hải
founded: 15 năm trước
founder: Trương Hải Bằng
emblem: Neo_Va_Khien.png
specialty: Cương Thể Thuật, Liên Thuyền Hộ Thuẫn Trận, hộ tống thương thuyền
economy:
  - Phí hộ tống thương thuyền
  - Hợp đồng bảo vệ từ thương nhân nhỏ
  - Thỉnh thoảng vận chuyển hàng hóa đặc biệt
arcs:
  - arc: 1
    status: Hoạt động ổn định
    rank: Hạng Năm
    leader: Đội Trưởng Trương Hải Bằng (Trúc Cơ Viên Mãn)
    population: 38
    territory:
      - Bến cảng Đông Phong — ven bờ đông Vô Tận Hải (kho hàng thuê)
    assets:
      - name: Kho hàng tại Bến Cảng Đông Phong
        type: Công Trình
      - name: Ba thuyền chiến nhỏ (cũ)
        type: Pháp Bảo
      - name: Miếng vảy rồng (bùa may mắn)
        type: Tài Nguyên
    stats: [60, 30, 80, 38, 50, 40]
    divisions:
      - name: Ban Chỉ Huy
        role: Lãnh đạo đội, nhận hợp đồng, phân công nhiệm vụ
        headcount:
          tuong: 1
          uy: 2
          binh: 0
        members:
          - character: Trương Hải Bằng
            position: Đội Trưởng
            cultivation: Trúc Cơ Viên Mãn
          - character: "[Phó Đội Trưởng 1]"
            position: Phó Đội
            cultivation: Trúc Cơ Trung Kỳ
            placeholder: true
          - character: "[Phó Đội Trưởng 2]"
            position: Phó Đội
            cultivation: Trúc Cơ Trung Kỳ
            placeholder: true
      - name: Hộ Vệ Viên
        role: Lực lượng chiến đấu chính, bảo vệ thương thuyền và hàng hóa
        headcount:
          tuong: 0
          uy: 0
          binh: 35
        members:
          - character: "[Hộ vệ viên trẻ có linh căn thủy hệ]"
            position: Hộ Vệ Viên
            cultivation: Luyện Khí Trung Kỳ
            placeholder: true
    relationships:
      - faction: Thiên Sa Thương Hội
        description: Quan hệ phức tạp — Trương Hải Bằng là cựu thủy thủ bị sa thải của Thiên Sa. Đội thuê kho hàng từ Thiên Sa với giá rẻ, nhưng cũng phải chịu sự khinh thường từ họ. Đôi khi nhận hợp đồng mà Thiên Sa không thèm làm.
        diplomacy:
          lien_minh: 10
          tin: 20
          uy_hiep: 0
          thuong_mai: 40
          on_oan: -20
          le_thuoc: 30
      - faction: Hắc Hải Hải Tặc
        description: Kẻ thù trực tiếp — đội từng chạm trán hải tặc nhiều lần, mất một thuyền và năm người trong trận đụng độ lớn nhất. Hải tặc coi đội là mục tiêu dễ bắt nạt.
        diplomacy:
          lien_minh: -80
          tin: -60
          uy_hiep: -40
          thuong_mai: -100
          on_oan: -50
          le_thuoc: 0
      - faction: Phong Bạo Thương Đội
        description: Cạnh tranh lành mạnh — cả hai đều nhận hợp đồng hộ tống thương thuyền, nhưng Phong Bạo mạnh hơn nên thường nhận các hợp đồng lớn, để lại hợp đồng nhỏ cho Hộ Vệ Đội.
        diplomacy:
          lien_minh: 15
          tin: 30
          uy_hiep: 0
          thuong_mai: 20
          on_oan: 0
          le_thuoc: 0
---

# Thuyền Nhân Hộ Vệ Đội (船人護衛隊)

## I. Tổng Quan (总览)

Thuyền Nhân Hộ Vệ Đội là một đội hộ tống nhỏ hoạt động tại vùng biển ven bờ đông Vô Tận Hải, chuyên bảo vệ thương thuyền cho các thương nhân nhỏ không đủ tiền thuê các đội hộ tống lớn. Với ba mươi tám thành viên, ba chiếc thuyền chiến cũ kỹ nhưng được bảo dưỡng cẩn thận, và một kho hàng thuê lại từ Thiên Sa Thương Hội, đội thuộc Hạng Năm — bé nhỏ nhất trong hệ thống phân hạng thế lực. Đội Trưởng Trương Hải Bằng, cựu thủy thủ Thiên Sa bị sa thải vì tuổi cao, đã gây dựng đội hộ vệ này bằng uy tín cá nhân và tinh thần "hàng đến nơi, người về nhà." Tuy lực lượng yếu, trang bị thiếu, nhưng đội nổi tiếng đáng tin cậy — giá rẻ, không bao giờ bỏ khách, và sẵn sàng chiến đấu đến cùng để bảo vệ hàng hóa.

## II. Địa Lý & Tài Nguyên (地理 与 资源)

Trụ sở của Thuyền Nhân Hộ Vệ Đội là một kho hàng cũ tại Bến Cảng Đông Phong, ven bờ đông Vô Tận Hải, thuê lại từ Thiên Sa Thương Hội với giá rẻ — phần vì kho nằm ở vị trí kém, phần vì Thiên Sa coi đây là giao dịch nhỏ không đáng bận tâm. Kho hàng vừa là nơi ở, vừa là phòng họp, vừa là xưởng sửa chữa. Đội sở hữu ba chiếc thuyền chiến nhỏ đã cũ, trang bị pháp khí phòng thủ cấp thấp — không đủ sức đối đầu hải tặc đông đảo nhưng đủ để bảo vệ thương thuyền trước mối đe dọa nhỏ. Không có tài nguyên riêng — toàn bộ thu nhập từ phí hộ tống. Thuyền chiến tuy cũ nhưng được Trương Hải Bằng tự tay bảo dưỡng mỗi tối, giữ chúng trong tình trạng hoạt động tốt nhất có thể.

## III. Văn Hóa & Tín Ngưỡng (文化 与 信仰)

Thành viên Thuyền Nhân Hộ Vệ Đội phần lớn là cựu binh, thủy thủ thất nghiệp, hoặc tu sĩ cấp thấp không vào được tông môn nào — những người bị xã hội tu luyện bỏ rơi nhưng vẫn muốn kiếm sống bằng sức lực trên biển. Văn hóa đội đơn giản nhưng vững chắc: tôn trọng danh dự và hợp đồng, nhận tiền thì bảo vệ đến cùng, không bao giờ bỏ chạy khi khách gặp nguy. Khẩu hiệu "Hàng đến nơi, người về nhà" không chỉ là câu quảng cáo mà là lời thề — mỗi thành viên mới đều phải lặp lại trước mặt toàn đội khi gia nhập. Đội không thờ thần linh cụ thể nhưng có truyền thống rót một chén rượu xuống biển trước mỗi chuyến hộ tống, tưởng nhớ năm đồng đội đã hy sinh trong trận đụng độ hải tặc.

## IV. Cơ Cấu Tổ Chức (组织结构)

Cơ cấu của Thuyền Nhân Hộ Vệ Đội đơn giản theo mô hình quân đoàn thu nhỏ. Đội Trưởng Trương Hải Bằng nắm quyền quyết định tối cao — từ nhận hợp đồng, phân công nhiệm vụ đến chiến thuật chiến đấu. Hai Phó Đội Trưởng cảnh giới Trúc Cơ Trung Kỳ hỗ trợ chỉ huy, mỗi người phụ trách một thuyền chiến. Ba mươi lăm Hộ Vệ Viên chia đều trên ba thuyền, cảnh giới từ Luyện Khí đến Trúc Cơ Sơ Kỳ. Trương Hải Bằng tự mình chỉ huy thuyền thứ ba — chiếc lớn nhất và cũ nhất, nhưng cũng là chiếc được bảo dưỡng tốt nhất. Quan hệ trong đội mang tính gia đình hơn quân đội — Trương Hải Bằng coi thành viên như em út, và thành viên gọi gã là "Lão Bằng" thay vì xưng hô theo cấp bậc.

## V. Công Pháp & Trận Pháp (功法 与 阵法)

Thành viên đội tu luyện các công pháp tạp nham không thống nhất — ai biết gì dùng nấy, không có hệ thống đào tạo bài bản. Trương Hải Bằng sở trường **Cương Thể Thuật** — một phương pháp luyện thân thể cứng như đá, không bay bổng nhưng cực kỳ thực dụng trên thuyền chiến nơi va chạm cận chiến là chủ yếu. Trận pháp duy nhất của đội là **Liên Thuyền Hộ Thuẫn Trận** — ba thuyền chiến dàn thành đội hình tam giác, kích hoạt pháp khí phòng thủ trên mỗi thuyền để tạo rào chắn linh lực bao quanh thương thuyền ở giữa. Trận pháp này không mạnh nhưng đủ chặn đạn pháo tầm xa và ngăn hải tặc tiếp cận thương thuyền trong thời gian ngắn. Gần đây, một hộ vệ viên trẻ phát hiện mình có linh căn thủy hệ, và Trương Hải Bằng đang tìm cách kiếm công pháp phù hợp cho cậu ta — hy vọng đây sẽ là bước đột phá cho sức mạnh của đội.

## VI. Đặc Sản Môn Phái (门派特产)

- **Liên Thuyền Hộ Thuẫn Trận:** Tuy chỉ là trận pháp cấp thấp, nhưng thiết kế phù hợp hoàn hảo cho hộ tống thương thuyền trên biển. Một số đội hộ tống nhỏ khác đã liên hệ muốn mua bản sao trận đồ, nhưng Trương Hải Bằng từ chối vì đây là lợi thế cạnh tranh duy nhất của đội.
- **Dịch Vụ Hộ Tống Giá Rẻ:** Không phải "đặc sản" theo nghĩa vật phẩm, nhưng uy tín "giá rẻ, đáng tin, không bỏ khách" của đội là thương hiệu quý giá trong giới thương nhân nhỏ vùng biển đông.
- **Kinh Nghiệm Hàng Hải Lão Luyện:** Trương Hải Bằng từng đi khắp Vô Tận Hải khi còn phục vụ Thiên Sa Thương Hội, nắm rõ hải lưu, bãi đá ngầm và vùng biển nguy hiểm — kiến thức này giúp đội chọn tuyến đường an toàn nhất cho mỗi chuyến hộ tống.

## VII. Cơ Sở Hạ Tầng (基础设施)

- **Kho Hàng Bến Cảng Đông Phong:** Trụ sở chính của đội, một kho hàng cũ thuê từ Thiên Sa Thương Hội. Bên trong chia thành khu sinh hoạt cho thành viên, phòng họp nhỏ, và xưởng sửa chữa thiết bị. Tuy chật chội và ẩm mốc, nhưng vị trí sát bến cảng thuận tiện cho việc nhận hợp đồng.
- **Ba Thuyền Chiến Nhỏ:** Tài sản quý giá nhất của đội. Mỗi thuyền trang bị pháp khí phòng thủ cấp thấp và một khẩu pháo linh lực tầm gần. Thuyền cũ nhưng được Trương Hải Bằng bảo dưỡng tận tay mỗi tối — thân thuyền sạch rong rêu, buồm vá nhưng chắc chắn, máy trận pháp luôn sẵn sàng kích hoạt.
- **Bến Neo Riêng:** Một góc nhỏ ở bến cảng Đông Phong, đủ chỗ cho ba thuyền chiến neo đậu. Không có cầu tàu riêng — phải dùng chung với thuyền cá.

## VIII. Kinh Tế (经济)

Kinh tế của Thuyền Nhân Hộ Vệ Đội hoàn toàn dựa vào phí hộ tống thương thuyền. Đội chuyên nhận các hợp đồng mà đội hộ tống lớn không thèm làm — hàng hóa giá trị thấp, tuyến đường ngắn, hoặc thương nhân không đủ tiền thuê Phong Bạo Thương Đội hay các đội mạnh hơn. Giá hộ tống của đội rẻ hơn thị trường khoảng ba mươi phần trăm, đổi lại thương nhân chấp nhận rủi ro cao hơn nếu gặp hải tặc mạnh. Thu nhập đủ để duy trì hoạt động — trả lương cho thành viên, mua vật tư sửa thuyền, thuê kho — nhưng không dư dả. Mỗi khi có hợp đồng lớn hiếm hoi, Trương Hải Bằng dồn toàn bộ lợi nhuận thêm vào sửa chữa thuyền và mua pháp khí phòng thủ, không bao giờ giữ cho riêng mình.

## IX. Lịch Sử Tóm Tắt (简史)

Mười lăm năm trước, Trương Hải Bằng — thủy thủ kỳ cựu của Thiên Sa Thương Hội — bị sa thải với lý do "tuổi cao, sức yếu so với tu sĩ trẻ." Ở tuổi ngoài bốn mươi với cảnh giới Trúc Cơ Viên Mãn — mạnh với phàm nhân nhưng tầm thường với giới tu luyện — gã thấy mình bị đào thải khỏi hệ thống mà gã phục vụ cả đời. Thay vì chấp nhận số phận, Trương Hải Bằng tập hợp một nhóm cựu đồng nghiệp cùng cảnh ngộ và lập đội hộ vệ riêng, chuyên nhận hợp đồng mà các đội lớn không thèm làm. Những năm đầu cực kỳ khó khăn — ít khách, ít tiền, thuyền cũ nát. Bước ngoặt đến khi đội chạm trán hải tặc trong chuyến hộ tống: mất một thuyền và năm người, nhưng bảo vệ được toàn bộ hàng hóa. Câu chuyện lan truyền trong giới thương nhân nhỏ, và từ đó, đội không bao giờ thiếu hợp đồng. Uy tín "giá rẻ, đáng tin, không bỏ khách" được xây bằng máu và nước mắt.

## X. Giai Thoại & Bí Mật (轶事 与 秘密)

Trương Hải Bằng giữ một miếng vảy rồng nhặt được trên biển trong một lần tuần tra — gã không biết giá trị thật của nó nhưng coi là bùa may mắn, luôn mang theo bên người. Nếu đó thật sự là vảy rồng, giá trị của nó có thể vượt xa tổng tài sản của cả đội. Đội từng vô tình hộ tống một kiện hàng chứa bảo vật cấm — suýt bị diệt khẩu bởi người thuê khi phát hiện ra, nhưng may mắn thoát nhờ Trương Hải Bằng nhận ra nguy hiểm sớm và chạy trước khi kẻ thuê kịp ra tay. Sự kiện này khiến Trương Hải Bằng thêm quy tắc mới: kiểm tra hàng hóa trước khi nhận hợp đồng, dù khách có trả thêm tiền bảo mật. Gần đây, một hộ vệ viên trẻ phát hiện mình có linh căn thủy hệ hiếm — Trương Hải Bằng đang bí mật tìm kiếm công pháp thủy hệ phù hợp, hy vọng cậu ta sẽ trở thành tu sĩ mạnh đầu tiên do đội tự đào tạo.

## XI. Quan Hệ Thế Lực (势力关系)

- **Thiên Sa Thương Hội:** Quan hệ phức tạp. Trương Hải Bằng bị Thiên Sa sa thải nhưng không oán hận — gã hiểu đó là quy luật đào thải. Đội thuê kho từ Thiên Sa với giá rẻ, và đôi khi nhận hợp đồng "rơi vãi" mà Thiên Sa không thèm làm. Thiên Sa coi đội là tồn tại vô hại, không đáng chú ý.
- **Hắc Hải Hải Tặc:** Kẻ thù trực tiếp. Đội từng mất một thuyền và năm thành viên trong trận đụng độ với hải tặc. Hải tặc coi đội là mục tiêu dễ bắt nạt vì lực lượng yếu, nhưng sau vài lần thất bại khi tấn công đội, một số nhóm nhỏ bắt đầu tránh xa.
- **Phong Bạo Thương Đội:** Cạnh tranh lành mạnh. Cả hai cùng hoạt động hộ tống nhưng ở phân khúc khác nhau — Phong Bạo nhận hợp đồng lớn, Hộ Vệ Đội nhận hợp đồng nhỏ. Đôi khi hai bên trao đổi thông tin về tình hình hải tặc, hợp tác hơn là đối đầu.
