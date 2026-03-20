---
type: faction
name: Hoang Dã Thợ Săn Bang
hantu: 荒野猎人帮
faction_type: Hội
alignment: -3
race: Đa chủng tộc (chủ yếu Nhân Tộc, Bán Yêu)
region: Đông Hoang
founded: 40 năm trước
founder: Liệp Phong
emblem: Hoang_Da_Tho_San_Bang.png
specialty: Săn linh thú, Hộ tống, Thu thập dược thảo, Ám sát
economy:
- Hợp đồng thưởng kim săn linh thú
- Dịch vụ hộ tống thương đoàn
- Buôn bán linh vật và vật liệu từ linh thú
arcs:
  - arc: 1
    status: Hoạt động mạnh
    rank: Hạng Tư
    leader: Bang Chủ Liệp Phong
    population: 180
    territory:
      - Ngoại vi phía tây Vạn Yêu Thành
      - Vùng hoang dã giữa nhân tộc và yêu tộc
    assets:
      - name: Khu Chợ Đen Hậu Quán
        type: Công Trình
      - name: Mạng lưới hợp đồng thưởng kim
        type: Tài Nguyên
      - name: Kho vũ khí và bẫy thú
        type: Trang Bị
    stats: [400, 200, 300, 180, 150, 350]
    divisions:
      - name: Bát Đại Tiểu Đội
        role: Tám đội săn chuyên nghiệp, mỗi đội phụ trách một loại hợp đồng
        headcount:
          hoi_truong: 1
          pho_hoi_truong: 1
          thanh_vien: 168
          tong_quan: 10
        members:
          - character: Liệp Phong
            position: Bang Chủ
            cultivation: Kim Đan Sơ Kỳ
          - character: "[Phó Bang Chủ]"
            position: Phó Bang Chủ
            cultivation: Trúc Cơ Viên Mãn
            placeholder: true
          - character: "[Đội Trưởng Nhất]"
            position: Đội Trưởng
            cultivation: Trúc Cơ Hậu Kỳ
            placeholder: true
    relationships:
      - faction: Vạn Yêu Thành
        description: Bang hoạt động ở ngoại vi thành, được thành ngầm cho phép tồn tại miễn không vi phạm luật thành. Một số thợ săn bí mật làm gián điệp cho thành.
        diplomacy:
          lien_minh: 10
          tin: -20
          uy_hiep: 30
          thuong_mai: 40
          on_oan: 0
          le_thuoc: 30
      - faction: Hoang Dã Yêu Liên
        description: Mối quan hệ phức tạp — thợ săn bang đôi khi nhận hợp đồng săn yêu tộc cấp thấp, nhưng cũng từng hợp tác khi có kẻ thù chung.
        diplomacy:
          lien_minh: -10
          tin: -30
          uy_hiep: 40
          thuong_mai: 10
          on_oan: -20
          le_thuoc: 0
      - faction: Thanh Vân Nghĩa Đoàn
        description: Đôi khi nhận hợp đồng từ nghĩa đoàn, quan hệ thuần túy thương mại, không bên nào tin tưởng bên nào.
        diplomacy:
          lien_minh: 0
          tin: -10
          uy_hiep: 10
          thuong_mai: 40
          on_oan: 0
          le_thuoc: 0
---

# Hoang Dã Thợ Săn Bang (荒野猎人帮)

## I. Tổng Quan (总览)
Hoang Dã Thợ Săn Bang là tổ chức thợ săn đánh thuê lớn nhất hoạt động ở ngoại vi Vạn Yêu Thành, chuyên nhận mọi loại hợp đồng từ săn linh thú, hộ tống thương đoàn, thu thập dược thảo cho đến cả ám sát. Dưới sự lãnh đạo của Bang Chủ Liệp Phong — một cường giả Kim Đan Sơ Kỳ nổi tiếng vì sống sót qua vùng lãnh thổ yêu thú cấp cao — bang duy trì gần hai trăm thợ săn thiện chiến, sống nhờ vùng xám giữa nhân tộc và yêu tộc. Triết lý "Tiền đến tay, việc phải xong" khiến bang vừa được kính nể vì sự chuyên nghiệp, vừa bị nghi kỵ vì không phân biệt chính tà khi nhận hợp đồng.

## II. Địa Lý & Tài Nguyên (地理与资源)
Trụ sở chính nằm ở ngoại vi phía tây Vạn Yêu Thành, ẩn trong một khu chợ đen phía sau dãy quán rượu. Khu vực này lộn xộn và hỗn tạp, quán rượu và lều trại xen kẽ, đường đi ngoằn ngoèo khiến người lạ dễ lạc. Đây chính là vùng xám nơi lãnh thổ nhân tộc và yêu tộc giao nhau, luật pháp của cả hai bên đều không hoàn toàn hiệu lực. Tài nguyên chính của bang không phải đất đai hay mỏ khoáng mà là mạng lưới hợp đồng thưởng kim từ các thế lực lớn nhỏ, cùng linh vật và vật liệu thu được từ nhiệm vụ. Khu Chợ Đen Hậu Quán phía sau trụ sở là nơi giao dịch ngầm, mua bán linh vật không rõ nguồn gốc và nhận hợp đồng mật.
Khu vực xung quanh ẩn chứa nhiều bí mật chưa được khám phá — hang động chưa ai đến, mạch khoáng chưa ai biết, dấu tích cổ đại mà thời gian chưa kịp xóa nhòa.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
Văn hóa bang đề cao chủ nghĩa chuyên nghiệp tuyệt đối. "Tiền đến tay, việc phải xong" không chỉ là khẩu hiệu mà là luật sinh tồn: nhận hợp đồng thì phải hoàn thành hoặc chết, phản bội đồng đội khi đang làm nhiệm vụ sẽ bị toàn bang truy sát không khoan nhượng. Thợ săn mới phải hoàn thành mười hợp đồng cấp thấp trước khi được nhận nhiệm vụ lớn hơn — đây vừa là bài kiểm tra năng lực, vừa là cách xây dựng lòng trung thành. Bang không quan tâm đến chủng tộc hay xuất thân của thành viên, chỉ cần có kỹ năng và giữ lời. Buổi tối, thợ săn tụ tập tại quán rượu kể chuyện săn bắn, uống đến say mèm — đó là cách duy nhất họ xả bỏ áp lực sau những nhiệm vụ nguy hiểm.
Mỗi thế hệ mới được truyền dạy không chỉ kỹ năng sinh tồn mà cả câu chuyện về nguồn cội, để ngọn lửa ký ức không bao giờ tắt dù hoàn cảnh khắc nghiệt đến đâu.

## IV. Cơ Cấu Tổ Chức (组织结构)
Đứng đầu bang là Liệp Phong, cựu thợ săn linh thú đã leo lên cảnh giới Kim Đan nhờ thực chiến liên tục trong vùng hoang dã. Dưới hắn là một Phó Bang Chủ Trúc Cơ Viên Mãn phụ trách hậu cần và phân phối hợp đồng. Lực lượng chính chia thành Bát Đại Tiểu Đội, mỗi đội do một Đội Trưởng cảnh giới Trúc Cơ dẫn dắt, quản lý từ năm đến hai mươi thợ săn. Các tiểu đội chuyên môn hóa theo loại nhiệm vụ: săn linh thú, hộ tống, thu thập, trinh sát, và ám sát. Ngoài ra có khoảng mười nhân viên hậu cần phụ trách kho vũ khí, quản lý hợp đồng, và liên lạc với khách hàng. Tổng cộng gần hai trăm thành viên, đa số cảnh giới Trúc Cơ, một số Luyện Khí có kỹ năng đặc biệt.

## V. Công Pháp & Trận Pháp (功法与阵法)
Bang không có công pháp thống nhất, mỗi thợ săn tự tu theo sở trường và xuất thân riêng. Sự đa dạng này vừa là điểm yếu vì thiếu sự phối hợp chiến đấu, vừa là điểm mạnh vì kẻ thù không thể dự đoán chiến thuật. Khi săn linh thú, các tiểu đội sử dụng bẫy trận đơn giản nhưng hiệu quả: bẫy nổ, bẫy lưới linh lực, và hố chông linh, kết hợp với chiến thuật vây hãm nhiều hướng. Liệp Phong sở hữu một bộ "Liệp Phong Đao Pháp" do hắn tự sáng tạo qua bốn mươi năm thực chiến — đao pháp mạnh mẽ, chú trọng một kích trí mạng, phù hợp cho việc hạ gục mục tiêu nhanh nhất có thể.

## VI. Đặc Sản Môn Phái (门派特产)
- **Bẫy Linh Thú Chuyên Nghiệp:** Các loại bẫy được thợ săn cải tiến qua nhiều thế hệ, từ bẫy nổ đến bẫy lưới linh lực, hiệu quả cao đối với linh thú cấp Luyện Khí đến Trúc Cơ.
- **Dầu Che Mùi Hoang Dã:** Hỗn hợp dầu thảo mộc do bang tự chế, bôi lên người giúp che giấu khí tức và mùi hương trước linh thú, tăng tỷ lệ tiếp cận mục tiêu thành công.
- **Bản Đồ Vùng Xám:** Các bản ghi chép chi tiết về địa hình, lãnh thổ linh thú, và đường đi an toàn trong vùng hoang dã giữa nhân tộc và yêu tộc, chỉ cung cấp cho thành viên bang.
Ngoài ra, Hoang Dã Thợ Săn Bang còn sở hữu vật phẩm có giá trị văn hóa hơn vật chất — thứ mà thương nhân bỏ qua nhưng nhà sử học trả bất cứ giá nào.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Khu Chợ Đen Hậu Quán:** Khu vực giao dịch ngầm phía sau dãy quán rượu, nơi nhận hợp đồng, mua bán linh vật và trao đổi thông tin tình báo.
- **Kho Vũ Khí và Bẫy:** Hầm ngầm dưới trụ sở chứa vũ khí, bẫy thú, và trang bị chiến đấu dự phòng cho toàn bang.
- **Quán Rượu Liệp Phong:** Quán rượu do bang điều hành, vừa là nơi nghỉ ngơi của thợ săn, vừa là mặt tiền che đậy cho hoạt động chợ đen phía sau.
Toàn bộ hạ tầng mang dấu ấn đặc trưng cộng đồng — không phải xa hoa mà là thực dụng đúc kết qua nhiều thế hệ thử nghiệm.

## VIII. Kinh Tế (经济)
Kinh tế bang dựa hoàn toàn vào hợp đồng thưởng kim. Mỗi hợp đồng hoàn thành, bang giữ ba mươi phần trăm, bảy mươi phần trăm thuộc về tiểu đội thực hiện. Nguồn thu đa dạng từ săn linh thú, hộ tống thương đoàn, thu thập dược thảo, đến các nhiệm vụ "đặc biệt" không nêu tên. Ngoài ra, quán rượu và chợ đen cũng mang lại thu nhập ổn định. Bang sống nhờ vị trí vùng xám — cả nhân tộc lẫn yêu tộc đều cần dịch vụ của thợ săn nhưng không bên nào chính thức thừa nhận quan hệ, điều này cho phép bang hoạt động tự do nhưng cũng thiếu sự bảo hộ.
Tiềm năng kinh tế vượt xa những gì đang được khai thác — sự thiếu hụt nhân lực, kiến thức thương mại, và bảo hộ chính trị khiến phần lớn giá trị vẫn nằm yên.

## IX. Lịch Sử Tóm Tắt (简史)
Bốn mươi năm trước, Liệp Phong chỉ là một thợ săn linh thú lang thang tụ tập cùng vài người có chung nghề nghiệp ở ngoại vi Vạn Yêu Thành. Nhóm nhỏ ban đầu chuyên săn linh thú kiếm sống, dần dần nhận thêm các loại hợp đồng khác khi danh tiếng lan rộng: hộ tống, thu thập dược thảo, và đôi khi cả ám sát. Khi Liệp Phong đột phá Kim Đan hai mươi năm trước, bang chính thức có đủ uy lực để được các thế lực lớn chú ý và tin dùng. Hiện tại, bang là tổ chức đánh thuê lớn nhất vùng ngoại vi, với gần hai trăm thành viên và mạng lưới hợp đồng trải khắp Đông Hoang. Tuy nhiên, vị trí vùng xám cũng khiến bang thường xuyên bị kẹt giữa các xung đột chính trị lớn hơn.
Mỗi thế hệ kế tiếp gánh di sản và gánh nặng thế hệ trước — nhưng cũng mang khả năng mới mà cha ông chưa từng tưởng tượng.

## X. Giai Thoại & Bí Mật (轶事与秘密)
Liệp Phong từng nhận một hợp đồng bí mật từ một thế lực cực lớn mà hắn không dám tiết lộ danh tính ngay cả với phó bang chủ. Nhiệm vụ đó đã âm thầm thay đổi cục diện quyền lực ở Đông Hoang nhưng không một ai biết Hoang Dã Thợ Săn Bang có liên quan. Liệp Phong giữ bí mật này như gánh nặng, vì hắn biết nếu sự thật lộ ra, bang sẽ bị nhiều thế lực truy sát cùng lúc. Một bí mật khác đáng lo ngại hơn: ít nhất năm thợ săn trong bang thực ra là gián điệp được cài cắm bởi Vạn Yêu Thành và các tông phái lớn, Liệp Phong biết điều này nhưng chọn cách giữ im lặng, vì trục xuất gián điệp sẽ gây chiến tranh mà bang không đủ sức chống chọi.
Những bí mật này, nếu được tiết lộ, có thể khiến nhiều thế lực phải nhìn lại đánh giá của mình về cộng đồng nhỏ bé này — vừa là cơ hội vừa là mối nguy.

## XI. Quan Hệ Thế Lực (势力关系)
- **Vạn Yêu Thành:** Bang hoạt động ở ngoại vi thành, được ngầm cho phép tồn tại miễn không vi phạm luật thành. Quan hệ phức tạp giữa phụ thuộc và lợi dụng lẫn nhau.
- **Hoang Dã Yêu Liên:** Mối quan hệ mâu thuẫn — thợ săn bang đôi khi nhận hợp đồng săn yêu tộc cấp thấp thuộc liên minh, nhưng cũng từng hợp tác khi có kẻ thù chung mạnh hơn.
- **Thanh Vân Nghĩa Đoàn:** Quan hệ thuần túy thương mại, bang nhận hợp đồng từ nghĩa đoàn khi nhiệm vụ phù hợp, không tin tưởng lẫn nhau nhưng tôn trọng sự chuyên nghiệp.
Nhìn tổng thể, mạng lưới quan hệ tuy mỏng manh nhưng đủ duy trì sự tồn tại — trong thế giới tu chân tàn khốc, tồn tại đã là chiến thắng.
