---
type: faction
name: Phế Độc Đường
hantu: 廢毒堂
faction_type: Tông Môn
alignment: 4
race: Nhân Tộc
region: Đông Hoang
founded: 15 năm trước
founder: Liễu Vô Hận
emblem: Phe_Doc_Duong.png
specialty: Độc học thanh lọc, Phế Độc Quyết, Trinh sát Vạn Độc Cốc
economy:
- Bán thuốc giải độc cao cấp (số lượng hạn chế)
- Trao đổi tình báo nội bộ Vạn Độc Môn lấy vật tư
- Trồng Ngũ Độc Thảo biến thể
arcs:
  - arc: 1
    status: Hoạt động ngầm
    rank: Hạng Tư
    leader: Đường Chủ Liễu Vô Hận
    population: 25
    territory:
      - Hang động ngầm gần Vạn Độc Cốc (dưới tầng rễ cổ thụ)
    assets:
      - name: Bản sao Vạn Độc Chân Kinh (một phần)
        type: Bảo Vật
      - name: Bản đồ nội bộ Vạn Độc Cốc (lỗi thời)
        type: Tài Nguyên
      - name: Ngũ Hành Giải Độc Trận
        type: Trận Pháp
      - name: Vườn Ngũ Độc Thảo bí mật
        type: Tài Nguyên
    stats: [200, 180, 160, 25, 350, 250]
    divisions:
      - name: Chính Đường
        role: Tu luyện Phế Độc Quyết, nghiên cứu giải độc và trinh sát Vạn Độc Cốc
        headcount:
          thai_thuong: 0
          ho_phap: 0
          truong_lao: 1
          chan_truyen: 5
          noi_mon: 10
          ngoai_mon: 0
          tap_dich: 9
        members:
          - character: Liễu Vô Hận
            position: Đường Chủ
            cultivation: Kim Đan Sơ Kỳ
          - character: Trần Khổ Tâm
            position: Phó Đường Chủ
            cultivation: Trúc Cơ Viên Mãn
          - character: "[Trinh Sát Nhất]"
            position: Đội Trưởng Trinh Sát
            cultivation: Trúc Cơ Trung Kỳ
            placeholder: true
    relationships:
      - faction: Vạn Độc Môn
        description: Tử địch cá nhân, Phế Độc Đường do cựu đệ tử phản bội lập nên, bị Vạn Độc Thất Sát đặc biệt truy sát.
        diplomacy:
          lien_minh: -100
          tin: -100
          uy_hiep: 90
          thuong_mai: -100
          on_oan: -100
          le_thuoc: 0
      - faction: Phản Độc Minh
        description: Đồng minh bí mật, trao đổi thông tin nội bộ Vạn Độc Môn lấy mạng lưới trinh sát biên giới và dược liệu.
        diplomacy:
          lien_minh: 60
          tin: 50
          uy_hiep: 0
          thuong_mai: 30
          on_oan: 20
          le_thuoc: 0
      - faction: Dược Vương Cốc
        description: Liễu Vô Hận từng liên lạc bí mật với Dược Vương Cốc để xin hỗ trợ phương pháp thanh lọc độc tố trong Phế Độc Quyết, nhưng bị từ chối vì sợ liên lụy.
        diplomacy:
          lien_minh: 5
          tin: 10
          uy_hiep: 0
          thuong_mai: 5
          on_oan: -10
          le_thuoc: 0
---

# PHẾ ĐỘC ĐƯỜNG (廢毒堂)

## I. Tổng Quan (总览)

Phế Độc Đường là tổ chức bí mật do những cựu đệ tử Vạn Độc Môn đào thoát thành lập, với mục tiêu duy nhất: tìm cách phá hủy Huyết Trì — trái tim quyền lực của Vạn Độc Môn. Dưới sự lãnh đạo của Đường Chủ Liễu Vô Hận — cựu nội môn đệ tử chi Xà, Kim Đan Sơ Kỳ — Phế Độc Đường chỉ có 25 thành viên nhưng sở hữu kiến thức nội bộ vô giá về cơ cấu, bí thuật và điểm yếu của Vạn Độc Môn. Triết lý "Độc có thể cứu người, không nhất thiết phải giết người" thể hiện niềm tin rằng Vạn Độc Môn đã đi chệch khỏi con đường nghiên cứu độc học chân chính vào tà đạo.

## II. Địa Lý & Tài Nguyên (地理与资源)

Trụ sở Phế Độc Đường ẩn trong hang động ngầm cách Vạn Độc Cốc chưa đầy 50 dặm — vị trí cực kỳ nguy hiểm nhưng cho phép theo dõi kẻ thù cũ sát sao. Mạng lưới hang nhỏ kết nối bằng đường hầm hẹp chỉ đủ một người đi, lối vào ngụy trang bằng rễ cây cổ thụ và chướng khí tự nhiên. Tài nguyên gồm bí phương luyện đan cấp thấp đánh cắp từ Vạn Độc Môn, bản đồ nội bộ Vạn Độc Cốc đã lỗi thời nhưng vẫn có giá trị định hướng, và một lượng nhỏ Ngũ Độc Thảo trồng lén trong hang — chất lượng kém hơn bản gốc nhưng đủ để bào chế thuốc giải cơ bản.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)

Phế Độc Đường xây dựng văn hóa trên nền tảng phản tỉnh và chuộc tội. Triết lý "Độc có thể cứu người, không nhất thiết phải giết người" phản ánh niềm tin rằng độc học là một nhánh tri thức trung lập — con người sử dụng nó mới quyết định thiện ác. Quy tắc nghiêm ngặt: cấm sử dụng Dược Nhân, cấm luyện Cổ bằng sinh mạng người vô tội, ai vi phạm sẽ bị phế bỏ tu vi. Thành viên mới phải uống "Phế Độc Thang" — loại thuốc thanh tẩy tà khí của Vạn Độc Môn khỏi cơ thể, quá trình cực kỳ đau đớn kéo dài ba ngày ba đêm, tượng trưng cho việc cắt đứt hoàn toàn với quá khứ tà đạo.

## IV. Cơ Cấu Tổ Chức (组织结构)

Tổ chức gọn nhẹ theo mô hình tông môn nhỏ. Đường Chủ Liễu Vô Hận — cựu nội môn đệ tử chi Xà của Vạn Độc Môn, phản bội sau khi chứng kiến Lễ Tế Cổ dùng trẻ em — nắm quyền quyết định tối cao ở cấp Kim Đan Sơ Kỳ. Phó Đường Chủ Trần Khổ Tâm là cựu Dược Nô sống sót, Trúc Cơ Viên Mãn, am hiểu quy trình luyện đan của Vạn Độc Môn từ trong ra ngoài. Đội trinh sát 5 người Trúc Cơ chuyên theo dõi động tĩnh Vạn Độc Cốc. Phần còn lại là 15 đệ tử — toàn bộ đều là cựu thành viên Vạn Độc Môn đào thoát qua các thời kỳ khác nhau.

## V. Công Pháp & Trận Pháp (功法与阵法)

- **Công Pháp:** "Phế Độc Quyết" — phiên bản thanh lọc của Vạn Độc Chân Kinh, bỏ đi phần tà đạo dùng sinh mạng người để tăng lực. Tu vi tăng chậm hơn bản gốc rất nhiều nhưng không có phản phệ tà khí. Liễu Vô Hận tự tay biên soạn lại từ phần Vạn Độc Chân Kinh mang theo khi đào thoát.
- **Trận Pháp:** "Ngũ Hành Giải Độc Trận" — trận pháp phòng thủ cấp thấp dùng ngũ hành tương khắc để hóa giải độc khí xâm nhập hang động. Không đủ mạnh để chống tu sĩ nhưng hiệu quả ngăn chặn côn trùng độc và chướng khí lan tỏa.

## VI. Đặc Sản Môn Phái (门派特产)

- **Phế Độc Thang:** Thuốc thanh tẩy tà khí Vạn Độc Môn khỏi kinh mạch tu sĩ, quá trình đau đớn nhưng hiệu quả. Là sản phẩm độc quyền mà không tông môn nào khác có thể bào chế vì cần hiểu biết sâu về cơ chế tà khí Vạn Độc Chân Kinh.
- **Ngũ Độc Thảo Biến Thể:** Ngũ Độc Thảo trồng trong môi trường hang động thiếu ánh sáng, chất lượng kém hơn bản gốc nhưng tính chất thay đổi — từ kịch độc chuyển thành bán độc, có thể dùng trực tiếp làm dược liệu giải độc mà không cần tinh luyện phức tạp.

## VII. Cơ Sở Hạ Tầng (基础设施)

- **Hang Động Chính:** Không gian lớn nhất trong mạng lưới hang, dùng làm nơi tu luyện và hội họp. Tường hang được khắc Ngũ Hành Giải Độc Trận để duy trì không khí trong lành.
- **Phòng Luyện Đan:** Hang nhỏ chuyên dụng trang bị lò đan thu nhỏ, nơi Trần Khổ Tâm bào chế thuốc giải và Phế Độc Thang.
- **Vườn Ngũ Độc Thảo:** Khu hang ẩm được chiếu sáng bằng dạ quang thạch, trồng Ngũ Độc Thảo biến thể và vài loại dược liệu giải độc khác.
- **Đường Hầm Thoát Hiểm:** Ba đường hầm bí mật dẫn ra ba hướng khác nhau, đảm bảo luôn có đường rút lui nếu bị Vạn Độc Thất Sát phát hiện.
- **Trạm Quan Sát:** Điểm quan sát ngụy trang trên bề mặt, hướng về phía Vạn Độc Cốc, do đội trinh sát luân phiên canh gác.

## VIII. Kinh Tế (经济)

Kinh tế của Phế Độc Đường cực kỳ khiêm tốn và bí mật. Thu nhập chính đến từ việc bán thuốc giải độc cao cấp cho tán tu qua trung gian ẩn danh — số lượng hạn chế để tránh thu hút sự chú ý. Trao đổi tình báo nội bộ Vạn Độc Môn với Phản Độc Minh là nguồn vật tư quan trọng. Ngũ Độc Thảo biến thể tự trồng giúp giảm phụ thuộc vào nguồn cung bên ngoài. Nhìn chung, Phế Độc Đường sống trong cảnh nghèo khổ tự nguyện — mọi nguồn lực đều dồn cho mục tiêu phá hủy Huyết Trì.

## IX. Lịch Sử Tóm Tắt (简史)

Liễu Vô Hận vốn là nội môn đệ tử xuất sắc chi Xà của Vạn Độc Môn, được kỳ vọng trở thành thế hệ kế cận. Tuy nhiên, 15 năm trước, khi chứng kiến Lễ Tế Cổ dùng trẻ em làm vật tế — hàng chục đứa trẻ bị đưa vào Huyết Trì để nuôi dưỡng Cổ Vương — Liễu Vô Hận quyết định phản bội. Hắn đánh cắp một phần Vạn Độc Chân Kinh và bỏ trốn cùng vài đồng môn có cùng suy nghĩ.

Cuộc đào thoát khốc liệt — Vạn Độc Thất Sát truy sát không ngừng, ba đồng đội hy sinh để Liễu Vô Hận thoát thân. Sau đó, hắn ẩn mình trong hang động ngầm gần Vạn Độc Cốc, lập Phế Độc Đường với mục tiêu duy nhất: phá hủy Huyết Trì. Qua 15 năm, hắn biên soạn lại Phế Độc Quyết, thu nhận thêm cựu đệ tử đào thoát, và gần đây bắt đầu liên lạc bí mật với Phản Độc Minh để mở rộng mạng lưới tình báo.

## X. Giai Thoại & Bí Mật (轶事与秘密)

- Liễu Vô Hận biết vị trí chính xác của "Cổ Vương" mà Độc Cô Lão Quái đang nuôi dưỡng trong Huyết Trì — nhưng hắn không dám tiết lộ cho bất kỳ ai vì sợ gây ra đại chiến mà phe chính đạo chưa sẵn sàng. Nếu Cổ Vương hoàn thành tiến hóa, sức mạnh sẽ ngang ngửa Hóa Thần.
- Phế Độc Quyết thực ra vẫn còn ẩn chứa một đoạn mật chú tà đạo mà Liễu Vô Hận chưa tìm ra cách loại bỏ. Tu luyện quá Kim Đan Trung Kỳ sẽ có nguy cơ tẩu hỏa nhập ma — điều này có nghĩa bản thân Liễu Vô Hận đang bước vào vùng nguy hiểm.
- Trần Khổ Tâm — Phó Đường Chủ, cựu Dược Nô — giấu kín một bí mật: hắn từng bị cưỡng ép tham gia luyện Cổ trước khi đào thoát, và trong cơ thể hắn vẫn còn một ấu trùng Cổ đang ngủ yên. Nếu ấu trùng tỉnh giấc, hắn sẽ bị Trùng Mẫu Vạn Trùng Cốc phát hiện vị trí.

## XI. Quan Hệ Thế Lực (势力关系)

| Thế Lực | Quan Hệ | Mô Tả |
|---------|---------|-------|
| Vạn Độc Môn | Tử địch | Mục tiêu phá hủy Huyết Trì, bị Thất Sát truy sát |
| Phản Độc Minh | Đồng minh bí mật | Trao đổi tình báo và mạng lưới trinh sát |
| Dược Vương Cốc | Thỉnh cầu bất thành | Từng xin hỗ trợ thanh lọc Phế Độc Quyết, bị từ chối |
