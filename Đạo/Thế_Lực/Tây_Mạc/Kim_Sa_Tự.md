---
type: faction
name: Kim Sa Tự
hantu: 金沙寺
faction_type: Tự Viện
alignment: 8
race: Nhân Tộc
region: Tây Mạc
founded: Kỷ Nguyên Khởi Nguyên
founder: Kim Sa Thiền Sư
emblem: Hoa_Sen_Vang.png
specialty: Kim Sa Luyện Thể, Bất Diệt Kim Thân
economy:
- Công đức phổ độ
- Khai thác Kim Sa Tinh
arcs:
  - arc: 1
    status: Hưng Thịnh
    rank: Hạng Nhất
    leader: Trụ Trì Không Độ
    population: 5000
    territory:
      - Kim Sa Nguyên
      - Ốc Đảo Thanh Lương
    assets:
      - name: Cửu Tầng Kim Tháp
        type: Công Trình
      - name: Kim Sa Đại Trận
        type: Trận Pháp
      - name: Kim Sa Bảo Trượng
        type: Pháp Bảo
    stats: [8000, 9000, 7500, 5000, 8500, 6000]
    divisions:
      - name: Đạt Ma Viện
        role: Chiến đấu và Hộ pháp
        headcount:
          tru_tri: 1
          truong_lao: 5
          tang_lu: 200
          sa_di: 500
          cu_si: 1000
        members:
          - character: Không Độ
            position: Trụ Trì
            cultivation: Hóa Thần Sơ Kỳ
          - character: "[Đại Trưởng Lão]"
            position: Trưởng Lão
            cultivation: Nguyên Anh Hậu Kỳ
            placeholder: true
      - name: Kinh Diệu Các
        role: Nghiên cứu kinh văn và thuật pháp
        headcount:
          tru_tri: 0
          truong_lao: 3
          tang_lu: 100
          sa_di: 200
          cu_si: 500
        members:
          - character: "[Trưởng Lão Tàng Kinh]"
            position: Thủ Các
            cultivation: Nguyên Anh Trung Kỳ
            placeholder: true
    relationships:
      - faction: Thiên Sa Thương Hội
        description: Giao thương linh thạch và cung cấp hộ vệ.
        diplomacy:
          lien_minh: 20
          tin: 50
          uy_hiep: 0
          thuong_mai: 80
          on_oan: 0
          le_thuoc: 0
      - faction: Phong Sát Cốc
        description: Trấn áp ma đạo và bão cát tà ác.
        diplomacy:
          lien_minh: -50
          tin: -100
          uy_hiep: 80
          thuong_mai: -100
          on_oan: -90
          le_thuoc: 0
---

# KIM SA TỰ (金沙寺)

## I. Tổng Quan (总览)
Kim Sa Tự là thánh địa Phật giáo lớn nhất tại Tây Mạc, nổi tiếng với con đường tu hành khổ hạnh và kỹ thuật luyện thể đạt đến cảnh giới bất diệt. Tự viện đóng vai trò là cột trụ chính đạo, bảo vệ cư dân sa mạc khỏi sự xâm lấn của ma đạo và thiên tai.

## II. Địa Lý & Tài Nguyên (地理与 tài nguyên)
Tọa lạc tại trung tâm Kim Sa Nguyên, nơi cát vàng tích tụ linh khí kim hệ dày đặc nhất. Tự viện sở hữu nhiều giếng cổ chứa linh dịch thanh khiết và các mỏ Kim Sa Tinh - nguyên liệu quý giá để rèn luyện pháp thân.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
Thờ phụng Kim Thân Đại Phật. Tín đồ tin rằng thân thể là đền đài của linh hồn, việc rèn luyện thân thể đến mức cực hạn là cách để thấu hiểu chân lý vĩnh hằng. Lễ hội Vạn Phật Cát là sự kiện lớn nhất, thu hút hàng vạn lữ khách sa mạc.

## IV. Cơ Cấu Tổ Chức (组织结构)
```mermaid
graph TD
    TT[Trụ Trì: Không Độ] --> HDTL[Hội Đồng Trưởng Lão]
    HDTL --> DMV[Đạt Ma Viện]
    HDTL --> KDC[Kinh Diệu Các]
    HDTL --> PDD[Phổ Độ Đường]
    DMV --> HTT[Khổ Hạnh Tăng]
    KDC --> SL[Tăng Lữ]
    PDD --> SD[Sa Di]
```

## V. Công Pháp & Trận Pháp (功法与阵法)
- **Công Pháp:** *Kim Sa Bất Diệt Quyết* (Luyện thể), *Đại Phạn Bát Nhã* (Tâm pháp).
- **Trận Pháp:** *Kim Sa Đại Trận* - biến toàn bộ cát vàng xung quanh tự viện thành lớp phòng thủ kiên cố hoặc bão cát nghiền nát kẻ thù.

## VI. Đặc Sản Môn Phái (门派特产)
- **Kim Sa Đan:** Đan dược hỗ trợ rèn luyện gân cốt.
- **Sa Thạch Niệm Châu:** Chuỗi hạt làm từ đá sa thạch có khả năng định tâm, kháng ảo giác.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Cửu Tầng Kim Tháp:** Nơi lưu trữ xá lợi của các vị cao tăng và cũng là trung tâm điều khiển đại trận.
- **Khổ Hạnh Lộ:** Con đường cát nóng hàng ngàn dặm dành cho việc rèn luyện đệ tử.

## VIII. Kinh Tế (经济)
Nguồn thu chính đến từ sự quyên góp của các tín đồ và việc kinh doanh Kim Sa Tinh cho các thương hội. Họ cũng nhận các hợp đồng hộ tống cao cấp xuyên sa mạc để gây quỹ cứu tế.

## IX. Lịch Sử Tóm Tắt (简史)
Sáng lập bởi Kim Sa Thiền Sư vào thời khởi nguyên. Ông đã dùng thần thông dời non lấp biển để tạo ra một vùng đất an lành giữa bão cát, đặt nền móng cho sự hưng thịnh của Phật pháp tại vùng đất cằn cỗi này.

## X. Giai Thoại & Bí Mật (轶 sự与秘密)
Tương truyền dưới đáy Cửu Tầng Kim Tháp có giam giữ một thực thể ma quỷ từ thời Thái Cổ, được trấn áp bởi sức mạnh của vạn dân tín ngưỡng.

## XI. Quan Hệ Thế Lực (势力关系)
```mermaid
graph LR
    KST[Kim Sa Tự] -- Giao hảo --> TSTH[Thiên Sa Thương Hội]
    KST -- Trừ ma --> PSC[Phong Sát Cốc]
    KST -- Hợp tác --> TLTV[Thanh Lương Thủ Vệ]
```
