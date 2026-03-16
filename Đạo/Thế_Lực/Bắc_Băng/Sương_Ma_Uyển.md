---
type: faction
name: Sương Ma Uyển
hantu: 霜魔苑
faction_type: Tông Môn
alignment: -9
race: Băng Tộc (Biến dị), Ma Tộc (Ẩn)
region: Bắc Băng
founded: Trung Cổ Kỷ Nguyên
founder: Sương Ma Cốc Chủ
emblem: Bong_Ma_Trong_Suong_Lanh.png
specialty: Ma Băng Công Pháp, Đoạt tủy hàn khí, Luyện chế Băng Thi
economy:
- Chiếm đoạt tài nguyên từ các bộ lạc Bắc Băng
- Buôn bán Băng Nô và Băng Thi
- Khai thác tà linh thạch trong sông băng
arcs:
  - arc: 1
    status: Đang bành trướng bóng tối
    rank: Hạng Nhì
    leader: Sương Ma Cốc Chủ
    population: 3000 (Ma tu) + 5000 (Băng nô)
    territory:
      - Khe nứt sông băng vĩnh cửu
      - Lâu đài Ma Sương (Bắc Băng)
    assets:
      - name: Huyết Băng Trì
        type: Tài Nguyên
      - name: Trận pháp "Cửu U Hàn Sát"
        type: Trận Pháp
      - name: Sương Ma Trượng
        type: Pháp Bảo
    stats: [4000, 3000, 3500, 8000, 4500, 3200]
    divisions:
      - name: Thập Nhị Sát Sương Quỷ
        role: Lực lượng sát thủ và hộ pháp nòng cốt
        headcount:
          thai_thuong: 1
          ho_phap: 12
          truong_lao: 0
          chan_truyen: 50
          noi_mon: 200
          ngoai_mon: 500
          tap_dich: 1000
        members:
          - character: "[Đại Quỷ Sương Ma]"
            position: Hộ Pháp
            cultivation: Nguyên Anh Hậu Kỳ
            placeholder: true
      - name: Băng Thi Đội
        role: Quân đoàn xác sống băng phục vụ chiến tranh
        headcount:
          thai_thuong: 0
          ho_phap: 1
          truong_lao: 5
          chan_truyen: 10
          noi_mon: 100
          ngoai_mon: 2000
          tap_dich: 0
        members:
          - character: "[Đại Sư Luyện Thi Băng]"
            position: Đường Chủ
            cultivation: Kim Đan Viên Mãn
            placeholder: true
    relationships:
      - faction: Huyền Băng Cung
        description: Tử địch, thường xuyên bị Huyền Băng Cung truy sát và ngược lại.
        diplomacy:
          lien_minh: -100
          tin: -100
          uy_hiep: 90
          thuong_mai: -100
          on_oan: -100
          le_thuoc: 0
      - faction: Cực Quang Thần Điện
        description: Đối địch sinh tử, coi sương ma là sự báng bổ thần linh.
        diplomacy:
          lien_minh: -100
          tin: -100
          uy_hiep: 80
          thuong_mai: -100
          on_oan: -100
          le_thuoc: 0
---

# SƯƠNG MA UYỂN (霜魔苑)

## I. Tổng Quan (总览)
Sương Ma Uyển là "vết sẹo đen" trên nền tuyết trắng của phương Bắc, một tông môn ma đạo tàn bạo chuyên tu luyện các loại tà thuật liên quan đến băng giá và cái chết. Thành viên của Uyển phần lớn là những kẻ bị trục xuất khỏi các tông môn chính đạo hoặc những sinh vật biến dị do hít phải chướng khí lạnh lẽo lâu ngày. Họ coi nhiệt lượng và sinh cơ của kẻ khác là nguồn tài nguyên để duy trì sự tồn tại và thăng tiến tu vi.

## II. Địa Lý & Tài Nguyên (地理 với tài nguyên)
Trụ sở chính là Lâu Đài Ma Sương, một pháo đài kiến trúc gai góc được xây dựng từ "Hắc Băng" nằm sâu trong một khe nứt sông băng vĩnh cửu. Nơi đây có "Huyết Băng Trì" - hồ nước chứa máu của hàng vạn sinh linh đã bị đóng băng, là nguồn cung cấp tà linh khí thủy hệ vô tận. Họ cũng kiểm soát các mạch sông băng ngầm chứa đầy tà linh thạch.

## III. Văn Hóa & Tín Ngưỡng (文化 với信仰)
Tôn thờ sự lạnh lẽo tuyệt đối và sự diệt vong. Thành viên Sương Ma Uyển tin rằng cảm xúc là thứ rác rưởi làm suy yếu con người, chỉ có sự vô tình như băng giá mới dẫn đến đỉnh cao sức mạnh. Văn hóa của họ cực kỳ điên loạn, nơi việc tra tấn và biến đổi cơ thể xác chết được coi là một loại hình nghệ thuật hắc ám.

## IV. Cơ Cấu Tổ Chức (组织结构)
```mermaid
graph TD
    SMC[Sương Ma Cốc Chủ] --> TSSQ[Thập Nhị Sát Sương Quỷ]
    TSSQ --> BTĐ[Băng Thi Đội]
    TSSQ --> BNĐ[Băng Nô Đội]
    TSSQ --> LTĐ[Luyện Tà Đường]
    BTĐ --> HK[Băng Thi]
    BNĐ --> NLE[Nô Lệ]
    LTĐ --> MT[Ma Tu]
```

## V. Công Pháp & Trận Pháp (功法 với阵法)
- **Công Pháp:** *Cửu U Băng Thi Quyết* (Luyện xác), *Đoạt Tủy Hàn Công* (Hút nhiệt lượng và linh lực).
- **Trận Pháp:** *Cửu U Hàn Sát Trận* - trận pháp bao phủ lâu đài, tạo ra một vùng không gian có nhiệt độ tuyệt đối âm, khiến mọi linh lực của đối phương bị đóng băng ngay khi vận hành.

## VI. Đặc Sản Môn Phái (门派特产)
- **Hắc Băng Châm:** Loại ám khí tàng hình trong tuyết, có khả năng đoạt mạng mục tiêu bằng cách làm đông máu tức thì.
- **Băng Nô:** Những tu sĩ chính đạo bị bắt và xóa sạch trí tuệ, biến thành những công cụ lao động và chiến đấu không biết mệt mỏi.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Lâu Đài Ma Sương:** Kiến trúc đen ngòm, lộng lẫy một cách đáng sợ giữa tuyết trắng.
- **Ngục Giam Hàn Băng:** Nơi giam giữ và "chế biến" các nạn nhân.

## VIII. Kinh Tế (経済)
Kinh tế dựa trên việc cướp phá các bộ lạc du mục và thương đoàn phương Bắc. Họ cũng là nhà cung cấp "Băng Thi" - những xác sống chiến đấu chất lượng cao cho các thế lực ma đạo khác trên lục địa để đổi lấy các tài nguyên tu luyện hiếm.

## IX. Lịch Sử Tóm Tắt (简史)
Sáng lập bởi Sương Ma Cốc Chủ, vốn là một Đại Trưởng Lão thiên tài của Huyền Băng Cung. Do quá ám ảnh với việc tìm kiếm sức mạnh băng hệ tối thượng mà ông đã sa đọa vào ma đạo, đánh cắp bí bảo tông môn và dẫn theo một nhóm đệ tử trung thành lập nên Sương Ma Uyển, trở thành nỗi kinh hoàng của toàn bộ Bắc Băng.

## X. Giai Thoại & Bí Mật (轶 sự với bí mật)
Tương truyền Sương Ma Cốc Chủ đã đóng băng trái tim của chính mình để đạt đến cảnh giới bất tử, và ông chỉ có thể cảm nhận được "sự ấm áp" khi nhìn thấy máu tươi đổ trên tuyết lạnh.

## XI. Quan Hệ Thế Lực (势力关系)
```mermaid
graph LR
    SMU[Sương Ma Uyển] -- Tử địch -- HBC[Huyền Băng Cung]
    SMU -- Đối địch -- CQTĐ[Cực Quang Thần Điện]
    SMU -- Giao dịch -- CUMT[Cửu U Ma Tông]
    SMU -- Săn đuổi -- BLBL[Băng Lang Bộ Lạc]
```
