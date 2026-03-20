---
type: faction
name: Băng Lang Bộ Lạc
hantu: 冰狼部落
faction_type: Bộ Lạc
alignment: 4
race: Nhân Tộc (Băng Tộc lai), Lang Yêu
region: Bắc Băng
founded: Trung Cổ Kỷ Nguyên
founder: Tuyết Lang Nha
emblem: Dau_Soi_Trong_Bao_Tuyet.png
specialty: Khế ước sinh tử với Băng Lang, Băng Luyện Thể, Săn bắn trong bão tuyết
economy:
- Bán da và nanh yêu thú cực hạn
- Trao đổi linh thảo băng hệ
- Thuê mướn kỵ sĩ sói bảo vệ đoàn lữ hành
arcs:
  - arc: 1
    status: Di cư sinh tồn
    rank: Hạng Ba (Quy mô lớn)
    leader: Đại Tù Trưởng Tuyết Lang
    population: 100000
    territory:
      - Rừng Tuyết biên thùy Bắc Băng
      - Các hang động băng đá (Trú đông)
    assets:
      - name: Hang Lang Thần
        type: Tài Nguyên
      - name: Trận pháp "Tuyết Ảnh Vây Hãm"
        type: Trận Pháp
      - name: Răng Nanh Thần Sói
        type: Pháp Bảo
    stats: [4000, 1500, 2500, 10000, 3000, 1800]
    divisions:
      - name: Kỵ Sĩ Sói
        role: Lực lượng chiến đấu và săn bắn chủ lực
        headcount:
          truong_lao: 5
          chien_binh: 2000
          dan_thuong: 5000
        members:
          - character: "[Thống Lĩnh Kỵ Sĩ Sói]"
            position: Tướng Quân
            cultivation: Kim Đan Đỉnh Phong
            placeholder: true
      - name: Lang Vu Viện
        role: Chữa bệnh, thực hiện nghi lễ và bói toán tuyết
        headcount:
          truong_lao: 10
          chien_binh: 100
          dan_thuong: 500
        members:
          - character: "[Đại Lang Vu]"
            position: Trưởng Lão
            cultivation: Nguyên Anh Sơ Kỳ
            placeholder: true
    relationships:
      - faction: Huyền Băng Cung
        description: Đối địch, thường xuyên cướp bóc xe lương để sinh tồn.
        diplomacy:
          lien_minh: -60
          tin: -80
          uy_hiep: 50
          thuong_mai: -100
          on_oan: -90
          le_thuoc: 0
      - faction: Bách Thú Sơn Trang
        description: Thân thiện, trao đổi nguyên liệu thú lấy vũ khí sắt.
        diplomacy:
          lien_minh: 40
          tin: 60
          uy_hiep: 0
          thuong_mai: 80
          on_oan: 0
          le_thuoc: 0
---

# BĂNG LANG BỘ LẠC (冰狼部落)

## I. Tổng Quan (总览)
Băng Lang Bộ Lạc là một cộng đồng du mục hùng mạnh cư ngụ tại ranh giới khắc nghiệt của Bắc Băng. Đây là sự kết hợp độc đáo giữa những con người mang huyết thống Băng Tộc và loài Winter Wolf (Băng Lang) thông thái. Thay vì tu luyện tiên pháp thanh cao, họ chọn con đường cộng sinh sinh tử với bầy sói, tạo nên một đạo quân kỵ sĩ sói dũng mãnh, có khả năng di chuyển và chiến đấu hiệu quả ngay cả trong những trận bão tuyết dữ dội nhất.

## II. Địa Lý & Tài Nguyên (地理 với tài nguyên)
Trụ sở chính là các lều trại di động di chuyển theo mùa dọc theo Rừng Tuyết biên thùy. Họ nắm giữ bí mật về các hang động băng giá chứa đựng "Băng Tinh Linh Thạch" và các loại rêu tuyết có tác dụng cầm máu thần kỳ. Tài nguyên lớn nhất chính là bầy sói hàng vạn con được thuần hóa qua nhiều thế hệ.

## III. Văn Hóa & Tín Ngưỡng (文化 với信仰)
Tôn thờ Lang Thần và sức mạnh của bầy đàn. Cư dân bộ lạc tin rằng "Một con sói đơn độc sẽ chết, nhưng cả đàn sẽ tồn tại". Văn hóa của họ đề cao sự dũng cảm, lòng trung thành tuyệt đối và bản năng sinh tồn. Nghi lễ lớn nhất là "Lễ Khế Ước", nơi một thiếu niên sẽ chọn cho mình một chú sói con để cùng nhau lớn lên và chiến đấu trọn đời.

## IV. Cơ Cấu Tổ Chức (组织结构)
```mermaid
graph TD
    LT[Lang Thần - Linh Vật] --> ĐTT[Đại Tù Trưởng: Tuyết Lang]
    ĐTT --> HDTT[Hội Đồng Tù Trưởng Bộ Lạc]
    HDTT --> KSS[Kỵ Sĩ Sói]
    HDTT --> LVV[Lang Vu Viện]
    HDTT --> TSĐ[Thợ Săn Đội]
    KSS --> KB[Chiến Binh]
    LVV --> LV[Lang Vu]
    TSĐ --> DT[Dân Thường]
```

## V. Công Pháp & Trận Pháp (功法 với阵法)
- **Công Pháp:** *Băng Lang Luyện Thể Quyết* (Cường hóa nhục thân), *Lang Tâm Thông* (Giao tiếp tâm linh với sói).
- **Trận Pháp:** *Tuyết Ảnh Vây Hãm Trận* - trận pháp phối hợp giữa hàng trăm kỵ sĩ sói, tạo ra các dư ảnh mờ ảo trong bão tuyết để cô lập và tiêu diệt quân địch.

## VI. Đặc Sản Môn Phái (门派特产)
- **Tuyết Lang Đao:** Kiếm ngắn làm từ nanh sói già, có khả năng gây đóng băng vết thương đối phương.
- **Rượu Lang Huyết:** Loại rượu mạnh giúp tu sĩ giữ ấm cơ thể và tăng cường khí huyết trong môi trường cực lạnh.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Hang Lang Thần:** Nơi tôn nghiêm nhất, nơi trú ngụ của Lang Vương và các vị tổ tiên.
- **Hệ thống Lều Trại Phù Văn:** Các lều trại có khả năng chống lại áp lực của bão tuyết cấp 10.

## VIII. Kinh Tế (経済)
Kinh tế dựa trên săn bắn và thu thập. Họ trao đổi da sói, xương yêu thú và các dược liệu băng hệ cho các thương hội từ Trung Tâm để lấy gạo, vải vóc và vũ khí kim loại. Họ cũng thỉnh thoảng nhận các nhiệm vụ bảo vệ các đoàn thám hiểm đi vào vùng lõi Bắc Băng.

## IX. Lịch Sử Tóm Tắt (简史)
Được thành lập bởi Tuyết Lang Nha, một vị anh hùng bị trục xuất khỏi Huyền Băng Cung do mang trong mình dòng máu lai. Ông đã thuần hóa được bầy sói hoang và tập hợp những kẻ bị ruồng bỏ để xây dựng nên một bộ lạc có thể kiêu hãnh tồn tại giữa tuyết trắng, thách thức sự thống trị của các tông môn chính thống.

## X. Giai Thoại & Bí Mật (轶 sự với bí mật)
Tương truyền mỗi khi trăng tròn đỏ xuất hiện, các chiến binh cao cấp của bộ lạc có thể thực hiện "Lang Hóa", biến thành những thực thể bán thú với sức mạnh tăng vọt gấp nhiều lần.

## XI. Quan Hệ Thế Lực (势力关系)
```mermaid
graph LR
    BLBL[Băng Lang Bộ Lạc] -- Đối địch -- HBC[Huyền Băng Cung]
    BLBL -- Thân thiện -- BTS[Bách Thú Sơn Trang]
    BLBL -- Giao thương -- BBC[Bách Bảo Các]
    BLBL -- Cảnh giác -- CQTĐ[Cực Quang Thần Điện]
```
