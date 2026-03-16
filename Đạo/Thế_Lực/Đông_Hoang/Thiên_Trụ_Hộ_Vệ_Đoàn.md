---
type: faction
name: Thiên Trụ Hộ Vệ Đoàn
hantu: 天柱护卫团
faction_type: Quân Đoàn
alignment: 7
race: Đa chủng tộc (Nhân, Cự tộc lai)
region: Đông Hoang
founded: Trung Cổ Kỷ Nguyên
founder: Đại Tướng Quân Thiên Giáp
emblem: Ngon_Giao_Va_Thap_Da.png
specialty: Trận pháp quân đội, Phòng thủ thành trì, Khí Cầm Cự
economy:
- Ngân sách từ Đại Càn Hoàng Triều và các đại tông môn
- Phí thông hành qua các cửa ải (Hợp pháp)
- Bán các loại binh khí phù văn quân dụng
arcs:
  - arc: 1
    status: Trấn thủ nghiêm ngặt
    rank: Hạng Nhất
    leader: Đại Tướng Quân Vô Nhai
    population: 50000
    territory:
      - Các bậc thang đá Thiên Trụ Sơn
      - Chín cửa ải chính (Cửu Trọng Thiên)
    assets:
      - name: Trận pháp "Cửu Trọng Hộ Thiên"
        type: Trận Pháp
      - name: Trấn Quốc Thần Pháo
        type: Pháp Bảo
      - name: Hệ thống thành lũy đá tảng
        type: Công Trình
    stats: [10000, 8000, 9000, 15000, 12000, 7000]
    divisions:
      - name: Kiếm Trận Quân
        role: Lực lượng bộ binh chủ lực sử dụng trận pháp liên kết linh lực
        headcount:
          tuong: 10
          uy: 100
          binh: 20000
        members:
          - character: "[Cửu Môn Đề Đốc]"
            position: Tướng Quân
            cultivation: Nguyên Anh Viên Mãn
            placeholder: true
      - name: Khí Cầm Đội
        role: Lực lượng pháo binh và phòng không tầm xa
        headcount:
          tuong: 5
          uy: 50
          binh: 5000
        members:
          - character: "[Thống Lĩnh Pháo Đài]"
            position: Uy Trấn
            cultivation: Nguyên Anh Sơ Kỳ
            placeholder: true
    relationships:
      - faction: Đại Càn Hoàng Triều
        description: Nhận mệnh lệnh và ngân sách duy trì trật tự trục thế giới.
        diplomacy:
          lien_minh: 80
          tin: 90
          uy_hiep: 0
          thuong_mai: 50
          on_oan: 0
          le_thuoc: 40
      - faction: Vân Tông
        description: Đồng minh, bảo vệ lối vào duy nhất dẫn lên cõi tiên của Vân Tông.
        diplomacy:
          lien_minh: 70
          tin: 80
          uy_hiep: 0
          thuong_mai: 20
          on_oan: 0
          le_thuoc: 0
---

# THIÊN TRỤ HỘ VỆ ĐOÀN (天柱护卫团)

## I. Tổng Quan (总览)
Thiên Trụ Hộ Vệ Đoàn là lực lượng quân sự kỷ luật nhất lục địa, có nhiệm vụ trấn giữ con đường bộ duy nhất dẫn lên đỉnh núi Thiên Trụ Sơn. Với quân số đông đảo và hệ thống trận pháp liên kết hàng vạn người, quân đoàn này là bức tường thép ngăn chặn mọi thế lực tà ác hoặc tội phạm muốn xâm nhập vào các vùng đất linh thiêng phía trên. Họ hoạt động dựa trên tôn chỉ: "Thiên Trụ không đổ, Hộ Vệ không lùi."

## II. Địa Lý & Tài Nguyên (地理 với tài nguyên)
Đóng quân dọc theo các bậc thang đá khổng lồ (Thiên Thang) của núi Thiên Trụ. Quân đoàn kiểm soát chín cửa ải chiến lược từ chân núi lên đến tầng mây. Tài nguyên chính của họ là các mỏ đá linh thạch cứng cáp dùng để gia cố thành lũy và nguồn linh khí phong phú từ trục thế giới tỏa ra.

## III. Văn Hóa & Tín Ngưỡng (文化 với信仰)
Tôn thờ kỷ luật và lòng trung thành. Thành viên hộ vệ đoàn coi nhiệm vụ trấn thủ là vinh dự cao quý nhất. Văn hóa quân đội tại đây rất nghiêm khắc, mọi hành vi vi phạm kỷ luật đều bị trừng trị bằng pháp hình nặng nề. Họ có nghi lễ "Thề Dưới Chân Cột Trời" mỗi khi có tân binh gia nhập.

## IV. Cơ Cấu Tổ Chức (组织结构)
```mermaid
graph TD
    DTHG[Đại Tướng Quân Thiên Giáp - Thủy Tổ] --> DTQ[Đại Tướng Quân: Vô Nhai]
    DTQ --> CMĐĐ[Cửu Môn Đề Đốc]
    CMĐĐ --> KTQ[Kiếm Trận Quân]
    CMĐĐ --> KCĐ[Khí Cầm Đội]
    CMĐĐ --> AVĐ[Ảnh Vệ Đội]
    KTQ --> BS[Binh Sĩ]
    KCĐ --> PS[Pháo Thủ]
    AVĐ --> MT[Mật Thám]
```

## V. Công Pháp & Trận Pháp (功法 với阵法)
- **Công Pháp:** *Thiên Trụ Trấn Áp Quyết* (Tăng cường trọng lực và phòng ngự), *Liên Tâm Công* (Chia sẻ linh lực).
- **Trận Pháp:** *Cửu Trọng Hộ Thiên Trận* - hệ thống trận pháp đa tầng kết nối chín cửa ải, có khả năng hóa đá không gian xung quanh để ngăn chặn các thực thể bay hoặc dịch chuyển tức thời.

## VI. Đặc Sản Môn Phái (门派特产)
- **Thiên Trụ Trấn Giáp:** Bộ giáp nặng làm từ đá thạch anh linh lực, có khả năng kháng lại mọi hiệu ứng đẩy lùi.
- **Linh Thạch Pháo:** Loại pháo cầm tay có sức công phá cực lớn, chuyên dùng để tiêu diệt yêu thú bay.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Cửu Trọng Quan:** Chín pháo đài đá kiên cố nằm ở các độ cao khác nhau trên núi.
- **Doanh Trại Phù Không:** Các doanh trại nằm lơ lửng giữa các tầng mây để dự phòng lực lượng.

## VIII. Kinh Tế (経済)
Ngân sách chủ yếu được cung cấp bởi Đại Càn Hoàng Triều và các đại tông môn có lợi ích tại Thiên Trụ Sơn. Họ cũng thu phí thông hành (hợp pháp) đối với các thương đoàn và tu sĩ hành tẩu qua các cửa ải để duy trì trang thiết bị quân sự.

## IX. Lịch Sử Tóm Tắt (简史)
Được thành lập vào thời Trung Cổ sau khi một nhóm ma tu lớn cố gắng leo lên Thiên Trụ để phá hoại Long Mạch thế giới. Đại Tướng Quân Thiên Giáp đã tập hợp những binh lính dũng cảm nhất để lập nên phòng tuyến này, từ đó về sau trở thành lực lượng bảo vệ trục thế giới chính thức.

## X. Giai Thoại & Bí Mật (轶 sự với bí mật)
Tương truyền dưới chân cửa ải thứ nhất có chôn cất một thanh "Trấn Thiên Kiếm", chỉ có Đại Tướng Quân mới có thể rút ra khi Thiên Trụ thực sự gặp nguy hiểm.

## XI. Quan Hệ Thế Lực (势力关系)
```mermaid
graph LR
    TTHVĐ[Thiên Trụ Hộ Vệ Đoàn] -- Phục vụ -- DCHH[Đại Càn Hoàng Triều]
    TTHVĐ -- Đồng minh -- VT[Vân Tông]
    TTHVĐ -- Cảnh giới -- HSM[Huyết Sát Minh]
    TTHVĐ -- Hợp tác -- SLC[Thạch Linh Cung]
```
