---
type: faction
name: Hải Miên Trùng Xã
hantu: 海绵虫社
faction_type: Bộ Lạc
alignment: 4
race: Trùng Tộc (Bọt Biển Linh)
region: Vô Tận Hải
founded: Thượng Cổ (tự sinh)
founder: Không có (hình thành tự nhiên)
emblem: Hai_Mien_Trung_Xa.png
specialty: Lọc nước biển, Sản sinh linh khí thuần, Cộng sinh hệ sinh thái
economy:
- Không có hoạt động kinh tế (sinh vật bất động)
arcs:
  - arc: 1
    status: Tồn tại bị động, đang bị đe dọa ở vùng nam
    rank: Không Xếp Hạng
    leader: Miên Mẫu
    population: 0
    territory:
      - Rạn san hô phía đông Vô Tận Hải
    assets:
      - name: Miên Mẫu (Bọt biển linh cổ thụ)
        type: Tài Nguyên
      - name: Hệ thống lọc nước tự nhiên
        type: Công Trình
    stats: [5, 15, 10, 30, 8, 5]
    divisions:
      - name: Quần Thể Bọt Biển Linh
        role: Lọc nước biển, hấp thụ tạp chất và linh khí ô nhiễm
        headcount:
          truong_lao: 1
          chien_binh: 0
          dan_thuong: 0
        members:
          - character: Miên Mẫu
            position: Bọt Biển Cổ Thụ / Lõi Quần Thể
            cultivation: Luyện Khí (tương đương)
    relationships:
      - faction: Hải Tảo Nông Dân Hội
        description: Mối quan hệ cộng sinh trực tiếp. Hải Tảo Nông Dân Hội phụ thuộc vào nước sạch do bọt biển lọc để trồng tảo linh, đổi lại tảo chết trở thành dinh dưỡng cho bọt biển.
        diplomacy:
          lien_minh: 50
          tin: 40
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 20
          le_thuoc: 0
      - faction: San Hô Đảo Quốc
        description: Bọt biển linh là thành phần không thể thiếu của rạn san hô — nền tảng sinh thái mà San Hô Đảo Quốc xây dựng trên đó. Đảo Quốc biết ơn nhưng chưa bao giờ chủ động bảo vệ.
        diplomacy:
          lien_minh: 30
          tin: 35
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 10
          le_thuoc: 0
      - faction: Hải Khuẩn Tịnh Hóa Đội
        description: Hai sinh vật cùng vai trò thanh lọc môi trường biển. Bọt biển lọc tạp chất, Hải Khuẩn phân giải độc tố — cộng sinh tự nhiên không cần giao tiếp.
        diplomacy:
          lien_minh: 30
          tin: 20
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 10
          le_thuoc: 0
---

# HẢI MIÊN TRÙNG XÃ (海绵虫社)

> *"Nước biển đục đến đâu, qua thân ta rồi cũng trong. Chẳng ai nhớ kẻ lọc nước, nhưng ai cũng cần nước trong."*
> — Lời vô thanh của Miên Mẫu, ghi lại bởi một dược sư biển vô danh đời Trung Cổ

## I. Tổng Quan (总览)
Hải Miên Trùng Xã là quần thể bọt biển linh — Trùng Tộc bất động, sống cố định trên rạn san hô phía đông Vô Tận Hải suốt hàng nghìn năm. Đây không phải một thế lực theo nghĩa thông thường, mà là một hệ sinh thái thu nhỏ, nơi hàng nghìn bọt biển linh âm thầm lọc nước biển, hấp thụ tạp chất và linh khí ô nhiễm, rồi giải phóng dòng nước trong lành giàu linh khí thuần tịnh. Đứng đầu — nếu có thể gọi như vậy — là Miên Mẫu, bọt biển linh lớn nhất có kích thước bằng chiếc thuyền nhỏ, đã lọc nước liên tục hàng nghìn năm không ngừng nghỉ. Trong cả đại dương Vô Tận Hải, không một sinh vật nào khác có thể thay thế vai trò mà Hải Miên Trùng Xã nắm giữ — chúng là trái tim thanh lọc của biển cả, dù trái tim ấy chẳng bao giờ biết đập.

## II. Địa Lý & Tài Nguyên (地理 与 资源)
Hải Miên Trùng Xã phân bố trên các rạn san hô phía đông Vô Tận Hải, bám chặt vào bề mặt đá ngầm và san hô chết, trải dài từ Đông Hải Nham — dải đá ngầm lớn nhất vùng biển đông — đến tận Ngọc Tảo Bình Nguyên phía nam. Khu vực trung tâm nơi Miên Mẫu tọa lạc được gọi là Thanh Thủy Uyên, nổi tiếng với nước trong vắt đến tận đáy, linh khí ổn định, là môi trường lý tưởng cho bọt biển linh phát triển. Bọt biển hấp thụ nước biển qua hệ thống lỗ nhỏ trên thân, lọc ra tạp chất và linh khí ô nhiễm, rồi thải ra nước sạch hơn và giàu linh khí thuần. Nước sau khi lọc trong sạch đến mức nhiều sinh vật biển — từ cá linh đến tôm hùm biển sâu — chủ động tìm đến khu vực bọt biển để "uống" và hấp thụ linh khí. Tài nguyên riêng của quần thể gần như không có, nhưng sự tồn tại của chúng chính là "tài nguyên" lớn nhất cho toàn bộ hệ sinh thái rạn san hô. Dòng hải lưu ấm Đông Phong mang phù sa từ khắp nơi đổ về, cung cấp nguồn dinh dưỡng vô tận cho quần thể.

## III. Văn Hóa & Tín Ngưỡng (文化 与 信仰)
Bọt biển linh là sinh vật bất động, sống cố định một chỗ suốt đời, không có văn hóa hay tín ngưỡng theo bất kỳ định nghĩa nào của các chủng tộc có tri giác. Tồn tại và lọc nước là bản năng duy nhất, là toàn bộ ý nghĩa sinh tồn của chúng. Tuy nhiên, điều kỳ lạ là các Hải Tộc khác lại tự phát hình thành tín ngưỡng xung quanh bọt biển — nhiều ngư dân Hải Tộc coi chúng là "thần lọc nước," thường xuyên cầu nguyện trước khi đi qua vùng bọt biển. Các bộ lạc ven rạn san hô có tục lệ "không được hái bọt biển linh" — dù không ai chính thức ban hành luật, đó là quy ước bất thành văn mà mọi sinh vật biển đều hiểu. Vào mỗi dịp Hải Triều Đại Lễ — ngày nước triều dâng cao nhất trong năm — ngư dân Hải Tảo Nông Dân Hội thả tảo linh tươi xuống vùng bọt biển như lễ vật tạ ơn, gọi là "Hoàn Miên Tế." Nghịch lý là: chúng được biết ơn nhưng không bao giờ được bảo vệ chủ động.

## IV. Cơ Cấu Tổ Chức (组织结构)
Hải Miên Trùng Xã không có hệ thống tổ chức theo nghĩa thông thường. Miên Mẫu — bọt biển linh lớn nhất — có kích thước bằng chiếc thuyền nhỏ, nằm ở trung tâm rạn san hô tại Thanh Thủy Uyên, là cá thể cổ xưa nhất và hấp thụ nhiều nhất. Xung quanh là hàng nghìn bọt biển linh nhỏ hơn, kích thước từ nắm tay đến chiếc bàn, phân bố đều trên mặt đá ngầm, tạo thành ba vòng đồng tâm mà ngư dân gọi là Nội Miên, Trung Miên, và Ngoại Miên. Không có quan hệ chỉ huy — mỗi bọt biển tự lọc nước trong khu vực của mình một cách độc lập. Sinh sản bằng phân chia — cứ vài chục năm, khi bọt biển lớn tích lũy đủ dinh dưỡng, nó tách thành hai con nhỏ hơn, dần dần phát triển lại. Quá trình này diễn ra cực kỳ chậm, khiến việc phục hồi quần thể sau khi bị tàn phá cần hàng trăm năm. Có ghi nhận cho thấy Miên Mẫu chưa bao giờ phân chia — như thể nó đã vượt qua giới hạn sinh học và trở thành một thực thể duy nhất, không thể thay thế.

## V. Công Pháp & Trận Pháp (功法 与 阵法)
Bọt biển linh không tu luyện công pháp — lọc nước là quá trình sinh học tự nhiên được linh khí bản thể tăng cường theo thời gian. Cơ chế phòng thủ duy nhất là khi bị tấn công, bọt biển co lại và tiết ra chất nhầy đắng — không gây thương tích nhưng mùi cực kỳ khó chịu, đủ để xua đuổi hầu hết kẻ tấn công thông thường. Chất nhầy này được gọi là "Hải Miên Khổ Dịch," có thể bám dính lên da và vảy suốt nhiều ngày, khiến sinh vật bị dính trở thành đối tượng xa lánh của đồng loại vì mùi hôi. Miên Mẫu có khả năng đặc biệt hơn — có thể hút nước mạnh tạo ra xoáy nhỏ xung quanh, được gọi là "Miên Mẫu Hấp Lực Trường," đủ sức cuốn cá nhỏ vào trong thân để tiêu hóa nhưng hoàn toàn vô hại với bất kỳ tu sĩ nào dù ở cảnh giới thấp nhất. Nói cách khác, bọt biển linh gần như không có khả năng tự vệ trước bất kỳ mối đe dọa có chủ đích nào — sự yếu đuối tuyệt đối này chính là bi kịch lớn nhất của chúng.

## VI. Đặc Sản Môn Phái (门派特产)
Bọt biển linh không chủ đích tạo ra sản phẩm, nhưng bản thân chúng và các phụ phẩm sinh học đều có giá trị nhất định. **Hải Miên Khổ Dịch** — chất nhầy bọt biển linh sau khi phơi khô — trở thành dược liệu giải độc cấp thấp mang tên "Khổ Miên Tán," được một số dược sư biển thu mua với giá hai linh thạch hạ phẩm mỗi lạng. **Miên Cốt Tịnh Lọc Thạch** — mảnh bọt biển linh khô sau khi bọt biển chết tự nhiên — có đặc tính hấp thụ độc tố, dùng để chế tạo bộ lọc cho pháp khí tịnh hóa nước, rất được trận sư và đan sư chuyên về thủy hệ ưa chuộng. **Miên Mẫu Phấn** — lớp bột mịn bong ra từ bề mặt Miên Mẫu mỗi mùa xuân — chứa linh khí thuần tịnh cô đặc, có tác dụng thanh lọc kinh mạch khi pha vào nước uống. Tuy nhiên, giá trị lớn nhất nằm ở Miên Mẫu — truyền thuyết kể rằng bên trong cơ thể bọt biển cổ thụ nghìn năm đã tích tụ tinh hoa của mọi thứ từng qua nước biển, kết tinh thành viên "Hải Miên Nội Đan" có giá trị ngang ngọc trai thượng phẩm.

## VII. Cơ Sở Hạ Tầng (基础设施)
Cơ sở hạ tầng của Hải Miên Trùng Xã chính là hệ sinh thái rạn san hô mà chúng bám vào. Bề mặt đá ngầm, san hô chết và san hô sống tạo thành nền tảng vật lý cho bọt biển linh gắn kết, trải dài suốt dải Đông Hải Nham dài hơn trăm dặm. Không có bất kỳ công trình nhân tạo nào — mọi thứ đều tự nhiên và hình thành qua hàng nghìn năm. Miên Mẫu tọa lạc trên "Thiên Niên Nham" — một tảng đá ngầm lớn ở trung tâm Thanh Thủy Uyên, xung quanh là quần thể bọt biển nhỏ hơn phân bố tỏa ra mọi hướng. Phía bắc rạn có "Tĩnh Lưu Hẻm" — nơi dòng hải lưu chậm lại, tạo vùng nước lặng cho bọt biển non bám rễ và phát triển, đóng vai trò như "vườn ươm" tự nhiên. Dòng hải lưu tự nhiên đưa nước ô nhiễm từ các vùng biển khác đến khu vực bọt biển, và mang nước sạch đi phân phối ra xung quanh — tạo thành "nhà máy lọc nước" tự nhiên hoạt động không ngừng nghỉ.

## VIII. Kinh Tế (经济)
Hải Miên Trùng Xã không tham gia vào bất kỳ hoạt động kinh tế nào. Chúng không sản xuất, không trao đổi, không tích trữ — tồn tại thuần túy theo bản năng sinh học. Tuy nhiên, giá trị kinh tế gián tiếp của quần thể là vô cùng lớn, ước tính bằng toàn bộ sản lượng nông nghiệp thủy sinh của vùng rạn san hô phía đông. Nước sạch do bọt biển lọc là nền tảng cho toàn bộ hệ sinh thái rạn san hô — nơi cung cấp thực phẩm, dược liệu và nguyên vật liệu cho hàng chục Hải Tộc sinh sống. Hải Tảo Nông Dân Hội phụ thuộc trực tiếp vào nước sạch do bọt biển lọc để trồng tảo linh, đặc biệt là giống Ngọc Tảo quý hiếm chỉ sống được trong nước có độ thuần tịnh cực cao. Khi một vùng bọt biển bị tận diệt, nước biển khu đó ô nhiễm nghiêm trọng, khiến toàn bộ chuỗi kinh tế biển trong khu vực sụp đổ dây chuyền — bài học đau thương từ vụ Đoạn Miên Sự Biến hai trăm năm trước vẫn còn ám ảnh các Hải Tộc.

## IX. Lịch Sử Tóm Tắt (简史)
Bọt biển linh tồn tại từ thời thượng cổ, là một trong những sinh vật cổ xưa nhất của Vô Tận Hải, luôn đóng vai trò thành phần quan trọng không thể thay thế trong hệ sinh thái rạn san hô. Trong suốt lịch sử, không ai coi chúng là "thế lực" — cho đến khi xảy ra Đoạn Miên Sự Biến cách đây hai trăm năm: một vùng bọt biển rộng mười dặm tại Ngọc Tảo Bình Nguyên bị tận diệt do thợ săn dược liệu Hoàng gia khai thác quá mức nhằm thu Hải Miên Nội Đan. Nước biển khu đó ô nhiễm nghiêm trọng trong thời gian ngắn, tảo linh chết sạch, cá linh bỏ đi, và ba trăm hộ ngư dân Hải Tộc buộc phải di cư. Sự kiện đó khiến Hải Thần Cung ban lệnh "Cấm Hại Miên Linh" — nhưng lệnh thiếu cơ chế thực thi, và vi phạm vẫn thỉnh thoảng xảy ra, đặc biệt từ tà tu và thương nhân tham lam. Gần đây, bọt biển linh ở vùng biển nam bắt đầu chết dần vì Huyết Độc lan đến — dấu hiệu đầu tiên xuất hiện vào mùa thu năm trước khi ngư dân phát hiện hàng trăm bọt biển chuyển sang màu đen tại rạn Nam Miên.

## X. Giai Thoại & Bí Mật (轶事 与 秘密)
Miên Mẫu đã lọc nước liên tục hàng nghìn năm — bên trong cơ thể khổng lồ của nó tích tụ tinh hoa của vô số vật chất từng qua nước biển. Có giả thuyết cho rằng nếu mổ Miên Mẫu ra, bên trong sẽ chứa một viên nội đan tinh hoa cô đọng — "Hải Miên Vạn Niên Đan" — giá trị ngang hoặc vượt ngọc trai thượng phẩm, có thể giúp tu sĩ đột phá cảnh giới nhờ linh khí thuần tịnh tích lũy hàng thiên niên kỷ. Một dược sư tên Huyền Hải Ông từng tuyên bố rằng viên nội đan này có thể thanh lọc mọi ô nhiễm trong cơ thể tu sĩ, kể cả tẩu hỏa nhập ma. Tuy nhiên, giết Miên Mẫu đồng nghĩa hủy hoại nguồn nước sạch cho cả vùng rạn san hô rộng lớn — hậu quả sinh thái khó lường trong hàng trăm năm. Đáng lo ngại, đã có không ít tà tu và thương nhân tham lam dòm ngó Miên Mẫu, trong đó nguy hiểm nhất là một tổ chức bí ẩn tự xưng "Tịnh Thủy Hội" chuyên thu gom phụ phẩm bọt biển linh với số lượng lớn bất thường. Ngoài ra, bọt biển linh ở vùng biển nam đang chết dần vì Huyết Độc — nước vùng đó ngày càng đục, sinh vật bắt đầu di cư ồ ạt, và nếu xu hướng này tiếp tục, cả hệ sinh thái biển nam sẽ sụp đổ. Điều bí ẩn nhất là Miên Mẫu gần đây bắt đầu thay đổi màu sắc — từ trắng ngà sang phớt xanh — như thể đang phản ứng với điều gì đó mà chưa sinh vật nào hiểu được.

## XI. Quan Hệ Thế Lực (势力关系)
Hải Miên Trùng Xã không có khả năng ngoại giao, nhưng mối quan hệ sinh thái của chúng là rõ ràng và thiết yếu, tạo thành mạng lưới phụ thuộc phức tạp trên toàn vùng rạn san hô phía đông. Hải Tảo Nông Dân Hội là đối tác cộng sinh trực tiếp nhất — nước sạch nuôi tảo linh, tảo chết nuôi bọt biển, vòng tuần hoàn hoàn hảo mà cả hai bên đều không thể thiếu; Hội Trưởng Tảo Nông từng nói: "Mất bọt biển, mất tất cả." San Hô Đảo Quốc xây dựng toàn bộ vương quốc trên hệ sinh thái mà bọt biển linh duy trì, nhưng chưa bao giờ chủ động bảo vệ quần thể bọt biển khỏi kẻ khai thác — sự thờ ơ này có thể trở thành sai lầm lịch sử khi Huyết Độc lan đến. Hải Khuẩn Tịnh Hóa Đội chia sẻ vai trò thanh lọc môi trường — bọt biển lọc tạp chất thông thường, Hải Khuẩn phân giải độc tố nặng, tạo thành hệ thống phòng thủ sinh thái hai lớp mà ngư dân gọi là "Song Tịnh Bích Lũy." Mối đe dọa lớn nhất đến từ Huyết Độc lan từ phương nam và lòng tham của những kẻ muốn khai thác Miên Mẫu — cả hai đều không thể chống lại bằng chất nhầy đắng.
