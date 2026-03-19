---
type: faction
name: Ốc Đảo Hộ Vệ Đội
hantu: 绿洲护卫队
faction_type: Quân Đoàn
alignment: 5
race: Nhân Tộc (Sa Tộc hỗn hợp)
region: Đông Hoang
founded: 40 năm trước
founder: Trần Sa Nghĩa
emblem: Oc_Dao_Ho_Ve_Doi.png
specialty: Bảo vệ nguồn nước ốc đảo, Chiến thuật phòng thủ sa mạc, Hệ thống cảnh báo rung động
economy:
- Thu phí bảo vệ nguồn nước cho dân cư ốc đảo
- Trao đổi nước sạch lấy lương thực và vật tư
- Bán thông tin về tình trạng nguồn nước cho tán tu
arcs:
  - arc: 1
    status: Cảnh giác cao
    rank: Không Xếp Hạng
    leader: Tổng Đội Trưởng Trần Sa Nghĩa
    population: 150
    territory:
      - Nguồn nước chính Huyết Tuyền Châu
      - Nguồn nước chính Khô Vinh Châu
    assets:
      - name: Hệ thống bẫy linh quanh nguồn nước
        type: Trận Pháp
      - name: Hệ thống ống tre cảm ứng rung động
        type: Công Trình
      - name: Bàn thờ Thủy Thần
        type: Linh Vật
    stats: [30, 20, 40, 45, 35, 25]
    divisions:
      - name: Đội Hộ Vệ
        role: Bảo vệ nguồn nước và tuần tra quanh ốc đảo
        headcount:
          tuong: 1
          uy: 4
          binh: 145
        members:
          - character: Trần Sa Nghĩa
            position: Tổng Đội Trưởng
            cultivation: Trúc Cơ Viên Mãn
          - character: "[Phó Đội Khu Đông]"
            position: Phó Đội
            cultivation: Trúc Cơ Trung Kỳ
            placeholder: true
          - character: "[Phó Đội Khu Tây]"
            position: Phó Đội
            cultivation: Trúc Cơ Sơ Kỳ
            placeholder: true
          - character: "[Phó Đội Khu Nam]"
            position: Phó Đội
            cultivation: Trúc Cơ Sơ Kỳ
            placeholder: true
          - character: "[Phó Đội Khu Bắc]"
            position: Phó Đội
            cultivation: Trúc Cơ Sơ Kỳ
            placeholder: true
    relationships:
      - faction: Ốc Đảo Vi Linh
        description: Hộ Vệ Đội nhận ra Vi Linh đang suy yếu và bí mật tìm cách bảo vệ chúng, coi Vi Linh là nền tảng sự sống của ốc đảo.
        diplomacy:
          lien_minh: 30
          tin: 40
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 10
          le_thuoc: 0
      - faction: Thiên Sa Thương Hội
        description: Đối nghịch sâu sắc, Hộ Vệ Đội biết Thương Hội từng tham gia âm mưu chiếm nguồn nước năm xưa.
        diplomacy:
          lien_minh: -60
          tin: -80
          uy_hiep: 30
          thuong_mai: -50
          on_oan: -70
          le_thuoc: 0
      - faction: Sa Trùng Vi Tộc
        description: Hợp tác ngầm sử dụng hệ thống rung động dưới đất để cảnh báo sớm kẻ xâm nhập.
        diplomacy:
          lien_minh: 40
          tin: 50
          uy_hiep: 0
          thuong_mai: 10
          on_oan: 0
          le_thuoc: 0
---

# ỐC ĐẢO HỘ VỆ ĐỘI (绿洲护卫队)

## I. Tổng Quan (总览)

Ốc Đảo Hộ Vệ Đội là lực lượng dân quân tự phát được thành lập cách đây 40 năm, chuyên bảo vệ các nguồn nước ốc đảo tại Huyết Tuyền Châu và Khô Vinh Châu khỏi sự xâm chiếm của các tông môn lớn. Dưới sự lãnh đạo của Tổng Đội Trưởng Trần Sa Nghĩa — một tán tu Trúc Cơ Viên Mãn xuất thân từ Sa Tộc — đội dân quân khoảng 150 người đã trở thành biểu tượng phản kháng của dân thường Tây Mạc. Dù trang bị thô sơ và tu vi thấp, Hộ Vệ Đội bù đắp bằng lòng dũng cảm, sự am hiểu địa hình sa mạc và hệ thống cảnh báo tinh vi kết hợp với Sa Trùng Vi Tộc.

## II. Địa Lý & Tài Nguyên (地理与资源)

Hộ Vệ Đội đóng quân quanh các nguồn nước chính của Huyết Tuyền Châu và Khô Vinh Châu — những ốc đảo nhỏ nơi nguồn nước quý hiếm hơn linh thạch. Địa hình xung quanh là cát sa mạc mênh mông, cây cối thưa thớt chỉ mọc được quanh mạch nước. Tài nguyên chính là vũ khí thô sơ tự rèn từ kim loại tái chế, bẫy cơ giới bố trí quanh nguồn nước, và một ít pháp khí cấp thấp do tán tu quyên góp. Đặc biệt, hệ thống ống tre cắm sâu dưới đất cho phép nghe tín hiệu rung động từ Sa Trùng, là phương tiện cảnh báo sớm vô cùng hiệu quả trong môi trường sa mạc bao la.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)

Triết lý cốt lõi của Hộ Vệ Đội được đúc kết trong câu: "Nước là máu của sa mạc — ai cướp nước, cướp mạng." Đây không chỉ là khẩu hiệu mà là quy tắc sống chết — bất kỳ ai, kể cả tu sĩ từ tông môn lớn, nếu cố chiếm đoạt nguồn nước đều sẽ bị đối đầu bằng mọi giá. Mỗi sáng, thành viên Hộ Vệ Đội rưới nước lên bàn thờ Thủy Thần nhỏ bằng đất nung — nghi thức đơn giản nhưng thể hiện sự tôn kính nguồn nước. Trong dân ốc đảo, Hộ Vệ Đội được kính trọng như những người hùng thầm lặng, nhưng các tông môn lớn lại gọi họ là "bọn bướng bỉnh" vì dám chống đối tu sĩ.

## IV. Cơ Cấu Tổ Chức (组织结构)

Tổ chức đơn giản theo kiểu quân sự dã chiến. Tổng Đội Trưởng Trần Sa Nghĩa — vốn là Sa Tộc, từ bỏ bộ lạc để bảo vệ ốc đảo — nắm quyền chỉ huy toàn bộ. Bốn Phó Đội tu vi từ Trúc Cơ Sơ đến Trung Kỳ, mỗi người phụ trách một khu vực ốc đảo. Dưới đó là khoảng 145 dân quân hỗn hợp phàm nhân và Luyện Khí, phân chia thành tổ tuần tra luân phiên canh gác nguồn nước suốt ngày đêm.

## V. Công Pháp & Trận Pháp (功法与阵法)

Hộ Vệ Đội không có công pháp chính thức. Trần Sa Nghĩa dạy một số chiêu thức Thủy hệ cơ bản cho thành viên có linh căn, đủ để phát hiện và bảo vệ nguồn nước chứ không phải để giao chiến. Hệ thống phòng thủ chính là bẫy linh bố trí quanh nguồn nước — khi có kẻ xâm nhập, bẫy kích hoạt tạo cột nước phun lên cao làm tín hiệu cảnh báo cho toàn đội. Chiến thuật phòng thủ cố định lợi dụng tối đa địa hình ốc đảo: hào nước, hố cát, và các bụi cây gai bao quanh tạo thành phòng tuyến tự nhiên.

## VI. Đặc Sản Môn Phái (门派特产)

- **Nước Ốc Đảo Tinh Lọc:** Nước nguồn được Vi Linh tịnh hóa, có hàm lượng linh lực nhẹ, uống vào giúp phục hồi thể lực cho phàm nhân và hỗ trợ tu luyện sơ cấp. Hộ Vệ Đội cung cấp cho dân cư ốc đảo với giá rẻ.
- **Bẫy Linh Cột Nước:** Pháp khí cấp thấp tự chế, khi kích hoạt sẽ phun cột nước cao ba trượng có chứa linh lực nhẹ. Không gây sát thương đáng kể nhưng hiệu quả cảnh báo tuyệt vời trong sa mạc bao la.

## VII. Cơ Sở Hạ Tầng (基础设施)

- **Dãy Lều Trụ Sở:** Khu lều tạm bợ dựng trên nền đất cao tránh ngập, xung quanh là hào nhỏ chứa dung dịch giải độc thô sơ chống côn trùng sa mạc.
- **Hệ Thống Ống Tre Rung Động:** Mạng lưới ống tre cắm sâu dưới đất, kết nối các điểm canh gác, dùng để nhận tín hiệu rung động từ Sa Trùng Vi Tộc khi có kẻ lạ tiếp cận.
- **Bàn Thờ Thủy Thần:** Bàn thờ đất nung nhỏ đặt bên mỗi nguồn nước chính, vừa là nơi cúng tế vừa là điểm tập kết khi có báo động.
- **Kho Vũ Khí:** Một hang đá nhỏ gần nguồn nước Huyết Tuyền Châu chứa vũ khí dự trữ và vài pháp khí cấp thấp do tán tu quyên góp.

## VIII. Kinh Tế (经济)

Kinh tế của Hộ Vệ Đội hoạt động theo mô hình cộng đồng tự cung tự cấp. Dân cư ốc đảo đóng góp lương thực, vải vóc và vật tư để nuôi dưỡng đội dân quân, đổi lại được bảo vệ nguồn nước an toàn. Một phần nhỏ nước sạch được đổi cho tán tu qua đường để lấy vật phẩm tu luyện cấp thấp. Thu nhập không đáng kể, hầu hết thành viên vẫn phải canh tác riêng để kiếm sống bên cạnh nhiệm vụ tuần tra.

## IX. Lịch Sử Tóm Tắt (简史)

Ốc Đảo Hộ Vệ Đội thành lập cách đây 40 năm khi một tông môn lớn cố chiếm độc quyền nguồn nước Huyết Tuyền Châu. Dân cư ốc đảo — phàm nhân và tán tu nghèo — không cam chịu mất đi nguồn sống duy nhất, tự võ trang chống trả. Trần Sa Nghĩa khi đó là tán tu Trúc Cơ Trung Kỳ, đứng ra lãnh đạo cuộc phản kháng. Tông môn cuối cùng rút lui vì không muốn mang tiếng "ức hiếp phàm nhân", nhưng luôn tìm cách gây áp lực gián tiếp thông qua Thiên Sa Thương Hội.

Từ chiến thắng đầu tiên ấy, Hộ Vệ Đội trở thành biểu tượng phản kháng của dân thường Tây Mạc. Trần Sa Nghĩa tiếp tục tu luyện đến Trúc Cơ Viên Mãn và mở rộng phạm vi bảo vệ sang cả Khô Vinh Châu. Gần đây, ông phát hiện Vi Linh trong nguồn nước đang dần suy yếu, khiến ông lo lắng nguồn nước sẽ cạn trong vài chục năm nếu không tìm ra nguyên nhân.

## X. Giai Thoại & Bí Mật (轶事与秘密)

- Trần Sa Nghĩa từng từ chối lời mời gia nhập Thiên Sa Thương Hội với đãi ngộ hậu hĩnh — lý do thực sự là ông biết Thương Hội đã tham gia vào âm mưu chiếm nguồn nước năm xưa. Nếu sự thật bại lộ, quan hệ giữa Thương Hội và dân ốc đảo sẽ hoàn toàn sụp đổ.
- Dưới lòng Huyết Tuyền Châu có một mạch nước ngầm cổ đại, nối liền với Lưu Sa Cổ Thành. Nguồn nước đó có vị tanh nhẹ như máu, và Vi Linh trong mạch nước này có màu đỏ nhạt thay vì xanh thông thường — Trần Sa Nghĩa nghi ngờ nguồn nước ấy không phải nước thường.
- Ốc Đảo Vi Linh trong nguồn nước đang dần yếu đi, nhưng Trần Sa Nghĩa chưa dám công khai sự thật này vì sợ gây hoảng loạn. Ông đang bí mật liên lạc với các dược sư để tìm cách cứu vãn.

## XI. Quan Hệ Thế Lực (势力关系)

| Thế Lực | Quan Hệ | Mô Tả |
|---------|---------|-------|
| Ốc Đảo Vi Linh | Bảo hộ ngầm | Bí mật bảo vệ Vi Linh vì chúng là nền tảng nguồn nước |
| Thiên Sa Thương Hội | Đối nghịch | Biết Thương Hội liên quan âm mưu chiếm nước năm xưa |
| Sa Trùng Vi Tộc | Hợp tác ngầm | Chia sẻ hệ thống cảnh báo rung động dưới đất |
