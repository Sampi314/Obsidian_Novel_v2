---
type: faction
name: Hoàng Tuyền Cứu Hộ Đội
hantu: 黄泉救护队
faction_type: Hội
alignment: 8
race: Đa chủng tộc (chủ yếu Nhân Tộc)
region: Đông Hoang
founded: 18 năm trước
founder: Bạch Cứu Mệnh
emblem: Hoang_Tuyen_Cuu_Ho_Doi.png
specialty: Cứu hộ tu sĩ, Y đạo chiến trường, Giải độc Nam Cương
economy:
- Quyên góp tự nguyện từ người được cứu
- Tài trợ từ các thế lực tôn trọng đội
- Bán dược liệu dư thừa
arcs:
  - arc: 1
    status: Hoạt động tích cực
    rank: Hạng Năm
    leader: Đội Trưởng Bạch Cứu Mệnh
    population: 40
    territory:
      - Trạm Biên Nam Cương (nhà gỗ hai tầng gần cổng bắc)
      - Vùng hoạt động bán kính 30 dặm quanh Trạm Biên
    assets:
      - name: Trạm Cứu Hộ Cổng Bắc
        type: Công Trình
      - name: Hệ thống tín hiệu khói
        type: Tài Nguyên
      - name: Nhẫn trữ vật của sư phụ (bí mật)
        type: Bảo Vật
    stats: [30, 60, 140, 40, 30, 100]
    divisions:
      - name: Đội Cứu Hộ
        role: Cứu hộ, sơ cứu và vận chuyển tu sĩ bị thương từ rừng sâu về Trạm Biên
        headcount:
          hoi_truong: 1
          pho_hoi_truong: 1
          thanh_vien: 28
          tong_quan: 10
        members:
          - character: Bạch Cứu Mệnh
            position: Đội Trưởng
            cultivation: Trúc Cơ Viên Mãn
          - character: "[Phó Đội Trưởng]"
            position: Phó Đội Trưởng
            cultivation: Trúc Cơ Trung Kỳ
            placeholder: true
          - character: "[Y Sư Nhất]"
            position: Y Sư
            cultivation: Trúc Cơ Sơ Kỳ
            placeholder: true
    relationships:
      - faction: Nam Cương Dược Sư Hội
        description: Đối tác cung cấp dược liệu giá ưu đãi, quan hệ hợp tác lâu dài dựa trên thiện chí chung.
        diplomacy:
          lien_minh: 40
          tin: 60
          uy_hiep: 0
          thuong_mai: 50
          on_oan: 30
          le_thuoc: 10
      - faction: Dược Thảo Tinh Linh Viện
        description: Nguồn cung cấp dược liệu giải độc và cầm máu chất lượng cao, Thảo Tâm Linh ưu đãi giá cho đội vì cùng lý tưởng cứu người.
        diplomacy:
          lien_minh: 30
          tin: 50
          uy_hiep: 0
          thuong_mai: 40
          on_oan: 20
          le_thuoc: 0
      - faction: Vạn Độc Môn
        description: Đội từng cứu đệ tử Vạn Độc Môn, nhờ đó môn phái này không chủ động gây khó dễ. Quan hệ trung lập đặc biệt giữa thiện và ác.
        diplomacy:
          lien_minh: 0
          tin: 10
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 20
          le_thuoc: 0
---

# Hoàng Tuyền Cứu Hộ Đội (黄泉救护队)

## I. Tổng Quan (总览)
Hoàng Tuyền Cứu Hộ Đội là tổ chức cứu hộ duy nhất hoạt động tại Trạm Biên Nam Cương, chuyên cứu giúp tu sĩ bị thương trở về từ rừng sâu mà không phân biệt chính tà, không thu phí, không hỏi danh tính. Dưới sự dẫn dắt của Đội Trưởng Bạch Cứu Mệnh — cựu quân y của một đoàn viễn chinh bị xóa sổ trong Rừng Huyết Độc — đội đã trở thành tổ chức duy nhất ở Nam Cương được cả chính đạo lẫn tà đạo tôn trọng. Với bốn mươi thành viên gồm tu sĩ và phàm nhân, đội duy trì hoạt động cứu hộ liên tục suốt mười tám năm, cứu sống hàng trăm mạng người và trở thành biểu tượng cho thiện tâm giữa vùng đất khắc nghiệt nhất Đông Hoang.

## II. Địa Lý & Tài Nguyên (地理与资源)
Trụ sở đặt tại vị trí chiến lược gần cổng bắc Trạm Biên Nam Cương — hướng mà hầu hết tu sĩ bị thương từ rừng sâu quay về. Nhà gỗ hai tầng được xây dựng chắc chắn: tầng dưới là phòng cấp cứu rộng rãi với giường bệnh, bàn phẫu thuật, và kho dược liệu; tầng trên là nơi nghỉ ngơi của đội viên. Phía sau có sân tập luyện cứu hộ, nơi cứu hộ viên mới rèn luyện kỹ năng leo trèo, chạy nhanh và vận chuyển thương binh. Tài nguyên gồm dược liệu giải độc và cầm máu cơ bản do Nam Cương Dược Sư Hội cung cấp giá ưu đãi, cáng khiêng bằng xương trùng nhẹ và bền, cùng hệ thống tín hiệu khói — mạng lưới báo động thô sơ nhưng hiệu quả trong bán kính ba mươi dặm.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
Triết lý sống của đội gói gọn trong câu: "Ở Nam Cương, không ai chết một mình nếu ta còn sống." Đây không chỉ là khẩu hiệu mà là cam kết bằng máu của mỗi đội viên khi gia nhập. Quy tắc bất di bất dịch là không thu phí cứu hộ, chỉ nhận quyên góp tự nguyện; không hỏi danh tính người được cứu; và không tham gia tranh chấp giữa các thế lực. Đội viên đeo dải băng trắng trên tay trái khi làm nhiệm vụ — ký hiệu này được mọi thế lực Nam Cương ngầm tôn trọng, kể cả sơn tặc. Tấn công người đeo băng trắng được coi là hành vi đáng khinh bỉ nhất vùng biên cương, và kẻ vi phạm sẽ bị cả chính đạo lẫn tà đạo truy sát.

## IV. Cơ Cấu Tổ Chức (组织结构)
Đứng đầu là Đội Trưởng Bạch Cứu Mệnh, cựu quân y cảnh giới Trúc Cơ Viên Mãn. Gã ở lại Nam Cương sau khi đoàn viễn chinh bị xóa sổ, cảm thấy nơi đây cần mình hơn bất kỳ đâu. Dưới gã là bốn Y Sư cảnh giới Trúc Cơ Sơ đến Trung Kỳ, có kiến thức y học và khả năng sử dụng linh lực chữa trị. Lực lượng chính gồm mười sáu Cứu Hộ Viên cảnh giới Luyện Khí, được tuyển chọn vì thể lực tốt, giỏi leo trèo và chạy nhanh trong địa hình hiểm trở. Ngoài ra có từ mười đến hai mươi Tình Nguyện Viên phàm nhân, phụ trách hậu cần, nấu ăn, giặt giũ, và chăm sóc bệnh nhân nhẹ. Tổng cộng khoảng bốn mươi người, quy mô nhỏ nhưng hoạt động hiệu quả nhờ tinh thần đoàn kết cao.

## V. Công Pháp & Trận Pháp (功法与阵法)
Đội không có công pháp chiến đấu và không tham gia bất kỳ xung đột vũ trang nào. Bạch Cứu Mệnh tu luyện "Thanh Tâm Hộ Mệnh Quyết" — một công pháp y đạo đặc biệt cho phép gã truyền linh lực sang cơ thể người khác để ổn định thương tích, cầm máu, và giải độc tạm thời. Tuy nhiên, mỗi lần sử dụng đều tổn hao tu vi bản thân, và sau mười tám năm liên tục cứu người, tu vi của gã đã suy giảm đáng kể so với đỉnh cao. Các Y Sư cũng biết vài biến thể đơn giản hơn của Thanh Tâm Hộ Mệnh Quyết, đủ để sơ cứu thương tích nhẹ. Phương tiện phòng thủ duy nhất là dải băng trắng và uy tín tích lũy suốt nhiều năm.

## VI. Đặc Sản Môn Phái (门派特产)
- **Dải Băng Trắng Cứu Hộ:** Biểu tượng được toàn Nam Cương tôn trọng, đeo trên tay trái khi làm nhiệm vụ, có tác dụng bảo vệ tốt hơn bất kỳ pháp khí nào nhờ vào uy tín của đội.
- **Thuốc Giải Độc Cấp Cứu:** Hỗn hợp dược liệu do Bạch Cứu Mệnh tự phát triển, có thể giải tạm thời hơn hai mươi loại độc phổ biến ở Nam Cương, đủ để ổn định nạn nhân trước khi đưa về trạm.
- **Cáng Xương Trùng:** Cáng khiêng làm từ xương trùng, nhẹ hơn tre nhưng bền hơn thép thường, thiết kế đặc biệt để vận chuyển thương binh qua địa hình rừng rậm hiểm trở.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Trạm Cứu Hộ Cổng Bắc:** Nhà gỗ hai tầng gần cổng bắc Trạm Biên, tầng dưới phòng cấp cứu và kho dược liệu, tầng trên nơi nghỉ của đội viên. Luôn có ít nhất hai người trực ca suốt ngày đêm.
- **Hệ Thống Tín Hiệu Khói:** Mạng lưới điểm phát tín hiệu rải rác trong bán kính ba mươi dặm quanh Trạm Biên, sử dụng khói màu đặc biệt để báo động vị trí nạn nhân cần cứu hộ.
- **Sân Tập Cứu Hộ:** Khu vực phía sau trụ sở dùng để huấn luyện cứu hộ viên mới, mô phỏng các tình huống cứu hộ trong rừng rậm, đầm lầy, và vách núi.

## VIII. Kinh Tế (经济)
Đội hoạt động phi lợi nhuận, không thu phí cứu hộ mà dựa vào quyên góp tự nguyện từ người được cứu và gia đình họ. Một số tu sĩ được cứu sống khi trở nên giàu có đã gửi tặng linh thạch và vật tư y tế, tạo thành nguồn tài trợ không ổn định nhưng đủ duy trì hoạt động cơ bản. Nam Cương Dược Sư Hội cung cấp dược liệu giá ưu đãi, và Dược Thảo Tinh Linh Viện cũng bán linh dược với giá gần như giá gốc. Ngoài ra, đội bán dược liệu dư thừa và cáng xương trùng cũ để bổ sung ngân quỹ. Tài chính luôn eo hẹp nhưng chưa bao giờ thiếu đến mức phải ngừng hoạt động.

## IX. Lịch Sử Tóm Tắt (简史)
Mười tám năm trước, Bạch Cứu Mệnh là quân y duy nhất sống sót sau khi đoàn viễn chinh bị xóa sổ trong Rừng Huyết Độc. Thay vì rời đi, gã ở lại Trạm Biên Nam Cương, bắt đầu từ việc một mình chạy ra rừng kéo xác tu sĩ bị thương về cấp cứu. Dần dần, những người có thiện tâm bị cảm động trước hành động của gã đã gia nhập, từ tu sĩ lang thang đến phàm nhân bản địa. Đội lớn dần và trở thành tổ chức duy nhất ở Nam Cương được cả chính đạo lẫn tà đạo tôn trọng. Sự kiện then chốt là khi đội cứu sống một đệ tử Vạn Độc Môn bị thương nặng — hành động này khiến ngay cả tà đạo cũng không dám gây khó dễ cho đội, vì tấn công đội cứu hộ đồng nghĩa với việc đối đầu dư luận toàn Nam Cương.

## X. Giai Thoại & Bí Mật (轶事与秘密)
Bạch Cứu Mệnh thực ra là đệ tử ruột của một cường giả Nguyên Anh đã thất tung nhiều năm trước. Chiếc nhẫn trữ vật trên tay gã chứa vài pháp khí cấp cao mà gã không bao giờ sử dụng, coi đó như di vật cuối cùng của sư phụ. Nếu gã buộc phải dùng đến, sức mạnh vượt xa cảnh giới Trúc Cơ Viên Mãn hiện tại sẽ khiến toàn Nam Cương chấn động. Một bí mật khác liên quan đến một "người" từ Mạch Ngầm mà đội từng cứu sống — kẻ đó hồi phục rồi biến mất không để lại dấu vết, chỉ để lại một viên đan dược phẩm chất kỳ lạ mà không ai trong Trạm Biên nhận ra. Bạch Cứu Mệnh cất giữ viên đan nhưng không dám sử dụng, vì gã cảm nhận được dược lực bên trong vượt xa bất cứ thứ gì gã từng thấy.

## XI. Quan Hệ Thế Lực (势力关系)
- **Nam Cương Dược Sư Hội:** Đối tác cung cấp dược liệu chính, quan hệ hợp tác lâu dài dựa trên thiện chí và lý tưởng chung về việc cứu người.
- **Dược Thảo Tinh Linh Viện:** Nguồn cung cấp linh dược chất lượng cao với giá ưu đãi, Thảo Tâm Linh coi đội cứu hộ là đối tác lý tưởng cùng chí hướng.
- **Vạn Độc Môn:** Quan hệ trung lập đặc biệt — đội từng cứu đệ tử của môn, nhờ đó Vạn Độc Môn không chủ động gây khó dễ, tạo nên một thỏa thuận bất thành văn giữa thiện và ác.
