---
type: faction
name: Độc Đảo Lưu Dân
hantu: 毒岛流民
faction_type: Bộ Lạc
alignment: 1
race: Đa chủng tộc (Phàm nhân, Phế tu, Tội phạm)
region: Đông Hoang
founded: 80 năm trước
founder: Mạc Lão Đầu
emblem: Gieng_Nuoc_Giua_Suong_Doc.png
specialty: Sinh tồn vùng độc, Giải độc dân gian, Bùn cách ly khí độc
economy:
- Tự cung tự cấp hoàn toàn
- Thu hoạch rau rêu trên đảo
- Khai thác bùn đầm lầy đặc biệt
arcs:
  - arc: 1
    status: Cô lập sinh tồn
    rank: Không Xếp Hạng
    leader: Trưởng Thôn Mạc Lão Đầu
    population: 150
    territory:
      - Hòn đảo giữa Đầm Lầy Tử Thần
    assets:
      - name: Giếng Nước Ngọt Kỳ Lạ
        type: Tài Nguyên
      - name: Bùn Đầm Lầy Đặc Biệt
        type: Tài Nguyên
    stats: [10, 30, 15, 150, 20, 5]
    divisions:
      - name: Hội Đồng Sinh Tồn
        role: Quản lý phân công lao động, phân phối nước và thức ăn, giải quyết tranh chấp
        headcount:
          truong_lao: 5
          chien_binh: 10
          dan_thuong: 135
        members:
          - character: Mạc Lão Đầu
            position: Trưởng Thôn
            cultivation: Luyện Khí Đỉnh Phong
          - character: "[Lão Nhân Bí Ẩn]"
            position: Dân cư
            cultivation: Không rõ (Nghi ngờ cao thủ ẩn thân)
            placeholder: true
    relationships:
      - faction: Vạn Độc Môn
        description: Kẻ thù gián tiếp, một số lưu dân từng bị Vạn Độc Môn truy sát trước khi trốn ra đảo. Vạn Độc Môn không biết đảo tồn tại.
        diplomacy:
          lien_minh: -30
          tin: -60
          uy_hiep: 50
          thuong_mai: 0
          on_oan: -50
          le_thuoc: 0
      - faction: Phế Linh Các
        description: Tiềm năng liên minh do nhiều phế linh căn tu sĩ trên đảo có hoàn cảnh tương tự thành viên Phế Linh Các.
        diplomacy:
          lien_minh: 10
          tin: 20
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 0
      - faction: Hoàng Tuyền Cứu Hộ Đội
        description: Hoàng Tuyền Cứu Hộ Đội từng vô tình phát hiện sương mù quanh đảo khi cứu hộ gần đầm lầy, nhưng chưa tiếp cận được.
        diplomacy:
          lien_minh: 0
          tin: 10
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 0
          le_thuoc: 0
---

# ĐỘC ĐẢO LƯU DÂN (毒岛流民)

## I. Tổng Quan (总览)
Độc Đảo Lưu Dân là một cộng đồng cô lập gồm khoảng một trăm năm mươi người — phàm nhân, phế tu, tàn binh, tội phạm trốn chạy — sống trên một hòn đảo nhỏ giữa Đầm Lầy Tử Thần. Không có ai chọn đến đây vì muốn, mà vì không còn nơi nào khác chịu chấp nhận họ. Với triết lý "Ở đây không ai hỏi ngươi từ đâu đến, chỉ hỏi ngươi có chịu nổi mùi không", cộng đồng này là nơi trú ẩn cuối cùng cho những kẻ bị thế giới ruồng bỏ, được bảo vệ bởi chính khí độc chết người bao quanh — thứ mà phần lớn kẻ mạnh không thèm vượt qua.

## II. Địa Lý & Tài Nguyên (地理与资源)
Hòn đảo là bãi đất bồi nhỏ giữa Đầm Lầy Tử Thần, đường kính chưa đầy hai dặm, chỉ có thể tiếp cận bằng thuyền nan qua lớp sương độc dày đặc. Đất pha cát và mùn thực vật, chỉ trồng được rau rêu tầm thường nhưng vô hại. Địa hình bằng phẳng, không có che chắn tự nhiên ngoài vài bụi cây còi cọc. Trung tâm đảo có một giếng nước ngọt duy nhất — điều kỳ lạ không thể giải thích giữa vùng đầm lầy độc. Nước giếng không chỉ sạch mà còn có tác dụng giải nhẹ độc tố trong cơ thể, chính nhờ nguồn nước này mà dân cư sống được giữa sương độc. Bùn đầm lầy quanh đảo có đặc tính kỳ lạ: bôi lên da có thể cách ly khí độc tạm thời, cho phép ngư dân ra ngoài đánh cá và thu hoạch rong rêu.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
Cộng đồng không có tín ngưỡng chính thức — phần lớn dân cư đã mất niềm tin vào mọi thần linh và thế lực sau khi bị cuộc đời ruồng bỏ. Thay vào đó, họ tin vào quy tắc đơn giản do Mạc Lão Đầu đặt ra: ai ở trên đảo đều phải đóng góp sức lao động, không cướp bóc lẫn nhau, nước giếng chia đều cho mọi người bất kể thân phận. Mỗi tối, cả cộng đồng quây quần quanh đống lửa kể chuyện — đây là hình thức giải trí duy nhất và cũng là cách truyền đạt kiến thức sinh tồn cho thế hệ sau. Không ai hỏi quá khứ của người khác, không ai phán xét — trên đảo, mọi người đều bình đẳng vì đều đã mất hết.

## IV. Cơ Cấu Tổ Chức (组织结构)
Trưởng Thôn Mạc Lão Đầu là phàm nhân sinh ra với linh căn phế, tự mày mò tu luyện đến Luyện Khí Đỉnh Phong nhờ nước giếng kỳ lạ bồi bổ kinh mạch suốt tám mươi năm. Tuổi đã ngoài một trăm nhưng vẫn minh mẫn, tóc bạc trắng, mắt đục nhưng tinh anh. Ông lãnh đạo bằng kinh nghiệm và sự công bằng, không bằng sức mạnh. Hội Đồng Trưởng Lão gồm năm người lớn tuổi nhất — hỗn hợp phàm nhân và Luyện Khí Sơ Kỳ — phụ trách phân công lao động hàng ngày: ai đi đánh cá, ai trồng rau, ai canh giếng. Một trăm năm mươi dân cư gồm đủ thành phần: phàm nhân già yếu, phế linh căn tu sĩ, tàn phế quân bị thương, tội phạm trốn truy sát. Mười người khỏe nhất tự nguyện làm đội tuần tra, canh chừng thuyền lạ tiếp cận đảo.

## V. Công Pháp & Trận Pháp (功法与阵法)
- **Công Pháp:** Không có công pháp hay trận pháp chính thức. Phòng thủ hoàn toàn dựa vào Đầm Lầy Tử Thần — kẻ nào muốn tấn công phải vượt qua hàng dặm sương độc chí mạng trước khi chạm được đến đảo. Vài phế tu trên đảo còn giữ được chút tu vi tàn dư, biết một hai chiêu tự vệ cơ bản, nhưng không đáng kể. Mạc Lão Đầu biết cách điều khiển bùn đầm lầy ở mức sơ đẳng — đủ để lái thuyền qua sương độc, không đủ để chiến đấu.
- **Trận Pháp:** Đầm Lầy Tử Thần bản thân đã là "trận pháp tự nhiên" hoàn hảo — sương độc giết chết Trúc Cơ trở xuống, làm suy yếu nghiêm trọng Kim Đan, và khiến bất kỳ ai mất phương hướng trong lớp sương dày đặc.

## VI. Đặc Sản Môn Phái (门派特产)
- **Bùn Cách Ly Khí Độc:** Bùn đầm lầy quanh đảo có đặc tính cách ly khí độc khi bôi lên da, tác dụng kéo dài vài canh giờ. Nếu được khai thác và bán ra ngoài, đây sẽ là sản phẩm cực kỳ giá trị cho bất kỳ ai hoạt động trong vùng độc — nhưng dân đảo không có kênh phân phối.
- **Nước Giếng Giải Độc:** Nước giếng trung tâm đảo có khả năng giải nhẹ hầu hết các loại độc tố phổ biến. Uống lâu dài còn có tác dụng tăng cường sức đề kháng với chất độc.
- **Kiến Thức Sinh Tồn Đầm Lầy:** Tám mươi năm sống giữa đầm lầy độc giúp dân đảo tích lũy kiến thức sinh tồn vô giá: cách nhận biết hướng gió để tránh sương độc đặc, loại rong rêu nào ăn được và loại nào chết người, thời điểm nào sương tan để ra ngoài an toàn.

## VII. Cơ Sở Hạ Tầng (基础设施)
- **Giếng Nước Trung Tâm:** Giếng đá tự nhiên sâu không thấy đáy, nước trong vắt và mát lạnh quanh năm. Được canh gác ngày đêm và chia nước theo khẩu phần — mỗi người một bát sáng, một bát tối.
- **Nhà Lều Dân Cư:** Khoảng ba mươi túp lều nhỏ xây từ bùn khô, gỗ trôi và lá rêu, xếp thành vòng tròn quanh giếng. Đơn sơ nhưng đủ che mưa che nắng.
- **Bến Thuyền Nan:** Bến nhỏ ở bờ đông đảo, nơi neo đậu mười chiếc thuyền nan — phương tiện duy nhất để ra ngoài đánh cá và thu hoạch rong rêu. Mỗi thuyền chỉ chở được hai người cùng một lớp bùn cách ly dày bôi khắp người.

## VIII. Kinh Tế (经济)
Kinh tế hoàn toàn tự cung tự cấp và ở mức sinh tồn tối thiểu. Thức ăn đến từ rau rêu trồng trên đảo, rong biển và cá đánh từ vùng nước quanh đầm lầy (phải bôi bùn cách ly trước khi ra ngoài), và đôi khi vài con thú nhỏ bắt được trên đảo. Không có tiền tệ, không có thương mại — mọi thứ chia sẻ theo nhu cầu. Cộng đồng gần như không tiếp xúc với thế giới bên ngoài, ngoại trừ rất hiếm khi có người mới trôi dạt đến.

## IX. Lịch Sử Tóm Tắt (简史)
Tám mươi năm trước, Mạc Lão Đầu — lúc đó chỉ là thanh niên phàm nhân linh căn phế — bị một thương nhân bỏ rơi giữa Đầm Lầy Tử Thần. Trong lúc tuyệt vọng, hắn tình cờ trôi dạt đến hòn đảo và phát hiện giếng nước ngọt cứu mạng. Dần dần, những kẻ tuyệt vọng khác tìm đến — người bị Vạn Độc Môn truy sát chạy vào đầm lầy liều chết, nô lệ trốn thoát bám theo dòng nước, phế nhân bị gia tộc ruồng bỏ lang thang cho đến khi lạc đến đây. Mạc Lão Đầu chưa bao giờ từ chối ai, miễn là người đó chấp nhận quy tắc của đảo. Tám mươi năm qua, cộng đồng phát triển lên một trăm năm mươi người, tự cung tự cấp và gần như cô lập hoàn toàn.

## X. Giai Thoại & Bí Mật (轶事与秘密)
Giếng nước trên đảo có thể là tàn tích của một linh mạch cổ đại — Mạc Lão Đầu nghi ngờ đáy giếng dẫn đến một không gian bí ẩn, vì đôi khi ban đêm giếng phát ra ánh sáng xanh lục nhẹ từ tận sâu. Chính nguồn nước này đã giúp ông tu luyện từ phàm nhân linh căn phế lên Luyện Khí Đỉnh Phong — điều bất khả thi theo lẽ thường. Nhưng không ai trên đảo đủ tu vi để lặn xuống thăm dò.

Trong số lưu dân có một lão nhân câm lặng đến đảo ba mươi năm trước — dáng vẻ tầm thường, mặc áo vải rách, suốt ngày ngồi câu cá ở bờ tây. Nhưng đôi khi vào ban đêm, Mạc Lão Đầu cảm nhận được từ lão nhân tỏa ra khí tức khiến ông rùng mình — thứ uy áp mà chỉ có cường giả thực sự mới có. Không ai dám hỏi lai lịch, và lão nhân cũng không bao giờ nói.

Gần đây, thuyền lạ bắt đầu xuất hiện trong sương mù đầm lầy — không phải thuyền nan của dân đảo mà là thuyền gỗ cứng có khắc phù văn chống độc. Ai đó đang tìm đường đến đảo một cách có chủ đích, nhưng chưa rõ mục đích thiện hay ác.

## XI. Quan Hệ Thế Lực (势力关系)
- **Vạn Độc Môn:** Kẻ thù gián tiếp. Nhiều lưu dân trên đảo từng bị Vạn Độc Môn truy sát trước khi trốn vào đầm lầy. Nếu Vạn Độc Môn biết đảo tồn tại, hậu quả khó lường.
- **Phế Linh Các:** Tiềm năng đồng cảm — Phế Linh Các quy tụ phế tu bị ruồng bỏ, hoàn cảnh tương tự nhiều dân cư trên đảo. Nhưng hai bên chưa biết đến sự tồn tại của nhau.
- **Hoàng Tuyền Cứu Hộ Đội:** Đội Cứu Hộ đã phát hiện sương mù bất thường quanh khu vực đảo nhưng chưa tiếp cận được, có thể là hy vọng liên lạc với bên ngoài trong tương lai.
