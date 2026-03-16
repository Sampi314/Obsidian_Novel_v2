---
type: faction
name: Đại Càn Hoàng Triều
hantu: 大乾皇朝
faction_type: Vương Quốc
alignment: 8
race: Nhân Tộc (Chủ đạo)
region: Trung Tâm
founded: Trung Cổ Kỷ Nguyên
founder: Đại Càn Thái Tổ
emblem: Rong_Vang_Dong_Lua.png
specialty: Long Mạch Chi Lực, Quản lý hành chính tu chân, Quân đội bọc giáp phù văn
economy:
- Thuế nông nghiệp và thương mại lục địa
- Khai thác linh thạch chính thống
- Phí bảo hộ và thông hành
arcs:
  - arc: 1
    status: Hưng thịnh ổn định
    rank: Hạng Nhất
    leader: Càn Đế
    population: 100000000
    territory:
      - Trung Tâm Đồng Bằng
      - Thiên Trụ Sơn (Chân núi)
    assets:
      - name: Càn Nguyên Cung
        type: Công Trình
      - name: Thái Bảo Ấn
        type: Pháp Bảo
      - name: Trận pháp "Cửu Long Hộ Quốc"
        type: Trận Pháp
    stats: [10000, 15000, 12000, 15000, 11000, 13000]
    divisions:
      - name: Thần Sách Quân
        role: Quân đội tu sĩ tinh nhuệ bảo vệ hoàng thành và biên giới
        headcount:
          vuong: 1
          dai_than: 10
          quan_vien: 100
          cam_ve: 10000
          dan: 50000
        members:
          - character: "[Thần Sách Đại Tướng]"
            position: Thống Lĩnh
            cultivation: Hóa Thần Sơ Kỳ
            placeholder: true
      - name: Khâm Thiên Giám
        role: Quan sát thiên văn, khí vận và quản lý tu sĩ hành pháp
        headcount:
          vuong: 0
          dai_than: 5
          quan_vien: 50
          cam_ve: 200
          dan: 1000
        members:
          - character: "[Khâm Thiên Giám Chính]"
            position: Giám Chính
            cultivation: Nguyên Anh Viên Mãn
            placeholder: true
    relationships:
      - faction: Cửu Hoa Kiếm Tông
        description: Đồng minh chiến lược lâu đời, hỗ trợ quân sự và đào tạo hoàng tộc.
        diplomacy:
          lien_minh: 90
          tin: 80
          uy_hiep: 0
          thuong_mai: 70
          on_oan: 0
          le_thuoc: 0
      - faction: Cửu U Ma Tông
        description: Tử địch, luôn tìm cách phá hoại Long Mạch và lật đổ vương triều.
        diplomacy:
          lien_minh: -100
          tin: -100
          uy_hiep: 100
          thuong_mai: -100
          on_oan: -100
          le_thuoc: 0
---

# ĐẠI CÀN HOÀNG TRIỀU (大乾皇朝)

## I. Tổng Quan (总览)
Đại Càn Hoàng Triều là thực thể chính trị lớn nhất và ổn định nhất Cố Nguyên Giới, cai trị vùng đất phì nhiêu nhất tại trung tâm lục địa. Đây là một đế quốc nơi phàm nhân và tu sĩ cùng tồn tại dưới sự quản lý chặt chẽ của luật pháp hoàng gia. Hoàng triều nắm giữ vận mệnh của hàng triệu dân chúng và là lá chắn vững chắc chống lại sự hỗn loạn của ma đạo.

## II. Địa Lý & Tài Nguyên (地理 với tài nguyên)
Tọa lạc tại vùng đồng bằng Trung Tâm, nơi hội tụ của chín mạch Long Mạch chính (Cửu Long tụ hội). Đất đai nơi đây vô cùng màu mỡ, sản sinh ra nhiều loại linh gạo và dược thảo phổ thông. Hoàng triều kiểm soát các cửa ngõ giao thương giữa các châu lục và nắm giữ nhiều mỏ linh thạch lộ thiên lớn.

## III. Văn Hóa & Tín Ngưỡng (文化 với信仰)
Đề cao Nho giáo tu chân, tôn trọng trật tự, lễ nghĩa và lòng trung quân ái quốc. Cư dân Đại Càn tin rằng Hoàng đế là con của trời (Thiên tử), người kết nối ý chí của nhân loại với Thiên Đạo. Văn hóa hoàng gia rất xa hoa, tinh tế với các buổi yến tiệc, thi cử và lễ tế trời quy mô lớn.

## IV. Cơ Cấu Tổ Chức (组织结构)
```mermaid
graph TD
    CD[Càn Đế] --> LBB[Lục Bộ Đại Thần]
    CD --> TSQ[Thần Sách Quân]
    CD --> KTG[Khâm Thiên Giám]
    LBB --> QLH[Quản Lý Hành Chính]
    TSQ --> QĐ[Quân Đội Tu Sĩ]
    KTG --> TSP[Tu Sĩ Pháp Sư]
    QLH --> DC[Dân Cư]
```

## V. Công Pháp & Trận Pháp (功法与阵法)
- **Công Pháp:** *Càn Khôn Đại Đạo Quyết* (Hoàng tộc), *Hoàng Long Kiếm Pháp* (Quân đội).
- **Trận Pháp:** *Cửu Long Hộ Quốc Trận* - đại trận bao phủ kinh thành, sử dụng sức mạnh của địa mạch để tạo ra lớp phòng ngự tuyệt đối trước các đòn tấn công cấp Hóa Thần.

## VI. Đặc Sản Môn Phái (门派特产)
- **Càn Nguyên Linh Gạo:** Loại gạo chứa linh lực, giúp phàm nhân kéo dài tuổi thọ và tu sĩ hồi phục thể lực.
- **Hoàng Gia Phù Văn:** Các loại bùa chú được đóng dấu ấn hoàng gia, có tính pháp lý và hiệu lực trấn áp ma khí cao.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Càn Nguyên Cung:** Tổ hợp cung điện lộng lẫy được xây dựng trên một mạch linh thạch khổng lồ.
- **Hệ thống Quan Đạo Phù Văn:** Các con đường huyết mạch được yểm bùa để tăng tốc độ di chuyển và đảm bảo an toàn cho thương đoàn.

## VIII. Kinh Tế (经济)
Nền kinh tế đa dạng dựa trên thuế, khai thác tài nguyên và phí bảo hộ. Đại Càn là trung tâm tiêu dùng linh dược và pháp bảo lớn nhất lục địa, tạo ra dòng chảy linh thạch không bao giờ cạn về kho bạc hoàng gia.

## IX. Lịch Sử Tóm Tắt (简史)
Được sáng lập bởi Đại Càn Thái Tổ sau khi ngài thống nhất hàng trăm tiểu quốc đang xâu xé mạch Long Mạch Trung Tâm. Trải qua hàng ngàn năm, dù có những thời kỳ suy vi nhưng nhờ liên minh chặt chẽ với các đại tông môn chính đạo, hoàng triều vẫn giữ vững được vị thế thống trị.

## X. Giai Thoại & Bí Mật (轶 sự với bí mật)
Tương truyền dưới lòng hoàng cung có một "Long Huyệt" chứa đựng chân thân của một con rồng vàng từ thời khai thiên lập địa, bảo vệ khí vận cho toàn bộ quốc gia.

## XI. Quan Hệ Thế Lực (势力关系)
```mermaid
graph LR
    DCHH[Đại Càn Hoàng Triều] -- Đồng minh -- CHKT[Cửu Hoa Kiếm Tông]
    DCHH -- Đối địch -- CUMT[Cửu U Ma Tông]
    DCHH -- Bảo hộ -- TKHV[Thiên Kiêu Học Viện]
    DCHH -- Giao thương -- BBC[Bách Bảo Các]
```
