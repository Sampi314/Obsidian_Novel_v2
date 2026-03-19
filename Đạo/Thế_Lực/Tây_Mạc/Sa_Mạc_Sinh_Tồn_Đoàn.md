---
type: faction
name: Sa Mạc Sinh Tồn Đoàn
hantu: 沙漠生存团
faction_type: Hội
alignment: 3
race: Nhân Tộc (Tán tu)
region: Tây Mạc
founded: Năm Khởi Nguyên 97.970
founder: Một nhóm tán tu Luyện Khí sống sót sau vụ tấn công của Sa Tặc
emblem: La_Ban_Va_Day_Thua.png
specialty: Dẫn đường sinh tồn, Cứu nạn sa mạc, Tìm kiếm thất lạc
economy:
  - Dịch vụ dẫn đường qua Hoàng Kim Sa Hải
  - Thu phí cứu nạn và tìm kiếm thất lạc
  - Bán bản đồ thủ công và thuốc giải độc sa trùng
arcs:
  - arc: 1
    status: Hoạt động (Dẫn đường tuyến Lưu Sa Khu)
    rank: Hạng Năm
    leader: Đoàn Trưởng Hạ Thiên Lý
    population: 50
    territory:
      - Thiên Lý Giới Tuyến (biên giới đông Tây Mạc)
      - Tuyến đường đến Lưu Sa Khu
    assets:
      - name: La bàn xương cổ
        type: Pháp Khí
      - name: Cuốn da thú ghi đường đi bí mật
        type: Bí Tịch
    stats: [30, 15, 40, 50, 10, 25]
    divisions:
      - name: Ban Dẫn Đường
        role: Dẫn đường cho thương đoàn và lữ khách qua sa mạc, tìm kiếm cứu nạn
        headcount:
          hoi_truong: 1
          pho_hoi_truong: 3
          thanh_vien: 46
          tong_quan: 0
        members:
          - character: Hạ Thiên Lý
            position: Đoàn Trưởng
            cultivation: Trúc Cơ Sơ Kỳ
          - character: "[Phó Đoàn Tuyến Bắc]"
            position: Phó Đoàn Trưởng
            cultivation: Luyện Khí Đỉnh Phong
            placeholder: true
          - character: "[Phó Đoàn Tuyến Trung]"
            position: Phó Đoàn Trưởng
            cultivation: Luyện Khí Đỉnh Phong
            placeholder: true
          - character: "[Phó Đoàn Tuyến Nam]"
            position: Phó Đoàn Trưởng
            cultivation: Luyện Khí Đỉnh Phong
            placeholder: true
    relationships:
      - faction: Sa Mạc Hướng Đạo Hội
        description: Cùng ngành dẫn đường, cạnh tranh nhẹ về khách hàng nhưng thường hợp tác chia sẻ thông tin đường đi.
        diplomacy:
          lien_minh: 30
          tin: 50
          uy_hiep: 0
          thuong_mai: 40
          on_oan: 0
          le_thuoc: 0
      - faction: Thiên Sa Thương Hội
        description: Nguồn khách hàng chính, nhận hợp đồng dẫn đường cho các thương đoàn nhỏ mà Thương Hội không trực tiếp hộ tống.
        diplomacy:
          lien_minh: 10
          tin: 30
          uy_hiep: 0
          thuong_mai: 60
          on_oan: 0
          le_thuoc: 20
      - faction: Sa Tặc Liên Minh
        description: Kẻ thù truyền kiếp, nguyên nhân thành lập đoàn. Thường xuyên phải đối phó khi Sa Tặc phục kích trên tuyến đường.
        diplomacy:
          lien_minh: -80
          tin: -70
          uy_hiep: 30
          thuong_mai: -100
          on_oan: -60
          le_thuoc: 0
---

# Sa Mạc Sinh Tồn Đoàn (沙漠生存团)

## I. Tổng Quan (总览)

Sa Mạc Sinh Tồn Đoàn là một tổ chức nhỏ gồm khoảng năm mươi tán tu chuyên cung cấp dịch vụ dẫn đường và cứu nạn trên sa mạc Hoàng Kim Sa Hải. Trụ sở đặt tại Thiên Lý Giới Tuyến, vùng chuyển tiếp giữa Trung Thổ và sa mạc, nơi phần lớn lữ khách bắt đầu hành trình xuyên cát. Dù chỉ là thế lực Hạng Năm với tu vi bình thường, đoàn lại có tỉ lệ dẫn khách sống sót cao đáng ngạc nhiên nhờ kinh nghiệm thực chiến dày dặn và sự am hiểu tường tận mọi dấu hiệu nguy hiểm trên sa mạc. Đoàn Trưởng Hạ Thiên Lý, một tán tu Trúc Cơ Sơ Kỳ từng suýt chết mười lần trên cát, đã đưa đoàn phát triển ổn định trong hai mươi năm qua.

## II. Địa Lý & Tài Nguyên (地理与资源)

Trụ sở chính đặt tại Thiên Lý Giới Tuyến, vùng đất cát xen lẫn đá sỏi nằm ở biên giới đông Tây Mạc. Gió thổi mạnh quanh năm, vài đụn cát lớn được dùng làm mốc dẫn đường tự nhiên. Tuy địa hình khắc nghiệt, đây lại là vị trí chiến lược vì mọi lữ khách muốn vào Hoàng Kim Sa Hải đều phải qua đây. Tài nguyên chính của đoàn không nằm ở khoáng sản hay linh điền, mà ở kiến thức: bản đồ thủ công vẽ bằng tay được cập nhật liên tục, la bàn linh thô sơ tự chế, nước dự trữ trong bầu da thú, và đặc biệt là một cuốn da thú ghi chép đường đi bí mật xuyên Hoàng Kim Sa Hải mà Đoàn Trưởng Hạ Thiên Lý nhận được từ một Sa Tộc trước khi chết.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)

Triết lý cốt lõi của đoàn là "Sống qua một đêm trên sa mạc, đã là chiến thắng." Đây không phải lời nói sáo rỗng mà là bài học máu xương của những người sáng lập, những tán tu từng bị bỏ rơi giữa sa mạc và thoát chết trong gang tấc. Ai muốn gia nhập phải vượt qua thử thách ba ngày ba đêm một mình trong Hoàng Kim Sa Hải, không mang theo pháp khí hỗ trợ. Trước mỗi chuyến đi, toàn đoàn có phong tục rắc cát lên trán cầu xin sa mạc "tha mạng", một nghi thức giản dị nhưng không ai dám bỏ qua. Cấm kỵ lớn nhất là bỏ rơi đồng đội, bất kể hoàn cảnh nào. Kẻ vi phạm sẽ bị trục xuất vĩnh viễn và tên bị xóa khỏi mọi ghi chép của đoàn.

## IV. Cơ Cấu Tổ Chức (组织结构)

Cơ cấu đoàn đơn giản gọn nhẹ, phù hợp với quy mô nhỏ và tính chất công việc thực địa. Đứng đầu là Đoàn Trưởng Hạ Thiên Lý, tán tu Trúc Cơ Sơ Kỳ, người từng suýt chết mười lần trên sa mạc và nhờ vậy thuộc lòng mọi dấu hiệu nguy hiểm. Dưới ông là ba Phó Đoàn Trưởng tu vi Luyện Khí Đỉnh Phong, mỗi người phụ trách một tuyến đường riêng: tuyến Bắc đến các ốc đảo phía bắc, tuyến Trung xuyên trung tâm Hoàng Kim Sa Hải, và tuyến Nam đến Lưu Sa Khu. Khoảng bốn mươi sáu thành viên còn lại đa phần là tán tu Luyện Khí Trung đến Hậu Kỳ, được phân tổ theo tuyến đường và luân phiên nghỉ ngơi giữa các chuyến dẫn khách.

## V. Công Pháp & Trận Pháp (功法与阵法)

Sa Mạc Sinh Tồn Đoàn không có công pháp chính thức truyền thừa. Thành viên chủ yếu dựa vào kinh nghiệm thực chiến và bản năng sinh tồn được mài giũa qua hàng trăm chuyến đi xuyên sa mạc. Kỹ thuật duy nhất được truyền dạy trong đoàn là Phong Sa Thuật sơ đẳng, cho phép tạo một lớp chắn cát mỏng khi gặp bão, đủ để bảo vệ khách hàng trong vài khắc chờ bão qua. Trang bị chủ yếu gồm dây thừng linh dùng để kết nối thành viên tránh thất lạc trong bão, đuốc chống gió chiếu sáng ban đêm, và thuốc giải độc sa trùng tự bào chế. Tuy thiếu sức mạnh chiến đấu, khả năng sinh tồn và ứng biến trên sa mạc của đoàn không hề thua kém bất kỳ thế lực nào.

## VI. Đặc Sản Môn Phái (门派特产)

- **Bản Đồ Sinh Tồn Thiên Lý:** Bản đồ vẽ tay chi tiết các tuyến đường an toàn xuyên Hoàng Kim Sa Hải, được cập nhật liên tục theo sự thay đổi của cát chảy và bão. Mỗi bản đồ đều đánh dấu điểm nước, vùng Sa Trùng nguy hiểm và khu vực Sa Tặc thường hoạt động.
- **Thuốc Giải Độc Sa Trùng:** Loại thuốc đơn giản nhưng hiệu quả do đoàn tự bào chế từ thảo dược sa mạc, chuyên trị nọc độc của các loài trùng nhỏ sống trong cát.

## VII. Cơ Sở Hạ Tầng (基础设施)

- **Trại Thiên Lý:** Trụ sở nhỏ tại Thiên Lý Giới Tuyến, gồm vài lều da thú và một kho chứa trang bị. Không hào nhoáng nhưng đủ để làm điểm xuất phát và nghỉ ngơi giữa các chuyến đi.
- **Trạm Dừng Chân Cát:** Ba trạm nhỏ đặt dọc các tuyến đường, mỗi trạm là một hố đào sâu trong cát có mái che, chứa nước dự trữ và vật tư cấp cứu cho trường hợp khẩn cấp.

## VIII. Kinh Tế (经济)

Kinh tế của đoàn dựa hoàn toàn vào dịch vụ dẫn đường và cứu nạn. Phí dẫn đường tính theo độ dài và độ nguy hiểm của tuyến đường, trong đó tuyến Lưu Sa Khu có giá cao nhất nhưng cũng rủi ro lớn nhất. Ngoài ra, đoàn còn bán bản đồ thủ công và thuốc giải độc sa trùng cho lữ khách, tuy thu nhập không nhiều nhưng đủ để duy trì hoạt động. Nguồn thu ổn định nhất đến từ các hợp đồng nhỏ của Thiên Sa Thương Hội, hộ tống những đoàn thương nhỏ mà Thương Hội không trực tiếp bảo vệ.

## IX. Lịch Sử Tóm Tắt (简史)

Sa Mạc Sinh Tồn Đoàn thành lập cách đây hơn ba mươi năm, khi một nhóm tán tu Luyện Khí bị bỏ rơi giữa sa mạc sau khi thương đoàn thuê họ bị Sa Tặc tấn công. Những kẻ sống sót, thay vì oán hận hay bỏ cuộc, quyết định lập đoàn tự cứu lẫn nhau, sau đó chuyển sang kiếm sống bằng nghề dẫn đường. Tiếng tăm dần lan rộng nhờ tỉ lệ sống sót cao đáng ngạc nhiên so với những hướng đạo tự do.

Hạ Thiên Lý gia nhập hai mươi năm trước với tư cách Luyện Khí Sơ Kỳ. Qua nhiều lần thoát chết trên sa mạc, ông tích lũy đủ ngộ tính và linh lực để đột phá Trúc Cơ, trở thành tu sĩ mạnh nhất đoàn và được bầu làm Đoàn Trưởng. Dưới thời ông, đoàn mạo hiểm mở thêm tuyến đường đến Lưu Sa Khu, tuyến nguy hiểm nhất nhưng lợi nhuận cũng cao nhất.

## X. Giai Thoại & Bí Mật (轶事与秘密)

Đoàn Trưởng Hạ Thiên Lý sở hữu một chiếc la bàn cổ bằng xương, không ai biết lai lịch. La bàn không chỉ hướng bắc như thông thường mà luôn chỉ về một nơi nào đó sâu trong Vĩnh Tịch Chi Địa, vùng cấm mà ngay cả Sa Mạc Hướng Đạo Hội cũng tuyệt đối không dẫn khách vào. Hạ Thiên Lý chưa bao giờ dám đi theo hướng la bàn chỉ, nhưng ông giữ nó bên mình suốt hai mươi năm như một lời nhắc nhở rằng sa mạc vẫn còn nhiều bí mật chưa ai chạm đến.

Có tin đồn rằng một vài thành viên cũ từng lạc vào Lưu Sa Cổ Thành và mang về di vật kỳ lạ, nhưng không ai dám nói thêm chi tiết, và những người đó sau này đều biến mất không dấu vết. Ngoài ra, đoàn từng cứu được một Sa Tộc bị thương nặng giữa sa mạc. Người đó trước khi chết đã tặng Hạ Thiên Lý cuốn da thú ghi chép đường đi bí mật xuyên Hoàng Kim Sa Hải, đây là bảo vật quý nhất mà đoàn sở hữu và cũng là lý do tuyến Lưu Sa Khu có thể mở được.

## XI. Quan Hệ Thế Lực (势力关系)

- **Sa Mạc Hướng Đạo Hội:** Cùng ngành dẫn đường, hai bên cạnh tranh nhẹ về khách hàng nhưng nhìn chung giữ quan hệ hữu hảo. Thường xuyên chia sẻ thông tin về tình hình đường đi và cảnh báo bão cát cho nhau. Sinh Tồn Đoàn chuyên các tuyến ngắn nguy hiểm, còn Hướng Đạo Hội thiên về tuyến dài an toàn.
- **Thiên Sa Thương Hội:** Nguồn khách hàng quan trọng nhất. Đoàn nhận hợp đồng hộ tống các thương đoàn nhỏ mà Thương Hội không trực tiếp bảo vệ. Quan hệ mang tính thương mại, không thân thiết nhưng ổn định.
- **Sa Tặc Liên Minh:** Kẻ thù truyền kiếp. Cuộc tấn công của Sa Tặc chính là nguyên nhân khiến đoàn ra đời. Đến nay, Sa Tặc vẫn thường xuyên phục kích trên các tuyến đường mà đoàn hoạt động, tạo nên mối thù không thể hóa giải.
