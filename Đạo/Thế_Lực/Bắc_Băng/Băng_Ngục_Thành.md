---
type: faction
name: Băng Ngục Thành
hantu: 冰狱城
faction_type: Thành Trì
alignment: -8
race: Đa chủng tộc (Tội phạm)
region: Bắc Băng
founded: Trung Cổ Kỷ Nguyên
founder: Liên Minh Đại Tông Môn (Khởi tạo)
emblem: Xich_Sat_Va_Nui_Bang.png
specialty: Sinh tồn cực đoan, Kháng độc, Kháng hàn thụ động, Hỗn chiến tàn bạo
economy:
- Thu phí bảo kê và "thuế sinh tồn"
- Buôn bán tài nguyên đen (Vật phẩm cấm vào tù)
- Đấu trường sinh tử (Cá cược linh thạch)
arcs:
  - arc: 1
    status: Hỗn loạn tự trị
    rank: Hạng Nhì (Quy mô tội phạm lớn)
    leader: Ngục Trưởng Vô Tình
    population: 200000
    territory:
      - Đảo Băng Ngục (Biển Bắc Băng)
      - Hệ thống ngục giam 4 tầng
    assets:
      - name: Trận pháp "Hàn Băng Tỏa Hồn"
        type: Trận Pháp
      - name: Đấu Trường Máu
        type: Công Trình
      - name: Xích Sắt Vạn Năm
        type: Tài Nguyên
    stats: [6000, 3000, 5000, 15000, 4000, 2500]
    divisions:
      - name: Cai Ngục Hắc Giáp
        role: Lực lượng bảo an tham nhũng và đàn áp tù nhân
        headcount:
          thanh_chu: 1
          pho_thanh_chu: 4
          ve_binh: 5000
          quan_vien: 100
          dan_cu: 0
        members:
          - character: Ngục Trưởng Vô Tình
            position: Thành Chủ
            cultivation: Hóa Thần Sơ Kỳ
          - character: "[Thống Lĩnh Hắc Giáp]"
            position: Tướng Quân
            cultivation: Nguyên Anh Hậu Kỳ
            placeholder: true
      - name: Tứ Đại Ác Nhân Đoàn
        role: Các băng nhóm tù nhân tự quản theo tầng ngục
        headcount:
          thanh_chu: 0
          pho_thanh_chu: 4
          ve_binh: 0
          quan_vien: 0
          dan_cu: 195000
        members:
          - character: "[Độc Vương Tù Trưởng]"
            position: Thủ Lĩnh Tầng 1
            cultivation: Nguyên Anh Trung Kỳ
            placeholder: true
    relationships:
      - faction: Thiên Sa Thương Hội
        description: Đối tác giao thương ngầm, cung cấp hàng xa xỉ và vũ khí cấm.
        diplomacy:
          lien_minh: 10
          tin: 20
          uy_hiep: 30
          thuong_mai: 100
          on_oan: 0
          le_thuoc: 0
      - faction: Đại Càn Hoàng Triều
        description: Quan hệ pháp lý, là nơi nhận tù nhân lưu đày nhưng thực tế đã mất kiểm soát.
        diplomacy:
          lien_minh: -20
          tin: 10
          uy_hiep: 50
          thuong_mai: 40
          on_oan: -60
          le_thuoc: 20
---

# BĂNG NGỤC THÀNH (冰狱城)

## I. Tổng Quan (总览)
Băng Ngục Thành là nhà tù lớn nhất và tàn khốc nhất lục địa, tọa lạc trên một hòn đảo băng trôi biệt lập tại Bắc Băng. Ban đầu được xây dựng bởi liên minh các đại tông môn để giam giữ những tội nhân không thể giết ngay lập tức, thành phố này dần biến thành một vương quốc tự trị của tội phạm và những kẻ bị ruồng bỏ. Tại đây, luật pháp duy nhất là sức mạnh của nắm đấm, nơi kẻ mạnh nhất làm vua và kẻ yếu nhất chỉ là phân bón cho băng tuyết.

## II. Địa Lý & Tài Nguyên (地理 với tài nguyên)
Thành phố được xây dựng sâu vào lòng một núi băng khổng lồ, chia làm 4 tầng ngục giam với độ khắc nghiệt tăng dần theo độ sâu. Tài nguyên duy nhất là "Xích Sắt Vạn Năm" - loại xích sắt bị nhiễm hàn khí cực nặng dùng để chế tạo vũ khí thô sơ. Thành phố hoàn toàn phụ thuộc vào nguồn cung ứng lương thực và linh thạch từ bên ngoài thông qua các đường dây buôn lậu.

## III. Văn Hóa & Tín Ngưỡng (文化 với信仰)
Tôn thờ Sức Mạnh và Sự Sinh Tồn. Cư dân Băng Ngục Thành không có đức tin vào thần thánh, họ chỉ tin vào lưỡi đao trên tay và số linh thạch có trong túi. Văn hóa tại đây mang đậm tính thực dụng dã man, nơi việc ăn thịt yêu thú sống hoặc thậm chí là đồng loại (trong những thời kỳ đói kém) không phải là hiếm thấy. Hình xăm và những vết sẹo được coi là biểu tượng của địa vị.

## IV. Cơ Cấu Tổ Chức (组织结构)
```mermaid
graph TD
    NT[Ngục Trưởng: Vô Tình] --> CNHG[Cai Ngục Hắc Giáp]
    CNHG --> TĐÂN[Tứ Đại Ác Nhân - Tù Trưởng]
    TĐÂN --> BN1[Băng Nhóm Tầng 1]
    TĐÂN --> BN2[Băng Nhóm Tầng 2]
    TĐÂN --> BN3[Băng Nhóm Tầng 3]
    TĐÂN --> BN4[Băng Nhóm Tầng 4]
    BN1 --> TN[Tù Nhân]
```

## V. Công Pháp & Trận Pháp (功法 với阵法)
- **Công Pháp:** Không có công pháp chính thống, cư dân học các *Cấm Thuật Sinh Tồn* (Kháng độc, ăn mòn linh lực).
- **Trận Pháp:** *Hàn Băng Tỏa Hồn Trận* - trận pháp khổng lồ bao phủ toàn bộ đảo, liên tục hút cạn linh lực của tù nhân để duy trì sự đóng băng của kết giới không gian, khiến việc đào tẩu là không thể.

## VI. Đặc Sản Môn Phái (门派特产)
- **Băng Ngục Huyết Rượu:** Loại rượu nấu từ linh thảo biến dị và máu yêu thú, giúp tu sĩ tạm thời quên đi cái lạnh và sự đau đớn.
- **Xương Mài Đao:** Vũ khí thô sơ được mài từ xương người hoặc thú, có khả năng xuyên thấu giáp trụ nhờ được tôi luyện trong tử khí lâu ngày.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Đấu Trường Máu:** Trung tâm giải trí duy nhất, nơi tù nhân chiến đấu sinh tử để giành lấy sự ưu tiên về lương thực và chỗ ở.
- **Cổng Trục Xuất:** Nơi duy nhất kết nối với thế giới bên ngoài, được canh giữ bởi trung đoàn Hắc Giáp.

## VIII. Kinh Tế (経済)
Kinh tế hoàn toàn dựa trên sự trao đổi và chiếm đoạt. Ngục trưởng và cai ngục thu lợi nhuận từ việc ăn bớt ngân sách của các tông môn gửi đến và tham gia vào mạng lưới buôn lậu với Thiên Sa Thương Hội. Linh thạch là thứ quý giá nhất, có thể dùng để đổi lấy bất kỳ đặc quyền nào trong tù.

## IX. Lịch Sử Tóm Tắt (简史)
Được thiết lập cách đây hàng nghìn năm bởi liên minh Chính Đạo nhằm mục đích giam giữ các đầu sỏ ma tộc sau đại chiến. Tuy nhiên, sự tham nhũng của các đời cai ngục và sự khắc nghiệt của môi trường đã khiến nơi đây mất đi ý nghĩa giáo hóa ban đầu, trở thành một hang ổ tội phạm quy mô lớn mà chính quyền cũng phải e ngại khi muốn can thiệp.

## X. Giai Thoại & Bí Mật (轶 sự với bí mật)
Tương truyền ở tầng sâu nhất (Tầng 4), có một tù nhân lão thái bà đã bị giam giữ từ thời Thái Cổ, người biết được bí mật về lối thoát duy nhất không cần thông qua Cổng Trục Xuất.

## XI. Quan Hệ Thế Lực (势力关系)
```mermaid
graph LR
    BNT[Băng Ngục Thành] -- Giao dịch ngầm -- TSTH[Thiên Sa Thương Hội]
    BNT -- Đối địch -- DCHH[Đại Càn Hoàng Triều]
    BNT -- Cung cấp nô lệ -- CUMT[Cửu U Ma Tông]
    BNT -- Trung lập -- SMU[Sương Ma Uyển]
```
