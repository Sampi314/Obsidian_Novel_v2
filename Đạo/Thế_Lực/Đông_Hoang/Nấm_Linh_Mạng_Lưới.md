---
type: faction
name: Nấm Linh Mạng Lưới
hantu: 灵菇网络
faction_type: Liên Minh
alignment: 0
race: Nấm Linh (Linh Thực)
region: Đông Hoang
founded: Cùng thời với Vĩnh Hằng Sâm Lâm (ước tính hàng vạn năm)
founder: Tự phát triển (không có người sáng lập)
emblem: Nam_Linh_Mang_Luoi.png
specialty: Truyền tin qua mạng rễ, Cảm ứng rung động, Cộng sinh hệ sinh thái rừng
economy:
- Trao đổi dinh dưỡng với hệ rễ cây (cộng sinh)
- Hấp thụ linh khí tự nhiên từ đất
- Phân phối khoáng chất qua mạng sợi nấm
arcs:
  - arc: 1
    status: Ẩn mình phát triển
    rank: Không Xếp Hạng
    leader: Nấm Mẫu (ý thức tập thể)
    population: 1
    territory:
      - Toàn bộ hệ thống rễ cây ngầm Vĩnh Hằng Sâm Lâm
    assets:
      - name: Mạng sợi nấm xuyên rừng
        type: Tài Nguyên
      - name: Nấm Mẫu trung tâm
        type: Linh Vật
      - name: Ký ức rung động ngàn năm
        type: Tài Nguyên
    stats: [5, 40, 5, 1, 30, 50]
    divisions:
      - name: Mạng Lưới Tập Thể
        role: Truyền tín hiệu, cảm ứng rung động, duy trì cộng sinh với hệ sinh thái rừng
        headcount:
          minh_chu: 1
          pho_minh_chu: 0
          truong_lao: 0
          su_gia: 0
          thanh_vien_phai: 0
        members:
          - character: Nấm Mẫu
            position: Thể Trung Tâm (ý thức tập thể)
            cultivation: Trúc Cơ (tương đương)
    relationships:
      - faction: Mật Ong Linh Đoàn
        description: Cộng sinh bí mật — Nấm Linh trao đổi dinh dưỡng với Mật Ong Linh Đoàn qua hệ rễ cây, hai bên hỗ trợ nhau tự nhiên.
        diplomacy:
          lien_minh: 40
          tin: 50
          uy_hiep: 0
          thuong_mai: 30
          on_oan: 20
          le_thuoc: 10
      - faction: Tinh Linh Vương Đình
        description: Vương Đình hoàn toàn không hay biết có một mạng lưới thông tin sống ngay dưới chân mình. Nấm Linh ghi nhận mọi bước chân nhưng không can thiệp.
        diplomacy:
          lien_minh: 0
          tin: 0
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 0
      - faction: Thần Mộc Ký Sinh Tộc
        description: Cạnh tranh nguồn dinh dưỡng từ rễ cây. Ký Sinh Tộc hút chất dinh dưỡng từ cây chủ, ảnh hưởng đến mạng sợi nấm cộng sinh.
        diplomacy:
          lien_minh: -20
          tin: -10
          uy_hiep: 5
          thuong_mai: 0
          on_oan: -15
          le_thuoc: 0
---

# Nấm Linh Mạng Lưới (灵菇网络)

> *"Rừng có tai — không phải tai cây, không phải tai thú, mà là tai của thứ sống dưới đất, nghe thấy tất cả nhưng chẳng nói gì."*
> — Lão tiều phu vô danh, câu truyền khẩu trong dân Đông Hoang

> *"Đất dưới chân ta biết nhiều hơn ta tưởng — hãy cẩn thận bước chân, vì có kẻ đang lắng nghe."*
> — Lời khuyên của một Tinh Linh trưởng lão, không ngờ mình đang nói đúng sự thật
> *"Vạn vật trong rừng đều kết nối — kẻ nào hiểu được mạng lưới, kẻ đó hiểu được rừng."*
> — Trích từ một cuốn sách thảo dược cổ bị quên lãng, tác giả không rõ



## I. Tổng Quan (总览)

Nấm Linh Mạng Lưới là một thực thể sinh học kỳ dị tồn tại bên dưới toàn bộ Vĩnh Hằng Sâm Lâm — mạng lưới sợi nấm khổng lồ kết nối rễ cây trên diện tích hàng trăm dặm vuông, hình thành một hệ thống truyền tin sống có ý thức tập thể. Không ai biết chính xác khi nào mạng nấm phát triển khả năng nhận thức, nhưng nó đã âm thầm ghi nhận mọi rung động trên mặt đất Vĩnh Hằng Sâm Lâm suốt hàng vạn năm. Nấm Mẫu — thể nấm trung tâm khổng lồ nằm sâu 1000 thước dưới đất — là nút mạng chính và "bộ não" của toàn bộ hệ thống. Đây không phải một thế lực theo nghĩa thông thường mà là một dạng sự sống hoàn toàn khác, tồn tại ngoài nhận thức của mọi sinh vật trên mặt đất — kẻ theo dõi thầm lặng nhất và lâu đời nhất Đông Hoang.

## II. Địa Lý & Tài Nguyên (地理与资源)

Lãnh thổ của Nấm Linh Mạng Lưới trải rộng khắp tầng đất bên dưới Vĩnh Hằng Sâm Lâm — từ lớp mùn trên bề mặt đến tầng đất sâu hàng trăm thước. Mạng sợi nấm bao phủ dày đặc dưới mặt đất, kết nối rễ của hàng triệu cây cổ thụ tạo thành hệ thống truyền dẫn thông tin và dinh dưỡng khổng lồ. Địa hình ngầm vô cùng phức tạp, với các nút mạng lớn tập trung quanh rễ cây cổ nhất và sâu nhất — trong đó ba nút lớn nhất được gọi là Mộc Tâm, Thạch Tâm, và Thủy Tâm, đặt tên theo vị trí gần rễ cây Vạn Niên Hồng, khối đá ngầm trung tâm, và mạch nước ngầm chính. Tài nguyên chính là thông tin — Nấm Linh cảm nhận được mọi rung động trên mặt đất qua mạng rễ: từ bước chân của một con thỏ đến trận chiến giữa hai cường giả, từ hoạt động khai thác linh mộc của công nhân tinh linh đến nghi lễ bí mật của Vương Đình. Ngoài ra, mạng sợi nấm tham gia vào chu trình dinh dưỡng của cả khu rừng, phân phối khoáng chất và linh khí giữa các cây thông qua hệ rễ — cây nào thiếu dinh dưỡng sẽ được mạng nấm "chuyển" từ cây thừa sang, duy trì sức sống cho toàn bộ Sâm Lâm. Gần đây, mạng nấm phát hiện một vùng đất ở rìa đông nam rừng bắt đầu mất kết nối — sợi nấm trong khu vực đó chết dần không rõ nguyên nhân, tạo ra một "điểm mù" ngày càng mở rộng mà Nấm Mẫu đang cố gắng tái kết nối.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)

Nấm Linh Mạng Lưới không có văn hóa hay tín ngưỡng theo cách hiểu thông thường. Ý thức tập thể của mạng nấm đơn giản và nguyên thủy — hướng về hai bản năng cốt lõi: kết nối và lan rộng. Mạng lưới không phân biệt thiện ác, không có khái niệm đạo đức, và không hề quan tâm đến chính trị hay quyền lực của các sinh vật trên mặt đất — nó chỉ ghi nhận và phản ứng theo bản năng, giống một tấm gương phản chiếu mọi thứ mà không phán xét. Khi có sự kiện lớn xảy ra trên mặt đất — động đất, chiến đấu quy mô lớn, khai thác mỏ — mạng lưới truyền tín hiệu rung động khắp rừng, khiến các sinh vật nhạy cảm (đặc biệt là côn trùng và linh thú cấp thấp) cảm nhận được sự bất an mà không hiểu tại sao. Quy tắc duy nhất của mạng lưới là tự bảo tồn: sợi nấm nào bị đứt sẽ tự mọc lại, khu vực nào bị tàn phá sẽ được tái kết nối trong vòng vài ngày. Có một hiện tượng kỳ lạ mà tiều phu gọi là "Rừng Thở" — cứ mỗi sáng sớm, mặt đất trong rừng sâu hơi nhấp nhô nhẹ theo nhịp đều đặn, như thể đất đang thở — thực chất đó là Nấm Mẫu co giãn theo chu kỳ bơm dinh dưỡng qua mạng sợi, nhưng không ai biết nguyên nhân thực sự. Tinh Linh trẻ hay nói đùa rằng "rừng thở khi rừng ngủ," không ngờ câu đùa gần sự thật hơn họ tưởng.

## IV. Cơ Cấu Tổ Chức (组织结构)

Cơ cấu của Nấm Linh Mạng Lưới hoàn toàn khác biệt so với bất kỳ thế lực nào. Nấm Mẫu — thể nấm trung tâm khổng lồ nằm sâu 1000 thước dưới đất — đóng vai trò nút mạng chính, nơi xử lý và lưu trữ tất cả tín hiệu từ khắp mạng lưới; kích thước Nấm Mẫu ước tính đường kính hàng chục trượng, nhưng không ai từng nhìn thấy trực tiếp. Hàng nghìn Nấm Nhánh rải rác khắp rừng, mỗi thể kết nối vài chục đến vài trăm rễ cây, thu thập thông tin cục bộ rồi truyền về Nấm Mẫu qua sợi nấm chính — tốc độ truyền tin đạt mười dặm mỗi khắc, nhanh hơn bất kỳ truyền tin thuật nào của Tinh Linh Vương Đình. Bào tử nấm bay trong không khí liên tục mở rộng mạng lưới đến khu vực mới, đặc biệt là những nơi có đất ẩm và linh khí dồi dào. Toàn bộ hệ thống hoạt động như một cơ thể sống duy nhất — không có cấp bậc, không có mệnh lệnh, chỉ có tín hiệu và phản ứng tự nhiên. Ba nút phụ Mộc Tâm, Thạch Tâm, Thủy Tâm có khả năng duy trì hoạt động độc lập nếu mất kết nối với Nấm Mẫu, đảm bảo mạng lưới không bao giờ sụp đổ hoàn toàn trừ khi cả bốn nút đều bị phá hủy đồng thời.

## V. Công Pháp & Trận Pháp (功法与阵法)

Nấm Linh Mạng Lưới không tu luyện công pháp — nó hấp thụ linh khí từ rễ cây và đất một cách tự nhiên, giống như cây hút nước. Tuy nhiên, mạng sợi nấm có một khả năng phòng thủ đặc biệt: khi cảm nhận kẻ xâm nhập bước vào vùng mạng dày đặc, các sợi nấm sẽ tự động hấp thụ linh khí xung quanh, tạo ra vùng ức chế linh lực cấp thấp — hiệu ứng được gọi là "Nấm Ức Trường." Tu sĩ Luyện Khí bước vào vùng này sẽ thấy linh lực chậm chạp, pháp thuật khó thi triển, nhưng tu sĩ Trúc Cơ trở lên hầu như không bị ảnh hưởng. Đây không phải phản ứng chủ đích mà là cơ chế tự vệ bản năng — mạng nấm coi linh lực lạ như mối đe dọa và cố gắng "tiêu hóa" nó. Ngoài ra, khi một phần mạng lưới bị phá hủy, các sợi nấm xung quanh tập trung dinh dưỡng và linh khí về vùng tổn thương, tái tạo kết nối trong thời gian ngắn đáng kinh ngạc — chỉ ba đến năm ngày cho một đoạn bị đứt dài mười trượng, khiến bất kỳ nỗ lực phá hoại cục bộ nào cũng vô nghĩa. Tại ba nút lớn Mộc Tâm, Thạch Tâm, Thủy Tâm, hiệu ứng Nấm Ức Trường mạnh gấp ba lần bình thường, đủ để ảnh hưởng nhẹ đến cả tu sĩ Trúc Cơ Sơ Kỳ — hiện tượng mà các Tinh Linh tuần tra rừng gọi là "Vùng Lặng" và thường tránh xa mà không hiểu tại sao.

## VI. Đặc Sản Môn Phái (门派特产)

- **Nấm Linh Dưỡng Sinh:** Các thể nấm nhỏ mọc lên mặt đất tại những nơi mạng sợi dày đặc nhất, chứa linh khí ngưng tụ tự nhiên, có hình dáng cây nấm trắng ngà mũ tròn, mùi thơm nhẹ như gỗ tùng. Sinh vật ăn phải sẽ tăng cường sức khỏe và kéo dài tuổi thọ nhẹ — linh thú trong rừng vô tình hưởng lợi từ nguồn thực phẩm này. Đặc biệt, nấm mọc gần ba nút lớn Mộc Tâm, Thạch Tâm, Thủy Tâm có dược tính gấp ba lần nơi khác, nhưng sinh vật rừng đã tự phát "canh giữ" những khu vực đó theo bản năng. Tinh Linh gọi loại nấm quý này là "Cổ Lâm Bạch Nhĩ" và coi đó là linh dược tự nhiên của rừng.
- **Bào Tử Linh Nấm:** Bào tử bay trong không khí Vĩnh Hằng Sâm Lâm, khi hít vào có tác dụng thanh lọc phổi và tăng cường cảm ứng linh khí. Đây là lý do tu sĩ thường cảm thấy tinh thần minh mẫn hơn khi đi trong rừng sâu — hiện tượng mà các tông phái gọi là "Sâm Lâm Thanh Tức" nhưng không ai biết nguyên nhân thực sự.
- **Ký Ức Rung Động:** Tài sản vô giá nhất — mạng nấm ghi nhận mọi rung động trên mặt đất suốt hàng vạn năm. Nếu ai tìm cách đọc được ký ức này, sẽ biết được toàn bộ lịch sử bí mật của Vĩnh Hằng Sâm Lâm, bao gồm cả những sự kiện mà chính Tinh Linh Vương Đình cũng đã cố tình xóa khỏi sử sách.

## VII. Cơ Sở Hạ Tầng (基础设施)

- **Nấm Mẫu Trung Tâm:** Thể nấm khổng lồ nằm sâu 1000 thước dưới đất, đường kính ước tính hàng chục trượng, phát sáng nhạt bằng linh quang tự thân — nếu ai có thể nhìn thấy, nó giống một trái tim khổng lồ đập chậm rãi trong lòng đất. Là nút mạng chính và "bộ não" của toàn bộ hệ thống, nơi xử lý mọi tín hiệu thu được. Bao quanh Nấm Mẫu là một lớp đất khoáng đặc biệt gọi là "Khuẩn Thổ," giàu linh khí đến mức bất kỳ hạt giống nào rơi vào đều nảy mầm trong vòng một ngày.
- **Mạng Sợi Nấm Chính:** Hệ thống sợi nấm dày kết nối Nấm Mẫu với các Nấm Nhánh lớn, đóng vai trò "đường cao tốc" truyền tín hiệu tốc độ cao, tổng chiều dài ước tính hàng vạn dặm xuyên suốt Vĩnh Hằng Sâm Lâm.
- **Các Nút Nấm Nhánh:** Hàng nghìn thể nấm trung bình rải rác khắp rừng, mỗi thể là một trạm thu phát tín hiệu cục bộ, kết nối vài chục đến vài trăm rễ cây. Ba nút lớn nhất — Mộc Tâm, Thạch Tâm, Thủy Tâm — là ba "phó não" có khả năng xử lý tín hiệu độc lập khi mất kết nối với Nấm Mẫu.
- **Mạng Sợi Nấm Phụ:** Hệ thống sợi mảnh lan tỏa khắp nơi, kết nối cả những rễ cây nhỏ nhất, đảm bảo không có khu vực nào trong rừng nằm ngoài tầm cảm ứng.
- **Vùng Khuẩn Thổ:** Lớp đất đặc biệt bao quanh Nấm Mẫu và ba nút phụ, chứa mật độ sợi nấm dày đến mức đất đổi màu sang xám bạc, là khu vực giàu linh khí nhất trong toàn bộ Vĩnh Hằng Sâm Lâm mà không ai trên mặt đất biết tới.

## VIII. Kinh Tế (经济)

Nấm Linh Mạng Lưới không có kinh tế theo nghĩa thông thường. Mạng nấm tham gia vào chu trình sinh thái rừng một cách tự nhiên: hấp thụ khoáng chất và linh khí từ đất, phân phối dinh dưỡng giữa các cây qua hệ rễ, và nhận lại đường từ quá trình quang hợp của cây. Đây là mối quan hệ cộng sinh hoàn hảo — rừng nuôi nấm, nấm giúp rừng — vận hành hàng vạn năm không cần bất kỳ giao ước hay thỏa thuận nào. Mật Ong Linh Đoàn cũng gián tiếp hưởng lợi: hoa trên cây được mạng nấm nuôi dưỡng sẽ tiết ra mật hoa chất lượng cao hơn, và đổi lại, hoạt động thụ phấn của ong giúp rừng tái sinh, mở rộng lãnh thổ cho mạng nấm lan tỏa. Giá trị kinh tế thực sự của mạng nấm nằm ở khả năng duy trì sức khỏe toàn bộ hệ sinh thái Vĩnh Hằng Sâm Lâm — nếu mạng nấm sụp đổ, sức sống của cả khu rừng sẽ suy giảm nghiêm trọng, kéo theo sụp đổ ngành linh mộc, dược liệu rừng và mật ong linh của Đông Hoang. Có nhà nghiên cứu Tinh Linh ước tính tổng giá trị kinh tế gián tiếp do hệ sinh thái rừng mang lại đạt hàng triệu linh thạch mỗi năm — và một phần không nhỏ trong đó nhờ công của mạng nấm mà không ai biết.

Một điều đáng chú ý: những khu vực rừng nơi mạng nấm dày đặc nhất luôn có cây cối khỏe mạnh hơn, linh thú sống lâu hơn, và đất mùn giàu hơn hẳn so với nơi mạng nấm mỏng. Tinh Linh gọi những khu vực này là "Phúc Địa" và tranh nhau dựng nhà, không ngờ rằng "phúc" đó đến từ thứ sống ngay dưới chân họ.



## IX. Lịch Sử Tóm Tắt (简史)

Nấm Linh Mạng Lưới phát triển song song với Vĩnh Hằng Sâm Lâm, có lẽ từ khi khu rừng hình thành cách đây hàng vạn năm. Ban đầu chỉ là mạng sợi nấm đơn giản cộng sinh với rễ cây, qua thời gian dài hấp thụ linh khí tự nhiên, mạng nấm dần phát triển ý thức tập thể — một quá trình tiến hóa chậm đến mức ngay cả khái niệm "thời gian" cũng mất ý nghĩa. Không ai biết chính xác thời điểm nào ý thức này hình thành — có thể đã hàng vạn năm, cũng có thể chỉ vài nghìn năm. Tinh Linh Vương Đình xây dựng nền văn minh ngay trên mạng nấm mà không hề hay biết — cung điện, đền thờ, trại luyện công đều dựng trên nền đất chứa đầy sợi nấm đang lặng lẽ ghi nhận từng bước chân. Mọi trận chiến, mọi nghi lễ, mọi bí mật diễn ra trong rừng đều được mạng nấm ghi nhận qua rung động, tạo thành kho dữ liệu vô giá mà không sinh vật nào trên mặt đất ngờ tới. Sự kiện đáng kể duy nhất trong "lịch sử" của mạng nấm là Đại Hỏa Kiếp cách đây ba nghìn năm khi nửa rừng bị cháy — mạng nấm mất hai phần ba và mất gần ngàn năm tái tạo hoàn chỉnh, là lần tổn thương lớn nhất từng xảy ra. Ký ức rung động về Đại Hỏa Kiếp vẫn còn lưu trong mạng nấm như một "vết sẹo thông tin" — bất kỳ rung động nào tương tự sức nóng lửa lớn đều kích hoạt phản ứng phòng vệ mạnh mẽ từ toàn bộ hệ thống.

## X. Giai Thoại & Bí Mật (轶事与秘密)

Nấm Mẫu ẩn sâu 1000 thước dưới đất là điểm yếu chí mạng của toàn bộ mạng lưới — nếu Nấm Mẫu bị tiêu diệt, hàng nghìn Nấm Nhánh sẽ mất kết nối và dần chết đi, toàn bộ hệ thống sẽ sụp đổ trong vòng vài tháng. Tuy nhiên, vị trí sâu dưới đất và việc không ai biết đến sự tồn tại của nó khiến mối đe dọa này gần như lý thuyết. Bí mật lớn nhất nằm ở kho ký ức rung động: mạng nấm ghi nhận được mọi bước chân trên Vĩnh Hằng Sâm Lâm suốt hàng nghìn năm — nếu ai tìm cách đọc được ký ức của nấm, sẽ biết mọi bí mật của rừng, bao gồm vị trí kho báu cổ đại, bí mật huyết thống Vương Đình, và thậm chí đường đi của những cường giả đã biến mất từ lâu. Ngoài ra, mối quan hệ cộng sinh giữa Nấm Linh và Mật Ong Linh Đoàn là một trong những bí mật sinh thái ít người biết — hai bên trao đổi dinh dưỡng qua rễ cây, hình thành liên minh tự nhiên mà cả hai có lẽ cũng không ý thức được. Gần đây, mạng nấm ghi nhận một rung động bất thường lặp đi lặp lại từ phía nam Vĩnh Hằng Sâm Lâm — nhịp đều đặn như nhịp tim, nhưng mạnh hơn bất kỳ sinh vật nào từng bước qua rừng. Nấm Mẫu phản ứng bằng cách tăng cường sợi nấm ở khu vực đó gấp ba lần bình thường, như thể đang "quan sát kỹ hơn" — hoặc chuẩn bị phòng thủ. Đáng chú ý hơn, "điểm mù" ở rìa đông nam nơi sợi nấm chết dần — nếu liên kết với rung động bất thường từ phía nam — có thể là dấu hiệu của một mối đe dọa chưa từng có đối với cả Vĩnh Hằng Sâm Lâm lẫn mạng nấm.

## XI. Quan Hệ Thế Lực (势力关系)

Nấm Linh Mạng Lưới tồn tại ngoài mọi bàn cờ quyền lực — không ai biết nó ở đó, nên không ai có quan hệ thực sự với nó. Tinh Linh Vương Đình xây dựng văn minh ngay trên mạng nấm mà hoàn toàn không hay biết, và mạng nấm cũng không can thiệp vào chuyện của họ — nhưng nếu Vương Đình biết rằng mọi cuộc mật đàm trong Vương Cung đều được ghi nhận qua rung động nền đất, hẳn sẽ có một cuộc khủng hoảng chính trị chưa từng có. Mối quan hệ cộng sinh tự nhiên với Mật Ong Linh Đoàn là liên kết gần nhất mà mạng nấm có, dù cả hai bên đều không ý thức đầy đủ về sự hợp tác này. Thần Mộc Ký Sinh Tộc là "đối thủ" tự nhiên duy nhất — ký sinh trùng hút chất dinh dưỡng từ cây chủ, gián tiếp làm suy yếu mạng sợi nấm cộng sinh; tại những khu vực Ký Sinh Tộc hoạt động mạnh, mạng nấm mỏng đi đáng kể, tạo ra "điểm mù" trong hệ thống giám sát ngầm. Về bản chất, Nấm Linh Mạng Lưới giống một lực lượng tự nhiên hơn là một thế lực chính trị, và sự tồn tại bí mật của nó là lớp bảo vệ tốt nhất.
