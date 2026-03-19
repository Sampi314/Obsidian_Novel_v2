---
type: faction
name: Hải Tặc Tàn Dư
hantu: 海贼残余
faction_type: Bộ Lạc
alignment: -5
race: Đa chủng tộc (Nhân tộc, Hải tộc bị trục xuất)
region: Vô Tận Hải
founded: Năm mươi năm trước (sau cuộc thanh trừng nội bộ Hắc Hải)
founder: Châu Thiết
emblem: Doc_Nhan_Kiem.png
specialty: Hải chiến du kích quy mô nhỏ, Buôn lậu, Sinh tồn vùng biển hoang
economy:
- Đánh cá và đổi chác với thương thuyền đi ngang
- Cướp bóc quy mô nhỏ (thuyền đánh cá, thương thuyền lẻ)
- Buôn bán thông tin về tuyến đường biển
arcs:
  - arc: 1
    status: Suy tàn cầm cự
    rank: Hạng Năm
    leader: '"Độc Nhãn" Châu Thiết'
    population: 33
    territory:
      - Đảo Vô Danh (vùng biển nam Vô Tận Hải)
      - Hang động ngầm giấu thuyền
    assets:
      - name: Hang Động Tàng Thuyền
        type: Công Trình
      - name: Mê Vụ Trận (thường xuyên hỏng)
        type: Trận Pháp
      - name: Bản đồ kho báu (chưa giải mã)
        type: Tài Nguyên
    stats: [30, 15, 20, 33, 25, 10]
    divisions:
      - name: Thuyền Đội
        role: Chiến đấu, tuần tra và cướp bóc trên biển
        headcount:
          truong_lao: 1
          chien_binh: 10
          dan_thuong: 22
        members:
          - character: Châu Thiết
            position: Thuyền Trưởng
            cultivation: Kim Đan Sơ Kỳ
            placeholder: false
          - character: "[Lý Hắc Ngư]"
            position: Phó Thuyền Trưởng
            cultivation: Trúc Cơ Hậu Kỳ
            placeholder: true
          - character: "[Trần Sóng]"
            position: Phó Thuyền Trưởng
            cultivation: Trúc Cơ Trung Kỳ
            placeholder: true
    relationships:
      - faction: Hắc Hải Hải Tặc
        description: Mối thù sâu sắc. Châu Thiết bị trục xuất sau cuộc thanh trừng nội bộ, mất một mắt và hàng chục đồng đội. Hắn mơ ngày phục thù nhưng không đủ sức.
        diplomacy:
          lien_minh: -80
          tin: -90
          uy_hiep: 0
          thuong_mai: -100
          on_oan: -95
          le_thuoc: 0
      - faction: Hải Thần Cung
        description: Bị truy nã với mức thưởng thấp. Hải Thần Cung coi nhóm này là mối phiền nhỏ, không đáng để điều quân tiêu diệt.
        diplomacy:
          lien_minh: -60
          tin: -70
          uy_hiep: 10
          thuong_mai: -80
          on_oan: -40
          le_thuoc: 0
      - faction: Phong Bạo Thương Đội
        description: Quan hệ nửa đe dọa nửa cầu xin. Châu Thiết đôi khi bán thông tin tuyến đường biển cho thương đội, đổi lại nhận lương thực và vật tư.
        diplomacy:
          lien_minh: -10
          tin: -20
          uy_hiep: 15
          thuong_mai: 30
          on_oan: -10
          le_thuoc: 0
---

# HẢI TẶC TÀN DƯ (海贼残余)

## I. Tổng Quan (总览)
Hải Tặc Tàn Dư là tàn dư của một phái hệ trong Hắc Hải Hải Tặc, do "Độc Nhãn" Châu Thiết dẫn đầu sau khi bị trục xuất trong cuộc thanh trừng nội bộ năm mươi năm trước. Với vỏn vẹn ba mươi ba người ẩn náu trên một hòn đảo hoang vùng biển nam, đây là một trong những thế lực nhỏ bé và thảm hại nhất Vô Tận Hải. Châu Thiết ở cảnh giới Kim Đan Sơ Kỳ, là tu sĩ mạnh nhất nhóm, nhưng sức mạnh đó không đủ để thực hiện bất kỳ mưu đồ lớn nào. Nhóm sống trong trạng thái nửa hải tặc nửa ngư dân, vừa muốn cướp vừa sợ bị phát hiện, vừa mơ phục thù vừa biết mình bất lực.

## II. Địa Lý & Tài Nguyên (地理 与 资源)
Đảo Vô Danh nằm khuất sau một hệ thống rạn đá ngầm phức tạp ở vùng biển nam Vô Tận Hải, khó tìm nếu không biết đường đi chính xác. Đảo nhỏ, diện tích chỉ bằng vài mẫu ruộng, địa hình đá lởm chởm với thảm thực vật nghèo nàn. Tài nguyên gần như không có — nhóm sống nhờ đánh cá, trộm cắp vặt, và đổi chác với thương thuyền đi ngang. Hang động ngầm phía tây đảo dùng làm nơi giấu thuyền và hàng hóa, lối vào chìm dưới mặt nước khi thủy triều lên. Nước ngọt khan hiếm — giếng đào trên đảo chỉ cho nước lợ, uống vào đỡ khát nhưng lâu dài ảnh hưởng sức khỏe. Mê Vụ Trận bao quanh đảo để che giấu vị trí, nhưng thường xuyên hỏng do thiếu linh thạch duy trì.

## III. Văn Hóa & Tín Ngưỡng (文化 与 信仰)
Thành viên đều là cựu thành viên Hắc Hải Hải Tặc bị trục xuất vì thua trong tranh giành quyền lực nội bộ, cùng một số phàm nhân gia nhập sau này vì không còn nơi nào khác để đi. Nhóm vẫn giữ luật "kẻ mạnh làm chủ" của hải tặc, nhưng trên thực tế Châu Thiết là người mạnh nhất áp đảo, nên luật này chỉ mang tính hình thức. Mơ ước chung là ngày quay lại Hắc Hải phục thù, nhưng sau năm mươi năm, giấc mơ đó đã mờ nhạt thành một câu chuyện kể bên bếp lửa lúc say rượu. Không có tín ngưỡng cụ thể — Châu Thiết chỉ tin vào sức mạnh cá nhân và vận may, dù cả hai đều đã bỏ rơi hắn từ lâu.

## IV. Cơ Cấu Tổ Chức (组织结构)
Châu Thiết nắm quyền tuyệt đối với tư cách Thuyền Trưởng, quyết định mọi việc lớn nhỏ. Hai phó thuyền trưởng là người thân tín nhất, đều ở cảnh giới Trúc Cơ, phụ trách điều hành thủy thủ và canh gác. Khoảng ba mươi thủy thủ còn lại phần lớn là Luyện Khí hoặc phàm nhân, trang bị thô sơ, tinh thần sa sút. Kỷ luật lỏng lẻo — thỉnh thoảng có thủy thủ bỏ trốn vì chán nản hoặc tuyệt vọng, nhưng đa số không biết bơi đủ xa để đến được nơi khác nên đành ở lại. Châu Thiết duy trì quyền lực bằng sự sợ hãi và sự thật rằng không ai trong nhóm có khả năng sống sót một mình giữa đại dương.

## V. Công Pháp & Trận Pháp (功法 与 阵法)
Nhóm sử dụng tàn bản Hắc Thủy Quyết — một công pháp thủy hệ tà đạo đã mất nhiều chương quan trọng khi Châu Thiết bỏ trốn. Vì thiếu các chương trình tu luyện cao cấp, không ai trong nhóm có thể đột phá quá Trúc Cơ, và bản thân Châu Thiết cũng bị kẹt ở Kim Đan Sơ Kỳ suốt mấy chục năm không tiến bộ. Trận pháp Mê Vụ Trận quanh đảo có tác dụng tạo sương mù che giấu vị trí, nhưng cần linh thạch duy trì liên tục — khi linh thạch cạn, sương tan và đảo lộ ra giữa biển khơi. Châu Thiết còn giữ một số chiêu thức cận chiến từ thời hải tặc, bao gồm Hắc Thủy Đao Pháp — một bộ đao pháp hung tàn nhưng đã lỗi thời so với các công pháp hiện đại.

## VI. Đặc Sản Môn Phái (门派特产)
- **Hắc Thủy Tửu:** Rượu ủ từ tảo biển lên men và nước biển lọc, vị mặn chát khó uống nhưng có tác dụng giữ ấm cơ thể trong vùng biển lạnh. Thủy thủ trong nhóm coi đây là niềm an ủi duy nhất.
- **Bản Đồ Ám Tiêu:** Châu Thiết vẽ bản đồ chi tiết các rạn đá ngầm và dòng hải lưu nguy hiểm ở vùng biển nam, bán cho thương thuyền đi ngang để đổi lấy vật tư. Độ chính xác cao vì dựa trên năm mươi năm kinh nghiệm.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Hang Động Tàng Thuyền:** Hang động tự nhiên phía tây đảo, đủ rộng để giấu ba chiếc thuyền nhỏ. Lối vào chìm dưới mặt nước khi thủy triều lên, là nơi cất giấu hàng hóa cướp được và vật tư dự trữ.
- **Trại Lều Trên Đảo:** Khu lều tạm bợ dựng bằng gỗ trôi dạt và vải buồm cũ, nơi thủy thủ nghỉ ngơi. Không có kiến trúc kiên cố nào, phản ánh tình trạng bấp bênh của nhóm.
- **Giếng Nước Lợ:** Giếng đào duy nhất trên đảo, nước có vị mặn nhưng vẫn uống được. Là nguồn nước ngọt quý giá nhất và cũng là lý do chính khiến nhóm không dời đảo.

## VIII. Kinh Tế (经济)
Kinh tế của Hải Tặc Tàn Dư nằm ở mức sinh tồn tối thiểu. Thu nhập chính đến từ việc đánh cá hàng ngày, đổi chác với thương thuyền đi ngang qua (bán cá tươi, bản đồ ám tiêu), và thỉnh thoảng cướp bóc những thuyền đánh cá nhỏ yếu thế. Châu Thiết muốn tổ chức các vụ cướp lớn hơn nhưng thiếu nhân lực, trang bị, và quan trọng nhất là thiếu can đảm — mỗi lần thất bại đều khiến nhóm mất thêm người. Quan hệ với thương thuyền mang tính nửa đe dọa nửa cầu xin — vừa muốn cướp vừa sợ bị tố giác cho Hải Thần Cung.

## IX. Lịch Sử Tóm Tắt (简史)
Năm mươi năm trước, Châu Thiết là thuyền phó dưới trướng một trong Thất Đại Hải Tặc Vương của Hắc Hải Hải Tặc. Khi cuộc thanh trừng nội bộ nổ ra nhằm tranh giành vị trí Hải Tặc Vương, Châu Thiết đứng sai phe và bị truy sát. Hắn mất một mắt trong trận chiến đó — vết thương không bao giờ lành vì bị tà khí từ Hắc Thủy Quyết xâm nhập vĩnh viễn. Dẫn theo vài chục người trung thành, hắn chạy trốn suốt nhiều tháng trên biển trước khi tìm được Đảo Vô Danh và định cư. Trong năm mươi năm qua, Châu Thiết nhiều lần toan tính lớn nhưng đều thất bại vì thiếu nhân lực và tài nguyên. Số thành viên dần giảm do bỏ trốn, bệnh tật và tuổi già, trong khi rất ít người mới gia nhập.

## X. Giai Thoại & Bí Mật (轶事 与 秘密)
Châu Thiết giấu kín một tấm bản đồ kho báu cướp được từ phòng riêng của Hải Tặc Vương trước khi bỏ trốn. Bản đồ chỉ đến một hòn đảo nằm sâu trong vùng biển cấm, nơi tương truyền chôn giấu pháp bảo và linh thạch từ thời cổ đại — nhưng Châu Thiết không đủ sức vượt qua hải vực nguy hiểm để đến đó. Trong hang động giấu thuyền có một cánh cửa đá cổ đại không ai mở được, bề mặt khắc hoa văn kỳ lạ không thuộc bất kỳ nền văn minh nào đã biết — có thể dẫn đến một di tích tiền cổ bị lãng quên. Vết thương mắt của Châu Thiết ngày càng lan rộng, tà khí đang dần xâm thực thần thức — hắn biết mình không còn nhiều năm, và nỗi ám ảnh phục thù đang biến thành sự tuyệt vọng thầm lặng.

## XI. Quan Hệ Thế Lực (势力关系)
Hải Tặc Tàn Dư bị cô lập gần như hoàn toàn trên chính trường Vô Tận Hải. Hắc Hải Hải Tặc coi nhóm này là phản bội đáng chết, sẽ giết ngay nếu gặp. Hải Thần Cung liệt nhóm vào danh sách truy nã nhưng với mức thưởng thấp đến nhục nhã, phản ánh sự coi thường tuyệt đối. Mối quan hệ duy nhất mang tính tích cực là với các thương thuyền nhỏ đi ngang, đặc biệt là Phong Bạo Thương Đội — nơi Châu Thiết đổi thông tin tuyến đường lấy lương thực, dù cả hai bên đều không tin tưởng nhau.
