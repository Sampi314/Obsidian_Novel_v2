---
type: faction
name: Bắc Hải Cự Yêu Hang
hantu: 北海巨妖穴
faction_type: Liên Minh
alignment: -2
race: Hải Tộc (Kraken, Xà Tinh), Yêu Thú Biển
region: Bắc Băng
founded: Thượng Cổ Kỷ Nguyên
founder: Kraken Thủy Tổ
emblem: Xuc_Tu_Khong_Lo_Trong_Bang.png
specialty: Thể chất khổng lồ, Thủy hệ tàn phá, Ngủ đông vạn năm
economy:
- Thu thập cổ vật từ tàu đắm (Thụ động)
- Trao đổi vật liệu cơ thể yêu thú cho ma đạo
arcs:
  - arc: 1
    status: Đang ngủ đông / Bị quấy rối
    rank: Hạng Nhì (Tiềm năng Hạng Nhất)
    leader: Kraken Già
    population: 500 (Thực thể khổng lồ)
    territory:
      - Hang Cự Yêu (Biển Bắc Băng)
      - Vùng Biển Băng Trôi
    assets:
      - name: Hang đá ngầm vạn năm
        type: Công Trình
      - name: Trận pháp "Hàn Băng Thâm Uyên"
        type: Trận Pháp
      - name: Vảy Xà Tinh Thượng Cổ
        type: Tài Nguyên
    stats: [5000, 2000, 4500, 500, 4000, 2500]
    divisions:
      - name: Cự Yêu Đội
        role: Các thực thể khổng lồ bảo vệ hang ổ
        headcount:
          minh_chu: 0
          pho_minh_chu: 1
          truong_lao: 10
          su_gia: 0
          thanh_vien_phai: 100
        members:
          - character: Kraken Già
            position: Minh Chủ
            cultivation: Hóa Thần Hậu Kỳ
          - character: "[Đại Xà Thâm Hải]"
            position: Trưởng Lão
            cultivation: Hóa Thần Sơ Kỳ
            placeholder: true
    relationships:
      - faction: Hắc Hải Hải Tặc
        description: Thường xuyên bị quấy rối bởi hải tặc muốn tìm kiếm bảo vật tàu đắm xung quanh hang.
        diplomacy:
          lien_minh: -20
          tin: 10
          uy_hiep: 60
          thuong_mai: 20
          on_oan: -40
          le_thuoc: 0
      - faction: Cực Quang Thần Điện
        description: Tránh né sự chú ý, thỉnh thoảng bị thần điện coi là quái vật cần thanh tẩy.
        diplomacy:
          lien_minh: -100
          tin: -100
          uy_hiep: 80
          thuong_mai: -100
          on_oan: -100
          le_thuoc: 0
---

# BẮC HẢI CỰ YÊU HANG (北海巨妖穴)

## I. Tổng Quan (总览)
Bắc Hải Cự Yêu Hang là một tổ hợp các hang động băng giá nằm tại ranh giới giữa biển Bắc Băng và Vô Tận Hải. Đây không phải là một thế lực chính trị có tổ chức chặt chẽ, mà là một "thánh địa ngủ đông" của những loài yêu thú biển khổng lồ nhất thế giới (Kraken, Xà Tinh, Kình Ngư Thượng Cổ). Dù không chủ động tham gia tranh đấu, nhưng sự tồn tại của chúng là một lá chắn tự nhiên ngăn chặn mọi hành trình vượt biển phương Bắc.

## II. Địa Lý & Tài Nguyên (地理 với tài nguyên)
Trụ sở chính là hệ thống hang đá ngầm khổng lồ nằm sâu dưới các tảng băng trôi vĩnh cửu. Nơi đây tích tụ linh khí hàn băng cực kỳ đậm đặc, giúp các cự yêu duy trì trạng thái ngủ đông kéo dài hàng ngàn năm. Tài nguyên chính là những mảnh vảy, xương cốt và nội đan của các loài thú cổ đại đã chết, cùng với vô số cổ vật từ những con tàu bị bão biển đánh chìm.

## III. Văn Hóa & Tín Ngưỡng (文化 với信仰)
Tôn thờ bản năng và sự tĩnh lặng của đại dương. Các cự yêu có một mối liên kết tâm linh lỏng lẻo thông qua tiếng sóng âm biển sâu. Họ coi hang ổ là vùng đất thánh và mọi sự xâm nhập đều bị coi là hành vi thách thức cần phải trừng phạt bằng sự hủy diệt diện rộng.

## IV. Cơ Cấu Tổ Chức (组织结构)
```mermaid
graph TD
    KTTZ[Kraken Thủy Tổ - Thần Thoại] --> KG[Kraken Già - Minh Chủ]
    KG --> HDCY[Hội Đồng Cự Yêu]
    HDCY --> CYĐ[Cự Yêu Đội]
    HDCY --> XTĐ[Xà Tinh Đội]
    CYĐ --> KRAKEN[Kraken Con]
    XTĐ --> DAX[Đại Xà]
```

## V. Công Pháp & Trận Pháp (功法 với阵法)
- **Công Pháp:** Không có công pháp tu luyện nhân tạo, sức mạnh đến từ *Huyết Mạch Thượng Cổ* và khả năng thao túng nước lạnh giá.
- **Trận Pháp:** *Hàn Băng Thâm Uyên Trận* - một trận pháp tự nhiên được cường hóa bởi ý chí của các cự yêu, biến vùng biển xung quanh thành một máy nghiền băng khổng lồ, bóp nát mọi chiến hạm.

## VI. Đặc Sản Môn Phái (门派特产)
- **Vảy Kraken:** Loại vật liệu cực bền, có khả năng kháng lại mọi loại đòn tấn công thủy hệ.
- **Băng Tinh Hải Tủy:** Tinh thể hình thành từ hơi thở của cự yêu, chứa đựng năng lượng hàn băng tinh thuần nhất thế giới.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Vạn Niên Băng Hang:** Những khoang rỗng khổng lồ dưới đáy biển băng dùng làm nơi trú ngụ.
- **Nghĩa Địa Tàu Đắm:** Khu vực xung quanh hang ổ chứa đựng xác của hàng ngàn con tàu từ nhiều thời đại.

## VIII. Kinh Tế (経済)
Kinh tế mang tính thụ động. Thỉnh thoảng, các thế lực ma đạo gan dạ (như Vực Thẳm Ma Cung) sẽ mạo hiểm đến đây để nhặt những mảnh vật liệu do cự yêu thải ra hoặc trao đổi các linh hồn tươi sống để lấy bảo vật tàu đắm.

## IX. Lịch Sử Tóm Tắt (简史)
Được hình thành ngay sau khi kỷ nguyên Thái Cổ kết thúc, khi các loài quái vật khổng lồ bị xua đuổi khỏi các vùng biển nông của Nhân Tộc và Long Tộc. Chúng tìm thấy sự an toàn trong bóng tối lạnh giá của phương Bắc và dần dần biến nơi này thành sào huyệt bất khả xâm phạm.

## X. Giai Thoại & Bí Mật (轶 sự với bí mật)
Tương truyền Kraken Già thực chất là một phần xúc tu của Kraken Thủy Tổ bị đứt ra và đã tự phát triển thành một thực thể độc lập có trí tuệ.

## XI. Quan Hệ Thế Lực (势力关系)
```mermaid
graph LR
    BHCYH[Bắc Hải Cự Yêu Hang] -- Bị quấy rối -- HHHT[Hắc Hải Hải Tặc]
    BHCYH -- Đối địch -- CQTĐ[Cực Quang Thần Điện]
    BHCYH -- Giao dịch -- VTMC[Vực Thẳm Ma Cung]
    BHCYH -- Tránh né -- LC[Long Cung]
```
