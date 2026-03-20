---
type: faction
name: Thiết Giáp Yêu Thú Đàn
hantu: 铁甲妖兽团
faction_type: Bộ Lạc
alignment: 3
race: Yêu Thú (Bọ giáp)
region: Tây Mạc
founded: Khoảng 200 năm trước (khi mối quan hệ cộng sinh với thương đoàn hình thành)
founder: Thiết Giáp Hùng (thế hệ trước)
emblem: Bo_Giap_Thiet.png
specialty: Hộ tống thương đoàn, Thiết Giáp Trận, Giáp xác thiên nhiên thiết khoáng
economy:
- Hộ tống thương đoàn đổi lấy khoáng linh và thức ăn
- Giáp xác rụng được thu gom và bán (không chính thức)
arcs:
  - arc: 1
    status: Hoạt động ổn định trên Thiên Sa Thương Đạo
    rank: Hạng Năm
    leader: Đàn Chủ Thiết Giáp Hùng
    population: 125
    territory:
      - Dọc Thiên Sa Thương Đạo (không có lãnh địa cố định)
      - Các trạm dừng chân trên thương đạo
    assets:
      - name: Giáp xác thiên nhiên thiết khoáng
        type: Tài Nguyên
    stats: [120, 30, 50, 125, 100, 40]
    divisions:
      - name: Cận Vệ Đàn
        role: Bảo vệ trực tiếp thương đoàn và bảo vệ ấu trùng
        headcount:
          truong_lao: 1
          chien_binh: 5
          dan_thuong: 0
        members:
          - character: Thiết Giáp Hùng
            position: Đàn Chủ
            cultivation: Trúc Cơ Viên Mãn (tương đương)
          - character: "[Cận Vệ Giáp Bạc]"
            position: Cận Vệ
            cultivation: Trúc Cơ Trung Kỳ (tương đương)
            placeholder: true
      - name: Đàn Chính
        role: Hộ tống thương đoàn, xếp trận phòng thủ
        headcount:
          truong_lao: 0
          chien_binh: 100
          dan_thuong: 20
        members:
          - character: "[Bọ Giáp Chiến Binh]"
            position: Hộ Tống
            cultivation: Luyện Khí - Trúc Cơ Sơ Kỳ (tương đương)
            placeholder: true
          - character: "[Ấu Trùng]"
            position: Ấu Trùng
            cultivation: Không có tu vi
            placeholder: true
    relationships:
      - faction: Thiên Sa Thương Hội
        description: Quan hệ cộng sinh lâu đời. Thương đoàn cung cấp khoáng linh và thức ăn, đàn bọ giáp cung cấp lực lượng hộ tống đáng tin cậy.
        diplomacy:
          lien_minh: 40
          tin: 60
          uy_hiep: 0
          thuong_mai: 70
          on_oan: 0
          le_thuoc: 40
      - faction: Cự Tộc Phu Khuân Vác
        description: Mối quan hệ bằng hữu tự nhiên. Cự Nhân và bọ giáp cùng dừng chân tại các trạm dừng, chia nhau thức ăn và nghỉ ngơi bên nhau.
        diplomacy:
          lien_minh: 30
          tin: 50
          uy_hiep: 0
          thuong_mai: 10
          on_oan: 0
          le_thuoc: 0
      - faction: Sa Tặc Liên Minh
        description: Kẻ thù thường xuyên giao chiến. Sa tặc tấn công thương đoàn, đàn bọ giáp đánh trả bảo vệ, hai bên đã đụng độ vô số lần.
        diplomacy:
          lien_minh: -80
          tin: -60
          uy_hiep: 30
          thuong_mai: 0
          on_oan: -50
          le_thuoc: 0
---

# Thiết Giáp Yêu Thú Đàn (铁甲妖兽团)

## I. Tổng Quan (总览)
Thiết Giáp Yêu Thú Đàn là một đàn bọ giáp yêu thú khoảng một trăm hai mươi lăm cá thể, hoạt động dọc Thiên Sa Thương Đạo với vai trò hộ tống thương đoàn. Dưới sự lãnh đạo của Thiết Giáp Hùng, một bọ giáp khổng lồ to bằng con trâu với giáp xác dày ba tầng, đàn trở thành một trong những lực lượng hộ tống đáng tin cậy nhất trên tuyến thương đạo. Mối quan hệ cộng sinh giữa đàn bọ giáp và thương nhân đã kéo dài hàng trăm năm, thương đoàn cung cấp khoáng linh và thức ăn, đàn bọ giáp đáp lại bằng giáp xác thép và lòng trung thành tuyệt đối. Đây là một trong số ít yêu thú được Nhân Tộc trên Thiên Sa Thương Đạo chấp nhận và tôn trọng.

## II. Địa Lý & Tài Nguyên (地理与资源)
Thiết Giáp Yêu Thú Đàn không có lãnh địa cố định, di chuyển liên tục dọc Thiên Sa Thương Đạo theo lịch trình của các thương đoàn thuê hộ tống. Giữa các hợp đồng, đàn nghỉ ngơi tại các trạm dừng chân trên thương đạo, nơi có đủ không gian cho cả trăm bọ giáp trú ẩn khỏi cát bão. Tài nguyên quý giá nhất của đàn là giáp xác tự nhiên bằng thiết khoáng, cứng như pháp khí hạ phẩm và ngày càng dày theo thời gian khi bọ giáp hấp thu kim linh từ cát sa mạc. Thu nhập chính đến từ khoáng linh và thức ăn do thương đoàn cung cấp, đổi lại đàn bọ giáp dùng thân mình làm lá chắn bảo vệ hàng hóa và con người.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
Triết lý cốt lõi của đàn được thể hiện qua câu nói mà thương nhân truyền miệng: "Giáp cứng, lòng trung. Ai nuôi ta, ta che chở." Đàn tuân thủ nghiêm ngặt quy tắc bảo vệ thương đoàn thuê cho đến khi hết hợp đồng, không bao giờ bỏ rơi hay phản bội người thuê dù gặp nguy hiểm. Sau mỗi trận chiến, dù thắng hay thua, cả đàn tập trung lại và gõ giáp xác vào nhau tạo ra âm thanh rền vang như tiếng trống chiến thắng, một phong tục đặc trưng khiến bất kỳ ai từng đi cùng đàn đều nhớ mãi. Ấu trùng được cả đàn bảo vệ tuyệt đối, bất kỳ mối đe dọa nào hướng đến ấu trùng đều khiến đàn bùng nổ chiến lực.

## IV. Cơ Cấu Tổ Chức (组织结构)
Đàn Chủ Thiết Giáp Hùng đứng đầu, là cá thể bọ giáp khổng lồ to bằng con trâu với giáp xác dày ba tầng, trí tuệ vượt trội đã tự học cách hiểu ý con người và điều phối cả đàn. Dưới Đàn Chủ là năm bọ giáp cận vệ tương đương Trúc Cơ Trung Kỳ, giáp xác phát sáng bạc, đảm nhiệm vai trò tiên phong và hậu vệ khi hộ tống. Đàn chính gồm khoảng một trăm bọ giáp từ Luyện Khí đến Trúc Cơ Sơ Kỳ tương đương, xếp thành đội hình phòng thủ theo hiệu lệnh của Đàn Chủ. Hai mươi ấu trùng đang trong giai đoạn phát triển, luôn được giữ ở trung tâm đội hình, bao bọc bởi lớp giáp dày nhất của cả đàn.

## V. Công Pháp & Trận Pháp (功法与阵法)
Thiết Giáp Yêu Thú Đàn không tu luyện công pháp, giáp xác tự nhiên của chúng cứng lên theo thời gian nhờ quá trình hấp thu kim linh từ cát sa mạc, một dạng tiến hóa tự nhiên chậm rãi nhưng bền vững. Trận pháp phòng thủ đặc trưng là "Thiết Giáp Trận", trong đó cả đàn xếp thành vòng tròn bao quanh thương đoàn, dùng giáp xác chắn mọi tấn công từ bên ngoài như một bức tường thép di động. Khi bị tấn công mạnh vượt quá khả năng chịu đựng, đàn chuyển sang thế "Thiết Cầu", toàn bộ cuộn lại thành quả cầu giáp xác khổng lồ và lăn qua kẻ thù với lực phá hủy kinh hoàng.

## VI. Đặc Sản Môn Phái (门派特产)
Giáp xác bọ giáp rụng ra theo chu kỳ lột xác chứa thiết khoáng quý, có thể dùng làm nguyên liệu rèn pháp khí hạ phẩm hoặc gia cố khiên chắn. Tuy nhiên, đây là sản phẩm tự nhiên chứ không phải hàng hóa được đàn chủ động bán, một số thương nhân lén thu gom giáp xác rụng mà không xin phép, khiến đàn dần mất lòng tin với con người. Ngoài ra, phân bọ giáp là loại phân bón linh lực thượng hạng cho cây trồng sa mạc, tuy ít người biết đến công dụng này.

## VII. Cơ Sở Hạ Tầng (基础设施)
Đàn không sở hữu bất kỳ cơ sở hạ tầng cố định nào. Các trạm dừng chân trên Thiên Sa Thương Đạo đóng vai trò "nhà tạm" cho đàn, nơi bọ giáp nghỉ ngơi, ấu trùng được cho ăn, và giáp xác bị hư hỏng được để tự phục hồi. Thiết Giáp Hùng thường chọn những trạm dừng có nền đá cứng để đàn có thể gõ giáp xác vào đá, kích thích quá trình hấp thu kim linh và gia cố giáp. Mối quan hệ giữa đàn và các trạm dừng mang tính cộng sinh, trạm dừng được bảo vệ khi đàn ở đó, và đàn được cung cấp nước và thức ăn.

## VIII. Kinh Tế (经济)
Nền kinh tế của đàn đơn giản và nguyên thủy, hoàn toàn dựa trên trao đổi dịch vụ. Thương đoàn thuê đàn hộ tống bằng cách cung cấp khoáng linh giúp bọ giáp tăng cường giáp xác, cùng với thức ăn đủ nuôi cả đàn trong suốt hành trình. Thiết Giáp Hùng không hiểu khái niệm tiền tệ nhưng hiểu rõ giá trị của khoáng linh và lòng trung thành. Nhiều thương đoàn tranh nhau thuê đàn vì uy tín bảo vệ tuyệt đối, tạo nên một thị trường cạnh tranh mà Thiết Giáp Hùng vô tình hưởng lợi từ đó.

## IX. Lịch Sử Tóm Tắt (简史)
Thiết Giáp Yêu Thú ban đầu là đàn bọ hoang dã sống rải rác trên sa mạc, được thương nhân phát hiện và lợi dụng bằng cách cho ăn khoáng linh. Dần dần, mối quan hệ cộng sinh hình thành một cách tự nhiên: thương đoàn cung cấp thức ăn quý giá, bọ giáp đáp lại bằng sự bảo vệ trung thành. Thiết Giáp Hùng hiện tại là cá thể thông minh nhất từng xuất hiện trong đàn, tự học cách hiểu ý con người và điều phối cả đàn theo đội hình chiến đấu có tổ chức. Dưới sự lãnh đạo của nó, đàn từ một nhóm yêu thú hỗn loạn trở thành lực lượng hộ tống có kỷ luật, được nhiều thương đoàn lớn trên Thiên Sa Thương Đạo tin tưởng và tranh nhau thuê mướn.

## X. Giai Thoại & Bí Mật (轶事与秘密)
Thiết Giáp Hùng từng một mình đứng chắn trước cả đàn Sa Mãng tấn công thương đoàn trong một trận chiến khốc liệt. Giáp xác bị nứt ba chỗ, một chân bị gãy, nhưng nó không lùi một bước cho đến khi đàn Sa Mãng rút lui. Vết nứt đó đến nay vẫn còn, trở thành "huân chương" mà thương nhân kể lại với giọng đầy kính nể. Một số thương nhân phát hiện rằng giáp xác rụng của bọ giáp chứa thiết khoáng quý hiếm, bắt đầu lén thu gom và bán kiếm lời. Hành vi này đang khiến đàn bọ dần mất lòng tin với con người, và nếu không được ngăn chặn, mối quan hệ cộng sinh kéo dài hàng trăm năm có thể tan vỡ.

Gần đây, một số thương nhân bắt đầu nhận ra rằng Thiết Giáp Hùng đang trở nên thông minh hơn rõ rệt — nó bắt đầu hiểu khái niệm "số lượng" (từ chối hộ tống khi khoáng linh ít hơn thường lệ), phân biệt được "thương nhân quen" và "thương nhân lạ" (đòi giá cao hơn cho người mới), và thậm chí thể hiện sự giận dữ có chủ đích khi phát hiện thương nhân lén thu gom giáp xác rụng. Nếu trí tuệ của Thiết Giáp Hùng tiếp tục phát triển, một ngày nào đó nó có thể đủ thông minh để nhận ra rằng mình đang bị lợi dụng — và khi đó, mối quan hệ cộng sinh kéo dài hàng trăm năm sẽ bước vào giai đoạn hoàn toàn mới.

## XI. Quan Hệ Thế Lực (势力关系)
- **Thiên Sa Thương Hội:** Quan hệ cộng sinh lâu đời, thương hội là nguồn cung cấp khoáng linh và thức ăn chính cho đàn, đổi lại được hộ tống trung thành.
- **Cự Tộc Phu Khuân Vác:** Bằng hữu tự nhiên, Cự Nhân và bọ giáp cùng dừng chân tại các trạm dừng, chia sẻ thức ăn và không gian nghỉ ngơi.
- **Sa Tặc Liên Minh:** Kẻ thù thường xuyên giao chiến, sa tặc cướp phá thương đoàn là mối đe dọa mà đàn phải đối mặt liên tục trên thương đạo.
