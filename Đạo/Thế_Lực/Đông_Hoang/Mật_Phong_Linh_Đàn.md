---
type: faction
name: Mật Phong Linh Đàn
hantu: 蜜蜂灵坛
faction_type: Bộ Lạc
alignment: 0
race: Vi Tộc (Ong Linh Thú)
region: Đông Hoang
founded: Cách đây hơn 300 năm (ba đời Ong Chúa)
founder: Không có — tiến hóa tự nhiên nhờ linh khí Hỏa Vân Sơn
emblem: Ong_Vang_Tren_Vach_Nui.png
specialty: Sản xuất Linh Mật và Sáp Linh, Phòng thủ bầy đàn bằng nọc độc, Thu thập Phấn Hoa Linh
economy:
- Sản xuất Linh Mật (thu mua bởi tu sĩ Trạm Biên)
- Sáp Linh dùng sửa pháp khí và phụ liệu luyện đan
- Phấn Hoa Linh dùng luyện đan cấp thấp
arcs:
  - arc: 1
    status: Ổn định nhưng cảnh giác (cảm nhận Hỏa Vân Sơn bất ổn)
    rank: Hạng Năm
    leader: Ong Chúa Kim Hoa
    population: 5500
    territory:
      - Vách núi phía đông Hỏa Vân Sơn
    assets:
      - name: Tổ Ong Sáp Linh Khổng Lồ
        type: Công Trình
      - name: Thiên Niên Linh Mật
        type: Bí Bảo
    stats: [120, 140, 40, 5500, 100, 30]
    divisions:
      - name: Đàn Ong Linh
        role: Thu phấn, sản xuất Linh Mật, bảo vệ tổ và Ong Chúa
        headcount:
          truong_lao: 5
          chien_binh: 500
          dan_thuong: 4995
        members:
          - character: Kim Hoa
            position: Ong Chúa
            cultivation: Tương đương Trúc Cơ Viên Mãn
          - character: "[Kim Vệ Nhất]"
            position: Ong Lính Đầu Lĩnh
            cultivation: Tương đương Luyện Khí Đỉnh Phong
            placeholder: true
    relationships:
      - faction: Vạn Độc Môn
        description: Kẻ thù nguy hiểm nhất — Vạn Độc Môn từng nhắm đến Kim Hoa để bắt luyện Cổ, nhưng vị trí vách núi dựng đứng và bão nọc độc khiến tấn công tổn thất quá lớn, buộc phải rút lui.
        diplomacy:
          lien_minh: -40
          tin: 0
          uy_hiep: 60
          thuong_mai: 0
          on_oan: -50
          le_thuoc: 0
      - faction: Mật Ong Linh Đoàn
        description: Chủng tộc tương cận — hai đàn ong linh ở hai vùng khác nhau, biết về nhau qua pheromone linh phát tán theo gió nhưng chưa từng tiếp xúc trực tiếp do khoảng cách quá xa.
        diplomacy:
          lien_minh: 20
          tin: 20
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 0
      - faction: Liệt Dương Tông
        description: Láng giềng gần trên Hỏa Vân Sơn — Liệt Dương Tông tu luyện hỏa hệ ở phía tây núi, hai bên không xung đột trực tiếp nhưng hoạt động của tông ảnh hưởng đến nguồn địa nhiệt nuôi dưỡng hoa linh phía đông.
        diplomacy:
          lien_minh: 0
          tin: 10
          uy_hiep: 20
          thuong_mai: 0
          on_oan: -10
          le_thuoc: 0
---

# Mật Phong Linh Đàn (蜜蜂灵坛)

## I. Tổng Quan (总览)
> *"Nếu muốn biết Hỏa Vân Sơn có bình yên hay không, hãy nhìn đàn ong — chúng biết trước con người."*
> — Tu sĩ Trạm Biên vô danh, ghi trong sổ tay quan sát


Mật Phong Linh Đàn là một đàn ong linh thú sinh sống trên vách núi phía đông Hỏa Vân Sơn, nơi hoa linh nở quanh năm nhờ địa nhiệt từ núi lửa. Đàn gồm hơn năm nghìn con, từ ong thợ nhỏ nhắn đến ong lính có nọc độc đủ sức tê liệt tu sĩ Trúc Cơ, tất cả phục vụ Ong Chúa Kim Hoa — ong linh thú thế hệ thứ ba, cơ thể vàng óng, có linh trí tương đương trẻ em mười tuổi và tu vi ngang Trúc Cơ Viên Mãn. Tổ ong bằng sáp linh cao hơn mười trượng dính chặt vào vách đá, là một kiệt tác kiến trúc tự nhiên mà ngay cả trận sư cũng phải thán phục. Đàn ong tồn tại ở Hỏa Vân Sơn hơn ba trăm năm, ba đời Ong Chúa, tiến hóa tự nhiên nhờ linh khí từ hoa linh và địa nhiệt núi lửa.

## II. Địa Lý & Tài Nguyên (地理与资源)

Tổ ong nằm trên vách núi dựng đứng phía đông Hỏa Vân Sơn, ở độ cao mà phàm nhân không thể leo tới. Vị trí này được chọn bởi ba yếu tố: địa nhiệt từ núi lửa giữ ấm quanh năm khiến hoa linh trên sườn đông không bao giờ tàn, vách đá dựng đứng tạo phòng thủ tự nhiên chống lại kẻ thù mặt đất, và dòng khí nóng bốc lên từ dưới giúp ong bay dễ dàng hơn. Tổ ong bằng sáp linh chia thành hàng trăm khoang chức năng: khoang chứa mật, khoang ấp trứng, khoang nghỉ ngơi cho ong lính, và phòng riêng của Ong Chúa nằm sâu nhất. Tài nguyên chính gồm Linh Mật — mật ong chứa linh khí loãng, có tác dụng bồi bổ kinh mạch và hồi phục thương tích nhẹ; Sáp Linh — dùng bịt kín vết nứt trên pháp khí hoặc phụ liệu luyện đan; và Phấn Hoa Linh — nguyên liệu luyện đan cấp thấp quý hiếm.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
> *"Ong biết trung thành hơn người — kẻ nào phản bội đàn, kẻ đó bị đuổi ra ngoài trời lạnh và không bao giờ được phép quay về."*
> — Tu sĩ vô danh, quan sát hành vi đàn ong linh trên Hỏa Vân Sơn


Mật Phong Linh Đàn hoạt động theo bản năng đàn thuần túy: cả đàn phục vụ Ong Chúa, Ong Chúa bảo vệ cả đàn, không có khái niệm "cá nhân." Ong thợ tuyệt đối trung thành, ong lính sẵn sàng hy sinh mạng sống bảo vệ tổ mà không do dự. Kẻ nào xâm phạm tổ sẽ bị cả đàn tấn công kamikaze — ong lính lao vào đâm kim rồi chết, nhưng số lượng áp đảo khiến ngay cả tu sĩ mạnh cũng phải bỏ chạy. Mỗi mùa hoa nở, Ong Chúa Kim Hoa bay ra ngoài tổ một lần duy nhất để chọn hoa đẹp nhất — nghi thức gọi là "Tuần Hoa Lễ," đánh dấu bắt đầu mùa thu hoạch. Đây là thời điểm duy nhất trong năm Ong Chúa rời khỏi tổ, và toàn bộ ong lính bay hộ tống tạo thành đám mây vàng rực rỡ trên sườn núi.

## IV. Cơ Cấu Tổ Chức (组织结构)

Ong Chúa Kim Hoa đứng đầu tuyệt đối, mọi quyết định từ hướng thu phấn đến phản ứng trước nguy hiểm đều do Kim Hoa ra lệnh thông qua pheromone linh. Kim Hoa là ong linh thú thế hệ thứ ba, cơ thể vàng óng ánh, đôi cánh phát ra tiếng vo có tác dụng an thần — ngay cả tu sĩ đứng gần cũng cảm thấy bình yên kỳ lạ. Linh trí của Kim Hoa tương đương trẻ em mười tuổi: hiểu được khái niệm nguy hiểm, biết phân biệt bạn thù, nhưng chưa có tư duy chiến lược phức tạp. Dưới Ong Chúa có năm trăm ong lính tương đương Luyện Khí, nọc có thể gây tê liệt tu sĩ Trúc Cơ. Hơn năm nghìn ong thợ không có sức chiến đấu, chuyên thu phấn và sản xuất mật. Ngoài ra có hàng trăm ấu trùng đang phát triển trong khoang trứng.

## V. Công Pháp & Trận Pháp (功法与阵法)

Mật Phong Linh Đàn không tu luyện công pháp, tiến hóa hoàn toàn tự nhiên nhờ hấp thụ linh khí từ hoa linh và địa nhiệt Hỏa Vân Sơn qua nhiều thế hệ. Tuy nhiên, bản năng chiến đấu tập thể của đàn tạo thành "Vạn Phong Trận" — khi bị đe dọa, cả đàn ong lính bay thành đội hình xoáy ốc, cánh vỗ đồng loạt tạo ra bão gió nhỏ trộn nọc độc phun sương. Bão nọc độc này đủ sức đẩy lùi yêu thú cấp Trúc Cơ và khiến tu sĩ Kim Đan phải che chắn cẩn thận. Ngoài Vạn Phong Trận, ong lính còn có chiến thuật "Kim Châm Vũ" — bay nhanh quanh kẻ thù và đâm kim từ mọi hướng, tạo áp lực liên tục không cho đối phương tập trung thần thức.

## VI. Đặc Sản Môn Phái (门派特产)

- **Linh Mật:** Mật ong chứa linh khí loãng, vị ngọt thanh khiết, có tác dụng bồi bổ kinh mạch và hồi phục thương tích nhẹ. Tu sĩ cấp thấp rất ưa chuộng vì giá rẻ hơn đan dược mà hiệu quả ổn định.
- **Sáp Linh:** Sáp ong chất lượng cao, bền và chịu nhiệt tốt nhờ ảnh hưởng từ địa nhiệt Hỏa Vân Sơn. Dùng bịt kín vết nứt trên pháp khí hoặc làm khuôn đúc phụ trong luyện khí.
- **Phấn Hoa Linh Hỏa Vân:** Phấn hoa thu từ linh hoa mọc trên sườn núi lửa, chứa hỏa linh lực vi lượng — nguyên liệu luyện đan cấp thấp quý hiếm, đặc biệt thích hợp cho hỏa hệ đan dược.

## VII. Cơ Sở Hạ Tầng (基础设施)

- **Tổ Ong Sáp Linh:** Kiến trúc tự nhiên cao hơn mười trượng, dính chặt vào vách đá bằng sáp linh đặc biệt bền chắc. Bên trong là mê cung khoang phòng với hàng trăm ngăn chức năng khác nhau, toàn bộ được xây dựng bởi ong thợ qua nhiều thế hệ.
- **Khoang Thiên Niên Linh Mật:** Khoang sâu nhất và được bảo vệ nghiêm ngặt nhất, nơi cất giữ giọt mật tích tụ linh khí suốt ba trăm năm. Lối vào chỉ Ong Chúa biết, được canh gác bởi ong lính tinh nhuệ nhất.
- **Tuyến Bay Thu Phấn:** Mạng lưới tuyến bay cố định kết nối tổ với các khu vực hoa linh trên sườn đông Hỏa Vân Sơn, được đánh dấu bằng pheromone linh để ong thợ không bị lạc.
- **Vách Đá Phòng Thủ:** Bản thân vách núi dựng đứng là hệ thống phòng thủ tự nhiên mạnh nhất — kẻ tấn công phải bay lên hoặc leo vách đá trong khi bị cả đàn ong tấn công từ trên xuống.

## VIII. Kinh Tế (经济)

Mật Phong Linh Đàn không có hoạt động kinh tế chủ động. Tuy nhiên, gần đây một số tu sĩ thông minh ở Trạm Biên gần đó bắt đầu "thuần hóa" quan hệ bằng cách để thức ăn chứa linh khí gần tổ để đổi lấy Linh Mật rơi vãi — một dạng trao đổi thương mại sơ khai mà Kim Hoa dần chấp nhận vì nhận ra lợi ích. Sáp Linh rơi từ tổ cũng được tu sĩ nhặt và bán trên thị trường. Phấn Hoa Linh Hỏa Vân được thu hoạch gián tiếp từ các khu vực ong đã thụ phấn xong. Nhìn chung, đàn ong không tham gia kinh tế nhưng sản phẩm của chúng tạo ra một thị trường ngách nhỏ mà tán tu địa phương phụ thuộc vào.

## IX. Lịch Sử Tóm Tắt (简史)
> *"Đàn ong di chuyển tổ lên cao — khi nào ong biết sợ, đó là lúc người phải chạy."*
> — Kinh nghiệm dân gian Trạm Biên, truyền khẩu qua nhiều đời


Đàn ong đầu tiên xuất hiện ở Hỏa Vân Sơn hơn ba trăm năm trước, ban đầu chỉ là đàn ong thường bị thu hút bởi hoa linh nở nhờ địa nhiệt. Ong Chúa đời thứ nhất là con ong đầu tiên phát triển linh trí sơ khai sau hàng chục năm hấp thụ linh khí, đánh dấu sự chuyển biến từ côn trùng bình thường sang linh thú cấp thấp. Ong Chúa đời thứ hai mở rộng tổ lên quy mô hiện tại và xây dựng khoang Thiên Niên Linh Mật. Ong Chúa Kim Hoa hiện tại là đời thứ ba, mạnh nhất trong lịch sử, đạt tu vi tương đương Trúc Cơ Viên Mãn. Mối đe dọa lớn nhất xảy ra khi Vạn Độc Môn phát hiện Kim Hoa và đem quân tấn công để bắt luyện Cổ, nhưng vị trí vách núi dựng đứng cùng Vạn Phong Trận khiến tổn thất quá lớn, buộc phải rút lui. Gần đây, Kim Hoa cảm nhận Hỏa Vân Sơn bất ổn — đàn ong bắt đầu di chuyển tổ lên cao hơn vách núi.

## X. Giai Thoại & Bí Mật (轶事与秘密)

Sâu trong tổ có một khoang mật đặc biệt chứa "Thiên Niên Linh Mật" — mật tích tụ linh khí suốt ba trăm năm qua ba đời Ong Chúa, truyền thuyết nói nuốt một giọt có thể giúp Trúc Cơ tu sĩ đột phá Kim Đan mà không cần nhập định bế quan. Ong Chúa Kim Hoa bảo vệ khoang này bằng tính mạng — đây là di sản của cả ba đời và là hy vọng để thế hệ Ong Chúa thứ tư đạt đến cảnh giới Kim Đan linh thú.

Kim Hoa có linh cảm Hỏa Vân Sơn sắp hoạt động mạnh hơn bình thường — đàn ong đã bắt đầu di chuyển tổ lên cao hơn trên vách núi, dấu hiệu mà tu sĩ hiểu biết sẽ nhận ra là cảnh báo sớm về núi lửa sắp phun trào. Một vài tu sĩ thông thái ở Trạm Biên đã chú ý đến hành vi bất thường này và lặng lẽ chuẩn bị sơ tán, nhưng đa số người dân chưa nhận ra mối nguy.

## XI. Quan Hệ Thế Lực (势力关系)

- **Vạn Độc Môn:** Kẻ thù nguy hiểm nhất — từng tấn công tổ để bắt Ong Chúa luyện Cổ. Dù đã rút lui nhưng mối đe dọa vẫn còn, Vạn Độc Môn không bao giờ từ bỏ mục tiêu một cách dễ dàng.
- **Mật Ong Linh Đoàn:** Chủng tộc anh em ở rừng hoa phía nam — hai đàn ong linh biết về nhau qua pheromone linh nhưng khoảng cách quá xa để giao tiếp trực tiếp. Nếu có ngày tiếp xúc, có thể trở thành đồng minh tự nhiên.
- **Liệt Dương Tông:** Láng giềng trên cùng ngọn núi — Liệt Dương Tông ở phía tây Hỏa Vân Sơn, không trực tiếp xung đột nhưng hoạt động tu luyện hỏa hệ của họ ảnh hưởng đến dòng địa nhiệt nuôi dưỡng hoa linh phía đông.
- **Tu sĩ Trạm Biên:** Quan hệ mới hình thành — một số tu sĩ bắt đầu "trao đổi" thức ăn linh để lấy Linh Mật rơi vãi, tạo ra dạng thương mại sơ khai mà Kim Hoa dần chấp nhận.
- **Liệt Dương Tông Đệ Tử:** Một số ngoại môn đệ tử Liệt Dương Tông lén lấy Linh Mật từ vách đá khi ong đi kiếm ăn, bị ong lính phát hiện và đuổi đánh nhiều lần. Kim Hoa đã học được cách phân biệt mùi đệ tử Liệt Dương Tông và tăng cường tuần tra khi ngửi thấy mùi lưu hoàng đặc trưng của hỏa hệ tu sĩ.


