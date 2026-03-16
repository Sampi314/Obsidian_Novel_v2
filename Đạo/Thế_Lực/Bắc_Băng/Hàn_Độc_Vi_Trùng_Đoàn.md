---
type: faction
name: Hàn Độc Vi Trùng Đoàn
hantu: 寒毒微虫团
faction_type: Đoàn
alignment: 2
race: Vi Tộc (Trùng băng độc)
region: Bắc Băng
founded: Thái Cổ Kỷ Nguyên
founder: Vi Trùng Nguyên Thủy
emblem: Vi_Trùng_Trong_Suốt_Va_Hàn_Độc.png
specialty: Phân giải Hàn Độc, Chuyển hóa linh lực thủy hệ, Tịnh hóa môi trường băng giá
economy:
- Tịnh hóa hàn độc cho hệ sinh thái (Thụ động)
- Cung cấp Hàn Độc Linh Dịch cho đan đạo và luyện khí
- Hợp tác với Tuyết Liên Dược Phường
arcs:
  - arc: 1
    status: Bận rộn do hàn độc gia tăng
    rank: Hạng Năm
    leader: Vi Thanh
    population: 5000
    territory:
      - Các vùng tundra bị nhiễm hàn độc (Bắc Băng)
    assets:
      - name: Quần Thể Vi Trùng
        type: Tài Nguyên
      - name: Trận pháp "Hàn Độc Thôn Phệ"
        type: Trận Pháp
      - name: Hạch Tâm Vi Trùng
        type: Pháp Bảo
    stats: [100, 300, 200, 5000, 400, 350]
    divisions:
      - name: Quần Thể Phân Giải
        role: Hấp thụ và chuyển hóa các loại hàn độc tàn dư
        headcount:
          hoi_truong: 1
          pho_hoi_truong: 0
          thanh_vien: 5000
          tong_quan: 0
        members:
          - character: Vi Thanh
            position: Đoàn Trưởng
            cultivation: Trúc Cơ Sơ Kỳ (Tương đương)
          - character: "[Vi Trùng Trưởng]"
            position: Thành Viên
            cultivation: Luyện Khí Đỉnh Phong
            placeholder: true
    relationships:
      - faction: Tuyết Liên Dược Phường
        description: Đối tác duy nhất biết cách giao tiếp và sử dụng dịch vụ tịnh hóa.
        diplomacy:
          lien_minh: 50
          tin: 80
          uy_hiep: 0
          thuong_mai: 60
          on_oan: 0
          le_thuoc: 0
      - faction: Sương Ma Uyển
        description: Cảnh giác, lo sợ bị bắt làm nguyên liệu luyện chế Băng Thi.
        diplomacy:
          lien_minh: -20
          tin: -40
          uy_hiep: 60
          thuong_mai: 0
          on_oan: -50
          le_thuoc: 0
---

# HÀN ĐỘC VI TRÙNG ĐOÀN (寒毒微虫团)

## I. Tổng Quan (总览)
Hàn Độc Vi Trùng Đoàn là một chủng tộc Vi Tộc chuyên biệt hóa cao, đóng vai trò là "hệ thống miễn dịch" của vùng biển và bình nguyên Bắc Băng. Tồn tại dưới dạng hàng ngàn cá thể trùng nhỏ li ti có khả năng hấp thụ và phân giải các loại hàn độc tàn dư từ thời chiến trường thượng cổ, đoàn đóng vai trò âm thầm nhưng cực kỳ quan trọng trong việc duy trì sự sống cho các chủng tộc khác. Dù mang trong mình độc tố, bản tính của chúng là tịnh hóa thay vì tàn phá.

## II. Địa Lý & Tài Nguyên (地理 với tài nguyên)
Hoạt động tại bất kỳ khu vực nào bị nhiễm hàn độc nặng nề trên vùng tundra hoặc các khe nứt sông băng. Tài nguyên chính của đoàn là "Hàn Độc Linh Dịch" - sản phẩm phụ của quá trình phân giải độc tố, có giá trị cực cao trong việc luyện chế các loại thuốc giải cấp cao. Họ nắm giữ khả năng phát hiện các nguồn ô nhiễm linh lực từ khoảng cách hàng trăm dặm.

## III. Văn Hóa & Tín Ngưỡng (文化 với信仰)
Đề cao triết lý: "Ăn độc trả lành". Mỗi cá thể vi trùng coi việc phân giải độc tố là sứ mệnh duy nhất của đời mình. Họ không có văn hóa xã hội phức tạp, giao tiếp thông qua sự thay đổi màu sắc của cơ thể trong suốt. Tín ngưỡng duy nhất là sự sùng bái đối với "Vi Trùng Nguyên Thủy" - thực thể được cho là khởi nguồn của giống loài.

## IV. Cơ Cấu Tổ Chức (组织结构)
```mermaid
graph TD
    VTNT[Vi Trùng Nguyên Thủy - Thủy Tổ] --> VT[Đoàn Trưởng: Vi Thanh]
    VT --> HDVT[Hội Đồng Vi Trùng Có Linh Trí]
    HDVT --> QTPG[Quần Thể Phân Giải]
    HDVT --> NTĐ[Nhóm Thám Độc]
    HDVT --> NBV[Nhóm Bảo Vệ Quần Thể]
    QTPG --> VTCT[Vi Trùng Cá Thể]
    NTĐ --> VTCT
    NBV --> VTCT
```

## V. Công Pháp & Trận Pháp (功法 với阵法)
- **Công Pháp:** Không có công pháp tu luyện nhân tạo, tiến hóa thông qua *Hàn Độc Thôn Phệ Thuật* - bản năng chuyển hóa độc tố thành linh lực thủy hệ tinh khiết.
- **Trận Pháp:** *Hàn Độc Tử Địa Trận* - khi toàn đoàn tập hợp và cùng lúc giải phóng lượng độc tố đã tích lũy, họ có thể tạo ra một vùng không gian cực độc có khả năng ăn mòn cả thần thức và nhục thân của những kẻ tấn công.

## VI. Đặc Sản Môn Phái (门派特产)
- **Hàn Độc Tinh Hoa:** Linh dịch cô đặc dùng để chế tác các loại ám khí độc hệ cực mạnh hoặc làm chất xúc tác cho luyện đan.
- **Vi Trùng Phấn:** Bào tử của vi trùng có tác dụng tịnh hóa các vùng đất bị nhiễm ma khí nhẹ.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Kén Trú Đông:** Các cấu trúc sinh học tạm thời dùng để bảo vệ quần thể trong những đợt bão tuyết quá mức.
- **Bể Chứa Độc:** Các hốc đá tự nhiên được yểm bùa để lưu trữ lượng độc tố chưa kịp phân giải.

## VIII. Kinh Tế (経済)
Kinh tế mang tính cộng sinh thụ động. Giá trị họ mang lại là sự thanh lọc môi trường cho toàn vùng Bắc Băng. Tuy nhiên, họ có mối quan hệ thương mại đặc biệt với Tuyết Liên Dược Phường, trao đổi linh dịch lấy các loại khoáng chất cần thiết cho sự tiến hóa của quần thể.

## IX. Lịch Sử Tóm Tắt (简史)
Xuất hiện từ kỷ nguyên Thái Cổ, Hàn Độc Vi Trùng đã cứu giúp hàng vạn làng phàm nhân và tu sĩ yếu khỏi cái chết do nhiễm độc từ các di tích cổ bị rò rỉ. Vi Thanh là cá thể hiếm hoi phát triển được ý thức cao và đã đứng ra tổ chức bầy trùng thành một "Đoàn" có hệ thống để bảo vệ giống loài trước sự săn lùng của tu sĩ tà đạo.

## X. Giai Thoại & Bí Mật (轶 sự với bí mật)
Tương truyền Vi Thanh đang cố gắng tiến hóa để có thể phân giải được cả "Ma Độc" - loại độc tố mang theo ý chí của ma tộc, một kỳ tích có thể thay đổi hoàn toàn cuộc chiến chống lại sự suy yếu của phong ấn Bắc Băng.

## XI. Quan Hệ Thế Lực (势力关系)
```mermaid
graph LR
    HĐVTD[Hàn Độc Vi Trùng Đoàn] -- Hợp tác -- TLDV[Tuyết Liên Dược Phường]
    HĐVTD -- Bị săn lùng -- MT Tà Đạo[Tu Sĩ Tà Đạo]
    HĐVTD -- Thanh lọc -- ALL[Hệ sinh thái Bắc Băng]
    HĐVTD -- Tránh né -- SMU[Sương Ma Uyển]
```
