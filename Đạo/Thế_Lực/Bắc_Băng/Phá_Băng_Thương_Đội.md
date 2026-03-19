---
type: faction
name: Phá Băng Thương Đội
hantu: 破冰商队
faction_type: Thương Hội
alignment: 3
race: Nhân Tộc
region: Bắc Băng
founded: Năm Khởi Nguyên 99.950
founder: Châu Phá Thiên
emblem: Xe_Hang_Xuyen_Tuyet.png
specialty: Vận chuyển hàng hóa xuyên tuyết, Buôn bán liên vùng Bắc Băng - Trung Thổ
economy:
- Phí vận chuyển hàng hóa và nguyên liệu
- Chênh lệch giá buôn bán giữa Bắc Băng và vùng ôn đới
- Dịch vụ đặt hàng theo yêu cầu cho các phường hội nhỏ
arcs:
  - arc: 1
    status: Hoạt động ổn định, đang mở rộng tuyến đường
    rank: Hạng Năm
    leader: Đội Trưởng Châu Phá Thiên
    population: 55
    territory:
      - Trạm trung chuyển rìa nam Bắc Băng
      - Tuyến đường thương mại rìa nam — chân Tuyết Sơn
    assets:
      - name: Trạm Trung Chuyển Phá Băng
        type: Công Trình
      - name: Đoàn xe kéo bọc da thú kháng hàn
        type: Pháp Bảo
      - name: Kho hàng ngầm dưới trạm
        type: Công Trình
    stats: [60, 120, 80, 55, 50, 100]
    divisions:
      - name: Ban Thương Mại
        role: Đàm phán giá cả, quản lý hàng hóa và quan hệ khách hàng
        headcount:
          hoi_truong: 1
          truong_lao: 0
          thuong_nhan: 8
          ho_ve: 10
          nhan_cong: 36
        members:
          - character: Châu Phá Thiên
            position: Đội Trưởng
            cultivation: Trúc Cơ Viên Mãn
          - character: "[Phó Đội Trưởng]"
            position: Phó Đội Trưởng
            cultivation: Trúc Cơ Trung Kỳ
            placeholder: true
          - character: "[Hộ Vệ Trưởng]"
            position: Đội Trưởng Hộ Vệ
            cultivation: Trúc Cơ Sơ Kỳ
            placeholder: true
    relationships:
      - faction: Băng Nguyên Tán Tu Hội
        description: Đối tác bảo vệ quan trọng nhất, cung cấp nhu yếu phẩm đổi lấy hộ tống an toàn.
        diplomacy:
          lien_minh: 30
          tin: 60
          uy_hiep: 0
          thuong_mai: 80
          on_oan: 20
          le_thuoc: 10
      - faction: Bắc Phong Thông Tín Trạm
        description: Nguồn thông tin thời tiết và cảnh báo bão tuyết không thể thiếu trước mỗi chuyến hàng.
        diplomacy:
          lien_minh: 20
          tin: 70
          uy_hiep: 0
          thuong_mai: 50
          on_oan: 0
          le_thuoc: 5
      - faction: Tuyết Liên Dược Phường
        description: Khách hàng thường xuyên, Thương Đội vận chuyển dược liệu và thành phẩm cho phường.
        diplomacy:
          lien_minh: 10
          tin: 50
          uy_hiep: 0
          thuong_mai: 70
          on_oan: 0
          le_thuoc: 0
---

# PHÁ BĂNG THƯƠNG ĐỘI (破冰商队)

## I. Tổng Quan (总览)
Phá Băng Thương Đội là một đoàn thương nhân nhỏ hoạt động tại rìa nam Bắc Băng, chuyên vận chuyển hàng hóa giữa vùng băng giá và các khu vực ôn đới phía nam. Đứng đầu là Châu Phá Thiên, một cựu đệ tử ngoại môn từ Trung Thổ có tu vi Trúc Cơ Viên Mãn, giỏi đàm phán hơn chiến đấu. Tuy quy mô nhỏ bé với chỉ vài chục người và mấy chiếc xe kéo bọc da thú, Thương Đội lại đóng vai trò mạch máu kinh tế quan trọng cho những thế lực nhỏ ở rìa Bắc Băng — nơi mà các thương hội lớn như Phong Bạo Thương Đội không thèm ghé qua vì lợi nhuận quá ít.

## II. Địa Lý & Tài Nguyên (地理 与 资源)
Trạm trung chuyển của Thương Đội nằm tại rìa nam Bắc Băng, đúng nơi giao thoa giữa vùng băng giá vĩnh cửu và vùng ôn đới. Đây là một cụm nhà gỗ thấp, kiên cố, bao quanh bởi hàng rào gỗ cắm sâu vào đất đóng băng. Tuyến đường thương mại chính kéo dài từ trạm trung chuyển qua các đồng tuyết, dọc theo chân Tuyết Sơn rồi quay về — mỗi chuyến mất 20 đến 30 ngày tùy thời tiết, mùa bão phải dừng hẳn hoạt động. Tài nguyên của Thương Đội không nằm ở đất đai mà ở mạng lưới quan hệ thương mại và kiến thức về các tuyến đường an toàn xuyên tuyết — thứ mà Châu Phá Thiên đã mất nhiều năm và không ít máu xương mới tích lũy được.

## III. Văn Hóa & Tín Ngưỡng (文化 与 信仰)
Triết lý kinh doanh của Châu Phá Thiên là "Lợi nhuận nhỏ nhưng chắc chắn" — không tham lam, không mạo hiểm quá sâu vào Bắc Băng, không nhận hàng cấm hay phục vụ tà đạo. Quy tắc cốt lõi: mất hàng thì cả đội chịu lỗ chung, lãi thì chia đều theo công sức. Điều này tạo nên tinh thần đoàn kết hiếm thấy trong giới thương nhân, nơi mà sự phản bội và trộm cắp là chuyện thường ngày. Trước mỗi chuyến hàng, Châu Phá Thiên dẫn cả đội đốt nhang tại trạm trung chuyển, cầu nguyện cho hành trình bình an — một tập tục mà hắn mang theo từ quê nhà ở Trung Thổ, nay đã trở thành nghi thức không thể thiếu.

## IV. Cơ Cấu Tổ Chức (组织结构)
Thương Đội hoạt động theo mô hình bán quân sự đơn giản, phù hợp với tính chất di chuyển liên tục và nguy hiểm cao. Châu Phá Thiên là Đội Trưởng kiêm luôn vai trò đàm phán viên chính, nắm quyền quyết định tuyến đường và chọn khách hàng. Phó Đội Trưởng quản lý hậu cần và phân công nhân lực. Đội Hộ Vệ gồm 10 Luyện Khí tu sĩ thuê theo mùa, chịu trách nhiệm bảo vệ đoàn hàng trước yêu thú và tuyết tặc. Còn lại là 36 phu khuân vác — phàm nhân khỏe mạnh quen chịu lạnh, nhiều người trong số họ đã theo Thương Đội từ những ngày đầu và trung thành tuyệt đối với Châu Phá Thiên.

## V. Công Pháp & Trận Pháp (功法 与 阵法)
Thương Đội không sở hữu công pháp riêng — Châu Phá Thiên tu luyện theo công pháp cấp thấp mang từ tông phái cũ, còn đội hộ vệ mỗi người một phương pháp tùy xuất thân. Để bù đắp cho yếu điểm này, Thương Đội dựa vào trang bị: bùa hộ thể cấp thấp mua từ Thiên Sa Thương Hội giúp chống lạnh, áo khoác da thú phù văn giữ nhiệt, và một bộ vũ khí thô sơ nhưng thực dụng gồm giáo sắt, cung tên và dao ngắn cho hộ vệ. Châu Phá Thiên còn mang theo một La Bàn Tuyết Địa — pháp khí cấp thấp có khả năng cảm ứng biến đổi thời tiết trong phạm vi mười dặm, giúp tránh bão kịp thời.

## VI. Đặc Sản Môn Phái (门派特产)
- **Dịch Vụ Vận Chuyển Xuyên Tuyết:** Thương Đội là một trong số rất ít đoàn buôn chịu nhận đơn hàng nhỏ lẻ cho các phường hội bé ở rìa Bắc Băng — nơi mà thương hội lớn coi thường.
- **Trà Kháng Hàn Châu Gia:** Loại trà pha chế từ thảo dược chịu lạnh mà Châu Phá Thiên tự mày mò phối chế, giúp cơ thể giữ ấm suốt nhiều giờ đi trong tuyết. Nhiều khách hàng quen mua riêng loại trà này.
- **Bản Đồ Tuyến Đường Mùa Đông:** Châu Phá Thiên ghi chép cẩn thận các tuyến đường an toàn theo từng mùa, thỉnh thoảng bán bản sao cho các đoàn thám hiểm nhỏ để kiếm thêm thu nhập.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Trạm Trung Chuyển Phá Băng:** Cụm nhà gỗ kiên cố gồm kho hàng, nhà ở cho nhân viên, chuồng ngựa và một sảnh giao dịch nhỏ. Tuy đơn sơ nhưng ấm áp nhờ lò sưởi đá lớn chạy suốt mùa đông.
- **Kho Hàng Ngầm:** Hầm chứa đào sâu dưới trạm, lợi dụng lớp đất đóng băng vĩnh cửu để bảo quản hàng hóa nhạy nhiệt như dược liệu tươi và da thú chưa thuộc.
- **Đoàn Xe Kéo Bọc Da:** Bốn chiếc xe kéo lớn bọc da thú Hàn Ngưu nhiều lớp, có khắc phù văn giữ nhiệt cơ bản — tài sản quý giá nhất của Thương Đội, mỗi chiếc trị giá bằng nửa năm lợi nhuận.

## VIII. Kinh Tế (经济)
Mô hình kinh tế của Thương Đội dựa trên chênh lệch giá giữa hai vùng: mang lương thực, vải vóc, dược liệu thường và vật phẩm tu luyện cơ bản từ vùng ôn đới lên Bắc Băng, rồi mang băng linh thạch, da thú quý, nấm tuyết và sản phẩm của các phường hội nhỏ về phía nam bán. Biên lợi nhuận mỏng nhưng ổn định, đủ để trả lương cho nhân viên và duy trì trang thiết bị. Châu Phá Thiên cũng nhận dịch vụ đặt hàng theo yêu cầu — tìm mua vật phẩm cụ thể cho khách quen với phí hoa hồng 15%, nguồn thu này chiếm gần một phần ba tổng doanh thu.

## IX. Lịch Sử Tóm Tắt (简史)
Châu Phá Thiên vốn là đệ tử ngoại môn của một tông phái nhỏ ở Trung Thổ, tu vi bình thường và không có triển vọng thăng tiến. Năm ba mươi tuổi, hắn nhận ra rằng con đường tu tiên chính thống không dành cho mình, bèn rời tông phái và đi về phía bắc tìm cơ hội buôn bán. Ban đầu Thương Đội chỉ có Châu Phá Thiên, hai con lừa và một xe hàng nhỏ. Nhiều lần suýt bị tuyết tặc cướp sạch, một lần bị yêu thú tấn công mất hết hàng hóa và phải bò về trạm trong tuyết ba ngày liền. Nhưng nhờ sự kiên trì, mối quan hệ tốt với Băng Nguyên Tán Tu Hội (cung cấp lương thực đổi lấy hộ tống), và uy tín thương mại "nói giá nào giá đó", Thương Đội dần lớn mạnh thành đoàn buôn ổn định nhất vùng rìa nam. Nay Châu Phá Thiên đang ấp ủ kế hoạch mở rộng tuyến đường sâu hơn vào Bắc Băng — nếu thành công, lợi nhuận sẽ tăng gấp nhiều lần.

## X. Giai Thoại & Bí Mật (轶事 与 秘密)
Châu Phá Thiên lén giấu một phần lợi nhuận mỗi chuyến hàng vào một tài khoản bí mật, tích lũy tài nguyên chuẩn bị cho việc đột phá Kim Đan — dù hắn biết rõ cơ hội thành công cực kỳ mong manh với căn cơ tầm thường của mình. Đáng lo ngại hơn, Thương Đội từng vô tình vận chuyển một kiện hàng niêm phong chứa linh vật cấm cho một khách hàng lạ mặt. Khi phát hiện thì đã muộn, kiện hàng đã giao xong, và từ đó Châu Phá Thiên có cảm giác bị một thế lực bí ẩn theo dõi — thi thoảng nhìn thấy bóng đen thoáng qua trên tuyến đường quen thuộc. Ngoài ra, hắn là một trong số rất ít người biết rằng Bạch Hồ Ẩn Tộc thực chất là yêu tộc ngụy trang thành nhân tộc, nhưng giữ kín bí mật này vì họ là khách hàng trung thành và trả giá hậu hĩnh.

## XI. Quan Hệ Thế Lực (势力关系)
```mermaid
graph LR
    PBTĐ[Phá Băng Thương Đội] -- Hợp tác bảo vệ -- BNTTH[Băng Nguyên Tán Tu Hội]
    PBTĐ -- Thông tin thời tiết -- BPTTT[Bắc Phong Thông Tín Trạm]
    PBTĐ -- Vận chuyển dược liệu -- TLDP[Tuyết Liên Dược Phường]
    PBTĐ -- Tránh cạnh tranh -- PBTĐ2[Phong Bạo Thương Đội]
    PBTĐ -- Khách hàng bí ẩn -- BHẤT[Bạch Hồ Ẩn Tộc]
```
