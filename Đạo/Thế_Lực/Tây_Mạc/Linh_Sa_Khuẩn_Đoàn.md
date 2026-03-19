---
type: faction
name: Linh Sa Khuẩn Đoàn
hantu: 灵沙菌团
faction_type: Liên Minh
alignment: 1
race: Vi Tộc (Khuẩn loại)
region: Tây Mạc
founded: Tự nhiên (Tồn tại từ thời Hồng Hoang)
founder: Không có (Hình thành tự nhiên)
emblem: Linh_Sa_Khuan_Doan.png
specialty: Phân giải tử khí, Tái tạo linh khí, Sản xuất sa đất dược tính
economy:
- Không có hoạt động kinh tế chủ động
- Sa đất dược tính bị thu gom bởi các thế lực khác
arcs:
  - arc: 1
    status: Tồn tại ổn định (Hệ sinh thái nền tảng)
    rank: Không Xếp Hạng
    leader: Khuẩn Mẫu (Bản năng điều phối)
    population: 10
    territory:
      - Hoàng Kim Sa Hải (Toàn vùng có xác chết)
    assets:
      - name: Khuẩn Mẫu Trung Tâm
        type: Sinh Vật
      - name: Sa Đất Dược Tính
        type: Tài Nguyên
    stats: [5, 30, 5, 10, 40, 10]
    divisions:
      - name: Khuẩn Mẫu Trung Tâm
        role: Phát tín hiệu hóa học điều phối toàn bộ quá trình phân giải
        headcount:
          truong_lao: 1
          chien_binh: 0
          dan_thuong: 9
        members:
          - character: "[Khuẩn Mẫu]"
            position: Cá thể trung tâm
            cultivation: Luyện Khí (Tương đương)
            placeholder: true
    relationships:
      - faction: Sa Mãng Tộc
        description: Cộng sinh âm thầm. Sa Mãng Tộc để xác con mồi ngoài hang cho Khuẩn Đoàn xử lý, đổi lại khu vực hang ổ được giữ sạch tử khí.
        diplomacy:
          lien_minh: 0
          tin: 0
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 20
          le_thuoc: 30
      - faction: Phế Khí Luyện Đan Phường
        description: Khách hàng bí mật lớn nhất — lén thu gom sa đất từ nơi Khuẩn Đoàn phân giải xác yêu thú để luyện đan dược đặc biệt.
        diplomacy:
          lien_minh: 0
          tin: 0
          uy_hiep: 0
          thuong_mai: 30
          on_oan: 0
          le_thuoc: 0
      - faction: Linh Sa Khuẩn Đoàn (Hệ sinh thái Tây Mạc)
        description: Là nền tảng sinh thái của Hoàng Kim Sa Hải. Không có Khuẩn Đoàn, tử khí sẽ tích tụ và biến sa mạc thành tử địa.
        diplomacy:
          lien_minh: 0
          tin: 0
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 0
---

# Linh Sa Khuẩn Đoàn (灵沙菌团)

## I. Tổng Quan (总览)
Linh Sa Khuẩn Đoàn là hệ sinh thái vi sinh vật nền tảng của Hoàng Kim Sa Hải, tồn tại từ thời Hồng Hoang khi sa mạc mới hình thành. Với hàng tỷ cá thể phân bố khắp mọi nơi có xác chết sinh vật, Khuẩn Đoàn đảm nhiệm vai trò "đội vệ sinh" của sa mạc — phân giải chất hữu cơ thành linh khí, ngăn tử khí tích tụ và duy trì sự cân bằng sinh thái cho toàn vùng. Mặc dù không có ý thức hay tổ chức theo nghĩa thông thường, Khuẩn Đoàn hoạt động như một thực thể tập thể hoàn chỉnh dưới sự điều phối bản năng của Khuẩn Mẫu trung tâm. Rất ít tu sĩ nhận ra sự tồn tại và tầm quan trọng thiết yếu của chúng đối với toàn bộ Tây Mạc.

## II. Địa Lý & Tài Nguyên (地理与资源)
Linh Sa Khuẩn Đoàn không có lãnh địa cố định mà xuất hiện ở bất kỳ nơi nào trong Hoàng Kim Sa Hải có xác chết sinh vật — từ xác yêu thú nhỏ đến thi thể tu sĩ bất hạnh. Chúng sống trên và bên trong xác chết, phân giải chất hữu cơ thành linh khí tái tạo. Vùng cát nơi Khuẩn Đoàn hoạt động mang một đặc tính đặc biệt: "sa đất" tại những khu vực này chứa dược tính quý hiếm, là nguyên liệu đan dược mà không có phương pháp nhân tạo nào có thể thay thế. Khuẩn Đoàn đặc biệt tập trung tại các bãi chiến trường cũ và các tuyến đường yêu thú di cư nơi tỉ lệ tử vong cao.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
Khuẩn Đoàn không có văn hóa hay tín ngưỡng theo nghĩa truyền thống, nhưng hành vi tập thể của chúng tuân theo một quy luật bất biến: "Chết không phải kết thúc — chết là bắt đầu cho thứ khác." Phân giải hoàn toàn, không để lại gì — xương cuối cùng cũng thành cát. Khi gặp xác chết lớn như yêu thú cấp cao hoặc tu sĩ mạnh, toàn bộ Khuẩn Đoàn trong phạm vi hàng dặm sẽ tụ họp thành "đại tiệc" để xử lý. Điều kỳ lạ nhất là Khuẩn Đoàn có bản năng tránh xa những xác chết còn dư ý chí mạnh mẽ — như thể chúng cảm nhận được sự "ám" từ linh hồn chưa siêu thoát, không dám đụng vào cho đến khi ý chí đó tự tan biến.

## IV. Cơ Cấu Tổ Chức (组织结构)
Cơ cấu của Khuẩn Đoàn hoàn toàn dựa trên bản năng sinh tồn, không có hệ thống cấp bậc hay mệnh lệnh. Khuẩn Mẫu là cá thể trung tâm, phát tín hiệu hóa học điều phối toàn bộ quá trình phân giải — quyết định khi nào tập trung, khi nào phân tán, và loại chất nào cần phân giải trước. Hàng tỷ cá thể khuẩn xung quanh được phân hóa thành nhiều nhóm chuyên biệt: nhóm phân giải thịt, nhóm phân giải xương, nhóm chuyển hóa tử khí thành linh khí. Tất cả hoạt động tự động và đồng bộ như một cơ thể sống khổng lồ, không cần bất kỳ sự can thiệp có ý thức nào.

## V. Công Pháp & Trận Pháp (功法与阵法)
Khuẩn Đoàn không tu luyện — quá trình phân giải tử khí và chuyển hóa thành linh khí là hoàn toàn tự nhiên, một sản phẩm phụ của chu kỳ sinh tồn bẩm sinh. Khi bị đe dọa bởi sinh vật khác, Khuẩn Đoàn tiết ra mùi hôi thối cực mạnh đủ để xua đuổi ngay cả yêu thú cấp cao — mùi này không chỉ khó chịu mà còn mang tử khí loãng, gây chóng mặt và buồn nôn cho kẻ tấn công. Ngoài ra, vùng đất nơi Khuẩn Đoàn hoạt động lâu ngày sẽ hình thành một lớp "sa đất" đặc biệt, chứa dược tính mà không có phương pháp luyện đan nhân tạo nào tái tạo được — đây là bí mật mà chỉ vài đan sư thông minh nhất Tây Mạc mới nắm được.

## VI. Đặc Sản Môn Phái (门派特产)
- **Sa Đất Dược Tính:** Lớp cát đặc biệt tại nơi Khuẩn Đoàn phân giải xác yêu thú cấp cao, chứa tinh chất linh khí đã được chuyển hóa tự nhiên. Là nguyên liệu bí mật cho một số đan dược đặc biệt, đặc biệt là đan dược thanh lọc tử khí và phục hồi linh mạch.
- **Linh Khí Tái Tạo:** Linh khí được Khuẩn Đoàn chuyển hóa từ tử khí có tính chất thuần khiết đặc biệt, nuôi dưỡng âm thầm các ốc đảo và linh mạch nhỏ khắp Hoàng Kim Sa Hải.

## VII. Cơ Sở Hạ Tầng (基础设施)
Khuẩn Đoàn không xây dựng bất kỳ cơ sở hạ tầng nào — chúng sống và chết ngay trên xác sinh vật mà chúng phân giải. Tuy nhiên, những khu vực Khuẩn Đoàn hoạt động lâu năm tự nhiên hình thành các "vùng thanh tịnh" — nơi tử khí gần như bằng không, cát mịn hơn và linh khí ổn định hơn so với các vùng xung quanh. Một số ốc đảo nhỏ trong Hoàng Kim Sa Hải thực chất tồn tại được là nhờ Khuẩn Đoàn đã thanh lọc tử khí trong khu vực suốt hàng nghìn năm, tạo điều kiện cho thực vật và mạch nước phát triển.

## VIII. Kinh Tế (经济)
Khuẩn Đoàn không có hoạt động kinh tế chủ động và không hiểu khái niệm giao dịch. Tuy nhiên, giá trị kinh tế gián tiếp của chúng là vô cùng lớn. Sa đất dược tính do chúng tạo ra là nguyên liệu quý hiếm được Phế Khí Luyện Đan Phường bí mật thu gom — đây là thành phần then chốt trong một số đan dược đặc biệt mà phường này nổi tiếng. Ngoài ra, vai trò thanh lọc tử khí của Khuẩn Đoàn gián tiếp duy trì giá trị thương mại của toàn bộ Thiên Sa Thương Đạo — nếu tử khí tràn ngập, không thương nhân nào dám đi qua sa mạc.

## IX. Lịch Sử Tóm Tắt (简史)
Linh Sa Khuẩn Đoàn tồn tại từ thời Hồng Hoang, song hành cùng sự hình thành của Hoàng Kim Sa Hải. Chúng là hệ sinh thái nền tảng — không có Khuẩn Đoàn, xác chết sinh vật sẽ tích tụ qua hàng vạn năm, tử khí sẽ ứ đọng và biến toàn bộ sa mạc thành vùng tử địa không thể sinh tồn. Xuyên suốt lịch sử, rất ít chủng tộc hay tu sĩ để ý đến sự tồn tại của chúng. Chỉ có những đan sư tinh anh nhất mới nhận ra rằng sa đất nơi Khuẩn Đoàn hoạt động chứa dược tính đặc biệt, và Phế Khí Luyện Đan Phường đã âm thầm khai thác nguồn tài nguyên này trong suốt nhiều thế kỷ mà không ai hay biết.

## X. Giai Thoại & Bí Mật (轶事与秘密)
- Phế Khí Luyện Đan Phường lén thu gom "sa đất" từ nơi Khuẩn Đoàn phân giải xác yêu thú cấp cao — đó là nguyên liệu bí mật cho một số đan dược đặc biệt của họ, và cũng là lý do phường này có thể luyện ra những loại đan mà nơi khác không thể bắt chước.
- Gần đây, Khuẩn Đoàn bắt đầu tránh xa một khu vực cụ thể trong Hoàng Kim Sa Hải — nơi đó có xác chết nhưng chúng không dám đến gần, như thể xác chết đó còn "sống". Hiện tượng này khiến tử khí tại khu vực đó tích tụ bất thường, thu hút sự chú ý của các thế lực xung quanh.
- Sa Mãng Tộc đôi khi để xác con mồi ngoài hang cho Khuẩn Đoàn xử lý — mối quan hệ cộng sinh âm thầm giữa hai bên đã kéo dài hàng nghìn năm, nhưng không bên nào thực sự "nhận thức" được sự hợp tác này.

## XI. Quan Hệ Thế Lực (势力关系)
- **Phế Khí Luyện Đan Phường:** Khách hàng bí mật lớn nhất, thu gom sa đất dược tính từ các khu vực Khuẩn Đoàn hoạt động. Mối quan hệ hoàn toàn một chiều — Khuẩn Đoàn không biết sự tồn tại của phường này.
- **Sa Mãng Tộc:** Cộng sinh tự nhiên, Sa Mãng để lại xác con mồi cho Khuẩn Đoàn phân giải, đổi lại hang ổ được giữ sạch tử khí. Hai bên tương tác hoàn toàn theo bản năng.
- **Hệ sinh thái Hoàng Kim Sa Hải:** Khuẩn Đoàn là nền tảng sinh thái không thể thay thế. Nếu chúng biến mất, tử khí sẽ tràn ngập và hủy diệt sự sống trên toàn sa mạc, kéo theo sự sụp đổ kinh tế của Thiên Sa Thương Đạo.
