---
type: faction
name: Cổ Yêu Thức Tỉnh Hội
hantu: 古妖觉醒会
faction_type: Hội
alignment: -1
race: Yêu Tộc (Cổ Yêu)
region: Đông Hoang
founded: 80 năm trước
founder: Cổ Giác
emblem: Mat_Than_Lan_Co_Dai.png
specialty: Pháp thuật Thượng Cổ tàn dư, Ký ức cổ đại, Thích nghi thời đại mới
economy:
- Bán mảnh vụn pháp khí cổ đại thu lượm từ phế tích
- Trao đổi kiến thức Thượng Cổ với các học giả
- Tự cung tự cấp bằng săn bắn trong rừng sâu
arcs:
  - arc: 1
    status: Ẩn mình hoạt động
    rank: Không Xếp Hạng
    leader: Hội Trưởng Cổ Giác
    population: 12
    territory:
      - Phế tích đền thờ cổ (Rừng sâu Đông Hoang)
    assets:
      - name: Phế Tích Đền Thờ Cổ Đại
        type: Công Trình
      - name: Đá Phong Ấn Tàn Dư
        type: Tài Nguyên
      - name: Mảnh Vụn Ký Ức Thượng Cổ
        type: Tài Nguyên
    stats: [40, 20, 10, 12, 30, 5]
    divisions:
      - name: Hội Đồng Cổ Yêu
        role: Hỗ trợ cổ yêu mới tỉnh thích nghi, nghiên cứu phục hồi ký ức và tu vi
        headcount:
          hoi_truong: 1
          pho_hoi_truong: 0
          thanh_vien: 8
          tong_quan: 1
        members:
          - character: Cổ Giác
            position: Hội Trưởng
            cultivation: Kim Đan Trung Kỳ
          - character: "[Liên Lạc Viên Nhất]"
            position: Liên Lạc Viên
            cultivation: Trúc Cơ Sơ Kỳ
            placeholder: true
          - character: "[Liên Lạc Viên Nhị]"
            position: Liên Lạc Viên
            cultivation: Luyện Khí Đỉnh Phong
            placeholder: true
    relationships:
      - faction: Thiên Yêu Đình
        description: Mối đe dọa lớn nhất. Nếu Thiên Yêu Đình biết có cổ yêu tỉnh dậy, chắc chắn sẽ can thiệp — hoặc chiêu mộ hoặc tiêu diệt.
        diplomacy:
          lien_minh: -20
          tin: -80
          uy_hiep: 70
          thuong_mai: 0
          on_oan: -30
          le_thuoc: 0
      - faction: Hoang Dã Yêu Liên
        description: Tiềm năng đồng minh, Hoang Dã Yêu Liên chứa chấp yêu tộc ngoài vòng kiểm soát của Thiên Yêu Đình. Cổ Giác đang cân nhắc liên lạc.
        diplomacy:
          lien_minh: 10
          tin: 20
          uy_hiep: 0
          thuong_mai: 10
          on_oan: 0
          le_thuoc: 0
      - faction: Vạn Pháp Thư Quán
        description: Quan hệ bí mật, một học giả của Thư Quán đã phát hiện sự tồn tại của Hội nhưng giữ im lặng để đổi lấy kiến thức Thượng Cổ.
        diplomacy:
          lien_minh: 10
          tin: 30
          uy_hiep: 0
          thuong_mai: 40
          on_oan: 0
          le_thuoc: 0
---

# CỔ YÊU THỨC TỈNH HỘI (古妖觉醒会)

## I. Tổng Quan (总览)
Cổ Yêu Thức Tỉnh Hội là một tổ chức bí mật cực nhỏ, quy tụ những cổ yêu vừa tỉnh dậy từ phong ấn Thượng Cổ trong rừng sâu Đông Hoang. Chỉ mười hai thành viên — tám cổ yêu và hai liên lạc viên yêu tộc hiện đại — ẩn mình trong phế tích một đền thờ cổ đại bị cây cối bao phủ hoàn toàn. Đây không phải thế lực chiến đấu hay thương mại, mà là nhóm hỗ trợ sinh tồn cho những sinh vật lạc thời, đang cố tìm hiểu một thế giới hoàn toàn khác xa với ký ức mơ hồ còn sót lại trong tâm trí họ.

## II. Địa Lý & Tài Nguyên (地理与资源)
Trụ sở của Hội là phế tích một đền thờ cổ đại nằm sâu trong rừng Đông Hoang, cách xa mọi tuyến đường thương mại và khu dân cư. Kiến trúc bằng đá đen cổ đại đã nửa sụp đổ, rêu xanh và dây leo bao phủ mọi bề mặt, khiến từ bên ngoài trông không khác gì một gò đá tự nhiên. Bên trong còn vài phòng nguyên vẹn nhờ trận pháp phong ấn tàn dư tự duy trì qua hàng vạn năm. Tài nguyên chủ yếu là những mảnh vụn ký ức Thượng Cổ trong tâm trí các cổ yêu, vài đá phong ấn còn sót lại mang năng lượng cổ đại, và các mảnh pháp khí gãy vỡ nằm rải rác trong đền. Linh khí tại phế tích loãng nhưng thuần khiết, mang hương vị cổ xưa khác hẳn linh khí hiện đại.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
"Chúng ta là tàn dư của thời đại đã mất" — câu nói này vừa là sự tự nhận thức vừa là nỗi đau chung của mọi thành viên. Các cổ yêu mang theo ký ức mơ hồ về một thế giới khác hẳn: linh khí dồi dào hơn, chủng tộc hùng mạnh hơn, nhưng cũng tàn khốc hơn. Quy tắc quan trọng nhất của Hội là tuyệt đối không tiết lộ thân phận cổ yêu cho bất kỳ ngoại nhân nào — trong thế giới hiện tại, cổ yêu là mục tiêu săn đuổi của quá nhiều thế lực. Mỗi cổ yêu mới tỉnh sẽ được dẫn đến phế tích, ngồi thiền trước bàn thờ cổ để ổn định ký ức bị phong ấn xáo trộn. Hội không thờ phụng thần linh nào — họ chỉ thờ ký ức về một thời đại đã chết.

## IV. Cơ Cấu Tổ Chức (组织结构)
Cổ Giác là hội trưởng kiêm lãnh đạo tinh thần — một cổ yêu thằn lằn tỉnh dậy từ phong ấn hai mươi năm trước, thân dài ba trượng khi hiện nguyên hình nhưng thường thu nhỏ thành hình người mảnh khảnh. Tu vi từ Nguyên Anh suy giảm xuống Kim Đan do phong ấn quá lâu làm tiêu hao linh lực tích tụ. Tám cổ yêu khác mỗi người từ một phong ấn khác nhau, đều tu vi suy giảm nghiêm trọng: có kẻ từ Kim Đan xuống Trúc Cơ, có kẻ gần như mất hết tu vi. Hai liên lạc viên là yêu tộc hiện đại tình cờ phát hiện Hội, được Cổ Giác thuyết phục ở lại giúp đỡ, đóng vai trò cầu nối giữa các cổ yêu lạc thời với thế giới mới.

## V. Công Pháp & Trận Pháp (功法与阵法)
- **Công Pháp:** Mỗi cổ yêu mang theo mảnh vụn công pháp Thượng Cổ, nhưng không hoàn chỉnh vì ký ức bị phong ấn xóa nhòa. Cổ Giác nhớ được khoảng ba phần mười bộ "Vạn Yêu Biến Hóa Kinh" — đủ để duy trì nhân hình và vài chiêu thức cơ bản. Những cổ yêu khác mỗi người nhớ được vài đoạn công pháp khác nhau, Hội đang cố ghép các mảnh lại nhưng tiến triển chậm chạp. Thêm vào đó, linh khí hiện đại loãng hơn Thượng Cổ rất nhiều, khiến các công pháp cổ đại vốn cần linh khí đậm đặc trở nên kém hiệu quả.
- **Trận Pháp:** Trận phong ấn tàn dư bao quanh phế tích đền thờ, tuy không còn đủ sức phong ấn bất kỳ ai, nhưng vô tình tạo ra lớp bảo vệ tự nhiên: người ngoài đi vào khu vực sẽ bị mất phương hướng, đi lòng vòng mà không tìm ra đền thờ.

## VI. Đặc Sản Môn Phái (门派特产)
- **Mảnh Vụn Công Pháp Thượng Cổ:** Dù không hoàn chỉnh, những đoạn công pháp cổ yêu ghi nhớ được vẫn có giá trị nghiên cứu vô giá. Mỗi mảnh vụn chứa nguyên lý tu luyện đã thất truyền hàng vạn năm.
- **Đá Phong Ấn Tàn Dư:** Những viên đá còn mang năng lượng phong ấn cổ đại, có thể dùng làm nguồn năng lượng nhỏ hoặc nguyên liệu nghiên cứu trận pháp thượng cổ.
- **Ký Ức Truyền Thừa:** Cổ Giác có khả năng truyền hình ảnh ký ức Thượng Cổ cho người khác thông qua tiếp xúc thần thức — đây là "hàng hóa" quý giá nhất mà Hội sở hữu, dù họ cực kỳ cẩn thận trong việc chia sẻ.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Phế Tích Đền Thờ Cổ Đại:** Khu kiến trúc đá đen rộng khoảng nửa mẫu đất, phần lớn sụp đổ. Năm phòng còn nguyên vẹn được dùng làm nơi ở, phòng thiền định, và kho chứa. Tường đá khắc những hoa văn cổ đại mà ngay cả Cổ Giác cũng không hoàn toàn giải mã được.
- **Bàn Thờ Trung Tâm:** Bàn thờ đá nguyên khối ở chính điện, nơi các cổ yêu mới tỉnh ngồi thiền ổn định ký ức. Bàn thờ phát ra rung động nhẹ giúp xoa dịu thần thức bị xáo trộn.
- **Vòng Tròn Phong Ấn Ngoại Vi:** Ranh giới trận phong ấn tàn dư, tạo thành kết giới mê hoặc tự nhiên quanh đền thờ trong bán kính khoảng một dặm.

## VIII. Kinh Tế (经济)
Hội gần như không có hoạt động kinh tế. Thức ăn đến từ săn bắn và hái lượm trong rừng, nước uống từ suối gần phế tích. Đôi khi, hai liên lạc viên mang một vài mảnh pháp khí cổ đại gãy vỡ ra ngoài đổi lấy vật dụng cần thiết — phải cực kỳ cẩn thận để không để lộ nguồn gốc Thượng Cổ của vật phẩm. Gần đây, thỏa thuận bí mật với một học giả Vạn Pháp Thư Quán mang lại nguồn cung ổn định hơn: Hội chia sẻ kiến thức Thượng Cổ, học giả cung cấp lương thực và tin tức thế giới bên ngoài.

## IX. Lịch Sử Tóm Tắt (简史)
Cổ yêu bị phong ấn từ Thượng Cổ vì nhiều lý do khác nhau — kẻ bại trận trong chiến tranh, kẻ bị trừng phạt bởi cường giả, kẻ tự nguyện ngủ đông để chờ thời đại tốt hơn. Qua hàng vạn năm, phần lớn phong ấn vẫn vững chắc, nhưng gần đây một số phong ấn bắt đầu suy yếu theo thời gian hoặc do biến động linh mạch. Cổ Giác là cổ yêu đầu tiên tỉnh dậy cách đây tám mươi năm, choáng ngợp và hoang mang trước thế giới hoàn toàn khác biệt — linh khí loãng, chủng tộc quen thuộc đã biến mất hoặc thay đổi hoàn toàn, thứ bậc quyền lực đảo lộn. Sau hai mươi năm lang thang cô độc, hắn gặp cổ yêu thứ hai tỉnh dậy và nhận ra mình không đơn lẻ. Từ đó lập Hội tại phế tích đền thờ — nơi mà hắn nghi ngờ chính là đền thờ của chủng tộc mình thời Thượng Cổ — để đón và giúp đỡ những cổ yêu tỉnh sau.

## X. Giai Thoại & Bí Mật (轶事与秘密)
Cổ Giác nhớ mơ hồ rằng trước khi bị phong ấn, hắn đã chứng kiến một sự kiện kinh thiên — bầu trời nứt vỡ, linh khí cuồn cuộn tràn ra như thác lũ, và một bóng dáng khổng lồ xuất hiện giữa hư không. Nhưng ký ức bị phong ấn xóa nhòa, hắn chỉ còn lại cảm giác khiếp sợ tuyệt đối mỗi khi cố nhớ lại. Hắn tin rằng sự kiện đó có liên quan đến lý do cổ yêu bị phong ấn hàng loạt.

Nếu Thiên Yêu Đình biết có cổ yêu tỉnh dậy, hậu quả khó lường — Đình có thể muốn chiêu mộ để tăng cường lực lượng, hoặc tiêu diệt vì sợ cổ yêu mang theo sức mạnh vượt tầm kiểm soát. Hội phải giữ bí mật tuyệt đối, và đây là áp lực lớn nhất đè lên vai Cổ Giác mỗi ngày.

Trong tám cổ yêu, có một người nhớ được vị trí của một kho báu Thượng Cổ bị chôn vùi — nhưng kho báu nằm sâu trong lãnh thổ của Thiên Yêu Đình, khiến việc tiếp cận là bất khả thi với sức mạnh hiện tại.

## XI. Quan Hệ Thế Lực (势力关系)
- **Thiên Yêu Đình:** Mối đe dọa sống còn. Hội phải giấu sự tồn tại của mình trước Đình bằng mọi giá, vì Đình chắc chắn sẽ can thiệp nếu biết có cổ yêu Thượng Cổ tỉnh dậy.
- **Hoang Dã Yêu Liên:** Đồng minh tiềm năng, Yêu Liên chứa chấp yêu tộc ngoài vòng kiểm soát. Cổ Giác đang cân nhắc tiếp cận nhưng chưa dám mạo hiểm.
- **Vạn Pháp Thư Quán:** Mối quan hệ bí mật duy nhất với bên ngoài. Một học giả Thư Quán phát hiện Hội nhưng giữ im lặng để đổi lấy cơ hội nghiên cứu ký ức Thượng Cổ — thỏa thuận mong manh dựa trên lòng tham tri thức.
