---
type: faction
name: Hải Tảo Nông Dân Hội
hantu: 海藻农民会
faction_type: Hội
alignment: 3
race: Hải Tộc (cá nhỏ, tôm, sinh vật biển cấp thấp)
region: Vô Tận Hải
founded: Không rõ (tồn tại từ rất lâu)
founder: Không rõ (tự phát hình thành)
emblem: Tao_Linh_Xanh.png
specialty: Dưỡng Tảo Thuật, Canh tác đáy biển, Nhạc nông nghiệp
economy:
- Trồng và thu hoạch tảo linh (lương thực chính của Hải Tộc)
- Bán tảo linh dư thừa cho thương nhân biển
- Cung cấp nguyên liệu thô cho Hải Thảo Dược Sư
arcs:
  - arc: 1
    status: Bị bóc lột ổn định
    rank: Không Xếp Hạng
    leader: Hội Trưởng Phì Ngư Ông
    population: 82
    territory:
      - Cánh Đồng Tảo (rìa lãnh thổ Hải Thần Cung)
    assets:
      - name: Cánh Đồng Tảo Linh
        type: Tài Nguyên
      - name: Tảo Đột Biến (bí mật)
        type: Tài Nguyên
    stats: [5, 30, 10, 50, 8, 5]
    divisions:
      - name: Nông Đoàn
        role: Trồng trọt, thu hoạch và phân phối tảo linh
        headcount:
          hoi_truong: 1
          pho_hoi_truong: 0
          thanh_vien: 79
          tong_quan: 2
        members:
          - character: Phì Ngư Ông
            position: Hội Trưởng
            cultivation: Trúc Cơ Sơ Kỳ
            placeholder: false
          - character: "[Giám Sát Viên Giáp]"
            position: Giám Sát Viên (do Hải Thần Cung cử)
            cultivation: Trúc Cơ Trung Kỳ
            placeholder: true
          - character: "[Giám Sát Viên Ất]"
            position: Giám Sát Viên (do Hải Thần Cung cử)
            cultivation: Luyện Khí Đỉnh Phong
            placeholder: true
    relationships:
      - faction: Hải Thần Cung
        description: Quan hệ chủ - tá điền. Hải Thần Cung sở hữu đất canh tác và thu thuế nặng, nông dân chỉ giữ lại chưa đến ba phần mười thu hoạch. Từng xin giảm thuế nhưng bị từ chối lạnh lùng.
        diplomacy:
          lien_minh: 0
          tin: 10
          uy_hiep: 70
          thuong_mai: 20
          on_oan: -30
          le_thuoc: 90
      - faction: Hải Thảo Dược Sư
        description: Quan hệ cung ứng thân thiện. Nông dân bán tảo linh nguyên liệu cho các dược sư, đổi lại nhận thuốc chữa bệnh miễn phí cho thành viên ốm yếu.
        diplomacy:
          lien_minh: 30
          tin: 50
          uy_hiep: 0
          thuong_mai: 60
          on_oan: 0
          le_thuoc: 0
      - faction: Hải Quy Trưởng Lão Hội
        description: Quan hệ láng giềng hòa hảo. Nông dân thỉnh thoảng mang tảo linh đến cúng dường các trưởng lão để đổi lấy lời khuyên và dự báo thời tiết biển.
        diplomacy:
          lien_minh: 20
          tin: 40
          uy_hiep: 0
          thuong_mai: 25
          on_oan: 0
          le_thuoc: 0
---

# HẢI TẢO NÔNG DÂN HỘI (海藻农民会)

## I. Tổng Quan (总览)
Hải Tảo Nông Dân Hội là tổ chức của những Hải Tộc cấp thấp chuyên canh tác tảo linh tại rìa lãnh thổ Hải Thần Cung, không xếp hạng trong bảng thế lực Vô Tận Hải. Với tám mươi hai thành viên gồm cá nhỏ, tôm, và các sinh vật biển giản đơn, hội là mắt xích thấp nhất trong chuỗi cung ứng lương thực dưới đáy biển — quan trọng nhưng bị coi thường. Đứng đầu là Hội Trưởng Phì Ngư Ông, một con cá linh béo tốt vui tính ở cảnh giới Trúc Cơ Sơ Kỳ, nổi tiếng với triết lý lạc quan bất chấp hoàn cảnh bị bóc lột. Tảo linh do hội trồng là lương thực chính của nhiều Hải Tộc, nhưng nông dân chỉ được giữ lại phần nhỏ thu hoạch sau khi nộp thuế cho Hải Thần Cung.

## II. Địa Lý & Tài Nguyên (地理 与 资源)
Cánh Đồng Tảo nằm ở rìa lãnh thổ Hải Thần Cung, trải dài trên một vùng đáy biển phì nhiêu nơi hải lưu ấm mang dinh dưỡng liên tục bồi đắp. Tảo linh là lương thực cơ bản của Hải Tộc, cung cấp năng lượng linh khí ở mức thấp nhưng ổn định, đủ để duy trì sự sống cho hàng nghìn cư dân biển. Đất canh tác thuộc quyền sở hữu của Hải Thần Cung — nông dân chỉ là tá điền, không có quyền sở hữu mảnh đất mình cày cuốc. Nếu hải lưu ấm thay đổi hướng, mùa màng sẽ thất thu nghiêm trọng, và nông dân không có tài nguyên dự trữ để chống chịu. Dưới lớp đất canh tác có tầng trầm tích cổ đại chứa hóa thạch linh, nhưng khai quật sẽ phá hủy cánh đồng nên chưa ai dám đụng đến.

## III. Văn Hóa & Tín Ngưỡng (文化 与 信仰)
Thành viên đều là Hải Tộc cấp thấp sống giản dị, quanh năm suốt tháng trồng tảo, thu hoạch, nộp thuế. Họ tin rằng tảo linh là "tóc của biển cả" — cắt đi sẽ mọc lại, nhưng phải tôn trọng và không được tham lam lấy quá nhiều, nếu không biển cả sẽ giận dữ. Mỗi mùa thu hoạch, nông dân cùng tổ chức Lễ Hạ Điền — tất cả quây quần hát bài ca cổ truyền từ đời ông cha, cầu mùa màng bội thu. Phì Ngư Ông thường nói: "Tảo mọc lại, nỗi buồn cũng qua đi" — câu nói này trở thành phương châm sống của cả hội, thể hiện sự chấp nhận số phận nhưng không hoàn toàn mất hy vọng. Dù bị bóc lột, nông dân vẫn giữ tình đoàn kết nội bộ mạnh mẽ, sẵn sàng chia sẻ phần tảo ít ỏi cho gia đình nào gặp khó khăn.

## IV. Cơ Cấu Tổ Chức (组织结构)
Hội có cơ cấu đơn giản, xoay quanh Phì Ngư Ông với vai trò hội trưởng kiêm người đại diện. Tám mươi nông dân Hải Tộc nhỏ, phần lớn ở Luyện Khí hoặc chưa khai mở linh trí, phân chia thành các nhóm canh tác theo từng khu vực của cánh đồng. Hai Giám Sát Viên do Hải Thần Cung cử đến thường trực, nhiệm vụ chính là thu thuế và giám sát sản lượng — trên danh nghĩa là bảo vệ nông dân, thực chất là đảm bảo Hải Thần Cung nhận đủ phần. Phì Ngư Ông không có quyền lực thực sự — mọi quyết định quan trọng đều phải qua sự đồng ý của giám sát viên. Tuy nhiên, ông được nông dân yêu mến và nghe theo vì sự vui vẻ, chân thành và khả năng trồng tảo vượt trội.

## V. Công Pháp & Trận Pháp (功法 与 阵法)
Hội không có bất kỳ công pháp chiến đấu nào, chỉ nắm giữ Dưỡng Tảo Thuật — kỹ thuật trồng và chăm sóc tảo linh được truyền từ đời này sang đời khác, bao gồm cách đọc hải lưu, phân biệt chất đất, và điều chỉnh mật độ gieo trồng. Phì Ngư Ông biết thêm Phì Thổ Thuật — một tiểu pháp thuật làm đáy biển phì nhiêu hơn bằng cách ngưng tụ dinh dưỡng từ nước biển vào đất, giúp tảo linh mọc tốt và nhanh hơn. Đây không phải công pháp chính thống mà là bí truyền nông nghiệp, không có giá trị chiến đấu nhưng vô cùng quý giá cho việc canh tác. Hội hoàn toàn không có khả năng tự vệ, phụ thuộc hoàn toàn vào sự bảo hộ danh nghĩa của Hải Thần Cung.

## VI. Đặc Sản Môn Phái (门派特产)
- **Tảo Linh Cơ Bản:** Lương thực chính của Hải Tộc cấp thấp, chứa linh khí thủy hệ ở mức tối thiểu. Tuy không quý giá nhưng là nhu yếu phẩm thiết yếu, thiếu nó thì hàng nghìn Hải Tộc sẽ đói.
- **Tảo Linh Phì Ông:** Loại tảo đặc biệt do Phì Ngư Ông dùng Phì Thổ Thuật trồng, kích thước lớn gấp đôi và hàm lượng dinh dưỡng cao hơn tảo thường. Được các Hải Tộc giàu có ưa chuộng làm thực phẩm cao cấp.
- **Nước Dưỡng Tảo:** Dung dịch dinh dưỡng chiết xuất từ quá trình canh tác, có tác dụng nuôi dưỡng linh thực vật thủy sinh. Hải Thảo Dược Sư mua để bổ sung cho rừng tảo dược liệu.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Cánh Đồng Tảo Linh:** Khu vực canh tác chính trải dài trên đáy biển phì nhiêu, chia thành mười hai lô theo hải lưu và chất đất. Mỗi lô do một nhóm nông dân phụ trách, luân canh theo mùa.
- **Lều Phì Ông:** Túp lều đơn sơ của Hội Trưởng nằm giữa cánh đồng, vừa là nơi ở vừa là chỗ họp mặt cho nông dân. Bên trong có bếp lửa san hô nhỏ dùng nấu canh tảo cho cả hội.
- **Trạm Thu Thuế:** Kiến trúc nhỏ do Hải Thần Cung xây, nơi hai giám sát viên đóng quân. Tảo linh thu hoạch được chuyển đến đây cân đo trước khi chia phần.

## VIII. Kinh Tế (经济)
Kinh tế của hội hoàn toàn xoay quanh việc trồng và thu hoạch tảo linh. Mỗi mùa thu hoạch, Hải Thần Cung lấy đi bảy phần mười sản lượng dưới danh nghĩa thuế sử dụng đất. Ba phần mười còn lại chia cho nông dân, trong đó một phần nhỏ được bán cho Hải Thảo Dược Sư và thương nhân biển để đổi lấy vật dụng cần thiết. Thu nhập cá nhân cực thấp, đủ sống nhưng không có tích lũy. Giám sát viên từ Hải Thần Cung thường xuyên ăn chặn — báo cáo thu hoạch thấp hơn thực tế, bỏ túi phần chênh lệch, khiến nông dân càng khốn đốn hơn. Phì Ngư Ông biết nhưng không dám tố cáo vì sợ bị trả thù.

## IX. Lịch Sử Tóm Tắt (简史)
Cánh Đồng Tảo tồn tại từ rất lâu trước khi hội được thành lập, luôn do Hải Tộc cấp thấp canh tác từ đời này sang đời khác. Khi Hải Thần Cung mở rộng lãnh thổ, vùng đất này bị sáp nhập và nông dân trở thành tá điền. Phì Ngư Ông đứng ra tổ chức nông dân thành hội để có tiếng nói chung, nhưng tiếng nói đó chưa bao giờ được lắng nghe. Hội từng gửi đơn xin giảm thuế lên Hải Thần Cung nhiều lần, tất cả đều bị từ chối với câu trả lời lạnh lùng: "Các ngươi nên biết ơn vì được phép canh tác trên đất của Hải Thần." Dù vậy, Phì Ngư Ông vẫn vui vẻ lạc quan, coi sự tồn tại bền bỉ của hội qua bao thế hệ là bằng chứng cho sức mạnh của sự khiêm nhường.

## X. Giai Thoại & Bí Mật (轶事 与 秘密)
Phì Ngư Ông vô tình phát hiện một loại tảo đột biến mọc nhanh gấp mười lần bình thường tại một góc khuất của cánh đồng. Ông giấu kín phát hiện này, chỉ bí mật trồng một mảnh nhỏ và chia cho những gia đình khó khăn nhất — nếu Hải Thần Cung biết, chắc chắn thuế sẽ tăng hoặc tảo đột biến sẽ bị tịch thu. Dưới cánh đồng tảo có tầng đất cổ đại chứa hóa thạch linh — các trưởng lão Hải Quy xác nhận đó là di tích từ kỷ nguyên trước, nếu khai quật có thể tìm được bảo vật nhưng đồng thời phá hủy hoàn toàn cánh đồng. Hai giám sát viên từ Hải Thần Cung đang bí mật ăn chặn thuế, báo cáo sản lượng thấp hơn thực tế và bỏ túi phần chênh lệch — nếu bị phát hiện, cả hai sẽ bị xử tử, nhưng nông dân không dám tố cáo vì sợ mất đi sự bảo hộ.

## XI. Quan Hệ Thế Lực (势力关系)
Hải Tảo Nông Dân Hội ở vị trí thấp nhất trong hệ thống quyền lực Vô Tận Hải, phụ thuộc hoàn toàn vào Hải Thần Cung về đất canh tác và sự bảo hộ. Mối quan hệ với Hải Thần Cung mang tính chủ - tá điền, bất bình đẳng sâu sắc nhưng nông dân không có lựa chọn nào khác. Hải Thảo Dược Sư là đối tác thương mại thân thiện nhất, thường xuyên mua tảo linh nguyên liệu và đổi lại cung cấp thuốc chữa bệnh. Hải Quy Trưởng Lão Hội là láng giềng đáng tin cậy, sẵn sàng cho lời khuyên và dự báo thời tiết biển giúp nông dân chuẩn bị cho mùa vụ.
