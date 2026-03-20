---
type: faction
name: Cửu U Ma Tông
hantu: 九幽魔宗
faction_type: Tông Môn
alignment: -10
race: Nhân Tộc, Ma Tộc (Ẩn)
region: Thiên Trụ
founded: Thái Cổ Kỷ Nguyên
founder: Cửu U Ma Đế
emblem: Cuu_U_Ma_An.png
specialty: Cửu U Ma Khí, Thao túng tàn hồn, Luyện xác
economy:
- Buôn bán tài nguyên ma đạo
- Sát thủ thuê cao cấp
- Khai thác ma linh thạch
arcs:
  - arc: 1
    status: Ẩn mình tích lũy
    rank: Hạng Nhất
    leader: Ma Chủ Vô Tên
    population: 10000
    territory:
      - Cửu U Địa Cung (Dưới lòng đất Trung Tâm)
      - Vực Thẳm Ma Cung (Đông Hoang - Chi nhánh)
    assets:
      - name: Cửu U Ma Tuyền
        type: Tài Nguyên
      - name: Vạn Ma Phệ Hồn Trận
        type: Trận Pháp
      - name: Cửu U Trảm
        type: Pháp Bảo
    stats: [12000, 9000, 10000, 10000, 11000, 15000]
    divisions:
      - name: Huyết Ma Đường
        role: Lực lượng chiến đấu xung kích và luyện huyết
        headcount:
          thai_thuong: 3
          ho_phap: 5
          truong_lao: 20
          chan_truyen: 100
          noi_mon: 1000
          ngoai_mon: 3000
          tap_dich: 2000
        members:
          - character: "[Đại Ma Vương Huyết Sát]"
            position: Đường Chủ
            cultivation: Hóa Thần Hậu Kỳ
            placeholder: true
      - name: Ảnh Ma Viện
        role: Do thám, ám sát và thu thập oán khí
        headcount:
          thai_thuong: 1
          ho_phap: 3
          truong_lao: 15
          chan_truyen: 50
          noi_mon: 500
          ngoai_mon: 1500
          tap_dich: 500
        members:
          - character: Ma Chủ Vô Tên
            position: Ma Chủ
            cultivation: Luyện Hư Trung Kỳ
    relationships:
      - faction: Đại Càn Hoàng Triều
        description: Kẻ thù truyền kiếp, luôn tìm cách lật đổ vương triều.
        diplomacy:
          lien_minh: -100
          tin: -100
          uy_hiep: 100
          thuong_mai: -100
          on_oan: -100
          le_thuoc: 0
      - faction: Huyết Ma Tông
        description: Tông môn con, trực thuộc sự quản lý của Cửu U.
        diplomacy:
          lien_minh: 100
          tin: 80
          uy_hiep: 50
          thuong_mai: 90
          on_oan: 0
          le_thuoc: 100
---

# CỬU U MA TÔNG (九幽魔宗)

## I. Tổng Quan (总览)
Cửu U Ma Tông là biểu tượng tối cao của ma đạo tại Cố Nguyên Giới, khởi nguồn từ thời Thái Cổ. Tông môn này không chỉ là một tổ chức tu luyện mà còn là một thế lực chính trị ngầm, nắm giữ những bí mật đen tối nhất của lục địa và luôn chờ đợi cơ hội để thay đổi trật tự thiên hạ.

## II. Địa Lý & Tài Nguyên (地理与 tài nguyên)
Trụ sở chính là Cửu U Địa Cung, một hệ thống cung điện khổng lồ nằm sâu hàng ngàn dặm dưới lòng đất khu vực Trung Tâm. Nơi đây tập trung các mạch ma khí cổ đại và Cửu U Ma Tuyền - hồ nước chứa đựng năng lượng ma quái nguyên thủy, là tài nguyên cốt lõi để đào tạo cao thủ ma đạo.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
Tôn thờ Cửu U Ma Đế và triết lý "Ma Đạo Tự Tại". Họ tin rằng mọi quy tắc của Chính Đạo và Thiên Đạo đều là xiềng xích ngăn cản sự tiến hóa của sinh linh. Tại đây, sự phản bội được coi là một phần của quá trình chọn lọc tự nhiên, chỉ kẻ mạnh nhất và xảo quyệt nhất mới có quyền tồn tại.

## IV. Cơ Cấu Tổ Chức (组织结构)
```mermaid
graph TD
    CUMD[Cửu U Ma Đế - Thủy Tổ] --> MC[Ma Chủ: Vô Tên]
    MC --> CM Vương[Cửu Đại Ma Vương]
    CM Vương --> HMD[Huyết Ma Đường]
    CM Vương --> AMV[Ảnh Ma Viện]
    CM Vương --> TMC[Thi Ma Các]
    HMD --> MB[Ma Binh]
    AMV --> MS[Ma Sứ]
    TMC --> HK[Huyết Khôi]
```

## V. Công Pháp & Trận Pháp (功法与阵法)
- **Công Pháp:** *Cửu U Ma Kinh* (Chấn phái), *Vạn Ma Quy Tông* (Hấp thụ công lực).
- **Trận Pháp:** *Vạn Ma Phệ Hồn Trận* - trận pháp tuyệt sát có khả năng nuốt chửng linh hồn của hàng vạn sinh linh trong nháy mắt để cường hóa ma lực.

## VI. Đặc Sản Môn Phái (门派特产)
- **Cửu U Ma Đan:** Đan dược giúp đột phá cảnh giới nhưng khiến người dùng vĩnh viễn rơi vào ma đạo.
- **Huyết Thi:** Những xác sống được luyện chế từ tu sĩ chính đạo, giữ nguyên một phần kỹ năng chiến đấu khi còn sống.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Cửu U Ma Điện:** Nơi đặt ngai vàng của Ma Chủ và bàn thạch tế tự Thái Cổ.
- **Luân Hồi Ngục:** Nơi giam giữ và tra tấn linh hồn những kẻ phản bội hoặc tù binh chính đạo.

## VIII. Kinh Tế (经济)
Kinh tế dựa trên việc thâu tóm các mạch linh thạch bị ô nhiễm ma khí và việc buôn bán các loại bảo vật tà ác. Họ cũng điều hành mạng lưới sát thủ đắt giá nhất lục địa, chuyên thực hiện các hợp đồng "không tưởng".

## IX. Lịch Sử Tóm Tắt (简史)
Được sáng lập bởi Cửu U Ma Đế, người đã từng đại chiến với Thiên Đạo và bị phong ấn. Tông môn đã trải qua hàng vạn năm ẩn nấp dưới lòng đất, âm thầm gieo rắc mầm mống ma đạo vào các tông môn chính đạo và chờ đợi ngày Ma Đế tái sinh.

## X. Giai Thoại & Bí Mật (轶 sự与秘密)
Đồn rằng sâu trong Ma Tuyền có một cánh cổng dẫn đến "Cửu U Minh Giới" - nơi ở của những thực thể ma quỷ thực sự chưa bao giờ xuất hiện trên mặt đất.

## XI. Quan Hệ Thế Lực (势力关系)
```mermaid
graph LR
    CUMT[Cửu U Ma Tông] -- Thiên địch -- DCHH[Đại Càn Hoàng Triều]
    CUMT -- Thao túng -- HSM[Huyết Sát Minh]
    CUMT -- Lãnh đạo -- HMT[Huyết Ma Tông]
```
