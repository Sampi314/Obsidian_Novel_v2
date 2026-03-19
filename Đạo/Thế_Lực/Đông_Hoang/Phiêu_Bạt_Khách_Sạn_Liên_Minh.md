---
type: faction
name: Phiêu Bạt Khách Sạn Liên Minh
hantu: 漂泊客栈联盟
faction_type: Liên Minh
alignment: 2
race: Đa chủng tộc (chủ yếu Nhân Tộc, Bán Yêu)
region: Đông Hoang
founded: 70 năm trước
founder: Phiêu Mẫu (Chưởng Quầy đầu tiên)
emblem: Phieu_Bat_Khach_San_Lien_Minh.png
specialty: Lưu trú, Trung gian giao dịch, Buôn bán tin tức, Bảo mật thông tin
economy:
- Tiền phòng lưu trú và ẩm thực
- Bán tin tức cho tán tu và thương nhân
- Trung gian giao dịch giữa các thế lực nhỏ
arcs:
  - arc: 1
    status: Hoạt động ổn định
    rank: Hạng Năm
    leader: Minh Chủ Phiêu Mẫu (danh nghĩa, thực tế các chi nhánh tự quản)
    population: 50
    territory:
      - 7 khách sạn rải rác dọc tuyến đường thương mại quanh Vạn Yêu Thành
      - Ngã ba đường và cửa rừng Đông Hoang
    assets:
      - name: Mạng lưới truyền thư linh cầm
        type: Tài Nguyên
      - name: Phiêu Bạt Lệnh (thẻ gỗ khách quen)
        type: Trang Bị
      - name: 7 khách sạn liên minh
        type: Công Trình
    stats: [30, 60, 80, 50, 40, 90]
    divisions:
      - name: Thất Đại Chi Nhánh
        role: Bảy khách sạn độc lập, mỗi nơi do một Chưởng Quầy điều hành, phối hợp qua truyền thư linh cầm
        headcount:
          minh_chu: 1
          pho_minh_chu: 0
          truong_lao: 0
          su_gia: 6
          thanh_vien_phai: 43
        members:
          - character: Phiêu Mẫu
            position: Minh Chủ (Chưởng Quầy chi nhánh chính)
            cultivation: Trúc Cơ Viên Mãn
          - character: "[Chưởng Quầy Nhị]"
            position: Sứ Giả (Chưởng Quầy chi nhánh 2)
            cultivation: Trúc Cơ Trung Kỳ
            placeholder: true
          - character: "[Chưởng Quầy Tam]"
            position: Sứ Giả (Chưởng Quầy chi nhánh 3)
            cultivation: Trúc Cơ Sơ Kỳ
            placeholder: true
    relationships:
      - faction: Ngoại Môn Đệ Tử Liên Minh
        description: Một trong bảy chi nhánh bí mật là điểm liên lạc của Ngoại Môn Đệ Tử Liên Minh. Chưởng Quầy chi nhánh đó không biết — hoặc giả vờ không biết — khách hàng thực sự đang làm gì phía sau cánh cửa đóng kín.
        diplomacy:
          lien_minh: 0
          tin: 0
          uy_hiep: 0
          thuong_mai: 10
          on_oan: 0
          le_thuoc: 0
      - faction: Hoang Dã Thợ Săn Bang
        description: Thợ săn bang thường xuyên thuê phòng tại các chi nhánh làm nơi nghỉ chân giữa các chuyến đi. Quan hệ thuần túy thương mại nhưng ổn định, cả hai bên đều có lợi.
        diplomacy:
          lien_minh: 10
          tin: 20
          uy_hiep: 0
          thuong_mai: 50
          on_oan: 0
          le_thuoc: 0
      - faction: Vạn Yêu Thành
        description: Liên Minh hoạt động ở ngoại vi Vạn Yêu Thành, được thành ngầm cho phép tồn tại nhờ tính trung lập. Đôi khi chính quyền thành mua tin từ Liên Minh, nhưng cũng ngầm theo dõi.
        diplomacy:
          lien_minh: 5
          tin: 10
          uy_hiep: 20
          thuong_mai: 30
          on_oan: 0
          le_thuoc: 20
---

# Phiêu Bạt Khách Sạn Liên Minh (漂泊客栈联盟)

## I. Tổng Quan (总览)
Phiêu Bạt Khách Sạn Liên Minh là mạng lưới bảy khách sạn rải rác dọc các tuyến đường thương mại quanh Vạn Yêu Thành, phục vụ tán tu, thương nhân, và mọi kẻ phiêu bạt không phân biệt chính tà. Dù chỉ xếp Hạng Năm về quy mô với khoảng năm mươi nhân viên, Liên Minh sở hữu thứ mà nhiều thế lực lớn hơn thèm muốn: mạng lưới thông tin rộng khắp về hoạt động tán tu toàn Đông Hoang. Triết lý "Vào cửa là khách, không phân tà chính" đã giúp Liên Minh tồn tại bảy mươi năm qua mà không bị cuốn vào bất kỳ cuộc xung đột nào, biến mỗi khách sạn thành vùng đất trung lập nơi kẻ thù có thể ngồi cùng bàn mà không rút kiếm.

## II. Địa Lý & Tài Nguyên (地理与资源)
Bảy khách sạn nằm rải rác tại các vị trí chiến lược dọc tuyến đường thương mại chính quanh Vạn Yêu Thành. Mỗi chi nhánh thường tọa lạc ở ngã ba đường hoặc cửa rừng — những nơi lữ khách bắt buộc phải dừng chân nghỉ ngơi trước khi tiếp tục hành trình. Kiến trúc mỗi khách sạn là tòa nhà gỗ đơn sơ hai hoặc ba tầng, bên ngoài trông tầm thường nhưng bên trong trang bị trận pháp cách âm và phòng thủ cấp thấp, đủ để đảm bảo an toàn cho khách. Tài nguyên chính của Liên Minh không phải phòng ốc mà là tin tức — hàng ngày, hàng trăm tán tu ghé qua trò chuyện, trao đổi, và vô tình tiết lộ thông tin về hoạt động khắp nơi. Hệ thống truyền thư linh cầm đơn giản kết nối bảy chi nhánh, cho phép tin tức lan truyền giữa các điểm trong vòng một ngày.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
"Vào cửa là khách, không phân tà chính" — đây không chỉ là khẩu hiệu mà là luật tối cao của Liên Minh, được khắc trên tấm bảng gỗ treo tại quầy tiếp tân mỗi chi nhánh. Bất kỳ ai trả tiền và không gây sự đều được tiếp đón, dù là tán tu lang thang, thương nhân giàu có, hay kẻ đào tẩu bị truy nã. Quy tắc nghiêm ngặt nhất là cấm đánh nhau trong khách sạn — ai vi phạm sẽ bị cấm cửa toàn bộ Liên Minh vĩnh viễn, danh tính được truyền đến tất cả bảy chi nhánh trong ngày. Thông tin khách hàng là tuyệt đối bảo mật: Chưởng Quầy thà mất mạng còn hơn tiết lộ ai đã ở đây đêm qua. Khách quen được tặng "Phiêu Bạt Lệnh" — thẻ gỗ đặc biệt cho phép giảm giá và ưu tiên phòng tốt ở mọi chi nhánh, trở thành dấu hiệu nhận diện của những kẻ lãng du kỳ cựu.

## IV. Cơ Cấu Tổ Chức (组织结构)
Liên Minh vận hành theo mô hình phân quyền triệt để. Mỗi chi nhánh do một Chưởng Quầy cảnh giới Trúc Cơ tự quản, có quyền quyết định mọi việc tại chi nhánh mình mà không cần xin phép ai. Phiêu Mẫu — Chưởng Quầy chi nhánh chính và cũng là người sáng lập — giữ vai trò Minh Chủ danh nghĩa, chỉ can thiệp khi có quyết định ảnh hưởng đến toàn bộ Liên Minh. Sáu Chưởng Quầy còn lại đóng vai trò Sứ Giả, mỗi người quản lý từ năm đến tám nhân viên gồm phục vụ, canh gác, và đầu bếp, đa số cảnh giới Luyện Khí. Tổng cộng khoảng năm mươi người, quy mô nhỏ nhưng hiệu quả. Các chi nhánh trao đổi tin tức qua hệ thống truyền thư linh cầm đơn giản, họp mặt chung mỗi năm một lần tại chi nhánh chính để thống nhất giá cả và chia sẻ tin tức quan trọng.

## V. Công Pháp & Trận Pháp (功法与阵法)
Liên Minh không có công pháp riêng biệt — nhân viên sử dụng kỹ thuật tu luyện cá nhân, đa phần là tán tu với công pháp tạp nham. Điểm mạnh phòng thủ nằm ở trận pháp: mỗi khách sạn được trang bị trận pháp cách âm và phòng thủ cấp thấp do phù sư thuê ngoài thiết lập, đủ sức ngăn chặn Luyện Khí gây rối và khiến Trúc Cơ phải suy nghĩ trước khi hành động. Một số chi nhánh ở vị trí nguy hiểm hơn còn có thêm trận pháp cảnh báo xâm nhập quanh chu vi, giúp Chưởng Quầy phát hiện kẻ lạ đến gần từ xa. Tuy nhiên, đây chỉ là biện pháp phòng thủ thụ động — nếu đối mặt cường giả Kim Đan trở lên, Liên Minh hoàn toàn bất lực.

## VI. Đặc Sản Môn Phái (门派特产)
- **Phiêu Bạt Lệnh:** Thẻ gỗ khắc danh hiệu Liên Minh, cấp cho khách quen đã lưu trú trên mười lần. Người sở hữu được giảm ba mươi phần trăm giá phòng và ưu tiên phòng tốt nhất tại mọi chi nhánh.
- **Trà Phiêu Bạt:** Loại trà thảo mộc đặc chế từ thảo dược hoang dã, có tác dụng giải mệt và an thần nhẹ. Mỗi chi nhánh có công thức riêng, khách quen thường ghé chi nhánh nào chỉ để thưởng thức vị trà đặc trưng nơi đó.
- **Tin Tức Đường Trường:** Dịch vụ ngầm nhưng ai cũng biết — trả thêm linh thạch, Chưởng Quầy sẽ chia sẻ tin tức về tình hình đường đi, linh thú xuất hiện, hoặc các thế lực hoạt động dọc tuyến.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Thất Đại Chi Nhánh:** Bảy khách sạn gỗ hai đến ba tầng, mỗi nơi có từ năm đến mười phòng cho khách, quầy ẩm thực tầng trệt, và phòng riêng cho Chưởng Quầy. Kiến trúc đơn sơ nhưng chắc chắn, phù hợp với lữ khách không cần xa hoa.
- **Hệ Thống Truyền Thư Linh Cầm:** Mạng lưới linh cầm cấp thấp (chim nhỏ đã được thuần hóa) kết nối bảy chi nhánh, cho phép truyền tin nhắn ngắn trong vòng một ngày.
- **Kho Dự Trữ:** Mỗi chi nhánh có hầm nhỏ chứa lương thực, dược liệu cơ bản, và vài pháp khí phòng thân cho nhân viên khi khẩn cấp.

## VIII. Kinh Tế (经济)
Kinh tế Liên Minh dựa trên ba nguồn thu chính. Thứ nhất là tiền phòng và ẩm thực — nguồn thu ổn định nhất, dù giá cả vừa phải, lượng khách đều đặn quanh năm nhờ vị trí chiến lược trên tuyến đường thương mại. Thứ hai là bán tin tức — Chưởng Quầy thu thập thông tin từ khách ghé qua rồi bán lại cho tán tu, thương nhân, hoặc thế lực nhỏ cần nắm tình hình. Dịch vụ này mang lại lợi nhuận cao nhưng phải cẩn thận — bán nhầm tin cho sai người có thể gây thù oán. Thứ ba là trung gian giao dịch: khách sạn đóng vai trò điểm hẹn để hai bên trao đổi hàng hóa, Liên Minh thu phí trung gian nhỏ và đảm bảo an toàn cho cả hai bên trong quá trình giao dịch.

## IX. Lịch Sử Tóm Tắt (简史)
Bảy mươi năm trước, Phiêu Mẫu chỉ là một tán tu nữ Trúc Cơ mở quán trọ nhỏ ở ngã ba đường gần Vạn Yêu Thành. Khi vài chủ quán tán tu khác ở các vị trí lân cận nhận ra rằng hợp tác chia sẻ tin tức có lợi hơn cạnh tranh, họ tự nhiên hình thành mạng lưới. Phiêu Mẫu — người có uy tín và cảnh giới cao nhất — trở thành Minh Chủ danh nghĩa, thiết lập hệ thống truyền thư linh cầm và quy tắc chung. Dần dần, mạng lưới mở rộng lên bảy chi nhánh, mỗi nơi do một Chưởng Quầy tự quản. Liên Minh tồn tại được suốt bảy thập kỷ nhờ tính trung lập tuyệt đối — không đứng về bên nào trong bất kỳ cuộc xung đột nào, dù đôi khi phải nuốt nhục khi cường giả uy hiếp.

## X. Giai Thoại & Bí Mật (轶事与秘密)
Một trong bảy chi nhánh bí mật là điểm liên lạc của Ngoại Môn Đệ Tử Liên Minh, nhưng các Chưởng Quầy khác hoàn toàn không biết. Chưởng Quầy chi nhánh đó nhận thêm thu nhập từ việc cho thuê phòng kín mà không hỏi mục đích, coi đây chỉ là giao dịch bình thường. Ngoài ra, Liên Minh nắm giữ lượng lớn tin tức tích lũy suốt bảy mươi năm về hoạt động tán tu ở Đông Hoang — nếu bán toàn bộ cho một thế lực lớn, giá trị có thể ngang hàng với kho bảo vật của một tông phái Hạng Ba. Tuy nhiên, Phiêu Mẫu hiểu rằng làm vậy sẽ phá hủy uy tín bảo mật mà Liên Minh xây dựng suốt nhiều thập kỷ, và khi mất uy tín, Liên Minh sẽ chẳng còn gì.

## XI. Quan Hệ Thế Lực (势力关系)
- **Ngoại Môn Đệ Tử Liên Minh:** Một chi nhánh vô tình cung cấp điểm hẹn cho tổ chức bí mật này. Quan hệ đơn phương — Ngoại Môn Đệ Tử Liên Minh lợi dụng tính bảo mật của khách sạn, còn Phiêu Bạt chỉ biết đó là khách thuê phòng bình thường.
- **Hoang Dã Thợ Săn Bang:** Thợ săn bang là nhóm khách hàng trung thành nhất, thường xuyên thuê phòng và mua tin tức về linh thú dọc đường. Quan hệ thương mại ổn định, lâu dài, có lợi cho cả hai bên.
- **Vạn Yêu Thành:** Liên Minh hoạt động ở ngoại vi thành, được chính quyền ngầm cho phép tồn tại nhờ tính trung lập và đôi khi cung cấp tin tức. Tuy nhiên, Liên Minh cũng bị thành theo dõi để đảm bảo không trở thành mối đe dọa.
