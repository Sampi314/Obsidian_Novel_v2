---
type: faction
name: Giao Nhân Bần Dân
hantu: 鲛人贫民
faction_type: Bộ Lạc
alignment: -2
race: Giao Nhân Tộc
region: Đông Hoang
founded: Từ thuở sơ khai Giao Nhân Tộc
founder: Không có (giai cấp tự nhiên hình thành)
emblem: Giao_Nhan_Ban_Dan.png
specialty: Dệt ti biển, Sản xuất ngọc trai nước mắt, Lao động thủ công dưới nước
economy:
- Dệt ti biển cho hoàng tộc
- Ngọc trai nước mắt (bị hoàng tộc thu hết)
- Lao động khổ sai đổi lương thực
arcs:
  - arc: 1
    status: Bị áp bức
    rank: Không Xếp Hạng
    leader: Trưởng Khu Lệ Vân
    population: 200
    territory:
      - Khu ổ chuột rìa ngoài lãnh hải Lệ Nhược Thủy
    assets:
      - name: Xưởng Dệt Ti Biển
        type: Công Trình
      - name: Hắc Ngọc Trai (bí mật)
        type: Bảo Vật
    stats: [5, 10, 5, 200, 5, 5]
    divisions:
      - name: Khu Bần Dân
        role: Sinh sống và lao động dệt ti biển cho hoàng tộc
        headcount:
          truong_lao: 1
          chien_binh: 0
          dan_thuong: 199
        members:
          - character: Lệ Vân
            position: Trưởng Khu
            cultivation: Trúc Cơ (tự học, giấu kín)
          - character: "[Bé Gái Hắc Ngọc]"
            position: Dân thường
            cultivation: Không
            placeholder: true
    relationships:
      - faction: Giao Nhân Hoàng Tộc
        description: Giai cấp bị áp bức và bóc lột, bần dân bị cấm rời khu vực mà không có giấy phép, ngọc trai nước mắt bị thu hết.
        diplomacy:
          lien_minh: -80
          tin: -60
          uy_hiep: 90
          thuong_mai: -90
          on_oan: -70
          le_thuoc: 95
      - faction: Giao Nhân Tộc Liên Minh
        description: Lệ Vân bí mật liên lạc với liên minh bên ngoài, tìm cách giải phóng bần dân khỏi ách thống trị.
        diplomacy:
          lien_minh: 40
          tin: 30
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 50
          le_thuoc: 0
      - faction: Ngọc Trai Sâu Phường
        description: Phường thu mua ngọc trai thông qua hoàng tộc, gián tiếp hưởng lợi từ sức lao động bần dân, bần dân căm ghét nhưng bất lực.
        diplomacy:
          lien_minh: -30
          tin: -20
          uy_hiep: 20
          thuong_mai: -50
          on_oan: -40
          le_thuoc: 30
---

# Giao Nhân Bần Dân (鲛人贫民)

## I. Tổng Quan (总览)
Giao Nhân Bần Dân không phải một thế lực theo nghĩa truyền thống mà là một giai cấp bị đè nén trong xã hội Giao Nhân Tộc. Khoảng hai trăm Giao Nhân sống chen chúc trong khu ổ chuột tồi tàn ở rìa ngoài lãnh hải Lệ Nhược Thủy, bị cấm tự do đi lại và phải lao động cực nhọc dệt ti biển cho tầng lớp hoàng tộc. Nước mắt họ hóa thành ngọc trai nhưng họ không được phép giữ lại một viên nào. Trưởng Khu Lệ Vân, một Giao Nhân già cảnh giới tương đương Trúc Cơ nhờ tự học, âm thầm giữ ngọn lửa phản kháng cháy âm ỉ trong lòng khu bần dân, chờ đợi thời cơ thay đổi số phận của cả cộng đồng.

## II. Địa Lý & Tài Nguyên (地理与资源)
Khu bần dân nằm ở vùng rìa ngoài lãnh hải Giao Nhân hoàng tộc, nơi dòng hải lưu lạnh và ánh sáng mặt trời hiếm khi xuyên tới. Nhà cửa được xây bằng xương cá lớn và rong biển ép chặt, chật chội, tối tăm, và luôn ẩm mốc. Các gia đình sáu bảy người chen chung trong những căn phòng chỉ rộng vài thước vuông. Tài nguyên duy nhất đáng kể là ti biển — loại tơ do Giao Nhân tiết ra từ tuyến dịch dưới da, mềm mại và bền hơn bất kỳ loại tơ nào trên cạn. Tuy nhiên, toàn bộ sản phẩm ti biển đều bị hoàng tộc thu hết, bần dân chỉ nhận lại lương thực tối thiểu đủ để sống sót và tiếp tục lao động.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
Văn hóa bần dân thấm đẫm nỗi buồn truyền đời. Câu nói "Sinh ra đã khóc, chết đi vẫn khóc" không chỉ là thành ngữ mà là sự thật hiện thực — nước mắt Giao Nhân hóa ngọc trai, và trong khu bần dân, không thiếu nước mắt. Trẻ em bắt đầu dệt ti biển từ năm tuổi, mười ngón tay chai sần là dấu hiệu nhận biết kẻ thuộc giai cấp dưới đáy. Hoàng tộc tuyên truyền rằng ngọc trai từ nước mắt bần dân có màu xám đục vì "tâm hồn không thuần khiết", nhưng sự thật là do cơ thể bần dân kiệt sức và suy dinh dưỡng trầm trọng. Dù trong cảnh khốn cùng, bần dân vẫn lưu truyền những bài hát ru bằng thứ tiếng Giao Nhân cổ mà hoàng tộc đã bỏ quên — trong các bài hát ấy ẩn chứa ký ức về thời kỳ Giao Nhân chưa phân chia giai cấp.

## IV. Cơ Cấu Tổ Chức (组织结构)
Khu bần dân không có tổ chức chính thức, chỉ có Trưởng Khu do hoàng tộc chỉ định để phân công lao động. Lệ Vân đảm nhiệm vai trò này, một Giao Nhân già mà hoàng tộc coi là ngoan ngoãn, nhưng thực tế lão là hậu duệ của người lãnh đạo cuộc nổi dậy hai trăm năm trước, mang trong lòng thù hận ngầm qua nhiều thế hệ. Dưới lão là năm mươi Thợ Dệt chính thức cảnh giới Luyện Khí, làm việc mười hai canh giờ mỗi ngày không ngừng nghỉ. Phần còn lại gồm người già, trẻ em, và những Giao Nhân quá yếu để dệt — họ làm các việc lặt vặt như thu hoạch rong biển, nấu ăn, và chăm sóc người bệnh.

## V. Công Pháp & Trận Pháp (功法与阵法)
Bần dân bị hoàng tộc cấm tuyệt đối không được tu luyện công pháp chiến đấu. Kỹ thuật duy nhất được phép học là Phưởng Ti Thuật — phương pháp kéo tơ từ tuyến dịch dưới da, thuần túy phục vụ sản xuất. Tuy nhiên, Lệ Vân đã bí mật tự học được Thủy Lưu Thuật từ một mảnh sách rách nhặt được trong đống rác hoàng tộc vứt bỏ. Lão luyện tập vào ban đêm khi không ai quan sát, và đã đạt cảnh giới tương đương Trúc Cơ. Nếu bị hoàng tộc phát hiện tu luyện trái phép, Lệ Vân sẽ bị xử tử làm gương, vì vậy lão che giấu vô cùng cẩn thận, ngay cả những bần dân thân cận nhất cũng không biết thực lực thực sự của lão.

## VI. Đặc Sản Môn Phái (门派特产)
- **Ti Biển Giao Nhân:** Loại tơ mềm mại, bền bỉ và có ánh ngọc trai nhẹ, được giới quyền quý khắp Đông Hoang săn đón. Toàn bộ sản phẩm bị hoàng tộc thu giữ và bán với giá cao ngất, bần dân không nhận được xu nào.
- **Ngọc Trai Nước Mắt Xám:** Ngọc trai kết tinh từ nước mắt bần dân, có màu xám đục do cơ thể suy kiệt. Tuy phẩm chất kém hơn ngọc trai hoàng tộc nhưng vẫn có giá trị nhất định trong luyện đan.
- **Bài Hát Ru Cổ:** Không phải sản phẩm vật chất nhưng là di sản văn hóa quý giá, lưu giữ tiếng Giao Nhân cổ mà hoàng tộc đã quên, trong đó ẩn chứa các giai điệu có tác dụng an thần dưới nước.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Xưởng Dệt Ti Biển:** Khu vực lao động chính, gồm hai mươi khung cửi thô sơ bằng xương cá và san hô chết, nơi Thợ Dệt làm việc suốt ngày đêm.
- **Nhà Ở Xương Cá:** Các túp lều chật chội bằng xương cá và rong biển, không có hệ thống sưởi ấm hay chiếu sáng, chỉ dựa vào ánh sáng lờ mờ từ rêu phát quang.
- **Bệ Tập Kết:** Khu vực hoàng tộc đến thu gom ti biển và ngọc trai mỗi tuần, cũng là nơi phát lương thực cho bần dân.

## VIII. Kinh Tế (经济)
Kinh tế khu bần dân hoàn toàn phụ thuộc vào hoàng tộc theo mô hình bóc lột triệt để. Bần dân sản xuất ti biển và ngọc trai nước mắt, toàn bộ sản phẩm bị hoàng tộc thu hết không trả thù lao, chỉ phát lại lương thực ở mức tối thiểu đủ để duy trì sức lao động. Bần dân không có quyền sở hữu tài sản, không được phép trao đổi hàng hóa với bên ngoài, và bị cấm rời khu vực mà không có giấy phép từ hoàng tộc. Đây là hệ thống nô lệ trá hình dưới lớp vỏ "phân công xã hội truyền thống", và là nguồn cơn cho mọi mâu thuẫn âm ỉ trong lòng xã hội Giao Nhân Tộc.

## IX. Lịch Sử Tóm Tắt (简史)
Giai cấp bần dân đã tồn tại song song với Giao Nhân hoàng tộc từ thuở sơ khai, hình thành từ sự phân hóa quyền lực trong nội bộ chủng tộc. Suốt hàng ngàn năm, bần dân cam chịu kiếp nô lệ, cho đến khi hai trăm năm trước, một cuộc nổi dậy bùng phát dưới sự lãnh đạo của tổ tiên Lệ Vân. Cuộc khởi nghĩa bị đàn áp tàn khốc, hàng trăm bần dân bị giết, và những quy định kiểm soát càng trở nên nghiệt ngã hơn. Lệ Vân, hậu duệ trực hệ của người lãnh đạo năm xưa, được chỉ định làm Trưởng Khu vì hoàng tộc cho rằng gia tộc này đã bị bẻ gãy ý chí. Họ không biết rằng lão đang âm thầm kết nối với Giao Nhân Tộc Liên Minh bên ngoài, chờ đợi thời cơ cho một cuộc giải phóng thực sự.

## X. Giai Thoại & Bí Mật (轶事与秘密)
Bí mật lớn nhất khu bần dân là sự tồn tại của một bé gái Giao Nhân có nước mắt hóa thành hắc ngọc trai — loại ngọc trai đen tuyền cực kỳ hiếm có, là vật cấm kỵ trong truyền thuyết Giao Nhân, tương truyền có khả năng hấp thu và phong ấn linh lực. Nếu hoàng tộc phát hiện, họ sẽ không ngần ngại giết cả khu bần dân để đoạt lấy cô bé. Lệ Vân đang che giấu cô bé bằng mọi giá, nhờ những Giao Nhân già đáng tin cậy nhất chăm sóc và đảm bảo cô bé không bao giờ khóc trước mặt người lạ. Ngoài ra, Lệ Vân đã bí mật thiết lập được đường dây liên lạc với Giao Nhân Tộc Liên Minh bên ngoài thông qua những con sứa truyền tin, lên kế hoạch cho một cuộc di tản quy mô lớn khi thời cơ chín muồi.

## XI. Quan Hệ Thế Lực (势力关系)
- **Giao Nhân Hoàng Tộc:** Kẻ áp bức trực tiếp, kiểm soát toàn diện đời sống bần dân từ lao động đến sinh sản. Bần dân căm ghét nhưng không dám phản kháng công khai.
- **Giao Nhân Tộc Liên Minh:** Hy vọng duy nhất của bần dân, Lệ Vân bí mật liên lạc để tìm kiếm sự hỗ trợ giải phóng. Tuy nhiên, liên minh cũng có mục đích riêng và bần dân không chắc có thể hoàn toàn tin tưởng.
- **Ngọc Trai Sâu Phường:** Phường thu mua ngọc trai gián tiếp hưởng lợi từ sức lao động bần dân, bần dân ghét nhưng không có khả năng đối đầu.
