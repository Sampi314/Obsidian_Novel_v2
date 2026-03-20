---
type: faction
name: Thiên Lý Truyền Thư Các
hantu: 千里传书阁
faction_type: Hội
alignment: 3
race: Nhân Tộc
region: Đông Hoang
founded: 40 năm trước
founder: Lý Phong Thư
emblem: Thien_Ly_Truyen_Thu_Cac.png
specialty: Truyền tin viễn cự, Thuần hóa Sa Ưng, Mạng lưới bưu tín
economy:
  - Phí gửi thư (thường, mật, gấp)
  - Vận chuyển gói nhỏ và vật phẩm
  - Dịch vụ truyền tin đặc biệt
arcs:
  - arc: 1
    status: Hoạt động (Mạng lưới truyền tin phát triển)
    rank: Hạng Năm
    leader: Các Chủ Lý Phong Thư
    population: 56
    territory:
      - Trụ sở chính tại Đông Hoang
      - 6 trạm trung chuyển rải rác
    assets:
      - name: Đội Sa Ưng Thuần Hóa (20 con)
        type: Linh Thú
      - name: Hệ Thống Trạm Trung Chuyển
        type: Công Trình
      - name: Bản Đồ Quan Hệ Ngầm
        type: Tình Báo
    stats: [15, 30, 80, 56, 20, 120]
    divisions:
      - name: Truyền Thư Viện
        role: Quản lý mạng lưới truyền tin, huấn luyện Sa Ưng và tín sứ
        headcount:
          hoi_truong: 1
          pho_hoi_truong: 0
          thanh_vien: 36
          tong_quan: 19
        members:
          - character: Lý Phong Thư
            position: Các Chủ
            cultivation: Trúc Cơ Trung Kỳ
          - character: Trần Phi Tín
            position: Truyền Thư Sứ
            cultivation: Trúc Cơ Sơ Kỳ
          - character: Phạm Tiểu Nhạn
            position: Đưa Thư Viên
            cultivation: Luyện Khí Hậu Kỳ
    relationships:
      - faction: Thiên Sa Thương Hội
        description: Khách hàng lớn nhất, sử dụng dịch vụ truyền tin thường xuyên để điều phối thương đoàn.
        diplomacy:
          lien_minh: 20
          tin: 40
          uy_hiep: 0
          thuong_mai: 70
          on_oan: 5
          le_thuoc: 20
      - faction: Vạn Yêu Thành
        description: Giao dịch trung lập, Truyền Thư Các chuyển thư cho tất cả bên không phân biệt, kể cả thế lực ngầm.
        diplomacy:
          lien_minh: 0
          tin: 20
          uy_hiep: 10
          thuong_mai: 30
          on_oan: 0
          le_thuoc: 0
      - faction: Cửu Hoa Kiếm Tông
        description: Đôi khi sử dụng dịch vụ cho các nhiệm vụ không quan trọng, nhưng Cửu Hoa có hệ thống truyền tin riêng nên không phụ thuộc.
        diplomacy:
          lien_minh: 5
          tin: 20
          uy_hiep: 0
          thuong_mai: 15
          on_oan: 0
          le_thuoc: 0
---

# Thiên Lý Truyền Thư Các (千里传书阁)

## I. Tổng Quan (总览)

Thiên Lý Truyền Thư Các là mạng lưới bưu tín tán tu lớn nhất khu vực Đông Hoang, chuyên cung cấp dịch vụ truyền tin viễn cự bằng Sa Ưng thuần hóa và tín sứ chạy bộ. Với khoảng 56 thành viên (gồm 30 tín sứ và 26 nhân viên hậu cần) cùng 20 Sa Ưng thuần hóa, Truyền Thư Các bao phủ phần lớn lãnh thổ Đông Hoang, trừ những vùng hiểm địa như Tử Vong Chi Thung Lũng. Dù tu vi thành viên chỉ ở mức Luyện Khí đến Trúc Cơ, tổ chức này nắm giữ sức mạnh đặc biệt: thông tin. Lý Phong Thư — Các Chủ — am hiểu luồng thư từ của mọi thế lực, biến mạng lưới bưu tín thành công cụ tình báo vô giá mà không ai ngờ tới.

## II. Địa Lý & Tài Nguyên (地理与资源)

Trụ sở chính đặt tại một điểm giao thoa chiến lược trong Đông Hoang, nơi các tuyến đường thương mại và lộ trình di chuyển giao nhau. Từ đây, 6 trạm trung chuyển tỏa ra các hướng, mỗi trạm do một Trạm Trưởng Luyện Khí Hậu Kỳ phụ trách. Tài nguyên quan trọng nhất là đội Sa Ưng thuần hóa — loài ưng lớn có khả năng bay đường dài xuyên gió mạnh mà không mệt mỏi. Ngoài ra, Truyền Thư Các sở hữu bùa truyền tin cấp thấp, mực linh viết thư mật (chỉ hiện chữ khi đốt nóng), và hệ thống mã hóa riêng cho thư bí mật.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)

Triết lý "Một lá thư có thể cứu mạng — hoặc giết người" được khắc sâu vào tâm trí mỗi thành viên, nhấn mạnh trọng trách của nghề truyền tin. Quy tắc tối thượng là bảo mật: không bao giờ đọc thư của khách, không tiết lộ danh tính người gửi hay người nhận, và vi phạm bí mật thư tín là tội nặng nhất — kẻ vi phạm bị trục xuất vĩnh viễn và bôi đen danh tiếng trong giới tán tu. Phong tục đặc biệt nhất là tang lễ Sa Ưng: mỗi con ưng khi chết được chôn cất trang trọng với một lá thư trắng trong mỏ, tượng trưng cho sứ mệnh cuối cùng chưa hoàn thành, thể hiện lòng kính trọng đối với những đối tác phi nhân trung thành.

## IV. Cơ Cấu Tổ Chức (组织结构)

Các Chủ Lý Phong Thư — tán tu thuần hóa Sa Ưng — là người sáng lập và điều hành toàn bộ mạng lưới. Bên dưới có 6 Trạm Trưởng (Luyện Khí Hậu Kỳ), mỗi người phụ trách một trạm trung chuyển và tuyến đường trong khu vực. 30 Tín Sứ (Luyện Khí) chuyên vận chuyển thư từ và gói nhỏ mà Sa Ưng không thể mang, trong đó nổi bật có Trần Phi Tín — truyền thư sứ nhanh nhẹn có thể chạy suốt ba ngày không nghỉ. Phạm Tiểu Nhạn — thiếu nữ 14 tuổi đang học thuần hóa Sa Ưng — đại diện cho thế hệ kế tiếp của Truyền Thư Các.

## V. Công Pháp & Trận Pháp (功法与阵法)

Công pháp đặc trưng là "Thuần Ưng Thuật" — kỹ thuật thuần hóa và huấn luyện Sa Ưng mang thư xuyên gió mạnh và thời tiết xấu. Đây không phải công pháp tu luyện mạnh mà là kỹ năng chuyên môn, đòi hỏi sự kiên nhẫn và khả năng cảm ứng tâm linh với chim ưng. Ngoài ra, Truyền Thư Các sử dụng bùa truyền tin sơ đẳng — chỉ truyền được vài chữ ngắn trong phạm vi hẹp — và bùa hộ mệnh nhỏ gắn trên Sa Ưng để giúp chúng bay qua vùng thời tiết khắc nghiệt. Không có trận pháp phòng thủ đáng kể.

## VI. Đặc Sản Môn Phái (门派特产)

Sản phẩm chính là dịch vụ truyền tin với ba cấp: thư thường (rẻ, giao trong 3-7 ngày), thư mật (đắt hơn, viết bằng mực linh chỉ hiện khi đốt nóng), và thư gấp (đắt nhất, dùng Sa Ưng nhanh nhất bay trực tiếp). Ngoài ra, Truyền Thư Các cung cấp dịch vụ vận chuyển gói nhỏ cho vật phẩm quý giá mà khách không muốn tự mang. Sản phẩm "ngầm" quý giá nhất chính là Bản Đồ Quan Hệ Ngầm — tập hợp dữ liệu về tần suất và hướng gửi thư của mỗi thế lực, cho phép suy luận mối quan hệ ngoại giao thực sự giữa các bên.

## VII. Cơ Sở Hạ Tầng (基础设施)

Trụ sở chính là một tòa các nhỏ hai tầng, tầng dưới dùng làm phòng tiếp khách và kho thư, tầng trên là nơi nuôi dưỡng và huấn luyện Sa Ưng với sàn trải cát và giá đậu bằng gỗ cứng. 6 trạm trung chuyển mỗi trạm gồm một túp lều kiên cố, chuồng ưng nhỏ và kho dự trữ thức ăn cho ưng. Hệ thống không có phòng thủ quân sự vì Truyền Thư Các dựa vào danh tiếng trung lập để bảo đảm an toàn — tấn công truyền thư sứ đồng nghĩa với việc mất khả năng liên lạc, điều không ai muốn.

## VIII. Kinh Tế (经济)

Nguồn thu chính là phí gửi thư — hệ thống giá linh hoạt dựa trên loại thư, khoảng cách và độ khẩn cấp. Thư thường rẻ đến mức ngay cả tán tu nghèo cũng đủ khả năng, trong khi thư mật và thư gấp mang lại lợi nhuận cao. Dịch vụ vận chuyển gói nhỏ là nguồn thu phụ nhưng đang tăng trưởng. Khách hàng bao gồm thương nhân, tán tu, tông môn nhỏ và đôi khi cả thế lực ngầm — Truyền Thư Các phục vụ tất cả không phân biệt, miễn trả đủ phí. Kinh tế ổn định vì nhu cầu liên lạc luôn tồn tại bất kể thời bình hay loạn.

## IX. Lịch Sử Tóm Tắt (简史)

Lý Phong Thư từng là tín sứ cho một tông môn, nhưng bị sa thải vì chậm trễ giao thư. Biến cố đó khiến ông nhận ra rằng thông tin liên lạc là thứ xa xỉ nhất trong thế giới tu luyện — các tông phái lớn có hệ thống truyền tin riêng, nhưng tán tu, thương nhân và tông môn nhỏ phải dựa vào may rủi. Ông bắt đầu thuần hóa Sa Ưng hoang dã, xây dựng mạng lưới từ một con ưng và một trạm, dần dần mở rộng thành hệ thống bưu tín tán tu duy nhất tại Đông Hoang. 40 năm sau, dù tu vi vẫn chỉ ở Trúc Cơ Trung Kỳ, Lý Phong Thư nắm trong tay mạng lưới thông tin mà nhiều thế lực mạnh hơn phải phụ thuộc.

## X. Giai Thoại & Bí Mật (轶事与秘密)

Lý Phong Thư mang trong mình một tội lỗi không thể gột rửa: ông từng vô tình chuyển một lá thư mật cho một bang phái tà đạo mà không biết nội dung — sau đó một thương đoàn bị phục kích, thiệt mạng nhiều người. Sự kiện đó ám ảnh ông đến tận bây giờ, và là lý do ông luôn đấu tranh nội tâm giữa nguyên tắc "không đọc thư khách" và trách nhiệm đạo đức.

Có một con Sa Ưng già nhất tên "Cổ Phong" — nó từng bay đến tận rìa Vĩnh Tịch Chi Địa rồi quay về, nhưng từ đó không chịu bay nữa, chỉ đậu trên giá im lặng nhìn ra xa. Không ai biết nó thấy gì ở ngoài đó, và Lý Phong Thư không dám ép nó bay lại.

Bí mật lớn nhất: Các Chủ lén ghi chép lại tần suất và hướng gửi thư của mỗi thế lực trong 40 năm qua, tạo thành bản đồ quan hệ ngầm cực kỳ chi tiết. Nếu bản đồ này bị lộ, Truyền Thư Các sẽ mất toàn bộ lòng tin và sụp đổ, nhưng nếu sử dụng đúng cách, nó có giá trị tình báo vượt xa bất kỳ pháp bảo nào.

## XI. Quan Hệ Thế Lực (势力关系)

- **Thiên Sa Thương Hội:** Khách hàng lớn nhất và bảo trợ ngầm, phụ thuộc vào Truyền Thư Các để điều phối thương đoàn xuyên Đông Hoang. Mối quan hệ lợi ích hai chiều bền vững.
- **Vạn Yêu Thành:** Giao dịch trung lập — Truyền Thư Các chuyển thư cho tất cả bên không phân biệt, kể cả thế lực ngầm trong Vạn Yêu Thành. Đây là nguồn thu đáng kể nhưng cũng là rủi ro đạo đức lớn nhất.
- **Cửu Hoa Kiếm Tông:** Đôi khi sử dụng dịch vụ cho các nhiệm vụ không mật, nhưng Cửu Hoa có truyền âm trận riêng nên không phụ thuộc. Quan hệ nhạt nhẽo, đơn thuần thương mại.
