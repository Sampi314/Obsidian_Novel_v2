---
type: faction
name: Mộc Tinh Linh Công Nhân
hantu: 木精灵工人
faction_type: Hội
alignment: -2
race: Tinh Linh
region: Đông Hoang
founded: Cùng thời với hệ thống giai cấp Vương Đình (khoảng 5000 năm trước)
founder: Không có (giai cấp bị áp đặt)
emblem: Moc_Tinh_Linh_Cong_Nhan.png
specialty: Khai thác linh mộc, Chăm sóc rừng, Lao động xây dựng
economy:
- Khai thác và vận chuyển linh mộc cho Vương Đình
- Chăm sóc và tái trồng rừng theo lệnh
- Xây dựng công trình cho giới quý tộc tinh linh
arcs:
  - arc: 1
    status: Bất mãn sôi sục
    rank: Không Xếp Hạng
    leader: Không có lãnh đạo chính thức
    population: 2000
    territory:
      - Khu vực rìa ngoài Vĩnh Hằng Sâm Lâm
      - Trại lao động phía đông rừng
      - Trại lao động phía nam rừng
    assets:
      - name: Công cụ khai thác linh mộc
        type: Tài Nguyên
      - name: Mạng lưới dân ca mật mã
        type: Tài Nguyên
    stats: [5, 10, 5, 2000, 5, 8]
    divisions:
      - name: Đội Lao Động (do Vương Đình chỉ định)
        role: Khai thác linh mộc, chăm sóc rừng, và xây dựng theo lệnh Vương Đình
        headcount:
          hoi_truong: 0
          pho_hoi_truong: 0
          thanh_vien: 1980
          tong_quan: 20
        members:
          - character: "[Đội Trưởng Giáp]"
            position: Đội Trưởng (do Vương Đình chỉ định)
            cultivation: Trúc Cơ Sơ Kỳ
            placeholder: true
          - character: "[Đội Trưởng Ất]"
            position: Đội Trưởng (do Vương Đình chỉ định)
            cultivation: Luyện Khí Đỉnh Phong
            placeholder: true
    relationships:
      - faction: Tinh Linh Vương Đình
        description: Quan hệ chủ - nô. Công nhân phải tuân lệnh tuyệt đối, bị cấm tổ chức tập thể, và không được hưởng quyền lợi cơ bản.
        diplomacy:
          lien_minh: -80
          tin: -70
          uy_hiep: 90
          thuong_mai: -100
          on_oan: -90
          le_thuoc: 95
      - faction: Bán Tinh Linh Hội
        description: Cùng chung cảnh ngộ bị áp bức, có sự đồng cảm ngầm nhưng chưa dám liên lạc công khai.
        diplomacy:
          lien_minh: 20
          tin: 30
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 0
      - faction: Hắc Tinh Linh Lưu Đày
        description: Một số công nhân bỏ trốn đã gia nhập Hắc Tinh Linh, tạo ra mối liên hệ ngầm giữa hai nhóm.
        diplomacy:
          lien_minh: 25
          tin: 35
          uy_hiep: 0
          thuong_mai: 5
          on_oan: 10
          le_thuoc: 0
---

# Mộc Tinh Linh Công Nhân (木精灵工人)

> *"Cây cũng biết đau, nhưng ai nghe tiếng cây khóc? Chúng ta cũng biết đau, nhưng ai nghe tiếng ta khóc?"*
> — Bài dân ca mật mã số 7, truyền miệng giữa các trại lao động

## I. Tổng Quan (总览)
Mộc Tinh Linh Công Nhân không phải một tổ chức tự nguyện mà là một giai cấp bị áp đặt bởi hệ thống đẳng cấp của Tinh Linh Vương Đình. Khoảng 2000 tinh linh cấp thấp — đa số ở trình độ Luyện Khí hoặc chưa tu luyện — bị phân vào tầng lớp lao động, suốt đời khai thác linh mộc, chăm sóc rừng, và xây dựng cho giới quý tộc mà không được đền đáp xứng đáng. Họ bị cấm tổ chức tập thể, cấm tu luyện công pháp chiến đấu, và bị giám sát chặt chẽ bởi các đội trưởng do Vương Đình chỉ định. Dù không có lãnh đạo hay cơ cấu chính thức, sự bất mãn đang âm ỉ trong hàng ngũ công nhân như lửa cháy dưới tro tàn, chỉ chờ ngọn gió đúng lúc để bùng lên.

## II. Địa Lý & Tài Nguyên (地理与资源)
Công nhân sinh sống và lao động tại khu vực rìa ngoài Vĩnh Hằng Sâm Lâm — nơi linh mộc được khai thác phục vụ nhu cầu của Vương Đình. Khu vực này bao gồm nhiều trại lao động rải rác, mỗi trại chứa vài trăm công nhân sống trong lều tạm bợ dựng bằng chính linh mộc họ khai thác. Trại lớn nhất — Đông Lâm Trại — nằm sát khu rừng Linh Sam cổ thụ, nơi linh mộc có tuổi thọ vài trăm năm bị đốn liên tục để cung cấp nguyên liệu chế tạo pháp khí cho quý tộc. Đất đai xung quanh các trại bạc màu do khai thác quá mức, trái ngược hoàn toàn với sự tươi tốt của rừng sâu nơi quý tộc tinh linh cư trú. Dọc theo con lạch Mộc Thanh chảy qua trại phía đông, nước đã đổi sang màu đục vàng vì đất bị xói mòn — dấu tích của hàng nghìn năm phá rừng không ngừng nghỉ. Công nhân không sở hữu bất kỳ tài nguyên nào — tất cả sản phẩm lao động từ gỗ linh mộc đến nhựa cây quý đều thuộc về Vương Đình. Tài sản duy nhất họ có là công cụ khai thác thô sơ và những bài dân ca cổ truyền miệng qua nhiều thế hệ.
Khu vực xung quanh ẩn chứa nhiều bí mật chưa được khám phá — hang động chưa ai đến, mạch khoáng chưa ai biết, dấu tích cổ đại mà thời gian chưa kịp xóa nhòa.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
Trong cảnh đời khốn khó, công nhân tinh linh vẫn duy trì một nền văn hóa ngầm đầy sức sống. Triết lý sống của họ được gói gọn trong câu nói truyền miệng: "Cây cũng biết đau, nhưng ai nghe tiếng cây khóc?" — vừa thể hiện sự đồng cảm với thiên nhiên bị khai thác, vừa ẩn dụ cho nỗi đau bị phớt lờ của chính họ. Quy tắc do Vương Đình áp đặt rất hà khắc: không được tụ tập quá 5 người, không được rời khu lao động khi chưa hoàn thành phần việc, không được hát bài ca nào chưa được duyệt. Tuy nhiên, công nhân bí mật gìn giữ và truyền bá những bài dân ca cổ khi làm việc — bài "Linh Sâm Khúc" ca ngợi rừng thiêng nhưng ẩn chứa số đếm thời gian tuần tra, bài "Lạc Diệp Dao" nghe như lời ru con nhưng thực chất là bản đồ các lối thoát qua rìa rừng. Bề ngoài, các bài ca này nghe như lời ngợi ca Vương Đình và rừng thiêng, nhưng ẩn trong ca từ là những thông điệp phản kháng, những lời hẹn ước và hy vọng về một ngày tự do. Một phong tục bí mật đặc biệt xúc động là nghi thức "Tặng Lá" — khi một công nhân già yếu sắp qua đời, đồng đội sẽ đặt lên lòng bàn tay người ấy một chiếc lá linh mộc non, tượng trưng cho lời hứa rằng thế hệ sau sẽ sống tốt hơn.
Mỗi thế hệ mới được truyền dạy không chỉ kỹ năng sinh tồn mà cả câu chuyện về nguồn cội, để ngọn lửa ký ức không bao giờ tắt dù hoàn cảnh khắc nghiệt đến đâu.

## IV. Cơ Cấu Tổ Chức (组织结构)
Mộc Tinh Linh Công Nhân không có tổ chức chính thức — Vương Đình nghiêm cấm mọi hình thức tập hợp tự phát. Cơ cấu quản lý hoàn toàn do Vương Đình áp đặt: khoảng 20 Đội Trưởng được chỉ định từ số tinh linh trung thành với hệ thống, mỗi người giám sát một nhóm 100 công nhân. Đội Trưởng vừa là giám sát viên vừa là kẻ chỉ điểm, báo cáo mọi dấu hiệu bất phục tùng lên quý tộc. Tuy nhiên, bên dưới bề mặt tuân phục, các mối liên hệ ngầm giữa công nhân tại các trại khác nhau vẫn tồn tại qua hệ thống dân ca mật mã. Không có ai đứng đầu phong trào ngầm này — nó tồn tại dưới dạng mạng lưới phân tán, khiến Vương Đình khó lòng triệt phá hoàn toàn.

## V. Công Pháp & Trận Pháp (功法与阵法)
Công nhân tinh linh bị cấm tuyệt đối tu luyện bất kỳ công pháp chiến đấu nào. Họ chỉ được phép sử dụng thuật mộc hệ cấp thấp nhất — vừa đủ để chặt cây, vận chuyển gỗ, và thực hiện các công việc lao động nặng nhọc. Thuật này bao gồm "Mộc Thao Khống" (điều khiển cành cây nhỏ), "Căn Hệ Cảm Ứng" (cảm nhận rễ cây để tránh đào trúng rễ chính), và "Vận Mộc Thuật" (dùng linh lực đẩy khối gỗ lớn). Không có trận pháp nào thuộc về công nhân — các trại lao động được bảo vệ bởi trận pháp giám sát của Vương Đình, nhưng mục đích là giam giữ chứ không phải bảo vệ.

## VI. Đặc Sản Môn Phái (门派特产)
- **Linh Mộc Khai Thác:** Gỗ linh mộc chất lượng cao được khai thác từ rìa Vĩnh Hằng Sâm Lâm, là nguyên liệu chế tạo pháp khí mộc hệ và xây dựng cung điện tinh linh. Đặc biệt quý giá là gỗ Linh Sam Thiên Niên từ khu rừng phía đông, có vân gỗ chứa linh lực tự nhiên và cứng hơn thép phàm. Tuy nhiên, toàn bộ sản phẩm thuộc về Vương Đình.
- **Thủ Công Ẩn Giấu:** Trong những khoảnh khắc hiếm hoi được nghỉ ngơi, một số công nhân khéo tay bí mật chế tạo các vật phẩm nhỏ từ mẩu gỗ thừa — tượng nhỏ hình chim trĩ (biểu tượng tự do), sáo trúc tự chế, hoặc bùa gỗ khắc ký hiệu đoàn kết mà chỉ công nhân mới hiểu. Những vật phẩm này được trao đổi giữa các trại như biểu tượng tình đoàn kết, và một chiếc bùa gỗ mang ký hiệu "Cành Gãy Mọc Lại" đã trở thành dấu hiệu nhận biết ngầm của phong trào phản kháng.
- **Dân Ca Mật Mã:** Tài sản tinh thần quý giá nhất — hệ thống gồm ít nhất hai mươi ba bài hát cổ mã hóa thông tin, truyền tin giữa các trại mà giám sát viên không thể phát hiện. Bài ca thứ mười ba — "Ngàn Rễ Một Gốc" — được coi là "quốc ca ngầm" của công nhân, hát lên khi có tin tốt lành từ bên ngoài.
Ngoài ra, Mộc Tinh Linh Công Nhân còn sở hữu vật phẩm có giá trị văn hóa hơn vật chất — thứ mà thương nhân bỏ qua nhưng nhà sử học trả bất cứ giá nào.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Trại Lao Động Phía Đông (Đông Lâm Trại):** Trại lớn nhất với khoảng 800 công nhân, chuyên khai thác linh mộc cỡ lớn. Lều tạm bợ xếp thành hàng, không có vách ngăn riêng tư. Nằm sát khu rừng Linh Sam, là nơi có điều kiện sống khắc nghiệt nhất.
- **Trại Lao Động Phía Nam (Nam Lâm Trại):** Trại thứ hai với 600 công nhân, tập trung vào chăm sóc và tái trồng rừng theo kế hoạch của Vương Đình.
- **Các Trại Nhỏ Rải Rác:** Khoảng 600 công nhân phân bổ tại nhiều trại nhỏ khắp rìa rừng, thực hiện các công việc xây dựng, vận chuyển, và bảo trì.
- **Nhà Kho Tập Kết:** Các điểm tập kết gỗ linh mộc trước khi vận chuyển vào Vương Đình, luôn có lính canh giám sát.
Toàn bộ hạ tầng mang dấu ấn đặc trưng cộng đồng — không phải xa hoa mà là thực dụng đúc kết qua nhiều thế hệ thử nghiệm.

## VIII. Kinh Tế (经济)
Mộc Tinh Linh Công Nhân không có kinh tế độc lập. Toàn bộ sức lao động bị chiếm đoạt bởi Vương Đình, đổi lại chỉ nhận được lương thực tối thiểu và chỗ ở tạm bợ. Giá trị kinh tế thực sự mà họ tạo ra rất lớn — linh mộc khai thác từ Vĩnh Hằng Sâm Lâm là một trong những nguồn tài nguyên giá trị nhất Đông Hoang, nhưng công nhân không được hưởng bất kỳ phần nào. Hoạt động kinh tế ngầm duy nhất là trao đổi nhỏ lẻ giữa các trại: thực phẩm, công cụ tự chế, và đôi khi vài mẩu linh mộc thừa giấu được. Hệ thống bóc lột này là một trong những nguyên nhân chính nuôi dưỡng sự bất mãn ngày càng sâu sắc.
Tiềm năng kinh tế vượt xa những gì đang được khai thác — sự thiếu hụt nhân lực, kiến thức thương mại, và bảo hộ chính trị khiến phần lớn giá trị vẫn nằm yên.

## IX. Lịch Sử Tóm Tắt (简史)
Kể từ khi Tinh Linh Vương Đình thiết lập hệ thống giai cấp cách đây khoảng 5000 năm, những tinh linh không mang huyết mạch cao quý bị phân vào tầng lớp lao động. Thế hệ này nối tiếp thế hệ khác, công nhân khai thác linh mộc, chăm sóc rừng, và xây dựng cho Vương Đình mà không được đền đáp xứng đáng. Trong lịch sử đã có ít nhất ba lần nổi loạn nhỏ: lần đầu cách đây 3000 năm khi một nhóm công nhân cố gắng bỏ trốn tập thể qua Khe Trúc phía tây nhưng bị kỵ sĩ linh ưng truy bắt, lần thứ hai khoảng 1500 năm trước khi Đội Trưởng Cổ Mộc quay sang bênh vực công nhân và tuyên bố "rừng không thuộc về bất kỳ vương triều nào" trước khi bị xử tử công khai, và lần gần nhất là 200 năm trước khi một cuộc đình công ngắn xảy ra tại trại phía đông do thiếu lương thực trầm trọng vào mùa đông giá rét. Cả ba đều bị Vương Đình dập tắt nhanh chóng và tàn nhẫn, kẻ cầm đầu bị lưu đày hoặc xử tử. Tuy nhiên, mỗi lần thất bại lại gieo thêm hạt giống bất mãn vào thế hệ sau — tên Cổ Mộc vẫn được nhắc đến trong bài dân ca mật mã số chín như một vị anh hùng.
Mỗi thế hệ kế tiếp gánh di sản và gánh nặng thế hệ trước — nhưng cũng mang khả năng mới mà cha ông chưa từng tưởng tượng.

## X. Giai Thoại & Bí Mật (轶事与秘密)
Trong đám công nhân đang hình thành một phong trào ngầm chưa có tên gọi chính thức, mà những người trong cuộc gọi bằng mật danh "Rễ Sâu." Không có lãnh đạo rõ ràng, không có cương lĩnh cụ thể — chỉ là sự bất mãn đang sôi sục lan tỏa qua những bài dân ca mật mã và ánh mắt trao nhau giữa các trại. Một số bài dân ca cổ mà công nhân hát khi làm việc thực chất chứa hệ thống mật mã tinh vi, cho phép truyền tin về lịch trình tuần tra của lính canh, thời điểm vận chuyển linh mộc, và thậm chí danh sách đội trưởng nào có thể tin tưởng. Mật mã dựa trên cách nhấn nhá âm điệu trong các cụm từ cổ ngữ tinh linh — thứ mà lính canh thế hệ mới không còn hiểu được.

Ngoài ra, có tin đồn rằng một số công nhân bỏ trốn thành công đã gia nhập hàng ngũ Hắc Tinh Linh Lưu Đày và đang bí mật liên lạc ngược về các trại, xây dựng cầu nối cho một cuộc thay đổi lớn hơn trong tương lai. Đặc biệt, có lời đồn về một tinh linh tên Mộc Ảnh — từng là công nhân trại phía nam — đã trốn thoát ba năm trước và hiện là người liên lạc giữa Hắc Tinh Linh và phong trào "Rễ Sâu," mang theo bản đồ các đường thoát bí mật ra ngoài rừng.
Những bí mật này, nếu được tiết lộ, có thể khiến nhiều thế lực phải nhìn lại đánh giá của mình về cộng đồng nhỏ bé này — vừa là cơ hội vừa là mối nguy.

## XI. Quan Hệ Thế Lực (势力关系)
Tinh Linh Vương Đình là thế lực duy nhất có quan hệ trực tiếp với công nhân — và đó là quan hệ chủ - nô, áp bức một chiều. Vương Đình coi công nhân như tài sản chứ không phải công dân, và mọi sản phẩm lao động đều bị chiếm đoạt. Bán Tinh Linh Hội — tổ chức của những tinh linh lai — chia sẻ cảnh ngộ bị kỳ thị, tạo ra sự đồng cảm ngầm dù hai bên chưa dám liên lạc công khai vì sợ bị Vương Đình phát hiện. Hắc Tinh Linh Lưu Đày tiếp nhận một số công nhân bỏ trốn, hình thành mối liên hệ ngầm mà Vương Đình chưa nắm rõ quy mô. Về bản chất, công nhân tinh linh là giai cấp bị cô lập có chủ đích — Vương Đình không muốn họ có bất kỳ mối quan hệ nào với bên ngoài.
Nhìn tổng thể, mạng lưới quan hệ tuy mỏng manh nhưng đủ duy trì sự tồn tại — trong thế giới tu chân tàn khốc, tồn tại đã là chiến thắng.
