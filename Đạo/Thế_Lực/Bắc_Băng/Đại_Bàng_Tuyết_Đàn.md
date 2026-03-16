---
type: faction
name: Đại Bàng Tuyết Đàn
hantu: 雪鹰团
faction_type: Hội
alignment: 2
race: Yêu Tộc (Ưng yêu)
region: Bắc Băng
founded: Năm Khởi Nguyên 99.950
founder: Ưng Liệt
emblem: Canh_Ung_Va_Mat_Bao.png
specialty: Trinh sát không trung tầm xa, Điềm báo bão tuyết, Giao dịch tin tức
economy:
- Buôn bán thông tin trinh sát địa hình và yêu thú
- Dịch vụ hộ tống đường không cho vật phẩm nhỏ
- Thu thập linh thạch rớt từ các vách đá cao
arcs:
  - arc: 1
    status: Hoạt động mạnh vùng không phận tundra
    rank: Hạng Năm
    leader: Ưng Liệt
    population: 26
    territory:
      - Không phận Tundra mở (Bắc Băng)
      - Tổ Ưng Vách Đá (Căn cứ tạm thời)
    assets:
      - name: Mạng lưới Ảnh Điệp Ưng
        type: Tài Nguyên
      - name: Trận pháp "Phong Linh Gia Tốc"
        type: Trận Pháp
      - name: Linh Mục Ưng Nhãn
        type: Pháp Bảo
    stats: [100, 200, 300, 26, 400, 500]
    divisions:
      - name: Đội Trinh Sát Không Trung
        role: Tuần tra và thu thập biến động thiên tượng
        headcount:
          hoi_truong: 1
          pho_hoi_truong: 0
          thanh_vien: 15
          tong_quan: 0
        members:
          - character: Ưng Liệt
            position: Đàn Trưởng
            cultivation: Trúc Cơ Trung Kỳ
          - character: "[Ưng Ảnh]"
            position: Đội Trưởng
            cultivation: Luyện Khí Đỉnh Phong
            placeholder: true
      - name: Ban Ấu Ưng
        role: Đào tạo và nuôi dưỡng thế hệ trẻ
        headcount:
          hoi_truong: 0
          pho_hoi_truong: 0
          thanh_vien: 10
          tong_quan: 0
        members:
          - character: "[Tiểu Ưng]"
            position: Học Viên
            cultivation: Luyện Khí Sơ Kỳ
            placeholder: true
    relationships:
      - faction: Phá Băng Thương Đội
        description: Khách hàng lớn nhất mua tin tức về các tuyến đường an toàn.
        diplomacy:
          lien_minh: 20
          tin: 60
          uy_hiep: 0
          thuong_mai: 90
          on_oan: 0
          le_thuoc: 0
      - faction: Bạch Cốt Hội
        description: Cảnh giác do lo sợ bị phát hiện các giao dịch ngầm.
        diplomacy:
          lien_minh: -10
          tin: 20
          uy_hiep: 50
          thuong_mai: 10
          on_oan: 0
          le_thuoc: 0
---

# ĐẠI BÀNG TUYẾT ĐÀN (雪鹰团)

## I. Tổng Quan (总览)
Đại Bàng Tuyết Đàn là một nhóm các ưng yêu chuyên nghiệp hoạt động tại vùng trời phía Bắc Bắc Băng. Với tầm nhìn sắc bén và khả năng bay lượn thượng thừa, họ đã biến bản năng săn mồi thành một dịch vụ cung cấp tin tức và trinh sát vô giá. Dù quân số không đông, đàn đóng vai trò là "đôi mắt trên cao" cho mọi cuộc hành trình xuyên qua vùng tundra đầy rẫy hiểm nguy.

## II. Địa Lý & Tài Nguyên (地理 với tài nguyên)
Hoạt động chủ yếu trên bầu trời tundra mở, nơi có tầm nhìn rộng nhất Bắc Băng. Họ không có căn cứ cố định dưới đất mà thường xuyên di chuyển theo các luồng gió ấm. Tài nguyên quý giá nhất của đàn là hệ thống "Thông Tin Không Trung" - các bản ghi chép chi tiết về sự phân bố của yêu thú và các vết nứt linh mạch rò rỉ dưới lớp băng.

## III. Văn Hóa & Tín Ngưỡng (文化 với信仰)
Đề cao triết lý: "Mắt trên trời, giá trên đất". Thành viên đàn coi sự chính xác của tin tức là danh dự hàng đầu. Văn hóa của họ mang đậm tính kỷ luật và sự kiên nhẫn, đề cao tinh thần độc lập nhưng tuyệt đối trung thành với lộ trình đã phân công. Nghi lễ lớn nhất là cuộc bay xuyên bão tuyết dành cho các ấu ưng để chứng minh tư cách gia nhập đàn.

## IV. Cơ Cấu Tổ Chức (组织结构)
```mermaid
graph TD
    ĐT[Đàn Trưởng: Ưng Liệt] --> HDTL[Hội Đồng Ưng Già]
    HDTL --> ĐTS[Đội Trinh Sát]
    HDTL --> BẦU[Ban Ấu Ưng]
    HDTL --> BGT[Ban Giao Thương]
    ĐTS --> ƯA[Ưng Ảnh]
    BẦU --> ƯN[Ưng Non]
    BGT --> SG[Sứ Giả Bán Tin]
```

## V. Công Pháp & Trận Pháp (功法 với阵法)
- **Công Pháp:** Dựa trên *Huyết Mạch Ưng Vương*, tập trung vào việc cường hóa nhãn lực và khả năng nương theo sức gió để tiết kiệm linh lực khi bay xa.
- **Trận Pháp:** *Phong Linh Gia Tốc Trận* - trận pháp sơ cấp giúp cả đàn tăng tốc độ bay gấp đôi trong thời gian ngắn để thoát khỏi các trận đại bão đột ngột.

## VI. Đặc Sản Môn Phái (门派特产)
- **Ưng Nhãn Phù:** Loại bùa chú giúp tu sĩ tạm thời có được tầm nhìn cực xa và khả năng nhìn xuyên qua sương mù mỏng.
- **Lông Ưng Tuyết:** Vật liệu nhẹ chứa phong linh khí, thường được dùng để chế tạo cánh phi thuyền hoặc ám khí.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Tổ Ưng Vách Đá:** Các điểm dừng chân bí mật trên các vách đá cao nhất Bắc Băng, nơi lót bằng cỏ linh sương ấm áp.
- **Đài Vọng Gió:** Các cột đá được khắc phù văn chỉ hướng gió tại các điểm nút giao thông đường không.

## VIII. Kinh Tế (経済)
Nguồn thu nhập chính đến từ việc bán tin tức trinh sát cho các thương đoàn và các hội tán tu. Họ cũng nhận các hợp đồng giao bưu kiện nhỏ cần tốc độ cao hoặc thám thính các khu vực bí cảnh mới lộ diện sau bão.

## IX. Lịch Sử Tóm Tắt (简史)
Được sáng lập bởi Ưng Liệt, một ưng yêu già từng bị thương nặng và mất khả năng chiến đấu đỉnh cao. Thay vì bỏ cuộc, ông nhận ra tiềm năng kinh tế từ việc quan sát và đã tập hợp những đồng loại có chung hoàn cảnh để xây dựng nên Đại Bàng Tuyết Đàn, biến sự suy yếu về thể chất thành sự vượt trội về thông tin.

## X. Giai Thoại & Bí Mật (轶 sự với bí mật)
Tương truyền Ưng Liệt từng nhìn thấy một thực thể khổng lồ đang ngủ say bên dưới lớp băng Bắc Hải, và toàn bộ lộ trình tuần tra của đàn hiện nay thực chất là để âm thầm giám sát sự thức tỉnh của thực thể đó.

## XI. Quan Hệ Thế Lực (势力关系)
```mermaid
graph LR
    ĐBTĐ[Đại Bàng Tuyết Đàn] -- Cung cấp tin -- PBTĐ[Phá Băng Thương Đội]
    ĐBTĐ -- Hợp tác -- HTQTCĐ[Hàn Tinh Quan Trắc Đài]
    ĐBTĐ -- Theo dõi -- BCH[Bạch Cốt Hội]
    ĐBTĐ -- Tránh né -- CQTĐ[Cực Quang Thần Điện]
```
