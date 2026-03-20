---
type: faction
name: Yêu Thú Cứu Hộ Đoàn
hantu: 妖獸救護團
faction_type: Hội
alignment: 8
race: Yêu Tộc (Đa loài)
region: Vô Tận Hải
founded: 60 năm trước
founder: Hùng Từ Bi
emblem: Ban_Tay_Gau_Om_La.png
specialty: Thổ Hệ Hộ Thể Quyết, cứu chữa linh thú, suối nước ấm linh
economy:
  - Quyên góp từ yêu tộc biết ơn
  - Bán dược thảo ven suối (số lượng nhỏ)
  - Đổi công chữa trị lấy vật tư từ các bộ lạc lân cận
arcs:
  - arc: 1
    status: Hoạt động ổn định
    rank: Hạng Năm
    leader: Đoàn Trưởng Hùng Từ Bi (Trúc Cơ Hậu Kỳ, gấu yêu)
    population: 25
    territory:
      - Sườn núi phía bắc dãy Núi Độc Long — khu rừng thưa quanh suối nước ấm
    assets:
      - name: Suối Nước Ấm Linh
        type: Tài Nguyên
      - name: Linh Mạch Nhỏ (bí mật)
        type: Bí Cảnh
      - name: Hang động hồi phục cho linh thú
        type: Công Trình
    stats: [30, 50, 100, 25, 40, 60]
    divisions:
      - name: Ban Chữa Trị
        role: Cứu chữa và chăm sóc linh thú bị thương
        headcount:
          hoi_truong: 1
          pho_hoi_truong: 1
          thanh_vien: 8
          tong_quan: 0
        members:
          - character: Hùng Từ Bi
            position: Đoàn Trưởng kiêm Trưởng Ban Chữa Trị
            cultivation: Trúc Cơ Hậu Kỳ
          - character: Yến Thanh
            position: Phó Đoàn kiêm Trinh Sát
            cultivation: Trúc Cơ Sơ Kỳ
      - name: Ban Trinh Sát
        role: Tuần tra rừng tìm linh thú bị thương, cảnh báo mối nguy
        headcount:
          hoi_truong: 0
          pho_hoi_truong: 0
          thanh_vien: 6
          tong_quan: 0
        members:
          - character: "[Trinh sát viên chim yêu]"
            position: Trinh Sát Viên
            cultivation: Luyện Khí Hậu Kỳ
            placeholder: true
      - name: Bệnh Nhân Thường Trực
        role: Linh thú đang hồi phục — một số chọn ở lại giúp đỡ sau khi khỏe
        headcount:
          hoi_truong: 0
          pho_hoi_truong: 0
          thanh_vien: 10
          tong_quan: 0
        members:
          - character: "[Hỏa Lân bị thương]"
            position: Bệnh nhân đặc biệt
            cultivation: Tương đương Trúc Cơ Trung Kỳ
            placeholder: true
    relationships:
      - faction: Mật Lâm Thợ Săn Hội
        description: Quan hệ từng xung đột — đã đạt thỏa thuận ngừng chiến. Thợ săn không săn ở vùng suối, đoàn cứu hộ không can thiệp vào vùng săn. Thỏa thuận mong manh nhưng được tôn trọng.
        diplomacy:
          lien_minh: -10
          tin: 10
          uy_hiep: 0
          thuong_mai: 0
          on_oan: -30
          le_thuoc: 0
      - faction: Kình Ngư Bộ Lạc
        description: Quan hệ hữu hảo — Kình Ngư Bộ Lạc đôi khi mang linh thú biển bị thương đến nhờ chữa trị. Hùng Từ Bi không phân biệt loài, luôn sẵn lòng giúp đỡ.
        diplomacy:
          lien_minh: 20
          tin: 40
          uy_hiep: 0
          thuong_mai: 10
          on_oan: 15
          le_thuoc: 0
      - faction: Hải Thảo Dược Sư
        description: Quan hệ hợp tác — Hải Thảo Dược Sư cung cấp dược liệu biển cho đoàn để chữa trị linh thú hải sinh, đổi lại đoàn chia sẻ kinh nghiệm về dược tính của dược thảo ven suối.
        diplomacy:
          lien_minh: 25
          tin: 35
          uy_hiep: 0
          thuong_mai: 30
          on_oan: 10
          le_thuoc: 0
---

# Yêu Thú Cứu Hộ Đoàn (妖獸救護團)

## I. Tổng Quan (总览)

Yêu Thú Cứu Hộ Đoàn là một tổ chức nhỏ chuyên cứu chữa linh thú bị thương, đặt trụ sở tại sườn núi phía bắc dãy Núi Độc Long, nơi có suối nước ấm chứa linh khí chữa lành. Đoàn Trưởng Hùng Từ Bi — một gấu đen yêu hóa hình thành lão nhân to lớn hiền lành — lập đoàn cách đây sáu mươi năm sau khi chứng kiến một đàn linh lộc bị thợ săn tàn sát. Với triết lý "yêu thú cũng biết đau, cũng xứng được cứu," đoàn không phân biệt loài — cứu tất cả linh thú bị thương, kể cả loài độc, miễn là chúng không đang tấn công người khác. Dù chỉ có hai mươi lăm thành viên — phần lớn là yêu tộc cấp thấp, nhiều con chính là linh thú được cứu trước đó — đoàn được linh thú toàn vùng tin tưởng và tự phát bảo vệ, biến lòng tin thành lá chắn vững chắc hơn bất kỳ trận pháp nào.

## II. Địa Lý & Tài Nguyên (地理 与 资源)

Đoàn đặt trụ sở tại sườn bắc Núi Độc Long, vùng rừng thưa nơi linh thú bị thương thường tìm đến vì có suối nước ấm chứa linh khí chữa lành. Khoảng đất bằng phẳng bên suối được bao quanh bởi cây cổ thụ che bóng, tạo không gian yên tĩnh và ấm áp lý tưởng cho linh thú hồi phục. Vài hang đá nhỏ ven suối được cải tạo thành phòng hồi phục cho linh thú lớn — đủ rộng để chứa một con gấu trưởng thành. Suối nước ấm linh có khả năng chữa vết thương ngoài da và giảm viêm, không phải thần dược nhưng hiệu quả đáng kể cho linh thú bị thương nhẹ đến trung bình. Dược thảo mọc ven suối không quý hiếm nhưng đủ dùng cho cứu chữa cơ bản. Tài nguyên quý giá nhất của đoàn không phải vật chất mà là lòng tin của linh thú vùng này — một thứ "tài sản vô hình" được xây dựng bằng sáu mươi năm kiên nhẫn và lương thiện.

## III. Văn Hóa & Tín Ngưỡng (文化 与 信仰)

Triết lý cốt lõi của Yêu Thú Cứu Hộ Đoàn là "yêu thú cũng biết đau, cũng xứng được cứu" — niềm tin rằng mọi sinh mạng đều đáng trân trọng, không phân biệt loài, cảnh giới hay xuất thân. Quy tắc của đoàn rõ ràng: cứu tất cả linh thú bị thương kể cả loài độc, không giam giữ linh thú đã hồi phục, và không can thiệp khi sinh vật đang tấn công người khác — đoàn cứu hộ, không phải đoàn chiến đấu. Phong tục đẹp nhất của đoàn là chính sách "tự nguyện ở lại": linh thú được cứu nếu muốn ở lại giúp đỡ thì được chào đón như thành viên, nhưng không bao giờ bị ép buộc. Nhiều thành viên hiện tại chính là linh thú từng được cứu — chúng chọn ở lại vì lòng biết ơn và vì tìm thấy ý nghĩa trong việc cứu giúp đồng loại.

## IV. Cơ Cấu Tổ Chức (组织结构)

Cơ cấu của Yêu Thú Cứu Hộ Đoàn đơn giản và linh hoạt, phản ánh bản chất nhân đạo của tổ chức. Đoàn Trưởng Hùng Từ Bi là linh hồn của đoàn — gấu đen yêu hóa hình thành lão nhân to lớn, tay chân thô kệch nhưng chữa trị linh thú với sự nhẹ nhàng khiến ai cũng ngạc nhiên. Gã từng bị thợ săn bắn trọng thương khi còn nhỏ, được một đạo sĩ cứu sống — trải nghiệm đó định hình toàn bộ triết lý sống của gã. Phó Đoàn Yến Thanh — chim yến yêu hình nhân — nhanh nhẹn và tinh mắt, phụ trách trinh sát tìm linh thú bị thương trong rừng. Mười lăm thành viên còn lại là yêu tộc cấp thấp đủ loài, cảnh giới từ Luyện Khí đến Trúc Cơ Sơ Kỳ. Ngoài ra, luôn có năm đến mười linh thú đang hồi phục tại trụ sở — chúng không phải thành viên nhưng được chăm sóc như thành viên.

## V. Công Pháp & Trận Pháp (功法 与 阵法)

Yêu Thú Cứu Hộ Đoàn không có công pháp chiến đấu chính thức — đây là đoàn cứu hộ, không phải tông môn hay quân đoàn. Hùng Từ Bi biết **Thổ Hệ Hộ Thể Quyết** — dùng linh lực thổ hệ bao bọc linh thú bị thương, ngăn chúng mất máu và ổn định vết thương trước khi chữa trị chi tiết. Quyết này không có tác dụng tấn công nhưng trong lĩnh vực cứu hộ, nó quý giá hơn bất kỳ sát chiêu nào. Phòng thủ của đoàn không dựa vào trận pháp hay vũ lực mà dựa vào danh tiếng — linh thú toàn vùng biết đây là nơi an toàn và tự phát bảo vệ nếu có kẻ tấn công. Từng có một nhóm thợ săn cố xâm nhập khu suối để bắt linh thú đang hồi phục; chúng bị hơn hai mươi linh thú hoang dã trong rừng xung quanh đồng loạt tấn công trước khi kịp đến gần — không phải vì đoàn ra lệnh, mà vì linh thú tự bảo vệ "bệnh viện" của chúng.

## VI. Đặc Sản Môn Phái (门派特产)

- **Dược Thảo Ven Suối:** Thảo dược mọc ven suối nước ấm linh hấp thụ linh khí chữa lành, có tác dụng giảm viêm, cầm máu và thúc đẩy tái sinh mô cho linh thú. Không quý hiếm nhưng hiệu quả ổn định, được các bộ lạc lân cận ưa chuộng.
- **Kinh Nghiệm Chữa Trị Linh Thú:** Sáu mươi năm cứu chữa đủ loài khiến Hùng Từ Bi tích lũy kiến thức y thuật linh thú phong phú hơn hầu hết đan dược sư. Kiến thức này không thành sách nhưng được truyền miệng cho thành viên đoàn.
- **Nước Suối Ấm Linh:** Nước suối đóng trong bình ngọc có thể giữ được linh tính chữa lành trong vài ngày, dùng làm thuốc rửa vết thương hoặc pha vào đan dược. Đoàn đôi khi đổi nước suối lấy vật tư từ các bộ lạc lân cận.

## VII. Cơ Sở Hạ Tầng (基础设施)

- **Suối Nước Ấm Linh:** Trái tim của trụ sở, suối nước ấm chảy ra từ một linh mạch nhỏ ẩn bên dưới. Nước suối trong vắt, nhiệt độ ấm vừa phải quanh năm, chứa linh khí chữa lành. Linh thú bị thương thường được ngâm trong suối để đẩy nhanh quá trình hồi phục.
- **Hang Động Hồi Phục:** Năm hang đá nhỏ ven suối, được cải tạo sạch sẽ và lót rơm khô, dùng làm phòng hồi phục cho linh thú lớn. Mỗi hang đủ rộng cho một con gấu trưởng thành nằm thoải mái.
- **Khu Vực Sinh Hoạt:** Vài túp lều gỗ đơn giản cho thành viên yêu tộc đã hóa hình ở. Những thành viên chưa hóa hình ngủ ngoài trời hoặc trong các bụi rậm — quen thuộc với đời sống tự nhiên.
- **Vườn Dược Thảo:** Mảnh vườn nhỏ ven suối nơi đoàn trồng thêm dược thảo chữa lành, bổ sung cho nguồn dược thảo mọc tự nhiên.

## VIII. Kinh Tế (经济)

Kinh tế của Yêu Thú Cứu Hộ Đoàn cực kỳ khiêm tốn và không ổn định. Thu nhập chính đến từ quyên góp tự nguyện của yêu tộc biết ơn — linh thú được cứu đôi khi mang về linh thạch, dược thảo quý hoặc vật liệu mà chúng tìm thấy trong rừng. Đoàn cũng bán một lượng nhỏ dược thảo ven suối và đổi nước suối ấm linh lấy vật tư từ các bộ lạc lân cận. Hải Thảo Dược Sư đôi khi cung cấp dược liệu biển miễn phí hoặc giá rẻ để đoàn chữa trị linh thú hải sinh. Hùng Từ Bi không bao giờ đặt mục tiêu tài chính — gã tin rằng chỉ cần đủ ăn đủ dùng là được, và suối nước ấm cung cấp phần lớn nhu cầu chữa trị. Tuy nhiên, những ca nặng đòi hỏi dược liệu quý thì đoàn thường phải chạy vạy khắp nơi.

## IX. Lịch Sử Tóm Tắt (简史)

Sáu mươi năm trước, Hùng Từ Bi — khi đó còn là một gấu đen yêu mới đạt Trúc Cơ — chứng kiến một đàn linh lộc bị thợ săn tàn sát tại chân Núi Độc Long. Chỉ một con non sống sót, run rẩy giữa đống xác đồng loại. Hùng Từ Bi ôm con lộc non về hang, chữa trị và nuôi lớn nó. Trải nghiệm đó thay đổi cuộc đời gã — gã quyết định dành phần đời còn lại để cứu giúp linh thú bị thương. Ban đầu chỉ mình gã hoạt động, dần có yêu tộc khác cảm kích mà gia nhập — Yến Thanh là thành viên đầu tiên, một chim yến yêu từng bị bẫy gãy cánh và được gã cứu. Đoàn từng xung đột với Mật Lâm Thợ Săn Hội khi cứu linh thú trong vùng săn của họ, suýt nổ ra chiến tranh nhỏ. Cuối cùng hai bên đạt thỏa thuận phân vùng: thợ săn không săn ở vùng suối, đoàn cứu hộ không can thiệp vào vùng săn. Thỏa thuận này duy trì đến nay dù đôi bên vẫn nghi ngờ lẫn nhau.

## X. Giai Thoại & Bí Mật (轶事 与 秘密)

Suối nước ấm thực ra chảy ra từ một linh mạch nhỏ ẩn dưới lòng đất — nếu ai đó phong ấn hoặc phá hủy mạch này, suối sẽ cạn và cả vùng mất đi năng lực chữa lành. Hùng Từ Bi biết chính xác vị trí linh mạch nhưng không nói cho bất kỳ ai, kể cả Yến Thanh. Gã sợ rằng nếu thông tin lộ ra, các thế lực lớn sẽ đến chiếm đoạt linh mạch hoặc kẻ xấu sẽ phá hủy nó để gây áp lực. Bí mật nguy hiểm hơn nằm ở một trong những "bệnh nhân" hiện tại: trong số linh thú đang hồi phục có một con **Hỏa Lân** — loài hiếm tưởng đã tuyệt chủng, lửa trên vảy của nó có thể dùng để luyện pháp khí cấp cao. Hùng Từ Bi đang tìm cách chữa trị và thả Hỏa Lân đi trước khi tin tức lộ ra — vì nếu bất kỳ tông môn hay thương hội nào biết có Hỏa Lân ở đây, chúng sẽ đến bằng mọi giá.

## XI. Quan Hệ Thế Lực (势力关系)

- **Mật Lâm Thợ Săn Hội:** Quan hệ căng thẳng nhưng có thỏa thuận. Hai bên từng xung đột trực tiếp khi đoàn cứu linh thú trong vùng săn. Sau đàm phán, đạt thỏa thuận phân vùng — mong manh nhưng được tôn trọng vì cả hai đều không muốn chiến tranh.
- **Kình Ngư Bộ Lạc:** Quan hệ hữu hảo. Kình Ngư Bộ Lạc đôi khi mang linh thú biển bị thương đến nhờ chữa trị, và Hùng Từ Bi luôn sẵn lòng giúp đỡ không điều kiện. Lòng biết ơn của Kình Ngư là một trong những mối quan hệ ngoại giao tốt nhất mà đoàn có.
- **Hải Thảo Dược Sư:** Quan hệ hợp tác chuyên môn. Hải Thảo Dược Sư cung cấp dược liệu biển cho đoàn để chữa trị linh thú hải sinh, đổi lại đoàn chia sẻ kiến thức về dược tính thảo mộc ven suối. Hai bên tôn trọng lẫn nhau trong lĩnh vực y thuật.
