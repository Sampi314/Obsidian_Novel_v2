---
type: faction
name: Độc Long Bảo
hantu: 毒龙堡
faction_type: Hội
alignment: -5
race: Nhân Tộc, Yêu Tộc (Hắc ám)
region: Nam Cương
founded: Trung Cổ Kỷ Nguyên
founder: Độc Long Lão Nhân
emblem: Doc_Long_Pháo_Đài.png
specialty: Thuần hóa Độc Long Tích, Ám sát bằng kịch độc
economy:
- Hợp đồng ám sát
- Bán vật liệu từ Độc Long Tích (Da, máu, xương)
- Cung cấp thú cưỡi độc cho ma đạo
arcs:
  - arc: 1
    status: Hoạt động mạnh
    rank: Hạng Nhì
    leader: Bảo Chủ Độc Nhãn
    population: 1500
    territory:
      - Núi Độc Long
      - Khe Nứt Tử Vong (Trạm gác)
    assets:
      - name: Đàn Độc Long Tích khổng lồ
        type: Tài Nguyên
      - name: Độc Long Đỉnh
        type: Công Trình
      - name: Long Lân Giáp
        type: Pháp Bảo
    stats: [2500, 2000, 3000, 1500, 3500, 2200]
    divisions:
      - name: Long Ảnh Đội
        role: Sát thủ cưỡi rồng và lực lượng phản ứng nhanh
        headcount:
          hoi_truong: 0
          pho_hoi_truong: 1
          thanh_vien: 100
          tong_quan: 10
        members:
          - character: "[Thống Lĩnh Long Ảnh]"
            position: Đội Trưởng
            cultivation: Nguyên Anh Sơ Kỳ
            placeholder: true
      - name: Phục Thú Viện
        role: Thuần hóa và lai tạo Độc Long Tích
        headcount:
          hoi_truong: 0
          pho_hoi_truong: 1
          thanh_vien: 50
          tong_quan: 5
        members:
          - character: "[Lão Nhân Phục Thú]"
            position: Viện Chủ
            cultivation: Kim Đan Đỉnh Phong
            placeholder: true
    relationships:
      - faction: Quỷ Thị Nam Cương
        description: Đối tác kinh doanh lâu đời, cung cấp hàng hóa độc quyền.
        diplomacy:
          lien_minh: 40
          tin: 60
          uy_hiep: 0
          thuong_mai: 90
          on_oan: 0
          le_thuoc: 0
      - faction: Vạn Độc Môn
        description: Cạnh tranh tài nguyên và địa bàn luyện độc tại Nam Cương.
        diplomacy:
          lien_minh: -20
          tin: -30
          uy_hiep: 50
          thuong_mai: 20
          on_oan: -40
          le_thuoc: 0
---

# ĐỘC LONG BẢO (毒龙堡)

## I. Tổng Quan (总览)
Độc Long Bảo là một tổ chức vũ trang đặc thù nằm ở ranh giới giữa ma đạo và trung lập, chuyên về nghệ thuật ám sát và điều khiển yêu thú. Pháo đài này nổi tiếng với việc biến loài Độc Long Tích tàn bạo thành những vũ khí chiến tranh di động, khiến họ trở thành một thế lực đáng gờm tại Nam Cương.

## II. Địa Lý & Tài Nguyên (地理与 tài nguyên)
Tọa lạc trên vách núi dựng đứng của Núi Độc Long, nơi chướng khí quanh năm không tan. Địa hình hiểm trở này là môi trường sống lý tưởng của Độc Long Tích. Bảo sở hữu các hang động tự nhiên được cải tạo thành chuồng trại khổng lồ và các lò luyện độc dược chiết xuất trực tiếp từ hơi thở của rồng đất.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
Đề cao sự sinh tồn và cộng sinh với yêu thú. Đệ tử Độc Long Bảo tin rằng chỉ có nọc độc và sức mạnh mới mang lại sự an toàn tuyệt đối. Họ có văn hóa đeo mặt nạ xương rồng và xăm hình vảy rồng lên cơ thể như một biểu tượng của địa vị và khả năng kháng độc.

## IV. Cơ Cấu Tổ Chức (组织结构)
```mermaid
graph TD
    BC[Bảo Chủ: Độc Nhãn] --> LTL[Long Trưởng Lão]
    LTL --> LAĐ[Long Ảnh Đội]
    LTL --> PTV[Phục Thú Viện]
    LTL --> DĐ[Độc Đường]
    LAĐ --> ST[Sát Thủ]
    PTV --> THS[Thuần Thú Sư]
    DĐ --> DSU[Dược Sư]
```

## V. Công Pháp & Trận Pháp (功法与阵法)
- **Công Pháp:** *Độc Long Thần Phục Quyết* (Điều khiển thú), *Vạn Độc Xuyên Tâm Thuật* (Ám sát).
- **Trận Pháp:** *Độc Sương Phục Kích Trận* - trận pháp phối hợp giữa người và thú trong môi trường sương mù, tăng cường khả năng ẩn nấp và sát thương độc hệ.

## VI. Đặc Sản Môn Phái (门派特产)
- **Độc Long Huyết:** Máu rồng dùng để nung nấu vũ khí hoặc pha chế thuốc tăng cường thể chất ngắn hạn.
- **Long Lân Giáp:** Giáp trụ làm từ vảy Độc Long Tích, cực kỳ nhẹ và có khả năng miễn nhiễm hầu hết các loại độc tố thông thường.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Độc Long Bảo:** Pháo đài đá kiên cố gắn liền với vách núi.
- **Hố Độc Tập Sự:** Nơi rèn luyện khả năng sinh tồn của các đệ tử mới bằng cách thả họ vào hang rết và rắn độc.

## VIII. Kinh Tế (经济)
Kinh tế dựa trên việc thực hiện các hợp đồng ám sát bí mật cho các thế lực ma đạo và việc bán các bộ phận quý giá của Độc Long Tích (da, máu, răng). Họ cũng là nhà cung cấp thú cưỡi chiến đấu hàng đầu cho những kẻ có đủ tài lực.

## IX. Lịch Sử Tóm Tắt (简史)
Được sáng lập bởi Độc Long Lão Nhân, một tu sĩ bị hãm hại và bị ném xuống vực sâu núi Độc Long. Ông không những không chết mà còn ngộ ra cách thuần phục bầy rồng đất tại đây, dùng chúng để quay lại báo thù và lập nên Độc Long Bảo.

## X. Giai Thoại & Bí Mật (轶 sự与秘密)
Đồn rằng sâu trong lòng núi có một con "Độc Long Vương" thực thụ từ thời Thái Cổ đang ngủ say, và hơi thở của nó chính là nguồn gốc của toàn bộ chướng khí tại Nam Cương.

## XI. Quan Hệ Thế Lực (势力关系)
```mermaid
graph LR
    DLB[Độc Long Bảo] -- Giao dịch -- QTNC[Quỷ Thị Nam Cương]
    DLB -- Đối đầu -- VDM[Vạn Độc Môn]
    DLB -- Thuê mướn -- CUMT[Cửu U Ma Tông]
```
