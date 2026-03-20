---
type: faction
name: Giáp Xác Liên Minh
hantu: 甲壳联盟
faction_type: Liên Minh
alignment: 1
race: Giáp Xác Linh (Hải Tộc)
region: Đông Hoang
founded: 50 năm trước
founder: Cương Giáp
emblem: Giap_Xac_Lien_Minh.png
specialty: Phòng thủ cương giáp, Chiến thuật biển sâu, Khai thác khoáng sản đáy biển
economy:
- Khai thác khoáng chất linh đáy biển
- Trao đổi vỏ giáp cứng cho các thế lực cần nguyên liệu rèn đúc
- Bảo vệ lãnh thổ rạn san hô thu phí đi qua
arcs:
  - arc: 1
    status: Giai đoạn xây dựng
    rank: Hạng Năm
    leader: Minh Chủ Cương Giáp
    population: 500
    territory:
      - Pháo Đài Vỏ Sò
      - Khu vực rạn san hô phía tây
    assets:
      - name: Pháo Đài Vỏ Sò
        type: Công Trình
      - name: Vỏ Sò Thượng Cổ Hải Thú
        type: Bí Cảnh
      - name: Mỏ khoáng chất linh đáy biển
        type: Tài Nguyên
    stats: [120, 80, 40, 500, 140, 30]
    divisions:
      - name: Tứ Đại Tộc Quân
        role: Bốn đơn vị chiến đấu theo loài, hợp thành lực lượng phòng thủ chính
        headcount:
          minh_chu: 1
          pho_minh_chu: 0
          truong_lao: 4
          su_gia: 0
          thanh_vien_phai: 495
        members:
          - character: Cương Giáp
            position: Minh Chủ
            cultivation: Trúc Cơ Hậu Kỳ
          - character: "[Tộc Trưởng Cua Hoàng Đế]"
            position: Trưởng Lão
            cultivation: Trúc Cơ Sơ Kỳ
            placeholder: true
          - character: "[Tộc Trưởng Tôm Hùm]"
            position: Trưởng Lão
            cultivation: Trúc Cơ Sơ Kỳ
            placeholder: true
          - character: "[Tộc Trưởng Tôm]"
            position: Trưởng Lão
            cultivation: Luyện Khí Hậu Kỳ
            placeholder: true
    relationships:
      - faction: Tiểu Ngư Nhân Thôn
        description: Hàng xóm đáy biển, quan hệ trung lập thiên tích cực, đôi khi trao đổi thực phẩm và thông tin.
        diplomacy:
          lien_minh: 20
          tin: 30
          uy_hiep: 0
          thuong_mai: 30
          on_oan: 0
          le_thuoc: 0
      - faction: Giao Nhân Hoàng Tộc
        description: Thế lực Hải Tộc lớn thường xuyên uy hiếp lãnh thổ rạn san hô, coi giáp xác linh là sinh vật hạ đẳng.
        diplomacy:
          lien_minh: -40
          tin: -30
          uy_hiep: 60
          thuong_mai: -20
          on_oan: -50
          le_thuoc: 0
      - faction: Hoang Dã Yêu Liên
        description: Liên minh yêu tộc cấp thấp trên cạn, cùng cảnh ngộ bị coi thường, có sự đồng cảm nhưng chưa liên kết chính thức do cách biệt môi trường sống.
        diplomacy:
          lien_minh: 10
          tin: 20
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 10
          le_thuoc: 0
---

# Giáp Xác Liên Minh (甲壳联盟)

## I. Tổng Quan (总览)
Giáp Xác Liên Minh là một liên minh non trẻ của các loài giáp xác linh biển — cua, tôm, tôm hùm, cua hoàng đế — tập hợp dưới sự lãnh đạo của Minh Chủ Cương Giáp, con cua linh đầu tiên khai mở linh trí trong lịch sử đáy biển phía tây. Thành lập chưa đầy năm mươi năm, liên minh vẫn đang trong giai đoạn xây dựng ban đầu, phải đối mặt với mâu thuẫn nội bộ giữa các loài và áp lực liên tục từ các thế lực Hải Tộc lớn hơn. Dù vậy, với năm trăm thành viên và Pháo Đài Vỏ Sò kiên cố, liên minh đã chứng minh rằng ngay cả những sinh vật từng chỉ là "thức ăn" cũng có thể đứng lên tự bảo vệ mình.

## II. Địa Lý & Tài Nguyên (地理与资源)
Trụ sở chính là Pháo Đài Vỏ Sò, công trình xây từ vỏ sò khổng lồ và mai cua chồng lên nhau tại vùng đáy biển rạn san hô phía tây. Tuy trông thô sơ và lộn xộn, pháo đài có độ bền đáng kinh ngạc nhờ lớp vỏ giáp xếp chồng tạo cấu trúc tổ ong tự nhiên. Pháo đài liên tục được mở rộng bằng vỏ sò và mai cua mới thu lượm, tạo nên một công trình xây dựng không bao giờ hoàn thành nhưng ngày càng kiên cố. Khu vực rạn san hô xung quanh giàu rong biển, giun biển và các loại khoáng chất linh đáy biển, là nguồn thức ăn và nguyên liệu tu luyện chính. Tuy nhiên, lãnh thổ này thường xuyên bị các thế lực Hải Tộc lớn hơn nhòm ngó và uy hiếp.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
Liên minh đề cao giá trị của vỏ giáp hơn tất cả, với câu tín điều "Giáp là mạng, mất giáp là chết" thấm sâu vào mọi khía cạnh đời sống. Nghi thức lột xác hàng năm được coi là thời khắc thiêng liêng nhất, khi mỗi giáp xác linh rời bỏ lớp vỏ cũ để khoác lên lớp vỏ mới cứng cáp hơn. Đây cũng là lúc dễ bị tổn thương nhất nên toàn liên minh thay phiên canh gác bảo vệ lẫn nhau. Dù nội bộ vẫn có mâu thuẫn giữa các loài — cua và tôm thường xuyên tranh cãi ai xứng đáng lãnh đạo hơn — nhưng trước kẻ thù chung, tất cả đoàn kết. Cương Giáp thường nói: "Một cái càng thì bẻ gãy, năm trăm cái càng thì xé nát mọi thứ."

## IV. Cơ Cấu Tổ Chức (组织结构)
Đứng đầu liên minh là Minh Chủ Cương Giáp, con cua linh lớn nhất pháo đài với mai cứng như thép và đôi càng có thể kẹp gãy pháp khí cấp thấp. Dưới Cương Giáp là Tứ Đại Tộc Trưởng, đại diện cho bốn loài chính: Cua, Tôm, Tôm Hùm, và Cua Hoàng Đế. Mỗi tộc trưởng quản lý thành viên cùng loài và chịu trách nhiệm huấn luyện chiến đấu cho bầy đàn. Năm trăm chiến binh giáp xác linh có cảnh giới từ Luyện Khí đến Trúc Cơ Sơ Kỳ, trong đó phần lớn là Luyện Khí. Các quyết định lớn được đưa ra tại Hội Nghị Vỏ Sò, nơi bốn tộc trưởng cùng Minh Chủ thảo luận và biểu quyết, nhưng khi ý kiến chia đều, quyền quyết định cuối cùng thuộc về Cương Giáp.

## V. Công Pháp & Trận Pháp (功法与阵法)
Công pháp chủ đạo là Cương Giáp Tu Luyện Pháp, phương pháp luyện vỏ giáp cứng hơn bằng cách hấp thu khoáng chất linh từ đáy biển. Tu sĩ giáp xác sẽ ngâm mình trong các mạch khoáng chất và dẫn dắt linh lực vào lớp vỏ, tăng cường độ cứng, chống va đập và kháng thuật pháp. Trận pháp đặc trưng là Giáp Trận, trong đó hàng trăm giáp xác linh xếp thành hàng tạo bức tường phòng thủ di động, lớp vỏ ngoài hấp thu và phân tán sát thương trong khi các chiến binh phía sau tung đòn phản công bằng càng và gọng kìm. Chiến thuật này đã nhiều lần đẩy lùi những kẻ xâm nhập mạnh hơn nhiều lần về cá nhân nhưng không thể chọc thủng đội hình giáp xác.

## VI. Đặc Sản Môn Phái (门派特产)
- **Giáp Xác Linh Mai:** Mai cua và vỏ tôm sau khi lột xác vẫn giữ nguyên linh lực, là nguyên liệu luyện khí thượng hạng cho các thợ rèn chế tạo khiên và áo giáp dưới nước.
- **Khoáng Chất Đáy Biển:** Các loại khoáng vật linh được liên minh khai thác từ vùng rạn san hô, đặc biệt là Hải Thiết Khoáng dùng trong luyện khí thủy hệ.
- **Keo Giáp Xác:** Chất dịch đặc biệt do giáp xác linh tiết ra khi xây pháo đài, có khả năng kết dính và chống nước cực mạnh, được một số thợ rèn trên cạn săn đón.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Pháo Đài Vỏ Sò:** Công trình phòng thủ chính, liên tục mở rộng, gồm nhiều tầng vỏ sò và mai cua chồng lên nhau với các phòng ở, kho lương, và phòng họp Hội Nghị Vỏ Sò.
- **Bãi Lột Xác An Toàn:** Khu vực được bảo vệ nghiêm ngặt nhất pháo đài, nơi giáp xác linh có thể lột xác an toàn dưới sự canh gác của đồng đội.
- **Mỏ Khoáng Rạn San Hô:** Các điểm khai thác khoáng chất linh rải rác quanh rạn san hô, mỗi điểm do một nhóm năm đến mười giáp xác canh giữ.

## VIII. Kinh Tế (经济)
Kinh tế liên minh còn thô sơ và chủ yếu dựa vào tự cung tự cấp. Nguồn thu chính đến từ việc khai thác khoáng chất linh đáy biển và bán vỏ giáp sau lột xác cho các thế lực cần nguyên liệu rèn đúc. Liên minh cũng thu phí đi qua lãnh thổ rạn san hô từ các thương nhân và du hành nhỏ lẻ, tuy nhiên thu nhập này bấp bênh vì các thế lực Hải Tộc lớn thường phớt lờ không trả. Cương Giáp đang cố gắng thiết lập quan hệ thương mại ổn định hơn với các cộng đồng đáy biển khác, nhưng vị thế thấp kém của giáp xác linh khiến đàm phán luôn bất lợi.

## IX. Lịch Sử Tóm Tắt (简史)
Từ xưa đến nay, giáp xác biển luôn nằm ở tầng đáy chuỗi thức ăn, bị mọi loài săn bắt và ăn thịt không thương tiếc. Năm mươi năm trước, Cương Giáp — một con cua biển bình thường — vô tình nuốt phải một viên linh đan rơi xuống đáy biển, từ đó khai mở linh trí và bắt đầu nhận thức được thân phận bi thảm của đồng loại. Hắn dành hai mươi năm tập hợp các giáp xác linh rải rác, thuyết phục chúng bỏ qua hiềm khích giữa các loài để liên kết tồn tại. Pháo Đài Vỏ Sò được xây dựng từ hai mươi năm trước và không ngừng mở rộng, trở thành biểu tượng cho ý chí "không muốn làm thức ăn nữa" của toàn liên minh. Dù nội bộ vẫn còn nhiều mâu thuẫn và liên minh chưa được bất kỳ thế lực lớn nào công nhận, sự tồn tại của Giáp Xác Liên Minh bản thân nó đã là một kỳ tích.

## X. Giai Thoại & Bí Mật (轶事与秘密)
Viên linh đan mà Cương Giáp nuốt phải khi còn nhỏ thực ra có nguồn gốc bí ẩn — nó rơi từ một trận chiến trên không giữa hai cường giả, và dược lực bên trong vượt xa một viên đan dược thông thường. Cương Giáp nghi ngờ mình khai mở linh trí không chỉ nhờ linh đan mà còn do tác động của một lực lượng nào đó không giải thích được. Bí mật lớn nhất nằm sâu trong Pháo Đài Vỏ Sò: chiếc vỏ sò khổng lồ mà pháo đài xây quanh thực ra là di hài vỏ của một Thượng Cổ Hải Thú, bên trong rỗng và tỏa ra linh lực cổ xưa. Cương Giáp phát hiện rằng ngồi thiền bên trong vỏ sò này giúp tu luyện nhanh hơn đáng kể, nhưng hắn giữ bí mật vì sợ nếu tin tức lọt ra ngoài, các thế lực Hải Tộc lớn sẽ không ngần ngại tiêu diệt toàn bộ liên minh để chiếm đoạt.

## XI. Quan Hệ Thế Lực (势力关系)
- **Giao Nhân Hoàng Tộc:** Thế lực Hải Tộc thống trị vùng biển, coi giáp xác linh là sinh vật hạ đẳng và thường xuyên uy hiếp lãnh thổ liên minh. Cương Giáp tránh đối đầu trực tiếp nhưng không bao giờ nhượng bộ lãnh thổ cốt lõi.
- **Tiểu Ngư Nhân Thôn:** Hàng xóm đáy biển, quan hệ hữu hảo, đôi khi trao đổi thực phẩm và thông tin về các mối đe dọa từ bên ngoài.
- **Hoang Dã Yêu Liên:** Liên minh yêu tộc cấp thấp trên cạn, cùng cảnh ngộ bị coi thường bởi các thế lực lớn. Tuy chưa liên kết chính thức do cách biệt môi trường sống, hai bên có sự đồng cảm ngầm.
