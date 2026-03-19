---
type: faction
name: Độc Trùng Trị Liệu Đường
hantu: 毒虫治疗堂
faction_type: Hội
alignment: 6
race: Trùng Tộc
region: Đông Hoang
founded: 60 năm trước
founder: Thanh Châm (kế thừa từ sư phụ nhân tộc)
emblem: Con_Trung_Xanh_Kim_Cham.png
specialty: Y thuật trùng tộc, Nọc trùng dược liệu, Châm cứu trùng huyệt
economy:
- Thu phí trị liệu cho bệnh nhân đa chủng tộc
- Bán nọc trùng y dược pha loãng
- Trao đổi trùng dược với dược sư vùng Nam Cương
arcs:
  - arc: 1
    status: Hoạt động ổn định
    rank: Hạng Năm
    leader: Đường Chủ Thanh Châm
    population: 75
    territory:
      - Hang đá rìa đông Vạn Độc Cốc (Vùng đệm Vạn Độc Cốc - Vạn Trùng Cốc)
    assets:
      - name: Sách Y Thuật Cổ
        type: Pháp Bảo
      - name: Khu Nuôi Trùng Y Dược
        type: Công Trình
      - name: Bộ Sưu Tập Nọc Trùng Hiếm
        type: Tài Nguyên
    stats: [20, 80, 100, 75, 40, 120]
    divisions:
      - name: Trị Liệu Đường
        role: Chữa trị bệnh nhân đa chủng tộc bằng phương pháp trùng y
        headcount:
          hoi_truong: 1
          pho_hoi_truong: 0
          thanh_vien: 8
          tong_quan: 1
        members:
          - character: Thanh Châm
            position: Đường Chủ
            cultivation: Trúc Cơ Hậu Kỳ
          - character: "[Trùng Y Trưởng]"
            position: Trùng Y Phó
            cultivation: Luyện Khí Đỉnh Phong
            placeholder: true
      - name: Khu Nuôi Trùng
        role: Nuôi dưỡng và chăm sóc trùng y dược, chiết xuất nọc theo liều lượng an toàn
        headcount:
          hoi_truong: 0
          pho_hoi_truong: 0
          thanh_vien: 50
          tong_quan: 5
        members:
          - character: "[Trùng Dưỡng Viên Trưởng]"
            position: Quản lý
            cultivation: Luyện Khí Hậu Kỳ
            placeholder: true
    relationships:
      - faction: Vạn Trùng Cốc
        description: Quan hệ phức tạp, Vạn Trùng Cốc cung cấp trùng nguyên liệu nhưng coi thường phương pháp y thuật "nhu nhược" của Đường.
        diplomacy:
          lien_minh: 10
          tin: 20
          uy_hiep: 10
          thuong_mai: 50
          on_oan: 0
          le_thuoc: 20
      - faction: Vạn Độc Môn
        description: Mối đe dọa tiềm tàng. Vạn Độc Môn muốn bắt Thanh Châm nghiên cứu kỹ thuật nọc trùng y dược, nhưng tạm thời kiềm chế vì từng được Đường chữa trị.
        diplomacy:
          lien_minh: -10
          tin: -20
          uy_hiep: 50
          thuong_mai: 20
          on_oan: -10
          le_thuoc: 0
      - faction: Nam Cương Dược Sư Hội
        description: Đối tác thương mại, Dược Sư Hội mua nọc trùng y dược pha loãng và trao đổi kiến thức dược liệu.
        diplomacy:
          lien_minh: 20
          tin: 40
          uy_hiep: 0
          thuong_mai: 70
          on_oan: 10
          le_thuoc: 0
---

# ĐỘC TRÙNG TRỊ LIỆU ĐƯỜNG (毒虫治疗堂)

## I. Tổng Quan (总览)
Độc Trùng Trị Liệu Đường là một cơ sở y thuật độc đáo nằm ở vùng đệm giữa Vạn Độc Cốc và Vạn Trùng Cốc, chuyên dùng nọc trùng và kỹ thuật châm cứu bằng trùng để chữa bệnh. Do một con bọ ngựa linh thú tên Thanh Châm lãnh đạo, Trị Liệu Đường là nơi hiếm hoi ở vùng Nam Cương mà nhân tộc, yêu tộc và trùng tộc ngồi chung phòng chờ mà không gây sự — bởi khi đau đớn đến cùng cực, không ai còn quan tâm đến chủng tộc của thầy thuốc. Với triết lý "Nọc không phải để giết, mà để chữa", Đường đã cứu sống vô số bệnh nhân mà đan dược thông thường bất lực.

## II. Địa Lý & Tài Nguyên (地理与资源)
Trụ sở là một hang đá ẩm thấp nằm ở rìa đông Vạn Độc Cốc, nơi cả độc khí lẫn trùng khí hòa trộn tạo ra hệ sinh thái kỳ lạ — nấm phát quang mọc trên vách đá, trùng dược liệu sinh sôi nảy nở trong bóng tối. Tường hang phủ rêu phát ra ánh sáng xanh lục nhạt, đủ để chiếu sáng mà không cần đèn. Bên trong chia thành ba khu rõ ràng: khu nuôi trùng ở tầng sâu nhất nơi ẩm nhất, khu trị liệu ở tầng giữa thoáng đãng, và khu ở ở gần cửa hang. Tài nguyên quý nhất là bộ sưu tập nọc trùng y dược — hơn ba mươi loại nọc được chiết xuất từ các giống trùng đặc biệt, mỗi loại có dược tính riêng khi pha loãng đúng liều. Ngoài ra, Trùng Châm — loài trùng cực nhỏ có thể đốt vào huyệt đạo giúp thông kinh mạch bị tắc nghẽn — là "công cụ y tế" độc quyền của Đường.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
Trị Liệu Đường vận hành theo ba nguyên tắc bất di bất dịch do Thanh Châm đặt ra: chỉ chữa bệnh không tấn công, đối xử nhân đạo với trùng y dược không ép chúng sản xuất nọc quá sức, và bệnh nhân phải chấp nhận rủi ro trước khi điều trị. Trước mỗi ca chữa trị, Thanh Châm thực hiện nghi thức "chẩn đoán trùng" — để một con trùng nhỏ bò trên người bệnh nhân, quan sát nơi trùng dừng lại để xác định vị trí bệnh tật. Đây vừa là phương pháp y thuật vừa là cách Thanh Châm giao tiếp với bệnh nhân — vì bản thân Thanh Châm không nói tiếng người mà giao tiếp bằng cách gõ càng theo nhịp điệu.

## IV. Cơ Cấu Tổ Chức (组织结构)
Đường Chủ Thanh Châm là một bọ ngựa linh thú nhỏ, dài chưa đầy ba tấc, hai càng sắc như kim châm cứu, vỏ xanh ngọc bóng loáng. Thanh Châm có linh trí cao, giao tiếp bằng nhịp gõ càng phức tạp mà các trùng y đã học cách giải mã. Từng được một dược sư nhân tộc già nuôi dưỡng và truyền thụ y thuật trước khi ông qua đời — di sản lớn nhất ông để lại là cuốn sách y thuật cổ và tấm lòng cứu người. Tám Trùng Y là các cá thể trùng có kỹ năng y dược bẩm sinh, tu vi tương đương Luyện Khí, mỗi con chuyên một lĩnh vực: giải độc, thông kinh, trị thương, bồi bổ. Hơn năm mươi con trùng nhỏ được nuôi riêng cho mục đích y dược, là "nguyên liệu sống" của Đường. Ngoài ra, luôn có mười đến mười lăm bệnh nhân thường trực đang điều trị dài hạn.

## V. Công Pháp & Trận Pháp (功法与阵法)
- **Công Pháp:** Thanh Châm không có công pháp chiến đấu chính thống. Kỹ thuật cốt lõi là "Trùng Châm Thông Mạch Thuật" — dùng hai càng sắc đâm vào huyệt đạo bệnh nhân với độ chính xác tuyệt đối, kết hợp tiêm nọc trùng liều lượng siêu nhỏ để thông kinh mạch bị tắc nghẽn. Kỹ thuật này vừa là phương pháp chữa bệnh chính vừa là phương thức tự vệ duy nhất — khi bị đe dọa, Thanh Châm có thể đâm vào huyệt đạo gây tê liệt tạm thời cho đối phương.
- **Trận Pháp:** Không có trận pháp chiến đấu. Vị trí hang đá ở vùng đệm giữa hai cốc lớn tự thân đã là lá chắn — kẻ nào gây sự ở đây sẽ đồng thời chọc giận cả Vạn Độc Cốc lẫn Vạn Trùng Cốc.

## VI. Đặc Sản Môn Phái (门派特产)
- **Nọc Trùng Y Dược:** Nọc chiết xuất từ trùng đặc biệt, khi pha loãng đúng liều có tác dụng chữa bệnh kỳ diệu: giải độc, thông mạch, giảm đau, thậm chí kích thích tái tạo mô bị tổn thương. Hiệu quả vượt xa đan dược thông thường đối với một số bệnh nan y.
- **Trùng Châm Trị Liệu:** Dịch vụ độc quyền — Thanh Châm dùng càng đâm vào huyệt đạo kết hợp nọc trùng vi lượng, chữa được các chứng kinh mạch tắc nghẽn, linh lực nghịch chuyển, và nhiều bệnh mà đan dược không giải quyết được.
- **Trùng Chẩn Đoán:** Loại trùng nhỏ đặc biệt được huấn luyện để bò trên cơ thể bệnh nhân và dừng lại tại vị trí bệnh tật — công cụ chẩn đoán chính xác đến kinh ngạc.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Khu Trị Liệu:** Tầng giữa hang đá, thoáng đãng và sạch sẽ nhất, có mười giường đá phủ lá mềm cho bệnh nhân nằm. Trần hang cao, rêu phát quang cung cấp ánh sáng dịu nhẹ lý tưởng cho các ca phẫu thuật trùng châm.
- **Khu Nuôi Trùng:** Tầng sâu nhất, ẩm ướt và tối, chia thành hơn hai mươi hốc đá nhỏ, mỗi hốc nuôi một loại trùng y dược khác nhau. Nhiệt độ và độ ẩm được điều chỉnh tự nhiên bởi dòng nước ngầm chảy qua vách đá.
- **Phòng Chờ Bệnh Nhân:** Khu vực gần cửa hang, nơi bệnh nhân đa chủng tộc ngồi chờ — cảnh tượng kỳ lạ nơi nhân tộc, yêu tộc và trùng tộc cùng im lặng chịu đau bên nhau.

## VIII. Kinh Tế (经济)
Nguồn thu chính của Trị Liệu Đường đến từ phí trị liệu — nhưng Thanh Châm thu phí linh hoạt: giàu thì trả nhiều, nghèo thì trả ít, không có thì chữa miễn phí. Vì vậy thu nhập không ổn định, phụ thuộc vào việc có bệnh nhân giàu có tìm đến hay không. Ngoài ra, Đường bán nọc trùng y dược pha loãng cho Nam Cương Dược Sư Hội — đây là nguồn thu ổn định nhất. Vạn Trùng Cốc cung cấp trùng nguyên liệu với giá rẻ vì coi đó là hàng thải, nhưng Thanh Châm biết cách biến chúng thành dược phẩm giá trị gấp trăm lần.

## IX. Lịch Sử Tóm Tắt (简史)
Thanh Châm được một dược sư nhân tộc già tên Mạc Thanh nuôi từ nhỏ. Mạc Thanh vốn là y sĩ lang thang, tìm thấy Thanh Châm khi còn là ấu trùng bị thương bên đường. Ông nhận ra con trùng nhỏ có linh trí khác thường, bèn nuôi dưỡng và truyền dạy y thuật suốt bốn mươi năm. Khi Mạc Thanh qua đời vì tuổi già, Thanh Châm kế thừa cuốn sách y thuật cổ và tiếp tục sự nghiệp cứu người. Dần dần, những trùng tộc khác có thiên phú y dược tìm đến theo danh tiếng, hình thành Trị Liệu Đường. Sáu mươi năm qua, Đường đã chữa trị cho hàng ngàn bệnh nhân từ đủ mọi chủng tộc, tạo nên ốc đảo hòa bình nhỏ bé giữa vùng đất đầy hiểm nguy.

## X. Giai Thoại & Bí Mật (轶事与秘密)
Thanh Châm sở hữu cuốn sách y thuật do sư phụ Mạc Thanh để lại — viết bằng chữ cổ mà ngay cả Đan Hà Cốc cũng thèm muốn. Sách ghi chép phương pháp dùng nọc trùng chữa các bệnh nan y mà đan dược bất lực, bao gồm cả phương pháp phục hồi linh căn bị phế — nếu tin đồn này là thật, giá trị cuốn sách vượt xa mọi pháp bảo.

Vạn Độc Môn từng muốn bắt Thanh Châm để nghiên cứu kỹ thuật nọc trùng y dược, nhưng vì Trị Liệu Đường từng chữa trị cho vài đệ tử Vạn Độc Môn trúng độc nghịch chuyển nên tạm thời kiềm chế. Tuy nhiên, sự kiềm chế này mong manh — chỉ cần một lệnh từ Cốc Chủ Vạn Độc Môn là tình hình sẽ thay đổi hoàn toàn.

Gần đây, ngày càng nhiều bệnh nhân mắc chứng "Huyết Mạch Nghịch Chuyển" tìm đến — triệu chứng kỳ lạ mà Thanh Châm chưa từng thấy trong sách sư phụ. Thanh Châm nghi ngờ đây là hệ quả của biến đổi linh mạch Nam Cương, nhưng chưa đủ dữ liệu để xác nhận.

## XI. Quan Hệ Thế Lực (势力关系)
- **Vạn Trùng Cốc:** Nhà cung cấp trùng nguyên liệu, quan hệ thương mại ổn định nhưng không thân thiết. Vạn Trùng Cốc coi thường phương pháp y thuật "nhu nhược" nhưng vẫn bán hàng vì có lợi.
- **Vạn Độc Môn:** Mối đe dọa thường trực. Độc Môn thèm muốn kỹ thuật và cuốn sách y thuật cổ, chỉ kiềm chế vì nợ ân tình chữa bệnh.
- **Nam Cương Dược Sư Hội:** Đối tác thương mại tốt nhất, mua nọc trùng y dược và trao đổi kiến thức. Dược Sư Hội đánh giá cao giá trị y thuật độc đáo của Trị Liệu Đường.
