---
type: faction
name: Dược Thảo Tinh Linh Viện
hantu: 药草精灵院
faction_type: Học Viện
alignment: 6
race: Tinh Linh Tộc
region: Đông Hoang
founded: 80 năm trước
founder: Thảo Tâm Linh
emblem: Duoc_Thao_Tinh_Linh_Vien.png
specialty: Canh tác linh dược, Mộc hệ dưỡng thảo thuật, Dược liệu chất lượng cao
economy:
- Bán linh dược chất lượng cao tại Trạm Biên
- Cung cấp dược liệu giá ưu đãi cho tổ chức y tế
- Đào tạo kỹ thuật canh tác linh dược
arcs:
  - arc: 1
    status: Phát triển ổn định
    rank: Hạng Năm
    leader: Viện Trưởng Thảo Tâm Linh
    population: 23
    territory:
      - Cụm 5 đảo nổi trên Đầm Lầy Tử Thần
    assets:
      - name: Ruộng Linh Dược 5 Đảo
        type: Tài Nguyên
      - name: Hạt Vạn Linh Hoa
        type: Bảo Vật
      - name: Hệ thống rễ cây linh phòng thủ
        type: Trận Pháp
    stats: [20, 130, 100, 23, 80, 60]
    divisions:
      - name: Ban Canh Tác
        role: Trồng trọt và chăm sóc linh dược trên 5 đảo nổi
        headcount:
          hoi_truong: 1
          pho_hoi_truong: 0
          thanh_vien: 20
          tong_quan: 2
        members:
          - character: Thảo Tâm Linh
            position: Viện Trưởng
            cultivation: Trúc Cơ Viên Mãn
          - character: "[Phó Viện Trưởng]"
            position: Phó Viện Trưởng
            cultivation: Trúc Cơ Trung Kỳ
            placeholder: true
    relationships:
      - faction: Tinh Linh Vương Đình
        description: Thảo Tâm Linh rời Vương Đình tự nguyện, quan hệ không thù địch nhưng xa cách, Vương Đình coi viện là nơi lưu lạc của kẻ lý tưởng.
        diplomacy:
          lien_minh: 0
          tin: 20
          uy_hiep: 10
          thuong_mai: 10
          on_oan: -10
          le_thuoc: 0
      - faction: Hoàng Tuyền Cứu Hộ Đội
        description: Cung cấp dược liệu giải độc và cầm máu cho đội cứu hộ với giá ưu đãi, quan hệ hợp tác thiện chí.
        diplomacy:
          lien_minh: 30
          tin: 50
          uy_hiep: 0
          thuong_mai: 40
          on_oan: 20
          le_thuoc: 0
      - faction: Nam Cương Dược Sư Hội
        description: Đối tác thương mại chính, viện cung cấp linh dược thô cho hội bán lẻ tại Trạm Biên.
        diplomacy:
          lien_minh: 20
          tin: 40
          uy_hiep: 0
          thuong_mai: 60
          on_oan: 10
          le_thuoc: 0
---

# Dược Thảo Tinh Linh Viện (药草精灵院)

## I. Tổng Quan (总览)
Dược Thảo Tinh Linh Viện là một học viện nhỏ bé do nhóm Tinh Linh ly khai thành lập trên cụm đảo nổi giữa Đầm Lầy Tử Thần. Khác với truyền thống bảo thủ của Vương Đình, viện đề cao triết lý phục vụ tất cả chủng tộc thông qua y dược, lấy việc trồng linh dược làm con đường tu luyện. Dù quy mô chỉ vỏn vẹn hai mươi ba thành viên, viện đã xây dựng được uy tín nhất định tại Trạm Biên nhờ chất lượng dược liệu vượt trội so với hàng hoang dã. Viện Trưởng Thảo Tâm Linh, một nữ Tinh Linh Trúc Cơ Viên Mãn, dẫn dắt viện với lòng kiên nhẫn và niềm tin rằng mỗi cây thuốc mọc lên là một mạng người có thể được cứu sống.

## II. Địa Lý & Tài Nguyên (地理与资源)
Viện tọa lạc trên cụm năm đảo nổi giữa mặt Đầm Lầy Tử Thần, vùng đất mà không thế lực nào muốn tranh giành vì nước đầm chứa độc tố chết người. Các đảo được tạo thành bằng rễ cây linh đan xen, nổi trên mặt nước nhờ linh lực mộc hệ của Thảo Tâm Linh duy trì suốt tám mươi năm. Năm đảo nối với nhau bằng cầu dây leo kiên cố, mỗi đảo rộng chừng vài mẫu, phủ đầy ruộng linh dược xanh tốt bất thường giữa cảnh quan đầm lầy hoang tàn xung quanh. Tài nguyên chính là linh dược trồng trọt đạt chất lượng cao hơn hẳn dược liệu hoang dã nhờ sự chăm sóc trực tiếp bằng mộc hệ linh lực của Tinh Linh. Nước đầm lầy sau khi lọc qua hệ thống rễ cây linh biến thành dung dịch dinh dưỡng đặc biệt, nuôi dưỡng linh dược sinh trưởng nhanh và dược tính mạnh hơn.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
Viện theo đuổi triết lý "Chữa lành đất, chữa lành người", tin rằng việc trồng dược liệu chính là một hình thức tu luyện cao quý, mỗi cây thuốc cứu được một mạng người là một bước tiến trên đạo lộ. Quy tắc nghiêm ngặt nhất là tuyệt đối không trồng dược liệu độc có chủ đích sát thương, và phân phối dược liệu ưu tiên cho người cần nhất thay vì kẻ trả giá cao nhất. Mỗi khi thu hoạch, các Tinh Linh sẽ cùng nhau hát "Khúc Cảm Ân" cho cây dược liệu — một phong tục xuất phát từ niềm tin rằng lời ca giúp dược liệu giữ được linh tính lâu hơn sau khi hái. Việc chăm sóc đất đai được coi ngang hàng với việc chăm sóc bản thân, và bất kỳ ai cố ý tàn phá ruộng dược đều bị trục xuất vĩnh viễn khỏi viện.

## IV. Cơ Cấu Tổ Chức (组织结构)
Viện có cơ cấu đơn giản, phù hợp với quy mô nhỏ bé. Đứng đầu là Viện Trưởng Thảo Tâm Linh, nữ Tinh Linh chỉ mới một trăm năm mươi tuổi theo tuổi Tinh Linh, với mái tóc xanh lá và bàn tay luôn dính đất. Bà rời Vương Đình vì muốn dùng phép thuật mộc hệ chữa bệnh cho mọi chủng tộc, không chỉ riêng Tinh Linh. Dưới bà là sáu Dược Sư Tinh Linh cảnh giới Trúc Cơ Sơ đến Trung Kỳ, mỗi người phụ trách một đảo trồng trọt. Tầng kế tiếp là mười hai học đồ Tinh Linh trẻ cùng ba hỗn huyết Tinh Linh cảnh giới Luyện Khí, đang trong giai đoạn học canh tác. Ngoài ra, viện có hai tu sĩ nhân tộc làm thương nhân đối tác, chịu trách nhiệm vận chuyển dược liệu ra Trạm Biên tiêu thụ.

## V. Công Pháp & Trận Pháp (功法与阵法)
Công pháp chính của viện là "Sinh Cơ Dưỡng Thảo Quyết", một công pháp mộc hệ chuyên về nuôi trồng linh dược. Công pháp này giúp người tu luyện kết nối linh lực trực tiếp với đất đai và hạt giống, thúc đẩy sinh trưởng nhanh chóng đồng thời nâng cao chất lượng dược tính. Tuy nhiên, Sinh Cơ Dưỡng Thảo Quyết hoàn toàn không có tác dụng chiến đấu, khiến viện gần như vô phòng bị trước các thế lực tấn công. Hệ thống phòng thủ duy nhất nằm ở lớp rễ cây linh bao bọc phía dưới các đảo nổi. Khi bị đe dọa, rễ cây có thể co lại và kéo toàn bộ đảo di chuyển trên mặt đầm lầy, tận dụng nước độc xung quanh làm rào cản tự nhiên. Chiến thuật "chạy trốn trên đầm lầy" này là phương án phòng thủ duy nhất nhưng đã chứng minh hiệu quả trong vài lần bị sơn tặc nhòm ngó.

## VI. Đặc Sản Môn Phái (门派特产)
- **Linh Dược Tinh Linh Chăm:** Các loại linh dược được Tinh Linh trực tiếp chăm sóc bằng mộc hệ linh lực, dược tính cao hơn ba mươi phần trăm so với hàng hoang dã cùng loại, đặc biệt là các loại dược thảo giải độc và cầm máu.
- **Dung Dịch Rễ Linh:** Nước đầm lầy lọc qua rễ cây linh, có tác dụng bổ trợ dinh dưỡng cho linh dược khi trồng trọt, được một số dược sư bên ngoài thu mua để nghiên cứu.
- **Khúc Cảm Ân Phù:** Phù giấy ghi lại giai điệu Khúc Cảm Ân, khi đốt sẽ tạo ra làn sóng âm thanh mộc hệ giúp bảo quản dược liệu lâu hơn trong quá trình vận chuyển.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Cụm Đảo Nổi Ngũ Linh:** Năm đảo nổi là toàn bộ lãnh thổ của viện, mỗi đảo được thiết kế chuyên trồng một nhóm dược thảo khác nhau tùy theo điều kiện ánh sáng và độ ẩm.
- **Cầu Dây Leo Liên Đảo:** Hệ thống cầu nối giữa các đảo bằng dây leo linh, vừa là đường đi vừa là kênh truyền linh lực giữa các đảo.
- **Kho Bảo Quản Rễ Linh:** Kho dược liệu dưới mặt đảo, được bao bọc bởi rễ cây linh tạo môi trường nhiệt độ và độ ẩm ổn định, giữ dược liệu tươi lâu hơn bình thường.

## VIII. Kinh Tế (经济)
Viện tự cung tự cấp phần lớn nhu cầu thông qua việc trồng trọt, nhưng nguồn thu chính đến từ việc bán linh dược chất lượng cao cho thương nhân tại Trạm Biên. Hai tu sĩ nhân tộc đối tác chịu trách nhiệm vận chuyển và phân phối, thu phí hoa hồng theo tỷ lệ cố định. Viện cũng cung cấp dược liệu giá ưu đãi cho Hoàng Tuyền Cứu Hộ Đội và Nam Cương Dược Sư Hội, đổi lại nhận được sự bảo hộ ngầm từ uy tín của hai tổ chức này. Thu nhập tuy không lớn nhưng đủ để duy trì hoạt động và mua sắm vật tư cần thiết mà viện không tự sản xuất được.

## IX. Lịch Sử Tóm Tắt (简史)
Tám mươi năm trước, Thảo Tâm Linh rời Tinh Linh Vương Đình mang theo một túi hạt giống linh dược quý, trong đó có hạt giống huyền thoại Vạn Linh Hoa. Bà chọn Đầm Lầy Tử Thần làm nơi lập nghiệp vì nơi đây không ai tranh giành, và tự tay tạo ra đảo nổi đầu tiên bằng mộc hệ linh lực. Những thập kỷ tiếp theo, bà dần thu hút các Tinh Linh trẻ có cùng lý tưởng muốn dùng sức mạnh thiên bẩm để phục vụ mọi chủng tộc, kể cả những hỗn huyết bị Vương Đình từ chối. Khi dược liệu của viện bắt đầu xuất hiện tại Trạm Biên với chất lượng vượt trội và giá cả phải chăng, viện dần được biết đến và tôn trọng trong giới dược sư khu vực.

## X. Giai Thoại & Bí Mật (轶事与秘密)
Trong số hạt giống Thảo Tâm Linh mang theo từ Vương Đình có một hạt "Vạn Linh Hoa" — loại linh hoa huyền thoại chỉ nở một lần mỗi ngàn năm, mỗi cánh hoa có khả năng chữa lành một loại bệnh nan y. Hạt giống đã được gieo xuống đảo trung tâm từ ngày đầu lập viện nhưng suốt tám mươi năm vẫn chưa nảy mầm, khiến Thảo Tâm Linh thường xuyên ngồi bên cạnh nó trò chuyện mỗi đêm. Một bí mật ít ai biết là vùng Đầm Lầy Tử Thần dưới các đảo nổi đang dần được rễ cây linh từ từ thanh lọc, nước gần đảo đã bớt độc đáng kể sau nhiều thập kỷ. Nếu quá trình này tiếp tục thêm vài trăm năm, nơi đây sẽ trở thành một ốc đảo sạch giữa đầm lầy chết chóc, và điều đó có thể thu hút sự chú ý không mong muốn từ các thế lực lớn hơn.

## XI. Quan Hệ Thế Lực (势力关系)
- **Tinh Linh Vương Đình:** Thảo Tâm Linh rời Vương Đình tự nguyện, không mang theo thù hận, nhưng Vương Đình coi bà là kẻ lý tưởng viển vông và không công nhận viện. Quan hệ xa cách nhưng không thù địch.
- **Hoàng Tuyền Cứu Hộ Đội:** Đối tác thiện chí, viện cung cấp dược liệu giải độc và cầm máu cho đội cứu hộ với giá ưu đãi, đổi lại đội cứu hộ giúp vận chuyển thông tin và cảnh báo nguy hiểm.
- **Nam Cương Dược Sư Hội:** Đối tác thương mại lớn nhất, viện cung cấp linh dược thô cho hội bán lẻ tại Trạm Biên, quan hệ đôi bên cùng có lợi.
