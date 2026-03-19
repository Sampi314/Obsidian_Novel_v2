---
type: faction
name: Tuyết Hoa Vi Linh
hantu: 雪花微灵
faction_type: Bộ Lạc
alignment: 3
race: Vi Tộc
region: Bắc Băng
founded: Thái Cổ Kỷ Nguyên (Tự sinh)
founder: Không có (Tự nhiên hình thành)
emblem: Bong_Tuyet_Phat_Sang.png
specialty: Thu thập thông tin thụ động, Hóa tuyết ngụy trang, Cộng hưởng linh lực tập thể
economy:
- Không tham gia thương mại (Thụ động)
- Kho tàng thông tin tích lũy hàng ngàn năm (Tiềm năng)
- Hàn quang vi lực phát tán tự nhiên (Vô thức)
arcs:
  - arc: 1
    status: Trôi nổi tự do, gần đây bắt đầu tránh xa vùng ma khí
    rank: Không Xếp Hạng
    leader: Không có (Ý thức tập thể)
    population: 10000
    territory:
      - Vùng trời gần Cực Quang Thần Điện
      - Toàn bộ không phận Bắc Băng (Trôi theo gió)
    assets:
      - name: Ký Ức Tập Thể Vạn Năm
        type: Tài Nguyên
      - name: Trường Cộng Hưởng Vi Linh
        type: Trận Pháp
    stats: [5, 10, 5, 10000, 50, 15]
    divisions:
      - name: Quần Thể Vi Linh
        role: Trôi nổi, quan sát, thu thập và chia sẻ thông tin qua cộng hưởng linh lực
        headcount:
          truong_lao: 0
          chien_binh: 0
          dan_thuong: 10000
        members:
          - character: "[Vi Linh Hạch Tâm]"
            position: Nút cộng hưởng trung tâm (Không phải lãnh đạo)
            cultivation: Luyện Khí Sơ Kỳ (Tương đương)
            placeholder: true
    relationships:
      - faction: Cực Quang Thần Điện
        description: Thần Điện nhiều lần cố bắt Vi Linh làm công cụ do thám nhưng thất bại hoàn toàn, vì Vi Linh không phục tùng bất kỳ ý chí nào.
        diplomacy:
          lien_minh: -20
          tin: -40
          uy_hiep: 30
          thuong_mai: 0
          on_oan: -30
          le_thuoc: 0
      - faction: Băng Tinh Khuẩn Tộc
        description: Đồng loại Vi Tộc, cảm nhận được sự tồn tại của nhau qua cộng hưởng linh lực dù hình thái khác biệt.
        diplomacy:
          lien_minh: 30
          tin: 50
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 0
      - faction: Huyền Băng Cung
        description: Huyền Băng Cung coi Vi Linh là hiện tượng tự nhiên vô hại, không chủ động giao tiếp. Vi Linh thỉnh thoảng trôi qua lãnh thổ của Cung mà không bị cản trở.
        diplomacy:
          lien_minh: 0
          tin: 10
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 0
---

# TUYẾT HOA VI LINH (雪花微灵)

## I. Tổng Quan (总览)
Tuyết Hoa Vi Linh là một dạng sống Vi Tộc đặc biệt tại Bắc Băng — những thực thể linh giác siêu nhỏ, mỗi cá thể chỉ bằng một bông tuyết, gần như hoàn toàn vô hình trước mắt thường. Chúng không có thủ lĩnh, không có tổ chức, không có lãnh thổ cố định — chỉ là hàng vạn bông tuyết sống trôi nổi theo gió Bắc Băng, âm thầm quan sát và thu thập mọi thứ chúng đi ngang qua. Dù không xếp hạng trong bất kỳ hệ thống thế lực nào, sự tồn tại của Vi Linh mang ý nghĩa tiềm ẩn to lớn: chúng là kho tàng ký ức sống của toàn bộ Bắc Băng, ghi nhận mọi lời nói, mọi trận chiến, mọi bí mật đã từng xảy ra trên vùng đất băng giá này suốt hàng vạn năm.

Không ai biết chính xác Vi Linh có bao nhiêu cá thể — con số dao động theo cường độ cực quang và nồng độ Hàn khí trong khí quyển. Trong những đêm cực quang rực rỡ, số lượng Vi Linh có thể tăng gấp mười lần khi hàng ngàn cá thể mới tự sinh ra từ sự giao thoa giữa quang năng và Hàn khí.

## II. Địa Lý & Tài Nguyên (地理 与 资源)
Tuyết Hoa Vi Linh không sở hữu lãnh thổ theo nghĩa truyền thống. Chúng trôi nổi tự do trên toàn bộ không phận Bắc Băng, nhưng mật độ tập trung cao nhất ở vùng trời gần Cực Quang Thần Điện — nơi cực quang chiếu sáng thường xuyên nhất và Hàn khí đậm đặc nhất. Gió mùa và dòng khí lạnh quyết định hướng di chuyển của quần thể, khiến chúng đôi khi trôi qua lãnh thổ của hầu hết mọi thế lực Bắc Băng mà không ai hay biết.

Tài nguyên duy nhất của Vi Linh chính là thông tin. Khi trôi qua bất kỳ đâu, chúng tự động ghi nhận mọi âm thanh, mọi dao động linh lực trong phạm vi gần. Những thông tin này được chia sẻ qua mạng lưới cộng hưởng linh lực giữa các cá thể, tạo thành một kho dữ liệu tập thể khổng lồ mà không một tổ chức tình báo nào trên lục địa có thể sánh được. Ngoài ra, bản thân Vi Linh cũng phát tán một lượng nhỏ vi hàn quang vô thức — loại năng lượng này tuy yếu nhưng có tác dụng tịnh hóa nhẹ đối với chướng khí trong không khí.

Gần đây, quần thể Vi Linh bắt đầu tự động tránh xa một khu vực cụ thể trên lãnh nguyên tundra — nơi đó ma khí đang âm thầm rỉ lên từ dưới lòng đất. Đây là dấu hiệu cảnh báo mà chưa thế lực nào nhận ra.

## III. Văn Hóa & Tín Ngưỡng (文化 与 信仰)
Vi Linh không có văn hóa hay tín ngưỡng theo cách hiểu thông thường. Chúng tồn tại bằng bản năng thuần khiết nhất — sự tò mò. Mọi hành vi của Vi Linh đều xoay quanh một xung lực đơn giản: quan sát, ghi nhận, chia sẻ. Chúng không phân biệt thiện ác, không đánh giá đúng sai, không can thiệp vào bất kỳ sự kiện nào chúng chứng kiến.

Quy tắc duy nhất trong quần thể là: không hại ai, không giúp ai — chỉ quan sát và thu thập. Đây không phải là luật lệ do ai đặt ra, mà là bản chất cố hữu trong linh giác của Vi Linh. Chúng hoàn toàn trung lập đến mức gần như vô cảm, xem mọi sự kiện — từ trận chiến hủy thiên diệt địa đến cuộc tình lãng mạn — đều chỉ là "thông tin cần ghi nhận".

Phong tục duy nhất có thể quan sát được: khi cực quang xuất hiện, toàn bộ Vi Linh trong khu vực sẽ bay lên cao nhất có thể, tụ lại thành những đám mây tuyết lấp lánh dưới ánh cực quang. Đó là thời khắc chúng hấp thu quang năng để tái sinh và sinh sản, đồng thời cũng là lúc mạng lưới cộng hưởng hoạt động mạnh nhất — toàn bộ thông tin thu thập được sẽ được đồng bộ hóa trong khoảnh khắc này.

## IV. Cơ Cấu Tổ Chức (组织结构)
Vi Linh không có tổ chức theo nghĩa truyền thống. Khoảng vạn cá thể cùng tồn tại và chia sẻ thông tin qua một trường cộng hưởng linh lực tự nhiên, không cần bất kỳ hệ thống chỉ huy nào. Mỗi Vi Linh là một đơn vị độc lập nhưng đồng thời cũng là một phần không thể tách rời của ý thức tập thể.

Mỗi cá thể nhỏ bằng một bông tuyết, cấu tạo từ Hàn khí ngưng kết và một tia linh giác siêu nhỏ — vừa đủ để cảm nhận môi trường xung quanh nhưng không đủ để tư duy phức tạp. Chính vì vậy, Vi Linh hoạt động theo kiểu "trí tuệ bầy đàn": từng cá thể đơn giản đến mức nguyên thủy, nhưng khi kết nối thành mạng lưới, chúng tạo ra một ý thức tập thể tinh vi hơn bất kỳ cá nhân nào.

Khi cần giao tiếp với sinh vật khác (điều cực kỳ hiếm), Vi Linh có thể hợp nhất tạm thời thành một hình dạng mờ ảo — thường là hình bông tuyết khổng lồ hoặc hình người lờ mờ. Trạng thái hợp nhất này tiêu tốn rất nhiều năng lượng và chỉ duy trì được trong thời gian ngắn.

## V. Công Pháp & Trận Pháp (功法 与 阵法)
Vi Linh không tu luyện theo bất kỳ hệ thống công pháp nào. Sự tồn tại của chúng hoàn toàn dựa vào quá trình hấp thu Hàn khí và quang năng cực quang một cách tự nhiên — giống như thực vật quang hợp hơn là tu sĩ luyện công. Mỗi cá thể chỉ tương đương cảnh giới Luyện Khí thấp nhất, nhưng sức mạnh thực sự nằm ở số lượng và khả năng phối hợp tập thể.

Khả năng đặc biệt nhất của Vi Linh là hóa thành bông tuyết hoàn hảo — không ai, kể cả tu sĩ Nguyên Anh, có thể phân biệt một Vi Linh với bông tuyết thường bằng mắt thường hay thần thức thông thường. Chỉ những tồn tại có trường cộng hưởng linh lực tương tự (như Băng Tinh Khuẩn Tộc) mới cảm nhận được sự hiện diện của chúng.

Trường cộng hưởng linh lực của Vi Linh tuy không phải trận pháp nhân tạo, nhưng hoạt động theo nguyên lý tương tự: khi số lượng đủ lớn, trường cộng hưởng có thể tạo ra hiệu ứng can thiệp nhẹ lên môi trường xung quanh — làm nhiễu loạn trận pháp cấp thấp, gây sai lệch la bàn linh lực, hoặc tạo ra "tiếng ồn trắng" che mờ tín hiệu truyền tin linh lực.

## VI. Đặc Sản Môn Phái (门派特产)
Vi Linh không sản xuất bất kỳ sản phẩm nào một cách chủ động. Tuy nhiên, sự tồn tại của chúng vô tình tạo ra một số thứ có giá trị:

- **Tuyết Linh Phấn:** Khi Vi Linh tự nhiên chết đi (do Hàn khí cạn kiệt hoặc gió ấm từ phương Nam), tàn thể của chúng hóa thành một loại bụi sáng cực mịn gọi là Tuyết Linh Phấn. Loại bụi này có đặc tính tăng cường thần thức trong thời gian ngắn nếu được hít vào, nhưng thu thập cực kỳ khó khăn vì nó gần như vô hình.

- **Ký Ức Tập Thể:** Tài sản quý giá nhất của Vi Linh không phải là vật chất mà là thông tin. Nếu có ai đó tìm cách kết nối được với mạng lưới cộng hưởng của chúng, người đó sẽ tiếp cận được kho tàng bí mật khổng lồ về mọi thế lực Bắc Băng tích lũy suốt hàng vạn năm — bao gồm cả những bí mật mà chính các thế lực đó đã quên từ lâu.

## VII. Cơ Sở Hạ Tầng (基础设施)
Vi Linh không xây dựng bất kỳ công trình nào. Chúng không cần nhà ở, không cần kho chứa, không cần đường sá. Toàn bộ "hạ tầng" của quần thể là bầu trời Bắc Băng và những dòng gió mang Hàn khí.

Tuy nhiên, có thể coi trường cộng hưởng linh lực của Vi Linh là một dạng hạ tầng vô hình — một mạng lưới thông tin xuyên suốt toàn bộ Bắc Băng, hoạt động liên tục và không thể bị phá hủy trừ khi tiêu diệt toàn bộ Vi Linh cùng lúc. Mạng lưới này có phạm vi phủ sóng rộng hơn bất kỳ hệ thống truyền tin nào do các tông môn thiết lập, mặc dù tốc độ truyền tin phụ thuộc vào mật độ Vi Linh trong khu vực.

## VIII. Kinh Tế (经济)
Vi Linh hoàn toàn đứng ngoài mọi hoạt động kinh tế. Chúng không mua bán, không trao đổi, không sản xuất. Sự tồn tại của chúng là tự cấp tự túc thông qua việc hấp thu Hàn khí và quang năng từ môi trường tự nhiên.

Giá trị kinh tế tiềm năng duy nhất nằm ở Tuyết Linh Phấn — tàn thể của Vi Linh đã chết. Một số luyện đan sư cấp cao biết đến sự tồn tại của loại nguyên liệu này và sẵn sàng trả giá rất cao, nhưng việc thu thập gần như bất khả thi do bụi Tuyết Linh Phấn quá nhỏ và nhanh chóng hòa tan vào Hàn khí xung quanh.

## IX. Lịch Sử Tóm Tắt (简史)
Tuyết Hoa Vi Linh đã tồn tại từ khi có cực quang ở Bắc Băng — có thể hàng vạn năm hoặc lâu hơn, không ai biết chính xác. Chúng tự sinh ra từ sự giao thoa giữa Hàn khí và quang năng cực quang, không có tổ tiên hay nguồn gốc chủng tộc rõ ràng. Số lượng Vi Linh tăng giảm theo cường độ cực quang qua các thời kỳ, nhưng chưa bao giờ hoàn toàn biến mất.

Trong suốt lịch sử Bắc Băng, Vi Linh luôn ở đó — lặng lẽ trôi qua những trận đại chiến, những cuộc hội đàm bí mật, những âm mưu lật đổ — ghi nhận tất cả mà không can thiệp. Cực Quang Thần Điện là thế lực duy nhất đã chính thức nhận ra sự tồn tại của Vi Linh và nhiều lần cố gắng bắt giữ, thuần hóa chúng để sử dụng làm mạng lưới do thám. Mọi nỗ lực đều thất bại thảm hại — Vi Linh đơn giản là trôi đi, không chống cự cũng không phục tùng, và việc bắt một bông tuyết giữa bão tuyết Bắc Băng là điều không tưởng.

## X. Giai Thoại & Bí Mật (轶事 与 秘密)
Có một thuyết bí truyền cho rằng Tuyết Hoa Vi Linh là "mắt" của Bắc Băng — chúng phản ánh trạng thái sức khỏe của toàn bộ vùng đất. Khi Vi Linh hoạt động bình thường, Bắc Băng an yên. Khi Vi Linh bất thường — tụ lại quá đông, hoặc đột ngột biến mất ở một khu vực — đó là điềm báo tai họa sắp xảy ra. Trong quá khứ, mỗi lần Vi Linh tránh xa một vùng đất, vùng đó đều gặp đại nạn không lâu sau.

Tương truyền, trong thời kỳ Thượng Cổ, đã từng có một vị tu sĩ ẩn dật thành công kết nối với ý thức tập thể của Vi Linh. Sau khoảnh khắc đó, vị tu sĩ này phát điên vì lượng thông tin khổng lồ tràn ngập thần thức — nhưng trước khi mất trí hoàn toàn, người đó đã viết lại một cuốn sách nhỏ chứa đựng những bí mật kinh hoàng về các phong ấn thượng cổ dưới lòng đất Bắc Băng. Cuốn sách đó hiện nằm ở đâu, không ai biết.

Gần đây, việc Vi Linh bắt đầu tránh xa một khu vực cụ thể trên tundra khiến một số vị đại năng bắt đầu lo ngại. Nơi đó ma khí đang rỉ lên từ dưới lòng đất — và nếu "mắt" của Bắc Băng đang nhìn chỗ khác, có lẽ vì thứ đang thức tỉnh ở dưới đó quá đáng sợ để nhìn.

## XI. Quan Hệ Thế Lực (势力关系)
- **Cực Quang Thần Điện:** Mối quan hệ một chiều — Thần Điện muốn kiểm soát Vi Linh làm công cụ do thám, nhưng Vi Linh hoàn toàn thờ ơ và không thể bị bắt giữ. Sự thất bại lặp đi lặp lại khiến Thần Điện vừa thèm muốn vừa bực bội.

- **Băng Tinh Khuẩn Tộc:** Hai chủng tộc Vi Tộc cảm nhận được sự tồn tại của nhau qua trường cộng hưởng linh lực. Tuy không giao tiếp trực tiếp, chúng có mối liên kết bản năng — khi một bên gặp nguy hiểm, bên kia cũng cảm thấy bất an. Đây là mối quan hệ cộng sinh tinh thần thầm lặng nhất Bắc Băng.

- **Huyền Băng Cung:** Đại tông môn Bắc Băng coi Vi Linh là hiện tượng tự nhiên vô hại, không chủ động giao tiếp. Vi Linh thường xuyên trôi qua lãnh thổ Huyền Băng Cung và vô tình trở thành "nhân chứng" cho nhiều bí mật nội bộ của tông môn.
