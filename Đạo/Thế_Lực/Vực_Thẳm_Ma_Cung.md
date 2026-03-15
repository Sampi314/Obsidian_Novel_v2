---
type: faction
name: Vực Thẳm Ma Cung
hantu: 深渊魔宫
faction_type: Tông Môn
alignment: -9
race: Hải Tộc (Biến dị), Thủy Ma
region: Vô Tận Hải
founded: Thái Cổ Kỷ Nguyên
founder: Thâm Uyên Ma Chủ
emblem: Con_Mat_Tim_Trong_Vuc_Tham.png
specialty: Áp Suất Khí, Bóng Tối Ma Pháp, Thao túng sinh vật biển sâu
economy:
- Cướp bóc tu sĩ và tàu thuyền
- Khai thác ma tinh thạch biển sâu
- Buôn bán nô lệ hải tộc
arcs:
  - arc: 1
    status: Đang trỗi dậy từ đáy sâu
    rank: Hạng Nhì (Nguy hiểm tột độ)
    leader: Ma Cung Chủ Thâm Hải
    population: 4000
    territory:
      - Rãnh Mariana (Vực Thẳm Hắc Ám)
      - Vùng Biển Chết
    assets:
      - name: Hắc Ma Tuyền biển sâu
        type: Tài Nguyên
      - name: Trận pháp "Áp Suất Diệt Tuyệt"
        type: Trận Pháp
      - name: Ma Nhãn Hắc Ám
        type: Pháp Bảo
    stats: [4000, 3000, 4500, 4000, 5000, 3500]
    divisions:
      - name: Thâm Hải Ma Quân
        role: Lực lượng chiến đấu xung kích dưới áp lực cực lớn
        headcount:
          thai_thuong: 1
          ho_phap: 3
          truong_lao: 12
          chan_truyen: 40
          noi_mon: 200
          ngoai_mon: 1000
          tap_dich: 500
        members:
          - character: "[Thống Lĩnh Thâm Hải]"
            position: Hộ Pháp
            cultivation: Nguyên Anh Hậu Kỳ
            placeholder: true
      - name: Ám Ảnh Ngư Đội
        role: Do thám, bắt cóc và ám sát trên mặt nước
        headcount:
          thai_thuong: 0
          ho_phap: 1
          truong_lao: 5
          chan_truyen: 20
          noi_mon: 100
          ngoai_mon: 500
          tap_dich: 100
        members:
          - character: "[Sát Thủ Bóng Đêm]"
            position: Đội Trưởng
            cultivation: Kim Đan Đỉnh Phong
            placeholder: true
    relationships:
      - faction: Long Cung
        description: Tử địch, luôn tìm cách phá hoại Long Mạch biển sâu và lật đổ sự thống trị của Long Tộc.
        diplomacy:
          lien_minh: -100
          tin: -100
          uy_hiep: 80
          thuong_mai: -100
          on_oan: -100
          le_thuoc: 0
      - faction: Cửu U Ma Tông
        description: Liên minh ma đạo lục địa, trao đổi tài nguyên và kỹ thuật luyện ma.
        diplomacy:
          lien_minh: 50
          tin: 40
          uy_hiep: 20
          thuong_mai: 70
          on_oan: 0
          le_thuoc: 0
---

# VỰC THẲM MA CUNG (深渊魔宫)

## I. Tổng Quan (总览)
Vực Thẳm Ma Cung là thế lực ma đạo đáng sợ nhất dưới lòng đại dương, ngự trị tại rãnh biển sâu nhất Vô Tận Hải - nơi ánh sáng mặt trời vĩnh viễn không thể chạm tới. Cư dân của ma cung là những sinh vật biển bị đột biến bởi ma khí và những ma tu chọn con đường tu luyện dựa trên áp suất nước và bóng tối tuyệt đối. Đây là một pháo đài tự nhiên không thể xâm phạm, nơi mọi quy luật của mặt đất đều trở nên vô nghĩa.

## II. Địa Lý & Tài Nguyên (地理 với tài nguyên)
Tọa lạc tại đáy Rãnh Mariana, trung tâm là một tòa thành đen ngòm xây dựng từ đá núi lửa và xương cốt yêu quái biển. Ma cung nắm giữ "Hắc Ma Tuyền biển sâu" - mạch ma khí thủy hệ mạnh nhất thế giới, cùng với các loại khoáng thạch chịu áp suất cực cao dùng để chế tạo giáp trụ và vũ khí ma đạo.

## III. Văn Hóa & Tín Ngưỡng (文化 với信仰)
Tôn thờ Thâm Uyên Ma Chủ và sức mạnh của bóng tối vĩnh cửu. Họ tin rằng đại dương cuối cùng sẽ nuốt chửng mọi lục địa và bóng tối là trạng thái nguyên thủy của vũ trụ. Văn hóa ma cung cực kỳ tàn bạo, kẻ yếu sẽ bị ép trở thành thức ăn cho các quái vật biển hoặc vật thí nghiệm cho các loại ma độc biển sâu.

## IV. Cơ Cấu Tổ Chức (组织结构)
```mermaid
graph TD
    TUMC[Thâm Uyên Ma Chủ - Thủy Tổ] --> CC[Cung Chủ: Thâm Hải]
    CC --> HDTL[Hội Đồng Ma Trưởng Lão]
    HDTL --> THMQ[Thâm Hải Ma Quân]
    HDTL --> AANĐ[Ám Ảnh Ngư Đội]
    HDTL --> TMC[Thi Ma Các biển sâu]
    THMQ --> MB[Ma Binh Biến Dị]
    AANĐ --> ST[Sát Thủ Bóng Tối]
    TMC --> HK[Huyết Khôi Biển]
```

## V. Công Pháp & Trận Pháp (功法 với阵法)
- **Công Pháp:** *Thâm Uyên Áp Sát Quyết* (Sử dụng áp lực nước để nghiền nát linh lực đối phương), *Hắc Ám Thủy Ma Pháp*.
- **Trận Pháp:** *Áp Suất Diệt Tuyệt Trận* - trận pháp phòng thủ bao quanh cung điện, tăng áp suất nước lên hàng vạn lần khiến bất kỳ kẻ xâm nhập nào cũng bị ép thành bã thịt ngay lập tức.

## VI. Đặc Sản Môn Phái (门派特产)
- **Ma Nhãn Hắc Ám:** Loại pháp bảo giúp tu sĩ nhìn thấu mọi vật trong bóng tối tuyệt đối và có khả năng phát ra tia sáng ăn mòn thần thức.
- **Thâm Hải Ma Độc:** Chất độc chiết xuất từ cá quỷ biển sâu, không màu không mùi, cực khó phát hiện trong môi trường nước.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Hắc Diệu Thạch Điện:** Cung điện trung tâm cứng cáp hơn cả kim cương, có khả năng chịu đựng sức ép của toàn bộ đại dương.
- **Bể Nuôi Cấy Đột Biến:** Nơi lai tạo ra các loài quái vật biển phục vụ chiến tranh.

## VIII. Kinh Tế (経済)
Kinh tế dựa trên việc cướp bóc các đoàn thuyền và tu sĩ hành tẩu trên biển. Họ cũng độc quyền cung cấp các loại ma tinh thạch chỉ có ở vùng biển cực sâu cho các thế lực ma đạo trên đất liền thông qua mạng lưới giao thương ngầm.

## IX. Lịch Sử Tóm Tắt (简史)
Sáng lập từ thời kỷ nguyên Thái Cổ bởi một vị Ma Chủ bị Long Tộc và Nhân Tộc liên thủ đánh đuổi xuống biển sâu. Hắn đã lợi dụng môi trường khắc nghiệt của rãnh biển để hồi phục và xây dựng nên một đế chế bóng tối, âm thầm chờ đợi ngày quay lại mặt đất để trả thù.

## X. Giai Thoại & Bí Mật (轶 sự với bí mật)
Đồn rằng Thâm Uyên Ma Chủ chưa bao giờ thực sự chết, mà hắn đã hóa thân thành chính rãnh biển Mariana, và mỗi đợt sóng thần trên thế giới đều là một lần hắn trở mình.

## XI. Quan Hệ Thế Lực (势力关系)
```mermaid
graph LR
    VTMC[Vực Thẳm Ma Cung] -- Tử địch -- LC[Long Cung]
    VTMC -- Liên minh -- CUMT[Cửu U Ma Tông]
    VTMC -- Thao túng -- HYMC[Hải Yêu Mê Cung]
    VTMC -- Đối địch -- HTC[Hải Thần Cung]
```
