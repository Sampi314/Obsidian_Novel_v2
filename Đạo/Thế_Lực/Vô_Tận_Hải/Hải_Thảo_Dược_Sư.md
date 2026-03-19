---
type: faction
name: Hải Thảo Dược Sư
hantu: 海草药师
faction_type: Hội
alignment: 4
race: Đa chủng tộc (Nhân tộc, Hải tộc)
region: Vô Tận Hải
founded: Khoảng hai trăm năm trước
founder: Hà Thanh Liên
emblem: Tao_Linh_Dan_Lo.png
specialty: Bào chế dược phẩm từ tảo linh, Thủy Tức Pháp, Nghiên cứu dược liệu biển
economy:
- Bán Tảo Linh Giải Độc Đan và Hải Thảo Hồi Khí Tán
- Cung cấp dược liệu biển cho tông môn trên đất liền
- Thu phí chữa bệnh cho ngư dân và thương nhân biển
arcs:
  - arc: 1
    status: Hoạt động âm thầm
    rank: Không Xếp Hạng
    leader: Dược Sư Trưởng Hà Thanh Liên
    population: 33
    territory:
      - Động Tảo Xanh (vùng biển sâu phía tây Vô Tận Hải)
      - Rừng Tảo Linh Khổng Lồ (vùng xám)
    assets:
      - name: Động Tảo Xanh
        type: Công Trình
      - name: Rừng Tảo Linh Dược Tính
        type: Tài Nguyên
      - name: Tảo Trường Sinh (bí mật)
        type: Tài Nguyên
    stats: [8, 40, 15, 33, 12, 20]
    divisions:
      - name: Dược Phòng
        role: Bào chế dược phẩm, nghiên cứu tảo linh dược tính, chữa bệnh
        headcount:
          hoi_truong: 1
          pho_hoi_truong: 0
          thanh_vien: 12
          tong_quan: 20
        members:
          - character: Hà Thanh Liên
            position: Dược Sư Trưởng
            cultivation: Trúc Cơ Viên Mãn
            placeholder: false
          - character: "[Lục Tảo Nhi]"
            position: Đại Đệ Tử
            cultivation: Trúc Cơ Trung Kỳ
            placeholder: true
          - character: "[Bạch Liên Tử]"
            position: Dược Sư
            cultivation: Trúc Cơ Sơ Kỳ
            placeholder: true
    relationships:
      - faction: Hải Tảo Nông Dân Hội
        description: Đối tác cung ứng quan trọng nhất. Mua tảo linh nguyên liệu từ nông dân, đổi lại cung cấp thuốc chữa bệnh miễn phí. Hai bên phụ thuộc lẫn nhau trong chuỗi cung ứng.
        diplomacy:
          lien_minh: 30
          tin: 50
          uy_hiep: 0
          thuong_mai: 60
          on_oan: 0
          le_thuoc: 0
      - faction: Hải Thần Cung
        description: Trung lập xa cách. Hải Thần Cung biết đến sự tồn tại của hội nhưng không coi trọng vì quy mô quá nhỏ. Hoạt động trong "vùng xám" nên không bị quản lý nhưng cũng không được bảo hộ.
        diplomacy:
          lien_minh: 0
          tin: 10
          uy_hiep: 5
          thuong_mai: 15
          on_oan: 0
          le_thuoc: 0
      - faction: Ngư Dân Tu Luyện Hội
        description: Khách hàng trung thành. Ngư dân biển là nhóm tin dùng dược phẩm tảo linh nhiều nhất, thường xuyên mua Giải Độc Đan để phòng thân khi ra khơi.
        diplomacy:
          lien_minh: 20
          tin: 45
          uy_hiep: 0
          thuong_mai: 55
          on_oan: 0
          le_thuoc: 0
---

# HẢI THẢO DƯỢC SƯ (海草药师)

## I. Tổng Quan (总览)
Hải Thảo Dược Sư là một hội nghề nhỏ chuyên bào chế dược phẩm từ tảo linh biển sâu, do Dược Sư Trưởng Hà Thanh Liên sáng lập và dẫn dắt. Với ba mươi ba thành viên gồm mười hai dược sư và hai mươi học đồ, hội hoạt động âm thầm tại Động Tảo Xanh trong vùng biển sâu phía tây Vô Tận Hải — nơi ánh sáng gần như không lọt xuống. Hà Thanh Liên, một cựu đệ tử Dược Vương Cốc trên đất liền bị trục xuất vì nghiên cứu "tà dược," đã dành cả đời chứng minh rằng dược liệu biển có giá trị ngang bằng thảo dược đất liền. Dù bị giới tu luyện chính thống hoài nghi, sản phẩm của hội vẫn được ngư dân và thương nhân biển tin dùng rộng rãi.

## II. Địa Lý & Tài Nguyên (地理 与 资源)
Hội hoạt động trong và xung quanh rừng tảo linh khổng lồ dưới đáy biển phía tây, nơi ánh sáng mặt trời không thể chạm tới. Rừng tảo trải dài hàng dặm, gồm nhiều loại tảo linh có dược tính quý giá: Huyết Tảo đỏ thẫm chuyên trị nội thương, Ngân Tảo phát quang dùng giải độc, và Bích Tảo xanh biếc có tác dụng hồi phục linh lực. Vùng tảo nằm trong "vùng xám" — không thuộc lãnh thổ chính thức của Hải Thần Cung hay Long Cung, nhưng cũng không an toàn vì thường xuyên có hải thú hoang dã và sinh vật biển sâu nguy hiểm xuất hiện. Hải lưu lạnh từ phương bắc mang dinh dưỡng nuôi rừng tảo — nếu hải lưu đổi hướng, toàn bộ rừng tảo sẽ héo tàn trong vài tháng, đồng nghĩa với sự sụp đổ của hội. Động Tảo Xanh, trụ sở chính, là một hang động tự nhiên ẩn giữa rừng tảo dày đặc, khó tìm nếu không có người dẫn đường.

## III. Văn Hóa & Tín Ngưỡng (文化 与 信仰)
Thành viên đều là dược sư hoặc người có kiến thức về thảo dược biển, chia sẻ niềm đam mê nghiên cứu và bào chế. Họ tin rằng tảo linh có linh hồn — trước khi thu hoạch bất kỳ cây tảo nào, dược sư phải quỳ xuống xin phép và hứa sẽ sử dụng đúng mục đích chữa bệnh cứu người. Mỗi dược sư mang theo một lọ nước biển cổ từ nơi mình sinh ra, gọi là "Cố Hương Thủy," đeo bên mình như bùa hộ mệnh và biểu tượng của nguồn cội. Hà Thanh Liên đặt ra quy tắc tối thượng: dược phẩm của hội không được dùng cho mục đích chiến tranh hay hại người, vi phạm sẽ bị trục xuất vĩnh viễn. Văn hóa nội bộ đề cao sự tỉ mỉ, kiên nhẫn, và lòng trắc ẩn — dược sư không chỉ chữa thân bệnh mà còn an ủi tâm bệnh.

## IV. Cơ Cấu Tổ Chức (组织结构)
Hà Thanh Liên đứng đầu với vai trò Dược Sư Trưởng, vừa là người lãnh đạo vừa là thầy dạy. Mười hai dược sư chính thức có tu vi từ Luyện Khí đến Trúc Cơ, mỗi người phụ trách một mảng chuyên môn riêng — có người chuyên thu hoạch, người chuyên bào chế, người chuyên nghiên cứu dược tính mới. Hai mươi học đồ phần lớn là phàm nhân đang theo học, được giao các công việc cơ bản như phơi tảo, nghiền bột, canh lửa lò đan. Thu nhập chính từ bán Tảo Linh Giải Độc Đan cho thương nhân biển, nhưng giá cả bấp bênh phụ thuộc vào mùa vụ và số lượng khách hàng. Hội không có hệ thống quân sự hay lực lượng tự vệ, phụ thuộc vào sự kín đáo của vị trí và rừng tảo dày đặc để bảo vệ.

## V. Công Pháp & Trận Pháp (功法 与 阵法)
Hội không có công pháp chiến đấu, chỉ nắm giữ Thủy Tức Pháp — kỹ thuật thở dưới nước bằng cách hấp thu oxy từ tảo linh xung quanh, cho phép nhân tộc hoạt động dưới biển sâu mà không cần pháp bảo hỗ trợ. Đây là phát minh độc đáo của Hà Thanh Liên, kết hợp kiến thức y dược với hiểu biết về sinh thái tảo linh. Dược phương gia truyền gồm Tảo Linh Giải Độc Đan — giải hầu hết các loại độc thủy hệ và một số tà độc cơ bản, và Hải Thảo Hồi Khí Tán — bột thuốc hít vào giúp hồi phục linh lực nhanh chóng dưới nước. Hiệu quả dược phẩm tảo linh bị giới tu luyện đất liền hoài nghi vì nguyên liệu lạ lẫm, nhưng ngư dân biển tin dùng tuyệt đối vì đã được chứng minh qua hàng trăm ca thực tế.

## VI. Đặc Sản Môn Phái (门派特产)
- **Tảo Linh Giải Độc Đan:** Viên đan màu xanh lục trong suốt, bào chế từ Ngân Tảo và Bích Tảo, có tác dụng giải hầu hết các loại độc thủy hệ. Là sản phẩm bán chạy nhất, mỗi ngư dân ra khơi đều mang theo vài viên phòng thân.
- **Hải Thảo Hồi Khí Tán:** Bột thuốc nghiền mịn từ Bích Tảo khô, hít vào qua mũi giúp hồi phục linh lực nhanh chóng khi chiến đấu hoặc tu luyện dưới nước. Tác dụng phụ là hơi thở có mùi tảo biển suốt vài ngày.
- **Huyết Tảo Cao:** Cao dán bào chế từ Huyết Tảo, dùng đắp lên vết thương nội ngoại đều có hiệu quả. Đặc biệt hữu ích cho thương tích do hải thú gây ra.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Động Tảo Xanh:** Hang động tự nhiên ẩn giữa rừng tảo dày đặc, bên trong được cải tạo thành vừa là nơi ở vừa là xưởng bào chế. Tường hang phủ đầy tảo phát quang tạo ánh sáng xanh dịu, đủ để làm việc mà không cần đèn.
- **Lò Đan Hải Thảo:** Ba lò đan nhỏ đặt sâu trong hang, dùng nhiệt từ mạch nước nóng ngầm thay vì lửa thông thường. Đây là thiết kế độc đáo của Hà Thanh Liên, tận dụng địa nhiệt để bào chế dược phẩm dưới nước.
- **Vườn Tảo Thí Nghiệm:** Khu vực riêng nơi Hà Thanh Liên trồng và thí nghiệm các giống tảo linh mới, được bảo vệ bằng rào cản tảo dày và dòng hải lưu nhân tạo.

## VIII. Kinh Tế (经济)
Kinh tế của hội phụ thuộc gần như hoàn toàn vào việc bán dược phẩm tảo linh. Tảo Linh Giải Độc Đan là sản phẩm chủ lực, chiếm hơn sáu phần mười doanh thu, chủ yếu bán cho ngư dân, thương nhân biển, và Ngư Dân Tu Luyện Hội. Hải Thảo Hồi Khí Tán và Huyết Tảo Cao bán ít hơn nhưng lợi nhuận cao hơn vì nguyên liệu quý hiếm. Ngoài ra, hội nhận chữa bệnh cho ngư dân và thương nhân đi ngang qua vùng biển phía tây, thu phí bằng linh thạch hoặc vật tư. Giá cả bấp bênh theo mùa — mùa hải lưu ấm, tảo mọc tốt, giá giảm; mùa hải lưu lạnh, tảo khan hiếm, giá tăng nhưng sản lượng giảm. Thu nhập đủ sống nhưng không dư dả, phần lớn lợi nhuận được đầu tư lại vào nghiên cứu.

## IX. Lịch Sử Tóm Tắt (简史)
Hà Thanh Liên vốn là đệ tử xuất sắc của Dược Vương Cốc trên đất liền, nhưng bị trục xuất vì nghiên cứu dược liệu biển — thứ mà sư phụ coi là "tà dược" không xứng đáng với y đạo chính thống. Không nản lòng, bà lặn xuống biển sâu tìm nguyên liệu và tình cờ phát hiện rừng tảo linh khổng lồ phía tây Vô Tận Hải. Nhận ra tiềm năng dược tính vô tận của tảo linh, bà quyết định ở lại và dành hàng thập kỷ nghiên cứu. Dần dần, những người bị y giới đất liền từ chối hoặc ngư dân muốn học nghề tìm đến, hình thành hội nghề nhỏ chuyên cung cấp dược liệu biển. Dù quy mô khiêm tốn, sản phẩm của hội đã cứu sống hàng nghìn ngư dân bị nhiễm độc hải thú, chứng minh giá trị của dược liệu biển mà Dược Vương Cốc từng phủ nhận.

## X. Giai Thoại & Bí Mật (轶事 与 秘密)
Hà Thanh Liên đã phát hiện một loại tảo cực hiếm mọc sâu nhất trong rừng tảo, gọi là Tảo Trường Sinh — loại tảo có khả năng kéo dài tuổi thọ đáng kể khi bào chế đúng cách. Bà giấu kín phát hiện này vì lo sợ các thế lực lớn sẽ cướp đoạt rừng tảo nếu biết tin. Trong rừng tảo sâu nhất có xác một con hải thú khổng lồ từ thời thượng cổ — tảo linh mọc trên xác nó, hấp thu tinh hoa thi thể qua hàng nghìn năm, đây chính là nguồn gốc dược tính đặc biệt của rừng tảo. Một số học đồ báo cáo nhìn thấy bóng hình mờ ảo di chuyển trong rừng tảo vào ban đêm — Hà Thanh Liên nghiêm cấm mọi người đi sâu sau hoàng hôn, nhưng bản thân bà biết đó là linh hồn tàn dư của con hải thú, vẫn chưa siêu thoát hoàn toàn.

## XI. Quan Hệ Thế Lực (势力关系)
Hải Thảo Dược Sư giữ thái độ trung lập và kín đáo, không tham gia chính trị hay tranh chấp. Hải Tảo Nông Dân Hội là đối tác cung ứng quan trọng nhất, cung cấp tảo linh nguyên liệu cơ bản, đổi lại nhận thuốc chữa bệnh miễn phí — hai bên phụ thuộc lẫn nhau trong chuỗi cung ứng. Ngư Dân Tu Luyện Hội là nhóm khách hàng trung thành nhất, tin dùng dược phẩm tảo linh trong mọi chuyến ra khơi. Hải Thần Cung biết đến sự tồn tại của hội nhưng không quan tâm vì quy mô quá nhỏ — điều này vừa là sự may mắn vừa là nỗi buồn, vì Hà Thanh Liên muốn dược liệu biển được công nhận rộng rãi nhưng không dám thu hút sự chú ý.
