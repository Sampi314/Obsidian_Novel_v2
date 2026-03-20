---
type: faction
name: Thâm Hải Vi Linh
hantu: 深海微靈
faction_type: Bộ Lạc
alignment: 0
race: Vi Tộc (Sinh vật vi mô biển sâu)
region: Vô Tận Hải
founded: Thượng Cổ (hàng triệu năm trước)
founder: Không rõ — tiến hóa tự nhiên
emblem: Vi_Linh_Phat_Quang.png
specialty: Phát Sáng Linh, truyền tải ký ức bằng ánh sáng, chịu áp suất cực hạn
economy:
  - Không có hoạt động kinh tế — tồn tại độc lập hoàn toàn
arcs:
  - arc: 1
    status: Ẩn cư tuyệt đối
    rank: Không Xếp Hạng
    leader: Thâm Uyên Mẫu Linh (tương đương Trúc Cơ Hậu Kỳ)
    population: 500000000
    territory:
      - Vực Thẳm Vạn Trượng — điểm sâu nhất của Vô Tận Hải
    assets:
      - name: Vực Thẳm Vạn Trượng
        type: Bí Cảnh
      - name: Quần Thể Ý Thức Vi Linh
        type: Tài Nguyên
      - name: Phong ấn bí ẩn dưới đáy vực
        type: Bí Cảnh
    stats: [5, 30, 10, 50, 45, 5]
    divisions:
      - name: Thâm Uyên Mẫu Linh
        role: Cá thể trung tâm, nắm giữ Quần Thể Ý Thức, điều phối toàn bộ mạng lưới Vi Linh
        headcount:
          truong_lao: 1
          chien_binh: 0
          dan_thuong: 0
        members:
          - character: Thâm Uyên Mẫu Linh
            position: Quần Thể Ý Thức Trung Tâm
            cultivation: Tương đương Trúc Cơ Hậu Kỳ
      - name: Vi Linh Đàn
        role: Phân bố khắp vực thẳm, mỗi nhóm kiểm soát một khu vực, truyền tải thông tin bằng ánh sáng
        headcount:
          truong_lao: 0
          chien_binh: 0
          dan_thuong: 500000000
        members:
          - character: "[Các cụm Vi Linh khu vực]"
            position: Đơn vị mạng lưới
            cultivation: Vô cảnh giới (bản năng thuần túy)
            placeholder: true
    relationships:
      - faction: Hải Quy Trưởng Lão Hội
        description: Hải Quy Trưởng Lão Hội biết đến sự tồn tại của Vi Linh qua ký ức cổ đại, nhưng không có cách tiếp cận Vực Thẳm Vạn Trượng.
        diplomacy:
          lien_minh: 0
          tin: 10
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 0
      - faction: Thâm Hải Thám Hiểm Đoàn
        description: Thám Hiểm Đoàn từng lặn sâu nhưng chưa bao giờ đến được nơi Vi Linh sinh sống. Vi Linh không biết đến sự tồn tại của họ.
        diplomacy:
          lien_minh: 0
          tin: 0
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 0
      - faction: Vực Thẳm Ma Cung
        description: Vực Thẳm Ma Cung nằm gần lãnh thổ của Vi Linh. Mỗi khi ma khí từ Ma Cung lan tỏa, Vi Linh đồng loạt rút xa — hai bên không giao tiếp nhưng có sự né tránh bản năng.
        diplomacy:
          lien_minh: -10
          tin: -20
          uy_hiep: 0
          thuong_mai: 0
          on_oan: -10
          le_thuoc: 0
---

# Thâm Hải Vi Linh (深海微靈)

## I. Tổng Quan (总览)

Thâm Hải Vi Linh là một quần thể sinh vật vi mô cổ đại sinh sống tại Vực Thẳm Vạn Trượng — điểm sâu nhất và tối tăm nhất của Vô Tận Hải. Với hàng trăm triệu cá thể kết nối thành một mạng lưới ý thức tập thể, chúng có lẽ là một trong những dạng sống lâu đời nhất trên thế giới. Mỗi cá thể Vi Linh cực nhỏ, phát ra ánh sáng xanh nhạt trong bóng tối vĩnh cửu của vực thẳm — tín hiệu duy nhất cho thấy sự sống tồn tại ở nơi mà áp suất nước có thể nghiền nát cả tu sĩ Kim Đan. Chúng không thuộc bất kỳ hệ thống tu luyện nào, không có chính trị hay chiến tranh, nhưng Quần Thể Ý Thức mà chúng hình thành phức tạp đến mức gần như có "cá tính" — đôi khi tò mò, đôi khi sợ hãi, đặc biệt khi thứ bị phong ấn dưới đáy vực phát ra rung động.

## II. Địa Lý & Tài Nguyên (地理 与 资源)

Thâm Hải Vi Linh cư trú tại Vực Thẳm Vạn Trượng, vùng biển sâu nhất của Vô Tận Hải, nơi nhiệt độ gần đóng băng và ánh sáng mặt trời không bao giờ chạm tới. Áp suất nước ở đây cực lớn, đủ để nghiền nát bất kỳ sinh vật nào từ mặt biển xuống nếu thiếu bảo hộ đặc biệt. Linh khí tại vực thẳm đậm đặc nhưng hỗn loạn, mang đặc tính nguyên thủy hoàn toàn khác với linh khí trên mặt biển — nhiều học giả tin rằng đây là dạng linh khí nguyên sinh từ thời khai thiên lập địa. Bóng tối vĩnh cửu bao trùm toàn bộ khu vực, chỉ có ánh sáng xanh nhạt từ hàng triệu Vi Linh phát sáng, tạo thành những dải ngân hà mờ ảo giữa lòng đại dương. Vực thẳm cũng chứa một phong ấn bí ẩn — thứ gì đó vẫn còn sống đang bị giam giữ dưới tầng đá sâu nhất.

## III. Văn Hóa & Tín Ngưỡng (文化 与 信仰)

Thâm Hải Vi Linh là Vi Tộc biển sâu đã tiến hóa hoàn toàn khác biệt với mọi sinh vật trên mặt biển qua hàng triệu năm cách ly. Chúng không có ngôn ngữ, không có nghi lễ, không có khái niệm văn hóa theo cách mà các chủng tộc thông minh hiểu. Tuy nhiên, Quần Thể Ý Thức của chúng phức tạp hơn bất kỳ Vi Tộc nào khác — chúng có khả năng suy nghĩ đơn giản, ghi nhớ, và thậm chí phản ứng cảm xúc trước các kích thích bên ngoài. Khi toàn bộ quần thể đồng loạt phát sáng theo nhịp, đó là dấu hiệu của "trạng thái suy nghĩ" — hàng trăm triệu cá thể cùng xử lý một thông tin. Chúng biết nhiều bí mật về đáy biển mà không sinh vật nào khác có thể tiếp cận, nhưng không có cách giao tiếp với thế giới bên ngoài.

## IV. Cơ Cấu Tổ Chức (组织结构)

Tổ chức của Thâm Hải Vi Linh không theo bất kỳ mô hình quyền lực nào mà hoàn toàn dựa trên mạng lưới sinh học. Thâm Uyên Mẫu Linh là cá thể lớn nhất và lâu đời nhất, đóng vai trò trung tâm nắm giữ Quần Thể Ý Thức — giống như bộ não cho toàn bộ mạng lưới. Hàng trăm triệu cá thể Vi Linh phân bố khắp vực thẳm, chia thành các cụm khu vực, mỗi cụm kiểm soát một phần của vực. Các cụm này liên lạc với nhau và với Mẫu Linh bằng tín hiệu ánh sáng — mỗi xung sáng mang theo thông tin, ký ức, hoặc cảnh báo. Khi một cụm phát hiện mối nguy, toàn bộ mạng lưới được thông báo trong tích tắc. Đây không phải hệ thống chỉ huy mà là hệ thống cộng sinh — mỗi cá thể vừa độc lập vừa là một phần không thể tách rời của tập thể.

## V. Công Pháp & Trận Pháp (功法 与 阵法)

Thâm Hải Vi Linh không tu luyện công pháp — cơ thể chúng chịu được áp suất cực hạn của vực thẳm nhờ quá trình tiến hóa hàng triệu năm, không phải nhờ linh lực hay pháp thuật. Khả năng đặc trưng nhất của chúng là **Phát Sáng Linh** — ánh sáng phát ra từ cơ thể Vi Linh không chỉ đơn thuần là hiện tượng sinh học mà còn chứa thông tin. Mỗi bước sóng ánh sáng tương ứng với một loại dữ liệu khác nhau, cho phép các nhóm Vi Linh truyền tải ký ức, cảm xúc và cảnh báo cho nhau xuyên qua bóng tối vực thẳm. Khi toàn bộ quần thể đồng loạt phát sáng cực đại, hiện tượng này tạo ra một vùng năng lượng quang học có thể gây rối loạn thần thức cho bất kỳ sinh vật nào tiếp cận — dù đây là phản ứng phòng thủ bản năng, không phải trận pháp có chủ đích.

## VI. Đặc Sản Môn Phái (门派特产)

- **Ánh Sáng Ký Ức:** Ánh sáng phát ra từ Vi Linh có thể lưu giữ ký ức hàng triệu năm. Nếu ai đó tìm được cách giải mã tín hiệu quang học này, họ sẽ tiếp cận được kho tàng kiến thức về lịch sử đại dương từ thời thượng cổ.
- **Thể Dịch Vi Linh:** Dịch thể trong suốt mà Vi Linh tiết ra có đặc tính chống áp suất cực mạnh. Về mặt lý thuyết, nếu thu thập được số lượng lớn, có thể dùng để chế tạo pháp khí chịu áp suất biển sâu — nhưng chưa ai từng thu thập thành công.
- **Linh Khí Nguyên Sinh:** Linh khí tại Vực Thẳm Vạn Trượng mang đặc tính nguyên thủy, khác biệt hoàn toàn với linh khí trên mặt biển. Các nhà nghiên cứu tin rằng nghiên cứu loại linh khí này có thể mở ra hiểu biết mới về nguồn gốc của tu luyện.

## VII. Cơ Sở Hạ Tầng (基础设施)

Thâm Hải Vi Linh không có cơ sở hạ tầng theo nghĩa thông thường. Toàn bộ "cấu trúc" của chúng là tự nhiên — các khe đá, hang động và địa hình vực thẳm tạo thành không gian sống. Mẫu Linh cư trú tại điểm sâu nhất của vực, nơi áp suất mạnh nhất nhưng linh khí cũng đậm đặc nhất. Xung quanh vị trí của Mẫu Linh, mật độ Vi Linh cao nhất, tạo thành một "lõi sáng" mờ ảo có thể nhìn thấy từ khoảng cách hàng trăm trượng. Phong ấn bí ẩn dưới đáy vực nằm bên dưới nơi Mẫu Linh cư trú — không rõ đây là trùng hợp hay Mẫu Linh cố ý canh giữ.

## VIII. Kinh Tế (经济)

Thâm Hải Vi Linh không có bất kỳ hoạt động kinh tế nào. Chúng tồn tại hoàn toàn độc lập, không giao thương, không sản xuất, không tiêu thụ theo cách mà các thế lực thông thường hiểu. Thức ăn của chúng là linh khí nguyên sinh hòa tan trong nước vực thẳm và các vi sinh vật đáy biển. Sự tồn tại của chúng là một vòng tuần hoàn khép kín hoàn hảo — sinh ra, hấp thu linh khí, phát sáng, truyền tải ký ức, rồi tan biến. Tuy nhiên, đối với thế giới bên ngoài, bản thân Vi Linh là một "tài nguyên" tiềm năng vô giá — dịch thể, ánh sáng ký ức, và linh khí nguyên sinh đều là thứ mà nhiều thế lực sẽ sẵn sàng giết để có được, nếu họ tìm được cách xuống vực thẳm.

## IX. Lịch Sử Tóm Tắt (简史)

Thâm Hải Vi Linh có thể là một trong những sinh vật cổ nhất trên đời — tuổi thọ của quần thể được ước tính bằng đơn vị triệu năm. Chúng đã tồn tại trước khi bất kỳ tông môn nào được thành lập, trước khi Hải Thần Cung nổi lên, thậm chí có thể trước khi các chủng tộc thông minh xuất hiện. Quần Thể Ý Thức của Mẫu Linh lưu giữ ký ức về những sự kiện mà không còn ai nhớ — sự hình thành của Vô Tận Hải, sự sụp đổ của các nền văn minh cổ đại, và thời khắc phong ấn dưới đáy vực được tạo ra. Chúng chưa bao giờ tiếp xúc với bất kỳ thế lực nào trên mặt biển — vực thẳm quá sâu để bất kỳ ai đến được. Thâm Hải Thám Hiểm Đoàn từng lặn sâu nhưng vẫn cách nơi Vi Linh sinh sống hàng nghìn trượng. Hải Quy Trưởng Lão Hội biết đến sự tồn tại của chúng qua ký ức cổ đại truyền từ đời này sang đời khác, nhưng cũng không có cách tiếp cận.

## X. Giai Thoại & Bí Mật (轶事 与 秘密)

Thâm Uyên Mẫu Linh lưu giữ ký ức về thứ gì đó bị phong ấn dưới đáy vực — thứ đó vẫn còn sống sau hàng triệu năm giam cầm. Không ai biết đó là gì — một thần linh cổ đại, một ma vật, hay thứ gì đó vượt ngoài mọi phân loại. Ánh sáng xanh mà Vi Linh phát ra đôi khi tự động sắp xếp thành hình ảnh — có nhà nghiên cứu (dựa trên ghi chép gián tiếp) tin rằng đó là bản đồ của thế giới cổ đại, vẽ lại địa hình từ triệu năm trước khi biển nhấn chìm mọi thứ. Điều đáng sợ nhất là phản ứng của Vi Linh trước phong ấn: mỗi khi thứ bị giam phát ra rung động, toàn bộ hàng trăm triệu Vi Linh đồng loạt tắt sáng như thể sợ hãi — bóng tối hoàn toàn bao trùm vực thẳm trong vài khắc trước khi chúng dám phát sáng trở lại.

## XI. Quan Hệ Thế Lực (势力关系)

- **Hải Quy Trưởng Lão Hội:** Hải Quy Trưởng Lão biết đến sự tồn tại của Vi Linh qua ký ức truyền thừa cổ đại, nhưng hai bên chưa bao giờ tiếp xúc trực tiếp. Đối với Trưởng Lão Hội, Vi Linh là bằng chứng sống về quá khứ xa xôi của đại dương.
- **Thâm Hải Thám Hiểm Đoàn:** Lục Thâm Hải từng nghe truyền thuyết về "ánh sáng dưới vực thẳm" và khao khát lặn đủ sâu để chứng kiến, nhưng với thiết bị hiện tại, vực thẳm vẫn nằm ngoài tầm với.
- **Vực Thẳm Ma Cung:** Ma khí từ Vực Thẳm Ma Cung đôi khi lan tỏa sang lãnh thổ Vi Linh. Mỗi lần như vậy, các cụm Vi Linh gần nhất tự động rút xa — một phản ứng phòng thủ bản năng cho thấy ma khí có hại cho chúng.
