---
type: faction
name: Cổ Tích Cự Nhân Thức Tỉnh
hantu: 古迹巨人觉醒
faction_type: Bộ Lạc
alignment: 0
race: Cự Tộc (Cổ đại)
region: Tây Mạc
founded: Không xác định (Thức tỉnh gần đây từ phong ấn cổ đại)
founder: Không có (Cộng đồng tự phát sau khi tỉnh dậy)
emblem: Cu_Nhan_Giua_Phe_Tich.png
specialty: Kỹ thuật chiến đấu cổ đại thất truyền, Trận pháp cổ Lưu Sa Cổ Thành, Cổ ngữ
economy:
- Tự cung tự cấp từ tài nguyên trong phế tích
- Khai thác vật liệu xây dựng cổ đại còn dư linh lực
- Săn bắt sinh vật trong Lưu Sa Khu
arcs:
  - arc: 1
    status: Hoang mang tìm hiểu (Mới thức tỉnh, chưa hòa nhập)
    rank: Không Xếp Hạng
    leader: Trưởng Lão Cổ Mộng
    population: 25
    territory:
      - Phế tích phía đông Lưu Sa Cổ Thành
    assets:
      - name: Phế tích Lưu Sa Cổ Thành
        type: Công Trình
      - name: Mảnh trận pháp cổ thành (còn kích hoạt một phần)
        type: Trận Pháp
      - name: Pháp khí cổ hư hỏng
        type: Pháp Bảo
    stats: [30, 15, 10, 25, 20, 5]
    divisions:
      - name: Hội Đồng Tỉnh Thức
        role: Duy trì tinh thần cộng đồng và tìm hiểu thế giới mới
        headcount:
          truong_lao: 3
          chien_binh: 0
          dan_thuong: 0
        members:
          - character: Cổ Mộng
            position: Trưởng Lão
            cultivation: Kim Đan (Tương đương, suy yếu)
          - character: "[Cự Nhân Im Lặng]"
            position: Thành Viên
            cultivation: Trúc Cơ Viên Mãn (Suy yếu)
            placeholder: true
      - name: Cộng Đồng Tỉnh Thức
        role: Sinh tồn và phục hồi trong phế tích
        headcount:
          truong_lao: 0
          chien_binh: 7
          dan_thuong: 15
        members: []
    relationships:
      - faction: Cổ Tích Thám Hiểm Đoàn
        description: Đang cố gắng tiếp cận để học cổ ngữ, nhưng Cự Nhân cổ đại chưa tin tưởng Nhân Tộc.
        diplomacy:
          lien_minh: 0
          tin: -20
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 0
      - faction: Cổ Sa Yêu Tộc
        description: Sự thức tỉnh của Cự Nhân khiến Cổ Sa lo ngại sâu sắc, quá khứ đang trỗi dậy.
        diplomacy:
          lien_minh: 0
          tin: -30
          uy_hiep: 0
          thuong_mai: 0
          on_oan: -40
          le_thuoc: 0
      - faction: Hoàng Sa Di Dân
        description: Hậu duệ phàm nhân của Cổ Quốc, Cự Nhân chưa biết về sự tồn tại của họ.
        diplomacy:
          lien_minh: 0
          tin: 0
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 10
          le_thuoc: 0
---

# Cổ Tích Cự Nhân Thức Tỉnh (古迹巨人觉醒)

## I. Tổng Quan (总览)
Cổ Tích Cự Nhân Thức Tỉnh là cộng đồng nhỏ bé gồm 25 Cự Nhân cổ đại vừa tỉnh dậy từ phong ấn bí ẩn trong Lưu Sa Cổ Thành — phế tích thuộc thời Hoàng Sa Cổ Quốc đã sụp đổ hàng ngàn năm trước. Đây không phải một thế lực có tổ chức mà là một nhóm sinh vật hoang mang, cô đơn và sợ hãi, đang cố gắng hiểu một thế giới hoàn toàn xa lạ mà họ không còn nhận ra. Dù hiện tại rất suy yếu do giấc ngủ dài, tiềm năng chiến đấu thực sự của họ nếu hồi phục hoàn toàn sẽ vượt xa mọi thế lực nhỏ ở Tây Mạc, khiến sự thức tỉnh này trở thành sự kiện đáng chú ý.

## II. Địa Lý & Tài Nguyên (地理与资源)
Cự Nhân cư ngụ trong phế tích phía đông Lưu Sa Cổ Thành — một cổ thành khổng lồ đã bị cát phủ một nửa, với kiến trúc được xây dựng theo kích thước Cự Tộc. Đá xây dựng trong thành tuy đã phong hóa nhưng vẫn còn dư linh lực đáng kể. Tuy nhiên, vị trí nằm sâu trong Lưu Sa Khu — một trong những vùng nguy hiểm nhất Tây Mạc — khiến việc tiếp cận từ bên ngoài cực kỳ khó khăn. Tài nguyên chủ yếu là di vật cổ trong thành, phần lớn không còn dùng được, cùng một vài pháp khí cổ hư hỏng mà không ai biết cách sửa chữa.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
Triết lý hiện tại của nhóm Cự Nhân là "Chúng ta ngủ một giấc — thế giới đã thay đổi hoàn toàn", phản ánh sự bàng hoàng sâu sắc trước thực tại. Quy tắc tạm thời là không rời Cổ Thành cho đến khi hiểu được thế giới hiện tại đủ để tự bảo vệ. Mỗi ngày, cả cộng đồng tụ họp để kể cho nhau nghe những gì mình nhớ từ trước khi bị phong ấn — những mảnh ký ức rời rạc và đôi khi mâu thuẫn nhau. Nhiều Cự Nhân bị nỗi sợ hãi chi phối — sợ thế giới mới, sợ không tìm thấy đồng loại, sợ thứ gì đó mà họ không dám nói ra từ ký ức cổ đại.

## IV. Cơ Cấu Tổ Chức (组织结构)
Không có cấp bậc rõ ràng — cộng đồng đang trong giai đoạn hoang mang tìm hiểu, mọi quyết định đều dựa trên sự đồng thuận mong manh. Trưởng Lão Cổ Mộng tự nhiên trở thành người dẫn dắt nhờ tu vi cao nhất (tương đương Kim Đan, dù đã suy yếu sau giấc ngủ dài) và ký ức phong phú nhất về thời Cổ Quốc. Tuy nhiên, ký ức của ông lẫn lộn giữa quá khứ và hiện tại, đôi khi nói những câu không ai hiểu bằng ngôn ngữ cổ đại. 25 Cự Nhân còn lại có tu vi từ Trúc Cơ đến Kim Đan nhưng tất cả đều suy yếu nghiêm trọng. Đặc biệt, họ giao tiếp bằng ngôn ngữ cổ mà Nhân Tộc hiện đại không thể hiểu.

## V. Công Pháp & Trận Pháp (功法与阵法)
- **Công Pháp:** Cự Nhân cổ đại sở hữu kỹ thuật chiến đấu đã hoàn toàn thất truyền trong thế giới hiện đại. Tuy nhiên, thân xác suy yếu sau giấc ngủ dài khiến họ không thể sử dụng đầy đủ sức mạnh. Nếu hồi phục hoàn toàn, năng lực chiến đấu sẽ vượt xa mọi thế lực nhỏ ở Tây Mạc.
- **Trận Pháp:** Một vài Cự Nhân còn nhớ được mảnh trận pháp bảo vệ Cổ Thành xưa, nhưng chỉ kích hoạt được một phần nhỏ. Phần trận pháp còn hoạt động đủ để tạo ra lớp phòng thủ sơ đẳng quanh khu vực sinh sống, nhưng không thể so với nguyên bản.

## VI. Đặc Sản Môn Phái (门派特产)
- **Cổ Ngữ Hoàng Sa:** Ngôn ngữ cổ đại từ thời Hoàng Sa Cổ Quốc, chỉ có Cự Nhân thức tỉnh mới nói được — vô giá đối với việc giải mã bia đá và di tích cổ trên toàn Tây Mạc.
- **Kiến Thức Kiến Trúc Cổ Đại:** Ký ức về cách xây dựng công trình theo kích thước Cự Tộc với kỹ thuật linh khí gia cố, đã thất truyền hoàn toàn ở thế giới hiện đại.
- **Ký Ức Cổ Quốc:** Những mảnh ký ức rời rạc về Hoàng Sa Cổ Quốc thời hưng thịnh — thông tin mà bất kỳ nhà nghiên cứu cổ sử nào cũng sẵn sàng trả giá đắt để có được.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Phế Tích Cổ Thành:** Các tòa nhà đổ nát theo kích thước Cự Tộc, một nửa bị cát phủ nhưng vẫn đủ che chắn cho cộng đồng nhỏ bé.
- **Quảng Trường Tụ Họp:** Khu vực trung tâm phế tích nơi Cự Nhân tụ tập mỗi ngày để chia sẻ ký ức và thảo luận.
- **Khu Phong Ấn Cũ:** Nơi Cự Nhân từng bị phong ấn, vẫn còn dấu tích của trận pháp cổ đại đã suy yếu đến mức vỡ vụn.

## VIII. Kinh Tế (经济)
Cổ Tích Cự Nhân Thức Tỉnh không có bất kỳ hoạt động kinh tế nào. Cộng đồng sống hoàn toàn dựa vào những gì tìm được trong phế tích và việc săn bắt sinh vật trong Lưu Sa Khu. Vị trí nằm sâu trong vùng nguy hiểm khiến việc giao thương với bên ngoài gần như bất khả thi, và bản thân Cự Nhân cũng chưa sẵn sàng tiếp xúc với thế giới hiện đại. Đây là tình trạng sinh tồn cơ bản nhất, không có tích lũy hay phát triển.

## IX. Lịch Sử Tóm Tắt (简史)
Nhóm 25 Cự Nhân này bị phong ấn trong Lưu Sa Cổ Thành từ thời Hoàng Sa Cổ Quốc, trong hoàn cảnh mà không ai trong số họ nhớ rõ ràng — ai phong ấn và vì sao vẫn là câu hỏi chưa có lời giải. Gần đây, do biến động linh mạch bất thường trong Lưu Sa Khu, phong ấn suy yếu và họ lần lượt tỉnh dậy. Thế giới bên ngoài hoàn toàn xa lạ — ngôn ngữ đã thay đổi, chủng tộc mới xuất hiện, Hoàng Sa Cổ Quốc từng hùng mạnh giờ chỉ còn là phế tích chìm trong cát. Trưởng Lão Cổ Mộng cố gắng giữ vững tinh thần cho cả cộng đồng, nhưng bản thân ông cũng đang chìm trong hoang mang và những mảnh ký ức lẫn lộn không thể sắp xếp.

## X. Giai Thoại & Bí Mật (轶事与秘密)
Trưởng Lão Cổ Mộng thỉnh thoảng nói những câu không ai hiểu bằng ngôn ngữ cổ đại, như thể đang trò chuyện với ai đó vô hình mà chỉ ông nhìn thấy — không rõ đó là ký ức lẫn lộn hay ông thực sự giao tiếp với một thực thể bí ẩn. Trong số 25 Cự Nhân tỉnh dậy, có 3 người từ chối nói bất kỳ điều gì — họ chỉ ngồi yên và nhìn chằm chằm về phía Vĩnh Tịch Chi Địa với ánh mắt sợ hãi tột cùng, như thể nhìn thấy điều gì đó trong ký ức mà họ không dám diễn tả bằng lời. Cổ Tích Thám Hiểm Đoàn đã bắt đầu cố gắng tiếp cận để học cổ ngữ và tìm hiểu lịch sử, nhưng rào cản ngôn ngữ và sự bất tín nhiệm sâu sắc của Cự Nhân đối với Nhân Tộc khiến quá trình này cực kỳ chậm chạp.

## XI. Quan Hệ Thế Lực (势力关系)
| Thế Lực | Quan Hệ | Mô Tả |
|---|---|---|
| Cổ Tích Thám Hiểm Đoàn | Dè chừng | Đang cố tiếp cận, nhưng Cự Nhân chưa tin tưởng |
| Cổ Sa Yêu Tộc | Bất an ngầm | Sự thức tỉnh gây lo ngại cho Yêu Tộc cổ đại |
| Hoàng Sa Di Dân | Chưa biết đến | Cùng gốc Cổ Quốc nhưng chưa gặp nhau |
