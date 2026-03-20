---
type: faction
name: Sa Mạc Hướng Đạo Hội
hantu: 沙漠向导会
faction_type: Hội
alignment: 3
race: Nhân Tộc, Sa Tộc (Tán tu đa nguồn)
region: Tây Mạc
founded: Cùng thời với Thiên Sa Thương Đạo
founder: Không rõ (Phát triển tự nhiên từ dân Sa Tộc)
emblem: Sa_Mac_Huong_Dao_Hoi.png
specialty: Dẫn đường sa mạc, Thuận Phong Bộ, Dự báo bão cát
economy:
- Phí dẫn đường cho thương đoàn và lữ khách
- Bán bản đồ và thông tin tuyến đường
- Dịch vụ tư vấn thời tiết sa mạc
arcs:
  - arc: 1
    status: Hưng thịnh (Trung lập bất khả xâm phạm)
    rank: Hạng Năm
    leader: Hội Trưởng Phong Sa Lão Nhân
    population: 80
    territory:
      - Thiên Lý Giới Tuyến (Trụ sở chính)
      - Chi nhánh tại các ốc đảo lớn
    assets:
      - name: Bản đồ Tây Mạc chi tiết nhất
        type: Tình Báo
      - name: Hệ thống la bàn linh tự chế
        type: Pháp Khí
      - name: Hắc Danh Sách
        type: Tình Báo
    stats: [30, 50, 120, 80, 40, 140]
    divisions:
      - name: Ban Lãnh Đạo
        role: Quản lý hội, đào tạo và phân công hướng đạo
        headcount:
          hoi_truong: 1
          pho_hoi_truong: 0
          thanh_vien: 76
          tong_quan: 3
        members:
          - character: Phong Sa Lão Nhân
            position: Hội Trưởng
            cultivation: Trúc Cơ Trung Kỳ
          - character: "[Trưởng Lão Đào Tạo]"
            position: Trưởng Lão
            cultivation: Trúc Cơ Sơ Kỳ
            placeholder: true
          - character: "[Trưởng Lão Phân Công]"
            position: Trưởng Lão
            cultivation: Trúc Cơ Sơ Kỳ
            placeholder: true
          - character: "[Trưởng Lão Liên Lạc]"
            position: Trưởng Lão
            cultivation: Trúc Cơ Sơ Kỳ
            placeholder: true
    relationships:
      - faction: Thiên Sa Thương Hội
        description: Đối tác quan trọng. Thương Hội thuê hướng đạo dẫn đường cho thương đoàn trên Thiên Sa Thương Đạo. Quan hệ tôn trọng lẫn nhau.
        diplomacy:
          lien_minh: 30
          tin: 50
          uy_hiep: 0
          thuong_mai: 80
          on_oan: 10
          le_thuoc: 20
      - faction: Sa Tặc Liên Minh
        description: Kẻ thù về đạo đức nhưng vẫn phải thuê hướng đạo. Sa Tặc không dám đắc tội hội vì không có hướng đạo thì không qua được sa mạc.
        diplomacy:
          lien_minh: -20
          tin: -30
          uy_hiep: 0
          thuong_mai: 40
          on_oan: -20
          le_thuoc: 30
      - faction: Phong Sa Bào Tử
        description: Hội là số ít biết về sự tồn tại của Bào Tử, sử dụng vệt sáng sau bão để xác định hướng gió và dự báo thời tiết.
        diplomacy:
          lien_minh: 0
          tin: 10
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 10
          le_thuoc: 0
---

# Sa Mạc Hướng Đạo Hội (沙漠向导会)

## I. Tổng Quan (总览)
Sa Mạc Hướng Đạo Hội là tổ chức dẫn đường chuyên nghiệp hoạt động trên toàn Tây Mạc, với trụ sở chính tại Thiên Lý Giới Tuyến và chi nhánh nhỏ tại mỗi ốc đảo lớn. Với khoảng tám mươi hướng đạo am hiểu mọi con đường, mọi mạch cát, mọi ốc đảo ẩn trong sa mạc, hội giữ vị thế "trung lập bất khả xâm phạm" — thế lực duy nhất mà cả Sa Tặc lẫn Thiên Sa Thương Hội đều không dám đắc tội. Lý do đơn giản: không có hướng đạo, không ai qua được sa mạc an toàn. Dưới sự lãnh đạo của Hội Trưởng Phong Sa Lão Nhân — lão nhân một trăm hai mươi tuổi, mù một mắt, đã đi khắp Tây Mạc hàng trăm lần — hội duy trì nguyên tắc tuyệt đối: không phản bội khách, không dẫn vào nguy hiểm cố ý, và tuyệt đối không bao giờ dẫn đường vào Vĩnh Tịch Chi Địa bất kể giá nào.

## II. Địa Lý & Tài Nguyên (地理与资源)
Trụ sở chính đặt tại Thiên Lý Giới Tuyến — ranh giới tự nhiên giữa vùng sa mạc an toàn và vùng nguy hiểm, vị trí chiến lược để tiếp nhận khách hàng từ mọi hướng. Ngoài ra, hội duy trì chi nhánh nhỏ tại mỗi ốc đảo lớn để hướng đạo luôn sẵn sàng khi cần. Tài sản quý giá nhất là bộ bản đồ chi tiết nhất Tây Mạc — vẽ tay, cập nhật liên tục theo sự thay đổi của địa hình cát, ghi chú mọi tuyến đường an toàn, điểm nước, và khu vực nguy hiểm. Bên cạnh đó, hội sở hữu hệ thống la bàn linh tự chế — pháp khí cấp thấp nhưng được hiệu chỉnh riêng cho từ trường đặc biệt của sa mạc, chính xác hơn bất kỳ la bàn thương mại nào.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
Triết lý của hội là "Đường đi không nằm trên bản đồ — nằm trong trí nhớ." Hướng đạo tin rằng sa mạc là thực thể sống, thay đổi mỗi ngày, và chỉ có trí nhớ và kinh nghiệm trực tiếp mới đáng tin cậy — bản đồ chỉ là tham khảo. Quy tắc tối thượng: không bao giờ phản bội khách thuê, không dẫn khách vào nguy hiểm cố ý, không tiết lộ lộ trình của khách này cho kẻ khác. Mỗi hướng đạo tân gia nhập phải hoàn thành nghi thức "Độc Hành" — đi bộ xuyên sa mạc một lần hoàn toàn không dùng pháp thuật, chỉ dựa vào trí nhớ và bản năng. Cấm kỵ lớn nhất: tuyệt đối không dẫn đường vào Vĩnh Tịch Chi Địa, bất kể khách trả bao nhiêu. Bất kỳ ai vi phạm sẽ bị khai trừ vĩnh viễn.

## IV. Cơ Cấu Tổ Chức (组织结构)
Hội Trưởng Phong Sa Lão Nhân đứng đầu hội, một trăm hai mươi tuổi, đã đi khắp Tây Mạc hàng trăm lần, mù mắt phải do một sự cố bí ẩn tại rìa Vĩnh Tịch Chi Địa. Dưới ông là ba Trưởng Lão Trúc Cơ Sơ Kỳ, phụ trách ba mảng: đào tạo hướng đạo mới, phân công nhiệm vụ, và liên lạc giữa các chi nhánh ốc đảo. Khoảng tám mươi hướng đạo chính thức, đa phần ở cảnh giới Luyện Khí Trung đến Hậu Kỳ, mỗi người thuộc lòng ít nhất năm tuyến đường xuyên sa mạc. Thành viên đa dạng về xuất thân — có cả Nhân Tộc, Sa Tộc và tán tu từ khắp nơi — nhưng sau khi gia nhập hội, tất cả đều trở thành "người của sa mạc" và không mang bất kỳ phe phái nào.

## V. Công Pháp & Trận Pháp (功法与阵法)
Hướng Đạo Hội không có công pháp chiến đấu — sức mạnh của họ nằm ở tri thức chứ không phải vũ lực. Chuyên tu luyện thuật cảm ứng phong sa để dự báo thời tiết và bão cát, hướng đạo giỏi nhất có thể cảm nhận được bão cát đang hình thành trước nửa ngày. Bộ pháp đặc trưng "Thuận Phong Bộ" giúp di chuyển nhanh trên cát mà không lún — kỹ thuật đơn giản nhưng cực kỳ thực dụng, cho phép hướng đạo duy trì tốc độ ổn định suốt nhiều ngày liên tục trên sa mạc. Ngoài ra, hướng đạo biết cách đọc vệt sáng của Phong Sa Bào Tử trên cát để xác định hướng gió chủ đạo — bí quyết mà không thế lực nào khác nắm được.

## VI. Đặc Sản Môn Phái (门派特产)
- **Bản Đồ Tây Mạc:** Bộ bản đồ vẽ tay chi tiết nhất sa mạc, được cập nhật liên tục qua hàng chục thế hệ. Không có bản sao — mỗi hướng đạo ghi nhớ bản đồ trong đầu và chỉ chia sẻ bằng miệng. Đây là tài sản vô giá mà không linh thạch nào mua được.
- **La Bàn Linh Sa Mạc:** Pháp khí cấp thấp do hội tự chế, được hiệu chỉnh riêng cho từ trường đặc biệt của Tây Mạc. Chính xác hơn la bàn linh thương mại ở môi trường sa mạc, nhưng vô dụng bên ngoài sa mạc.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Trụ Sở Thiên Lý Giới Tuyến:** Tòa nhà đá nhỏ nhưng kiên cố tại ranh giới an toàn — nguy hiểm, nơi tiếp nhận khách hàng và phân công hướng đạo. Bên trong có phòng bản đồ riêng chỉ Hội Trưởng và Trưởng Lão được vào.
- **Chi Nhánh Ốc Đảo:** Các trạm nhỏ đặt tại mỗi ốc đảo lớn trên Thiên Sa Thương Đạo, nơi hướng đạo túc trực chờ khách. Mỗi trạm có ít nhất hai hướng đạo và một kho vật tư dự trữ.

## VIII. Kinh Tế (经济)
Nền kinh tế của hội dựa hoàn toàn vào dịch vụ dẫn đường. Phí dẫn đường tính theo độ dài và mức độ nguy hiểm của tuyến đường — tuyến an toàn giá rẻ, tuyến qua vùng Sa Tặc hoạt động giá gấp ba, và tuyến gần rìa Vĩnh Tịch Chi Địa thì không ai nhận bất kể giá nào. Ngoài ra, hội bán thông tin tuyến đường và tư vấn thời tiết sa mạc cho các thế lực lớn. Thiên Sa Thương Hội là khách hàng lớn nhất, trả phí cố định hàng năm để được ưu tiên sử dụng hướng đạo. Ngay cả Sa Tặc Liên Minh cũng phải trả tiền thuê hướng đạo khi cần di chuyển qua vùng xa lạ — đây là minh chứng rõ nhất cho vị thế trung lập của hội.

## IX. Lịch Sử Tóm Tắt (简史)
Hướng Đạo Hội ra đời cùng lúc với Thiên Sa Thương Đạo, ban đầu chỉ là vài dân Sa Tộc bán kiến thức đường đi cho thương nhân muốn băng qua sa mạc. Dần dần, tán tu từ khắp nơi gia nhập — những kẻ không đủ mạnh để lập tông, không đủ giàu để buôn bán, nhưng thông thạo sa mạc hơn bất kỳ ai. Qua nhiều thế hệ, hội xây dựng được vị thế "trung lập bất khả xâm phạm" — không phải bằng vũ lực mà bằng sự cần thiết. Dù yếu về tu vi, Hướng Đạo Hội là thế lực duy nhất mà mọi phe phái đều không dám đắc tội, vì thiếu họ thì sa mạc trở thành mê cung không lối thoát.

## X. Giai Thoại & Bí Mật (轶事与秘密)
- Phong Sa Lão Nhân mất con mắt phải không phải do bão cát như ông thường nói — mà do nhìn thấy thứ gì đó ở rìa Vĩnh Tịch Chi Địa trong một chuyến thám hiểm thời trẻ. Ông từ chối kể chi tiết, chỉ nói "có thứ không nên nhìn thấy, và mất một mắt là giá rẻ."
- Hội duy trì một "Hắc Danh Sách" bí mật, ghi tên những kẻ từng phản bội hoặc hại hướng đạo — bất kỳ ai trong danh sách đều không thuê được hướng đạo nào trong toàn Tây Mạc. Đây là hình phạt nặng hơn cả truy sát, vì ở sa mạc, không có người dẫn đường đồng nghĩa với cái chết.
- Gần đây, ngày càng nhiều tuyến đường cũ trở nên nguy hiểm vì cát chảy bất thường — Lão Nhân nghi ngờ Lưu Sa Khu đang mở rộng phạm vi, và nếu xu hướng này tiếp tục, toàn bộ bản đồ sa mạc sẽ phải vẽ lại từ đầu.

## XI. Quan Hệ Thế Lực (势力关系)
- **Thiên Sa Thương Hội:** Đối tác thương mại quan trọng nhất. Thương Hội trả phí cố định hàng năm để được ưu tiên thuê hướng đạo cho các thương đoàn. Quan hệ tôn trọng lẫn nhau, dù đôi khi Thương Hội cố đàm phán giảm phí.
- **Sa Tặc Liên Minh:** Kẻ thù về đạo đức nhưng khách hàng về thực tế. Sa Tặc không dám hại hướng đạo vì biết mình cũng cần dẫn đường. Mối quan hệ dựa trên sự cần thiết lẫn nhau, không phải thiện chí.
- **Phong Sa Bào Tử:** Hội là một trong số ít thế lực biết về sự tồn tại của Bào Tử. Hướng đạo sử dụng vệt sáng của Bào Tử sau bão như la bàn tự nhiên, và gọi Bào Tử Vương đen là "Hắc Tinh" — điềm xấu báo trước bão cát bất thường.
