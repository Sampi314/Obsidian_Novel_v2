---
type: faction
name: Huyết Hổ Hạ Chúng
hantu: 血虎下众
faction_type: Bộ Lạc
alignment: -3
race: Yêu Tộc (Hổ Yêu)
region: Vô Tận Hải
founded: 800 năm trước
founder: Huyết Hổ Vương (bắt buộc thần phục)
emblem: Mong_Vuot_Ho_Do.png
specialty: Săn bắt bản năng, Trinh sát rừng tuyết, Huyết mạch hổ chiến
economy:
- Săn bắt thú rừng cống nạp
- Buôn bán da lông và xương thú
- Canh gác lãnh thổ cho Huyết Hổ Vương
arcs:
  - arc: 1
    status: Nô dịch — oán hận ngầm
    rank: Hạng Năm
    leader: Quản Sự Hổ Nha Tam
    population: 120
    territory:
      - Vùng ven biển Bắc Hải
      - Rừng tuyết ngoại vi Núi Độc Long
    assets:
      - name: Hang Đá Tuyết Lâm
        type: Công Trình
      - name: Kho Cống Nạp Bí Mật
        type: Tài Nguyên
    stats: [40, 20, 10, 120, 30, 15]
    divisions:
      - name: Thợ Săn Đội
        role: Săn bắt thú rừng, thu thập tài nguyên, cống nạp cho Huyết Hổ Vương
        headcount:
          truong_lao: 1
          chien_binh: 35
          dan_thuong: 84
        members:
          - character: Hổ Nha Tam
            position: Quản Sự (Tộc Trưởng)
            cultivation: Trúc Cơ Viên Mãn
            placeholder: false
          - character: "[Hổ Yêu Trắng Đột Biến]"
            position: Ấu Sinh
            cultivation: Chưa hóa hình
            placeholder: true
    relationships:
      - faction: Huyết Hổ Vương
        description: Phục tùng tuyệt đối dưới sức mạnh áp chế. Hạ Chúng là nô bộc, đời đời kiếp kiếp cống nạp và phục dịch, oán hận tích tụ ngấm ngầm.
        diplomacy:
          lien_minh: -10
          tin: -70
          uy_hiep: 95
          thuong_mai: -50
          on_oan: -80
          le_thuoc: 95
      - faction: Bắc Hải Cự Yêu Hang
        description: Hổ Nha Tam lén liên lạc tìm đồng minh, hy vọng có ngày thoát khỏi sự cai trị tàn bạo của Huyết Hổ Vương.
        diplomacy:
          lien_minh: 15
          tin: 10
          uy_hiep: 0
          thuong_mai: 5
          on_oan: 0
          le_thuoc: 0
      - faction: Băng Lang Tàn Đội
        description: Cùng là yêu tộc cấp thấp bị áp bức, đồng cảnh ngộ nhưng chưa liên lạc chính thức.
        diplomacy:
          lien_minh: 5
          tin: 5
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 0
---

# Huyết Hổ Hạ Chúng (血虎下众)

## I. Tổng Quan (总览)
Huyết Hổ Hạ Chúng là tập hợp những hổ yêu cấp thấp sống dưới sự cai trị tàn bạo của Huyết Hổ Vương tại vùng ven biển Bắc Hải. Với khoảng một trăm hai mươi thành viên gồm hổ yêu đã hóa hình và ấu sinh chưa khai linh, Hạ Chúng tồn tại như một bộ lạc nô dịch — săn bắt, cống nạp, canh gác, và đổi lại chỉ nhận được sự "bảo hộ" khỏi các yêu tộc khác. Quản Sự Hổ Nha Tam, một hổ yêu già tu vi Trúc Cơ Viên Mãn, giữ vai trò truyền đạt mệnh lệnh của Huyết Hổ Vương, nhưng trong lòng ấp ủ những toan tính riêng. Đây là thế lực Hạng Năm, yếu ớt về mọi mặt nhưng chứa đựng những mầm mống phản kháng đáng chú ý.

## II. Địa Lý & Tài Nguyên (地理 与 资源)
Hạ Chúng cư ngụ tại vùng đá ven rừng tuyết, nơi biên giới giữa Bắc Hải và ngoại vi dãy Núi Độc Long giao nhau. Địa hình chủ yếu là rừng tuyết rậm rạp, hang đá tự nhiên xen kẽ giữa các vách núi thấp, và những dòng suối nhỏ đóng băng nửa năm. Hang đá được chia thành nhiều ngách, mỗi gia đình hổ yêu chiếm một khu vực riêng, với hang lớn nhất dành cho Quản Sự. Tài nguyên chính gồm thịt thú săn, xương thú dùng luyện khí sơ cấp, và da lông có giá trị trên thị trường phàm nhân — tuy nhiên phần lớn phải cống nạp cho Huyết Hổ Vương, chỉ giữ lại đủ để tồn tại. Vùng rừng tuyết cũng có một số loại thảo dược chịu lạnh, nhưng Hạ Chúng không có kiến thức bào chế để khai thác.

## III. Văn Hóa & Tín Ngưỡng (文化 与 信仰)
Triết lý sống của Hạ Chúng được gói gọn trong câu "Phục tùng hoặc chết" — luật huyết mạch do Huyết Hổ Vương áp đặt từ khi lập tộc. Mỗi khi Huyết Hổ Vương gầm, toàn bộ hổ yêu trong phạm vi lãnh thổ phải quỳ phục, đó không chỉ là quy tắc mà còn là phản xạ bẩm sinh do áp chế huyết mạch. Mỗi mùa, Hạ Chúng phải cống nạp một phần ba thu hoạch; không hổ yêu nào được rời lãnh thổ mà không có lệnh. Dù bị áp bức, hổ yêu trẻ vẫn lén truyền nhau những câu chuyện về thời kỳ Hổ Tộc tự do, khi chưa có Huyết Hổ Vương cai trị. Các hổ yêu già dạy con cháu rằng lòng kiên nhẫn là vũ khí duy nhất của kẻ yếu.

## IV. Cơ Cấu Tổ Chức (组织结构)
Cơ cấu cực kỳ đơn giản, phản ánh bản chất nô dịch của bộ lạc. Quản Sự Hổ Nha Tam đứng đầu, phụ trách truyền đạt mệnh lệnh từ Huyết Hổ Vương và phân công công việc. Dưới Quản Sự là đội thợ săn gồm ba mươi lăm hổ yêu Luyện Khí, chịu trách nhiệm săn bắt, cống nạp và tuần tra. Phần còn lại là hổ yêu cấp thấp chưa đủ tu vi chiến đấu và khoảng năm mươi ấu sinh chưa hóa hình. Không có hội đồng trưởng lão hay hệ thống phân cấp phức tạp — Huyết Hổ Vương cố tình giữ Hạ Chúng ở trạng thái đơn giản để dễ kiểm soát.

## V. Công Pháp & Trận Pháp (功法 与 阵法)
Hạ Chúng tu luyện hoàn toàn bằng bản năng Huyết Mạch Hổ, một phương pháp cấp thấp chỉ tăng cường thể phách và giác quan mà không có hệ thống bài bản. Huyết Hổ Vương cố tình không truyền thụ công pháp cao cấp để ngăn Hạ Chúng trở nên đủ mạnh để phản kháng. Tu vi tối đa mà hổ yêu trong Hạ Chúng có thể đạt được là Trúc Cơ Viên Mãn — muốn đột phá Kim Đan phải được Huyết Hổ Vương cho phép, điều chưa bao giờ xảy ra. Không có trận pháp hay chiến thuật phối hợp, chiến đấu hoàn toàn dựa vào sức mạnh thể xác đơn thuần.

## VI. Đặc Sản Môn Phái (门派特产)
Hạ Chúng không có đặc sản nổi bật theo nghĩa truyền thống. Sản phẩm chính là da lông hổ yêu tự nhiên rụng theo mùa, có tác dụng giữ ấm và kháng hàn khí, được phàm nhân và tu sĩ cấp thấp ưa chuộng. Xương thú săn được cũng có thể dùng làm nguyên liệu luyện khí sơ cấp. Tuy nhiên, phần lớn sản phẩm chất lượng cao đều phải cống nạp, Hạ Chúng chỉ giữ lại đồ thứ phẩm.

## VII. Cơ Sở Hạ Tầng (基础设施)
Hạ tầng thô sơ, gồm hệ thống hang đá tự nhiên được mở rộng bằng móng vuốt. Hang chính của Quản Sự là nơi rộng nhất, có thể chứa toàn bộ Hạ Chúng khi họp. Bãi sân trước hang dùng làm nơi phơi da, xử lý thú săn và tập trung khi có lệnh triệu tập. Một kho nhỏ giấu sâu trong khe đá — do Hổ Nha Tam bí mật lập ra — chứa phần cống nạp bị giấu đi mỗi mùa, tích lũy tài nguyên cho ngày Huyết Hổ Vương suy yếu.

## VIII. Kinh Tế (经济)
Kinh tế Hạ Chúng hoàn toàn mang tính tự cung tự cấp và cống nạp. Thu nhập đến từ săn bắt thú rừng và thu thập tài nguyên thiên nhiên, nhưng một phần ba bắt buộc phải nộp cho Huyết Hổ Vương. Phần còn lại chỉ vừa đủ duy trì sự sống cho cả bộ lạc. Không có hoạt động thương mại chính thức với bên ngoài — mọi giao dịch đều phải thông qua sự cho phép của Huyết Hổ Vương, điều hiếm khi xảy ra. Đây là một trong những yếu tố khiến Hạ Chúng mãi không thể phát triển.

## IX. Lịch Sử Tóm Tắt (简史)
Huyết Hổ Vương chinh phục vùng rừng tuyết ven Bắc Hải bằng sức mạnh tuyệt đối cách đây khoảng tám trăm năm. Những hổ yêu hoang dã trong khu vực bị bắt buộc phục tùng, trở thành Hạ Chúng — đời đời kiếp kiếp làm nô bộc, săn bắt, xây hang, canh gác, và đổi lại chỉ nhận được sự "bảo hộ" khỏi các yêu tộc khác. Nhiều thế hệ hổ yêu đã cố phản kháng nhưng chênh lệch tu vi quá lớn, mỗi lần nổi loạn đều bị dập tắt trong máu. Năm trước, Huyết Hổ Vương giết ba hổ yêu vì cống nạp thiếu — cả Hạ Chúng run sợ, oán hận ngấm ngầm tích tụ đến điểm bùng phát.

## X. Giai Thoại & Bí Mật (轶事 与 秘密)
Hổ Nha Tam bí mật giấu một phần cống nạp mỗi mùa, tích lũy tài nguyên trong hang khe đá sâu, chuẩn bị cho ngày Huyết Hổ Vương suy yếu. Lão hổ yêu này cũng lén liên lạc với Bắc Hải Cự Yêu Hang, tìm kiếm đồng minh tiềm năng cho cuộc phản kháng trong tương lai. Đáng chú ý nhất, trong đám ấu sinh có một con hổ yêu trắng đột biến — huyết mạch thuần khiết đến mức phát sáng dưới ánh trăng. Huyết Hổ Vương chưa biết sự tồn tại của nó; nếu biết sẽ giết ngay vì sợ bị soán ngôi, bởi bạch hổ trong truyền thuyết là dấu hiệu của Hổ Hoàng chân chính.

## XI. Quan Hệ Thế Lực (势力关系)
- **Huyết Hổ Vương:** Chủ nhân tàn bạo, quan hệ áp chế tuyệt đối. Hạ Chúng phục tùng vì không đủ sức phản kháng, nhưng oán hận tích tụ qua nhiều thế hệ.
- **Bắc Hải Cự Yêu Hang:** Liên lạc ngầm do Hổ Nha Tam thiết lập, tìm kiếm đồng minh chống Huyết Hổ Vương. Mối quan hệ còn sơ khai và đầy rủi ro.
- **Băng Lang Tàn Đội:** Cùng là yêu tộc yếu bị áp bức, có sự đồng cảm tự nhiên nhưng chưa liên lạc chính thức do cả hai đều quá yếu và sợ bị phát hiện.
