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

> *"Chết không phải kết thúc — chết là bắt đầu cho thứ khác. Xương cuối cùng cũng thành cát, và cát nuôi mầm sống mới."*
> — Quy luật bất biến của Khuẩn Đoàn, ghi nhận bởi đan sư Hồng Luyện của Phế Khí Luyện Đan Phường

> *"Nơi nào Khuẩn Đoàn không đến, nơi đó có oán linh — đó không phải mê tín, đó là quy tắc sống còn."*
> — Kinh nghiệm dân gian sa mạc, truyền khẩu khắp Thiên Sa Thương Đạo
> *"Sa mạc không nuốt chửng — sa mạc tiêu hóa. Và kẻ tiêu hóa chính là Khuẩn Đoàn."*
> — Đan sư Hồng Luyện, ghi trong sổ tay nghiên cứu bí mật



## I. Tổng Quan (总览)

Linh Sa Khuẩn Đoàn là hệ sinh thái vi sinh vật nền tảng của Hoàng Kim Sa Hải, tồn tại từ thời Hồng Hoang khi sa mạc mới hình thành. Với hàng tỷ cá thể phân bố khắp mọi nơi có xác chết sinh vật, Khuẩn Đoàn đảm nhiệm vai trò "đội vệ sinh" của sa mạc — phân giải chất hữu cơ thành linh khí, ngăn tử khí tích tụ và duy trì sự cân bằng sinh thái cho toàn vùng. Mặc dù không có ý thức hay tổ chức theo nghĩa thông thường, Khuẩn Đoàn hoạt động như một thực thể tập thể hoàn chỉnh dưới sự điều phối bản năng của Khuẩn Mẫu trung tâm — cá thể khuẩn cổ xưa nhất, tồn tại liên tục từ thời nguyên thủy, mang trong mình "ký ức phân giải" của mọi xác chết đã qua tay Khuẩn Đoàn. Rất ít tu sĩ nhận ra sự tồn tại và tầm quan trọng thiết yếu của chúng đối với toàn bộ Tây Mạc — nếu Khuẩn Đoàn biến mất, sa mạc sẽ chìm trong tử khí chỉ sau vài thập kỷ.

## II. Địa Lý & Tài Nguyên (地理 与 资源)

Linh Sa Khuẩn Đoàn không có lãnh địa cố định mà xuất hiện ở bất kỳ nơi nào trong Hoàng Kim Sa Hải có xác chết sinh vật — từ xác yêu thú nhỏ bằng nắm tay đến thi thể tu sĩ bất hạnh. Chúng sống trên và bên trong xác chết, phân giải chất hữu cơ thành linh khí tái tạo, biến cái chết thành nguồn sống mới cho sa mạc. Vùng cát nơi Khuẩn Đoàn hoạt động mang một đặc tính đặc biệt: "sa đất" tại những khu vực này chứa dược tính quý hiếm, là nguyên liệu đan dược mà không có phương pháp nhân tạo nào có thể thay thế. Khuẩn Đoàn đặc biệt tập trung tại ba địa điểm nổi tiếng: **Vạn Cốt Sa Trường** — bãi chiến trường cổ phía bắc Hoàng Kim Sa Hải nơi hàng vạn sinh vật từng ngã xuống trong đại chiến thượng cổ; **Tuyến Di Cư Huyết Lộ** — con đường yêu thú di cư qua sa mạc nơi tỉ lệ tử vong cao, trải dài hơn nghìn dặm; và **Tử Khí Hồ** — vùng trũng tự nhiên nơi tử khí tích tụ dày đặc, là "khu bếp ăn" lớn nhất của Khuẩn Đoàn. Khuẩn Mẫu thường xuyên di chuyển giữa ba điểm này theo mùa chết — mùa hè nóng bức khi yêu thú chết nhiều nhất, Khuẩn Mẫu thường ở Tuyến Di Cư Huyết Lộ; mùa đông lạnh giá, nó rút về Tử Khí Hồ nơi tử khí cũ vẫn còn dày.

## III. Văn Hóa & Tín Ngưỡng (文化 与 信仰)

Khuẩn Đoàn không có văn hóa hay tín ngưỡng theo nghĩa truyền thống, nhưng hành vi tập thể của chúng tuân theo một quy luật bất biến mà đan sư Hồng Luyện gọi là "Phân Giải Đạo": mọi thứ chết đi phải được trả về cho đất, không ngoại lệ. Phân giải hoàn toàn, không để lại gì — xương cuối cùng cũng thành cát, gân cuối cùng cũng thành bụi. Khi gặp xác chết lớn như yêu thú cấp cao hoặc tu sĩ Kim Đan trở lên, toàn bộ Khuẩn Đoàn trong phạm vi hàng dặm sẽ tụ họp thành "Đại Phân Giải Hội" — quá trình có thể kéo dài nhiều tháng, tạo ra lượng sa đất dược tính lớn bất thường thu hút sự chú ý của đan sư. Điều kỳ lạ nhất là Khuẩn Đoàn có bản năng tránh xa những xác chết còn dư ý chí mạnh mẽ — như thể chúng cảm nhận được sự "ám" từ linh hồn chưa siêu thoát, không dám đụng vào cho đến khi ý chí đó tự tan biến. Thương nhân Thiên Sa Thương Đạo có kinh nghiệm: khi thấy xác chết giữa sa mạc mà cát xung quanh vẫn sạch bóng, không một con khuẩn nào dám đến gần — hãy chạy ngay lập tức, vì xác đó "chưa chết hẳn."

## IV. Cơ Cấu Tổ Chức (组织结构)
> *"Nhục Khuẩn đỏ nâu, Cốt Khuẩn trắng xám, Linh Khuẩn phát sáng, Bì Khuẩn vàng nhạt — mỗi loại một việc, phối hợp hoàn hảo hơn bất kỳ tông môn nào."*
> — Ghi chú nghiên cứu của đan sư Vân Hạ, Phế Khí Luyện Đan Phường


Cơ cấu của Khuẩn Đoàn hoàn toàn dựa trên bản năng sinh tồn, không có hệ thống cấp bậc hay mệnh lệnh — một dạng "dân chủ sinh học" nguyên thủy nhất. Khuẩn Mẫu là cá thể trung tâm, phát tín hiệu hóa học điều phối toàn bộ quá trình phân giải — quyết định khi nào tập trung, khi nào phân tán, và loại chất nào cần phân giải trước. Khuẩn Mẫu không di chuyển bằng chân mà bằng cách liên tục sinh sản theo hướng mục tiêu và để phần sau chết đi, tạo ấn tượng nó đang "bò" qua cát — tốc độ di chuyển khoảng một dặm mỗi ngày, chậm nhưng không bao giờ dừng. Hàng tỷ cá thể khuẩn xung quanh được phân hóa thành nhiều nhóm chuyên biệt: **Nhục Khuẩn** chuyên phân giải thịt và cơ, có màu đỏ nâu; **Cốt Khuẩn** chuyên phân giải xương và gân, có màu trắng xám; **Linh Khuẩn** chuyên chuyển hóa tử khí thành linh khí, phát sáng nhạt trong đêm tối; và **Bì Khuẩn** xử lý da và lông, có màu vàng nhạt. Tất cả hoạt động tự động và đồng bộ như một cơ thể sống khổng lồ, không cần bất kỳ sự can thiệp có ý thức nào.

## V. Công Pháp & Trận Pháp (功法 与 阵法)

Khuẩn Đoàn không tu luyện — quá trình phân giải tử khí và chuyển hóa thành linh khí là hoàn toàn tự nhiên, một sản phẩm phụ của chu kỳ sinh tồn bẩm sinh vận hành liên tục từ thời Hồng Hoang. Khi bị đe dọa bởi sinh vật khác, Khuẩn Đoàn sử dụng "Tử Khí Bạo Phóng" — tiết ra mùi hôi thối cực mạnh đủ để xua đuổi ngay cả yêu thú cấp cao — mùi này không chỉ khó chịu mà còn mang tử khí loãng, gây chóng mặt, buồn nôn, và ở nồng độ cao có thể khiến tu sĩ Luyện Khí bất tỉnh trong vài khắc. Một đan sư Phế Khí Luyện Đan Phường tên Vân Hạ từng phải dùng giải độc đan sau khi tiến quá gần Đại Phân Giải Hội, về sau cô ghi trong sổ tay: "Cách Đại Hội tối thiểu mười trượng — không bao giờ quên." Ngoài ra, vùng đất nơi Khuẩn Đoàn hoạt động lâu ngày sẽ hình thành một lớp "sa đất" đặc biệt — "Linh Tử Sa" — chứa dược tính mà không có phương pháp luyện đan nhân tạo nào tái tạo được: tinh chất linh khí đã được chuyển hóa tự nhiên từ tử khí, mang cả tính âm lẫn tính dương, cân bằng hoàn hảo theo cách mà đan sư gọi là "Tử Sinh Hòa Hợp."

## VI. Đặc Sản Môn Phái (门派特产)

- **Linh Tử Sa (Sa Đất Dược Tính):** Lớp cát đặc biệt tại nơi Khuẩn Đoàn phân giải xác yêu thú cấp cao, chứa tinh chất linh khí đã được chuyển hóa tự nhiên qua quá trình phân giải. Chất lượng phân chia ba bậc: Hạ Phẩm — từ xác yêu thú thường, màu nâu nhạt; Trung Phẩm — từ xác yêu thú linh trí, màu xám bạc; Thượng Phẩm — từ xác tu sĩ Trúc Cơ trở lên, màu đen ánh tím, cực kỳ hiếm. Là nguyên liệu bí mật then chốt cho đan dược "Hồi Sinh Tán" và "Tử Tịnh Đan" nổi tiếng của Phế Khí Luyện Đan Phường.
- **Linh Khí Tái Tạo:** Linh khí được Khuẩn Đoàn chuyển hóa từ tử khí có tính chất thuần khiết đặc biệt, nuôi dưỡng âm thầm các ốc đảo và linh mạch nhỏ khắp Hoàng Kim Sa Hải. Ốc đảo Cam Tuyền — nổi tiếng nhất Tây Mạc, nơi mọi thương đoàn đều dừng chân — thực chất tồn tại được là nhờ Khuẩn Đoàn thanh lọc tử khí khu vực đó suốt hàng ngàn năm.
- **Cốt Phấn Tịnh Sa:** Bột xương siêu mịn — sản phẩm cuối cùng sau khi Cốt Khuẩn phân giải hoàn toàn xương thú — có tác dụng cường cốt khi pha vào đan dược, được một số dược sư am hiểu sẵn sàng trả giá mười linh thạch hạ phẩm mỗi lạng.

## VII. Cơ Sở Hạ Tầng (基础设施)

Khuẩn Đoàn không xây dựng bất kỳ cơ sở hạ tầng nào — chúng sống và chết ngay trên xác sinh vật mà chúng phân giải, biến cái chết thành ngôi nhà tạm. Tuy nhiên, những khu vực Khuẩn Đoàn hoạt động lâu năm tự nhiên hình thành các "Tịnh Vực" — nơi tử khí gần như bằng không, cát mịn hơn và linh khí ổn định hơn so với các vùng xung quanh, thu hút sinh vật đến trú ngụ. **Vạn Cốt Sa Trường** — bãi chiến trường cổ phía bắc — là Tịnh Vực lớn nhất, giờ đây trở thành vùng đất màu mỡ nhất trong sa mạc dù từng ngập ngụa xác chết; thương nhân qua đường thường dừng nghỉ ở đây vì "không khí trong lành hơn" mà không biết đang đứng trên nghĩa trang ngàn năm. **Ốc đảo Cam Tuyền** cùng bốn ốc đảo nhỏ khác — Bạch Sa Tuyền, Lục Nham Uyên, Thạch Bàn Trạch, và Minh Sa Hồ — trong Hoàng Kim Sa Hải thực chất tồn tại được là nhờ Khuẩn Đoàn đã thanh lọc tử khí trong khu vực suốt hàng nghìn năm, tạo điều kiện cho thực vật và mạch nước phát triển. Những Tịnh Vực này là "di sản" vô hình của Khuẩn Đoàn mà không ai nhận ra.

## VIII. Kinh Tế (经济)
> *"Nếu tính giá trị thực sự, Khuẩn Đoàn là thế lực giàu nhất Tây Mạc — chỉ là chúng không biết đếm tiền."*
> — Phường Chủ Hồng Luyện, nói đùa với đệ tử thân tín


Khuẩn Đoàn không có hoạt động kinh tế chủ động và không hiểu khái niệm giao dịch — chúng phân giải vì bản năng, không vì lợi nhuận. Tuy nhiên, giá trị kinh tế gián tiếp của chúng là vô cùng lớn và nhiều tầng. Linh Tử Sa do chúng tạo ra là nguyên liệu quý hiếm được Phế Khí Luyện Đan Phường bí mật thu gom — Phường Chủ Hồng Luyện cử đội ngũ chuyên trách gồm năm đệ tử luân phiên theo dõi các Đại Phân Giải Hội để thu gom sa đất ngay khi Khuẩn Đoàn hoàn thành công việc, đây là thành phần then chốt trong "Hồi Sinh Tán" và "Tử Tịnh Đan" nổi tiếng — hai loại đan dược mang lại hơn nửa doanh thu hàng năm của phường. Ngoài ra, vai trò thanh lọc tử khí của Khuẩn Đoàn gián tiếp duy trì giá trị thương mại của toàn bộ Thiên Sa Thương Đạo — nếu tử khí tràn ngập, không thương nhân nào dám đi qua sa mạc, và toàn bộ tuyến thương mại xuyên Tây Mạc trị giá hàng triệu linh thạch mỗi năm sẽ sụp đổ.

## IX. Lịch Sử Tóm Tắt (简史)

Linh Sa Khuẩn Đoàn tồn tại từ thời Hồng Hoang, song hành cùng sự hình thành của Hoàng Kim Sa Hải — khi sa mạc mới là biển cạn dần, xác sinh vật biển phơi trên cát, và Khuẩn Đoàn nguyên thủy bắt đầu vai trò phân giải đầu tiên. Chúng là hệ sinh thái nền tảng — không có Khuẩn Đoàn, xác chết sinh vật sẽ tích tụ qua hàng vạn năm, tử khí sẽ ứ đọng và biến toàn bộ sa mạc thành vùng tử địa không thể sinh tồn. Xuyên suốt lịch sử, rất ít chủng tộc hay tu sĩ để ý đến sự tồn tại của chúng — xác chết biến mất trong cát được coi là "sa mạc nuốt chửng mọi thứ," không ai nghĩ đó là công trình của hàng tỷ vi sinh vật. Cách đây ba trăm năm, đan sư kỳ tài Hồng Luyện — khi đó còn là tán tu lang thang — vô tình phát hiện Linh Tử Sa khi nằm ngủ trên nền đất nơi Khuẩn Đoàn vừa phân giải xác sa mãng cổ, sáng dậy thấy bệnh cũ thuyên giảm rõ rệt. Từ đó bà nghiên cứu và khai thác nguồn tài nguyên này, thành lập Phế Khí Luyện Đan Phường trên nền tảng bí mật về Khuẩn Đoàn — câu chuyện khởi nghiệp kỳ lạ nhất Tây Mạc.

## X. Giai Thoại & Bí Mật (轶事 与 秘密)

- Phế Khí Luyện Đan Phường lén thu gom Linh Tử Sa từ nơi Khuẩn Đoàn phân giải xác yêu thú cấp cao — đó là nguyên liệu bí mật cho "Hồi Sinh Tán" và "Tử Tịnh Đan" nổi danh, và cũng là lý do phường này có thể luyện ra những loại đan mà nơi khác không thể bắt chước dù có đủ công thức. Phường Chủ Hồng Luyện giấu bí mật này như giữ mạng sống — chỉ năm đệ tử thân tín nhất mới biết nguồn gốc thực sự của nguyên liệu, và mỗi đệ tử đều phải lập Tâm Thệ không tiết lộ.
- Gần đây, Khuẩn Đoàn bắt đầu tránh xa một khu vực cụ thể trong Hoàng Kim Sa Hải — "Tử Bất Phân Vực" — nơi đó có xác chết nhưng chúng không dám đến gần, mùi tử khí nồng nặc mà Khuẩn Đoàn vốn không bao giờ sợ lại khiến chúng rút lui. Xác chết đó còn "sống" theo nghĩa nào đó — tử khí tại khu vực đó tích tụ bất thường, hình thành "Tử Khí Cột" cao mười trượng nhìn thấy bằng mắt thường trong đêm tối, thu hút sự chú ý lo ngại của các thế lực xung quanh. Thương nhân đi ngang qua khu vực đó kể rằng lạc đà cưỡi không chịu bước vào bán kính năm dặm, dù đánh đập cỡ nào cũng không đi.
- Sa Mãng Tộc đôi khi để xác con mồi ngoài hang cho Khuẩn Đoàn xử lý — mối quan hệ cộng sinh âm thầm giữa hai bên đã kéo dài hàng nghìn năm. Trưởng Lão Sa Mãng tên Hoàng Quyển thậm chí có thói quen ném xương thú về phía vùng cát mà lão cảm nhận Khuẩn Đoàn đang hoạt động, như thể "cho ăn" — nhưng không bên nào thực sự "nhận thức" được sự hợp tác này.

## XI. Quan Hệ Thế Lực (势力关系)

- **Phế Khí Luyện Đan Phường:** Khách hàng bí mật lớn nhất và kẻ khai thác duy nhất biết đến giá trị thực sự của Khuẩn Đoàn. Thu gom Linh Tử Sa từ các khu vực Khuẩn Đoàn hoạt động, coi đây là bí mật thương mại tối thượng. Mối quan hệ hoàn toàn một chiều — Khuẩn Đoàn không biết sự tồn tại của phường này, và Phường Chủ Hồng Luyện sẵn sàng tiêu diệt bất kỳ ai phát hiện ra bí mật, kể cả đệ tử phản bội.
- **Sa Mãng Tộc:** Cộng sinh tự nhiên lâu đời nhất trong Hoàng Kim Sa Hải. Sa Mãng để lại xác con mồi cho Khuẩn Đoàn phân giải, đổi lại hang ổ được giữ sạch tử khí — vòng tuần hoàn hoàn hảo vận hành bằng bản năng thay vì giao ước. Hai bên tương tác hoàn toàn tự nhiên, không lời nói, không cam kết, nhưng bền vững hơn mọi hiệp ước chính trị.
- **Hệ sinh thái Hoàng Kim Sa Hải:** Khuẩn Đoàn là nền tảng sinh thái không thể thay thế. Nếu chúng biến mất, tử khí sẽ tràn ngập và hủy diệt sự sống trên toàn sa mạc trong vòng vài thập kỷ, kéo theo sự sụp đổ kinh tế của Thiên Sa Thương Đạo và mọi thế lực phụ thuộc vào tuyến thương mại xuyên Tây Mạc. Cam Tuyền ốc đảo sẽ là nơi đầu tiên chết — và cũng là nơi mà mọi thương nhân sẽ nhận ra quá muộn rằng mình đã mất gì.

Ngoài ra, có một hiện tượng mà dân sa mạc gọi là "Đêm Phát Sáng" — vào những đêm không trăng, vùng cát nơi Khuẩn Đoàn đang phân giải xác yêu thú lớn phát ra ánh sáng xanh nhạt mờ ảo. Đó là Linh Khuẩn đang chuyển hóa tử khí thành linh khí với cường độ cao, và ánh sáng chính là sản phẩm phụ của quá trình. Thương nhân mê tín coi đó là hồn ma yêu thú, nhưng đan sư Hồng Luyện dùng ánh sáng này làm chỉ dấu để tìm nguồn Linh Tử Sa chất lượng cao nhất.

