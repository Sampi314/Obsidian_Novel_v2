---
type: faction
name: Phiêu Lưu Đảo Liên Minh
hantu: 漂流岛联盟
faction_type: Liên Minh
alignment: 2
race: Nhân Tộc (ngư dân phiêu bạt)
region: Vô Tận Hải
founded: Ba trăm năm trước
founder: Các trưởng đảo đầu tiên sau trận bão lớn
emblem: Den_Tren_Song.png
specialty: Hàng hải cận duyên, Ngư nghiệp truyền thống, Hải Triều Cảnh Giới Trận
economy:
  - Đánh bắt và buôn bán hải sản
  - Vận chuyển hàng hóa nhỏ lẻ bằng thương thuyền chung
  - Khai thác linh thạch phẩm chất thấp từ rạn đá ngầm
arcs:
  - arc: 1
    status: Tồn tại khiêm nhường
    rank: Hạng Năm
    leader: Tổng Đảo Chủ Trần Hải Phong
    population: 500
    territory:
      - Quần đảo mười bảy hòn (bờ đông Vô Tận Hải)
    assets:
      - name: Hải Triều Cảnh Giới Trận
        type: Trận Pháp
      - name: Thương Thuyền Chung (năm chiếc)
        type: Công Trình
      - name: Mỏ Linh Thạch Rạn Đá
        type: Tài Nguyên
    stats: [15, 20, 10, 50, 12, 8]
    divisions:
      - name: Hội Đồng Đảo Chủ
        role: Cơ quan quyết sách tối cao, mỗi đảo cử một đại diện
        headcount:
          minh_chu: 1
          pho_minh_chu: 2
          truong_lao: 0
          su_gia: 0
          thanh_vien_phai: 17
        members:
          - character: Trần Hải Phong
            position: Tổng Đảo Chủ (Minh Chủ)
            cultivation: Kim Đan Sơ Kỳ
            placeholder: false
          - character: "[Phó Đảo Chủ Đông]"
            position: Phó Minh Chủ
            cultivation: Trúc Cơ Hậu Kỳ
            placeholder: true
      - name: Hải Tuần Đội
        role: Tuần tra bảo vệ vùng biển quanh quần đảo
        headcount:
          minh_chu: 0
          pho_minh_chu: 0
          truong_lao: 0
          su_gia: 0
          thanh_vien_phai: 30
        members:
          - character: "[Đội Trưởng Hải Tuần]"
            position: Đội Trưởng
            cultivation: Trúc Cơ Sơ Kỳ
            placeholder: true
      - name: Thương Thuyền Đoàn
        role: Vận chuyển hàng hóa trao đổi với đất liền
        headcount:
          minh_chu: 0
          pho_minh_chu: 0
          truong_lao: 0
          su_gia: 0
          thanh_vien_phai: 25
        members:
          - character: "[Thuyền Trưởng Chính]"
            position: Thuyền Trưởng
            cultivation: Luyện Khí Viên Mãn
            placeholder: true
    relationships:
      - faction: Đảo Quốc Tự Trị Hội
        description: Quan hệ thân thiện, hai bên hỗ trợ lẫn nhau khi bị hải tặc tấn công, thường xuyên trao đổi lương thực và tin tức.
        diplomacy:
          lien_minh: 60
          tin: 55
          uy_hiep: 0
          thuong_mai: 50
          on_oan: 40
          le_thuoc: 0
      - faction: Hắc Hải Hải Tặc
        description: Nạn nhân thường xuyên bị cướp phá, buộc phải nộp "thuế bình an" hàng năm để tránh bị tấn công.
        diplomacy:
          lien_minh: -80
          tin: -90
          uy_hiep: -70
          thuong_mai: -60
          on_oan: -80
          le_thuoc: -50
      - faction: Hải Thần Cung
        description: Kính trọng nhưng xa cách, ngư dân cầu nguyện Hải Thần phù hộ nhưng Hải Thần Cung không quan tâm đến liên minh nhỏ bé này.
        diplomacy:
          lien_minh: 5
          tin: 10
          uy_hiep: 0
          thuong_mai: 5
          on_oan: 0
          le_thuoc: 15
---

# Phiêu Lưu Đảo Liên Minh (漂流岛联盟)

## I. Tổng Quan (总览)
Phiêu Lưu Đảo Liên Minh là liên minh của mười bảy hòn đảo nhỏ rải rác gần bờ đông Vô Tận Hải, nơi khoảng năm trăm ngư dân phiêu bạt quây quần sinh sống. Đây là một thế lực Hạng Năm khiêm nhường, không có tham vọng lớn lao hay sức mạnh đáng kể — mục tiêu duy nhất của họ là tồn tại qua mỗi mùa bão và kiếm đủ cái ăn giữa đại dương mênh mông. Dưới sự dẫn dắt của Tổng Đảo Chủ Trần Hải Phong — một tu sĩ Kim Đan Sơ Kỳ từng là đệ tử ngoại môn bị trục xuất — liên minh duy trì sự gắn kết lỏng lẻo nhưng chân thành giữa các đảo, nơi mỗi hộ gia đình vừa là ngư dân vừa là chiến sĩ khi cần thiết.

## II. Địa Lý & Tài Nguyên (地理 与 资源)
Liên minh gồm mười bảy hòn đảo nhỏ rải rác gần bờ đông Vô Tận Hải, mỗi đảo chỉ đủ chỗ cho vài chục hộ gia đình. Phần lớn là đảo đá thấp phủ rêu biển, một vài đảo có lớp đất mỏng đủ trồng rau và thảo dược cơ bản. Tài nguyên chính là hải sản — cá, tôm, rong biển — cùng gỗ trôi dạt từ đất liền và một ít linh thạch phẩm chất thấp khai thác từ rạn đá ngầm giữa các đảo. Giữa các đảo có hải lưu nguy hiểm khiến việc di chuyển phụ thuộc hoàn toàn vào thuyền nhỏ và kinh nghiệm lái thuyền qua nhiều đời. Nước ngọt là vấn đề nan giải nhất — cư dân phải hứng nước mưa bằng các bể đá tự nhiên và sử dụng pháp khí lọc muối thô sơ do Trần Hải Phong chế tạo, mỗi ngày chỉ lọc được lượng nước vừa đủ cho nhu cầu tối thiểu.

## III. Văn Hóa & Tín Ngưỡng (文化 与 信仰)
Cư dân liên minh tôn thờ Hải Mẫu — vị thần biển cổ đại mà ngư dân truyền miệng qua nhiều thế hệ, không rõ có thật hay chỉ là truyền thuyết. Mỗi đảo có phong tục riêng — đảo phía bắc kiêng ra biển vào ngày trăng mới, đảo phía nam có tục xăm hình cá lên cánh tay trẻ sơ sinh — nhưng tất cả đều chung một nguyên tắc sống: "Biển cho gì, nhận nấy." Hàng năm vào đêm rằm tháng mười, toàn liên minh tổ chức Lễ Phóng Đèn trên biển, thả hàng trăm chiếc đèn hoa đăng để tưởng nhớ những người đã mất vì sóng dữ. Đó là đêm duy nhất trong năm mà mười bảy đảo cùng thắp sáng, tạo nên cảnh tượng đẹp đến nao lòng giữa đại dương tối tăm. Người dân nơi đây sống giản dị, không coi trọng tu luyện mà đề cao sự đoàn kết và chia sẻ — một mẻ cá lớn luôn được chia đều cho mọi hộ trên đảo.

## IV. Cơ Cấu Tổ Chức (组织结构)
Liên minh hoạt động theo mô hình dân chủ thô sơ: mỗi đảo cử một đại diện tham gia Hội Đồng Đảo Chủ, cùng bầu ra Tổng Đảo Chủ để đại diện đối ngoại và quyết định các vấn đề chung. Trần Hải Phong được bầu làm Tổng Đảo Chủ nhờ là tu sĩ duy nhất đạt Kim Đan trong liên minh, đồng thời có kinh nghiệm từ thời làm đệ tử ngoại môn. Bên dưới Hội Đồng là Hải Tuần Đội — khoảng ba mươi ngư dân khỏe nhất luân phiên tuần tra vùng biển quanh đảo, trang bị thuyền nhỏ và lưới bẫy thô sơ. Thương Thuyền Đoàn gồm năm chiếc thuyền buôn dùng chung giữa các đảo, chở hải sản đổi lấy ngũ cốc, vải vóc và pháp khí cơ bản từ đất liền. Dân số khoảng năm trăm người rải rác trên mười bảy đảo, đại đa số là phàm nhân, chỉ có chưa đến mười người đạt Luyện Khí.

## V. Công Pháp & Trận Pháp (功法 与 阵法)
Phiêu Lưu Đảo Liên Minh không có công pháp chính thức nào. Toàn bộ "kho tàng tu luyện" chỉ là vài cuốn sách Luyện Khí cấp thấp đã bạc màu, truyền lại từ đời trước mà không rõ nguồn gốc, nội dung thiếu sót và có chỗ sai lệch. Trần Hải Phong đã cố gắng chỉnh sửa những cuốn sách này dựa trên kiến thức từ thời làm đệ tử ngoại môn, nhưng khả năng có hạn nên kết quả cũng không đáng kể. Trận pháp duy nhất của liên minh là Hải Triều Cảnh Giới Trận — một trận pháp cảnh báo đơn giản đặt quanh rìa quần đảo, phát sáng khi có sóng lớn bất thường hoặc hải thú cấp thấp đến gần. Trận pháp này do Trần Hải Phong dựng lên từ kiến thức cơ bản, dùng linh thạch phẩm chất thấp làm năng lượng, hiệu quả hạn chế nhưng đã nhiều lần cứu mạng ngư dân.

## VI. Đặc Sản Môn Phái (门派特产)
- **Hải Mẫu Đèn Hoa:** Đèn hoa đăng truyền thống làm từ vỏ ốc biển lớn, bên trong đặt lõi thảo dược phát sáng. Mỗi chiếc đèn có thể trôi trên mặt biển ba ngày đêm mà không tắt, tạo ra ánh sáng ấm áp dẫn đường cho thuyền đánh cá trong đêm tối. Không có giá trị tu luyện nhưng được thương nhân đất liền ưa chuộng làm vật trang trí.
- **Muối Linh:** Muối biển kết tinh tự nhiên tại các rạn đá ngầm giàu linh khí, có hàm lượng linh khí vi lượng giúp tăng cường thể chất phàm nhân. Là mặt hàng trao đổi chính của liên minh với đất liền, tuy phẩm chất không cao nhưng giá thành rẻ nên có thị trường ổn định.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Đảo Trung Tâm (Đảo số bảy):** Hòn đảo lớn nhất trong quần đảo, nơi Hội Đồng Đảo Chủ họp mặt và đặt kho lương thực chung. Có một bến thuyền nhỏ xây bằng đá san hô, đủ neo đậu năm thương thuyền và vài chục thuyền đánh cá.
- **Bể Lọc Nước:** Hệ thống bể đá tự nhiên trên mỗi đảo, kết hợp pháp khí lọc muối thô sơ do Trần Hải Phong chế tạo, cung cấp nước ngọt cho cư dân.
- **Hải Triều Đài:** Đỉnh đá cao nhất trên Đảo Trung Tâm, nơi đặt trận pháp cảnh báo và cũng là nơi canh gác, quan sát vùng biển xung quanh.

## VIII. Kinh Tế (经济)
Kinh tế của Phiêu Lưu Đảo Liên Minh hoàn toàn dựa vào ngư nghiệp và trao đổi hàng hóa quy mô nhỏ. Hải sản đánh bắt hàng ngày vừa phục vụ nhu cầu ăn uống, vừa được phơi khô làm hàng trao đổi. Thương Thuyền Đoàn thực hiện hai đến ba chuyến đi đất liền mỗi năm, mang theo cá khô, muối linh và ngọc trai nhỏ để đổi lấy ngũ cốc, thuốc men, vải vóc và linh thạch cấp thấp. Thu nhập eo hẹp còn bị cắt giảm thêm bởi "thuế bình an" phải nộp cho Hắc Hải Hải Tặc hàng năm — một gánh nặng khiến liên minh luôn trong tình trạng thiếu thốn. Mỏ linh thạch phẩm chất thấp tại rạn đá ngầm đang dần cạn kiệt, khiến tương lai kinh tế của liên minh càng thêm bấp bênh.

## IX. Lịch Sử Tóm Tắt (简史)
Phiêu Lưu Đảo Liên Minh hình thành tự nhiên khi các nhóm ngư dân phiêu bạt, bị bão cuốn ra khỏi đất liền, dần định cư trên quần đảo nhỏ gần bờ đông. Trong suốt nhiều thế kỷ, mỗi đảo tự quản lý cuộc sống riêng mà không có sự liên kết chính thức. Ba trăm năm trước, một trận bão khủng khiếp gần như xóa sổ ba hòn đảo, giết chết hàng chục người và phá hủy mọi thuyền bè. Sau thảm họa đó, các đảo còn lại nhận ra rằng nếu không đoàn kết, họ sẽ bị biển cả nuốt chửng từng đảo một. Liên minh chính thức ra đời, với nguyên tắc chia sẻ tài nguyên và bảo vệ lẫn nhau. Từ đó đến nay, liên minh đã trải qua nhiều lần bị Hắc Hải Hải Tặc cướp phá, mỗi lần đều mất mát nặng nề nhưng vẫn kiên cường gượng dậy.

## X. Giai Thoại & Bí Mật (轶事 与 秘密)
Có tin đồn rằng một trong các đảo ẩn chứa di tích cổ đại dưới lòng đất — có thể là phế tích của một thế lực đã biến mất từ thượng cổ — nhưng không ai trong liên minh đủ sức khai quật. Tổng Đảo Chủ Trần Hải Phong thực ra là cựu đệ tử ngoại môn của một tông môn trên đất liền, bị trục xuất vì tư chất tu luyện quá kém; ông giấu kín quá khứ này vì sợ mất uy tín trước dân đảo. Đảo thứ mười ba là nơi không có người ở và không ai dám đến gần — ngư dân nói rằng ban đêm từ lòng đảo vọng lên tiếng hát du dương nhưng ai nghe quá lâu sẽ bị mê muội, lao đầu xuống biển. Trần Hải Phong từng bí mật đến Đảo thứ mười ba một mình, sau đó trở về với vẻ mặt tái nhợt và cấm tuyệt đối mọi người tiếp cận, nhưng không giải thích lý do.

## XI. Quan Hệ Thế Lực (势力关系)
- **Đảo Quốc Tự Trị Hội:** Mối quan hệ thân thiện nhất của liên minh. Hai bên cùng là những cộng đồng nhỏ bé trên biển, thường xuyên hỗ trợ lẫn nhau khi bị tấn công, trao đổi lương thực và chia sẻ tin tức về tình hình hải tặc. Đây là liên minh tự nhiên giữa những kẻ yếu để cùng tồn tại.
- **Hắc Hải Hải Tặc:** Nỗi ám ảnh thường trực. Liên minh từng bị cướp phá nhiều lần, phải chấp nhận nộp "thuế bình an" hàng năm — một hình thức tống tiền trá hình mà họ không đủ sức chống lại. Mỗi lần thương thuyền ra khơi đều phải cầu nguyện không gặp phải hạm đội của Hắc Hải.
- **Hải Thần Cung:** Ngư dân kính trọng Hải Thần và thường cầu nguyện trước khi ra biển, nhưng Hải Thần Cung không hề biết đến sự tồn tại của liên minh nhỏ bé này, hoặc biết mà không quan tâm. Trần Hải Phong từng cố gắng gửi thỉnh nguyện xin bảo hộ nhưng không nhận được hồi đáp.
