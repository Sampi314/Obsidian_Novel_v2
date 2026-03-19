---
type: faction
name: Cổ Thụ Thủ Hộ Đoàn
hantu: 古树守护团
faction_type: Hội
alignment: 7
race: Tinh Linh Tộc
region: Đông Hoang
founded: Năm Khởi Nguyên 99.000
founder: Tinh Linh Vương Đình (chỉ định)
emblem: Re_Cay_Xanh_Khien.png
specialty: Phòng thủ biên giới rừng, Liên kết cổ thụ, Kháng huyết độc
economy:
- Thu hoạch nhựa cổ thụ chống huyết độc
- Bán linh thức trái cây mùa từ cổ thụ
- Nhận viện trợ từ các thế lực đồng minh (không ổn định)
arcs:
  - arc: 1
    status: Kiên trì cầm cự
    rank: Hạng Năm
    leader: Đoàn Trưởng Mộc Thâm Căn
    population: 28
    territory:
      - Tuyến phòng thủ rìa Rừng Huyết Độc (Biên giới Vĩnh Hằng Sâm Lâm)
    assets:
      - name: Vạn Niên Tùng
        type: Tài Nguyên
      - name: 12 Cổ Thụ Thiêng Liên Kết
        type: Tài Nguyên
      - name: Trận pháp "Vạn Căn Hộ Lâm Trận"
        type: Trận Pháp
    stats: [80, 100, 120, 28, 150, 60]
    divisions:
      - name: Thủ Hộ Đội
        role: Tuần tra tuyến phòng thủ, ngăn chặn huyết độc xâm nhập Vĩnh Hằng Sâm Lâm
        headcount:
          hoi_truong: 1
          pho_hoi_truong: 4
          thanh_vien: 20
          tong_quan: 3
        members:
          - character: Mộc Thâm Căn
            position: Đoàn Trưởng
            cultivation: Kim Đan Sơ Kỳ
          - character: "[Thủ Hộ Trưởng Bắc]"
            position: Thủ Hộ Trưởng
            cultivation: Trúc Cơ Hậu Kỳ
            placeholder: true
          - character: "[Thủ Hộ Trưởng Nam]"
            position: Thủ Hộ Trưởng
            cultivation: Trúc Cơ Hậu Kỳ
            placeholder: true
    relationships:
      - faction: Tinh Linh Vương Đình
        description: Quan hệ chủ tớ trên danh nghĩa nhưng thực tế bị bỏ rơi. Đoàn vẫn trung thành gửi báo cáo, Vương Đình không hồi đáp.
        diplomacy:
          lien_minh: 20
          tin: 10
          uy_hiep: 0
          thuong_mai: 0
          on_oan: -30
          le_thuoc: 40
      - faction: Cổ Thụ Tế Tự Đoàn
        description: Cùng tôn thờ cổ thụ, Tế Tự Đoàn hỗ trợ kiến thức về linh thực và nhựa cổ thụ. Hai bên tôn trọng lẫn nhau.
        diplomacy:
          lien_minh: 40
          tin: 50
          uy_hiep: 0
          thuong_mai: 20
          on_oan: 10
          le_thuoc: 0
      - faction: Huyết Thảo Đường
        description: Kẻ thù tự nhiên, Huyết Thảo Đường khai thác tài nguyên từ Rừng Huyết Độc và vô tình thúc đẩy huyết độc lan rộng.
        diplomacy:
          lien_minh: -30
          tin: -40
          uy_hiep: 30
          thuong_mai: -50
          on_oan: -40
          le_thuoc: 0
---

# CỔ THỤ THỦ HỘ ĐOÀN (古树守护团)

## I. Tổng Quan (总览)
Cổ Thụ Thủ Hộ Đoàn là tiền đồn phòng thủ cuối cùng ngăn chặn Rừng Huyết Độc xâm nhập Vĩnh Hằng Sâm Lâm, tọa lạc tại vùng biên giới nơi hai hệ sinh thái đối lập va chạm. Được Tinh Linh Vương Đình thành lập cách đây ngàn năm, Đoàn đã bị lãng quên bởi chính người tạo ra nó khi Vương Đình rút sâu vào rừng và cô lập. Dù không còn tiếp tế, không còn viện trợ, hai mươi tám thành viên vẫn kiên trì sứ mệnh ban đầu — bảo vệ hàng cổ thụ thiêng, duy trì tuyến phòng thủ sinh tử cho cả chủng tộc.

## II. Địa Lý & Tài Nguyên (地理与资源)
Tuyến phòng thủ của Đoàn nằm ở vùng rìa nơi Rừng Huyết Độc giáp Vĩnh Hằng Sâm Lâm — một dải đất hẹp nơi cây xanh và cây đỏ đan xen, khí lành và khí độc hòa trộn tạo nên bầu không khí ngột ngạt. Mười hai cổ thụ thiêng xếp thành hàng, rễ đan xen dưới mặt đất tạo thành hàng rào tự nhiên, thân cây khổng lồ nối liền bằng cành lá tạo bức tường xanh. Tinh Linh sống trong hốc cây và trên cành, nơi cao nhất là Vạn Niên Tùng — cổ thụ lớn nhất, gốc rộng như một ngôi nhà, thân cao xuyên qua tầng sương. Nhựa cổ thụ tại đây có tác dụng đặc biệt chống huyết độc xâm nhập, là tài nguyên quý giá nhất của Đoàn. Mỗi mùa, cổ thụ ra trái linh có tác dụng bồi bổ linh lực cho người ăn.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
"Cổ thụ đứng vững ngàn năm, ta cũng phải đứng vững." Câu nói này là tín điều duy nhất của Thủ Hộ Đoàn. Sứ mệnh bảo vệ cổ thụ thiêng không chỉ là nhiệm vụ mà là lý do tồn tại duy nhất của mọi thành viên. Mỗi Tinh Linh khi gia nhập sẽ chọn một cổ thụ làm "Bạn Cây" — thực hiện nghi lễ liên kết linh hồn, từ đó cùng sống cùng chết với cây. Quy tắc nghiêm khắc nhất: không rời vị trí canh gác khi có dấu hiệu huyết độc lan rộng, không chặt cành cổ thụ thiêng dù bất kỳ lý do gì. Thà chết tại chỗ còn hơn để cổ thụ bị tổn hại.

## IV. Cơ Cấu Tổ Chức (组织结构)
Đoàn Trưởng Mộc Thâm Căn là nam Tinh Linh cổ đại, da xám như vỏ cây, đôi mắt xanh lá sáng rực trong bóng tối. Ông đã liên kết với Vạn Niên Tùng hơn 800 năm, hấp thụ linh lực từ cây để duy trì tu vi Kim Đan Sơ Kỳ. Bốn Thủ Hộ Trưởng tu vi Trúc Cơ Hậu Kỳ, mỗi người phụ trách canh giữ một đoạn tuyến phòng thủ, chỉ huy các Thủ Hộ Viên tuần tra liên tục ngày đêm. Hai mươi Thủ Hộ Viên từ Luyện Khí đến Trúc Cơ Sơ Kỳ, chính là lực lượng chiến đấu trực tiếp. Ngoài ra, mỗi một trong mười hai cổ thụ thiêng đều đã liên kết với một Tinh Linh, hình thành cặp đôi "Nhân Thụ Nhất Thể".

## V. Công Pháp & Trận Pháp (功法与阵法)
- **Công Pháp:** "Cổ Thụ Liên Tâm Quyết" — Tinh Linh liên kết thần thức với cổ thụ bạn cây, hấp thụ linh lực từ rễ cây để tu luyện, đổi lại phải bảo vệ cây bằng tính mạng. Người tu luyện có thể mượn sức mạnh mộc hệ của cổ thụ để tăng cường phòng ngự nhất thời, biến da thịt cứng như vỏ cây cổ đại. Tuy nhiên, nếu cổ thụ bạn cây chết, Tinh Linh liên kết sẽ bị phản phệ, nhẹ thì tu vi tàn phế, nặng thì tử vong.
- **Trận Pháp:** "Vạn Căn Hộ Lâm Trận" — mười hai cổ thụ thiêng đồng thời kích hoạt hệ rễ dưới đất, tạo thành bức tường rễ cây dày đặc ngăn mọi sự xâm nhập từ Rừng Huyết Độc. Khi trận pháp kích hoạt, rễ cây bùng lên khỏi mặt đất như bức thành sống, có thể trói chặt và nghiền nát bất kỳ thứ gì cố vượt qua. Cần cả mười hai cây hoạt động đồng bộ mới đạt hiệu quả tối đa — hiện đã mất bốn cây, sức mạnh trận pháp giảm đáng kể.

## VI. Đặc Sản Môn Phái (门派特产)
- **Nhựa Kháng Huyết Độc:** Nhựa cổ thụ thiêng đặc chế, bôi lên da có thể cách ly huyết độc trong vài canh giờ. Đây là vật phẩm sinh tồn quan trọng nhất cho bất kỳ ai hoạt động gần Rừng Huyết Độc.
- **Linh Thức Trái Mùa:** Trái cây linh từ cổ thụ thiêng, mỗi mùa chỉ ra vài chục quả. Ăn vào bồi bổ linh lực mộc hệ, đặc biệt hữu dụng cho tu sĩ bị nội thương.
- **Mộc Giáp Vỏ Cây:** Vỏ cây cổ thụ rụng tự nhiên được thu gom và chế tác thành áo giáp nhẹ nhưng cứng, có khả năng tự phục hồi nếu được tưới nhựa cổ thụ.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Tuyến Phòng Thủ Cổ Thụ:** Hàng mười hai cổ thụ thiêng xếp thành dải dài, rễ đan xen dưới đất và cành nối trên cao tạo thành bức tường phòng thủ tự nhiên. Đây là công trình phòng thủ sống, có khả năng tự tái tạo nhưng đang suy yếu do huyết độc xâm thực.
- **Hốc Cây Quân Doanh:** Mỗi Tinh Linh ở trong hốc tự nhiên trên thân cổ thụ bạn cây, vừa là nơi nghỉ ngơi vừa là vị trí chiến đấu. Từ các hốc trên cao có thể quan sát được toàn bộ tuyến biên giới.
- **Đài Quan Sát Vạn Niên Tùng:** Trên ngọn Vạn Niên Tùng có đài quan sát bằng gỗ đã phong hóa, nơi Mộc Thâm Căn theo dõi tình hình Rừng Huyết Độc hàng ngày.

## VIII. Kinh Tế (经济)
Kinh tế của Thủ Hộ Đoàn gần như không tồn tại theo nghĩa thông thường. Khi còn được Vương Đình hỗ trợ, Đoàn nhận tiếp tế đều đặn về lương thực, dược phẩm và vật tư. Kể từ khi Vương Đình cô lập, Đoàn phải tự cung tự cấp bằng cách thu hoạch trái cây linh từ cổ thụ, đổi nhựa kháng huyết độc với các nhóm nhỏ qua lại vùng biên giới. Đời sống cực kỳ thiếu thốn, nhiều thành viên phải nhịn ăn hoặc chia sẻ khẩu phần ít ỏi.

## IX. Lịch Sử Tóm Tắt (简史)
Cổ Thụ Thủ Hộ Đoàn được Tinh Linh Vương Đình thành lập cách đây một ngàn năm khi huyết độc bắt đầu lan từ Rừng Huyết Độc sang Vĩnh Hằng Sâm Lâm. Buổi đầu, Đoàn có hơn trăm thành viên tinh nhuệ, được trang bị đầy đủ và nhận viện trợ thường xuyên. Khi Vương Đình dần rút sâu vào trung tâm rừng và cắt đứt liên lạc với bên ngoài, Đoàn bị bỏ rơi — không tiếp tế, không thay quân, không chỉ thị mới. Trong 200 năm qua, Đoàn đã mất tám thành viên vì huyết độc xâm nhập mạnh hơn: cổ thụ bạn cây bị huyết độc giết chết, Tinh Linh liên kết cũng theo cây mà chết. Mộc Thâm Căn gửi đi vô số thông điệp cầu cứu nhưng không bao giờ nhận được hồi âm.

## X. Giai Thoại & Bí Mật (轶事与秘密)
Vạn Niên Tùng — cổ thụ lớn nhất — thực ra có linh trí riêng, có thể giao tiếp với Mộc Thâm Căn bằng hình ảnh mơ hồ trong giấc mơ. Cây đã cho ông thấy ký ức về thời Thượng Cổ khi Rừng Huyết Độc chưa tồn tại — toàn bộ vùng đất ấy từng là rừng xanh bạt ngàn, và điều gì đó kinh thiên đã xảy ra khiến nó biến thành vùng đất chết.

Mộc Thâm Căn biết rằng huyết độc đang lan nhanh hơn mỗi năm, xâm thực dần từng tấc rễ cổ thụ thiêng. Theo tính toán của ông, trong năm mươi năm nữa tuyến phòng thủ sẽ sụp đổ hoàn toàn, huyết độc sẽ tràn vào Vĩnh Hằng Sâm Lâm. Ông đã chuẩn bị một hạt giống từ Vạn Niên Tùng, giao cho Hộ Vệ trẻ nhất với nhiệm vụ: nếu tuyến phòng thủ thất thủ, hãy mang hạt giống chạy sâu vào rừng và gieo ở nơi an toàn nhất.

## XI. Quan Hệ Thế Lực (势力关系)
- **Tinh Linh Vương Đình:** Trên danh nghĩa vẫn là cấp dưới, nhưng thực tế đã bị bỏ rơi hoàn toàn. Mộc Thâm Căn không oán hận mà chỉ thất vọng, vẫn giữ trung thành với sứ mệnh ban đầu.
- **Cổ Thụ Tế Tự Đoàn:** Đồng đạo cùng tôn thờ cổ thụ. Tế Tự Đoàn đôi khi gửi nhựa cổ thụ có dược tính đặc biệt giúp Thủ Hộ Đoàn chống huyết độc.
- **Huyết Thảo Đường:** Kẻ thù gián tiếp. Huyết Thảo Đường khai thác huyết thảo trong Rừng Huyết Độc, hoạt động của họ vô tình khuấy động huyết độc và thúc đẩy nó lan rộng hơn.
