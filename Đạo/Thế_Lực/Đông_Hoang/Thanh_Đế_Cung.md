---
type: faction
name: Thanh Đế Cung
hantu: 青帝宫
faction_type: Tông Môn
alignment: 9
race: Nhân Tộc, Tinh Linh Tộc (Hợp tác)
region: Đông Hoang
founded: Thái Cổ Kỷ Nguyên
founder: Thanh Đế
emblem: Thanh_De_Cung.png
specialty: Mộc Hệ Công Pháp, Chữa lành và Hồi sinh
economy:
- Trồng trọt linh dược quý hiếm
- Bán đan dược trị liệu
- Phí bảo hộ rừng già
arcs:
  - arc: 1
    status: Đang gặp nguy
    rank: Hạng Nhất
    leader: Cung Chủ Mộc Thanh Tiên
    population: 8000
    territory:
      - Thanh Đế Sơn
      - Mộc Linh Trận Địa
    assets:
      - name: Thanh Đế Linh Tháp
        type: Công Trình
      - name: Vườn Dược Thượng Cổ
        type: Bí Cảnh
      - name: Thanh Đế Kiếm
        type: Pháp Bảo
    stats: [8000, 10000, 7000, 8000, 9000, 10000]
    divisions:
      - name: Dược Tiên Viện
        role: Trị liệu và Điều chế đan dược
        headcount:
          thai_thuong: 2
          ho_phap: 1
          truong_lao: 12
          chan_truyen: 40
          noi_mon: 200
          ngoai_mon: 1000
          tap_dich: 500
        members:
          - character: Mộc Thanh Tiên
            position: Cung Chủ
            cultivation: Hóa Thần Trung Kỳ
          - character: "[Đại Trưởng Lão Dược Sư]"
            position: Viện Chủ
            cultivation: Nguyên Anh Hậu Kỳ
            placeholder: true
      - name: Mộc Linh Vệ
        role: Lực lượng chiến đấu bảo vệ rừng và địa mạch
        headcount:
          thai_thuong: 1
          ho_phap: 3
          truong_lao: 10
          chan_truyen: 50
          noi_mon: 300
          ngoai_mon: 2000
          tap_dich: 500
        members:
          - character: "[Thống Lĩnh Mộc Linh]"
            position: Hộ Pháp
            cultivation: Nguyên Anh Đỉnh Phong
            placeholder: true
    relationships:
      - faction: Tinh Linh Vương Đình
        description: Đồng minh thân thiết nhất, cùng bảo vệ linh hồn của rừng.
        diplomacy:
          lien_minh: 100
          tin: 100
          uy_hiep: 0
          thuong_mai: 50
          on_oan: 0
          le_thuoc: 0
      - faction: Vạn Độc Môn
        description: Đối địch do Vạn Độc Môn thường xuyên đầu độc rừng rậm.
        diplomacy:
          lien_minh: -80
          tin: -100
          uy_hiep: 70
          thuong_mai: -90
          on_oan: -100
          le_thuoc: 0
---

# THANH ĐẾ CUNG (青帝宫)

## I. Tổng Quan (总览)
Thanh Đế Cung là tông môn Mộc tu hàng đầu tại Đông Hoang, được coi là người bảo hộ của mọi sinh linh thảo mộc. Tông môn không chỉ sở hữu những bí thuật trị liệu huyền diệu mà còn gánh vác sứ mệnh canh giữ Mộc Linh Trận Địa - trái tim xanh của địa mạch khu vực phía Đông.

## II. Địa Lý & Tài Nguyên (地理与 tài nguyên)
Tọa lạc trên Thanh Đế Sơn, ngọn núi được bao phủ bởi rừng rậm quanh năm xanh tốt và linh khí mộc hệ dồi dào. Nơi đây sở hữu Vườn Dược Thượng Cổ, nơi quy tụ những loài linh thảo tuyệt chủng ở thế giới bên ngoài, cùng với các mạch linh tuyền có khả năng chữa lành thần kỳ.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
Tôn thờ Thanh Đế và triết lý "Sinh Sinh Bất Tức" (Sự sống luân hồi không dứt). Đệ tử Thanh Đế Cung luôn hướng tới sự hòa hợp giữa con người và thiên nhiên, coi việc bảo vệ sự sống là trọng trách tối thượng. Họ có lối sống thanh đạm, gần gũi với cỏ cây.

## IV. Cơ Cấu Tổ Chức (组织结构)
```mermaid
graph TD
    TT[Thái Thượng Hội] --> CC[Cung Chủ: Mộc Thanh Tiên]
    CC --> HDTL[Hội Đồng Trưởng Lão]
    HDTL --> DTV[Dược Tiên Viện]
    HDTL --> MLV[Mộc Linh Vệ]
    HDTL --> TSC[Trường Sinh Các]
    DTV --> DS[Dược Sư]
    MLV --> MLV_BINH[Vệ Binh Xanh]
    TSC --> NT[Nghiên Cứu Viên]
```

## V. Công Pháp & Trận Pháp (功法与阵法)
- **Công Pháp:** *Thanh Đế Trường Sinh Quyết* (Tu luyện sinh cơ), *Vạn Diệp Phi Hoa Lệnh* (Tấn công linh hoạt).
- **Trận Pháp:** *Mộc Linh Tịnh Hóa Trận* - có khả năng thanh lọc mọi loại độc tố và tăng tốc độ hồi phục cho đồng minh trong phạm vi lớn.

## VI. Đặc Sản Môn Phái (门派特产)
- **Thanh Đế Trường Sinh Đan:** Đan dược cực phẩm có thể kéo dài tuổi thọ và hồi phục trọng thương.
- **Linh Mộc Phù:** Phù văn chế tác từ gỗ linh mộc, dùng để hộ thân hoặc trấn áp tử khí.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Thanh Đế Linh Tháp:** Tháp canh cao vút dùng để theo dõi tình trạng sức khỏe của rừng rậm Đông Hoang.
- **Mộc Linh Trận Địa:** Hệ thống rễ cây và địa mạch được cường hóa bằng trận pháp thượng cổ.

## VIII. Kinh Tế (经济)
Kinh tế dựa trên việc cung cấp đan dược trị liệu và các loại linh thảo quý hiếm cho toàn bộ lục địa. Họ cũng nhận được phí bảo hộ từ các bộ lạc và thương hội muốn băng qua những khu rừng nguy hiểm.

## IX. Lịch Sử Tóm Tắt (简史)
Được sáng lập bởi Thanh Đế vào cuối thời Thái Cổ, nhằm tạo ra một lá chắn ngăn chặn sự héo úa của thế giới. Thanh Đế Cung đã vượt qua vô số cuộc chiến với các thế lực ma đạo để giữ vững màu xanh cho Đông Hoang.

## X. Giai Thoại & Bí Mật (轶 sự与秘密)
Tương truyền trung tâm của Thanh Đế Cung là một hạt giống của Cây Thế Giới chưa nở, chờ đợi một vị chân chúa xuất hiện để hồi sinh lại kỷ nguyên rực rỡ nhất của mộc hệ.

## XI. Quan Hệ Thế Lực (势力关系)
```mermaid
graph LR
    TDC[Thanh Đế Cung] -- Đồng minh -- TLVD[Tinh Linh Vương Đình]
    TDC -- Đối địch -- VDM[Vạn Độc Môn]
    TDC -- Hợp tác -- DVC[Dược Vương Cốc]
```
