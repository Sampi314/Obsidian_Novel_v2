---
type: faction
name: San Hô Thủ Hộ Đoàn
hantu: 珊瑚守护团
faction_type: Hội
alignment: 5
race: Hải Tộc (Tiểu hải linh)
region: Tây Mạc
founded: Khoảng 50 năm trước khi truyện bắt đầu
founder: Thủy Linh Nhi
emblem: Ran_San_Ho_Phat_Sang.png
specialty: San Hô Cộng Minh Thuật, Bảo vệ hệ sinh thái rạn san hô, Giám sát ô nhiễm biển
economy:
- Không có hoạt động kinh tế — tồn tại hoàn toàn dựa vào hệ sinh thái tự nhiên
- Trao đổi thông tin sinh thái với các thế lực biển nhỏ
arcs:
  - arc: 1
    status: Đang chống chọi ô nhiễm Huyết Độc từ Nam Cương
    rank: Hạng Năm
    leader: Đoàn Trưởng Thủy Linh Nhi
    population: 30
    territory:
      - Rạn San Hô Đại Bích (vùng biển nam gần Nam Cương)
    assets:
      - name: Lõi San Hô Cổ Đại
        type: Tài Nguyên
      - name: Mạng lưới cảm ứng san hô linh
        type: Trận Pháp
    stats: [15, 10, 20, 30, 30, 15]
    divisions:
      - name: Ban Tuần Tra
        role: Tuần tra bảo vệ rạn san hô, xua đuổi kẻ phá hoại
        headcount:
          hoi_truong: 1
          pho_hoi_truong: 0
          thanh_vien: 20
          tong_quan: 0
        members:
          - character: Thủy Linh Nhi
            position: Đoàn Trưởng
            cultivation: Trúc Cơ Viên Mãn (tương đương)
          - character: "[Tuần Tra Viên]"
            position: Tuần Tra
            cultivation: Luyện Khí
            placeholder: true
      - name: Ban Trinh Sát
        role: Do thám vùng biển xung quanh, phát hiện sớm mối đe dọa
        headcount:
          hoi_truong: 0
          pho_hoi_truong: 0
          thanh_vien: 10
          tong_quan: 0
        members:
          - character: "[Cá Linh Trinh Sát]"
            position: Trinh Sát
            cultivation: Luyện Khí Sơ Kỳ
            placeholder: true
    relationships:
      - faction: San Hô Vi Trùng
        description: Tôn trọng như tổ tiên — Vi Trùng xây dựng san hô, Thủ Hộ Đoàn bảo vệ san hô. Dù hai bên không thể giao tiếp trực tiếp.
        diplomacy:
          lien_minh: 50
          tin: 30
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 0
      - faction: San Hô Thợ Lặn Đội
        description: Quan hệ hữu hảo, Thợ Lặn Đội tuân thủ quy tắc khai thác bền vững, hai bên trao đổi thông tin về tình trạng rạn san hô.
        diplomacy:
          lien_minh: 20
          tin: 40
          uy_hiep: 0
          thuong_mai: 10
          on_oan: 0
          le_thuoc: 0
      - faction: Hải Thần Cung
        description: Từng cầu cứu nhưng bị bỏ mặc. Hải Thần Cung coi rạn san hô nhỏ không đáng quan tâm, khiến Thủy Linh Nhi vô cùng thất vọng.
        diplomacy:
          lien_minh: -20
          tin: -30
          uy_hiep: 0
          thuong_mai: 0
          on_oan: -20
          le_thuoc: 0
---

# San Hô Thủ Hộ Đoàn (珊瑚守护团)

## I. Tổng Quan (总览)
San Hô Thủ Hộ Đoàn là một tổ chức nhỏ bé gồm các Hải Tộc siêu nhỏ tự nguyện tập hợp lại để bảo vệ Rạn San Hô Đại Bích, một trong những rạn san hô linh lớn nhất vùng biển nam Vô Tận Hải. Dưới sự lãnh đạo của Đoàn Trưởng Thủy Linh Nhi, một Mỹ Nhân Ngư nhỏ bé nhưng kiên cường, đoàn gánh vác trọng trách bảo vệ nền tảng sinh thái của toàn bộ vùng biển nam. Dù không có sức mạnh chiến đấu đáng kể, đoàn vẫn kiên trì canh giữ rạn san hô trước nạn khai thác bừa bãi và gần đây là mối đe dọa chết người từ ô nhiễm Huyết Độc lan ra từ Nam Cương.

## II. Địa Lý & Tài Nguyên (地理与资源)
Rạn San Hô Đại Bích trải dài hàng chục dặm dưới vùng biển nam, gần ranh giới với Nam Cương. Đây là một trong những rạn san hô linh lớn nhất khu vực, đóng vai trò nền tảng sinh thái cho toàn bộ sinh vật biển vùng nam. San hô linh tại đây tuy không có giá trị khai thác lớn đối với các thế lực hùng mạnh, nhưng lại là nguồn sống của vô số loài sinh vật nhỏ. Vùng biển giàu đa dạng sinh học nhưng nghèo linh thạch, khiến các tông môn lớn không thèm để mắt. Gần đây, nước biển vùng nam bắt đầu chuyển sang màu đỏ nhạt đáng lo ngại do ô nhiễm Huyết Độc từ Nam Cương lan ra, đe dọa sự sống của toàn bộ rạn san hô.
Khu vực xung quanh ẩn chứa nhiều bí mật chưa được khám phá — hang động chưa ai đến, mạch khoáng chưa ai biết, dấu tích cổ đại mà thời gian chưa kịp xóa nhòa.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
Thành viên đoàn là các Hải Tộc nhỏ bé gồm cá linh, tôm linh, sò linh và các sinh vật biển có linh trí thấp, cùng tập hợp lại vì một mục đích chung: bảo vệ rạn san hô. Họ tin rằng san hô linh có một linh hồn chung, kết nối mọi cành san hô trong rạn thành một thực thể sống. Nếu rạn san hô bị phá hủy hoàn toàn, linh hồn chung đó sẽ trỗi dậy và nguyền rủa kẻ gây ra. Niềm tin này tuy mang tính truyền thuyết nhưng là sợi dây tinh thần gắn kết các thành viên đa chủng tộc trong đoàn. Phương châm hành động là dùng số đông và tiếng kêu cứu để xua đuổi kẻ phá hoại, bởi đoàn hoàn toàn không có khả năng chiến đấu trực diện.
Mỗi thế hệ mới được truyền dạy không chỉ kỹ năng sinh tồn mà cả câu chuyện về nguồn cội, để ngọn lửa ký ức không bao giờ tắt dù hoàn cảnh khắc nghiệt đến đâu.

## IV. Cơ Cấu Tổ Chức (组织结构)
Đoàn Trưởng Thủy Linh Nhi đứng đầu tổ chức, là Mỹ Nhân Ngư nhỏ nhất từng lãnh đạo một đoàn trong lịch sử Hải Tộc vùng biển nam. Dưới cô là hai mươi tuần tra viên, đều là Hải Tộc nhỏ ở cảnh giới Luyện Khí, phụ trách canh gác các khu vực khác nhau của rạn san hô. Mười con cá linh nhanh nhẹn đảm nhiệm vai trò trinh sát, chuyên do thám vùng biển xung quanh để phát hiện sớm mối đe dọa. Đoàn hợp tác chặt chẽ với Hải Khuẩn Tịnh Hóa Đội trong nỗ lực chống ô nhiễm, nhưng cả hai tổ chức đều quá yếu để tạo ra thay đổi thực sự. Cơ cấu tổ chức linh hoạt, không có hệ thống cấp bậc cứng nhắc, mọi thành viên đều có tiếng nói.

## V. Công Pháp & Trận Pháp (功法与阵法)
Công pháp cốt lõi của đoàn là San Hô Cộng Minh Thuật, cho phép Thủy Linh Nhi kết nối ý thức với san hô linh trong rạn để cảm nhận mọi biến động, từ sự xâm nhập của sinh vật lạ đến sự thay đổi dòng chảy bất thường. Khi bị tấn công, san hô linh có thể phản ứng bằng cách phóng gai nhỏ về phía kẻ xâm nhập, gây đau rát nhưng không đủ sức gây thương tích nghiêm trọng cho tu sĩ có tu vi cao. Chiến thuật phòng thủ chính của đoàn là "vây quanh kêu cứu", tức huy động toàn bộ thành viên bao quanh kẻ thù và phát ra tiếng kêu liên tục với hy vọng thu hút sự chú ý của sinh vật biển lớn hơn đến giúp đỡ.

## VI. Đặc Sản Môn Phái (门派特产)
Đoàn không sản xuất hay buôn bán bất kỳ sản phẩm nào, bởi mục đích duy nhất là bảo tồn chứ không phải khai thác. Tuy nhiên, trong quá trình tuần tra, đoàn thu thập được lượng lớn kiến thức về hệ sinh thái rạn san hô, bao gồm vị trí của các loài sinh vật quý hiếm, chu kỳ sinh sản của san hô linh, và sự biến đổi của dòng hải lưu theo mùa. Những kiến thức này tuy không có giá trị thương mại trực tiếp nhưng vô cùng quý giá cho bất kỳ ai muốn nghiên cứu hay bảo tồn biển.
Ngoài ra, San Hô Thủ Hộ Đoàn còn sở hữu vật phẩm có giá trị văn hóa hơn vật chất — thứ mà thương nhân bỏ qua nhưng nhà sử học trả bất cứ giá nào.

## VII. Cơ Sở Hạ Tầng (基础设施)
Đoàn không có cơ sở hạ tầng nhân tạo nào. Trụ sở là một hang san hô tự nhiên lớn nằm ở trung tâm Rạn San Hô Đại Bích, nơi Thủy Linh Nhi và các tuần tra viên tụ họp để trao đổi thông tin. Các trinh sát viên nghỉ ngơi trong những hốc san hô rải rác khắp rạn, tạo thành mạng lưới trạm gác tự nhiên. Hệ thống "cảnh báo" duy nhất là mạng lưới cộng minh với san hô linh do Thủy Linh Nhi duy trì, cho phép cảm nhận mọi xáo trộn trong toàn bộ rạn san hô.
Toàn bộ hạ tầng mang dấu ấn đặc trưng cộng đồng — không phải xa hoa mà là thực dụng đúc kết qua nhiều thế hệ thử nghiệm.

## VIII. Kinh Tế (经济)
San Hô Thủ Hộ Đoàn không có hoạt động kinh tế nào. Thành viên sống dựa hoàn toàn vào hệ sinh thái tự nhiên của rạn san hô, ăn rong biển và sinh vật nhỏ. Đoàn tồn tại bằng tinh thần tự nguyện, không có lương bổng hay phần thưởng vật chất. Điều này vừa là điểm yếu vừa là điểm mạnh, bởi không ai có thể dùng tiền bạc để mua chuộc hay uy hiếp đoàn, nhưng đồng thời đoàn cũng không có nguồn lực để phát triển hay trang bị vũ khí phòng thân.
Tiềm năng kinh tế vượt xa những gì đang được khai thác — sự thiếu hụt nhân lực, kiến thức thương mại, và bảo hộ chính trị khiến phần lớn giá trị vẫn nằm yên.

## IX. Lịch Sử Tóm Tắt (简史)
San Hô Thủ Hộ Đoàn được Thủy Linh Nhi thành lập sau một sự kiện đau lòng: một nhóm tu sĩ nhân tộc đến khai thác san hô linh bừa bãi, phá hủy cả một khu vực rạn san hô rộng lớn chỉ trong vài ngày. Chứng kiến cảnh tàn phá, Thủy Linh Nhi quyết tâm tập hợp các Hải Tộc nhỏ để bảo vệ những gì còn lại. Cô từng cầu cứu Hải Thần Cung nhưng bị bỏ mặc với lý do "rạn san hô nhỏ không đáng để quan tâm". Sự thờ ơ đó khiến Thủy Linh Nhi hiểu rằng không ai sẽ đến cứu nếu họ không tự cứu mình. Các Hải Tộc lớn trong vùng cười nhạo một Mỹ Nhân Ngư nhỏ bé dám lãnh đạo cả đoàn, nhưng Thủy Linh Nhi không nản chí. Gần đây, mối đe dọa mới từ ô nhiễm Huyết Độc Nam Cương lan ra biển đang khiến đoàn đối mặt với thử thách lớn nhất từ khi thành lập.
Mỗi thế hệ kế tiếp gánh di sản và gánh nặng thế hệ trước — nhưng cũng mang khả năng mới mà cha ông chưa từng tưởng tượng.

## X. Giai Thoại & Bí Mật (轶事与秘密)
Sâu bên dưới Rạn San Hô Đại Bích, ẩn giấu một lõi san hô cổ đại khổng lồ, tồn tại từ hàng triệu năm trước. Nếu lõi này bị phá hủy, cả vùng biển nam sẽ mất cân bằng sinh thái nghiêm trọng, sóng biển dâng cao và sinh vật chết hàng loạt. Thủy Linh Nhi gần đây phát hiện một hiện tượng kỳ lạ: san hô linh trong rạn đang chậm rãi hấp thu Huyết Độc từ nước biển và biến đổi cấu trúc, một số cành san hô chuyển từ màu xanh lam sang đỏ thẫm. Cô không rõ hậu quả của sự biến đổi này là gì, liệu san hô đang tự cứu mình hay đang bị tha hóa thành thứ gì đó nguy hiểm hơn.
Những bí mật này, nếu được tiết lộ, có thể khiến nhiều thế lực phải nhìn lại đánh giá của mình về cộng đồng nhỏ bé này — vừa là cơ hội vừa là mối nguy.

## XI. Quan Hệ Thế Lực (势力关系)
- **San Hô Vi Trùng:** Tôn trọng sâu sắc, coi Vi Trùng như những thợ xây vĩ đại tạo nên nền tảng sinh thái. Dù hai bên không thể giao tiếp, Thủ Hộ Đoàn luôn bảo vệ Vi Trùng một cách vô điều kiện.
- **San Hô Thợ Lặn Đội:** Quan hệ hữu hảo, Thủy Linh Nhi đánh giá cao việc Thợ Lặn Đội tuân thủ quy tắc khai thác bền vững, đôi khi trao đổi thông tin với Nguyễn Thủy Tiên.
- **Hải Thần Cung:** Thất vọng và oán giận, từng bị bỏ mặc khi cầu cứu. Thủy Linh Nhi không còn tin tưởng vào sự bảo hộ của Hải Thần Cung.
Nhìn tổng thể, mạng lưới quan hệ tuy mỏng manh nhưng đủ duy trì sự tồn tại — trong thế giới tu chân tàn khốc, tồn tại đã là chiến thắng.
