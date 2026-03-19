---
type: faction
name: Thạch Linh Đồng Tử Hội
hantu: 石灵童子会
faction_type: Hội
alignment: 5
race: Thạch Tộc
region: Đông Hoang
founded: Không xác định (hình thành tự nhiên)
founder: Không có (tự phát)
emblem: Thach_Linh_Dong_Tu_Hoi.png
specialty: Không có (trẻ con chưa phát triển kỹ năng)
economy:
- Không có hoạt động kinh tế
arcs:
  - arc: 1
    status: Tồn tại tự nhiên
    rank: Không Xếp Hạng
    leader: Không có lãnh đạo chính thức
    population: 50
    territory:
      - Quanh mỏ đá lớn Đông Hoang
      - Bãi đá và vách núi nơi linh thạch ngưng tụ
    assets:
      - name: Mỏ linh thạch (nơi sinh ra)
        type: Tài Nguyên
      - name: Bộ sưu tập sỏi đẹp
        type: Tài Nguyên
    stats: [5, 15, 10, 50, 10, 5]
    divisions:
      - name: Quần Thể Đồng Tử
        role: Nhóm trẻ con tự phát, chơi đùa và học hỏi thế giới quanh mỏ đá
        headcount:
          hoi_truong: 0
          pho_hoi_truong: 0
          thanh_vien: 50
          tong_quan: 0
        members:
          - character: "[Đồng Tử Lớn Nhất]"
            position: Thành Viên (tự nhiên dẫn dắt)
            cultivation: Tương đương Luyện Khí Sơ Kỳ
            placeholder: true
          - character: "[Đồng Tử Pha Lê]"
            position: Thành Viên
            cultivation: Không xác định (đặc biệt)
            placeholder: true
    relationships:
      - faction: Thạch Tâm Thủ Hộ Đoàn
        description: Thạch Tâm Thủ Hộ Đoàn coi việc bảo vệ mỏ linh thạch là nhiệm vụ, gián tiếp bảo vệ bọn trẻ. Vài Thạch Tộc trưởng thành từ Đoàn lặng lẽ canh chừng từ xa mà bọn trẻ không biết.
        diplomacy:
          lien_minh: 20
          tin: 30
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 20
          le_thuoc: 30
      - faction: Sơn Cốc Cự Tộc Ẩn Sĩ
        description: Trưởng lão trong thung lũng biết về bọn trẻ và lặng lẽ quan sát từ xa. Một số Đồng Tử là hậu duệ xa của Cự Tộc thu nhỏ qua tiến hóa, nhưng bọn trẻ không biết điều này.
        diplomacy:
          lien_minh: 5
          tin: 5
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 10
          le_thuoc: 0
      - faction: Ngọc Thạch Thợ Mỏ
        description: Thợ mỏ khai thác linh thạch tại cùng khu vực, đôi khi vô tình phá hủy nơi sinh của Thạch Tộc trẻ. Bọn trẻ sợ hãi tiếng đục đá nhưng không hiểu tại sao người lớn lại phá nhà chúng.
        diplomacy:
          lien_minh: -20
          tin: -30
          uy_hiep: 40
          thuong_mai: 0
          on_oan: -30
          le_thuoc: 0
---

# Thạch Linh Đồng Tử Hội (石灵童子会)

## I. Tổng Quan (总览)
Thạch Linh Đồng Tử Hội không phải tổ chức chính thức mà là hiện tượng tự nhiên: năm mươi Thạch Tộc trẻ tụ tập quanh mỏ đá lớn Đông Hoang — nơi chúng "nở" ra từ linh thạch ngưng tụ — chơi đùa, tò mò, và dần học cách hiểu thế giới xung quanh. Không có lãnh đạo, không có quy tắc, không có mục đích ngoài sự tò mò vô hạn của trẻ con. Cao từ ba mươi centimet đến một mét, tuổi từ vài năm đến vài chục năm, bọn trẻ sống bản năng giữa bãi đá và khe nứt, tặng nhau sỏi đẹp làm quà, và hoàn toàn không biết rằng thế giới bên ngoài đầy hiểm nguy. Không xếp hạng trên bất kỳ bảng thế lực nào, nhưng sự tồn tại của chúng gắn liền với tương lai của Thạch Tộc — và mối đe dọa âm thầm từ các tông phái nhân tộc muốn bắt chúng làm vật liệu.

## II. Địa Lý & Tài Nguyên (地理与资源)
Bọn trẻ sống quanh mỏ đá lớn và các vách núi nơi linh thạch ngưng tụ — chính là nơi chúng sinh ra. Khi linh thạch trong mỏ tích tụ linh khí đủ lâu, dần dần hình thành ý thức và tách ra khỏi đá mẹ thành cá thể nhỏ bé. Bãi đá rộng với hốc đá và khe nứt nhỏ là sân chơi và chỗ ngủ lý tưởng. Tài nguyên theo nghĩa thông thường gần như không có — bọn trẻ thu nhặt mảnh linh thạch vụn và sỏi đẹp coi như đồ chơi quý giá, trao đổi với nhau bằng những quy tắc đơn giản mà chỉ trẻ con mới hiểu. Tuy nhiên, bản thân mỏ linh thạch là tài nguyên cực kỳ giá trị với thế giới bên ngoài, và đó chính là nguồn gốc của mối nguy mà bọn trẻ không nhận thức được.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
Không có triết lý hay tín ngưỡng — chỉ có sự tò mò vô hạn, niềm vui đơn thuần, và bản năng bầy đàn của trẻ con. Quy tắc "không được đi quá xa mỏ đá" và "không được nghịch linh thạch của người lớn" không phải luật mà là lời dặn dò được truyền miệng từ Thạch Tộc trưởng thành canh chừng ngoài rìa. Khi có nguy hiểm, bọn trẻ biết phải nghe lời Thạch Tộc lớn — bản năng sinh tồn duy nhất chúng có. Phong tục đáng yêu nhất: khi một Thạch Tộc mới "nở" ra từ đá — tách khỏi linh thạch mẹ lần đầu tiên, nhỏ xíu và bối rối — cả nhóm sẽ vây quanh, mỗi đứa tặng viên sỏi đẹp nhất mình có làm quà chào đời. Đó là truyền thống tự phát, không ai dạy, nhưng đứa nào cũng làm.

## IV. Cơ Cấu Tổ Chức (组织结构)
Không có cơ cấu tổ chức chính thức. Nhóm tự tổ chức theo bản năng bầy đàn: đứa lớn nhất — khoảng một mét, tuổi vài chục năm — tự nhiên trở thành "thủ lĩnh" dẫn dắt nhóm đi chơi, tìm sỏi, và chạy trốn khi có nguy hiểm. Nhưng "thủ lĩnh" này không có quyền lực thực sự — bọn trẻ khác nghe theo chỉ vì nó lớn hơn và biết nhiều hơn, nếu ai không thích thì tự đi chơi chỗ khác. Năm mươi Thạch Tộc trẻ chia thành vài nhóm nhỏ theo sở thích: nhóm thích nhặt sỏi, nhóm thích leo trèo, nhóm thích nằm im hấp thụ linh khí. Bảo hộ từ bên ngoài là vài Thạch Tộc trưởng thành thuộc Thạch Tâm Thủ Hộ Đoàn lặng lẽ canh chừng từ xa, không chính thức thuộc Hội nhưng sẵn sàng can thiệp khi có nguy hiểm.

## V. Công Pháp & Trận Pháp (功法与阵法)
Bọn trẻ Thạch Tộc không có công pháp — chúng hấp thụ linh khí từ đá mẹ và linh thạch xung quanh một cách hoàn toàn tự nhiên, giống như cây hấp thụ nước và ánh sáng. Quá trình này rất chậm nhưng ổn định, sau vài trăm năm chúng sẽ lớn lên đủ để gia nhập các nhóm Thạch Tộc trưởng thành. Không có trận pháp hay bất kỳ biện pháp phòng thủ nào — bọn trẻ hoàn toàn phụ thuộc vào sự bảo vệ gián tiếp của Thạch Tộc trưởng thành và sự hẻo lánh của mỏ đá. Khả năng chiến đấu bằng không — ngay cả phàm nhân cũng có thể bắt một Thạch Tộc trẻ bỏ vào túi. Biện pháp tự vệ duy nhất là giả đá: khi sợ hãi, Thạch Tộc trẻ thu mình lại, đứng im bất động, trông giống hệt một tảng đá nhỏ bình thường.

## VI. Đặc Sản Môn Phái (门派特产)
- **Sỏi Tặng Quà:** Những viên sỏi đẹp nhất mà bọn trẻ tặng nhau — không có giá trị tu luyện nhưng chứa linh khí nhẹ do Thạch Tộc trẻ truyền vào qua quá trình chơi đùa. Một số tu sĩ coi đây là vật may mắn.
- **Linh Thạch Trẻ:** Mảnh linh thạch nơi Thạch Tộc từng "nở" ra, chứa dấu vết ý thức đầu tiên, có dược tính đặc biệt trong một số đan phương liên quan đến thần thức. Cực kỳ hiếm và gần như không thể thu thập mà không làm hại mỏ.
- **Bụi Đá Linh:** Bụi đá do Thạch Tộc trẻ vô tình tạo ra khi chơi đùa va chạm, chứa linh khí loãng, có thể dùng làm nguyên liệu phụ trong luyện khí.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Mỏ Đá Sinh Sản:** Khu vực linh thạch ngưng tụ nơi Thạch Tộc mới "nở" ra, là nơi thiêng liêng nhất (dù bọn trẻ không hiểu khái niệm thiêng liêng). Thạch Tộc trưởng thành cố gắng bảo vệ khu vực này khỏi thợ mỏ.
- **Bãi Đá Sân Chơi:** Bãi đá rộng nơi bọn trẻ chơi đùa, leo trèo, và thi nhặt sỏi. Hốc đá nhỏ được bọn trẻ biến thành "nhà" để cất giấu bộ sưu tập sỏi.
- **Khe Nứt Ngủ:** Các khe nứt hẹp trong vách đá nơi bọn trẻ chui vào ngủ, đủ nhỏ để sinh vật lớn hơn không lọt vào, tạo cảm giác an toàn.

## VIII. Kinh Tế (经济)
Thạch Linh Đồng Tử Hội hoàn toàn không có hoạt động kinh tế. Bọn trẻ Thạch Tộc không cần ăn uống theo nghĩa thông thường — chúng hấp thụ linh khí từ đá và linh thạch xung quanh. Không cần quần áo vì thân thể bằng đá. Không cần nhà ở vì khe nứt và hốc đá là đủ. "Nền kinh tế" duy nhất là hệ thống trao đổi sỏi giữa bọn trẻ: viên sỏi đẹp hơn có "giá trị" cao hơn, nhưng tiêu chuẩn đẹp xấu thay đổi tùy ngày tùy tâm trạng. Tuy nhiên, bản thân sự tồn tại của bọn trẻ lại có giá trị kinh tế khổng lồ với thế giới bên ngoài: một số tông phái nhân tộc sẵn sàng trả giá cao để bắt Thạch Tộc trẻ làm thú cưng hoặc tệ hơn, nghiền thành bột làm vật liệu luyện khí.

## IX. Lịch Sử Tóm Tắt (简史)
Thạch Tộc sinh ra từ đá — đây là sự thật đơn giản và kỳ diệu nhất. Khi linh thạch trong mỏ ngưng tụ đủ lâu, linh khí dần hình thành mạng lưới phức tạp bên trong đá, rồi sản sinh ý thức. Ý thức lớn dần, đá nứt ra, một cá thể Thạch Tộc nhỏ bé tách ra khỏi đá mẹ lần đầu tiên nhìn thế giới. Thạch Linh Đồng Tử Hội không có ngày thành lập — nó tồn tại bao lâu thì mỏ đá tồn tại bấy lâu. Bọn trẻ tụ tập, chơi đùa, học hỏi, rồi sau vài trăm năm lớn lên và rời đi gia nhập các cộng đồng Thạch Tộc trưởng thành. Đồng thời, Thạch Tộc mới liên tục "nở" ra từ mỏ đá, bổ sung vào nhóm. Chu kỳ này đã lặp lại từ thời viễn cổ, và sẽ tiếp tục — trừ khi mỏ đá bị khai thác hết.

## X. Giai Thoại & Bí Mật (轶事与秘密)
Trong đám trẻ con có một Thạch Tộc sinh ra từ linh thạch đặc biệt hiếm — toàn thân trong suốt như pha lê, phát ra ánh sáng nhẹ trong bóng tối. Không ai — kể cả Thạch Tộc trưởng thành canh chừng — biết nó sẽ phát triển thành gì, nhưng bản năng mách bảo rằng đây không phải Thạch Tộc bình thường. Bọn trẻ khác gọi nó là "Sáng Sáng" và đặc biệt thích chơi cùng vì nó phát ra ánh sáng ấm áp. Bí mật tối tăm hơn là mối đe dọa từ bên ngoài: các tông phái nhân tộc đôi khi cử người đến mỏ đá bắt Thạch Tộc trẻ về làm thú cưng hoặc nghiền thành bột làm vật liệu luyện khí. Bọn trẻ không hiểu tại sao đôi khi bạn chơi biến mất và không bao giờ quay lại — nhưng Thạch Tộc trưởng thành biết, và nỗi sợ hãi đó là lý do họ luôn canh chừng từ xa.

## XI. Quan Hệ Thế Lực (势力关系)
- **Thạch Tâm Thủ Hộ Đoàn:** Người bảo hộ gián tiếp quan trọng nhất. Đoàn coi việc bảo vệ mỏ linh thạch là nhiệm vụ, qua đó gián tiếp bảo vệ bọn trẻ. Vài Thạch Tộc trưởng thành từ Đoàn lặng lẽ canh chừng, sẵn sàng hành động khi có kẻ xâm phạm.
- **Sơn Cốc Cự Tộc Ẩn Sĩ:** Trưởng lão trong thung lũng biết về bọn trẻ và quan sát từ xa. Một số Đồng Tử có thể là hậu duệ tiến hóa xa của Cự Tộc, nhưng sự liên kết quá mờ nhạt để xác nhận.
- **Ngọc Thạch Thợ Mỏ:** Mối đe dọa lớn nhất đối với bọn trẻ. Thợ mỏ khai thác linh thạch tại cùng khu vực, vô tình hoặc cố ý phá hủy nơi sinh của Thạch Tộc trẻ. Bọn trẻ sợ hãi tiếng đục đá nhưng không hiểu rằng chính ngôi nhà của chúng đang bị phá hủy dần.
