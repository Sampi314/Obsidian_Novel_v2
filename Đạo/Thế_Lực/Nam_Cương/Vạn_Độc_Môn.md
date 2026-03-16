---
type: faction
name: Vạn Độc Môn
hantu: 万毒门
faction_type: Tông Môn
alignment: -10
race: Nhân Tộc (Ma tu), Yêu Tộc (Cổ trùng)
region: Nam Cương
founded: Năm 82.000 (Khởi Nguyên)
founder: Độc Cô Thiên Sát
emblem: Dau_Re_Va_Mang_Nhen_Doc.png
specialty: Vạn Độc Chân Kinh, Luyện chế Cổ Trùng, Dược Nhân thuật
economy:
- Buôn bán kỳ độc và cổ trùng (Hắc thị)
- Chiếm đoạt tài nguyên dược liệu từ rừng già
- Thu phí bảo hộ (ép buộc) các bộ lạc Nam Cương
arcs:
  - arc: 1
    status: Bành trướng đe dọa
    rank: Hạng Nhất (Siêu cấp nguy hiểm)
    leader: Môn Chủ Độc Cô Lão Quái
    population: 5000 (Ma tu) + 10000 (Dược nhân/Nô lệ)
    territory:
      - Vạn Độc Cốc
      - Nấm Độc Lâm
      - Hệ thống kho chứa ngầm Nam Cương
    assets:
      - name: Huyết Trì Cổ Vương
        type: Tài Nguyên
      - name: Trận pháp "Vạn Độc Phệ Tâm"
        type: Trận Pháp
      - name: Vạn Độc Phù (Chấn môn chi bảo)
        type: Pháp Bảo
    stats: [13000, 9000, 11000, 8000, 12000, 14000]
    divisions:
      - name: Ngũ Độc Trưởng Lão
        role: Quản lý 5 chi nhánh luyện cổ (Xà, Rết, Bò Cạp, Cóc, Nhện)
        headcount:
          thai_thuong: 1
          ho_phap: 5
          truong_lao: 25
          chan_truyen: 50
          noi_mon: 500
          ngoai_mon: 2000
          tap_dich: 1000
        members:
          - character: Độc Cô Lão Quái
            position: Môn Chủ
            cultivation: Hóa Thần Sơ Kỳ
          - character: Lệ Vô Tâm
            position: Thánh Tử
            cultivation: Trúc Cơ Viên Mãn
      - name: Vạn Độc Thất Sát
        role: Đội ngũ sát thủ tinh nhuệ thực hiện nhiệm vụ đặc biệt
        headcount:
          thai_thuong: 0
          ho_phap: 0
          truong_lao: 0
          chan_truyen: 7
          noi_mon: 0
          ngoai_mon: 0
          tap_dich: 0
        members:
          - character: "[Nhất Sát]"
            position: Thống Lĩnh
            cultivation: Giả Đan Cảnh
            placeholder: true
    relationships:
      - faction: Dược Vương Cốc
        description: Tử địch truyền kiếp, mâu thuẫn sâu sắc về y đạo và độc đạo.
        diplomacy:
          lien_minh: -100
          tin: -100
          uy_hiep: 90
          thuong_mai: -100
          on_oan: -100
          le_thuoc: 0
      - faction: Huyết Ma Tông
        description: Đồng minh tạm thời, liên kết khi đối phó Chính Đạo Trung Thổ.
        diplomacy:
          lien_minh: 40
          tin: 20
          uy_hiep: 30
          thuong_mai: 50
          on_oan: 0
          le_thuoc: 0
---

# VẠN ĐỘC MÔN (万毒门)

## I. Tổng Quan (总览)
Vạn Độc Môn là thế lực ma đạo thống trị tuyệt đối tại vùng rừng rậm Nam Cương, khởi nguồn từ sự phản bội của một thiên tài y thuật. Tông môn này biến nọc độc và cổ trùng thành một loại nghệ thuật chiến tranh đáng sợ, có khả năng tiêu diệt toàn bộ một thành trì chỉ bằng một làn khói độc. Với triết lý "Cường giả vi tôn", đây là nơi của những kẻ tàn nhẫn nhất, sẵn sàng hiến tế đồng môn và chính bản thân mình để đạt đến cảnh giới vạn độc bất xâm.

## II. Địa Lý & Tài Nguyên (地理 với tài nguyên)
Trụ sở chính là Vạn Độc Cốc, một thung lũng hình bát quái ngược nằm sâu trong rừng rậm nguyên sinh, quanh năm bao phủ bởi độc vụ màu tím lục. Trung tâm cốc là "Huyết Trì" - nơi nuôi dưỡng những loài cổ trùng vương giả. Tông môn kiểm soát hệ thống "Kho Chứa Ngầm" khổng lồ dùng để vận chuyển hàng cấm và nuôi dưỡng các mẫu vật thí nghiệm kinh tởm như "Dược Nhân".

## III. Văn Hóa & Tín Ngưỡng (文化 với信仰)
Tôn thờ sức mạnh của độc tố và sự đào thải tự nhiên. Đệ tử Vạn Độc Môn tin rằng độc là bản chất của sự sống và cái chết. Văn hóa môn phái cực kỳ tàn bạo, việc đệ tử tàn sát lẫn nhau để tranh giành cổ vương được coi là hợp lệ. Mỗi thành viên đều phải mang trong mình một "Bản Mệnh Cổ Trùng", thứ gắn liền sinh mạng của họ với sức mạnh tà đạo.

## IV. Cơ Cấu Tổ Chức (组织结构)
```mermaid
graph TD
    ĐCTS[Độc Cô Thiên Sát - Thủy Tổ] --> MCLQ[Môn Chủ: Độc Cô Lão Quái]
    MCLQ --> HDTL[Hội Đồng Ngũ Độc Trưởng Lão]
    HDTL --> VĐTS[Vạn Độc Thất Sát]
    HDTL --> MĐS[Mộc Độc Sư]
    HDTL --> LTĐ[Luyện Tà Đường]
    VĐTS --> ST[Sát Thủ]
    MĐS --> TV[Thực Vật Độc]
    LTĐ --> CS[Cổ Sư]
```

## V. Công Pháp & Trận Pháp (功法 với阵法)
- **Công Pháp:** *Vạn Độc Chân Kinh* (Hấp thụ vạn độc rèn luyện nhục thân), *Thiên Cổ Bí Thuật*.
- **Trận Pháp:** *Vạn Độc Phệ Tâm Trận* - trận pháp hộ môn sử dụng độc vụ và ảo giác để ăn mòn thần thức kẻ thù, biến họ thành những dược nhân điên loạn ngay tại chỗ.

## VI. Đặc Sản Môn Phái (门派特产)
- **Cổ Vương:** Những thực thể cổ trùng cấp cao có khả năng ký sinh và điều khiển tu sĩ cấp Nguyên Anh.
- **Vạn Độc Phấn:** Loại bột kịch độc không màu, không mùi, có khả năng vô hiệu hóa linh lực đối phương trong thời gian ngắn.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Huyết Trì Cổ Vương:** Hồ máu trung tâm, nơi diễn ra lễ tế cổ hàng năm.
- **Nấm Độc Lâm:** Vùng ngoại vi đầy những bào tử nấm đột biến, đóng vai trò là hàng rào phòng thủ tự nhiên.

## VIII. Kinh Tế (経済)
Nguồn thu khổng lồ từ việc buôn bán các loại kỳ độc, cổ trùng và thuốc giải độc (thực chất là thuốc khống chế) trên hắc thị. Họ cũng chiếm đoạt tài nguyên dược liệu quý hiếm của Nam Cương thông qua việc cưỡng bức các bộ lạc bản địa lao dịch và nộp phí bảo hộ.

## IX. Lịch Sử Tóm Tắt (简史)
Sáng lập bởi Độc Cô Thiên Sát, một phản đồ thiên tài của Dược Vương Cốc chạy trốn đến Nam Cương sau khi đánh cắp bí mật độc đạo. Ông đã biến vùng đất hoang dã này thành một đế chế ma đạo, liên tục đối đầu với các tông môn chính đạo phương Bắc trong suốt hàng ngàn năm qua.

## X. Giai Thoại & Bí Mật (轶 sự với bí mật)
Tương truyền Độc Cô Lão Quái đang bí mật nuôi dưỡng một "Thần Cổ" có khả năng nuốt chửng linh mạch của toàn bộ thế giới để biến ông ta thành vị thần độc đạo đầu tiên.

## XI. Quan Hệ Thế Lực (势力关系)
```mermaid
graph LR
    VDM[Vạn Độc Môn] -- Tử địch -- DVC[Dược Vương Cốc]
    VDM -- Đối địch -- ĐHC[Đan Hà Cốc]
    VDM -- Đồng minh -- HMT[Huyết Ma Tông]
    VDM -- Thao túng -- HBT[Hắc Báo Trại]
```
