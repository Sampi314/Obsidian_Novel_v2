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

> *"Hổ không quên — dù bị xích ngàn năm, vuốt vẫn sắc, và cơn giận vẫn nóng."*
> — Hổ Nha Tam, thì thầm bên bếp lửa trong đêm tuyết, khi chỉ có ấu sinh nghe thấy

## I. Tổng Quan (总览)
Huyết Hổ Hạ Chúng là tập hợp những hổ yêu cấp thấp sống dưới sự cai trị tàn bạo của Huyết Hổ Vương tại vùng ven biển Bắc Hải. Với khoảng một trăm hai mươi thành viên gồm hổ yêu đã hóa hình và ấu sinh chưa khai linh, Hạ Chúng tồn tại như một bộ lạc nô dịch — săn bắt, cống nạp, canh gác, và đổi lại chỉ nhận được sự "bảo hộ" khỏi các yêu tộc khác. Quản Sự Hổ Nha Tam, một hổ yêu già tu vi Trúc Cơ Viên Mãn, giữ vai trò truyền đạt mệnh lệnh của Huyết Hổ Vương, nhưng trong lòng ấp ủ những toan tính riêng mà lão giấu kín suốt hai trăm năm. Đây là thế lực Hạng Năm, yếu ớt về mọi mặt nhưng chứa đựng những mầm mống phản kháng đáng chú ý, và một bí mật huyết thống có thể lật đổ trật tự quyền lực trong vùng.

## II. Địa Lý & Tài Nguyên (地理 与 资源)
Hạ Chúng cư ngụ tại vùng đá ven rừng tuyết, nơi biên giới giữa Bắc Hải và ngoại vi dãy Núi Độc Long giao nhau. Địa hình chủ yếu là rừng tuyết rậm rạp, hang đá tự nhiên xen kẽ giữa các vách núi thấp, và những dòng suối nhỏ đóng băng nửa năm — vào mùa đông, cả vùng phủ trắng tuyết dày đến đầu gối, gió bắc thổi buốt xương, chỉ có hổ yêu chịu lạnh bẩm sinh mới sống nổi. Hang đá chính nằm dưới chân Bạch Nha Nham — vách đá trắng nhô lên giữa rừng tuyết như chiếc nanh khổng lồ, là địa điểm dễ nhận biết nhất của Hạ Chúng. Hang được chia thành nhiều ngách, mỗi gia đình hổ yêu chiếm một khu vực riêng, với hang lớn nhất dành cho Quản Sự. Tài nguyên chính gồm thịt thú săn, xương thú dùng luyện khí sơ cấp, và da lông có giá trị trên thị trường phàm nhân — tuy nhiên phần lớn phải cống nạp cho Huyết Hổ Vương, chỉ giữ lại đủ để tồn tại. Vùng rừng tuyết cũng có một số loại thảo dược chịu lạnh quý hiếm, đặc biệt là Tuyết Nhung Thảo mọc dưới gốc tùng già — nhưng Hạ Chúng không có kiến thức bào chế để khai thác, để mặc cho thảo dược rụng rữa trong tuyết.

## III. Văn Hóa & Tín Ngưỡng (文化 与 信仰)
Triết lý sống của Hạ Chúng được gói gọn trong câu "Phục tùng hoặc chết" — luật huyết mạch do Huyết Hổ Vương áp đặt từ khi lập tộc. Mỗi khi Huyết Hổ Vương gầm, toàn bộ hổ yêu trong phạm vi lãnh thổ phải quỳ phục, đó không chỉ là quy tắc mà còn là phản xạ bẩm sinh do áp chế huyết mạch — ngay cả Hổ Nha Tam cũng không cưỡng lại được bản năng quỳ gối khi tiếng gầm vang lên, dù trong lòng sục sôi căm phẫn. Mỗi mùa, Hạ Chúng phải cống nạp một phần ba thu hoạch; không hổ yêu nào được rời lãnh thổ mà không có lệnh. Dù bị áp bức, hổ yêu trẻ vẫn lén truyền nhau những câu chuyện về thời kỳ Hổ Tộc tự do, khi chưa có Huyết Hổ Vương cai trị — những câu chuyện được kể bên bếp lửa trong đêm tuyết, gọi là "Hỏa Đàm," bằng thứ tiếng rì rầm thấp hơn cả tiếng gió, đề phòng tai mắt của Huyết Hổ Vương. Các hổ yêu già dạy con cháu rằng lòng kiên nhẫn là vũ khí duy nhất của kẻ yếu, và truyền lại bài vè: "Tuyết rơi trắng rừng — hổ nằm đợi; tuyết tan lộ đất — hổ vùng dậy."

## IV. Cơ Cấu Tổ Chức (组织结构)
Cơ cấu cực kỳ đơn giản, phản ánh bản chất nô dịch của bộ lạc. Quản Sự Hổ Nha Tam đứng đầu, phụ trách truyền đạt mệnh lệnh từ Huyết Hổ Vương và phân công công việc — lão mang vẻ ngoài khúm núm và tay chân khi đối diện Huyết Hổ Vương, nhưng khi ở giữa đồng tộc, mắt lão sáng quắc với ánh nhìn của kẻ đang tính toán. Dưới Quản Sự là đội thợ săn gồm ba mươi lăm hổ yêu Luyện Khí, chia thành ba tổ luân phiên — Tổ Nha phụ trách săn bắt, Tổ Vuốt phụ trách tuần tra canh gác, và Tổ Bì phụ trách xử lý da thú và cống nạp. Phần còn lại là hổ yêu cấp thấp chưa đủ tu vi chiến đấu và khoảng năm mươi ấu sinh chưa hóa hình. Không có hội đồng trưởng lão hay hệ thống phân cấp phức tạp — Huyết Hổ Vương cố tình giữ Hạ Chúng ở trạng thái đơn giản để dễ kiểm soát. Tuy nhiên, Hổ Nha Tam đã bí mật tuyển chọn bảy hổ yêu trẻ đáng tin nhất lập thành "Ám Nha" — nhóm liên lạc ngầm do lão trực tiếp chỉ đạo, chuyên thu thập tin tức về động tĩnh của Huyết Hổ Vương.

## V. Công Pháp & Trận Pháp (功法 与 阵法)
Hạ Chúng tu luyện hoàn toàn bằng bản năng Huyết Mạch Hổ, một phương pháp cấp thấp chỉ tăng cường thể phách và giác quan mà không có hệ thống bài bản — hổ yêu tự mò mẫm cách vận dụng sức mạnh trong cơ thể, không có bài tập chuẩn hay lộ trình tu luyện rõ ràng. Huyết Hổ Vương cố tình không truyền thụ công pháp cao cấp để ngăn Hạ Chúng trở nên đủ mạnh để phản kháng. Tu vi tối đa mà hổ yêu trong Hạ Chúng có thể đạt được là Trúc Cơ Viên Mãn — muốn đột phá Kim Đan phải được Huyết Hổ Vương cho phép, điều chưa bao giờ xảy ra. Không có trận pháp hay chiến thuật phối hợp, chiến đấu hoàn toàn dựa vào sức mạnh thể xác đơn thuần. Tuy nhiên, bản năng săn mồi của hổ yêu không thể coi thường — trong rừng tuyết quen thuộc, một đội ba mươi lăm hổ yêu Luyện Khí phối hợp phục kích có thể hạ gục linh thú Trúc Cơ, và đó là khả năng chiến đấu duy nhất mà Hạ Chúng sở hữu. Hổ Nha Tam lặng lẽ dạy nhóm Ám Nha cách phối hợp bầy đàn tinh vi hơn — không phải để săn thú, mà để chuẩn bị cho một mục tiêu khác.

## VI. Đặc Sản Môn Phái (门派特产)
Hạ Chúng không có đặc sản nổi bật theo nghĩa truyền thống, nhưng vùng rừng tuyết cung cấp một số sản phẩm có giá trị nhất định. **Hổ Nhung Bì** — da lông hổ yêu tự nhiên rụng theo mùa — có tác dụng giữ ấm và kháng hàn khí vượt trội, được phàm nhân và tu sĩ cấp thấp ưa chuộng; một tấm Hổ Nhung Bì thượng phẩm bán được mười lăm linh thạch hạ phẩm tại chợ phàm nhân, nhưng hàng tốt nhất đều phải cống nạp. **Xương Linh Thú Rừng Tuyết** — xương thú săn được từ những loài linh thú chịu lạnh đặc hữu — dùng làm nguyên liệu luyện khí sơ cấp, đặc biệt là xương Băng Nai chứa hàn khí tự nhiên, hữu ích cho tu sĩ thủy hệ và băng hệ. **Tuyết Nhung Thảo Khô** — dù Hạ Chúng không biết bào chế, Hổ Nha Tam gần đây bắt đầu lén thu thập Tuyết Nhung Thảo phơi khô cất giấu trong kho bí mật, vì nghe nói loại thảo dược này có thể bán giá cao cho dược sư bên ngoài — thêm một nguồn tài nguyên cho ngày khởi sự.

## VII. Cơ Sở Hạ Tầng (基础设施)
Hạ tầng thô sơ, gồm hệ thống hang đá tự nhiên được mở rộng bằng móng vuốt qua nhiều thế hệ. **Bạch Nha Đại Sảnh** — hang chính dưới chân Bạch Nha Nham — là nơi rộng nhất, trần hang cao ba trượng, có thể chứa toàn bộ Hạ Chúng khi họp hoặc khi Huyết Hổ Vương triệu tập. Nền hang lát đá phẳng mài nhẵn bởi hàng trăm năm hổ yêu ngồi xổm, tường khắc dấu vuốt đếm ngày — mỗi hổ yêu khắc một vạch mỗi mùa cống nạp, vạch cũ nhất đã mờ không đọc được. **Bãi Phơi Da** — sân trước hang dùng để phơi da thú, xử lý thú săn và tập trung khi có lệnh triệu tập, mặt đất đông cứng quanh năm trừ hai tháng hè. **Tuyết Huyệt** — kho lạnh tự nhiên trong khe đá dùng để bảo quản thịt thú qua mùa đông dài. Một kho nhỏ giấu sâu trong khe đá phía đông — do Hổ Nha Tam bí mật lập ra, ngụy trang bằng tuyết và đá vụn, lối vào chỉ vừa một hổ yêu chui qua — chứa phần cống nạp bị giấu đi mỗi mùa, tích lũy tài nguyên cho ngày Huyết Hổ Vương suy yếu.

## VIII. Kinh Tế (经济)
Kinh tế Hạ Chúng hoàn toàn mang tính tự cung tự cấp và cống nạp. Thu nhập đến từ săn bắt thú rừng và thu thập tài nguyên thiên nhiên, nhưng một phần ba bắt buộc phải nộp cho Huyết Hổ Vương — lần nào thiếu cũng có hổ yêu bị phạt, nhẹ thì đánh, nặng thì giết. Phần còn lại chỉ vừa đủ duy trì sự sống cho cả bộ lạc, và mùa đông khắc nghiệt thường xuyên có hổ yêu già và ấu sinh chết đói. Không có hoạt động thương mại chính thức với bên ngoài — mọi giao dịch đều phải thông qua sự cho phép của Huyết Hổ Vương, điều hiếm khi xảy ra. Hổ Nha Tam đã tìm được một kênh buôn bán lén qua Bắc Hải Cự Yêu Hang — đổi da thú lấy linh thạch hạ phẩm, chậm chạp nhưng kiên trì — tổng tích lũy trong kho bí mật hiện là hai trăm linh thạch hạ phẩm và ba mươi cân xương linh thú, đủ để mua một bộ công pháp cấp thấp nếu cần.

## IX. Lịch Sử Tóm Tắt (简史)
Huyết Hổ Vương chinh phục vùng rừng tuyết ven Bắc Hải bằng sức mạnh tuyệt đối cách đây khoảng tám trăm năm — một đêm bão tuyết, hắn hạ xuống giữa bầy hổ hoang, giết tộc trưởng cũ bằng một đòn vuốt xé toạc đầu đến chân, máu nhuộm đỏ tuyết trắng suốt ba dặm. Những hổ yêu hoang dã trong khu vực bị bắt buộc phục tùng, trở thành Hạ Chúng — đời đời kiếp kiếp làm nô bộc, săn bắt, xây hang, canh gác, và đổi lại chỉ nhận được sự "bảo hộ" khỏi các yêu tộc khác. Nhiều thế hệ hổ yêu đã cố phản kháng nhưng chênh lệch tu vi quá lớn, mỗi lần nổi loạn đều bị dập tắt trong máu — lần gần nhất cách đây trăm năm, mười hai hổ yêu dũng cảm nhất tấn công Huyết Hổ Vương khi hắn đang tĩnh tu, cả mười hai bị giết trong chưa đầy mười hơi thở. Năm trước, Huyết Hổ Vương giết ba hổ yêu vì cống nạp thiếu — cả Hạ Chúng run sợ, oán hận ngấm ngầm tích tụ đến điểm bùng phát, nhưng Hổ Nha Tam biết rằng bùng phát bây giờ chỉ là tự sát — lão cần thêm thời gian, thêm đồng minh, và thêm một phép màu.

## X. Giai Thoại & Bí Mật (轶事 与 秘密)
Hổ Nha Tam bí mật giấu một phần cống nạp mỗi mùa, tích lũy tài nguyên trong hang khe đá sâu phía đông, chuẩn bị cho ngày Huyết Hổ Vương suy yếu. Lão hổ yêu này cũng lén liên lạc với Bắc Hải Cự Yêu Hang, tìm kiếm đồng minh tiềm năng cho cuộc phản kháng trong tương lai — mỗi lần liên lạc đều qua một con chim ưng tuyết mà lão thuần hóa từ nhỏ, bay đi đêm về sáng, không để lại dấu vết. Đáng chú ý nhất, trong đám ấu sinh có một con hổ yêu trắng đột biến — huyết mạch thuần khiết đến mức lông phát sáng dưới ánh trăng, mắt trong vắt như pha lê xanh. Huyết Hổ Vương chưa biết sự tồn tại của nó; nếu biết sẽ giết ngay vì sợ bị soán ngôi, bởi bạch hổ trong truyền thuyết là dấu hiệu của Hổ Hoàng chân chính — loài hổ yêu cao quý nhất, sinh ra một lần trong ngàn năm, mang trong mình huyết mạch thượng cổ vượt xa Huyết Hổ Vương. Hổ Nha Tam giấu ấu sinh bạch hổ trong ngách hang sâu nhất, bao quanh bởi ba hổ yêu cái đáng tin nhất làm bảo mẫu. Lão biết rằng con bạch hổ này là hy vọng duy nhất — nhưng cũng là mối nguy chết người nếu bị phát hiện quá sớm.

## XI. Quan Hệ Thế Lực (势力关系)
- **Huyết Hổ Vương:** Chủ nhân tàn bạo, quan hệ áp chế tuyệt đối. Hạ Chúng phục tùng vì không đủ sức phản kháng, nhưng oán hận tích tụ qua nhiều thế hệ đã đến mức chỉ cần một tia lửa là bùng cháy — câu hỏi không phải "có nổi dậy không" mà là "khi nào."
- **Bắc Hải Cự Yêu Hang:** Liên lạc ngầm do Hổ Nha Tam thiết lập qua chim ưng tuyết, tìm kiếm đồng minh chống Huyết Hổ Vương. Mối quan hệ còn sơ khai và đầy rủi ro — Cự Yêu Hang chưa cam kết gì cụ thể, chỉ trao đổi tin tức và hàng hóa, nhưng sự tồn tại của kênh liên lạc này đã là bước tiến lớn so với tám trăm năm cô lập hoàn toàn.
- **Băng Lang Tàn Đội:** Cùng là yêu tộc yếu bị áp bức, có sự đồng cảm tự nhiên nhưng chưa liên lạc chính thức do cả hai đều quá yếu và sợ bị phát hiện. Hổ Nha Tam đang tìm cách thiết lập liên lạc qua trung gian Bắc Hải Cự Yêu Hang, tin rằng liên minh giữa hai bộ lạc nô lệ sẽ mạnh hơn hai bên riêng lẻ — dù "mạnh hơn" ở đây vẫn yếu hơn Huyết Hổ Vương rất nhiều.