---
type: faction
name: San Hô Vi Trùng
hantu: 珊瑚微虫
faction_type: Bộ Lạc
alignment: 0
race: Vi Trùng (Sinh vật cực nhỏ)
region: Tây Mạc
founded: Thượng Cổ (trước cả Long Cung và Hải Thần Cung)
founder: Không có (tồn tại từ thuở khai thiên lập địa)
emblem: San_Ho_Vi_Trung.png
specialty: Xây dựng san hô linh, Chuyển hóa linh khí thành khoáng linh, Lưu giữ ký ức địa chất
economy:
- Không có hoạt động kinh tế — sinh vật bản năng thuần túy
arcs:
  - arc: 1
    status: Đang bị Huyết Độc giết chết hàng loạt
    rank: Không Xếp Hạng
    leader: San Hô Mẫu Trùng
    population: 0
    territory:
      - Toàn bộ rạn san hô trong Vô Tận Hải
    assets:
      - name: Rạn san hô cổ nhất Vô Tận Hải
        type: Tài Nguyên
      - name: Hóa thạch linh trong cấu trúc san hô
        type: Tài Nguyên
    stats: [5, 50, 5, 50, 10, 5]
    divisions:
      - name: San Hô Mẫu Trùng
        role: Điều phối hướng xây dựng san hô, duy trì trật tự tập thể
        headcount:
          truong_lao: 1
          chien_binh: 0
          dan_thuong: 0
        members:
          - character: San Hô Mẫu Trùng
            position: Mẫu Trùng
            cultivation: Luyện Khí (tương đương)
      - name: Vi Trùng Thợ Xây
        role: Tiết ra chất khoáng linh để xây dựng san hô linh liên tục
        headcount:
          truong_lao: 0
          chien_binh: 0
          dan_thuong: 0
        members:
          - character: "[Vi Trùng Thợ]"
            position: Vi Trùng
            cultivation: Không có tu vi
            placeholder: true
    relationships:
      - faction: San Hô Thủ Hộ Đoàn
        description: Được Thủ Hộ Đoàn tôn trọng như tổ tiên và bảo vệ vô điều kiện. Vi Trùng không có linh trí đủ để nhận thức mối quan hệ này.
        diplomacy:
          lien_minh: 50
          tin: 30
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 0
      - faction: San Hô Thợ Lặn Đội
        description: Sản phẩm của Vi Trùng (san hô linh) bị thợ lặn thu hoạch. Vi Trùng không nhận thức được mối quan hệ khai thác này.
        diplomacy:
          lien_minh: 0
          tin: 0
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 0
      - faction: Hải Tộc (toàn bộ vùng biển)
        description: Vi Trùng là nền tảng sinh thái cho mọi Hải Tộc, nhưng hầu hết Hải Tộc không nhận thức sự tồn tại của chúng.
        diplomacy:
          lien_minh: 0
          tin: 0
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 0
---

# San Hô Vi Trùng (珊瑚微虫)

> *"Sinh vật nhỏ nhất xây nên công trình lớn nhất — đó là đạo lý mà cả thiên hạ tu sĩ đều quên."*
> — Trích bút ký của Hải Quy trưởng lão Huyền Quy

## I. Tổng Quan (总览)
San Hô Vi Trùng là loài sinh vật cực nhỏ tồn tại từ thời thượng cổ, trước cả khi Long Cung hay Hải Thần Cung được thành lập. Mỗi con Vi Trùng nhỏ hơn một hạt cát, nhưng hàng tỷ con cùng làm việc không ngừng nghỉ qua hàng triệu năm đã tạo nên toàn bộ rạn san hô linh trong Vô Tận Hải — từ Bạch San Hô Lĩnh trải dài như dãy núi ngầm dưới đáy biển đến Hồng San Hô Viên ở vùng nước nông phía đông, mỗi rạn đều là kiệt tác kiến trúc sống của hàng nghìn thế hệ Vi Trùng. Chúng không có linh trí theo nghĩa thông thường, hành động hoàn toàn theo bản năng xây dựng, nhưng chính sự tồn tại thầm lặng của chúng là nền tảng cho toàn bộ hệ sinh thái biển. Không ai coi chúng là một "thế lực", nhưng nếu San Hô Vi Trùng biến mất, hệ sinh thái Vô Tận Hải sẽ sụp đổ hoàn toàn.

## II. Địa Lý & Tài Nguyên (地理与资源)
San Hô Vi Trùng sống bên trong và trên bề mặt mọi rạn san hô trong Vô Tận Hải, phân bố rộng khắp từ vùng nước nông ven bờ đến những rạn san hô sâu dưới đáy biển. Nơi nào có san hô linh là nơi đó có sự hiện diện của Vi Trùng — từ Đại San Hô Trường Thành chạy dài hơn nghìn dặm ở biên giới đông nam, đến quần thể Tử San Hô Đàn nhỏ bé quanh chân San Hô Đảo Quốc. Mỗi con Vi Trùng liên tục tiết ra chất khoáng linh, dần dần kết tinh thành cấu trúc san hô cứng cáp trong quá trình kéo dài hàng nghìn năm. Tốc độ xây dựng cực kỳ chậm chạp, một cành san hô nhỏ bằng ngón tay mất hàng trăm năm mới hình thành — học giả Hải Tộc gọi đó là "Vạn Niên Nhất Chỉ" để minh họa cho sự kiên nhẫn siêu phàm. Tài nguyên lớn nhất mà Vi Trùng sở hữu chính là thời gian và sự kiên nhẫn vô hạn, thứ mà không tông môn hay thế lực nào có thể sánh được.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
San Hô Vi Trùng là sinh vật cực nhỏ, không có văn hóa hay tín ngưỡng theo nghĩa thông thường. Chúng hành động hoàn toàn theo bản năng xây dựng được mã hóa trong cấu trúc sinh học: suốt đời tiết ra chất khoáng linh, chết đi thì thế hệ sau tiếp tục công việc chưa hoàn thành — xác chúng hòa vào thân san hô, trở thành một phần của công trình mà mình đã cống hiến cả đời. Chu kỳ sống ngắn ngủi nhưng công trình kéo dài hàng triệu năm. Các Hải Tộc khác coi chúng là "thợ xây vô hình", nền tảng thầm lặng của toàn bộ hệ sinh thái rạn san hô. San Hô Thủ Hộ Đoàn tôn trọng chúng như tổ tiên, dù hai bên không thể giao tiếp. Thủy Linh Nhi từng dạy đệ tử: "Ngươi thấy rạn san hô hùng vĩ ư? Đó là mồ hôi của vạn ức sinh linh mà mắt ngươi không nhìn thấy — hãy cúi đầu tạ ơn trước khi bước lên."

## IV. Cơ Cấu Tổ Chức (组织结构)
Cơ cấu tổ chức của San Hô Vi Trùng không theo bất kỳ mô hình quản lý nào, mà hoạt động theo bản năng tập thể. San Hô Mẫu Trùng là con Vi Trùng lớn nhất trong đàn, đóng vai trò điều phối hướng xây dựng san hô bằng cách tiết ra tín hiệu hóa học — loại tín hiệu mà Hải Quy trưởng lão gọi là "Kiến Trúc Chi Ngữ," ngôn ngữ xây dựng của Vi Trùng. Hàng tỷ Vi Trùng Thợ, mỗi con nhỏ hơn hạt cát, tiếp nhận tín hiệu và làm việc không ngừng nghỉ. Khi San Hô Mẫu Trùng chết đi, con Vi Trùng lớn nhất trong đàn sẽ dần phát triển để kế thừa vai trò, quá trình chuyển giao diễn ra âm thầm qua hàng chục năm mà không gây xáo trộn cho hoạt động xây dựng. Mỗi rạn san hô lớn thường có một Mẫu Trùng riêng, và các Mẫu Trùng ở các rạn khác nhau hoạt động độc lập — không có hệ thống chỉ huy liên rạn.

## V. Công Pháp & Trận Pháp (功法与阵法)
San Hô Vi Trùng không có công pháp, quá trình chuyển hóa linh khí trong nước biển thành chất khoáng linh là bản năng sinh học thuần túy, không cần tu luyện hay truyền dạy. Tuy nhiên, khi rạn san hô bị đe dọa nghiêm trọng, Vi Trùng có khả năng phản ứng phòng vệ bằng cách tăng tốc tiết chất khoáng linh, bọc kín kẻ xâm nhập trong lớp san hô đang kết tinh — ngư dân gọi hiện tượng này là "San Hô Phong Ấn," và trong rạn san hô cổ nhất đôi khi tìm thấy xác sinh vật bị bọc kín hoàn toàn trong san hô linh, giữ nguyên hình dạng từ hàng vạn năm trước. Quá trình này rất chậm, chỉ hiệu quả với những sinh vật bất động hoặc di chuyển chậm, hoàn toàn vô hại với tu sĩ có tu vi cao. Dù vậy, đã có ghi chép về một Hải Tộc trưởng lão vô tình ngủ quên trong hang san hô cổ và tỉnh dậy thấy hai chân bị bọc kín — phải nhờ đệ tử đục mất nửa ngày mới thoát.

## VI. Đặc Sản Môn Phái (门派特产)
Sản phẩm duy nhất của San Hô Vi Trùng chính là san hô linh, thứ được hình thành qua hàng nghìn năm tích lũy chất khoáng linh. San hô linh có giá trị sử dụng đa dạng: làm nguyên liệu phụ trong luyện đan, trang trí linh khí, chế tạo pháp khí thủy hệ cấp thấp, và làm nền tảng nuôi dưỡng các loại dược liệu biển. Đặc biệt, san hô linh lấy từ rạn Hồng San Hô Viên có sắc đỏ rực và linh khí thuần khiết hơn loại thường, được các dược sư ưa chuộng để luyện "San Hô Dưỡng Nhan Đan." Ngoài ra, cấu trúc san hô cổ nhất chứa hóa thạch linh, trong đó ẩn giấu thông tin về lịch sử Vô Tận Hải từ thuở khai thiên lập địa, tuy chưa ai giải mã được.

## VII. Cơ Sở Hạ Tầng (基础设施)
San Hô Vi Trùng không xây dựng cơ sở hạ tầng theo nghĩa thông thường, nhưng chính bản thân rạn san hô do chúng tạo ra chính là công trình kiến trúc vĩ đại nhất Vô Tận Hải. Mỗi rạn san hô là một mê cung phức tạp gồm hàng triệu ngóc ngách, hang động, và hành lang, cung cấp nơi ẩn náu cho vô số loài sinh vật biển. Rạn san hô cổ nhất — Thái Cổ San Hô Lĩnh — có tuổi đời ước tính hàng triệu năm, lớp ngoài cùng vẫn đang được Vi Trùng xây dựng tiếp trong khi lõi bên trong đã hóa thạch từ lâu, tạo thành cấu trúc phân tầng mà Hải Quy học giả ví như "cuốn biên niên sử bằng đá." Các hang động lớn nhất trong rạn san hô cổ đôi khi được Hải Tộc sử dụng làm nơi ẩn cư hoặc kho chứa, nhưng họ cẩn thận không phá vỡ cấu trúc xung quanh để tránh làm sập toàn bộ rạn.

## VIII. Kinh Tế (经济)
San Hô Vi Trùng không có bất kỳ hoạt động kinh tế nào. Chúng không trao đổi, không buôn bán, không tích trữ. Tuy nhiên, sản phẩm mà chúng vô tình tạo ra, san hô linh, lại là nguồn tài nguyên kinh tế quan trọng cho nhiều thế lực khác. San Hô Thợ Lặn Đội thu hoạch san hô linh để bán cho Thiên Sa Thương Hội, các tông môn luyện đan mua san hô linh làm nguyên liệu phụ, và nhiều tu sĩ thủy hệ sử dụng san hô linh trong tu luyện. Riêng tại chợ San Hô Đảo Quốc, mỗi năm giao dịch san hô linh đạt giá trị hơn hai vạn linh thạch hạ phẩm — con số ấn tượng cho một sản phẩm do sinh vật không có ý thức tạo ra. Nghịch lý là sinh vật nhỏ bé nhất lại tạo ra nền tảng cho chuỗi kinh tế biển rộng lớn.

## IX. Lịch Sử Tóm Tắt (简史)
San Hô Vi Trùng tồn tại từ thời thượng cổ, trước cả khi có Long Cung hay Hải Thần Cung. Mọi rạn san hô trong Vô Tận Hải đều là công trình của chúng qua hàng triệu năm kiên nhẫn xây dựng, thế hệ nối tiếp thế hệ không ngừng nghỉ. Trong suốt lịch sử dài đằng đẵng đó, Vi Trùng chưa bao giờ tham gia vào bất kỳ cuộc chiến tranh hay xung đột nào, chỉ lặng lẽ làm việc và để lại công trình cho hậu thế. Hải Tộc trưởng lão có câu: "Đế vương hưng vong trong ngàn năm, nhưng san hô vẫn xây trong vạn năm — ai mới là kẻ bền bỉ nhất đại dương?" Gần đây, Huyết Độc từ Nam Cương đang giết chết Vi Trùng hàng loạt, khiến san hô linh chuyển sang màu trắng bạch — hiện tượng mà ngư dân gọi là "Bạch Cốt Hải," vì rạn san hô trắng xóa trông như nghĩa địa xương dưới đáy biển. Nếu tình trạng này tiếp tục, hàng triệu năm công sức xây dựng có thể bị xóa sổ trong vài thập kỷ.

## X. Giai Thoại & Bí Mật (轶事与秘密)
Có giả thuyết trong giới học giả Hải Tộc rằng San Hô Mẫu Trùng lưu giữ ký ức tập thể từ thời thượng cổ trong cấu trúc tinh thể của san hô. Nếu giả thuyết này đúng, rạn san hô cổ nhất chính là cuốn sử sách lớn nhất Vô Tận Hải, ghi lại mọi biến cố từ khi khai thiên lập địa. Rạn san hô cổ nhất chứa hóa thạch linh với cấu trúc phức tạp đến mức không ai giải mã nổi, có học giả tin rằng đó là "ngôn ngữ" của Vi Trùng, ghi chép lại lịch sử Vô Tận Hải bằng cách mã hóa thông tin vào khoáng chất — mỗi lớp khoáng linh tương ứng với một giai đoạn lịch sử, giống như vân gỗ cổ thụ ghi lại từng mùa mưa nắng. Gần đây, hiện tượng san hô bạch hóa do Huyết Độc không chỉ giết chết Vi Trùng mà còn có thể phá hủy vĩnh viễn những "hồ sơ" thượng cổ này. Thủy Linh Nhi từng khóc khi chứng kiến một rạn san hô nghìn năm bạch hóa: "Chúng ta không chỉ mất san hô — chúng ta đang đốt cháy thư viện của biển cả."

## XI. Quan Hệ Thế Lực (势力关系)
- **San Hô Thủ Hộ Đoàn:** Được tôn trọng và bảo vệ vô điều kiện bởi đoàn. Thủy Linh Nhi coi Vi Trùng như tổ tiên của rạn san hô, dù hai bên không thể giao tiếp. Đoàn tuần tra các rạn san hô mỗi tháng để kiểm tra tình trạng bạch hóa và xua đuổi kẻ khai thác trái phép.
- **San Hô Thợ Lặn Đội:** Thợ lặn thu hoạch sản phẩm của Vi Trùng nhưng tuân thủ quy tắc khai thác bền vững do Thủ Hộ Đoàn đặt ra, chỉ lấy san hô ở lớp ngoài cùng và chừa lại phần lõi đang phát triển, không đe dọa sự tồn vong của loài.
- **Hải Tộc (toàn bộ vùng biển):** Vi Trùng là nền tảng sinh thái cho mọi Hải Tộc, nhưng hầu hết Hải Tộc không nhận thức sự tồn tại của sinh vật nhỏ bé này. Chỉ khi rạn san hô bạch hóa, cá chết nổi trắng mặt nước và ngư trường biến mất, họ mới bắt đầu hỏi: "Chuyện gì đã xảy ra?"
