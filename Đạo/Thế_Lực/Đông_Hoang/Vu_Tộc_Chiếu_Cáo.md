---
type: faction
name: Vu Tộc Tế Đàn
hantu: 巫族祭坛
faction_type: Bộ Lạc
alignment: 0
race: Lai Cự Tộc, Nhân Tộc
region: Đông Hoang
founded: Thái Cổ Kỷ Nguyên
founder: Đại Vu Tổ
emblem: Ban_Tay_Da_Ran_Doc.png
specialty: Vu Thuật Luyện Thể, Độc Dịch Cường Hóa, Giao tiếp linh hồn tổ tiên
economy:
- Săn bắn yêu thú lấy nguyên liệu
- Khai thác dược thảo độc tính cao
- Trao đổi vật phẩm cổ vật
arcs:
  - arc: 1
    status: Cô lập bảo thủ
    rank: Hạng Ba
    leader: Đại Tế Tư Vu Huyết
    population: 3000
    territory:
      - Vu Độc Sơn Mạch
      - Tế Đàn Thượng Cổ
    assets:
      - name: Vạn Độc Trì
        type: Tài Nguyên
      - name: Cự Thạch Đồ Đằng
        type: Công Trình
      - name: Rìu Đá Cự Thần
        type: Pháp Bảo
    stats: [2000, 1000, 1500, 3000, 2500, 1200]
    divisions:
      - name: Chiến Vu Đội
        role: Lực lượng chiến binh bảo vệ bộ lạc và săn bắn
        headcount:
          truong_lao: 2
          chien_binh: 500
          dan_thuong: 1000
        members:
          - character: "[Thống Lĩnh Vu Chiến]"
            position: Tướng Quân
            cultivation: Kim Đan Viên Mãn
            placeholder: true
      - name: Tế Tư Viện
        role: Thực hiện nghi lễ, bói toán và điều chế độc dược
        headcount:
          truong_lao: 5
          chien_binh: 50
          dan_thuong: 200
        members:
          - character: Vu Huyết
            position: Đại Tế Tư
            cultivation: Nguyên Anh Trung Kỳ
          - character: "[Vu Chúc Cổ]"
            position: Trưởng Lão
            cultivation: Kim Đan Sơ Kỳ
            placeholder: true
    relationships:
      - faction: Thiên Yêu Đình
        description: Giao hảo lâu đời, cùng chia sẻ không gian sống tại Đông Hoang.
        diplomacy:
          lien_minh: 40
          tin: 50
          uy_hiep: 0
          thuong_mai: 30
          on_oan: 0
          le_thuoc: 0
      - faction: Vạn Độc Môn
        description: Đối địch gay gắt do Vạn Độc Môn thường xuyên săn lùng người của bộ lạc để thí nghiệm.
        diplomacy:
          lien_minh: -50
          tin: -80
          uy_hiep: 60
          thuong_mai: -40
          on_oan: -100
          le_thuoc: 0
---

# VU TỘC TẾ ĐÀN (巫族祭坛)

## I. Tổng Quan (总览)
Vu Tộc Tế Đàn là một bộ lạc cổ xưa và huyền bí, giữ gìn những phương pháp tu luyện hoang sơ nhất từ thời Thái Cổ. Họ từ chối linh khí tinh thuần của tiên đạo, thay vào đó tập trung vào việc cường hóa nhục thân bằng nọc độc và sức mạnh của đất đá. Bộ lạc này sống tách biệt và chỉ hành động khi vùng đất thiêng của họ bị xâm phạm.

## II. Địa Lý & Tài Nguyên (地理 với tài nguyên)
Trụ sở chính nằm sâu trong dãy Vu Độc Sơn Mạch, một khu vực hiểm trở với sương mù độc bao phủ quanh năm. Bộ lạc sở hữu "Vạn Độc Trì" - một hồ nước tự nhiên tích tụ nọc độc của hàng vạn loài côn trùng và bò sát qua hàng nghìn năm, là tài nguyên quý giá nhất để rèn luyện "Vu Thể".

## III. Văn Hóa & Tín Ngưỡng (文化 với信仰)
Tôn thờ Đại Vu Tổ và các linh hồn tổ tiên. Họ tin rằng mỗi vết xăm trên cơ thể là một lần giao tiếp với thần linh và mỗi vết sẹo là một huân chương danh dự. Văn hóa của họ mang đậm tính nghi lễ, với các vũ điệu tế đàn và tiếng trống da thú vang vọng trong những đêm trăng máu.

## IV. Cơ Cấu Tổ Chức (组织结构)
```mermaid
graph TD
    DVT[Đại Vu Tổ - Thủy Tổ] --> ĐTS[Đại Tế Tư: Vu Huyết]
    ĐTS --> HDTL[Hội Đồng Vu Chúc]
    HDTL --> CVĐ[Chiến Vu Đội]
    HDTL --> TSV[Tế Tư Viện]
    HDTL --> ĐTĐ[Độc Thảo Đường]
    CVĐ --> CB[Chiến Binh]
    TSV --> VC[Vu Chúc]
    ĐTĐ --> TS[Thợ Săn]
```

## V. Công Pháp & Trận Pháp (功法与阵法)
- **Công Pháp:** *Vu Huyết Thần Thể* (Luyện thể ngoại công), *Đại Địa Trọng Kích* (Sát thương vật lý mạnh).
- **Trận Pháp:** *Vu Độc Đồ Đằng Trận* - trận pháp phòng thủ dựa trên các cột đá khắc phù văn, có khả năng phun ra độc khí và làm suy yếu linh lực kẻ thù.

## VI. Đặc Sản Môn Phái (门派特产)
- **Vu Độc Cao:** Loại cao bôi ngoài da giúp tăng cường độ cứng cáp và khả năng kháng độc.
- **Xương Thú Phù:** Những mảnh xương yêu thú được khắc phù văn, dùng để triệu hồi linh hồn chiến thú trợ chiến.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Tế Đàn Thượng Cổ:** Nơi diễn ra các nghi lễ quan trọng và là điểm tập trung năng lượng của toàn bộ lạc.
- **Hang Động Luyện Thể:** Hệ thống hang động chứa đầy độc vật dành cho việc rèn luyện đệ tử.

## VIII. Kinh Tế (经济)
Kinh tế tự cung tự cấp là chính. Họ thỉnh thoảng trao đổi các loại dược liệu độc hiếm và cổ vật khai quật được cho những thương nhân gan dạ để lấy các vật dụng sinh hoạt từ thế giới bên ngoài.

## IX. Lịch Sử Tóm Tắt (简史)
Là hậu duệ của những chiến binh Cự Tộc và Nhân Tộc đã sát cánh bên nhau trong cuộc chiến Thái Cổ. Sau khi chiến tranh kết thúc, họ chọn ở lại vùng núi độc này để canh giữ bí mật của tổ tiên và duy trì dòng máu lai đặc biệt của mình.

## X. Giai Thoại & Bí Mật (轶 sự với bí mật)
Tương truyền dưới lòng Tế Đàn Thượng Cổ có chôn cất "Trái Tim Của Đất", thứ cung cấp sức mạnh luyện thể vô hạn cho những ai đủ can đảm để dung hợp với nó.

## XI. Quan Hệ Thế Lực (势力关系)
```mermaid
graph LR
    VTTĐ[Vu Tộc Tế Đàn] -- Tôn trọng -- TYD[Thiên Yêu Đình]
    VTTĐ -- Tử địch -- VDM[Vạn Độc Môn]
    VTTĐ -- Cảnh giác -- TAM[Thái Ất Môn]
```
