---
type: faction
name: Tằm Ti Dệt Phường
hantu: 蚕丝织坊
faction_type: Thương Hội
alignment: 2
race: Tằm Tộc (Linh Thú)
region: Đông Hoang
founded: 200 năm trước
founder: Tằm Mẫu đời đầu
emblem: Tam_Ti_Det_Phuong.png
specialty: Dệt Linh Ti, May y phục phòng thủ, Kỹ thuật dệt truyền thống
economy:
- Bán Linh Ti (tơ tằm linh) ra Trạm Biên
- May y phục phòng thủ cấp thấp theo đặt hàng
- Trao đổi Lá Dâu Linh làm dược liệu an thần
arcs:
  - arc: 1
    status: Hoạt động ổn định
    rank: Hạng Năm
    leader: Tằm Mẫu Bạch Ti
    population: 135
    territory:
      - Rừng dâu tằm gần chân Hỏa Vân Sơn phía nam
    assets:
      - name: Rừng Dâu Linh
        type: Tài Nguyên
      - name: Phường Dệt
        type: Công Trình
      - name: Vạn Ti Mê Trận
        type: Trang Bị
      - name: Cuộn tơ ký ức Tằm Mẫu các đời
        type: Tài Nguyên
    stats: [20, 100, 50, 135, 80, 40]
    divisions:
      - name: Phường Dệt
        role: Sản xuất Linh Ti và may y phục phòng thủ, giao dịch với thương nhân bên ngoài
        headcount:
          hoi_truong: 1
          truong_lao: 0
          thuong_nhan: 5
          ho_ve: 0
          nhan_cong: 129
        members:
          - character: Bạch Ti
            position: Hội Trưởng (Tằm Mẫu)
            cultivation: Tương đương Trúc Cơ Hậu Kỳ
          - character: "[Thương Nhân Đối Tác 1]"
            position: Thương Nhân (Đại diện Trạm Biên)
            cultivation: Phàm Nhân
            placeholder: true
          - character: "[Thương Nhân Đối Tác 2]"
            position: Thương Nhân
            cultivation: Phàm Nhân
            placeholder: true
    relationships:
      - faction: Vạn Yêu Thành
        description: Linh Ti của Phường là mặt hàng được các thương nhân Vạn Yêu Thành ưa chuộng. Một số thương nhân thành thỉnh thoảng cử người đến rừng dâu đặt hàng trực tiếp. Quan hệ thương mại đơn thuần.
        diplomacy:
          lien_minh: 0
          tin: 10
          uy_hiep: 10
          thuong_mai: 50
          on_oan: 0
          le_thuoc: 10
      - faction: Hoang Dã Thợ Săn Bang
        description: Tằm Mẫu đời thứ 3 từng bị nhóm tán tu cướp bóc tơ tằm, và Thợ Săn Bang đã không can thiệp dù ở gần đó. Phường không thù hận nhưng không tin tưởng thợ săn.
        diplomacy:
          lien_minh: -5
          tin: -20
          uy_hiep: 20
          thuong_mai: 10
          on_oan: -10
          le_thuoc: 0
      - faction: Nham Thạch Tiểu Đội
        description: Nham Thạch Tiểu Đội đóng gần Hỏa Vân Sơn và đôi khi đi qua rừng dâu. Hai bên tôn trọng lãnh thổ của nhau, thỉnh thoảng Tằm Tộc dệt bao tay chịu nhiệt cho Tiểu Đội đổi lấy khoáng vật núi lửa.
        diplomacy:
          lien_minh: 10
          tin: 20
          uy_hiep: 0
          thuong_mai: 30
          on_oan: 0
          le_thuoc: 0
---

# Tằm Ti Dệt Phường (蚕丝织坊)

## I. Tổng Quan (总览)
Tằm Ti Dệt Phường là cộng đồng Tằm Tộc linh thú cư trú trong rừng dâu tằm gần chân Hỏa Vân Sơn phía nam, chuyên sản xuất Linh Ti — loại tơ tằm chứa linh khí, nhẹ nhưng cứng hơn thép thường, dùng may y phục phòng thủ cấp thấp được thương nhân khắp Đông Hoang săn đón. Đứng đầu là Tằm Mẫu đời thứ năm mang danh hiệu Bạch Ti — con tằm trắng bạc dài ba thước, tương đương Trúc Cơ Hậu Kỳ, có thể giao tiếp bằng cách rung sợi tơ tạo ra âm thanh phức tạp. Với một trăm ba mươi lăm cá thể bao gồm ba mươi tằm trưởng thành và hơn một trăm tằm non, Phường xếp Hạng Năm về quy mô nhưng sản phẩm Linh Ti khiến nhiều thế lực lớn hơn phải trả giá xứng đáng.

## II. Địa Lý & Tài Nguyên (地理与资源)
Rừng dâu tằm nằm ở chân phía nam Hỏa Vân Sơn, nơi đất đai màu mỡ nhờ tro núi lửa tích tụ hàng trăm năm và linh khí ôn hòa từ linh mạch nhỏ chạy qua bên dưới. Rừng dâu rậm rạp, tán lá che kín ánh sáng mặt trời, tơ tằm giăng khắp nơi tạo thành màn sương bạc lấp lánh khi ánh sáng lọt qua kẽ lá. Trung tâm rừng là "Phường Dệt" — khoảng trống tự nhiên rộng lớn nơi Tằm Tộc trưởng thành tập trung dệt vải. Tài nguyên chính gồm ba thứ: Linh Ti — tơ tằm chứa linh khí là sản phẩm thương mại chủ lực; Lá Dâu Linh — thức ăn chính của Tằm Tộc đồng thời là dược liệu cấp thấp có tính an thần; và kỹ thuật dệt tinh xảo được truyền từ Tằm Mẫu đời này sang đời khác qua cuộn tơ ký ức.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
"Một sợi tơ không chắc, vạn sợi tơ thành giáp." Triết lý này thấm vào bản chất Tằm Tộc — sinh vật yếu ớt đơn lẻ nhưng khi kết hợp lại tạo ra sản phẩm vượt xa khả năng cá nhân. Phường đề cao sự kiên nhẫn, tỉ mỉ, và công bằng trong giao dịch: Tằm Tộc chỉ dệt cho khách hàng trả giá xứng đáng, từ chối mọi đơn hàng vũ khí hay bẫy giết người, và bảo vệ rừng dâu bằng mọi giá vì đó là nguồn sống duy nhất. Phong tục thiêng liêng nhất là nghi thức truyền thừa: khi Tằm Mẫu sắp chết, bà sẽ nhả ra cuộn tơ cuối cùng chứa toàn bộ ký ức và kỹ thuật dệt tích lũy suốt đời, truyền lại cho Tằm Mẫu kế nhiệm. Nhờ vậy, mỗi đời Tằm Mẫu mới đều thừa kế trí tuệ của tất cả các đời trước.

## IV. Cơ Cấu Tổ Chức (组织结构)
Bạch Ti — Tằm Mẫu đời thứ năm — là trung tâm tuyệt đối của Phường. Hình dáng là con tằm trắng bạc dài ba thước, to hơn mọi Tằm Tộc khác gấp mười lần, có thể giao tiếp bằng rung sợi tơ tạo ra âm thanh mà tu sĩ và thương nhân nhân tộc hiểu được. Dưới Bạch Ti là ba mươi tằm trưởng thành tương đương Luyện Khí, chuyên nhả tơ và dệt. Hơn một trăm tằm non đang ăn lá dâu để phát triển, chưa có khả năng nhả tơ chất lượng. Năm thương nhân phàm nhân đóng vai trò đối tác, giúp bán Linh Ti ra Trạm Biên và các chợ bên ngoài, đổi lại cam kết bảo vệ rừng dâu khỏi kẻ xâm phạm. Cơ cấu đơn giản nhưng hiệu quả — Bạch Ti ra lệnh, tằm dệt, thương nhân bán.

## V. Công Pháp & Trận Pháp (功法与阵法)
Tằm Tộc không có công pháp chiến đấu theo nghĩa thông thường. Chúng tiến hóa qua quá trình ăn Lá Dâu Linh và nhả tơ — mỗi lần lột xác là một lần nâng cấp, tơ nhả ra sau mỗi lần lột xác mạnh hơn và chứa nhiều linh khí hơn. Bạch Ti đã lột xác năm lần, đạt cảnh giới tương đương Trúc Cơ Hậu Kỳ. Phòng thủ chính là "Vạn Ti Mê Trận" — mạng tơ giăng khắp rừng dâu, mỗi sợi tơ mảnh hơn tóc nhưng cứng hơn dây thép, gần như vô hình trong ánh sáng mờ. Kẻ xâm nhập sẽ bị dính tơ, và càng vùng vẫy càng bị quấn chặt — giống như côn trùng sa lưới nhện nhưng ở quy mô tu sĩ. Vạn Ti Mê Trận đủ sức giữ chân Trúc Cơ Trung Kỳ trong thời gian đáng kể.

## VI. Đặc Sản Môn Phái (门派特产)
- **Linh Ti:** Tơ tằm chứa linh khí, nhẹ như lông vũ nhưng cứng hơn thép thường, chống được đòn đánh cấp Luyện Khí. Nguyên liệu chính để may y phục phòng thủ cấp thấp, được thương nhân khắp Đông Hoang săn đón.
- **Y Phục Linh Ti:** Áo dài dệt từ Linh Ti tinh chế, nhẹ nhàng, thoáng mát, có khả năng phòng thủ chống đòn đánh vật lý cấp Luyện Khí đến Trúc Cơ Sơ Kỳ. Mỗi bộ cần một tằm trưởng thành nhả tơ liên tục mười ngày.
- **Lá Dâu Linh:** Dược liệu cấp thấp có tính an thần, giúp ổn định tâm trí khi tu luyện. Sản phẩm phụ từ rừng dâu, giá rẻ nhưng cung ổn định.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Phường Dệt:** Khoảng trống tự nhiên giữa rừng dâu nơi tằm trưởng thành tập trung nhả tơ và dệt vải. Được che phủ bởi tán lá và tơ tằm, tạo không gian ấm áp, ẩm ướt lý tưởng cho công việc.
- **Vạn Ti Mê Trận:** Mạng lưới tơ phòng thủ bao phủ toàn bộ rừng dâu, được Tằm Tộc bổ sung và sửa chữa hàng ngày. Vừa là hệ thống phòng thủ vừa là hệ thống cảnh báo — Bạch Ti cảm nhận mọi rung động trên mạng tơ.
- **Khu Ấp Trứng:** Vùng sâu nhất rừng dâu nơi tằm non được bảo vệ nghiêm ngặt nhất, nhiệt độ và độ ẩm ổn định nhờ tán lá dày đặc.
- **Điểm Giao Dịch:** Rìa rừng nơi thương nhân đối tác đến nhận Linh Ti và giao vật phẩm trao đổi. Tằm Tộc không bao giờ ra khỏi rừng.

## VIII. Kinh Tế (经济)
Kinh tế Phường dựa hoàn toàn vào sản xuất và bán Linh Ti. Ba mươi tằm trưởng thành nhả tơ liên tục, sản lượng đủ cung cấp cho nhu cầu thường xuyên từ Trạm Biên và các thương nhân vãng lai. Năm thương nhân phàm nhân đối tác đảm nhận khâu vận chuyển và phân phối, giữ lại hai mươi phần trăm doanh thu làm phí. Ngoài Linh Ti thô, Phường cũng nhận đặt hàng may y phục phòng thủ với giá cao hơn nhiều — nhưng năng lực sản xuất hạn chế nên mỗi tháng chỉ nhận tối đa hai đơn. Lá Dâu Linh là sản phẩm phụ giá rẻ nhưng lượng lớn, bán cho thương nhân dược liệu. Thu nhập đủ để Phường mua những thứ Tằm Tộc không tự sản xuất được: pháp khí phòng thân cho thương nhân đối tác và nguyên liệu gia cố Vạn Ti Mê Trận.

## IX. Lịch Sử Tóm Tắt (简史)
Hơn hai trăm năm trước, rừng dâu tằm hình thành tự nhiên nhờ tro Hỏa Vân Sơn bón đất và linh khí ôn hòa từ linh mạch bên dưới. Tằm Tộc tìm đến cư trú khi phát hiện Lá Dâu Linh — thức ăn lý tưởng cho quá trình tiến hóa. Tằm Mẫu đời đầu tiên khai sáng kỹ thuật dệt Linh Ti và thiết lập truyền thống truyền thừa qua cuộn tơ ký ức. Bi kịch lớn nhất xảy ra khi Tằm Mẫu đời thứ ba bị nhóm tán tu xâm nhập cướp bóc tơ tằm — bà hy sinh bản thân, kích hoạt Vạn Ti Mê Trận ở mức tối đa để bảo vệ đàn, tiêu diệt kẻ xâm nhập nhưng cũng cạn kiệt sinh lực. Từ đó, Phường thiết lập quan hệ thương mại ổn định với Trạm Biên thông qua năm thương nhân đối tác, biến Linh Ti từ mục tiêu cướp bóc thành mặt hàng được bảo vệ bởi lợi ích chung.

## X. Giai Thoại & Bí Mật (轶事与秘密)
Cuộn tơ ký ức của Tằm Mẫu đời đầu tiên vẫn còn, giấu sâu trong rừng tại vị trí chỉ Bạch Ti biết. Cuộn tơ này chứa thông tin về thời điểm Hỏa Vân Sơn còn là núi lửa chết, trước khi linh khí hồi phục — kiến thức địa chất cổ đại mà không ai khác nắm giữ. Bí mật quan trọng hơn nằm ở dự án nghiên cứu bí mật của Bạch Ti: "Kén Hộ Thể" — loại kén đặc biệt dệt từ Linh Ti tinh chế nhất, có thể bao bọc tu sĩ nhân tộc bên trong khi họ đột phá cảnh giới, ngăn chặn hiện tượng phản phệ linh khí gây chết người. Nếu thành công, sản phẩm này sẽ khiến mọi tu sĩ trên thế giới muốn làm khách hàng của Phường — nhưng cũng có thể khiến Phường trở thành mục tiêu cướp bóc lớn hơn bao giờ hết.

## XI. Quan Hệ Thế Lực (势力关系)
- **Vạn Yêu Thành:** Linh Ti là mặt hàng được thương nhân thành ưa chuộng, một số cử người đến rừng dâu đặt hàng trực tiếp. Quan hệ thương mại đơn thuần nhưng ổn định, mang lại sự bảo vệ gián tiếp cho Phường.
- **Hoang Dã Thợ Săn Bang:** Phường không tin tưởng thợ săn bang vì họ đã không can thiệp khi Tằm Mẫu đời ba bị cướp bóc. Quan hệ lạnh nhạt, chỉ giao dịch khi cần thiết.
- **Nham Thạch Tiểu Đội:** Láng giềng tốt ở chân Hỏa Vân Sơn. Hai bên tôn trọng lãnh thổ, thỉnh thoảng Tằm Tộc dệt bao tay chịu nhiệt cho Tiểu Đội đổi lấy khoáng vật núi lửa bón rừng dâu.
