---
type: faction
name: Kim Sa Thợ Mỏ Hội
hantu: 金沙矿工会
faction_type: Hội
alignment: 4
race: Nhân Tộc (Thợ mỏ tán tu và phàm nhân)
region: Tây Mạc
founded: Năm Khởi Nguyên 99.990
founder: Mạc Kim Thạch
emblem: Cuoc_Mo_Va_Linh_Thach.png
specialty: Khai mỏ linh thạch, Đàm phán tập thể, Tự vệ bằng dụng cụ mỏ
economy:
- Khai thác linh thạch hạ phẩm và sa kim
- Bán khoáng vật thường cho thương đoàn
- Nhận hợp đồng đào hầm cho các tông môn nhỏ
arcs:
  - arc: 1
    status: Đang phát triển — thu hút thêm thợ mỏ từ các mỏ khác
    rank: Hạng Năm
    leader: Hội Trưởng Mạc Kim Thạch
    population: 500
    territory:
      - Khu mỏ linh thạch cấp thấp phía bắc Minh Nguyệt Châu
    assets:
      - name: Hầm Mỏ Chính Bắc Minh
        type: Công Trình
      - name: Bích Họa Cổ Đại Trong Hầm Sâu
        type: Di Tích
    stats: [300, 200, 250, 500, 150, 200]
    divisions:
      - name: Ban Lãnh Đạo
        role: Đàm phán quyền lợi với tông môn, điều hành hội và phân công khai thác
        headcount:
          hoi_truong: 1
          pho_hoi_truong: 2
          thanh_vien: 0
          tong_quan: 0
        members:
          - character: Mạc Kim Thạch
            position: Hội Trưởng
            cultivation: Trúc Cơ Sơ Kỳ
          - character: "[Phó Hội Giáp]"
            position: Phó Hội — Đàm phán
            cultivation: Luyện Khí Đỉnh Phong
            placeholder: true
          - character: "[Phó Hội Ất]"
            position: Phó Hội — Hậu cần
            cultivation: Luyện Khí Đỉnh Phong
            placeholder: true
      - name: Đội Thợ Mỏ
        role: Khai thác linh thạch và khoáng vật trong hầm mỏ
        headcount:
          hoi_truong: 0
          pho_hoi_truong: 0
          thanh_vien: 480
          tong_quan: 15
        members:
          - character: "[Trưởng Tổ Đào Sâu]"
            position: Tổ Trưởng
            cultivation: Luyện Khí Trung Kỳ
            placeholder: true
      - name: Đội Tự Vệ
        role: Bảo vệ hầm mỏ và thợ mỏ khỏi cướp bóc, tuần tra khu vực khai thác
        headcount:
          hoi_truong: 0
          pho_hoi_truong: 0
          thanh_vien: 50
          tong_quan: 2
        members:
          - character: "[Đội Trưởng Tự Vệ]"
            position: Đội Trưởng
            cultivation: Luyện Khí Hậu Kỳ
            placeholder: true
    relationships:
      - faction: Thiên Sa Thương Hội
        description: Quan hệ căng thẳng và bất đối xứng — thương hội ép giá thu mua linh thạch, Mạc Kim Thạch đàm phán nhưng không đủ sức gây áp lực. Bất mãn ngày càng lớn.
        diplomacy:
          lien_minh: -20
          tin: -30
          uy_hiep: 60
          thuong_mai: 70
          on_oan: -40
          le_thuoc: 50
      - faction: Kim Sa Vi Mạch
        description: Kim Sa Vi Mạch coi thợ mỏ là kẻ thù tự nhiên vì khai thác phá hủy mạch ngầm, nhưng thợ mỏ hoàn toàn không biết sự tồn tại của Vi Tộc này.
        diplomacy:
          lien_minh: 0
          tin: 0
          uy_hiep: 0
          thuong_mai: 0
          on_oan: -50
          le_thuoc: 0
      - faction: Sa Tặc Liên Minh
        description: Sa tặc thỉnh thoảng tấn công đoàn vận chuyển linh thạch từ mỏ về Minh Nguyệt Châu, khiến thợ mỏ phải tổ chức đội tự vệ.
        diplomacy:
          lien_minh: -50
          tin: -60
          uy_hiep: 40
          thuong_mai: -100
          on_oan: -30
          le_thuoc: 0
---

# Kim Sa Thợ Mỏ Hội (金沙矿工会)

## I. Tổng Quan (总览)
Kim Sa Thợ Mỏ Hội là công hội tập hợp khoảng năm trăm thợ mỏ — đa phần là tán tu cấp thấp và phàm nhân — khai thác linh thạch hạ phẩm, sa kim và khoáng vật thường tại khu mỏ phía bắc Minh Nguyệt Châu. Đứng đầu bởi Hội Trưởng Mạc Kim Thạch, một cựu thợ mỏ đạt Trúc Cơ Sơ Kỳ nhờ viên linh thạch may mắn nhặt được trong hầm sập, công hội ra đời từ nhu cầu bức thiết: bảo vệ quyền lợi của thợ mỏ trước sự bóc lột của các tông môn lớn. Với triết lý "Mồ hôi rẻ hơn linh thạch — nhưng không có mồ hôi thì không có linh thạch", Kim Sa Thợ Mỏ Hội đang dần lớn mạnh và thu hút thêm thợ mỏ từ các mỏ khác gia nhập, trở thành tiếng nói hiếm hoi của tầng lớp lao động trong một thế giới tu luyện coi trọng sức mạnh.

## II. Địa Lý & Tài Nguyên (地理与资源)
Khu mỏ chính nằm phía bắc Minh Nguyệt Châu, nơi các mạch linh thạch cấp thấp phân bố dày đặc dưới lớp cát đá. Hầm mỏ đào sâu vào lòng đất, không khí ngột ngạt, nhiệt độ cao, và nguy cơ sập hầm luôn hiện hữu. Tài nguyên khai thác chủ yếu là linh thạch hạ phẩm, sa kim lấp lánh lẫn trong cát, và các loại khoáng vật thường dùng trong xây dựng và rèn pháp khí cấp thấp. Phần lớn sản lượng bị các tông môn lớn — đặc biệt là Thiên Sa Thương Hội — thu mua ép giá, khiến thợ mỏ lao động cực nhọc mà thu nhập chỉ đủ sống qua ngày. Tai nạn sập hầm xảy ra thường xuyên, và trước khi công hội ra đời, thợ mỏ chết không ai bồi thường.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
Văn hóa thợ mỏ mang đậm tính cộng đồng và đoàn kết giai cấp. Trước khi xuống mỏ mỗi ngày, thợ mỏ gõ ba tiếng vào vách đá để "xin phép Thổ Linh" — phong tục truyền đời dù không ai chắc Thổ Linh có thật hay không. Quy tắc quan trọng nhất của hội là tương trợ: thợ mỏ bị thương được hội lo chi phí chữa trị, gia đình thợ mỏ tử nạn được hội nuôi con đến khi trưởng thành. Đây là lý do công hội thu hút ngày càng nhiều thành viên — không phải vì mạnh, mà vì có tình. Tuy nhiên, bất mãn ngày càng lớn với Thiên Sa Thương Hội vì bị ép giá quá đáng đang dần biến từ uất ức thầm lặng thành phẫn nộ công khai.

## IV. Cơ Cấu Tổ Chức (组织结构)
Hội Trưởng Mạc Kim Thạch đứng đầu, bên cạnh hai Phó Hội tương đương Luyện Khí Đỉnh Phong — một phụ trách đàm phán với các tông môn thu mua, một quản lý hậu cần và phân phối vật tư. Dưới ban lãnh đạo là đội thợ mỏ gồm khoảng bốn trăm tám mươi người chia thành các tổ nhỏ, mỗi tổ phụ trách một hầm hoặc khu vực khai thác, có tổ trưởng quản lý. Mười lăm tổng quản phụ trách điều phối giữa các tổ, đảm bảo an toàn và phân chia sản lượng công bằng. Gần đây, Mạc Kim Thạch thành lập thêm Đội Tự Vệ gồm năm mươi thợ mỏ khỏe nhất, trang bị cuốc mỏ và búa gia cố, chuyên bảo vệ đoàn vận chuyển linh thạch khỏi sa tặc và tuần tra khu vực khai thác.

## V. Công Pháp & Trận Pháp (功法与阵法)
Kim Sa Thợ Mỏ Hội không sở hữu công pháp chiến đấu chính thức. Thợ mỏ sử dụng kỹ thuật Thổ hệ sơ đẳng để đào hầm và gia cố vách đá — những kỹ năng học được qua kinh nghiệm chứ không phải truyền thụ bài bản. Trong hầm mỏ có hệ thống bẫy sập đơn giản để phòng kẻ xâm nhập trộm khoáng vật. Gần đây, khi bất mãn với Thiên Sa Thương Hội leo thang và sa tặc ngày càng táo bạo, Đội Tự Vệ bắt đầu luyện tập chiến đấu bằng cuốc mỏ và búa — vũ khí thô sơ nhưng trong tay thợ mỏ khỏe mạnh quen lao động nặng thì cũng đủ gây sát thương đáng kể cho kẻ địch cấp thấp.

## VI. Đặc Sản Môn Phái (门派特产)
- **Linh Thạch Hạ Phẩm:** Sản phẩm khai thác chính, dùng làm đơn vị tiền tệ cơ bản và nguyên liệu tu luyện cấp thấp, được bán số lượng lớn cho Thiên Sa Thương Hội.
- **Sa Kim:** Cát vàng lấp lánh lẫn trong lớp đất mỏ, sau tinh chế trở thành nguyên liệu mạ pháp khí, giá trị không cao nhưng nhu cầu ổn định.
- **Khoáng Vật Xây Dựng:** Đá và khoáng chất cứng dùng trong xây dựng công trình và rèn pháp khí cấp thấp, cung cấp cho thương đoàn và cư dân Minh Nguyệt Châu.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Hầm Mỏ Chính Bắc Minh:** Hệ thống hầm mỏ sâu nhiều tầng, là nơi khai thác linh thạch chính, được gia cố bằng cột gỗ và trận pháp Thổ hệ sơ đẳng.
- **Trụ Sở Công Hội:** Nhà đá lớn tại cửa mỏ, nơi ban lãnh đạo họp mặt, tiếp nhận thành viên mới, và phân phối lương bổng.
- **Khu Trại Thợ Mỏ:** Dãy lều và nhà đá dọc theo khu mỏ, cung cấp chỗ ở cho thợ mỏ và gia đình, có khu chợ nhỏ và trạm y tế sơ cấp.

## VIII. Kinh Tế (经济)
Kinh tế của Kim Sa Thợ Mỏ Hội dựa hoàn toàn vào khai thác khoáng sản. Linh thạch hạ phẩm là mặt hàng chủ lực, nhưng lợi nhuận bị Thiên Sa Thương Hội bóp nghẹt qua cơ chế thu mua ép giá — thương hội mua với giá thấp rồi bán lại cho tông môn với lợi nhuận gấp nhiều lần. Sa kim và khoáng vật thường mang lại thu nhập bổ sung nhưng không đáng kể. Gần đây, hội bắt đầu nhận hợp đồng đào hầm cho các tông môn nhỏ muốn khai thác lãnh thổ riêng, giúp đa dạng hóa nguồn thu và giảm phụ thuộc vào thương hội. Mạc Kim Thạch đang tìm cách bán trực tiếp cho các tông môn nhỏ mà không qua trung gian, nhưng Thiên Sa Thương Hội không dễ dàng cho phép điều đó.

## IX. Lịch Sử Tóm Tắt (简史)
Hàng trăm năm qua, thợ mỏ Tây Mạc bị các tông môn lớn bóc lột tàn nhẫn — lương thấp, điều kiện nguy hiểm, chết không ai chịu trách nhiệm. Mạc Kim Thạch vốn là một thợ mỏ bình thường, suýt chết trong vụ sập hầm nhưng may mắn nhặt được viên linh thạch trung phẩm, nhờ đó đạt Trúc Cơ Sơ Kỳ. Thay vì rời bỏ đời thợ mỏ để theo đuổi tu luyện như nhiều người khác, ông quay lại tập hợp anh em thợ mỏ lập công hội, đàm phán tập thể với các tông môn về giá thu mua và điều kiện an toàn. Kết quả ban đầu khiêm tốn — giá mua tăng chút ít, tai nạn được bồi thường phần nào — nhưng ít nhất thợ mỏ giờ có tổ chức đứng sau lưng. Hội đang dần lớn mạnh, thu hút thợ mỏ từ các mỏ xa hơn, và Thiên Sa Thương Hội bắt đầu cảm thấy lo ngại.

## X. Giai Thoại & Bí Mật (轶事与秘密)
Trong hầm mỏ sâu nhất, thợ mỏ từng đào trúng một không gian rỗng chứa đầy bích họa cổ đại — những hình vẽ mô tả một thành phố nguy nga dưới lòng cát, có thể liên quan đến Lưu Sa Cổ Thành huyền thoại. Mạc Kim Thạch cho niêm phong khu vực và chưa tiết lộ cho ai ngoài ban lãnh đạo. Ông bị Thiên Sa Thương Hội đe dọa nhiều lần — cả ngầm lẫn công khai — nhưng vẫn không khuất phục, và có người đồn rằng ông được một thế lực bí ẩn ngầm bảo vệ, dù không ai biết thế lực đó là ai. Điều mà Mạc Kim Thạch không biết là Kim Sa Vi Mạch — Vi Tộc sống trong mạch vàng ngầm — coi thợ mỏ là kẻ thù tự nhiên phá hủy nhà của chúng, và đang âm thầm di tản khỏi các mạch gần khu mỏ.

## XI. Quan Hệ Thế Lực (势力关系)
- **Thiên Sa Thương Hội:** Quan hệ căng thẳng nhất và quan trọng nhất. Thương hội ép giá thu mua linh thạch, coi công hội là mối phiền phức vì dám đàm phán tập thể. Mạc Kim Thạch bị đe dọa nhiều lần nhưng không lùi bước. Sự phụ thuộc kinh tế vào thương hội là điểm yếu lớn nhất của công hội.
- **Kim Sa Vi Mạch:** Mối thù một chiều mà thợ mỏ hoàn toàn không biết. Vi Mạch coi việc khai thác mỏ là phá hủy nhà của chúng, nhưng không đủ mạnh để phản kháng trực tiếp mà chỉ âm thầm rút đi.
- **Sa Tặc Liên Minh:** Kẻ thù trực tiếp. Sa tặc thường xuyên tấn công đoàn vận chuyển linh thạch từ mỏ về Minh Nguyệt Châu, buộc công hội phải thành lập Đội Tự Vệ và tìm cách thuê hộ vệ.
