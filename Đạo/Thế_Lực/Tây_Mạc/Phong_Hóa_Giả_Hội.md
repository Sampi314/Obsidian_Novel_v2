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

> *"Phong hóa không phải cái chết — là trở về với cát bụi, là gửi ký ức vào lòng đất, là ngủ trong gió vạn năm."*
> — Hội Trưởng Tàn Nham, lời tụng đọc trong nghi thức tiễn đưa

> *"Mỗi hạt cát trên Xích Nham từng là một phần của ai đó. Ngươi đang đứng trên vai tổ tiên — hãy kể cho ta nghe chuyện của ngươi, để tổ tiên không cô đơn."*
> — Tàn Nham, nói với mỗi Thạch Tộc mới đến

## I. Tổng Quan (总览)
Phong Hóa Giả Hội là nơi tụ họp của những Thạch Tộc già sắp bước vào giai đoạn phong hóa — cái chết tự nhiên của chủng tộc đá, khi thân xác dần nứt vỡ, bong tróc và cuối cùng tan thành cát bụi. Với khoảng ba mươi thành viên, hội không phải thế lực chiến đấu mà là bảo tàng sống của lịch sử Thạch Tộc, nơi những ký ức hàng nghìn năm được khắc vào đá trước khi vĩnh viễn biến mất cùng chủ nhân.

Dưới sự chủ trì của Hội Trưởng Tàn Nham — Thạch Tộc cổ đã sống hơn hai nghìn năm — hội mang ý nghĩa thiêng liêng với mọi Thạch Tộc: không ai phải chết trong cô đơn, và không câu chuyện nào bị lãng quên. Nơi đây là điểm đến cuối cùng trên hành trình ngàn năm của những tảng đá biết đi, biết nghĩ, biết nhớ — và biết kể lại trước khi trở về thành cát bụi.

## II. Địa Lý & Tài Nguyên (地理与资源)
Hội tọa lạc trên một mỏm đá phẳng tại đỉnh Xích Nham Sơn Mạch, ở độ cao ba nghìn trượng nơi gió thổi quanh năm không ngừng nghỉ — gió ở đây mang theo cát bụi sa mạc và mùi đất khô, Thạch Tộc gọi ngọn gió đó là "Phong Hóa Phong," ngọn gió tiễn đưa.

Xung quanh là vách đá bị bào mòn thành những hình thù kỳ dị như tác phẩm điêu khắc tự nhiên — nhưng thực tế nhiều trong số đó là Thạch Tộc đã phong hóa hoàn toàn, thân xác hóa thành một phần của núi đá, dáng vẻ tọa thiền hay đứng trầm ngâm vẫn còn phảng phất. Có nơi, hai Thạch Tộc hóa đá đứng cạnh nhau tay nắm tay — truyền thuyết kể họ là đôi bạn đồng hành suốt sáu trăm năm, cùng phong hóa trong một ngày. Con đường leo núi dẫn lên đỉnh Xích Nham mang tên Thiên Bộ Đạo — bào mòn nhẵn bóng bởi hàng vạn bước chân đá qua bao thế kỷ, mỗi bước chân để lại vết trũng nhỏ trên đá cứng.

Vách đá khắc đầy ký ức của các thế hệ Thạch Tộc, trải dài hơn ba trăm trượng bao quanh mỏm đá, tạo thành một kho lưu trữ lịch sử khổng lồ trải dài hàng nghìn năm. Tài nguyên vật chất gần như không có — hội không cần thức ăn, nước uống hay linh thạch. Thứ duy nhất có giá trị ở đây là ký ức và kinh nghiệm của những người sắp ra đi, cùng ngọn gió vĩnh hằng mang cát bụi phong hóa bay khắp Tây Mạc.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
Triết lý cốt lõi của hội là "Phong hóa không phải cái chết — là trở về với cát bụi." Thạch Tộc tin rằng sự phong hóa là vòng tuần hoàn tự nhiên: sinh ra từ đá, sống như đá, và cuối cùng trở về thành cát bụi nuôi dưỡng đất đai — cát bụi đó theo gió bay đi, một ngày sẽ lắng đọng thành đá mới, và từ đá mới lại sinh ra Thạch Tộc mới.

Bất kỳ Thạch Tộc già nào cảm thấy thân xác bắt đầu vỡ vụn đều được chào đón, không phân biệt bộ lạc, thành phần, hay quá khứ — kể cả Thạch Tộc từng phạm tội nặng cũng được phép đến kể chuyện đời trước khi đi.

Phong tục quan trọng nhất là nghi thức "Thạch Ngữ": mỗi thành viên phải kể lại câu chuyện đời mình trước vòng tròn đồng tộc, được những Thạch Tộc khác khắc lên vách đá bằng kỹ thuật Ký Ức Thạch Khắc — để thế hệ sau chạm vào đá có thể "nhìn thấy" và "cảm nhận" toàn bộ ký ức đó. Nghi thức kéo dài từ vài ngày đến vài tuần tùy theo độ dài cuộc đời người kể, và không ai được phép ngắt lời — dù câu chuyện có nhàm chán đến đâu, vì mọi cuộc đời đều đáng được lắng nghe.

Nơi đây không có tang lễ, không có nước mắt, chỉ có sự tĩnh lặng trang nghiêm khi một Thạch Tộc hoàn tất quá trình phong hóa — cát bụi từ thân xác được gió cuốn đi, vòng tròn còn lại ngồi im lặng cho đến khi hạt cát cuối cùng biến mất trong chân trời.

## IV. Cơ Cấu Tổ Chức (组织结构)
Hội không có cấp bậc — tất cả bình đẳng trước sự phong hóa, từ cựu trưởng lão bộ lạc đến thợ đá bình thường. Hội Trưởng Tàn Nham giữ vai trò không phải lãnh đạo mà là người chủ trì — ông sắp xếp thứ tự Thạch Ngữ, đảm bảo mỗi ký ức được khắc đúng và đầy đủ, kiểm tra vách đá cũ xem ký ức nào đang mờ nhạt cần tu bổ.

Khoảng ba mươi Thạch Tộc già đang sinh hoạt, tu vi dao động từ tương đương Trúc Cơ đến Kim Đan nhưng tất cả đều đã suy yếu nghiêm trọng. Trong số ba mươi người, có Thạch Phong — cựu Tộc Trưởng Sa Thạch Du Mục, người đã đi bộ qua toàn bộ Tây Mạc ba lần trong đời; Ngọc Nham — cựu thợ đá tinh xảo nhất Cổ Nham, người khắc ký ức rõ nét nhất; và Thiết Thạch — cựu chiến binh già nhất, thân đã nứt đến mức chỉ còn một cánh tay cử động được nhưng vẫn cố kể nốt câu chuyện về trận đại chiến với yêu thú sa mạc hai trăm năm trước.

Ngoài thành viên chính thức, Thạch Tộc trẻ từ các bộ lạc đôi khi đến thăm viếng — Tàn Nham luôn dặn họ: "Hãy nghe cho kỹ, vì mỗi câu chuyện chỉ được kể một lần."

## V. Công Pháp & Trận Pháp (功法与阵法)
Phong Hóa Giả Hội không có công pháp chiến đấu — mục đích duy nhất của hội là chia sẻ kinh nghiệm và chuẩn bị cho cái chết. Kỹ thuật quan trọng nhất và cũng là di sản lớn nhất của hội là "Ký Ức Thạch Khắc" — phương pháp khắc ký ức trực tiếp vào đá bằng linh lực Thạch Tộc, cho phép người chạm vào đá sau này có thể "nhìn thấy" toàn bộ hình ảnh, âm thanh và cảm xúc của người khắc.

Quá trình khắc đòi hỏi người thực hiện phải chạm tay vào vách đá và truyền linh lực liên tục trong nhiều giờ, mỗi lần khắc tiêu hao đáng kể lượng linh lực cuối cùng của Thạch Tộc già, đẩy nhanh quá trình phong hóa — vì vậy mỗi lần khắc ký ức đều là sự hy sinh thật sự. Ngọc Nham — thợ khắc tài giỏi nhất hiện tại — cho biết bí quyết là "không khắc bằng tay mà khắc bằng lòng — tay chỉ là cầu nối, ký ức tự tìm đường vào đá."

Đây là kỹ thuật Thạch Tộc duy nhất có khả năng lưu trữ ký ức qua hàng nghìn năm mà không suy giảm chất lượng. Một số vách đá cổ nhất mang ký ức từ thời Hoàng Sa Cổ Quốc còn thịnh vượng — nhưng đá cũng phong hóa theo thời gian, và những ký ức đó đang dần mờ nhạt không thể phục hồi.

## VI. Đặc Sản Môn Phái (门派特产)
**Vách Đá Ký Ức** là di sản quý giá nhất — toàn bộ vách đá xung quanh mỏm đá phẳng được khắc đầy ký ức của hàng trăm thế hệ Thạch Tộc, chia thành bảy khu vực theo niên đại. Chạm vào bất kỳ vị trí nào đều có thể nhìn thấy một đoạn đời của ai đó — có đoạn từ hàng nghìn năm trước, khi Hoàng Sa Cổ Quốc còn tồn tại, ghi lại hình ảnh thành phố sa mạc huy hoàng với tháp vàng chạm mây mà ngày nay chỉ còn là phế tích.

Khu vực ký ức cổ nhất mang tên "Thạch Sử Bích" nằm ở vách phía bắc, đá đã nứt nẻ và ký ức bên trong lập lờ như giấc mơ sắp tan — Tàn Nham cố gắng tu bổ mỗi năm nhưng sức ông ngày càng yếu.

**Cát Bụi Phong Hóa** từ Thạch Tộc phong hóa mang linh lực đặc biệt, có giá trị dược tính cao — khi hòa vào đan dược, tăng cường độ cứng của kinh mạch và xương cốt người uống. Tuy nhiên, việc thu gom cát bụi này bị toàn bộ Thạch Tộc coi là hành vi báng bổ tổ tiên tối thượng — Tàn Nham từng nói: "Ai lấy cát bụi tổ tiên ta, đó là kẻ mổ xẻ linh hồn."

## VII. Cơ Sở Hạ Tầng (基础设施)
**Mỏm Đá Phẳng** là sân tụ họp tự nhiên trên đỉnh Xích Nham Sơn Mạch, đường kính khoảng mười trượng, đủ rộng cho ba mươi Thạch Tộc ngồi thành vòng tròn. Trung tâm vòng tròn có một hốc nhỏ tự nhiên gọi là "Tâm Thạch," nơi người kể chuyện ngồi khi thực hiện nghi thức Thạch Ngữ — hốc đá đã mòn nhẵn bởi hàng ngàn người từng ngồi đó qua bao thế kỷ.

Gió thổi liên tục mang đi cát bụi từ những Thạch Tộc đang phong hóa, như một nghi thức tiễn đưa tự nhiên — vào những ngày gió lớn, cát bụi bay thành dải vàng óng ánh trong nắng chiều, đẹp đến xót xa.

**Vách Đá Khắc** là hệ thống vách đá xung quanh được sử dụng như thư viện, chia thành bảy khu vực: Khu Thượng Cổ, Khu Cổ Quốc, Khu Chiến Tranh, Khu Du Mục, Khu Nghệ Nhân, Khu Chiến Binh, và Khu Phàm Thường — mỗi khu tương ứng với một loại ký ức. Những vách đá cũ nhất ở Khu Thượng Cổ đã phong hóa đến mức ký ức bên trong trở nên mờ nhạt và đứt đoạn, khiến Tàn Nham lo lắng rằng lịch sử xa xưa nhất sẽ vĩnh viễn mất đi.

## VIII. Kinh Tế (经济)
Phong Hóa Giả Hội không có bất kỳ hoạt động kinh tế nào. Thạch Tộc không cần ăn uống, không cần linh thạch ở giai đoạn sắp phong hóa, và không có nhu cầu vật chất. Tài sản duy nhất của hội là tri thức và ký ức — thứ không thể mua bán nhưng có giá trị lịch sử vô song.

Một số tông môn Nhân Tộc từng cố mua quyền tiếp cận vách đá ký ức bằng linh thạch — có ghi chép rằng Thiên Sa Thương Hội từng đề nghị một nghìn linh thạch trung phẩm để được xem ký ức về vị trí Lưu Sa Cổ Thành — nhưng đều bị từ chối thẳng thừng. Tàn Nham trả lời: "Ký ức tổ tiên không có giá — không phải vì rẻ, mà vì quá quý để định giá." Chỉ có Thạch Tộc mới được phép chạm vào vách đá thiêng, ngoại trừ trường hợp đặc biệt được Hội Trưởng đích thân cho phép — trong lịch sử hội, ngoại lệ này chỉ xảy ra hai lần.

## IX. Lịch Sử Tóm Tắt (简史)
Phong Hóa Giả Hội ra đời không có ngày tháng chính xác — có lẽ từ khi Thạch Tộc đầu tiên già đi và tìm đến đồng loại để không phải chết trong cô đơn. Truyền thuyết kể rằng Thạch Tộc đầu tiên tìm đến mỏm đá này là Sơ Nham — một chiến binh cổ đại sống sót qua đại chiến Hoàng Sa, leo lên đỉnh Xích Nham với thân xác nứt nẻ, ngồi xuống và khắc câu chuyện đời mình vào đá trước khi phong hóa thành bụi.

Qua hàng nghìn năm, mỏm đá trở thành nơi hành hương cuối cùng của mọi Thạch Tộc già. Ký ức được tích lũy trên vách đá ngày càng dày đặc, biến nơi đây thành kho lưu trữ lịch sử sống lớn nhất của chủng tộc đá. Hội Trưởng Tàn Nham đã chủ trì hội suốt hơn tám trăm năm và chứng kiến hàng trăm đồng tộc hoàn tất quá trình phong hóa trước mặt ông — ông nhớ tên từng người, từng câu chuyện, từng hạt cát cuối cùng bay đi trong gió.

## X. Giai Thoại & Bí Mật (轶事与秘密)
Tàn Nham đã sống hơn hai nghìn năm — ông nhớ thời Hoàng Sa Cổ Quốc còn tồn tại, khi thành Hoàng Sa vàng rực như mặt trời giữa sa mạc. Tuy nhiên ký ức đã mờ nhạt và lẫn lộn — tên vua, tên tướng, và lý do Cổ Quốc sụp đổ trộn lẫn thành mớ hỗn độn. Ông đang gấp rút khắc lại những gì còn nhớ trước khi quên hết, và một số ký ức đó có thể chứa manh mối về vị trí của Lưu Sa Cổ Thành — kinh đô bị vùi lấp dưới cát mà vô số tu sĩ và thương hội đang săn lùng.

Gần đây, Tàn Nham bắt đầu khắc ký ức nhanh hơn bình thường — ông cảm thấy thời gian không còn nhiều, thân xác nứt nẻ ngày càng nghiêm trọng, cánh tay trái đã vỡ mất hai ngón, và mỗi sáng ông phải dùng đất sét đắp lại những mảnh vỡ mới. Có những ký ức đặc biệt ông muốn lưu lại bằng mọi giá nhưng từ chối tiết lộ nội dung cho bất kỳ ai trước khi hoàn tất — Ngọc Nham nghi rằng đó là ký ức liên quan đến nguyên nhân thực sự khiến Hoàng Sa Cổ Quốc diệt vong.

Có người nói rằng cát bụi từ Thạch Tộc phong hóa mang linh lực đặc biệt — một số tông môn Nhân Tộc, đặc biệt là chi nhánh phía tây của Dược Vương Cốc, lén cử đệ tử đến thu gom để luyện đan, điều khiến toàn bộ Thạch Tộc vô cùng phẫn nộ. Tàn Nham đã hai lần bắt quả tang đệ tử Nhân Tộc thu gom cát bụi và đuổi đi — lần thứ nhất bằng lời cảnh cáo, lần thứ hai bằng cú đấm cuối cùng mà cánh tay phải ông còn đủ sức vung ra.

## XI. Quan Hệ Thế Lực (势力关系)
- **Cổ Nham Bộ Lạc:** Mối quan hệ thân thiện và tôn trọng lẫn nhau. Nhiều thành viên Phong Hóa Giả Hội từng thuộc Cổ Nham, và bộ lạc thường gửi Thạch Tộc trẻ đến nghe các bậc tiền bối kể chuyện. Đại Tế Tư Bàn Thạch coi hội là nơi thiêng liêng, mỗi năm đích thân mang một tảng đá mới từ bộ lạc lên để mở rộng khu vách đá khắc.
- **Sa Thạch Du Mục:** Thạch Tộc du mục già đôi khi tìm đến hội để kể chuyện đời mình trước khi phong hóa. Dù phong cách sống khác biệt, trước cái chết thì mọi Thạch Tộc đều bình đẳng, và ký ức của người du mục thường mang đến góc nhìn khác biệt quý giá — Thạch Phong từng kể liên tục mười hai ngày đêm về những vùng đất xa xôi mà không ai trong hội từng đặt chân đến.
- **Nhân Tộc (Một số tông môn):** Mối quan hệ căng thẳng do hành vi thu gom cát bụi phong hóa để luyện đan. Tàn Nham đã cảnh báo rằng nếu còn tiếp tục, toàn bộ Thạch Tộc sẽ đoàn kết trả thù — đó không phải lời nói suông, vì dù yếu ớt sắp chết, ba mươi Thạch Tộc già sẵn sàng phong hóa đồng loạt tạo thành bão cát linh lực đủ chôn vùi kẻ xâm phạm.