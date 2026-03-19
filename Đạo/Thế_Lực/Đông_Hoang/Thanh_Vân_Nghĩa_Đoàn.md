---
type: faction
name: Thanh Vân Nghĩa Đoàn
hantu: 青云义团
faction_type: Hội
alignment: 9
race: Nhân Tộc
region: Đông Hoang
founded: 25 năm trước
founder: Vân Thiết Trụ
emblem: Thanh_Van_Nghia_Doan.png
specialty: Bảo vệ phàm nhân, Tuần tra ngoại vi, Diệt trừ yêu thú cấp thấp
economy:
  - Tự trồng dược thảo cấp thấp
  - Quyên góp lương thực từ dân làng
  - Nhận thưởng săn yêu thú (không thường xuyên)
arcs:
  - arc: 1
    status: Hoạt động (Nghèo khó)
    rank: Hạng Năm
    leader: Đoàn Trưởng Vân Thiết Trụ
    population: 60
    territory:
      - Các làng phàm nhân quanh ngoại vi Cửu Hoa Kiếm Tông
      - Vùng đồng bằng và đồi thấp phía nam Cửu Hoa Sơn
    assets:
      - name: Trận Pháp Phòng Thủ Làng
        type: Trận Pháp (đơn giản)
      - name: Vườn Dược Thảo Cấp Thấp
        type: Tài Nguyên
    stats: [40, 15, 30, 60, 25, 20]
    divisions:
      - name: Nghĩa Quân
        role: Tuần tra bảo vệ các làng phàm nhân khỏi yêu thú và tán tu
        headcount:
          hoi_truong: 1
          pho_hoi_truong: 2
          thanh_vien: 50
          tong_quan: 7
        members:
          - character: Vân Thiết Trụ
            position: Đoàn Trưởng
            cultivation: Trúc Cơ Viên Mãn
          - character: "[Phó Đoàn Trưởng Nhất]"
            position: Phó Đoàn Trưởng
            cultivation: Trúc Cơ Trung Kỳ
            placeholder: true
          - character: "[Phó Đoàn Trưởng Nhị]"
            position: Phó Đoàn Trưởng
            cultivation: Trúc Cơ Trung Kỳ
            placeholder: true
    relationships:
      - faction: Cửu Hoa Kiếm Tông
        description: Cửu Hoa biết Nghĩa Đoàn tồn tại nhưng coi như không thấy — vừa không cần diệt, vừa ngại mang tiếng bỏ mặc phàm nhân.
        diplomacy:
          lien_minh: 5
          tin: 10
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 10
          le_thuoc: 30
      - faction: Hoang Dã Thợ Săn Bang
        description: Đôi khi hợp tác diệt trừ yêu thú cấp thấp gần các làng, chia sẻ thông tin về tình hình yêu thú.
        diplomacy:
          lien_minh: 20
          tin: 30
          uy_hiep: 0
          thuong_mai: 10
          on_oan: 5
          le_thuoc: 0
      - faction: Thiên Yêu Đình
        description: Không có quan hệ trực tiếp, nhưng yêu thú cấp thấp từ lãnh thổ Thiên Yêu Đình đôi khi tràn ra tấn công các làng phàm nhân.
        diplomacy:
          lien_minh: -10
          tin: -5
          uy_hiep: 20
          thuong_mai: 0
          on_oan: -15
          le_thuoc: 0
---

# Thanh Vân Nghĩa Đoàn (青云义团)

## I. Tổng Quan (总览)

Thanh Vân Nghĩa Đoàn là một tổ chức nghĩa quân nhỏ gồm khoảng 60 tu sĩ, hoạt động miễn phí để bảo vệ các làng phàm nhân nằm ở vùng ngoại vi Cửu Hoa Kiếm Tông. Do Vân Thiết Trụ — con nhà phàm nhân tự tu luyện đến Trúc Cơ Viên Mãn — thành lập cách đây 25 năm, Nghĩa Đoàn mang trong mình lý tưởng cao cả: tu sĩ mạnh phải bảo vệ kẻ yếu. Tuy nhiên, lý tưởng không đổi được thực tại nghèo khó — Nghĩa Đoàn luôn thiếu tài nguyên trầm trọng, vũ khí phần lớn là hàng thường, thành viên đa số chỉ ở cấp Luyện Khí. Họ tồn tại không nhờ sức mạnh mà nhờ lòng biết ơn của dân làng và ý chí kiên cường của người sáng lập.

## II. Địa Lý & Tài Nguyên (地理与资源)

Nghĩa Đoàn hoạt động rải rác quanh vùng ngoại vi Cửu Hoa Kiếm Tông, chủ yếu ở các làng phàm nhân trên đồng bằng và đồi thấp phía nam Cửu Hoa Sơn. Đây là vùng canh tác nông nghiệp của phàm nhân, địa hình trống trải, không có mạch linh khí mạnh nên không được tông phái nào quan tâm. Tài nguyên cực kỳ hạn hẹp — vũ khí thường lấy từ lò rèn phàm nhân, dược thảo cấp thấp tự trồng trong vườn nhỏ, và lương thực chủ yếu do dân làng quyên góp để trả ơn. Đây là vùng đất mà thế giới tu luyện coi là "vùng trống" — quá yếu để khai thác, quá xa để bảo vệ.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)

Triết lý cốt lõi là "Tu sĩ mạnh bảo vệ kẻ yếu, đó mới là đạo." Vân Thiết Trụ tin rằng mục đích cuối cùng của tu luyện không phải trường sinh bất lão mà là sức mạnh để bảo vệ những người không thể tự bảo vệ. Quy tắc nghiêm ngặt bao gồm: không nhận tiền bảo vệ phàm nhân, không lạm dụng tu vi để ức hiếp người thường, và không được coi thường phàm nhân. Mỗi thành viên mới phải trải qua "Lễ Nhập Đoàn" — sống một tháng trong làng phàm nhân, làm việc đồng áng như người thường để hiểu cuộc sống khó khăn của những người mà họ sẽ bảo vệ.

## IV. Cơ Cấu Tổ Chức (组织结构)

Đoàn Trưởng Vân Thiết Trụ là linh hồn và trụ cột của Nghĩa Đoàn, kiêm luôn vai trò chiến đấu chính vì tu vi cao nhất. Bên dưới có 2 Phó Đoàn Trưởng (Trúc Cơ Trung Kỳ) phụ trách điều phối nhân lực và huấn luyện. 50 thành viên chính đa số ở cấp Luyện Khí với vài Trúc Cơ Sơ Kỳ, được chia thành các tổ nhỏ phụ trách từng cụm làng. 7 tổng quản là những phàm nhân có kinh nghiệm, đóng vai trò liên lạc giữa Nghĩa Đoàn và dân làng. Cơ cấu đơn giản, linh hoạt, không có hệ thống thứ bậc cứng nhắc.

## V. Công Pháp & Trận Pháp (功法与阵法)

Nghĩa Đoàn không có công pháp riêng — mỗi thành viên tu theo sở học cá nhân, phần lớn là công pháp tạp loại cấp thấp mua được hoặc học lỏm. Vân Thiết Trụ tự mình kết hợp nhiều công pháp tạp loại thành một bộ chiến kỹ thực dụng, thiên về bền bỉ hơn bùng nổ. Về trận pháp, Đoàn bố trí vài trận pháp phòng thủ đơn giản quanh các làng trọng điểm — phần lớn là trận cảnh giới sơ đẳng để phát hiện yêu thú tiếp cận, không đủ mạnh để ngăn chặn tu sĩ có tu vi. Hiệu quả giới hạn nhưng đủ để cảnh báo sớm.

## VI. Đặc Sản Môn Phái (门派特产)

Nghĩa Đoàn không có đặc sản gì nổi bật. Sản phẩm duy nhất đáng kể là "Dược Thảo Làng" — dược liệu cấp thấp trồng trong vườn của Đoàn, chủ yếu phục vụ chữa trị vết thương và bệnh tật cho dân làng. Ngoài ra, qua 25 năm hoạt động, Nghĩa Đoàn tích lũy được kiến thức thực tiễn về hành vi yêu thú cấp thấp và cách đối phó — kinh nghiệm chiến trường thực tế mà nhiều đệ tử tông phái lớn thiếu.

## VII. Cơ Sở Hạ Tầng (基础设施)

Trụ sở chính chỉ là một nông trại cũ được cải tạo thành doanh trại đơn giản, nằm giữa ba làng lớn nhất. Có phòng họp, kho vũ khí (chủ yếu dao kiếm thường), vườn dược thảo nhỏ và khu huấn luyện ngoài trời. Các trạm tiền tiêu rải rác ở mỗi làng là những túp lều đơn sơ, dùng làm nơi trú ngụ cho tổ tuần tra. Không có trận pháp bảo vệ trụ sở chính — Nghĩa Đoàn tin rằng cần dồn toàn bộ nguồn lực ít ỏi để bảo vệ dân làng chứ không phải bảo vệ mình.

## VIII. Kinh Tế (经济)

Kinh tế của Nghĩa Đoàn luôn trong trạng thái thiếu hụt nghiêm trọng vì hoạt động miễn phí. Thu nhập chính đến từ ba nguồn: quyên góp lương thực và vật tư từ dân làng (phần lớn), bán dược thảo cấp thấp cho tán tu qua đường (ít ỏi), và thưởng săn yêu thú từ huyện phàm nhân (không thường xuyên). Chi phí chính là lương thực, vũ khí thay thế và nguyên liệu dược thảo. Nghĩa Đoàn thường xuyên rơi vào tình trạng ăn bữa nay lo bữa mai, nhưng chưa bao giờ thu phí bảo vệ từ phàm nhân.

## IX. Lịch Sử Tóm Tắt (简史)

Vân Thiết Trụ lớn lên trong một làng phàm nhân bị yêu thú tấn công. Gia đình bị giết, chỉ mình hắn sống sót nhờ được một tán tu đi ngang cứu giúp. Sự kiện đó khắc sâu vào tâm trí hắn — tại sao những tu sĩ mạnh mẽ không bảo vệ phàm nhân yếu đuối? Tại sao Cửu Hoa Kiếm Tông hùng mạnh ngay bên cạnh mà không thèm để mắt đến những ngôi làng nhỏ bé? Sau khi tu luyện từ linh căn tạp loại lên đến Trúc Cơ Viên Mãn bằng ý chí thuần túy, hắn lập Thanh Vân Nghĩa Đoàn 25 năm trước, tập hợp những tu sĩ cùng chí hướng để làm điều mà các tông phái lớn không thèm làm: bảo vệ phàm nhân. Nghĩa Đoàn hoạt động miễn phí nên luôn thiếu tài nguyên trầm trọng, nhưng đã cứu được vô số mạng sống.

## X. Giai Thoại & Bí Mật (轶事与秘密)

Cửu Hoa Kiếm Tông hoàn toàn biết Nghĩa Đoàn tồn tại nhưng chọn cách coi như không thấy. Lý do phức tạp: nếu thừa nhận Nghĩa Đoàn, đồng nghĩa thừa nhận mình đã bỏ mặc phàm nhân; nếu diệt Nghĩa Đoàn, mang tiếng ức hiếp kẻ yếu. Vì vậy, trạng thái hiện tại — giả vờ không biết — là lựa chọn tối ưu nhất cho Cửu Hoa.

Vân Thiết Trụ bí mật hy vọng một ngày Nghĩa Đoàn sẽ được Cửu Hoa thừa nhận, thậm chí sáp nhập thành một ngoại viện bảo vệ phàm nhân chính thức. Nhưng hắn hiểu rằng điều đó gần như không thể — thế giới tu luyện vận hành bằng sức mạnh, không phải lý tưởng, và 60 Luyện Khí-Trúc Cơ không đủ tư cách để Cửu Hoa Kiếm Tông nhìn thẳng vào mặt.

## XI. Quan Hệ Thế Lực (势力关系)

- **Cửu Hoa Kiếm Tông:** Quan hệ một chiều — Nghĩa Đoàn kính trọng và ngưỡng vọng, Cửu Hoa giả vờ không biết. Sự tồn tại của Nghĩa Đoàn vô tình trở thành "lá chắn" cho Cửu Hoa trước chỉ trích bỏ mặc phàm nhân.
- **Hoang Dã Thợ Săn Bang:** Đồng minh thực tế, thường xuyên hợp tác diệt trừ yêu thú cấp thấp gần làng. Quan hệ dựa trên lợi ích chung — Thợ Săn Bang lấy chiến lợi phẩm, Nghĩa Đoàn bảo vệ dân.
- **Thiên Yêu Đình:** Không có quan hệ trực tiếp, nhưng yêu thú cấp thấp từ lãnh thổ rộng lớn của Thiên Yêu Đình đôi khi tràn ra ngoại vi, tạo thành nguồn đe dọa chính cho các làng mà Nghĩa Đoàn bảo vệ.
