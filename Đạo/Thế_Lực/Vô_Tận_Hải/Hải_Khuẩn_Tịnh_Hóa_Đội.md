---
type: faction
name: Hải Khuẩn Tịnh Hóa Đội
hantu: 海菌净化队
faction_type: Bộ Lạc
alignment: 5
race: Vi Tộc (Khuẩn Biển Linh)
region: Vô Tận Hải
founded: Thượng Cổ (tự sinh)
founder: Không có (hình thành tự nhiên)
emblem: Hai_Khuan_Tinh_Hoa.png
specialty: Phân giải Huyết Độc, Tịnh hóa nước biển, Quần Thể Ý Thức
economy:
- Không có hoạt động kinh tế (sinh vật bản năng)
arcs:
  - arc: 1
    status: Đang bị áp đảo bởi Huyết Độc
    rank: Không Xếp Hạng
    leader: Tịnh Hóa Chủ (Khuẩn Mẫu)
    population: 0
    territory:
      - Vùng biển nam Vô Tận Hải (giáp ranh Nam Cương)
    assets:
      - name: Quần Thể Ý Thức
        type: Trận Pháp
      - name: Enzym Tịnh Hóa
        type: Tài Nguyên
    stats: [10, 5, 10, 50, 15, 5]
    divisions:
      - name: Khuẩn Đội Chính
        role: Phân giải Huyết Độc tại các khu vực ô nhiễm nặng nhất
        headcount:
          truong_lao: 1
          chien_binh: 0
          dan_thuong: 0
        members:
          - character: Tịnh Hóa Chủ
            position: Khuẩn Mẫu / Điều phối Quần Thể
            cultivation: Trúc Cơ (tương đương)
      - name: Khuẩn Đội Tiền Tuyến
        role: Hoạt động tại ranh giới ô nhiễm mở rộng, hy sinh cao
        headcount:
          truong_lao: 0
          chien_binh: 0
          dan_thuong: 0
        members:
          - character: "[Khuẩn Đội Trưởng Tiền Tuyến]"
            position: Khuẩn Mẫu Phụ
            cultivation: Luyện Khí (tương đương)
            placeholder: true
    relationships:
      - faction: San Hô Đảo Quốc
        description: Đồng minh sinh thái tự nhiên. San Hô Thủ Hộ Đoàn của San Hô Đảo Quốc phối hợp với Hải Khuẩn chống ô nhiễm ở tuyến đầu, bảo vệ rạn san hô khỏi Huyết Độc.
        diplomacy:
          lien_minh: 60
          tin: 50
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 30
          le_thuoc: 0
      - faction: Hải Thần Cung
        description: Hải Thần Cung biết đến sự tồn tại của Hải Khuẩn nhưng không can thiệp, giữ thái độ "để tự nhiên xử lý." Không có giao tiếp trực tiếp.
        diplomacy:
          lien_minh: 0
          tin: 10
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 0
      - faction: Hải Miên Trùng Xã
        description: Hai sinh vật cùng đóng vai trò lọc sạch môi trường biển. Hải Khuẩn phân giải độc tố, Hải Miên lọc tạp chất — mối quan hệ cộng sinh tự nhiên không cần giao tiếp.
        diplomacy:
          lien_minh: 30
          tin: 20
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 10
          le_thuoc: 0
---

# HẢI KHUẨN TỊNH HÓA ĐỘI (海菌净化队)

> *"Đại dương không tự chữa lành — mà có kẻ âm thầm chữa lành cho nó."*
> — Trích lời Hải Quy trưởng lão Huyền Quy khi bàn về vai trò sinh thái Vô Tận Hải

## I. Tổng Quan (总览)
Hải Khuẩn Tịnh Hóa Đội là quần thể vi sinh vật linh — khuẩn biển chuyên phân giải chất độc trong nước — hoạt động tại vùng biển nam Vô Tận Hải giáp ranh Nam Cương. Đây không phải một tổ chức theo nghĩa thông thường, mà là một quần thể sinh vật bản năng, khi tập hợp đủ số lượng sẽ hình thành Quần Thể Ý Thức giản đơn có khả năng phối hợp hành động. Tịnh Hóa Chủ — Khuẩn Mẫu lớn nhất — đóng vai trò trung tâm điều phối, dẫn dắt hàng tỷ Hải Khuẩn nhỏ bé thực hiện "sứ mệnh thiên sinh" là thanh lọc đại dương khỏi Huyết Độc đang lan tràn từ Nam Cương. Trong bảng xếp hạng thế lực, không ai liệt kê Hải Khuẩn vào danh sách — nhưng nếu một ngày chúng biến mất, toàn bộ nền kinh tế biển sẽ sụp đổ nhanh hơn bất kỳ cuộc chiến tranh nào có thể gây ra.

## II. Địa Lý & Tài Nguyên (地理 与 资源)
Hải Khuẩn Tịnh Hóa Đội hoạt động tại vùng biển nam Vô Tận Hải — khu vực bị ô nhiễm Huyết Độc nặng nhất, nơi nước biển chuyển sang màu đỏ sẫm đáng sợ. Huyết Độc từ Nam Cương rò rỉ ra biển qua các mạch nước ngầm và hải lưu, tạo thành một vùng "biển đỏ" ngày càng mở rộng, dân biển gọi là Xích Triều Vực. Linh khí trong khu vực bị vẩn đục nghiêm trọng, sinh vật thường gặp đột biến kỳ quái — cá mọc thêm mắt, rong biển tiết dịch đen, ốc sên biển di chuyển theo vòng tròn vô tận cho đến chết. Hải Khuẩn sống nhờ phân giải Huyết Độc — chất độc là "thức ăn" nuôi sống chúng nhưng đồng thời cũng là mối nguy khi nồng độ quá cao, vượt ngưỡng hấp thụ sẽ khiến khuẩn bị đột biến ngược. Ranh giới ô nhiễm mở rộng mỗi năm khoảng ba dặm về phía bắc, buộc Hải Khuẩn phải liên tục di chuyển theo để duy trì phòng tuyến thanh lọc mà ngư dân gọi là "Dải Xanh Cuối Cùng" — một dải nước biển xanh lục mỏng manh nằm giữa biển đỏ phía nam và biển xanh phía bắc, ranh giới mong manh giữa sự sống và cái chết.

## III. Văn Hóa & Tín Ngưỡng (文化 与 信仰)
Hải Khuẩn là Vi Tộc khuẩn biển — sinh vật cực nhỏ không có văn hóa hay tín ngưỡng theo nghĩa thông thường. Tuy nhiên, khi tập hợp đủ số lượng, chúng hình thành Quần Thể Ý Thức giản đơn, cho phép phối hợp hành động ở mức độ bản năng cao — một dạng trí tuệ tập thể mà các học giả Hải Quy Trưởng Lão Hội gọi là "Vô Ngã Chi Trí," trí tuệ không có cái tôi. Chúng coi việc thanh lọc Huyết Độc là "sứ mệnh thiên sinh" — bản năng sâu xa nhất thôi thúc chúng tìm đến bất cứ nơi nào có ô nhiễm, giống như lửa tìm đến gỗ khô. Các Hải Tộc khác nhận ra vai trò quan trọng của Hải Khuẩn trong việc duy trì sự sạch sẽ của đại dương, nhưng hiếm ai coi chúng là "thế lực" đúng nghĩa — cho đến khi chứng kiến hậu quả khi một vùng Hải Khuẩn bị tận diệt: nước biển đổi màu, cá chết nổi trắng mặt biển, và mùi tanh thối lan ra hàng chục dặm. Trong dân gian Hải Tộc có câu: "Khi biển xanh thì quên khuẩn, khi biển đỏ thì nhớ ơn" — nhưng cũng chỉ dừng lại ở mức nhớ ơn, không ai giúp đỡ thực sự. Thủy Linh Nhi từng giận dữ nói trong hội nghị San Hô Đảo Quốc: "Các ngươi uống nước sạch mỗi ngày mà quên ai đã lọc nước cho mình."

## IV. Cơ Cấu Tổ Chức (组织结构)
Tổ chức của Hải Khuẩn Tịnh Hóa Đội hoạt động hoàn toàn theo bản năng sinh học, không có hệ thống thứ bậc theo nghĩa xã hội. Tịnh Hóa Chủ — Khuẩn Mẫu lớn nhất, kích thước bằng chiếc thuyền nhỏ — là trung tâm phát sóng điều phối, xác định hướng thanh lọc và phân bổ quần thể đến các khu vực ô nhiễm nặng. Hàng tỷ Hải Khuẩn nhỏ bé chia thành các nhóm tự động theo khu vực ô nhiễm, mỗi nhóm có một Khuẩn Mẫu Phụ đóng vai trò trung chuyển tín hiệu — hiện tại có bảy Khuẩn Mẫu Phụ phân bố dọc Dải Xanh Cuối Cùng, mỗi vị phụ trách một đoạn dài khoảng mười lăm dặm. Hoạt động không cần chỉ huy chi tiết — mỗi Hải Khuẩn tự nhận biết nồng độ Huyết Độc xung quanh và di chuyển đến nơi cần thiết. Khu vực Hải Khuẩn hoạt động có mùi tanh đặc trưng — đó là dấu hiệu nhận biết vùng ô nhiễm đang được xử lý, và cũng là mùi mà ngư dân kinh nghiệm dùng để phân biệt vùng biển an toàn với vùng biển chết.

## V. Công Pháp & Trận Pháp (功法 与 阵法)
Hải Khuẩn không tu luyện công pháp — việc phân giải Huyết Độc là quá trình sinh học tự nhiên được tăng cường bởi linh khí bản thể. Mỗi Hải Khuẩn hấp thụ Huyết Độc qua màng tế bào, chuyển hóa thành chất vô hại và giải phóng linh khí thuần tịnh trở lại nước biển — quá trình này mà Hải Quy trưởng lão gọi là "Thiên Nhiên Tịnh Hóa Pháp." Khi gặp nồng độ Huyết Độc quá cao vượt ngưỡng xử lý, Hải Khuẩn sẽ kích hoạt cơ chế tự hủy — tự phát nổ phóng thích enzym tịnh hóa cô đặc, hy sinh bản thân để trung hòa một lượng lớn Huyết Độc trong khoảnh khắc. Đây là chiến thuật "hy sinh cá nhân vì tập thể" mà Quần Thể Ý Thức điều phối khi tình hình nghiêm trọng. Mỗi lần tự hủy hàng loạt, mặt biển bùng lên ánh sáng xanh lục nhạt kéo dài vài khắc — ngư dân gọi hiện tượng này là "Lệ Khuẩn Quang," dấu hiệu đáng buồn cho thấy phòng tuyến đang bị ép đến giới hạn. Gần đây, Lệ Khuẩn Quang xuất hiện ngày càng thường xuyên — từ mỗi tháng một lần tăng lên mỗi tuần, khiến ngư dân vùng biên thùy hoang mang rời bỏ ngư trường.

## VI. Đặc Sản Môn Phái (门派特产)
Hải Khuẩn Tịnh Hóa Đội không sản xuất bất kỳ sản phẩm nào có chủ đích, nhưng quá trình thanh lọc tạo ra một số phụ phẩm có giá trị. Linh khí thuần tịnh được giải phóng sau khi phân giải Huyết Độc có chất lượng cao hơn linh khí thông thường — dược sư gọi loại linh khí này là "Tịnh Linh Khí" — thu hút nhiều sinh vật biển đến khu vực vừa được lọc sạch. Xác Hải Khuẩn sau khi tự hủy kết tinh thành một loại bột mịn gọi là "Tịnh Hóa Sa," có tác dụng trung hòa độc tố khi pha vào nước, đặc biệt hiệu quả đối với huyết độc cấp thấp và nọc xà biển. Một số dược sư biển đã thu thập Tịnh Hóa Sa làm nguyên liệu giải độc, nhưng nguồn cung rất hạn chế và quá trình thu thập nguy hiểm — phải lặn sâu vào vùng Xích Triều Vực trong lúc khuẩn đang tự hủy. Ngoài ra, trong lớp trầm tích dưới phòng tuyến thanh lọc, đôi khi tìm thấy "Tịnh Khuẩn Thạch" — viên đá nhỏ bằng ngón tay cái được tạo thành từ hàng triệu xác khuẩn hóa thạch nén chặt, chứa enzym tịnh hóa cô đặc, là nguyên liệu quý trong luyện đan giải độc cấp cao mà chỉ Hải Thảo Dược Sư mới biết cách sử dụng.

## VII. Cơ Sở Hạ Tầng (基础设施)
Hải Khuẩn Tịnh Hóa Đội không có cơ sở hạ tầng nhân tạo. Nơi chúng tập trung hoạt động chính là vùng ranh giới ô nhiễm — một dải biển dài hơn trăm dặm và rộng chừng nửa dặm, nơi nước đỏ sẫm dần chuyển sang trong xanh, ngư dân gọi ranh giới đó là "Tuyến Tịnh." Từ trên cao nhìn xuống, Tuyến Tịnh trông như một sợi chỉ xanh mỏng manh ngăn cách hai thế giới — một bên là biển sống, một bên là biển chết. Tịnh Hóa Chủ thường tọa lạc tại trung tâm phòng tuyến, bám trên một tảng đá ngầm lớn tên Hải Khuẩn Đài gần đáy biển, từ đó phát sóng điều phối ra toàn bộ quần thể. Các Khuẩn Mẫu Phụ phân bố dọc phòng tuyến cách nhau khoảng mười dặm, mỗi Mẫu Phụ phụ trách một đoạn ranh giới. Hệ thống này tự dịch chuyển theo sự mở rộng của vùng ô nhiễm, khiến "phòng tuyến" luôn ở trạng thái linh hoạt — đôi khi thuyền của ngư dân cắm cọc ở Tuyến Tịnh hôm trước, hôm sau đã nằm trong vùng đỏ vì ranh giới dịch chuyển qua đêm.

## VIII. Kinh Tế (经济)
Hải Khuẩn Tịnh Hóa Đội không có bất kỳ hoạt động kinh tế nào theo nghĩa thông thường. Chúng là sinh vật bản năng, không sản xuất, không trao đổi, không tích trữ. Giá trị kinh tế gián tiếp của chúng nằm ở việc duy trì sự sạch sẽ của nước biển — nền tảng cho mọi hoạt động kinh tế biển khác. Khi một vùng Hải Khuẩn bị tận diệt, nước biển khu vực đó ô nhiễm nghiêm trọng, khiến các Hải Tộc phải di cư, ngư trường bị phá hủy và tuyến đường thương mại biển bị gián đoạn. Phong Bạo Thương Đội từng ước tính rằng nếu mất Hải Khuẩn ở vùng biển nam, tổn thất thương mại hàng năm sẽ tương đương mười vạn linh thạch hạ phẩm — con số khiến ngay cả Hải Thần Cung cũng phải nhíu mày. Nói cách khác, sự tồn tại của Hải Khuẩn là điều kiện tiên quyết cho nền kinh tế biển, dù không ai trả thù lao cho chúng — Thủy Linh Nhi gọi đây là "nghịch lý lớn nhất Vô Tận Hải: kẻ quan trọng nhất lại là kẻ được trả công ít nhất."

## IX. Lịch Sử Tóm Tắt (简史)
Hải Khuẩn luôn tồn tại trong lòng đại dương từ thời thượng cổ, là thành phần tự nhiên không thể thiếu của hệ sinh thái biển, cũ hơn cả lịch sử thành văn của bất kỳ Hải Tộc nào. Số lượng của chúng tăng vọt khi Huyết Độc từ Nam Cương bắt đầu lan ra vùng biển nam khoảng ba trăm năm trước, như một phản ứng tự nhiên của đại dương trước mối đe dọa ô nhiễm — các trưởng lão Hải Quy gọi đó là "Hải Dương Miễn Dịch," hệ miễn dịch của biển cả. Ban đầu, Hải Khuẩn hoạt động hiệu quả cao, duy trì cân bằng giữa tốc độ ô nhiễm và tốc độ thanh lọc suốt hai trăm năm. Tuy nhiên, trong vài thập kỷ gần đây, nồng độ Huyết Độc ngày càng đậm đặc — đặc biệt sau khi Huyết Ma Tông mở rộng các thí nghiệm tại Nam Cương — tốc độ lan rộng vượt quá khả năng phân giải của quần thể. Hải Thần Cung biết đến sự tồn tại của chúng nhưng không can thiệp, giữ thái độ "để tự nhiên xử lý." Chỉ có San Hô Thủ Hộ Đoàn là đồng minh duy nhất chủ động phối hợp chống ô nhiễm ở tuyến đầu — Thủy Linh Nhi từng nói: "Khuẩn là bạn, không phải công cụ." Gần đây, tốc độ Tuyến Tịnh lùi về phía bắc tăng gấp đôi so với năm ngoái, và nhiều ngư dân đã bắt đầu bỏ biển lên bờ.

## X. Giai Thoại & Bí Mật (轶事 与 秘密)
Một số Hải Khuẩn tiếp xúc Huyết Độc lâu ngày đã bị đột biến đáng lo ngại — chuyển từ thanh lọc sang sản xuất độc tố mạnh hơn cả Huyết Độc gốc. Những Hải Khuẩn đột biến này mang màu đen thay vì xanh lục bình thường, và bắt đầu tấn công cả đồng loại — ngư dân gọi chúng là "Hắc Khuẩn," còn Hải Quy trưởng lão dùng thuật ngữ nghiêm trọng hơn: "Nghịch Tịnh Thể." Tịnh Hóa Chủ dường như đang dần mất kiểm soát đối với phần quần thể này — nếu Quần Thể Ý Thức sụp đổ hoàn toàn, Hải Khuẩn đột biến sẽ trở thành một mối đe dọa sinh thái mới nghiêm trọng không kém Huyết Độc. Đáng lo ngại hơn, nồng độ Huyết Độc đang tăng nhanh hơn khả năng thanh lọc — các dự đoán của Hải Quy trưởng lão cho thấy trong vài chục năm nữa, vùng biển nam có thể hoàn toàn trở thành "Biển Chết," nơi không sinh vật nào có thể tồn tại. Có tin đồn rằng sâu dưới Hải Khuẩn Đài, tảng đá nơi Tịnh Hóa Chủ tọa lạc, ẩn giấu một mạch linh khí cổ đại bị phong ấn — chính mạch linh khí này từng nuôi dưỡng Hải Khuẩn qua hàng vạn năm, nhưng phong ấn đang dần suy yếu, và không ai biết phong ấn đó do ai đặt hay vì mục đích gì.

## XI. Quan Hệ Thế Lực (势力关系)
Hải Khuẩn Tịnh Hóa Đội không có khả năng giao tiếp hay ngoại giao theo nghĩa thông thường, nhưng mối quan hệ sinh thái của chúng rõ ràng và quan trọng. San Hô Đảo Quốc và San Hô Thủ Hộ Đoàn là đồng minh tự nhiên gần gũi nhất — hai bên phối hợp chống ô nhiễm tại phòng tuyến biển nam, dù sự "phối hợp" này mang tính bản năng hơn là chiến lược. Thủy Linh Nhi là người duy nhất chủ động bảo vệ Hải Khuẩn, đôi khi cử đệ tử dọn sạch xác Hắc Khuẩn để ngăn đột biến lan rộng. Hải Miên Trùng Xã chia sẻ vai trò lọc sạch môi trường biển, tạo thành mối cộng sinh tự nhiên mà các học giả gọi là "Tam Tịnh Liên Hoàn" — khuẩn phân giải độc, miên lọc tạp chất, san hô tái tạo cấu trúc. Hải Thần Cung nhận thức được giá trị của Hải Khuẩn nhưng giữ thái độ bàng quan, không hỗ trợ cũng không cản trở — Long Cung Đại Thần Quan Trần Hải Triều từng nói: "Khuẩn tự sinh, khuẩn tự diệt, can dự làm chi." Mối đe dọa lớn nhất không đến từ bất kỳ thế lực nào, mà từ chính nồng độ Huyết Độc ngày càng tăng — kẻ thù của Hải Khuẩn là sự ô nhiễm, không phải chiến tranh.
