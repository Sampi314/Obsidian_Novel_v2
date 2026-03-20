---
type: faction
name: Phản Sào Trùng Quần
hantu: 反巢蟲群
faction_type: Bộ Lạc
alignment: 3
race: Trùng Tộc (hỗn hợp côn trùng linh trí)
region: Đông Hoang
founded: 40 năm trước
founder: Xích Giác
emblem: Phan_Sao_Trung_Quan.png
specialty: Ngụy trang bào tử, Trùng Tường phòng thủ, Tiến hóa tự phát
economy:
- Trao đổi mật tiết chữa lành với sinh vật rừng
- Thu thập khoáng thạch và tàn dư linh khí
arcs:
  - arc: 1
    status: Lẩn trốn
    rank: Hạng Năm
    leader: Trùng Trưởng Xích Giác
    population: 200
    territory:
      - Mạng lưới hang nhỏ rìa tây Vạn Trùng Cốc
    assets:
      - name: Bào Tử Ngụy Trang
        type: Bảo Vật
      - name: Mạng lưới hang đất sét đỏ
        type: Công Trình
      - name: Sâu Bạch Kim kỳ dị
        type: Linh Vật
    stats: [80, 25, 10, 120, 60, 15]
    divisions:
      - name: Đàn Phản Sào
        role: Sinh tồn tự do ngoài tầm kiểm soát của Trùng Mẫu
        headcount:
          truong_lao: 5
          chien_binh: 40
          dan_thuong: 155
        members:
          - character: Xích Giác
            position: Trùng Trưởng
            cultivation: Trúc Cơ Hậu Kỳ (tương đương)
          - character: "[Tứ Hộ Vệ Nhất]"
            position: Hộ Vệ
            cultivation: Trúc Cơ Sơ Kỳ (tương đương)
            placeholder: true
          - character: "[Sâu Bạch Kim]"
            position: Thành viên đặc biệt
            cultivation: Không xác định
            placeholder: true
    relationships:
      - faction: Vạn Trùng Cốc
        description: Tử địch, Phản Sào Trùng Quần là nhóm phản loạn thoát khỏi sự kiểm soát tâm trí của Trùng Mẫu, bị truy sát nếu phát hiện.
        diplomacy:
          lien_minh: -100
          tin: -100
          uy_hiep: 90
          thuong_mai: -100
          on_oan: -80
          le_thuoc: 0
      - faction: Trùng Cốc Tàn Binh
        description: Đồng cảnh ngộ — Tàn Binh là những cá thể bị Trùng Mẫu bỏ rơi, Phản Sào là những cá thể chủ động rời đi. Có tiềm năng hợp tác nhưng chưa tiếp xúc.
        diplomacy:
          lien_minh: 10
          tin: 15
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 5
          le_thuoc: 0
      - faction: Độc Trùng Trị Liệu Đường
        description: Trị Liệu Đường đôi khi tìm kiếm côn trùng quý hiếm ở rìa Vạn Trùng Cốc, Xích Giác quan sát từ xa nhưng chưa tiếp cận.
        diplomacy:
          lien_minh: 0
          tin: 5
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 0
---

# PHẢN SÀO TRÙNG QUẦN (反巢蟲群)

## I. Tổng Quan (总览)

Phản Sào Trùng Quần là một bộ lạc Trùng Tộc đặc biệt — quần thể khoảng 200 cá thể côn trùng linh trí đã thoát khỏi sự kiểm soát tâm trí của Trùng Mẫu Vạn Trùng Cốc. Dưới sự dẫn dắt của Trùng Trưởng Xích Giác — bọ cánh cứng đột biến sừng đỏ, một trong số ít Trùng Tộc có linh trí tự phát — đàn phản sào sống lẩn trốn suốt 40 năm tại rìa tây Vạn Trùng Cốc. Chúng chấp nhận yếu hơn để giữ ý thức riêng, coi tự do tư duy là giá trị tối thượng không thể đánh đổi. Dù quy mô nhỏ bé so với hàng tỷ cá thể trong Vạn Trùng Cốc, sự tồn tại của Phản Sào Trùng Quần là bằng chứng rằng Trùng Tộc có khả năng vượt qua bản năng bầy đàn.

## II. Địa Lý & Tài Nguyên (地理与资源)

Phản Sào Trùng Quần cư ngụ tại rìa tây Vạn Trùng Cốc — vùng đất bị Trùng Mẫu bỏ quên vì linh khí quá loãng, không đáng để mở rộng lãnh thổ. Hệ thống hang nhỏ đào trong đất sét đỏ, mỗi hang chỉ đủ cho vài chục cá thể, được ngụy trang bằng mùi bào tử đặc biệt đánh lừa Trùng Binh tuần tra. Tài nguyên chính là khả năng tái tạo nhanh — lợi thế sinh học bẩm sinh của Trùng Tộc — và mật tiết từ cơ thể có tác dụng chữa lành vết thương nhẹ, là món hàng trao đổi duy nhất với sinh vật rừng. Bào tử ngụy trang do Xích Giác phát triển là tài sản sinh tồn quan trọng nhất.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)

Triết lý cốt lõi của Phản Sào Trùng Quần được đúc kết trong câu: "Tự do hơn là bị nuốt." Chúng từ chối sự kiểm soát tâm trí của Trùng Mẫu, chấp nhận yếu hơn những đồng loại trong bầy đàn để giữ ý thức riêng biệt. Quy tắc sinh tồn tối cao là không bao giờ để Trùng Mẫu phát hiện vị trí — không giao tiếp với Trùng Binh, không tiếp cận lãnh thổ cốt lõi, nếu bị phát hiện thì cả đàn lập tức di dời. Phong tục đặc biệt nhất: trùng con mới sinh được nuôi cách ly khỏi tín hiệu tâm trí của Trùng Mẫu trong bảy ngày đầu đời, đảm bảo phát triển ý thức độc lập trước khi hòa nhập quần thể.

## IV. Cơ Cấu Tổ Chức (组织结构)

Cơ cấu tổ chức đơn giản theo kiểu bộ lạc nguyên thủy. Trùng Trưởng Xích Giác — bọ cánh cứng đột biến sừng đỏ, giao tiếp bằng rung động cơ thể — là lãnh đạo tuyệt đối, cá thể mạnh nhất và có linh trí cao nhất trong đàn. Tứ Hộ Vệ gồm bốn cá thể mạnh nhất kế tiếp, tu vi tương đương Trúc Cơ Sơ Kỳ, chuyên bảo vệ đàn khi di chuyển. Phần còn lại là khoảng 200 cá thể đủ loại — kiến, bọ, sâu — tất cả đều có linh trí sơ khai, phân công theo bản năng giữa trinh sát, kiếm ăn và bảo vệ ấu trùng.

## V. Công Pháp & Trận Pháp (功法与阵法)

Phản Sào Trùng Quần không tu luyện công pháp theo nghĩa thông thường. Chúng tiến hóa bằng bản năng — hấp thụ linh khí tự nhiên từ đất đá và thức ăn, dần dần gia tăng sức mạnh thể chất và linh trí. Kỹ năng chiến đấu đáng kể nhất là "Trùng Tường" — khi bị tấn công, hàng trăm cá thể kết hợp thành một bức tường phòng thủ liền mạch, giáp xác cứng chồng lên nhau tạo nên lớp bảo vệ có thể chống được tấn công của trùng cỡ lớn hoặc tu sĩ cấp Luyện Khí. Ngoài ra, bào tử ngụy trang tiết ra mùi hương đánh lừa giác quan của Trùng Binh là chiến thuật sinh tồn hiệu quả nhất.

## VI. Đặc Sản Môn Phái (门派特产)

- **Mật Tiết Chữa Lành:** Chất lỏng do cơ thể Trùng Tộc tiết ra, có tác dụng chữa lành vết thương nhỏ và kích thích tái tạo tế bào. Hiệu quả kém xa linh dược nhưng sản lượng lớn và không cần bào chế.
- **Bào Tử Ngụy Trang:** Bào tử đặc biệt do Xích Giác phát triển, tiết ra mùi hương che giấu sự hiện diện của đàn trước giác quan Trùng Mẫu và Trùng Binh. Nếu thu thập được với số lượng lớn, có thể dùng ngụy trang cả tu sĩ nhân tộc khi xâm nhập Vạn Trùng Cốc.

## VII. Cơ Sở Hạ Tầng (基础设施)

- **Mạng Lưới Hang Đất Sét Đỏ:** Hệ thống hang ngầm phân tán, mỗi hang chỉ đủ cho vài chục cá thể. Thiết kế phân tán đảm bảo nếu một hang bị phát hiện, phần còn lại vẫn an toàn.
- **Đường Hầm Liên Kết:** Các đường hầm nhỏ hẹp nối các hang chính, chỉ đủ cho côn trùng cỡ nhỏ di chuyển, quá nhỏ cho Trùng Binh cỡ lớn xâm nhập.
- **Khu Ấp Nở Cách Ly:** Hang đặc biệt nằm xa nhất khỏi Vạn Trùng Cốc, nơi trùng con mới sinh được nuôi cách ly khỏi tín hiệu Trùng Mẫu trong bảy ngày.
- **Trạm Quan Sát Biên Giới:** Vài điểm quan sát được ngụy trang trên bề mặt, nơi trinh sát theo dõi hoạt động tuần tra của Trùng Binh.

## VIII. Kinh Tế (经济)

Kinh tế của Phản Sào Trùng Quần mang tính tự cung tự cấp hoàn toàn. Chúng kiếm ăn bằng cách thu thập khoáng thạch, thực vật mục nát và xác côn trùng nhỏ trong rừng. Mật tiết chữa lành được dùng trao đổi với một số sinh vật rừng thân thiện để đổi lấy thông tin về đường tuần tra của Trùng Binh. Không có giao thương với nhân tộc hay bất kỳ thế lực tu chân nào — sự tồn tại bí mật là ưu tiên cao hơn mọi lợi ích kinh tế.

## IX. Lịch Sử Tóm Tắt (简史)

Xích Giác vốn là một Trùng Binh trong đội quân của Hắc Hạt Ma Trùng — một trong những Trùng Vương mạnh nhất Vạn Trùng Cốc. Trong một trận chiến lãnh thổ, Xích Giác bị thương nặng đến mức liên kết tâm trí với Trùng Mẫu bị đứt. Lần đầu tiên tỉnh dậy với ý thức riêng, Xích Giác kinh hoàng nhận ra suốt bao năm qua mình chỉ là con rối không tư duy.

Bỏ trốn khỏi bầy đàn, Xích Giác sống lang thang tại rìa tây Vạn Trùng Cốc. Dần dần, những cá thể khác cũng bị đứt liên kết — do bị thương, do đột biến, do mạch tín hiệu quá yếu ở vùng rìa — tìm đến Xích Giác. Qua 40 năm, đàn phản sào phát triển lên khoảng 200 cá thể, nhiều lần suýt bị Trùng Mẫu phát hiện và phải di dời toàn bộ. Sự tồn tại của chúng vẫn là bí mật mà Trùng Mẫu chưa nắm rõ.

## X. Giai Thoại & Bí Mật (轶事与秘密)

- Xích Giác đang nghiên cứu cách cắt đứt liên kết tâm trí hàng loạt — nếu thành công, có thể giải phóng hàng ngàn Trùng Binh khỏi sự kiểm soát của Trùng Mẫu, gây ra nội loạn chưa từng có trong lịch sử Vạn Trùng Cốc. Phương pháp này dựa trên kinh nghiệm đứt liên kết của bản thân nhưng chưa tìm được cách nhân rộng.
- Trong đàn có một con sâu bạch kim kỳ dị — nó không ăn thịt, chỉ ăn khoáng thạch, và cơ thể ngày càng tỏa ra ánh sáng dịu. Xích Giác linh cảm con sâu này đang tiến hóa thành thứ gì đó vượt xa tầm hiểu biết của hắn — có thể là một dạng Trùng Hoàng chưa từng xuất hiện trong lịch sử Trùng Tộc.
- Có dấu hiệu cho thấy Trùng Mẫu bắt đầu nhận ra sự thiếu hụt cá thể ở vùng rìa tây, và đã tăng cường tuần tra. Áp lực sinh tồn đối với Phản Sào Trùng Quần đang gia tăng từng ngày.

## XI. Quan Hệ Thế Lực (势力关系)

| Thế Lực | Quan Hệ | Mô Tả |
|---------|---------|-------|
| Vạn Trùng Cốc | Tử địch | Phản loạn thoát kiểm soát, bị truy sát nếu phát hiện |
| Trùng Cốc Tàn Binh | Đồng cảnh ngộ | Cùng thoát khỏi bầy đàn, tiềm năng hợp tác |
| Độc Trùng Trị Liệu Đường | Quan sát từ xa | Chưa tiếp xúc trực tiếp |
