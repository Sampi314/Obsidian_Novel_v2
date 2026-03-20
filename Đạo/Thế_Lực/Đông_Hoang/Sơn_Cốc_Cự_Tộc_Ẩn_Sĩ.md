---
type: faction
name: Sơn Cốc Cự Tộc Ẩn Sĩ
hantu: 山谷巨族隐士
faction_type: Bộ Lạc
alignment: 3
race: Cự Tộc
region: Đông Hoang
founded: Hàng nghìn năm trước (Thượng Cổ)
founder: Thạch Tổ
emblem: Son_Coc_Cu_Toc_An_Si.png
specialty: Thể phách cổ pháp, Đại địa chi lực, Phong ấn trận pháp
economy:
- Không có hoạt động kinh tế (tự cung tự cấp)
arcs:
  - arc: 1
    status: Ẩn cư (gần như bất động)
    rank: Hạng Ba
    leader: Thạch Tổ (Hóa Thần, đang ngủ sâu) — thực quyền Trưởng Lão Đại
    population: 15
    territory:
      - Thung lũng cổ đại sâu trong dãy núi Đông Hoang (lối vào bị đá khổng lồ che kín)
    assets:
      - name: Long mạch nhỏ trong thung lũng
        type: Tài Nguyên
      - name: Cổ pháp Cự Tộc Thượng Cổ
        type: Tài Nguyên
      - name: Trận pháp phong ấn cổ đại
        type: Trang Bị
    stats: [1500, 300, 100, 15, 1800, 50]
    divisions:
      - name: Cộng Đồng Thung Lũng
        role: Cộng đồng ẩn cư, canh gác giấc ngủ của Thạch Tổ và duy trì sự sống trong thung lũng
        headcount:
          truong_lao: 3
          chien_binh: 0
          dan_thuong: 12
        members:
          - character: Thạch Tổ
            position: Trưởng Lão (Tộc Trưởng, đang ngủ sâu)
            cultivation: Hóa Thần
          - character: "[Trưởng Lão Đại]"
            position: Trưởng Lão (Quyền nhiếp chính)
            cultivation: Kim Đan Hậu Kỳ
            placeholder: true
          - character: "[Trưởng Lão Nhị]"
            position: Trưởng Lão
            cultivation: Kim Đan Trung Kỳ
            placeholder: true
          - character: "[Trưởng Lão Tam]"
            position: Trưởng Lão
            cultivation: Kim Đan Sơ Kỳ
            placeholder: true
    relationships:
      - faction: Thạch Tâm Thủ Hộ Đoàn
        description: Thạch Tâm Thủ Hộ Đoàn biết về sự tồn tại của thung lũng ẩn sĩ nhưng tôn trọng quyết định không can thiệp của các trưởng lão. Đôi khi Đoàn gửi tin về tình hình bên ngoài vào thung lũng.
        diplomacy:
          lien_minh: 20
          tin: 30
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 10
          le_thuoc: 0
      - faction: Thạch Linh Đồng Tử Hội
        description: Các trưởng lão trong thung lũng biết về bọn trẻ Thạch Tộc ở mỏ đá gần đó, đôi khi lặng lẽ quan sát chúng từ xa. Nhưng việc tiết lộ vị trí thung lũng cho bọn trẻ quá rủi ro.
        diplomacy:
          lien_minh: 5
          tin: 5
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 10
          le_thuoc: 0
      - faction: Cự Tộc Thợ Xây
        description: Cự Tộc Thợ Xây là hậu duệ xa của cùng dòng máu Cự Tộc nhưng đã chọn con đường hòa nhập với thế giới thay vì ẩn cư. Trưởng lão thung lũng coi họ là "kẻ quên nguồn cội" nhưng không thù ghét.
        diplomacy:
          lien_minh: 0
          tin: -10
          uy_hiep: 0
          thuong_mai: 0
          on_oan: -10
          le_thuoc: 0
---

# Sơn Cốc Cự Tộc Ẩn Sĩ (山谷巨族隐士)

## I. Tổng Quan (总览)
Sơn Cốc Cự Tộc Ẩn Sĩ là cộng đồng mười lăm Cự Tộc già cỗi cuối cùng, ẩn cư trong thung lũng sâu thẳm giữa dãy núi Đông Hoang, canh gác giấc ngủ ngàn năm của Thạch Tổ — một trong những Cự Tộc cuối cùng đạt cảnh giới Hóa Thần. Dù danh nghĩa xếp Hạng Ba nhờ sức mạnh tiềm ẩn khủng khiếp của Thạch Tổ, cộng đồng gần như không hoạt động: mười hai Cự Tộc già cao hai mươi đến ba mươi mét đa số đang ngủ dài hạn hoặc chờ chết, ba trưởng lão Kim Đan lo liệu mọi việc. Triết lý "Thế giới đã thay đổi, nhưng núi vẫn đứng" phản ánh tâm thế của những kẻ đã chấp nhận sự suy tàn của chủng tộc mình và tìm kiếm bình yên trong im lặng.

## II. Địa Lý & Tài Nguyên (地理与资源)
Thung lũng nằm sâu trong dãy núi Đông Hoang, bao bọc hoàn toàn bởi vách núi dựng đứng mà chỉ Cự Tộc mới đủ lớn để dời những tảng đá khổng lồ che kín lối vào. Bên trong là không gian rộng lớn với hồ nước trong vắt, cỏ linh cổ đại mọc hoang dại, và vài hang động khổng lồ được khoét sâu vào vách núi làm nơi ở. Một long mạch nhỏ chảy qua lòng thung lũng cung cấp linh khí ổn định, nuôi sống cỏ linh và duy trì trận pháp phong ấn. Đá linh tự nhiên nổi lên từ lòng đất, phát ra ánh sáng dịu nhẹ vào ban đêm, biến thung lũng thành không gian kỳ ảo tách biệt hoàn toàn với thế giới bên ngoài. Tài nguyên tuy không phong phú nhưng đủ để mười lăm Cự Tộc sinh tồn vô thời hạn.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
"Thế giới đã thay đổi, nhưng núi vẫn đứng" — triết lý này thấm vào từng thớ đá trong thung lũng. Cự Tộc ẩn sĩ không còn tham vọng, không còn sân hận, chỉ giữ ba quy tắc đơn giản: không can thiệp vào thế giới bên ngoài, không tiết lộ vị trí thung lũng cho bất kỳ ai, và bảo vệ giấc ngủ của Thạch Tổ bằng mọi giá. Mỗi trăm năm, Cự Tộc già nhất còn tỉnh thay phiên canh gác hang Thạch Tổ — nghi thức thiêng liêng duy nhất còn sót lại từ thời Thượng Cổ. Các trưởng lão kể lại truyền thuyết về thời hoàng kim của Cự Tộc cho những ai còn muốn nghe, nhưng ngày càng ít cá thể quan tâm — đa số chỉ muốn ngủ và chờ kết thúc tự nhiên.

## IV. Cơ Cấu Tổ Chức (组织结构)
Cơ cấu tối giản phù hợp với cộng đồng chỉ mười lăm cá thể. Thạch Tổ là Tộc Trưởng danh nghĩa nhưng đang ngủ sâu trong hang lớn nhất, thân thể cao năm mươi mét đã hóa đá một phần, chỉ trái tim còn đập chậm rãi. Ba trưởng lão Kim Đan lo liệu mọi việc: Trưởng Lão Đại giữ quyền nhiếp chính và quyết định mọi vấn đề lớn; Trưởng Lão Nhị phụ trách canh gác trận pháp phong ấn; Trưởng Lão Tam chăm sóc long mạch và cỏ linh. Mười hai Cự Tộc còn lại đa số nằm im trong hang động riêng, ngủ hàng thập kỷ rồi tỉnh dậy vài ngày trước khi ngủ tiếp, dần dần hóa đá như Thạch Tổ.

## V. Công Pháp & Trận Pháp (功法与阵法)
Cự Tộc ẩn sĩ thừa kế cổ pháp truyền từ Thượng Cổ, nặng về thể phách và đại địa chi lực — kỹ thuật tu luyện khai thác sức mạnh trực tiếp từ đất đá và long mạch. Không giống công pháp hiện đại chú trọng linh khí tinh luyện, cổ pháp Cự Tộc thô kệch nhưng uy lực vĩ đại, phù hợp với thân thể khổng lồ của chủng tộc. Trận pháp phong ấn cổ đại do Thạch Tổ đích thân bố trí bảo vệ lối vào thung lũng: tảng đá khổng lồ che cửa thực ra là một phần của trận pháp, kết nối với long mạch bên dưới, tạo ra kết giới vô hình khiến bất kỳ ai đến gần đều cảm thấy choáng váng và mất phương hướng. Chỉ Cự Tộc mang huyết mạch thuần chủng mới không bị ảnh hưởng.

## VI. Đặc Sản Môn Phái (门派特产)
- **Cổ Pháp Thể Phách:** Kỹ thuật tu luyện thân thể bằng cách hấp thụ tinh hoa đất đá và long mạch, tăng cường sức mạnh vật lý đến mức phi thường. Đã thất truyền với thế giới bên ngoài, chỉ ba trưởng lão còn nắm giữ.
- **Đá Linh Tự Nhiên:** Đá đặc biệt chỉ sinh ra trong thung lũng, phát ra ánh sáng dịu nhẹ, chứa linh khí ngưng tụ hàng nghìn năm. Giá trị cực cao nếu mang ra ngoài nhưng Cự Tộc coi đó là vật thiêng.
- **Cỏ Linh Cổ Đại:** Loại cỏ linh mọc hoang từ thời Thượng Cổ, tuổi đời hàng nghìn năm, có dược tính vượt xa mọi thảo dược hiện đại nhưng chỉ phát huy tác dụng với Cự Tộc.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Hang Thạch Tổ:** Hang động khổng lồ nơi Thạch Tổ nằm ngủ, trần hang cao hơn năm mươi mét, được trận pháp cổ đại bảo vệ. Không khí bên trong nặng nề, linh khí đặc quánh.
- **Hang Cư Trú:** Mười hai hang động nhỏ hơn (nhưng vẫn khổng lồ so với tiêu chuẩn nhân tộc) khoét vào vách núi, mỗi hang là nơi ở của một Cự Tộc.
- **Hồ Thung Lũng:** Hồ nước trong vắt được long mạch bên dưới nuôi dưỡng, nước có tính dược nhẹ, giúp duy trì sự sống cho Cự Tộc già yếu.
- **Trận Pháp Phong Ấn:** Bao phủ toàn bộ lối vào, gây mất phương hướng cho kẻ xâm nhập, kết nối với long mạch nên gần như vĩnh viễn không cần bổ sung năng lượng.

## VIII. Kinh Tế (经济)
Sơn Cốc Cự Tộc Ẩn Sĩ không có hoạt động kinh tế nào. Cộng đồng hoàn toàn tự cung tự cấp: long mạch cung cấp linh khí tu luyện, hồ nước và cỏ linh cung cấp dinh dưỡng, đá linh phát sáng tự nhiên thay đèn. Cự Tộc không cần y phục, vũ khí, hay bất kỳ vật phẩm nào từ thế giới bên ngoài. Trên thực tế, tài nguyên trong thung lũng — đá linh tự nhiên, cỏ linh cổ đại, nước long mạch — sẽ có giá trị thiên văn nếu đưa ra thị trường, nhưng các trưởng lão coi đó là điều không thể tưởng tượng. Sự cô lập hoàn toàn là lựa chọn có chủ đích, không phải sự bất lực.

## IX. Lịch Sử Tóm Tắt (简史)
Hàng nghìn năm trước, trong thời Thượng Cổ, Cự Tộc là chủng tộc hùng mạnh bậc nhất, chiếm lĩnh sơn hà. Nhưng khi linh khí thế giới thay đổi, thân thể khổng lồ từ lợi thế trở thành gánh nặng — cần quá nhiều tài nguyên, quá dễ bị phát hiện, quá chậm để thích ứng. Cự Tộc dần suy tàn, từ hàng vạn còn vài trăm, rồi vài chục. Thạch Tổ — một trong những Cự Tộc cuối cùng đạt Hóa Thần — nhận ra rằng chủng tộc không thể cứu vãn, quyết định dẫn nhóm nhỏ nhất vào thung lũng ẩn cư. Sau khi bố trí trận pháp phong ấn, Thạch Tổ rơi vào giấc ngủ dài. Các Cự Tộc còn lại canh gác, chờ đợi ngày Thạch Tổ tỉnh dậy, hoặc chờ cái chết đến trước.

## X. Giai Thoại & Bí Mật (轶事与秘密)
Thạch Tổ không phải đang ngủ — hắn đang chiến đấu với thứ gì đó trong mộng cảnh, và đã chiến đấu suốt hàng nghìn năm. Ba trưởng lão cảm nhận được qua long mạch: rung động nhẹ, nhịp tim bất thường, và đôi khi tiếng rên khe khẽ từ hang Thạch Tổ vang vọng trong đêm khuya. Họ không biết Thạch Tổ đang chiến đấu với cái gì, nhưng biết rằng nếu hắn thua, hậu quả sẽ vượt xa thung lũng. Bí mật thứ hai đáng lo ngại không kém: nếu Thạch Tổ tỉnh dậy, sức mạnh Hóa Thần giải phóng đột ngột sẽ gây chấn động toàn Đông Hoang — nhưng cũng hoàn toàn có khả năng hắn tỉnh dậy trong trạng thái tẩu hỏa nhập ma, và không gì trên đời có thể ngăn cản một Cự Tộc Hóa Thần điên cuồng.

Trưởng Lão Đại thỉnh thoảng đứng ở lối vào thung lũng, đặt tay lên tảng đá khổng lồ che cửa và lắng nghe. Ông nói rằng qua tảng đá, ông có thể cảm nhận nhịp đập của thế giới bên ngoài — và nhịp đập đó ngày càng nhanh và hỗn loạn hơn qua mỗi thập kỷ. *"Ta không biết điều gì đang đến,"* ông từng nói với Trưởng Lão Nhị trong một đêm khuya, *"nhưng đất đang run — và khi đất run, nghĩa là thứ gì đó rất lớn đang thức dậy."*

## XI. Quan Hệ Thế Lực (势力关系)
- **Thạch Tâm Thủ Hộ Đoàn:** Đoàn biết về sự tồn tại của thung lũng nhưng tôn trọng quyết định ẩn cư. Quan hệ xa cách nhưng có tình đồng tộc, đôi khi Đoàn gửi tin về biến động bên ngoài vào thung lũng qua cách để lại dấu hiệu trên đá gần lối vào.
- **Thạch Linh Đồng Tử Hội:** Các trưởng lão biết về bọn trẻ Thạch Tộc ở mỏ đá gần đó và lặng lẽ quan sát từ xa. Muốn bảo vệ nhưng không thể tiết lộ vị trí thung lũng, nên chỉ đành giữ khoảng cách.
- **Cự Tộc Thợ Xây:** Hậu duệ xa của cùng dòng máu nhưng đã chọn hòa nhập với thế giới thay vì ẩn cư. Trưởng lão thung lũng coi họ là "kẻ quên nguồn cội" nhưng thực ra trong lòng vừa buồn vừa nhẹ nhõm — ít nhất một nhánh Cự Tộc vẫn tồn tại.
