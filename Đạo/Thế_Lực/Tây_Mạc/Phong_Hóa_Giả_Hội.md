---
type: faction
name: Phong Hóa Giả Hội
hantu: 风化者会
faction_type: Hội
alignment: 3
race: Thạch Tộc
region: Tây Mạc
founded: Không rõ (Có lẽ từ khi Thạch Tộc đầu tiên già đi)
founder: Không rõ (Tự phát hình thành)
emblem: Phong_Hoa_Gia_Hoi.png
specialty: Ký Ức Thạch Khắc, Lưu trữ lịch sử Thạch Tộc
economy:
- Không có hoạt động kinh tế
- Tri thức lịch sử là tài sản duy nhất
arcs:
  - arc: 1
    status: Tồn tại yên bình (Nơi an nghỉ cuối cùng)
    rank: Không Xếp Hạng
    leader: Hội Trưởng Tàn Nham
    population: 30
    territory:
      - Đỉnh Xích Nham Sơn Mạch (Mỏm đá phẳng)
    assets:
      - name: Vách Đá Ký Ức
        type: Di Tích
      - name: Kỹ thuật Ký Ức Thạch Khắc
        type: Bí Thuật
    stats: [5, 10, 30, 30, 15, 20]
    divisions:
      - name: Hội Viên
        role: Chia sẻ kinh nghiệm, truyền lại tri thức trước khi phong hóa
        headcount:
          hoi_truong: 1
          pho_hoi_truong: 0
          thanh_vien: 29
          tong_quan: 0
        members:
          - character: Tàn Nham
            position: Hội Trưởng
            cultivation: Kim Đan (Đã suy yếu)
          - character: "[Thạch Tộc Trưởng Lão]"
            position: Thành viên
            cultivation: Trúc Cơ — Kim Đan (Đều suy yếu)
            placeholder: true
    relationships:
      - faction: Cổ Nham Bộ Lạc
        description: Nhiều thành viên Phong Hóa Giả Hội từng thuộc Cổ Nham Bộ Lạc. Bộ lạc coi hội là nơi thiêng liêng và thường gửi Thạch Tộc trẻ đến nghe chuyện.
        diplomacy:
          lien_minh: 30
          tin: 60
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 40
          le_thuoc: 0
      - faction: Sa Thạch Du Mục
        description: Thạch Tộc du mục già đôi khi tìm đến hội để kể chuyện đời trước khi phong hóa. Hội chào đón tất cả Thạch Tộc bất kể xuất thân.
        diplomacy:
          lien_minh: 10
          tin: 40
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 20
          le_thuoc: 0
      - faction: Nhân Tộc (Một số tông môn)
        description: Một số tông môn Nhân Tộc lén thu gom cát bụi từ Thạch Tộc phong hóa để luyện đan, điều khiến toàn bộ Thạch Tộc vô cùng phẫn nộ.
        diplomacy:
          lien_minh: -50
          tin: -80
          uy_hiep: 0
          thuong_mai: -100
          on_oan: -60
          le_thuoc: 0
---

# Phong Hóa Giả Hội (风化者会)

## I. Tổng Quan (总览)
Phong Hóa Giả Hội là nơi tụ họp của những Thạch Tộc già sắp bước vào giai đoạn phong hóa — cái chết tự nhiên của chủng tộc đá, khi thân xác dần nứt vỡ, bong tróc và cuối cùng tan thành cát bụi. Với khoảng ba mươi thành viên, hội không phải thế lực chiến đấu mà là bảo tàng sống của lịch sử Thạch Tộc, nơi những ký ức hàng nghìn năm được khắc vào đá trước khi vĩnh viễn biến mất cùng chủ nhân. Dưới sự chủ trì của Hội Trưởng Tàn Nham — Thạch Tộc cổ đã sống hơn hai nghìn năm — hội mang ý nghĩa thiêng liêng với mọi Thạch Tộc: không ai phải chết trong cô đơn, và không câu chuyện nào bị lãng quên.

## II. Địa Lý & Tài Nguyên (地理与资源)
Hội tọa lạc trên một mỏm đá phẳng tại đỉnh Xích Nham Sơn Mạch, nơi gió thổi quanh năm không ngừng nghỉ. Xung quanh là vách đá bị bào mòn thành những hình thù kỳ dị như tác phẩm điêu khắc tự nhiên — nhưng thực tế nhiều trong số đó là Thạch Tộc đã phong hóa hoàn toàn, thân xác hóa thành một phần của núi đá. Vách đá khắc đầy ký ức của các thế hệ Thạch Tộc, tạo thành một kho lưu trữ lịch sử khổng lồ trải dài hàng nghìn năm. Tài nguyên vật chất gần như không có — hội không cần thức ăn, nước uống hay linh thạch. Thứ duy nhất có giá trị ở đây là ký ức và kinh nghiệm của những người sắp ra đi.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
Triết lý cốt lõi của hội là "Phong hóa không phải cái chết — là trở về với cát bụi." Thạch Tộc tin rằng sự phong hóa là vòng tuần hoàn tự nhiên: sinh ra từ đá, sống như đá, và cuối cùng trở về thành cát bụi nuôi dưỡng đất đai. Bất kỳ Thạch Tộc già nào cảm thấy thân xác bắt đầu vỡ vụn đều được chào đón, không phân biệt bộ lạc hay thành phần. Phong tục quan trọng nhất là mỗi thành viên phải kể lại câu chuyện đời mình, được những Thạch Tộc khác khắc lên vách đá bằng kỹ thuật Ký Ức Thạch Khắc — để thế hệ sau chạm vào đá có thể "nhìn thấy" và "cảm nhận" toàn bộ ký ức đó. Nơi đây không có tang lễ, không có nước mắt, chỉ có sự tĩnh lặng trang nghiêm khi một Thạch Tộc hoàn tất quá trình phong hóa.

## IV. Cơ Cấu Tổ Chức (组织结构)
Hội không có cấp bậc — tất cả bình đẳng trước sự phong hóa, từ cựu trưởng lão bộ lạc đến thợ đá bình thường. Hội Trưởng Tàn Nham giữ vai trò không phải lãnh đạo mà là người chủ trì — ông sắp xếp thứ tự kể chuyện, đảm bảo mỗi ký ức được khắc đúng và đầy đủ. Khoảng ba mươi Thạch Tộc già đang sinh hoạt, tu vi dao động từ tương đương Trúc Cơ đến Kim Đan nhưng tất cả đều đã suy yếu nghiêm trọng — linh lực cạn dần theo mức độ phong hóa. Ngoài thành viên chính thức, Thạch Tộc trẻ từ các bộ lạc đôi khi đến thăm viếng, nghe chuyện và học hỏi từ các bậc tiền bối.

## V. Công Pháp & Trận Pháp (功法与阵法)
Phong Hóa Giả Hội không có công pháp chiến đấu — mục đích duy nhất của hội là chia sẻ kinh nghiệm và chuẩn bị cho cái chết. Kỹ thuật quan trọng nhất và cũng là di sản lớn nhất của hội là "Ký Ức Thạch Khắc" — phương pháp khắc ký ức trực tiếp vào đá bằng linh lực Thạch Tộc, cho phép người chạm vào đá sau này có thể "nhìn thấy" toàn bộ hình ảnh, âm thanh và cảm xúc của người khắc. Đây là kỹ thuật Thạch Tộc duy nhất có khả năng lưu trữ ký ức qua hàng nghìn năm mà không suy giảm chất lượng, và cũng là lý do vách đá quanh hội trở thành kho lưu trữ lịch sử vô giá.

## VI. Đặc Sản Môn Phái (门派特产)
- **Vách Đá Ký Ức:** Toàn bộ vách đá xung quanh mỏm đá phẳng được khắc đầy ký ức của hàng trăm thế hệ Thạch Tộc. Chạm vào bất kỳ vị trí nào đều có thể nhìn thấy một đoạn đời của ai đó — có đoạn từ hàng nghìn năm trước, khi Hoàng Sa Cổ Quốc còn tồn tại.
- **Cát Bụi Phong Hóa:** Cát bụi từ Thạch Tộc phong hóa mang linh lực đặc biệt, có giá trị dược tính cao. Tuy nhiên, việc thu gom cát bụi này bị toàn bộ Thạch Tộc coi là hành vi báng bổ tổ tiên tối thượng.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Mỏm Đá Phẳng:** Sân tụ họp tự nhiên trên đỉnh Xích Nham Sơn Mạch, đủ rộng cho vài chục Thạch Tộc ngồi thành vòng tròn. Gió thổi liên tục mang đi cát bụi từ những Thạch Tộc đang phong hóa, như một nghi thức tiễn đưa tự nhiên.
- **Vách Đá Khắc:** Hệ thống vách đá xung quanh được sử dụng như thư viện, mỗi khu vực tương ứng với một giai đoạn lịch sử. Những vách đá cũ nhất đã phong hóa đến mức ký ức bên trong trở nên mờ nhạt và đứt đoạn.

## VIII. Kinh Tế (经济)
Phong Hóa Giả Hội không có bất kỳ hoạt động kinh tế nào. Thạch Tộc không cần ăn uống, không cần linh thạch ở giai đoạn sắp phong hóa, và không có nhu cầu vật chất. Tài sản duy nhất của hội là tri thức và ký ức — thứ không thể mua bán nhưng có giá trị lịch sử vô song. Một số tông môn Nhân Tộc từng cố mua quyền tiếp cận vách đá ký ức bằng linh thạch, nhưng đều bị từ chối thẳng thừng. Chỉ có Thạch Tộc mới được phép chạm vào vách đá thiêng.

## IX. Lịch Sử Tóm Tắt (简史)
Phong Hóa Giả Hội ra đời không có ngày tháng chính xác — có lẽ từ khi Thạch Tộc đầu tiên già đi và tìm đến đồng loại để không phải chết trong cô đơn. Qua hàng nghìn năm, mỏm đá trên đỉnh Xích Nham Sơn Mạch trở thành nơi hành hương cuối cùng của mọi Thạch Tộc già. Ký ức được tích lũy trên vách đá ngày càng dày đặc, biến nơi đây thành kho lưu trữ lịch sử sống lớn nhất của chủng tộc đá. Hội Trưởng Tàn Nham, Thạch Tộc già nhất hiện tại, đã chủ trì hội suốt hơn tám trăm năm và chứng kiến hàng trăm đồng tộc hoàn tất quá trình phong hóa trước mặt ông.

## X. Giai Thoại & Bí Mật (轶事与秘密)
- Tàn Nham đã sống hơn hai nghìn năm — ông nhớ thời Hoàng Sa Cổ Quốc còn tồn tại, nhưng ký ức đã mờ nhạt và lẫn lộn. Ông đang gấp rút khắc lại những gì còn nhớ trước khi quên hết, và một số ký ức đó có thể chứa manh mối về vị trí của Lưu Sa Cổ Thành.
- Có người nói rằng cát bụi từ Thạch Tộc phong hóa mang linh lực đặc biệt — một số tông môn Nhân Tộc lén thu gom để luyện đan, điều khiến toàn bộ Thạch Tộc vô cùng phẫn nộ và coi đó là hành vi xúc phạm tổ tiên không thể tha thứ.
- Gần đây, Tàn Nham bắt đầu khắc ký ức nhanh hơn bình thường — ông cảm thấy thời gian không còn nhiều, thân xác nứt nẻ ngày càng nghiêm trọng. Có những ký ức đặc biệt ông muốn lưu lại bằng mọi giá, nhưng ông từ chối tiết lộ nội dung cho bất kỳ ai trước khi hoàn tất việc khắc.

## XI. Quan Hệ Thế Lực (势力关系)
- **Cổ Nham Bộ Lạc:** Mối quan hệ thân thiện và tôn trọng lẫn nhau. Nhiều thành viên Phong Hóa Giả Hội từng thuộc Cổ Nham, và bộ lạc thường gửi Thạch Tộc trẻ đến nghe các bậc tiền bối kể chuyện. Đại Tế Tư Bàn Thạch coi hội là nơi thiêng liêng.
- **Sa Thạch Du Mục:** Thạch Tộc du mục già đôi khi tìm đến hội để kể chuyện đời mình trước khi phong hóa. Dù phong cách sống khác biệt, trước cái chết thì mọi Thạch Tộc đều bình đẳng.
- **Nhân Tộc (Một số tông môn):** Mối quan hệ căng thẳng do hành vi thu gom cát bụi phong hóa để luyện đan. Tàn Nham đã cảnh báo rằng nếu còn tiếp tục, toàn bộ Thạch Tộc sẽ đoàn kết trả thù.
