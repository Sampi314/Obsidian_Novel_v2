---
type: faction
name: Cự Tộc Thợ Xây
hantu: 巨族建筑工
faction_type: Hội
alignment: 3
race: Cự Tộc
region: Đông Hoang
founded: 30 năm trước
founder: Thạch Lực
emblem: Bua_Da_Va_Tuong.png
specialty: Xây dựng quy mô lớn, Khuân vác trọng tải, Đào móng
economy:
- Nhận khoán xây thành quách và công trình cho nhân tộc
- Đào kênh mương và khai thác đá
- Khuân vác hàng hóa siêu trọng
arcs:
  - arc: 1
    status: Lao động bần cùng
    rank: Hạng Năm
    leader: Phường Trưởng Thạch Lực
    population: 26
    territory:
      - Trại lều ngoại ô (Di chuyển theo công trình)
    assets:
      - name: Bộ Công Cụ Xây Dựng Cự Tộc
        type: Pháp Bảo
      - name: Di Vật Cổ (Thu giấu)
        type: Tài Nguyên
    stats: [60, 30, 20, 26, 15, 10]
    divisions:
      - name: Phường Thợ Xây
        role: Xây dựng công trình, đào móng, khuân đá cho các thành thị nhân tộc
        headcount:
          hoi_truong: 1
          pho_hoi_truong: 5
          thanh_vien: 20
          tong_quan: 0
        members:
          - character: Thạch Lực
            position: Phường Trưởng
            cultivation: Trúc Cơ Trung Kỳ
          - character: "[Thợ Cả Đá]"
            position: Thợ Cả
            cultivation: Luyện Khí Đỉnh Phong
            placeholder: true
          - character: "[Thợ Cả Gỗ]"
            position: Thợ Cả
            cultivation: Luyện Khí Hậu Kỳ
            placeholder: true
    relationships:
      - faction: Sơn Cốc Cự Tộc Ẩn Sĩ
        description: Cùng chủng tộc nhưng triết lý đối lập. Ẩn Sĩ chọn ẩn dật, Thợ Xây chọn hòa nhập xã hội dù bị bóc lột.
        diplomacy:
          lien_minh: 20
          tin: 30
          uy_hiep: 0
          thuong_mai: 10
          on_oan: 0
          le_thuoc: 0
      - faction: Bách Nghệ Phường Tổng Đàn
        description: Đôi khi hợp tác trong các dự án xây dựng lớn. Bách Nghệ Phường đánh giá cao kỹ năng Cự Tộc nhưng trả công công bằng hơn nhân tộc bình thường.
        diplomacy:
          lien_minh: 20
          tin: 40
          uy_hiep: 0
          thuong_mai: 50
          on_oan: 10
          le_thuoc: 0
      - faction: Tiểu Cự Nhân Đoàn
        description: Quan hệ huyết thống, Tiểu Cự Nhân Đoàn là nhóm Cự Tộc lai kích thước nhỏ hơn. Hai bên thỉnh thoảng chia sẻ thức ăn và tin tức.
        diplomacy:
          lien_minh: 30
          tin: 50
          uy_hiep: 0
          thuong_mai: 20
          on_oan: 10
          le_thuoc: 0
---

# CỰ TỘC THỢ XÂY (巨族建筑工)

## I. Tổng Quan (总览)
Cự Tộc Thợ Xây là một phường thợ xây dựng do Cự Tộc thành lập, chuyên nhận khoán các công trình nặng nhọc mà nhân tộc không đủ sức thực hiện. Với sức mạnh thể xác bẩm sinh — một Cự Tộc có thể làm bằng một trăm nhân tộc — họ là lực lượng lao động không thể thay thế trong việc xây thành quách, đào kênh, khuân đá. Tuy nhiên, vị thế xã hội của Phường cực kỳ thấp: bị nhân tộc chèn ép giá công, bị coi như sức kéo rẻ mạt, tiền kiếm được chỉ đủ nuôi sống hai mươi sáu thành viên qua ngày. Với triết lý "Sức mạnh để xây dựng, không phải để phá hủy", Phường tự an ủi rằng lao động cũng là một dạng tu hành — dù thực tế đắng cay hơn nhiều.

## II. Địa Lý & Tài Nguyên (地理与资源)
Phường không có trụ sở cố định mà di chuyển theo công trình, dựng trại ngoại ô các thành thị nhân tộc. Lều trại làm từ da thú và cột gỗ, kích thước lớn gấp năm lần lều bình thường để phù hợp với thân hình Cự Tộc cao ba đến năm trượng. Vị trí dựng trại thường ở ngoài rìa thành — nhân tộc không cho phép Cự Tộc vào thành vì sợ gây hư hại đường xá. Tài nguyên duy nhất của Phường là sức mạnh thể xác và bộ công cụ xây dựng thô sơ bằng đá và gỗ cứng, được chế tác theo kích thước Cự Tộc.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
Cự Tộc Thợ Xây giữ lại một phần văn hóa Cự Tộc cổ đại: tôn trọng đá và đất, coi mỗi tảng đá là một phần xương cốt của đại địa. Trước mỗi công trình mới, Thạch Lực sẽ gõ búa xuống đất ba lần và nói lời cảm ơn với núi đá đã cung cấp nguyên liệu. Quy tắc của Phường rõ ràng: nhận việc thì làm hết sức, không gây sự với khách hàng dù bị chèn ép, tiền kiếm được chia đều cho tất cả. Phong tục đáng chú ý nhất là mỗi công trình hoàn thành, Cự Tộc thợ xây bí mật khắc một ký hiệu nhỏ lên đá nền — dấu ấn âm thầm chứng minh rằng chính tay họ đã xây nên tòa thành này, dù không ai biết đến.

## IV. Cơ Cấu Tổ Chức (组织结构)
Phường Trưởng Thạch Lực là Cự Tộc trung niên, cao bốn trượng, da xám đá, mặt trầm lặng hiếm khi bộc lộ cảm xúc. Hắn đóng vai trò trung gian đàm phán với khách hàng nhân tộc — công việc hắn ghét nhất nhưng không ai khác làm được vì phải kiềm chế cơn giận trước sự khinh miệt. Tu vi tương đương Trúc Cơ Trung Kỳ nhờ thể phách bẩm sinh, không tu luyện công pháp. Năm Thợ Cả là Cự Tộc kinh nghiệm, mỗi người chuyên một loại công trình: đá, gỗ, đất, kênh mương, và vận chuyển. Hai mươi Thợ hầu hết là Cự Tộc trẻ, bán sức lao động để kiếm linh thạch và thực phẩm.

## V. Công Pháp & Trận Pháp (功法与阵法)
- **Công Pháp:** Phường không tu luyện công pháp chính thống. Cự Tộc dựa hoàn toàn vào sức mạnh thể phách bẩm sinh — da cứng như đá, cơ bắp phi thường, sức chịu đựng vượt xa mọi chủng tộc. Thạch Lực biết một bài "Thạch Phách Cường Hóa Thuật" truyền miệng trong Cự Tộc, giúp tăng cường độ cứng của da thịt tạm thời, nhưng không phải công pháp tu tiên chính quy.
- **Trận Pháp:** Không có trận pháp. Phòng thủ duy nhất là sức mạnh thể xác — bất kỳ kẻ nào tấn công trại đều phải đối mặt với hai mươi sáu Cự Tộc giận dữ, mỗi người có thể lật đổ một tòa thành nhỏ.

## VI. Đặc Sản Môn Phái (门派特产)
- **Công Trình Cự Tộc:** Thành quách và kiến trúc do Cự Tộc xây dựng nổi tiếng bền vững hơn hẳn — móng sâu hơn, tường dày hơn, đá xếp khít hơn nhờ sức mạnh phi thường. Nhiều thành trì trứ danh Đông Hoang thực ra do Cự Tộc xây nhưng không ai thừa nhận.
- **Ký Hiệu Đá Nền:** Những ký hiệu Cự Tộc khắc trên đá nền mỗi công trình, theo thời gian trở thành dấu hiệu bảo chứng chất lượng — dù chỉ những ai biết tìm mới nhận ra.
- **Đá Tạc Tay:** Thỉnh thoảng, Cự Tộc dùng thời gian rảnh tạc tượng đá nhỏ (nhỏ theo tiêu chuẩn Cự Tộc, tức bằng người thường) để bán kiếm thêm. Tượng thô mộc nhưng có thần thái sống động.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Trại Lều Di Động:** Năm chiếc lều khổng lồ bằng da thú, dựng đi dựng lại mỗi lần chuyển công trình. Lều lớn nhất là "lều hội" nơi cả Phường ăn uống và nghỉ ngơi chung.
- **Bãi Công Cụ:** Khu vực chứa búa, đục, xà beng và các dụng cụ xây dựng kích thước Cự Tộc. Đây là tài sản giá trị nhất của Phường, được bảo vệ cẩn thận.
- **Hố Lửa Trung Tâm:** Đống lửa lớn giữa trại, nơi Cự Tộc nấu ăn và sưởi ấm. Mỗi tối, cả Phường ngồi quanh lửa ăn cơm và kể chuyện — khoảnh khắc duy nhất trong ngày họ cảm thấy bình yên.

## VIII. Kinh Tế (经济)
Kinh tế của Phường cực kỳ bấp bênh và bị bóc lột nặng nề. Nhân tộc trả công cho Cự Tộc chưa đến một phần mười giá trị lao động thực tế — xây một bức tường thành mất ba tháng nhưng tiền công chỉ bằng một tuần thuê nhân công bình thường. Thạch Lực biết nhưng không có lựa chọn: Cự Tộc bị kỳ thị, không ai khác chịu thuê, và hai mươi sáu miệng ăn cần được nuôi. Thu nhập chia đều, mỗi người đủ mua thực phẩm cơ bản và vài viên linh thạch hạ phẩm. Không có tiết kiệm, không có dự phòng — mất một hợp đồng là cả Phường đói.

## IX. Lịch Sử Tóm Tắt (简史)
Khi Cự Tộc suy tàn, phần lớn bị xua đuổi khỏi vùng đất tổ tiên, nhiều người không có chỗ đứng trong thế giới mới do nhân tộc thống trị. Thạch Lực nhận ra sức mạnh thể xác bẩm sinh là thứ duy nhất Cự Tộc còn có giá trị — một Cự Tộc có thể khuân tảng đá mà trăm nhân tộc không nhúc nhích nổi. Ba mươi năm trước, hắn lập Phường, nhận khoán xây thành quách, đào kênh, khuân đá cho các thành thị nhân tộc. Công việc nặng nhọc, giá rẻ mạt, nhưng ít nhất Cự Tộc có cái ăn. Qua ba thập kỷ, Phường đã xây không biết bao nhiêu công trình, nhưng chưa bao giờ được ghi nhận.

## X. Giai Thoại & Bí Mật (轶事与秘密)
Thạch Lực bị nhân tộc trả công bằng chưa đến một phần mười giá trị lao động thực — hắn biết, mọi người trong Phường đều biết, nhưng không ai dám phản kháng. Có lần, một Cự Tộc trẻ nổi giận đòi công bằng, suýt đánh chết chủ thầu nhân tộc. Thạch Lực phải quỳ xuống xin lỗi suốt một ngày trời trước cổng thành để Phường không bị cấm nhận việc vĩnh viễn.

Trong quá trình đào móng các công trình, Cự Tộc đôi khi phát hiện di vật cổ đại dưới đất — mảnh pháp khí, đá khắc chữ lạ, đôi khi cả cốt hài tu sĩ bị chôn vùi. Thạch Lực lén giấu vài thứ lại, bọc cẩn thận trong da thú và chôn dưới trại. Hắn không biết chúng là gì, nhưng bản năng bảo hắn rằng một ngày nào đó chúng sẽ hữu dụng — có lẽ là thứ duy nhất giúp Cự Tộc thay đổi số phận.

## XI. Quan Hệ Thế Lực (势力关系)
- **Sơn Cốc Cự Tộc Ẩn Sĩ:** Cùng chủng tộc nhưng triết lý đối lập. Ẩn Sĩ chọn ẩn dật trong núi, Thợ Xây chọn hòa nhập dù bị bóc lột. Hai bên tôn trọng lựa chọn của nhau và đôi khi trao đổi tin tức.
- **Bách Nghệ Phường Tổng Đàn:** Đối tác hợp tác trong dự án xây dựng, Bách Nghệ Phường trả công công bằng hơn và đối xử tử tế hơn nhân tộc khác.
- **Tiểu Cự Nhân Đoàn:** Đồng tộc, Tiểu Cự Nhân kích thước nhỏ hơn nhưng cùng mang máu Cự Tộc. Hai bên chia sẻ thức ăn và tin tức trong những lúc khó khăn.
