---
type: faction
name: Thủy Kiếm Đảo
hantu: 水剑岛
faction_type: Tông Môn
alignment: 2
race: Nhân Tộc
region: Vô Tận Hải
founded: Trung Cổ Kỷ Nguyên
founder: Hải Triều Kiếm Khách
emblem: Thuy_Kiem_Trong_Song.png
specialty: Hải Triều Kiếm Pháp, Thủy Hệ Tấn Công, Chiến đấu trên mặt nước
economy:
- Săn bắn yêu thú biển lấy nội đan
- Khai thác san hô linh thạch và ngọc trai biển sâu
- Thu phí bảo hộ các làng chài lân cận
arcs:
  - arc: 1
    status: Độc lập phát triển
    rank: Hạng Ba
    leader: Đảo Chủ Thủy Vô Trần
    population: 1800
    territory:
      - Thủy Kiếm Đảo
      - Vùng biển bao quanh (Bán kính 100 dặm)
    assets:
      - name: Kiếm Ý Thạch
        type: Tài Nguyên
      - name: Đội thuyền chiến "Sóng Thần"
        type: Tài Nguyên
      - name: Thủy Tinh Kiếm
        type: Pháp Bảo
    stats: [2000, 1500, 1800, 1800, 1600, 1400]
    divisions:
      - name: Triều Tịch Đội
        role: Lực lượng chiến đấu chủ lực theo nhịp điệu thủy triều
        headcount:
          thai_thuong: 0
          ho_phap: 1
          truong_lao: 5
          chan_truyen: 20
          noi_mon: 100
          ngoai_mon: 400
          tap_dich: 100
        members:
          - character: Thủy Vô Trần
            position: Đảo Chủ
            cultivation: Nguyên Anh Trung Kỳ
          - character: "[Trưởng Lão Triều Tịch]"
            position: Đội Trưởng
            cultivation: Kim Đan Viên Mãn
            placeholder: true
      - name: Hải Ngự Đoàn
        role: Tuần tra biên giới biển và phòng thủ bờ đảo
        headcount:
          thai_thuong: 0
          ho_phap: 1
          truong_lao: 3
          chan_truyen: 10
          noi_mon: 50
          ngoai_mon: 300
          tap_dich: 50
        members:
          - character: "[Thống Lĩnh Hải Ngự]"
            position: Hộ Pháp
            cultivation: Kim Đan Đỉnh Phong
            placeholder: true
    relationships:
      - faction: Long Cung
        description: Cẩn trọng duy trì hòa bình, tránh va chạm với các tuần thú của rồng.
        diplomacy:
          lien_minh: 0
          tin: 20
          uy_hiep: 60
          thuong_mai: 10
          on_oan: 0
          le_thuoc: 0
      - faction: Hắc Hải Hải Tặc
        description: Đối địch, thường xuyên giao chiến để bảo vệ tuyến đường biển.
        diplomacy:
          lien_minh: -80
          tin: -100
          uy_hiep: 40
          thuong_mai: -90
          on_oan: -100
          le_thuoc: 0
---

# THỦY KIẾM ĐẢO (水剑岛)

## I. Tổng Quan (总览)
Thủy Kiếm Đảo là một tông môn kiếm tu đặc thù chọn đại dương làm thánh địa tu luyện. Với phong cách chiến đấu biến hóa như nước, lúc nhu hòa uyển chuyển, lúc cuồng bạo như sóng thần, các kiếm tu tại đây là những bậc thầy làm chủ không gian mặt biển. Tông môn giữ vị thế độc lập và là lá chắn quan trọng bảo vệ cư dân ven biển khỏi sự quấy nhiễu của yêu thú và hải tặc.

## II. Địa Lý & Tài Nguyên (地理 với tài nguyên)
Tọa lạc trên một hòn đảo có hình dáng như một thanh kiếm khổng lồ đâm thẳng xuống lòng Vô Tận Hải. Đảo sở hữu "Kiếm Ý Thạch" - những khối đá ngầm bị sóng biển bào mòn thành hình lưỡi kiếm, chứa đựng kiếm khí tự nhiên của trời đất. Vùng biển xung quanh đảo trù phú với các loại san hô linh thạch và ngọc trai biển sâu, là nguồn tài nguyên kinh tế chính.

## III. Văn Hóa & Tín Ngưỡng (文化 với信仰)
Tôn thờ Hải Triều Kiếm Khách và triết lý "Tâm Tĩnh Như Thủy, Kiếm Xuất Như Triều". Đệ tử Thủy Kiếm Đảo có lối sống tự do, phóng khoáng, tâm hồn hòa quyện với tiếng sóng và gió biển. Hàng năm, họ tổ chức "Đại Hội Triều Tịch" để các kiếm tu so tài ngay trên những con sóng dữ nhất.

## IV. Cơ Cấu Tổ Chức (组织结构)
```mermaid
graph TD
    HTKK[Hải Triều Kiếm Khách - Tổ Sư] --> ĐC[Đảo Chủ: Thủy Vô Trần]
    ĐC --> HDTL[Hội Đồng Kiếm Sư]
    HDTL --> TTĐ[Triều Tịch Đội]
    HDTL --> LVV[Lưu Thủy Viện]
    HDTL --> HNĐ[Hải Ngự Đoàn]
    TTĐ --> KĐ[Kiếm Đồ]
    LVV --> DS[Dược Sư Biển]
    HNĐ --> NKD[Ngư Kiếm Dân]
```

## V. Công Pháp & Trận Pháp (功法 với阵法)
- **Công Pháp:** *Hải Triều Vạn Lớp Kiếm* (Tấn công dồn dập), *Thủy Tinh Tâm Pháp* (Hồi phục và phòng ngự).
- **Trận Pháp:** *Vạn Kiếm Sóng Thần Trận* - trận pháp phòng thủ đảo, ngưng tụ nước biển thành hàng vạn lưỡi kiếm bay lơ lửng, tạo thành một bức tường kiếm bao quanh đảo khi có địch xâm lăng.

## VI. Đặc Sản Môn Phái (门派特产)
- **Thủy Tinh Kiếm:** Phi kiếm chế tác từ pha lê biển sâu, có khả năng ẩn hình khi ở dưới nước.
- **Hải Linh Đan:** Đan dược giúp tu sĩ hít thở và hoạt động bình thường dưới đáy biển trong thời gian dài.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Thính Triều Đài:** Nơi Đảo chủ tọa thiền và cảm nhận nhịp điệu của đại dương.
- **Kiếm Trì Dưới Nước:** Khu vực rèn luyện kiếm ý dưới áp lực nước cực lớn.

## VIII. Kinh Tế (経済)
Kinh tế dựa trên việc săn bắn yêu thú biển để lấy nội đan và các vật liệu quý giá. Họ cũng nổi tiếng với nghề khai thác ngọc trai linh khí và cung cấp dịch vụ bảo hộ cho các thương thuyền băng qua vùng biển phía Đông.

## IX. Lịch Sử Tóm Tắt (简史)
Sáng lập bởi Hải Triều Kiếm Khách vào thời kỷ nguyên Trung Cổ. Sau một lần thoát chết kỳ diệu giữa cơn bão thần, ông đã ngộ ra sự tương đồng giữa kiếm đạo và thủy triều, từ đó xây dựng nên tông môn trên hòn đảo hình kiếm này để truyền bá tư tưởng của mình.

## X. Giai Thoại & Bí Mật (轶 sự với bí mật)
Tương truyền Thủy Kiếm Đảo thực chất là một thanh thần binh của một vị đại năng thời Thái Cổ để lại, và hòn đảo sẽ trỗi dậy thành một thực thể khổng lồ khi thế giới gặp đại nạn.

## XI. Quan Hệ Thế Lực (势力关系)
```mermaid
graph LR
    TKĐ[Thủy Kiếm Đảo] -- Cẩn trọng -- LC[Long Cung]
    TKĐ -- Tử địch -- HHHT[Hắc Hải Hải Tặc]
    TKĐ -- Giao hảo -- CHKT[Cửu Hoa Kiếm Tông]
    TKĐ -- Hợp tác -- SHĐQ[San Hô Đảo Quốc]
```
