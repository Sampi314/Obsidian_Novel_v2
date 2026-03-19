---
type: faction
name: Linh Trần Vi Tộc
hantu: 灵尘微族
faction_type: Bộ Lạc
alignment: 0
race: Vi Tộc (Bụi Linh)
region: Đông Hoang
founded: Thái Cổ Kỷ Nguyên (Không xác định chính xác)
founder: Không có — phát sinh tự nhiên từ linh khí ngưng tụ
emblem: Linh_Tran_Phat_Quang.png
specialty: Ghi nhớ ký ức qua tiếp xúc, Cảm ứng linh khí vi lượng, Nhiễu loạn thần thức
economy:
- Không có hoạt động kinh tế chủ động
- Một số tu sĩ thu thập bụi linh làm nguyên liệu luyện đan phụ trợ
arcs:
  - arc: 1
    status: Tồn tại thụ động
    rank: Không Xếp Hạng
    leader: Không có lãnh đạo cá thể
    population: Không đếm được (hàng triệu vi thể)
    territory:
      - Rừng rậm Đông Hoang (trôi nổi trong không khí)
      - Các vùng linh khí dày đặc quanh linh mạch lộ thiên
    assets:
      - name: Ký Ức Linh Trần
        type: Tài Nguyên
      - name: Linh Quang Trường
        type: Hiện Tượng Tự Nhiên
    stats: [5, 10, 5, 50, 30, 10]
    divisions:
      - name: Quần Thể Linh Trần
        role: Tồn tại và hấp thụ linh khí tự nhiên, ghi nhớ mọi ký ức tiếp xúc
        headcount:
          truong_lao: 0
          chien_binh: 0
          dan_thuong: 50
        members:
          - character: "[Ý Thức Tập Thể Linh Trần]"
            position: Không có
            cultivation: Tương đương Luyện Khí (tổng thể)
            placeholder: true
    relationships:
      - faction: Nấm Linh Mạng Lưới
        description: Hai dạng sống vi thể cổ xưa cùng tồn tại, Linh Trần trôi nổi trên không còn Nấm Linh lan tỏa dưới đất — đôi khi linh khí trao đổi qua lại tạo thành hiện tượng cộng sinh tự nhiên.
        diplomacy:
          lien_minh: 20
          tin: 30
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 0
      - faction: Dược Vương Cốc
        description: Một số đệ tử Dược Vương Cốc thu thập bụi linh làm phụ liệu luyện đan, nhưng không coi Linh Trần là đối tác mà chỉ xem như tài nguyên tự nhiên.
        diplomacy:
          lien_minh: 0
          tin: 10
          uy_hiep: 0
          thuong_mai: 10
          on_oan: -10
          le_thuoc: 0
      - faction: Linh Khuẩn Dược Viên
        description: Viên chủ nghiên cứu tương tác giữa linh khuẩn và bụi linh, phát hiện bụi linh có thể thúc đẩy sinh trưởng nấm linh dược — là thế lực hiếm hoi nhận ra Linh Trần có ý thức.
        diplomacy:
          lien_minh: 10
          tin: 20
          uy_hiep: 0
          thuong_mai: 5
          on_oan: 0
          le_thuoc: 0
---

# Linh Trần Vi Tộc (灵尘微族)

## I. Tổng Quan (总览)
Linh Trần Vi Tộc là dạng sống vi thể cổ xưa nhất được ghi nhận ở Đông Hoang, tồn tại dưới hình thức hàng triệu hạt bụi linh quang trôi nổi trong không khí. Chúng không có hình dạng cố định, không có cá thể lãnh đạo, cũng không có tổ chức xã hội theo nghĩa thông thường. Đa phần sinh vật lớn hơn thậm chí không nhận ra đây là một chủng tộc sống — chỉ coi là hiện tượng tự nhiên giống sương mù phát sáng. Tuy nhiên, Linh Trần sở hữu một dạng ý thức tập thể sơ khai, có khả năng phản ứng với môi trường xung quanh và ghi nhớ mọi thứ chúng từng chạm vào. Vì không có sức chiến đấu đáng kể và hoàn toàn sống theo bản năng, Linh Trần Vi Tộc được xếp vào dạng Không Xếp Hạng — tồn tại bên lề thế giới tu chân mà không ai để ý.

## II. Địa Lý & Tài Nguyên (地理与资源)
Linh Trần Vi Tộc không có lãnh thổ cố định. Chúng trôi nổi khắp các khu rừng rậm Đông Hoang, tập trung đông đảo nhất ở những nơi linh khí dày đặc — gần linh mạch lộ thiên, quanh cổ thụ ngàn năm, hoặc trong các thung lũng sương mù không bao giờ tan. Vào những đêm trăng tròn, linh khí thiên nhiên dồi dào khiến bụi linh tụ lại thành những đám mây phát sáng rực rỡ, soi sáng cả cánh rừng. Tài nguyên của Linh Trần hoàn toàn là linh khí tản mạn trong không khí — chúng không cần thức ăn, nước uống hay bất kỳ vật chất nào khác. Bản thân bụi linh cũng là một loại tài nguyên: khi thu thập đủ số lượng, có thể dùng làm phụ liệu luyện đan hoặc vẽ phù lục cấp thấp, nhưng quá trình thu thập rất mất thời gian vì bụi linh tự động tản ra khi cảm nhận nguy hiểm.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
Nói Linh Trần Vi Tộc có "văn hóa" là hơi quá — chúng hoạt động hoàn toàn theo bản năng tập thể, hướng về nơi linh khí dồi dào và tránh xa nơi có tà khí hoặc sát khí mạnh. Tuy nhiên, ý thức tập thể của chúng thể hiện một số hành vi đáng chú ý: khi linh khí đặc biệt dồi dào, cả quần thể đồng loạt phát sáng trong hiện tượng mà tu sĩ gọi là "Linh Trần Dạ Quang" — đêm phát sáng linh trần. Người địa phương coi đây là điềm lành, báo hiệu linh khí vùng đó đang ở trạng thái thuần tịnh. Ngược lại, nếu bụi linh đột ngột biến mất khỏi một khu vực, đó là dấu hiệu cực kỳ đáng lo vì chứng tỏ linh khí nơi đó đã bị ô nhiễm hoặc có thực thể nguy hiểm đang ẩn nấp.

## IV. Cơ Cấu Tổ Chức (组织结构)
Linh Trần Vi Tộc không có tổ chức theo nghĩa thông thường. Hàng triệu vi thể bụi linh hoạt động như một quần thể sinh vật đơn giản, không có cá thể lãnh đạo, không phân chia đẳng cấp hay chức vụ. Ý thức tập thể của chúng giống như một bầy đàn — mỗi hạt bụi linh chứa một phần cực nhỏ của ý thức chung, khi tụ lại đủ đông thì khả năng cảm nhận và phản ứng tăng lên đáng kể. Dân số không thể đếm chính xác vì bụi linh liên tục sinh ra và tan biến theo chu kỳ linh khí. Ước tính có hàng triệu vi thể rải rác khắp rừng Đông Hoang, nhưng con số này thay đổi theo mùa.

## V. Công Pháp & Trận Pháp (功法与阵法)
Linh Trần Vi Tộc không tu luyện bất kỳ công pháp nào — chúng tồn tại bằng bản năng hấp thụ linh khí tự nhiên, quá trình này diễn ra hoàn toàn thụ động giống như thực vật quang hợp. Tuy không có trận pháp, bản thân đám bụi linh khi tụ lại với mật độ cao sẽ tạo ra hiệu ứng nhiễu loạn thần thức tự nhiên — tu sĩ đi qua vùng bụi linh dày đặc sẽ cảm thấy mê mang, mất phương hướng, đôi khi nhìn thấy ảo ảnh từ ký ức của người khác mà bụi linh đang mang theo. Hiệu ứng này không đủ mạnh để gây nguy hiểm cho Trúc Cơ tu sĩ, nhưng phàm nhân và Luyện Khí sơ kỳ có thể bị lạc trong rừng nhiều ngày.

## VI. Đặc Sản Môn Phái (门派特产)
- **Linh Trần Phấn:** Bụi linh được thu thập và cô đọng lại, dùng làm phụ liệu vẽ phù lục cấp thấp hoặc pha chế đan dược bổ trợ kinh mạch. Chất lượng phụ thuộc vào nơi thu thập — bụi linh gần linh mạch có dược tính cao hơn.
- **Linh Trần Dạ Minh Châu:** Hiện tượng cực hiếm — khi một lượng lớn bụi linh ngưng tụ tự nhiên qua hàng nghìn năm, tạo thành viên châu phát sáng vĩnh cửu. Giá trị không nằm ở tu luyện mà ở khả năng chiếu sáng ổn định, được dùng trong trận pháp chiếu sáng và trang trí phủ đệ tu sĩ.

## VII. Cơ Sở Hạ Tầng (基础设施)
Linh Trần Vi Tộc không có bất kỳ cơ sở hạ tầng nào theo nghĩa thông thường. Chúng không xây dựng, không cư trú tại một địa điểm cố định, và không sử dụng công cụ. Tuy nhiên, sự tồn tại của chúng tạo ra một loại "hạ tầng tự nhiên" cho hệ sinh thái rừng Đông Hoang: đám bụi linh giúp phân bổ linh khí đều đặn hơn, giảm thiểu tình trạng tích tụ linh khí cục bộ gây bạo phát linh thú. Một số trận sư đã nhận ra rằng nơi nào có Linh Trần trú ngụ, trận pháp đặt tại đó sẽ hoạt động ổn định hơn nhờ dòng linh khí được "làm mịn".

## VIII. Kinh Tế (经济)
Linh Trần Vi Tộc không tham gia bất kỳ hoạt động kinh tế nào. Chúng không sản xuất, không trao đổi, không tích trữ. Tuy nhiên, sự tồn tại của chúng gián tiếp tạo ra giá trị kinh tế cho người khác: tán tu nghèo đôi khi thu thập bụi linh bán cho tiệm dược hoặc phù sư, dù giá rất rẻ vì quá trình thu thập chậm chạp và bụi linh mất dược tính nhanh sau khi tách khỏi quần thể. Một vài dược sư am hiểu sẵn sàng trả giá cao hơn cho Linh Trần Phấn chất lượng cao, nhưng thị trường quá nhỏ để tạo thành ngành kinh tế thực sự.

## IX. Lịch Sử Tóm Tắt (简史)
Linh Trần Vi Tộc có lẽ là dạng sống cổ xưa nhất ở Đông Hoang, xuất hiện từ khi linh khí bắt đầu ngưng tụ trong Thái Cổ Kỷ Nguyên. Không có sử liệu nào ghi chép thời điểm chúng ra đời vì khi các chủng tộc có trí tuệ bắt đầu ghi chép lịch sử, bụi linh đã tồn tại từ lâu. Qua hàng vạn năm, Linh Trần chứng kiến mọi biến cố lớn của Đông Hoang mà không hề tham gia — từ cuộc chiến giữa các yêu vương thượng cổ, sự trỗi dậy của nhân tộc, đến việc thành lập các tông môn lớn. Tất cả đều được ghi nhớ trong ý thức tập thể của chúng, nhưng không ai biết cách truy xuất. Hầu hết sinh vật lớn không nhận ra đây là một chủng tộc — chỉ coi là hiện tượng tự nhiên.

## X. Giai Thoại & Bí Mật (轶事与秘密)
Linh Trần Vi Tộc thực ra có khả năng ghi nhớ — đám bụi mang theo ký ức về mọi thứ chúng từng chạm vào, bao gồm cả bí mật của tu sĩ đi qua rừng. Mỗi khi bụi linh tiếp xúc với một sinh vật, một phần ký ức và cảm xúc của sinh vật đó sẽ được "in" vào bụi linh. Nếu ai đó tìm ra cách giao tiếp với Linh Trần, sẽ có được kho thông tin vô giá về lịch sử Đông Hoang hàng vạn năm — bao gồm cả vị trí di tích cổ đại, bí mật của các tông phái đã diệt vong, và thậm chí ký ức của những cường giả đã ngã xuống trong rừng sâu.

Có tin đồn rằng một vị cổ tu đời xưa từng thành công trong việc "hợp nhất" với đám bụi linh, dùng thần thức hòa vào ý thức tập thể của chúng để thấy được mọi thứ đã xảy ra trong rừng Đông Hoang suốt hàng vạn năm. Tuy nhiên, khi rút thần thức ra, vị này đã phát điên vì lượng thông tin quá lớn, cuối cùng bản thân cũng tan biến thành bụi linh.

## XI. Quan Hệ Thế Lực (势力关系)
- **Nấm Linh Mạng Lưới:** Hai dạng sống vi thể cổ xưa cùng tồn tại trong hệ sinh thái Đông Hoang — Linh Trần trôi nổi trên không, Nấm Linh lan tỏa dưới đất, tạo thành một mạng lưới cảm ứng linh khí hoàn chỉnh từ mặt đất đến bầu trời.
- **Dược Vương Cốc:** Đệ tử Dược Vương Cốc thu thập bụi linh làm phụ liệu, nhưng không coi Linh Trần là đối tác ngang hàng — chỉ xem như tài nguyên tự nhiên khai thác khi cần.
- **Linh Khuẩn Dược Viên:** Thế lực hiếm hoi nhận ra Linh Trần có ý thức, đang nghiên cứu tương tác giữa linh khuẩn và bụi linh để tìm cách giao tiếp.
