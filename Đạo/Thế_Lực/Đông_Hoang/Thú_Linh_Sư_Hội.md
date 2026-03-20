---
type: faction
name: Thú Linh Sư Hội
hantu: 兽灵师会
faction_type: Hội
alignment: 7
race: Nhân Tộc
region: Đông Hoang
founded: 60 năm trước
founder: Thú Ngữ Ông
emblem: Thu_Linh_Su_Hoi.png
specialty: Kết giao linh thú, Giao tiếp tâm linh với động vật, Sinh tồn trong rừng
economy:
  - Dịch vụ tìm kiếm và kết giao linh thú cho tu sĩ
  - Bán dược thảo và vật liệu thú thu thập từ rừng
  - Hướng dẫn sinh tồn rừng rậm
arcs:
  - arc: 1
    status: Ổn định (Ẩn dật trong rừng)
    rank: Hạng Năm
    leader: Hội Trưởng Thú Ngữ Ông
    population: 80
    territory:
      - Rừng rậm phía đông Đông Hoang
      - Khu vực linh thú cấp thấp sinh sống
    assets:
      - name: Linh Thú Đồng Hành (200+ con)
        type: Linh Thú
      - name: Kiến Thức Về Linh Thú
        type: Tri Thức
      - name: Khu Rừng Trú Ẩn
        type: Địa Lợi
    stats: [60, 40, 50, 80, 30, 35]
    divisions:
      - name: Linh Sư Đường
        role: Nghiên cứu, kết giao và chăm sóc linh thú đồng hành
        headcount:
          hoi_truong: 1
          pho_hoi_truong: 3
          thanh_vien: 70
          tong_quan: 6
        members:
          - character: Thú Ngữ Ông
            position: Hội Trưởng
            cultivation: Trúc Cơ Viên Mãn
          - character: "[Trưởng Lão Phi Cầm]"
            position: Trưởng Lão
            cultivation: Trúc Cơ Hậu Kỳ
            placeholder: true
          - character: "[Trưởng Lão Tẩu Thú]"
            position: Trưởng Lão
            cultivation: Trúc Cơ Trung Kỳ
            placeholder: true
          - character: "[Trưởng Lão Thủy Sinh]"
            position: Trưởng Lão
            cultivation: Trúc Cơ Trung Kỳ
            placeholder: true
    relationships:
      - faction: Bách Thú Sơn Trang
        description: Khác biệt triết lý cơ bản — Sơn Trang dùng khế ước cưỡng chế, Hội dùng lòng chân thành. Quan hệ căng thẳng.
        diplomacy:
          lien_minh: -20
          tin: 10
          uy_hiep: 30
          thuong_mai: 10
          on_oan: -40
          le_thuoc: 0
      - faction: Thiên Yêu Đình
        description: Thiên Yêu Đình biết Hội tồn tại nhưng không quan tâm vì quá nhỏ. Hội cẩn thận không xâm phạm lãnh thổ yêu tộc.
        diplomacy:
          lien_minh: 0
          tin: 10
          uy_hiep: 20
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 5
      - faction: Hoang Dã Thợ Săn Bang
        description: Mâu thuẫn tự nhiên — Thợ Săn Bang săn linh thú, Hội bảo vệ linh thú. Đôi khi xảy ra xung đột nhỏ.
        diplomacy:
          lien_minh: -30
          tin: -20
          uy_hiep: 15
          thuong_mai: -10
          on_oan: -25
          le_thuoc: 0
---

# Thú Linh Sư Hội (兽灵师会)

## I. Tổng Quan (总览)

Thú Linh Sư Hội là tổ chức tu sĩ chuyên về kết giao linh thú bằng tâm linh, do Thú Ngữ Ông — lão nhân có thiên phú giao tiếp với động vật — thành lập cách đây 60 năm. Gồm khoảng 80 thành viên, đa số ở cấp Luyện Khí, mỗi người sở hữu 1-3 linh thú đồng hành tự nguyện đi theo. Khác biệt cốt lõi giữa Thú Linh Sư Hội và các thế lực ngự thú khác (như Bách Thú Sơn Trang) là triết lý: "Kết giao thay vì khuất phục." Hội không dùng khế ước cưỡng chế hay bùa trấn áp mà dùng lòng chân thành và tâm linh để xây dựng mối quan hệ bình đẳng giữa người và thú. Điều này khiến linh thú đồng hành trung thành tuyệt đối nhưng cũng có nghĩa quá trình kết giao rất chậm và đòi hỏi kiên nhẫn lớn.

## II. Địa Lý & Tài Nguyên (地理与资源)

Trụ sở Hội nằm sâu trong rừng rậm phía đông Đông Hoang, cách Vạn Yêu Thành khoảng 300 dặm — đủ xa để tránh sự chú ý nhưng đủ gần để tiếp cận nguồn linh thú đa dạng. Khu vực xung quanh là rừng rậm tự nhiên với nhiều hang động, suối trong và bãi cỏ nhỏ — môi trường lý tưởng cho linh thú cấp thấp sinh sống. Tài nguyên chính bao gồm linh thú cấp thấp (đối tượng kết giao), dược thảo mọc hoang (dùng chữa trị cho cả người và thú), và lông vũ, xương thú rơi tự nhiên (dùng chế tác đồ vật đơn giản).

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)

Toàn bộ văn hóa Hội xoay quanh sự tôn trọng tuyệt đối đối với linh thú. Quy tắc nghiêm ngặt bao gồm: cấm giết linh thú đã kết giao, cấm buôn bán linh thú, và ai ngược đãi thú sẽ bị trục xuất vĩnh viễn. Nghi lễ nhập hội đặc biệt: thành viên mới phải sống một mình trong rừng ba tháng liên tiếp, không được mang theo vũ khí hay pháp khí, chỉ dựa vào bản năng sinh tồn và tâm linh để tự tìm một linh thú nguyện ý đi theo. Nếu sau ba tháng không có linh thú nào chấp nhận, người đó không đủ tư cách gia nhập. Nghi lễ này đảm bảo chỉ những người thực sự có thiên phú và lòng chân thành mới trở thành Thú Linh Sư.

## IV. Cơ Cấu Tổ Chức (组织结构)

Hội Trưởng Thú Ngữ Ông là lão nhân có khả năng giao tiếp với hầu hết linh thú cấp thấp, là trụ cột tinh thần và kỹ thuật của Hội. 3 Trưởng Lão (Trúc Cơ) phân công theo chuyên môn: Trưởng Lão Phi Cầm (chuyên chim), Trưởng Lão Tẩu Thú (chuyên thú chạy), và Trưởng Lão Thủy Sinh (chuyên thú nước). 70 thành viên chính đa số ở cấp Luyện Khí, mỗi người có ít nhất một linh thú đồng hành. 6 tổng quản phụ trách hậu cần, chăm sóc thú bị thương và quản lý khu cư trú. Tổng cộng Hội có hơn 200 linh thú đồng hành các loại.

## V. Công Pháp & Trận Pháp (功法与阵法)

Công pháp chấn hội là "Thú Linh Tâm Ấn" — không phải công pháp tăng tu vi mà là phương pháp dùng tâm thức để thiết lập liên kết tâm linh với linh thú. Người tu luyện Tâm Ấn có thể cảm nhận cảm xúc, ý định và nhu cầu của linh thú đồng hành trong bán kính nhất định, tạo nền tảng cho sự phối hợp chiến đấu nhịp nhàng. Hội không có trận pháp chính thống mà dựa vào linh thú tuần tra cảnh giới — mạng lưới linh thú nhỏ (chim, thú, côn trùng) bao phủ khu vực xung quanh trụ sở, phát hiện kẻ xâm nhập nhanh hơn bất kỳ trận cảnh giới nào.

## VI. Đặc Sản Môn Phái (门派特产)

Sản phẩm quý giá nhất là dịch vụ kết giao linh thú — giúp tu sĩ bên ngoài tìm và kết giao linh thú đồng hành phù hợp tính cách. Phí dịch vụ dựa trên cấp bậc linh thú và độ khó kết giao. Ngoài ra, Hội bán dược thảo hoang thu thập từ rừng sâu và vật liệu thú tự nhiên (lông vũ, xương, vảy rơi) — không phải săn bắt mà là thu nhặt những gì linh thú thay đổi tự nhiên. Kiến thức về tập tính linh thú tích lũy 60 năm cũng là tài sản vô hình quý giá, nhưng Hội chỉ chia sẻ cho những ai chứng minh lòng tôn trọng động vật.

## VII. Cơ Sở Hạ Tầng (基础设施)

Trụ sở là một quần thể nhà gỗ xen kẽ hang đá tự nhiên trong rừng sâu, thiết kế hòa hợp với môi trường để không xua đuổi linh thú. Khu cư trú của thành viên nằm trên cây lớn và trong hang, mỗi nơi đều có không gian cho linh thú đồng hành. Khu chữa trị thú bị thương là hang đá rộng với suối nước chảy qua, dùng dược thảo tươi để điều trị. Bãi tập ngoài trời dùng cho huấn luyện phối hợp chiến đấu người-thú. Không có tường thành hay cổng — ranh giới trụ sở do linh thú tuần tra tự nhiên đánh dấu.

## VIII. Kinh Tế (经济)

Kinh tế của Hội ổn định ở mức thấp, đủ duy trì nhưng không dư dả. Thu nhập chính từ dịch vụ kết giao linh thú (phí dao động tùy yêu cầu), bán dược thảo hoang và vật liệu thú tự nhiên. Chi phí chính là lương thực cho 80 thành viên và hơn 200 linh thú — đặc biệt linh thú cấp cao cần thức ăn đặc biệt. Hội cũng nhận hướng dẫn sinh tồn rừng rậm cho tu sĩ trẻ, thu phí nhỏ nhưng ổn định. Tổng thể, Hội sống tự cung tự cấp phần lớn, chỉ cần mua sắm vật tư không thể tìm trong rừng.

## IX. Lịch Sử Tóm Tắt (简史)

Thú Ngữ Ông là tán tu linh căn yếu, tu đến Trúc Cơ Viên Mãn đã là giới hạn tuyệt đối. Nhưng ông sở hữu thiên phú bẩm sinh đặc biệt trong việc giao tiếp với linh thú — có thể cảm nhận cảm xúc và ý định của động vật chỉ bằng ánh mắt. 60 năm trước, ông nhận ra rằng nhiều tu sĩ yếu có thể sinh tồn tốt hơn nếu có linh thú đồng hành — không phải nô lệ mà là bạn đồng hành. Ông lập Hội để dạy những tu sĩ tương tự mình cách kết giao linh thú bằng tâm linh, biến điểm yếu tu vi thành sức mạnh qua sự phối hợp người-thú. Hội nhỏ bé, ẩn dật trong rừng, không ai để ý — và Thú Ngữ Ông thích điều đó.

## X. Giai Thoại & Bí Mật (轶事与秘密)

Trong rừng sâu gần trụ sở, một linh thú cấp cao bí ẩn đôi khi xuất hiện — không ai biết loài gì, hình dạng thay đổi mỗi lần, nhưng luôn phát ra khí tức áp đảo khiến mọi linh thú trong khu vực nằm rạp. Thú Ngữ Ông biết sự tồn tại của nó nhưng không dám tiếp cận — linh cảm của lão nói rằng sinh vật đó không phải linh thú bình thường, có thể là cổ yêu hoặc thứ gì đó cổ đại hơn. Lão giữ bí mật này vì sợ gây hoang mang trong Hội và thu hút sự chú ý không mong muốn từ bên ngoài.

Một bí mật nghiêm trọng hơn: vài thành viên bí mật bán thông tin về phân bố linh thú cho thợ săn bên ngoài để kiếm thêm linh thạch. Nếu bị phát hiện, sự phản bội này sẽ gây ra khủng hoảng lòng tin nghiêm trọng — vì toàn bộ Hội được xây dựng trên niềm tin tôn trọng linh thú, và bán thông tin cho thợ săn là hành vi đi ngược lại mọi nguyên tắc.

## XI. Quan Hệ Thế Lực (势力关系)

- **Bách Thú Sơn Trang:** Mâu thuẫn triết lý cốt lõi — Sơn Trang dùng khế ước cưỡng chế linh thú, Hội coi đó là "nô dịch." Tuy nhiên, Sơn Trang là Hạng Nhì nên Hội không dám công khai phản đối, chỉ ngầm chỉ trích.
- **Thiên Yêu Đình:** Thiên Yêu Đình biết Hội tồn tại nhưng coi là quá nhỏ để quan tâm. Hội cẩn thận không xâm phạm lãnh thổ yêu tộc, duy trì khoảng cách an toàn.
- **Hoang Dã Thợ Săn Bang:** Kẻ thù tự nhiên — Thợ Săn Bang săn bắt linh thú mà Hội bảo vệ. Xung đột nhỏ xảy ra thường xuyên nhưng chưa leo thang vì cả hai đều yếu.
