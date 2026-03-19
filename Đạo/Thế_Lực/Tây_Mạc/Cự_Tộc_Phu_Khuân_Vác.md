---
type: faction
name: Cự Tộc Phu Khuân Vác
hantu: 巨族搬运工
faction_type: Hội
alignment: 1
race: Cự Tộc (Cự Nhân nghèo)
region: Tây Mạc
founded: Khoảng 30 năm trước
founder: Sa Lực
emblem: Vai_Cu_Nhan_Khuan_Hang.png
specialty: Sức mạnh thể chất bẩm sinh Cự Tộc, Vận chuyển hàng hóa siêu trọng, Đình công tập thể
economy:
- Tiền công khuân vác cho các thương đoàn
- Vận chuyển hàng hóa siêu nặng trên Thiên Sa Thương Đạo
- Dỡ hàng tại các trạm dừng và kho chứa
arcs:
  - arc: 1
    status: Hoạt động bền bỉ (Bị bóc lột nhưng không thể thiếu)
    rank: Không Xếp Hạng
    leader: Công Đầu Sa Lực
    population: 60
    territory:
      - Các trạm dừng lớn trên Thiên Sa Thương Đạo
    assets:
      - name: Bãi tập kết hàng hóa
        type: Công Trình
      - name: Kho chứa tạm trên thương đạo
        type: Công Trình
    stats: [30, 10, 20, 60, 15, 40]
    divisions:
      - name: Ban Điều Hành
        role: Đàm phán hợp đồng, phân công lao động, bảo vệ quyền lợi phường viên
        headcount:
          hoi_truong: 1
          pho_hoi_truong: 0
          thanh_vien: 4
          tong_quan: 0
        members:
          - character: Sa Lực
            position: Công Đầu
            cultivation: Trúc Cơ (Tương đương, không tu luyện)
          - character: "[Tổ Trưởng Sa Hùng]"
            position: Tổ Trưởng Trạm Bắc
            cultivation: Luyện Khí Hậu Kỳ
            placeholder: true
      - name: Phu Khuân Vác
        role: Khuân vác hàng hóa cho các thương đoàn trên Thiên Sa Thương Đạo
        headcount:
          hoi_truong: 0
          pho_hoi_truong: 0
          thanh_vien: 55
          tong_quan: 0
        members:
          - character: Sa Mặc
            position: Phu Khuân Vác
            cultivation: Không có tu vi (Sức mạnh thể chất gấp ba Cự Nhân thường)
    relationships:
      - faction: Thiên Sa Thương Hội
        description: Bị coi là công cụ rẻ tiền, nhưng nếu phường đình công thì toàn bộ thương đạo tê liệt.
        diplomacy:
          lien_minh: -20
          tin: -30
          uy_hiep: 0
          thuong_mai: 60
          on_oan: -40
          le_thuoc: 50
      - faction: Kim Sa Thợ Mỏ Hội
        description: Đang lên kế hoạch liên minh, nếu thợ mỏ và phu khuân vác cùng đình công sẽ gây khó lớn.
        diplomacy:
          lien_minh: 50
          tin: 40
          uy_hiep: 0
          thuong_mai: 20
          on_oan: 0
          le_thuoc: 0
      - faction: Sa Cự Nhân Bộ Lạc
        description: Nhiều phu khuân vác xuất thân từ bộ lạc, vẫn giữ liên lạc qua lại.
        diplomacy:
          lien_minh: 30
          tin: 50
          uy_hiep: 0
          thuong_mai: 10
          on_oan: 0
          le_thuoc: 0
---

# Cự Tộc Phu Khuân Vác (巨族搬运工)

## I. Tổng Quan (总览)
Cự Tộc Phu Khuân Vác là phường lao động do Cự Nhân nghèo trên Thiên Sa Thương Đạo tập hợp lại, dưới sự dẫn dắt của Công Đầu Sa Lực. Với khoảng 60 Cự Nhân không có đất đai, không có mỏ, và không có kỹ năng tu luyện, thứ duy nhất họ sở hữu là sức lực bẩm sinh phi thường của Cự Tộc. Phường nhận hợp đồng khuân vác từ các thương đoàn trên thương đạo, tiền công rẻ mạt so với sức lao động bỏ ra nhưng đủ để nuôi sống gia đình. Tuy bị coi thường và bóc lột, phường nắm giữ một vũ khí đặc biệt: nếu tất cả phu khuân vác đình công đồng loạt, toàn bộ huyết mạch vận tải trên Thiên Sa Thương Đạo sẽ tê liệt hoàn toàn.

## II. Địa Lý & Tài Nguyên (地理与资源)
Phường không có lãnh địa riêng, hoạt động rải rác tại các trạm dừng lớn trên Thiên Sa Thương Đạo. Mỗi trạm dừng có một bãi tập kết hàng hóa và kho chứa tạm do phường quản lý — đây là nơi hàng hóa được chuyển giao giữa các thương đoàn và là nguồn việc làm chính. Tài nguyên duy nhất và quý giá nhất của phường là sức lực — một Cự Nhân trưởng thành khuân được lượng hàng bằng 20 Nhân Tộc lực sĩ, khiến họ trở thành lực lượng vận chuyển không thể thay thế trên tuyến đường thương mại quan trọng nhất Tây Mạc.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
Triết lý sống của phường là "Lưng thẳng, vai chắc — Cự Nhân không quỳ trước ai, kể cả khi khuân hàng", thể hiện lòng tự tôn mãnh liệt dù ở vị thế thấp nhất trong xã hội. Quy tắc quan trọng nhất: nhận tiền công xong mới giao hàng, không chịu nợ, không bị quỵt — ai vi phạm sẽ bị cả phường tẩy chay. Mỗi tối sau khi làm xong việc, Cự Nhân cùng nhau ngồi ăn cơm và kể chuyện cười — khoảnh khắc giản dị nhất nhưng là chất keo gắn kết cả phường. Dù làm công việc nặng nhọc nhất, phường tuyệt đối không cho phép ai xúc phạm nhân phẩm Cự Tộc — đây là ranh giới không bao giờ được vượt qua.

## IV. Cơ Cấu Tổ Chức (组织结构)
Công Đầu Sa Lực đứng đầu phường — Cự Nhân thấp nhất bộ lạc nhưng khỏe nhất và có tài đàm phán giỏi. Dưới ông là 4 Tổ Trưởng tương đương Luyện Khí Hậu Kỳ (tu vi bẩm sinh, không phải tu luyện chính thức), mỗi người phụ trách một trạm dừng trên thương đạo. Khoảng 60 phu khuân vác đa phần không có tu vi, dùng hoàn toàn sức thể chất thuần túy để làm việc. Đáng chú ý, trong phường có vài Cự Nhân già từng là chiến binh dày dạn kinh nghiệm, giờ già yếu chỉ còn đủ sức khuân hàng — nhưng kinh nghiệm chiến đấu của họ vẫn là nguồn lực tiềm ẩn.

## V. Công Pháp & Trận Pháp (功法与阵法)
- **Công Pháp:** Không có bất kỳ công pháp tu luyện nào. Toàn bộ sức mạnh dựa vào thể chất bẩm sinh phi thường của Cự Tộc — xương cốt cứng, cơ bắp dẻo dai, sức chịu đựng vượt xa Nhân Tộc nhiều lần.
- **Chiến Thuật:** Khi bị ức hiếp hoặc quỵt tiền, vũ khí duy nhất nhưng cực kỳ hiệu quả là đình công tập thể. Khi cả 60 Cự Nhân đồng loạt ngừng làm việc, không có lực lượng nào trên thương đạo thay thế được, khiến hàng hóa ứ đọng và thương đoàn chịu tổn thất nặng nề.

## VI. Đặc Sản Môn Phái (门派特产)
- **Dịch Vụ Khuân Vác Siêu Trọng:** Khả năng vận chuyển hàng hóa có trọng lượng mà không pháp khí hay linh thú nào có thể thay thế trên địa hình sa mạc khắc nghiệt.
- **Kinh Nghiệm Thương Đạo:** Kiến thức thực tiễn về mọi trạm dừng, tuyến đường, thời tiết sa mạc và các mối nguy trên Thiên Sa Thương Đạo — thông tin mà thương nhân mới luôn cần.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Bãi Tập Kết Hàng Hóa:** Khu vực rộng tại mỗi trạm dừng lớn, nơi hàng hóa được phân loại và chuyển giao giữa các thương đoàn.
- **Kho Chứa Tạm:** Nhà kho đơn giản xây bằng đá sa thạch, bảo vệ hàng hóa khỏi bão cát trong thời gian chờ vận chuyển.
- **Lều Nghỉ Phu:** Nơi ở tạm bợ cho phu khuân vác, dựng bằng vải bạt và xương yêu thú, đơn sơ nhưng đủ che nắng mưa.

## VIII. Kinh Tế (经济)
Kinh tế của phường hoàn toàn phụ thuộc vào tiền công khuân vác — mức thù lao rẻ mạt so với sức lao động bỏ ra, nhưng là nguồn thu nhập duy nhất cho 60 gia đình Cự Nhân nghèo. Thiên Sa Thương Hội trả lương thấp và đối xử như công cụ, nhưng không dám cắt hoàn toàn vì biết rằng không có ai thay thế được Cự Tộc trong việc khuân hàng siêu nặng. Gần đây, Sa Lực bắt đầu đàm phán tăng lương và cải thiện điều kiện làm việc, đồng thời bí mật liên hệ với Kim Sa Thợ Mỏ Hội để bàn chuyện phối hợp đình công — nếu thành công, đây sẽ là đòn đánh kinh tế nặng nề nhất vào Thiên Sa Thương Hội.

## IX. Lịch Sử Tóm Tắt (简史)
Cự Tộc nghèo trên Thiên Sa Thương Đạo từ lâu sống phân tán, nhận việc khuân vác lẻ tẻ từ các thương nhân qua đường với tiền công bèo bọt. Sa Lực — Cự Nhân thấp bé nhất nhưng khỏe nhất và thông minh nhất trong nhóm — nhận ra rằng nếu tập hợp lại thành phường, họ sẽ có sức mạnh đàm phán thay vì bị bóc lột từng cá nhân. Khoảng 30 năm trước, ông thành lập phường khuân vác, đặt ra quy tắc rõ ràng về tiền công và nhân phẩm. Kết quả khiêm tốn — tiền lương tăng chút ít, điều kiện tốt hơn chút ít — nhưng quan trọng nhất là phường đã cho Cự Nhân nghèo một tổ chức để dựa vào, thay vì đứng một mình giữa sa mạc khắc nghiệt.

## X. Giai Thoại & Bí Mật (轶事与秘密)
Sa Lực từng từ chối khuân một kiện hàng đặc biệt — ông nói "hàng đó có mùi máu" mà không giải thích thêm. Thương nhân sở hữu kiện hàng đó sau này bị phát hiện là kẻ buôn bán nô lệ, và kiện hàng chính là lồng giam người bọc kín. Trong phường có một Cự Nhân câm tên Sa Mặc — hắn khỏe gấp ba người thường, không ai biết lai lịch, và đôi khi ban đêm hắn nhìn lên trời với ánh mắt buồn không tả, như thể nhớ về một quá khứ mà hắn không thể kể. Kim Sa Thợ Mỏ Hội đang bí mật lên kế hoạch liên minh với phường — nếu cả thợ mỏ lẫn phu khuân vác cùng đình công, Thiên Sa Thương Hội sẽ đối mặt với cuộc khủng hoảng kinh tế nghiêm trọng nhất trong lịch sử.

## XI. Quan Hệ Thế Lực (势力关系)
| Thế Lực | Quan Hệ | Mô Tả |
|---|---|---|
| Thiên Sa Thương Hội | Lệ thuộc kinh tế | Bị bóc lột nhưng không thể thiếu |
| Kim Sa Thợ Mỏ Hội | Liên minh tiềm năng | Bí mật bàn kế hoạch đình công chung |
| Sa Cự Nhân Bộ Lạc | Huynh đệ | Nhiều phu khuân vác xuất thân từ bộ lạc |
