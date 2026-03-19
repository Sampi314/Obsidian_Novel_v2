---
type: faction
name: Tạp Huyết Long Đàn
hantu: 杂血龙团
faction_type: Bộ Lạc
alignment: -2
race: Long Tộc Tạp Huyết (huyết mạch dưới 30%)
region: Vô Tận Hải
founded: Khoảng năm mươi năm trước
founder: Xích Giác
emblem: Vay_Gay_Do.png
specialty: Chân Long Cửu Biến phiên bản suy yếu, Bán hóa long, Sinh tồn vùng biển hoang dã
economy:
  - Săn bắt hải thú nhỏ và đánh bắt cá
  - Trao đổi bí mật tin tức bên ngoài với Phản Loạn Long Tử lấy thức ăn
  - Thu lượm vật liệu từ xác tàu đắm và di vật trôi dạt
arcs:
  - arc: 1
    status: Lưu vong sinh tồn
    rank: Hạng Tư
    leader: Đàn Chủ Xích Giác
    population: 43
    territory:
      - Quần đảo Vảy Gãy (vùng biển xa Long Cung)
    assets:
      - name: Quần đảo Vảy Gãy
        type: Công Trình
      - name: Vảy Rồng Cổ (rải rác trên bờ đá)
        type: Tài Nguyên
    stats: [200, 160, 180, 150, 170, 155]
    divisions:
      - name: Trưởng Lão Hội
        role: Cố vấn và giữ gìn truyền thống Long Tộc
        headcount:
          truong_lao: 3
          chien_binh: 0
          dan_thuong: 0
        members:
          - character: "[Trưởng Lão Bạch Vảy]"
            position: Trưởng Lão
            cultivation: Trúc Cơ Hậu Kỳ
            placeholder: true
          - character: "[Trưởng Lão Thanh Giác]"
            position: Trưởng Lão
            cultivation: Trúc Cơ Hậu Kỳ
            placeholder: true
          - character: "[Trưởng Lão Ám Lân]"
            position: Trưởng Lão
            cultivation: Trúc Cơ Hậu Kỳ
            placeholder: true
      - name: Chiến Đoàn
        role: Lực lượng chiến đấu và săn bắt bảo vệ quần đảo
        headcount:
          truong_lao: 0
          chien_binh: 15
          dan_thuong: 0
        members:
          - character: Xích Giác
            position: Đàn Chủ
            cultivation: Kim Đan Sơ Kỳ (tương đương)
            placeholder: false
          - character: "[Phó Đàn Chủ Hắc Vĩ]"
            position: Phó Đàn Chủ
            cultivation: Trúc Cơ Viên Mãn
            placeholder: true
      - name: Dân Thường
        role: Long Tộc tạp huyết già yếu, phụ nữ và con nhỏ
        headcount:
          truong_lao: 0
          chien_binh: 0
          dan_thuong: 25
        members:
          - character: "[Long Tộc Tạp Huyết]"
            position: Dân thường
            cultivation: Luyện Khí hoặc Phàm Nhân
            placeholder: true
    relationships:
      - faction: Long Cung
        description: Bị Long Cung coi là "ô uế" và trục xuất, từng xin quay về nhưng bị từ chối và nhục mạ công khai. Mang mặc cảm vừa hận vừa khao khát được công nhận.
        diplomacy:
          lien_minh: -90
          tin: -100
          uy_hiep: -60
          thuong_mai: -100
          on_oan: -95
          le_thuoc: 0
      - faction: Phản Loạn Long Tử
        description: Bí mật trao đổi — nhận thức ăn và vật tư từ Phản Loạn Long Tử, đổi lấy tin tức về tình hình bên ngoài Long Cung. Quan hệ thận trọng nhưng có thiện chí.
        diplomacy:
          lien_minh: 40
          tin: 30
          uy_hiep: 0
          thuong_mai: 35
          on_oan: 50
          le_thuoc: 0
      - faction: Giao Long Lưu Vong
        description: Đồng cảnh ngộ bị Long Cung trục xuất, nhưng Giao Long Lưu Vong có huyết mạch cao hơn nên vẫn giữ khoảng cách. Hai bên thỉnh thoảng gặp nhau ở vùng biển trung lập.
        diplomacy:
          lien_minh: 25
          tin: 20
          uy_hiep: 0
          thuong_mai: 15
          on_oan: 35
          le_thuoc: 0
---

# Tạp Huyết Long Đàn (杂血龙团)

## I. Tổng Quan (总览)
Tạp Huyết Long Đàn là cộng đồng bốn mươi ba Long Tộc tạp huyết — những sinh vật mang dòng máu rồng dưới ba mươi phần trăm — bị Long Cung trục xuất và coi là "ô uế." Dưới sự dẫn dắt của Đàn Chủ Xích Giác, một hỗn huyết Long có sừng đỏ nhỏ trên trán và tu vi tương đương Kim Đan, đàn sống sót trên Quần đảo Vảy Gãy — vùng biển hoang dã xa Long Cung nơi linh khí loãng và sóng dữ quanh năm. Là thế lực Hạng Tư, Tạp Huyết Long Đàn không có tham vọng bá quyền mà chỉ cố gắng tồn tại và giữ gìn chút ít tự hào còn sót lại của dòng máu Long Tộc. Nỗi đau của họ mang hai mặt: vừa căm hận Long Cung đã khinh thường và ruồng bỏ, vừa khao khát được thừa nhận là con cháu chính thống của Long Tộc.

## II. Địa Lý & Tài Nguyên (地理 与 资源)
Quần đảo Vảy Gãy là một chuỗi đảo đá đen nằm xa Long Cung, nơi sóng dữ quanh năm đập vào bờ đá sắc nhọn và linh khí loãng đến mức tu sĩ bình thường sẽ cảm thấy ngột ngạt. Tên "Vảy Gãy" xuất phát từ những mảnh vảy rồng gãy nát rải rác trên bờ đá khắp quần đảo — không rõ là vảy của ai, từ thời nào, nhưng sự hiện diện của chúng khiến nơi đây mang một nỗi buồn kỳ lạ. Tài nguyên cực kỳ ít ỏi: thành viên trong đàn ăn cá sống, uống nước mưa, thỉnh thoảng săn hải thú nhỏ đi lạc vào vùng biển. Vị trí xa Long Cung đủ để tránh bị truy đuổi, nhưng cũng xa mọi tuyến thương mại — sự cô lập vừa là lá chắn vừa là gông cùm. Hang động trên đảo lớn nhất được dùng làm nơi trú ẩn chung, tuy chật chội nhưng che chắn được gió bão.

## III. Văn Hóa & Tín Ngưỡng (文化 与 信仰)
Thành viên Tạp Huyết Long Đàn đều mang huyết mạch Long Tộc dưới ba mươi phần trăm — bị Long Cung coi là "không đủ tư cách" làm rồng. Dù vậy, họ vẫn kiên quyết tự hào với dòng máu rồng còn sót lại, dù chỉ là chút ít. Nội bộ đàn thường xuyên tranh cãi ai "thuần" hơn ai — một thành viên có vảy trên cánh tay tự coi mình cao hơn kẻ chỉ có móng vuốt hơi cong, kẻ phun được khói tự coi mình vượt trội hơn kẻ chỉ có đôi mắt dọc. Mặc cảm sâu sắc thấm vào mọi khía cạnh đời sống: vừa hận Long Cung khinh thường, vừa khao khát được quay về; vừa khinh bỉ nhân tộc, vừa phải dùng công pháp nhân tộc để tồn tại. Đó là bi kịch của những kẻ không thuộc về đâu — không đủ rồng để được Long Cung chấp nhận, không đủ người để hòa nhập với nhân tộc.

## IV. Cơ Cấu Tổ Chức (组织结构)
Đàn được tổ chức theo mô hình bộ lạc đơn giản. Xích Giác giữ vị trí Đàn Chủ không phải vì bầu cử hay truyền thừa, mà vì ông là cá thể mạnh nhất — có sừng đỏ nhỏ trên trán, bằng chứng duy nhất rõ ràng nhất về huyết mạch Long Tộc, và là người duy nhất có thể bán hóa long dù chỉ trong thời gian ngắn. Ba Trưởng Lão là ba Long Tộc tạp huyết già nhất trong đàn, tu vi Trúc Cơ Hậu Kỳ, đóng vai trò cố vấn và giữ gìn những nghi thức truyền thống Long Tộc còn nhớ được. Mười lăm chiến binh là những cá thể khỏe mạnh nhất, đảm nhiệm việc săn bắt và bảo vệ đàn. Hai mươi lăm thành viên còn lại là Long Tộc tạp huyết già yếu, phụ nữ và con nhỏ, đa phần chỉ có ngoại hình hơi giống rồng — vảy thưa, không biết phun lửa, đuôi ngắn hoặc không có. Nội bộ thường xuyên xảy ra xung đột về thứ bậc, mỗi thành viên đều muốn chứng minh mình "thuần" hơn người khác.

## V. Công Pháp & Trận Pháp (功法 与 阵法)
Tạp Huyết Long Đàn tu luyện phiên bản suy yếu của Chân Long Cửu Biến — công pháp biến hình chính thống của Long Tộc, nhưng do huyết mạch quá loãng nên chỉ có thể biến được một hoặc hai bộ phận thay vì toàn thân. Xích Giác là người thành công nhất: có thể hóa nửa rồng trong thời gian ngắn — nửa trên biến thành thân rồng với vảy đỏ và sừng, nửa dưới vẫn giữ hình dáng bán nhân — nhưng sau đó kiệt sức hoàn toàn và phải nghỉ ngơi nhiều ngày. Một số thành viên khác chỉ biến được cánh tay thành vuốt rồng hoặc mọc vảy trên lưng trong vài phút. Có một số tạp huyết tu luyện nhân tộc công pháp thay thế để bù đắp hạn chế của huyết mạch, nhưng bị trong đàn coi là "phản bội Long Tộc" — một mâu thuẫn đau đớn vì sự thật là nhân tộc công pháp đôi khi hiệu quả hơn phiên bản suy yếu của Long Tộc.

## VI. Đặc Sản Môn Phái (门派特产)
- **Tạp Huyết Long Vảy:** Vảy rồng tạp huyết tuy phẩm chất thấp hơn nhiều so với Chân Long Vảy, nhưng vẫn có hàm lượng long khí nhất định, có thể dùng làm nguyên liệu luyện khí phẩm chất trung bình hoặc gia cố giáp bảo vệ cấp thấp. Tuy nhiên, không ai trong đàn bán vảy của mình — đó là niềm tự hào cuối cùng.
- **Hỗn Huyết Nhục Thân:** Thể chất của Long Tộc tạp huyết tuy không bằng Chân Long nhưng vẫn vượt xa nhân tộc bình thường. Sức mạnh thể xác, khả năng phục hồi vết thương, và thời gian nín thở dưới nước đều cao hơn đáng kể. Đây là lý do họ có thể sinh tồn trong vùng biển khắc nghiệt mà nhân tộc phàm nhân sẽ chết trong vài ngày.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Hang Chính (Đảo Sừng Gãy):** Hang động lớn nhất trên đảo chính của quần đảo, được dùng làm nơi trú ẩn chung cho toàn đàn. Bên trong chia thành nhiều ngóc ngách tự nhiên, mỗi gia đình chiếm một khu vực. Sàn hang phủ rong biển khô làm chỗ ngủ, tường hang khắc đầy ký hiệu Long Tộc — nỗ lực giữ gìn bản sắc của những kẻ lưu vong.
- **Bãi Săn:** Vùng biển quanh quần đảo được chia thành các khu vực săn bắt luân phiên, đảm bảo hải sản không bị khai thác kiệt. Mỗi chiến binh phụ trách một khu, thay phiên theo mùa.
- **Đá Thề:** Tảng đá đen lớn nhất trên đỉnh Đảo Sừng Gãy, nơi Xích Giác từng thề sẽ dẫn đàn tìm lại vinh quang. Mỗi thành viên mới gia nhập phải lên Đá Thề tuyên thệ trung thành với đàn.

## VIII. Kinh Tế (经济)
Kinh tế của Tạp Huyết Long Đàn gần như không tồn tại theo nghĩa thông thường. Thức ăn đến từ việc săn bắt hải thú nhỏ và đánh bắt cá quanh quần đảo — vừa đủ để không chết đói nhưng hiếm khi no. Nước uống hoàn toàn phụ thuộc vào nước mưa, mùa khô là thời kỳ khốn khổ nhất. Kênh thu nhập duy nhất từ bên ngoài là trao đổi bí mật với Phản Loạn Long Tử: đàn cung cấp tin tức về tình hình bên ngoài Long Cung — các thế lực đang lớn mạnh, các tuyến đường biển mới, tin đồn về hải thú — đổi lấy thức ăn, thuốc men và thỉnh thoảng vài viên linh thạch phẩm chất thấp. Ngoài ra, chiến binh trong đàn thường xuyên thu lượm vật liệu từ xác tàu đắm trôi dạt gần quần đảo — đồng, sắt, vải buồm — tất cả đều quý giá đối với những kẻ không có gì.

## IX. Lịch Sử Tóm Tắt (简史)
Xích Giác sinh ra trong Long Cung với tất cả hy vọng của cha mẹ — cho đến khi kiểm tra huyết mạch cho kết quả chỉ hai mươi tám phần trăm. Lập tức bị tuyên bố "ô uế" và trục xuất khỏi Long Cung theo luật cổ, Xích Giác lang thang trên biển với nỗi nhục nhã khắc sâu vào xương. Trên đường phiêu bạt, ông dần gặp những Long Tộc tạp huyết khác cùng cảnh ngộ — bị bỏ rơi, bị khinh thường, sống vất vưởng giữa đại dương mà không thuộc về đâu. Xích Giác tập hợp họ lại, tìm đến Quần đảo Vảy Gãy và lập nên đàn. Từng ba lần gửi thỉnh nguyện đến Long Cung xin cho phép quay về, cả ba lần đều bị từ chối và nhục mạ công khai — lần cuối cùng, sứ giả bị đánh gãy sừng trước mặt triều thần. Từ đó, Xích Giác không còn xin xỏ nữa, mà bắt đầu bí mật liên lạc với Phản Loạn Long Tử — trao đổi thức ăn đổi lấy tin tức, đồng thời nuôi hy vọng rằng một ngày nào đó, hệ thống huyết mạch sẽ thay đổi.

## X. Giai Thoại & Bí Mật (轶事 与 秘密)
Xích Giác tin rằng huyết mạch Long Tộc có thể tịnh hóa nếu tìm được Hóa Long Trì thứ hai — truyền thuyết nói có một cái ẩn sâu dưới đáy vực sâu nhất của Vô Tận Hải, nơi mà ngay cả Long Vương cũng ngại đến. Ông đã bí mật phái chiến binh thăm dò nhưng chưa ai quay về mang theo kết quả rõ ràng. Trong đàn có một con rồng tạp huyết trẻ tuổi bất ngờ thức tỉnh năng lực phun băng — một năng lực cực kỳ hiếm mà ngay cả Chân Long cũng ít khi sở hữu. Sự kiện này gây chấn động trong đàn: nếu một tạp huyết có thể thức tỉnh năng lực cao cấp, liệu hệ thống phân chia huyết mạch của Long Cung có thật sự chính xác? Ngoài ra, Quần đảo Vảy Gãy được đặt tên theo những mảnh vảy rồng gãy rải rác trên bờ đá — không rõ là vảy của ai, từ bao giờ. Ba Trưởng Lão tin rằng đó là vảy của một Chân Long cổ đại đã chết tại đây, và linh hồn của nó vẫn bảo vệ quần đảo — giải thích vì sao hải thú lớn hiếm khi đến gần.

## XI. Quan Hệ Thế Lực (势力关系)
- **Long Cung:** Mối quan hệ đau đớn nhất. Long Cung coi Tạp Huyết Long Đàn là "sỉ nhục của Long Tộc" — sự tồn tại của họ là bằng chứng rằng huyết mạch Long Tộc có thể bị "pha loãng," điều mà Long Cung không bao giờ muốn thừa nhận. Từng ba lần xin quay về, ba lần bị từ chối nhục nhã. Hiện tại, Long Cung không chủ động truy sát nhưng cũng không thừa nhận sự tồn tại của đàn.
- **Phản Loạn Long Tử:** Mối quan hệ bí mật quan trọng nhất. Phản Loạn Long Tử nhìn thấy ở Tạp Huyết Long Đàn bằng chứng sống về sự bất công của hệ thống huyết mạch, và đã thiết lập kênh trao đổi bí mật: thức ăn và vật tư đổi lấy tin tức. Hai bên chia sẻ mục tiêu chung nhưng giữ khoảng cách thận trọng.
- **Giao Long Lưu Vong:** Đồng cảnh ngộ bị Long Cung trục xuất, nhưng mối quan hệ không hẳn thân thiết. Giao Long Lưu Vong có huyết mạch cao hơn Tạp Huyết và vẫn giữ nghi thức Long Cung chính thống, khiến hai bên dù thông cảm nhưng vẫn có khoảng cách tâm lý. Thỉnh thoảng gặp nhau ở vùng biển trung lập để trao đổi tin tức, nhưng chưa bao giờ chính thức liên minh.
