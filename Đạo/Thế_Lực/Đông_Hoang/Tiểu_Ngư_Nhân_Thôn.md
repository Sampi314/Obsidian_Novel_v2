---
type: faction
name: Tiểu Ngư Nhân Thôn
hantu: 小鱼人村
faction_type: Bộ Lạc
alignment: 0
race: Ngư Nhân (Hải Tộc cấp thấp)
region: Đông Hoang
founded: Hàng nghìn năm trước (không rõ thời điểm chính xác)
founder: Không rõ (hình thành tự nhiên)
emblem: Tieu_Ngu_Nhan_Thon.png
specialty: Sóng âm liên lạc cấp thấp, Sinh tồn rạn san hô
economy:
- Bắt cá và hải sản cấp thấp
- Thu nhặt san hô chết và vỏ sò
arcs:
  - arc: 1
    status: Tồn tại bấp bênh
    rank: Không Xếp Hạng
    leader: Thôn Trưởng Lão Ngư Vĩ
    population: 100
    territory:
      - Rạn san hô Thất Sắc (vùng biển nông gần bờ đông)
    assets:
      - name: Làng San Hô
        type: Công Trình
      - name: Hang động phát sáng bí ẩn
        type: Bí Cảnh
    stats: [5, 10, 5, 100, 15, 5]
    divisions:
      - name: Toàn Thôn
        role: Sinh tồn, bắt cá và bảo vệ rạn san hô
        headcount:
          truong_lao: 1
          chien_binh: 10
          dan_thuong: 89
        members:
          - character: "[Lão Ngư Vĩ]"
            position: Thôn Trưởng
            cultivation: Luyện Khí (tương đương)
            placeholder: true
    relationships:
      - faction: Giao Nhân Bần Dân
        description: Từng bị Giao Nhân Tộc bắt làm nô lệ. Dù đã trốn thoát, ký ức kinh hoàng khiến Ngư Nhân sợ hãi mọi thứ liên quan đến Giao Nhân.
        diplomacy:
          lien_minh: -80
          tin: -90
          uy_hiep: 80
          thuong_mai: -100
          on_oan: -70
          le_thuoc: 0
      - faction: Triều Tịch Quan Trắc Đài
        description: Quan trắc viên của Đài đôi khi quan sát Ngư Nhân từ xa để nghiên cứu hải sinh. Ngư Nhân không biết họ đang bị quan sát.
        diplomacy:
          lien_minh: 0
          tin: 0
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 0
      - faction: Giáp Xác Liên Minh
        description: Đôi khi cạnh tranh nguồn thức ăn tại rạn san hô, nhưng cả hai đều quá yếu để xảy ra xung đột thực sự.
        diplomacy:
          lien_minh: -5
          tin: 0
          uy_hiep: 10
          thuong_mai: 0
          on_oan: -10
          le_thuoc: 0
---

# Tiểu Ngư Nhân Thôn (小鱼人村)

## I. Tổng Quan (总览)

Tiểu Ngư Nhân Thôn là một cộng đồng nhỏ bé gồm khoảng một trăm con Ngư Nhân — chủng tộc cấp thấp nhất trong Hải Tộc, sống quần tụ tại rạn san hô Thất Sắc ở vùng biển nông gần bờ đông Đông Hoang. Với hình dáng nửa người nửa cá và trí tuệ giản đơn, Ngư Nhân sống theo bản năng thuần túy: bắt cá, sinh sản, tránh kẻ thù lớn. Nhiều Hải Tộc cao cấp thậm chí không coi chúng là "người" mà chỉ xem như "cá biết đi". Tuy thân phận thấp kém và sức mạnh gần như không đáng kể, ngôi thôn nhỏ này lại ẩn chứa những bí ẩn khiến kẻ mạnh cũng phải tò mò — nếu họ biết về sự tồn tại của nó.

## II. Địa Lý & Tài Nguyên (地理与资源)

Ngôi làng nằm giữa rạn san hô Thất Sắc — một hệ thống san hô đa sắc màu trải dài trong vùng nước nông, ấm áp gần bờ biển phía đông. Nhà cửa được xây từ vỏ sò và san hô chết, tuy đơn sơ nhưng hòa lẫn hoàn hảo với môi trường xung quanh. Rạn san hô đóng vai trò lá chắn tự nhiên, ngăn cản hải thú lớn tiếp cận nhờ khe hẹp và cấu trúc phức tạp — đây là nơi trú ẩn tự nhiên duy nhất của Ngư Nhân. Vùng nước nông cung cấp nguồn cá nhỏ dồi dào nhưng không có gì có giá trị đối với tu sĩ. Linh khí cực thấp, tuy nhiên Ngư Nhân cấp thấp không cần nhiều linh khí để sống, nên điều này vô hình trung bảo vệ họ khỏi sự chú ý của các thế lực lớn.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)

Ngư Nhân có đời sống văn hóa cực kỳ nguyên thủy. Hoạt động chính xoay quanh ba bản năng: kiếm ăn, sinh tồn và sinh sản. Hệ thống giao tiếp dựa vào sóng âm cấp thấp và ngôn ngữ cơ thể đơn giản — chỉ Thôn Trưởng Lão Ngư Vĩ là biết nói vài câu tiếng người thô sơ. Tín ngưỡng duy nhất là thờ cúng "Đại Ngư" — con cá khổng lồ huyền thoại mà truyền thuyết kể rằng đã bảo vệ loài Ngư Nhân từ thuở hồng hoang. Mỗi khi có trăng tròn, cả thôn tập trung bơi thành vòng tròn và phát ra sóng âm đồng loạt để "gọi Đại Ngư", dù chưa bao giờ có phản hồi nào.

## IV. Cơ Cấu Tổ Chức (组织结构)

Cơ cấu tổ chức cực kỳ đơn giản, gần như theo bản năng bầy đàn.

- **Thôn Trưởng — Lão Ngư Vĩ:** Con Ngư Nhân già nhất còn sống, có vảy đã bạc trắng và đuôi dài nhất thôn. Là cá thể duy nhất biết nói vài câu tiếng người, được cả thôn kính trọng vì tuổi tác và kinh nghiệm.
- **Thợ Săn (10 con):** Mười con Ngư Nhân khỏe nhất, phụ trách bắt cá cho cả thôn. Chúng bơi nhanh nhất và có răng sắc nhất.
- **Dân Thường (khoảng 89 con):** Bao gồm Ngư Nhân trưởng thành yếu hơn, ấu trùng và những cá thể đang trong giai đoạn biến thái từ dạng cá sang dạng nửa người.

Đời sống đơn giản đến mức nhiều Hải Tộc cao cấp khi biết đến sự tồn tại của thôn này chỉ xem đó là một bầy cá có hình dạng kỳ quặc, không đáng để ý.

## V. Công Pháp & Trận Pháp (功法与阵法)

Ngư Nhân hoàn toàn không có công pháp — chúng tu luyện theo bản năng, hấp thu linh khí vi mô trong nước biển thông qua mang và vảy. Quá trình này chậm đến mức phải mất hàng trăm năm mới đạt được tu vi tương đương Luyện Khí sơ kỳ. Kỹ năng duy nhất đáng kể là khả năng phát ra sóng âm cấp thấp — dùng để liên lạc giữa các cá thể trong phạm vi rạn san hô và xua đuổi loài cá ăn thịt nhỏ. Đặc biệt, một số Ngư Nhân già tự nhiên mọc ra lớp vảy cứng hơn bình thường, có khả năng chống chịu va đập tốt hơn — có thể là dấu hiệu của một dạng tiến hóa chậm rãi đang diễn ra.

## VI. Đặc Sản Môn Phái (门派特产)

- **San Hô Thất Sắc:** Các mảnh san hô tự nhiên có bảy màu sắc rực rỡ, tuy không có giá trị tu luyện nhưng được một số nhân tộc ven biển ưa chuộng làm đồ trang trí. Ngư Nhân không biết giá trị thương mại của chúng.
- **Mực Ngư Nhân:** Một loại mực đặc biệt mà Ngư Nhân tiết ra khi hoảng sợ, có tác dụng gây mù tạm thời cho kẻ săn mồi. Thành phần hóa học độc đáo, có thể hữu ích cho dược sư nếu ai đó buồn thu thập.
- **Sóng Âm Đồng Loạt:** Khi cả thôn cùng phát sóng âm, tạo ra một dao động tần số thấp có thể làm chóng mặt các sinh vật cỡ trung trong bán kính nhỏ — thứ vũ khí phòng vệ bản năng duy nhất.

## VII. Cơ Sở Hạ Tầng (基础设施)

- **Làng San Hô:** Khoảng 30 "ngôi nhà" xây từ vỏ sò và san hô chết xếp chồng, mỗi nhà đủ chỗ cho 3-4 Ngư Nhân. Không có cửa — chỉ là các khoang trống trong rạn san hô.
- **Bãi Ấp Trứng:** Khu vực cát mịn ấm áp ở trung tâm rạn san hô, nơi Ngư Nhân đặt trứng và ấu trùng phát triển.
- **Hang Động Phát Sáng:** Một hang động nhỏ nằm sâu trong rạn san hô, phát ra ánh sáng lạ bí ẩn. Ngư Nhân không dám vào vì sợ, nhưng đó rất có thể là mảnh vỡ pháp bảo cổ đại chìm dưới đáy biển từ thượng cổ.

## VIII. Kinh Tế (经济)

Tiểu Ngư Nhân Thôn không có khái niệm kinh tế theo nghĩa truyền thống. Mọi hoạt động đều xoay quanh việc sinh tồn: Thợ Săn bắt cá mang về chia cho cả thôn, san hô chết và vỏ sò được thu nhặt để xây dựng và sửa chữa nhà cửa. Không có giao thương, không có tiền tệ, không có khái niệm sở hữu cá nhân. Mọi thứ thuộc về cả thôn và được phân phối theo nhu cầu cơ bản. Đây là nền kinh tế nguyên thủy nhất trong tất cả các thế lực được ghi nhận tại Đông Hoang.

## IX. Lịch Sử Tóm Tắt (简史)

Thôn đã tồn tại hàng nghìn năm, nhưng không có sự kiện lịch sử đáng kể nào được ghi nhận — bản thân Ngư Nhân cũng không có khả năng ghi chép lịch sử. Sự kiện đau thương nhất trong ký ức tập thể là thời kỳ bị Giao Nhân Tộc bắt làm nô lệ, ép khai thác ngọc trai và san hô dưới đáy biển sâu. Sau khi trốn thoát trong một trận hải triều lớn, Ngư Nhân ẩn náu trong rạn san hô Thất Sắc và không bao giờ dám rời đi xa. Đôi khi, ngư dân nhân tộc vô tình kéo lưới bắt được Ngư Nhân, khiến cả thôn hoảng loạn mấy ngày trời. Gần đây, sự xuất hiện của một con Ngư Nhân trẻ có linh trí cao bất thường đang tạo ra những thay đổi tiềm ẩn trong cộng đồng nhỏ bé này.

## X. Giai Thoại & Bí Mật (轶事与秘密)

- Lão Ngư Vĩ là con Ngư Nhân duy nhất từng nhìn thấy Hải Thần Cung — nhưng vì ngôn ngữ hạn chế, lão không thể diễn tả chính xác những gì mình đã thấy. Lão chỉ có thể lặp đi lặp lại từ "sáng... lớn... sáng..." khi cố kể lại.
- Trong rạn san hô có một hang động nhỏ phát ra ánh sáng kỳ lạ. Ngư Nhân không dám vào vì bản năng cảnh báo nguy hiểm, nhưng ánh sáng đó rất có thể đến từ mảnh vỡ của một pháp bảo cổ đại — nếu bị phát hiện bởi tu sĩ, nó có thể thay đổi vận mệnh của cả thôn, theo cả nghĩa tốt lẫn xấu.
- Gần đây xuất hiện một con Ngư Nhân trẻ biết vẽ hình trên cát — dấu hiệu linh trí cao bất thường cho loài này. Nếu cá thể này tiếp tục phát triển, nó có thể trở thành Ngư Nhân đầu tiên trong lịch sử đạt được trí tuệ ngang tầm nhân tộc.

## XI. Quan Hệ Thế Lực (势力关系)

- **Giao Nhân Tộc (bao gồm Giao Nhân Bần Dân):** Ký ức kinh hoàng về thời kỳ nô lệ khiến Ngư Nhân sợ hãi tất cả những gì liên quan đến Giao Nhân. Dù Giao Nhân Bần Dân cũng chỉ là tầng lớp thấp kém, Ngư Nhân vẫn tránh xa bằng mọi giá.
- **Triều Tịch Quan Trắc Đài:** Quan trắc viên đôi khi quan sát Ngư Nhân từ xa như một phần nghiên cứu hải sinh. Ngư Nhân hoàn toàn không biết mình đang bị quan sát.
- **Giáp Xác Liên Minh:** Đôi khi cạnh tranh nguồn cá nhỏ trong rạn san hô, nhưng xung đột chỉ ở mức xua đuổi lẫn nhau, cả hai đều quá yếu để gây ra tổn thương thực sự.
