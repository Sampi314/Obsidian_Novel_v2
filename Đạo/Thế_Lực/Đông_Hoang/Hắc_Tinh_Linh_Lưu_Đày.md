---
type: faction
name: Hắc Tinh Linh Lưu Đày
hantu: 黑精灵流放
faction_type: Bộ Lạc
alignment: -1
race: Tinh Linh Tộc (Hắc Tinh Linh)
region: Đông Hoang
founded: 300 năm trước (hình thành cộng đồng)
founder: Ám Diệp (người tổ chức đầu tiên)
emblem: Hac_Tinh_Linh_Luu_Day.png
specialty: Ám hệ dược thảo, Thích nghi bóng tối, Mộc hệ biến thể ám
economy:
- Thu hái nấm linh ám hệ và dược thảo hiếm
- Trao đổi côn trùng phát quang cho các thương nhân
- Chế tác vật phẩm từ mộc linh ám
arcs:
  - arc: 1
    status: Ẩn dật tự trị
    rank: Không Xếp Hạng
    leader: Trưởng Lão Ám Diệp
    population: 100
    territory:
      - Rìa tối phía tây Vĩnh Hằng Sâm Lâm
    assets:
      - name: Khu rừng ám cổ thụ
        type: Bí Cảnh
      - name: Vườn nấm phát quang
        type: Tài Nguyên
    stats: [30, 40, 20, 100, 35, 10]
    divisions:
      - name: Cộng Đồng Rìa Tối
        role: Sinh sống, tự vệ và quản lý lãnh thổ rìa tối Vĩnh Hằng Sâm Lâm
        headcount:
          truong_lao: 4
          chien_binh: 16
          dan_thuong: 80
        members:
          - character: Ám Diệp
            position: Trưởng Lão
            cultivation: Trúc Cơ Viên Mãn
          - character: "[Hội Đồng Nhất]"
            position: Trưởng Lão Hội Đồng
            cultivation: Trúc Cơ Trung Kỳ
            placeholder: true
          - character: "[Hội Đồng Nhị]"
            position: Trưởng Lão Hội Đồng
            cultivation: Trúc Cơ Sơ Kỳ
            placeholder: true
          - character: "[Hội Đồng Tam]"
            position: Trưởng Lão Hội Đồng
            cultivation: Trúc Cơ Sơ Kỳ
            placeholder: true
    relationships:
      - faction: Tinh Linh Vương Đình
        description: Kẻ đã lưu đày họ, quan hệ thù hận sâu sắc nhưng bất lực. Vương Đình coi Hắc Tinh Linh là tội nhân vĩnh viễn.
        diplomacy:
          lien_minh: -60
          tin: -50
          uy_hiep: 40
          thuong_mai: -80
          on_oan: -70
          le_thuoc: 0
      - faction: Bán Tinh Linh Hội
        description: Liên lạc ngầm, cùng là kẻ bị Vương Đình chối bỏ, tìm kiếm sự đồng cảm và hỗ trợ lẫn nhau.
        diplomacy:
          lien_minh: 30
          tin: 40
          uy_hiep: 0
          thuong_mai: 20
          on_oan: 0
          le_thuoc: 0
      - faction: Dược Thảo Tinh Linh Viện
        description: Thỉnh thoảng trao đổi dược thảo ám hệ hiếm, Thảo Tâm Linh không kỳ thị Hắc Tinh Linh nhưng giữ khoảng cách vì sợ liên lụy.
        diplomacy:
          lien_minh: 10
          tin: 25
          uy_hiep: 0
          thuong_mai: 30
          on_oan: 0
          le_thuoc: 0
---

# Hắc Tinh Linh Lưu Đày (黑精灵流放)

## I. Tổng Quan (总览)
Hắc Tinh Linh Lưu Đày là cộng đồng khoảng một trăm Tinh Linh bị Vương Đình đày ra rìa tối Vĩnh Hằng Sâm Lâm qua nhiều thế hệ. Những kẻ bị lưu đày — phần lớn vì tội phạm thượng, bất đồng chính kiến, hoặc đơn giản là bị chính trị nội bộ hãm hại — đã dần thích nghi với bóng tối và phát triển thành một chủng tộc phụ với đặc điểm thể chất khác biệt: da tối màu hơn, mắt phát quang nhẹ trong bóng tối. Dưới sự dẫn dắt của Trưởng Lão Ám Diệp, một Tinh Linh bị lưu đày ba trăm năm trước vì dám nói xấu Vương Đình, cộng đồng đã biến nơi trừng phạt thành quê hương, xây dựng triết lý sống riêng và nuôi dưỡng sức mạnh trong im lặng.

## II. Địa Lý & Tài Nguyên (地理与资源)
Cộng đồng cư trú tại rìa tối phía tây Vĩnh Hằng Sâm Lâm, khu vực mà ánh sáng mặt trời hiếm khi lọt qua tán cây dày đặc nhiều tầng. Đây là vùng đất bị Vương Đình bỏ mặc, coi như nơi chôn sống tội nhân. Rừng rậm tối tăm với cây cối biến dị do thiếu ánh sáng, nhiều loài cây phát triển theo hướng kỳ quái, thân xoắn và rễ lộ thiên. Nguồn sáng chính đến từ nấm phát quang mọc trên thân cây và mặt đất, tạo nên cảnh quan huyền ảo xanh lam nhạt. Tài nguyên gồm nấm linh cấp thấp nhưng số lượng dồi dào, dược thảo ám hệ hiếm có mà vùng sáng không thể trồng được, và côn trùng phát quang có giá trị trong luyện đan.
Khu vực xung quanh ẩn chứa nhiều bí mật chưa được khám phá — hang động chưa ai đến, mạch khoáng chưa ai biết, dấu tích cổ đại mà thời gian chưa kịp xóa nhòa.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
Triết lý sống của cộng đồng gói gọn trong câu: "Bóng tối không phải trừng phạt, mà là tự do." Hắc Tinh Linh đã biến ý nghĩa của sự lưu đày từ hình phạt thành cơ hội giải thoát khỏi sự kiểm soát của Vương Đình. Quy tắc quan trọng nhất là không ai hỏi tội cũ của ai — bước vào rìa tối nghĩa là bắt đầu lại từ đầu, quá khứ bị xóa sạch. Cộng đồng bảo vệ lẫn nhau trước yêu thú và hiểm nguy trong rừng tối. Phong tục đặc trưng nhất là khi một Tinh Linh lưu đày mới đến, người đó phải tự tay trồng một cây riêng — nếu cây sống thì người được ở lại, nếu cây chết thì phải rời đi, bởi rìa tối chỉ chấp nhận những kẻ sẵn lòng gắn bó với bóng tối.
Mỗi thế hệ mới được truyền dạy không chỉ kỹ năng sinh tồn mà cả câu chuyện về nguồn cội, để ngọn lửa ký ức không bao giờ tắt dù hoàn cảnh khắc nghiệt đến đâu.

## IV. Cơ Cấu Tổ Chức (组织结构)
Cộng đồng hoạt động theo mô hình bộ lạc tự trị với cơ cấu đơn giản. Đứng đầu là Trưởng Lão Ám Diệp, Tinh Linh bị lưu đày lâu nhất còn sống, đã hoàn toàn thích nghi với bóng tối và có thể nhìn rõ mọi thứ trong đêm đen tuyệt đối. Bên dưới là Hội Đồng ba Tinh Linh lưu đày lâu năm, cùng Ám Diệp thảo luận và quyết định mọi việc chung của cộng đồng. Khoảng mười sáu Tinh Linh trẻ khỏe đảm nhận vai trò tuần tra và bảo vệ, còn lại tám mươi thành viên gồm người già, trẻ em sinh tại rìa tối, và những kẻ mới bị lưu đày đang thích nghi. Không có hệ thống quân sự chính quy, mọi thành viên đều sẵn sàng chiến đấu khi cần thiết.

## V. Công Pháp & Trận Pháp (功法与阵法)
Hắc Tinh Linh không có công pháp chính thức mà tu luyện bằng biến thể thuật mộc hệ đã thích nghi với bóng tối. Công pháp này cho phép trồng cây và nuôi dưỡng thực vật mà không cần ánh sáng, dựa vào linh lực ám hệ trong đất và không khí rìa tối để thay thế quang năng. Một số Hắc Tinh Linh thế hệ thứ hai trở đi đã phát triển khả năng cảm ứng bóng tối — có thể cảm nhận mọi chuyển động trong bán kính rộng thông qua dao động linh lực trong bóng tối, hiệu quả hơn cả thị giác trong môi trường này. Về phòng thủ, cộng đồng dựa hoàn toàn vào địa hình tối tăm và hiểm trở của rìa tối, nơi mà bất kỳ kẻ xâm nhập không quen thuộc đều mất phương hướng trong vài phút.

## VI. Đặc Sản Môn Phái (门派特产)
- **Dược Thảo Ám Hệ:** Các loại thảo dược chỉ sinh trưởng trong bóng tối tuyệt đối, có dược tính đặc biệt trong lĩnh vực trị liệu thần thức và an thần, không thể tìm thấy ở bất kỳ đâu khác trong Đông Hoang.
- **Nấm Phát Quang Linh:** Nấm mọc tự nhiên tại rìa tối, phát ra ánh sáng dịu xanh lam, có tác dụng bổ trợ tu luyện thần thức khi sử dụng trong thiền định.
- **Mộc Linh Ám:** Gỗ linh từ cây trồng bằng công pháp ám hệ, có đặc tính hấp thu và tàng trữ ám khí, được một số luyện khí sư trên cạn tìm mua để chế tạo pháp khí đặc thù.
Ngoài ra, Hắc Tinh Linh Lưu Đày còn sở hữu vật phẩm có giá trị văn hóa hơn vật chất — thứ mà thương nhân bỏ qua nhưng nhà sử học trả bất cứ giá nào.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Làng Cây Rìa Tối:** Khu cư trú chính gồm các nhà cây xây quanh thân cổ thụ biến dị, hòa nhập hoàn toàn vào rừng tối, từ bên ngoài gần như không thể phát hiện.
- **Vườn Nấm Phát Quang:** Khu vực canh tác nấm linh chính, cũng là nguồn chiếu sáng tự nhiên cho cộng đồng, được chăm sóc cẩn thận để duy trì ánh sáng ổn định.
- **Đường Mòn Bóng Tối:** Hệ thống đường đi bí mật giữa các khu vực trong rìa tối, được đánh dấu bằng nấm phát quang mà chỉ mắt Hắc Tinh Linh mới nhận ra.
Toàn bộ hạ tầng mang dấu ấn đặc trưng cộng đồng — không phải xa hoa mà là thực dụng đúc kết qua nhiều thế hệ thử nghiệm.

## VIII. Kinh Tế (经济)
Kinh tế cộng đồng chủ yếu tự cung tự cấp, dựa vào thu hái nấm linh, dược thảo ám hệ, và săn bắt côn trùng phát quang trong rừng tối. Một phần nhỏ sản phẩm được trao đổi với bên ngoài thông qua những thương nhân can đảm dám vào rìa tối, hoặc qua đường liên lạc ngầm với Bán Tinh Linh Hội. Dược thảo ám hệ có giá trị cao trên thị trường nhưng cộng đồng không dám bán công khai vì sợ lộ vị trí và quy mô, chỉ trao đổi lượng nhỏ với những đối tác đáng tin cậy để đổi lấy nhu yếu phẩm mà rìa tối không sản xuất được.
Tiềm năng kinh tế vượt xa những gì đang được khai thác — sự thiếu hụt nhân lực, kiến thức thương mại, và bảo hộ chính trị khiến phần lớn giá trị vẫn nằm yên.

## IX. Lịch Sử Tóm Tắt (简史)
Vương Đình dùng rìa tối Vĩnh Hằng Sâm Lâm làm nơi lưu đày Tinh Linh phạm tội hoặc bất đồng chính kiến từ hàng ngàn năm trước. Ban đầu đây là hình phạt tàn nhẫn — đa số bị lưu đày chết trong bóng tối vì không thích nghi được. Nhưng qua hàng trăm năm, những kẻ sống sót dần thích nghi về cả thể chất lẫn tinh thần, da trở nên tối hơn, mắt phát triển khả năng nhìn trong đêm. Ba trăm năm trước, Ám Diệp bị lưu đày vì dám công khai chỉ trích chính sách bảo thủ của Vương Đình. Thay vì gục ngã, lão tổ chức những kẻ lưu đày rải rác thành cộng đồng có tổ chức, xây dựng làng cây, và biến rìa tối từ nhà tù thành quê hương. Biến đổi thể chất qua nhiều thế hệ khiến họ bị gọi là "Hắc Tinh Linh" — một danh xưng ban đầu mang tính kỳ thị nhưng cộng đồng đã tự hào đón nhận.
Mỗi thế hệ kế tiếp gánh di sản và gánh nặng thế hệ trước — nhưng cũng mang khả năng mới mà cha ông chưa từng tưởng tượng.

## X. Giai Thoại & Bí Mật (轶事与秘密)
Trong vùng sâu nhất của rìa tối có những cổ thụ còn cổ hơn cả Vĩnh Hằng Sâm Lâm, thân cây lớn đến mức mười Tinh Linh nối tay cũng không ôm hết. Ám Diệp tin rằng những cổ thụ này ẩn chứa bí mật về nguồn gốc thực sự của Tinh Linh Tộc, có thể lật đổ hoàn toàn câu chuyện chính thống mà Vương Đình truyền bá. Lão đã dành hàng trăm năm cố gắng giao tiếp với chúng nhưng chưa thành công. Một bí mật đáng lo ngại hơn là một số Hắc Tinh Linh thế hệ thứ ba đã phát triển khả năng đặc biệt mà Tinh Linh bình thường không có — khả năng thao túng bóng tối, tạo ra ảo ảnh, và thậm chí hấp thu linh lực từ bóng tối thuần túy. Nếu Vương Đình phát hiện những năng lực này, họ chắc chắn sẽ coi đó là mối đe dọa và có thể phái quân tiêu diệt cộng đồng.
Những bí mật này, nếu được tiết lộ, có thể khiến nhiều thế lực phải nhìn lại đánh giá của mình về cộng đồng nhỏ bé này — vừa là cơ hội vừa là mối nguy.

## XI. Quan Hệ Thế Lực (势力关系)
- **Tinh Linh Vương Đình:** Kẻ đã lưu đày và bỏ mặc họ. Hắc Tinh Linh mang thù hận sâu sắc nhưng không đủ sức đối đầu, chọn cách ẩn dật và phát triển âm thầm.
- **Bán Tinh Linh Hội:** Đồng minh ngầm, cùng là nạn nhân của chính sách phân biệt Vương Đình. Hai bên liên lạc bí mật, trao đổi thông tin và hỗ trợ lẫn nhau khi cần thiết.
- **Dược Thảo Tinh Linh Viện:** Thỉnh thoảng trao đổi dược thảo ám hệ, Thảo Tâm Linh là một trong số ít Tinh Linh bên ngoài không kỳ thị Hắc Tinh Linh, nhưng giữ khoảng cách vì sợ liên lụy với Vương Đình.
Nhìn tổng thể, mạng lưới quan hệ tuy mỏng manh nhưng đủ duy trì sự tồn tại — trong thế giới tu chân tàn khốc, tồn tại đã là chiến thắng.
