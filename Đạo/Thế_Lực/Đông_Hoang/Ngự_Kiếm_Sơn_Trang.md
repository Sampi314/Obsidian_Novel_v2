---
type: faction
name: Ngự Kiếm Sơn Trang
hantu: 御剑山庄
faction_type: Tông Môn
alignment: 6
race: Nhân Tộc
region: Đông Hoang
founded: Trung Cổ Kỷ Nguyên
founder: Kiếm Vô Trần
emblem: Ngu_Kiem_Son_Trang.png
specialty: Đúc tạo phi kiếm, Ngự Kiếm Thuật
economy:
- Sản xuất và bán phi kiếm cao cấp
- Dịch vụ bảo trì linh binh
- Đào tạo kiếm tu cơ bản
arcs:
  - arc: 1
    status: Phát triển rực rỡ
    rank: Hạng Nhì
    leader: Trang Chủ Kiếm Nam Thiên
    population: 2500
    territory:
      - Ngự Kiếm Sơn
      - Kiếm Trì
    assets:
      - name: Vạn Kiếm Quy Tông Trận
        type: Trận Pháp
      - name: Lò đúc Thiên Hỏa
        type: Công Trình
      - name: Long Tuyền Kiếm
        type: Pháp Bảo
    stats: [3500, 3000, 4500, 2500, 3200, 3800]
    divisions:
      - name: Kiếm Đúc Viện
        role: Nghiên cứu và chế tác phi kiếm
        headcount:
          thai_thuong: 1
          ho_phap: 0
          truong_lao: 10
          chan_truyen: 30
          noi_mon: 100
          ngoai_mon: 500
          tap_dich: 300
        members:
          - character: "[Đại Sư Đúc Kiếm]"
            position: Viện Chủ
            cultivation: Nguyên Anh Hậu Kỳ
            placeholder: true
      - name: Ngự Kiếm Đường
        role: Huấn luyện chiến đấu và ngự kiếm thuật
        headcount:
          thai_thuong: 0
          ho_phap: 2
          truong_lao: 8
          chan_truyen: 50
          noi_mon: 200
          ngoai_mon: 1000
          tap_dich: 200
        members:
          - character: Kiếm Nam Thiên
            position: Trang Chủ
            cultivation: Nguyên Anh Viên Mãn
          - character: "[Thống Lĩnh Kiếm Vệ]"
            position: Hộ Pháp
            cultivation: Nguyên Anh Sơ Kỳ
            placeholder: true
    relationships:
      - faction: Cửu Hoa Kiếm Tông
        description: Giao hảo lâu đời, nguồn gốc xuất thân của tổ sư.
        diplomacy:
          lien_minh: 80
          tin: 90
          uy_hiep: 0
          thuong_mai: 70
          on_oan: 0
          le_thuoc: 0
      - faction: Thạch Linh Cung
        description: Đối tác chiến lược cung cấp phôi kiếm và quặng hiếm.
        diplomacy:
          lien_minh: 50
          tin: 70
          uy_hiep: 0
          thuong_mai: 100
          on_oan: 0
          le_thuoc: 0
---

# NGỰ KIẾM SƠN TRANG (御剑山庄)

## I. Tổng Quan (总览)
Ngự Kiếm Sơn Trang là trung tâm chế tác phi kiếm lớn nhất Đông Hoang, nổi tiếng với sự kết hợp hoàn mỹ giữa kỹ thuật luyện khí và kiếm đạo. Sơn trang không chỉ cung cấp binh khí cho các kiếm tu mà còn là nơi lưu giữ những bí thuật ngự kiếm cổ xưa, giữ vai trò quan trọng trong việc duy trì sức mạnh của các thế lực Chính Đạo.

## II. Địa Lý & Tài Nguyên (地理 với tài nguyên)
Tọa lạc trên Ngự Kiếm Sơn, một ngọn núi có hình dáng như một thanh đại kiếm vươn thẳng lên trời. Dưới chân núi là Kiếm Trì - một hồ nước linh thiêng chứa đựng kiếm ý tích tụ hàng nghìn năm, là nơi lý tưởng để rèn luyện và khai phong cho các thanh linh binh. Sơn trang còn sở hữu các mạch hỏa tự nhiên phục vụ cho việc đúc kiếm.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
Đề cao triết lý "Nhân Kiếm Hợp Nhất". Đệ tử Ngự Kiếm Sơn Trang coi thanh kiếm là người bạn đời, là linh hồn của mình. Văn hóa của sơn trang xoay quanh sự tỉ mỉ, kiên nhẫn và lòng trung thành. Hàng năm, họ tổ chức "Lễ Khai Phong" để tôn vinh những thanh kiếm xuất sắc nhất được ra đời.

## IV. Cơ Cấu Tổ Chức (组织结构)
```mermaid
graph TD
    KVTS[Kiếm Vô Trần - Tổ Sư] --> TC[Trang Chủ: Kiếm Nam Thiên]
    TC --> HDTL[Hội Đồng Trưởng Lão]
    HDTL --> KDV[Kiếm Đúc Viện]
    HDTL --> NKĐ[Ngự Kiếm Đường]
    HDTL --> TKC[Tàng Kiếm Các]
    KDV --> DKS[Đúc Kiếm Sư]
    NKĐ --> KV[Kiếm Vệ]
    TKC --> QL[Quản Thủ]
```

## V. Công Pháp & Trận Pháp (功法与阵法)
- **Công Pháp:** *Ngự Kiếm Tâm Kinh* (Điều khiển kiếm ý), *Thiên Hỏa Luyện Kim Thuật* (Kỹ thuật đúc).
- **Trận Pháp:** *Vạn Kiếm Quy Tông Trận* - trận pháp phòng thủ tối thượng, điều khiển hàng vạn thanh kiếm tạo thành một lưới bảo vệ bất khả xâm phạm xung quanh sơn trang.

## VI. Đặc Sản Môn Phái (门派特产)
- **Thanh Phong Kiếm:** Loại phi kiếm phổ thông nhưng có độ linh hoạt và sắc bén cực cao.
- **Kiếm Hạp Thiên Cơ:** Hộp đựng kiếm đặc chế có khả năng dưỡng kiếm và phóng kiếm tự động.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Kiếm Trì:** Nơi rèn luyện kiếm ý và thử nghiệm sức mạnh của kiếm.
- **Lò đúc Thiên Hỏa:** Hệ thống lò luyện khổng lồ tận dụng địa hỏa để nung chảy linh kim.

## VIII. Kinh Tế (经济)
Nguồn thu chính đến từ việc sản xuất và bán các loại phi kiếm cho tu sĩ khắp lục địa. Họ cũng cung cấp dịch vụ bảo trì, nâng cấp linh binh và đào tạo các khóa học ngự kiếm ngắn hạn cho các tán tu.

## IX. Lịch Sử Tóm Tắt (简史)
Được sáng lập bởi Kiếm Vô Trần, một thiên tài đúc kiếm từng là trưởng lão của Cửu Hoa Kiếm Tông. Ông tách ra để theo đuổi con đường luyện khí thuần túy, nhưng vẫn giữ mối liên hệ mật thiết với tông môn cũ, biến sơn trang thành một thế lực độc lập nhưng uy tín.

## X. Giai Thoại & Bí Mật (轶 sự với bí mật)
Đồn rằng trong lòng Kiếm Trì có một thanh "Thần Kiếm Phôi" chưa hoàn thiện, được tổ sư để lại và chỉ có người mang kiếm ý thuần khiết nhất mới có thể đánh thức nó.

## XI. Quan Hệ Thế Lực (势力关系)
```mermaid
graph LR
    NKST[Ngự Kiếm Sơn Trang] -- Giao hảo -- CHKT[Cửu Hoa Kiếm Tông]
    NKST -- Đối tác -- SLC[Thạch Linh Cung]
    NKST -- Cung cấp -- TAM[Thái Ất Môn]
```
