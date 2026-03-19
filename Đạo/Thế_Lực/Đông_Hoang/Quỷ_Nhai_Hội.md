---
type: faction
name: Quỷ Nhai Hội
hantu: 鬼崖会
faction_type: Hội
alignment: -6
race: Đa chủng tộc (chủ yếu Nhân Tộc, Bán Yêu, Yêu Tộc)
region: Đông Hoang
founded: 80 năm trước (cùng sự phát triển của Quỷ Thị Nam Cương)
founder: Quỷ Chủ đời đầu (danh tính bất minh)
emblem: Quy_Nhai_Hoi.png
specialty: Chợ đen, Buôn bán hàng cấm, Tình báo ngầm, Trung gian giao dịch phi pháp
economy:
- Phí giao dịch chợ đen (mọi hàng hóa cấm)
- Bán thông tin tình báo ngầm
- Lưu trữ và vận chuyển hàng lậu
- Trung gian cho các thỏa thuận bí mật
arcs:
  - arc: 1
    status: Hoạt động mạnh
    rank: Hạng Ba
    leader: Quỷ Chủ Nhị (danh tính bất minh)
    population: 800
    territory:
      - Hệ thống hang ngầm dưới Quỷ Thị Nam Cương
      - Mạng lưới mật thám rải khắp Trạm Biên và các làng xung quanh
    assets:
      - name: Mê Cung Quỷ Nhai
        type: Công Trình
      - name: Kho Hàng Cấm
        type: Tài Nguyên
      - name: Mạng lưới Mắt Quỷ
        type: Tài Nguyên
      - name: Sổ Giao Dịch 80 Năm
        type: Tài Nguyên
    stats: [600, 500, 700, 800, 800, 900]
    divisions:
      - name: Tứ Quỷ Sứ Bộ
        role: Bốn bộ phận chuyên trách, mỗi bộ do một Quỷ Sứ (Trúc Cơ Viên Mãn) quản lý
        headcount:
          hoi_truong: 1
          pho_hoi_truong: 0
          thanh_vien: 750
          tong_quan: 49
        members:
          - character: "[Quỷ Chủ Nhị]"
            position: Hội Trưởng
            cultivation: Kim Đan trở lên (ước tính)
            placeholder: true
          - character: "[Quỷ Sứ — Giao Dịch]"
            position: Tổng Quản (Quản Lý Giao Dịch)
            cultivation: Trúc Cơ Viên Mãn
            placeholder: true
          - character: "[Quỷ Sứ — Tình Báo]"
            position: Tổng Quản (Quản Lý Tình Báo)
            cultivation: Trúc Cơ Viên Mãn
            placeholder: true
          - character: "[Quỷ Sứ — Kho Hàng]"
            position: Tổng Quản (Quản Lý Kho)
            cultivation: Trúc Cơ Viên Mãn
            placeholder: true
          - character: "[Quỷ Sứ — An Ninh]"
            position: Tổng Quản (Quản Lý An Ninh)
            cultivation: Trúc Cơ Viên Mãn
            placeholder: true
    relationships:
      - faction: Vạn Yêu Thành
        description: Quan hệ cộng sinh phức tạp. Quỷ Nhai Hội xử lý mặt tối mà chính quyền thành không muốn dính vào, đổi lại được tồn tại dưới lòng đất. Cả hai bên đều biết bên kia đang theo dõi mình.
        diplomacy:
          lien_minh: -10
          tin: -30
          uy_hiep: 40
          thuong_mai: 50
          on_oan: -10
          le_thuoc: 30
      - faction: Hoang Dã Thợ Săn Bang
        description: Thợ săn bang là nguồn cung cấp linh vật không rõ nguồn gốc chính cho chợ đen. Đôi khi Quỷ Nhai cũng thuê thợ săn làm nhiệm vụ vận chuyển nguy hiểm.
        diplomacy:
          lien_minh: 0
          tin: -10
          uy_hiep: 20
          thuong_mai: 60
          on_oan: 0
          le_thuoc: 0
      - faction: Huyết Sát Minh
        description: Huyết Sát Minh là khách hàng thường xuyên của chợ đen, mua độc dược và vũ khí ám sát. Quỷ Nhai bán cho ai trả giá cao nhất, không quan tâm mục đích sử dụng.
        diplomacy:
          lien_minh: 0
          tin: -20
          uy_hiep: 30
          thuong_mai: 50
          on_oan: 0
          le_thuoc: 0
---

# Quỷ Nhai Hội (鬼崖会)

## I. Tổng Quan (总览)
Quỷ Nhai Hội là tổ chức ngầm lớn nhất hoạt động dưới lòng đất Quỷ Thị Nam Cương, điều hành mạng lưới chợ đen rộng khắp với tám trăm thành viên ẩn sau những chiếc mặt nạ xương. Xếp Hạng Ba nhờ mạng lưới thông tin và quan hệ chằng chịt với mọi thế lực ngầm, Hội nắm trong tay mọi giao dịch cấm từ độc dược, pháp khí đánh cắp, bản đồ cấm địa, đến thông tin truy nã phạm. Đứng đầu là Quỷ Chủ Nhị — nhân vật bí ẩn luôn giao tiếp qua trung gian, cảnh giới ước tính Kim Đan trở lên, mà không ai biết "Nhị" ám chỉ đây là tay chân của Quỷ Chủ thật sự hay chính là Quỷ Chủ duy nhất. Triết lý "Vàng không hỏi xuất xứ, người không hỏi tên thật" đã biến Quỷ Nhai thành nơi duy nhất ở Đông Hoang mà kẻ thù có thể ngồi cùng bàn giao dịch mà không cần rút kiếm.

## II. Địa Lý & Tài Nguyên (地理与资源)
Quỷ Nhai Hội tọa lạc trực tiếp dưới Quỷ Thị Nam Cương, hệ thống hang động đá vôi tự nhiên được mở rộng nhân tạo qua nhiều thập kỷ, kết nối với Mạch Ngầm bí ẩn phía sâu hơn. Mê cung đường hầm chia thành nhiều tầng rõ ràng: tầng giao dịch ở trên cùng, rộng rãi và chiếu sáng bằng đèn dạ minh châu cấp thấp, nơi mọi giao dịch diễn ra; tầng kho hàng ở giữa, chứa đầy hàng lậu và vật phẩm đang chờ giao; tầng cấm ở sâu nhất, nối thẳng vào Mạch Ngầm, tuyệt đối cấm mọi người trừ Quỷ Chủ Nhị. Không khí ẩm thấp, lạnh, mang mùi đá cũ và hương nhang tà thuật. Tài nguyên chính không phải khoáng sản mà là thông tin — mạng lưới mật thám Mắt Quỷ rải khắp Trạm Biên và các làng xung quanh ghi nhận mọi giao dịch, mọi di chuyển, mọi thì thầm.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
"Vàng không hỏi xuất xứ, người không hỏi tên thật." Lợi nhuận là đạo lý duy nhất trong Quỷ Nhai, và mọi người đều bình đẳng trước đồng tiền. Văn hóa Hội đề cao sự công bằng trong giao dịch với hình phạt tàn khốc cho kẻ phá luật: lừa đảo trong Quỷ Nhai sẽ bị cắt tay trái, không ngoại lệ. Quy tắc thứ hai là bảo mật tuyệt đối — không tiết lộ danh tính khách hàng, không ghi nhận giao dịch bằng tên thật, mọi thứ đều thông qua ám hiệu và mã số. Quy tắc thứ ba: không mang chiến đấu vào khu giao dịch, ai rút vũ khí trước sẽ bị toàn bộ Quỷ Tốt bao vây. Đặc biệt, mọi người trong Quỷ Nhai đều đeo mặt nạ xương — không ai biết mặt thật của ai, kể cả đồng nghiệp làm việc cạnh nhau nhiều năm. Đây vừa là truyền thống vừa là biện pháp bảo vệ: nếu một người bị bắt, hắn không thể khai báo danh tính người khác.

## IV. Cơ Cấu Tổ Chức (组织结构)
Quỷ Chủ Nhị đứng trên đỉnh, điều hành toàn bộ Hội nhưng không bao giờ lộ diện trực tiếp, luôn giao tiếp qua Tứ Quỷ Sứ hoặc lệnh viết trên mặt nạ xương đặc biệt. Bốn Quỷ Sứ, mỗi vị cảnh giới Trúc Cơ Viên Mãn, phụ trách bốn mảng: Giao Dịch quản lý mọi hoạt động mua bán tại tầng giao dịch; Tình Báo điều phối mạng lưới Mắt Quỷ thu thập thông tin bên ngoài; Kho Hàng kiểm soát tầng kho và luồng hàng lậu ra vào; An Ninh bảo vệ mê cung bằng bẫy cơ quan và đội Quỷ Tốt. Dưới Tứ Quỷ Sứ là khoảng bốn mươi lăm quản lý cấp thấp, mỗi người phụ trách một khu vực hoặc tuyến giao dịch cụ thể. Lực lượng chính gồm bảy trăm năm mươi Quỷ Tốt từ Luyện Khí đến Trúc Cơ, làm vệ sĩ, vận chuyển, giao dịch viên, và mật thám.

## V. Công Pháp & Trận Pháp (功法与阵法)
Quỷ Nhai Hội không có công pháp thống nhất — thành viên đến từ mọi nền tảng, sử dụng đa dạng tà thuật, ám khí, và kỹ thuật chiến đấu cá nhân. Sự đa dạng này khiến kẻ thù không thể dự đoán đối thủ sẽ dùng chiêu gì. Sức mạnh phòng thủ thực sự nằm ở hệ thống bẫy cơ quan và mê trận bên trong hang động: hành lang giả dẫn vào ngõ cụt chứa bẫy nổ, sàn sập lộ hố sâu, tường phun khí độc, và nhiều cơ quan chí mạng khác được thiết kế để tiêu diệt kẻ xâm nhập trước khi chúng kịp đến tầng giao dịch. Chỉ người có mặt nạ xương chính thức mới biết đường đi an toàn — mà đường đi này thay đổi mỗi tuần theo lệnh của Quỷ Sứ An Ninh.

## VI. Đặc Sản Môn Phái (门派特产)
- **Mặt Nạ Xương Quỷ Nhai:** Mỗi thành viên được cấp một mặt nạ xương độc nhất, chế tác từ xương linh thú, khắc mã số bí mật xác nhận danh tính. Mất mặt nạ đồng nghĩa mất tư cách thành viên.
- **Quỷ Nhai Ấn:** Con dấu đặc biệt đóng lên hợp đồng giao dịch, xác nhận Quỷ Nhai Hội bảo chứng cho giao dịch. Kẻ nào phá vỡ hợp đồng có Quỷ Nhai Ấn sẽ bị toàn bộ mạng lưới ngầm tẩy chay.
- **Bản Đồ Mê Cung Tạm Thời:** Bản đồ vẽ bằng mực tự tiêu, chỉ hiệu lực một ngày, cấp cho khách hàng VIP khi cần đi sâu vào các tầng phía trong.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Mê Cung Quỷ Nhai:** Hệ thống hang động nhiều tầng dưới Quỷ Thị, mở rộng nhân tạo qua tám mươi năm, với bẫy cơ quan bảo vệ mọi ngã rẽ.
- **Tầng Giao Dịch:** Không gian rộng nhất, chiếu sáng bằng dạ minh châu, chia thành các gian hàng nơi mọi loại giao dịch diễn ra. Luôn có Quỷ Tốt tuần tra.
- **Tầng Kho Hàng:** Khu vực lưu trữ hàng lậu với hệ thống quản lý nghiêm ngặt, mỗi lô hàng có mã số riêng, chỉ Quỷ Sứ Kho Hàng mới biết toàn bộ nội dung.
- **Mạng Lưới Mắt Quỷ:** Hàng trăm mật thám cải trang rải khắp Trạm Biên và các làng xung quanh, báo cáo mọi biến động về hang chính.

## VIII. Kinh Tế (经济)
Kinh tế Quỷ Nhai Hội dựa trên bốn trụ cột. Thứ nhất là phí giao dịch chợ đen — mọi giao dịch tại tầng giao dịch phải nộp mười phần trăm giá trị cho Hội, đổi lại được bảo chứng an toàn và bảo mật. Thứ hai là bán thông tin tình báo — mạng lưới Mắt Quỷ thu thập tin tức rồi bán cho ai trả giá cao nhất, từ tu sĩ cá nhân đến thế lực lớn. Thứ ba là dịch vụ lưu trữ và vận chuyển — kho hàng an toàn nhất dưới lòng đất và đội vận chuyển bí mật có thể đưa bất kỳ thứ gì đến bất kỳ đâu mà không bị phát hiện. Thứ tư là trung gian cho các thỏa thuận bí mật — khi hai thế lực muốn đàm phán mà không để ai biết, Quỷ Nhai cung cấp không gian và bảo chứng, thu phí trung gian rất cao.

## IX. Lịch Sử Tóm Tắt (简史)
Quỷ Nhai Hội hình thành tự nhiên cùng với sự phát triển của Quỷ Thị Nam Cương tám mươi năm trước, ban đầu chỉ là một nhóm khuân vác hàng lậu sống dưới hang đá vôi. Khi Quỷ Thị phía trên ngày càng phồn hoa, nhu cầu giao dịch ngầm tăng vọt, nhóm khuân vác dần phát triển thành mạng lưới chợ đen có tổ chức. Quỷ Chủ đời đầu thiết lập hệ thống mặt nạ xương và quy tắc giao dịch, biến hang động hỗn loạn thành chợ đen có trật tự. Sau khi Quỷ Chủ đời đầu biến mất trong hoàn cảnh bí ẩn, Quỷ Chủ Nhị tiếp quản và mở rộng quy mô lên tám trăm người, xây dựng mạng lưới Mắt Quỷ, thiết lập quan hệ "cộng sinh" với Quỷ Thị: Quỷ Thị lo phía trên, Quỷ Nhai lo phía dưới.

## X. Giai Thoại & Bí Mật (轶事与秘密)
Tầng sâu nhất của hang — "Tầng Cấm" — nối thẳng vào Mạch Ngầm. Có kẻ từng báo cáo thấy sinh vật khổng lồ bò qua trong bóng tối, tạo ra rung chấn mà cả tầng kho hàng phía trên cũng cảm nhận được. Quỷ Chủ Nhị lập tức ra lệnh không ai được xuống Tầng Cấm, và từ đó cho xây bốn lớp cửa đá phong ấn. Bí mật nguy hiểm hơn nằm ở Sổ Giao Dịch — Quỷ Nhai thực ra ghi chép lại mọi giao dịch cấm trong tám mươi năm, dù ngoài mặt tuyên bố không lưu hồ sơ. Bộ sổ này chứa đủ bằng chứng để hủy diệt danh tiếng của hàng chục "chính đạo" tu sĩ nếu công khai, và là lá bài cuối cùng đảm bảo sự sống còn của Hội.

## XI. Quan Hệ Thế Lực (势力关系)
- **Vạn Yêu Thành:** Quan hệ cộng sinh phức tạp — Quỷ Nhai xử lý mặt tối mà chính quyền không muốn dính vào, đổi lại được tồn tại. Cả hai bên theo dõi lẫn nhau không ngừng, duy trì thế cân bằng mong manh.
- **Hoang Dã Thợ Săn Bang:** Thợ săn bang là nguồn cung linh vật không rõ nguồn gốc chính cho chợ đen, đồng thời đôi khi được Quỷ Nhai thuê vận chuyển hàng nguy hiểm. Quan hệ thuần thương mại, không tin tưởng nhưng có lợi.
- **Huyết Sát Minh:** Khách hàng thường xuyên mua độc dược, vũ khí ám sát, và thông tin mục tiêu từ chợ đen. Quỷ Nhai bán cho ai trả tiền, không quan tâm đến mục đích — nhưng cũng ngầm theo dõi hoạt động của Huyết Sát Minh để phòng thân.
