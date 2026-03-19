---
type: faction
name: Triều Tịch Quan Trắc Đài
hantu: 潮汐观测台
faction_type: Hội
alignment: 5
race: Nhân Tộc
region: Đông Hoang
founded: 35 năm trước
founder: Tô Vọng Nguyệt
emblem: Trieu_Tich_Quan_Trac_Dai.png
specialty: Quan trắc hải dương, Dự báo phong ba, Lập bản đồ hải lưu
economy:
- Bán bản đồ hải lưu cho thương thuyền
- Nhận phí dự báo thời tiết biển
arcs:
  - arc: 1
    status: Hoạt động thầm lặng
    rank: Không Xếp Hạng
    leader: Đài Trưởng Tô Vọng Nguyệt
    population: 11
    territory:
      - Tháp đá trên đảo đá giữa Vô Tận Hải
    assets:
      - name: Tháp Quan Trắc
        type: Công Trình
      - name: Kho dữ liệu hải dương (6000+ cuốn sổ)
        type: Tài Nguyên
      - name: Phong Ba Dự Báo Trận
        type: Trận Pháp
    stats: [5, 10, 20, 11, 15, 30]
    divisions:
      - name: Toàn Đài
        role: Quan trắc hải dương, ghi chép dữ liệu và dự báo phong ba
        headcount:
          hoi_truong: 1
          pho_hoi_truong: 0
          thanh_vien: 7
          tong_quan: 3
        members:
          - character: "[Tô Vọng Nguyệt]"
            position: Đài Trưởng
            cultivation: Trúc Cơ Viên Mãn
            placeholder: true
    relationships:
      - faction: Thương Hội Bạch Lang
        description: Khách hàng mua bản đồ hải lưu. Thương đoàn đường biển thường xuyên cần thông tin thời tiết trước mỗi chuyến đi.
        diplomacy:
          lien_minh: 10
          tin: 30
          uy_hiep: 0
          thuong_mai: 50
          on_oan: 0
          le_thuoc: 0
      - faction: Lưu Vong Thuyền Đội
        description: Khách hàng thân thiết nhất. Thuyền Đội thường mua bản đồ hải lưu trước mỗi chuyến hộ tống và đôi khi cung cấp vật tư cho Đài.
        diplomacy:
          lien_minh: 20
          tin: 40
          uy_hiep: 0
          thuong_mai: 60
          on_oan: 10
          le_thuoc: 0
      - faction: Tiểu Ngư Nhân Thôn
        description: Đối tượng nghiên cứu bị động. Quan trắc viên đôi khi quan sát Ngư Nhân từ xa để hiểu thêm về hệ sinh thái hải dương.
        diplomacy:
          lien_minh: 0
          tin: 0
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 0
---

# Triều Tịch Quan Trắc Đài (潮汐观测台)

## I. Tổng Quan (总览)

Triều Tịch Quan Trắc Đài là một tổ chức nghiên cứu thiên văn hải dương nhỏ bé nhưng sở hữu kho dữ liệu quý giá nhất về biển cả trong toàn bộ Đông Hoang. Tọa lạc trên một cột đá cô độc giữa vùng Vô Tận Hải, Đài được thành lập và dẫn dắt bởi Tô Vọng Nguyệt — một cựu đệ tử Thiên Môn Kính Đài bị đồng môn coi là "lãng phí tài năng vào nghiên cứu vô dụng". Với chỉ 11 thành viên sống trong điều kiện khắc nghiệt giữa gió biển và bão tố, Đài lặng lẽ tích lũy hơn sáu nghìn cuốn sổ quan trắc — kho dữ liệu hải dương lớn nhất mà không thế lực lớn nào hay biết.

## II. Địa Lý & Tài Nguyên (地理与资源)

Đài tọa lạc trên một cột đá tự nhiên cao chót vót giữa vùng biển sâu Vô Tận Hải, xung quanh là dòng nước xoáy nguy hiểm khiến tàu thuyền không thể tiếp cận dễ dàng. Cột đá này là phần nhô lên duy nhất của một dãy núi ngầm dưới đáy biển, vị trí đắc địa cho phép quan sát toàn cảnh hải lưu, sóng thần và di chuyển của hải thú lớn trong bán kính rộng. Tuy nhiên, địa điểm này hoàn toàn không có tài nguyên thiên nhiên — mọi vật tư, lương thực và linh thạch đều phải vận chuyển từ đất liền bằng phi thuyền nhỏ hoặc thuyền buồm, khiến chi phí sinh hoạt cực kỳ cao. Cột đá thường xuyên bị sóng biển đánh xói mòn, mỗi năm phải gia cố bằng linh thạch ít ỏi để tránh sụp đổ.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)

Thành viên Triều Tịch Quan Trắc Đài đều là những người đam mê nghiên cứu thiên văn hải dương đến mức cuồng nhiệt, hoàn toàn không quan tâm đến tranh đấu quyền lực hay danh vọng tu luyện. Họ tin rằng thủy triều chứa đựng quy luật của Thiên Đạo — rằng sự lên xuống của nước biển phản ánh nhịp thở của chính vũ trụ, và nếu giải mã được quy luật này, sẽ hiểu được bí mật cốt lõi của tạo hóa. Đời sống thanh đạm đến khổ hạnh: ăn uống đơn giản, ngủ ít, suốt ngày đêm ghi chép số liệu, quan sát sóng biển và vẽ bản đồ hải lưu. Tô Vọng Nguyệt thường nói: "Vạn vật lên xuống theo triều, hiểu triều tức hiểu Đạo."

## IV. Cơ Cấu Tổ Chức (组织结构)

Cơ cấu tổ chức tối giản, phẳng và gần như không có hệ thống thứ bậc chính thức.

- **Đài Trưởng — Tô Vọng Nguyệt:** Nhà nghiên cứu cô độc, cựu đệ tử Thiên Môn Kính Đài, tu vi Trúc Cơ Viên Mãn. Là người sáng lập, nguồn tài trợ chính và bộ não của toàn bộ hoạt động nghiên cứu.
- **Quan Trắc Viên (7 người):** Tu vi từ Luyện Khí đến Trúc Cơ Sơ Kỳ. Phụ trách quan sát hải lưu, đo đạc sóng triều, theo dõi di chuyển của hải thú và ghi chép hiện tượng thời tiết bất thường theo ca trực luân phiên.
- **Ghi Chép Viên (3 người):** Phàm nhân không có tu vi, chuyên sao chép, phân loại và bảo quản tài liệu. Họ ở đây vì tình yêu tri thức và vì Tô Vọng Nguyệt trả lương đủ sống.

Điều kiện sống khắc nghiệt — gió biển mặn quanh năm, mùa bão phải chui vào hầm đá trú ẩn suốt nhiều ngày. Nhiều quan trắc viên chỉ trụ được vài năm trước khi xin rời đi.

## V. Công Pháp & Trận Pháp (功法与阵法)

Đài không có công pháp chiến đấu. Tô Vọng Nguyệt chỉ thông thạo một kỹ thuật duy nhất: Thủy Cảm Thuật — khả năng cảm nhận mọi biến động trong nước biển trong phạm vi rộng, từ sự thay đổi nhiệt độ vi mô đến chuyển động của hải thú sâu dưới đáy biển. Đây không phải chiến đấu thuật mà là công cụ nghiên cứu, nhưng trong tay Tô Vọng Nguyệt, nó đã được tinh luyện đến mức có thể phát hiện sóng thần trước hai ngày.

Trận pháp duy nhất là Phong Ba Dự Báo Trận — một trận pháp cảm ứng được Tô Vọng Nguyệt tự phát triển, sử dụng các trụ linh thạch cắm trên cột đá để thu thập thông tin về áp suất không khí và dòng hải lưu. Trận pháp này không có tác dụng phòng thủ hay tấn công, nhưng có thể dự đoán chính xác bão biển trước ba ngày — thông tin vô giá đối với bất kỳ ai hoạt động trên biển.

## VI. Đặc Sản Môn Phái (门派特产)

- **Bản Đồ Hải Lưu Triều Tịch:** Sản phẩm thương mại duy nhất và cũng là nguồn thu nhập chính. Được cập nhật mỗi mùa, bản đồ ghi chép chi tiết các dòng hải lưu, khu vực nước xoáy, mùa di cư của hải thú và tuyến đường an toàn cho tàu thuyền. Nhiều thương thuyền và hộ vệ đội biển sẵn sàng trả giá cao để có được.
- **Lịch Triều Tịch:** Bảng dự báo thủy triều chính xác trong 12 tháng tới, tính toán dựa trên hàng chục năm dữ liệu quan trắc. Hữu ích cho ngư dân, thương thuyền và bất kỳ ai hoạt động ven biển.
- **Sổ Quan Trắc Gốc:** Hơn 6000 cuốn sổ ghi chép thủ công của Tô Vọng Nguyệt và các quan trắc viên. Tuy chưa ai nhận ra, nhưng đây có thể là kho dữ liệu hải dương có giá trị nhất Cố Nguyên Giới.

## VII. Cơ Sở Hạ Tầng (基础设施)

- **Tháp Quan Trắc:** Tháp đá ba tầng xây trên đỉnh cột đá, tầng trên cùng là đài quan sát lộ thiên trang bị Thiên Nhãn Kính (pháp khí phóng đại tầm nhìn), tầng giữa là phòng nghiên cứu và thư phòng, tầng dưới là khu sinh hoạt và kho chứa.
- **Hầm Đá Trú Ẩn:** Phòng ngầm đào sâu trong lòng cột đá, dùng làm nơi trú bão. Đủ chỗ cho toàn bộ 11 thành viên cùng lương thực dự trữ cho một tháng.
- **Bến Đỗ Nhỏ:** Một mỏm đá phẳng ở chân cột đá, nơi thuyền tiếp tế cập bến. Chỉ sử dụng được khi biển lặng, mùa bão hoàn toàn bị cô lập.

## VIII. Kinh Tế (经济)

Kinh tế Triều Tịch Quan Trắc Đài cực kỳ eo hẹp và phụ thuộc gần như hoàn toàn vào việc bán bản đồ hải lưu. Khách hàng chính là các thương thuyền và hộ vệ đội biển — đặc biệt là Lưu Vong Thuyền Đội, khách hàng thân thiết nhất, thường mua bản đồ trước mỗi chuyến hộ tống. Thu nhập từ bản đồ chỉ vừa đủ trang trải chi phí vận chuyển vật tư từ đất liền, trả lương cho Ghi Chép Viên và mua linh thạch gia cố cột đá. Tô Vọng Nguyệt thường phải bù đắp thâm hụt bằng tiết kiệm cá nhân từ thời còn ở Thiên Môn Kính Đài. Nghịch lý là Đài sở hữu kho dữ liệu có giá trị tiềm tàng khổng lồ, nhưng vì không ai biết đến sự tồn tại của nó, nên giá trị thương mại thực tế gần như bằng không.

## IX. Lịch Sử Tóm Tắt (简史)

Tô Vọng Nguyệt vốn là đệ tử tài năng của Thiên Môn Kính Đài, nhưng niềm đam mê nghiên cứu hải dương khiến ông bị đồng môn chê cười là "lãng phí tài năng vào nghiên cứu vô dụng". Ba mươi lăm năm trước, sau một cuộc tranh luận gay gắt với Sư Tổ về giá trị của nghiên cứu thuần túy, Tô Vọng Nguyệt quyết định rời tông môn. Một mình ông tìm đến cột đá giữa Vô Tận Hải — vị trí lý tưởng nhất để quan sát hải lưu — và bắt đầu xây tháp quan trắc bằng tay không. Dần dần, một số người có cùng đam mê tìm đến gia nhập, hình thành nên Triều Tịch Quan Trắc Đài như hiện tại. Suốt 35 năm, Tô Vọng Nguyệt kiên trì ghi chép mỗi ngày không ngừng nghỉ, tích lũy hơn 6000 cuốn sổ quan trắc — kho dữ liệu mà nếu được khai thác đúng cách, có thể thay đổi hiểu biết của cả Cố Nguyên Giới về biển cả.

## X. Giai Thoại & Bí Mật (轶事与秘密)

- Tô Vọng Nguyệt đã phát hiện rằng chu kỳ di chuyển của Hải Thần Cung trùng khớp hoàn hảo với một quy luật cổ đại ghi trong kinh điển thượng cổ — nhưng ông chưa dám công bố vì sợ thu hút sự chú ý của các thế lực lớn và đặt Đài vào nguy hiểm.
- Đài từng ghi nhận một cơn sóng dị thường đến từ vùng biển sâu nhất của Vô Tận Hải — nơi không có sinh vật nào được biết là sống sót trở về. Sóng đó mang theo tần số mà Tô Vọng Nguyệt chưa bao giờ thấy trong 35 năm quan trắc, như thể có thứ gì đó khổng lồ đang thức giấc dưới đáy đại dương.
- Kho 6000 cuốn sổ quan trắc ẩn chứa một phát hiện mà ngay cả Tô Vọng Nguyệt cũng chưa nhận ra: nếu xâu chuỗi lại, dữ liệu cho thấy thủy triều đang dần thay đổi theo một quy luật chưa từng có trong lịch sử — dấu hiệu rằng điều gì đó đang xảy ra ở quy mô toàn cầu.

## XI. Quan Hệ Thế Lực (势力关系)

- **Lưu Vong Thuyền Đội:** Khách hàng thân thiết nhất và cũng là đường dây tiếp tế chính cho Đài. Thuyền Đội thường mua bản đồ hải lưu trước mỗi chuyến hộ tống và đôi khi mang theo vật tư cho Tô Vọng Nguyệt như một cử chỉ thiện chí.
- **Thương Hội Bạch Lang:** Khách hàng mua bản đồ thường xuyên cho các thương đoàn đường biển. Quan hệ thuần túy thương mại nhưng ổn định.
- **Tiểu Ngư Nhân Thôn:** Đối tượng nghiên cứu bị động. Quan trắc viên đôi khi quan sát Ngư Nhân từ xa như một phần nghiên cứu hệ sinh thái hải dương. Ngư Nhân hoàn toàn không biết đến sự tồn tại của Đài.
