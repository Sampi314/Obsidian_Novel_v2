---
type: faction
name: Hoang Dã Yêu Liên
hantu: 荒野妖联
faction_type: Liên Minh
alignment: -1
race: Yêu Tộc (đa loài cấp thấp)
region: Đông Hoang
founded: 30 năm trước
founder: Huyền Nha
emblem: Hoang_Da_Yeu_Lien.png
specialty: Trinh sát hoang dã, Quần chiến số đông, Mạng lưới tình báo rìa rừng
economy:
- Săn bắt con mồi nhỏ trong hoang dã
- Trao đổi thông tin tình báo lấy thức ăn
- Thu lượm linh thảo hoang dã cấp thấp
arcs:
  - arc: 1
    status: Hoạt động cảnh giác
    rank: Hạng Năm
    leader: Liên Trưởng Huyền Nha
    population: 300
    territory:
      - Rìa phía tây Rừng Huyết Độc
      - Vùng cỏ dại xen kẽ rừng thưa
    assets:
      - name: Đá Hội
        type: Công Trình
      - name: Mạng lưới tai mắt hoang dã
        type: Tài Nguyên
      - name: Phòng pháp khí cổ đại (chưa khai phá)
        type: Bí Cảnh
    stats: [100, 50, 30, 300, 40, 60]
    divisions:
      - name: Thất Đại Bầy
        role: Bảy bầy yêu tộc hợp thành lực lượng chính của liên minh
        headcount:
          minh_chu: 1
          pho_minh_chu: 0
          truong_lao: 7
          su_gia: 0
          thanh_vien_phai: 292
        members:
          - character: Huyền Nha
            position: Liên Trưởng
            cultivation: Trúc Cơ Trung Kỳ
          - character: "[Đầu Lĩnh Sói]"
            position: Đầu Lĩnh Bầy
            cultivation: Trúc Cơ Sơ Kỳ
            placeholder: true
          - character: "[Đầu Lĩnh Lợn Rừng]"
            position: Đầu Lĩnh Bầy
            cultivation: Luyện Khí Hậu Kỳ
            placeholder: true
          - character: "[Địa Thử Vương]"
            position: Đầu Lĩnh Bầy Chuột
            cultivation: Luyện Khí Trung Kỳ
            placeholder: true
    relationships:
      - faction: Hoang Dã Thợ Săn Bang
        description: Kẻ thù tiềm tàng, thợ săn bang thường nhận hợp đồng săn yêu tộc cấp thấp trong liên minh. Tuy nhiên đôi khi hợp tác khi có mối đe dọa chung.
        diplomacy:
          lien_minh: -10
          tin: -30
          uy_hiep: 40
          thuong_mai: 10
          on_oan: -20
          le_thuoc: 0
      - faction: Vạn Yêu Thành
        description: Vạn Yêu Thành không coi liên minh yêu tộc cấp thấp là đối tượng đáng chú ý, nhưng một số yêu tướng ngầm bảo hộ vùng hoang dã này.
        diplomacy:
          lien_minh: 5
          tin: 10
          uy_hiep: 20
          thuong_mai: 5
          on_oan: 0
          le_thuoc: 10
      - faction: Hỗn Huyết Yêu Đoàn
        description: Cùng cảnh ngộ yêu tộc bị coi thường, đôi khi trao đổi thành viên và hỗ trợ khi bị tấn công.
        diplomacy:
          lien_minh: 25
          tin: 30
          uy_hiep: 0
          thuong_mai: 15
          on_oan: 10
          le_thuoc: 0
---

# Hoang Dã Yêu Liên (荒野妖联)

## I. Tổng Quan (总览)
Hoang Dã Yêu Liên là liên minh của bảy bầy yêu tộc cấp thấp tập hợp tại vùng hoang dã rìa phía tây Rừng Huyết Độc, nơi mà cả nhân tộc lẫn yêu tộc mạnh đều không muốn chiếm vì quá cằn cỗi. Với hơn ba trăm thành viên gồm sói yêu, lợn rừng linh, chuột linh, quạ yêu, thỏ linh, rắn nhỏ linh, và khỉ linh, liên minh ra đời từ bản năng sinh tồn đơn giản nhất: một con sói yếu, nhưng cả bầy sói mạnh. Liên Trưởng Huyền Nha, một quạ yêu già không thể hóa hình nhưng thông minh phi thường, được bầu dẫn dắt liên minh vì sự công bằng và khả năng bay cao quan sát chiến trường mà không thiên vị loài nào.

## II. Địa Lý & Tài Nguyên (地理与资源)
Liên minh cư trú tại vùng đất hoang vu giữa Rừng Huyết Độc và các khu dân cư, nơi không ai muốn chiếm vì quá cằn cỗi. Địa hình gồm đồng cỏ dại xen lẫn bụi gai và đá tảng, vài cây cổ thụ khô héo rải rác, không có kiến trúc cố định. Mỗi bầy chiếm một khu vực theo thói quen và tập tính riêng: bầy sói ở vùng đá cao, bầy chuột đào hang dưới đất, bầy quạ trên ngọn cây, bầy rắn trong bụi gai. Tài nguyên vật chất nghèo nàn — chỉ có con mồi nhỏ đủ ăn nhưng không dư — nhưng tài nguyên lớn nhất là thông tin. Với mắt và tai rải khắp nơi từ trên trời đến dưới đất, liên minh biết mọi chuyện xảy ra ở rìa rừng trước bất kỳ ai khác.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
Triết lý cốt lõi là "Một con sói yếu, cả bầy sói mạnh" — bài học sinh tồn được Huyền Nha truyền đạt cho toàn liên minh. Quy tắc quan trọng nhất là không cắn nhau trong nội bộ liên minh, ngoại trừ tranh chấp lãnh thổ nhỏ được giải quyết theo quy định bằng tỉ thí không giết chóc. Tất cả phải cùng chống kẻ thù chung và chia sẻ thông tin về mối nguy. Mỗi mùa đông, các bầy cử đại diện đến "Đá Hội" — tảng đá lớn nhất vùng — để trao đổi tin tức, giải quyết tranh chấp, và thảo luận chiến lược chung. Đá Hội là nơi linh thiêng duy nhất của liên minh, không ai được phép chiến đấu trong phạm vi mười trượng quanh nó.

## IV. Cơ Cấu Tổ Chức (组织结构)
Đứng đầu là Liên Trưởng Huyền Nha, quạ yêu già đã sống hơn bốn trăm năm — thọ mệnh bất thường cho một quạ yêu Trúc Cơ. Gã không thể hóa hình thành người nhưng bù lại có trí tuệ vượt trội và khả năng bay cao quan sát chiến trường. Dưới gã là bảy Đầu Lĩnh Bầy, đại diện cho bảy loài: sói, lợn rừng, chuột, quạ, thỏ, rắn nhỏ, và khỉ. Cảnh giới của các đầu lĩnh dao động từ Luyện Khí Hậu Kỳ đến Trúc Cơ Sơ Kỳ. Hơn ba trăm thành viên còn lại đa số chưa khai mở linh trí hoàn toàn, chiến đấu bằng bản năng thú hơn là pháp thuật. Quyết định lớn được biểu quyết tại Đá Hội, nhưng trong tình huống khẩn cấp, Huyền Nha có quyền ra lệnh trực tiếp.

## V. Công Pháp & Trận Pháp (功法与阵法)
Liên minh không có bất kỳ công pháp nào. Tất cả chiến đấu bằng bản năng thú thuần túy: nanh, vuốt, nọc, tốc độ, và sức mạnh thể chất. Chiến thuật duy nhất nhưng cực kỳ hiệu quả là "Quần Yêu Chiến" — khi có kẻ thù xâm nhập, cả liên minh huy động từ mọi hướng, dùng số lượng áp đảo để bao vây và tiêu hao. Bầy sói cắn từ hai bên sườn, lợn rừng húc chính diện, chuột chui từ dưới đất lên cắn chân, quạ tấn công từ trên cao, rắn phun nọc từ bụi gai, khỉ ném đá từ cây. Sự phối hợp đa loài này tạo nên áp lực khủng khiếp mà ngay cả tu sĩ Trúc Cơ Hậu Kỳ cũng phải e dè.

## VI. Đặc Sản Môn Phái (门派特产)
- **Tình Báo Hoang Dã:** Sản phẩm giá trị nhất của liên minh không phải vật chất mà là thông tin. Với mạng lưới tai mắt trải khắp rìa rừng từ trên trời đến dưới đất, liên minh nắm bắt mọi biến động nhanh hơn bất kỳ tổ chức nào.
- **Nọc Rắn Linh:** Nọc độc từ bầy rắn nhỏ linh, tuy cấp thấp nhưng có số lượng lớn, được một số dược sư thu mua để bào chế giải độc dược.
- **Lông Quạ Yêu:** Lông vũ của quạ yêu có khả năng hấp thu phong hệ linh lực nhẹ, dùng làm nguyên liệu phù lục cấp thấp.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Đá Hội:** Tảng đá lớn nhất vùng hoang dã, nơi họp mặt liên minh mỗi mùa đông và giải quyết tranh chấp. Đây là công trình duy nhất có ý nghĩa biểu tượng trong liên minh.
- **Hang Bầy:** Mỗi bầy tự xây dựng nơi ở theo tập tính: hang đá cho sói, hang đất cho chuột, tổ cây cho quạ, bụi gai cho rắn. Không có kiến trúc cố định hay phòng thủ nhân tạo.
- **Điểm Canh Gác:** Các vị trí cao do bầy quạ và khỉ luân phiên canh gác, quan sát mọi chuyển động ra vào vùng hoang dã.

## VIII. Kinh Tế (经济)
Kinh tế liên minh ở mức sinh tồn tối thiểu, dựa hoàn toàn vào săn bắt và hái lượm tự nhiên. Con mồi nhỏ trong hoang dã đủ ăn nhưng không bao giờ dư, và trong mùa đông khắc nghiệt, đói kém là mối đe dọa thường trực. Nguồn thu bổ sung duy nhất đến từ việc trao đổi thông tin tình báo — liên minh cung cấp tin tức về biến động rìa rừng cho các nhóm bên ngoài, đổi lại nhận thức ăn hoặc vật liệu cơ bản. Quan hệ trao đổi tạm thời với một số nhóm như Bán Yêu Thôn giúp liên minh vượt qua những thời kỳ khó khăn nhất.

## IX. Lịch Sử Tóm Tắt (简史)
Ba mươi năm trước, Huyền Nha chứng kiến từng bầy yêu tộc nhỏ bị tiêu diệt từng đợt bởi thợ săn nhân tộc và các đợt Trùng Triều tràn ra từ rừng sâu. Gã nhận ra rằng đơn lẻ thì bất kỳ bầy nào cũng sẽ bị xóa sổ, chỉ có liên kết mới có cơ hội sống sót. Gã bay khắp vùng hoang dã, thuyết phục từng đầu lĩnh bầy bỏ qua hiềm khích giữa loài ăn thịt và con mồi để cùng đối mặt với mối nguy chung. Quá trình liên kết mất gần năm năm, nhiều lần suýt đổ vỡ vì bầy sói muốn ăn thịt bầy thỏ, nhưng cuối cùng lời cam kết không cắn nhau đã được giữ vững. Liên minh đã nhiều lần đẩy lùi Hắc Báo Trại khi chúng vào vùng hoang dã cướp bóc, và dần được các thế lực nhỏ xung quanh thừa nhận sự tồn tại.

## X. Giai Thoại & Bí Mật (轶事与秘密)
Huyền Nha thực ra đã sống hơn bốn trăm năm, thọ mệnh bất thường đến khó tin cho một quạ yêu Trúc Cơ Trung Kỳ. Gã nghi ngờ rằng mình đã vô tình nuốt phải một thứ gì đó khi bay qua phế tích Thượng Cổ lúc nhỏ, nhưng không biết đó là gì và không dám kể cho ai. Bí mật lớn nhất nằm ở bầy chuột: con "Địa Thử Vương" — con chuột đào hang sâu nhất vùng — đã vô tình phát hiện một căn phòng cất giấu pháp khí cổ đại dưới lòng đất sâu hàng trăm trượng. Nó không biết đó là gì, chỉ thấy ấm áp nên thường nằm ngủ ở đó. Gần đây, bầy sói phát hiện dấu vết của một linh thú cấp cao đi qua vùng hoang dã — mùi hương lạ khiến cả liên minh bất an, vì bất kỳ sinh vật nào cấp Kim Đan trở lên đi qua đều có thể tiện tay diệt sạch cả liên minh.

## XI. Quan Hệ Thế Lực (势力关系)
- **Hoang Dã Thợ Săn Bang:** Kẻ thù tiềm tàng, thợ săn thường nhận hợp đồng săn yêu tộc cấp thấp trong liên minh. Quan hệ căng thẳng nhưng đôi khi hợp tác trước mối đe dọa lớn hơn.
- **Vạn Yêu Thành:** Thành không coi liên minh là đối tượng đáng chú ý, nhưng một số yêu tướng ngầm bảo hộ vùng hoang dã này vì coi đó là vùng đệm chiến lược.
- **Hỗn Huyết Yêu Đoàn:** Cùng cảnh ngộ yêu tộc bị coi thường, hai bên đôi khi trao đổi thành viên và hỗ trợ nhau khi bị tấn công.
