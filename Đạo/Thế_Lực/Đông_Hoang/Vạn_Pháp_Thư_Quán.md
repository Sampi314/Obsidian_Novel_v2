---
type: faction
name: Vạn Pháp Thư Quán
hantu: 萬法書館
faction_type: Hội
alignment: 3
race: Đa chủng tộc (Chủ yếu Nhân Tộc tán tu)
region: Đông Hoang
founded: Khoảng 400 năm trước
founder: Thư Lão (danh tính thật không rõ)
emblem: Thu_Quan_Co_Thu.png
specialty: Lưu trữ bí kíp tàn khuyết, Sao chép công pháp, Nghiên cứu tán tu
economy:
- Phí đọc sách (đổi bằng bí kíp hoặc bút ký tu luyện)
- Sao chép bí kíp theo yêu cầu
- Bán bản sao công pháp cấp thấp
arcs:
  - arc: 1
    status: Ẩn dật hoạt động
    rank: Hạng Năm
    leader: Quán Chủ Thư Lão
    population: 40
    territory:
      - Hang động rừng sâu phía bắc Đông Hoang
    assets:
      - name: Kho Sách Vạn Quyển
        type: Bảo Vật
      - name: Trận Pháp Phòng Hỏa Phòng Ẩm
        type: Trận Pháp
    stats: [20, 80, 30, 40, 60, 15]
    divisions:
      - name: Ban Quản Lý Thư Quán
        role: Phân loại, bảo quản và quản lý kho sách
        headcount:
          hoi_truong: 1
          pho_hoi_truong: 0
          thanh_vien: 5
          tong_quan: 34
        members:
          - character: Thư Lão
            position: Quán Chủ
            cultivation: Kim Đan Trung Kỳ
          - character: "[Thủ Thư Nhất]"
            position: Thủ Thư Trưởng
            cultivation: Trúc Cơ Hậu Kỳ
            placeholder: true
    relationships:
      - faction: Thanh Vân Nghĩa Đoàn
        description: Tán tu trong Nghĩa Đoàn thường ghé Thư Quán đổi sách, là nguồn cung cấp bí kíp chính.
        diplomacy:
          lien_minh: 30
          tin: 40
          uy_hiep: 0
          thuong_mai: 50
          on_oan: 0
          le_thuoc: 0
      - faction: Phế Linh Các
        description: Trao đổi tài liệu về phế linh vật và công pháp tàn khuyết, cùng nghiên cứu.
        diplomacy:
          lien_minh: 20
          tin: 30
          uy_hiep: 0
          thuong_mai: 40
          on_oan: 0
          le_thuoc: 0
      - faction: Cửu Hoa Kiếm Tông
        description: Thư Quán giữ vài bản sao ngoại môn kiếm phổ cũ, Cửu Hoa biết nhưng không thèm truy cứu.
        diplomacy:
          lien_minh: 0
          tin: -10
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 0
---

# Vạn Pháp Thư Quán (萬法書館)

## I. Tổng Quan (总览)
Vạn Pháp Thư Quán là một thư viện bí mật nằm sâu trong rừng rậm phía bắc Đông Hoang, chuyên thu thập và lưu trữ các bí kíp tàn khuyết, công pháp không hoàn chỉnh, cùng bút ký tu luyện của tán tu qua nhiều đời. Xếp hạng Hạng Năm, quy mô nhỏ bé với khoảng bốn mươi người thường trú, Thư Quán tồn tại được nhờ quá xa xôi và quá khiêm tốn để bất kỳ thế lực lớn nào thèm để mắt tới. Quán Chủ là Thư Lão — một lão nhân bí ẩn tự xưng Kim Đan Trung Kỳ, đã trấn giữ nơi đây suốt bốn trăm năm. Triết lý cốt lõi của Thư Quán là "tri thức không nên bị độc quyền" — phản đối việc các đại tông phái giữ bí kíp làm của riêng, cho rằng mọi tu sĩ đều có quyền tiếp cận kiến thức tu luyện bất kể xuất thân.

## II. Địa Lý & Tài Nguyên (地理与资源)
Thư Quán tọa lạc trong một hệ thống hang động tự nhiên giữa rừng sâu phía bắc Đông Hoang, cách các tuyến đường chính ít nhất hai trăm dặm. Lối vào ẩn sau tán cây rậm rạp, không có chỉ dẫn hay cổng chào — chỉ những ai được tán tu truyền miệng mới tìm thấy. Hang đá rộng rãi, khô ráo và mát mẻ quanh năm, tạo điều kiện lý tưởng cho việc bảo quản sách vở lâu dài. Tài nguyên chủ yếu là hàng nghìn cuốn bí kíp tàn khuyết, phần lớn đã mất trang hoặc bị mờ chữ, nhưng trong đống sách tưởng như vô giá trị đó đôi khi ẩn chứa viên ngọc quý — một đoạn công pháp thượng cổ, một bút ký ghi lại ngộ giải tu luyện độc đáo mà không bí kíp hoàn chỉnh nào có được.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
Thư Quán không theo bất kỳ tín ngưỡng hay giáo phái nào. Triết lý duy nhất là chia sẻ tri thức — ai muốn đọc sách phải đóng góp, mang đến ít nhất một bí kíp hoặc bút ký tu luyện để đổi quyền đọc. Cấm tuyệt đối phá hủy sách dù tàn khuyết đến đâu, vì "mỗi dòng chữ đều là dấu vết của một tiền nhân đã bước trên con đường tu luyện." Tán tu đến đây thường ở lại vài tháng, vừa đọc vừa sao chép, vô tình tạo thành một cộng đồng nhỏ tạm thời nơi mà tu sĩ lang thang có thể trao đổi kinh nghiệm mà không sợ bị khinh miệt vì xuất thân thấp kém.

## IV. Cơ Cấu Tổ Chức (组织结构)
Cơ cấu cực kỳ đơn giản, không có hệ thống phẩm trật phức tạp. Quán Chủ Thư Lão đứng đầu, phụ trách mọi quyết định lớn nhỏ. Dưới trướng có năm vị Thủ Thư ở cảnh giới Trúc Cơ, chịu trách nhiệm phân loại kho sách thành các khu vực: Kiếm Pháp, Đan Đạo, Trận Pháp, Phù Lục, và Tạp Loại. Ngoài ra có khoảng ba mươi tán tu lưu lại dài hạn, tình nguyện giúp việc — sao chép sách bị mờ chữ, dọn dẹp hang động, canh gác — để đổi lấy quyền đọc không giới hạn. Không có quy tắc gia nhập chính thức, không có lễ bái sư, cũng không có nghĩa vụ trung thành.

## V. Công Pháp & Trận Pháp (功法与阵法)
Thư Quán không sở hữu công pháp riêng — bản thân nó là nơi lưu trữ, không phải nơi tu luyện. Tuy nhiên, kho sách chứa hàng trăm bản công pháp tàn khuyết thuộc đủ loại hệ phái, từ kiếm pháp thượng cổ bị mất đoạn đến đan quyết do tán tu tự sáng tạo. Về trận pháp, Thư Lão đích thân bố trí một trận pháp phòng hỏa và phòng ẩm bao quanh toàn bộ kho sách, đảm bảo không một tia lửa hay giọt nước nào có thể xâm nhập. Trận pháp này hoạt động âm thầm suốt bốn trăm năm, chất lượng tinh xảo đến mức nhiều tán tu nghi ngờ Thư Lão không chỉ đơn thuần là Kim Đan Trung Kỳ.

## VI. Đặc Sản Môn Phái (门派特产)
- **Bản Sao Tàn Khuyết:** Thư Quán cung cấp bản sao chép tay các bí kíp cấp thấp cho tán tu không có nguồn gốc tông môn, dù không hoàn chỉnh nhưng đủ để tu luyện qua giai đoạn Luyện Khí và Trúc Cơ.
- **Bút Ký Tổng Hợp:** Thủ Thư biên soạn các tập bút ký tổng hợp kinh nghiệm tu luyện từ nhiều tán tu khác nhau, gọi là "Tán Tu Chỉ Nam," được coi là tài liệu quý giá nhất cho tu sĩ không có sư phụ.
- **Dịch Vụ Giám Định:** Thư Lão có khả năng giám định sơ bộ một bí kíp là thật hay giả, tàn khuyết ở mức nào — dịch vụ này thu phí bằng linh thạch hoặc bí kíp khác.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Kho Sách Chính:** Hang động trung tâm rộng lớn nhất, tường đá được mài nhẵn và khắc kệ sách, chứa hàng nghìn cuốn phân loại theo hệ phái.
- **Phòng Sao Chép:** Bốn phòng nhỏ trang bị bàn đá, mực linh và giấy phù — nơi tán tu ngồi sao chép sách.
- **Khu Nghỉ Ngơi:** Các hốc đá tự nhiên được mở rộng làm phòng ngủ cho khách thường trú.
- **Phòng Kín Thư Lão:** Một hang động riêng biệt nằm sâu nhất, khóa bằng trận pháp đặc biệt — nơi Thư Lão cất giữ những cuốn sách mà lão cho là quá nguy hiểm hoặc quá quý giá để mở cho công chúng.

## VIII. Kinh Tế (经济)
Kinh tế của Thư Quán gần như tự cung tự cấp và phi tiền tệ. Hệ thống trao đổi chính là "sách đổi sách" — mang đến một bí kíp để đổi quyền đọc, hoặc sao chép xong một cuốn sách bị mờ chữ để đổi lấy quyền đọc cuốn khác. Thỉnh thoảng, tán tu giàu có hơn trả bằng linh thạch để mua bản sao, nhưng số lượng ít ỏi. Thư Quán không tích lũy tài sản, không buôn bán lớn — tồn tại hoàn toàn nhờ lòng tự nguyện đóng góp của cộng đồng tán tu.

## IX. Lịch Sử Tóm Tắt (简史)
Thư Lão xuất hiện ở rừng sâu Đông Hoang khoảng bốn trăm năm trước, bắt đầu thu thập bí kíp tàn khuyết mà các tông phái vứt bỏ. Không ai biết lão từ đâu đến hay vì sao chọn cuộc sống ẩn dật giữa rừng già. Dần dần, tiếng đồn lan trong giới tán tu — có một nơi trong rừng sâu mà ai cũng được đọc sách miễn phí nếu mang đến thứ gì đó để đổi. Từ một hang đá nhỏ chứa vài chục cuốn sách, Thư Quán phát triển thành kho tàng hàng nghìn quyển. Thư Quán chưa bao giờ bị tấn công hay cướp phá — không phải vì mạnh mà vì quá xa xôi và trong mắt các thế lực lớn, một đống bí kíp tàn khuyết không đáng để hao binh tốn sức.

## X. Giai Thoại & Bí Mật (轶事与秘密)
Có tin đồn Thư Lão thực ra là một Nguyên Anh bị tổn thương tu vi, ẩn thân dưới dạng Kim Đan. Bằng chứng gián tiếp là trận pháp phòng hỏa do lão bố trí có độ tinh xảo vượt xa tầm Kim Đan — ít nhất phải là Nguyên Anh mới có thể tạo ra trận pháp bền vững suốt bốn trăm năm mà không cần bảo trì.

Trong kho sách có một cuốn bí kíp bị Thư Lão khóa kín bằng trận pháp riêng, không cho bất kỳ ai đọc — dù nhiều tán tu cầu xin và đề nghị trả giá cao. Có giả thuyết rằng đó là một phần của công pháp cấm đã thất truyền, và chính cuốn sách này là lý do thực sự Thư Lão mở Thư Quán — lão đang tìm kiếm những phần còn lại thông qua mạng lưới tán tu mang sách đến đổi chác.

## XI. Quan Hệ Thế Lực (势力关系)
- **Thanh Vân Nghĩa Đoàn:** Nguồn cung cấp bí kíp chính, tán tu trong Nghĩa Đoàn thường ghé Thư Quán đổi sách sau mỗi chuyến phiêu lưu.
- **Phế Linh Các:** Trao đổi tài liệu về phế linh vật và công pháp tàn khuyết, mối quan hệ nghiên cứu đôi bên cùng có lợi.
- **Cửu Hoa Kiếm Tông:** Thư Quán giữ vài bản sao kiếm phổ ngoại môn cũ của Cửu Hoa; tông môn biết nhưng coi nhẹ, không buồn truy cứu vì chỉ là bản tàn khuyết.
