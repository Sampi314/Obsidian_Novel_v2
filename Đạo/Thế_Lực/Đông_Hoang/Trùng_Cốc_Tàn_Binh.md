---
type: faction
name: Trùng Cốc Tàn Binh
hantu: 蟲谷殘兵
faction_type: Liên Minh
alignment: 2
race: Đa chủng tộc (Nhân Tộc, Bán Yêu, Tán Tu)
region: Đông Hoang
founded: 25 năm trước
founder: Đoàn Thiết Giáp
emblem: Trung_Coc_Tan_Binh.png
specialty: Chiến thuật chống Trùng Triều, Chế tạo giáp kháng axit, Y thuật chữa nọc trùng
economy:
- Bán giáp xác trùng và nọc trùng thu thập
- Nhận phí bảo vệ làng biên giới khỏi Trùng Triều
- Trao đổi kinh nghiệm chống trùng lấy vật tư
arcs:
  - arc: 1
    status: Chiến đấu tiêu hao
    rank: Hạng Tư
    leader: Liên Minh Chủ Đoàn Thiết Giáp
    population: 200
    territory:
      - Pháo đài gỗ biên giới phía nam Vạn Trùng Cốc
      - Vùng đệm giữa Vạn Trùng Cốc và khu dân cư Nam Cương
    assets:
      - name: Pháo Đài Trùng Cốc
        type: Công Trình
      - name: Thiết Bích Phòng Trùng Trận
        type: Trận Pháp
      - name: Quả trứng Trùng Vương
        type: Bảo Vật
      - name: Kho nọc trùng và giáp xác
        type: Tài Nguyên
    stats: [400, 200, 300, 200, 350, 150]
    divisions:
      - name: Chiến Binh Tiền Tuyến
        role: Trực tiếp chiến đấu chống Trùng Triều và tuần tra vùng đệm
        headcount:
          tuong: 2
          uy: 8
          binh: 170
        members:
          - character: "[Đoàn Thiết Giáp]"
            position: Liên Minh Chủ
            cultivation: Kim Đan Sơ Kỳ
            placeholder: true
          - character: "[Ngô Kỳ]"
            position: Phó Minh Chủ
            cultivation: Trúc Cơ Viên Mãn
            placeholder: true
      - name: Hậu Cần & Y Sư
        role: Chữa trị vết thương nọc trùng, quản lý kho vật tư và lương thực
        headcount:
          tuong: 0
          uy: 2
          binh: 18
        members:
          - character: "[Y Sư Trưởng]"
            position: Y Sư Trưởng
            cultivation: Trúc Cơ Trung Kỳ
            placeholder: true
    relationships:
      - faction: Vạn Trùng Cốc
        description: Kẻ thù chính. Trùng Cốc Tàn Binh tồn tại với mục đích duy nhất là ngăn chặn Trùng Triều từ Vạn Trùng Cốc tràn ra khu dân cư.
        diplomacy:
          lien_minh: -100
          tin: -100
          uy_hiep: 40
          thuong_mai: -100
          on_oan: -90
          le_thuoc: 0
      - faction: Vạn Độc Môn
        description: Từng nhiều lần xin viện trợ nhưng đều bị từ chối lạnh lùng. Đoàn Thiết Giáp nghi ngờ Vạn Độc Môn có liên quan đến việc kích hoạt Trùng Triều.
        diplomacy:
          lien_minh: -30
          tin: -60
          uy_hiep: 20
          thuong_mai: -10
          on_oan: -40
          le_thuoc: 0
      - faction: Phản Sào Trùng Quần
        description: Đồng minh tiềm năng. Cùng chống lại Trùng Tộc nhưng từ hai hướng khác nhau — Tàn Binh bảo vệ nhân tộc, Phản Sào là trùng chống trùng.
        diplomacy:
          lien_minh: 30
          tin: 20
          uy_hiep: 10
          thuong_mai: 10
          on_oan: 0
          le_thuoc: 0
---

# Trùng Cốc Tàn Binh (蟲谷殘兵)

## I. Tổng Quan (总览)

Trùng Cốc Tàn Binh là một liên minh quân sự gồm khoảng 200 chiến binh đa chủng tộc, đóng quân tại vùng đệm giữa Vạn Trùng Cốc và khu dân cư Nam Cương với sứ mệnh duy nhất: ngăn chặn Trùng Triều tràn ra tàn phá. Được thành lập bởi Đoàn Thiết Giáp — một cựu đội trưởng thương đoàn mất cả đoàn trong Trùng Triều, tự tu luyện đến Kim Đan nhờ lòng hận thù — liên minh này là lá chắn cuối cùng giữa hàng triệu con Trùng Binh và dân thường vô tội. Với triết lý "Sống sót là đã thắng", Tàn Binh chào đón bất kỳ ai sẵn sàng chiến đấu, bất kể chủng tộc, quá khứ hay con đường tu luyện.

## II. Địa Lý & Tài Nguyên (地理与资源)

Pháo đài của Trùng Cốc Tàn Binh tọa lạc tại biên giới phía nam Vạn Trùng Cốc — vùng đệm giữa rừng trùng và khu dân cư Nam Cương, nơi Trùng Triều thường xuyên tràn qua mỗi khi bùng phát. Đất đai xung quanh pháo đài hoang tàn, trơ trụi do nhiều lần bị Trùng Triều tàn phá — cây cối bị ăn sạch, đất bị axit trùng ăn mòn đến mức không thể trồng trọt. Pháo đài xây bằng gỗ gia cố bằng xương Trùng Tộc, xung quanh là hào sâu đổ dầu chống trùng — tuyến phòng thủ tạm bợ nhưng đã đứng vững suốt 25 năm. Tài nguyên chính đến từ xác Trùng Tộc sau mỗi đợt Trùng Triều: giáp xác trùng dùng chế tạo áo giáp nhẹ và khiên chống axit, nọc trùng thu thập từ xác Trùng Binh bán cho dược sư và độc sư. Tuy nhiên, tài nguyên quý giá nhất của Tàn Binh không phải vật chất mà là kinh nghiệm chiến đấu chống Trùng Triều — thứ mà không linh thạch nào mua được.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)

Văn hóa Trùng Cốc Tàn Binh là văn hóa của những kẻ sống sót — thực dụng, cứng rắn và không màng danh lợi. Triết lý cốt lõi là "Sống sót là đã thắng": chỉ cần ngày mai vẫn còn thở, đó đã là chiến thắng. Quy tắc duy nhất nghiêm ngặt là "Bất kể chủng tộc, ai muốn chống Trùng Triều đều được chào đón. Kẻ đào ngũ khi Trùng Triều đến sẽ bị trục xuất vĩnh viễn." Sau mỗi đợt Trùng Triều, những thành viên sống sót tập trung lại cùng uống "rượu trùng" — rượu ngâm nọc trùng pha loãng — để kỷ niệm việc còn sống. Tên của người chết được khắc lên cột gỗ chính của pháo đài, đến nay cột gỗ đã gần kín chữ, ghi nhận hàng trăm linh hồn đã ngã xuống tại nơi này.

## IV. Cơ Cấu Tổ Chức (组织结构)

Cơ cấu tổ chức theo mô hình quân đoàn đơn giản, coi trọng hiệu quả chiến đấu hơn hình thức.

- **Liên Minh Chủ — Đoàn Thiết Giáp:** Cựu đội trưởng thương đoàn, mất cả đoàn trong đợt Trùng Triều lớn nhất 200 năm. Lòng hận thù đã thúc đẩy ông tự tu luyện đến Kim Đan Sơ Kỳ — thành tựu phi thường đối với một tán tu không có tài nguyên tông môn. Ông là linh hồn và cũng là trụ cột chiến lực của toàn liên minh.
- **Phó Minh Chủ — Ngô Kỳ:** Bán yêu (nhân-trùng hỗn huyết), tu vi Trúc Cơ Viên Mãn. Ghét Trùng Tộc hơn bất kỳ ai vì bị cả nhân tộc lẫn trùng tộc khinh bỉ. Sự am hiểu bản năng trùng tộc của Ngô Kỳ là vũ khí chiến lược quý giá.
- **Chiến Binh (khoảng 170 người):** Tu vi từ Luyện Khí đến Trúc Cơ, đủ mọi chủng tộc — nhân tộc, bán yêu, thậm chí cả vài Thạch Tộc. Tất cả đều có chung một điểm: lý do cá nhân để hận Trùng Triều.
- **Hậu Cần & Y Sư (20 người):** Chuyên chữa trị vết thương do nọc trùng, pha chế thuốc giải độc và quản lý kho lương thực eo hẹp.

## V. Công Pháp & Trận Pháp (功法与阵法)

Trùng Cốc Tàn Binh không có công pháp chấn phái — mỗi chiến binh tu luyện theo cách riêng tùy thuộc vào xuất thân. Tuy nhiên, liên minh sở hữu một hệ thống chiến thuật chống Trùng Triều cực kỳ hiệu quả được đúc kết từ 25 năm kinh nghiệm xương máu.

- **Trận Pháp:** *Thiết Bích Phòng Trùng Trận* — trận pháp phòng thủ dùng hỏa hệ linh thạch tạo tường lửa ngăn Trùng Binh. Hiệu quả cao trước trùng cấp thấp và trung bình, nhưng có hạn trước trùng cấp cao.
- **Chiến thuật bẫy hỏa:** Chiến binh sử dụng vũ khí phủ dầu lửa kết hợp bẫy hố chứa axit thu thập từ xác trùng — biến vũ khí của kẻ thù thành công cụ phòng thủ.
- **Đội hình "Thiết Giáp":** Do Đoàn Thiết Giáp sáng tạo, chiến binh xếp thành hàng rào khiên từ giáp xác trùng, lùi dần có tổ chức trong khi hỏa công thiêu đốt tuyến trước — chiến thuật tiêu hao hiệu quả nhất chống lại số lượng áp đảo của Trùng Binh.

## VI. Đặc Sản Môn Phái (门派特产)

- **Giáp Trùng Xác:** Áo giáp nhẹ chế tạo từ giáp xác trùng thu thập sau mỗi đợt Trùng Triều. Tuy không đẹp mắt nhưng cực kỳ bền, kháng axit và nhẹ hơn giáp kim loại thông thường. Được một số thế lực bên ngoài mua với giá khá.
- **Nọc Trùng Tinh Chế:** Nọc trùng thu thập từ xác Trùng Binh, được Y Sư tinh chế thành các lọ nhỏ bán cho dược sư và độc sư. Là nguyên liệu quý cho nhiều loại độc dược và cũng là thành phần chính của thuốc giải nọc trùng.
- **Rượu Trùng:** Rượu ngâm nọc trùng pha loãng — đặc sản "văn hóa" của Tàn Binh. Vị cực đắng và hơi tê lưỡi, nhưng có tác dụng tăng cường kháng độc tạm thời. Chỉ những chiến binh sống sót qua ít nhất một đợt Trùng Triều mới được uống.

## VII. Cơ Sở Hạ Tầng (基础设施)

- **Pháo Đài Trùng Cốc:** Pháo đài gỗ gia cố bằng xương Trùng Tộc, bao gồm tường thành cao 10 mét, cổng chính bọc giáp xác trùng, và nhiều vọng gác quan sát. Tuy tạm bợ nhưng đã đứng vững 25 năm nhờ sửa chữa liên tục.
- **Hào Dầu Chống Trùng:** Hào sâu 3 mét bao quanh pháo đài, chứa dầu lửa có thể đốt cháy khi Trùng Triều tấn công, tạo tường lửa ngăn cách đầu tiên.
- **Kho Nọc Trùng & Giáp Xác:** Kho chứa ngầm bên trong pháo đài, lưu trữ nọc trùng tinh chế, giáp xác trùng và vũ khí dự phòng.
- **Doanh Trại Y Xá:** Khu vực điều trị thương binh nằm ở trung tâm pháo đài, trang bị thuốc giải nọc trùng và các loại dược liệu cơ bản.
- **Cột Gỗ Tưởng Niệm:** Cột gỗ khổng lồ đặt giữa sân pháo đài, khắc tên tất cả chiến binh đã hi sinh. Gần đầy chữ, sắp phải dựng cột thứ hai.

## VIII. Kinh Tế (经济)

Kinh tế Trùng Cốc Tàn Binh luôn trong tình trạng eo hẹp và bấp bênh. Nguồn thu chính đến từ việc bán giáp xác trùng và nọc trùng tinh chế — sản phẩm phụ từ xác Trùng Binh sau mỗi đợt chiến đấu. Ngoài ra, một số làng biên giới Nam Cương đóng phí bảo hộ cho Tàn Binh, nhưng số tiền này ít ỏi vì dân biên giới cũng nghèo khó. Đoàn Thiết Giáp từng nhiều lần gửi thư xin viện trợ từ Vạn Độc Môn và Đan Hà Cốc — hai thế lực lớn gần nhất — nhưng đều bị từ chối lạnh lùng. Kết quả là Tàn Binh phải tự cung tự cấp trong điều kiện thiếu thốn triền miên: vũ khí cũ, linh thạch hao hụt, thuốc men không đủ. Mỗi đợt Trùng Triều đều là canh bạc sinh tử không chỉ vì Trùng Binh mà còn vì thiếu vật tư chiến đấu.

## IX. Lịch Sử Tóm Tắt (简史)

Hai mươi lăm năm trước, đợt Trùng Triều lớn nhất trong 200 năm bùng phát từ Vạn Trùng Cốc, tàn phá 3 làng biên giới Nam Cương, giết chết hàng trăm dân thường và tu sĩ. Đoàn Thiết Giáp — khi đó chỉ là đội trưởng một thương đoàn nhỏ — mất toàn bộ đồng đội trong thảm họa đó. Lòng hận thù biến thành động lực tu luyện, ông tự mình đạt Kim Đan Sơ Kỳ trong hoàn cảnh không có tài nguyên tông môn. Sau đó, ông tập hợp những kẻ sống sót từ nhiều chủng tộc — bất kể quá khứ, ai muốn trả thù Trùng Triều đều được chào đón — cùng thề xây pháo đài tại nơi ba làng bị hủy diệt. Suốt 25 năm, Trùng Cốc Tàn Binh đã đẩy lùi 6 đợt Trùng Triều nhỏ, nhưng mỗi lần đều tổn thất nặng nề. Liên minh tồn tại không phải nhờ sức mạnh áp đảo mà nhờ ý chí bất khuất và kinh nghiệm xương máu.

## X. Giai Thoại & Bí Mật (轶事与秘密)

- Đoàn Thiết Giáp nghi ngờ Trùng Triều không phải hiện tượng tự nhiên mà do ai đó cố ý kích hoạt Trùng Mẫu — sinh vật mẹ sinh ra tất cả Trùng Binh. Ông đang bí mật điều tra manh mối dẫn đến Vạn Độc Môn, nhưng chưa có đủ bằng chứng.
- Trong pháo đài có một quả trứng Trùng Vương bị bắt từ đợt Trùng Triều trước — Đoàn Thiết Giáp giữ nó như vũ khí cuối cùng, dự định kích nở và thuần hóa để có thể chống lại Trùng Triều bằng chính loài trùng. Tuy nhiên, ông không biết rằng quả trứng sắp tự nở mà không cần ai kích hoạt.
- Ngô Kỳ — Phó Minh Chủ bán yêu nhân-trùng — đôi khi nghe thấy "tiếng gọi" từ sâu trong Vạn Trùng Cốc, như thể Trùng Mẫu đang cố thu hút phần trùng trong huyết mạch của anh ta. Ngô Kỳ chưa nói điều này với ai.

## XI. Quan Hệ Thế Lực (势力关系)

- **Vạn Trùng Cốc:** Kẻ thù tuyệt đối. Trùng Cốc Tàn Binh tồn tại với mục đích duy nhất là ngăn chặn Trùng Triều. Không có bất kỳ không gian nào cho đàm phán hay hòa giải.
- **Vạn Độc Môn:** Thế lực lớn gần nhất nhưng từ chối mọi yêu cầu viện trợ. Đoàn Thiết Giáp nghi ngờ Vạn Độc Môn có liên quan đến việc kích hoạt Trùng Triều, khiến mối quan hệ vốn lạnh nhạt càng thêm căng thẳng.
- **Phản Sào Trùng Quần:** Đồng minh tiềm năng bất ngờ. Phản Sào là những Trùng Tộc nổi loạn chống lại Trùng Mẫu — kẻ thù của kẻ thù. Hai bên đang thăm dò khả năng hợp tác, dù sự nghi kỵ giữa nhân tộc và trùng tộc vẫn là rào cản lớn.
- **Dân Làng Biên Giới Nam Cương:** Người dân mà Tàn Binh bảo vệ. Dù nghèo khó, họ vẫn đóng góp lương thực và vật tư trong khả năng, thể hiện lòng biết ơn đối với lá chắn duy nhất giữa họ và Trùng Triều.
