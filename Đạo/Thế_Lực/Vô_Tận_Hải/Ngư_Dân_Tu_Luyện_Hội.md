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

## I. Tổng Quan (总览)
Ngư Dân Tu Luyện Hội là một tổ chức nhỏ bé và đáng yêu nhất Vô Tận Hải — một làng chài phàm nhân mà thành viên vô tình phát hiện rằng ngâm mình trong nước biển lâu năm có thể cải thiện thể chất. Với hơn hai trăm dân cư gồm năm mươi hộ gia đình, Hội do Lão Ngư Ông Lý Đại Hải — người mất sáu mươi năm mới đạt Luyện Khí Đỉnh Phong — làm hội trưởng. Đây là thế lực Không Xếp Hạng, yếu đến mức bất kỳ tu sĩ chính quy nào cũng có thể xóa sổ trong nháy mắt. Tuy nhiên, ẩn dưới sự tầm thường của làng chài là những bí mật mà ngay cả dân làng cũng chưa hiểu hết.

## II. Địa Lý & Tài Nguyên (地理 与 资源)
Làng chài nằm sát mép nước bờ biển đông Vô Tận Hải, nhà cửa dựng bằng gỗ trôi và xương cá lớn — kiến trúc thô sơ nhưng chịu được gió biển. Vùng biển gần bờ có một linh mạch yếu ớt, chỉ hoạt động khi thủy triều lên, cung cấp đủ linh khí để ngư dân hấp thu một chút khi đánh cá. Tài nguyên chính gồm cá linh cấp thấp, tảo biển giàu dinh dưỡng, và vỏ sò chứa vi lượng linh lực. Đáng chú ý nhất là mạch nước ấm bất thường ở đáy biển gần làng — có thể là dấu vết của linh mạch cổ đại bị phong ấn, nhưng không ai trong làng đủ kiến thức để khám phá.

## III. Văn Hóa & Tín Ngưỡng (文化 与 信仰)
Phần lớn thành viên là phàm nhân thuần túy, quan niệm sống giản dị: "Tu luyện là phụ, kiếm cơm là chính." Họ không có hệ thống tín ngưỡng tu chân, chỉ thờ cúng tổ tiên và cầu biển lặng sóng yên trước mỗi chuyến ra khơi. Trẻ em trong làng bơi giỏi hơn đi bộ — nhiều đứa có thể lặn sâu mười trượng mà không cần trợ giúp, điều mà chính tu sĩ Luyện Khí cũng phải bất ngờ. Văn hóa làng chài đề cao sự đoàn kết, chia sẻ và lòng biết ơn đại dương. Mỗi khi đánh được mẻ cá lớn, cả làng cùng chia đều, không phân biệt giàu nghèo.

## IV. Cơ Cấu Tổ Chức (组织结构)
Tổ chức cực kỳ lỏng lẻo, gần như là cơ cấu làng xã phàm nhân hơn là thế lực tu chân. Lão Ngư Ông Lý Đại Hải được tôn làm hội trưởng vì là người lớn tuổi nhất và có kinh nghiệm biển nhiều nhất, không phải vì tu vi. Mỗi đội đánh cá gồm năm đến mười người có một Ngư Đội Trưởng, phụ trách phân công khu vực đánh bắt. Không có phó hội trưởng, trưởng lão hay hệ thống cấp bậc — mọi quyết định lớn đều do cả làng họp bàn dưới cây đa đầu làng. Gần đây, một đệ tử trẻ bất ngờ đột phá Luyện Khí tầng ba, cả làng ăn mừng ba ngày — sự kiện lớn nhất trong lịch sử Hội.

## V. Công Pháp & Trận Pháp (功法 与 阵法)
Hội không có công pháp chính thức. "Phương pháp tu luyện" duy nhất là hít thở theo nhịp sóng biển khi ngâm mình trong nước — hiệu quả cực thấp, gần như là hấp thu linh khí một cách thụ động và vô thức. Lão Lý Đại Hải mất sáu mươi năm kiên trì hít thở theo cách này mới đạt Luyện Khí Đỉnh Phong, tốc độ chậm đến mức bất kỳ tu sĩ chính quy nào cũng coi là trò đùa. Không có trận pháp, không có kỹ năng chiến đấu, không có bất kỳ phương tiện tự vệ nào ngoài mái chèo và lưới cá. Tuy nhiên, thể chất của ngư dân lâu năm cường tráng bất thường so với phàm nhân bình thường.

## VI. Đặc Sản Môn Phái (门派特产)
Cá linh cấp thấp đánh bắt gần vùng linh mạch có hương vị đặc biệt và tác dụng bổ khí nhẹ — tu sĩ cấp cao coi thường, nhưng phàm nhân và tu sĩ Luyện Khí rất ưa thích. Tảo biển phơi khô gần mạch nước ấm cũng có dược tính nhẹ, giúp tăng cường thể lực. Vỏ sò thu thập từ đáy biển đôi khi chứa vi lượng linh lực, có thể dùng làm vật liệu trang trí cấp thấp nhất. Sản phẩm tuy tầm thường nhưng đều mang dấu vết kỳ lạ của linh mạch cổ đại ẩn dưới đáy biển.

## VII. Cơ Sở Hạ Tầng (基础设施)
Làng chài gồm khoảng năm mươi ngôi nhà gỗ trôi và xương cá, xếp dọc theo bờ biển. Cầu cảng nhỏ bằng gỗ là nơi neo đậu thuyền đánh cá. Một quảng trường nhỏ dưới cây đa cổ thụ là trung tâm sinh hoạt cộng đồng. Kho chứa cá và khu phơi tảo nằm ở rìa làng. Toàn bộ hạ tầng đều thô sơ, không có bất kỳ trận pháp bảo hộ hay cơ chế phòng thủ nào — mưa bão lớn đôi khi cuốn trôi vài ngôi nhà.

## VIII. Kinh Tế (经济)
Kinh tế thuần nông nghiệp biển, thu nhập hoàn toàn từ đánh bắt hải sản và bán cho thương nhân qua đường. Phong Bạo Thương Đội là đối tác thương mại thường xuyên nhất, ghé mua cá linh và tảo biển mỗi tháng. Hội cũng trao đổi hải sản với Hải Tảo Nông Dân Hội để đổi lấy các loại tảo khô dùng nấu ăn. Thu nhập thấp nhưng ổn định, đủ cho cuộc sống giản dị. Ngư dân không biết giá trị thực sự của vùng biển họ đang khai thác — nếu tin tức về linh mạch cổ đại và mạch nước ấm lọt đến tai tu sĩ, làng chài sẽ bị nuốt chửng trong chớp mắt.

## IX. Lịch Sử Tóm Tắt (简史)
Làng chài đã tồn tại hàng trăm năm như một cộng đồng phàm nhân bình thường. Sáu mươi năm trước, Lão Lý Đại Hải phát hiện rằng ngư dân già trong làng không mắc bệnh tật và sống thọ hơn người thường — ông bắt đầu có ý thức hít thở theo nhịp sóng và gọi đó là "tu luyện." Ban đầu bị cả làng cười, nhưng khi Lão Lý thể hiện sức mạnh thể chất vượt xa người bình thường, một số ngư dân bắt đầu bắt chước. "Hội" chính thức thành lập khi có đủ mười người "tu luyện" theo phương pháp của Lão Lý. Từng bị tu sĩ qua đường cười nhạo vì gọi việc ngâm nước biển là tu luyện, nhưng gần đây sự kiện đệ tử trẻ đột phá Luyện Khí tầng ba đã khiến cả làng tràn đầy hy vọng.

## X. Giai Thoại & Bí Mật (轶事 与 秘密)
Vùng biển gần làng ẩn chứa một mạch nước ấm bất thường, có ngư dân già thì thầm rằng cá bắt được gần mạch nước này ăn vào thì sức khỏe tốt hẳn lên — nhưng không dám nói lớn sợ thu hút tu sĩ đến cướp. Lão Lý từng nhìn thấy bóng rồng dưới đáy biển khi còn trẻ, hình ảnh đó ám ảnh ông suốt đời nhưng không ai tin. Nếu lời kể của Lão Lý là thật, rất có thể bên dưới làng chài là di tích của Long Cung cổ đại hoặc một phong ấn thượng cổ — và linh mạch yếu ớt chỉ là rò rỉ nhỏ từ nguồn năng lượng khổng lồ bên dưới.

## XI. Quan Hệ Thế Lực (势力关系)
- **Phong Bạo Thương Đội:** Đối tác thương mại thường xuyên, ghé mua hải sản mỗi tháng. Quan hệ thân thiện nhưng bất bình đẳng — thương đội trả giá thấp vì biết ngư dân không có lựa chọn khác.
- **Hải Tảo Nông Dân Hội:** Láng giềng ven biển, thường xuyên trao đổi hải sản và tảo biển. Quan hệ tốt đẹp, cùng cảnh ngộ phàm nhân ven biển.
- **Long Cung:** Không có quan hệ chính thức. Nếu Long Cung biết đến sự tồn tại của Hội, họ sẽ coi như bụi trần — trừ khi phát hiện ra bí mật dưới đáy biển gần làng.
