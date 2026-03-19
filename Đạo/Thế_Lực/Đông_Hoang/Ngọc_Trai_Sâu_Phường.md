---
type: faction
name: Ngọc Trai Sâu Phường
hantu: 珍珠虫坊
faction_type: Bộ Lạc
alignment: -3
race: Trùng Tộc (Sâu Ngọc Trai Linh)
region: Đông Hoang
founded: Thượng Cổ (bị Giao Nhân thuần phục)
founder: Không có (quần thể tự nhiên bị bắt giữ)
emblem: Ngoc_Trai_Sau_Phuong.png
specialty: Sản xuất ngọc trai linh, Tiết chất khoáng bọc ngọc
economy:
- Sản xuất ngọc trai linh (bị Giao Nhân thu hết)
- Trao đổi ngầm mật khoáng với sinh vật biển nhỏ
arcs:
  - arc: 1
    status: Bị bóc lột
    rank: Không Xếp Hạng
    leader: Phường Chủ Trùng Bạch
    population: 30
    territory:
      - Rạn san hô vùng biển nam lãnh hải Giao Nhân
    assets:
      - name: Rạn San Hô Sản Xuất Ngọc
        type: Công Trình
      - name: Hắc Ngọc Trai
        type: Bảo Vật
    stats: [5, 30, 5, 30, 10, 5]
    divisions:
      - name: Quần Thể Sâu Ngọc Trai
        role: Sản xuất ngọc trai linh và duy trì rạn san hô
        headcount:
          truong_lao: 1
          chien_binh: 0
          dan_thuong: 29
        members:
          - character: Trùng Bạch
            position: Phường Chủ
            cultivation: Trúc Cơ (tương đương)
          - character: "[Giám Sát Giao Nhân]"
            position: Giám Sát
            cultivation: Luyện Khí Hậu Kỳ
            placeholder: true
    relationships:
      - faction: Giao Nhân Hoàng Tộc
        description: Bị hoàng tộc nuôi nhốt và cưỡng ép sản xuất ngọc trai từ thời thượng cổ, không có quyền tự chủ.
        diplomacy:
          lien_minh: -100
          tin: -100
          uy_hiep: 90
          thuong_mai: -80
          on_oan: -90
          le_thuoc: 100
      - faction: Giao Nhân Bần Dân
        description: Đồng cảm với nhau vì cùng bị hoàng tộc bóc lột, bần dân giám sát ngọc trai nhưng ngầm thông cảm.
        diplomacy:
          lien_minh: 20
          tin: 30
          uy_hiep: 0
          thuong_mai: 5
          on_oan: 10
          le_thuoc: 0
      - faction: Giáp Xác Liên Minh
        description: Các sinh vật giáp xác đôi khi ghé rạn san hô, trao đổi tin tức biển sâu với Trùng Bạch.
        diplomacy:
          lien_minh: 5
          tin: 10
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 0
---

# NGỌC TRAI SÂU PHƯỜNG (珍珠虫坊)

## I. Tổng Quan (总览)

Ngọc Trai Sâu Phường là một quần thể sâu ngọc trai linh — loại Trùng Tộc biển nhỏ bé chuyên tiết chất khoáng bọc quanh hạt cát để tạo thành ngọc trai. Chúng bị Giao Nhân hoàng tộc nuôi nhốt và khai thác từ thời thượng cổ, sống chen chúc trong hốc đá nhỏ tại rạn san hô vùng biển nam. Phường Chủ Trùng Bạch là con sâu ngọc trai lớn nhất và là thế hệ đầu tiên đạt được linh trí, hiểu được thân phận bị bóc lột của cả quần thể. Dù vô cùng yếu ớt về sức chiến đấu, Ngọc Trai Sâu Phường ẩn chứa một vũ khí hủy diệt cuối cùng mà ngay cả Giao Nhân cũng không hay biết.

## II. Địa Lý & Tài Nguyên (地理与资源)

Ngọc Trai Sâu Phường cư ngụ trong một vùng rạn san hô rộng khoảng nửa dặm, nằm sâu dưới lãnh hải do Giao Nhân hoàng tộc kiểm soát. Rạn san hô này giàu khoáng chất và cát linh — nguyên liệu thiết yếu cho quá trình tạo ngọc. Tuy nhiên, khu vực chật hẹp đến mức hàng chục cá thể phải sống chen chúc trong từng hốc đá nhỏ. Nguồn nước sạch hoàn toàn phụ thuộc vào dòng hải lưu mà Giao Nhân kiểm soát, khiến sâu ngọc trai không thể rời đi ngay cả khi muốn. Ngọc trai linh sản xuất tại đây tuy nhỏ hơn và kém giá trị hơn ngọc trai do Giao Nhân tự tạo, nhưng số lượng lớn và ổn định, là nguồn cung cấp quan trọng cho nền kinh tế hoàng tộc.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)

Sâu ngọc trai linh là sinh vật đơn giản, không có hệ thống tín ngưỡng phức tạp. Tuy nhiên, kể từ khi Trùng Bạch đạt linh trí, một hình thức văn hóa sơ khai đã nảy sinh: "Bài Ca Buồn" — giai điệu rung động trong nước được truyền từ thế hệ này sang thế hệ khác. Bài ca chứa đựng ký ức về nỗi khổ bị giam cầm và ước mơ mơ hồ về tự do, nhưng tần số rung động quá thấp nên Giao Nhân không nghe được. Đối với sâu ngọc trai, tiết chất khoáng tạo ngọc là bản năng sinh học, không khác gì hơi thở — và chính bản năng này đã trở thành xiềng xích trói buộc chúng vào kiếp nô lệ.

## IV. Cơ Cấu Tổ Chức (组织结构)

Cơ cấu của Ngọc Trai Sâu Phường cực kỳ đơn giản, phản ánh bản chất quần thể sinh vật nhỏ bé. Phường Chủ Trùng Bạch là cá thể duy nhất có linh trí đầy đủ, đóng vai trò đại diện giao tiếp với ba Giao Nhân bần dân được cử đến giám sát và thu gom ngọc trai. Phần còn lại là hàng nghìn sâu ngọc trai có linh trí sơ khai, mỗi con tạo ra một đến hai viên ngọc mỗi năm. Chúng hoạt động theo bản năng dưới sự điều phối nhẹ nhàng của Trùng Bạch thông qua rung động cơ thể.

## V. Công Pháp & Trận Pháp (功法与阵法)

Ngọc Trai Sâu Phường không có công pháp chiến đấu theo nghĩa thông thường. Việc tiết chất khoáng bọc quanh hạt cát tạo ngọc hoàn toàn là bản năng sinh học, không cần tu luyện. Kỹ năng duy nhất đáng kể là khả năng của Trùng Bạch: tạo ra ngọc trai đặc biệt cứng với tốc độ nhanh, có thể bắn ra như đạn phòng thủ — tuy nhiên sức công phá chỉ đủ xua đuổi cá nhỏ hoặc làm chậm kẻ tấn công cấp Luyện Khí. Ngoài ra, quần thể có thể đồng loạt tiết chất khoáng tạo thành một lớp vỏ bảo vệ tạm thời quanh rạn san hô, nhưng lớp vỏ này mỏng manh và dễ phá vỡ.

## VI. Đặc Sản Môn Phái (门派特产)

- **Ngọc Trai Linh:** Loại ngọc trai nhỏ chứa linh lực ổn định, được Giao Nhân hoàng tộc dùng làm nguyên liệu chế tác trang sức linh khí và trang trí cung điện. Chất lượng kém hơn ngọc trai do Giao Nhân tự tạo từ nước mắt, nhưng số lượng lớn và giá thành thấp.
- **Mật Khoáng:** Chất tiết phụ phẩm trong quá trình tạo ngọc, có tác dụng bảo dưỡng san hô và nuôi dưỡng vi sinh vật biển. Giao Nhân coi đây là phế phẩm không đáng giá, nhưng thực ra mật khoáng có tiềm năng dược liệu mà chưa ai khai phá.

## VII. Cơ Sở Hạ Tầng (基础设施)

- **Rạn San Hô Sản Xuất Ngọc:** Khu vực chính nơi sâu ngọc trai sinh sống và làm việc, gồm hàng trăm hốc đá nhỏ xếp san sát nhau. Giao Nhân dựng một hàng rào linh khí xung quanh để ngăn sâu bỏ trốn.
- **Hốc Giấu Của Trùng Bạch:** Một khe đá hẹp ẩn dưới lớp san hô chết, nơi Trùng Bạch bí mật cất giấu Hắc Ngọc Trai và vài viên ngọc trai chất lượng cao giấu khỏi tay Giao Nhân.
- **Bãi Thu Gom:** Khu vực phẳng giữa rạn san hô nơi ba Giao Nhân bần dân đến thu gom ngọc trai theo lịch trình cố định mỗi tháng.

## VIII. Kinh Tế (经济)

Nền kinh tế của Ngọc Trai Sâu Phường thực chất là nền kinh tế nô lệ. Toàn bộ sản lượng ngọc trai phải nộp cho Giao Nhân hoàng tộc, chúng chỉ được giữ lại phần nhỏ mật khoáng đủ để duy trì sự sống. Không có hoạt động thương mại nào được phép. Trùng Bạch bí mật giấu lại vài viên ngọc chất lượng cao mỗi năm, tích lũy như một quỹ dự phòng cho ngày thoát thân — nhưng ngọc trai không có giá trị gì với loài sâu, chúng cần thức ăn khoáng chất mà Giao Nhân kiểm soát nguồn cung.

## IX. Lịch Sử Tóm Tắt (简史)

Sâu ngọc trai linh tồn tại từ thời thượng cổ, sống tự do trong các rạn san hô khi Giao Nhân chưa xuất hiện. Truyền thuyết kể rằng thời ấy, sâu ngọc trai từng tạo ra ngọc trai lớn như quả trứng vì được tự do hấp thụ linh khí biển sâu mà không bị hạn chế. Khi Giao Nhân hoàng tộc bành trướng lãnh hải, sâu ngọc trai bị bắt giữ và thuần phục thành nguồn cung cấp ngọc trai giá rẻ.

Suốt nhiều ngàn năm, sâu ngọc trai chỉ là sinh vật bản năng không có linh trí. Trùng Bạch là cá thể đầu tiên đạt được linh trí tự phát — một hiện tượng mà Giao Nhân không lường trước. Khi hiểu được thân phận bị bóc lột, Trùng Bạch từng tổ chức "đình công" khiến toàn bộ quần thể ngừng sản xuất ngọc trai. Giao Nhân đáp trả bằng cách cắt nguồn nước sạch, buộc chúng phải khuất phục. Từ đó, Trùng Bạch chuyển sang chiến lược ẩn nhẫn, bí mật chuẩn bị cho ngày phản kháng trong tương lai.

## X. Giai Thoại & Bí Mật (轶事与秘密)

- Trùng Bạch bí mật giấu một viên Hắc Ngọc Trai — ngọc trai tối màu chứa năng lượng cô đọng tích lũy qua nhiều thập kỷ. Nếu phát nổ, sức công phá tương đương nhất kích của tu sĩ Kim Đan, đủ để hủy hoại cả rạn san hô và giết chết mọi Giao Nhân trong phạm vi nửa dặm. Đây là vũ khí cuối cùng mà Trùng Bạch không muốn dùng, vì kích nổ đồng nghĩa hy sinh toàn bộ quần thể.
- Có tin đồn loài sâu ngọc trai từng tự do trước khi Giao Nhân đến, và trong quá khứ xa xôi chúng từng tạo ra ngọc trai lớn như quả trứng — nếu lời đồn là thật, giá trị của những viên ngọc cổ đại ấy sẽ khiến cả tu chân giới điên đảo.
- Ba Giao Nhân bần dân được cử đến giám sát thực ra đồng cảm sâu sắc với Ngọc Trai Sâu Phường, vì bản thân họ cũng bị hoàng tộc bóc lột. Có dấu hiệu cho thấy họ đang ngầm giúp Trùng Bạch giấu bớt sản lượng ngọc trai.

## XI. Quan Hệ Thế Lực (势力关系)

| Thế Lực | Quan Hệ | Mô Tả |
|---------|---------|-------|
| Giao Nhân Hoàng Tộc | Nô lệ | Bị nuôi nhốt và cưỡng ép sản xuất ngọc trai |
| Giao Nhân Bần Dân | Đồng cảm ngầm | Cùng bị hoàng tộc bóc lột, ngầm thông cảm |
| Giáp Xác Liên Minh | Trung lập | Thi thoảng trao đổi tin tức biển sâu |
