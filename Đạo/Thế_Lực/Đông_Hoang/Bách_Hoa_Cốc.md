---
type: faction
name: Bách Hoa Cốc
hantu: 百花谷
faction_type: Tông Môn
alignment: 7
race: Nhân Tộc (Nữ)
region: Đông Hoang
founded: Trung Cổ Kỷ Nguyên
founder: Bách Hoa Tiên Tử
emblem: Bach_Hoa_No_Ro.png
specialty: Mộc Hệ Trị Liệu, Kiếm Vũ Bách Hoa, Chế tạo phấn hoa linh dược
economy:
- Bán phấn hoa và linh dược đặc thù
- Dịch vụ chữa thương cao cấp cho tu sĩ chính đạo
- Kinh doanh hương liệu linh khí
arcs:
  - arc: 1
    status: Yên bình
    rank: Hạng Nhì
    leader: Cốc Chủ Hoa Nguyệt Tiên
    population: 3000
    territory:
      - Bách Hoa Thung Lũng
      - Hồ Hương Sắc
    assets:
      - name: Vườn Hoa Linh Cảm
        type: Bí Cảnh
      - name: Bách Hoa Trận
        type: Trận Pháp
      - name: Bách Hoa Tán
        type: Pháp Bảo
    stats: [2000, 4500, 3500, 3000, 4000, 4200]
    divisions:
      - name: Hoa Linh Đường
        role: Chữa thương, điều chế dược thảo và tiếp đón lữ khách
        headcount:
          thai_thuong: 1
          ho_phap: 0
          truong_lao: 8
          chan_truyen: 30
          noi_mon: 300
          ngoai_mon: 1000
          tap_dich: 500
        members:
          - character: Hoa Nguyệt Tiên
            position: Cốc Chủ
            cultivation: Nguyên Anh Hậu Kỳ
          - character: "[Đại Trưởng Lão Hoa Linh]"
            position: Đường Chủ
            cultivation: Nguyên Anh Sơ Kỳ
            placeholder: true
      - name: Kiếm Hoa Viện
        role: Lực lượng chiến đấu bảo vệ thung lũng
        headcount:
          thai_thuong: 0
          ho_phap: 2
          truong_lao: 5
          chan_truyen: 20
          noi_mon: 100
          ngoai_mon: 500
          tap_dich: 100
        members:
          - character: "[Thống Lĩnh Vệ Hoa]"
            position: Viện Chủ
            cultivation: Nguyên Anh Trung Kỳ
            placeholder: true
    relationships:
      - faction: Thái Ất Môn
        description: Giao hảo lâu đời, trao đổi đan dược và bí thuật trận pháp.
        diplomacy:
          lien_minh: 70
          tin: 80
          uy_hiep: 0
          thuong_mai: 60
          on_oan: 0
          le_thuoc: 0
      - faction: Hợp Hoan Tông
        description: Tử địch do các hành vi bắt cóc nữ đệ tử để làm lô đỉnh.
        diplomacy:
          lien_minh: -100
          tin: -100
          uy_hiep: 40
          thuong_mai: -100
          on_oan: -100
          le_thuoc: 0
---

# BÁCH HOA CỐC (百花谷)

## I. Tổng Quan (总览)
Bách Hoa Cốc là tông môn nữ tu danh tiếng nhất Đông Hoang, nổi bật với sự kết hợp giữa vẻ đẹp thanh cao và sức mạnh mộc hệ huyền diệu. Tông môn không chỉ là một cơ sở tu luyện mà còn là một thánh địa trị liệu, nơi cung cấp những loại linh dược quý hiếm nhất lục địa.

## II. Địa Lý & Tài Nguyên (地理与 tài nguyên)
Ẩn mình trong một thung lũng được bảo vệ bởi những rặng núi đá dựng đứng, nơi đây có khí hậu bốn mùa như xuân. Thung lũng sở hữu Vườn Hoa Linh Cảm - nơi quy tụ hàng vạn loài hoa linh dược có khả năng tự hấp thụ linh khí trời đất, tạo nên một môi trường tu luyện mộc hệ hoàn hảo.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
Tôn thờ Bách Hoa Tiên Tử và triết lý "Vạn Vật Hữu Linh, Hoa Khai Kiến Đạo". Đệ tử Bách Hoa Cốc đề cao sự dịu dàng nhưng kiên cường, coi trọng nghệ thuật và sự hòa hợp. Mỗi đệ tử khi nhập môn đều chọn cho mình một loài hoa bản mệnh để tu luyện.

## IV. Cơ Cấu Tổ Chức (组织结构)
```mermaid
graph TD
    BHTS[Bách Hoa Tiên Tử - Tổ Sư] --> CC[Cốc Chủ: Hoa Nguyệt Tiên]
    CC --> HDTL[Hội Đồng Trưởng Lão]
    HDTL --> HLĐ[Hoa Linh Đường]
    HDTL --> KHV[Kiếm Hoa Viện]
    HDTL --> HPC[Hương Phấn Các]
    HLĐ --> DSU[Dược Sư]
    KHV --> VHS[Vệ Hoa Sứ]
    HPC --> CTC[Chế Tác Viên]
```

## V. Công Pháp & Trận Pháp (功法与阵法)
- **Công Pháp:** *Bách Hoa Diễn Nghĩa* (Biến hóa linh hoạt), *Linh Hoa Kiếm Quyết* (Kiếm pháp thanh thoát).
- **Trận Pháp:** *Bách Hoa Trận* - một đại trận ảo giác dựa trên hương thơm và sắc màu, có khả năng ru ngủ hoặc làm hỗn loạn thần thức quân địch.

## VI. Đặc Sản Môn Phái (门派特产)
- **Bách Hoa Linh Sương:** Tinh chất thu thập từ cánh hoa buổi sớm, có tác dụng thanh tẩy tâm hồn và hồi phục linh lực.
- **Phấn Hoa Mê Hồn:** Loại bột mịn có khả năng tạo ra ảo giác ngắn hạn khi tiếp xúc.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Hương Sắc Điện:** Trung tâm của cốc, nơi đặt linh vị tổ sư và tổ chức các lễ hội hoa.
- **Hồ Hương Sắc:** Hồ nước trung tâm chứa đựng linh dịch hòa tan từ phấn hoa, là nơi rèn luyện của các đệ tử cấp cao.

## VIII. Kinh Tế (经济)
Nguồn thu khổng lồ từ việc cung cấp linh dược và dịch vụ chữa thương cho các tông môn chính đạo. Họ cũng nắm giữ thị trường hương liệu cao cấp và các loại mỹ phẩm linh khí dành cho nữ tu sĩ khắp lục địa.

## IX. Lịch Sử Tóm Tắt (简史)
Được sáng lập bởi Bách Hoa Tiên Tử vào thời Trung Cổ, người đã tìm thấy thung lũng này trong một lần bị thương nặng và được vạn hoa chữa lành. Bà đã lập ra môn phái để che chở cho những nữ tu muốn tìm kiếm sự bình yên giữa thế giới tu chân đầy khốc liệt.

## X. Giai Thoại & Bí Mật (轶 sự với bí mật)
Tương truyền "Nước mắt hoa hồng" của Bách Hoa Tiên Tử vẫn còn lưu lại trong hồ Hương Sắc, và ai có duyên tìm được sẽ đạt đến cảnh giới mộc tu tối thượng.

## XI. Quan Hệ Thế Lực (势力关系)
```mermaid
graph LR
    BHC[Bách Hoa Cốc] -- Đồng minh -- TAM[Thái Ất Môn]
    BHC -- Tử địch -- HHT[Hợp Hoan Tông]
    BHC -- Đối tác -- DVC[Dược Vương Cốc]
```
