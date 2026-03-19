---
type: faction
name: Thương Hội Bạch Lang
hantu: 商会白狼
faction_type: Thương Hội
alignment: 1
race: Nhân Tộc (đa số), Tán Tu đa chủng tộc
region: Đông Hoang
founded: 80 năm trước
founder: Bạch Lang Lão Nhân (biệt danh, tên thật đã thất truyền)
emblem: Thuong_Hoi_Bach_Lang.png
specialty: Hộ tống thương đoàn, Mạng lưới tình báo biên giới, Sinh tồn vùng hiểm
economy:
- Phí hộ tống thương đoàn xuyên Nam Cương
- Mua bán dược liệu và quặng lạ
- Bán thông tin tình báo biên giới
arcs:
  - arc: 1
    status: Hoạt động mạnh
    rank: Hạng Ba
    leader: Hội Trưởng Đại Lang Hắc Nha
    population: 600
    territory:
      - Trạm Biên (cơ sở chính)
      - Tuyến thương đạo Nam Cương — Đông Hoang
      - Các trạm dừng chân biên giới
    assets:
      - name: Trạm Biên Tổng Bộ
        type: Công Trình
      - name: Mạng lưới tình báo biên giới
        type: Tài Nguyên
      - name: Kho dược liệu và quặng
        type: Tài Nguyên
    stats: [800, 600, 1200, 600, 500, 1500]
    divisions:
      - name: Sói Đầu Đàn (Quản Sự)
        role: Chỉ huy các thương đoàn cụ thể, đàm phán hợp đồng và chỉ huy chiến đấu
        headcount:
          hoi_truong: 1
          truong_lao: 3
          thuong_nhan: 30
          ho_ve: 200
          nhan_cong: 366
        members:
          - character: "[Đại Lang Hắc Nha]"
            position: Hội Trưởng
            cultivation: Trúc Cơ Viên Mãn
            placeholder: true
          - character: "[Ngân Lang]"
            position: Quản Sự Trưởng
            cultivation: Trúc Cơ Hậu Kỳ
            placeholder: true
          - character: Lâm Phong
            position: Hộ Vệ Ngoại Vi (thân phận giả)
            cultivation: Trúc Cơ Sơ Kỳ
          - character: Diệp Tĩnh Sương
            position: Hộ Vệ Ngoại Vi (thân phận giả)
            cultivation: Trúc Cơ Sơ Kỳ
    relationships:
      - faction: Cửu Hoa Kiếm Tông
        description: Đối tác thương mại lớn nhất. Thương Hội cung cấp tài nguyên biên giới, tông môn trả linh thạch và đan dược.
        diplomacy:
          lien_minh: 20
          tin: 40
          uy_hiep: 5
          thuong_mai: 80
          on_oan: 10
          le_thuoc: 15
      - faction: Vạn Độc Môn
        description: Quan hệ căng thẳng. Thường phải đóng phí mãi lộ nhưng vẫn xảy ra xung đột đẫm máu khi bị cướp bóc.
        diplomacy:
          lien_minh: -40
          tin: -50
          uy_hiep: 60
          thuong_mai: -20
          on_oan: -60
          le_thuoc: 30
      - faction: Huyết Sát Minh
        description: Kẻ thù tiềm tàng. Huyết Sát Minh thường xuyên phục kích các thương đoàn để cướp huyết khí và tài nguyên.
        diplomacy:
          lien_minh: -60
          tin: -70
          uy_hiep: 70
          thuong_mai: -80
          on_oan: -50
          le_thuoc: 0
---

# Thương Hội Bạch Lang (商会白狼)

## I. Tổng Quan (总览)

Thương Hội Bạch Lang là một tổ chức thương mại kiêm hộ tống vũ trang hoạt động chủ yếu tại vùng biên giới Nam Cương thuộc Đông Hoang. Được thành lập bởi những tán tu từng là lính đánh thuê và thợ săn kỳ cựu, Thương Hội nổi tiếng với sự liều lĩnh, kinh nghiệm sinh tồn trong môi trường khắc nghiệt và khả năng tuyển mộ những tán tu tài năng làm hộ vệ. Với triết lý "Tín trong kinh doanh, Sói trong chiến đấu", tổ chức này tuy không thể sánh ngang các đại thương hội như Thiên Sa Thương Hội ở Tây Mạc, nhưng lại là một trong số ít phương tiện di chuyển an toàn qua các tuyến đường chết chóc của Nam Cương. Biểu tượng cờ hiệu hình con sói trắng tru trên nền đen đã trở thành dấu hiệu của sự bảo đảm và uy tín trên khắp các tuyến thương đạo biên giới.

## II. Địa Lý & Tài Nguyên (地理与资源)

Thương Hội Bạch Lang không có lãnh thổ cố định theo nghĩa truyền thống, thay vào đó kiểm soát một mạng lưới các trạm dừng chân và cơ sở hậu cần dọc theo tuyến thương đạo xuyên Nam Cương. Trụ sở chính đặt tại Trạm Biên — một thành trì biên giới nằm ở ranh giới giữa vùng đất văn minh và hoang dã. Các tuyến đường hộ tống băng qua những địa hình cực kỳ nguy hiểm bao gồm Rừng Huyết Độc với chướng khí chết người, dãy Núi Độc Long nơi trú ngụ của hải lượng yêu thú hung tợn, và các vùng đất hoang dã chưa được khám phá. Tài nguyên chính của Thương Hội không phải đất đai mà là tri thức — bản đồ các tuyến đường an toàn, thời điểm di chuyển tối ưu, và mạng lưới thông tin về các mối đe dọa dọc đường. Ngoài ra, họ trực tiếp thu mua dược liệu quý hiếm, quặng lạ và chiến lợi phẩm từ thợ săn và tán tu tại Trạm Biên.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)

Văn hóa Thương Hội Bạch Lang mang đậm tính thực dụng của lính đánh thuê. Họ không bị ràng buộc bởi các quy tắc "Chính Đạo" hay "Ma Đạo" cứng nhắc — điều duy nhất quan trọng là hoàn thành hợp đồng và sống sót. Tuy nhiên, Thương Hội nổi tiếng với chữ "Tín": một khi đã nhận tiền bảo kê, họ sẽ tử chiến để bảo vệ hàng hóa, dù phải đổi bằng tính mạng. Thành viên cốt lõi mặc áo giáp da thú nhẹ, linh hoạt, khoác thêm áo choàng lông sói trắng (hoặc giả lông) để nhận diện nhau trong địa hình phức tạp. Họ tự gọi nhau bằng danh xưng "Lang" (Sói), từ Đại Lang (Hội Trưởng) đến Lang Tử (tân binh), thể hiện tinh thần bầy đàn: đoàn kết khi săn mồi, chia đều chiến lợi phẩm, bảo vệ đồng đội đến cùng.

## IV. Cơ Cấu Tổ Chức (组织结构)

Thương Hội hoạt động theo cấu trúc quân sự hóa lỏng lẻo, linh hoạt hơn so với các tông môn truyền thống nhưng kỷ luật hơn so với những nhóm tán tu thông thường.

- **Hội Trưởng (Đại Lang):** Nắm quyền quyết định tối cao về các tuyến đường, hợp đồng lớn và nhân sự cốt cán. Thường là cường giả Trúc Cơ Hậu Kỳ hoặc Viên Mãn.
- **Quản Sự (Sói Đầu Đàn):** Phụ trách chỉ huy từng thương đoàn cụ thể. Là những người giàu kinh nghiệm, vừa biết cách chỉ huy chiến đấu vừa giỏi đàm phán giá cả. Thương Hội hiện có 3 Quản Sự thường trực.
- **Hộ Vệ Cốt Cán (Sói Bạc):** Đội ngũ lính đánh thuê thường trực, yêu cầu tu vi Trúc Cơ Sơ Kỳ trở lên. Khoảng 200 người, là xương sống chiến đấu của Thương Hội.
- **Hộ Vệ Ngoại Vi:** Tán tu được thuê mướn tạm thời cho từng chuyến đi. Thường là Luyện Khí kỳ, làm nhiệm vụ do thám, khuân vác hoặc làm tiền quân trong các cuộc phục kích.
- **Thương Nhân & Nhân Công:** Những thành viên phụ trách hậu cần, khuân vác hàng hóa, quản lý kho bãi và giao dịch tại các trạm.

## V. Công Pháp & Trận Pháp (功法与阵法)

Thương Hội Bạch Lang không có công pháp chấn phái — thành viên đến từ nhiều nguồn khác nhau, mỗi người tu luyện theo cách riêng. Tuy nhiên, Thương Hội có một bộ chiến thuật phối hợp đặc trưng gọi là "Lang Trận": khi bị phục kích, các hộ vệ tự động xếp thành đội hình vòng tròn bảo vệ hàng hóa ở trung tâm, Sói Bạc đảm nhận tuyến trước, Hộ Vệ Ngoại Vi bọc hậu và do thám. Ngoài ra, Quản Sự thường mang theo Phòng Hộ Trận Bàn — một pháp khí cấp thấp tạo được rào chắn linh lực tạm thời xung quanh đoàn xe, đủ sức cầm cự vài canh giờ trước khi tán tu cấp Trúc Cơ phá vỡ.

## VI. Đặc Sản Môn Phái (门派特产)

- **Sói Trắng Tín Bài:** Chiếc thẻ bài bằng bạch ngọc hình đầu sói, là vật nhận diện hội viên cốt cán. Khi gặp nguy, có thể phát tín hiệu cầu cứu đến các trạm dừng chân gần nhất.
- **Dược Liệu Biên Giới:** Thương Hội thu mua và chế biến sơ bộ các loại dược liệu hiếm từ Nam Cương — bao gồm Huyết Hoa, Độc Long Thảo và Âm Dương Quả — trước khi bán cho các tông môn lớn với giá cao.
- **Bản Đồ Thương Đạo:** Được cập nhật liên tục theo mùa, ghi chép chi tiết các tuyến đường an toàn, hang ổ yêu thú, và khu vực chướng khí. Là sản phẩm thông tin có giá trị cao mà nhiều thế lực sẵn sàng trả giá lớn.

## VII. Cơ Sở Hạ Tầng (基础设施)

- **Trạm Biên Tổng Bộ:** Tòa nhà gỗ kiên cố nằm trong lòng thành Trạm Biên, bao gồm kho hàng, phòng đàm phán, nhà trọ cho hộ vệ và chuồng linh thú kéo xe.
- **Trạm Dừng Chân (Lang Trại):** Một chuỗi 7 trạm nhỏ dọc theo tuyến thương đạo chính, mỗi trạm có kho lương thực dự trữ, giếng nước và hầm trú ẩn khẩn cấp.
- **Kho Quặng & Dược Liệu:** Kho chứa ngầm dưới Trạm Biên, được bảo vệ bởi trận pháp đơn giản chống trộm cắp và chống ẩm mốc.

## VIII. Kinh Tế (经济)

Kinh tế Thương Hội Bạch Lang xoay quanh ba trụ cột chính. Thứ nhất là phí hộ tống — chiếm khoảng 60% doanh thu, thu từ các thương đoàn và cá nhân cần di chuyển an toàn qua Nam Cương. Phí được tính theo mức độ nguy hiểm của tuyến đường và giá trị hàng hóa. Thứ hai là mua bán tài nguyên — Thương Hội thu mua chiến lợi phẩm, dược liệu và quặng lạ trực tiếp từ thợ săn và tán tu tại Trạm Biên với giá rẻ, sau đó bán lại cho các tông môn lớn như Cửu Hoa Kiếm Tông và Dược Vương Cốc với mức lợi nhuận đáng kể. Thứ ba là bán thông tin — mạng lưới tình báo biên giới cung cấp tin tức về tình hình yêu thú, chướng khí, hoạt động của các thế lực đen tối, được bán cho bất kỳ ai trả đủ tiền.

## IX. Lịch Sử Tóm Tắt (简史)

Thương Hội Bạch Lang được thành lập khoảng 80 năm trước bởi Bạch Lang Lão Nhân — một tán tu từng là lính đánh thuê kỳ cựu ở khu vực biên giới Nam Cương. Nhận thấy nhu cầu vận chuyển hàng hóa xuyên qua những tuyến đường nguy hiểm, ông liên kết các tán tu và thợ săn dày dạn kinh nghiệm, tạo thành tổ chức chuyên bảo kê và hộ tống. Trải qua hàng chục năm phát triển, từ một nhóm lính đánh thuê rời rạc, Thương Hội đã vươn lên thành một trong những tổ chức giao thương có thế lực tại vùng biên. Trong bối cảnh Huyết Thần Độc bùng phát và sự lũng đoạn của Vạn Độc Môn, Thương Hội trở thành một trong số ít phương tiện di chuyển an toàn rời khỏi Nam Cương. Đây cũng là tổ chức mà Lâm Phong và Diệp Tĩnh Sương đã chọn gia nhập dưới thân phận giả để che giấu tung tích và tìm đường đến Cửu Hoa Kiếm Tông.

## X. Giai Thoại & Bí Mật (轶事与秘密)

- Bạch Lang Lão Nhân đã mất tích 30 năm trước trong một chuyến hộ tống xuyên vùng Hắc Vụ — nơi không ai từng trở về. Một số tin ông đã chết, nhưng có tin đồn rằng ông vẫn còn sống, đang ẩn dật ở nơi nào đó sâu trong Nam Cương.
- Thương Hội bí mật nắm giữ một bản đồ cổ ghi lại vị trí của "Rồng Xương" — một di tích thượng cổ nằm sâu trong lòng Núi Độc Long. Không ai dám đi tìm, nhưng giá trị của bản đồ đủ để nhiều thế lực lớn sẵn sàng hủy diệt Thương Hội để chiếm đoạt.
- Gần đây, một số chuyến hàng liên tiếp bị tấn công bởi những kẻ sử dụng huyết thuật — dấu hiệu cho thấy Huyết Sát Minh đang nhắm vào tuyến thương đạo Nam Cương.

## XI. Quan Hệ Thế Lực (势力关系)

- **Cửu Hoa Kiếm Tông:** Đối tác thương mại quan trọng nhất. Thương Hội cung cấp tài nguyên biên giới (dược liệu, quặng), đổi lại nhận linh thạch và đan dược. Quan hệ ổn định dựa trên lợi ích chung.
- **Vạn Độc Môn:** Luôn duy trì thái độ cảnh giác cao độ. Thương Hội thường xuyên phải đóng "phí mãi lộ" để được yên ổn làm ăn, nhưng không ít lần xảy ra xung đột vũ trang đẫm máu khi bị cướp bóc quá mức.
- **Huyết Sát Minh:** Kẻ thù tiềm tàng nguy hiểm nhất. Các phân đà của Huyết Sát Minh thường phục kích thương đoàn trên các tuyến đường vắng để thu thập huyết khí và tài nguyên.
- **Tán Tu:** Nguồn nhân lực chính. Thương Hội cung cấp cho tán tu cơ hội kiếm tiền và sự bảo vệ tạm thời khỏi các hiểm họa ở Nam Cương, đổi lại nhận được sức chiến đấu khi cần.
