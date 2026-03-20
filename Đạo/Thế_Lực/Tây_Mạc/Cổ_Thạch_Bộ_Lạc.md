---
type: faction
name: Cổ Thạch Bộ Lạc
hantu: 古石部落
faction_type: Bộ Lạc
alignment: 1
race: Thạch Tộc (Người Đá, Người Ngọc, Người Nham Thạch)
region: Tây Mạc
founded: Thượng Cổ Kỷ Nguyên (Sau Đại Chiến Thượng Cổ)
founder: Thạch Tổ (Khối đá linh trí nguyên thủy)
emblem: Rung_Da_Khong_Lo_Va_Thach_To.png
specialty: Bất Diệt Thạch Thể, Đại Địa Mạch Động, Đồng hóa địa hình
economy:
- Khai thác linh thạch từ Khe Nứt Dung Nham
- Trao đổi khoáng vật quý với các chủng tộc tự nhiên
- Chế tác vật liệu đá đặc chủng cho xây dựng
arcs:
  - arc: 1
    status: Ẩn cư ổn định (Trung lập, quan sát thế giới)
    rank: Hạng Ba
    leader: Trưởng Lão Hội
    population: 800
    territory:
      - Thạch Lâm Uyển (Rừng đá khổng lồ)
      - Khe Nứt Dung Nham
      - Rìa Đông Hoang và Vùng Núi Đá Tây Mạc
    assets:
      - name: Thạch Tổ (Khối đá linh trí hàng triệu năm)
        type: Thánh Địa
      - name: Thạch Lâm Uyển
        type: Công Trình
      - name: Khe Nứt Dung Nham
        type: Tài Nguyên
    stats: [1200, 1500, 800, 800, 1800, 600]
    divisions:
      - name: Trưởng Lão Hội
        role: Quản lý và định hướng bộ lạc, kết nối với Thạch Tổ
        headcount:
          truong_lao: 7
          chien_binh: 0
          dan_thuong: 0
        members:
          - character: "[Đại Trưởng Lão Vạn Niên Nham]"
            position: Đại Trưởng Lão
            cultivation: Kim Đan Hậu Kỳ (Tương đương)
            placeholder: true
          - character: "[Trưởng Lão Ngọc Tâm]"
            position: Trưởng Lão
            cultivation: Kim Đan Sơ Kỳ
            placeholder: true
      - name: Chiến Thạch Thần
        role: Lực lượng bảo vệ bộ lạc, ngăn chặn kẻ xâm phạm thánh địa
        headcount:
          truong_lao: 0
          chien_binh: 50
          dan_thuong: 0
        members:
          - character: "[Chiến Thạch Thủ Lĩnh Cương Nham]"
            position: Thủ Lĩnh
            cultivation: Trúc Cơ Viên Mãn
            placeholder: true
      - name: Dân Bộ Lạc
        role: Sinh sống trong Thạch Lâm Uyển, hấp thụ linh khí để phát triển
        headcount:
          truong_lao: 0
          chien_binh: 0
          dan_thuong: 743
        members: []
    relationships:
      - faction: Cổ Nham Bộ Lạc
        description: Cùng Thạch Tộc, tôn trọng lẫn nhau dù ít giao lưu. Coi nhau là bào tộc xa.
        diplomacy:
          lien_minh: 30
          tin: 40
          uy_hiep: 0
          thuong_mai: 20
          on_oan: 0
          le_thuoc: 0
      - faction: Sa Cự Nhân Bộ Lạc
        description: Giao lưu sức mạnh vật lý, quan hệ thân thiện giữa hai chủng tộc mạnh mẽ.
        diplomacy:
          lien_minh: 40
          tin: 50
          uy_hiep: 0
          thuong_mai: 30
          on_oan: 0
          le_thuoc: 0
      - faction: Kim Sa Thợ Mỏ Hội
        description: Cảnh giác cao độ, sẵn sàng tiêu diệt ai dám khai thác linh thạch trên thân thể Thạch Tộc.
        diplomacy:
          lien_minh: -40
          tin: -50
          uy_hiep: 70
          thuong_mai: -30
          on_oan: -40
          le_thuoc: 0
---

# Cổ Thạch Bộ Lạc (古石部落)

## I. Tổng Quan (总览)
Cổ Thạch Bộ Lạc là thế lực Thạch Tộc nguyên thủy lớn nhất tại vùng rìa Đông Hoang và Vùng Núi Đá Tây Mạc, tồn tại từ sau cuộc Đại Chiến Thượng Cổ. Bộ lạc là kết tinh của năng lượng Thổ nguyên thủy, với trung tâm linh hồn là Thạch Tổ — khối đá có linh trí hàng triệu năm tuổi nằm sâu trong Thạch Lâm Uyển. Với khoảng 800 cá thể đa dạng hình dạng từ Người Đá, Người Ngọc đến Người Nham Thạch, đây là cộng đồng Thạch Tộc đông đúc nhất còn tồn tại, mang tính chất trung lập, ẩn cư, và sở hữu sức mạnh phòng thủ gần như bất hoại nhờ bản chất thể chất đặc thù.

## II. Địa Lý & Tài Nguyên (地理与资源)
Cổ Thạch Bộ Lạc cư ngụ tại Thạch Lâm Uyển — một rừng đá khổng lồ trải rộng nơi giao giới giữa rìa Đông Hoang và Vùng Núi Đá Tây Mạc. Những cột đá cao vút trong rừng thực chất là nơi an nghỉ và thiền định của Thạch Tổ và các Trưởng Lão cổ xưa nhất. Khe Nứt Dung Nham nằm ở rìa nam lãnh địa, nơi nham thạch nóng chảy từ sâu trong lòng đất lộ ra bề mặt, là địa điểm rèn luyện thân thể chính của Thạch Tộc Nham Thạch. Toàn bộ vùng đất thấm đẫm linh khí Thổ và Kim thuộc tính, cung cấp nguồn năng lượng dồi dào cho Thạch Tộc hấp thụ và phát triển.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
Cổ Thạch Bộ Lạc tôn thờ Thạch Tổ như một vị tổ tiên thần thánh, tin rằng mọi Thạch Tộc đều sinh ra từ linh khí kết tụ trong Mạch Khoáng nguyên thủy. Triết lý sống là sự tĩnh lặng và kiên nhẫn vô hạn — Thạch Tộc không vội vã, không tham lam, chỉ tồn tại và quan sát thế giới biến đổi xung quanh mình. Phong tục quan trọng nhất là "Hồi Quy Thạch Tổ" — khi một Thạch Nhân cảm thấy đã đến lúc, sẽ đi vào Thạch Lâm Uyển sâu nhất, đứng yên và dần hóa thành một phần của rừng đá, hòa nhập vĩnh viễn với Thạch Tổ. Bộ lạc có quy tắc bất di bất dịch: ai dám khai thác linh thạch trên cơ thể Thạch Tộc hoặc xâm phạm Thạch Lâm Uyển sẽ bị tiêu diệt không thương tiếc.

## IV. Cơ Cấu Tổ Chức (组织结构)
Bộ lạc sống theo đàn và phụ thuộc vào trí tuệ của những Thạch Tộc cổ đại. Đứng đầu là Trưởng Lão Hội gồm 7 vị Thạch Nhân sống trên 10 vạn năm, mỗi vị đại diện cho một loại Thạch Tộc khác nhau. Đại Trưởng Lão Vạn Niên Nham là người kết nối trực tiếp với Thạch Tổ, truyền đạt ý chỉ của khối đá linh trí cho toàn bộ lạc. Lực lượng bảo vệ là Chiến Thạch Thần — 50 Thạch Nhân chiến binh có khả năng chiến đấu phi thường, cơ thể chính là vũ khí sắc bén và cứng rắn nhất. Phần đông dân bộ lạc là những khối đá từ nhỏ đến lớn đang dần tụ linh khí để có hình người, mỗi cá thể mất hàng ngàn năm mới hoàn thiện.

## V. Công Pháp & Trận Pháp (功法与阵法)
- **Công Pháp:** *Bất Diệt Thạch Thể* — công pháp tu luyện tối thượng của Thạch Tộc, hấp thụ linh khí Thổ và Kim từ quặng mỏ để gia cố thân thể đến mức gần như bất hoại. *Đại Địa Mạch Động* — kỹ thuật kết nối với mạch đất để cảm nhận mọi rung động trong phạm vi rộng.
- **Trận Pháp:** Thạch Tộc không sử dụng trận pháp theo cách truyền thống. Thay vào đó, họ có khả năng *Đồng Hóa Địa Hình* — biến thân thể thành một phần của núi non, điều khiển cát đá trong phạm vi lớn, và tạo ra rung chấn đủ mạnh để hủy diệt công trình. Khi cả bộ lạc phối hợp, sức mạnh tập thể có thể thay đổi cả địa hình khu vực.
- **Đặc Tính:** Thạch Tộc miễn nhiễm tự nhiên với độc tố và huyễn thuật, khiến phần lớn các thủ đoạn thông thường hoàn toàn vô hiệu trước họ.

## VI. Đặc Sản Môn Phái (门派特产)
- **Ngọc Thạch Tâm:** Loại ngọc kết tinh từ lõi thân thể Thạch Tộc Ngọc sau khi họ "Hồi Quy Thạch Tổ", chứa linh lực Thổ thuần khiết cực cao, là nguyên liệu luyện đan hàng đầu.
- **Nham Thạch Nguyên Chất:** Khoáng vật đặc biệt chỉ có tại Khe Nứt Dung Nham, cứng hơn huyền thiết gấp nhiều lần, là vật liệu luyện khí hệ Kim-Thổ tối thượng.
- **Thạch Tộc Giáp Phiến:** Mảnh giáp đá rơi tự nhiên từ thân Chiến Thạch Thần, có thể dùng làm hộ giáp hạng nhất cho Nhân Tộc.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Thạch Lâm Uyển:** Rừng đá khổng lồ trung tâm bộ lạc, nơi Thạch Tổ an nghỉ và các Trưởng Lão thiền định. Mỗi cột đá trong rừng đều mang linh trí.
- **Khe Nứt Dung Nham:** Địa điểm rèn luyện thân thể cho Thạch Tộc Nham Thạch, nơi nham thạch nóng chảy lộ ra bề mặt, nhiệt độ đủ cao để tôi luyện cơ thể đá.
- **Đại Sảnh Thạch Tổ:** Hang động khổng lồ bao quanh Thạch Tổ, nơi tổ chức hội họp quan trọng của Trưởng Lão Hội.

## VIII. Kinh Tế (经济)
Cổ Thạch Bộ Lạc không có nền kinh tế thương mại theo nghĩa thông thường. Thạch Tộc "ăn" linh khí từ đá và khoáng vật, không cần thức ăn hay nước uống như các chủng tộc khác. Thỉnh thoảng, bộ lạc trao đổi khoáng vật quý hiếm khai thác từ Khe Nứt Dung Nham với các chủng tộc tự nhiên thân thiện như Cự Tộc để lấy thông tin về thế giới bên ngoài. Hoạt động chế tác vật liệu đá đặc chủng cũng diễn ra nhỏ lẻ, chủ yếu phục vụ nội bộ. Triết lý kinh tế là "lấy vừa đủ, không khai thác cạn kiệt".

## IX. Lịch Sử Tóm Tắt (简史)
Cổ Thạch Bộ Lạc được sinh ra từ Mạch Khoáng linh khí sau cuộc Đại Chiến Thượng Cổ — khi năng lượng Thổ nguyên thủy kết tinh thành những khối đá đầu tiên có linh trí. Thạch Tổ là khối đá nguyên thủy nhất, đã tồn tại hàng triệu năm và là trung tâm linh hồn cho toàn bộ chủng tộc. Qua vô số kỷ nguyên, Cổ Thạch Bộ Lạc đã chứng kiến sự ra đời và diệt vong của nhiều chủng tộc khác mà vẫn sừng sững tồn tại nhờ bản chất bất hoại đặc trưng. Tuy nhiên, tỉ lệ sinh cực kỳ thấp — mỗi cá thể Thạch Tộc mới cần hàng ngàn năm để hình thành — khiến dân số tăng trưởng rất chậm, và mối đe dọa lớn nhất không phải kẻ thù bên ngoài mà là sự cạn kiệt linh khí trong các mạch khoáng do hoạt động khai thác ngày càng tăng của Nhân Tộc.

## X. Giai Thoại & Bí Mật (轶事与秘密)
Truyền thuyết bộ lạc kể rằng Thạch Tổ không chỉ là khối đá linh trí thông thường mà thực chất là tàn tích của một vị thần Thổ cổ đại đã hy sinh trong Đại Chiến Thượng Cổ — xương cốt thần linh hóa thành đá, thần trí tan vào khoáng mạch, và từ đó Thạch Tộc ra đời. Những Trưởng Lão cổ xưa nhất thỉnh thoảng "nghe" được tiếng thì thầm từ Thạch Tổ, nhưng nội dung luôn mơ hồ và khó hiểu, như ký ức rời rạc của một thực thể đã mất phần lớn ý thức. Gần đây, Chiến Thạch Thần phát hiện dấu vết của nhóm người lạ đào bới gần rìa Thạch Lâm Uyển — nghi ngờ liên quan đến hoạt động khai thác mỏ mở rộng, khiến Trưởng Lão Hội bắt đầu thảo luận về việc phá bỏ chính sách trung lập kéo dài hàng vạn năm.

## XI. Quan Hệ Thế Lực (势力关系)
| Thế Lực | Quan Hệ | Mô Tả |
|---|---|---|
| Cổ Nham Bộ Lạc | Bào tộc | Cùng Thạch Tộc, tôn trọng lẫn nhau |
| Sa Cự Nhân Bộ Lạc | Thân thiện | Giao lưu sức mạnh vật lý, cùng hệ tự nhiên |
| Kim Sa Thợ Mỏ Hội | Cảnh giác | Sẵn sàng tiêu diệt nếu xâm phạm thánh địa |
