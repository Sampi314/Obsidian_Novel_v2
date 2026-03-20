---
type: faction
name: Lông Vũ Phường
hantu: 羽毛坊
faction_type: Thương Hội
alignment: 3
race: Vũ Tộc
region: Đông Hoang
founded: Cách đây 20 năm
founder: Vũ Mao Nhi
emblem: Long_Vu_Trang_Xanh.png
specialty: Thu mua và phân loại lông vũ linh, Bảo quản linh lực trong lông vũ, Chế tác lông vũ trang sức
economy:
- Bán lông vũ linh cho thợ rèn pháp khí cấp thấp
- Thu mua lông rụng tự nhiên từ Vũ Tộc
- Nghiên cứu dệt y phục chống lạnh từ lông vũ
arcs:
  - arc: 1
    status: Hoạt động ổn định
    rank: Hạng Năm
    leader: Phường Chủ Vũ Mao Nhi
    population: 12
    territory:
      - Vách đá tundra gần Vũ Tộc Lưu Dân Trại
    assets:
      - name: Kho Bảo Quản Lông Vũ
        type: Công Trình
      - name: Thuật Bảo Quản Linh Vũ
        type: Bí Thuật
    stats: [10, 30, 20, 12, 15, 25]
    divisions:
      - name: Phường Chính
        role: Thu mua, phân loại, bảo quản và đóng gói lông vũ linh để xuất bán
        headcount:
          hoi_truong: 1
          truong_lao: 0
          thuong_nhan: 3
          ho_ve: 0
          nhan_cong: 8
        members:
          - character: Vũ Mao Nhi
            position: Phường Chủ
            cultivation: Luyện Khí Đỉnh Phong
          - character: "[Vũ Tiểu Dực]"
            position: Thợ Phân Loại Trưởng
            cultivation: Luyện Khí Trung Kỳ
            placeholder: true
    relationships:
      - faction: Vũ Tộc Lưu Dân Trại
        description: Nguồn cung lông vũ chính, quan hệ hợp tác bền vững — Lông Vũ Phường mua lông rụng tự nhiên từ Vũ Tộc nghèo, tạo nguồn thu nhập ổn định cho họ.
        diplomacy:
          lien_minh: 40
          tin: 50
          uy_hiep: 0
          thuong_mai: 70
          on_oan: 20
          le_thuoc: 30
      - faction: Phá Băng Thương Đội
        description: Đối tác vận chuyển duy nhất, chịu trách nhiệm chuyển lông vũ về Trung Thổ bán cho thợ rèn pháp khí cấp thấp.
        diplomacy:
          lien_minh: 20
          tin: 40
          uy_hiep: 0
          thuong_mai: 60
          on_oan: 0
          le_thuoc: 40
      - faction: Băng Tằm Ti Phường
        description: Cạnh tranh tiềm năng trên thị trường nguyên liệu pháp khí cấp thấp — cả hai cùng bán sản phẩm cho thợ rèn Trung Thổ, nhưng hiện chưa xung đột trực tiếp.
        diplomacy:
          lien_minh: 0
          tin: 20
          uy_hiep: 10
          thuong_mai: 30
          on_oan: -10
          le_thuoc: 0
---

# Lông Vũ Phường (羽毛坊)

> *"Lông rụng vẫn có giá — chỉ cần có người biết nhìn."*
> — Vũ Mao Nhi, triết lý kinh doanh

> *"Bà lão Vũ Tộc ấy biến rác thành vàng, biến sự khinh miệt thành kế sinh nhai — đó mới là bản lĩnh thực sự."*
> — Một thương nhân Phá Băng Thương Đội, nhận xét về Vũ Mao Nhi

## I. Tổng Quan (总览)
Lông Vũ Phường là một phường buôn nhỏ chuyên thu mua, phân loại và bán lông vũ linh của Vũ Tộc. Tọa lạc trên vách đá tundra gần Vũ Tộc Lưu Dân Trại, phường do Vũ Mao Nhi — một Vũ Tộc nữ già có kinh nghiệm bốn mươi năm phân biệt chất lượng lông vũ — sáng lập và điều hành. Dù quy mô nhỏ bé với chỉ mười hai thành viên, Lông Vũ Phường đóng vai trò quan trọng trong đời sống kinh tế của Vũ Tộc nghèo vùng Bắc Băng, biến thứ mà nhiều người coi là rác rưởi — lông vũ rụng tự nhiên — thành nguồn thu nhập nuôi sống cả cộng đồng.

## II. Địa Lý & Tài Nguyên (地理与资源)
Phường đặt trụ sở tại một dãy hang đá khô ráo trên vách đá tundra, vị trí này được chọn vì ba lý do: gần nguồn cung Vũ Tộc Lưu Dân Trại, nhiệt độ thấp tự nhiên giúp bảo quản lông vũ lâu hơn, và đủ xa các thế lực lớn để tránh phiền phức. Hang đá được cải tạo thành kho chứa với các giá treo lông vũ phân theo màu sắc và cấp độ linh lực. Tài nguyên chính là lông vũ linh — lông rụng tự nhiên từ Vũ Tộc, chứa Phong linh lực vi lượng. Lông trắng tinh khiết là quý nhất vì chứa linh lực thuần khiết nhất, tiếp theo là lông xanh nhạt, còn lông xám thường là loại phổ thông nhất.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
Triết lý của phường rất giản dị: "Lông rụng vẫn có giá" — tận dụng mọi thứ Vũ Tộc có để đổi lấy thức ăn và vật tư sinh hoạt. Quy tắc tối cao là chỉ thu mua lông rụng tự nhiên, tuyệt đối không được nhổ lông người sống — vi phạm sẽ bị đuổi khỏi phường vĩnh viễn. Phong tục phân loại lông vũ rất tỉ mỉ: mỗi chiếc lông được kiểm tra dưới ánh sáng linh thạch, xoay ba vòng để đánh giá độ bóng và cảm nhận linh lực tàn dư bằng tay. Vũ Mao Nhi tin rằng mỗi chiếc lông vũ mang theo một phần linh hồn của chủ nhân, nên bà đối xử với chúng rất trân trọng.

## IV. Cơ Cấu Tổ Chức (组织结构)
Phường có cơ cấu rất đơn giản do quy mô nhỏ. Vũ Mao Nhi là Phường Chủ, nắm quyền quyết định mọi việc từ giá thu mua đến đối tác bán hàng. Dưới bà có ba thương nhân phụ trách giao dịch với Phá Băng Thương Đội và các khách hàng lẻ, cùng tám nhân công — hỗn hợp Vũ Tộc và Nhân Tộc — chuyên thu gom, phân loại, và đóng gói lông vũ. Nhân công đa phần là Vũ Tộc nghèo từ Lưu Dân Trại, được trả công bằng thức ăn và linh thạch cấp thấp. Phường không có lực lượng hộ vệ riêng — nếu gặp nguy hiểm, họ dựa vào sự che chở của Vũ Tộc Lưu Dân Trại.

## V. Công Pháp & Trận Pháp (功法与阵法)
Lông Vũ Phường không có công pháp chiến đấu — bản thân Vũ Mao Nhi chỉ ở mức Luyện Khí Đỉnh Phong và không có tham vọng đột phá. Tuy nhiên, bà sở hữu một bài thuật bảo quản độc đáo gọi là "Phong Vũ Tỏa Linh Thuật" — kỹ thuật dùng linh lực phong hệ vi lượng bịt kín linh lực bên trong lông vũ, ngăn nó tiêu tán theo thời gian. Nhờ thuật này, lông vũ của Lông Vũ Phường giữ được dược tính lâu gấp ba lần lông vũ thông thường, trở thành lợi thế cạnh tranh lớn nhất của phường. Bà chỉ truyền thuật này cho người kế nhiệm và yêu cầu tuyệt đối giữ bí mật.

## VI. Đặc Sản Môn Phái (门派特产)
- **Lông Vũ Linh Cấp Nhất:** Lông trắng tinh khiết từ Vũ Tộc trưởng lão, chứa Phong linh lực đậm đặc, dùng trong luyện chế pháp khí phong hệ cấp thấp. Số lượng cực hiếm, mỗi năm chỉ thu được vài chiếc.
- **Bó Lông Vũ Phổ Thông:** Lông xám và xanh nhạt đóng thành bó một trăm chiếc, bán sỉ cho thợ rèn Trung Thổ qua Phá Băng Thương Đội. Dùng làm nguyên liệu pháp khí cấp thấp hoặc trang trí phù lục.
- **Vũ Nhung Y (đang nghiên cứu):** Vũ Mao Nhi đang thử nghiệm dệt lông vũ thành y phục chống lạnh cấp thấp — nếu thành công sẽ mở ra thị trường mới.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Hang Đá Kho Chứa:** Hệ thống hang đá tự nhiên được cải tạo, chia thành ba khu vực — kho nguyên liệu thô, phòng phân loại, và kho thành phẩm đã đóng gói. Nhiệt độ tự nhiên thấp giúp bảo quản lông vũ tốt hơn.
- **Bàn Phân Loại Linh Thạch:** Bàn gỗ dài đặt dưới ánh sáng linh thạch, nơi thợ phân loại kiểm tra từng chiếc lông vũ. Linh thạch chiếu sáng giúp phát hiện những chiếc lông chứa linh lực ẩn mà mắt thường không thấy.
- **Điểm Giao Dịch Ngoài Trời:** Khu vực phẳng trước cửa hang, nơi Phá Băng Thương Đội đến nhận hàng theo định kỳ mỗi hai tháng.

## VIII. Kinh Tế (经济)
Kinh tế của Lông Vũ Phường xoay quanh một chuỗi cung ứng đơn giản: thu mua lông rụng từ Vũ Tộc Lưu Dân Trại và Đoản Dực Lạc Đoàn với giá thấp, phân loại và bảo quản bằng thuật độc quyền, rồi bán cho Phá Băng Thương Đội vận chuyển về Trung Thổ. Lợi nhuận trên mỗi đơn hàng rất thấp, nhưng nhờ lượng lông vũ ổn định và chi phí vận hành gần như bằng không (nhân công là Vũ Tộc nghèo sẵn sàng làm việc đổi thức ăn), phường vẫn duy trì được hoạt động và tạo nguồn thu đều đặn cho cộng đồng Vũ Tộc. Vũ Mao Nhi đang tìm cách nâng giá trị sản phẩm bằng việc nghiên cứu dệt y phục, hy vọng thoát khỏi vị thế "nhà cung cấp nguyên liệu thô rẻ mạt."

## IX. Lịch Sử Tóm Tắt (简史)
Hai mươi năm trước, Vũ Mao Nhi — một Vũ Tộc nữ già không có gia đình — phát hiện rằng lông vũ rụng tự nhiên của Vũ Tộc chứa Phong linh lực vi lượng. Dù linh lực rất loãng, thợ rèn pháp khí cấp thấp ở Trung Thổ vẫn cần vì nguồn nguyên liệu phong hệ luôn khan hiếm. Bà bắt đầu thu gom lông rụng từ mặt đất, phân loại theo kinh nghiệm, rồi nhờ Phá Băng Thương Đội chuyển đi bán. Dần dần, Vũ Tộc nghèo ở Lưu Dân Trại bắt đầu chủ động mang lông rụng đến bán cho bà, và Lông Vũ Phường ra đời. Qua hai thập kỷ, phường trở thành nguồn thu nhập chính cho Vũ Tộc nghèo vùng Bắc Băng, dù bản thân Vũ Mao Nhi vẫn sống thanh đạm trong hang đá.

## X. Giai Thoại & Bí Mật (轶事与秘密)
Vũ Mao Nhi từng thu được một chiếc lông phượng hoàng băng — lông vũ phát ra hàn khí lạnh đến mức đóng băng cả kho chứa. Bà giấu kỹ chiếc lông này trong một ngăn bí mật sâu nhất hang đá, không dám bán vì biết rằng nếu tin tức lộ ra, cả Vũ Hoàng Các lẫn các tông phái lớn sẽ đổ xô đến, và Lưu Dân Trại sẽ bị cuốn vào tranh đoạt đẫm máu.

Có thương nhân Trung Thổ từng đề nghị mua lông vũ Vũ Hoàng Các với giá cắt cổ — lông của Vũ Hoàng cấp cao chứa linh lực phong hệ thuần khiết, giá trị gấp nghìn lần lông thường. Vũ Mao Nhi từ chối thẳng vì biết đó là tử lộ: Vũ Hoàng Các sẽ không bao giờ tha thứ cho kẻ dám buôn bán lông của tộc nhân cao cấp của họ.

## XI. Quan Hệ Thế Lực (势力关系)
- **Vũ Tộc Lưu Dân Trại:** Nguồn cung lông vũ chính, quan hệ cộng sinh — phường mua lông rụng tạo thu nhập cho Vũ Tộc nghèo, đổi lại Lưu Dân Trại bảo vệ phường khỏi sơn tặc và thú dữ.
- **Đoản Dực Lạc Đoàn:** Nguồn cung phụ, cung cấp lông vũ từ Vũ Tộc du mục — chất lượng thấp hơn nhưng số lượng lớn.
- **Phá Băng Thương Đội:** Đối tác vận chuyển duy nhất, chịu trách nhiệm đưa lông vũ về Trung Thổ. Quan hệ phụ thuộc — nếu Phá Băng ngừng hợp tác, phường sẽ mất kênh bán hàng chính.
- **Băng Tằm Ti Phường:** Cạnh tranh tiềm năng trên thị trường nguyên liệu pháp khí — hiện chưa xung đột trực tiếp nhưng nếu Vũ Mao Nhi thành công dệt y phục chống lạnh, hai bên sẽ tranh giành khách hàng.
