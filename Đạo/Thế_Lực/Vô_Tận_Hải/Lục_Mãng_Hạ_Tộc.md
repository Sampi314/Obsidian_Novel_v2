---
type: faction
name: Lục Mãng Hạ Tộc
hantu: 绿蟒下族
faction_type: Bộ Lạc
alignment: -2
race: Yêu Tộc (Xà Yêu)
region: Vô Tận Hải
founded: 300 năm trước
founder: Lục Mãng Vương (bắt buộc thần phục)
emblem: Vay_Ran_Luc.png
specialty: Trinh sát rung động mặt đất, Nọc xà chiến đấu, Mãng Trận hợp kích
economy:
- Cống nạp nọc xà cho Lục Mãng Vương
- Bán da rắn lột cho dược sư và thợ may
- Dịch vụ trinh sát cho các thế lực lân cận (bí mật)
arcs:
  - arc: 1
    status: Nô dịch — kiệt sức
    rank: Hạng Năm
    leader: Tộc Trưởng Thanh Lân
    population: 90
    territory:
      - Rừng rậm biên giới phía đông Núi Độc Long
    assets:
      - name: Hang Gốc Cây Cổ Thụ
        type: Công Trình
      - name: Nguồn Nọc Xà Tự Nhiên
        type: Tài Nguyên
    stats: [50, 25, 15, 90, 40, 20]
    divisions:
      - name: Xà Chiến Đội
        role: Tuần tra lãnh thổ, chiến đấu khi được triệu tập, và trinh sát cho Lục Mãng Vương
        headcount:
          truong_lao: 1
          chien_binh: 20
          dan_thuong: 69
        members:
          - character: Thanh Lân
            position: Tộc Trưởng
            cultivation: Trúc Cơ Hậu Kỳ
            placeholder: false
          - character: Hắc Vĩ
            position: Phó Tộc Trưởng
            cultivation: Trúc Cơ Sơ Kỳ
            placeholder: false
          - character: "[Bạch Xà Đột Biến]"
            position: Ấu Sinh
            cultivation: Chưa hóa hình
            placeholder: true
    relationships:
      - faction: Lục Mãng Vương
        description: Phục tùng tuyệt đối theo luật huyết mạch. Hạ Tộc phải cung cấp nọc xà, da rắn và trinh sát viên theo yêu cầu, đổi lại được bảo hộ lãnh thổ.
        diplomacy:
          lien_minh: -5
          tin: -50
          uy_hiep: 90
          thuong_mai: -40
          on_oan: -60
          le_thuoc: 90
      - faction: Linh Hồ Tàn Tộc
        description: Biết sự tồn tại của Hồ Tộc gần Núi Độc Long nhờ khả năng trinh sát. Giữ khoảng cách nhưng không thù địch, đôi khi trao đổi tin tức ngầm.
        diplomacy:
          lien_minh: 10
          tin: 15
          uy_hiep: 0
          thuong_mai: 5
          on_oan: 0
          le_thuoc: 0
      - faction: Huyết Hổ Hạ Chúng
        description: Cùng cảnh ngộ yêu tộc cấp thấp bị áp bức bởi chúa tể mạnh hơn. Thanh Lân đồng cảm nhưng chưa dám liên lạc chính thức.
        diplomacy:
          lien_minh: 5
          tin: 5
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 0
---

# Lục Mãng Hạ Tộc (绿蟒下族)

## I. Tổng Quan (总览)
Lục Mãng Hạ Tộc là bộ lạc xà yêu cấp thấp sống dưới quyền cai quản của Lục Mãng Vương — một Xà Yêu cảnh giới Nguyên Anh thống trị vùng Núi Độc Long. Với khoảng chín mươi thành viên gồm xà yêu đã hóa hình, chiến sĩ Luyện Khí và xà non, Hạ Tộc do Tộc Trưởng Thanh Lân (Trúc Cơ Hậu Kỳ) dẫn dắt. Đây là thế lực Hạng Năm, tồn tại chủ yếu nhờ giá trị trinh sát và cung cấp nọc xà cho Lục Mãng Vương. Thanh Lân là kẻ trung thành bề ngoài nhưng trong lòng lo lắng cho vận mệnh tộc nhân đang dần kiệt sức.

## II. Địa Lý & Tài Nguyên (地理 与 资源)
Hạ Tộc cư ngụ trong rừng rậm ẩm ướt ở biên giới phía đông dãy Núi Độc Long, vùng đất nóng ẩm lý tưởng cho xà tộc. Địa hình gồm rừng cây thấp dày đặc, đầm nước nông rải rác, và đất mềm lầy lội — môi trường tự nhiên giúp xà yêu di chuyển nhanh và ẩn nấp dễ dàng. Xà yêu đào hang dưới gốc cây cổ thụ để ở, mỗi hang là một gia đình, nối với nhau bằng đường hầm ngầm. Tài nguyên chính gồm da rắn lột — nguyên liệu luyện khí và may áo giáp cấp thấp — và nọc xà, bán được cho dược sư với giá ổn định dù không cao. Đặc biệt, xà yêu có khả năng cảm nhận rung động mặt đất cực nhạy, biết kẻ lạ đến từ hàng dặm xa — kỹ năng trinh sát bẩm sinh quý giá.

## III. Văn Hóa & Tín Ngưỡng (文化 与 信仰)
Triết lý sống của Hạ Tộc là "Phục tùng là sống, phản kháng là diệt" — luật sắt do Lục Mãng Vương ban hành. Lệnh của Lục Mãng Vương là tối thượng, không ai được đặt câu hỏi. Mỗi mùa xuân, Hạ Tộc phải cống nạp da rắn đẹp nhất và một phần nọc xà; không xà yêu nào được rời lãnh thổ mà không có phép. Dù bị áp bức, Hạ Tộc vẫn giữ được phong tục tổ tiên: mỗi đêm trăng non, cả tộc cùng lột da — xà yêu coi đó là nghi lễ tái sinh, biểu tượng của sự kiên nhẫn và khả năng thay đổi. Thanh Lân thầm dạy xà non rằng lột da không chỉ là bản năng, mà là lời nhắc nhở rằng một ngày nào đó, tộc nhân sẽ thoát khỏi lớp vỏ nô lệ.

## IV. Cơ Cấu Tổ Chức (组织结构)
Tộc Trưởng Thanh Lân đứng đầu, hình dáng nguyên hình là mãng xà xanh dài năm trượng, hóa nhân thành thanh niên da ngăm trầm lặng. Thanh Lân trung thành với Lục Mãng Vương trên bề mặt nhưng thầm lo lắng cho tộc nhân. Phó Tộc Trưởng Hắc Vĩ (Trúc Cơ Sơ Kỳ) là một rắn đen hung tợn, phụ trách kỷ luật và hình phạt — trung thành thực sự với Lục Mãng Vương hơn là với Thanh Lân. Hai mươi chiến sĩ Luyện Khí đảm nhiệm tuần tra và chiến đấu khi được triệu tập. Hơn sáu mươi xà yêu cấp thấp gồm cả xà non sinh sống và sản xuất nọc xà. Mâu thuẫn ngầm giữa Thanh Lân và Hắc Vĩ là bất ổn tiềm tàng của bộ lạc.

## V. Công Pháp & Trận Pháp (功法 与 阵法)
Công pháp chính là "Thanh Mãng Thôn Thiên Quyết" — phiên bản giản lược do Lục Mãng Vương ban cho, giới hạn tu vi tối đa Trúc Cơ Viên Mãn. Muốn đột phá Kim Đan phải đến xin phép Lục Mãng Vương — một cách kiểm soát tinh vi để Hạ Tộc mãi không thể vượt qua chủ nhân. Ngoài ra, Hạ Tộc sở hữu "Mãng Trận" — chiến thuật phối hợp mười xà yêu kết thành vòng tròn siết, tạo lực ép đủ nghiền nát tu sĩ Trúc Cơ. Đây là trận pháp chiến đấu duy nhất, đơn giản nhưng hiệu quả trong phạm vi hẹp, phản ánh bản năng hợp kích của loài rắn.

## VI. Đặc Sản Môn Phái (门派特产)
Da rắn lột là sản phẩm đặc trưng, có độ dai và chịu nhiệt tốt, được dược sư và thợ may cấp thấp ưa chuộng để luyện bọc pháp khí hoặc may áo giáp nội giáp. Nọc xà Lục Mãng cũng là nguyên liệu đan dược có nhu cầu ổn định, dùng trong các loại thuốc giải độc nghịch (lấy độc trị độc) và thuốc tê liệt thần kinh. Tuy nhiên, phần lớn sản phẩm chất lượng cao phải cống nạp, chỉ những thứ hạng thấp nhất mới được giữ lại để trao đổi.

## VII. Cơ Sở Hạ Tầng (基础设施)
Hệ thống hang dưới gốc cây cổ thụ tạo thành mạng lưới liên hoàn, nối bằng đường hầm đất ẩm. Hang lớn nhất của Tộc Trưởng có thể chứa toàn bộ chiến sĩ khi họp bàn. Khu đầm nước nông phía nam dùng làm nơi thu thập nọc xà và lột da theo mùa. Một hang bí mật sâu nhất — nơi Thanh Lân giấu con bạch xà đột biến — được che phủ bằng đất đá và mùi thảo mộc để đánh lừa bất kỳ kẻ nào đến gần.

## VIII. Kinh Tế (经济)
Kinh tế mang tính cống nạp bắt buộc, gần như toàn bộ sản lượng nọc xà và da rắn chất lượng cao phải nộp cho Lục Mãng Vương mỗi mùa xuân. Phần giữ lại chỉ đủ cho Hạ Tộc trao đổi nhu yếu phẩm cơ bản với thương nhân qua đường. Gần đây, Lục Mãng Vương yêu cầu tăng lượng cống nạp nọc xà, khiến tộc nhân phải ép xuất nọc nhiều hơn mức an toàn — một số xà yêu già bắt đầu suy kiệt. Thanh Lân lo lắng rằng nếu tình hình tiếp tục, tộc nhân sẽ chết vì kiệt sức trước khi có cơ hội thoát thân.

## IX. Lịch Sử Tóm Tắt (简史)
Lục Mãng Hạ Tộc tồn tại hơn ba trăm năm, kể từ khi Lục Mãng Vương chinh phục vùng Núi Độc Long và bắt buộc các xà yêu hoang dã trong khu vực phải thần phục. Hạ Tộc nhiều lần bị đẩy ra tiền tuyến trong các cuộc xung đột lãnh thổ giữa Lục Mãng Vương và các yêu tộc lân cận — tổn thất nặng nề nhưng không ai dám phản đối. Ba mươi năm trước, một tộc trưởng đời trước từng thử phản kháng và bị Lục Mãng Vương nuốt sống trước mặt toàn tộc — bài học đẫm máu đó khắc sâu vào ký ức mọi thành viên hiện tại.

## X. Giai Thoại & Bí Mật (轶事 与 秘密)
Thanh Lân thầm nuôi ý định tìm một công pháp khác để tộc nhân không còn phụ thuộc vào "Thanh Mãng Thôn Thiên Quyết" của Lục Mãng Vương, nhưng chưa tìm được và không dám để lộ. Bí mật nguy hiểm nhất nằm trong hang sâu nhất: một con bạch xà đột biến với huyết mạch thuần khiết đến mức có thể tiến hóa thành Giao Long nếu đủ cơ duyên. Thanh Lân giấu nó vì biết rằng nếu Lục Mãng Vương phát hiện, hoặc sẽ nuốt huyết mạch để tăng cường bản thân, hoặc gả con gái cho nó để kiểm soát. Cả hai kết cục đều là thảm họa cho Hạ Tộc.

## XI. Quan Hệ Thế Lực (势力关系)
- **Lục Mãng Vương:** Chủ nhân tuyệt đối, quan hệ áp chế bằng sức mạnh và công pháp bị giới hạn. Hạ Tộc phục tùng vì không có lựa chọn khác, nhưng gánh nặng cống nạp ngày càng đè nặng.
- **Linh Hồ Tàn Tộc:** Biết sự tồn tại của nhau nhờ khả năng trinh sát của xà yêu và huyễn thuật ẩn thân không hoàn hảo của hồ yêu. Giữ khoảng cách tôn trọng, đôi khi trao đổi tin tức ngầm về tình hình an ninh khu vực.
- **Huyết Hổ Hạ Chúng:** Đồng cảnh ngộ yêu tộc bị nô dịch, nhưng cách xa về địa lý và đều quá yếu để liên lạc chính thức mà không bị chủ nhân phát hiện.
