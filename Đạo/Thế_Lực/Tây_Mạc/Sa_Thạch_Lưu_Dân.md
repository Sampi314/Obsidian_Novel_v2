---
type: faction
name: Sa Thạch Lưu Dân
hantu: 砂石流民
faction_type: Hội
alignment: 4
race: Thạch Tộc (Bị phong hóa)
region: Tây Mạc
founded: Năm Khởi Nguyên 97.950
founder: Sa Tàn
emblem: Vien_Da_Nut_Giua_Bui_Cat.png
specialty: Không có (Thạch Tộc bị phong hóa mất khả năng tu luyện)
economy:
  - Nhặt nhạnh mảnh linh thạch vụn từ mỏ bỏ hoang
  - Thu gom nước mưa đọng trong hốc đá
arcs:
  - arc: 1
    status: Lang thang (Tìm kiếm phương pháp chữa trị phong hóa)
    rank: Không Xếp Hạng
    leader: Trưởng Đoàn Sa Tàn
    population: 40
    territory:
      - Vùng mỏ đá bỏ hoang Đông Hoang (lang thang, không cố định)
    assets:
      - name: Thạch Tộc trẻ có khả năng nghịch chuyển phong hóa
        type: Nhân Tài
    stats: [5, 5, 10, 40, 5, 5]
    divisions:
      - name: Đoàn Lưu Dân
        role: Toàn bộ đoàn di chuyển cùng nhau, bảo vệ và chăm sóc lẫn nhau
        headcount:
          hoi_truong: 1
          pho_hoi_truong: 0
          thanh_vien: 36
          tong_quan: 3
        members:
          - character: Sa Tàn
            position: Trưởng Đoàn
            cultivation: Trúc Cơ (tương đương, suy yếu do phong hóa)
          - character: "[Hộ Vệ Thạch Kiên]"
            position: Hộ Vệ
            cultivation: Luyện Khí Hậu Kỳ (tương đương)
            placeholder: true
          - character: "[Thạch Tộc Trẻ Nghịch Chuyển]"
            position: Thành Viên Đặc Biệt
            cultivation: Không rõ
            placeholder: true
    relationships:
      - faction: Cổ Nham Bộ Lạc
        description: Lưu dân từng xin Cổ Nham che chở nhưng bị từ chối vì Cổ Nham sợ phong hóa "lây nhiễm". Mối quan hệ đau lòng giữa đồng tộc.
        diplomacy:
          lien_minh: -10
          tin: -20
          uy_hiep: 0
          thuong_mai: 0
          on_oan: -30
          le_thuoc: 0
      - faction: Sa Thạch Du Mục
        description: Sa Thạch Du Mục thỉnh thoảng chia sẻ khoáng linh dư thừa cho lưu dân, nhưng cũng giữ khoảng cách vì sợ phong hóa. Tình thương có nhưng nỗi sợ cũng có.
        diplomacy:
          lien_minh: 10
          tin: 10
          uy_hiep: 0
          thuong_mai: 10
          on_oan: -10
          le_thuoc: 10
      - faction: Phong Hóa Giả Hội
        description: Phong Hóa Giả Hội nghiên cứu hiện tượng phong hóa từ góc nhìn học thuật, đôi khi tìm đến lưu dân để quan sát. Sa Tàn chấp nhận hợp tác với hy vọng tìm được cách chữa trị.
        diplomacy:
          lien_minh: 20
          tin: 20
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 10
---

# Sa Thạch Lưu Dân (砂石流民)

## I. Tổng Quan (总览)

Sa Thạch Lưu Dân là cộng đồng khoảng bốn mươi Thạch Tộc bị phong hóa, lang thang giữa các mỏ đá bỏ hoang và vùng hoang mạc đá Đông Hoang. Họ không phải thế lực theo nghĩa thông thường mà là một nhóm lưu dân bị chính đồng tộc xa lánh, quây quần bên nhau để tồn tại. Trưởng Đoàn Sa Tàn, một Thạch Tộc bị phong hóa nửa thân nhưng ý chí kiên cường, đã tập hợp lưu dân từ năm mươi năm trước và dẫn họ lang thang tìm kiếm phương pháp chữa trị. Dù yếu ớt và thiếu thốn mọi thứ, đoàn vẫn duy trì tinh thần không từ bỏ hy vọng, được thể hiện qua triết lý "Dù thân vỡ vụn, linh hồn vẫn còn."

## II. Địa Lý & Tài Nguyên (地理与资源)

Sa Thạch Lưu Dân không có lãnh thổ cố định. Họ lang thang giữa các mỏ đá bỏ hoang và vùng hoang mạc đá Đông Hoang, nơi cảnh quan hoang tàn với đá phong hóa và cát bụi mịn trải dài. Tài nguyên gần như không có: nguồn sống chủ yếu là mảnh linh thạch vụn nhặt nhạnh từ mỏ bỏ hoang mà Nhân Tộc đã khai thác xong, và nước mưa đọng trong hốc đá. Đối với Thạch Tộc, khoáng linh là thức ăn duy trì thân xác, nhưng Thạch Tộc phong hóa hấp thu khoáng linh kém hiệu quả hơn nhiều so với bình thường, phần lớn năng lượng bị rò rỉ qua các vết nứt trên thân. Tình trạng này tạo ra vòng luẩn quẩn đau đớn: càng thiếu khoáng linh thì phong hóa càng nhanh, càng phong hóa thì hấp thu càng kém.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)

Triết lý sống của Sa Thạch Lưu Dân là: "Dù thân vỡ vụn, linh hồn vẫn còn." Đây không phải câu nói sáo rỗng mà là niềm tin thật sự của những Thạch Tộc đang từng ngày chứng kiến thân xác mình tan rã. Quy tắc duy nhất nhưng bất di bất dịch là chia sẻ mọi thứ tìm được và không bỏ rơi đồng tộc, dù người đó đã vỡ nát quá nửa thân. Khi một Thạch Tộc phong hóa hoàn toàn và vỡ thành cát, cả đoàn dừng lại, gom mảnh vụn chôn cất cẩn thận và cùng hát bài ai ca cổ truyền từ đời Thạch Tộc nguyên thủy. Nghi thức tang lễ giản dị này là khoảnh khắc trang nghiêm nhất của đoàn, nhắc nhở mỗi thành viên rằng họ cũng sẽ có ngày đó, nhưng cho đến khi đó, họ phải sống.

## IV. Cơ Cấu Tổ Chức (组织结构)

Cơ cấu cực kỳ đơn giản, phản ánh tình trạng khốn khó của đoàn. Đứng đầu là Trưởng Đoàn Sa Tàn, Thạch Tộc bị phong hóa nửa thân, một bên cơ thể đã nứt nẻ lộ lớp cát bên trong nhưng ý chí không hề suy giảm. Tu vi của Sa Tàn tương đương Trúc Cơ nhưng đã suy yếu đáng kể do phong hóa. Ba Thạch Tộc hộ vệ còn tương đối nguyên vẹn đảm nhận vai trò bảo vệ những kẻ yếu nhất trong đoàn, dẫn đường và cảnh giới. Ba mươi sáu Thạch Tộc còn lại bị phong hóa ở các mức độ khác nhau, từ nứt nhẹ đến gần tan rã, mỗi người đều cố gắng đóng góp theo khả năng còn lại của mình.

## V. Công Pháp & Trận Pháp (功法与阵法)

Sa Thạch Lưu Dân không có công pháp và trận pháp. Phong hóa khiến thân thể Thạch Tộc không thể tu luyện bình thường vì khoáng linh hấp thu vào sẽ rò rỉ qua các vết nứt trước khi kịp chuyển hóa. Ngay cả Nham Giáp Thuật cơ bản của Thạch Tộc cũng không thể sử dụng vì lớp ngoài thân thể đã bị bong tróc. Khả năng chiến đấu của đoàn gần như bằng không, họ dựa hoàn toàn vào việc di chuyển vào những vùng mà không ai muốn đến, những mỏ bỏ hoang và hoang mạc cằn cỗi, để tránh xung đột. Tuy nhiên, trong đoàn có một Thạch Tộc trẻ phát triển khả năng kỳ lạ: biến cát thành đá tạm thời, hoàn toàn nghịch lại với hiện tượng phong hóa. Khả năng này vẫn yếu và không ổn định, nhưng là tia hy vọng duy nhất của cả đoàn.

## VI. Đặc Sản Môn Phái (门派特产)

- **Cát Phong Hóa:** Cát bụi sinh ra khi thân xác Thạch Tộc phong hóa, vẫn còn chứa vi lượng linh lực đặc thù. Một số dược sư và luyện đan sư tìm kiếm loại cát này vì nó có tính chất đặc biệt khi pha vào đan dược hệ Thổ, nhưng lưu dân hiếm khi bán vì coi đó là xương thịt đồng tộc.
- **Ai Ca Thạch Tộc:** Bài hát tang lễ cổ xưa, truyền miệng từ đời này sang đời khác. Không có giá trị vật chất nhưng là di sản văn hóa quý giá cuối cùng mà lưu dân còn giữ được.

## VII. Cơ Sở Hạ Tầng (基础设施)

- **Không có cơ sở hạ tầng cố định.** Đoàn lưu dân sống trong hang đá bỏ hoang hoặc hốc đá tự nhiên, di chuyển liên tục. Khi dừng chân, Thạch Tộc hộ vệ tạo ra những bức tường đá thấp tạm thời để che chắn gió cho đồng tộc yếu nhất.
- **"Nghĩa Trang Di Động":** Mỗi khi một Thạch Tộc vỡ hoàn toàn, mảnh vụn được gom vào một chiếc bao đá do Sa Tàn mang theo. Đây vừa là nơi an nghỉ của đồng tộc, vừa là gánh nặng trên vai Trưởng Đoàn, nhắc nhở ông về trách nhiệm tìm cách cứu những người còn sống.

## VIII. Kinh Tế (经济)

Kinh tế của Sa Thạch Lưu Dân ở mức sinh tồn tối thiểu, thấp nhất trong mọi thế lực Tây Mạc. Nguồn sống chính là mảnh linh thạch vụn nhặt nhạnh từ mỏ bỏ hoang, thứ mà Nhân Tộc coi là phế phẩm nhưng với Thạch Tộc phong hóa là cứu cánh sống còn. Đôi khi Sa Thạch Du Mục thương tình chia sẻ chút khoáng linh dư thừa, nhưng số lượng quá ít và không thường xuyên. Đoàn không có gì để trao đổi thương mại ngoài cát phong hóa, thứ mà bản thân họ coi là xương thịt đồng tộc và không muốn bán. Tình trạng kinh tế bấp bênh này khiến mỗi ngày tồn tại đều là một phép màu nhỏ.

## IX. Lịch Sử Tóm Tắt (简史)

Hiện tượng phong hóa Thạch Tộc là một bí ẩn tồn tại từ lâu đời. Cơ thể đá dần nứt vỡ, bong tróc, biến thành cát, không thể đảo ngược bằng bất kỳ phương pháp nào đã biết. Nguyên nhân chưa rõ ràng: có giả thuyết cho rằng do linh khí suy kiệt, bệnh tật, hoặc thậm chí là tàn dư của một lời nguyền từ thời Thượng Cổ. Những Thạch Tộc mắc phải hiện tượng này bị đồng loại e ngại và xa lánh vì sợ "lây nhiễm", dù chưa có bằng chứng phong hóa có thể lây.

Sa Tàn, bản thân cũng là nạn nhân phong hóa, tập hợp lưu dân từ năm mươi năm trước khi nhận ra không ai khác sẽ giúp họ. Từ đó, đoàn lang thang không ngừng, vừa nhặt nhạnh linh thạch vụn để tồn tại, vừa tìm kiếm bất kỳ manh mối nào về phương pháp chữa trị. Năm mươi năm qua, nhiều thành viên đã vỡ hoàn toàn, nhưng cũng có vài Thạch Tộc phong hóa mới gia nhập, giữ cho đoàn không hoàn toàn biến mất.

## X. Giai Thoại & Bí Mật (轶事与秘密)

Sa Tàn tin rằng phong hóa không phải bệnh tự nhiên mà là tàn dư của một lời nguyền từ Thượng Cổ, có thể liên quan đến sự sụp đổ của một nền văn minh Thạch Tộc cổ đại. Ông đã dành cả đời tìm kiếm manh mối về nguồn gốc lời nguyền, tin rằng nếu tìm được thì có thể tìm cách giải trừ. Tuy nhiên, năm mươi năm trôi qua mà chưa có kết quả.

Bí mật lớn nhất và cũng là hy vọng lớn nhất của đoàn nằm ở một Thạch Tộc trẻ bị phong hóa nhưng lại phát triển khả năng kỳ lạ: biến cát thành đá tạm thời, hoàn toàn ngược lại với hiện tượng phong hóa. Khả năng này vẫn yếu, không ổn định và chỉ kéo dài vài khắc, nhưng Sa Tàn coi đây là bằng chứng rằng phong hóa có thể đảo ngược. Ông bảo vệ Thạch Tộc trẻ này như bảo vật, sợ bất kỳ thế lực nào bên ngoài biết được và muốn đem đi nghiên cứu.

## XI. Quan Hệ Thế Lực (势力关系)

- **Cổ Nham Bộ Lạc:** Mối quan hệ đau lòng nhất. Lưu dân từng xin Cổ Nham che chở nhưng bị Đại Tế Tư Bàn Thạch từ chối vì sợ phong hóa lây lan. Cả hai đều là Thạch Tộc, nhưng nỗi sợ đã đặt lên trên tình đồng tộc.
- **Sa Thạch Du Mục:** Bộ lạc du mục thỉnh thoảng chia sẻ khoáng linh dư thừa cho lưu dân khi gặp trên đường, nhưng cũng giữ khoảng cách vì lo ngại phong hóa. Tình thương có, nỗi sợ cũng có, tạo nên mối quan hệ nửa gần nửa xa.
- **Phong Hóa Giả Hội:** Tổ chức nghiên cứu hiện tượng phong hóa từ góc nhìn học thuật. Đôi khi tìm đến lưu dân để quan sát và ghi chép. Sa Tàn chấp nhận hợp tác vì hy vọng nghiên cứu của họ có thể dẫn đến phương pháp chữa trị, dù đến nay chưa có kết quả thực tế.
