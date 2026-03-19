---
type: faction
name: Lưu Sa Đào Binh
hantu: 流沙逃兵
faction_type: Quân Đoàn
alignment: -1
race: Đa chủng (Nhân Tộc, Sa Tộc)
region: Tây Mạc
founded: Không rõ (Tự phát từ hàng ngàn năm trước)
founder: '"Vô Danh" (Người tổ chức đầu tiên)'
emblem: Luu_Sa_Dao_Binh.png
specialty: Ẩn Sa Thuật, Du kích sa mạc, Đa dạng chiến thuật
economy:
- Cướp chọn lọc từ thương đoàn giàu có
- Đổi chác tài nguyên sa mạc
- Tự cung tự cấp trong Lưu Sa Khu
arcs:
  - arc: 1
    status: Ẩn mình hoạt động (Bí mật trong Lưu Sa Khu)
    rank: Không Xếp Hạng
    leader: Thủ Lĩnh "Vô Danh"
    population: 60
    territory:
      - Lưu Sa Khu (Trung tâm Hoàng Kim Sa Hải)
    assets:
      - name: Lưu Sa Khu (Vùng ẩn náu tự nhiên)
        type: Địa Lợi
      - name: Vũ khí đa nguồn gốc
        type: Quân Bị
    stats: [40, 15, 5, 30, 45, 10]
    divisions:
      - name: Đội Trinh Sát
        role: Dò đường, theo dõi thương đoàn và lực lượng truy sát
        headcount:
          tuong: 0
          uy: 2
          binh: 15
        members:
          - character: "[Phó Thủ Lĩnh Trinh Sát]"
            position: Phó Thủ Lĩnh
            cultivation: Trúc Cơ Sơ Kỳ
            placeholder: true
      - name: Đội Phòng Thủ
        role: Bảo vệ doanh trại di động, thiết lập bẫy cát
        headcount:
          tuong: 0
          uy: 2
          binh: 15
        members:
          - character: "[Phó Thủ Lĩnh Phòng Thủ]"
            position: Phó Thủ Lĩnh
            cultivation: Trúc Cơ Sơ Kỳ
            placeholder: true
      - name: Đội Hậu Cần
        role: Thu gom nước, lương thực và duy trì sinh hoạt
        headcount:
          tuong: 1
          uy: 0
          binh: 25
        members:
          - character: "[Vô Danh]"
            position: Thủ Lĩnh
            cultivation: Trúc Cơ Hậu Kỳ
            placeholder: true
    relationships:
      - faction: Thiên Sa Thương Hội
        description: Mục tiêu cướp chọn lọc. Đào Binh chỉ lấy từ thương đoàn giàu có, tránh đụng hộ vệ cấp cao.
        diplomacy:
          lien_minh: -30
          tin: -50
          uy_hiep: 10
          thuong_mai: -30
          on_oan: -20
          le_thuoc: 0
      - faction: Sa Tặc Liên Minh
        description: Cùng là thành phần ngoài vòng pháp luật nhưng không hợp tác. Sa Tặc coi Đào Binh là hèn nhát, Đào Binh coi Sa Tặc là tàn bạo.
        diplomacy:
          lien_minh: -20
          tin: -40
          uy_hiep: 20
          thuong_mai: 0
          on_oan: -30
          le_thuoc: 0
      - faction: Sa Mạc Hướng Đạo Hội
        description: Biết về sự tồn tại của Đào Binh nhưng giữ im lặng. Đôi khi hướng đạo vô tình dẫn đường tránh xa doanh trại Đào Binh.
        diplomacy:
          lien_minh: 0
          tin: 10
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 10
          le_thuoc: 0
---

# Lưu Sa Đào Binh (流沙逃兵)

## I. Tổng Quan (总览)
Lưu Sa Đào Binh là tổ chức ngầm quy tụ những kẻ đào ngũ từ các thế lực lớn nhỏ khắp Tây Mạc, ẩn náu trong vùng cát chảy liên tục tại trung tâm Hoàng Kim Sa Hải. Với khoảng sáu mươi thành viên đến từ đủ mọi nguồn gốc, Đào Binh là tập hợp của những kẻ từ chối chiến tranh và bạo lực vô nghĩa — họ không phải anh hùng, cũng không phải tội phạm, mà là những người chọn sống sót bằng cách biến mất khỏi thế giới tu luyện. Dưới sự tổ chức của thủ lĩnh bí ẩn mang biệt danh "Vô Danh", nhóm đào binh hỗn tạp này đã trở thành một lực lượng nhỏ nhưng có quy củ, sống theo nguyên tắc riêng giữa lòng sa mạc khắc nghiệt.

## II. Địa Lý & Tài Nguyên (地理与资源)
Đào Binh ẩn náu trong Lưu Sa Khu — vùng cát chảy liên tục tại trung tâm Hoàng Kim Sa Hải, nơi địa hình thay đổi mỗi ngày và không bản đồ nào ghi lại chính xác được. Chính sự bất ổn định này lại là tấm khiên bảo vệ tốt nhất: kể cả tu sĩ Kim Đan cũng khó truy tìm một nhóm người nhỏ trong vùng cát chảy bất tận. Tài nguyên của Đào Binh đến từ vũ khí cũ mang theo khi đào ngũ, nước và lương thực cướp được hoặc đổi chác từ các thương đoàn nhỏ. Doanh trại không bao giờ ở một chỗ quá ba ngày, di chuyển liên tục theo nhịp chảy của cát.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
Triết lý cốt lõi của Đào Binh là "Chiến tranh không phải của chúng ta — sống mới là của chúng ta." Không ai được hỏi quá khứ của ai, không ai dùng tên thật — mọi người đều là "Vô Danh" theo nghĩa rộng nhất. Khi có người mới gia nhập, nghi thức duy nhất là chôn toàn bộ đồ cũ mang theo xuống cát — biểu tượng cho việc xóa bỏ kiếp trước và bắt đầu lại. Cấm kỵ lớn nhất là quay lại thế lực cũ: bất kỳ ai vi phạm sẽ bị xử tử, không phải vì tàn nhẫn mà vì sự an toàn của toàn nhóm. Dù sống ngoài vòng pháp luật, Đào Binh giữ nguyên tắc không cướp bóc dân thường và không giết người vô tội.

## IV. Cơ Cấu Tổ Chức (组织结构)
Tổ chức của Đào Binh đơn giản và linh hoạt, phản ánh bản chất du kích của họ. Đứng đầu là "Vô Danh" — không ai biết tên thật, chỉ biết ông từng là quân nhân cấp cao Trúc Cơ Hậu Kỳ trong một thế lực đã bị tiêu diệt. Dưới ông là hai Phó Thủ Lĩnh Trúc Cơ Sơ Kỳ, một phụ trách trinh sát và một phụ trách phòng thủ. Khoảng sáu mươi thành viên còn lại đa phần ở cảnh giới Luyện Khí, đào ngũ từ nhiều thế lực khác nhau — trong số họ có thợ rèn, đan sư bỏ nghề, trinh sát viên, và cả cựu y sư quân đội. Chính sự đa dạng kỹ năng này khiến nhóm nhỏ nhưng tự túc được mọi mặt.

## V. Công Pháp & Trận Pháp (功法与阵法)
Mỗi thành viên Đào Binh mang theo kỹ năng riêng từ thế lực cũ, tạo nên kho chiến thuật đa dạng bất ngờ. Kỹ thuật chung duy nhất là "Ẩn Sa Thuật" — phương pháp dùng linh lực hòa tan khí tức vào cát xung quanh, khiến thần thức kẻ truy sát không phân biệt được người và cát. Chiến thuật cốt lõi là du kích thuần túy: phục kích nhanh từ dưới cát, đánh tản mát rồi rút lui ngay, tuyệt đối không bao giờ đối đầu trực diện. Ưu thế lớn nhất của họ không phải sức mạnh mà là sự biến ảo — kẻ thù không biết mình đang đối mặt với thợ rèn, đan sư hay sát thủ cho đến khi đã quá muộn.

## VI. Đặc Sản Môn Phái (门派特产)
- **Ẩn Sa Phù:** Linh phù tự chế từ cát Lưu Sa Khu, kích hoạt sẽ tạo ra vùng che giấu khí tức trong bán kính nhỏ. Hiệu quả không cao nhưng đủ để thoát thân trong tình huống nguy cấp.
- **Tạp Kỹ Vũ Khí:** Vũ khí và pháp khí thu thập từ nhiều nguồn gốc khác nhau, được thợ rèn trong nhóm sửa chữa và cải tiến. Không có hai vũ khí giống nhau, khiến kẻ thù không thể phán đoán xuất thân của Đào Binh.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Doanh Trại Di Động:** Lều và vật dụng gọn nhẹ có thể tháo dỡ trong một khắc. Không để lại dấu vết nào trên cát — gió và cát chảy sẽ xóa sạch mọi thứ sau vài canh giờ.
- **Kho Chôn Cát:** Các điểm chôn giấu vật tư dự trữ rải rác trong Lưu Sa Khu, được đánh dấu bằng hệ thống ký hiệu mà chỉ thành viên Đào Binh mới hiểu. Vị trí thay đổi theo chu kỳ cát chảy.

## VIII. Kinh Tế (经济)
Kinh tế của Đào Binh hoàn toàn dựa trên tự cung tự cấp và cướp có chọn lọc. "Vô Danh" đặt ra nguyên tắc nghiêm ngặt: chỉ lấy từ thương đoàn giàu có hoặc tông môn áp bức, tuyệt đối không cướp bóc dân thường hay tiểu thương. Nước và lương thực là tài sản quý giá nhất, được phân phối công bằng tuyệt đối. Đôi khi, Đào Binh đổi chác với các tiểu thương lẻ — dùng vũ khí cũ hoặc kỹ năng sửa chữa để đổi lấy nhu yếu phẩm, nhưng luôn đảm bảo không ai biết họ là ai.

## IX. Lịch Sử Tóm Tắt (简史)
Lưu Sa Đào Binh không có ngày thành lập chính thức. Trong suốt lịch sử Tây Mạc, mỗi cuộc chiến giữa các tông môn đều để lại những kẻ đào ngũ — binh lính từ chối tàn sát dân thường, tu sĩ mất hết niềm tin vào thế lực của mình, hay đơn giản là những kẻ muốn sống. Họ tìm đến nhau trong sa mạc, kết thành các nhóm nhỏ để sinh tồn. "Vô Danh" là người đầu tiên tổ chức họ thành một lực lượng có quy củ, đặt ra nguyên tắc và kỷ luật. Ông không xưng vương hay lập tông, chỉ đơn giản muốn những kẻ chạy trốn chiến tranh có nơi nương náu và không phải chết trong cô đơn giữa sa mạc.

## X. Giai Thoại & Bí Mật (轶事与秘密)
- "Vô Danh" được đồn là cựu tướng quân của một thế lực đã bị tiêu diệt hoàn toàn — ông đào ngũ không phải vì hèn nhát, mà vì cấp trên ra lệnh tàn sát dân thường và ông từ chối tuân theo. Đôi khi, trong đêm khuya, ông ngồi một mình nhìn về hướng đông với ánh mắt đầy ân hận.
- Có tin đồn Đào Binh đã phát hiện một lối đi bí mật xuyên Lưu Sa Khu dẫn thẳng đến Lưu Sa Cổ Thành, nhưng không ai dám xác nhận hay sử dụng con đường đó vì sợ những gì chờ đợi ở đầu kia.
- Một vài đào binh gần đây bắt đầu nói mê trong giấc ngủ bằng thứ ngôn ngữ không ai hiểu — hiện tượng bắt đầu sau khi họ cắm trại gần Lưu Sa Cổ Thành. "Vô Danh" đã ra lệnh không ai được đến gần khu vực đó nữa, nhưng một số thành viên vẫn bị thứ ngôn ngữ kỳ lạ ám ảnh trong giấc mơ.

## XI. Quan Hệ Thế Lực (势力关系)
- **Thiên Sa Thương Hội:** Mục tiêu cướp chọn lọc. Đào Binh chỉ nhắm vào các thương đoàn giàu có nhất, tránh xa hộ vệ cấp cao. Thương Hội biết về sự tồn tại của Đào Binh nhưng coi họ là mối phiền nhỏ so với Sa Tặc.
- **Sa Tặc Liên Minh:** Cùng hoạt động ngoài vòng pháp luật nhưng hoàn toàn khác biệt về bản chất. Sa Tặc coi Đào Binh là đám hèn nhát, Đào Binh coi Sa Tặc là lũ cướp tàn bạo vô nguyên tắc. Hai bên đôi khi đụng độ khi tranh giành mục tiêu.
- **Sa Mạc Hướng Đạo Hội:** Một số hướng đạo lão luyện biết về sự tồn tại của Đào Binh nhưng giữ im lặng — có lẽ vì đồng cảm, hoặc đơn giản vì Đào Binh chưa bao giờ làm hại hướng đạo nào.
