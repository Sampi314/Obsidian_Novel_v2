---
type: faction
name: Cổ Sa Yêu Tộc
hantu: 古沙妖族
faction_type: Bộ Lạc
alignment: -2
race: Yêu Tộc (Cổ đại)
region: Tây Mạc
founded: Hoàng Sa Cổ Quốc Kỷ Nguyên
founder: Tổ tiên Yêu Tộc phục vụ Cổ Quốc
emblem: Bich_Hoa_Co_Trong_Hang_Toi.png
specialty: Cổ Sa Yêu Thuật, Sa Yêu Quyết, Trận pháp cổ đại
economy:
- Tự cung tự cấp từ tài nguyên trong hang cổ
- Khai thác di vật cổ đại để duy trì trận pháp
- Săn bắt sinh vật sa mạc ngầm
arcs:
  - arc: 1
    status: Ẩn cư suy yếu (Cắt đứt liên lạc với thế giới bên ngoài)
    rank: Hạng Ba
    leader: Tộc Trưởng Cổ Sa
    population: 70
    territory:
      - Hệ thống hang cổ đại sâu trong Hoàng Kim Sa Hải
    assets:
      - name: Hang Cổ Hoàng Sa
        type: Công Trình
      - name: Di vật thời Hoàng Sa Cổ Quốc
        type: Tài Nguyên
      - name: Trận pháp cổ bảo vệ hang
        type: Trận Pháp
      - name: Căn phòng phong ấn bí mật
        type: Thánh Địa
    stats: [800, 600, 500, 70, 1500, 300]
    divisions:
      - name: Hội Đồng Trưởng Lão
        role: Duy trì ký ức và kiến thức cổ đại, quyết định đường lối cộng đồng
        headcount:
          truong_lao: 4
          chien_binh: 0
          dan_thuong: 0
        members:
          - character: Cổ Sa
            position: Tộc Trưởng
            cultivation: Kim Đan Hậu Kỳ (Tương đương)
          - character: "[Trưởng Lão Ám Sa]"
            position: Trưởng Lão
            cultivation: Kim Đan Sơ Kỳ
            placeholder: true
      - name: Đội Thám Tử
        role: Ngụy trang theo dõi chuyển động của Nhân Tộc trên sa mạc
        headcount:
          truong_lao: 0
          chien_binh: 5
          dan_thuong: 0
        members:
          - character: "[Thám Tử Trưởng Mê Sa]"
            position: Thám Tử Trưởng
            cultivation: Trúc Cơ Hậu Kỳ
            placeholder: true
      - name: Tộc Nhân
        role: Sinh sống trong hang cổ, bảo tồn di sản và truyền thống
        headcount:
          truong_lao: 0
          chien_binh: 15
          dan_thuong: 46
        members: []
    relationships:
      - faction: Sa Mạc Yêu Hồ
        description: Hồ Nguyệt Nhi biết về sự tồn tại của Cổ Sa nhưng rất sợ, cấm tộc nhân hoạt động gần hang cổ.
        diplomacy:
          lien_minh: -10
          tin: -50
          uy_hiep: 60
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 0
      - faction: Cổ Tích Thám Hiểm Đoàn
        description: Đối tượng bị theo dõi nghiêm ngặt, tuyệt đối không để phát hiện hang cổ.
        diplomacy:
          lien_minh: -30
          tin: -60
          uy_hiep: 0
          thuong_mai: 0
          on_oan: -20
          le_thuoc: 0
      - faction: Hoàng Sa Di Dân
        description: Nhận ra hậu duệ mang máu vương tộc cũ, nhưng chưa quyết định tiếp cận hay tránh xa.
        diplomacy:
          lien_minh: 0
          tin: 10
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 20
          le_thuoc: 0
      - faction: Cổ Tích Cự Nhân Thức Tỉnh
        description: Lo ngại sâu sắc trước sự thức tỉnh của Cự Nhân cổ đại tại Lưu Sa Cổ Thành.
        diplomacy:
          lien_minh: 0
          tin: -30
          uy_hiep: 0
          thuong_mai: 0
          on_oan: -40
          le_thuoc: 0
---

# Cổ Sa Yêu Tộc (古沙妖族)

## I. Tổng Quan (总览)
Cổ Sa Yêu Tộc là tộc yêu cổ đại từng phục vụ Hoàng Sa Cổ Quốc trong thời kỳ hưng thịnh, hiện ẩn cư sâu trong hệ thống hang động bí mật giữa lòng Hoàng Kim Sa Hải. Với khoảng 70 Yêu Tộc cổ còn sống sót, đây là một cộng đồng khép kín và bí ẩn, sở hữu kiến thức và di vật từ thời đại đã mất nhưng đang dần suy yếu do thời gian dài ẩn cư. Dù dân số ít ỏi, di sản cổ đại mà họ nắm giữ — đặc biệt là trận pháp bảo vệ hang và hệ thống yêu thuật cổ — khiến Cổ Sa Yêu Tộc vẫn là một thế lực đáng gờm mà rất ít ai biết đến.

## II. Địa Lý & Tài Nguyên (地理与资源)
Lãnh địa của Cổ Sa Yêu Tộc là hệ thống hang cổ đại nằm sâu trong lòng Hoàng Kim Sa Hải, gần khu vực Lưu Sa. Hang động rộng lớn với kiến trúc phi Nhân Tộc, tường vách trang trí bằng bích họa cổ đại mô tả lịch sử Hoàng Sa Cổ Quốc và đời sống Yêu Tộc thuở xưa. Bên trong hang chứa đựng di vật từ thời Cổ Quốc — phần lớn đã hư hỏng qua hàng ngàn năm, nhưng một vài pháp khí cổ vẫn còn dư linh lực. Trận pháp cổ bao bọc toàn bộ hệ thống hang tuy đã suy yếu đáng kể, nhưng vẫn đủ sức ngăn cản tu sĩ cấp Kim Đan xâm nhập, khiến vị trí hang động gần như bất khả phát hiện từ bề mặt sa mạc.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
Triết lý sống của Cổ Sa Yêu Tộc là "Chúng ta ở đây trước tất cả — và sẽ ở đây sau tất cả", thể hiện niềm tự hào sâu sắc về nguồn gốc cổ đại và sự kiên nhẫn vô hạn trước dòng chảy thời gian. Quy tắc tối cao là tuyệt đối không giao tiếp với Nhân Tộc trừ khi bắt buộc, và giữ bí mật vị trí hang cổ bằng mọi giá. Yêu Tộc duy trì truyền thống kể lại lịch sử bằng hình ảnh vẽ trên vách hang — phương thức lưu giữ ký ức từ thời Hoàng Sa Cổ Quốc, đảm bảo rằng dù ngôn ngữ có thay đổi, lịch sử vẫn được truyền lại. Đặc biệt cảnh giác với Cổ Tích Thám Hiểm Đoàn và bất kỳ nhóm thám hiểm Nhân Tộc nào hoạt động gần khu vực hang.

## IV. Cơ Cấu Tổ Chức (组织结构)
Tộc Trưởng Cổ Sa đứng đầu cộng đồng — một Yêu Tộc cổ đại với hình dạng nửa người nửa thú, mang trong mình ký ức kéo dài hàng ngàn năm từ thời Hoàng Sa Cổ Quốc còn hưng thịnh. Dưới Cổ Sa là 3 Trưởng Lão tương đương Kim Đan Sơ đến Trung Kỳ, nhưng tất cả đều đã già yếu, linh lực suy giảm rõ rệt. Khoảng 70 tộc nhân còn lại đa dạng hình dạng, từ thú hóa nhân đến nhân hóa thú, tu vi từ Trúc Cơ trở lên. Đội Thám Tử gồm 5 Yêu Tộc nhỏ có khả năng ngụy trang xuất sắc, chuyên trách theo dõi mọi chuyển động của Nhân Tộc trên bề mặt sa mạc, đảm bảo hang cổ không bao giờ bị phát hiện.

## V. Công Pháp & Trận Pháp (功法与阵法)
- **Công Pháp:** *Cổ Sa Yêu Thuật* — hệ thống yêu thuật hoàn chỉnh truyền từ thời Hoàng Sa Cổ Quốc, từng cực kỳ mạnh mẽ nhưng đã mất nhiều phần quan trọng qua hàng ngàn năm thất truyền. *Sa Yêu Quyết* — kỹ thuật biến cát thành vũ khí sắc bén, chỉ một số trưởng lão già nhất còn nhớ cách sử dụng.
- **Trận Pháp:** Trận pháp cổ bao bọc toàn bộ hệ thống hang, tuy suy yếu nhưng vẫn tạo ra lớp ngụy trang và phòng thủ đủ mạnh để ngăn Kim Đan xâm nhập. Cổ Sa biết cách kích hoạt một phần trận pháp khi cần thiết, nhưng không đủ kiến thức để sửa chữa hoặc khôi phục hoàn toàn.

## VI. Đặc Sản Môn Phái (门派特产)
- **Bích Họa Cổ Đại:** Những bức tranh tường vẽ trên vách hang bằng chất liệu đặc biệt không phai theo thời gian, ghi lại lịch sử chi tiết của Hoàng Sa Cổ Quốc — vô giá đối với các nhà nghiên cứu cổ sử.
- **Pháp Khí Cổ Hư Hỏng:** Di vật từ thời Cổ Quốc, tuy đã hỏng nhưng vẫn chứa nguyên lý chế tạo tiên tiến vượt xa trình độ hiện đại.
- **Cổ Sa Mật Dược:** Loại dược liệu bí truyền chế từ khoáng vật sâu trong hang và nọc độc Yêu Tộc, có tác dụng kéo dài tuổi thọ cho Yêu Tộc.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Đại Sảnh Bích Họa:** Hang động chính rộng lớn, tường vách phủ kín bích họa cổ đại, nơi tộc nhân tụ họp và kể lại lịch sử.
- **Phòng Phong Ấn:** Căn phòng bí mật nằm sâu nhất trong hệ thống hang, bị phong ấn nghiêm ngặt — Tộc Trưởng Cổ Sa cấm tuyệt đối mọi tộc nhân đến gần, chỉ nói đó là "nơi giam giữ thứ không nên thả ra".
- **Mạng Lưới Hang Ngầm:** Hệ thống đường hầm chằng chịt kết nối các khu sinh sống, kho lưu trữ di vật, và các lối thoát bí mật dẫn ra bề mặt sa mạc.

## VIII. Kinh Tế (经济)
Cổ Sa Yêu Tộc sống hoàn toàn tự cung tự cấp, không có bất kỳ hoạt động thương mại nào với thế giới bên ngoài. Nguồn sống chính đến từ việc săn bắt sinh vật sa mạc ngầm trong hệ thống hang động, khai thác khoáng vật và nguồn nước mạch ngầm. Di vật cổ đại tuy nhiều nhưng không được buôn bán, mà dành để duy trì trận pháp bảo vệ hang và phục vụ sinh hoạt nội bộ. Tình trạng kinh tế nghèo nàn nhưng đủ để duy trì cộng đồng nhỏ bé.

## IX. Lịch Sử Tóm Tắt (简史)
Cổ Sa Yêu Tộc là dòng Yêu Tộc phục vụ trung thành cho Hoàng Sa Cổ Quốc từ thời hưng thịnh nhất của vương quốc sa mạc huyền thoại này. Khi Cổ Quốc sụp đổ vì nguyên nhân mà Tộc Trưởng Cổ Sa biết rõ nhưng từ chối tiết lộ, Yêu Tộc rút sâu vào hệ thống hang cổ và cắt đứt mọi liên lạc với thế giới bên ngoài. Hàng ngàn năm ẩn cư khiến cộng đồng dần suy yếu trên mọi phương diện — dân số giảm, kiến thức thất truyền, pháp khí hư hỏng không thể sửa chữa. Gần đây, sự thức tỉnh bất ngờ của nhóm Cổ Tích Cự Nhân tại Lưu Sa Cổ Thành đã gây ra làn sóng lo ngại sâu sắc trong nội bộ Yêu Tộc — quá khứ đã chôn vùi đang trỗi dậy, và Cổ Sa lo rằng bí mật mà tộc mình canh giữ cũng sẽ sớm bị phơi bày.

## X. Giai Thoại & Bí Mật (轶事与秘密)
Tộc Trưởng Cổ Sa biết rõ lý do Hoàng Sa Cổ Quốc sụp đổ, nhưng kiên quyết từ chối tiết lộ, chỉ cảnh báo bằng một câu duy nhất: "Đừng đào sâu quá, đừng đi xa quá về phía tây." Trong hang cổ sâu nhất có một căn phòng bị phong ấn bằng trận pháp cổ đại cấp cao — Cổ Sa nói đó là "nơi giam giữ thứ không nên thả ra" và cấm tuyệt đối mọi tộc nhân đến gần, kể cả các Trưởng Lão. Hồ Nguyệt Nhi của Sa Mạc Yêu Hồ bằng cách nào đó biết về sự tồn tại của Cổ Sa Yêu Tộc và rất sợ họ — bà ta lệnh cho tộc nhân tuyệt đối không hoạt động gần khu vực hang cổ, thà mất lợi nhuận còn hơn đụng chạm đến Yêu Tộc cổ đại.

## XI. Quan Hệ Thế Lực (势力关系)
| Thế Lực | Quan Hệ | Mô Tả |
|---|---|---|
| Sa Mạc Yêu Hồ | Uy hiếp ngầm | Hồ Nguyệt Nhi sợ hãi, cấm tộc nhân đến gần |
| Cổ Tích Thám Hiểm Đoàn | Cảnh giác tuyệt đối | Theo dõi nghiêm ngặt, không để lộ hang cổ |
| Hoàng Sa Di Dân | Quan sát từ xa | Nhận ra huyết mạch vương tộc, chưa quyết định |
| Cổ Tích Cự Nhân Thức Tỉnh | Lo ngại sâu sắc | Quá khứ trỗi dậy gây bất an |
