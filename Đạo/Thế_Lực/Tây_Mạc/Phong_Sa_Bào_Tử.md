---
type: faction
name: Phong Sa Bào Tử
hantu: 风沙孢子
faction_type: Liên Minh
alignment: 0
race: Vi Tộc (Bào Tử loại)
region: Tây Mạc
founded: Tự nhiên (Tồn tại song hành cùng bão cát Tây Mạc)
founder: Không có (Hình thành tự nhiên)
emblem: Phong_Sa_Bao_Tu.png
specialty: Hấp thu khoáng linh vi mô, Phát sáng tín hiệu, Dự báo hướng gió
economy:
- Không có hoạt động kinh tế chủ động
- Khoáng linh vi mô bị thu gom bởi đan sư
arcs:
  - arc: 1
    status: Tồn tại ổn định (Trôi nổi cùng bão cát)
    rank: Không Xếp Hạng
    leader: Bào Tử Vương (Bản năng điều phối)
    population: 10
    territory:
      - Hoàng Kim Sa Hải (Bất kỳ nơi nào có bão cát)
    assets:
      - name: Bào Tử Vương
        type: Sinh Vật
      - name: Khoáng linh vi mô
        type: Tài Nguyên
    stats: [5, 20, 5, 10, 10, 15]
    divisions:
      - name: Đoàn Bào Tử
        role: Bay cùng bão cát, thu khoáng linh vi mô, phân phối tập thể
        headcount:
          truong_lao: 1
          chien_binh: 0
          dan_thuong: 9
        members:
          - character: "[Bào Tử Vương]"
            position: Cá thể lớn nhất (Điều phối đoàn)
            cultivation: Luyện Khí (Tương đương)
            placeholder: true
    relationships:
      - faction: Sa Mạc Hướng Đạo Hội
        description: Hướng Đạo Hội là số ít biết về Bào Tử, sử dụng vệt sáng sau bão để xác định hướng gió và dự báo thời tiết.
        diplomacy:
          lien_minh: 0
          tin: 10
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 10
          le_thuoc: 0
      - faction: Phế Khí Luyện Đan Phường
        description: Từng thu gom Bào Tử rơi sau bão, phát hiện chứa khoáng linh tinh khiết nhưng lượng quá ít để sử dụng thương mại.
        diplomacy:
          lien_minh: 0
          tin: 0
          uy_hiep: 0
          thuong_mai: 10
          on_oan: 0
          le_thuoc: 0
      - faction: Linh Sa Khuẩn Đoàn
        description: Cùng là Vi Tộc trong Hoàng Kim Sa Hải nhưng không tương tác. Khuẩn Đoàn sống dưới đất, Bào Tử sống trên không — hai hệ sinh thái song song.
        diplomacy:
          lien_minh: 0
          tin: 0
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 0
---

# Phong Sa Bào Tử (风沙孢子)

## I. Tổng Quan (总览)
Phong Sa Bào Tử là Vi Tộc cổ xưa sống lơ lửng trong các trận bão cát của Hoàng Kim Sa Hải — chủng tộc duy nhất trong toàn Tây Mạc sinh tồn trên không trung thay vì dưới đất hay trong nước. Mỗi đoàn gồm hàng triệu bào tử bay cùng nhau như một đám mây sống, hấp thu khoáng linh vi mô phân tán trong bão cát mà không sinh vật nào khác có khả năng thu thập. Dưới sự điều phối của Bào Tử Vương — cá thể lớn nhất, to bằng hạt gạo — đoàn bào tử hoạt động hoàn toàn tập thể, giao tiếp bằng ánh sáng và sống chết cùng bão. Rất ít chủng tộc biết đến sự tồn tại của chúng, và đối với phần lớn cư dân sa mạc, vệt sáng nhạt trên cát sau bão chỉ là hiện tượng tự nhiên bình thường.

## II. Địa Lý & Tài Nguyên (地理与资源)
Phong Sa Bào Tử xuất hiện ở bất kỳ nơi nào có bão cát trong Hoàng Kim Sa Hải, không có lãnh địa cố định. Khi bão hoạt động, chúng bay lơ lửng trong tầng không khí cao nhất của cơn bão, hấp thu khoáng linh vi mô — những hạt khoáng chất siêu nhỏ mà mắt thường không thấy nhưng chứa linh lực thuần khiết. Khi bão tạnh, toàn bộ đoàn "rơi" xuống cát cùng nhau, tạo thành vệt sáng nhạt lung linh trên mặt sa mạc — đây là khoảnh khắc duy nhất có thể quan sát được sự tồn tại của chúng. Khoáng linh vi mô là tài nguyên bẩm sinh của Bào Tử, tinh khiết đến mức đan sư phải kinh ngạc, nhưng lượng thu được từ mỗi đoàn quá ít để khai thác thương mại.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
Triết lý sinh tồn của Bào Tử đơn giản đến thuần khiết: "Gió đưa đi đâu — đi đó. Bão cho gì — nhận đó." Chúng không chống lại gió, không chọn hướng, hoàn toàn thuận theo bão cát để di chuyển. Khi bão tạnh và đoàn rơi xuống, tất cả cùng nghỉ ngơi trong im lặng trước khi cơn bão tiếp theo nâng chúng lên lại. Giao tiếp bằng phương thức phát sáng theo nhịp điệu — mỗi tần số ánh sáng mang một ý nghĩa khác nhau, tạo nên một ngôn ngữ ánh sáng tinh tế mà không loài nào khác giải mã được. Không có phân chia vai trò — tất cả cùng bay, cùng thu khoáng linh, cùng phân phối đều cho nhau.

## IV. Cơ Cấu Tổ Chức (组织结构)
Cơ cấu của Bào Tử cực kỳ đơn giản và bình đẳng tuyệt đối. Bào Tử Vương là cá thể lớn nhất trong đoàn, to bằng hạt gạo trong khi các cá thể khác nhỏ như hạt bụi, phát tín hiệu ánh sáng mạnh nhất để điều phối toàn đoàn bay theo cùng hướng và tập trung hấp thu khoáng linh. Hàng triệu bào tử còn lại hành động tập thể, không có phân chia nhóm hay nhiệm vụ riêng biệt. Khi Bào Tử Vương chết, cá thể lớn thứ hai tự động thay thế mà không có bất kỳ tranh chấp hay nghi thức nào — quá trình chuyển giao diễn ra trong tích tắc, hoàn toàn theo bản năng.

## V. Công Pháp & Trận Pháp (功法与阵法)
Bào Tử không tu luyện — khả năng hấp thu khoáng linh vi mô là bẩm sinh, một phần của chu kỳ sinh tồn tự nhiên. Khi bị đe dọa bởi yêu thú hay sinh vật khác, toàn đoàn đồng loạt phát sáng chói lòa, tạo ra hiệu ứng "linh quang bạo phát" làm lóa mắt và nhiễu thần thức kẻ tấn công trong khoảnh khắc — đủ để đoàn tản mát và thoát thân theo gió. Ngoài ra, khi đoàn rơi xuống cát sau bão, chúng tạo ra hiện tượng "mưa linh quang" — hàng triệu điểm sáng nhỏ li ti rơi xuống như mưa sao, vô cùng đẹp mắt nhưng hoàn toàn vô hại. Đây là cảnh tượng mà rất ít người từng chứng kiến.

## VI. Đặc Sản Môn Phái (门派特产)
- **Khoáng Linh Vi Mô:** Hạt khoáng chất siêu nhỏ chứa linh lực thuần khiết đặc biệt, do Bào Tử hấp thu từ bão cát và tích lũy trong cơ thể. Tinh khiết hơn bất kỳ loại linh thạch nào, nhưng lượng thu được từ mỗi đoàn cực kỳ ít, khiến việc khai thác thương mại gần như bất khả thi.
- **Vệt Sáng Bào Tử:** Dấu vết lung linh trên cát sau khi đoàn Bào Tử rơi xuống, chứa một lượng nhỏ khoáng linh. Sa Mạc Hướng Đạo Hội sử dụng vệt sáng này như la bàn tự nhiên để xác định hướng gió chủ đạo.

## VII. Cơ Sở Hạ Tầng (基础设施)
Phong Sa Bào Tử không xây dựng bất kỳ cơ sở hạ tầng nào — chúng là sinh vật trôi nổi hoàn toàn, sống và chết trong không trung. Khi bão hoạt động, không gian bên trong cơn bão chính là "nhà" của chúng. Khi bão tạnh, mặt cát nơi đoàn rơi xuống tạm thời trở thành nơi nghỉ ngơi — nhưng không bao giờ cố định vì bão tiếp theo sẽ nâng chúng lên lại. Điều đáng chú ý là những khu vực Bào Tử thường xuyên rơi xuống có nồng độ khoáng linh trong cát cao hơn bình thường, vô tình tạo ra những "điểm phì nhiêu" giữa lòng sa mạc mà không ai giải thích được nguồn gốc.

## VIII. Kinh Tế (经济)
Bào Tử không có khái niệm kinh tế hay giao dịch. Giá trị kinh tế gián tiếp của chúng nằm ở khoáng linh vi mô — Phế Khí Luyện Đan Phường từng thu gom Bào Tử rơi trên cát sau bão và phát hiện chúng chứa khoáng linh tinh khiết đặc biệt, nhưng lượng quá ít để sử dụng thương mại nên đã ngừng thu gom. Ngoài ra, vệt sáng của Bào Tử có giá trị gián tiếp với Sa Mạc Hướng Đạo Hội như một công cụ dự báo thời tiết và xác định hướng gió — thứ mà không pháp khí nào có thể thay thế.

## IX. Lịch Sử Tóm Tắt (简史)
Phong Sa Bào Tử tồn tại từ thời cổ đại, song hành cùng các trận bão cát đầu tiên của Tây Mạc. Chúng không có lịch sử theo nghĩa thông thường — không có sự kiện trọng đại, không có biến cố, chỉ có chu kỳ bất tận của bay lên và rơi xuống. Rất ít chủng tộc từng nhận ra sự tồn tại của chúng. Sa Mạc Hướng Đạo Hội là thế lực đầu tiên ghi nhận Bào Tử như một hiện tượng tự nhiên có quy luật, và học cách đọc vệt sáng của chúng để xác định hướng gió. Ngoài ra, Bào Tử tồn tại trong im lặng, không gây ảnh hưởng và cũng không bị ảnh hưởng bởi bất kỳ cuộc chiến hay biến cố nào trên sa mạc.

## X. Giai Thoại & Bí Mật (轶事与秘密)
- Phế Khí Luyện Đan Phường từng thu gom Bào Tử rơi trên cát sau bão — phát hiện chúng chứa khoáng linh tinh khiết vượt xa linh thạch thông thường, nhưng lượng quá ít để sử dụng thương mại. Một số đan sư vẫn lặng lẽ tìm kiếm vệt sáng Bào Tử sau mỗi trận bão lớn.
- Có lần một trận bão khổng lồ đưa một đoàn Bào Tử đến tận rìa Vĩnh Tịch Chi Địa — toàn bộ đoàn chết sạch trong khoảnh khắc, chỉ Bào Tử Vương sống sót nhưng từ đó phát sáng đen thay vì trắng. Bào Tử Vương đen đó giờ bay một mình, không theo bão nào nữa, lang thang như bóng ma giữa sa mạc.
- Sa Mạc Hướng Đạo Hội gọi Bào Tử Vương đen là "Hắc Tinh" và coi mỗi lần nhìn thấy nó là điềm xấu — nơi nào Hắc Tinh xuất hiện, bão cát bất thường sẽ đến trong vòng ba ngày. Phong Sa Lão Nhân từng cố theo dõi Hắc Tinh nhưng nó biến mất mỗi khi có người đến gần.

## XI. Quan Hệ Thế Lực (势力关系)
- **Sa Mạc Hướng Đạo Hội:** Thế lực duy nhất nhận ra và ghi nhận Bào Tử như hiện tượng tự nhiên có quy luật. Hướng đạo sử dụng vệt sáng Bào Tử để dự báo hướng gió và cảnh báo bão cát, biến sự tồn tại vô hình của Bào Tử thành công cụ sinh tồn thực tế.
- **Phế Khí Luyện Đan Phường:** Từng nghiên cứu Bào Tử vì khoáng linh tinh khiết, nhưng đã ngừng thu gom do lượng quá ít. Vẫn coi Bào Tử là đề tài nghiên cứu tiềm năng.
- **Linh Sa Khuẩn Đoàn:** Cùng là Vi Tộc cổ đại trong Hoàng Kim Sa Hải nhưng chiếm hai hệ sinh thái hoàn toàn khác biệt — Khuẩn Đoàn dưới đất, Bào Tử trên không — không tương tác và không cạnh tranh.
