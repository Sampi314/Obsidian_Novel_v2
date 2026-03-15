---
type: faction
name: Hoàng Sa Cổ Quốc
hantu: 黄沙古国
faction_type: Vương Quốc
alignment: -7
race: Nhân Tộc (Xác ướp), Thổ Ma
region: Tây Mạc
founded: Thái Cổ Kỷ Nguyên
founder: Hoàng Sa Đại Đế
emblem: Kim_Tu_Thap_Vo.png
specialty: Thao túng cát chết (Tử Sa), Thuật phong ấn linh hồn, Quân đoàn tượng đá
economy:
- Khai thác bảo vật từ lăng mộ cổ
- Chiếm đoạt linh hồn lữ khách
- Thu thập tài nguyên từ vùng đất chết
arcs:
  - arc: 1
    status: Đang thức tỉnh
    rank: Hạng Nhì
    leader: Hoàng Sa Quyền Trượng
    population: 5000
    territory:
      - Hoàng Sa Địa Cung
      - Vùng Sa Mạc Chết (Tây Mạc)
    assets:
      - name: Kim Tự Tháp Vĩnh Hằng
        type: Công Trình
      - name: Quân đoàn tượng đá
        type: Tài Nguyên
      - name: Trượng Hoàng Gia
        type: Pháp Bảo
    stats: [4500, 3000, 5000, 5000, 2500, 4800]
    divisions:
      - name: Sa Quỷ Quân
        role: Lực lượng bộ binh xác sống chủ lực
        headcount:
          vuong: 0
          dai_than: 1
          quan_vien: 10
          cam_ve: 1000
          dan: 2000
        members:
          - character: "[Sa Tướng Bất Tử]"
            position: Thống Lĩnh
            cultivation: Nguyên Anh Trung Kỳ
            placeholder: true
      - name: Tế Tư Các
        role: Duy trì trận pháp lăng mộ và hồi sinh binh lính
        headcount:
          vuong: 0
          dai_than: 5
          quan_vien: 20
          cam_ve: 50
          dan: 100
        members:
          - character: "[Đại Tế Tư Hoàng Sa]"
            position: Các Chủ
            cultivation: Nguyên Anh Hậu Kỳ
            placeholder: true
    relationships:
      - faction: Kim Sa Tự
        description: Thiên địch, linh khí thuần dương là khắc tinh của tử khí sa mạc.
        diplomacy:
          lien_minh: -100
          tin: -100
          uy_hiep: 80
          thuong_mai: -100
          on_oan: -100
          le_thuoc: 0
      - faction: Sa Tặc Liên Minh
        description: Thao túng ngầm, sử dụng sa tặc như nô lệ và tai mắt trên mặt đất.
        diplomacy:
          lien_minh: 20
          tin: 10
          uy_hiep: 90
          thuong_mai: 30
          on_oan: 0
          le_thuoc: 70
---

# HOÀNG SA CỔ QUỐC (黄沙古国)

## I. Tổng Quan (总览)
Hoàng Sa Cổ Quốc là một vương quốc xác sống (Undead) trỗi dậy từ đống đổ nát của kỷ nguyên Thái Cổ. Tọa lạc sâu dưới lòng cát Tây Mạc, thế lực này đại diện cho nỗi ám ảnh về một quá khứ huy hoàng muốn nuốt chửng hiện tại. Họ không chỉ là những chiến binh bất tử mà còn là những bậc thầy về tà thuật liên quan đến linh hồn và cát bụi.

## II. Địa Lý & Tài Nguyên (地理 với tài nguyên)
Trụ sở chính là Hoàng Sa Địa Cung, một mê cung khổng lồ gồm các lăng mộ, đền đài và thành quách chôn vùi dưới cồn cát. Nơi đây sở hữu "Tử Sa Mạch" - nguồn linh khí chết chóc cung cấp năng lượng cho quân đoàn xác sống và "Kim Tự Tháp Vĩnh Hằng" - trung tâm điều khiển khí vận của toàn vương quốc.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
Tôn thờ Hoàng Sa Đại Đế như một vị thần bất tử. Cư dân cổ quốc tin rằng sự sống chỉ là một giai đoạn tạm thời và cái chết mới là sự khởi đầu của vinh quang vĩnh cửu. Văn hóa của họ mang đậm màu sắc tang tóc, lễ nghi ướp xác và các cuộc hiến tế linh hồn.

## IV. Cơ Cấu Tổ Chức (组织结构)
```mermaid
graph TD
    HSDĐ[Hoàng Sa Đại Đế - Chủ Nhân] --> HSQT[Hoàng Sa Quyền Trượng - Nhiếp Chính]
    HSQT --> TTC[Tế Tư Các]
    HSQT --> SQK[Sa Quỷ Quân]
    HSQT --> KLKB[Khô Lâu Kỵ Binh]
    TTC --> PMS[Pháp Sư Xác Ướp]
    SQK --> ST[Sa Tướng]
    KLKB --> KB[Kỵ Binh]
```

## V. Công Pháp & Trận Pháp (功法与阵法)
- **Công Pháp:** *Hoàng Sa Nghịch Thiên Quyết* (Chống lại quy luật sinh tử), *Tử Sa Thực Hồn Thuật* (Ăn mòn linh hồn).
- **Trận Pháp:** *Hoàng Sa Thực Cốt Trận* - trận pháp bao trùm vùng sa mạc chết, khiến bất kỳ sinh vật sống nào đi vào đều bị hút cạn sinh cơ và biến thành một phần của cát bụi.

## VI. Đặc Sản Môn Phái (门派特产)
- **Tử Sa Châu:** Viên ngọc chứa đựng tử khí cực nồng, dùng để đầu độc linh mạch đối phương.
- **Băng Quấn Cổ Đại:** Loại vải được yểm bùa có khả năng phục hồi cơ thể xác sống và kháng lại các đòn tấn công vật lý.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Kim Tự Tháp Vĩnh Hằng:** Nơi ngự trị của Đại Đế và là trạm thu phát tín hiệu tâm linh cho quân đoàn.
- **Hầm Mộ Vô Tận:** Khu vực lưu trữ hàng triệu xác ướp binh lính đang chờ được đánh thức.

## VIII. Kinh Tế (经济)
Kinh tế mang tính chất chiếm đoạt. Họ thu thập các cổ vật thượng cổ từ chính các lăng mộ của mình và chiếm đoạt tài sản của những thương đoàn xấu số đi lạc. Họ không cần linh thạch thông thường mà cần "Linh Hồn Tinh Thạch" để duy trì sự tồn tại.

## IX. Lịch Sử Tóm Tắt (简史)
Vốn là đế quốc hùng mạnh nhất Tây Mạc thời Thái Cổ, bị diệt vong do một lời nguyền không gian khiến toàn bộ vương quốc bị chôn vùi trong một đêm. Hàng vạn năm sau, khi phong ấn suy yếu, ý chí của Hoàng Sa Đại Đế đã đánh thức các thần dân của mình để thực hiện kế hoạch khôi phục đế chế.

## X. Giai Thoại & Bí Mật (轶 sự với bí mật)
Tương truyền Hoàng Sa Đại Đế không phải là người, mà là một thực thể sinh ra từ oán niệm của sa mạc đối với ánh mặt trời quá gay gắt.

## XI. Quan Hệ Thế Lực (势力关系)
```mermaid
graph LR
    HSCQ[Hoàng Sa Cổ Quốc] -- Tử địch -- KST[Kim Sa Tự]
    HSCQ -- Thao túng -- STLM[Sa Tặc Liên Minh]
    HSCQ -- Cạnh tranh -- LSHC[Lưu Sa Huyễn Cung]
```
