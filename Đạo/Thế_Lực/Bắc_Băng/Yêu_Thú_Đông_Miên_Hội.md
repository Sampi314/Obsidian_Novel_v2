---
type: faction
name: Yêu Thú Đông Miên Hội
hantu: 妖兽冬眠会
faction_type: Hội
alignment: -1
race: Yêu Tộc (tạp loại)
region: Bắc Băng
founded: Năm Khởi Nguyên 99.780
founder: Hùng Đông
emblem: Gau_Ngu_Dong_Trong_Hang.png
specialty: Đông miên tập thể, Sinh tồn yêu tộc yếu, Chia sẻ hơi ấm hang động
economy:
- Thu thập nấm hang động và địa y bán cho dược phường
- Đổi da thú lột mùa xuân lấy lương thực
- Khai thác nước ngầm ấm chưng cất thành dược dịch thô
arcs:
  - arc: 1
    status: Vừa tỉnh dậy sau mùa đông bất thường
    rank: Không Xếp Hạng
    leader: Hội Trưởng "Lão Gấu" Hùng Đông
    population: 38
    territory:
      - Hệ thống hang động địa nhiệt trên tundra Bắc Băng
      - Khu rừng thưa quanh cửa hang (vùng kiếm ăn mùa hè)
    assets:
      - name: Hang Địa Nhiệt Chính
        type: Tài Nguyên
      - name: Mạch Nước Ngầm Ấm
        type: Tài Nguyên
      - name: Nhánh Hang Cấm (Phong ấn cổ đại)
        type: Bí Cảnh
    stats: [10, 15, 5, 38, 30, 5]
    divisions:
      - name: Ban Canh Gác
        role: Bảo vệ cửa hang trong suốt mùa đông miên, tuần tra khu vực xung quanh
        headcount:
          hoi_truong: 1
          pho_hoi_truong: 0
          thanh_vien: 32
          tong_quan: 5
        members:
          - character: Hùng Đông
            position: Hội Trưởng
            cultivation: Trúc Cơ Sơ Kỳ
          - character: "[Thỏ Yêu Canh Trưởng]"
            position: Trưởng Ban Canh Gác
            cultivation: Luyện Khí Đỉnh Phong
            placeholder: true
          - character: "[Rắn Yêu Trưởng Lão]"
            position: Cố Vấn
            cultivation: Luyện Khí Trung Kỳ
            placeholder: true
    relationships:
      - faction: Băng Lang Bộ Lạc
        description: Sợ hãi và né tránh, luôn tránh xa lãnh thổ săn bắn của sói yêu.
        diplomacy:
          lien_minh: -80
          tin: -70
          uy_hiep: -90
          thuong_mai: -100
          on_oan: -40
          le_thuoc: 0
      - faction: Bạch Hồ Ẩn Tộc
        description: Có vài yêu tộc nhỏ từng nhờ cậy nương náu, giữ thái độ thận trọng nhưng không thù địch.
        diplomacy:
          lien_minh: 5
          tin: 10
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 0
      - faction: Đại Bàng Tuyết Đàn
        description: Đại bàng tuyết thỉnh thoảng bắt yêu thú nhỏ quanh cửa hang làm mồi, Hội rất e dè.
        diplomacy:
          lien_minh: -30
          tin: -20
          uy_hiep: -60
          thuong_mai: -100
          on_oan: -20
          le_thuoc: 0
---

# YÊU THÚ ĐÔNG MIÊN HỘI (妖兽冬眠会)

## I. Tổng Quan (总览)
Yêu Thú Đông Miên Hội là một tập hợp nhỏ gồm các yêu tộc yếu ớt, không thuộc bất kỳ thế lực yêu tộc lớn nào, cùng nhau trú đông trong hệ thống hang động có mạch địa nhiệt trên tundra Bắc Băng. Đứng đầu là "Lão Gấu" Hùng Đông, một gấu yêu hiền lành tu vi chỉ đạt Trúc Cơ Sơ Kỳ nhưng có bản năng tìm hang và bảo vệ đồng loại bẩm sinh. Hội không có tham vọng tranh đoạt, mục tiêu duy nhất là giúp các thành viên sống sót qua mùa đông khắc nghiệt của Bắc Băng — nơi mà những yêu thú đơn lẻ tu vi thấp gần như chắc chắn sẽ chết cóng hoặc trở thành con mồi cho kẻ mạnh.

## II. Địa Lý & Tài Nguyên (地理 与 资源)
Trụ sở của Hội nằm sâu trong một hệ thống hang động tự nhiên trên vùng tundra hoang vu, cách xa lãnh thổ của các yêu tộc lớn như Băng Lang Bộ Lạc hay Bắc Hải Cự Yêu Hang. Điều đặc biệt nhất của hang là mạch địa nhiệt chạy ngầm bên dưới, tỏa ra hơi ấm vừa đủ để giữ cho nhiệt độ bên trong luôn trên mức đóng băng ngay cả giữa mùa đông khốc liệt nhất. Ngoài ra, hang còn sở hữu nguồn nước ngầm ấm tự nhiên, các vách đá phủ đầy nấm hang động giàu linh khí cấp thấp và những mảng địa y có thể làm thức ăn dự trữ. Xung quanh cửa hang là khu rừng thưa — nơi các thành viên kiếm ăn và tích trữ lương thực suốt mùa hè trước khi bước vào mùa đông miên.

## III. Văn Hóa & Tín Ngưỡng (文化 与 信仰)
Triết lý cốt lõi của Hội được Hùng Đông đúc kết trong một câu giản dị: "Ngủ qua mùa đông, tỉnh dậy sống tiếp." Đây không phải lời cao siêu của bậc đắc đạo, mà là sự thật trần trụi của những yêu thú yếu ớt không đủ sức chống chọi thiên nhiên. Quy tắc bất di bất dịch duy nhất: không đánh nhau trong hang, bất kể loài nào, bất kể thù oán cũ. Trong hang, mọi yêu thú đều bình đẳng — con gấu khổng lồ nằm cạnh con nhím bé nhỏ, chia sẻ hơi ấm và thức ăn dự trữ. Trước khi bước vào giấc đông miên tập thể mỗi năm, cả Hội quây quần ăn bữa cuối cùng, kể chuyện mùa hè vừa qua và chúc nhau tỉnh dậy an toàn — một nghi lễ mộc mạc nhưng mang ý nghĩa sâu sắc, bởi không ai dám chắc rằng tất cả sẽ sống sót.

## IV. Cơ Cấu Tổ Chức (组织结构)
Cơ cấu của Hội hết sức đơn giản, phản ánh bản chất một nhóm sinh tồn hơn là một thế lực thực thụ. Hùng Đông là Hội Trưởng, chịu trách nhiệm chọn hang, phân chia vị trí ngủ đông và giải quyết mâu thuẫn giữa các loài. Dưới hắn có Ban Canh Gác gồm 5 yêu thú khỏe nhất (tương đối) thay phiên canh cửa hang trong suốt mùa đông, đảm bảo không có kẻ thù hay yêu thú hoang xâm nhập khi cả Hội đang ngủ. Khoảng 30 thành viên còn lại là yêu tộc tạp loại — gấu yêu, thỏ yêu, rắn yêu, nhím yêu, chồn yêu — đa số chỉ ở mức Luyện Khí Sơ đến Trung Kỳ, thậm chí có vài con chưa khai mở linh trí hoàn toàn.

## V. Công Pháp & Trận Pháp (功法 与 阵法)
Hội không có công pháp thống nhất — mỗi loài yêu thú tu theo bản năng huyết mạch riêng, đa số chỉ dựa vào việc hấp thụ linh khí tự nhiên chậm rãi qua năm tháng. Điểm sáng duy nhất là bài "Đông Miên Tức" do Hùng Đông tự mày mò lĩnh ngộ, giúp giảm tiêu hao linh lực và khí huyết khi ngủ đông xuống mức tối thiểu, kéo dài thời gian có thể đông miên mà không cần ăn uống. Bài pháp này tuy thô sơ nhưng thực tế vô cùng, đã cứu mạng không ít yêu thú yếu qua những mùa đông kéo dài bất thường. Về trận pháp, Hội hoàn toàn không có — hang động tự nhiên với lối vào hẹp chính là "phòng thủ" duy nhất mà họ sở hữu.

## VI. Đặc Sản Môn Phái (门派特产)
- **Nấm Địa Nhiệt Hang Động:** Loại nấm chỉ mọc trong môi trường ẩm ấm của hang, có tác dụng bổ khí huyết nhẹ. Không quý giá đối với tu sĩ nhưng là nguồn dinh dưỡng tuyệt vời cho yêu thú cấp thấp và phàm nhân.
- **Dược Dịch Nước Ngầm Thô:** Nước ngầm ấm được chưng cất tự nhiên qua các lớp đá khoáng, chứa vi lượng linh khí. Hùng Đông thỉnh thoảng đổi vài bình cho thợ săn dược liệu đi ngang để lấy thức ăn khô.
- **Lông Tơ Đông Miên:** Lông tơ rụng tự nhiên từ các yêu thú trong mùa đông miên, mềm và ấm bất thường, được một số thợ dệt ở rìa Bắc Băng thu mua với giá rẻ.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Hang Chính (Đại Sảnh Đông Miên):** Khoang hang rộng nhất, nơi tất cả thành viên quây quần ngủ đông. Nền hang được phủ một lớp rêu dày giữ nhiệt, trần hang đủ cao cho Hùng Đông đứng thẳng.
- **Kho Dự Trữ:** Một nhánh hang nhỏ được dùng làm nơi chứa thức ăn khô, quả dại và nấm phơi cho mùa đông. Hùng Đông chỉ định hai thỏ yêu quản lý vì chúng cẩn thận nhất.
- **Nhánh Hang Cấm:** Lối đi sâu vào lòng đất mà Hùng Đông tuyệt đối cấm mọi thành viên bước vào. Nơi đây toát ra hơi ấm mạnh hơn hẳn phần còn lại, và đôi khi vọng lên tiếng thở đều đặn kỳ lạ — không thuộc về bất kỳ loài yêu thú nào quen biết.

## VIII. Kinh Tế (经济)
Kinh tế của Hội gần như không tồn tại theo nghĩa truyền thống. Hầu hết thành viên tự kiếm ăn suốt mùa hè, tích trữ riêng cho mùa đông. Hùng Đông duy trì một "quỹ chung" bằng cách thu thập nấm hang động và nước ngầm ấm, thỉnh thoảng đổi cho thợ săn hay tán tu đi ngang để lấy muối, thảo dược chữa thương cơ bản hoặc da thú lót ổ. Đây là một nền kinh tế vật đổi vật ở mức sơ khai nhất, nhưng cũng chính sự nghèo nàn này khiến Hội không thu hút sự chú ý hay dòm ngó của bất kỳ thế lực nào.

## IX. Lịch Sử Tóm Tắt (简史)
Hai mươi năm trước, Bắc Băng trải qua một đợt Hàn Triều bất thường kéo dài suốt ba tháng, giết chết hàng loạt yêu thú yếu ớt không có nơi trú ẩn. Hùng Đông, khi đó chỉ là một gấu yêu vô danh mới khai linh trí, tình cờ tìm thấy hệ thống hang động có mạch địa nhiệt ấm áp. Hắn mời những yêu tộc yếu lân cận cùng vào hang trú đông, ban đầu nhiều loài nghi ngờ — gấu yêu và thỏ yêu vốn là quan hệ săn-mồi, rắn yêu thì thích ở một mình. Nhưng sau mùa đông đầu tiên không ai chết, tin tưởng dần hình thành. Mỗi năm Hội có thêm vài thành viên mới, cũng có vài thành viên cũ rời đi khi đủ mạnh. Mùa đông vừa qua là khó khăn nhất trong hai thập niên — nhiệt lượng trong hang bất thường tăng giảm thất thường, khiến nhiều thành viên không ngủ sâu được và tiêu hao linh lực nặng nề. Hùng Đông nghi ngờ có điều gì đó đang thay đổi sâu dưới lòng đất.

## X. Giai Thoại & Bí Mật (轶事 与 秘密)
Mạch địa nhiệt trong hang không phải hiện tượng tự nhiên đơn thuần — thực chất đó là tàn dư nhiệt lượng rò rỉ từ một phong ấn cổ đại bị vùi sâu dưới lòng đất, nhưng không ai trong Hội đủ kiến thức hay tu vi để nhận biết điều này. Nhiệt lượng bất thường tăng giảm gần đây chính là dấu hiệu phong ấn đang dần suy yếu. Mỗi năm sau khi tỉnh dậy từ giấc đông miên, có vài thành viên biến mất không dấu vết — Hùng Đông đã âm thầm tìm kiếm nhiều lần nhưng không có manh mối, chỉ phát hiện những vết cào lạ trên vách đá gần nhánh hang cấm. Sâu trong nhánh hang mà Hùng Đông cấm mọi người vào, hắn từng nghe thấy tiếng thở đều đặn hùng vĩ — không phải của yêu thú, mà giống như một thực thể cổ đại đang chìm trong giấc ngủ ngàn năm, và mỗi nhịp thở khiến mặt đất rung nhẹ.

## XI. Quan Hệ Thế Lực (势力关系)
```mermaid
graph LR
    YTĐMH[Yêu Thú Đông Miên Hội] -- Sợ hãi / Né tránh -- BLBL[Băng Lang Bộ Lạc]
    YTĐMH -- Thận trọng -- BHẤT[Bạch Hồ Ẩn Tộc]
    YTĐMH -- E dè -- ĐBTĐ[Đại Bàng Tuyết Đàn]
    YTĐMH -- Không liên hệ -- NT[Nhân Tộc]
```
