---
type: faction
name: Quỷ Thị Nam Cương
hantu: 南疆鬼市
faction_type: Hội
alignment: -3
race: Đa chủng tộc
region: Nam Cương
founded: Trung Cổ Kỷ Nguyên
founder: Quỷ Chủ Vô Danh
emblem: Dau_Lau_Xanh_Trong_Suong_Mu.png
specialty: Giao dịch đồ cấm, Thu thập tình báo ngầm, Đấu giá đen
economy:
- Thu phí bến bãi và thông hành (Linh thạch đen)
- Chiết khấu từ các giao dịch bất hợp pháp
- Buôn bán thông tin tuyệt mật
arcs:
  - arc: 1
    status: Hoạt động mạnh trong đêm
    rank: Hạng Nhì (Quy mô ngầm)
    leader: Quỷ Chủ
    population: 10000 (Lưu động)
    territory:
      - Dịch chuyển ngẫu nhiên tại Nam Cương
      - Các cổng kết nối không gian tạm thời
    assets:
      - name: Quỷ Môn Quan (Cổng vào)
        type: Trận Pháp
      - name: Sổ Sinh Tử (Danh sách giao dịch)
        type: Pháp Bảo
      - name: Chấp Pháp Quỷ
        type: Quân Lực
    stats: [3500, 5000, 4000, 10000, 3000, 4500]
    divisions:
      - name: Chấp Pháp Quỷ
        role: Duy trì trật tự tối thiểu và trừng phạt kẻ phá luật chợ
        headcount:
          hoi_truong: 0
          pho_hoi_truong: 1
          thanh_vien: 500
          tong_quan: 20
        members:
          - character: "[Thống Lĩnh Quỷ Sai]"
            position: Thống Lĩnh
            cultivation: Nguyên Anh Hậu Kỳ
            placeholder: true
      - name: Người Đưa Đò
        role: Quản lý lối vào và phát giấy thông hành
        headcount:
          hoi_truong: 0
          pho_hoi_truong: 1
          thanh_vien: 100
          tong_quan: 5
        members:
          - character: "[Lão Giả Đưa Đò]"
            position: Quản Sự
            cultivation: Kim Đan Viên Mãn
            placeholder: true
    relationships:
      - faction: Ảnh Nguyệt Uyển
        description: Đối tác tin cậy trong việc trao đổi tin tức và ám sát.
        diplomacy:
          lien_minh: 50
          tin: 60
          uy_hiep: 0
          thuong_mai: 80
          on_oan: 0
          le_thuoc: 0
      - faction: Vạn Độc Môn
        description: Giao dịch ngầm tài nguyên độc dược và cổ trùng.
        diplomacy:
          lien_minh: 20
          tin: 30
          uy_hiep: 40
          thuong_mai: 70
          on_oan: 0
          le_thuoc: 0
---

# QUỶ THỊ NAM CƯƠNG (南疆鬼市)

## I. Tổng Quan (总览)
Quỷ Thị Nam Cương là chợ đen lớn nhất và bí ẩn nhất lục địa, chỉ xuất hiện vào những đêm không trăng tại các địa điểm ngẫu nhiên trong rừng rậm Nam Cương. Đây là nơi trú ẩn của những kẻ bị truy nã, những tán tu tà ác và cả những đại năng muốn tìm kiếm những món đồ không thể tìm thấy ở bất kỳ đâu khác. Tại Quỷ Thị, luật pháp duy nhất là: "Chỉ có giao dịch, không có đạo đức."

## II. Địa Lý & Tài Nguyên (地理 với tài nguyên)
Quỷ Thị không có vị trí cố định mà tồn tại trong một không gian kẽ hở giữa thực tại và ảo ảnh. Khi đến giờ khai thị, sương mù dày đặc sẽ hiện ra và những kẻ có "Giấy thông hành" sẽ thấy được cổng vào. Tài nguyên của Quỷ Thị chính là dòng chảy của vô số kỳ vật, nội đan yêu thú, thi thể cường giả và các loại công pháp cấm kỵ.

## III. Văn Hóa & Tín Ngưỡng (文化 với信仰)
Tôn thờ sự bí mật và lợi nhuận. Cư dân và khách hàng tại Quỷ Thị thường đeo mặt nạ hoặc sử dụng các phép thuật che giấu danh tính. Văn hóa tại đây lạnh lùng và thực dụng đến cực điểm. Mọi cuộc tranh chấp đều phải giải quyết bên ngoài phạm vi chợ, kẻ nào dám đổ máu trong chợ sẽ bị "Chấp Pháp Quỷ" truy sát đến cùng trời cuối đất.

## IV. Cơ Cấu Tổ Chức (组织结构)
```mermaid
graph TD
    QC[Quỷ Chủ - Bí Ẩn] --> NDĐ[Hội Đồng Người Đưa Đò]
    NDĐ --> CPQ[Chấp Pháp Quỷ]
    NDĐ --> QL Gian[Quản Lý Gian Hàng]
    NDĐ --> TT Vien[Thu Thập Tình Báo]
    CPQ --> QS[Quỷ Sai]
    QL Gian --> TN[Thương Nhân Ngầm]
    TT Vien --> AT[Ảnh Tử]
```

## V. Công Pháp & Trận Pháp (功法 với阵法)
- **Công Pháp:** *Ẩn Diệt Thuật* (Che giấu khí tức), *Quỷ Ảnh Bộ* (Di chuyển trong bóng tối).
- **Trận Pháp:** *Quỷ Môn Quan Trận* - trận pháp không gian dùng để dịch chuyển toàn bộ khu chợ và ngăn chặn những kẻ không có thẩm quyền đột nhập.

## VI. Đặc Sản Môn Phái (门派特产)
- **Giấy Thông Hành Quỷ Thị:** Linh phù dùng một lần để tìm thấy lối vào chợ.
- **Hắc Linh Thạch:** Loại linh thạch biến dị thường được dùng làm đơn vị tiền tệ chính trong chợ.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Quỷ Môn Quan:** Cổng đá khổng lồ chỉ xuất hiện trong sương mù.
- **Sàn Đấu Giá Đen:** Nơi diễn ra các cuộc đấu giá những món hàng "nóng" và quý hiếm nhất.

## VIII. Kinh Tế (経済)
Nguồn thu khổng lồ từ việc thu phí bến bãi của hàng vạn gian hàng tạm thời và phí môi giới cho các giao dịch lớn. Quỷ Thị cũng nắm giữ huyết mạch thông tin của giới tội phạm và ma tu toàn lục địa.

## IX. Lịch Sử Tóm Tắt (简史)
Không ai biết chính xác Quỷ Thị ra đời từ khi nào. Có lời đồn rằng nó được lập ra bởi Quỷ Chủ - một vị cường giả Hóa Thần bị phản bội bởi chính đạo và quyết định tạo ra một thế giới riêng cho những kẻ bị ruồng bỏ. Qua hàng nghìn năm, Quỷ Thị đã trở thành một phần không thể thiếu trong hệ sinh thái của Nam Cương.

## X. Giai Thoại & Bí Mật (轶 sự với bí mật)
Tương truyền Quỷ Chủ sở hữu "Sổ Sinh Tử", ghi lại mọi giao dịch đã từng diễn ra tại đây, và bất kỳ ai nợ tiền Quỷ Thị mà không trả đều sẽ bị gạch tên khỏi sổ sinh tử và chết một cách bí ẩn.

## XI. Quan Hệ Thế Lực (势力关系)
```mermaid
graph LR
    QTNC[Quỷ Thị Nam Cương] -- Hợp tác -- ANU[Ảnh Nguyệt Uyển]
    QTNC -- Giao dịch -- VDM[Vạn Độc Môn]
    QTNC -- Đối tác -- DLB[Độc Long Bảo]
    QTNC -- Cảnh giác -- DCHH[Đại Càn Hoàng Triều]
```
