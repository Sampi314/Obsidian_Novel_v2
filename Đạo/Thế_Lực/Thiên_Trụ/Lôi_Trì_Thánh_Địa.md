---
type: faction
name: Lôi Trì Thánh Địa
hantu: 雷池圣地
faction_type: Tông Môn
alignment: 5
race: Nhân Tộc (Lôi tu), Lôi Yêu
region: Thiên Trụ
founded: Thái Cổ Kỷ Nguyên
founder: Lôi Tôn Cổ Đại
emblem: Tia_Set_Xuyen_Tam_Cuc.png
specialty: Lôi Tu Tuyệt Đối, Hấp thụ Cửu Cực Thiên Lôi, Hành pháp Thiên Đạo
economy:
- Cung cấp dịch vụ hộ pháp lôi kiếp
- Bán lôi tinh thạch và linh phù lôi hệ
- Thu phí luyện thể tại ngoại vi Lôi Trì
arcs:
  - arc: 1
    status: Ẩn thế tu luyện
    rank: Hạng Nhất (Chiến lực đặc biệt)
    leader: Lôi Tôn đương nhiệm
    population: 500
    territory:
      - Sườn phía Đông Thiên Trụ Sơn
      - Lôi Trì (Hồ Sấm Sét)
    assets:
      - name: Cửu Cực Lôi Đài
        type: Công Trình
      - name: Trận pháp "Thiên Cương Lôi Giới"
        type: Trận Pháp
      - name: Lôi Phạt Tiễn
        type: Pháp Bảo
    stats: [15000, 5000, 8000, 500, 12000, 10000]
    divisions:
      - name: Lôi Phạt Sứ
        role: Lực lượng thực thi hình pháp và hành đạo lục địa
        headcount:
          thai_thuong: 1
          ho_phap: 5
          truong_lao: 10
          chan_truyen: 20
          noi_mon: 50
          ngoai_mon: 100
          tap_dich: 0
        members:
          - character: "[Đại Sứ Lôi Phạt]"
            position: Hộ Pháp
            cultivation: Hóa Thần Sơ Kỳ
            placeholder: true
      - name: Lôi Thể Viện
        role: Nghiên cứu rèn luyện nhục thân thông qua sấm sét
        headcount:
          thai_thuong: 0
          ho_phap: 2
          truong_lao: 5
          chan_truyen: 15
          noi_mon: 100
          ngoai_mon: 200
          tap_dich: 0
        members:
          - character: "[Trưởng Lão Lôi Thể]"
            position: Viện Chủ
            cultivation: Nguyên Anh Viên Mãn
            placeholder: true
    relationships:
      - faction: Long Cung
        description: Cạnh tranh và xung đột tài nguyên Lôi Kiếp cổ đại.
        diplomacy:
          lien_minh: -20
          tin: 10
          uy_hiep: 60
          thuong_mai: 20
          on_oan: -40
          le_thuoc: 0
      - faction: Thiên Môn Kính Đài
        description: Hợp tác trong việc trấn áp các đại ma đầu tà đạo.
        diplomacy:
          lien_minh: 40
          tin: 70
          uy_hiep: 0
          thuong_mai: 30
          on_oan: 0
          le_thuoc: 0
---

# LÔI TRÌ THÁNH ĐỊA (雷池圣地)

## I. Tổng Quan (总览)
Lôi Trì Thánh Địa là một trong những thế lực ẩn thế mạnh nhất Cố Nguyên Giới, đóng vai trò là "Kẻ hành pháp của Thiên Đạo". Tọa lạc tại khu vực có mật độ sấm sét dày đặc nhất xung quanh núi Thiên Trụ, thánh địa này chỉ thu nạp những tu sĩ có linh căn lôi hệ tinh thuần nhất hoặc những thực thể lôi yêu mang huyết thống thượng cổ. Đây là nơi duy nhất trên thế giới mà con người dám trực tiếp đối mặt và hấp thụ sức mạnh hủy diệt của Thiên Lôi để rèn luyện bản thân.

## II. Địa Lý & Tài Nguyên (地理 với tài nguyên)
Nằm ở sườn phía Đông của Thiên Trụ Sơn, trung tâm là Lôi Trì - một hồ linh dịch khổng lồ liên tục bị sấm sét từ chín tầng trời đánh xuống. Nơi đây sở hữu "Lôi Tinh Thạch" vạn năm và các mạch "Điện Linh Thủy", là nguồn tài nguyên vô giá cho việc đột phá cảnh giới và rèn luyện pháp bảo lôi hệ.

## III. Văn Hóa & Tín Ngưỡng (文化 với信仰)
Tôn thờ sức mạnh của sự công bằng và hủy diệt (Thiên Phạt). Đệ tử Lôi Trì có tính cách thẳng thắn, bộc trực và coi trọng sự thanh tẩy. Họ tin rằng sấm sét là công cụ để loại bỏ mọi sự ô uế và tà đạo trên thế gian. Văn hóa thánh địa đề cao thực lực tuyệt đối và sự kiên trì vượt qua nỗi sợ hãi trước cái chết.

## IV. Cơ Cấu Tổ Chức (组织结构)
```mermaid
graph TD
    LTCD[Lôi Tôn Cổ Đại - Thủy Tổ] --> LT[Lôi Tôn - Chủ Nhân]
    LT --> HDTL[Hội Đồng Lôi Trưởng Lão]
    HDTL --> LPS[Lôi Phạt Sứ]
    HDTL --> LTV[Lôi Thể Viện]
    HDTL --> LKT[Lôi Kiếp Đường]
    LPS --> LP_VIÊN[Lôi Phạt Viên]
    LTV --> LT_TU[Lôi Thể Tu Sĩ]
    LKT --> HP_KIẾP[Hộ Pháp Kiếp]
```

## V. Công Pháp & Trận Pháp (功法 với阵法)
- **Công Pháp:** *Thiên Cương Lôi Quyết* (Chấn phái), *Ngũ Lôi Oanh Đỉnh Thuật* (Tấn công đơn mục tiêu cực mạnh).
- **Trận Pháp:** *Thiên Cương Lôi Giới* - trận pháp bao phủ toàn bộ thánh địa, biến khu vực này thành một vùng cấm bay tuyệt đối, mọi thực thể không có lôi ấn sẽ bị sấm sét đánh tan xác ngay khi đi vào.

## VI. Đặc Sản Môn Phái (门派特产)
- **Lôi Kiếp Dịch:** Linh dịch lấy từ tâm Lôi Trì, giúp tu sĩ tăng khả năng sống sót khi vượt qua thiên kiếp.
- **Lôi Phạt Tiễn:** Mũi tên chứa đựng sức mạnh của một đạo thiên lôi, có khả năng xuyên phá mọi tà khí.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Cửu Cực Lôi Đài:** Nơi đệ tử đứng chịu sét để đột phá cảnh giới.
- **Lôi Đình Điện:** Cung điện xây dựng bằng kim loại dẫn điện cao cấp, nơi hội họp của các trưởng lão.

## VIII. Kinh Tế (経済)
Kinh tế dựa trên việc cung cấp dịch vụ "Hộ Pháp Lôi Kiếp" - hỗ trợ các tu sĩ từ các tông môn khác vượt qua thiên kiếp một cách an toàn (với giá cực đắt). Họ cũng bán các loại vật liệu lôi hệ hiếm và nhận các hợp đồng thực thi công lý đối với các tội đồ lục địa.

## IX. Lịch Sử Tóm Tắt (简史)
Sáng lập bởi Lôi Tôn Cổ Đại vào cuối thời Thái Cổ, người đã dùng nhục thân để trấn áp một vụ nổ linh mạch lôi hệ khổng lồ tại Thiên Trụ Sơn. Ông đã biến thảm họa thành một vùng đất tu luyện và để lại truyền thừa về sự thanh tẩy của sấm sét cho hậu thế.

## X. Giai Thoại & Bí Mật (轶 sự với bí mật)
Tương truyền dưới đáy Lôi Trì có cất giấu "Trái Tim Của Sấm Sét", thứ có thể điều khiển toàn bộ thời tiết và khí hậu của Cố Nguyên Giới nếu được kích hoạt hoàn toàn.

## XI. Quan Hệ Thế Lực (势力关系)
```mermaid
graph LR
    LTTH[Lôi Trì Thánh Địa] -- Hợp tác -- TMKĐ[Thiên Môn Kính Đài]
    LTTH -- Đối địch -- LC[Long Cung]
    LTTH -- Trừ ma -- HMT[Huyết Ma Tông]
    LTTH -- Trung lập -- TAM[Thái Ất Môn]
```
