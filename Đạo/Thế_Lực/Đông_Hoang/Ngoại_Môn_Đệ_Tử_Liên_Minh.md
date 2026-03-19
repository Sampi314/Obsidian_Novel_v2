---
type: faction
name: Ngoại Môn Đệ Tử Liên Minh
hantu: 外门弟子联盟
faction_type: Liên Minh
alignment: 1
race: Nhân Tộc
region: Đông Hoang
founded: 30 năm trước
founder: Ảnh Thủ (danh tính bí mật)
emblem: Ngoai_Mon_De_Tu_Lien_Minh.png
specialty: Tình báo nội bộ tông phái, Trao đổi tài nguyên cấp thấp, Hỗ trợ ngoại môn đệ tử
economy:
- Trao đổi tài nguyên tu luyện cấp thấp giữa các tông phái
- Chia sẻ thông tin nội bộ và cảnh báo nguy hiểm
- Buôn bán nhỏ lẻ pháp khí và đan dược bị thải loại
arcs:
  - arc: 1
    status: Hoạt động bí mật
    rank: Không Xếp Hạng
    leader: Ảnh Thủ (bí mật)
    population: 150
    territory:
      - Không có lãnh thổ cố định
    assets:
      - name: Hệ thống Truyền Âm Phù tự hủy
        type: Tài Nguyên
      - name: Mạng lưới liên lạc viên tại các tông phái
        type: Tài Nguyên
    stats: [10, 15, 5, 150, 5, 30]
    divisions:
      - name: Ban Liên Lạc Trung Tâm
        role: Điều phối thông tin giữa các liên lạc viên tại từng tông phái
        headcount:
          minh_chu: 1
          pho_minh_chu: 0
          truong_lao: 0
          su_gia: 5
          thanh_vien_phai: 144
        members:
          - character: "[Ảnh Thủ]"
            position: Minh Chủ
            cultivation: Trúc Cơ Viên Mãn
            placeholder: true
          - character: "[Liên Lạc Viên — Cửu Hoa Kiếm Tông]"
            position: Sứ Giả
            cultivation: Trúc Cơ Trung Kỳ
            placeholder: true
          - character: "[Liên Lạc Viên — Vân Tông]"
            position: Sứ Giả
            cultivation: Trúc Cơ Sơ Kỳ
            placeholder: true
    relationships:
      - faction: Cửu Hoa Kiếm Tông
        description: Liên Minh có nhiều thành viên nhất từ ngoại môn Cửu Hoa. Nếu bị phát hiện, toàn bộ thành viên sẽ bị trục xuất hoặc tệ hơn.
        diplomacy:
          lien_minh: -50
          tin: -60
          uy_hiep: 70
          thuong_mai: 0
          on_oan: -40
          le_thuoc: 60
      - faction: Vân Tông
        description: Ngoại môn đệ tử Vân Tông cũng bí mật tham gia. Vân Tông có phần ôn hòa hơn nhưng vẫn sẽ trừng phạt nếu phát hiện.
        diplomacy:
          lien_minh: -40
          tin: -50
          uy_hiep: 50
          thuong_mai: 0
          on_oan: -30
          le_thuoc: 50
      - faction: Phiêu Bạt Khách Sạn Liên Minh
        description: Một số điểm hẹn bí mật của Liên Minh đặt tại quán trọ thuộc Phiêu Bạt Khách Sạn Liên Minh, nhưng chủ quán không biết khách hàng thực sự là ai.
        diplomacy:
          lien_minh: 0
          tin: 0
          uy_hiep: 0
          thuong_mai: 10
          on_oan: 0
          le_thuoc: 0
---

# Ngoại Môn Đệ Tử Liên Minh (外门弟子联盟)

## I. Tổng Quan (总览)
Ngoại Môn Đệ Tử Liên Minh là một tổ chức bí mật kết nối ngoại môn đệ tử từ nhiều tông phái lớn tại Đông Hoang. Ra đời từ sự bất mãn với hệ thống phân biệt đối xử giữa nội môn và ngoại môn, Liên Minh cung cấp cho những đệ tử bị thiệt thòi một mạng lưới hỗ trợ lẫn nhau — chia sẻ thông tin, trao đổi tài nguyên cấp thấp, và cảnh báo nguy hiểm. Với ước tính 100-200 thành viên rải rác tại nhiều tông phái, Liên Minh hoạt động cực kỳ kín đáo dưới sự điều phối của một nhân vật bí ẩn chỉ biết qua danh hiệu "Ảnh Thủ". Dù không có lãnh thổ, không có trụ sở, và không xếp hạng trên bất kỳ bảng thế lực nào, Liên Minh nắm giữ thứ mà nhiều tông phái sợ hãi: thông tin nội bộ từ bên trong chính họ.

## II. Địa Lý & Tài Nguyên (地理与资源)
Ngoại Môn Đệ Tử Liên Minh không có lãnh thổ hay trụ sở cố định — đây vừa là điểm yếu vừa là lớp bảo vệ quan trọng nhất. Các cuộc họp diễn ra tại những địa điểm bí mật thay đổi liên tục: hang động hoang vắng gần các tông phái, quán trà ven đường ít người qua lại, hoặc khoảng rừng thưa xa khu dân cư. Liên lạc viên tại mỗi tông phái chịu trách nhiệm chọn và thay đổi điểm hẹn, đảm bảo không bao giờ dùng cùng một địa điểm quá hai lần. Tài nguyên quý giá nhất là thông tin nội bộ các tông phái — lịch trình tuần tra, phân phối nhiệm vụ, thời gian bế quan của trưởng lão, và đặc biệt là danh sách pháp khí bị thải loại từ nội môn mà ngoại môn có thể thu gom. Ngoài ra, hệ thống Truyền Âm Phù tự hủy là công cụ liên lạc duy nhất, được chế tạo đơn giản nhưng hiệu quả.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
Triết lý cốt lõi của Liên Minh nằm trong câu nói truyền miệng: "Ngoại môn cũng là đệ tử, nhưng chẳng ai coi chúng ta là người." Đây không phải lời kêu gọi nổi loạn mà là sự khẳng định quyền được đối xử công bằng. Thành viên Liên Minh tin rằng hệ thống phân biệt nội - ngoại môn ở hầu hết các tông phái là bất công: ngoại môn đệ tử chịu nhiệm vụ nặng nhọc nhất, nhận tài nguyên ít nhất, và bị khinh thường bởi nội môn dù cùng tu luyện dưới một mái nhà. Quy tắc sống còn duy nhất là tuyệt đối giữ bí mật thân phận — nếu bị phát hiện, Liên Minh sẽ không thừa nhận và không thể cứu. Cách nhận diện đồng minh được thực hiện qua ám hiệu tinh tế: cầm chén trà lật ngược khi uống xong. Đơn giản nhưng hiệu quả — chỉ người trong cuộc mới nhận ra.

## IV. Cơ Cấu Tổ Chức (组织结构)
Liên Minh có cơ cấu tối giản nhằm giảm thiểu rủi ro bị phát hiện. Đứng đầu là Ảnh Thủ — người sáng lập, thân phận hoàn toàn bí mật, chỉ liên lạc với năm Liên Lạc Viên thông qua Truyền Âm Phù. Không ai biết Ảnh Thủ là nam hay nữ, thuộc tông phái nào, hay thậm chí còn sống hay không. Năm Liên Lạc Viên, mỗi người phụ trách mạng lưới thành viên tại một tông phái lớn, đều là ngoại môn đệ tử tại chỗ. Họ không biết danh tính thực của nhau — chỉ giao tiếp qua Truyền Âm Phù và ám hiệu. Dưới mỗi Liên Lạc Viên là các thành viên thường, ước tính 100-200 người, nhưng không ai nắm được con số chính xác vì hệ thống được thiết kế để mỗi người chỉ biết tối đa 3-5 đồng minh.

## V. Công Pháp & Trận Pháp (功法与阵法)
Ngoại Môn Đệ Tử Liên Minh không có công pháp riêng biệt — thành viên tu luyện theo công pháp ngoại môn của tông phái mình. Đây vừa là hạn chế vừa là lợi thế: không có dấu hiệu tu luyện nào có thể lộ danh tính thành viên Liên Minh. Tuy nhiên, Liên Minh khuyến khích thành viên trao đổi kinh nghiệm tu luyện giữa các tông phái — một ngoại môn đệ tử Cửu Hoa có thể học được vài chiêu thức phòng thân từ ngoại môn Vân Tông thông qua mô tả bằng lời. Công cụ đặc trưng duy nhất là hệ thống Truyền Âm Phù tự hủy — phù lục đơn giản ghi thông điệp ngắn, tự bốc cháy sau khi người nhận đọc xong, không để lại bằng chứng. Kỹ thuật chế tạo phù này được Ảnh Thủ phát minh và truyền cho các Liên Lạc Viên.

## VI. Đặc Sản Môn Phái (门派特产)
- **Truyền Âm Phù Tự Hủy:** Phù lục chế tạo đơn giản từ giấy linh và một ít mực linh khí, có thể ghi thông điệp ngắn. Sau khi mở ra đọc, phù tự bốc cháy trong 10 giây, không để lại tro hay dấu vết. Sản phẩm độc quyền của Liên Minh.
- **Mạng Lưới Thông Tin Nội Bộ:** Tài sản vô hình nhưng giá trị nhất — Liên Minh nắm được lịch trình, phân bổ tài nguyên, và những bí mật nhỏ của nhiều tông phái, tạo ra lợi thế sinh tồn cho ngoại môn đệ tử.
- **Pháp Khí Tái Chế:** Thành viên thu gom pháp khí bị thải loại từ nội môn, sửa chữa sơ bộ rồi trao đổi giữa các tông phái, giúp ngoại môn đệ tử có trang bị tốt hơn với chi phí thấp.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Điểm Hẹn Luân Chuyển:** Danh sách các địa điểm bí mật gần từng tông phái, được thay đổi định kỳ. Bao gồm hang động, quán trà, rừng thưa, và đôi khi phòng trọ tại quán khách vùng biên.
- **Kho Trao Đổi Tạm:** Các điểm cất giấu nhỏ (hốc đá, gốc cây rỗng) nơi thành viên để lại và nhận tài nguyên trao đổi mà không cần gặp mặt trực tiếp.
- **Hệ Thống Ám Hiệu:** Bộ ám hiệu phức tạp bao gồm cách cầm chén trà, cách xếp đũa, và vài cử chỉ tay nhất định, dùng để nhận diện đồng minh trong đám đông.

## VIII. Kinh Tế (经济)
Kinh tế của Liên Minh hoạt động trên nguyên tắc trao đổi ngang hàng, không dùng linh thạch làm trung gian để tránh để lại dấu vết giao dịch. Thành viên trao đổi tài nguyên tu luyện cấp thấp: đan dược sắp hết hạn, pháp khí bị thải loại đã sửa chữa, nguyên liệu luyện khí phổ thông, và đặc biệt là thông tin. Một ngoại môn đệ tử Cửu Hoa có thể đổi tin tức về khu vực nhiệm vụ nguy hiểm để lấy vài viên Luyện Khí Đan từ ngoại môn đệ tử Liệt Dương Tông. Quy mô giao dịch rất nhỏ — mỗi lần chỉ vài món — nhưng đối với ngoại môn đệ tử vốn bị thiệt thòi về tài nguyên, mỗi viên đan dược và mỗi mẩu thông tin đều có thể là sự khác biệt giữa sống và chết.

## IX. Lịch Sử Tóm Tắt (简史)
Liên Minh hình thành khoảng 30 năm trước từ một nhóm nhỏ ngoại môn đệ tử Cửu Hoa Kiếm Tông bí mật bàn cách giúp đỡ lẫn nhau. Người khởi xướng — sau này lấy danh hiệu Ảnh Thủ — nhận ra rằng ngoại môn đệ tử ở mọi tông phái đều chung cảnh ngộ: nhiệm vụ nặng, tài nguyên ít, cơ hội thăng tiến gần như không có. Từ nhóm 5-6 người ban đầu, Ảnh Thủ dần kết nối với ngoại môn đệ tử tại Vân Tông, Liệt Dương Tông, Thái Ất Môn và các tông phái khác. Hoạt động chính luôn giữ ở mức tối thiểu — chia sẻ thông tin, trao đổi vật phẩm nhỏ, và cảnh báo nhau khi có nguy hiểm — vì Ảnh Thủ hiểu rằng bất kỳ hành động nào quá lớn sẽ thu hút sự chú ý của các tông phái. Trong 30 năm qua, Liên Minh chưa từng bị phát hiện, nhưng cũng chưa từng dám làm điều gì táo bạo.

## X. Giai Thoại & Bí Mật (轶事与秘密)
Danh tính của Ảnh Thủ là bí ẩn lớn nhất của Liên Minh. Có giả thuyết cho rằng "Ảnh Thủ" không phải một người mà là một nhóm người thay phiên nhau đóng vai — điều này giải thích tại sao phong cách chỉ đạo qua Truyền Âm Phù đôi khi mâu thuẫn. Một bí mật động trời hơn là một số nội môn đệ tử cấp thấp cũng bí mật tham gia Liên Minh — những người này tuy thuộc nội môn nhưng bị kỳ thị vì xuất thân thấp kém hoặc linh căn tầm thường. Sự hiện diện của họ là tuyệt mật, vì nếu lộ ra sẽ chứng minh rằng bất mãn không chỉ giới hạn ở ngoại môn. Ngoài ra, Ảnh Thủ được cho là đã thu thập đủ bí mật nội bộ để gây thiệt hại nghiêm trọng cho ít nhất hai tông phái lớn nếu bị dồn vào đường cùng — nhưng đây là lá bài cuối cùng mà không ai muốn phải dùng.

## XI. Quan Hệ Thế Lực (势力关系)
Quan hệ của Liên Minh với các thế lực khác mang tính nghịch lý: thành viên Liên Minh chính là đệ tử của những tông phái mà Liên Minh đang bí mật hoạt động bên trong. Cửu Hoa Kiếm Tông là tông phái có nhiều thành viên Liên Minh nhất và cũng là nơi Liên Minh ra đời — nếu bị phát hiện, hậu quả sẽ nặng nề nhất tại đây. Vân Tông tuy ôn hòa hơn nhưng vẫn không thể chấp nhận một tổ chức bí mật hoạt động trong hàng ngũ đệ tử. Phiêu Bạt Khách Sạn Liên Minh vô tình cung cấp địa điểm họp cho Liên Minh thông qua các quán trọ vùng biên — chủ quán không biết khách hàng thực sự đang làm gì phía sau cánh cửa đóng kín. Về bản chất, Liên Minh tồn tại trong bóng tối của chính hệ thống mà nó ký sinh, và sự an toàn của nó phụ thuộc hoàn toàn vào khả năng giữ bí mật.
