---
type: faction
name: Cổ Tích Thám Hiểm Đoàn
hantu: 古迹探险团
faction_type: Hội
alignment: 2
race: Nhân Tộc (Tán tu)
region: Tây Mạc
founded: Khoảng 50 năm trước
founder: Lý Cổ Trần
emblem: Cuon_So_Va_Bia_Da_Co.png
specialty: Khảo cổ di tích, Giải mã cổ văn, Thổ Độn Thuật, Phá bẫy cấm chế
economy:
- Bán di vật khai quật được
- Nhận hợp đồng thăm dò từ tông môn nhỏ
- Bán bản đồ và thông tin về vị trí di tích
arcs:
  - arc: 1
    status: Hoạt động tích cực (Đang mở rộng thăm dò gần Lưu Sa Cổ Thành)
    rank: Hạng Tư
    leader: Đoàn Trưởng Lý Cổ Trần
    population: 40
    territory:
      - Dọc Thiên Sa Thương Đạo (di động)
      - Khu vực gần Lưu Sa Cổ Thành
    assets:
      - name: Bộ sưu tập bản đồ cổ Tây Mạc
        type: Tài Nguyên
      - name: Dụng cụ khai quật linh khí
        type: Pháp Bảo
      - name: Mảnh bia đá khắc cổ văn Hoàng Sa
        type: Tài Nguyên
    stats: [200, 150, 300, 40, 150, 250]
    divisions:
      - name: Ban Chỉ Huy
        role: Lãnh đạo đoàn, quyết định mục tiêu thám hiểm và phân phối tài nguyên
        headcount:
          hoi_truong: 1
          pho_hoi_truong: 2
          thanh_vien: 0
          tong_quan: 0
        members:
          - character: Lý Cổ Trần
            position: Đoàn Trưởng
            cultivation: Kim Đan Sơ Kỳ
          - character: "[Phó Đoàn Trần Minh]"
            position: Phó Đoàn (Hậu cần)
            cultivation: Trúc Cơ Viên Mãn
            placeholder: true
          - character: "[Phó Đoàn Vũ Thiết]"
            position: Phó Đoàn (Chiến đấu)
            cultivation: Trúc Cơ Viên Mãn
            placeholder: true
      - name: Đội Thám Hiểm
        role: Khai quật di tích, giải mã cổ văn, phá bẫy và thu thập di vật
        headcount:
          hoi_truong: 0
          pho_hoi_truong: 0
          thanh_vien: 37
          tong_quan: 0
        members:
          - character: "[Chuyên Gia Cổ Văn Linh Sa]"
            position: Chuyên Gia Giải Mã
            cultivation: Trúc Cơ Hậu Kỳ
            placeholder: true
    relationships:
      - faction: Cổ Tích Cự Nhân Thức Tỉnh
        description: Đang cố gắng tiếp cận để học cổ ngữ, quá trình chậm chạp do rào cản niềm tin.
        diplomacy:
          lien_minh: 10
          tin: -10
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 0
      - faction: Hoàng Sa Di Dân
        description: Liên hệ gần đây để tìm hiểu thêm về Hoàng Sa Cổ Quốc qua truyền thuyết truyền miệng.
        diplomacy:
          lien_minh: 20
          tin: 30
          uy_hiep: 0
          thuong_mai: 10
          on_oan: 0
          le_thuoc: 0
      - faction: Cổ Sa Yêu Tộc
        description: Bị theo dõi nghiêm ngặt mà không hề hay biết, Yêu Tộc coi đoàn là mối đe dọa lớn nhất.
        diplomacy:
          lien_minh: 0
          tin: 0
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 0
      - faction: Cổ Nham Bộ Lạc
        description: Bị từ chối khi xin phép thăm dò khu vực đỉnh thiêng, quan hệ không tốt.
        diplomacy:
          lien_minh: -10
          tin: -20
          uy_hiep: 0
          thuong_mai: 0
          on_oan: -10
          le_thuoc: 0
---

# Cổ Tích Thám Hiểm Đoàn (古迹探险团)

## I. Tổng Quan (总览)
Cổ Tích Thám Hiểm Đoàn là đoàn thám hiểm di tích cổ đại do tán tu Lý Cổ Trần thành lập, chuyên hoạt động trên khắp Tây Mạc để tìm kiếm, khai quật và nghiên cứu tàn tích của các nền văn minh đã mất. Với khoảng 40 tán tu đa dạng chuyên môn, đoàn không có lãnh địa cố định mà di chuyển theo tin tức về di tích mới phát hiện, lấy Thiên Sa Thương Đạo làm tuyến hoạt động chính. Dù bị các tông môn lớn thường xuyên chiếm đoạt thành quả, đoàn vẫn kiên trì theo đuổi sứ mệnh bảo tồn lịch sử — đặc biệt đang tập trung vào bí ẩn xung quanh Hoàng Sa Cổ Quốc và Lưu Sa Cổ Thành.

## II. Địa Lý & Tài Nguyên (地理与资源)
Cổ Tích Thám Hiểm Đoàn không có trụ sở cố định, thường đóng tại các trạm dừng dọc Thiên Sa Thương Đạo và di chuyển liên tục theo tin tức về di tích. Khu vực hoạt động chủ yếu nằm trong Hoàng Kim Sa Hải và vùng phụ cận Lưu Sa Cổ Thành. Tài sản quý giá nhất của đoàn là bộ sưu tập bản đồ cổ sưu tầm qua nhiều năm, cùng dụng cụ khai quật chuyên dụng và bùa hộ mệnh chống cấm chế. Nguồn thu nhập đến từ việc bán di vật khai quật được và nhận hợp đồng thăm dò từ các tông môn nhỏ không đủ nhân lực tự khám phá.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
Triết lý cốt lõi của đoàn là "Di tích là sách sử — phá hủy di tích là xóa ký ức", thể hiện sự tôn trọng sâu sắc đối với lịch sử và các nền văn minh đã mất. Quy tắc bắt buộc là phải ghi chép tỉ mỉ mọi phát hiện trước khi lấy đi bất kỳ thứ gì, và chiến lợi phẩm được chia đều cho tất cả thành viên. Trước khi vào mỗi di tích, đoàn đốt hương cầu xin vong linh cổ nhân cho phép — một nghi thức mà Đoàn Trưởng Lý rất coi trọng. Tuy nhiên, mâu thuẫn nội bộ luôn âm ỉ: nhiều thành viên muốn bán di vật để kiếm tiền sinh sống, trong khi Đoàn Trưởng muốn giữ lại để nghiên cứu.

## IV. Cơ Cấu Tổ Chức (组织结构)
Đoàn Trưởng Lý Cổ Trần đứng đầu — một tán tu Kim Đan Sơ Kỳ bị ám ảnh bởi lịch sử Hoàng Sa Cổ Quốc. Ông vốn là thư sinh nghèo đạt Kim Đan nhờ cơ duyên trong một di tích nhỏ, từ đó dành cả đời cho việc tìm kiếm cổ tích. Dưới ông là 2 Phó Đoàn Trúc Cơ Viên Mãn, một phụ trách hậu cần và một phụ trách chiến đấu. Khoảng 40 thành viên là tán tu từ Trúc Cơ Sơ đến Hậu Kỳ, mỗi người mang chuyên môn riêng biệt — giải mã cổ văn, phá bẫy, dược liệu, vẽ bản đồ, và nhiều kỹ năng khác cần thiết cho công tác khảo cổ.

## V. Công Pháp & Trận Pháp (功法与阵法)
- **Công Pháp:** *Thổ Độn Thuật* cấp trung — công pháp sở trường của Đoàn Trưởng, dùng để đào hầm an toàn và tránh bẫy trong di tích. Một số thành viên biết *Cấm Chế Giải Thuật* sơ đẳng, đủ để phá bỏ bẫy đơn giản trong các di tích cấp thấp.
- **Trang Bị:** Bùa chiếu sáng, dây linh dẫn đường, thuốc giải độc khí cổ mộ — đây là trang bị tiêu chuẩn cho mỗi chuyến thám hiểm. Không có trận pháp phòng thủ riêng, dựa vào sự cơ động và kinh nghiệm thực chiến.

## VI. Đặc Sản Môn Phái (门派特产)
- **Bản Đồ Di Tích Tây Mạc:** Bộ sưu tập bản đồ chi tiết nhất về các di tích đã biết trên toàn Tây Mạc, là sản phẩm tích lũy qua nhiều thập kỷ thám hiểm.
- **Sổ Ghi Chép Cổ Văn:** Bản dịch và phân tích cổ văn từ hàng trăm di tích khác nhau, có giá trị nghiên cứu lịch sử cực cao.
- **Bùa Chống Cấm Chế:** Bùa hộ mệnh tự chế giúp giảm thiểu tác dụng của cấm chế cổ đại, tuy hiệu quả hạn chế nhưng là thứ mà các nhà thám hiểm khác rất muốn có.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Trại Di Động:** Hệ thống lều trại có thể dựng và thu gọn nhanh chóng, trang bị trận pháp cảnh giới đơn giản.
- **Kho Lưu Trữ Di Vật:** Kho bí mật đặt tại một trạm dừng trên Thiên Sa Thương Đạo, chứa các di vật đang được nghiên cứu.
- **Phòng Nghiên Cứu Dã Chiến:** Khu vực trong trại được Đoàn Trưởng dành riêng cho việc giải mã cổ văn và phân tích di vật.

## VIII. Kinh Tế (经济)
Kinh tế của Cổ Tích Thám Hiểm Đoàn bấp bênh và phụ thuộc hoàn toàn vào kết quả khai quật. Nguồn thu chính đến từ việc bán di vật không có giá trị nghiên cứu cho thương nhân trên Thiên Sa Thương Đạo, cùng các hợp đồng thăm dò thuê từ tông môn nhỏ. Tuy nhiên, những di tích lớn thường bị các tông môn mạnh chiếm đoạt thành quả, khiến đoàn chỉ kiếm được từ các phát hiện nhỏ lẻ. Mâu thuẫn giữa nhu cầu kiếm tiền sinh sống và lý tưởng bảo tồn lịch sử của Đoàn Trưởng là vấn đề nội bộ chưa có lời giải.

## IX. Lịch Sử Tóm Tắt (简史)
Lý Cổ Trần vốn là thư sinh nghèo không có sư phụ, đạt Kim Đan hoàn toàn nhờ cơ duyên khi vô tình bước vào một di tích nhỏ và thu được pháp bảo cùng linh dược. Trải nghiệm đó thay đổi cuộc đời ông — từ đó, Lý Cổ Trần dành trọn tâm huyết đi tìm kiếm tàn tích cổ đại khắp Tây Mạc. Cổ Tích Thám Hiểm Đoàn ra đời khi ngày càng nhiều tán tu muốn đi theo ông, thu hút bởi tài năng khảo cổ và sự trung thực trong chia sẻ chiến lợi phẩm. Đoàn nổi tiếng vì khám phá nhiều di tích nhỏ, nhưng mỗi lần tìm thấy di tích lớn đều bị các tông môn mạnh cướp lấy thành quả. Gần đây, Lý Cổ Trần bắt đầu liên hệ với Hoàng Sa Di Dân để tìm hiểu thêm về Cổ Quốc, và có tin đồn ông đã bí mật tiếp xúc với Cổ Tích Cự Nhân Thức Tỉnh.

## X. Giai Thoại & Bí Mật (轶事与秘密)
Đoàn Trưởng Lý sở hữu một mảnh bia đá khắc cổ văn Hoàng Sa, trên đó ghi chép về "Vĩnh Hằng Sa Hải" — có thể là tên thật của Vĩnh Tịch Chi Địa, thông tin mà nếu lộ ra sẽ gây chấn động giới tu luyện Tây Mạc. Trong một lần khai quật gần Lưu Sa Cổ Thành, đoàn tìm thấy một căn phòng ngầm chứa xác tu sĩ cổ đại ngồi xếp bằng — xác không phân hủy, tóc vẫn mọc dài, như thể người này vẫn đang tu luyện dù đã chết hàng ngàn năm. Đoàn Trưởng phong ấn căn phòng và cấm mọi người nói ra. Có tin đồn lan truyền rằng Lý Cổ Trần đã bí mật tiếp xúc với Cự Nhân thức tỉnh trong Lưu Sa Cổ Thành để học cổ ngữ, nhưng ông không xác nhận cũng không phủ nhận.

## XI. Quan Hệ Thế Lực (势力关系)
| Thế Lực | Quan Hệ | Mô Tả |
|---|---|---|
| Cổ Tích Cự Nhân Thức Tỉnh | Tìm cách tiếp cận | Muốn học cổ ngữ, tiến triển chậm |
| Hoàng Sa Di Dân | Hợp tác mới | Liên hệ tìm hiểu truyền thuyết Cổ Quốc |
| Cổ Sa Yêu Tộc | Bị theo dõi | Không hay biết bị Yêu Tộc cổ đại giám sát |
| Cổ Nham Bộ Lạc | Bị từ chối | Xin thăm dò đỉnh thiêng bị cự tuyệt |
