---
type: faction
name: Hợp Hoan Tông
hantu: 合欢宗
faction_type: Tông Môn
alignment: -6
race: Nhân Tộc, Yêu Tộc (Hấp dẫn)
region: Đông Hoang
founded: Trung Cổ Kỷ Nguyên
founder: Hợp Hoan Ma Nữ
emblem: Hop_Hoan_Bao_Diep.png
specialty: Song Tu Đại Pháp, Mê Hoặc Thuật, Thu thập tình báo
economy:
- Kinh doanh mạng lưới thanh lâu (Xuân Phong Lâu)
- Buôn bán hương liệu và xuân dược
- Bán tin tức tình báo
arcs:
  - arc: 1
    status: Hoạt động ngầm
    rank: Hạng Nhì
    leader: Tông Chủ Mị Cơ
    population: 4000
    territory:
      - Hợp Hoan Đảo
      - Mạng lưới Xuân Phong Lâu (Toàn lục địa)
    assets:
      - name: Mê Hồn Trận
        type: Trận Pháp
      - name: Vườn Đào Vạn Năm
        type: Bí Cảnh
      - name: Phấn Hồng Trướng
        type: Pháp Bảo
    stats: [2500, 4500, 3000, 4000, 2000, 4800]
    divisions:
      - name: Hồng Phấn Các
        role: Giao tiếp, ngoại giao và thu thập tình báo
        headcount:
          thai_thuong: 1
          ho_phap: 2
          truong_lao: 10
          chan_truyen: 50
          noi_mon: 500
          ngoai_mon: 2000
          tap_dich: 1000
        members:
          - character: Mị Cơ
            position: Tông Chủ
            cultivation: Nguyên Anh Hậu Kỳ
          - character: "[Trưởng Lão Hồng Phấn]"
            position: Các Chủ
            cultivation: Nguyên Anh Sơ Kỳ
            placeholder: true
      - name: Ám Hương Viện
        role: Lực lượng chiến đấu và sát thủ
        headcount:
          thai_thuong: 0
          ho_phap: 1
          truong_lao: 5
          chan_truyen: 20
          noi_mon: 100
          ngoai_mon: 300
          tap_dich: 100
        members:
          - character: "[Hộ Pháp Ám Hương]"
            position: Viện Chủ
            cultivation: Nguyên Anh Trung Kỳ
            placeholder: true
    relationships:
      - faction: Cửu U Ma Tông
        description: Liên minh ma đạo, phụ thuộc về tài nguyên ma khí.
        diplomacy:
          lien_minh: 60
          tin: 30
          uy_hiep: 40
          thuong_mai: 50
          on_oan: 0
          le_thuoc: 20
      - faction: Cửu Hoa Kiếm Tông
        description: Đối địch, thường xuyên bị các đệ tử chính đạo vây quét.
        diplomacy:
          lien_minh: -90
          tin: -100
          uy_hiep: 20
          thuong_mai: -80
          on_oan: -100
          le_thuoc: 0
---

# HỢP HOAN TÔNG (合欢宗)

## I. Tổng Quan (总览)
Hợp Hoan Tông là một thế lực ma đạo đặc thù, chuyên tu luyện thông qua con đường âm dương hòa hợp. Thay vì chiến đấu trực diện, họ sử dụng sự quyến rũ, ảo giác và mạng lưới thông tin khổng lồ để thao túng đối thủ. Tông môn này vừa bị khinh bỉ bởi chính đạo, vừa là nỗi khiếp sợ ngầm của các tu sĩ có tâm tính không kiên định.

## II. Địa Lý & Tài Nguyên (地理与 tài nguyên)
Trụ sở chính nằm trên Hợp Hoan Đảo, một hòn đảo thơ mộng ẩn giấu giữa các lớp sương mù ảo ảnh tại vùng biển Đông Hoang. Nơi đây có Vườn Đào Vạn Năm, nơi hoa đào nở rộ quanh năm cung cấp linh khí và hương liệu đặc trưng cho công pháp của tông môn.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
Tôn thờ chủ nghĩa khoái lạc và sự tự do của dục vọng. Họ tin rằng cảm xúc và sự ham muốn là nguồn năng lượng mạnh mẽ nhất của linh hồn. Đệ tử Hợp Hoan Tông thường có lối sống phóng túng, trang phục gợi cảm và luôn mang theo hương thơm mê hoặc.

## IV. Cơ Cấu Tổ Chức (组织结构)
```mermaid
graph TD
    HHTNS[Hợp Hoan Ma Nữ - Tổ Sư] --> TC[Tông Chủ: Mị Cơ]
    TC --> HDTL[Hội Đồng Trưởng Lão]
    HDTL --> HPC[Hồng Phấn Các]
    HDTL --> AHV[Ám Hương Viện]
    HDTL --> DHD[Đào Hoa Đường]
    HPC --> XP_LAU[Hệ thống Xuân Phong Lâu]
    AHV --> S_THU[Sát Thủ Ám Hương]
    DHD --> D_SU[Dược Sư Luyện Đan]
```

## V. Công Pháp & Trận Pháp (功法与阵法)
- **Công Pháp:** *Hợp Hoan Thiên Thư* (Bí tịch tối cao), *Mê Hồn Đại Pháp* (Thao túng tâm trí).
- **Trận Pháp:** *Hồng Phấn Mê Hồn Trận* - tạo ra ảo cảnh cực lạc khiến quân địch mất đi ý chí chiến đấu và dần bị hút cạn tinh khí.

## VI. Đặc Sản Môn Phái (门派特产)
- **Hợp Hoan Tán:** Loại xuân dược và thuốc mê mạnh nhất lục địa.
- **Ám Hương Phù:** Linh phù tỏa hương có khả năng làm nhiễu loạn thần thức đối phương.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Hương Phấn Điện:** Trung tâm điều hành và nơi tổ chức các nghi lễ lớn của tông môn.
- **Xuân Phong Lâu:** Mạng lưới cơ sở kinh doanh trải dài khắp các thành trì lớn, đóng vai trò là "mắt thần" thu thập tin tức.

## VIII. Kinh Tế (经济)
Kinh tế cực kỳ hưng thịnh nhờ việc kinh doanh các dịch vụ giải trí (thanh lâu, tửu quán) và buôn bán các loại hương liệu, đan dược đặc thù. Họ cũng nắm giữ nguồn thu lớn từ việc bán thông tin tình báo cho các thế lực khác.

## IX. Lịch Sử Tóm Tắt (简史)
Được sáng lập bởi Hợp Hoan Ma Nữ, một nữ tu thiên tài nhưng bị tổn thương tình cảm sâu sắc. Bà đã sáng tạo ra con đường tu luyện dựa trên việc chiếm đoạt nguyên âm và nguyên dương để nhanh chóng thăng tiến tu vi, biến Hợp Hoan Tông thành một thế lực đáng gờm.

## X. Giai Thoại & Bí Mật (轶 sự与秘密)
Đồn rằng trong sâu thẳm Hợp Hoan Đảo có một "Hồ Ước Nguyện", nơi những ai hiến tế ký ức đau khổ về tình yêu sẽ nhận được sức mạnh mê hoặc vô song.

## XI. Quan Hệ Thế Lực (势力关系)
```mermaid
graph LR
    HHT[Hợp Hoan Tông] -- Phụ thuộc -- CUMT[Cửu U Ma Tông]
    HHT -- Cung cấp tin tức -- HSM[Huyết Sát Minh]
    HHT -- Tử địch -- CHKT[Cửu Hoa Kiếm Tông]
```
