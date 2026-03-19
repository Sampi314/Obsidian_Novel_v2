---
type: faction
name: Sa Cự Nhân Bộ Lạc
hantu: 沙巨人部落
faction_type: Bộ Lạc
alignment: 2
race: Cự Tộc (Sa Cự Nhân)
region: Tây Mạc
founded: Trước thời Nhân Tộc đến Tây Mạc
founder: Không rõ (Bộ lạc nguyên thủy)
emblem: Sa_Cu_Nhan_Bo_Lac.png
specialty: Đào giếng sa mạc, Sa Quyền, Cảm nhận mạch nước ngầm
economy:
- Đào giếng thuê cho các thế lực và ốc đảo
- Đổi nước ngầm lấy vật tư sinh hoạt
- Xương yêu thú chế tạo dụng cụ
arcs:
  - arc: 1
    status: Ổn định (Giá trị không thể thay thế)
    rank: Hạng Năm
    leader: Tộc Trưởng Sa Cương
    population: 80
    territory:
      - Vùng đụn cát cao phía nam Hoàng Kim Sa Hải
    assets:
      - name: Hệ thống giếng sâu
        type: Tài Nguyên
      - name: Mạch nước ngầm phía nam
        type: Địa Lợi
      - name: Xương yêu thú dụng cụ
        type: Quân Bị
    stats: [80, 100, 50, 80, 60, 70]
    divisions:
      - name: Đội Đào Giếng
        role: Đào giếng sâu tìm mạch nước ngầm, duy trì nguồn nước cho bộ lạc và ốc đảo xung quanh
        headcount:
          truong_lao: 3
          chien_binh: 30
          dan_thuong: 47
        members:
          - character: Sa Cương
            position: Tộc Trưởng
            cultivation: Kim Đan (Tương đương)
          - character: Lão Sa
            position: Thợ Đào Giỏi Nhất
            cultivation: Trúc Cơ Trung Kỳ (Tương đương)
          - character: "[Trưởng Lão 1]"
            position: Trưởng Lão
            cultivation: Trúc Cơ Viên Mãn (Tương đương)
            placeholder: true
          - character: "[Trưởng Lão 2]"
            position: Trưởng Lão
            cultivation: Trúc Cơ Viên Mãn (Tương đương)
            placeholder: true
          - character: "[Trưởng Lão 3]"
            position: Trưởng Lão
            cultivation: Trúc Cơ Viên Mãn (Tương đương)
            placeholder: true
    relationships:
      - faction: Thiên Sa Thương Hội
        description: Quan hệ phức tạp. Thương Hội cần giếng nước của Cự Nhân để duy trì các trạm thương đạo, nhưng thường xuyên cố ép giá đào giếng.
        diplomacy:
          lien_minh: 10
          tin: 20
          uy_hiep: 40
          thuong_mai: 60
          on_oan: -30
          le_thuoc: 20
      - faction: Bán Thạch Cự Nhân
        description: Bán Thạch Cự Nhân đôi khi đến xin gia nhập bộ lạc nhưng bị từ chối do truyền thống. Sa Cương thấy có lỗi nhưng chưa dám thay đổi.
        diplomacy:
          lien_minh: -10
          tin: 10
          uy_hiep: 0
          thuong_mai: 0
          on_oan: -20
          le_thuoc: 0
      - faction: Thủy Nguồn Bảo Vệ Đoàn
        description: Cùng bảo vệ nguồn nước sa mạc, mối quan hệ hợp tác tự nhiên dựa trên mục tiêu chung.
        diplomacy:
          lien_minh: 30
          tin: 40
          uy_hiep: 0
          thuong_mai: 20
          on_oan: 20
          le_thuoc: 0
---

# Sa Cự Nhân Bộ Lạc (沙巨人部落)

## I. Tổng Quan (总览)
Sa Cự Nhân Bộ Lạc là bộ lạc Cự Tộc sa mạc sống tại vùng đụn cát cao phía nam Hoàng Kim Sa Hải, tồn tại từ trước thời Nhân Tộc đặt chân đến Tây Mạc. Với khoảng tám mươi Cự Nhân da màu cát, bộ lạc nắm giữ vai trò không thể thay thế trong hệ sinh thái sa mạc: đào giếng sâu hàng trăm trượng để tìm mạch nước ngầm. Nước ngầm sa mạc quyết định sự sống còn của mọi sinh vật, và Sa Cự Nhân là chủng tộc duy nhất có khả năng bẩm sinh cảm nhận mạch nước dưới lòng cát. Dưới sự lãnh đạo của Tộc Trưởng Sa Cương — Cự Nhân tương đương Kim Đan, cao năm trượng — bộ lạc kiên quyết đòi trả công xứng đáng cho lao động của mình, bất chấp áp lực từ các thế lực lớn.

## II. Địa Lý & Tài Nguyên (地理与资源)
Bộ lạc cư ngụ tại vùng đụn cát khổng lồ phía nam Hoàng Kim Sa Hải, gần các mạch nước ngầm sâu nhất của sa mạc. Đụn cát ở đây cao hàng chục trượng, tạo thành những "ngọn núi cát" mà chỉ Cự Nhân mới có thể di chuyển thoải mái trên đó. Tài nguyên quý giá nhất là nước ngầm — quý hơn vàng trong sa mạc — mà bộ lạc khai thác qua hệ thống giếng sâu được đào qua nhiều thế hệ. Ngoài ra, xương yêu thú lớn thu lượm được trong sa mạc là nguyên liệu chế tạo dụng cụ và vũ khí của Cự Nhân. Giá trị chiến lược của bộ lạc nằm ở việc họ là nguồn cung cấp nước duy nhất cho nhiều ốc đảo nhỏ trong vùng — không có giếng của họ, các ốc đảo sẽ khô cạn và chết.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
Triết lý cốt lõi của bộ lạc là "Cát càng sâu, nước càng ngọt — khổ đau càng nhiều, linh hồn càng mạnh." Cự Nhân coi việc đào giếng là sứ mệnh thiêng liêng chứ không phải lao động khổ sai — mỗi giếng nước mới là một sinh mệnh mới cho sa mạc. Cự Nhân nào đào được giếng đầu tiên sẽ được đặt tên cho giếng đó, vinh dự lớn nhất trong đời. Phong tục tang lễ đặc biệt: khi Cự Nhân chết, đồng tộc chôn thi thể đứng thẳng dưới cát, để linh hồn "đứng canh" cho bộ lạc từ dưới lòng đất. Truyền thuyết kể rằng những Cự Nhân đã chết vẫn cảm nhận được mạch nước, và đôi khi hướng dẫn người sống tìm đến nguồn nước mới qua giấc mơ.

## IV. Cơ Cấu Tổ Chức (组织结构)
Đứng đầu bộ lạc là Tộc Trưởng Sa Cương — Cự Nhân da màu cát, cao năm trượng, bàn tay to lớn có thể bốc cát lên và cảm nhận mạch nước bên dưới chỉ bằng xúc giác. Dưới ông là ba Trưởng Lão tương đương Trúc Cơ Viên Mãn, phụ trách huấn luyện thế hệ trẻ và bảo vệ bộ lạc. Khoảng tám mươi Cự Nhân bao gồm chiến binh và thợ đào giếng — thực tế hai vai trò này thường là một, vì đào giếng đòi hỏi sức mạnh không kém chiến đấu. Nhân vật đáng chú ý là "Lão Sa" — thợ đào giỏi nhất bộ lạc, đã đào hơn một trăm giếng trong đời, mù cả hai mắt vì cát nhưng cảm nhận mạch nước bằng rung động dưới chân chính xác hơn bất kỳ ai.

## V. Công Pháp & Trận Pháp (功法与阵法)
Công pháp chính của bộ lạc là "Sa Quyền" — quyền thuật Cự Tộc sa mạc, mỗi cú đấm tạo ra sóng cát mạnh mẽ quét sạch kẻ thù trong phạm vi rộng. Cự Nhân sa mạc có khả năng bẩm sinh cảm nhận mạch nước ngầm qua rung động dưới chân — kỹ năng này vừa dùng để đào giếng vừa dùng để cảm nhận bước chân kẻ thù từ xa. Chiến thuật phòng thủ đặc trưng: khi cả bộ lạc giậm chân đồng loạt, tám mươi Cự Nhân cùng lúc tạo ra "trận động cát" — mặt cát rung chuyển dữ dội làm kẻ thù mất thăng bằng, lún sâu vào cát và hoàn toàn mất khả năng chiến đấu. Đây là lý do không thế lực nào dám tấn công trực diện bộ lạc trên chính lãnh địa của họ.

## VI. Đặc Sản Môn Phái (门派特产)
- **Nước Giếng Sâu:** Nước từ các giếng sâu nhất do Cự Nhân đào chứa khoáng chất đặc biệt, uống vào giúp phục hồi thể lực và ổn định linh lực. Một số giếng cổ đại thậm chí cho nước có dược tính nhẹ, được các tông môn thu mua với giá cao.
- **Dụng Cụ Xương Thú:** Vũ khí và công cụ chế tạo từ xương yêu thú lớn thu lượm trong sa mạc, bền chắc và nhẹ hơn kim loại thông thường, phù hợp với tầm vóc khổng lồ của Cự Nhân.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Hệ Thống Giếng Sâu:** Hàng trăm giếng được đào qua nhiều thế hệ, sâu nhất đến hàng trăm trượng, cung cấp nước cho bộ lạc và các ốc đảo xung quanh. Mỗi giếng mang tên người đào ra nó, tạo thành một bản đồ lịch sử sống của bộ lạc.
- **Doanh Trại Đụn Cát:** Khu sinh hoạt nằm giữa các đụn cát cao, sử dụng xương yêu thú làm khung lều và da thú làm vách che. Đơn giản nhưng chắc chắn, chịu được bão cát và nắng nóng sa mạc.

## VIII. Kinh Tế (经济)
Kinh tế của bộ lạc dựa hoàn toàn vào việc đào giếng thuê và trao đổi nước ngầm. Các thế lực lớn nhỏ trong Tây Mạc đều cần giếng nước để duy trì ốc đảo, trạm dừng chân và căn cứ — và chỉ có Sa Cự Nhân mới đào được giếng sâu đủ để chạm mạch nước ngầm. Thiên Sa Thương Hội là khách hàng lớn nhất nhưng cũng là kẻ ép giá tàn nhẫn nhất. Sa Cương kiên quyết đòi trả công xứng đáng, dẫn đến nhiều xung đột kéo dài. Ngoài đào giếng, bộ lạc đổi nước lấy lương thực, vải vóc và vật tư sinh hoạt từ các thương nhân qua đường.

## IX. Lịch Sử Tóm Tắt (简史)
Sa Cự Nhân Bộ Lạc sống ở Hoàng Kim Sa Hải từ trước khi Nhân Tộc đến Tây Mạc. Da họ tiến hóa thành màu cát để ngụy trang trong sa mạc, và khả năng cảm nhận mạch nước ngầm là bẩm sinh qua hàng vạn năm thích nghi. Công việc chính từ xưa đến nay không thay đổi: đào giếng. Nước ngầm sa mạc quyết định sự sống còn của mọi sinh vật, và điều này cho bộ lạc giá trị không thể thay thế. Tuy nhiên, giá trị lớn cũng mang đến áp bức lớn — nhiều thế lực liên tục cố cưỡng ép Cự Nhân đào giếng miễn phí hoặc với giá rẻ mạt. Tộc Trưởng Sa Cương là người đầu tiên dám đứng lên đòi quyền lợi cho bộ lạc, và cuộc đấu tranh đó vẫn đang tiếp diễn.

## X. Giai Thoại & Bí Mật (轶事与秘密)
- Tộc Trưởng Sa Cương từng đào trúng một tầng nước ngầm có màu vàng óng — nước đó uống vào tăng linh lực tạm thời đáng kể, nhưng ông lấp lại giếng ngay lập tức vì sợ bị các thế lực lớn tranh đoạt. Vị trí giếng vàng chỉ mình ông biết, và ông chưa tiết lộ cho bất kỳ ai, kể cả các Trưởng Lão.
- Truyền thuyết bộ lạc kể rằng dưới Hoàng Kim Sa Hải có một "Biển Ngầm" — đại dương nước ngọt cổ đại nằm sâu dưới lòng cát, nơi Cự Tộc nguyên thủy từng sinh sống trước khi di cư lên mặt đất. Lão Sa nói rằng khi đào giếng sâu nhất, ông nghe thấy tiếng sóng.
- Bán Thạch Cự Nhân đôi khi tìm đến xin gia nhập bộ lạc nhưng đều bị từ chối — Sa Cương thấy có lỗi vì biết họ cũng mang dòng máu Cự Tộc, nhưng truyền thống bộ lạc không cho phép tiếp nhận lai tộc. Đây là mâu thuẫn nội tâm mà ông chưa giải quyết được.

## XI. Quan Hệ Thế Lực (势力关系)
- **Thiên Sa Thương Hội:** Quan hệ phức tạp và căng thẳng. Thương Hội cần giếng nước Cự Nhân để duy trì hệ thống trạm dừng trên Thiên Sa Thương Đạo, nhưng liên tục cố ép giá. Sa Cương từ chối khuất phục, dẫn đến xung đột kéo dài nhưng chưa bao giờ leo thang thành chiến tranh — vì hai bên đều cần nhau.
- **Bán Thạch Cự Nhân:** Mối quan hệ đau đớn giữa đồng tộc và ngoại tộc. Bán Thạch mang dòng máu Cự Nhân lẫn Thạch Tộc, muốn gia nhập bộ lạc nhưng bị từ chối bởi truyền thống. Sa Cương âm thầm day dứt.
- **Thủy Nguồn Bảo Vệ Đoàn:** Đồng minh tự nhiên trong việc bảo vệ nguồn nước sa mạc. Hai bên hợp tác dựa trên mục tiêu chung: đảm bảo nước ngầm không bị khai thác cạn kiệt bởi các tông môn tham lam.
