---
type: faction
name: Mật Lâm Thợ Săn Hội
hantu: 密林猎人会
faction_type: Hội
alignment: 1
race: Nhân Tộc (Tán tu)
region: Đông Hoang
founded: Cách đây hơn 100 năm
founder: Nhóm tán tu khai hoang
emblem: Dau_Chan_Thu_Va_Mui_Ten.png
specialty: Săn bắt yêu thú rừng rậm, Di chuyển vô thanh trong rừng sâu, Chế tạo bẫy thú cấp thấp
economy:
- Bán nội đan yêu thú cấp thấp
- Bán da, xương, gân yêu thú cho thương nhân
- Dịch vụ hướng đạo rừng rậm cho tán tu và thương đội
arcs:
  - arc: 1
    status: Hoạt động ổn định (bị sơn tặc quấy rối)
    rank: Hạng Năm
    leader: Hội Trưởng Mã Lâm
    population: 80
    territory:
      - Trạm Biên Nam Cương (trụ sở chính)
      - Rừng rậm ngoại vi Rừng Huyết Độc (khu vực săn bắt)
    assets:
      - name: Kho Da Thú và Xương Yêu
        type: Kho Tàng
      - name: Bản đồ đường rừng chi tiết nhất Trạm Biên
        type: Tài Nguyên
      - name: Mật Lâm Bộ Pháp
        type: Bí Thuật
    stats: [100, 80, 60, 80, 50, 40]
    divisions:
      - name: Đội Săn
        role: Tổ chức các chuyến săn yêu thú theo khu vực, thu thập nội đan và nguyên liệu từ thú
        headcount:
          hoi_truong: 1
          pho_hoi_truong: 1
          thanh_vien: 48
          tong_quan: 30
        members:
          - character: Mã Lâm
            position: Hội Trưởng
            cultivation: Trúc Cơ Hậu Kỳ
          - character: Diệp Hồng Nương
            position: Phó Hội Trưởng
            cultivation: Trúc Cơ Trung Kỳ
          - character: "[Thiết Trảo]"
            position: Đội Trưởng Đội Nhất
            cultivation: Trúc Cơ Sơ Kỳ
            placeholder: true
    relationships:
      - faction: Hắc Báo Trại
        description: Xung đột thường xuyên — sơn tặc Hắc Báo Trại hay phục kích cướp chiến lợi phẩm của thợ săn trên đường từ rừng về trạm, gây tổn thất nặng nề.
        diplomacy:
          lien_minh: -50
          tin: 0
          uy_hiep: 40
          thuong_mai: 0
          on_oan: -60
          le_thuoc: 0
      - faction: Vạn Trùng Cốc
        description: Sợ hãi và tránh xa — Mã Lâm từng lạc vào lãnh địa Vạn Trùng Cốc và suýt mất mạng, từ đó cấm tuyệt đối thành viên tiếp cận khu vực này.
        diplomacy:
          lien_minh: -20
          tin: 5
          uy_hiep: 70
          thuong_mai: 0
          on_oan: -30
          le_thuoc: 0
      - faction: Hoang Dã Thợ Săn Bang
        description: Quan hệ ngang hàng nhưng ngại nhau — hai bên cùng nghề săn bắt nhưng hoạt động ở vùng khác nhau. Đôi khi chia sẻ thông tin về yêu thú nguy hiểm.
        diplomacy:
          lien_minh: 20
          tin: 30
          uy_hiep: 0
          thuong_mai: 20
          on_oan: 0
          le_thuoc: 0
---

# Mật Lâm Thợ Săn Hội (密林猎人会)

## I. Tổng Quan (总览)
Mật Lâm Thợ Săn Hội là một tổ chức thợ săn yêu thú có trụ sở tại Trạm Biên Nam Cương, chuyên hoạt động trong vùng rừng rậm ngoại vi Rừng Huyết Độc. Với khoảng tám mươi thành viên từ phàm nhân học việc đến Trúc Cơ kỳ cựu, Hội là thế lực nhỏ nhưng không thể thiếu tại Trạm Biên — họ cung cấp nội đan, da xương yêu thú, và đặc biệt là bản đồ đường rừng chi tiết nhất khu vực cho các đoàn thám hiểm. Dẫn dắt bởi Hội Trưởng Mã Lâm, một thợ săn kỳ cựu với bốn mươi năm kinh nghiệm và cơ thể đầy sẹo từ nanh vuốt yêu thú, Hội tồn tại bằng triết lý giản dị: sống nhờ rừng nhưng không lấy quá phần mình.

## II. Địa Lý & Tài Nguyên (地理与资源)
Trụ sở chính đặt tại khu nhà gỗ phía đông Trạm Biên Nam Cương, gần cổng rừng — vị trí thuận lợi để xuất phát và trở về sau mỗi chuyến săn. Khu trụ sở gồm một dãy nhà gỗ thấp với kho chứa da thú và xương yêu, phòng họp, và nhà nghỉ cho thợ săn. Sâu trong rừng rậm, Hội duy trì một hệ thống trạm nghỉ tạm rải rác, đánh dấu bằng vết khắc bí mật trên thân cây mà chỉ thành viên Hội mới nhận ra. Khu vực săn bắt chủ yếu ở vùng ngoại vi Rừng Huyết Độc — sâu hơn nữa thì yêu thú quá mạnh, nông hơn thì thú đã bị săn cạn. Tài nguyên chính là nội đan yêu thú cấp thấp, da, xương, gân yêu thú — tất cả đều có giá trị với thương nhân và tu sĩ cần nguyên liệu.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
Triết lý cốt lõi của Hội là "Rừng cho ta sống, ta không lấy quá phần mình." Thợ săn chỉ săn để mưu sinh, không tàn sát bừa bãi, và tôn trọng cân bằng sinh thái của rừng. Quy tắc bất khả xâm phạm gồm ba điều: không săn yêu thú mang thai, không vào lãnh địa của yêu thú đã hóa hình, và mỗi chuyến săn phải chia phần cho người canh gác trạm. Trước mỗi chuyến săn, thành viên đốt một nắm lá rừng cầu bình an — nghi thức đơn giản nhưng không ai bỏ qua vì tin rằng rừng sẽ phù hộ kẻ kính cẩn. Thợ săn chết trong rừng sẽ được chôn tại chỗ, trồng cây lên mộ — họ tin rằng linh hồn thợ săn sẽ hóa thành thần rừng bảo vệ đồng đội.

## IV. Cơ Cấu Tổ Chức (组织结构)
Hội Trưởng Mã Lâm nắm quyền quyết định mọi việc, từ phân chia khu vực săn bắt đến đối ngoại. Phó Hội Trưởng Diệp Hồng Nương — nữ thợ săn giỏi nhất Hội, chuyên gia đặt bẫy — hỗ trợ quản lý và thay thế khi Mã Lâm đi vắng. Dưới hai người là năm đội săn, mỗi đội sáu đến tám người từ Luyện Khí đến Trúc Cơ Sơ Kỳ, phụ trách một khu vực rừng riêng biệt. Mỗi đội có một Đội Trưởng chịu trách nhiệm an toàn cho cả nhóm. Ngoài ra có khoảng ba mươi phàm nhân đang học nghề — tân binh phải đi theo đội cũ ít nhất một năm trước khi được phép tự hành động. Tổng cộng khoảng tám mươi người, quy mô nhỏ nhưng gắn bó chặt chẽ.

## V. Công Pháp & Trận Pháp (功法与阵法)
Hội không có công pháp chính thức truyền thừa — thành viên tu luyện các tạp công pháp luyện thể và cảm ứng yêu khí tùy theo khả năng cá nhân. Tuy nhiên, Hội sở hữu bộ "Mật Lâm Bộ Pháp" — kỹ thuật di chuyển trong rừng rậm không phát ra tiếng động, truyền miệng từ thế hệ sáng lập. Bộ pháp này không phải công pháp tu tiên mà là kinh nghiệm thực chiến: cách đặt chân tránh lá khô, cách điều hòa hơi thở khiến yêu thú không nghe thấy, cách di chuyển ngược gió để che mùi. Về bẫy trận, Diệp Hồng Nương phát triển một bộ "Thiên La Bẫy Trận" gồm hàng chục kiểu bẫy kết hợp dây, gỗ, và phù lục cấp thấp, có thể bắt sống yêu thú Luyện Khí và làm chậm yêu thú Trúc Cơ.

## VI. Đặc Sản Môn Phái (门派特产)
- **Nội Đan Yêu Thú Cấp Thấp:** Sản phẩm chính, thu được từ yêu thú Luyện Khí trong rừng. Chất lượng ổn định vì thợ săn kinh nghiệm biết cách lấy đan mà không làm vỡ.
- **Bộ Da Xương Yêu Thú:** Nguyên liệu luyện khí và chế tác pháp khí cấp thấp, đặc biệt da Huyết Báo rừng rất được ưa chuộng vì bền và nhẹ.
- **Bản Đồ Đường Rừng:** Bản đồ chi tiết nhất Trạm Biên về đường đi trong rừng rậm, đánh dấu hang ổ yêu thú, vùng nguy hiểm, và nguồn nước an toàn. Chỉ bán cho khách hàng được tin tưởng.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Dãy Nhà Gỗ Trụ Sở:** Khu nhà gỗ thấp tại phía đông Trạm Biên, gồm phòng họp, nhà nghỉ, và kho chứa chiến lợi phẩm. Tường nhà treo đầy da thú và vũ khí cũ như trang trí kiêm nhắc nhở.
- **Kho Da Thú và Xương Yêu:** Kho chứa lớn nhất, dùng muối linh và tro thuốc để bảo quản da xương, ngăn mùi hôi và phân hủy.
- **Hệ Thống Trạm Nghỉ Rừng:** Năm trạm nghỉ tạm nằm sâu trong rừng, mỗi trạm là một hốc đá hoặc nhà cây nhỏ có dự trữ thức ăn khô và thuốc sơ cứu. Vị trí đánh dấu bằng vết khắc bí mật.
- **Sân Huấn Luyện Tân Binh:** Khu đất trống phía sau trụ sở, nơi tân binh luyện tập đặt bẫy, theo dấu, và chiến đấu cơ bản.

## VIII. Kinh Tế (经济)
Kinh tế của Hội dựa hoàn toàn vào săn bắt. Sau mỗi chuyến săn, chiến lợi phẩm được phân chia theo quy tắc: ba phần mười nộp cho Hội (duy trì hoạt động chung), bảy phần mười chia cho đội săn theo công sức. Nội đan bán cho thương nhân lưu động hoặc tiệm dược ở Trạm Biên, da xương bán cho thợ rèn và thợ thuộc da. Doanh thu không cao vì yêu thú cấp thấp cho nội đan giá rẻ, nhưng đủ để duy trì Hội và nuôi sống gia đình thành viên. Gần đây, thu nhập giảm sút vì Hắc Báo Trại liên tục cướp chiến lợi phẩm trên đường về, khiến một số đội phải đổi tuyến đường dài hơn và tốn kém hơn.

## IX. Lịch Sử Tóm Tắt (简史)
Hội thành lập hơn một trăm năm trước bởi một nhóm tán tu không đủ tài nguyên và tư chất để tu luyện, quyết định chuyển sang săn yêu thú kiếm sống. Ban đầu chỉ có bảy người, dần dần thu hút thêm tán tu và phàm nhân cùng cảnh ngộ. Hai mươi năm trước, Hội chịu tổn thất nặng nề nhất trong lịch sử khi một đợt Trùng Triều — hiện tượng yêu trùng bùng phát từ rừng sâu — tràn qua khu vực săn bắt, giết chết gần nửa thành viên. Mã Lâm, khi đó là Đội Trưởng Đội Nhất, dẫn số sống sót rút về Trạm Biên và gây dựng lại Hội từ đống đổ nát. Ông trở thành Hội Trưởng và giữ chức vụ này đến nay. Gần đây, mối đe dọa chính không còn là yêu thú mà là Hắc Báo Trại — sơn tặc ngày càng liều lĩnh cướp bóc thợ săn.

## X. Giai Thoại & Bí Mật (轶事与秘密)
Mã Lâm từng lạc vào sào huyệt Vạn Trùng Cốc và sống sót nhờ mùi dược thảo trên người khiến trùng không dám lại gần. Loại dược thảo đó mọc ở một nơi bí mật trong rừng mà hắn chỉ chia sẻ vị trí với người kế nhiệm — đây là "bảo hiểm sinh mạng" cuối cùng của Hội Trưởng.

Trong rừng sâu có một "Cấm Địa Thợ Săn" mà không ai dám bước vào — nơi đó có xác một yêu thú cổ đại chưa phân hủy, thi thể tỏa ra uy áp khiến ngay cả Trúc Cơ cũng run rẩy. Một số thợ săn già tin rằng nếu ai lấy được nội đan của xác yêu thú đó, có thể đổi đời, nhưng chưa ai đủ dũng cảm thử. Diệp Hồng Nương lặng lẽ nghiên cứu loại bẫy mới, hy vọng một ngày có thể trấn áp uy áp tàn dư của xác thú cổ đại kia.

## XI. Quan Hệ Thế Lực (势力关系)
- **Hắc Báo Trại:** Kẻ thù trực tiếp — sơn tặc liên tục phục kích cướp chiến lợi phẩm của thợ săn. Hai bên đã nhiều lần đụng độ đẫm máu, nhưng Hội không đủ sức tiêu diệt Trại.
- **Vạn Trùng Cốc:** Mối đe dọa tiềm tàng — Hội tuyệt đối tránh xa lãnh thổ Vạn Trùng Cốc. Đợt Trùng Triều hai mươi năm trước khiến Hội mất gần nửa người, nỗi sợ vẫn còn ám ảnh.
- **Hoang Dã Thợ Săn Bang:** Đồng nghiệp cùng ngành, hoạt động ở vùng khác nhưng đôi khi chia sẻ thông tin về yêu thú nguy hiểm và tuyến đường an toàn.
- **Nam Cương Dược Sư Hội:** Khách hàng mua nội đan và nguyên liệu yêu thú để luyện dược, quan hệ thương mại ổn định.
