---
type: faction
name: Phế Khí Luyện Đan Phường
hantu: 废弃炼丹坊
faction_type: Thương Hội
alignment: 6
race: Nhân Tộc
region: Đông Hoang
founded: 20 năm trước
founder: Tôn Hoài Cựu
emblem: Phe_Khi_Luyen_Dan_Phuong.png
specialty: Phế Vật Hồi Luyện Thuật, Đan dược cấp thấp giá rẻ, Tái chế phế liệu luyện đan
economy:
- Bán đan dược cấp thấp cho tán tu nghèo và phàm nhân
- Thu gom phế liệu đan lò từ tông môn lớn
- Trao đổi dược liệu tái chế với Linh Sa Khuẩn Đoàn
arcs:
  - arc: 1
    status: Hoạt động ổn định
    rank: Hạng Năm
    leader: Phường Chủ Tôn Hoài Cựu
    population: 35
    territory:
      - Góc tây nam ốc đảo Minh Nguyệt Châu
    assets:
      - name: Lò đan tái chế
        type: Công Trình
      - name: Viên đan phát sáng xanh bí ẩn
        type: Bảo Vật
      - name: Bãi thu gom phế liệu
        type: Tài Nguyên
    stats: [10, 60, 30, 35, 15, 40]
    divisions:
      - name: Ban Luyện Đan & Thu Gom
        role: Thu gom phế liệu, luyện đan tái chế và bán hàng cho tán tu nghèo
        headcount:
          hoi_truong: 1
          truong_lao: 0
          thuong_nhan: 5
          ho_ve: 0
          nhan_cong: 29
        members:
          - character: Tôn Hoài Cựu
            position: Phường Chủ
            cultivation: Trúc Cơ Hậu Kỳ
          - character: "[Đan Sư Phó]"
            position: Đan Sư
            cultivation: Trúc Cơ Sơ Kỳ
            placeholder: true
    relationships:
      - faction: Thiên Sa Thương Hội
        description: Thương Hội từng đề nghị mua lại phường với giá rẻ mạt, bị từ chối. Từ đó gây khó dễ về nguồn cung phế liệu.
        diplomacy:
          lien_minh: -30
          tin: -40
          uy_hiep: 30
          thuong_mai: -40
          on_oan: -30
          le_thuoc: 0
      - faction: Linh Sa Khuẩn Đoàn
        description: Đối tác trao đổi dược liệu, khuẩn đoàn cung cấp nguyên liệu sinh học, đan phường đổi lại đan dược cấp thấp.
        diplomacy:
          lien_minh: 20
          tin: 30
          uy_hiep: 0
          thuong_mai: 60
          on_oan: 0
          le_thuoc: 0
      - faction: Kim Sa Tự
        description: Phế liệu từ Kim Sa Tự chứa thành phần lạ, có thể là tàn dư đan phương cổ đại. Đan phường thu mua đều đặn.
        diplomacy:
          lien_minh: 5
          tin: 15
          uy_hiep: 0
          thuong_mai: 40
          on_oan: 0
          le_thuoc: 0
---

# PHẾ KHÍ LUYỆN ĐAN PHƯỜNG (废弃炼丹坊)

## I. Tổng Quan (总览)

Phế Khí Luyện Đan Phường là một cơ sở luyện đan nhỏ bé tại ốc đảo Minh Nguyệt Châu, chuyên tái chế phế liệu đan lò bị các tông môn lớn vứt bỏ để luyện thành đan dược cấp thấp phục vụ tán tu nghèo và phàm nhân bệnh tật. Với khoảng 35 thành viên dưới sự lãnh đạo của Phường Chủ Tôn Hoài Cựu — cựu đệ tử ngoại môn đan phái bị trục xuất vì "lãng phí nguyên liệu" — Đan Phường tuy bị gọi là "Đan Phường Ăn Mày" nhưng đã âm thầm cứu nhiều mạng sống mà không ai để ý. Triết lý "Rác của tông môn, cơm của chúng ta" phản ánh tinh thần tận dụng triệt để và không khinh thường bất kỳ nguồn tài nguyên nào.

## II. Địa Lý & Tài Nguyên (地理与资源)

Đan Phường đóng tại góc tây nam Minh Nguyệt Châu, khu vực gần bãi rác thải của các tông môn lớn — vị trí bị khinh rẻ nhưng lý tưởng cho hoạt động thu gom phế liệu. Khu nhà cũ kỹ xây bằng đá sa mạc, khói lò đan bốc lên cả ngày lẫn đêm tạo nên cảnh tượng bụi bặm nhưng đầy sinh khí. Tài nguyên chính là phế liệu đan lò, dược thảo tàn, cặn linh thạch — tất cả đều là đồ bỏ đi của người khác nhưng dưới tay Tôn Hoài Cựu trở thành nguyên liệu đan dược giá rẻ. Nước linh từ ốc đảo Minh Nguyệt Châu — được Ốc Đảo Vi Linh tịnh hóa mà Đan Phường không biết — cũng góp phần nâng cao chất lượng đan dược.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)

Văn hóa Đan Phường xây dựng trên nền tảng tiết kiệm cực đoan và tôn trọng vật liệu. Triết lý "Rác của tông môn, cơm của chúng ta" không chỉ là khẩu hiệu mà là nguyên tắc sống — không ai được phép chê bai nguyên liệu dù là cặn bã, vì trong mắt đan sư chân chính, mọi thứ đều có giá trị tiềm ẩn. Mỗi viên đan luyện xong phải thử trên bản thân trước khi bán cho khách — quy tắc này đảm bảo không bao giờ bán đan dược có hại, đồng thời thể hiện tinh thần trách nhiệm cao. Danh tiếng "Đan Phường Ăn Mày" bị tông môn lớn dùng để chế nhạo, nhưng trong giới tán tu nghèo, đây là nơi đáng tin cậy nhất.

## IV. Cơ Cấu Tổ Chức (组织结构)

Cơ cấu đơn giản theo mô hình phường hội nhỏ. Phường Chủ Tôn Hoài Cựu — từng là đệ tử ngoại môn của một đan phái, bị đuổi vì "lãng phí nguyên liệu" (thực ra là vì thí nghiệm luyện đan quá táo bạo vượt khuôn khổ) — là đan sư giỏi nhất và người ra quyết định duy nhất. Năm Đan Sư tán tu Trúc Cơ Sơ Kỳ phụ trách luyện đan cơ bản dưới sự hướng dẫn của Phường Chủ. Khoảng 30 thợ phụ Luyện Khí đảm nhận thu gom phế liệu từ bãi rác, vận chuyển nguyên liệu và canh lò suốt ngày đêm.

## V. Công Pháp & Trận Pháp (功法与阵法)

Sở hữu "Phế Vật Hồi Luyện Thuật" — kỹ thuật luyện đan do Tôn Hoài Cựu tự sáng tạo, tận dụng cặn dược và linh thạch đã cạn kiệt luyện lại thành đan dược cấp thấp. Kỹ thuật này đòi hỏi khả năng khống chế lửa lò cực kỳ tinh tế, vì nguyên liệu tạp loại dễ phát nổ nếu lửa quá mạnh. Đan dược thành phẩm hiệu quả chỉ bằng 30-50% hàng chính hãng, nhưng giá rẻ gấp mười lần, phù hợp với túi tiền tán tu nghèo. Đôi khi kết hợp với dược liệu từ Linh Sa Khuẩn Đoàn thu gom, tạo ra hiệu quả bất ngờ — một số viên đan tái chế có tác dụng phụ không lường trước nhưng vô hại.

## VI. Đặc Sản Môn Phái (门派特产)

- **Phế Liệu Hồi Xuân Đan:** Đan dược cấp thấp luyện từ cặn dược tái chế, có tác dụng chữa lành vết thương nhẹ và bổ sung thể lực cho phàm nhân. Hiệu quả khiêm tốn nhưng giá rẻ đến mức ai cũng mua được.
- **Tạp Khí Thanh Linh Đan:** Đan dược hỗ trợ tu luyện cấp Luyện Khí, luyện từ cặn linh thạch và dược thảo tàn. Chất lượng không ổn định — mỗi mẻ có hiệu quả khác nhau — nhưng đôi khi xuất hiện viên đan chất lượng bất ngờ cao.
- **Viên Đan Phát Sáng Xanh:** Viên đan duy nhất Tôn Hoài Cựu vô tình luyện được từ cặn bã, phát sáng xanh và có mùi hương chưa từng thấy. Ông không dám dùng và giấu kỹ, nghi ngờ đây có thể liên quan đến đan phương cổ đại.

## VII. Cơ Sở Hạ Tầng (基础设施)

- **Lò Đan Tái Chế:** Ba lò đan cũ kỹ nhưng vẫn hoạt động, trong đó lò chính do Tôn Hoài Cựu tự sửa chữa từ lò hỏng mua lại với giá rẻ. Khói lò bốc cả ngày lẫn đêm.
- **Bãi Thu Gom Phế Liệu:** Khu đất rộng phía sau phường, nơi phân loại và lưu trữ cặn dược, linh thạch cạn và phế liệu đan lò từ các tông môn lớn.
- **Kho Thành Phẩm:** Phòng nhỏ bảo quản đan dược thành phẩm, được niêm phong bằng phù lục giữ nhiệt đơn giản để duy trì dược tính.
- **Quầy Bán Hàng:** Một quầy nhỏ mặt tiền hướng ra đường chính ốc đảo, nơi bán đan dược trực tiếp cho tán tu và phàm nhân.

## VIII. Kinh Tế (经济)

Kinh tế Đan Phường xoay quanh chu trình tái chế: thu gom phế liệu miễn phí hoặc giá rẻ từ bãi rác tông môn lớn, luyện thành đan dược cấp thấp, bán cho tán tu nghèo và phàm nhân bệnh tật với giá vừa túi tiền. Lợi nhuận thấp nhưng ổn định, đủ nuôi sống 35 thành viên. Trao đổi dược liệu sinh học với Linh Sa Khuẩn Đoàn là nguồn nguyên liệu bổ sung quan trọng. Tuy nhiên, kể từ khi từ chối lời đề nghị mua lại của Thiên Sa Thương Hội, nguồn cung phế liệu bị gây khó dễ — một số tông môn lớn được Thương Hội gợi ý đã ngừng vứt phế liệu tại bãi rác gần Đan Phường.

## IX. Lịch Sử Tóm Tắt (简史)

Tôn Hoài Cựu bị trục xuất khỏi đan phái cách đây 20 năm vì thí nghiệm luyện đan quá táo bạo — thực chất là kỹ thuật tái chế phế liệu mà đan phái coi là "xúc phạm nghề luyện đan." Lang thang đến Minh Nguyệt Châu, ông nhận thấy lượng phế liệu khổng lồ bị các tông môn lớn vứt bỏ mà không ai nhặt. Bắt đầu từ một cái lò nứt và vài viên dược thảo héo, Tôn Hoài Cựu dần xây dựng phường luyện đan phục vụ tán tu nghèo và phàm nhân bệnh tật.

Hai thập kỷ qua, Đan Phường phát triển chậm mà chắc, từ một người tăng lên 35 thành viên. Phường nhỏ bé nhưng đã cứu được nhiều mạng sống mà không ai để ý — những viên đan rẻ tiền ấy là hy vọng duy nhất của nhiều tán tu không đủ tiền mua thuốc chính hãng. Gần đây, một đan sư phát hiện cặn dược từ Kim Sa Tự chứa thành phần lạ, có thể là tàn dư của đan phương cổ đại — phát hiện này có thể thay đổi vận mệnh Đan Phường.

## X. Giai Thoại & Bí Mật (轶事与秘密)

- Phường Chủ vô tình luyện được một viên đan kỳ lạ từ cặn bã — viên đan phát sáng xanh và có mùi hương chưa từng thấy trong bất kỳ sách luyện đan nào. Tôn Hoài Cựu không dám dùng và giấu kỹ, nhưng đêm đêm viên đan phát ra hào quang mờ nhạt xuyên qua lớp vải bọc, khiến ông mất ngủ vì tò mò.
- Thiên Sa Thương Hội đề nghị mua lại phường với giá 50 hạ phẩm linh thạch — mức giá xúc phạm đối với 20 năm tâm huyết. Tôn Hoài Cựu từ chối thẳng, và từ đó Thương Hội bắt đầu gây sức ép bằng cách cắt nguồn cung phế liệu. Cuộc chiến kinh tế này đang đẩy Đan Phường vào thế khó.
- Một đan sư trong phường gần đây phát hiện rằng cặn dược từ Kim Sa Tự chứa thành phần lạ — phân tích sơ bộ cho thấy đó là tàn dư của đan phương cổ đại, có thể có từ thời Thượng Cổ. Nếu giải mã được, Đan Phường sẽ sở hữu bí phương mà cả lục địa thèm muốn.

## XI. Quan Hệ Thế Lực (势力关系)

| Thế Lực | Quan Hệ | Mô Tả |
|---------|---------|-------|
| Thiên Sa Thương Hội | Đối nghịch | Bị gây khó dễ nguồn cung sau khi từ chối bán phường |
| Linh Sa Khuẩn Đoàn | Đối tác | Trao đổi dược liệu sinh học lấy đan dược |
| Kim Sa Tự | Nguồn cung | Phế liệu chứa thành phần cổ đại bí ẩn |
