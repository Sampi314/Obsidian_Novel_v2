---
type: faction
name: Thủy Mẫu Trùng Đàn
hantu: 水母蟲團
faction_type: Bộ Lạc
alignment: 2
race: Trùng Tộc (Sứa Linh)
region: Vô Tận Hải
founded: Thượng Cổ — tồn tại từ khi có biển
founder: Không rõ — tiến hóa tự nhiên
emblem: Sua_Linh_Phat_Quang.png
specialty: Phát quang đa sắc, dự báo thiên tai, linh độc nhẹ trong xúc tu
economy:
  - Không có hoạt động kinh tế chủ động
  - Dịch phát quang bị khai thác bởi các thế lực bên ngoài
arcs:
  - arc: 1
    status: Du cư theo hải lưu
    rank: Không Xếp Hạng
    leader: Đàn Mẫu Nguyệt Quang (tương đương Trúc Cơ)
    population: 100000
    territory:
      - Tầng nước giữa phía bắc Vô Tận Hải (di động)
    assets:
      - name: Dịch Phát Quang Sứa Linh
        type: Tài Nguyên
      - name: Rừng Đèn Lồng di động
        type: Bí Cảnh
    stats: [15, 10, 20, 40, 10, 15]
    divisions:
      - name: Đàn Mẫu
        role: Lãnh đạo đàn, quyết định hướng di chuyển, bảo vệ ấu trùng
        headcount:
          truong_lao: 1
          chien_binh: 0
          dan_thuong: 0
        members:
          - character: Nguyệt Quang
            position: Đàn Mẫu
            cultivation: Tương đương Trúc Cơ
      - name: Sứa Linh Trưởng Thành
        role: Lực lượng chính của đàn, phát quang và bảo vệ khu vực
        headcount:
          truong_lao: 0
          chien_binh: 50000
          dan_thuong: 0
        members:
          - character: "[Sứa Linh cá thể]"
            position: Thành viên đàn
            cultivation: Vô cảnh giới (bản năng)
            placeholder: true
      - name: Ấu Trùng
        role: Thế hệ kế tiếp, kích thước bằng hạt gạo, phát sáng yếu ớt
        headcount:
          truong_lao: 0
          chien_binh: 0
          dan_thuong: 50000
        members:
          - character: "[Ấu trùng sứa linh]"
            position: Cá thể non
            cultivation: Không
            placeholder: true
    relationships:
      - faction: Hải Thần Cung
        description: Quan hệ tiêu cực — Hải Thần Cung từng bắt sứa linh số lượng lớn để chiết xuất dịch phát quang làm đèn cung điện. Nguyệt Quang dẫn đàn tránh xa vùng biển gần Hải Thần Cung kể từ đó.
        diplomacy:
          lien_minh: -30
          tin: -50
          uy_hiep: 40
          thuong_mai: -20
          on_oan: -40
          le_thuoc: 0
      - faction: Lưu Vong Thuyền Đội
        description: Quan hệ tốt — Lưu Vong Thuyền Đội từng đi theo đàn sứa linh trong một đêm bão và nhờ vậy tránh được xoáy nước chết người. Từ đó, thuyền đội coi sứa linh là điềm lành.
        diplomacy:
          lien_minh: 20
          tin: 30
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 20
          le_thuoc: 0
      - faction: Kình Ngư Bộ Lạc
        description: Trung lập — sứa linh đôi khi trôi qua lãnh thổ Kình Ngư Bộ Lạc, hai bên không xung đột nhưng cũng không hợp tác.
        diplomacy:
          lien_minh: 5
          tin: 10
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 0
---

# Thủy Mẫu Trùng Đàn (水母蟲團)

## I. Tổng Quan (总览)

Thủy Mẫu Trùng Đàn là một đàn sứa linh khổng lồ trôi nổi trong lòng Vô Tận Hải, gồm hàng vạn cá thể phát quang đa sắc tạo thành cảnh tượng mà nhiều Hải Tộc gọi là "rừng đèn lồng giữa biển tối." Đàn Mẫu Nguyệt Quang — sứa linh lớn nhất với đường kính ba trượng, phát sáng bạc rực rỡ — dẫn dắt toàn bộ đàn di chuyển theo hải lưu, không chiếm giữ lãnh thổ cố định. Đây không phải thế lực theo nghĩa chính trị, mà là một hệ sinh thái di động: sứa linh đóng vai trò dẫn đường cho sinh vật biển di cư, đánh dấu vùng nước an toàn, và thậm chí được tin là có khả năng dự báo thiên tai. Tuy không xếp hạng trong bất kỳ bảng xếp hạng thế lực nào, sự tồn tại của chúng ảnh hưởng sâu rộng đến hệ sinh thái và tín ngưỡng dân gian của cả vùng biển.

## II. Địa Lý & Tài Nguyên (地理 与 资源)

Thủy Mẫu Trùng Đàn sinh sống ở tầng nước giữa — không quá sâu để áp suất nghiền nát, không quá nông để bị tàu thuyền quấy nhiễu. Đàn sứa linh không cố định ở một vị trí mà trôi nổi theo hải lưu, xuất hiện ở nhiều vùng biển khác nhau trong suốt chu kỳ di cư hàng năm. Nơi đàn sứa trôi qua, nước biển ấm lên nhẹ vì năng lượng phát quang tỏa nhiệt, tạo thành dấu hiệu nhận biết cho ngư dân và hải tộc. Ánh sáng đa sắc từ hàng vạn cá thể biến vùng biển tối đen thành một "khu rừng đèn lồng" lung linh, thu hút các loài sinh vật biển nhỏ đến kiếm ăn. Tài nguyên chính của đàn là dịch phát quang — chất lỏng quý giá trong cơ thể sứa linh, được nhiều thế lực thèm muốn để làm đèn chiếu sáng và luyện đan.

## III. Văn Hóa & Tín Ngưỡng (文化 与 信仰)

Sứa linh thuộc Trùng Tộc biển — sinh vật thân mềm, trong suốt, phát quang theo bản năng. Chúng không có ngôn ngữ hay văn hóa theo nghĩa thông thường, nhưng hành vi tập thể của đàn mang tính "nghi lễ" đáng kinh ngạc. Khi tập hợp đông đủ, ánh sáng từ hàng vạn cá thể đồng bộ nhịp nhàng — nhấp nháy cùng tần số, chuyển màu theo chu kỳ — nhiều Hải Tộc coi đây là "vũ điệu thiên giới" và tin rằng sứa linh đang giao tiếp với thần linh biển cả. Trong tín ngưỡng dân gian của ngư dân, sứa linh là điềm lành: nơi nào đàn sứa trôi qua, nơi đó biển yên sóng lặng và cá tôm dồi dào. Vai trò sinh thái thực sự của chúng là dẫn đường cho sinh vật biển di cư và đánh dấu vùng nước an toàn — tránh xa những nơi có hải lưu chết hoặc xoáy nước ngầm.

## IV. Cơ Cấu Tổ Chức (组织结构)

Cơ cấu của Thủy Mẫu Trùng Đàn hoàn toàn dựa trên bản năng sinh học, không có hệ thống chỉ huy nhân tạo. Đàn Mẫu Nguyệt Quang là cá thể lớn nhất và lâu đời nhất, với đường kính ba trượng và khả năng phát sáng bạc rực rỡ nhất đàn. Nguyệt Quang quyết định hướng di chuyển của toàn đàn bằng cách thay đổi nhịp phát sáng — khi Mẫu chuyển hướng, toàn bộ sứa linh trưởng thành theo sau theo bản năng. Bên dưới Mẫu là hàng vạn sứa linh trưởng thành, kích thước từ nắm tay đến chiếc thuyền nhỏ, tạo thành lực lượng chính của đàn. Cuối cùng là hàng triệu ấu trùng bằng hạt gạo, phát sáng yếu ớt, trôi nổi trong vùng bảo vệ ở trung tâm đàn nơi mật độ sứa trưởng thành cao nhất.

## V. Công Pháp & Trận Pháp (功法 与 阵法)

Thủy Mẫu Trùng Đàn không tu luyện công pháp — mọi khả năng đều là bản năng tự nhiên được mài giũa qua hàng vạn năm tiến hóa. Phát quang là đặc tính nổi bật nhất: mỗi cá thể sứa linh phát ra ánh sáng với màu sắc và cường độ riêng, khi kết hợp tạo thành dải quang phổ đa sắc mê hoặc. Xúc tu sứa linh chứa **linh độc nhẹ** — đủ sức tê liệt sinh vật Luyện Khí trong vài canh giờ, nhưng vô hại với tu sĩ Trúc Cơ trở lên. Đây là cơ chế phòng thủ thụ động: hải thú ăn sứa linh sẽ bị đau bụng nhiều ngày, học được bài học để không tái phạm. Khả năng đáng sợ nhất là khi cả đàn đồng loạt phát sáng cực đại — hiện tượng "Bạch Quang Bão" tạo ra luồng ánh sáng chói lòa có thể gây ảo giác, mất phương hướng và thậm chí hôn mê tạm thời cho bất kỳ sinh vật nào nhìn trực tiếp.

## VI. Đặc Sản Môn Phái (门派特产)

- **Dịch Phát Quang Sứa Linh:** Chất lỏng phát sáng chiết xuất từ cơ thể sứa linh, dùng làm đèn chiếu sáng trong cung điện dưới biển. Hải Thần Cung từng thu thập số lượng lớn, gây ra xung đột với đàn. Dịch này cũng là nguyên liệu quý trong luyện đan — một số đan dược chiếu sáng và dẫn đường sử dụng nó làm chủ dược.
- **Xúc Tu Sứa Linh Khô:** Xúc tu phơi khô chứa linh độc nhẹ, được đan dược sư dùng làm phụ liệu trong thuốc tê và thuốc giảm đau. Giá không cao nhưng nhu cầu ổn định.
- **Nguyệt Quang Tinh:** Cực kỳ hiếm — tinh thể kết tinh từ dịch phát quang của chính Đàn Mẫu Nguyệt Quang, phát sáng bạc vĩnh cửu. Chỉ xuất hiện khi Nguyệt Quang lột xác, khoảng mỗi trăm năm một lần.

## VII. Cơ Sở Hạ Tầng (基础设施)

Thủy Mẫu Trùng Đàn không có cơ sở hạ tầng cố định — toàn bộ "lãnh thổ" của chúng là vùng nước mà đàn đang chiếm giữ tại bất kỳ thời điểm nào. Cấu trúc duy nhất là đội hình di chuyển tự nhiên: Đàn Mẫu Nguyệt Quang ở trung tâm phía trước, sứa linh trưởng thành lớn nhất bao quanh tạo thành "vòng bảo vệ ngoài", ấu trùng nằm trong lõi an toàn giữa đàn. Khi dừng lại nghỉ ngơi, đàn sứa tự động dàn thành hình cầu, xúc tu hướng ra ngoài như một "pháo đài sống" — bất kỳ sinh vật nào xâm nhập đều bị hàng nghìn xúc tu chứa linh độc quấn lấy. Vùng nước bên trong "pháo đài" ấm hơn vùng nước xung quanh vài độ, tạo môi trường lý tưởng cho ấu trùng phát triển.

## VIII. Kinh Tế (经济)

Thủy Mẫu Trùng Đàn không có hoạt động kinh tế chủ động — chúng không sản xuất, không giao thương, không tích lũy. Tuy nhiên, cơ thể sứa linh chứa dịch phát quang quý giá, khiến chúng trở thành "nguồn tài nguyên sống" bị nhiều thế lực khai thác. Hải Thần Cung từng tổ chức chiến dịch bắt sứa linh quy mô lớn để chiết xuất dịch phát quang trang trí cung điện. Các đan dược sư và thương nhân cũng thu mua xúc tu sứa linh khô làm nguyên liệu luyện đan. Sứa linh không phản kháng một cách có tổ chức — phản ứng duy nhất của Nguyệt Quang là dẫn đàn di chuyển tránh xa vùng nguy hiểm. Điều này khiến đàn sứa dần bị đẩy ra những vùng biển xa xôi hơn, ảnh hưởng đến hệ sinh thái nơi chúng từng cư trú.

## IX. Lịch Sử Tóm Tắt (简史)

Sứa linh đã tồn tại trong Vô Tận Hải từ thời thượng cổ — ngư dân thế hệ này sang thế hệ khác đều nhắc đến "những ngọn đèn lồng dưới biển" như một phần không thể thiếu của đại dương. Trong suốt lịch sử, đàn sứa vẫn trôi nổi theo hải lưu, không can dự vào chiến tranh hay chính trị của các thế lực biển. Sự kiện đáng nhớ nhất là chiến dịch bắt sứa quy mô lớn của Hải Thần Cung cách đây khoảng ba trăm năm, khi hàng nghìn sứa linh bị bắt để chiết xuất dịch phát quang dùng làm đèn trong cung điện. Đàn mất gần một phần tư số lượng, và Nguyệt Quang — hoặc Đàn Mẫu thời đó — dẫn toàn bộ đàn tránh xa vùng biển gần Hải Thần Cung. Kể từ đó, đàn sứa chủ yếu di chuyển ở vùng biển phía bắc, nơi ít thế lực lớn kiểm soát. Sứa linh nhỏ đôi khi vẫn bị hải thú ăn, nhưng linh độc trong xúc tu khiến kẻ ăn đau bụng nhiều ngày, đủ để hầu hết hải thú học cách tránh xa.

## X. Giai Thoại & Bí Mật (轶事 与 秘密)

Nguyệt Quang phát sáng bạc vào ban đêm nhưng chuyển sang đỏ thẫm vào ngày trăng tròn — không ai giải thích được hiện tượng này, kể cả các học giả chuyên nghiên cứu Trùng Tộc biển. Một số người tin rằng ánh sáng đỏ thẫm là dấu hiệu Nguyệt Quang đang "giao tiếp" với mặt trăng, nhưng đây có lẽ chỉ là mê tín. Có truyền thuyết rằng đàn sứa linh biết trước thiên tai — mỗi khi toàn bộ đàn đồng loạt di chuyển về một hướng, bão lớn sẽ đến từ hướng ngược lại. Truyền thuyết này đã được xác nhận nhiều lần bởi ngư dân và thủy thủ, khiến nhiều thương thuyền chọn đi theo hướng đàn sứa khi thấy chúng di chuyển bất thường. Lưu Vong Thuyền Đội từng cứu được cả đoàn nhờ đi theo đàn sứa linh trong một đêm bão, tránh được xoáy nước chết người mà không tàu nào phát hiện bằng mắt thường.

## XI. Quan Hệ Thế Lực (势力关系)

- **Hải Thần Cung:** Quan hệ tiêu cực. Chiến dịch bắt sứa linh quy mô lớn cách đây ba trăm năm khiến đàn mất gần một phần tư số lượng. Nguyệt Quang dẫn đàn tránh xa vùng biển Hải Thần Cung và chưa bao giờ quay lại.
- **Lưu Vong Thuyền Đội:** Quan hệ tốt một chiều. Thuyền đội coi sứa linh là điềm lành và không bao giờ làm hại chúng. Sứa linh không nhận thức được mối quan hệ này nhưng cũng không coi thuyền đội là mối đe dọa.
- **Kình Ngư Bộ Lạc:** Trung lập. Đàn sứa đôi khi trôi qua lãnh thổ Kình Ngư, hai bên cùng tồn tại mà không can thiệp lẫn nhau. Kình ngư quá lớn để bị linh độc sứa ảnh hưởng, và sứa linh không có gì Kình Ngư cần.
