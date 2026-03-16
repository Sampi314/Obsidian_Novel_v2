---
type: faction
name: Cực Quang Thần Điện
hantu: 极光神殿
faction_type: Giáo Phái
alignment: -2
race: Băng Tộc thuần huyết
region: Bắc Băng
founded: Trung Cổ Kỷ Nguyên
founder: Đại Tế Tư Ánh Sáng
emblem: Anh_Sang_Cuc_Quang_Va_Thap_Bang.png
specialty: Quang Tu Băng Giá, Ảo ảnh ánh sáng khúc xạ, Thiêu đốt linh hồn bằng ánh sáng lạnh
economy:
- Thu thuế tín ngưỡng từ các bộ lạc Băng Tộc
- Khai thác linh thạch quang hệ biển băng
- Bán các loại bùa chú "Thần Lực Cực Quang"
arcs:
  - arc: 1
    status: Đang bành trướng tín ngưỡng
    rank: Hạng Nhì (Tiềm lực Hạng Nhất)
    leader: Thánh Nữ Cực Quang
    population: 10000 (Linh mục & Chiến binh)
    territory:
      - Vùng cực Bắc (Bắc Băng)
      - Thung lũng Ánh Sáng Vĩnh Cửu
    assets:
      - name: Cực Quang Bảo Tháp
        type: Công Trình
      - name: Trận pháp "Quang Ảnh Vô Hình"
        type: Trận Pháp
      - name: Cực Quang Trượng
        type: Pháp Bảo
    stats: [4500, 3500, 4000, 8000, 3000, 4800]
    divisions:
      - name: Hiệp Sĩ Băng Lăng
        role: Lực lượng hộ pháp và chiến đấu bảo vệ Thần Điện
        headcount:
          minh_chu: 0
          pho_minh_chu: 1
          truong_lao: 10
          su_gia: 50
          thanh_vien_phai: 2000
        members:
          - character: "[Thống Lĩnh Băng Lăng]"
            position: Tướng Quân
            cultivation: Nguyên Anh Hậu Kỳ
            placeholder: true
      - name: Tế Tư Viện
        role: Thực hiện nghi lễ tế tự và truyền bá giáo lý cuồng tín
        headcount:
          minh_chu: 0
          pho_minh_chu: 3
          truong_lao: 20
          su_gia: 100
          thanh_vien_phai: 500
        members:
          - character: "[Đại Tế Tư Ánh Sáng]"
            position: Viện Chủ
            cultivation: Nguyên Anh Viên Mãn
            placeholder: true
    relationships:
      - faction: Huyền Băng Cung
        description: Kẻ thù truyền kiếp, tranh giành địa vị thống trị đức tin của Băng Tộc.
        diplomacy:
          lien_minh: -100
          tin: -100
          uy_hiep: 90
          thuong_mai: -100
          on_oan: -100
          le_thuoc: 0
      - faction: Sương Ma Uyển
        description: Đối địch, coi sương ma là sự báng bổ đối với ánh sáng thần thánh.
        diplomacy:
          lien_minh: -80
          tin: -90
          uy_hiep: 70
          thuong_mai: -100
          on_oan: -90
          le_thuoc: 0
---

# CỰC QUANG THẦN ĐIỆN (极光神殿)

## I. Tổng Quan (总览)
Cực Quang Thần Điện là thế lực tôn giáo cuồng tín nhất vùng Bắc Băng, ngự trị tại vĩ độ cao nhất nơi ánh sáng cực quang rực rỡ nhất thế giới. Họ tin rằng cực quang là ý chí của một vị thần ánh sáng cổ đại và nhiệm vụ của họ là thanh lọc thế gian bằng ánh sáng lạnh giá. Với sự kết hợp giữa kỹ thuật quang tu và băng hệ công pháp, thần điện là một đối trọng đáng sợ đối với Huyền Băng Cung, thường xuyên sử dụng các biện pháp cực đoan để bành trướng tầm ảnh hưởng.

## II. Địa Lý & Tài Nguyên (地理 với tài nguyên)
Trụ sở chính nằm tại Thung lũng Ánh Sáng Vĩnh Cửu, một khu vực quanh năm được chiếu sáng bởi hiện tượng cực quang ma thuật. Thần điện kiểm soát những mỏ "Quang Linh Thạch" chỉ hình thành dưới sự tác động lâu dài của ánh sáng cực cao và nhiệt độ cực thấp. Nơi đây sở hữu môi trường linh khí quang hệ tinh thuần nhất, giúp tu sĩ đột phá thần thức nhanh chóng nhưng cũng dễ dẫn đến tâm tính lạnh lùng, vô cảm.

## III. Văn Hóa & Tín Ngưỡng (文化 với信仰)
Tôn thờ Thánh Nữ Cực Quang như hiện thân sống của thần linh. Cư dân tin rằng cảm xúc là rào cản đối với sự giác ngộ ánh sáng. Văn hóa thần điện mang đậm tính kỷ luật thép và sự phục tùng tuyệt đối. Nghi lễ quan trọng nhất là "Tế Tự Ánh Sáng", nơi các tín đồ hiến tế linh lực và máu băng để duy trì độ rực rỡ của Cực Quang Bảo Tháp.

## IV. Cơ Cấu Tổ Chức (组织结构)
```mermaid
graph TD
    TNCD[Thánh Nữ Cực Quang - Lãnh Đạo Tối Cao] --> ĐTS[Đại Tế Tư Ánh Sáng - Điều Hành]
    ĐTS --> HDTL[Hội Đồng Linh Mục]
    HDTL --> HSBL[Hiệp Sĩ Băng Lăng]
    HDTL --> TSV[Tế Tư Viện]
    HDTL --> CDĐ[Chấp Đạo Đội]
    HSBL --> CB[Chiến Binh Ánh Sáng]
    TSV --> LM[Linh Mục]
    CDĐ --> MT[Mật Thám Tín Ngưỡng]
```

## V. Công Pháp & Trận Pháp (功法 với阵法)
- **Công Pháp:** *Cực Quang Xuyên Tâm Quyết* (Tấn công xuyên thấu), *Đại Băng Chú* (Phong ấn diện rộng).
- **Trận Pháp:** *Quang Ảnh Vô Hình Trận* - trận pháp sử dụng sự khúc xạ ánh sáng trên các tinh thể băng khổng lồ để che giấu hoàn toàn thần điện hoặc tạo ra hàng vạn phân thân ảo ảnh của quân đội, khiến kẻ thù không thể phân biệt thật giả.

## VI. Đặc Sản Môn Phái (门派特产)
- **Quang Băng Châm:** Loại ám khí tỏa ra ánh sáng chói lòa khiến mục tiêu bị mù tạm thời và đóng băng linh mạch ngay khi chạm vào.
- **Thần Lực Linh Phù:** Linh phù chứa đựng năng lượng cực quang, dùng để tăng cường uy lực cho các chiêu thức quang hệ.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Cực Quang Bảo Tháp:** Tòa tháp pha lê cao vút, trung tâm thu phát và khuếch đại năng lượng cực quang.
- **Quảng Trường Thanh Tẩy:** Nơi thực hiện các cuộc hành hình và thanh lọc những kẻ bị coi là dị giáo.

## VIII. Kinh Tế (経済)
Kinh tế dựa trên hệ thống thuế tín ngưỡng bắt buộc đối với các bộ lạc dưới quyền bảo hộ. Thần điện cũng nắm giữ thị trường linh thạch quang hệ cao cấp và các loại vật phẩm tâm linh. Họ thường xuyên tổ chức các cuộc viễn chinh "thánh chiến" để chiếm đoạt tài nguyên từ các vùng đất lân cận.

## IX. Lịch Sử Tóm Tắt (简史)
Sáng lập bởi Đại Tế Tư Ánh Sáng đầu tiên, người đã tuyên bố nhận được thiên mệnh từ bầu trời Bắc Băng sau khi một trận đại dịch quét qua vùng cực. Thần điện đã nhanh chóng trở thành một thế lực chính trị mạnh mẽ, cạnh tranh quyết liệt với Huyền Băng Cung để giành quyền lãnh đạo tinh thần của toàn bộ Băng Tộc.

## X. Giai Thoại & Bí Mật (轶 sự với bí mật)
Tương truyền Thánh Nữ Cực Quang không bao giờ già đi và cơ thể nàng thực chất được cấu tạo từ ánh sáng tinh thuần, không có máu thịt như con người bình thường.

## XI. Quan Hệ Thế Lực (势力关系)
```mermaid
graph LR
    CQTĐ[Cực Quang Thần Điện] -- Tử địch -- HBC[Huyền Băng Cung]
    CQTĐ -- Đối địch -- SMU[Sương Ma Uyển]
    CQTĐ -- Thao túng -- BLBL[Băng Lang Bộ Lạc]
    CQTĐ -- Cảnh giác -- TAM[Thái Ất Môn]
```
