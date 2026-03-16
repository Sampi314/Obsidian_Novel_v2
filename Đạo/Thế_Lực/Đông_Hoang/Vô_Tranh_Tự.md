---
type: faction
name: Vô Tranh Tự
hantu: 无争寺
faction_type: Tự Viện
alignment: 10
race: Nhân Tộc
region: Đông Hoang
founded: Thượng Cổ Kỷ Nguyên
founder: Vô Tranh Thiền Sư
emblem: Bong_Truc_Va_Chu_Van.png
specialty: Phật Pháp Vô Biên, Kim Cương Bất Hoại, Tịnh hóa oan hồn
economy:
- Công đức từ thiện nam tín nữ
- Bán các loại kinh văn và vật phẩm định tâm
- Dịch vụ tịnh hóa và siêu độ linh hồn
arcs:
  - arc: 1
    status: Đóng cửa đọc kinh
    rank: Hạng Nhất
    leader: Phương Trượng Vô Nhai
    population: 10000
    territory:
      - Rừng Trúc Thiên Trụ Sơn (Phía Tây)
      - Chùa Vô Tranh
    assets:
      - name: Tàng Kinh Các Thượng Cổ
        type: Công Trình
      - name: Trận pháp "Bát Nhã Tâm Giới"
        type: Trận Pháp
      - name: Xá Lợi Tử (Chấn tự chi bảo)
        type: Pháp Bảo
    stats: [9000, 15000, 12000, 8000, 10000, 14000]
    divisions:
      - name: La Hán Đường
        role: Võ tăng thực chiến, bảo vệ tự viện và hàng yêu phục ma
        headcount:
          thai_thuong: 2
          ho_phap: 10
          tang_lu: 500
          sa_di: 1000
          cu_si: 2000
        members:
          - character: "[Thống Lĩnh La Hán]"
            position: Thủ Tọa
            cultivation: Hóa Thần Sơ Kỳ
            placeholder: true
      - name: Đạt Ma Viện
        role: Nghiên cứu phật pháp thâm sâu và giam giữ tà ma
        headcount:
          thai_thuong: 5
          ho_phap: 2
          tang_lu: 200
          sa_di: 500
          cu_si: 1000
        members:
          - character: Vô Nhai
            position: Phương Trượng
            cultivation: Hóa Thần Hậu Kỳ
    relationships:
      - faction: Huyết Ma Tông
        description: Tử địch, từng dẫn đầu cuộc chiến trấn áp ma tu huyết đạo.
        diplomacy:
          lien_minh: -100
          tin: -100
          uy_hiep: 90
          thuong_mai: -100
          on_oan: -100
          le_thuoc: 0
      - faction: Kim Sa Tự
        description: Đồng môn phật giáo, cùng chia sẻ lý tưởng phổ độ chúng sinh.
        diplomacy:
          lien_minh: 80
          tin: 100
          uy_hiep: 0
          thuong_mai: 50
          on_oan: 0
          le_thuoc: 0
---

# VÔ TRANH TỰ (无争寺)

## I. Tổng Quan (总览)
Vô Tranh Tự là thánh địa Phật giáo uy nghiêm nhất Cố Nguyên Giới, nổi tiếng với triết lý từ bi và sự tĩnh lặng tuyệt đối. Khác với sự khổ hạnh của Kim Sa Tự, Vô Tranh Tự tập trung vào việc tu luyện tâm thức và tịnh hóa thế gian. Tự viện là nơi lưu giữ những bộ kinh phật thượng cổ quý giá nhất và là lá chắn tinh thần vững chắc cho nhân loại trước sự trỗi dậy của các thế lực tà ác.

## II. Địa Lý & Tài Nguyên (地理 với tài nguyên)
Tọa lạc trong một rừng trúc xanh mướt quanh năm sương khói bao phủ ở phía Tây dãy núi Thiên Trụ Sơn. Nơi đây có môi trường linh khí vô cùng hòa nhã, phù hợp cho việc thiền định lâu dài. Tài nguyên chính của tự viện là các mạch "Phật Quang Thạch" - loại đá có khả năng tự phát sáng và xua đuổi ma khí, cùng với tàng kinh các chứa đựng hàng vạn điển tịch tu tâm.

## III. Văn Hóa & Tín Ngưỡng (文化 với信仰)
Tôn thờ Phật Tổ và triết lý "Vạn Pháp Giai Không, Vô Tranh Thị Đạo". Tăng lữ tại đây sống cuộc đời thanh bạch, ăn chay niệm phật và không tham gia vào các cuộc tranh giành quyền lực thế tục. Họ đề cao sự nhẫn nhịn nhưng cũng cực kỳ kiên quyết khi đối mặt với tà ma ngoại đạo đang gây hại cho chúng sinh.

## IV. Cơ Cấu Tổ Chức (组织结构)
```mermaid
graph TD
    PT[Phương Trượng: Vô Nhai] --> HDTL[Hội Đồng Trưởng Lão]
    HDTL --> LHĐ[La Hán Đường]
    HDTL --> ĐMV[Đạt Ma Viện]
    HDTL --> PHĐ[Phổ Hiền Đường]
    LHĐ --> VT[Võ Tăng]
    ĐMV --> TL[Tăng Lữ Nghiên Cứu]
    PHĐ --> HG[Hành Giả]
```

## V. Công Pháp & Trận Pháp (功法 với阵法)
- **Công Pháp:** *Kim Cương Bất Hoại Thể* (Phòng ngự tuyệt đối), *Đại Bi Chú* (Âm công tịnh hóa tâm hồn).
- **Trận Pháp:** *Bát Nhã Tâm Giới Trận* - trận pháp bao phủ tự viện, có khả năng phản chiếu nội tâm kẻ thù, khiến những kẻ mang tâm địa tà ác tự rơi vào mê cung của chính mình.

## VI. Đặc Sản Môn Phái (门派特产)
- **Vô Tranh Trà:** Loại trà mọc trong rừng trúc, giúp tu sĩ bình ổn tâm ma và tăng cường thần thức.
- **Phật Châu Định Tâm:** Chuỗi hạt đã được trì chú, có tác dụng hộ thân và xua đuổi tà mị cực tốt.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Đại Hùng Bảo Điện:** Nơi đặt pho tượng Phật tổ khổng lồ dát vàng, trung tâm của mọi nghi lễ.
- **Vạn Phật Động:** Hệ thống hang động chứa hàng vạn bức tượng Phật được tạc trực tiếp vào vách đá Thiên Trụ Sơn.

## VIII. Kinh Tế (経済)
Nguồn thu chủ yếu đến từ sự quyên góp tự nguyện của hàng triệu tín đồ khắp lục địa. Tự viện cũng cung cấp các loại vật phẩm tâm linh và dịch vụ tịnh hóa linh hồn cho những gia tộc lớn gặp phải các vấn đề về oan hồn hoặc tà thuật.

## IX. Lịch Sử Tóm Tắt (简史)
Sáng lập bởi Vô Tranh Thiền Sư vào thời Thượng Cổ, người đã dùng phật pháp để cảm hóa một con ma long đang tàn phá thế gian. Tự viện đã trải qua hàng nghìn năm đứng vững như một biểu tượng của chính đạo, từng dẫn đầu nhiều cuộc thập tự chinh tiêu diệt ma đầu nhưng sau đó lại rút về ẩn thế đọc kinh.

## X. Giai Thoại & Bí Mật (轶 sự với bí mật)
Tương truyền trong Đạt Ma Viện có giam giữ một "Ma Quân" từ thời Thái Cổ không thể tiêu diệt, và các vị cao tăng phải thay phiên nhau tụng kinh vạn năm để trấn áp hắn.

## XI. Quan Hệ Thế Lực (势力关系)
```mermaid
graph LR
    VTT[Vô Tranh Tự] -- Tử địch -- HMT[Huyết Ma Tông]
    VTT -- Đồng môn -- KST[Kim Sa Tự]
    VTT -- Cố vấn -- DCHH[大乾皇朝]
    VTT -- Đối địch -- HHHT[Hắc Hải Hải Tặc]
```
