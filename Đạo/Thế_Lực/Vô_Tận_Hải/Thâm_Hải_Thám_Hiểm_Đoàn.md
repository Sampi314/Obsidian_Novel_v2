---
type: faction
name: Thâm Hải Thám Hiểm Đoàn
hantu: 深海探險團
faction_type: Hội
alignment: 3
race: Nhân Tộc
region: Vô Tận Hải
founded: 120 năm trước
founder: Lục Thâm Hải
emblem: Tham_Hiem_Tham_Hai.png
specialty: Thâm Hải Hộ Thể Quyết, khai quật di tích đáy biển, giải mã cổ trận
economy:
  - Bán pháp khí cổ đại khai quật từ đáy biển
  - Nhận hợp đồng thám hiểm từ các thế lực lớn
  - Bán bản đồ và thông tin về di tích chìm
arcs:
  - arc: 1
    status: Hoạt động tích cực
    rank: Hạng Tư
    leader: Đoàn Trưởng Lục Thâm Hải (Kim Đan Sơ Kỳ)
    population: 27
    territory:
      - Thuyền mẹ "Thâm Uyên Hào" — neo đậu vùng biển trung tâm Vô Tận Hải
      - Một số điểm trung chuyển tạm thời tại các bến cảng ven biển
    assets:
      - name: Thâm Uyên Hào
        type: Công Trình
      - name: Thâm Hải Giáp (3 bộ)
        type: Pháp Bảo
      - name: Mảnh bản đồ Hải Để Thần Điện
        type: Tài Nguyên
    stats: [200, 180, 350, 160, 150, 250]
    divisions:
      - name: Đội Lặn Sâu
        role: Thực hiện các chuyến thám hiểm dưới đáy biển, khai quật di tích
        headcount:
          hoi_truong: 1
          pho_hoi_truong: 0
          thanh_vien: 15
          tong_quan: 0
        members:
          - character: Lục Thâm Hải
            position: Đoàn Trưởng kiêm Trưởng Đội Lặn
            cultivation: Kim Đan Sơ Kỳ
          - character: "[Phó Đội Lặn Alpha]"
            position: Đội Trưởng Đội Lặn 1
            cultivation: Trúc Cơ Hậu Kỳ
            placeholder: true
          - character: "[Phó Đội Lặn Beta]"
            position: Đội Trưởng Đội Lặn 2
            cultivation: Trúc Cơ Trung Kỳ
            placeholder: true
          - character: "[Phó Đội Lặn Gamma]"
            position: Đội Trưởng Đội Lặn 3
            cultivation: Trúc Cơ Trung Kỳ
            placeholder: true
      - name: Đội Hậu Cần
        role: Vận hành thuyền mẹ, bảo dưỡng thiết bị, hỗ trợ y tế
        headcount:
          hoi_truong: 0
          pho_hoi_truong: 0
          thanh_vien: 10
          tong_quan: 0
        members:
          - character: "[Quản Sự Thuyền Mẹ]"
            position: Trưởng Hậu Cần
            cultivation: Luyện Khí Viên Mãn
            placeholder: true
      - name: Chuyên Gia Giải Mã
        role: Nghiên cứu cổ tự, phân tích trận pháp cổ đại, lập bản đồ di tích
        headcount:
          hoi_truong: 0
          pho_hoi_truong: 0
          thanh_vien: 2
          tong_quan: 0
        members:
          - character: "[Cổ Văn Chuyên Gia]"
            position: Trưởng Giải Mã
            cultivation: Trúc Cơ Sơ Kỳ
            placeholder: true
    relationships:
      - faction: Hải Thần Cung
        description: Quan hệ căng thẳng — Hải Thần Cung từng tịch thu toàn bộ chiến lợi phẩm từ một di tích lớn mà đoàn phát hiện, gây ra oán hận sâu sắc.
        diplomacy:
          lien_minh: -20
          tin: -40
          uy_hiep: 60
          thuong_mai: 10
          on_oan: -50
          le_thuoc: 30
      - faction: Hải Quy Trưởng Lão Hội
        description: Quan hệ tốt — Hải Quy Trưởng Lão Hội đôi khi cung cấp thông tin về vị trí di tích cổ đại để đổi lấy hiện vật khai quật được.
        diplomacy:
          lien_minh: 30
          tin: 40
          uy_hiep: 0
          thuong_mai: 50
          on_oan: 20
          le_thuoc: 0
      - faction: Thâm Hải Vi Linh
        description: Chưa tiếp xúc — biết đến sự tồn tại của Vi Linh qua truyền thuyết nhưng chưa lặn đủ sâu để gặp chúng.
        diplomacy:
          lien_minh: 0
          tin: 0
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 0
---

# Thâm Hải Thám Hiểm Đoàn (深海探險團)

## I. Tổng Quan (总览)

Thâm Hải Thám Hiểm Đoàn là một tổ chức nhỏ chuyên khai quật di tích và tàn tích của các nền văn minh cổ đại bị nhấn chìm dưới đáy Vô Tận Hải. Với chỉ hai mươi bảy thành viên và ba bộ Thâm Hải Giáp cũ kỹ, đoàn thuộc hạng tư về quy mô nhưng sở hữu kinh nghiệm thám hiểm biển sâu vượt xa bất kỳ thế lực nào khác. Trụ sở của đoàn là thuyền mẹ "Thâm Uyên Hào", một chiến hạm cải tạo neo đậu tại vùng biển trung tâm Vô Tận Hải. Đoàn trưởng Lục Thâm Hải — người sống sót qua hơn năm mươi chuyến thám hiểm — là linh hồn và xương sống của toàn tổ chức. Tỷ lệ tử vong trung bình ba trong mười người mỗi chuyến khiến đoàn nổi tiếng là nơi nguy hiểm nhất để mưu sinh, nhưng cũng là nơi duy nhất có thể chạm tay vào những bí mật bị thời gian vùi lấp.

## II. Địa Lý & Tài Nguyên (地理 与 资源)

Thâm Hải Thám Hiểm Đoàn không sở hữu lãnh thổ cố định mà hoạt động trên khắp các vùng biển sâu của Vô Tận Hải, nơi ẩn chứa di tích của những nền văn minh cổ đại đã bị nhấn chìm. Các khu vực thám hiểm thường nằm ở độ sâu hàng trăm trượng, nơi áp suất nước có thể nghiền nát tu sĩ Trúc Cơ thiếu bảo hộ, hải thú hung dữ rình rập, và trận pháp cổ đại vẫn còn vận hành sau hàng vạn năm. Tài nguyên thu được từ các chuyến lặn bao gồm pháp khí hư hỏng, linh thạch phong hóa, cổ thư đã mờ chữ, và thỉnh thoảng là một bảo vật thật sự có giá trị. Thuyền mẹ Thâm Uyên Hào tuy không lộng lẫy nhưng được trang bị đầy đủ kho chứa, phòng nghiên cứu và thiết bị lặn — tất cả đều do Lục Thâm Hải tự tay cải tiến qua nhiều năm.

## III. Văn Hóa & Tín Ngưỡng (文化 与 信仰)

Thành viên Thâm Hải Thám Hiểm Đoàn đều là những kẻ liều mạng — họ coi trọng phát hiện hơn mạng sống, đặt sự tò mò về quá khứ lên trên bản năng sinh tồn. Trước mỗi chuyến lặn lớn, cả đoàn tập trung trên boong thuyền mẹ, uống rượu biển và viết di chúc. Đây không phải nghi thức mê tín mà là truyền thống thực tế — bởi cứ mười người xuống biển sâu thì trung bình ba người không bao giờ trở lại. Những ai sống sót sau mười chuyến được gọi là "Lão Quỷ Biển Sâu", một danh hiệu vừa kính trọng vừa mỉa mai. Đoàn không thờ thần linh nào cụ thể, nhưng có một quy tắc bất thành văn: mỗi khi phát hiện hài cốt dưới đáy biển, phải dành một phút im lặng tưởng niệm trước khi tiếp tục khai quật.

## IV. Cơ Cấu Tổ Chức (组织结构)

Thâm Hải Thám Hiểm Đoàn có cơ cấu đơn giản, chia thành ba bộ phận chính dưới quyền chỉ huy của Đoàn Trưởng Lục Thâm Hải. Đội Lặn Sâu gồm ba tiểu đội, mỗi đội năm người từ Trúc Cơ trở lên, là lực lượng nòng cốt trực tiếp xuống di tích. Đội Hậu Cần gồm mười người Luyện Khí phụ trách vận hành thuyền mẹ, bảo dưỡng Thâm Hải Giáp, và chuẩn bị vật tư cho mỗi chuyến lặn. Hai Chuyên Gia Giải Mã chuyên nghiên cứu cổ tự và phân tích trận pháp cổ đại, giúp đoàn tránh kích hoạt nhầm cơ quan phòng thủ trong di tích. Việc tuyển dụng cực kỳ khó khăn — ít ai muốn gia nhập một tổ chức có tỷ lệ tử vong ba trên mười, nên phần lớn thành viên mới đều là kẻ tuyệt vọng, người bị truy nã, hoặc tu sĩ tán tu không có nơi nào khác chấp nhận.

## V. Công Pháp & Trận Pháp (功法 与 阵法)

Công pháp cốt lõi của đoàn là **Thâm Hải Hộ Thể Quyết**, một phương pháp vận dụng linh lực tạo lớp bảo hộ chống áp suất nước sâu quanh cơ thể. Quyết này không tăng sức chiến đấu nhưng là điều kiện tiên quyết để sinh tồn dưới đáy biển — không có nó, ngay cả tu sĩ Kim Đan cũng khó chịu nổi áp suất ở độ sâu quá năm trăm trượng. Pháp khí đặc chế của đoàn là **Thâm Hải Giáp** — bộ giáp linh khí cho phép người mặc lặn sâu hàng trăm trượng, bảo vệ khỏi áp suất và cung cấp dưỡng khí. Hiện chỉ còn ba bộ hoạt động; hai bộ khác đã hỏng nặng và đoàn không có đủ tài nguyên để sửa chữa. Ngoài ra, đội giải mã thường xuyên phải đối mặt với trận pháp cổ đại trong di tích — việc giải trận sai một bước có thể khiến cả đội bị chôn vùi.

## VI. Đặc Sản Môn Phái (门派特产)

- **Hải Để Cổ Vật:** Pháp khí, linh thạch và cổ thư khai quật từ di tích chìm, nhiều món có tuổi đời hàng vạn năm. Tuy phần lớn đã hư hỏng, nhưng những món còn nguyên vẹn có giá trị cực cao trên thị trường.
- **Bản Đồ Đáy Biển:** Thâm Hải Thám Hiểm Đoàn là tổ chức duy nhất có hệ thống bản đồ chi tiết về các di tích đáy biển Vô Tận Hải. Các thế lực lớn phải trả giá cao để mua thông tin này.
- **Thâm Hải Hộ Thể Phù:** Bùa hộ thể dùng một lần, chế tác dựa trên Thâm Hải Hộ Thể Quyết, cho phép tu sĩ Luyện Khí chịu được áp suất biển sâu trong thời gian ngắn.

## VII. Cơ Sở Hạ Tầng (基础设施)

- **Thâm Uyên Hào:** Thuyền mẹ của đoàn, một chiến hạm cũ được cải tạo thành tổng hành dinh di động. Bên trong có kho chứa hiện vật, phòng nghiên cứu giải mã, xưởng bảo dưỡng Thâm Hải Giáp, và khu sinh hoạt cho toàn bộ thành viên.
- **Phòng Giải Mã:** Nằm trong lòng thuyền mẹ, chứa đầy cổ thư sao chép, mẫu cổ tự và bản đồ di tích. Hai chuyên gia giải mã dành phần lớn thời gian ở đây.
- **Xưởng Bảo Dưỡng:** Nơi sửa chữa và bảo trì ba bộ Thâm Hải Giáp — thiết bị quý giá nhất của đoàn. Trang bị thô sơ, phần lớn công việc phải làm thủ công.

## VIII. Kinh Tế (经济)

Kinh tế của Thâm Hải Thám Hiểm Đoàn hoàn toàn phụ thuộc vào kết quả khai quật. Sau mỗi chuyến thám hiểm thành công, đoàn bán pháp khí cổ đại, linh thạch phong hóa và cổ vật cho các thương hội hoặc tông môn có nhu cầu. Ngoài ra, đoàn cũng nhận hợp đồng thám hiểm theo yêu cầu từ các thế lực lớn — ví dụ tìm kiếm một bảo vật cụ thể hoặc khảo sát một vùng biển chưa được khai phá. Thông tin về vị trí di tích cũng là nguồn thu — bản đồ đáy biển của đoàn được nhiều bên săn đón. Tuy nhiên, thu nhập cực kỳ bất ổn: một chuyến thám hiểm thất bại không chỉ không thu được gì mà còn mất người và thiết bị, đẩy đoàn vào cảnh nợ nần.

## IX. Lịch Sử Tóm Tắt (简史)

Lục Thâm Hải vốn là kẻ mồ côi lớn lên trên bến cảng, từ nhỏ đã bị ám ảnh bởi truyền thuyết về những thành phố chìm dưới đáy biển. Khi vừa đạt Trúc Cơ, gã tập hợp một nhóm bạn bè liều lĩnh và lập đoàn thám hiểm. Những năm đầu là thảm họa — gã mất gần hết đồng đội trong các chuyến lặn sơ khai, khi thiết bị thô sơ và kinh nghiệm bằng không. Nhưng Lục Thâm Hải không bỏ cuộc; mỗi lần mất người, gã học thêm một bài học bằng máu và nước mắt. Dần dần, đoàn tích lũy đủ kinh nghiệm để giảm tỷ lệ tử vong từ bảy trên mười xuống còn ba trên mười — một thành tựu mà Lục Thâm Hải vừa tự hào vừa xấu hổ. Sự kiện đau đớn nhất trong lịch sử đoàn là khi họ phát hiện một di tích lớn chứa đầy bảo vật, chỉ để Hải Thần Cung xuất hiện và "tịch thu" toàn bộ chiến lợi phẩm với lý do "bảo vệ di sản biển cả."

## X. Giai Thoại & Bí Mật (轶事 与 秘密)

Lục Thâm Hải giấu một mảnh bản đồ chỉ đến "Hải Để Thần Điện" — nơi được cho là cung điện của vị Thần Nước đầu tiên, nằm sâu hơn bất kỳ di tích nào đoàn từng khám phá. Gã không dám tiết lộ cho ai vì biết rằng một khi tin tức lộ ra, các thế lực lớn sẽ tranh giành và đoàn nhỏ bé của gã sẽ bị nghiền nát. Trong một chuyến lặn cách đây mười năm, đoàn phát hiện xác một tu sĩ cảnh giới cực cao chết trong tư thế ngồi thiền dưới đáy biển — linh khí quanh thi thể vẫn dày đặc đến mức khiến hai thành viên đoàn bất tỉnh. Lục Thâm Hải mang theo vết sẹo lớn trên lưng — kỷ niệm từ lần suýt chết đầu tiên khi mới mười sáu tuổi, bị một xúc tu hải quái kéo xuống vực — và gã coi vết sẹo đó là lời nhắc nhở rằng biển cả không bao giờ tha thứ cho sự bất cẩn.

## XI. Quan Hệ Thế Lực (势力关系)

- **Hải Thần Cung:** Quan hệ căng thẳng. Hải Thần Cung từng tịch thu chiến lợi phẩm của đoàn từ một di tích lớn, khiến Lục Thâm Hải oán hận sâu sắc. Tuy nhiên, đoàn quá nhỏ để đối đầu và phải cúi đầu chấp nhận.
- **Hải Quy Trưởng Lão Hội:** Quan hệ hợp tác. Các trưởng lão rùa biển sống lâu năm nắm giữ ký ức về vị trí nhiều di tích cổ đại. Đoàn đổi cổ vật khai quật được để lấy thông tin từ họ, hai bên cùng có lợi.
- **Thâm Hải Vi Linh:** Chưa tiếp xúc trực tiếp. Đoàn biết đến sự tồn tại của Vi Linh qua truyền thuyết và ghi chép cổ, nhưng chưa bao giờ lặn đủ sâu để chạm tới Vực Thẳm Vạn Trượng nơi chúng sinh sống.
