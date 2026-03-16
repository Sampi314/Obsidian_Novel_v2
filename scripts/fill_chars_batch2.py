#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fill in character details for Nam Cương factions (batch 2)."""

import os
import unicodedata

BASE = '/Users/sampi_wu/Documents/GitHub/Obsidian_Novel_v2/Đạo/Nhân_Vật/Nam_Cương'

# Each entry: "faction_dir/filename" -> (section_ii, section_iii, section_iv, section_v)
CHARACTERS = {

# ============================================================
# HUYẾT MA TÔNG (血魔宗)
# ============================================================

"Huyết_Ma_Tông/Huyết_Tôn.md": (
# II
"Dáng người cao gầy, da trắng bệch như chưa từng thấy ánh mặt trời, đôi mắt đỏ sẫm luôn toát ra uy áp khiến người đối diện không dám nhìn thẳng. Tóc bạc trắng buông dài, thường mặc huyết y đỏ thẫm, trên người phảng phất mùi tanh nhẹ của máu. Tính cách lạnh lùng, tàn nhẫn nhưng cực kỳ kiên nhẫn — sẵn sàng ẩn nhẫn hàng trăm năm để tái thiết Huyết Ma Tông từ đống tro tàn.",
# III
"Chuyên tu luyện Huyết Ma Đại Pháp, có thể hấp thu tinh huyết của kẻ khác để tăng cường tu vi. Sở hữu chiêu thức cấm \"Vạn Huyết Quy Tông\" — triệu hồi toàn bộ huyết khí trong bán kính trăm trượng về một điểm, gây sát thương hủy diệt. Ngoài ra còn tinh thông Huyết Độn Thuật, có thể hóa thân thành sương máu để di chuyển tức thời.",
# IV
"""- **[[Mộ Dung Huyết Thiên]]** — Thái Thượng Trưởng Lão, bậc tiền bối mà Huyết Tôn tôn kính nhất, người truyền thụ Huyết Ma Đại Pháp.
- **[[Cừu Thiên]]** — Đệ Nhất Huyết Tướng, cánh tay phải đắc lực nhất, được giao nhiệm vụ chinh phạt bên ngoài.
- **[[Trương Phách]]** — Huyết Nô Viện Chủ, quản lý nguồn huyết nô cung cấp tài nguyên tu luyện cho tông môn.""",
# V
"Huyết Tôn vốn là một tu sĩ vô danh bị bỏ rơi trong chiến loạn Nam Cương, suýt chết vì trọng thương. Được Mộ Dung Huyết Thiên cứu sống bằng huyết thuật và thu làm đệ tử. Sau khi Huyết Ma Tông bị liên minh các phái đánh tan, Huyết Tôn cùng tàn dư ẩn mình trong vùng sơn cốc hẻo lánh, âm thầm tái thiết thế lực suốt hai trăm năm. Hiện tại đã gây dựng lại bốn Huyết Tướng và hệ thống Huyết Nô Viện, chỉ chờ thời cơ chín muồi để trở lại."
),

"Huyết_Ma_Tông/Mộ_Dung_Huyết_Thiên.md": (
# II
"Hình hài là một lão nhân khô gầy, da nhăn nheo như vỏ cây khô, nhưng đôi mắt đỏ rực vẫn sáng như hai ngọn đèn huyết. Thân hình tuy nhỏ bé nhưng khí thế cổ xưa, mỗi bước đi đều khiến không khí xung quanh nặng nề. Tính cách trầm mặc ít nói, nhưng một khi mở miệng thì lời nào cũng mang trọng lượng tuyệt đối trong tông môn.",
# III
"Là người tu luyện Huyết Ma Đại Pháp lâu đời nhất, đã đạt đến cảnh giới \"Huyết Hải Vô Nhai\" — có thể biến linh lực thành biển máu nuốt chửng mọi thứ. Sở hữu bí thuật thất truyền \"Cửu Chuyển Huyết Liên\" cho phép tái sinh từ một giọt máu. Dù tuổi tác đã cao nhưng chiến lực đỉnh phong vẫn đủ sức đe dọa bất kỳ Nguyên Anh cường giả nào trong Nam Cương.",
# IV
"""- **[[Huyết Tôn]]** — Đệ tử ruột, người kế thừa Huyết Ma Tông mà lão đã đích thân truyền thụ công pháp.
- **[[Hà Minh Phong]]** — Đệ Nhị Huyết Tướng, đệ tử thế hệ thứ hai mà lão đánh giá cao nhất về mưu lược.""",
# V
"Mộ Dung Huyết Thiên là Trưởng Lão cuối cùng còn sống sót từ thời Huyết Ma Tông cực thịnh, đã tu luyện hơn tám trăm năm. Trong trận đại chiến với liên minh chính đạo, lão bị trọng thương suýt chết nhưng nhờ Cửu Chuyển Huyết Liên mà tái sinh. Sau đó thu nhận Huyết Tôn làm đệ tử và giao lại quyền lãnh đạo, lui về hậu phương tĩnh dưỡng. Hiện tại thường xuyên bế quan, chỉ xuất hiện khi tông môn gặp nguy cấp."
),

"Huyết_Ma_Tông/Cừu_Thiên.md": (
# II
"Thân hình vạm vỡ như tháp sắt, cao hơn hai mét, toàn thân phủ đầy sẹo chiến đấu. Mái tóc đỏ rực như lửa, đôi mắt hung dữ luôn tràn đầy sát khí. Tính cách nóng nảy, hiếu chiến, coi việc chiến đấu là niềm vui lớn nhất, thường xuyên tự ý ra ngoài tìm người giao đấu bất chấp lệnh của Tông Chủ.",
# III
"Chuyên tu Cuồng Huyết Chiến Thể — biến máu trong người thành giáp trụ và vũ khí, càng bị thương càng mạnh. Sử dụng đại phủ (rìu lớn) nặng nghìn cân tẩm huyết khí, mỗi nhát chém có thể xẻ núi. Chiêu tuyệt mệnh \"Huyết Bạo\" kích hoạt toàn bộ huyết mạch trong người, tạm thời nâng chiến lực lên gấp ba nhưng sau đó kiệt sức hoàn toàn.",
# IV
"""- **[[Huyết Tôn]]** — Tông Chủ, người mà Cừu Thiên tuyệt đối trung thành dù thường xuyên làm trái ý.
- **[[Cừu Tiểu Đao]]** — Con trai ruột, đang được Cừu Thiên huấn luyện trở thành chiến sĩ mạnh nhất thế hệ mới.
- **[[Hà Minh Phong]]** — Đệ Nhị Huyết Tướng, người mà Cừu Thiên khinh thường vì chỉ biết dùng mưu kế.""",
# V
"Cừu Thiên xuất thân từ một bộ lạc chiến binh ở vùng biên giới Nam Cương, từ nhỏ đã sống bằng việc săn yêu thú. Bị Huyết Tôn đánh bại và khuất phục, từ đó trở thành Đệ Nhất Huyết Tướng trung thành nhất. Trong các cuộc tập kích bí mật để thu thập tài nguyên cho tông môn, Cừu Thiên luôn là người xung phong đầu tiên. Có một đứa con trai tên Cừu Tiểu Đao đang theo hắn học nghệ."
),

"Huyết_Ma_Tông/Hà_Minh_Phong.md": (
# II
"Dáng người thanh mảnh, gương mặt trắng trẻo như thư sinh, luôn mang theo nụ cười nhẹ nhàng khiến người ta mất cảnh giác. Mặc trường bào trắng sạch sẽ, tay luôn cầm quạt xếp, trông không giống tu sĩ tà đạo mà giống một mưu sĩ cung đình. Tính cách thâm trầm, đa mưu túc trí, mọi hành động đều được tính toán kỹ lưỡng từ trước.",
# III
"Tu luyện Huyết Ty Thuật — điều khiển sợi máu mỏng như tơ nhện nhưng sắc bén hơn đao kiếm, có thể giăng bẫy trong bán kính rộng. Giỏi bày trận pháp huyết mạch, biến cả một khu vực thành tử địa mà kẻ địch không hề hay biết. Không mạnh về đối đầu trực diện nhưng trong chiến thuật phục kích và ám sát thì hiếm ai sánh bằng.",
# IV
"""- **[[Huyết Tôn]]** — Tông Chủ, người trọng dụng Hà Minh Phong làm quân sư chiến lược.
- **[[Hà Linh]]** — Con gái ruột, đang được cha bí mật dạy Huyết Ty Thuật ngoài giờ tu luyện chính thức.
- **[[Cừu Thiên]]** — Đệ Nhất Huyết Tướng, kẻ mà Hà Minh Phong phải thường xuyên dọn dẹp hậu quả sau mỗi lần gây rối.""",
# V
"Hà Minh Phong vốn là một mưu sĩ của tiểu thế gia ở Nam Cương, bị gia tộc phản bội và suýt bị diệt khẩu. Được Huyết Tôn cứu mạng và thu nạp vào tông môn, nhanh chóng chứng minh giá trị bằng tài mưu lược xuất chúng. Là người vạch ra kế hoạch tái thiết Huyết Ma Tông từng bước một, bao gồm cả việc thiết lập mạng lưới gián điệp ở các thành trấn. Có một con gái tên Hà Linh cũng đang tu luyện trong tông môn."
),

"Huyết_Ma_Tông/Lý_Ám.md": (
# II
"Thân hình mảnh khảnh, di chuyển không một tiếng động, như bóng ma lướt trên mặt đất. Gương mặt xanh xao, đôi mắt đen thẳm không cảm xúc, thường ẩn mình trong bóng tối. Tính cách lặng lẽ, ít giao tiếp, chỉ xuất hiện khi được Tông Chủ triệu tập hoặc khi có mục tiêu cần giải quyết.",
# III
"Chuyên tu Huyết Ảnh Thuật — hòa nhập bản thân vào bóng tối, trở thành vô hình hoàn toàn. Sử dụng đoản đao tẩm huyết độc, chỉ cần một vết cắt nhỏ cũng đủ khiến nạn nhân mất hết sức chiến đấu. Là sát thủ số một của Huyết Ma Tông, chuyên thực hiện các nhiệm vụ ám sát và do thám.",
# IV
"""- **[[Huyết Tôn]]** — Tông Chủ, người duy nhất mà Lý Ám tuyệt đối phục tùng.
- **[[Tôn Hàn Thiết]]** — Đệ Tứ Huyết Tướng, đồng liêu mà Lý Ám thỉnh thoảng phối hợp trong nhiệm vụ.
- **[[Hà Minh Phong]]** — Đệ Nhị Huyết Tướng, người thường xuyên giao nhiệm vụ tình báo cho Lý Ám.""",
# V
"Lý Ám là trẻ mồ côi lớn lên trong khu ổ chuột của một thành trấn biên giới Nam Cương, sống bằng nghề trộm cắp từ nhỏ. Bị Huyết Tôn phát hiện thiên phú ẩn thân phi thường và thu nạp vào tông. Qua nhiều năm huấn luyện khắc nghiệt, trở thành Đệ Tam Huyết Tướng chuyên trách ám sát và trinh sát. Đã thực hiện hàng chục nhiệm vụ mà không ai phát hiện tung tích."
),

"Huyết_Ma_Tông/Tôn_Hàn_Thiết.md": (
# II
"Thân hình vạm vỡ như gấu, da đen sạm vì rèn luyện dưới nắng, toàn thân cơ bắp cuồn cuộn. Gương mặt vuông vức, râu quai nón rậm, đôi mắt kiên định tựa đá. Tính cách trầm ổn, kiên nhẫn, là người đáng tin cậy nhất trong Tứ Đại Huyết Tướng, chuyên đứng ra bảo vệ tông môn khi bị tấn công.",
# III
"Tu luyện Huyết Giáp Thuật — ngưng tụ huyết khí thành lớp giáp phòng ngự cứng như thép trên toàn thân. Sử dụng khiên lớn và thương dài, chuyên phòng thủ trận địa. Chiêu thức \"Thiết Bích Huyết Thành\" tạo ra bức tường huyết khí bất khả xâm phạm, có thể chống đỡ đòn tấn công liên tục từ nhiều kẻ địch cùng lúc.",
# IV
"""- **[[Huyết Tôn]]** — Tông Chủ, người mà Tôn Hàn Thiết nguyện lấy mạng bảo vệ.
- **[[Cừu Thiên]]** — Đệ Nhất Huyết Tướng, thường xuyên phối hợp chiến đấu — Cừu Thiên tấn công, Tôn Hàn Thiết phòng thủ.
- **[[Lý Ám]]** — Đệ Tam Huyết Tướng, đồng liêu ít nói nhưng đáng tin cậy trong nhiệm vụ.""",
# V
"Tôn Hàn Thiết xuất thân từ một gia tộc thợ rèn ở Nam Cương, từ nhỏ đã quen với lửa nóng và kim loại. Gia tộc bị diệt bởi thổ phỉ, một mình sống sót nhờ thể chất cường tráng phi thường. Được Huyết Tôn thu nạp và truyền thụ Huyết Giáp Thuật, trở thành bức tường thành vững chắc nhất của Huyết Ma Tông. Luôn tự nhận mình là lá chắn cuối cùng của tông môn."
),

"Huyết_Ma_Tông/Trương_Phách.md": (
# II
"Dáng người tầm thước, gương mặt bình thường dễ lẫn vào đám đông, nhưng ánh mắt lạnh lùng tàn nhẫn khi nhìn huyết nô. Luôn mặc áo choàng xám bẩn vấy máu khô, tay đeo găng da dày. Tính cách tàn ác với kẻ dưới nhưng khúm núm với bề trên, là kẻ điển hình của loại người bắt nạt yếu sợ mạnh.",
# III
"Tinh thông Huyết Khống Thuật — điều khiển huyết mạch của người khác từ xa, biến họ thành con rối. Có thể đồng thời khống chế hàng chục huyết nô chiến đấu theo ý mình. Bản thân chiến lực không cao nhưng nhờ quân đoàn huyết nô mà trở thành lực lượng đáng sợ.",
# IV
"""- **[[Huyết Tôn]]** — Tông Chủ, người giao quyền quản lý toàn bộ Huyết Nô Viện.
- **[[Cừu Thiên]]** — Đệ Nhất Huyết Tướng, thường xuyên yêu cầu cung cấp huyết nô cho các chiến dịch.
- **[[Ân Thiết]]** — Nội Môn đệ tử, phụ tá đắc lực trong việc quản lý huyết nô hàng ngày.""",
# V
"Trương Phách vốn là thương nhân buôn nô lệ ở chợ đen Nam Cương, bị Huyết Ma Tông ép gia nhập vì có kinh nghiệm quản lý \"hàng hóa\" sống. Tuy miễn cưỡng lúc đầu nhưng sau khi học được Huyết Khống Thuật, hắn phát hiện niềm vui bệnh hoạn trong việc điều khiển người khác. Hiện quản lý hơn ba trăm huyết nô, cung cấp nguồn lực huyết khí chính cho toàn tông."
),

"Huyết_Ma_Tông/Cừu_Tiểu_Đao.md": (
# II
"Thanh niên mười tám tuổi, thừa hưởng thể hình cao lớn của cha nhưng gương mặt trẻ trung hơn nhiều. Tóc đỏ ngắn dựng đứng, ánh mắt háo thắng, luôn mang theo thanh đao đỏ trên lưng. Tính cách bộc trực, nóng nảy giống cha, nhưng có phần ngây thơ và trọng nghĩa khí hơn so với các trưởng bối trong tông.",
# III
"Đang tu luyện phiên bản cơ bản của Cuồng Huyết Chiến Thể do cha truyền dạy, tuy chưa thành thục nhưng tiềm lực rất lớn. Sử dụng đơn đao, đao pháp trực diện mãnh liệt, thiên về tấn công áp đảo. Có thể kích hoạt \"Tiểu Huyết Bạo\" trong thời gian ngắn nhưng sau đó sẽ bất tỉnh.",
# IV
"""- **[[Cừu Thiên]]** — Cha ruột kiêm sư phụ, người mà Tiểu Đao vừa kính trọng vừa muốn vượt qua.
- **[[Hà Linh]]** — Đồng môn cùng lứa, thường xuyên tranh cãi nhưng ngầm coi nhau là bạn.""",
# V
"Cừu Tiểu Đao sinh ra và lớn lên trong Huyết Ma Tông, chưa từng biết thế giới bên ngoài. Được cha Cừu Thiên huấn luyện chiến đấu từ khi biết đi, coi việc tu luyện huyết thuật là lẽ tự nhiên. Tuy nhiên, bản tính trọng nghĩa khí khiến hắn đôi khi lén giúp đỡ huyết nô bị đối xử tàn ác, điều mà cha hắn không hề biết."
),

"Huyết_Ma_Tông/Hà_Linh.md": (
# II
"Thiếu nữ mười sáu tuổi, dung mạo thanh tú thừa hưởng từ cha, da trắng mịn, đôi mắt sáng lanh lợi. Tóc đen dài buộc gọn, thích mặc y phục gọn gàng tiện di chuyển. Tính cách thông minh, hay quan sát, ít bộc lộ cảm xúc trước mặt người lạ nhưng với người thân thì hoạt bát hơn nhiều.",
# III
"Được cha bí mật truyền dạy Huyết Ty Thuật cơ bản, có thể tạo ra vài sợi huyết ty để phòng thân. Ngoài ra tinh thông thuật chế tạo phù lục huyết mạch — loại bùa chú dùng máu làm mực. Tu vi tuy chưa cao nhưng trí tuệ sắc bén, giỏi phân tích trận pháp và tìm điểm yếu.",
# IV
"""- **[[Hà Minh Phong]]** — Cha ruột, người luôn bảo vệ và dìu dắt nàng trong bóng tối.
- **[[Cừu Tiểu Đao]]** — Đồng môn cùng thế hệ, hay cãi nhau nhưng thực ra rất quan tâm lẫn nhau.""",
# V
"Hà Linh sinh ra trong Huyết Ma Tông, được cha Hà Minh Phong nuôi dạy cẩn thận, vừa tu luyện vừa học mưu lược. Là một trong ít người trẻ trong tông biết đọc sách và nghiên cứu trận pháp. Dù sống trong môi trường tà đạo nhưng bản tính không tàn ác, thường âm thầm giảm nhẹ hình phạt cho huyết nô khi cha không để ý."
),

"Huyết_Ma_Tông/Ân_Thiết.md": (
# II
"Thanh niên hai mươi tuổi, thể hình trung bình, gương mặt hiền lành trông không giống đệ tử tà phái. Da hơi xanh xao do thường xuyên ở trong Huyết Nô Viện, đôi mắt mệt mỏi nhưng kiên định. Tính cách trầm lặng, chăm chỉ, làm việc không kêu ca, là loại người mà ai cũng dễ bỏ qua.",
# III
"Tu luyện Huyết Khí Cơ Bản Công, nắm vững các kỹ thuật quản lý và kiểm soát huyết nô cấp thấp. Biết sử dụng roi huyết — vũ khí tẩm huyết khí có thể gây đau đớn mà không để lại thương tích. Chiến lực cá nhân không nổi bật nhưng am hiểu điểm yếu của huyết nô hơn bất kỳ ai.",
# IV
"""- **[[Trương Phách]]** — Huyết Nô Viện Chủ, thượng cấp trực tiếp, người giao việc hàng ngày.
- **[[Hà Linh]]** — Đồng môn, người mà Ân Thiết thầm cảm phục vì trí tuệ và sự nhân hậu hiếm có trong tông.""",
# V
"Ân Thiết là trẻ mồ côi được Huyết Ma Tông thu nhận từ nhỏ, lớn lên trong Huyết Nô Viện nên quen với cảnh máu me. Vì thiên phú tu luyện không cao nên bị phân công làm phụ tá quản lý thay vì chiến đấu tiền tuyến. Tuy vị trí thấp nhưng nhờ sự chăm chỉ và đáng tin cậy mà được Trương Phách trọng dụng."
),

# ============================================================
# QUỶ THỊ NAM CƯƠNG (鬼市南疆)
# ============================================================

"Quỷ_Thị_Nam_Cương/Mạc_Vô_Diện.md": (
# II
"Không ai từng thấy gương mặt thật của Mạc Vô Diện — luôn đeo mặt nạ trắng trơn không có bất kỳ nét vẽ nào, che kín toàn bộ đầu. Thân hình trung bình, mặc trường bào đen rộng, di chuyển không tiếng động như bóng ma. Tính cách bí ẩn, giọng nói biến đổi liên tục khiến không ai phân biệt được giới tính hay tuổi tác thật sự, mọi quyết định đều lạnh lùng và tuyệt đối công bằng trong giao dịch.",
# III
"Sở hữu Vô Diện Thuật — có thể thay đổi hoàn toàn ngoại hình, giọng nói, thậm chí khí tức tu vi trong thời gian dài. Tinh thông thuật cấm không gian, tạo ra các \"phòng giao dịch\" không gian xếp chồng bên trong Quỷ Thị. Chiến đấu thực sự cực kỳ hiếm khi xảy ra, nhưng những kẻ từng thách thức quyền uy của Quỷ Chủ đều biến mất không dấu vết.",
# IV
"""- **[[Chu Thiết Diện]]** — Trưởng Lão Chấp Pháp, cánh tay phải thực thi luật lệ Quỷ Thị.
- **[[Hồ Vô Thanh]]** — Tổng Quản, người điều hành mọi hoạt động hàng ngày theo chỉ thị của Quỷ Chủ.
- **[[Vương Cổ Thuyền]]** — Đưa Đò Trưởng, người kiểm soát con đường duy nhất dẫn vào Quỷ Thị.""",
# V
"Lai lịch của Mạc Vô Diện là bí ẩn lớn nhất Nam Cương — có người đồn đó là một nữ tu sĩ cổ đại, có kẻ cho rằng đó là yêu thú hóa hình. Quỷ Thị Nam Cương được lập ra từ hơn năm trăm năm trước, trở thành chợ đen lớn nhất vùng, nơi mà cả chính đạo lẫn tà đạo đều phải tuân thủ quy tắc. Dưới sự cai quản của Mạc Vô Diện, Quỷ Thị giữ lập trường trung lập tuyệt đối, không thiên vị bất kỳ thế lực nào."
),

"Quỷ_Thị_Nam_Cương/Chu_Thiết_Diện.md": (
# II
"Thân hình cao lớn uy nghi, luôn đeo mặt nạ sắt đen nặng nề che kín nửa trên gương mặt, để lộ hàm răng nghiến chặt và bộ râu đen rậm. Mặc giáp da đen, lưng đeo đại đao, bước đi nặng nề vang vọng khắp hành lang Quỷ Thị. Tính cách cứng nhắc, nghiêm khắc, thi hành luật lệ không chút nương tay, kể cả với người quen.",
# III
"Tu luyện Thiết Diện Công — mặt nạ sắt hợp nhất với thân thể, tạo ra lớp phòng ngự kiên cố và tăng cường sức mạnh thể chất. Sử dụng đại đao chấp pháp nặng ba trăm cân, mỗi nhát chém mang theo uy áp của luật lệ Quỷ Thị. Có thể phát động \"Thiết Diện Phán Quyết\" — khóa chặt mục tiêu trong vòng mười trượng, khiến đối phương không thể trốn thoát.",
# IV
"""- **[[Mạc Vô Diện]]** — Quỷ Chủ, thượng cấp tối cao mà Chu Thiết Diện tuyệt đối trung thành.
- **[[Ám Nhị]]** — Tổng Quản phụ, người hỗ trợ điều tra các vụ vi phạm luật lệ trong Quỷ Thị.
- **[[Lệ Tam]]** — Đấu Giá Sư, kẻ hay gây phiền phức bằng miệng lưỡi nhưng Chu Thiết Diện phải bảo vệ an toàn.""",
# V
"Chu Thiết Diện vốn là một võ phu lang thang, bị trọng thương và được Mạc Vô Diện cứu sống với điều kiện phải phục vụ Quỷ Thị suốt đời. Từ đó đeo mặt nạ sắt như biểu tượng của sự ràng buộc, trở thành Trưởng Lão Chấp Pháp đáng sợ nhất. Hơn hai trăm năm qua, không một kẻ vi phạm nào thoát khỏi tay hắn. Ngoài Quỷ Thị, hắn không có bất kỳ mối quan hệ hay mục đích sống nào khác."
),

"Quỷ_Thị_Nam_Cương/Vương_Cổ_Thuyền.md": (
# II
"Ông lão gầy gò, da đen sạm vì nắng gió sông nước, mặc áo tơi lá rách rưới, đội nón lá cũ kỹ. Đôi mắt nheo lại như luôn ngái ngủ, nhưng thực tế quan sát mọi thứ cực kỳ tinh tường. Tính cách chậm rãi, ít nói, thích ngâm nga những bài hát cổ kỳ lạ khi chèo đò, đối xử với khách vừa thân thiện vừa bí ẩn.",
# III
"Tinh thông Thủy Hành Thuật — điều khiển dòng nước và sương mù trên con sông dẫn vào Quỷ Thị, khiến kẻ không được phép vĩnh viễn lạc lối. Con thuyền của lão là pháp khí đặc biệt, có thể đi xuyên qua kết giới mà không cần mở cổng. Trong trường hợp bị tấn công, lão có thể triệu hồi xoáy nước nuốt chửng kẻ thù xuống đáy sông.",
# IV
"""- **[[Mạc Vô Diện]]** — Quỷ Chủ, người giao cho lão nhiệm vụ canh giữ lối vào duy nhất.
- **[[Hồ Vô Thanh]]** — Tổng Quản, người thường xuyên gửi danh sách khách được phép vào Quỷ Thị.""",
# V
"Vương Cổ Thuyền là dân chài sống trên sông từ nhỏ, tình cờ phát hiện lối vào Quỷ Thị khi đuổi theo một con cá lạ. Được Mạc Vô Diện giữ lại làm Đưa Đò Trưởng, lão dần dần tu luyện Thủy Hành Thuật và gắn bó với con sông hàng trăm năm. Không ai biết lão đã bao nhiêu tuổi, nhưng con thuyền cũ kỹ của lão là thứ duy nhất có thể đưa người qua vùng sương mù an toàn."
),

"Quỷ_Thị_Nam_Cương/Hồ_Vô_Thanh.md": (
# II
"Đàn ông trung niên, gương mặt tầm thường, đeo mặt nạ nửa mặt màu xám nhạt. Dáng đi nhẹ nhàng, luôn xuất hiện ở đúng nơi cần thiết mà không ai nhận ra. Tính cách cẩn thận, kín đáo, giao tiếp chủ yếu bằng cử chỉ và ghi chép trên giấy — rất ít khi mở miệng nói chuyện, thậm chí có người nghi ngờ hắn bị câm.",
# III
"Tu luyện Vô Thanh Thuật — triệt tiêu mọi âm thanh trong phạm vi nhất định, kể cả tiếng chân, tiếng thở, tiếng tim đập. Giỏi thuật nghe trộm ngược — dùng linh lực cảm nhận rung động không khí để nghe mọi cuộc trò chuyện trong Quỷ Thị. Chiến đấu trực diện không phải sở trường nhưng khả năng thu thập tình báo thì vô song.",
# IV
"""- **[[Mạc Vô Diện]]** — Quỷ Chủ, người duy nhất mà Hồ Vô Thanh báo cáo trực tiếp.
- **[[Ám Nhị]]** — Tổng Quản phụ, đồng sự chia sẻ gánh nặng quản lý hàng ngày.
- **[[Chu Thiết Diện]]** — Trưởng Lão Chấp Pháp, người mà Hồ Vô Thanh cung cấp thông tin vi phạm để xử lý.""",
# V
"Hồ Vô Thanh từng là gián điệp của một thế lực lớn, bị phát hiện và truy sát, chạy trốn vào Quỷ Thị xin tị nạn. Mạc Vô Diện đồng ý che chở với điều kiện hắn phải phục vụ vĩnh viễn, dùng tài năng tình báo để quản lý Quỷ Thị. Hàng chục năm qua, Hồ Vô Thanh trở thành tai mắt của Quỷ Chủ, nắm rõ mọi bí mật giao dịch trong chợ đen."
),

"Quỷ_Thị_Nam_Cương/Ám_Nhị.md": (
# II
"Thân hình nhỏ nhắn, giới tính khó phân biệt, đeo mặt nạ đen chỉ lộ đôi mắt sắc lạnh. Luôn ẩn mình trong góc tối, di chuyển như bóng đổ trên tường. Tính cách thận trọng, nghi ngờ tất cả mọi người, luôn có kế hoạch dự phòng cho mọi tình huống.",
# III
"Tu luyện Ám Ảnh Thuật — tạo ra nhiều phân thân bóng tối để giám sát nhiều khu vực cùng lúc. Sử dụng ám khí tẩm thuốc mê, chuyên khống chế mục tiêu mà không gây ồn ào. Phối hợp xuất sắc với Hồ Vô Thanh trong việc duy trì trật tự — một người lo tình báo, một người lo hành động.",
# IV
"""- **[[Mạc Vô Diện]]** — Quỷ Chủ, thượng cấp tối cao.
- **[[Hồ Vô Thanh]]** — Tổng Quản chính, đồng sự phối hợp ăn ý trong quản lý Quỷ Thị.
- **[[Chu Thiết Diện]]** — Trưởng Lão Chấp Pháp, người mà Ám Nhị hỗ trợ trong các vụ điều tra.""",
# V
"Ám Nhị là \"sản phẩm\" của Quỷ Thị — một đứa trẻ bị bỏ rơi trong chợ đen, được Mạc Vô Diện nhặt về nuôi dưỡng. Lớn lên không biết gì ngoài Quỷ Thị, coi đây là nhà và Quỷ Chủ là ân nhân duy nhất. Được đào tạo bài bản từ nhỏ để trở thành Tổng Quản phụ, chuyên xử lý các công việc mà Hồ Vô Thanh không tiện ra mặt."
),

"Quỷ_Thị_Nam_Cương/Lệ_Tam.md": (
# II
"Đàn ông trung niên mập mạp, gương mặt tròn phúc hậu luôn nở nụ cười, đeo mặt nạ nửa mặt vàng óng trang trí hoa mỹ. Ăn mặc sặc sỡ, tay đeo đầy nhẫn ngọc, thích phô trương và thu hút sự chú ý. Tính cách hoạt bát, mồm mép lanh lợi, có thể biến thứ tầm thường thành báu vật bằng lời nói.",
# III
"Không có tu vi chiến đấu nổi bật, nhưng sở hữu Hoạt Thiệt Thuật — giọng nói mang theo linh lực mê hoặc, khiến người nghe bị kích động và sẵn sàng trả giá cao hơn. Giỏi thẩm định linh thạch, dược liệu, pháp khí — hiếm có vật phẩm nào qua mắt được hắn. Trong tình huống nguy hiểm, có thể dùng \"Sư Tử Hống\" gây choáng kẻ địch trong chốc lát.",
# IV
"""- **[[Mạc Vô Diện]]** — Quỷ Chủ, người giao quyền tổ chức mọi phiên đấu giá lớn.
- **[[Chu Thiết Diện]]** — Trưởng Lão Chấp Pháp, người bảo vệ an toàn cho Lệ Tam trong các phiên đấu giá.
- **[[Hồ Vô Thanh]]** — Tổng Quản, người cung cấp thông tin về nguồn gốc vật phẩm cho Lệ Tam thẩm định.""",
# V
"Lệ Tam vốn là thương nhân lưu động, nổi tiếng khắp Nam Cương với khả năng bán bất cứ thứ gì cho bất kỳ ai. Được Mạc Vô Diện mời về Quỷ Thị làm Đấu Giá Sư sau khi chứng kiến hắn bán một cục đá vô dụng với giá mười viên linh thạch. Từ đó trở thành linh hồn của mọi phiên đấu giá, nơi mà tiền bạc xoay chuyển nhiều nhất trong toàn bộ Nam Cương."
),

# ============================================================
# HẮC BÁO TRẠI (黑豹寨)
# ============================================================

"Hắc_Báo_Trại/Đỗ_Môn.md": (
# II
"Đàn ông trung niên, da ngăm đen vì sống trong rừng rậm, thân hình rắn rỏi như cây cổ thụ. Mặt vuông chữ điền, râu quai nón, đôi mắt sắc như báo đêm, trên mặt có vết sẹo dài từ trán xuống má trái. Tính cách hào sảng, trọng tình nghĩa với anh em trong trại, nhưng tàn nhẫn không thương tiếc với kẻ thù và khách qua đường.",
# III
"Tuy tu vi không cao nhưng kinh nghiệm chiến đấu trong rừng cực kỳ phong phú, am hiểu mọi loại bẫy và địa hình. Sử dụng song đao ngắn, chuyên đánh cận chiến trong không gian hẹp giữa cây cối. Sở trường chiến thuật du kích — phục kích, đánh nhanh rút gọn, dùng số đông bao vây đối thủ mạnh hơn.",
# IV
"""- **[[Đỗ Hải]]** — Em trai ruột, Phó Trại Chủ, người chia sẻ gánh nặng cai quản Hắc Báo Trại.
- **[[Đỗ Hùng]]** — Con trai trưởng, Báo Ảnh Đội Trưởng, niềm tự hào và hy vọng của gia tộc Đỗ.
- **[[Lý Sơn Đao]]** — Hắc Đao Trưởng Lão, chiến hữu lâu năm, người mà Đỗ Môn tin tưởng nhất ngoài huyết thống.""",
# V
"Đỗ Môn là con trưởng gia tộc Đỗ, một gia tộc thợ săn sống trong rừng sâu Nam Cương từ nhiều đời. Khi gia tộc bị một thế lực tu tiên cướp đất, Đỗ Môn dẫn người nhà vào rừng rậm lập Hắc Báo Trại, trở thành thổ phỉ. Dưới sự lãnh đạo của hắn, Hắc Báo Trại từ nhóm người vô gia cư trở thành thế lực khiến các thương đoàn qua đường phải cống nạp. Tuy là thổ phỉ nhưng có quy tắc riêng: không giết phụ nữ và trẻ em."
),

"Hắc_Báo_Trại/Đỗ_Hải.md": (
# II
"Thấp hơn anh trai một cái đầu nhưng bề ngang vạm vỡ hơn, cơ bắp cuồn cuộn, da đen bóng. Gương mặt hung tợn, mũi gãy do đánh nhau nhiều, nhưng nụ cười lại hiền lành bất ngờ. Tính cách thô lỗ, hay nói bậy nhưng rất chiều anh em trong trại, luôn là người đầu tiên chia cơm nhường áo.",
# III
"Sử dụng đại chùy (búa lớn) nặng hơn trăm cân, dựa vào sức mạnh thể chất thuần túy hơn là linh lực. Chuyên đánh phá vỡ phòng tuyến, là lực lượng xung kích chính khi phục kích thất bại phải đối đầu trực diện. Có biệt danh \"Hắc Gấu\" vì chiến đấu hung hãn như gấu hoang.",
# IV
"""- **[[Đỗ Môn]]** — Anh trai ruột kiêm Trại Chủ, người mà Đỗ Hải sẵn sàng chết thay.
- **[[Đỗ Hùng]]** — Cháu trai, con của anh, Đỗ Hải rất cưng chiều.
- **[[Vương Thiết Nha]]** — Hắc Đao Trưởng Lão, chiến hữu thường xuyên uống rượu cùng.""",
# V
"Đỗ Hải theo anh trai vào rừng lập trại từ khi còn niên thiếu, là người đầu tiên ủng hộ quyết định trở thành thổ phỉ. Tuy không giỏi mưu kế nhưng sức mạnh và lòng trung thành khiến hắn trở thành Phó Trại Chủ xứng đáng. Trong trại, hắn phụ trách huấn luyện tân binh và quản lý hậu cần, đảm bảo anh em luôn có đủ lương thực."
),

"Hắc_Báo_Trại/Đỗ_Hùng.md": (
# II
"Thanh niên hai mươi tuổi, thân hình nhanh nhẹn, cơ thể linh hoạt như báo đen. Da ngăm, mắt sáng tinh anh, luôn leo trèo trên cành cây cao quan sát. Tính cách lanh lợi, mưu trí, thích nghĩ ra các chiến thuật phục kích mới, là thế hệ trẻ tài năng nhất của Hắc Báo Trại.",
# III
"Chuyên sử dụng cung tên và phi đao, bắn tỉa chính xác từ trên cao. Sở trường ngụy trang trong rừng — có thể nằm im hàng giờ mà thú rừng đi qua cũng không phát hiện. Dẫn đầu Báo Ảnh Đội, chuyên trinh sát và phục kích, là đôi mắt của Hắc Báo Trại.",
# IV
"""- **[[Đỗ Môn]]** — Cha ruột kiêm Trại Chủ, người mà Đỗ Hùng muốn chứng minh bản thân xứng đáng kế thừa.
- **[[Đỗ Hải]]** — Chú ruột, người cưng chiều và bảo vệ Đỗ Hùng từ nhỏ.
- **[[Đỗ Tiểu Hổ]]** — Em họ, đệ tử nhỏ tuổi nhất mà Đỗ Hùng luôn dẫn theo dạy dỗ.""",
# V
"Đỗ Hùng sinh ra trong Hắc Báo Trại, lớn lên giữa rừng già, coi cây cối là nhà. Được cha Đỗ Môn huấn luyện thuật sinh tồn từ khi năm tuổi, mười tuổi đã một mình hạ được bạo hùng (loại khỉ dữ). Hiện dẫn Báo Ảnh Đội — đội trinh sát tinh nhuệ nhất trại, chuyên nắm bắt di chuyển của thương đoàn và tuần tra lãnh thổ."
),

"Hắc_Báo_Trại/Lý_Sơn_Đao.md": (
# II
"Lão nhân ngoài năm mươi, tóc hoa râm, thân hình khô gầy nhưng gân guốc, mỗi cử động đều toát ra sự nguy hiểm. Tay phải có sẹo cũ chằng chịt do luyện đao từ nhỏ, mắt phải bị mù do chiến đấu. Tính cách trầm mặc, ít nói, chỉ mở miệng khi cần, nhưng khi rút đao thì không còn do dự.",
# III
"Sử dụng hắc thiết đao — loại đao nặng rèn từ quặng sắt đen vùng núi Nam Cương, bền hơn đao thường. Đao pháp mộc mạc nhưng sát thương cao, thiên về một kích chí mạng hơn là biến hóa hoa mỹ. Đã từng đánh bại tu sĩ Trúc Cơ Viên Mãn chỉ bằng kinh nghiệm chiến đấu thuần túy.",
# IV
"""- **[[Đỗ Môn]]** — Trại Chủ, chiến hữu tri kỷ từ thời trẻ, người mà Lý Sơn Đao nguyện phò tá cả đời.
- **[[Lý Sơn Nhi]]** — Con gái ruột, đang theo cha học đao pháp trong trại.
- **[[Vương Thiết Nha]]** — Đồng liêu Hắc Đao Trưởng Lão, chiến hữu đánh trận cùng nhau nhiều năm.""",
# V
"Lý Sơn Đao vốn là thợ săn cô độc sống trên núi, nổi tiếng trong vùng vì một mình giết được hổ dữ. Khi gia tộc Đỗ bị đuổi khỏi đất, Lý Sơn Đao tự nguyện đi theo Đỗ Môn vào rừng vì tình nghĩa láng giềng. Mang theo con gái Lý Sơn Nhi, trở thành một trong hai Hắc Đao Trưởng Lão — cột trụ chiến lực của Hắc Báo Trại."
),

"Hắc_Báo_Trại/Vương_Thiết_Nha.md": (
# II
"Đàn ông trung niên, thân hình thấp đậm, mặt đầy sẹo, thiếu hai chiếc răng cửa nên cười lên trông rất dữ tợn. Cơ bắp vai và cánh tay phát triển bất thường do luyện đao nặng nhiều năm. Tính cách nóng nảy, thẳng tính, hay gây gổ nhưng trung thành tuyệt đối với Hắc Báo Trại.",
# III
"Sử dụng quỷ đầu đao — loại đao cong nặng có lưỡi răng cưa, gây vết thương khó lành. Chiến đấu theo kiểu hung hãn, dùng sức mạnh áp đảo, ít kỹ xảo. Phối hợp tốt với Lý Sơn Đao trong trận chiến — một người đánh mở đường, một người kết liễu.",
# IV
"""- **[[Đỗ Môn]]** — Trại Chủ, ân nhân cứu mạng, người mà Vương Thiết Nha thề trung thành.
- **[[Lý Sơn Đao]]** — Đồng liêu Hắc Đao Trưởng Lão, chiến hữu đánh trận bên nhau.
- **[[Đỗ Hải]]** — Phó Trại Chủ, bạn nhậu thân thiết.""",
# V
"Vương Thiết Nha là tội phạm bị truy nã ở một thành trấn biên giới, chạy trốn vào rừng rậm và suýt chết đói. Được Đỗ Môn cứu sống và thu nạp vào Hắc Báo Trại, từ đó thề trung thành suốt đời. Tuy xuất thân thấp kém nhưng nhờ sức mạnh và sự liều mạng mà được phong Hắc Đao Trưởng Lão."
),

"Hắc_Báo_Trại/Đỗ_Tiểu_Hổ.md": (
# II
"Cậu bé mười bốn tuổi, thân hình nhỏ nhắn nhưng nhanh nhẹn, da ngăm đen, mắt to tròn sáng rực đầy tò mò. Tóc ngắn bù xù, quần áo luôn lấm bẩn vì leo trèo và chạy nhảy trong rừng suốt ngày. Tính cách hiếu động, gan dạ, không biết sợ, luôn muốn chứng minh mình không thua kém người lớn.",
# III
"Chưa có tu vi đáng kể nhưng được huấn luyện sinh tồn trong rừng từ nhỏ, biết đặt bẫy, theo dấu thú, nhận biết thảo dược. Đang học dùng dao ngắn và ná bắn đá, độ chính xác khá tốt cho tuổi. Tiềm năng tu luyện chưa được đánh giá nhưng thể chất và ý chí vượt xa bạn bè cùng trang lứa.",
# IV
"""- **[[Đỗ Hùng]]** — Anh họ, người dẫn dắt và dạy dỗ Tiểu Hổ nhiều nhất.
- **[[Đỗ Môn]]** — Bác ruột kiêm Trại Chủ, người mà Tiểu Hổ ngưỡng mộ nhất.
- **[[Lý Sơn Nhi]]** — Bạn cùng trang lứa, hay cùng nhau phiêu lưu trong rừng.""",
# V
"Đỗ Tiểu Hổ sinh ra trong Hắc Báo Trại, là con của một người em họ Đỗ Môn đã mất sớm. Được cả trại nuôi dưỡng, coi mọi người trong trại là gia đình. Dù còn nhỏ nhưng đã tham gia trinh sát cùng Báo Ảnh Đội của Đỗ Hùng, thường được giao nhiệm vụ chui vào những khe hẹp mà người lớn không vào được."
),

"Hắc_Báo_Trại/Lý_Sơn_Nhi.md": (
# II
"Thiếu nữ mười lăm tuổi, gương mặt khỏe khoắn, da rám nắng, mắt sáng, tóc đen cột đuôi ngựa. Thân hình mảnh nhưng dẻo dai, tay có vết chai do luyện đao. Tính cách mạnh mẽ, bướng bỉnh, không chịu thua kém con trai, luôn muốn chứng minh con gái cũng có thể chiến đấu.",
# III
"Được cha Lý Sơn Đao dạy đao pháp cơ bản, tuy chưa thuần thục nhưng nền tảng vững. Giỏi dùng ná và phi tiêu tẩm thuốc mê chiết xuất từ thảo dược rừng. Am hiểu thảo dược địa phương, có thể chế thuốc chữa thương đơn giản cho anh em trong trại.",
# IV
"""- **[[Lý Sơn Đao]]** — Cha ruột kiêm sư phụ, người nghiêm khắc nhưng yêu thương.
- **[[Đỗ Tiểu Hổ]]** — Bạn cùng trang lứa, hay cùng nhau phiêu lưu và gây rối.
- **[[Đỗ Hùng]]** — Đại ca mà Sơn Nhi kính trọng, người dẫn dắt thế hệ trẻ.""",
# V
"Lý Sơn Nhi theo cha vào Hắc Báo Trại từ khi còn bé, lớn lên giữa rừng già và đám thổ phỉ. Mẹ mất sớm, được cha và các chú bác trong trại nuôi dưỡng. Tuy là con gái duy nhất trong trại nhưng không hề yếu đuối, tự nguyện xin gia nhập Báo Ảnh Đội để trinh sát cùng Đỗ Hùng."
),

# ============================================================
# ĐỘC LONG BẢO (獨龍堡)
# ============================================================

"Độc_Long_Bảo/Độc_Nhãn.md": (
# II
"Đàn ông trung niên, thân hình cao lớn, mất mắt trái — hốc mắt bị sẹo cháy che kín, mắt phải sắc lạnh như mắt rồng. Da thô ráp đầy sẹo, mặc giáp da thú rừng, vai trái luôn đậu một con ưng đen trinh sát. Tính cách quả quyết, ít tin người, cai trị bằng sức mạnh và sự sợ hãi, nhưng công bằng với thuộc hạ trung thành.",
# III
"Tu luyện Long Nhãn Thuật — con mắt còn lại có thể nhìn xuyên sương mù và bóng tối, phát hiện kẻ địch trong bán kính năm dặm. Sử dụng trường thương kết hợp với thuần thú chiến đấu, chỉ huy đàn dã thú tấn công phối hợp. Chiêu tuyệt mệnh \"Độc Long Phá Trận\" — tập trung toàn bộ linh lực vào một mũi thương duy nhất, xuyên thủng mọi phòng ngự.",
# IV
"""- **[[Lưu Ám Ảnh]]** — Long Ảnh Đội Trưởng, cánh tay phải chỉ huy đội trinh sát tinh nhuệ.
- **[[Trần Phục Long]]** — Phục Thú Viện Chủ, người quản lý toàn bộ thú chiến của Độc Long Bảo.
- **[[Hoàng Thạch]]** — Trưởng Lão đáng tin cậy nhất, phụ trách phòng thủ nội bảo.""",
# V
"Độc Nhãn vốn là thợ săn nổi tiếng vùng núi Nam Cương, mất mắt trái trong trận chiến với một con mãng xà yêu thú cấp Kim Đan. Sau khi giết được mãng xà, hắn dùng nội đan của nó đột phá tu vi và chiếm lĩnh ải núi lập nên Độc Long Bảo. Nhờ vị trí hiểm yếu kiểm soát con đèo duy nhất, Độc Long Bảo thu phí qua đường và trở thành thế lực không ai dám xem thường."
),

"Độc_Long_Bảo/Lưu_Ám_Ảnh.md": (
# II
"Thanh niên ngoài ba mươi, thân hình mảnh khảnh nhưng cơ bắp dẻo dai, di chuyển nhanh và nhẹ như mèo rừng. Gương mặt lạnh lùng, ít biểu cảm, mắt hẹp luôn quan sát. Thường mặc y phục màu xám đen hòa lẫn vào đá núi, hiếm khi nói nhiều hơn một câu.",
# III
"Tinh thông thuật ẩn thân và trinh sát trong địa hình núi đá — có thể nằm im trên vách đá hàng ngày mà không bị phát hiện. Sử dụng song đoản kiếm, chuyên tấn công bất ngờ từ điểm mù. Dẫn đầu Long Ảnh Đội — đội trinh sát tinh nhuệ nhất Độc Long Bảo, mắt và tai của toàn bảo.",
# IV
"""- **[[Độc Nhãn]]** — Bảo Chủ, người mà Lưu Ám Ảnh tuyệt đối trung thành.
- **[[Lưu Tiểu Long]]** — Con trai, đang được huấn luyện để kế thừa Long Ảnh Đội.
- **[[Trần Phục Long]]** — Phục Thú Viện Chủ, đồng liêu thường phối hợp — Lưu Ám Ảnh trinh sát, Trần Phục Long dùng thú tấn công.""",
# V
"Lưu Ám Ảnh là cựu trinh sát của một đội thương đoàn bị cướp sạch khi qua ải núi Độc Long. Thay vì bị giết, hắn được Độc Nhãn tha mạng và thu nạp vì ấn tượng với khả năng ẩn thân. Từ đó gây dựng Long Ảnh Đội, biến nó thành lực lượng trinh sát chuyên nghiệp. Có một con trai tên Lưu Tiểu Long đang theo cha học nghề."
),

"Độc_Long_Bảo/Trần_Phục_Long.md": (
# II
"Đàn ông trung niên, thân hình thấp đậm, da nâu sạm, tay chân đầy vết cào cấu và vết thương cũ do tiếp xúc với dã thú. Mùi cơ thể luôn nồng nặc mùi thú rừng, quần áo dính lông thú. Tính cách ôn hòa, kiên nhẫn phi thường, đối xử với thú chiến như con cái ruột thịt, nhưng khi chiến đấu thì lạnh lùng quyết đoán.",
# III
"Chuyên tu Phục Thú Thuật — dùng linh lực hòa vào bản năng thú, thu phục và chỉ huy dã thú chiến đấu. Hiện quản lý hơn hai mươi thú chiến bao gồm sơn ưng, mãng xà, hắc báo và kỳ lân thú. Bản thân chiến lực cá nhân tầm thường nhưng cùng đàn thú thì có thể đối đầu cường giả cao hơn một cảnh giới.",
# IV
"""- **[[Độc Nhãn]]** — Bảo Chủ, người cung cấp tài nguyên nuôi thú và giao nhiệm vụ.
- **[[Lưu Ám Ảnh]]** — Long Ảnh Đội Trưởng, đồng liêu phối hợp trinh sát và tấn công.
- **[[Hoàng Nhi]]** — Nội Môn đệ tử, học trò có thiên phú thuần thú khiến Trần Phục Long chú ý.""",
# V
"Trần Phục Long sinh ra trong gia đình thợ săn nhưng từ nhỏ đã không nỡ giết thú, thay vào đó tìm cách giao tiếp và thuần phục chúng. Bị gia đình xua đuổi vì \"bất hiếu\", lang thang trong rừng sống cùng dã thú nhiều năm. Được Độc Nhãn phát hiện khi đang cưỡi hắc báo đi qua ải núi, lập tức mời về lập Phục Thú Viện. Từ đó trở thành cột trụ không thể thiếu của Độc Long Bảo."
),

"Độc_Long_Bảo/Hoàng_Thạch.md": (
# II
"Lão nhân ngoài sáu mươi, thân hình chắc nịch như tảng đá, da mặt nhăn nheo nhưng cơ bắp vẫn rắn chắc. Tóc bạc cắt ngắn, râu ngắn gọn gàng, ánh mắt ổn định tựa núi không lay. Tính cách điềm đạm, trung hậu, là trụ cột tinh thần của Độc Long Bảo, mọi người đều kính trọng.",
# III
"Tu luyện Thạch Bì Công — biến da thịt cứng như đá, chịu được đòn đánh thường mà không tổn thương. Sử dụng côn sắt dài, đánh chậm nhưng mỗi đòn nặng như núi đổ. Chuyên phòng thủ cổng chính và nội bảo, là tuyến phòng ngự cuối cùng của Độc Long Bảo.",
# IV
"""- **[[Độc Nhãn]]** — Bảo Chủ, người mà Hoàng Thạch phò tá từ ngày đầu lập bảo.
- **[[Hoàng Nhi]]** — Con gái ruột, niềm vui tuổi già, đang tu luyện trong bảo.
- **[[Triệu Long Hổ]]** — Đồng liêu Trưởng Lão, chiến hữu cùng thế hệ.""",
# V
"Hoàng Thạch là bạn đồng hành của Độc Nhãn từ thời còn trẻ, cùng nhau săn thú và chiến đấu khắp vùng núi. Khi Độc Nhãn lập Độc Long Bảo, Hoàng Thạch là người đầu tiên gia nhập. Cống hiến cả đời cho sự phồn vinh của bảo, hiện đã bắt đầu lão hóa nhưng vẫn kiên trì trấn giữ."
),

"Độc_Long_Bảo/Triệu_Long_Hổ.md": (
# II
"Đàn ông trung niên, thân hình cao ráo, gương mặt cương nghị, có hàng lông mày rậm như kiếm. Da ngăm đen, lưng thẳng tắp, luôn mặc giáp da gọn gàng sẵn sàng chiến đấu. Tính cách nóng nảy nhưng trung thực, nói gì làm nấy, ghét nhất kẻ phản bội.",
# III
"Sử dụng đại đao kết hợp với thuật cưỡi dã thú — chiến đấu trên lưng hắc báo chiến, tấn công di động cực nhanh. Chuyên dẫn đội tập kích trên đèo núi, lợi dụng địa hình hiểm trở để phục kích thương đoàn và kẻ xâm nhập. Sức mạnh thể chất và phản xạ chiến đấu xuất sắc dù tu vi không cao.",
# IV
"""- **[[Độc Nhãn]]** — Bảo Chủ, thượng cấp mà Triệu Long Hổ trung thành tuyệt đối.
- **[[Hoàng Thạch]]** — Đồng liêu Trưởng Lão, bạn chiến đấu lâu năm.
- **[[Mạc Vân]]** — Đồng liêu Trưởng Lão, người mà Triệu Long Hổ thường bất đồng ý kiến vì khác biệt tính cách.""",
# V
"Triệu Long Hổ là cựu binh của một tiểu quốc đã sụp đổ ở biên giới Nam Cương, sau khi mất nước thì lang thang thành lính đánh thuê. Được Độc Nhãn thu phục bằng một trận đấu tay đôi — thua nhưng tâm phục. Từ đó gia nhập Độc Long Bảo, trở thành Trưởng Lão phụ trách tập kích và tuần tra ngoại vi."
),

"Độc_Long_Bảo/Mạc_Vân.md": (
# II
"Phụ nữ trung niên, dáng người thanh mảnh, gương mặt điềm tĩnh, tóc đen dài buông sau lưng. Mặc y phục giản dị màu xanh sẫm, tay luôn cầm ống trúc đựng bản đồ. Tính cách trầm tĩnh, tỉ mỉ, giỏi phân tích tình hình, là quân sư không chính thức của Độc Long Bảo.",
# III
"Tu luyện Vân Vụ Thuật — tạo ra sương mù che phủ cả ải núi, khiến kẻ xâm nhập mất phương hướng. Giỏi trận pháp phòng thủ, đã bày bố hệ thống cảnh báo và bẫy phòng thủ khắp Độc Long Bảo. Chiến lực cá nhân tầm thường nhưng giá trị chiến lược vô cùng lớn.",
# IV
"""- **[[Độc Nhãn]]** — Bảo Chủ, người trọng dụng Mạc Vân làm cố vấn chiến thuật.
- **[[Triệu Long Hổ]]** — Đồng liêu Trưởng Lão, hay bất đồng vì Triệu Long Hổ thiên về tấn công còn Mạc Vân thiên về phòng thủ.
- **[[Hoàng Thạch]]** — Đồng liêu Trưởng Lão, người luôn ủng hộ ý kiến của Mạc Vân.""",
# V
"Mạc Vân từng là đệ tử ngoại môn của một tiểu phái đã bị diệt, một mình sống sót nhờ trận pháp phòng thủ tự học. Lang thang đến ải núi Độc Long, được Độc Nhãn thu nạp khi nhận ra tài năng bày trận. Từ đó thiết kế toàn bộ hệ thống phòng thủ của Độc Long Bảo, biến nơi đây thành pháo đài gần như bất khả xâm phạm."
),

"Độc_Long_Bảo/Lưu_Tiểu_Long.md": (
# II
"Thiếu niên mười bảy tuổi, thân hình mảnh, di chuyển nhẹ nhàng giống cha. Gương mặt trẻ trung, mắt sáng, luôn tò mò quan sát mọi thứ xung quanh. Tính cách trầm tĩnh hơn tuổi, ít nói, nhưng khi cần thì quyết đoán — bản sao thu nhỏ của Lưu Ám Ảnh.",
# III
"Đang học thuật ẩn thân và trinh sát từ cha, đã có thể nằm im trên vách đá vài canh giờ. Sử dụng đoản kiếm nhẹ và ám khí, chuyên tấn công nhanh rồi rút lui. Có thiên phú đặc biệt trong việc bắt chước tiếng kêu của thú rừng để liên lạc tín hiệu.",
# IV
"""- **[[Lưu Ám Ảnh]]** — Cha ruột kiêm sư phụ, người mà Tiểu Long muốn noi theo.
- **[[Hoàng Nhi]]** — Bạn đồng trang lứa, thường cùng nhau luyện tập và tuần tra.""",
# V
"Lưu Tiểu Long sinh ra và lớn lên trong Độc Long Bảo, được cha Lưu Ám Ảnh huấn luyện từ nhỏ. Thừa hưởng thiên phú ẩn thân của cha, mười tuổi đã có thể lẩn trốn khỏi sự truy tìm của người lớn. Hiện là thành viên trẻ nhất của Long Ảnh Đội, chuyên thực hiện các nhiệm vụ trinh sát đòi hỏi len lỏi vào nơi chật hẹp."
),

"Độc_Long_Bảo/Hoàng_Nhi.md": (
# II
"Thiếu nữ mười lăm tuổi, gương mặt tròn trịa, da trắng hơn so với người trong bảo, mắt to hiền lành. Tóc đen buộc hai bên, thường mặc y phục nâu giản dị, tay luôn có vết cào từ thú nhỏ. Tính cách hiền hậu, yêu thương động vật, có năng khiếu kỳ lạ khiến dã thú tự nguyện đến gần.",
# III
"Có thiên phú Thân Thú đặc biệt — dã thú tự nhiên thân thiện và vâng lời mà không cần dùng thuật. Đang được Trần Phục Long hướng dẫn cơ bản về Phục Thú Thuật, tiến bộ rất nhanh. Tu vi chiến đấu chưa có nhưng có thể gọi thú nhỏ đến giúp cảnh báo nguy hiểm.",
# IV
"""- **[[Hoàng Thạch]]** — Cha ruột, người bảo vệ và lo lắng cho Hoàng Nhi nhất.
- **[[Trần Phục Long]]** — Sư phụ dạy Phục Thú Thuật, người phát hiện thiên phú của nàng.
- **[[Lưu Tiểu Long]]** — Bạn đồng trang lứa, thường cùng nhau đi tuần.""",
# V
"Hoàng Nhi sinh ra trong Độc Long Bảo, từ nhỏ đã có khả năng kỳ lạ khiến thú rừng không sợ hãi mà thân thiện. Cha Hoàng Thạch ban đầu lo lắng nhưng khi Trần Phục Long phát hiện thiên phú Thân Thú, lão mới yên tâm cho con gái theo học. Hiện Hoàng Nhi là người duy nhất có thể chạm vào con hắc báo chiến hung dữ nhất bảo mà không bị tấn công."
),

# ============================================================
# BÁN YÊU THÔN (半妖村)
# ============================================================

"Bán_Yêu_Thôn/Lý_Bán_Huyền.md": (
# II
"Lão nhân ngoài sáu mươi nhưng vẫn tráng kiện, mái tóc bạc trắng nhưng có những sợi xanh biếc xen lẫn — dấu hiệu của huyết mạch yêu tộc. Đôi mắt một đen một vàng kim, da có vảy nhỏ mờ nhạt ở hai bên thái dương. Tính cách trầm ổn, nhân hậu, luôn đặt sự an toàn của thôn dân lên trên hết, là trụ cột tinh thần của Bán Yêu Thôn.",
# III
"Tu luyện Hỗn Nguyên Thuật — dung hợp linh lực nhân tộc và yêu khí, tạo ra nguồn năng lượng đặc biệt mà cả hai phe đều khó khắc chế. Có thể biến hóa một phần cơ thể thành hình thái yêu — mọc vuốt, vảy cứng — để tăng sức chiến đấu. Sở trường chiến đấu phòng thủ, dùng kết giới bảo vệ toàn thôn.",
# IV
"""- **[[Lý Bán Sơn]]** — Em trai ruột, cùng nhau gánh vác trọng trách bảo vệ thôn.
- **[[Thượng Quan Yêu Nhi]]** — Đội Trưởng Tuần Tra, hậu bối đáng tin cậy nhất.""",
# V
"Lý Bán Huyền là con lai giữa một tu sĩ nhân tộc và một nữ yêu xà, bị cả hai bên ruồng bỏ từ nhỏ. Cùng em trai Lý Bán Sơn lưu lạc, cuối cùng tìm đến Bán Yêu Thôn — nơi quy tụ những kẻ lai như họ. Nhờ tu vi cao nhất trong thôn và tính cách nhân hậu, được bầu làm Trưởng Lão. Suốt đời cống hiến cho việc bảo vệ thôn dân khỏi sự kỳ thị của cả nhân tộc lẫn yêu tộc."
),

"Bán_Yêu_Thôn/Lý_Bán_Sơn.md": (
# II
"Đàn ông trung niên, thân hình cao lớn vạm vỡ, da có vảy mờ nhạt như anh trai nhưng rõ hơn, đặc biệt ở cánh tay và cổ. Mắt vàng kim cả hai bên, răng nanh hơi nhọn, trông có vẻ hung dữ nhưng thực tế rất hiền. Tính cách thẳng thắn, nóng tính, hay hành động trước suy nghĩ sau, nhưng hết lòng bảo vệ thôn dân.",
# III
"Thiên về hình thái yêu nhiều hơn anh — có thể biến hóa nửa thân thành hình dạng xà nhân, tăng gấp đôi sức mạnh và tốc độ. Sử dụng trảo công (kỹ thuật vuốt), đánh cận chiến hung mãnh. Nhược điểm là biến hóa quá lâu sẽ mất kiểm soát lý trí, cần anh trai kiềm chế.",
# IV
"""- **[[Lý Bán Huyền]]** — Anh trai ruột, người mà Bán Sơn kính trọng và vâng lời nhất.
- **[[Thượng Quan Yêu Nhi]]** — Hậu bối, người mà Bán Sơn coi như cháu gái.""",
# V
"Lý Bán Sơn cùng anh trai lưu lạc từ nhỏ, chịu nhiều kỳ thị do ngoại hình yêu tộc rõ ràng hơn anh. Từng bị một nhóm tu sĩ chính đạo truy sát vì tưởng là yêu thú, may mắn được anh cứu. Trải nghiệm đó khiến Bán Sơn cực kỳ cảnh giác với người ngoài, luôn sẵn sàng chiến đấu bảo vệ thôn. Là tuyến phòng thủ mạnh nhất khi thôn bị tấn công."
),

"Bán_Yêu_Thôn/Thượng_Quan_Yêu_Nhi.md": (
# II
"Thiếu nữ ngoài hai mươi, dung mạo xinh đẹp nhưng có đôi tai nhọn dài đặc trưng của bán yêu hồ ly. Tóc đen dài có ánh đỏ, đuôi cáo mảnh thỉnh thoảng hiện ra khi xúc động. Tính cách hoạt bát, lanh lợi, thông minh, luôn vui vẻ động viên mọi người trong thôn dù trong lòng cũng mang nỗi buồn bị kỳ thị.",
# III
"Thừa hưởng huyết mạch hồ ly, có khả năng ảo thuật cơ bản — tạo ảo ảnh đánh lừa thị giác kẻ thù. Sử dụng đoản kiếm kết hợp thuật ảo, chiến đấu linh hoạt, khó đoán. Dẫn đầu Đội Tuần Tra của Bán Yêu Thôn, bảo vệ vòng ngoài khỏi thú dữ và kẻ xâm nhập.",
# IV
"""- **[[Lý Bán Huyền]]** — Trưởng Lão, người mà Yêu Nhi kính trọng như ông nội.
- **[[Lý Bán Sơn]]** — Trưởng Lão phó, người mà Yêu Nhi coi như chú ruột.""",
# V
"Thượng Quan Yêu Nhi là con lai giữa nhân tộc và yêu hồ, bị bỏ rơi trước cổng Bán Yêu Thôn khi còn là trẻ sơ sinh. Được thôn dân chung tay nuôi nấng, coi cả thôn là gia đình. Nhờ tính cách hoạt bát và tài năng chiến đấu, được bầu làm Đội Trưởng Tuần Tra dù còn trẻ. Luôn ước mơ một ngày thế giới không còn phân biệt nhân tộc và yêu tộc."
),

# ============================================================
# ĐỊA MẠCH THÁM HIỂM ĐỘI (地脈探險隊)
# ============================================================

"Địa_Mạch_Thám_Hiểm_Đội/Thạch_Vạn_Lý.md": (
# II
"Đàn ông trung niên, thân hình vạm vỡ, da nâu sạm do sống dưới lòng đất lâu ngày, bàn tay thô ráp đầy chai sạn. Đầu cạo trọc, trán rộng, đôi mắt đã quen với bóng tối nên hay nheo lại khi ra ngoài ánh sáng. Tính cách vững chãi như đá, bình tĩnh trong mọi tình huống, là người mà đội viên tin tưởng tuyệt đối khi ở dưới lòng đất.",
# III
"Tu luyện Địa Hành Thuật — cảm nhận rung động của đất đá, phát hiện hang động ẩn, mạch khoáng, và nguy hiểm dưới lòng đất. Sử dụng cuốc chiến đấu bằng huyền thiết, vừa là công cụ đào vừa là vũ khí. Có thể phát động \"Địa Chấn Chưởng\" — đập tay xuống đất gây chấn động trong phạm vi hẹp, làm kẻ thù mất thăng bằng.",
# IV
"""- **[[Lý Ám Dạ]]** — Phó Đội, cánh tay phải đáng tin cậy nhất, phụ trách an toàn đội.
- **[[Châu Hàn Dạ]]** — Bản Đồ Sư, người vẽ bản đồ dẫn đường dưới lòng đất.
- **[[Trần Thạch Nham]]** — Khai Khoáng Sư, chuyên gia khai thác tài nguyên.""",
# V
"Thạch Vạn Lý xuất thân từ gia tộc thợ mỏ ở Nam Cương, từ nhỏ đã theo cha xuống hầm đào khoáng. Sau khi phát hiện thiên phú cảm nhận đất đá, bắt đầu tu luyện và lập Địa Mạch Thám Hiểm Đội. Đã dẫn đội khám phá hàng chục hệ thống hang động chưa ai biết, phát hiện nhiều mỏ quặng quý hiếm. Ước mơ lớn nhất là lập bản đồ toàn bộ hệ thống địa mạch dưới lòng Nam Cương."
),

"Địa_Mạch_Thám_Hiểm_Đội/Lý_Ám_Dạ.md": (
# II
"Phụ nữ ngoài ba mươi, thân hình gọn gàng, cơ bắp dẻo dai, da trắng nhợt vì ít thấy ánh mặt trời. Mắt lớn có thể nhìn rõ trong bóng tối, tóc đen cột gọn sau gáy. Tính cách cẩn thận, chu đáo, luôn kiểm tra an toàn ba lần trước khi cho đội tiến vào hang mới, được đội viên gọi là \"chị cả\".",
# III
"Tu luyện Dạ Thị Thuật — đôi mắt có thể nhìn xuyên bóng tối hoàn toàn, phát hiện nguy hiểm mà người thường không thấy. Sử dụng roi da dài vừa làm vũ khí vừa làm dây thừng khi leo trèo trong hang. Chuyên phát hiện và vô hiệu hóa bẫy tự nhiên cũng như nhân tạo dưới lòng đất.",
# IV
"""- **[[Thạch Vạn Lý]]** — Đội Trưởng, người mà Ám Dạ kính trọng và phò tá hết mình.
- **[[Lâm Tiểu Đăng]]** — Thám Hiểm Viên trẻ nhất đội, người mà Ám Dạ chăm sóc và bảo vệ.""",
# V
"Lý Ám Dạ từng là nô lệ lao động trong một hầm mỏ bất hợp pháp, bị ép đào khoáng từ nhỏ đến lớn. Được Thạch Vạn Lý giải cứu khi phát hiện hầm mỏ phi pháp trong một chuyến thám hiểm. Từ đó gia nhập Địa Mạch Thám Hiểm Đội, dùng kinh nghiệm nhiều năm dưới lòng đất để bảo vệ đồng đội. Luôn coi trọng sự an toàn của mọi người hơn bất kỳ phát hiện nào."
),

"Địa_Mạch_Thám_Hiểm_Đội/Châu_Hàn_Dạ.md": (
# II
"Thanh niên gầy gò, da xanh xao, đeo kính tròn dày cộp, tay luôn cầm bút và cuộn giấy da. Lưng hơi gù vì hay cúi xuống vẽ bản đồ, ngón tay luôn dính mực. Tính cách hướng nội, ít nói, nhưng khi bàn về địa hình và bản đồ thì trở nên say sưa không ngừng, là \"bộ nhớ sống\" của đội.",
# III
"Tu luyện Địa Mạch Cảm Ứng cơ bản — cảm nhận hướng đi của địa mạch để xác định phương hướng dưới lòng đất. Không giỏi chiến đấu nhưng có trí nhớ phi thường, có thể ghi nhớ và tái tạo bản đồ phức tạp chỉ sau một lần đi qua. Biết sử dụng bút lông đặc biệt làm vũ khí tự vệ — phóng mực linh lực gây mù mắt kẻ thù.",
# IV
"""- **[[Thạch Vạn Lý]]** — Đội Trưởng, ân nhân thu nạp và cho cơ hội phát huy tài năng.
- **[[Trần Thạch Nham]]** — Đồng đội, thường phối hợp — một người tìm đường, một người đào khoáng.""",
# V
"Châu Hàn Dạ vốn là thư sinh nghèo mê nghiên cứu địa lý nhưng không đủ tiền theo học tại bất kỳ thư viện hay học viện nào. Gặp Thạch Vạn Lý trong một quán trà khi đang vẽ bản đồ khu vực, bị đội trưởng ấn tượng với tài năng bản đồ học và mời gia nhập. Từ đó trở thành Bản Đồ Sư không thể thiếu, đã vẽ hơn ba trăm tấm bản đồ hang động chi tiết."
),

"Địa_Mạch_Thám_Hiểm_Đội/Trần_Thạch_Nham.md": (
# II
"Đàn ông trẻ tuổi, thân hình vạm vỡ thấp đậm, bàn tay to như quạt, cơ bắp cánh tay phát triển vượt mức bình thường do đào đá nhiều năm. Da nâu đất, mặt vuông, nụ cười chất phác hiền lành. Tính cách thật thà, chịu khó, ít tham vọng, chỉ thích đào đất và tìm đá quý.",
# III
"Tu luyện Toái Thạch Chưởng — tay trần có thể đập vỡ đá cứng, khai thác khoáng vật mà không cần công cụ. Tinh thông phân biệt các loại quặng và khoáng vật bằng cách ngửi, nếm, và cảm nhận rung động. Trong chiến đấu, Toái Thạch Chưởng biến bàn tay thành vũ khí tàn phá, mỗi quyền đánh vỡ giáp phòng hộ.",
# IV
"""- **[[Thạch Vạn Lý]]** — Đội Trưởng, người hướng dẫn phương hướng khai thác.
- **[[Châu Hàn Dạ]]** — Đồng đội, người tìm đường dẫn đến mỏ quặng mới.""",
# V
"Trần Thạch Nham là con trai thợ mỏ, thừa hưởng sức mạnh và kỹ năng đào khoáng từ cha. Gia nhập Địa Mạch Thám Hiểm Đội sau khi mỏ nhà bị sập, cần nơi mới để mưu sinh. Nhờ khả năng phân biệt khoáng vật thiên bẩm mà nhanh chóng trở thành Khai Khoáng Sư chính. Đã phát hiện ba mỏ linh thạch nhỏ cho đội, đóng góp lớn vào nguồn thu."
),

"Địa_Mạch_Thám_Hiểm_Đội/Lâm_Tiểu_Đăng.md": (
# II
"Thiếu niên mười sáu tuổi, thân hình nhỏ nhắn, da trắng, mắt to tròn tràn đầy sự tò mò và hào hứng. Luôn mang theo chiếc đèn dầu nhỏ tự chế, tóc ngắn bù xù, quần áo rộng thùng thình. Tính cách lạc quan, nhiệt tình, không sợ bóng tối, coi mỗi chuyến thám hiểm là một cuộc phiêu lưu mới.",
# III
"Tu vi còn thấp nhưng có thể tạo ra viên linh quang nhỏ từ lòng bàn tay để chiếu sáng — vì vậy được gọi là \"Tiểu Đăng\" (đèn nhỏ). Thân hình nhỏ cho phép chui vào các khe hẹp mà người lớn không vào được. Đang học cơ bản Địa Hành Thuật từ Thạch Vạn Lý, tiến bộ chậm nhưng đều đặn.",
# IV
"""- **[[Thạch Vạn Lý]]** — Đội Trưởng kiêm sư phụ, người mà Tiểu Đăng ngưỡng mộ nhất.
- **[[Lý Ám Dạ]]** — Phó Đội, \"chị cả\" luôn chăm sóc và bảo vệ Tiểu Đăng.""",
# V
"Lâm Tiểu Đăng là trẻ mồ côi sống lang thang ở chợ Nam Cương, tình cờ gặp Thạch Vạn Lý khi đang trốn trong một hang nhỏ ven đường. Được Đội Trưởng nhận nuôi và đưa vào đội, nhanh chóng chứng minh giá trị nhờ thân hình nhỏ và sự gan dạ. Dù nhỏ tuổi nhất đội nhưng đã tham gia hơn mười chuyến thám hiểm, nhiều lần phát hiện lối đi mới nhờ chui vào khe hẹp."
),

# ============================================================
# SMALL FACTIONS
# ============================================================

"Cổ_Kén_Tu_Luyện_Xã/Tằm_Dạ_Quang.md": (
# II
"Hình dáng nửa người nửa trùng — phần trên mang dáng vẻ phụ nữ trung niên thanh mảnh, nhưng da có ánh bạc lấp lánh như tơ tằm. Đôi mắt lớn không có lòng trắng, toàn bộ là màu tím óng ánh. Tóc thực chất là hàng ngàn sợi tơ mảnh phát sáng nhẹ trong bóng tối. Tính cách điềm đạm, kiên nhẫn vô hạn, nói năng chậm rãi như đang kéo tơ.",
# III
"Tu luyện Thiên Tằm Tơ Công — tạo ra tơ linh lực cực kỳ bền, có thể dùng làm vũ khí trói buộc, phòng thủ, hoặc dệt thành pháp y. Có thể phun tơ dính bẫy kẻ thù trong bán kính rộng, tơ cứng hơn thép nhưng nhẹ hơn lông vũ. Ngoài ra tinh thông thuật kén hóa — kết kén bảo vệ bản thân để chữa thương hoặc đột phá tu vi.",
# IV
"""- **[[Phấn Vũ]]** — Đồng minh Bụi Phấn Hội, duy trì quan hệ trao đổi tơ lụa lấy phấn hoa dược liệu.
- **[[Phấn Thanh Lộ]]** — Đồng minh Bụi Phấn Hội, cung cấp sương lộ đặc biệt dùng trong quá trình dệt tơ.""",
# V
"Tằm Dạ Quang thuộc Trùng Tộc — một chủng tộc hiếm gặp ở Nam Cương sống bằng nghề dệt tơ linh lực. Cổ Kén Tu Luyện Xã là một nhóm nhỏ Trùng Tộc chuyên nghiên cứu cách kết hợp tơ tằm với linh lực. Tằm Dạ Quang là cố vấn cao cấp nhất của xã, đã dệt được loại tơ phát sáng trong đêm — vì vậy mang danh \"Dạ Quang\". Sống ẩn dật, chỉ giao dịch với số ít người đáng tin cậy."
),

"Bụi_Phấn_Hội/Phấn_Vũ.md": (
# II
"Thân hình tí hon chỉ cao bằng ngón tay, có đôi cánh mỏng trong suốt phía sau lưng như cánh bướm. Da phủ lớp phấn vàng nhạt phát sáng nhẹ, tóc xanh lá ngắn tủa ra mọi hướng. Tính cách năng động, nhanh nhẹn, nói rất nhanh, hay hào hứng quá mức khi phát hiện loài hoa mới.",
# III
"Là Vi Tộc nên chiến đấu trực diện không phải sở trường, nhưng tinh thông Phấn Hoa Thuật — thu thập và sử dụng phấn hoa các loài thực vật có linh tính. Có thể rải phấn gây mê, phấn gây ngứa, phấn chữa thương tùy theo loại hoa. Sở hữu bộ sưu tập hơn trăm loại phấn hoa khác nhau, mỗi loại có công dụng riêng.",
# IV
"""- **[[Phấn Thanh Lộ]]** — Đồng môn Bụi Phấn Hội, em nuôi, cùng nhau nghiên cứu thực vật.
- **[[Tằm Dạ Quang]]** — Đồng minh Cổ Kén Tu Luyện Xã, đối tác trao đổi lâu dài.""",
# V
"Phấn Vũ thuộc Vi Tộc — chủng tộc nhỏ bé sống cộng sinh với thực vật trong rừng sâu Nam Cương. Bụi Phấn Hội là tổ chức nhỏ của Vi Tộc chuyên nghiên cứu và thu thập phấn hoa có linh tính. Phấn Vũ là Phấn Sư giàu kinh nghiệm nhất hội, đã phân loại và ghi chép hàng trăm loài thực vật linh tính. Dù thân hình nhỏ bé nhưng kiến thức về thảo dược và phấn hoa khiến nhiều tu sĩ lớn phải tìm đến nhờ giúp."
),

"Bụi_Phấn_Hội/Phấn_Thanh_Lộ.md": (
# II
"Vi Tộc nữ, thân hình tí hon, nhỏ hơn Phấn Vũ một chút, cánh mỏng có ánh xanh ngọc. Da phủ lớp phấn xanh nhạt, tóc dài màu trắng buông xuống như giọt sương. Đôi mắt trong veo như nước suối, biểu cảm luôn dịu dàng. Tính cách trầm lặng, nhẹ nhàng, thích ngồi trên lá cây ngắm sương sớm.",
# III
"Chuyên tu Thanh Lộ Thuật — thu thập và tinh chế giọt sương mai có chứa linh khí từ các loài thực vật đặc biệt. Sương lộ của nàng có công dụng chữa thương, giải độc, và bổ trợ tu luyện. Chiến đấu không phải sở trường nhưng có thể dùng sương lộ đông cứng thành kim băng nhỏ bắn vào kẻ thù để tự vệ.",
# IV
"""- **[[Phấn Vũ]]** — Chị nuôi trong Bụi Phấn Hội, người dẫn dắt và bảo vệ.
- **[[Tằm Dạ Quang]]** — Khách hàng thân thiết, thường đặt mua sương lộ để dùng trong dệt tơ.""",
# V
"Phấn Thanh Lộ là Vi Tộc trẻ tuổi, được Phấn Vũ nhặt về nuôi khi còn nhỏ và dạy dỗ trong Bụi Phấn Hội. Có thiên phú đặc biệt trong việc cảm nhận sương lộ có linh khí, nhanh chóng trở thành chuyên gia thu thập sương. Tuy tu vi thấp nhưng sản phẩm sương lộ tinh chế của nàng được nhiều tu sĩ trong vùng tìm mua, tạo nguồn thu chính cho Bụi Phấn Hội."
),

}


def fill_character(filepath, sections):
    """Replace placeholder text in a character file with real content."""
    sec_ii, sec_iii, sec_iv, sec_v = sections

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check that the file has placeholders to replace
    placeholder = '*(Chưa xác định)*'
    if placeholder not in content:
        print(f"  SKIP (no placeholder): {filepath}")
        return False

    # Split content into sections and replace
    # Strategy: find each section header and replace the placeholder after it
    replacements = {
        '## II. NGOẠI HÌNH & TÍNH CÁCH': sec_ii,
        '## III. NĂNG LỰC & CHIẾN ĐẤU': sec_iii,
        '## IV. CÁC MỐI QUAN HỆ': sec_iv,
        '## V. TIỂU SỬ & HÀNH TRÌNH': sec_v,
    }

    for header, new_content in replacements.items():
        # Find the header and replace the placeholder after it
        marker = f"{header}\n{placeholder}"
        replacement = f"{header}\n{new_content}"
        if marker in content:
            content = content.replace(marker, replacement, 1)
        else:
            print(f"  WARNING: Could not find '{header}' + placeholder in {filepath}")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return True


def main():
    updated = 0
    skipped = 0
    errors = 0

    for filename, sections in CHARACTERS.items():
        # Normalize to NFD for macOS filesystem compatibility
        filepath = unicodedata.normalize('NFD', os.path.join(BASE, filename))
        if not os.path.exists(filepath):
            print(f"  ERROR: File not found: {filepath}")
            errors += 1
            continue

        try:
            if fill_character(filepath, sections):
                print(f"  OK: {filename}")
                updated += 1
            else:
                skipped += 1
        except Exception as e:
            print(f"  ERROR: {filename}: {e}")
            errors += 1

    print(f"\nDone: {updated} updated, {skipped} skipped, {errors} errors")


if __name__ == '__main__':
    main()
