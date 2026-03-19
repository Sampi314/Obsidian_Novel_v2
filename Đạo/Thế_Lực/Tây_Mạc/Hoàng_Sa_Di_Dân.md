---
type: faction
name: Hoàng Sa Di Dân
hantu: 黄沙移民
faction_type: Bộ Lạc
alignment: 2
race: Nhân Tộc (Hậu duệ Hoàng Sa Cổ Quốc)
region: Tây Mạc
founded: Không rõ (lưu lạc sau khi Hoàng Sa Cổ Quốc diệt vong)
founder: Không rõ (thần dân Cổ Quốc lưu lạc)
emblem: Manh_Ngoc_Vang_Co.png
specialty: Truyền thuyết truyền miệng Hoàng Sa Cổ Quốc, Di vật cổ đại, Huyết mạch vương tộc
economy:
- Trồng trọt nhỏ lẻ tại rìa ốc đảo
- Bán lao động cho thương đoàn qua đường
- Đổi truyền thuyết và cổ vật lấy thực phẩm
arcs:
  - arc: 1
    status: Tồn tại bấp bênh tại rìa Minh Nguyệt Châu
    rank: Không Xếp Hạng
    leader: Trưởng Lão Hoàng Cổ Nham
    population: 300
    territory:
      - Khu ngoại vi ốc đảo Minh Nguyệt Châu (vùng đất cằn cỗi nhất)
    assets:
      - name: Di Vật Hoàng Sa Cổ Quốc
        type: Cổ Vật
      - name: Tấm Bản Đồ Nát (chỉ đến Hoàng Sa Vương Lăng)
        type: Tư Liệu
      - name: Mảnh Ngọc Khắc Cổ Văn
        type: Cổ Vật
    stats: [5, 10, 20, 40, 5, 15]
    divisions:
      - name: Hội Đồng Bô Lão
        role: Quyết định mọi việc lớn và bảo tồn truyền thuyết tổ tiên
        headcount:
          truong_lao: 5
          chien_binh: 0
          dan_thuong: 295
        members:
          - character: Hoàng Cổ Nham
            position: Trưởng Lão
            cultivation: Phàm nhân
          - character: "[Bô Lão Nhị]"
            position: Bô Lão
            cultivation: Phàm nhân
            placeholder: true
          - character: "[Đứa Trẻ Huyết Mạch]"
            position: Dân thường (huyết mạch vương tộc thức tỉnh)
            cultivation: Phàm nhân (linh căn tiềm ẩn)
            placeholder: true
    relationships:
      - faction: Cổ Tích Thám Hiểm Đoàn
        description: Mối liên hệ mong manh nhưng có ý nghĩa — Lý Cổ Trần bắt đầu quan tâm đến truyền thuyết của Di Dân và chia sẻ phát hiện khảo cổ, đổi lại được nghe ký ức truyền miệng về Cổ Quốc.
        diplomacy:
          lien_minh: 20
          tin: 40
          uy_hiep: 0
          thuong_mai: 30
          on_oan: 0
          le_thuoc: 0
      - faction: Cổ Sa Yêu Tộc
        description: Cổ Sa Yêu Tộc lén quan sát cộng đồng từ xa, nhận ra Di Dân mang máu vương tộc Hoàng Sa cũ nhưng chưa quyết định tiếp cận hay tránh xa.
        diplomacy:
          lien_minh: 0
          tin: 0
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 0
      - faction: Thiên Sa Thương Hội
        description: Thương hội coi Di Dân là nhóm phàm nhân nghèo không đáng để ý, đôi khi thuê họ làm lao động giá rẻ tại bến hàng Minh Nguyệt Châu.
        diplomacy:
          lien_minh: 0
          tin: 10
          uy_hiep: 20
          thuong_mai: 15
          on_oan: 0
          le_thuoc: 30
---

# Hoàng Sa Di Dân (黄沙移民)

## I. Tổng Quan (总览)
Hoàng Sa Di Dân là cộng đồng khoảng ba trăm phàm nhân — hậu duệ cuối cùng của thần dân Hoàng Sa Cổ Quốc, vương quốc sa mạc hùng mạnh đã diệt vong cách đây hàng ngàn năm. Định cư tại rìa cằn cỗi nhất của ốc đảo Minh Nguyệt Châu, nơi nguồn nước ít và cát sa mạc không ngừng tràn vào, cộng đồng sống một cuộc sống bấp bênh nhưng kiên cường. Dưới sự dẫn dắt của Trưởng Lão Hoàng Cổ Nham — một ông già tám mươi tuổi phàm nhân không biết tu luyện nhưng thuộc lòng mọi ký ức truyền miệng — Di Dân bền bỉ giữ gìn di sản tổ tiên qua từng thế hệ, dù bị mọi thế lực mạnh hơn coi thường. Triết lý của họ giản dị mà sâu sắc: "Máu Hoàng Sa không bao giờ khô — chỉ là chìm trong cát".

## II. Địa Lý & Tài Nguyên (地理与资源)
Hoàng Sa Di Dân cư trú tại khu ngoại vi ốc đảo Minh Nguyệt Châu, chính xác là vùng bìa ốc đảo giáp Hoàng Kim Sa Hải — nơi nguồn nước ít nhất, đất đai cằn cỗi nhất, và cát từ sa mạc tràn vào liên tục theo mùa gió. Họ không sở hữu đất canh tác tốt hay mỏ khoáng, nhưng lại giữ trong tay thứ mà nhiều thế lực khao khát mà không biết: di vật của Hoàng Sa Cổ Quốc. Phần lớn di vật đã hư hỏng theo thời gian, chỉ còn vài mảnh ngọc khắc cổ văn mà không ai đọc được, và một tấm bản đồ nát mà Trưởng Lão cất giữ cẩn thận hơn mạng sống. Sinh kế của cộng đồng chủ yếu dựa vào trồng trọt nhỏ lẻ, bán sức lao động cho thương đoàn qua đường, và đôi khi đổi truyền thuyết lấy thức ăn từ những lữ khách tò mò.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
Văn hóa của Hoàng Sa Di Dân xoay quanh việc bảo tồn ký ức. Quy tắc tối cao là mỗi thế hệ phải truyền lại truyền thuyết về Hoàng Sa Cổ Quốc bằng miệng, không được thêm bớt, không được quên. Đêm rằm hàng tháng, toàn cộng đồng tụ họp dưới ánh trăng, đốt nhang hướng về phía tây — nơi cổ quốc từng tọa lạc — và kể chuyện xưa cho con cháu nghe. Đây không chỉ là nghi lễ mà là sợi dây duy nhất nối họ với quá khứ huy hoàng. Cấm kỵ lớn nhất của cộng đồng là bán di vật cho ngoại nhân — ai vi phạm sẽ bị trục xuất vĩnh viễn, mất quyền nghe truyền thuyết và không còn được coi là con cháu Hoàng Sa. Tuy nhiên, mâu thuẫn thế hệ ngày càng sâu sắc: nhiều thanh niên muốn rời đi tìm cuộc sống tốt hơn, coi truyền thuyết là gánh nặng thay vì di sản.

## IV. Cơ Cấu Tổ Chức (组织结构)
Cộng đồng được tổ chức theo mô hình bộ lạc truyền thống với Hội Đồng Bô Lão gồm năm người già nhất quyết định mọi việc lớn. Trưởng Lão Hoàng Cổ Nham là người có tiếng nói nặng ký nhất, không phải vì quyền lực mà vì ông là người thuộc lòng nhiều truyền thuyết nhất và được cả cộng đồng kính trọng. Bốn bô lão còn lại phụ trách từng mảng: phân chia đất canh tác, điều phối lao động, giải quyết tranh chấp nội bộ, và bảo quản di vật. Dưới Hội Đồng là khoảng ba trăm phàm nhân bao gồm cả người già, thanh niên và trẻ em, trong đó vài người có linh căn nhưng không đủ tiền bái sư nên chưa từng tu luyện. Gần đây, một đứa trẻ trong cộng đồng bỗng kích hoạt được mảnh ngọc cổ, phát ra ánh sáng vàng — sự kiện chấn động cho thấy huyết mạch vương tộc vẫn chưa hoàn toàn tắt.

## V. Công Pháp & Trận Pháp (功法与阵法)
Hoàng Sa Di Dân hoàn toàn là phàm nhân, không có công pháp hay trận pháp nào. Họ không biết tu luyện và không có ai đủ trình độ dạy bảo. Tuy nhiên, cộng đồng sở hữu một số di vật cổ đại mà không ai biết cách kích hoạt — các mảnh ngọc và phiến đá khắc cổ văn mà truyền thuyết nói rằng chỉ huyết mạch vương tộc Hoàng Sa mới có thể đánh thức. Gần đây, đứa trẻ kích hoạt được mảnh ngọc là bằng chứng đầu tiên trong hàng trăm năm rằng truyền thuyết có thể là sự thật. Nếu ai đó trong cộng đồng có thể học cách kiểm soát sức mạnh của di vật, Hoàng Sa Di Dân sẽ không còn hoàn toàn bất lực — nhưng đó vẫn là chuyện xa vời.

## VI. Đặc Sản Môn Phái (门派特产)
- **Mảnh Ngọc Hoàng Sa:** Di vật cổ khắc cổ văn không ai đọc được, có khả năng phát sáng khi tiếp xúc với huyết mạch vương tộc, giá trị khảo cổ và lịch sử vô cùng lớn.
- **Truyền Thuyết Truyền Miệng:** Hệ thống ký ức truyền qua hàng chục thế hệ về Hoàng Sa Cổ Quốc, bao gồm tên các vị vua, vị trí cung điện, và phong tục cổ — thông tin mà Cổ Tích Thám Hiểm Đoàn đánh giá rất cao.
- **Tấm Bản Đồ Nát:** Bản đồ cổ được cho là chỉ đến Hoàng Sa Vương Lăng, nơi chôn cất vua cuối cùng, đầy bảo vật nhưng cũng đầy cấm chế.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Khu Định Cư Bìa Ốc Đảo:** Tập hợp lều trại và nhà đất thấp dọc theo rìa Minh Nguyệt Châu, thường xuyên phải sửa chữa vì cát tràn vào.
- **Giếng Nước Cộng Đồng:** Một giếng nước duy nhất đào sâu đến mạch ngầm, cung cấp nước sinh hoạt cho toàn bộ ba trăm người, là tài sản quan trọng nhất.
- **Nhà Hội Bô Lão:** Căn nhà lớn nhất cộng đồng, nơi Hội Đồng họp mặt và cất giữ di vật, cũng là nơi tổ chức đêm kể chuyện mỗi rằm.

## VIII. Kinh Tế (经济)
Kinh tế của Hoàng Sa Di Dân ở mức sinh tồn tối thiểu. Nguồn thu nhập chính là lao động phổ thông — thanh niên trong cộng đồng làm phu khuân vác cho thương đoàn dừng chân tại Minh Nguyệt Châu, phụ nữ và người già trồng trọt rau quả nhỏ lẻ trên mảnh đất cằn cỗi. Đôi khi, lữ khách tò mò sẵn sàng trả vài đồng linh thạch hạ phẩm để nghe truyền thuyết về Hoàng Sa Cổ Quốc, và đây trớ trêu thay lại là nguồn thu nhập ổn định nhất. Cộng đồng không có khả năng tích lũy tài sản — mọi thu nhập đều dùng ngay cho thực phẩm và nhu yếu phẩm. Trưởng Lão nghiêm cấm bán di vật dù nhiều thương nhân sẵn sàng trả giá cao.

## IX. Lịch Sử Tóm Tắt (简史)
Hậu duệ của thần dân Hoàng Sa Cổ Quốc — vương quốc sa mạc hùng mạnh đã diệt vong cách đây hàng ngàn năm vì lý do không hoàn toàn rõ ràng. Truyền thuyết nói rằng cổ quốc sụp đổ trong một đêm, khi sa mạc nuốt chửng toàn bộ thành trì và cung điện. Nhóm thần dân sống sót lưu lạc qua nhiều đời, bị xua đuổi khắp nơi vì không có sức mạnh tu luyện và không thuộc về thế lực nào. Cuối cùng, vài thế hệ trước, họ định cư tại rìa Minh Nguyệt Châu — vùng đất mà không thế lực nào thèm tranh giành. Dù bị coi thường, cộng đồng vẫn bền bỉ giữ gìn truyền thuyết và di vật, tin rằng một ngày nào đó vương tộc Hoàng Sa sẽ trỗi dậy. Gần đây, Cổ Tích Thám Hiểm Đoàn bắt đầu quan tâm đến họ, và đứa trẻ kích hoạt mảnh ngọc đã khiến cả cộng đồng xáo động — niềm hy vọng bùng lên sau hàng trăm năm im lặng.

## X. Giai Thoại & Bí Mật (轶事与秘密)
Tấm bản đồ nát mà Trưởng Lão Hoàng Cổ Nham cất giữ được cho là chỉ đến Hoàng Sa Vương Lăng — nơi chôn cất vị vua cuối cùng của Cổ Quốc, một nơi đầy bảo vật nhưng cũng đầy cấm chế chết người mà ngay cả Kim Đan cường giả cũng phải dè chừng. Sự kiện đứa trẻ kích hoạt mảnh ngọc cổ phát ra ánh sáng vàng là dấu hiệu rõ ràng nhất từ trước đến nay về sự tồn tại của huyết mạch vương tộc Hoàng Sa trong cộng đồng. Cổ Sa Yêu Tộc từng lén quan sát cộng đồng từ xa và đã nhận ra điều này, nhưng vẫn chưa quyết định tiếp cận hay tránh xa — sự do dự của họ cho thấy huyết mạch vương tộc Hoàng Sa có ý nghĩa quan trọng hơn nhiều so với những gì Di Dân hiểu biết hiện tại.

## XI. Quan Hệ Thế Lực (势力关系)
- **Cổ Tích Thám Hiểm Đoàn:** Mối liên hệ mong manh nhưng đầy tiềm năng. Đoàn Trưởng Lý Cổ Trần bắt đầu tiếp xúc với cộng đồng để thu thập truyền thuyết và đối chiếu với phát hiện khảo cổ, đổi lại ông chia sẻ kiến thức về cổ văn và lịch sử. Đây là mối quan hệ đôi bên cùng có lợi hiếm hoi mà Di Dân có được.
- **Cổ Sa Yêu Tộc:** Quan hệ một chiều và bí ẩn. Cổ Sa Yêu Tộc biết đến sự tồn tại của Di Dân và nhận ra máu vương tộc trong huyết quản họ, nhưng giữ khoảng cách, chưa tiếp xúc trực tiếp. Di Dân hoàn toàn không biết mình đang bị theo dõi.
- **Thiên Sa Thương Hội:** Quan hệ bất đối xứng. Thương hội coi Di Dân là nhóm phàm nhân nghèo không đáng để ý, chỉ thuê làm lao động giá rẻ khi cần. Di Dân phụ thuộc một phần vào các thương đoàn để kiếm sống nhưng không có vị thế đàm phán.
