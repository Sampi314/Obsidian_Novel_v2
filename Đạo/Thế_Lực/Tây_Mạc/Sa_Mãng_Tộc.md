---
type: faction
name: Sa Mãng Tộc
hantu: 沙蟒族
faction_type: Bộ Lạc
alignment: -2
race: Yêu Tộc (Sa Mãng)
region: Tây Mạc
founded: Thượng Cổ (Tồn tại từ lâu đời)
founder: Không rõ (Bẩm sinh từ sa mạc)
emblem: Sa_Mang_Den_Cuon_Tron.png
specialty: Sa Độn Thuật, Nọc độc tê liệt, Phục kích từ dưới cát
economy:
  - Trao đổi nọc độc lấy thực phẩm (bí mật)
  - Săn bắt yêu thú nhỏ trong hang ngầm
  - Thu lượm trứng sa mãng có dược tính
arcs:
  - arc: 1
    status: Ẩn náu (Sống kín đáo dưới cát)
    rank: Hạng Năm
    leader: Tộc Trưởng Huyền Sa
    population: 200
    territory:
      - Hệ thống hang ngầm dưới Hoàng Kim Sa Hải
    assets:
      - name: Bộ xương Mãng cổ đại
        type: Di Tích
      - name: Nọc độc Sa Mãng
        type: Tài Nguyên
    stats: [80, 40, 10, 200, 60, 15]
    divisions:
      - name: Đàn Chính
        role: Toàn bộ quần thể Sa Mãng sống trong hang ngầm, săn mồi và bảo vệ lãnh thổ
        headcount:
          truong_lao: 3
          chien_binh: 10
          dan_thuong: 187
        members:
          - character: Huyền Sa
            position: Tộc Trưởng
            cultivation: Trúc Cơ Hậu Kỳ (tương đương)
          - character: "[Trưởng Lão Sa Mãng Xám]"
            position: Trưởng Lão
            cultivation: Trúc Cơ Sơ Kỳ (tương đương)
            placeholder: true
          - character: "[Trưởng Lão Sa Mãng Đỏ]"
            position: Trưởng Lão
            cultivation: Trúc Cơ Trung Kỳ (tương đương)
            placeholder: true
    relationships:
      - faction: Sa Trùng Vi Tộc
        description: Coi Sa Trùng là "bà con xa", có cấm kỵ không được ăn thịt Sa Trùng. Hai bên cùng sống dưới đất nhưng hiếm khi giao tiếp.
        diplomacy:
          lien_minh: 20
          tin: 10
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 0
      - faction: Thiết Giáp Yêu Thú Đàn
        description: Kẻ thù tự nhiên, thường xuyên đụng độ khi Sa Mãng phục kích thương đoàn được bọ giáp bảo vệ. Hai bên săn mồi cùng khu vực, xung đột là tất yếu.
        diplomacy:
          lien_minh: -60
          tin: -50
          uy_hiep: 40
          thuong_mai: 0
          on_oan: -40
          le_thuoc: 0
      - faction: Sa Tặc Liên Minh
        description: Quan hệ bí mật và mập mờ. Có tin đồn Sa Mãng lén cung cấp nọc độc cho Sa Tặc để đổi lấy thực phẩm, nhưng Tộc Trưởng Huyền Sa phủ nhận.
        diplomacy:
          lien_minh: 10
          tin: -10
          uy_hiep: 20
          thuong_mai: 30
          on_oan: 0
          le_thuoc: 0
---

# Sa Mãng Tộc (沙蟒族)

## I. Tổng Quan (总览)

Sa Mãng Tộc là bộ lạc xà yêu sống ẩn mình dưới lớp cát sâu của Hoàng Kim Sa Hải, gồm khoảng hai trăm cá thể Sa Mãng sinh sống trong hệ thống hang ngầm phức tạp. Phần lớn Sa Mãng trong tộc chưa khai linh trí, chỉ là thú thường có chút linh lực, hành động theo bản năng. Chỉ vài cá thể sống đủ lâu mới khai mở trí tuệ và hóa thành yêu thật sự. Tộc Trưởng Huyền Sa, một Sa Mãng đen dài mười lăm trượng đã khai linh trí hoàn chỉnh, là cá thể mạnh nhất với tu vi tương đương Trúc Cơ Hậu Kỳ. Dưới sự dẫn dắt của Huyền Sa, bộ lạc sống kín đáo dưới cát, tránh xa các thế lực mạnh, hiếm khi giao tiếp với thế giới bên trên.

## II. Địa Lý & Tài Nguyên (地理与资源)

Lãnh thổ của Sa Mãng Tộc nằm dưới lớp cát sâu từ mười đến ba mươi trượng trong lòng Hoàng Kim Sa Hải. Hệ thống hang ngầm được đào bằng chính thân xà của Sa Mãng qua nhiều thế hệ, nối liền nhau thành mạng lưới phức tạp trải rộng diện tích lớn. Lợi thế chiến lược của lãnh thổ này là gần như không thể phát hiện từ mặt đất, mọi dấu hiệu trên bề mặt cát đều bị gió xóa sạch trong vài canh giờ. Tài nguyên chính gồm xác yêu thú nhỏ chui vào hang (nguồn thức ăn chủ yếu), trứng sa mãng có dược tính nhẹ được một số thế lực bên ngoài tìm kiếm, và nọc độc Sa Mãng vừa là vũ khí tự vệ vừa là vật phẩm trao đổi bí mật.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)

Triết lý sống của Sa Mãng Tộc giản đơn nhưng sâu sắc: "Cát che chở — cát là áo giáp của kẻ yếu." Họ không tôn thờ thần linh cụ thể mà kính sợ sa mạc như một thực thể sống, nơi che chở và cũng có thể nuốt chửng bất kỳ ai. Quy tắc chiến đấu bất di bất dịch là không bao giờ giao chiến trên mặt cát, luôn kéo kẻ thù xuống hang nơi Sa Mãng có lợi thế tuyệt đối. Mỗi năm khi Sa Mãng lột xác, da cũ được dâng lên tổ tiên trong hang sâu nhất, nơi bộ xương Mãng cổ đại nằm yên. Cấm kỵ quan trọng nhất là không ăn thịt Sa Trùng Vi Tộc, vì Sa Mãng coi chúng là "bà con xa" cùng sống dưới lòng đất.

## IV. Cơ Cấu Tổ Chức (组织结构)

Cơ cấu bộ lạc đơn giản theo bản năng đàn. Đứng đầu là Tộc Trưởng Huyền Sa, Sa Mãng đen dài mười lăm trượng, cá thể duy nhất khai linh trí hoàn chỉnh và nói được tiếng người. Dưới Huyền Sa là ba Trưởng Lão Sa Mãng tu vi tương đương Trúc Cơ Sơ đến Trung Kỳ, đã khai linh trí bán phần và có thể hiểu lệnh phức tạp. Mười Sa Mãng trinh sát nhỏ nhẹn được Huyền Sa chọn riêng, chuyên bò lên gần mặt đất thăm dò tình hình. Khoảng một trăm tám mươi bảy Sa Mãng còn lại đa phần chưa khai linh trí, hành động theo bản năng và tín hiệu rung động từ Tộc Trưởng, sống đời giản đơn trong hang.

## V. Công Pháp & Trận Pháp (功法与阵法)

Sa Mãng Tộc không tu luyện theo phương thức của Nhân Tộc mà dựa vào bản năng và khả năng bẩm sinh. Kỹ thuật đặc trưng nhất là Sa Độn Thuật, cho phép Sa Mãng chui trong cát với tốc độ cực nhanh, phục kích con mồi từ bên dưới mà không phát ra tiếng động. Nọc độc Sa Mãng gây tê liệt thần kinh, không chết người nhưng đủ để bắt sống con mồi hoặc khiến kẻ thù mất khả năng chiến đấu. Khi bị đe dọa nghiêm trọng, cả đàn phối hợp rung động thân thể đồng loạt, tạo ra hiện tượng cát lún trên diện rộng, kéo kẻ thù từ mặt đất xuống sâu trong cát nơi chúng chiếm ưu thế tuyệt đối.

## VI. Đặc Sản Môn Phái (门派特产)

- **Nọc Độc Sa Mãng:** Nọc độc gây tê liệt thần kinh, không chí mạng nhưng khiến nạn nhân mất khả năng vận công và cử động trong vài canh giờ. Được một số thế lực bên ngoài (đặc biệt Sa Tặc) tìm kiếm để tẩm vũ khí.
- **Trứng Sa Mãng:** Trứng chưa nở có dược tính nhẹ, thường được dùng làm nguyên liệu luyện đan hoặc bào chế thuốc giải độc cho các loại nọc rắn khác. Hiếm và khó kiếm vì Sa Mãng bảo vệ trứng rất kỹ.

## VII. Cơ Sở Hạ Tầng (基础设施)

- **Hang Chính (Ổ Tộc):** Khoang ngầm rộng lớn nằm ở trung tâm mạng lưới hang, nơi Huyền Sa và phần lớn tộc nhân cư trú. Tường hang nhẵn bóng do thân xà cọ xát qua hàng ngàn năm.
- **Hang Tổ Tiên:** Hang sâu nhất trong hệ thống, nơi đặt bộ xương Mãng cổ đại dài hơn một trăm trượng. Bộ xương vẫn tỏa ra uy áp khiến mọi Sa Mãng không dám đến gần, chỉ Huyền Sa mới có thể vào sâu bên trong.
- **Mạng Lưới Đường Hầm:** Hàng chục nhánh hang nhỏ tỏa ra từ hang chính, dùng làm đường săn mồi, đường thoát hiểm và đường trinh sát lên gần mặt đất.

## VIII. Kinh Tế (经济)

Kinh tế của Sa Mãng Tộc gần như tự cung tự cấp ở mức nguyên thủy. Nguồn thức ăn chính là yêu thú nhỏ chui vào hang và các sinh vật sống dưới lòng đất. Trứng sa mãng có giá trị dược liệu nhưng tộc rất ít khi đem trao đổi vì bảo vệ thế hệ sau là ưu tiên hàng đầu. Nguồn thu duy nhất từ bên ngoài, nếu tin đồn là thật, là việc lén cung cấp nọc độc cho Sa Tặc Liên Minh để đổi lấy thực phẩm và vật tư mà Sa Mãng không thể tự sản xuất. Tuy nhiên, Tộc Trưởng Huyền Sa kiên quyết phủ nhận mối quan hệ này.

## IX. Lịch Sử Tóm Tắt (简史)

Sa Mãng Tộc là loài xà yêu cấp thấp sống dưới cát từ lâu đời, có thể từ trước khi Nhân Tộc đặt chân đến Tây Mạc. Trong phần lớn lịch sử, chúng chỉ là thú thường có chút linh lực, không khác gì rắn lớn bình thường. Hiếm hoi mới có cá thể sống đủ lâu để khai linh trí và bắt đầu tư duy như sinh vật thông minh.

Huyền Sa là Sa Mãng hiếm hoi đạt được linh trí hoàn chỉnh, nói được tiếng người và có tư duy chiến lược. Ông dẫn dắt tộc nhân tránh xa các thế lực mạnh, đào hệ thống hang ngầm sâu hơn và rộng hơn để đảm bảo an toàn. Nhờ chiến lược ẩn mình này, Sa Mãng Tộc tồn tại yên ổn trong khi nhiều yêu tộc khác bị Nhân Tộc truy sát hoặc khuất phục.

## X. Giai Thoại & Bí Mật (轶事与秘密)

Bí mật lớn nhất của Sa Mãng Tộc nằm trong hang sâu nhất, nơi Huyền Sa tìm thấy bộ xương mãng cổ đại dài hơn một trăm trượng. Bộ xương vẫn tỏa ra uy áp đáng sợ dù đã chết từ vô số năm trước, khiến mọi Sa Mãng không dám đến gần. Huyền Sa tin rằng đây là xương của một Sa Mãng thượng cổ đã tu luyện đến cảnh giới không thể tưởng tượng. Nếu có thể giải mã bí mật trong bộ xương này, có lẽ Sa Mãng Tộc sẽ tìm được con đường tu luyện chân chính thay vì chỉ dựa vào bản năng.

Mối quan hệ với Thiết Giáp Yêu Thú Đàn là xung đột tự nhiên dai dẳng. Hai bên thường xuyên đụng độ khi Sa Mãng phục kích thương đoàn mà bọ giáp đang bảo vệ, tạo nên chuỗi thù oán không hồi kết giữa hai loài yêu thú. Ngoài ra, tin đồn về việc cung cấp nọc độc cho Sa Tặc Liên Minh vẫn là vấn đề nhạy cảm mà Huyền Sa không muốn đề cập.

## XI. Quan Hệ Thế Lực (势力关系)

- **Sa Trùng Vi Tộc:** Coi như "bà con xa" cùng sống dưới lòng đất. Có cấm kỵ không ăn thịt Sa Trùng. Hai bên hiếm khi giao tiếp trực tiếp nhưng đôi khi Sa Mãng cảm nhận được tín hiệu rung động của Sa Trùng và dùng nó để phán đoán tình hình bên trên.
- **Thiết Giáp Yêu Thú Đàn:** Kẻ thù tự nhiên. Thiết Giáp Bọ có giáp cứng kháng được nọc độc Sa Mãng, còn Sa Mãng có lợi thế dưới cát. Hai bên thường xuyên đụng độ khi cùng săn mồi hoặc tấn công thương đoàn.
- **Sa Tặc Liên Minh:** Quan hệ mập mờ, không rõ ràng. Nếu tin đồn đúng, đây là mối quan hệ trao đổi bí mật: nọc độc đổi thực phẩm. Nhưng Huyền Sa duy trì lập trường phủ nhận để tránh bị các thế lực khác coi là đồng minh của tặc khấu.
