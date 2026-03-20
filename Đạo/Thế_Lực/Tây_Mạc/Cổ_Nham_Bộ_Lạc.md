---
type: faction
name: Cổ Nham Bộ Lạc
hantu: 古岩部落
faction_type: Bộ Lạc
alignment: 3
race: Thạch Tộc
region: Tây Mạc
founded: Thái Cổ Kỷ Nguyên
founder: Nham Thần (truyền thuyết)
emblem: Dinh_Nui_Lua_Va_Vien_Huyen_Vu_Nham.png
specialty: Nham Thần Chú, Cứng hóa cực độ, Kích hoạt mạch nham thạch
economy:
- Khai thác linh thạch từ mạch nham cổ đại
- Trao đổi suối khoáng nóng cho các bộ lạc lân cận
- Chế tác vật liệu nham thạch đặc chủng
arcs:
  - arc: 1
    status: Suy thoái dần (Dân số giảm, tỉ lệ sinh cực thấp)
    rank: Hạng Tư
    leader: Đại Tế Tư Bàn Thạch
    population: 200
    territory:
      - Đỉnh Xích Nham Sơn Mạch (đỉnh núi thiêng)
      - Suối khoáng nóng bên trong núi
    assets:
      - name: Miệng Núi Lửa Tắt (Thánh Địa Nham Thần)
        type: Thánh Địa
      - name: Mạch Nham Thạch Cổ Đại
        type: Tài Nguyên
      - name: Tường Đá Tự Nhiên
        type: Trận Pháp
    stats: [300, 400, 350, 200, 450, 200]
    divisions:
      - name: Tế Tư Đoàn
        role: Chủ trì nghi lễ Nham Thần, giáo dục và duy trì tín ngưỡng bộ lạc
        headcount:
          truong_lao: 5
          chien_binh: 0
          dan_thuong: 0
        members:
          - character: Bàn Thạch
            position: Đại Tế Tư
            cultivation: Kim Đan (Tương đương)
          - character: "[Tế Tư Huyền Nham]"
            position: Tế Tư
            cultivation: Trúc Cơ Viên Mãn
            placeholder: true
      - name: Thủ Vệ Đoàn
        role: Canh giữ con đường duy nhất lên đỉnh núi thiêng
        headcount:
          truong_lao: 0
          chien_binh: 20
          dan_thuong: 0
        members:
          - character: "[Thủ Vệ Trưởng Nham Giáp]"
            position: Thủ Vệ Trưởng
            cultivation: Trúc Cơ Trung Kỳ
            placeholder: true
      - name: Dân Bộ Lạc
        role: Sinh sống trên và trong lòng núi, khai thác nham thạch
        headcount:
          truong_lao: 0
          chien_binh: 0
          dan_thuong: 175
        members: []
    relationships:
      - faction: Sa Thạch Du Mục
        description: Coi là "người anh em lạc lối", muốn họ quay về thờ Nham Thần nhưng không ép buộc.
        diplomacy:
          lien_minh: 20
          tin: 30
          uy_hiep: 0
          thuong_mai: 10
          on_oan: 0
          le_thuoc: 0
      - faction: Địa Tâm Thám Hiểm Đội
        description: Từ chối cho phép đào sâu dưới đỉnh thiêng, quan hệ lạnh nhạt.
        diplomacy:
          lien_minh: -10
          tin: -20
          uy_hiep: 0
          thuong_mai: 0
          on_oan: -30
          le_thuoc: 0
      - faction: Cổ Thạch Bộ Lạc
        description: Cùng chủng tộc Thạch Tộc, tôn trọng lẫn nhau nhưng ít qua lại do cách biệt địa lý.
        diplomacy:
          lien_minh: 30
          tin: 40
          uy_hiep: 0
          thuong_mai: 20
          on_oan: 0
          le_thuoc: 0
---

# Cổ Nham Bộ Lạc (古岩部落)

## I. Tổng Quan (总览)
Cổ Nham Bộ Lạc là bộ lạc Thạch Tộc cổ xưa nhất tại Xích Nham Sơn Mạch, tự nhận là hậu duệ trực tiếp của Nham Thần — thực thể mà họ tin đã tạo ra mọi Thạch Tộc từ nham thạch nóng chảy. Bộ lạc chiếm giữ đỉnh cao nhất của sơn mạch, nơi đá đỏ chuyển sang đen, lấy miệng núi lửa đã tắt làm thánh địa. Với khoảng 200 Thạch Tộc còn sống, đây là một cộng đồng đang trên đà suy thoái do tỉ lệ sinh cực thấp, nhưng vẫn giữ vững niềm tin tâm linh mãnh liệt và sở hữu sức mạnh phòng thủ đáng nể nhờ địa thế hiểm trở tự nhiên.

## II. Địa Lý & Tài Nguyên (地理与资源)
Cổ Nham Bộ Lạc đóng trên đỉnh cao nhất của Xích Nham Sơn Mạch, nơi nham thạch cổ đại chuyển từ sắc đỏ sang sắc đen huyền bí. Đỉnh núi là một cao nguyên phẳng tự nhiên hiếm có, xung quanh là vực sâu thăm thẳm, chỉ có một con đường đá duy nhất dẫn lên — địa thế hoàn hảo cho phòng thủ. Bên trong lòng núi ẩn chứa hệ thống suối khoáng nóng phong phú, cung cấp nước và khoáng chất cho cả bộ lạc. Mạch nham thạch cổ đại tại đây chứa linh lực dồi dào, là nguồn dinh dưỡng tâm linh mà Thạch Tộc cần để duy trì thân xác đá đặc thù của mình.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
Toàn bộ đời sống tinh thần của Cổ Nham Bộ Lạc xoay quanh Nham Thần — thực thể sáng tạo theo tín ngưỡng truyền đời. Triết lý cốt lõi là "Nham Thần tạo ra Thạch Tộc — Thạch Tộc phải trở về với Nham Thần", thể hiện niềm tin rằng cái chết không phải kết thúc mà là sự hồi quy về cội nguồn. Mỗi năm, bộ lạc tổ chức đại tế lễ Nham Thần, hiến dâng viên linh thạch quý nhất vào miệng núi lửa đã tắt trên đỉnh thiêng. Đỉnh núi được coi là bất khả xâm phạm, tuyệt đối không ai được khai thác đá tại đây. Bộ lạc cũng coi Sa Thạch Du Mục là "người anh em lạc lối" đã quên mất Nham Thần, và luôn mong muốn họ quay về con đường tín ngưỡng đúng đắn.

## IV. Cơ Cấu Tổ Chức (组织结构)
Bộ lạc được dẫn dắt bởi Đại Tế Tư Bàn Thạch — một Thạch Tộc cổ xưa với thân xác bằng huyền vũ nham, giao tiếp chậm rãi và trầm mặc. Bàn Thạch là Đại Tế Tư đời thứ mười bảy, sở hữu tu vi tương đương Kim Đan, và ông lo lắng mình có thể là đời cuối cùng do không tìm được người kế nhiệm xứng đáng. Dưới ông là 4 Tế Tư tương đương Trúc Cơ Viên Mãn, phụ trách nghi lễ và giáo dục. 20 Thạch Tộc chiến binh hợp thành Thủ Vệ Đoàn, ngày đêm canh giữ con đường duy nhất lên đỉnh. Phần còn lại là dân bộ lạc sinh sống trên bề mặt và trong lòng núi.

## V. Công Pháp & Trận Pháp (功法与阵法)
- **Công Pháp:** *Nham Thần Chú* — nghi thức cầu nguyện thiêng liêng giúp Thạch Tộc cứng hóa thân xác đến mức cực độ trong thời gian ngắn, biến toàn thân thành huyền vũ nham bất khả phá. Chỉ có Đại Tế Tư và các Tế Tư được truyền dạy bản hoàn chỉnh.
- **Trận Pháp:** *Nham Mạch Kích Hoạt Trận* — kỹ thuật kích hoạt mạch nham thạch ngầm để tạo ra tường đá tự nhiên dựng lên từ mặt đất, chặn đứng kẻ xâm nhập. Kết hợp với địa thế hiểm trở, khả năng phòng thủ của đỉnh núi gần như bất khả công.
- **Bí Truyền:** Truyền thuyết nói rằng Đại Tế Tư có thể "đánh thức" toàn bộ ngọn núi nếu bộ lạc bị đe dọa diệt vong, nhưng cái giá phải trả là gì thì không ai biết.

## VI. Đặc Sản Môn Phái (门派特产)
- **Huyền Vũ Nham Khối:** Loại nham thạch đặc biệt chỉ có trên đỉnh núi thiêng, cứng hơn thép thường gấp nhiều lần, được các thợ rèn Tây Mạc khao khát nhưng bộ lạc cấm khai thác.
- **Suối Khoáng Nham Thần:** Nước suối khoáng nóng bên trong lòng núi, có tác dụng phục hồi thân xác Thạch Tộc bị nứt vỡ và tăng cường linh lực cho khoáng vật.
- **Nham Thần Hương:** Loại hương đốt chế từ bột đá nghiền và dược liệu núi đá, dùng trong tế lễ, có tác dụng trấn tĩnh thần thức.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Đỉnh Thiêng Nham Thần:** Cao nguyên phẳng trên đỉnh núi, nơi đặt bàn tế và miệng núi lửa tắt — trung tâm tín ngưỡng của toàn bộ lạc.
- **Nham Động Quần Cư:** Hệ thống hang động được đục mở trong lòng núi, nơi cư ngụ chính của Thạch Tộc, kết nối với suối khoáng nóng.
- **Đường Đá Độc Đạo:** Con đường duy nhất dẫn từ chân núi lên đỉnh, hẹp và cheo leo, được 20 thủ vệ canh giữ nghiêm ngặt.

## VIII. Kinh Tế (经济)
Cổ Nham Bộ Lạc không theo đuổi lợi nhuận thương mại. Kinh tế của họ dựa trên sự tự cung tự cấp từ mạch nham thạch cổ đại và suối khoáng nóng bên trong lòng núi. Thỉnh thoảng, bộ lạc trao đổi linh thạch thô và nước khoáng nóng với các cộng đồng Thạch Tộc lân cận để lấy thông tin hoặc vật liệu đặc thù. Tuy nhiên, nguyên tắc "không khai thác đỉnh thiêng" khiến nguồn tài nguyên khai thác được ngày càng hạn chế, góp phần vào tình trạng suy thoái chung.

## IX. Lịch Sử Tóm Tắt (简史)
Cổ Nham Bộ Lạc tự nhận là Thạch Tộc nguyên thủy, tồn tại từ trước khi Nhân Tộc đặt chân đến Tây Mạc. Theo truyền thuyết, Nham Thần đã nặn ra những Thạch Tộc đầu tiên từ nham thạch nóng chảy trong lòng núi lửa, và ban cho họ linh trí để canh giữ ngọn núi thiêng. Qua hàng ngàn năm, bộ lạc trải qua nhiều thời kỳ thịnh suy. Từng có lúc dân số lên đến hàng ngàn, nhưng tỉ lệ sinh cực thấp đặc trưng của Thạch Tộc khiến số lượng giảm dần không thể cứu vãn. Bàn Thạch, Đại Tế Tư đời thứ mười bảy, là vị lãnh đạo già nhất và cô đơn nhất trong lịch sử bộ lạc — ông vừa lo giữ gìn tín ngưỡng, vừa phải đối mặt với nguy cơ tuyệt diệt chủng tộc ngay trước mắt.

## X. Giai Thoại & Bí Mật (轶事与秘密)
Miệng núi lửa tắt trên đỉnh thiêng không hoàn toàn "tắt" như người ta nghĩ. Đôi khi từ dưới vực sâu vọng lên tiếng gầm rất nhẹ, Đại Tế Tư Bàn Thạch gọi đó là "Nham Thần Thở" — nhưng liệu đó thực sự là hơi thở của thần linh hay chỉ là hoạt động địa chất, không ai dám khẳng định. Bàn Thạch tin rằng nếu Nham Thần thức tỉnh hoàn toàn, Xích Nham Sơn Mạch sẽ phun trào dữ dội và mọi Thạch Tộc sẽ được "tái sinh" trong nham thạch nóng chảy — nhưng kèm theo đó là sự hủy diệt toàn bộ vùng đất xung quanh. Địa Tâm Thám Hiểm Đội của Thâm Nham từng xin phép được đào sâu dưới đỉnh thiêng để nghiên cứu cội nguồn Thạch Tộc, nhưng bị Bàn Thạch từ chối thẳng thừng — kể từ đó quan hệ hai bên trở nên lạnh nhạt, và Bàn Thạch bắt đầu coi Thâm Nham là kẻ "phỉ báng Nham Thần".

## XI. Quan Hệ Thế Lực (势力关系)
| Thế Lực | Quan Hệ | Mô Tả |
|---|---|---|
| Sa Thạch Du Mục | Huynh đệ xa cách | Coi là "anh em lạc lối", muốn họ quay về Nham Thần |
| Địa Tâm Thám Hiểm Đội | Lạnh nhạt | Từ chối cho đào sâu dưới đỉnh thiêng |
| Cổ Thạch Bộ Lạc | Tôn trọng | Cùng Thạch Tộc, ít qua lại nhưng kính trọng lẫn nhau |
