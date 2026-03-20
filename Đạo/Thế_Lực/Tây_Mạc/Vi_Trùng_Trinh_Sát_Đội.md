---
type: faction
name: Vi Trùng Trinh Sát Đội
hantu: 微虫侦察队
faction_type: Hội
alignment: 0
race: Vi Trùng (Sinh vật cực nhỏ có linh trí)
region: Tây Mạc
founded: Xa xưa (không rõ chính xác)
founder: Thiên Mục thế hệ đầu tiên
emblem: Mat_Vi_Trung.png
specialty: Vạn Mục Quan Sát, Trinh sát toàn diện Mạch Ngầm, Thu thập tình báo tuyệt mật
economy:
- Không có hoạt động kinh tế — tồn tại hoàn toàn bí mật
arcs:
  - arc: 1
    status: Hoạt động bí mật, chưa từng bị phát hiện
    rank: Không Xếp Hạng
    leader: Đội Trưởng Thiên Mục (thế hệ thứ 7)
    population: 31
    territory:
      - Huyết Uyên và hệ thống Mạch Ngầm (không có trụ sở cố định)
    assets:
      - name: Bản đồ Mạch Ngầm hoàn chỉnh nhất
        type: Tài Nguyên
      - name: Ký ức tập thể 7 thế hệ
        type: Tài Nguyên
    stats: [5, 5, 5, 31, 5, 5]
    divisions:
      - name: Ban Trinh Sát
        role: Do thám các khu vực Mạch Ngầm và thu thập tình báo
        headcount:
          hoi_truong: 1
          pho_hoi_truong: 0
          thanh_vien: 30
          tong_quan: 0
        members:
          - character: Thiên Mục
            position: Đội Trưởng
            cultivation: Luyện Khí Đỉnh Phong (tương đương)
          - character: "[Trinh Sát Viên]"
            position: Trinh Sát
            cultivation: Luyện Khí Sơ-Trung Kỳ (tương đương)
            placeholder: true
      - name: Bầy Lũ Cảm Biến
        role: Phân tán khắp Mạch Ngầm làm "cảm biến" thu thập dữ liệu môi trường
        headcount:
          hoi_truong: 0
          pho_hoi_truong: 0
          thanh_vien: 0
          tong_quan: 0
        members:
          - character: "[Vi Trùng Cảm Biến]"
            position: Cảm Biến
            cultivation: Không có linh trí
            placeholder: true
    relationships:
      - faction: Địa Mạch Thám Hiểm Đội
        description: Đội Trinh Sát nắm giữ bản đồ Mạch Ngầm vượt xa Thám Hiểm Đội, nhưng Thám Hiểm Đội hoàn toàn không biết sự tồn tại của Vi Trùng.
        diplomacy:
          lien_minh: 0
          tin: 0
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 0
      - faction: San Hô Vi Trùng
        description: Cùng là vi trùng nhưng khác loài hoàn toàn. Vi Trùng Trinh Sát có linh trí, San Hô Vi Trùng hoạt động theo bản năng. Không có tương tác.
        diplomacy:
          lien_minh: 0
          tin: 0
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 0
      - faction: Mọi thế lực trong Mạch Ngầm
        description: Vi Trùng Trinh Sát Đội quan sát tất cả nhưng không bao giờ tiết lộ sự tồn tại. Chưa từng có sinh vật lớn nào phát hiện ra chúng.
        diplomacy:
          lien_minh: 0
          tin: 0
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 0
---

# Vi Trùng Trinh Sát Đội (微虫侦察队)

## I. Tổng Quan (总览)
Vi Trùng Trinh Sát Đội là một tổ chức trinh sát bí mật gồm ba mươi mốt vi trùng có linh trí, hoạt động trong Huyết Uyên và hệ thống Mạch Ngầm mà không bao giờ để lộ sự tồn tại cho bất kỳ sinh vật lớn nào. Dưới sự lãnh đạo của Đội Trưởng Thiên Mục, vi trùng trinh sát thế hệ thứ bảy với cơ thể bằng hạt bụi và hàng ngàn mắt đơn bao phủ khắp thân, đội nắm giữ lượng tình báo khổng lồ về mọi hoạt động trong Mạch Ngầm. Với phương châm "nhìn mà không bị nhìn, biết mà không bị biết", đội tồn tại như những bóng ma vô hình, chứng kiến mọi sự kiện lớn nhỏ mà không bao giờ can thiệp.

## II. Địa Lý & Tài Nguyên (地理与资源)
Vi Trùng Trinh Sát Đội hoạt động khắp Huyết Uyên và hệ thống Mạch Ngầm, di chuyển liên tục và không bao giờ ở một chỗ quá ba ngày. Chúng sử dụng mọi kẽ nứt, ống dẫn nước, lỗ thông gió trong hệ thống Mạch Ngầm làm đường di chuyển, kích thước siêu nhỏ cho phép đi qua những nơi mà tu sĩ hay sinh vật lớn không thể với tới. Tài nguyên duy nhất và quý giá nhất của đội là thông tin tình báo: bản đồ Mạch Ngầm hoàn chỉnh nhất tồn tại, dữ liệu về mọi thế lực hoạt động trong hệ thống ngầm, và khả năng xâm nhập mọi nơi mà không bị phát hiện. Mạng lưới trinh sát bao phủ toàn bộ hệ thống ngầm Nam Cương, một tài sản mà nếu bất kỳ thế lực lớn nào biết đến, chắc chắn sẽ truy tìm bằng mọi giá.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
Triết lý cốt lõi của đội là "Nhìn mà không bị nhìn, biết mà không bị biết", tồn tại bằng cách trở nên hoàn toàn vô hình trước mọi sinh vật khác. Quy tắc tối thượng: không bao giờ tiết lộ sự tồn tại cho sinh vật lớn, thông tin thu thập chỉ chia sẻ nội bộ trong đội, và nếu bị phát hiện phải giả chết hoặc bỏ chạy, tuyệt đối không chiến đấu. Phong tục đặc trưng là "đánh dấu mùi", mỗi khi phát hiện thông tin quan trọng, Thiên Mục tiết ra pheromone đặc biệt để phân loại mức độ nguy hiểm của thông tin, tạo thành hệ thống lưu trữ dữ liệu sinh học độc đáo. Đội hoạt động dựa trên nguyên tắc sinh tồn tuyệt đối: sống sót quan trọng hơn bất kỳ thông tin nào.

## IV. Cơ Cấu Tổ Chức (组织结构)
Đội Trưởng Thiên Mục đứng đầu tổ chức, là vi trùng trinh sát thế hệ thứ bảy, kích thước bằng hạt bụi nhưng sở hữu hàng ngàn mắt đơn bao phủ cơ thể cho khả năng quan sát toàn phương vị. Linh trí của Thiên Mục tương đương Luyện Khí Đỉnh Phong, vượt trội so với các vi trùng thông thường. Ba mươi trinh sát viên có linh trí ở mức Luyện Khí Sơ đến Trung Kỳ tương đương, mỗi con phụ trách giám sát một khu vực cụ thể trong Mạch Ngầm. Ngoài ra, hàng vạn vi trùng không có linh trí hoạt động theo tín hiệu pheromone của Thiên Mục, đóng vai trò "cảm biến" phân tán thu thập dữ liệu môi trường cơ bản.

## V. Công Pháp & Trận Pháp (功法与阵法)
Vi Trùng Trinh Sát Đội không có công pháp hay trận pháp, chiến lực bằng không. Năng lực đặc biệt duy nhất là "Vạn Mục Quan Sát", cho phép Thiên Mục nhìn qua mắt của bất kỳ vi trùng nào trong bầy lũ cảm biến, tạo thành mạng lưới giám sát khổng lồ bao phủ toàn bộ hệ thống Mạch Ngầm. Khả năng này không mang tính chiến đấu nhưng có giá trị tình báo vô song. Mỗi vi trùng trong bầy lũ hoạt động như một "mắt thần" độc lập, truyền hình ảnh về cho Thiên Mục qua tín hiệu linh lực cực nhỏ mà không sinh vật nào phát hiện được.

## VI. Đặc Sản Môn Phái (门派特产)
Sản phẩm duy nhất của Vi Trùng Trinh Sát Đội là thông tin tình báo, nhưng sản phẩm này chưa bao giờ được "bán" hay chia sẻ với bất kỳ ai bên ngoài. Bản đồ Mạch Ngầm mà Thiên Mục lưu giữ trong ký ức là bản đồ hoàn chỉnh nhất tồn tại trong Cố Nguyên Giới, vượt xa những gì Địa Mạch Thám Hiểm Đội có, bao gồm cả những khu vực mà không sinh vật lớn nào từng đặt chân đến. Ngoài ra, ký ức tập thể truyền qua bảy thế hệ chứa đựng lịch sử Mạch Ngầm từ hàng ngàn năm trước, một kho tàng kiến thức mà không ai biết đến.

## VII. Cơ Sở Hạ Tầng (基础设施)
Vi Trùng Trinh Sát Đội không có bất kỳ cơ sở hạ tầng nào. Chúng sống trong kẽ nứt đá, ống dẫn nước, và lỗ thông gió tự nhiên của Mạch Ngầm, di chuyển liên tục và không bao giờ thiết lập trụ sở cố định. Nơi nghỉ ngơi thay đổi mỗi ba ngày theo quy tắc an ninh nghiêm ngặt. Kích thước siêu nhỏ cho phép chúng sử dụng bất kỳ khe hở nào làm nơi ẩn náu tạm thời, biến toàn bộ hệ thống Mạch Ngầm thành "nhà" của đội.

## VIII. Kinh Tế (经济)
Vi Trùng Trinh Sát Đội không có bất kỳ hoạt động kinh tế nào. Chúng tồn tại bằng cách hấp thu linh khí vi lượng từ môi trường Mạch Ngầm và ăn vi khuẩn cùng các vi sinh vật nhỏ hơn. Không cần tiền bạc, không cần trao đổi, không cần tích trữ. Sự tự cung tự cấp hoàn toàn ở cấp độ vi sinh là yếu tố then chốt giúp đội duy trì bí mật tuyệt đối suốt nhiều thế hệ, bởi không có giao dịch nào để lại dấu vết.

## IX. Lịch Sử Tóm Tắt (简史)
Vi Trùng Trinh Sát Đội tồn tại từ xa xưa, không ai biết chính xác bao lâu vì chưa ai phát hiện ra sự tồn tại của chúng. Thiên Mục hiện tại là thế hệ thứ bảy, mỗi thế hệ truyền lại toàn bộ ký ức trinh sát cho thế hệ sau qua quá trình phân chia tế bào đặc biệt, đảm bảo kiến thức tích lũy không bao giờ bị mất. Suốt nhiều thế hệ, đội đã chứng kiến mọi sự kiện lớn trong Mạch Ngầm mà không bao giờ can thiệp: các cuộc chiến tranh giữa các thế lực ngầm, sự sụp đổ và trỗi dậy của các đế chế dưới lòng đất, và những bí mật mà không ai khác biết. Gần đây, Thiên Mục cảm nhận được rung chấn bất thường từ sâu dưới Mạch Ngầm, một hiện tượng chưa từng xảy ra trong ký ức bảy thế hệ, đang mạnh dần theo thời gian.

## X. Giai Thoại & Bí Mật (轶事与秘密)
Trong khu vực sâu nhất của Mạch Ngầm, nơi mà ngay cả Địa Mạch Thám Hiểm Đội cũng chưa từng đặt chân, Thiên Mục đã nhìn thấy một "cánh cửa đá" khổng lồ khắc đầy ký tự cổ đại. Mỗi lần vi trùng tiến đến gần, ký tự trên cửa phát sáng rực rỡ và tạo ra lực đẩy nhẹ nhàng nhưng kiên quyết, đẩy chúng ra xa. Thiên Mục đã ghi nhớ hình dạng của mọi ký tự trên cánh cửa nhưng không biết chia sẻ cho ai, bởi tiết lộ sự tồn tại đồng nghĩa với tự hủy diệt. Bản đồ Mạch Ngầm trong ký ức Thiên Mục bao gồm những đường hầm cổ đại mà không sinh vật lớn nào từng biết đến, một số đường hầm dẫn đến những không gian rỗng chứa đầy ký tự phát sáng giống hệt trên cánh cửa đá.

## XI. Quan Hệ Thế Lực (势力关系)
- **Địa Mạch Thám Hiểm Đội:** Đội Trinh Sát nắm giữ bản đồ Mạch Ngầm vượt xa Thám Hiểm Đội, nhưng hai bên chưa bao giờ tiếp xúc. Thám Hiểm Đội hoàn toàn không biết sự tồn tại của Vi Trùng.
- **San Hô Vi Trùng:** Cùng mang tên "vi trùng" nhưng khác loài hoàn toàn. Vi Trùng Trinh Sát có linh trí và mục đích rõ ràng, San Hô Vi Trùng hoạt động theo bản năng thuần túy.
- **Mọi thế lực trong Mạch Ngầm:** Vi Trùng Trinh Sát Đội quan sát tất cả mà không bao giờ bị quan sát lại, tồn tại như những bóng ma vô hình trong lòng đất.
