---
type: faction
name: Thạch Tượng Thủ Vệ
hantu: 石像守卫
faction_type: Hội
alignment: 5
race: Thạch Tộc
region: Đông Hoang
founded: Thượng Cổ
founder: Không rõ (Chủ nhân cổ đại)
emblem: Thach_Tuong_Thu_Ve.png
specialty: Thạch Hóa bảo tồn, Canh giữ di tích, Chiến đấu phòng ngự
economy:
  - Không có kinh tế (tự cung tự cấp từ linh khí)
  - Hấp thụ linh khí tự nhiên từ di tích
arcs:
  - arc: 1
    status: Ngủ đông (Phần lớn hóa đá)
    rank: Hạng Tư
    leader: Thủ Vệ Trưởng Thạch Miên
    population: 23
    territory:
      - Di tích cổ đại trong hang núi sâu Đông Hoang
      - Hệ thống hành lang và đại sảnh cổ
    assets:
      - name: Di Tích Thượng Cổ
        type: Bí Cảnh
      - name: Đại Trận Cổ Đại (suy yếu)
        type: Trận Pháp
      - name: Căn Phòng Cấm
        type: Bí Cảnh
    stats: [300, 200, 50, 23, 450, 20]
    divisions:
      - name: Thủ Vệ Đội
        role: Canh giữ di tích cổ đại theo lời thề Thượng Cổ
        headcount:
          hoi_truong: 1
          pho_hoi_truong: 0
          thanh_vien: 3
          tong_quan: 19
        members:
          - character: Thạch Miên
            position: Thủ Vệ Trưởng
            cultivation: Kim Đan (đang ngủ)
          - character: "[Thủ Vệ Nhất]"
            position: Thủ Vệ Tỉnh Táo
            cultivation: Trúc Cơ Hậu Kỳ
            placeholder: true
          - character: "[Thủ Vệ Nhị]"
            position: Thủ Vệ Tỉnh Táo
            cultivation: Trúc Cơ Trung Kỳ
            placeholder: true
          - character: "[Thủ Vệ Tam]"
            position: Thủ Vệ Tỉnh Táo
            cultivation: Trúc Cơ Sơ Kỳ
            placeholder: true
    relationships:
      - faction: Thạch Tâm Thủ Hộ Đoàn
        description: Cùng là Cự Tộc / Thạch Tộc canh giữ di sản, nhưng chưa biết nhau tồn tại.
        diplomacy:
          lien_minh: 0
          tin: 0
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 0
      - faction: Vạn Pháp Thư Quán
        description: Nếu phát hiện di tích, Thư Quán sẽ rất quan tâm vì giá trị khảo cổ, nhưng Thủ Vệ sẽ ngăn cản mọi kẻ xâm nhập.
        diplomacy:
          lien_minh: -20
          tin: -30
          uy_hiep: 40
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 0
      - faction: Cổ Yêu Thức Tỉnh Hội
        description: Cả hai đều là tàn dư Thượng Cổ đang chờ đợi, nhưng hoàn toàn không biết đến sự tồn tại của nhau.
        diplomacy:
          lien_minh: 0
          tin: 0
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 0
---

# Thạch Tượng Thủ Vệ (石像守卫)

## I. Tổng Quan (总览)

Thạch Tượng Thủ Vệ là một tổ chức Thạch Tộc cổ đại được giao nhiệm vụ canh giữ một di tích Thượng Cổ bí ẩn nằm sâu trong hang núi Đông Hoang. Gồm 23 Thạch Tộc, nhưng phần lớn đã hóa đá vĩnh viễn do hết năng lượng, chỉ còn 3 cá thể duy trì trạng thái tỉnh táo. Trên danh nghĩa, đây là lực lượng Hạng Tư vì Thủ Vệ Trưởng Thạch Miên sở hữu tu vi tương đương Kim Đan, nhưng thực tế chiến lực hiện tại chỉ ngang Hạng Năm do nhân lực hoạt động quá ít. Điều đáng kinh ngạc nhất về Thạch Tượng Thủ Vệ không phải sức mạnh mà là sự trung thành — hàng vạn năm trôi qua, chủ nhân không bao giờ trở lại, nhưng họ vẫn kiên trì canh giữ vì đó là lời thề.

## II. Địa Lý & Tài Nguyên (地理与资源)

Di tích nằm sâu trong một hang núi cổ đại, lối vào bị đá sụp che khuất khiến gần như không thể phát hiện từ bên ngoài. Bên trong là quần thể kiến trúc đá hoành tráng gồm nhiều hành lang, đại sảnh và phòng nghi lễ, tường và trần khắc đầy ký tự cổ đại mà ngay cả Thạch Miên cũng không thể đọc hết. Kiến trúc cho thấy nền văn minh xây dựng di tích này sở hữu trình độ vượt xa thời đại hiện tại. Giá trị khảo cổ và tu luyện là vô cùng lớn, nhưng vì không ai biết đến sự tồn tại của di tích nên tài nguyên này hoàn toàn "đóng băng." Linh khí tàn dư trong di tích vẫn đủ để duy trì sự sống tối thiểu cho 3 Thạch Tộc tỉnh táo.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)

Văn hóa của Thạch Tượng Thủ Vệ xoay quanh một khái niệm duy nhất: lời thề. "Lời thề canh giữ vĩnh hằng, dù thế giới đổi thay" — câu nói này được khắc vào ý thức của mỗi Thạch Tộc từ khi nhận nhiệm vụ. Quy tắc tuyệt đối bao gồm: không rời khỏi di tích, không để bất kỳ ai vào mà không có mật lệnh cổ đại, và canh giữ cho đến khi chủ nhân trở lại. Đặc biệt, khi hết năng lượng, Thạch Tộc không chết mà tự hóa đá thành tượng, rơi vào trạng thái ngủ vĩnh viễn — nhưng nếu có linh khí mạnh hoặc kẻ xâm nhập kích hoạt, tượng đá có thể tỉnh dậy. Đây là cơ chế phòng thủ tự nhiên đáng sợ nhất của di tích.

## IV. Cơ Cấu Tổ Chức (组织结构)

Tổ chức rất đơn giản vì phần lớn thành viên đang ngủ. Thủ Vệ Trưởng Thạch Miên — Thạch Tộc cổ đại sở hữu tu vi Kim Đan — hiện hóa thạch tại vị trí canh gác trung tâm, chỉ tỉnh khi bị kích hoạt bởi xâm nhập quy mô lớn. 3 Thạch Tộc tỉnh táo (tương đương Trúc Cơ) luân phiên tuần tra các hành lang chính, đảm bảo cấu trúc di tích không bị sập và không có kẻ lạ xâm nhập. 19 tượng đá còn lại rải rác khắp di tích, mỗi tượng đều là một Thạch Tộc đang ngủ, sẵn sàng tỉnh dậy nếu có đủ linh khí.

## V. Công Pháp & Trận Pháp (功法与阵法)

Cổ pháp "Thạch Hóa Vĩnh Hằng" là công pháp cốt lõi của Thạch Tượng Thủ Vệ, cho phép Thạch Tộc hóa đá để bảo tồn sinh lực vô hạn, nhưng đánh đổi bằng việc mất hoàn toàn ý thức trong trạng thái ngủ. Đây là lý do 20 Thạch Tộc có thể tồn tại hàng vạn năm mà không chết. Bản thân di tích là một đại trận cổ đại khổng lồ, được khắc vào nền tảng kiến trúc từ thời Thượng Cổ. Tuy nhiên, trải qua vạn năm suy yếu, đại trận hiện chỉ còn đủ sức ngăn cản tu sĩ Trúc Cơ trở xuống xâm nhập — đối với Kim Đan trở lên thì gần như vô dụng.

## VI. Đặc Sản Môn Phái (门派特产)

Thạch Tượng Thủ Vệ không sản xuất bất kỳ thứ gì và không có khái niệm "đặc sản." Tuy nhiên, di tích mà họ canh giữ chứa đựng các ký tự cổ đại trên tường và trần — những ký tự này có thể là bí kíp, bản đồ, hoặc ghi chép từ nền văn minh Thượng Cổ. Nếu ai đó giải mã được, giá trị kiến thức sẽ vượt xa bất kỳ pháp bảo nào. Ngoài ra, bụi đá từ tượng Thạch Tộc cổ đại có chứa linh khí ngưng tụ qua vạn năm, nhưng không ai biết để khai thác.

## VII. Cơ Sở Hạ Tầng (基础设施)

Di tích tự thân là một kiệt tác kiến trúc Thượng Cổ, gồm đại sảnh trung tâm (nơi Thạch Miên hóa thạch), các hành lang phức tạp xuyên sâu vào lòng núi, nhiều phòng chức năng chưa rõ mục đích, và một căn phòng cấm mà ngay cả Thạch Miên cũng không được phép vào. Mặc dù trải qua vạn năm, phần lớn cấu trúc vẫn nguyên vẹn nhờ chất liệu xây dựng đặc biệt — một loại đá chưa từng thấy ở thời đại hiện tại, có khả năng tự phục hồi chậm.

## VIII. Kinh Tế (经济)

Hoàn toàn không có hoạt động kinh tế. Thạch Tộc duy trì sự sống bằng cách hấp thụ linh khí tàn dư trong di tích, không cần ăn uống hay vật tư. 3 Thạch Tộc tỉnh táo đôi khi phải vào trạng thái ngủ ngắn để tiết kiệm năng lượng, sau đó tỉnh lại tiếp tục tuần tra. Đây là nền kinh tế tự cung tự cấp ở mức tối thiểu tuyệt đối — sống để canh giữ, không có nhu cầu nào khác.

## IX. Lịch Sử Tóm Tắt (简史)

Di tích có từ thời Thượng Cổ, do một thế lực vô danh xây dựng với mục đích không rõ ràng. Thạch Tộc được giao nhiệm vụ canh giữ bằng lời thề ràng buộc linh hồn — mọi thế hệ Thạch Tộc sinh ra trong di tích đều tự động kế thừa lời thề. Hàng vạn năm trôi qua, chủ nhân không bao giờ trở lại, thế giới bên ngoài thay đổi hoàn toàn, nhưng Thạch Tộc vẫn kiên trì. Dần dần, phần lớn hóa đá vĩnh viễn vì linh khí trong di tích ngày càng cạn kiệt, chỉ còn vài tượng giữ được chút ý thức. Đến hiện tại, Thạch Tượng Thủ Vệ là tàn dư cuối cùng của một thời đại đã mất, canh giữ thứ mà chính họ cũng không hoàn toàn hiểu.

## X. Giai Thoại & Bí Mật (轶事与秘密)

Bên trong di tích có một căn phòng mà ngay cả Thạch Miên — kẻ mạnh nhất và lâu đời nhất — cũng không được phép vào. Lời thề cấm hắn mở cánh cửa đó, và điều đáng sợ nhất là hắn không nhớ tại sao. Ký ức về nội dung bên trong đã bị xóa sạch, chỉ còn lại lệnh cấm tuyệt đối khắc vào linh hồn. Đôi khi, từ sau cánh cửa vọng ra những rung động kỳ lạ khiến cả di tích cộng hưởng, và mỗi lần như vậy, một vài tượng đá rung nhẹ như muốn tỉnh dậy.

Nếu tất cả 20 Thạch Tộc cùng tỉnh dậy, sức mạnh tổng hợp đủ để đối đầu cường giả Nguyên Anh — nhưng điều đó cần lượng linh khí khổng lồ mà hiện tại không có. Đây là "vũ khí cuối cùng" của di tích, và là lý do các thế lực bên ngoài nên cẩn thận nếu vô tình phát hiện nơi này.

## XI. Quan Hệ Thế Lực (势力关系)

- **Thạch Tâm Thủ Hộ Đoàn:** Cùng là Thạch Tộc / Cự Tộc có sứ mệnh canh giữ, nhưng chưa từng giao tiếp vì cả hai hoạt động bí mật. Tiềm năng đồng minh tự nhiên nếu biết nhau.
- **Vạn Pháp Thư Quán:** Nếu phát hiện di tích, Thư Quán sẽ coi đây là khám phá khảo cổ vĩ đại nhất Đông Hoang — nhưng Thủ Vệ sẽ coi họ là kẻ xâm nhập cần tiêu diệt.
- **Cổ Yêu Thức Tỉnh Hội:** Cả hai đều là tàn dư Thượng Cổ đang chờ đợi điều gì đó, nhưng hoàn toàn không biết đến sự tồn tại của nhau. Nếu gặp nhau, có thể ghép nối được những mảnh ký ức về thời đại đã mất.
