---
type: faction
name: Ngư Dân Tu Luyện Hội
hantu: 渔民修炼会
faction_type: Hội
alignment: 3
race: Nhân Tộc (Phàm nhân bán tu)
region: Vô Tận Hải
founded: 60 năm trước
founder: Lão Ngư Ông Lý Đại Hải
emblem: Luoi_Ca_Linh_Khi.png
specialty: Hô hấp theo nhịp sóng, Lặn biển sâu, Đánh bắt linh ngư cấp thấp
economy:
- Đánh bắt và bán cá linh cấp thấp
- Thu thập tảo biển và vỏ sò chứa linh lực
- Trao đổi hải sản với thương nhân ven biển
arcs:
  - arc: 1
    status: Bình yên — phát triển chậm
    rank: Không Xếp Hạng
    leader: Hội Trưởng Lý Đại Hải
    population: 210
    territory:
      - Làng chài ven bờ biển đông Vô Tận Hải
      - Vùng biển gần bờ (linh mạch yếu)
    assets:
      - name: Linh Mạch Thủy Triều
        type: Tài Nguyên
      - name: Mạch Nước Ấm Bí Ẩn
        type: Bí Cảnh
    stats: [5, 8, 5, 210, 5, 5]
    divisions:
      - name: Ngư Đội
        role: Đánh bắt hải sản, thu thập tài nguyên biển, và "tu luyện" theo nhịp sóng
        headcount:
          hoi_truong: 1
          pho_hoi_truong: 0
          thanh_vien: 50
          tong_quan: 0
        members:
          - character: Lý Đại Hải
            position: Hội Trưởng (Lão Ngư Ông)
            cultivation: Luyện Khí Đỉnh Phong
            placeholder: false
          - character: "[Đệ Tử Trẻ Đột Phá]"
            position: Thành Viên
            cultivation: Luyện Khí Tam Tầng
            placeholder: true
    relationships:
      - faction: Phong Bạo Thương Đội
        description: Thương đội đôi khi ghé qua mua hải sản, là nguồn thu nhập ổn định nhất của Hội. Quan hệ thân thiện nhưng bất bình đẳng.
        diplomacy:
          lien_minh: 5
          tin: 20
          uy_hiep: 0
          thuong_mai: 40
          on_oan: 0
          le_thuoc: 10
      - faction: Hải Tảo Nông Dân Hội
        description: Cùng là tổ chức phàm nhân ven biển, đôi khi trao đổi hải sản lấy tảo biển và ngược lại. Quan hệ láng giềng tốt.
        diplomacy:
          lien_minh: 15
          tin: 25
          uy_hiep: 0
          thuong_mai: 30
          on_oan: 0
          le_thuoc: 0
      - faction: Long Cung
        description: Lão Lý từng nhìn thấy bóng rồng dưới đáy biển nhưng không ai tin. Nếu Long Cung biết đến Hội, họ sẽ coi như bụi trần không đáng bận tâm.
        diplomacy:
          lien_minh: 0
          tin: 0
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 0
---

# Ngư Dân Tu Luyện Hội (渔民修炼会)

> *"Biển nuôi ta, sóng dạy ta, gió nhắc ta khiêm nhường."*
> — Lão Ngư Ông Lý Đại Hải, khi giải thích triết lý tu luyện cho lũ trẻ trong làng

## I. Tổng Quan (总览)
Ngư Dân Tu Luyện Hội là một tổ chức nhỏ bé và đáng yêu nhất Vô Tận Hải — một làng chài phàm nhân mà thành viên vô tình phát hiện rằng ngâm mình trong nước biển lâu năm có thể cải thiện thể chất. Với hơn hai trăm dân cư gồm năm mươi hộ gia đình, Hội do Lão Ngư Ông Lý Đại Hải — người mất sáu mươi năm mới đạt Luyện Khí Đỉnh Phong — làm hội trưởng. Đây là thế lực Không Xếp Hạng, yếu đến mức bất kỳ tu sĩ chính quy nào cũng có thể xóa sổ trong nháy mắt. Tuy nhiên, ẩn dưới sự tầm thường của làng chài là những bí mật mà ngay cả dân làng cũng chưa hiểu hết — một mạch nước ấm bất thường, một bóng rồng dưới đáy biển, và thể chất bất thường của lũ trẻ con sinh ra ở đây.

## II. Địa Lý & Tài Nguyên (地理 与 资源)
Làng chài nằm sát mép nước bờ biển đông Vô Tận Hải, tại một vịnh nhỏ hình bán nguyệt mà dân làng gọi là Vịnh Ngư Ông, được hai mỏm đá tự nhiên tên "Hàm Rồng Đông" và "Hàm Rồng Tây" che chắn gió bão — dân làng không biết rằng hai mỏm đá này trông giống hàm rồng không phải ngẫu nhiên. Nhà cửa dựng bằng gỗ trôi và xương cá lớn — kiến trúc thô sơ nhưng chịu được gió biển, mỗi mái nhà phủ một lớp rong biển khô dày ba tấc giữ ấm. Vùng biển gần bờ có một linh mạch yếu ớt, chỉ hoạt động khi thủy triều lên, cung cấp đủ linh khí để ngư dân hấp thu một chút khi đánh cá — dân làng không biết tên gọi, nhưng Lão Lý đặt cho nó cái tên "Linh Mạch Thủy Triều." Tài nguyên chính gồm cá linh cấp thấp (đặc biệt là loại Ngân Lân Ngư vảy bạc lấp lánh), tảo biển giàu dinh dưỡng gọi là Lục Ti Tảo, và vỏ sò chứa vi lượng linh lực. Đáng chú ý nhất là mạch nước ấm bất thường ở đáy biển gần làng, nơi nước ấm hơn xung quanh mười độ quanh năm — có thể là dấu vết của linh mạch cổ đại bị phong ấn, nhưng không ai trong làng đủ kiến thức để khám phá.

## III. Văn Hóa & Tín Ngưỡng (文化 与 信仰)
Phần lớn thành viên là phàm nhân thuần túy, quan niệm sống giản dị: "Tu luyện là phụ, kiếm cơm là chính." Họ không có hệ thống tín ngưỡng tu chân, chỉ thờ cúng tổ tiên và cầu biển lặng sóng yên trước mỗi chuyến ra khơi tại Miếu Hải Bình — miếu nhỏ bằng đá san hô đặt ở đầu cầu cảng, bên trong chỉ có một bát hương và tấm bài vị khắc chữ "Hải Bình An Lạc." Trẻ em trong làng bơi giỏi hơn đi bộ — nhiều đứa có thể lặn sâu mười trượng mà không cần trợ giúp, điều mà chính tu sĩ Luyện Khí cũng phải bất ngờ. Mỗi tối sau bữa cơm, cả làng tụ tập dưới cây đa cổ thụ nghe Lão Lý kể chuyện biển và chuyện "tu luyện" — nội dung phần lớn là kinh nghiệm đánh cá pha trộn triết lý sống giản dị, nhưng lũ trẻ nghe say mê như được truyền bí pháp thượng thừa. Phong tục đặc biệt nhất: mỗi khi đánh được mẻ cá lớn, cả làng cùng chia đều, không phân biệt giàu nghèo, và phần cá đầu tiên luôn được thả trở lại biển như một nghi thức tạ ơn gọi là "Hoàn Hải Lễ." Lão Lý dạy: "Biển cho ta sáu mươi năm, ta trả lại biển mỗi ngày một con cá — chưa bao giờ đủ."

## IV. Cơ Cấu Tổ Chức (组织结构)
Tổ chức cực kỳ lỏng lẻo, gần như là cơ cấu làng xã phàm nhân hơn là thế lực tu chân. Lão Ngư Ông Lý Đại Hải được tôn làm hội trưởng vì là người lớn tuổi nhất và có kinh nghiệm biển nhiều nhất, không phải vì tu vi. Mỗi đội đánh cá gồm năm đến mười người có một Ngư Đội Trưởng, phụ trách phân công khu vực đánh bắt — hiện có năm đội: Đội Đông do lão Trần Biển Sâu dẫn, chuyên khu vực gần mạch nước ấm nơi cá Ngân Lân tập trung đông nhất; Đội Tây do bà Nguyễn Thị Sóng phụ trách, chuyên thu hoạch Lục Ti Tảo ở bãi đá phía tây; và ba đội còn lại do các ngư dân trung niên luân phiên chỉ huy. Không có phó hội trưởng, trưởng lão hay hệ thống cấp bậc — mọi quyết định lớn đều do cả làng họp bàn dưới cây đa đầu làng. Gần đây, một đệ tử trẻ tên Lý Tiểu Ba bất ngờ đột phá Luyện Khí tầng ba, cả làng ăn mừng ba ngày — sự kiện lớn nhất trong lịch sử Hội, Lão Lý xúc động đến mức rơi nước mắt và tuyên bố "tương lai của Hội đã sáng rồi."

## V. Công Pháp & Trận Pháp (功法 与 阵法)
Hội không có công pháp chính thức. "Phương pháp tu luyện" duy nhất là hít thở theo nhịp sóng biển khi ngâm mình trong nước — hiệu quả cực thấp, gần như là hấp thu linh khí một cách thụ động và vô thức, mà Lão Lý đặt tên rất nghiêm túc là "Triều Tức Dẫn Khí Pháp." Lão Lý mất sáu mươi năm kiên trì hít thở theo cách này mới đạt Luyện Khí Đỉnh Phong, tốc độ chậm đến mức bất kỳ tu sĩ chính quy nào cũng coi là trò đùa. Có lần một tán tu qua đường tên Trương Vân Phi nghe Lão Lý giải thích phương pháp, cười đến chảy nước mắt và để lại lời bình: "Ông ngâm nước sáu mươi năm mà bằng ta ngồi thiền một tháng, tội nghiệp thay!" Không có trận pháp, không có kỹ năng chiến đấu, không có bất kỳ phương tiện tự vệ nào ngoài mái chèo và lưới cá. Tuy nhiên, thể chất của ngư dân lâu năm cường tráng bất thường so với phàm nhân bình thường — xương chắc, da dày, hơi thở dài, lặn sâu không vấn đề — dấu hiệu cho thấy linh mạch ẩn dưới đáy biển đang âm thầm cải tạo cơ thể họ theo cách mà chính họ cũng không hay biết. Đặc biệt, trẻ em sinh ra tại làng có xương nặng hơn trẻ thường đến hai mươi phần trăm — chi tiết mà chưa ai trong làng để ý.

## VI. Đặc Sản Môn Phái (门派特产)
- **Ngân Lân Ngư:** Cá vảy bạc lấp lánh chỉ xuất hiện vào đêm trăng tròn gần mạch nước ấm, có vị ngọt thanh và tác dụng an thần nhẹ, giúp tu sĩ Luyện Khí dễ nhập định. Dân làng gọi là "Cá Trăng" vì chỉ bắt được khi trăng sáng, và tin rằng ăn Cá Trăng sẽ ngủ ngon không mơ ác mộng.
- **Lục Ti Tảo Khô:** Tảo biển phơi khô gần mạch nước ấm có dược tính nhẹ, giúp tăng cường thể lực. Bà Nguyễn Thị Sóng là người phơi tảo giỏi nhất làng, khéo đến mức từng tảo khô đều cuộn tròn đều đặn như sản phẩm thủ công — thương nhân Phong Bạo gọi tảo của bà là "Sóng Quyển" và luôn mua hết mỗi khi ghé làng.
- **Vòng Ngư Phúc:** Vỏ sò thu thập từ đáy biển đôi khi chứa vi lượng linh lực, lũ trẻ trong làng xâu thành vòng cổ bán cho thương nhân qua đường. Sản phẩm tuy tầm thường nhưng đều mang dấu vết kỳ lạ của linh mạch cổ đại ẩn dưới đáy biển, và một vài tu sĩ tinh ý đã bắt đầu chú ý.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Bến Ba Cọc:** Cầu cảng nhỏ bằng gỗ gọi vậy vì chỉ có ba cọc chính chống đỡ, là nơi neo đậu mười hai chiếc thuyền đánh cá. Mỗi thuyền đặt tên theo con cá đầu tiên mà chủ thuyền bắt được — "Thuyền Cá Kiếm," "Thuyền Tôm Vàng," v.v.
- **Quảng Trường Cây Đa:** Khu vực dưới cây đa cổ thụ hơn trăm năm tuổi là trung tâm sinh hoạt cộng đồng, nơi họp bàn, kể chuyện, và ăn mừng. Gốc cây đa có một hốc tự nhiên mà Lão Lý dùng cất giấu "bí kíp" — thực ra là cuốn sổ ghi chép kinh nghiệm đánh cá và hít thở sáu mươi năm của ông.
- **Kho Chứa Cá Đá Xếp:** Kho bằng đá xếp tay, lạnh tự nhiên nhờ gió biển, dùng bảo quản hải sản trước khi bán.
- **Khu Phơi Tảo:** Bãi đá phẳng phía tây làng nơi bà Sóng phơi Lục Ti Tảo, bày trải hàng trăm cuộn tảo xanh mướt dưới nắng biển.
- **Miếu Hải Bình:** "Kiến trúc" trang nghiêm nhất làng, nhỏ xíu đầu cầu cảng, xây bằng đá san hô do dân làng tự xếp. Không có bất kỳ trận pháp bảo hộ hay cơ chế phòng thủ nào — mưa bão lớn đôi khi cuốn trôi vài ngôi nhà, cả làng lại chung sức dựng lại trong vài ngày.

## VIII. Kinh Tế (经济)
Kinh tế thuần nông nghiệp biển, thu nhập hoàn toàn từ đánh bắt hải sản và bán cho thương nhân qua đường. Phong Bạo Thương Đội là đối tác thương mại thường xuyên nhất, thuyền buôn của họ ghé Vịnh Ngư Ông mua cá linh và tảo biển mỗi tháng một lần, trả bằng gạo, vải và dụng cụ kim loại. Hội cũng trao đổi hải sản với Hải Tảo Nông Dân Hội ở làng bên để đổi lấy các loại tảo khô dùng nấu ăn và làm thuốc dân gian. Thu nhập thấp nhưng ổn định, đủ cho cuộc sống giản dị — mỗi hộ kiếm được khoảng hai mươi đồng bạc phàm mỗi tháng, tương đương một phần mười viên linh thạch hạ phẩm. Ngư dân không biết giá trị thực sự của vùng biển họ đang khai thác — nếu tin tức về linh mạch cổ đại và mạch nước ấm lọt đến tai tu sĩ, làng chài sẽ bị nuốt chửng trong chớp mắt. Lão Lý từng nói với lũ trẻ: "Nghèo có cái hay của nghèo — không ai thèm nhìn thì không ai đến cướp."

## IX. Lịch Sử Tóm Tắt (简史)
Làng chài đã tồn tại hàng trăm năm như một cộng đồng phàm nhân bình thường, ban đầu chỉ là nơi trú ngụ của vài gia đình ngư dân trốn nạn binh đao trên đất liền. Sáu mươi năm trước, Lão Lý Đại Hải — khi đó mới ba mươi tuổi — phát hiện rằng ngư dân già trong làng không mắc bệnh tật và sống thọ hơn người thường gần hai mươi năm, ông bắt đầu có ý thức hít thở theo nhịp sóng và gọi đó là "tu luyện." Ban đầu bị cả làng cười, đặc biệt là bà vợ Trần Thị Nguyệt mắng ông "ngâm nước nhiều thành con cá rồi," nhưng khi Lão Lý thể hiện sức mạnh thể chất vượt xa người bình thường — có lần tay không kéo thuyền mắc cạn nặng ba trăm cân lên bờ — một số ngư dân bắt đầu bắt chước. "Hội" chính thức thành lập khi có đủ mười người "tu luyện" theo phương pháp của Lão Lý, nghi lễ thành lập giản dị đến mức chỉ là mười người uống rượu dưới cây đa rồi Lão Lý tuyên bố "từ nay chúng ta là Ngư Dân Tu Luyện Hội." Từng bị tu sĩ qua đường cười nhạo vì gọi việc ngâm nước biển là tu luyện, nhưng gần đây sự kiện Lý Tiểu Ba đột phá Luyện Khí tầng ba đã khiến cả làng tràn đầy hy vọng — và khiến vài tán tu bắt đầu tò mò vì tốc độ đột phá của cậu thanh niên này nhanh bất thường so với phương pháp "ngâm nước."

## X. Giai Thoại & Bí Mật (轶事 与 秘密)
Vùng biển gần làng ẩn chứa một mạch nước ấm bất thường tại vị trí mà ngư dân gọi là "Giếng Trời" — nơi nước biển sủi bọt nhẹ quanh năm, tạo thành một vòng tròn nước ấm đường kính khoảng hai mươi trượng mà cá linh đặc biệt thích tụ tập. Có ngư dân già thì thầm rằng cá bắt được gần Giếng Trời ăn vào thì sức khỏe tốt hẳn lên, vết thương lành nhanh hơn — nhưng không dám nói lớn sợ thu hút tu sĩ đến cướp. Lão Lý từng nhìn thấy bóng rồng dưới đáy biển khi còn trẻ, trong một lần lặn sâu gần Giếng Trời vào đêm nguyệt thực — bóng dáng khổng lồ vàng óng ánh lướt qua tầm nhìn chỉ trong khoảnh khắc, hình ảnh đó ám ảnh ông suốt đời nhưng không ai tin, mọi người bảo ông say sóng mà hoa mắt. Nếu lời kể của Lão Lý là thật, rất có thể bên dưới làng chài là di tích của Long Cung cổ đại hoặc một phong ấn thượng cổ — và linh mạch yếu ớt chỉ là rò rỉ nhỏ từ nguồn năng lượng khổng lồ bên dưới.

Gần đây, Lý Tiểu Ba — đệ tử trẻ mới đột phá — báo cáo rằng khi luyện tập gần Giếng Trời vào ban đêm, cậu nghe thấy tiếng ngâm kinh trầm ấm vọng lên từ đáy biển, nhưng Lão Lý dặn cậu giữ bí mật tuyệt đối. Ông già ngồi lặng rất lâu rồi nói: "Nếu dưới đó có thứ gì, thì nó đã ở đó trước cả khi ông nội ta đến đây. Chúng ta không đủ mạnh để tìm hiểu, và cũng không đủ khôn để giấu kín. Vậy thì cứ giả vờ không biết — đó là cách sống sót duy nhất của kẻ yếu."

Điều trớ trêu nhất: dân làng sống trên nguồn linh lực có thể khiến các đại tông phái tranh giành đến đổ máu, nhưng chính sự nghèo khó và tầm thường của họ lại là lá chắn bảo vệ hiệu quả nhất. Lão Lý hiểu điều này bằng bản năng sinh tồn của kẻ yếu: *"Cá nhỏ sống lâu vì cá lớn không thèm nhìn. Ta cũng vậy — nghèo có cái hay của nghèo."* Tuy nhiên, sự kiện Lý Tiểu Ba đột phá bất thường đang thu hút sự tò mò của vài tán tu qua đường, và nếu họ điều tra kỹ hơn, bí mật Giếng Trời có thể không giữ được bao lâu nữa. Lão Lý đã bắt đầu tính đến phương án xấu nhất: nếu tu sĩ mạnh đến chiếm Giếng Trời, cả làng sẽ rút lên đồi cao phía bắc — nơi ông đã âm thầm giấu thuyền dự phòng và lương khô đủ cho ba tháng.

## XI. Quan Hệ Thế Lực (势力关系)
- **Phong Bạo Thương Đội:** Đối tác thương mại thường xuyên, ghé mua hải sản mỗi tháng. Quan hệ thân thiện nhưng bất bình đẳng — thương đội trả giá thấp vì biết ngư dân không có lựa chọn khác. Thuyền trưởng Hải Phong đôi khi mang quà nhỏ cho lũ trẻ, nhưng giá mua cá thì không bao giờ nhượng bộ. Lão Lý nói đùa: "Ông Hải Phong tốt bụng lắm, cho kẹo con nít nhưng bóp cổ người lớn."
- **Hải Tảo Nông Dân Hội:** Láng giềng ven biển ở làng cách ba dặm về phía nam, thường xuyên trao đổi hải sản và tảo biển. Quan hệ tốt đẹp, cùng cảnh ngộ phàm nhân ven biển — hai bên từng giúp nhau dựng lại nhà sau bão lớn, và con gái Hải Tảo hay gả cho con trai Ngư Dân, tạo thành mối thông gia bền chặt.
- **Long Cung:** Không có quan hệ chính thức. Nếu Long Cung biết đến sự tồn tại của Hội, họ sẽ coi như bụi trần — trừ khi phát hiện ra bí mật dưới đáy biển gần làng, khi đó số phận của hai trăm dân chài sẽ nằm hoàn toàn trong tay những sinh vật mà họ thậm chí không biết là có thật.
