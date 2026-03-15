---
type: faction
name: Hải Thần Cung
hantu: 海神宫
faction_type: Tông Môn
alignment: 9
race: Hải Tộc (Đa chủng tộc)
region: Vô Tận Hải
founded: Kỷ Nguyên Khởi Nguyên
founder: Hải Thần Thủy Tổ
emblem: Dinh_Ba_Va_Tranh_Chau.png
specialty: Hải Thần Lộ, Vạn Thủy Quy Tông, Giao tiếp sóng âm biển sâu
economy:
- Thu thuế từ các bộ lạc hải tộc
- Khai thác linh thạch thủy hệ và trân châu biển sâu
- Bảo hộ các tuyến đường hàng hải quốc tế (Hợp pháp)
arcs:
  - arc: 1
    status: Thống trị tuyệt đối
    rank: Hạng Nhất (Siêu cấp)
    leader: Hải Đế đương nhiệm
    population: 1000000 (Binh lính và cư dân)
    territory:
      - Đáy biển Vô Tận Hải (1/3 diện tích)
      - Thủy Tinh Cung
    assets:
      - name: Hải Thần Cấm Địa
        type: Bí Cảnh
      - name: Trận pháp "Vạn Hải Triều Tịch"
        type: Trận Pháp
      - name: Hải Thần Đinh Ba
        type: Pháp Bảo
    stats: [15000, 12000, 13000, 10000, 11000, 14000]
    divisions:
      - name: Bát Đại Tướng Quân Phủ
        role: Thống lĩnh quân đội trấn giữ 8 phương biển
        headcount:
          thanh_chu: 1
          pho_thanh_chu: 8
          ve_binh: 500000
          quan_vien: 1000
          dan_cu: 0
        members:
          - character: "[Hải Đế]"
            position: Lãnh Đạo Tối Cao
            cultivation: Hóa Thần Hậu Kỳ
          - character: "[Đông Hải Đại Tướng]"
            position: Tướng Quân
            cultivation: Hóa Thần Sơ Kỳ
            placeholder: true
      - name: Tứ Đại Tế Tư Viện
        role: Thực hiện nghi lễ, bói toán và duy trì đức tin Hải Thần
        headcount:
          thanh_chu: 0
          pho_thanh_chu: 4
          ve_binh: 1000
          quan_vien: 500
          dan_cu: 5000
        members:
          - character: "[Đại Tế Tư Biển Cả]"
            position: Viện Chủ
            cultivation: Nguyên Anh Viên Mãn
            placeholder: true
    relationships:
      - faction: Long Cung
        description: Cạnh tranh quyền bá chủ đại dương, quan hệ căng thẳng.
        diplomacy:
          lien_minh: -30
          tin: 20
          uy_hiep: 70
          thuong_mai: 40
          on_oan: -60
          le_thuoc: 0
      - faction: Hắc Hải Hải Tặc
        description: Tử địch, thường xuyên vây quét các băng nhóm hải tặc.
        diplomacy:
          lien_minh: -100
          tin: -100
          uy_hiep: 90
          thuong_mai: -100
          on_oan: -100
          le_thuoc: 0
---

# HẢI THẦN CUNG (海神宫)

## I. Tổng Quan (总览)
Hải Thần Cung là thực thể chính trị và tôn giáo hùng mạnh nhất dưới lòng Vô Tận Hải, được coi là người bảo hộ chính thống của mọi cư dân biển. Với niềm tin tuyệt đối vào Hải Thần, cung điện này duy trì trật tự cho hàng triệu sinh linh và là lá chắn vững chắc chống lại những quái vật khổng lồ của đại dương. Hải Thần Cung đại diện cho sự uy nghiêm, chính nghĩa và sức mạnh vô tận của nước, giữ vai trò cân bằng khí vận cho toàn bộ hệ sinh thái biển sâu.

## II. Địa Lý & Tài Nguyên (地理 với tài nguyên)
Trụ sở chính là Thủy Tinh Cung, một tổ hợp kiến trúc lộng lẫy xây dựng từ pha lê tự nhiên nằm tại điểm sâu nhất và giàu linh khí nhất của Vô Tận Hải. Cung điện kiểm soát "Hải Thần Mạch" - mạch linh khí thủy hệ nguyên thủy, cùng với các khu vực bảo tồn trân châu linh thạch và san hô ma thuật quy mô lớn. Nơi đây còn có "Hải Thần Cấm Địa", nơi giam giữ những bí mật cổ đại về nguồn gốc của đại dương.

## III. Văn Hóa & Tín Ngưỡng (文化 với信仰)
Tôn thờ Hải Thần Thủy Tổ. Cư dân tin rằng biển cả là nguồn sống và mọi hành vi xúc phạm đến đại dương đều phải trả giá. Văn hóa Hải Thần Cung mang đậm tính tôn nghiêm, nghi lễ và lòng tự hào chủng tộc. Họ đề cao sự trung thành, lòng dũng cảm và khả năng phối hợp tập thể. Lễ hội "Triều Tịch Đại Điển" hàng năm là dịp để vạn dân hướng về Thủy Tinh Cung cầu nguyện bình an.

## IV. Cơ Cấu Tổ Chức (组织结构)
```mermaid
graph TD
    HTTT[Hải Thần Thủy Tổ - Thần Linh] --> HĐ[Hải Đế]
    HĐ --> TĐTT[Tứ Đại Tế Tư]
    HĐ --> BĐTQ[Bát Đại Tướng Quân]
    TĐTT --> LM[Linh Mục Biển]
    BĐTQ --> HTQ[Hải Tộc Quân]
    HTQ --> BT[Binh Tôm Tướng Cá]
```

## V. Công Pháp & Trận Pháp (功法 với阵法)
- **Công Pháp:** *Hải Thần Lộ* (Chuyển hóa nước thành linh lực tối cao), *Vạn Thủy Quy Tông* (Điều khiển dòng chảy diện rộng).
- **Trận Pháp:** *Vạn Hải Triều Tịch Trận* - trận pháp hộ môn siêu cấp, có khả năng điều khiển toàn bộ hải lưu của Vô Tận Hải để tạo ra những vòng xoáy khổng lồ nghiền nát bất kỳ hạm đội nào xâm lược.

## VI. Đặc Sản Môn Phái (门派特产)
- **Hải Thần Trân Châu:** Loại ngọc chứa đựng tinh hoa của đại dương, có tác dụng tăng cường tuổi thọ và kháng lại mọi loại độc tố nước.
- **Thủy Tinh Khải:** Bộ giáp làm từ pha lê biển sâu, cực kỳ bền chắc và giúp người mặc di chuyển nhanh gấp đôi dưới nước.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Thủy Tinh Cung:** Cung điện vòm khổng lồ rực rỡ ánh sáng linh lực.
- **Quảng Trường Hải Thần:** Nơi đặt pho tượng Hải Thần bằng vàng ròng cao hàng trăm trượng.

## VIII. Kinh Tế (経済)
Nền kinh tế vững mạnh dựa trên việc thu thuế và phí bảo hộ từ các bộ lạc hải tộc và thương thuyền. Họ cũng nắm giữ nguồn cung ứng ngọc trai linh khí và các dược liệu biển sâu quý giá cho đất liền. Hải Thần Cung là đơn vị điều tiết giá cả của các vật phẩm thủy hệ trên toàn thế giới.

## IX. Lịch Sử Tóm Tắt (简史)
Được thành lập từ thời kỳ Khởi Nguyên bởi vị Thần Nước đầu tiên để tập hợp các chủng tộc biển nhỏ bé chống lại sự tàn sát của các yêu quái biển cổ đại khổng lồ. Qua hàng triệu năm, Hải Thần Cung đã phát triển từ một liên minh tự vệ thành một đế chế hải dương không thể lay chuyển, chứng kiến sự hưng vong của hàng nghìn vương triều trên mặt đất.

## X. Giai Thoại & Bí Mật (轶 sự với bí mật)
Tương truyền dưới Hải Thần Cấm Địa có phong ấn trái tim của một vị thần ma cổ đại, và Hải Đế mỗi đời đều phải dùng linh hồn của mình để gia cố phong ấn này.

## XI. Quan Hệ Thế Lực (势力关系)
```mermaid
graph LR
    HTC[Hải Thần Cung] -- Cạnh tranh -- LC[Long Cung]
    HTC -- Tử địch -- HHHT[Hắc Hải Hải Tặc]
    HTC -- Bảo hộ -- SHĐQ[San Hô Đảo Quốc]
    HTC -- Trung lập -- DCHH[Đại Càn Hoàng Triều]
```
