---
type: faction
name: Ký Sinh Liên Minh
hantu: 寄生联盟
faction_type: Liên Minh
alignment: -5
race: Vi Tộc (Ký Sinh Thể)
region: Tây Mạc
founded: Không rõ (hình thành tự nhiên khi ký sinh thể phát triển linh trí)
founder: Không có (tự phát)
emblem: Mang_Luoi_Te_Bao.png
specialty: Ám Thị Vi Tế, Ký sinh vô hình, Mạng lưới tình báo sinh học
economy:
- Không có kinh tế — tồn tại bằng cách ký sinh trong cơ thể vật chủ
- Tài sản thực sự là thông tin bí mật thu thập từ mọi vật chủ
- Trao đổi thông tin giữa các thành viên qua Mạch Ngầm
arcs:
  - arc: 1
    status: Mở rộng âm thầm — phát triển khả năng nhảy vật chủ
    rank: Không Xếp Hạng
    leader: Không có thủ lĩnh (phi tập trung)
    population: 7
    territory:
      - Huyết Uyên và Mạch Ngầm (hành lang liên lạc)
      - Bên trong cơ thể các vật chủ (phân bố rải rác)
    assets:
      - name: Mạng Lưới Tình Báo Sinh Học
        type: Mạng Lưới
      - name: Bí mật về Huyết Trì
        type: Tình Báo
    stats: [5, 5, 5, 7, 5, 30]
    divisions:
      - name: Ký Sinh Trưởng
        role: Bảy cá thể lâu đời nhất, mỗi cá thể ký sinh trong một vật chủ quan trọng, thu thập và chia sẻ thông tin
        headcount:
          minh_chu: 0
          pho_minh_chu: 0
          truong_lao: 7
          su_gia: 0
          thanh_vien_phai: 0
        members:
          - character: "[Ký Sinh Trưởng Nhất]"
            position: Ký Sinh Trưởng — Ký sinh trong cường giả Kim Đan
            cultivation: Luyện Khí Hậu Kỳ (tương đương)
            placeholder: true
          - character: "[Ký Sinh Trưởng Nhị]"
            position: Ký Sinh Trưởng — Ký sinh trong đệ tử Vạn Độc Môn
            cultivation: Luyện Khí Trung Kỳ (tương đương)
            placeholder: true
    relationships:
      - faction: Vạn Độc Môn
        description: Ký sinh trong đệ tử Vạn Độc Môn và tiếp cận bí mật nội bộ, nhưng Vạn Độc Môn hoàn toàn không biết sự tồn tại của Liên Minh dù là tổ chức am hiểu sinh vật nhất.
        diplomacy:
          lien_minh: 0
          tin: 0
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 0
      - faction: Sa Trùng Vi Tộc
        description: Cùng là Vi Tộc nhưng phương thức tồn tại khác biệt — Sa Trùng sống tự do trong cát, Ký Sinh sống bên trong sinh vật khác. Hai bên biết về nhau qua Mạch Ngầm nhưng hiếm khi tương tác.
        diplomacy:
          lien_minh: 10
          tin: 20
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 0
      - faction: Linh Sa Khuẩn Đoàn
        description: Cùng sử dụng Mạch Ngầm làm hành lang liên lạc, đôi khi tranh giành không gian trong mạch ẩm ướt. Quan hệ cạnh tranh nhẹ nhưng không thù địch.
        diplomacy:
          lien_minh: 5
          tin: 15
          uy_hiep: 0
          thuong_mai: 0
          on_oan: -10
          le_thuoc: 0
---

# Ký Sinh Liên Minh (寄生联盟)

## I. Tổng Quan (总览)
Ký Sinh Liên Minh là một mạng lưới phi tập trung gồm các Vi Tộc ký sinh đã phát triển linh trí, tồn tại bên trong cơ thể sinh vật khác mà vật chủ hoàn toàn không hay biết. Không có thủ lĩnh duy nhất, không có trụ sở cố định, không có quân đội — Liên Minh vận hành như một hệ thần kinh phân tán, trong đó bảy Ký Sinh Trưởng lâu đời nhất đóng vai trò nút giao thông tin. Mỗi Ký Sinh Trưởng ký sinh trong cơ thể một vật chủ quan trọng, tiếp cận mọi bí mật của người đó mà không để lại dấu vết. Triết lý cốt lõi là "Sống trong kẻ khác, biết hơn chính họ" — họ coi ký sinh là hình thức cộng sinh bất đối xứng, có lợi cho cả hai bên dù vật chủ không biết. Về sức chiến đấu, Liên Minh gần như bằng không, nhưng về thông tin tình báo, chúng có tiềm năng trở thành mạng lưới đáng sợ nhất Tây Mạc.

## II. Địa Lý & Tài Nguyên (地理与资源)
Ký Sinh Liên Minh không có lãnh thổ theo nghĩa truyền thống. Thành viên tồn tại bên trong cơ thể sinh vật khác — yêu thú, trùng tộc, thậm chí cả tu sĩ Nhân Tộc — phân bố rải rác khắp nơi. Huyết Uyên và Mạch Ngầm ẩm thấp đóng vai trò "hành lang liên lạc" chính, nơi Vi Tộc ký sinh rời khỏi vật chủ tạm thời để trao đổi thông tin qua tín hiệu sinh hóa. Tài nguyên lớn nhất của Liên Minh không phải vật chất mà là thông tin bí mật — ký sinh trong cơ thể sinh vật khác cho phép tiếp cận mọi trải nghiệm, cảm xúc, và quyết định của vật chủ. Mạng lưới phân bố rộng khắp nhưng mật độ thấp, và khả năng thao túng nhẹ lên cảm xúc vật chủ — tạo ra bất an, hưng phấn, hoặc buồn ngủ — là công cụ vi tế nhưng hiệu quả.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
Liên Minh theo triết lý cộng sinh bất đối xứng: tin rằng ký sinh có lợi cho cả hai bên, vì ký sinh thể giúp cân bằng hệ sinh học nội tại của vật chủ, dù vật chủ không bao giờ biết điều đó. Quy tắc tối cao là không bao giờ giết vật chủ — vật chủ chết thì ký sinh cũng vong, và đây là giới hạn không thể vượt qua. Mỗi cá thể không được ký sinh đồng thời quá ba vật chủ để tránh phân tán linh trí. Mọi thông tin phải chia sẻ qua Mạch Ngầm, không qua vật chủ, để tránh bị phát hiện. Khi hai thành viên gặp nhau trong Mạch Ngầm, họ thực hiện "Lễ Dung Hợp" — trao đổi một phần tế bào để cập nhật thông tin và DNA, một nghi thức vừa mang tính sinh học vừa mang tính xã hội.

## IV. Cơ Cấu Tổ Chức (组织结构)
Liên Minh không có cấu trúc phân cấp truyền thống mà vận hành như mạng lưới phi tập trung — mỗi cá thể tự quyết định hành động, chia sẻ thông tin tự nguyện. Bảy Ký Sinh Trưởng là các cá thể lâu đời nhất, tương đương Luyện Khí, mỗi cá thể ký sinh trong một vật chủ quan trọng — có kẻ trong cơ thể đệ tử tông môn, có kẻ trong cơ thể yêu thú cấp cao, và đáng sợ nhất là một Ký Sinh Trưởng đang ký sinh trong cơ thể một cường giả Kim Đan mà vật chủ hoàn toàn không biết. Dưới bảy Ký Sinh Trưởng là hàng trăm ký sinh thường — vi thể rải rác, đa số không có linh trí, chỉ tồn tại theo bản năng. Ngoài ra còn có số lượng không xác định ký sinh ngầm mà ngay cả Liên Minh cũng không nắm được — những vi thể đã mất liên lạc hoặc chưa bao giờ gia nhập mạng lưới.

## V. Công Pháp & Trận Pháp (功法与阵法)
Ký Sinh Liên Minh không có công pháp hay trận pháp. Chiến lực trong chiến đấu trực tiếp gần như bằng không — nếu bị phát hiện và tách khỏi vật chủ, ký sinh thể gần như không có cách tự vệ. Năng lực đặc biệt duy nhất là "Ám Thị Vi Tế" — khả năng ảnh hưởng nhẹ lên hệ thần kinh vật chủ, tạo ra cảm giác bất an, hưng phấn, hoặc buồn ngủ. Ám Thị Vi Tế không đủ mạnh để kiểm soát hoàn toàn ý chí vật chủ, chỉ có thể đẩy nhẹ quyết định theo hướng có lợi cho ký sinh thể. Tuy nhiên, qua hàng chục năm tích lũy, những "cú đẩy nhẹ" này có thể ảnh hưởng sâu sắc đến cuộc đời và quyết định của vật chủ mà không ai ngờ tới.

## VI. Đặc Sản Môn Phái (门派特产)
- **Ám Thị Vi Tế:** Khả năng thao túng cảm xúc vật chủ ở mức vi tế — không phải pháp bảo hay đan dược mà là năng lực bẩm sinh, có tiềm năng trở thành vũ khí tình báo đáng sợ nhất nếu được hoàn thiện.
- **Lễ Dung Hợp:** Nghi thức trao đổi tế bào và thông tin giữa các thành viên, cho phép cập nhật DNA và kiến thức tập thể, là cách Liên Minh tiến hóa mà không cần sinh sản thông thường.
- **Tình Báo Nội Tại:** Mỗi Ký Sinh Trưởng mang theo hàng chục năm ký ức của vật chủ — mưu đồ, bí mật, điểm yếu — thông tin vô giá mà không mạng lưới gián điệp nào có thể thu thập được bằng phương pháp thông thường.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Mạch Ngầm Ẩm Ướt:** Hành lang liên lạc chính, nơi ký sinh thể tạm thời rời vật chủ để trao đổi thông tin và thực hiện Lễ Dung Hợp. Phân bố rải rác dọc theo các mạch nước ngầm.
- **Huyết Uyên:** Vùng nước đặc biệt giàu dưỡng chất, nơi ký sinh thể non được sinh ra và nuôi dưỡng trước khi tìm vật chủ đầu tiên.
- **Nút Thông Tin:** Các điểm hẹn cố định trong Mạch Ngầm nơi Ký Sinh Trưởng để lại tín hiệu sinh hóa, cho phép trao đổi thông tin không đồng bộ.

## VIII. Kinh Tế (经济)
Ký Sinh Liên Minh không có kinh tế — chúng không sản xuất, không mua bán, không tích lũy tài sản vật chất. Sự tồn tại hoàn toàn dựa vào vật chủ: ký sinh thể hấp thu một lượng nhỏ dinh dưỡng từ cơ thể vật chủ, ít đến mức không gây ảnh hưởng sức khỏe. "Đồng tiền" duy nhất trong Liên Minh là thông tin — ai sở hữu bí mật lớn hơn thì có tiếng nói nặng hơn trong mạng lưới. Xét ở góc độ khác, Liên Minh là thế lực "giàu nhất" Tây Mạc về mặt tình báo: chúng nắm giữ bí mật của vô số cá thể mạnh, nhưng không có cách biến thông tin thành sức mạnh vật lý.

## IX. Lịch Sử Tóm Tắt (简史)
Ký Sinh Liên Minh hình thành tự nhiên khi các Vi Tộc ký sinh bắt đầu phát triển linh trí và nhận ra lợi ích của việc chia sẻ thông tin qua Mạch Ngầm. Không có thời điểm sáng lập cụ thể, không có người sáng lập — Liên Minh lớn lên từ bản năng sinh tồn tập thể. Chúng tồn tại âm thầm hàng trăm năm mà không ai biết, kể cả Vạn Độc Môn — tổ chức am hiểu sinh vật nhất — cũng không ngờ rằng bên trong cơ thể đệ tử của mình có một vi thể đang ghi nhớ mọi bí mật. Gần đây, một Ký Sinh Trưởng ký sinh trong đệ tử Vạn Độc Môn đã phát hiện thông tin quan trọng về Huyết Trì — bí mật đang được lan truyền chậm rãi qua mạng lưới, và nếu Liên Minh quyết định hành động dựa trên thông tin này, hậu quả có thể rất lớn.

## X. Giai Thoại & Bí Mật (轶事与秘密)
Một trong bảy Ký Sinh Trưởng đang ký sinh trong cơ thể một cường giả Kim Đan, đã chứng kiến hàng chục năm mưu đồ và toan tính của vị cường giả này mà không để lộ bất kỳ dấu hiệu nào. Vật chủ Kim Đan hoàn toàn không biết rằng mỗi suy nghĩ thầm kín nhất, mỗi âm mưu bí mật nhất đều có một vi thể đang lặng lẽ ghi nhớ. Đáng lo ngại hơn, Liên Minh đang dần phát triển khả năng "nhảy vật chủ" — chuyển từ sinh vật này sang sinh vật khác mà không cần quay về Mạch Ngầm. Nếu hoàn thiện kỹ thuật này, Ký Sinh Liên Minh sẽ trở thành mạng lưới tình báo đáng sợ nhất thế giới tu luyện — có mặt ở khắp nơi, biết mọi bí mật, nhưng yếu nhất về sức mạnh chiến đấu, tạo ra một nghịch lý đáng sợ.

## XI. Quan Hệ Thế Lực (势力关系)
- **Vạn Độc Môn:** Quan hệ một chiều ký sinh. Liên Minh có thành viên ký sinh trong đệ tử Vạn Độc Môn và đang thu thập bí mật nội bộ, bao gồm thông tin về Huyết Trì. Vạn Độc Môn — tổ chức am hiểu sinh vật nhất — hoàn toàn không biết sự tồn tại của Liên Minh.
- **Sa Trùng Vi Tộc:** Đồng loại Vi Tộc nhưng phương thức tồn tại khác biệt. Hai bên biết về nhau qua Mạch Ngầm, thỉnh thoảng trao đổi tín hiệu, nhưng hiếm khi hợp tác trực tiếp vì mục tiêu sinh tồn khác nhau.
- **Linh Sa Khuẩn Đoàn:** Cùng sử dụng Mạch Ngầm ẩm ướt làm hành lang di chuyển, đôi khi tranh giành không gian sống trong các mạch nước hẹp. Quan hệ cạnh tranh nhẹ nhưng không thù địch, vì cả hai đều quá nhỏ bé để đe dọa lẫn nhau.
