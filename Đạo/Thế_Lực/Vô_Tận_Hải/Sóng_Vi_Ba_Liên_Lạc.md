---
type: faction
name: Sóng Vi Ba Liên Lạc
hantu: 波微联络
faction_type: Bộ Lạc
alignment: 0
race: Vi Tộc (Vi Ba Linh — sinh vật vi sóng)
region: Vô Tận Hải
founded: Thượng Cổ (không xác định chính xác)
founder: Không có (hình thành tự nhiên hoặc nhân tạo cổ đại)
emblem: Song_Vi_Ba.png
specialty: Truyền tín hiệu vi sóng dưới nước, Mạng lưới liên lạc bao phủ toàn đại dương
economy:
  - Không có nền kinh tế (tồn tại bằng hấp thu linh khí vi lượng)
arcs:
  - arc: 1
    status: Tồn tại tự nhiên
    rank: Không Xếp Hạng
    leader: Ba Mẫu
    population: Hàng tỷ cá thể
    territory:
      - Toàn bộ Vô Tận Hải (phân bố từ mặt biển đến vùng nước sâu)
    assets:
      - name: Mạng Lưới Vi Ba Toàn Hải
        type: Công Trình
      - name: Kho Tín Hiệu của Ba Mẫu
        type: Tài Nguyên
    stats: [5, 5, 5, 50, 5, 45]
    divisions:
      - name: Ba Mẫu
        role: Cá thể trung tâm, "tổng đài" xử lý lượng tín hiệu lớn nhất trong mạng lưới
        headcount:
          truong_lao: 1
          chien_binh: 0
          dan_thuong: 0
        members:
          - character: "[Ba Mẫu]"
            position: Trưởng Lão (Tổng Đài Trung Tâm)
            cultivation: Luyện Khí (tương đương)
            placeholder: true
      - name: Mạng Lưới Vi Ba Linh
        role: Hàng tỷ cá thể phân bố khắp biển, nhận và truyền tín hiệu tự động
        headcount:
          truong_lao: 0
          chien_binh: 0
          dan_thuong: 0
        members:
          - character: "[Vi Ba Linh cá thể]"
            position: Nốt mạng lưới
            cultivation: Không có
            placeholder: true
    relationships:
      - faction: Hải Thần Cung
        description: Hải Thần Cung là thế lực đầu tiên phát hiện và lợi dụng mạng lưới Vi Ba để truyền tin nội bộ, nhưng không kiểm soát được nó.
        diplomacy:
          lien_minh: 0
          tin: 0
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 0
          le_thuoc: -20
      - faction: Hắc Hải Hải Tặc
        description: Hắc Hải Hải Tặc phát hiện mạng lưới Vi Ba và lợi dụng để nghe trộm thông tin thương mại, gây thiệt hại gián tiếp cho nhiều thế lực.
        diplomacy:
          lien_minh: 0
          tin: 0
          uy_hiep: 0
          thuong_mai: 0
          on_oan: -10
          le_thuoc: -15
      - faction: Phù Du Linh Đoàn
        description: Hai Vi Tộc cùng tồn tại trong hệ sinh thái biển sâu, không cạnh tranh tài nguyên. Phù Du phát sáng, Vi Ba truyền sóng — bổ sung cho nhau.
        diplomacy:
          lien_minh: 0
          tin: 0
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 0
---

# Sóng Vi Ba Liên Lạc (波微联络)

> *"Đại dương có đôi tai — nó nghe thấy tất cả, nhớ tất cả, nhưng không bao giờ nói lại."*
> — Tác giả không rõ, khắc trên vách đá một phế tích dưới đáy biển

## I. Tổng Quan (总览)
Sóng Vi Ba Liên Lạc là mạng lưới liên lạc tự nhiên — hoặc có thể là nhân tạo cổ đại — bao phủ toàn bộ Vô Tận Hải, được tạo thành từ hàng tỷ sinh vật cực nhỏ thuộc Vi Tộc gọi là Vi Ba Linh. Mỗi Vi Ba Linh là một "nốt" trong mạng lưới khổng lồ, nhận tín hiệu từ môi trường xung quanh rồi truyền đi dưới dạng vi sóng trong nước — nhanh hơn bất kỳ phương tiện liên lạc nào khác dưới biển. Đứng đầu hệ thống là Ba Mẫu — cá thể trung tâm đóng vai trò "tổng đài," xử lý lượng tín hiệu lớn nhất và ghi nhận mọi thông tin đã truyền qua mạng lưới từ hàng nghìn năm. Sóng Vi Ba Liên Lạc không xếp hạng và không được coi là một thế lực thực sự, nhưng ảnh hưởng gián tiếp của nó là vô cùng lớn: bất kỳ ai kiểm soát được mạng lưới này sẽ nắm trong tay hệ thống tình báo bao phủ toàn bộ đại dương.

## II. Địa Lý & Tài Nguyên (地理与资源)
Vi Ba Linh phân bố khắp mọi tầng nước trong Vô Tận Hải, từ lớp nước ấm gần mặt biển nơi mật độ cao nhất, đến vùng nước sâu tối tăm nơi chúng thưa dần nhưng không bao giờ hoàn toàn vắng bóng. Chúng không chiếm giữ lãnh thổ theo nghĩa thông thường — tồn tại như một lớp mỏng vô hình hòa lẫn trong nước biển, không thể nhìn thấy bằng mắt thường hay cảm nhận bằng thần thức thông thường. Mật độ Vi Ba Linh dày đặc nhất tại ba khu vực: eo biển Xích Long — huyết mạch giao thương giữa Đông Hoang và Vô Tận Hải, vùng nước quanh San Hô Đảo Quốc — nơi tín hiệu liên lạc nội bộ của đảo quốc tạo ra lượng dữ liệu khổng lồ, và vùng biển phía bắc gần Bắc Hải — nơi hải lưu ấm lạnh giao nhau tạo điều kiện sinh sản lý tưởng cho Vi Ba Linh. Tài nguyên duy nhất mà Vi Ba Linh cần là linh khí vi lượng trong nước, một lượng đủ để duy trì sự sống và chức năng truyền sóng nhưng không hơn. Ba Mẫu cư trú tại một vị trí cố định trong tầng nước trung — điểm hội tụ của nhiều hải lưu lớn gọi là "Vạn Lưu Điểm" — nơi tín hiệu từ mọi phương đều có thể đến được với tốc độ nhanh nhất.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
Vi Ba Linh không có văn hóa hay tín ngưỡng. Chúng là những "bưu tá vô thức" của đại dương — chỉ biết nhận tín hiệu và truyền đi, không hiểu nội dung, không phân biệt nguồn gốc, không phán xét mục đích. Mỗi cá thể hoạt động theo bản năng sinh học thuần túy: khi tiếp nhận một vi sóng, cơ thể tự động khuếch đại và phát lại theo hướng lan tỏa, như những gợn sóng trên mặt nước nhưng nhanh hơn và có trật tự hơn. Vi Ba Linh không phân biệt tín hiệu của Hải Thần Cung với tín hiệu của Hắc Hải Hải Tặc, không biết đâu là mệnh lệnh quân sự, đâu là thông tin thương mại — tất cả đều được truyền đi với cùng tốc độ và sự trung thực tuyệt đối. Chính sự "vô tư" này khiến mạng lưới vừa vô cùng hữu ích, vừa vô cùng nguy hiểm. Một nghiên cứu sinh của Triều Tịch Quan Trắc Đài từng nhận xét: "Vi Ba Linh là bằng chứng rằng sự trung lập tuyệt đối cũng là một dạng quyền lực — thứ quyền lực mà không ai kiểm soát được."

## IV. Cơ Cấu Tổ Chức (组织结构)
Cơ cấu của Sóng Vi Ba Liên Lạc cực kỳ đơn giản nhưng hiệu quả vượt trội. Ba Mẫu là cá thể trung tâm duy nhất, đóng vai trò "tổng đài" xử lý lượng tín hiệu lớn nhất — mọi vi sóng truyền qua mạng lưới cuối cùng đều đi qua Ba Mẫu ít nhất một lần. Hàng tỷ Vi Ba Linh còn lại phân bố đều khắp Vô Tận Hải, mỗi cá thể kết nối với hàng nghìn cá thể lân cận, tạo thành mạng lưới dày đặc với độ dư thừa cực cao — nếu hàng triệu cá thể bị tiêu diệt, mạng lưới vẫn hoạt động bình thường vì tín hiệu tự tìm đường đi khác. Hệ thống hoạt động hoàn toàn tự động, không cần ai điều khiển hay bảo trì. Vi Ba Linh sinh sản liên tục để thay thế những cá thể già chết, duy trì mật độ mạng lưới ổn định qua hàng nghìn năm.

## V. Công Pháp & Trận Pháp (功法与阵法)
Vi Ba Linh không tu luyện bất kỳ công pháp nào — truyền sóng là bản năng sinh học bẩm sinh, giống như cá bơi hay chim bay. Mỗi cá thể có một cơ quan đặc biệt trong cơ thể vi mô gọi là "Ba Hạch" — một tinh thể linh khí siêu nhỏ có khả năng tiếp nhận dao động trong nước, khuếch đại và phát lại theo tần số cụ thể. Tốc độ truyền tín hiệu qua mạng lưới Vi Ba nhanh hơn bất kỳ phương tiện liên lạc nào khác dưới biển — một thông điệp có thể đi từ bờ đông sang bờ tây Vô Tận Hải trong vài canh giờ, trong khi truyền âm thông thường phải mất nhiều ngày. Nhược điểm lớn nhất là tín hiệu không mã hóa: Vi Ba Linh truyền nguyên bản mọi dao động mà chúng tiếp nhận, nghĩa là bất kỳ ai biết cách "nghe" tần số vi sóng đều có thể chặn và giải mã nội dung — một lỗ hổng an ninh mà nhiều thế lực đã khai thác.

## VI. Đặc Sản Môn Phái (门派特产)
- **Vi Ba Tần Phổ:** Kiến thức về cách "nghe" mạng lưới Vi Ba là tài sản giá trị nhất liên quan đến Vi Tộc này. Bất kỳ ai nắm được tần số và cách giải mã vi sóng đều có thể biến toàn bộ Vô Tận Hải thành phòng nghe trộm riêng. Hiện tại, chỉ Hải Thần Cung, Hắc Hải Hải Tặc và Triều Tịch Quan Trắc Đài nắm được kỹ thuật này, mỗi bên với mức độ thông thạo khác nhau. Hải Thần Cung sử dụng một pháp khí gọi là "Thính Hải Loa" — vỏ ốc linh khổng lồ được khắc phù văn, có thể lọc và khuếch đại tín hiệu Vi Ba trong phạm vi nhất định.
- **Ba Mẫu Ký Ức:** Ba Mẫu ghi nhận mọi tín hiệu đã truyền qua mạng lưới từ hàng nghìn năm — một kho thông tin khổng lồ chứa đựng mọi bí mật quân sự, thương mại và ngoại giao đã từng được trao đổi trên biển. Nếu ai đó tìm cách truy cập được ký ức của Ba Mẫu, họ sẽ sở hữu kho tình báo lớn nhất lịch sử — nhưng cho đến nay chưa ai biết cách. Có giả thuyết rằng cần một thần thức cấp Hóa Thần mới có thể tiếp xúc trực tiếp với ý thức nguyên thủy của Ba Mẫu mà không bị dòng thác tín hiệu cuốn đi.
- **Ba Hạch Tinh Thể:** Khi Vi Ba Linh chết, Ba Hạch của chúng kết tinh thành hạt vi tinh thể có khả năng dao động với tần số cố định. Thợ rèn chế tạo truyền âm bảo đã thu mua loại tinh thể này để gắn vào các pháp khí liên lạc, tăng phạm vi truyền tin đáng kể. Giá mỗi lạng Ba Hạch Tinh Thể là năm linh thạch trung phẩm tại chợ San Hô Đảo Quốc.

## VII. Cơ Sở Hạ Tầng (基础设施)
Mạng lưới Vi Ba Linh bản thân nó chính là cơ sở hạ tầng — một hệ thống liên lạc sống bao phủ toàn bộ đại dương, tự duy trì và tự sửa chữa qua hàng nghìn năm. Ba Mẫu cư trú tại Vạn Lưu Điểm trong tầng nước trung, nơi giao nhau của nhiều hải lưu lớn, tạo thành "nút trung tâm" tự nhiên của mạng lưới. Vị trí chính xác của Ba Mẫu là bí mật — không phải vì ai đó cố tình giấu, mà vì chưa ai tìm ra trong vùng biển mênh mông. Ngoài ra, mạng lưới có những "nút phụ" — những cá thể Vi Ba Linh lớn hơn bình thường phân bố tại các giao điểm hải lưu quan trọng — đóng vai trò trạm chuyển tiếp, đảm bảo tín hiệu không bị suy yếu trên quãng đường dài.

## VIII. Kinh Tế (经济)
Sóng Vi Ba Liên Lạc không có nền kinh tế riêng, nhưng giá trị kinh tế gián tiếp mà mạng lưới tạo ra là vô cùng lớn. Hải Thần Cung sử dụng mạng lưới Vi Ba như một kênh liên lạc quân sự bổ sung, tiết kiệm chi phí vận hành hệ thống truyền tin riêng. Hắc Hải Hải Tặc khai thác mạng lưới để nghe trộm lộ trình thương thuyền, từ đó phục kích chính xác hơn — gây thiệt hại hàng triệu linh thạch cho các thương hội mỗi năm. Triều Tịch Quan Trắc Đài thu thập dữ liệu từ mạng lưới Vi Ba để nghiên cứu thủy văn và dự báo thủy triều, phục vụ mục đích khoa học. Tóm lại, Vi Ba Linh không kiếm lợi nhuận, nhưng mạng lưới của chúng là nguồn tài nguyên thông tin mà nhiều thế lực đang tranh nhau khai thác.

## IX. Lịch Sử Tóm Tắt (简史)
Mạng lưới Vi Ba Linh tồn tại từ thượng cổ nhưng chỉ được phát hiện trong thời kỳ gần đây. Triều Tịch Quan Trắc Đài là tổ chức đầu tiên ghi nhận sự tồn tại của mạng lưới khi nhà nghiên cứu Hà Tĩnh Ba phát hiện các dao động bất thường trong nước biển và nhận ra rằng chúng không phải hiện tượng tự nhiên mà là tín hiệu có cấu trúc — bà gọi chúng là "Hải Mạch Sóng" trong bản báo cáo đầu tiên. Sau đó, một nhà nghiên cứu của Hải Thần Cung tên Lương Hải Vân xác nhận nguồn gốc sinh học của tín hiệu và đặt tên cho sinh vật tạo ra chúng là "Vi Ba Linh." Hải Thần Cung nhanh chóng học cách lợi dụng mạng lưới để truyền tin nội bộ bằng cách tạo dao động nhân tạo ở tần số tương thích, nhưng nhận ra rằng không thể kiểm soát hay độc quyền nó — mạng lưới thuộc về đại dương, không thuộc về ai. Khoảng năm trăm năm trước, Hắc Hải Hải Tặc qua một thương nhân phản bội từ San Hô Đảo Quốc cũng phát hiện và bắt đầu dùng mạng lưới để nghe trộm, khiến mạng lưới trở thành chiến trường tình báo ngầm giữa các thế lực. Gần đây, Hải Thần Cung bắt đầu nghiên cứu cách "gây nhiễu" mạng lưới Vi Ba trong phạm vi nhỏ để ngăn nghe trộm — một dự án bí mật do Tư Mã Hải Thần đích thân giám sát.

## X. Giai Thoại & Bí Mật (轶事与秘密)
Ba Mẫu ghi nhận mọi tín hiệu đã truyền qua mạng lưới từ hàng nghìn năm — một kho thông tin khổng lồ nhưng không ai truy cập được, như một thư viện khổng lồ mà không ai tìm thấy cửa vào. Có giả thuyết rằng mạng lưới Vi Ba Linh không phải hình thành tự nhiên mà là công trình nhân tạo của một nền văn minh cổ đại đã diệt vong — nếu đúng, nền văn minh đó phải có trình độ sinh học và kỹ thuật vượt xa mọi thế lực hiện tại. Bằng chứng gián tiếp là cấu trúc mạng lưới quá hoàn hảo, quá đồng đều để là sản phẩm của tiến hóa tự nhiên — đặc biệt là cách Ba Hạch trong cơ thể Vi Ba Linh được "thiết kế" với tần số dao động chính xác đến mức không thể là ngẫu nhiên.

Nếu ai đó kiểm soát được Ba Mẫu, họ không chỉ nắm mạng lưới tình báo toàn đại dương mà còn có thể truy cập kho ký ức hàng nghìn năm — biết được mọi bí mật mà mọi thế lực từng trao đổi trên biển, bao gồm vị trí kho báu chìm, hiệp ước mật, và đường đi bí mật giữa các đảo. Đây là lý do nhiều thế lực đang bí mật tìm kiếm vị trí của Ba Mẫu, nhưng trong đại dương mênh mông, đó là nhiệm vụ gần như bất khả thi. Có lời đồn rằng Hắc Hải Hải Tặc đã thu hẹp phạm vi tìm kiếm xuống còn một vùng biển rộng nghìn dặm vuông — vẫn quá lớn, nhưng đã gần hơn bất kỳ ai khác.

Một giả thuyết gây tranh cãi cho rằng Ba Mẫu không chỉ là "tổng đài" mà còn có ý thức nguyên thủy — một dạng thần thức cực kỳ đơn giản phát triển qua hàng nghìn năm tiếp nhận tín hiệu. Nếu giả thuyết này đúng, Ba Mẫu có thể "hiểu" nội dung tín hiệu truyền qua mạng lưới, và kho ký ức của nó không phải ghi nhận cơ học mà là ký ức có ý thức. Hà Tĩnh Ba từng viết trong nhật ký: *"Nếu đại dương có linh hồn, Ba Mẫu chính là tiềm thức của nó — nó biết tất cả nhưng không bao giờ nói ra, giống như kẻ giữ bí mật vĩ đại nhất lịch sử mà không ai đặt câu hỏi."* Điều đáng lo ngại: nếu Ba Mẫu có ý thức, liệu nó có đang đánh giá các thế lực dựa trên hành vi của họ trên biển? Và nếu có, nó sẽ đứng về phía ai?

## XI. Quan Hệ Thế Lực (势力关系)
- **Hải Thần Cung:** Thế lực đầu tiên phát hiện và khai thác mạng lưới Vi Ba cho mục đích liên lạc quân sự. Hải Thần Cung coi mạng lưới như một công cụ tiện lợi nhưng nhận ra rằng không thể kiểm soát hay độc quyền nó. Mối lo lớn nhất của Hải Thần Cung là các thế lực thù địch cũng đang nghe trộm trên cùng mạng lưới.
- **Hắc Hải Hải Tặc:** Kẻ khai thác bất hợp pháp lớn nhất. Hải tặc dùng mạng lưới Vi Ba để nghe trộm lộ trình thương thuyền và thông tin quân sự, biến một hệ sinh thái tự nhiên thành vũ khí tình báo. Điều này gây thiệt hại gián tiếp cho Vi Ba Linh vì các thế lực lớn bắt đầu tìm cách phá hủy một phần mạng lưới để ngăn chặn rò rỉ thông tin.
- **Phù Du Linh Đoàn:** Hai Vi Tộc cùng tồn tại trong hệ sinh thái Vô Tận Hải mà không cạnh tranh. Phù Du Linh phát sáng ở tầng nước tối, Vi Ba Linh truyền sóng khắp mọi tầng — hai hệ thống bổ sung cho nhau, cùng tạo nên một lớp hạ tầng sinh thái ngầm mà phần lớn các thế lực trên mặt nước không biết đến.
