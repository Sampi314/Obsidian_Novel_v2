#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fill character details for 3 Thiên Trụ factions: Đại Càn Hoàng Triều, Cửu U Ma Tông, Thiên Kiêu Học Viện."""

import os
import re
import unicodedata

BASE = "/Users/sampi_wu/Documents/GitHub/Obsidian_Novel_v2/Đạo/Nhân_Vật/Thiên_Trụ"

FACTION_DIRS = {
    "Đại Càn Hoàng Triều": "Đại_Càn_Hoàng_Triều",
    "Cửu U Ma Tông": "Cửu_U_Ma_Tông",
    "Thiên Kiêu Học Viện": "Thiên_Kiêu_Học_Viện",
}

# Each entry: filename -> (section_ii, section_iii, section_iv, section_v)

CHARS = {
    # ============================================================
    # FACTION 1: ĐẠI CÀN HOÀNG TRIỀU
    # ============================================================
    "Lý_Thiên_Vũ.md": (
        # II
        "Dáng người cao lớn, uy nghi, khoác long bào vàng thêu chín rồng uốn lượn. Đôi mắt sắc bén như đại bàng, mày kiếm thẳng tắp, tóc búi cao dưới miện Long Thiên. Tính cách trầm ổn, quyết đoán, mang khí phách của bậc đế vương trị vì thiên hạ. Ngoài triều đường lạnh lùng uy nghiêm, nhưng với con cái lại ẩn chứa sự trìu mến khó nhận ra.",
        # III
        "Tu luyện Hoàng Đạo Chân Kinh — bí truyền của hoàng tộc Lý gia, kết hợp Nho giáo tu chân với Long Mạch chi lực. Chưởng khống Long Mạch trung ương, có thể triệu hoán Long Khí hộ thể, một chưởng đủ sức san bằng cả tòa sơn phong. Khi lâm trận, đế uy bao trùm bốn phía, khiến kẻ tu vi thấp hơn không dám ngẩng đầu.",
        # IV
        "- [[Lý Thiên Long]] — Thái Tử, trưởng tử, người kế vị được kỳ vọng nhất.\n- [[Lý Thiên Phượng]] — Nhị Hoàng Tử, con trai thứ, tài năng nhưng dã tâm.\n- [[Lý Nguyệt Nhi]] — Công Chúa, con gái yêu quý, được sủng ái nhất hậu cung.\n- [[Mộ Dung Chiến]] — Thần Sách Đại Tướng, cánh tay quân sự đáng tin cậy nhất.\n- [[Tư Mã Tinh Vân]] — Khâm Thiên Giám Chính, cố vấn thiên cơ bên cạnh ngai vàng.",
        # V
        "Lý Thiên Vũ kế thừa ngôi vị Càn Đế từ phụ hoàng hơn ba trăm năm trước, khi Đại Càn vừa trải qua loạn Thất Vương. Ông dùng thiết huyết thủ đoạn dẹp yên phản loạn, tái lập quyền uy hoàng triều trên toàn Thiên Trụ trung nguyên. Dưới triều đại của ông, Lục Bộ được cải tổ, Thần Sách Quân trở thành đạo quân tinh nhuệ nhất nhân giới. Hiện tại, ông đang bí mật lo ngại về sự trỗi dậy của Cửu U Ma Tông ở biên cương."
    ),
    "Trần_Bách_Tài.md": (
        "Người trung niên mập mạp, da trắng hồng hào, luôn mặc quan phục lụa tím thêu hoa văn kim tiền. Đôi mắt nhỏ nhưng tinh anh, miệng luôn nở nụ cười thương nhân. Tính tình viên hoạt, giỏi giao thiệp, nhưng trong bụng tính toán cực kỳ sắc bén, không bao giờ chịu lỗ.",
        "Tu luyện Kim Toán Quyết, có thể dùng linh lực biến hóa thành kim ti vô hình để thăm dò, trói buộc hoặc phòng thủ. Không chuyên chiến đấu chính diện, nhưng khả năng bố trận phòng ngự bằng trận pháp tài vật cực kỳ tinh xảo. Thường mang theo Vạn Bảo Nang chứa vô số pháp khí phòng thân.",
        "- [[Lý Thiên Vũ]] — Càn Đế, chủ quân mà hắn tận trung phụng sự về tài chính.\n- [[Lỗ Thiên Kiều]] — Công Bộ Thượng Thư, đồng liêu thường xuyên phối hợp ngân sách.\n- [[Khổng Minh Đức]] — Lễ Bộ Thượng Thư, tri kỷ trong triều, thường luận đạo sau giờ hội triều.",
        "Xuất thân từ thương gia đại tộc Trần gia ở Càn Dương Thành, từ nhỏ đã bộc lộ thiên phú quản lý tài vật. Sau khi bái nhập Nho giáo tu chân, hắn kết hợp thương đạo với tu luyện, phát triển Kim Toán Quyết độc đáo. Được Càn Đế bổ nhiệm Hộ Bộ Thượng Thư nhờ công lao ổn định tài chính quốc khố sau loạn Thất Vương. Quản lý toàn bộ thuế khóa, linh thạch, tài nguyên tu luyện của hoàng triều."
    ),
    "Khổng_Minh_Đức.md": (
        "Lão nhân dáng người thanh gầy, tóc bạc búi cao, mặc nho phục trắng tinh khiết. Khuôn mặt hiền hòa với đôi mắt sâu thẳm chứa đựng trí tuệ tích lũy hàng trăm năm. Tính cách chính trực, coi trọng lễ nghĩa hơn tất cả, là người giữ gìn truyền thống Nho giáo tu chân nghiêm ngặt nhất triều đình.",
        "Tu luyện Lễ Nhạc Chân Kinh, có thể dùng âm luật và nghi thức cổ xưa kích phát sức mạnh thiên địa. Khi tụng kinh, lễ nhạc vang lên có thể trấn áp tà ma, tịnh hóa uế khí trong phạm vi rộng lớn. Chuyên về nghi thức tế lễ Long Mạch, là người duy nhất ngoài Hoàng Đế có thể tiến hành đại lễ kết nối Long Khí.",
        "- [[Lý Thiên Vũ]] — Càn Đế, bậc quân vương mà ông cung kính phò tá về lễ chế.\n- [[Trần Bách Tài]] — Hộ Bộ Thượng Thư, bằng hữu thân thiết, thường uống trà luận đạo.\n- [[Trương Văn Hàn]] — Hàn Lâm Học Sĩ, đệ tử đắc ý nhất, được ông đích thân dạy dỗ.",
        "Hậu duệ của Khổng gia — một trong những dòng tộc Nho tu lâu đời nhất Thiên Trụ. Từ nhỏ được giáo dục nghiêm cách theo lễ giáo cổ phong, năm hai trăm tuổi đã đột phá Nguyên Anh. Được bổ nhiệm Lễ Bộ Thượng Thư nhờ uyên bác về nghi lễ và khả năng kết nối Long Mạch hiếm có. Ông cũng là người đề xuất khôi phục lại chế độ khoa cử tu chân, tuyển chọn nhân tài cho hoàng triều."
    ),
    "Vương_Thiết_Kỵ.md": (
        "Thân hình vạm vỡ như tháp sắt, cao hơn hai mét, da ngăm đen rám nắng, mặt đầy sẹo chiến trận. Luôn mang giáp chiến nặng nề ngay cả khi thượng triều, tay không rời đại đao Trảm Long. Tính cách cương trực như sắt thép, nóng nảy nhưng trung thành tuyệt đối, là mẫu võ tướng điển hình.",
        "Tu luyện Thiết Kỵ Chiến Thể, toàn thân cứng như huyền thiết, có thể chịu được công kích của tu sĩ cùng cảnh giới mà không hề hấn. Sở trường chiến đấu cận chiến với đại đao, mỗi nhát chém mang theo sát khí nghìn quân. Thống lĩnh binh pháp trận đồ, có thể chỉ huy quân đoàn tu sĩ bài binh bố trận trên chiến trường.",
        "- [[Lý Thiên Vũ]] — Càn Đế, chủ soái mà hắn thề nguyện bảo vệ đến chết.\n- [[Mộ Dung Chiến]] — Thần Sách Đại Tướng, chiến hữu sống chết từ thuở loạn Thất Vương.\n- [[Triệu Vạn Quân]] — Phó Tướng Thần Sách, thuộc hạ tin cậy được hắn đề bạt.",
        "Xuất thân từ biên cương phía bắc, là con trai một tướng quân trấn thủ đã tử trận khi chống Ma Tông xâm lấn. Mang thù nhà nợ nước, Vương Thiết Kỵ gia nhập quân đội hoàng triều từ năm mười sáu tuổi, lập vô số chiến công. Trong loạn Thất Vương, hắn cùng Mộ Dung Chiến đánh lui phản quân ở Thiết Quan, được Càn Đế phong Binh Bộ Thượng Thư. Chủ trương cứng rắn với các thế lực ma đạo, luôn đề nghị xuất binh tiêu diệt Cửu U Ma Tông."
    ),
    "Bao_Chính.md": (
        "Khuôn mặt lạnh lùng nghiêm nghị, da ngăm đen, trán rộng, mày rậm che đôi mắt sáng như sao. Luôn mặc hắc phục quan viên, thắt đai bạc, tay cầm Thiện Ác Bút — bút phán xét của Hình Bộ. Tính cách cương trực bất khuất, không nể nang quyền quý, được dân gian gọi là \"Bao Thiết Diện\".",
        "Tu luyện Thiện Ác Minh Kính Thuật, có thể nhìn thấu tâm tính thiện ác của đối phương, phát hiện lời nói dối và ảo thuật che giấu. Thiện Ác Bút khi kích phát có thể phóng ra Hình Phạt Chi Quang, chuyên trị ma khí và tà thuật. Tuy tu vi không phải cao nhất Lục Bộ, nhưng năng lực phán xét và trấn áp tà đạo khiến cả cường giả cũng kiêng dè.",
        "- [[Lý Thiên Vũ]] — Càn Đế, quân vương duy nhất mà hắn cúi đầu phục tùng.\n- [[Tôn Hiền]] — Lại Bộ Thượng Thư, đồng liêu chính trực, cùng chí hướng chống tham nhũng.\n- [[Vương Thiết Kỵ]] — Binh Bộ Thượng Thư, kính trọng lẫn nhau vì cùng tính cương trực.",
        "Mồ côi từ nhỏ, được một vị quan hưu trí nhặt về nuôi dạy theo đạo công chính liêm minh. Bao Chính nổi tiếng từ khi còn trẻ vì dám đàn hặc một vị hoàng thân tham ô, bất chấp áp lực quyền quý. Càn Đế ấn tượng với sự cương trực, bổ nhiệm hắn làm Hình Bộ Thượng Thư chuyên trách pháp luật tu chân giới. Dưới tay hắn, hàng chục vụ án oan sai được minh oan, kỷ cương triều đình được chấn chỉnh."
    ),
    "Lỗ_Thiên_Kiều.md": (
        "Trung niên nam tử dáng người thấp đậm, tay chai sạn, luôn mang theo cuộn bản vẽ và thước đo linh mạch. Mặc quan phục nâu giản dị, tóc buộc lỏng lẻo, râu quai nón rậm rạp. Tính tình thực tế, ít nói chuyện hoa mỹ, chỉ quan tâm đến công trình và xây dựng, là nhà kiến trúc tu chân hàng đầu hoàng triều.",
        "Tu luyện Bách Công Diệu Thuật, chuyên về xây dựng và gia cố công trình bằng linh lực. Có thể dùng Địa Mạch Thuật đo đạc và điều chỉnh dòng chảy Long Mạch để tối ưu phong thủy kiến trúc. Tuy chiến lực trực diện không mạnh, nhưng trận pháp phòng ngự do hắn thiết kế có thể chặn đứng cường giả Nguyên Anh.",
        "- [[Trần Bách Tài]] — Hộ Bộ Thượng Thư, thường xuyên phối hợp ngân sách cho công trình.\n- [[Lý Thiên Vũ]] — Càn Đế, người giao phó trọng trách xây dựng phòng tuyến biên cương.\n- [[Tôn Hiền]] — Lại Bộ Thượng Thư, bạn cờ buổi tối, mối quan hệ thoải mái nhất triều đình.",
        "Xuất thân từ Lỗ gia — gia tộc công tượng nổi tiếng nhiều đời, chuyên xây dựng cung điện và thành trì. Lỗ Thiên Kiều kế thừa tuyệt học gia truyền, nâng cấp thành Bách Công Diệu Thuật kết hợp kiến trúc với tu chân. Công trình nổi bật nhất là gia cố Vạn Lý Linh Tường — phòng tuyến chống ma tộc ở biên cương bắc. Được bổ nhiệm Công Bộ Thượng Thư nhờ công lao tái thiết kinh đô sau loạn Thất Vương."
    ),
    "Tôn_Hiền.md": (
        "Nho nhã thư sinh, dáng người mảnh khảnh, khuôn mặt thanh tú mang nét nho nhã. Luôn mặc thanh sam giản dị, tay cầm quạt gấp vẽ tranh sơn thủy. Tính cách ôn hòa, điềm đạm, nhưng khi xử lý nhân sự thì công tư phân minh, không chút thiên vị.",
        "Tu luyện Nhân Tâm Minh Giám Thuật, có thể đánh giá tài năng và phẩm chất của tu sĩ thông qua quan sát khí chất. Quạt gấp Nhân Hòa Phiến có thể phóng ra linh phong ôn hòa, dùng để bảo vệ hoặc trấn áp. Sở trường quản lý và đánh giá nhân sự, không phải chiến đấu gia, nhưng tự vệ quá đủ.",
        "- [[Lý Thiên Vũ]] — Càn Đế, quân vương mà hắn tận tâm tuyển chọn nhân tài phục vụ.\n- [[Bao Chính]] — Hình Bộ Thượng Thư, cùng chí hướng thanh liêm, thường trao đổi ý kiến.\n- [[Lỗ Thiên Kiều]] — Công Bộ Thượng Thư, bạn cờ thân thiết, mối quan hệ nhẹ nhàng thoải mái.",
        "Con trai dòng chính Tôn gia, một gia tộc nho tu trung lưu. Từ nhỏ được giáo dục bài bản về đạo trị nhân, sớm nổi tiếng với khả năng nhìn người chuẩn xác. Bước vào quan trường từ chức vụ nhỏ, dần thăng tiến nhờ tài năng thực sự và sự liêm chính. Hiện quản lý toàn bộ nhân sự quan viên hoàng triều, quyết định bổ nhiệm, thăng giáng và luân chuyển."
    ),
    "Mộ_Dung_Chiến.md": (
        "Trung niên uy mãnh, thân hình rắn chắc như đúc từ tinh cương, khuôn mặt lạnh lùng đầy sát khí. Mặc chiến giáp huyền thiết đen bóng, vai mang chiến bào đỏ thẫm, lưng đeo song kiếm Phong Vân. Tính cách quả quyết, ít lời, chỉ hành động, là vị tướng khiến ba quân kính sợ và kẻ thù khiếp đảm.",
        "Tu luyện Chiến Thần Quyết — công pháp chuyên cho chiến trường, tu vi càng cao thì sát khí càng mạnh. Song kiếm Phong Vân khi hợp bích tạo ra kiếm trận vạn nhận, có thể quét sạch cả quân đoàn. Là cường giả Hóa Thần Sơ Kỳ duy nhất trong Thần Sách Quân, một mình có thể chấn giữ cả chiến tuyến.",
        "- [[Lý Thiên Vũ]] — Càn Đế, chủ soái mà hắn tuyệt đối trung thành từ thuở hàn vi.\n- [[Vương Thiết Kỵ]] — Binh Bộ Thượng Thư, chiến hữu từ loạn Thất Vương, tri kỷ quân lữ.\n- [[Triệu Vạn Quân]] — Phó Tướng, phó thủ đáng tin cậy nhất, được hắn đích thân huấn luyện.",
        "Xuất thân từ Mộ Dung gia — gia tộc võ tướng truyền đời ở biên cương tây bắc. Theo Lý Thiên Vũ từ khi còn là phiên vương, cùng nhau chinh chiến trong loạn Thất Vương. Trận chiến Thiết Quan quyết định, Mộ Dung Chiến một mình chặn ba vạn phản quân, lập chiến công hiển hách. Sau khi Lý Thiên Vũ đăng cơ, được phong Thần Sách Đại Tướng, thống lĩnh đạo quân tinh nhuệ nhất hoàng triều."
    ),
    "Triệu_Vạn_Quân.md": (
        "Thanh niên cường tráng, dung mạo anh tuấn, đôi mắt sáng rực chiến ý. Mặc khinh giáp bạc, lưng đeo thương dài Xuyên Vân, di chuyển nhanh nhẹn như gió. Tính cách nhiệt huyết, trọng nghĩa khí, đối xử với binh sĩ như huynh đệ, được tướng sĩ Thần Sách yêu mến.",
        "Tu luyện Vạn Quân Phá Trận Thương Pháp, mỗi nhát đâm mang theo khí thế vạn quân xung phong. Khinh công cực kỳ xuất sắc, chuyên đột kích và đánh nhanh rút gọn trên chiến trường. Có thể kết hợp thương pháp với trận pháp quân đội, khuếch đại sức chiến đấu của cả đội hình.",
        "- [[Mộ Dung Chiến]] — Thần Sách Đại Tướng, sư phụ kiêm thượng cấp, hắn kính trọng vô cùng.\n- [[Vương Thiết Kỵ]] — Binh Bộ Thượng Thư, người tiến cử hắn vào Thần Sách Quân.\n- [[Lưu Phong Thành]] — Tướng Quân Thị Vệ, bằng hữu cùng trang lứa, thường so kiếm luyện tập.",
        "Xuất thân bình dân, con trai một nông dân biên cương, nhờ thiên phú tu luyện được Vương Thiết Kỵ phát hiện và tiến cử. Gia nhập Thần Sách Quân từ binh sĩ thường, nhanh chóng thăng cấp nhờ chiến công liên tiếp ở biên giới bắc. Được Mộ Dung Chiến đích thân thu nhận làm đệ tử, truyền thụ Chiến Thần Quyết. Hiện là Phó Tướng trẻ nhất lịch sử Thần Sách, được kỳ vọng kế nhiệm vị trí Đại Tướng."
    ),
    "Tư_Mã_Tinh_Vân.md": (
        "Lão nhân tóc bạc phơ, mắt mờ đục như bị sương phủ, nhưng khi quan sát tinh tú thì sáng rực dị thường. Khoác đạo bào xanh thẫm thêu tinh đồ, tay luôn cầm Hồn Thiên Nghi — dụng cụ quan trắc thiên cơ. Tính cách kỳ quái, thường nói những lời mập mờ khó hiểu, nhưng mỗi lời dự đoán đều ứng nghiệm.",
        "Tu luyện Quan Tinh Thuật — tuyệt học quan sát tinh tú để suy đoán thiên cơ, vận mệnh và cát hung. Có thể dùng Tinh Vân Trận Pháp triển khai trận thế dựa trên vị trí tinh tú, uy lực biến ảo khôn lường. Ngoài ra còn tinh thông bốc quẻ, phong thủy, và dự đoán thiên tai, là bộ não chiến lược ẩn sau triều đình.",
        "- [[Lý Thiên Vũ]] — Càn Đế, quân vương mà ông bí mật cố vấn thiên cơ đại sự.\n- [[Hà Thiên Chiêu]] — Phó Giám, đệ tử thân cận nhất, được truyền thụ Quan Tinh Thuật.\n- [[Khổng Minh Đức]] — Lễ Bộ Thượng Thư, cùng hợp tác trong các đại lễ tế Long Mạch.",
        "Xuất thân từ Tư Mã gia — gia tộc thiên văn lâu đời nhất Đại Càn, đời đời giữ chức Khâm Thiên Giám. Từ thuở nhỏ đã có thể nhìn thấy tinh tú giữa ban ngày, được coi là thiên tài bẩm sinh. Dự đoán chính xác loạn Thất Vương trước ba năm, giúp Lý Thiên Vũ chuẩn bị đối phó kịp thời. Hiện đang lo lắng vì tinh tượng gần đây cho thấy một kiếp nạn lớn sắp giáng xuống Thiên Trụ."
    ),
    "Hà_Thiên_Chiêu.md": (
        "Thiếu nữ trẻ tuổi dáng mảnh mai, mái tóc dài đen mượt buông xõa, đôi mắt trong veo như hồ nước phản chiếu bầu trời đêm. Mặc đạo bào xanh nhạt, eo thắt dây ngọc treo la bàn tinh tú nhỏ. Tính cách trầm tĩnh, ít nói, nhưng khi quan sát tinh tượng thì tập trung đến mức quên ăn quên ngủ.",
        "Tu luyện Quan Tinh Thuật do Tư Mã Tinh Vân truyền dạy, tuy chưa đạt đến trình độ của sư phụ nhưng đã có thể dự đoán cát hung ngắn hạn. Sở trường sử dụng Tinh La Bàn để định vị và truy tìm, có thể tìm ra vị trí của bất kỳ ai trong phạm vi nghìn dặm. Đang nghiên cứu cách kết hợp Quan Tinh Thuật với Long Mạch Thuật để nâng cao độ chính xác dự đoán.",
        "- [[Tư Mã Tinh Vân]] — Khâm Thiên Giám Chính, sư phụ kính yêu, người dẫn dắt cô vào thiên đạo.\n- [[Lý Nguyệt Nhi]] — Công Chúa, bằng hữu thân thiết, thường cùng nhau ngắm sao đêm.\n- [[Trương Văn Hàn]] — Hàn Lâm Học Sĩ, sư huynh cùng theo học Nho đạo thời niên thiếu.",
        "Mồ côi từ nhỏ, được Tư Mã Tinh Vân nhặt về nuôi dạy khi phát hiện cô có linh căn đặc biệt tương thích với Quan Tinh Thuật. Cô lớn lên trong Khâm Thiên Giám, coi tinh tú là bạn bè, sư phụ là cha. Tuy tuổi còn trẻ nhưng đã lập công lớn khi dự đoán chính xác vị trí bọn gián điệp Ma Tông trong kinh thành. Được bổ nhiệm Phó Giám, là nữ quan viên trẻ nhất trong lịch sử Khâm Thiên Giám."
    ),
    "Lý_Thiên_Long.md": (
        "Thanh niên tuấn tú, dung mạo giống Càn Đế thời trẻ, nhưng ánh mắt mềm mại hơn, mang nét nhân hậu. Mặc hoàng bào vàng nhạt thêu rồng đơn, đầu đội kim quan Thái Tử, phong thái đường đường chính chính. Tính cách nhân từ, coi trọng dân sinh, nhưng đôi khi bị cho là quá mềm yếu so với phụ hoàng.",
        "Tu luyện Hoàng Đạo Chân Kinh phiên bản Thái Tử, mới nắm được ba tầng, có thể triệu hồi Long Khí nhỏ hộ thể. Kiếm pháp do Mộ Dung Chiến đích thân chỉ dạy, tuy chưa tinh thông nhưng cơ bản vững chắc. Đang tập trung tu luyện, cố gắng đột phá Nguyên Anh Trung Kỳ trước khi kế vị.",
        "- [[Lý Thiên Vũ]] — Phụ hoàng, người mà hắn kính trọng nhưng cũng chịu áp lực nặng nề.\n- [[Lý Thiên Phượng]] — Nhị đệ, mối quan hệ phức tạp, vừa thương vừa cảnh giác.\n- [[Lý Nguyệt Nhi]] — Muội muội yêu quý, người duy nhất hắn có thể thổ lộ tâm sự.",
        "Là trưởng tử của Càn Đế, được lập Thái Tử từ khi còn nhỏ. Lớn lên dưới sự giáo dục nghiêm khắc của Khổng Minh Đức về lễ nghĩa và Mộ Dung Chiến về võ công. Tính cách nhân hậu khiến hắn được lòng dân nhưng bị một số quan thần cho là thiếu quyết đoán. Đang đối mặt với áp lực từ Nhị Hoàng Tử Lý Thiên Phượng, người được cho là tài năng hơn nhưng dã tâm khó lường."
    ),
    "Lý_Thiên_Phượng.md": (
        "Thanh niên dung mạo tuấn mỹ phi phàm, hơn cả Thái Tử về phong thái, ánh mắt sắc sảo ẩn chứa dã tâm. Mặc bạch bào hoàng tử thêu phượng, quạt gấp kim sa không rời tay, dáng vẻ phong lưu nhàn nhã. Tính cách thông minh mưu lược, ngoài mặt khiêm nhường nhưng trong lòng nuôi chí lớn, luôn ngấm ngầm kết giao thế lực.",
        "Tu luyện Phượng Vũ Quyết — biến thể của Hoàng Đạo Chân Kinh do tự nghiên cứu, thiên về tốc độ và biến hóa. Quạt gấp kim sa là pháp khí ẩn giấu sức mạnh, có thể phóng ra phượng hỏa đốt cháy mọi thứ. Tuy tu vi mới Kết Đan Viên Mãn nhưng chiến lực thực tế vượt xa cảnh giới nhờ trí tuệ và mưu lược.",
        "- [[Lý Thiên Long]] — Thái Tử huynh, đối thủ ngôi vị, ngoài mặt kính trọng nhưng trong lòng không phục.\n- [[Lý Thiên Vũ]] — Phụ hoàng, người mà hắn vừa kính sợ vừa muốn vượt qua.\n- [[Trần Bách Tài]] — Hộ Bộ Thượng Thư, ngấm ngầm kết giao để nắm tài chính.",
        "Là thứ tử của Càn Đế, từ nhỏ đã thể hiện thiên phú vượt trội hơn Thái Tử. Nhưng vì không phải trưởng tử, bị bỏ qua ngôi vị kế thừa, nuôi mối bất mãn sâu trong lòng. Tự nghiên cứu biến thể Hoàng Đạo Chân Kinh, chứng minh tài năng tu luyện phi phàm. Đang bí mật xây dựng thế lực riêng trong triều đình, chờ thời cơ tranh đoạt ngai vàng."
    ),
    "Lý_Nguyệt_Nhi.md": (
        "Thiếu nữ xinh đẹp thanh thoát, dung mạo như trăng rằm sáng tỏ, nụ cười ấm áp khiến người đối diện dịu lòng. Mặc hoàng sam nhạt thêu hoa lan, tóc dài búi nửa cài trâm ngọc nguyệt. Tính cách hoạt bát, thông minh, có tấm lòng nhân hậu, là ánh sáng duy nhất giữa những mưu mô của hoàng cung.",
        "Tu luyện Nguyệt Hoa Thuật — chi lưu nhẹ nhàng của Hoàng Đạo Chân Kinh, chuyên về chữa trị và bảo hộ. Linh lực mang thuộc tính nguyệt quang, có thể chữa lành vết thương và giải trừ độc tố. Tuy chiến lực không cao nhưng năng lực chữa trị hiếm có, được coi là báu vật của hoàng gia.",
        "- [[Lý Thiên Vũ]] — Phụ hoàng, người sủng ái cô nhất, luôn bảo vệ khỏi mưu mô triều chính.\n- [[Lý Thiên Long]] — Thái Tử huynh, người mà cô thương yêu và lo lắng nhất.\n- [[Hà Thiên Chiêu]] — Bằng hữu thân thiết, thường cùng nhau ngắm trăng sao trong cung.",
        "Là con gái duy nhất của Càn Đế, được sủng ái vô cùng. Từ nhỏ không thích mưu mô chính trị, chỉ say mê tu luyện y thuật và ngắm trăng sao. Phát hiện Nguyệt Hoa Thuật hoàn toàn ngẫu nhiên khi cố chữa trị cho con chim bị thương trong cung. Luôn lo lắng về mâu thuẫn ngày càng gay gắt giữa hai anh trai, hy vọng gia đình hoàng thất có thể hòa thuận."
    ),
    "Trương_Văn_Hàn.md": (
        "Thư sinh trung niên dáng mảnh mai, khuôn mặt hiền hòa, đeo kính tròn bằng ngọc minh quang. Luôn mang theo chồng sách cổ và bút lông, mực tự chế từ linh thảo. Tính cách ôn nhu, lễ độ, nhưng khi tranh luận học thuật thì hùng biện không ai địch nổi.",
        "Tu luyện Văn Đạo Chân Kinh — dùng chữ viết và văn chương làm phương tiện tu luyện, mỗi chữ viết ra đều chứa linh lực. Có thể dùng Thiên Chương Bút vẽ phù chú trên không trung, tạo ra kết giới bảo hộ hoặc tấn công. Sở trường nghiên cứu và phân tích, là bộ óc tri thức của hoàng triều.",
        "- [[Khổng Minh Đức]] — Lễ Bộ Thượng Thư, ân sư truyền dạy Nho đạo tu chân.\n- [[Hà Thiên Chiêu]] — Phó Giám Khâm Thiên, sư muội thời niên thiếu, mối quan hệ thân thiết.\n- [[Lý Thiên Long]] — Thái Tử, được hắn dạy kèm kinh sử và trị quốc chi đạo.",
        "Xuất thân hàn môn, nhờ thiên phú văn học xuất chúng mà trúng tuyển khoa cử tu chân do Khổng Minh Đức tổ chức. Được Khổng Minh Đức thu nhận làm đệ tử, truyền dạy Nho đạo tu chân và Văn Đạo Chân Kinh. Sau khi đỗ đầu, được bổ nhiệm Hàn Lâm Học Sĩ, chuyên nghiên cứu cổ tịch và cố vấn cho hoàng triều. Tuy chức vị không cao nhưng được Càn Đế trọng dụng, thường triệu vào cung bàn luận đại sự."
    ),
    "Lưu_Phong_Thành.md": (
        "Thanh niên vạm vỡ, khuôn mặt vuông vức cương nghị, đôi mắt luôn cảnh giác quan sát xung quanh. Mặc cấm vệ giáp vàng, lưng đeo thần binh Phong Thành Kích, mỗi bước đi đều vững chãi như núi. Tính cách trung thành, nghiêm túc, coi việc bảo vệ hoàng gia là sứ mệnh thiêng liêng nhất.",
        "Tu luyện Cấm Vệ Thần Công — công pháp chuyên cho thị vệ hoàng cung, tăng cường cảm quan và phản ứng. Kích pháp mạnh mẽ, mỗi nhát chém tạo ra phong nhận sắc bén, có thể cắt đứt cả kết giới. Chuyên phối hợp trận pháp cấm vệ, mười sáu thị vệ dưới quyền hợp lực có thể chặn đứng cường giả Nguyên Anh.",
        "- [[Lý Thiên Vũ]] — Càn Đế, chủ nhân mà hắn thề bảo vệ bằng mạng sống.\n- [[Triệu Vạn Quân]] — Phó Tướng Thần Sách, bằng hữu cùng lứa, thường thi đấu luyện tập.\n- [[Lý Nguyệt Nhi]] — Công Chúa, đối tượng bảo vệ đặc biệt, trong lòng có chút tình cảm ẩn giấu.",
        "Xuất thân từ gia tộc thị vệ truyền đời, cha là cấm vệ quân trưởng tiền nhiệm đã hy sinh khi bảo vệ Càn Đế trong loạn Thất Vương. Kế thừa di chí của cha, Lưu Phong Thành gia nhập cấm vệ quân từ thiếu niên, nhanh chóng vượt qua mọi thử thách. Được Càn Đế bổ nhiệm Tướng Quân Thị Vệ nhờ lòng trung thành tuyệt đối và tài năng chiến đấu. Bí mật mang trong lòng tình cảm với Công Chúa Nguyệt Nhi, nhưng không dám thổ lộ vì thân phận cách biệt."
    ),

    # ============================================================
    # FACTION 2: CỬU U MA TÔNG
    # ============================================================
    "Ma_Chủ_Vô_Tên.md": (
        "Không ai từng thấy chân dung — luôn ẩn sau lớp hắc ám nồng đặc, chỉ thấy bóng dáng mờ ảo và đôi mắt đỏ rực như hai hố thẳm. Giọng nói không phân biệt nam nữ, khi thì trầm khàn, khi thì lanh lảnh, như thể có nhiều linh hồn cùng nói. Khí chất ma đạo thuần túy, sự hiện diện khiến không gian xung quanh méo mó, bầu trời tối sầm.",
        "Tu luyện Vạn Ma Chân Kinh — tuyệt học tối thượng của Cửu U Ma Tông, có thể triệu hồi và dung hợp vạn loại ma lực. Một tay có thể xé rách không gian, triệu hoán quỷ vật từ U Minh giới xông ra. Thực lực đạt Luyện Hư Trung Kỳ, đứng đầu toàn bộ ma đạo, ngay cả Cửu Đại Ma Vương hợp lực cũng không phải đối thủ.",
        "- [[Cừu Huyết Thiên]] — Đệ Nhất Ma Vương, thuộc hạ trung thành nhất, thi hành mọi mệnh lệnh.\n- [[Âm Phong]] — Đệ Nhị Ma Vương, công cụ chiến đấu mạnh nhất dưới trướng.\n- [[Lý Vô Ảnh]] — Ảnh Ma Viện Chủ, mắt và tai bí mật, nắm mạng lưới tình báo.",
        "Không ai biết lai lịch thật sự của Ma Chủ Vô Tên — có giả thuyết nói đó là một cổ ma từ thời thượng cổ tái sinh, có giả thuyết nói đó là tu sĩ chính đạo đọa lạc. Ma Chủ xuất hiện bốn trăm năm trước, bằng thực lực tuyệt đối khuất phục Cửu Đại Ma Vương, thống nhất các thế lực ma đạo rời rạc thành Cửu U Ma Tông. Dưới sự lãnh đạo bí ẩn, Ma Tông từ tổ chức nhỏ bé trở thành thế lực đáng sợ nhất bên ngoài Đại Càn. Mục đích thật sự vẫn là bí ẩn lớn nhất Thiên Trụ."
    ),
    "Cừu_Huyết_Thiên.md": (
        "Trung niên dung mạo tuấn mỹ nhưng đáng sợ, da trắng bệch như không có máu, môi đỏ tươi như vừa uống huyết. Mặc huyết bào đỏ thẫm, tóc đen dài buông xõa, đôi mắt đỏ hồng phát sáng trong bóng tối. Tính cách tàn nhẫn, thích đùa cợt với con mồi trước khi giết, nhưng đối với Ma Chủ thì tuyệt đối trung thành.",
        "Tu luyện Huyết Ma Đại Pháp — hút huyết dịch của tu sĩ khác để tăng cường tu vi và hồi phục thương tích. Có thể biến huyết dịch thành vũ khí, tạo ra huyết kiếm, huyết trận, huyết phong bao phủ chiến trường. Là Huyết Ma Đường Chủ, nắm trong tay hàng nghìn huyết nô — tu sĩ bị cưỡng chế hút huyết biến thành bù nhìn.",
        "- [[Ma Chủ Vô Tên]] — Ma Chủ, đấng tối cao mà hắn tuyệt đối trung thành phục tùng.\n- [[Âm Phong]] — Đệ Nhị Ma Vương, kẻ mà hắn vừa coi thường vừa cảnh giác.\n- [[Cừu Huyết Nhi]] — Con gái, đệ tử chân truyền, hy vọng duy nhất kế thừa Huyết Ma Đường.",
        "Xuất thân từ một gia tộc tu chân nhỏ bị diệt môn, Cừu Huyết Thiên là người sống sót duy nhất. Mang thù hận tận xương, hắn tình nguyện tu luyện Huyết Ma Đại Pháp — công pháp bị cấm kỵ nhất tu chân giới. Hắn dùng chính huyết của kẻ diệt gia tộc mình để đột phá, rồi gia nhập Cửu U Ma Tông, nhanh chóng leo lên vị trí Đệ Nhất Ma Vương. Lập Huyết Ma Đường, biến nó thành cỗ máy thu hoạch huyết dịch kinh hoàng nhất ma đạo."
    ),
    "Âm_Phong.md": (
        "Thân hình cao gầy như bộ xương di động, da xanh xao, tóc bạc trắng bay phần phật trong gió âm. Khoác hắc bào rách rưới, mặt luôn đeo mặt nạ trắng nứt nẻ chỉ lộ đôi mắt xám lạnh. Tính cách âm trầm, ít nói, nhưng mỗi lời phát ra đều lạnh như gió cắt da thịt, khiến người nghe rùng mình.",
        "Tu luyện Âm Phong Hàn Sát Thuật — triệu hồi gió âm từ U Minh giới, mang theo hàn khí cực độ có thể đóng băng linh hồn. Khi toàn lực, gió âm bao phủ phạm vi vạn trượng, biến mọi thứ thành băng giá, kể cả linh lực đối phương. Tốc độ di chuyển trong gió âm nhanh đến mức vô hình, khiến đối thủ không kịp phản ứng.",
        "- [[Ma Chủ Vô Tên]] — Ma Chủ, đấng tối cao duy nhất mà hắn phục tùng.\n- [[Cừu Huyết Thiên]] — Đệ Nhất Ma Vương, đối thủ cạnh tranh ngôi vị, mối quan hệ căng thẳng.\n- [[Hồn Diệt]] — Đệ Tam Ma Vương, đồng minh tạm thời, cùng nhau kiềm chế Cừu Huyết Thiên.",
        "Không ai biết tên thật và gốc gác, Âm Phong xuất hiện như bóng ma trong một trận bão tuyết ở biên cương bắc, hủy diệt cả một thị trấn tu chân trong một đêm. Ma Chủ Vô Tên đích thân tìm đến chiêu mộ, phong làm Đệ Nhị Ma Vương sau khi chứng kiến sức mạnh kinh hoàng. Hắn là lưỡi dao sắc nhất của Ma Tông, được phái đi mỗi khi cần hủy diệt hoàn toàn mục tiêu. Âm thầm nuôi dã tâm vượt qua Cừu Huyết Thiên để trở thành kẻ đứng dưới một người trên vạn người."
    ),
    "Hồn_Diệt.md": (
        "Bóng dáng mờ ảo, thân hình lúc đậm lúc nhạt như ảo ảnh, khuôn mặt xanh xám với đôi mắt trống rỗng không có đồng tử. Khoác ma bào đen tuyền, xung quanh thân thể luôn vang lên tiếng khóc than của hồn ma. Tính cách lạnh lùng vô cảm, không quan tâm đến sinh tử, coi sự hủy diệt linh hồn là nghệ thuật tối cao.",
        "Tu luyện Diệt Hồn Đại Pháp — chuyên tấn công linh hồn, bỏ qua mọi phòng ngự vật lý. Có thể rút hồn đối phương ra khỏi thể xác, nuốt chửng để tăng cường thần thức. Sở hữu Vạn Hồn Phiên — pháp khí chứa hàng vạn linh hồn bị giam cầm, có thể phóng ra tạo thành biển hồn tấn công.",
        "- [[Ma Chủ Vô Tên]] — Ma Chủ, kẻ duy nhất mà hắn không dám rút hồn.\n- [[Âm Phong]] — Đệ Nhị Ma Vương, đồng minh tạm thời chống lại phe Cừu Huyết Thiên.\n- [[Nạp Lan U Minh]] — Đệ Tứ Ma Vương, mối quan hệ cộng sinh — một bên diệt hồn, một bên triệu hồn.",
        "Trước đây là một tu sĩ chính đạo tu luyện hồn thuật để chữa bệnh, nhưng sau khi chứng kiến toàn bộ gia đình bị giết hại, linh hồn của hắn bị tổn thương nghiêm trọng. Trong cơn điên loạn, hắn rút hồn kẻ thù, vô tình kích hoạt Diệt Hồn Đại Pháp bị cấm. Kể từ đó, hắn mất đi mọi cảm xúc, trở thành cỗ máy hủy diệt linh hồn lạnh lùng. Gia nhập Cửu U Ma Tông vì đó là nơi duy nhất dung nạp kẻ tu luyện tà thuật như hắn."
    ),
    "Nạp_Lan_U_Minh.md": (
        "Trung niên dung mạo quý phái, da trắng xanh như ngọc, mắt tím đậm phát quang quỷ dị. Mặc tử bào thêu hoa văn U Minh cổ ngữ, tay cầm xương trượng khắc đầu lâu. Tính cách trầm mặc, thâm trầm, ít khi tức giận nhưng mỗi khi nổi giận thì quỷ khốc thần sầu.",
        "Tu luyện U Minh Triệu Hồn Thuật — có thể mở cổng kết nối với U Minh giới, triệu hồi quỷ vật và vong linh chiến đấu. Xương trượng là chìa khóa mở U Minh Môn, có thể triệu hoán từ tiểu quỷ đến đại quỷ tướng. Khi toàn lực có thể triệu hồi U Minh Chi Quân — đạo quân vong linh hàng vạn, đủ sức tàn phá cả thành trì.",
        "- [[Ma Chủ Vô Tên]] — Ma Chủ, đấng tối cao mà hắn kính sợ và phục tùng.\n- [[Hồn Diệt]] — Đệ Tam Ma Vương, mối quan hệ cộng sinh đặc biệt.\n- [[Nạp Lan Tiểu U]] — Con gái yêu quý, đệ tử chân truyền, kế thừa U Minh Thuật.",
        "Xuất thân từ Nạp Lan gia — gia tộc cổ xưa có huyết mạch liên hệ với U Minh giới. Từ nhỏ có thể nhìn thấy quỷ vật mà người thường không thấy, bị gia tộc và xã hội coi là yêu nghiệt. Bị trục xuất khỏi gia tộc, lang thang vô định cho đến khi Ma Chủ Vô Tên tìm thấy và nhận ra tiềm năng. Trong Ma Tông, hắn tìm được chỗ đứng, phát triển U Minh Triệu Hồn Thuật đến cảnh giới kinh ngạc."
    ),
    "Lý_Cửu_Âm.md": (
        "Lão nhân gầy gò, da nhăn nheo xám xịt, móng tay dài đen sì luôn nhỏ giọt chất lỏng xanh lục. Khoác lục bào bạc màu, lưng còng, nhưng đôi mắt xanh lục sáng rực tinh quái. Tính cách xảo quyệt, thích nghiên cứu và thí nghiệm, coi tu sĩ khác là vật liệu thí nghiệm tiềm năng.",
        "Tu luyện Cửu Âm Độc Kinh — tuyệt học dùng âm độc (độc tố từ nguồn âm khí) xâm nhập kinh mạch đối phương. Có thể bào chế vạn loại kịch độc, từ độc sát thể xác đến độc hại linh hồn. Bản thân đã miễn dịch với mọi loại độc tố, thậm chí máu và hơi thở cũng mang kịch độc.",
        "- [[Ma Chủ Vô Tên]] — Ma Chủ, người cung cấp tài nguyên cho nghiên cứu độc thuật.\n- [[Mạc U Hồn]] — Đệ Lục Ma Vương, đối tác nghiên cứu, thường trao đổi tà thuật.\n- [[Bạch Cốt]] — Đệ Thất Ma Vương, cung cấp xương cốt làm nguyên liệu bào chế độc.",
        "Xuất thân là một dược sư tu chân, từng phục vụ một tông phái chính đạo. Vì nghiên cứu độc dược bị cấm, bị trục xuất và truy sát, buộc phải chạy vào ma đạo. Trong Cửu U Ma Tông, hắn tìm được tự do nghiên cứu không giới hạn, phát triển Cửu Âm Độc Kinh đến cảnh giới biến hóa khôn lường. Phụ trách bào chế ma dược và độc vật cho toàn Ma Tông, là trụ cột hậu cần không thể thiếu."
    ),
    "Mạc_U_Hồn.md": (
        "Thanh niên dung mạo bí ẩn, nửa khuôn mặt bị che bởi mặt nạ quỷ hỏa, nửa còn lại lộ ra làn da trắng nhợt nhạt. Đôi mắt một đỏ một xanh, luôn bập bùng ngọn lửa quỷ xanh lục xung quanh thân. Tính cách thất thường, lúc điên cuồng cười lớn, lúc lạnh lùng im lặng, khó ai đoán được tâm tư.",
        "Tu luyện Quỷ Hỏa Phần Thiên Thuật — triệu hồi và thao túng quỷ hỏa (lửa ma) từ U Minh giới, nhiệt độ không đốt thể xác mà đốt cháy linh hồn. Quỷ hỏa không thể dập tắt bằng nước hay linh lực thông thường, chỉ có thể tự tắt khi linh hồn mục tiêu bị thiêu hủy hoàn toàn. Khi phát động Quỷ Hỏa Liên Ngục, cả vùng biến thành biển lửa xanh lục, sinh linh không thể thoát thân.",
        "- [[Ma Chủ Vô Tên]] — Ma Chủ, đấng tối cao mà hắn điên cuồng sùng bái.\n- [[Lý Cửu Âm]] — Đệ Ngũ Ma Vương, đối tác nghiên cứu, cùng trao đổi tà thuật kinh dị.\n- [[Diệp Huyền Minh]] — Đệ Bát Ma Vương, kẻ mà hắn hay trêu chọc nhưng ngầm kính trọng.",
        "Xuất thân bất minh, chỉ biết rằng hắn xuất hiện sau một trận hỏa hoạn quỷ dị thiêu rụi cả một thung lũng. Khi được Ma Tông tìm thấy, hắn đã mất trí nhớ, chỉ nhớ cách thao túng quỷ hỏa. Ma Chủ Vô Tên phong hắn làm Đệ Lục Ma Vương sau khi chứng kiến hắn đốt cháy linh hồn của ba vị trưởng lão phản bội. Hắn là kẻ không thể kiểm soát hoàn toàn, nhưng sức mạnh quỷ hỏa khiến Ma Tông không thể bỏ rơi."
    ),
    "Bạch_Cốt.md": (
        "Thân hình cao lớn dị thường, toàn thân bọc trong bạch cốt giáp — bộ giáp ghép từ xương cốt tu sĩ, trắng ngà lấp lánh. Khuôn mặt che sau mặt nạ sọ người, chỉ lộ đôi mắt vàng âm u. Tính cách trầm mặc ít nói, nhưng ám ảnh với việc thu thập xương cốt, coi đó là \"tác phẩm nghệ thuật\".",
        "Tu luyện Bạch Cốt Ma Công — dùng xương cốt làm vũ khí và phương tiện tu luyện, có thể thao túng cốt cách của đối phương. Có thể rút xương đối thủ ra khỏi thân thể, hoặc tạo ra quái vật xương cốt khổng lồ chiến đấu. Bạch Cốt Giáp trên người hấp thụ sát thương và tự phục hồi, gần như bất hoại.",
        "- [[Ma Chủ Vô Tên]] — Ma Chủ, chủ nhân mà hắn phục tùng không điều kiện.\n- [[Lý Cửu Âm]] — Đệ Ngũ Ma Vương, cung cấp xương cốt cho nghiên cứu độc dược, đổi lấy ma dược.\n- [[Quỷ Diện]] — Đệ Cửu Ma Vương, tiểu đệ mà hắn vô cùng ghét bỏ vì tính cách xảo trá.",
        "Xuất thân là con trai một nghệ nhân điêu khắc xương nổi tiếng, từ nhỏ đã quen thuộc với việc xử lý xương cốt. Sau khi cha bị giết vì từ chối tạo pháp khí xương cho một tà tu, hắn dùng chính kỹ thuật của cha để trả thù. Quá trình trả thù vô tình lĩnh ngộ Bạch Cốt Ma Công, từ đó bước vào con đường ma đạo không thể quay đầu. Gia nhập Ma Tông, trở thành Đệ Thất Ma Vương, bộ sưu tập xương cốt của hắn là nỗi kinh hoàng của tu chân giới."
    ),
    "Diệp_Huyền_Minh.md": (
        "Thanh niên dung mạo thanh tú, trông như thư sinh nho nhã, hoàn toàn không giống ma tu. Da trắng sáng, mắt đen sâu thẳm, luôn mang nụ cười nhẹ bí ẩn. Tính cách trầm tĩnh, mưu lược, thích dùng trí tuệ hơn bạo lực, là bộ óc chiến thuật của Cửu Đại Ma Vương.",
        "Tu luyện Huyền Minh Ảo Trận Thuật — chuyên về ảo thuật và trận pháp hắc ám, có thể tạo ra ảo cảnh đánh lừa cả thần thức cường giả. Trận pháp của hắn kết hợp ảo thuật với sát trận, kẻ rơi vào không phân biệt được thực hư, dần dần bị tiêu diệt mà không hay biết. Ngoài ra còn tinh thông ma đạo trận đồ phòng thủ, là người thiết kế hệ thống phòng ngự cho tổng đàn Ma Tông.",
        "- [[Ma Chủ Vô Tên]] — Ma Chủ, đấng tối cao mà hắn phục tùng và ngưỡng mộ trí tuệ.\n- [[Mạc U Hồn]] — Đệ Lục Ma Vương, kẻ hay trêu chọc hắn nhưng thực lực khiến hắn phải cẩn trọng.\n- [[Lý Vô Ảnh]] — Ảnh Ma Viện Chủ, đối tác chia sẻ thông tin và phối hợp trận pháp.",
        "Xuất thân từ một gia tộc trận sư chính đạo, nhưng phát hiện bí mật đen tối của gia tộc — họ đã lén lút sử dụng ma đạo trận pháp suốt nhiều đời. Vỡ mộng với sự giả dối của chính đạo, hắn chủ động tìm đến Cửu U Ma Tông, mang theo toàn bộ tri thức trận pháp gia truyền. Ma Chủ đánh giá cao trí tuệ của hắn, phong làm Đệ Bát Ma Vương và giao nhiệm vụ xây dựng phòng tuyến tổng đàn. Hắn là Ma Vương ôn hòa nhất, hiếm khi trực tiếp giết người, nhưng trận pháp của hắn đã gián tiếp cướp đi vô số sinh mạng."
    ),
    "Quỷ_Diện.md": (
        "Không có dung mạo cố định — khuôn mặt thay đổi liên tục, lúc là nam lúc là nữ, lúc trẻ lúc già. Thân hình cũng biến hóa theo, có thể trở thành bất kỳ ai đã từng gặp. Tính cách mưu mô xảo quyệt, thích lừa gạt và giả mạo, coi việc đánh cắp danh tính người khác là trò chơi thú vị nhất.",
        "Tu luyện Thiên Biến Vạn Hóa Thuật — có thể biến hình thành bất kỳ ai, sao chép hoàn hảo cả ngoại hình, giọng nói, khí tức và thần thái. Ngoài biến hình, có thể \"ăn cắp\" một phần năng lực của đối tượng bị sao chép trong thời gian ngắn. Tuy tu vi thấp nhất trong Cửu Đại Ma Vương, nhưng khả năng gián điệp và ám sát khiến hắn trở thành kẻ nguy hiểm nhất.",
        "- [[Ma Chủ Vô Tên]] — Ma Chủ, người duy nhất mà hắn không thể sao chép, vì vậy càng kính sợ.\n- [[Lý Vô Ảnh]] — Ảnh Ma Viện Chủ, thượng cấp trực tiếp trong nhiều nhiệm vụ gián điệp.\n- [[Bạch Cốt]] — Đệ Thất Ma Vương, kẻ ghét hắn cay đắng, luôn muốn rút xương hắn.",
        "Không ai biết Quỷ Diện thật sự là ai — ngay cả hắn cũng quên mất khuôn mặt thật sau hàng trăm năm biến hình. Có giả thuyết nói hắn từng là tội phạm bị xử tử, dùng Thiên Biến Vạn Hóa Thuật thay thế người khác để trốn thoát. Gia nhập Ma Tông và trở thành gián điệp hoàn hảo, xâm nhập nhiều tông phái chính đạo đánh cắp bí mật. Được phong Đệ Cửu Ma Vương tuy tu vi thấp nhưng công lao tình báo vượt trội, là con dao bí mật sắc bén nhất của Ma Chủ."
    ),
    "Lý_Vô_Ảnh.md": (
        "Nhân dạng mờ ảo, thường chỉ thấy bóng đen lướt qua, khuôn mặt che kín sau đầu trùm đen. Thân hình mảnh mai, di chuyển không tiếng động, sự hiện diện mờ nhạt đến mức ngay cả đồng môn cũng quên mất hắn đang ở đó. Tính cách lạnh lùng, hiệu quả, coi cảm xúc là điểm yếu, hoàn thành nhiệm vụ là tất cả.",
        "Tu luyện Vô Ảnh Ám Sát Thuật — tuyệt học ẩn mình trong bóng tối, xóa hoàn toàn khí tức và sự tồn tại. Có thể di chuyển qua bóng tối như xuyên không gian, xuất hiện ở bất kỳ nơi nào có bóng râm. Ám khí của hắn mang ma lực xâm thực, một khi trúng đòn, ma khí sẽ lan ra phá hủy kinh mạch từ bên trong.",
        "- [[Ma Chủ Vô Tên]] — Ma Chủ, chủ nhân trực tiếp giao nhiệm vụ tình báo và ám sát.\n- [[Quỷ Diện]] — Đệ Cửu Ma Vương, thuộc hạ thường xuyên phối hợp trong nhiệm vụ gián điệp.\n- [[Diệp Huyền Minh]] — Đệ Bát Ma Vương, đối tác chia sẻ thông tin chiến lược.",
        "Xuất thân là trẻ mồ côi được Cửu U Ma Tông thu nhận từ nhỏ, được huấn luyện thành sát thủ hoàn hảo từ khi lên năm. Không có ký ức về gia đình, không có tên thật, \"Lý Vô Ảnh\" là danh hiệu Ma Chủ ban cho. Xây dựng Ảnh Ma Viện thành mạng lưới tình báo đáng sợ nhất Thiên Trụ, mắt tai có mặt ở mọi nơi. Là cánh tay bí mật của Ma Chủ, thực hiện những nhiệm vụ mà ngay cả Cửu Đại Ma Vương cũng không được biết."
    ),
    "Nạp_Lan_Tiểu_U.md": (
        "Thiếu nữ mười sáu tuổi, dung mạo thanh lệ pha nét quỷ mị di truyền từ phụ thân, mắt tím nhạt phát sáng nhẹ. Mặc hắc sam ngắn tiện lợi, tóc buộc hai bên, trông ngây thơ nhưng ánh mắt lạnh lùng vượt tuổi. Tính cách kiêu ngạo, ít nói với người ngoài, nhưng với phụ thân thì tỏ ra nũng nịu hiếm thấy.",
        "Tu luyện U Minh Triệu Hồn Thuật phiên bản đơn giản hóa do phụ thân truyền dạy, có thể triệu hồi tiểu quỷ cấp thấp. Tuy tu vi mới Kết Đan Đỉnh Phong nhưng thiên phú kiểm soát quỷ vật vượt xa phụ thân thời trẻ. Đang nghiên cứu cách kết hợp quỷ vật với trận pháp, thể hiện tư duy sáng tạo phi phàm.",
        "- [[Nạp Lan U Minh]] — Phụ thân, người mà cô kính yêu nhất, sư phụ kiêm cha.\n- [[Cừu Huyết Nhi]] — Bằng hữu duy nhất trong Ma Tông, cùng trang lứa.\n- [[Mạc Ám]] — Sư huynh nội môn, kẻ mà cô ngầm cảnh giác.",
        "Sinh ra trong Cửu U Ma Tông, là con gái duy nhất của Đệ Tứ Ma Vương Nạp Lan U Minh. Từ nhỏ lớn lên giữa ma khí và quỷ vật, coi đó là chuyện bình thường. Được phụ thân bảo vệ cẩn thận, nhưng bản thân cô cũng chứng minh tài năng bằng cách thuần hóa một U Minh Quỷ Thú ở tuổi mười hai. Là chân truyền đệ tử được kỳ vọng kế thừa U Minh Triệu Hồn Thuật, nhưng trong lòng cô thỉnh thoảng tò mò về thế giới bên ngoài Ma Tông."
    ),
    "Cừu_Huyết_Nhi.md": (
        "Thiếu nữ nhỏ tuổi, da trắng bệch giống phụ thân, mái tóc đỏ huyết dị thường, đôi mắt hồng nhạt trong veo. Mặc hồng sam nhạt, trông mong manh như búp bê sứ, nhưng ẩn chứa huyết ma khí nồng nặc. Tính cách nhút nhát, ít nói, sợ máu dù là hậu duệ Huyết Ma, luôn tự dằn vặt về bản năng hút huyết.",
        "Tu luyện Huyết Ma Đại Pháp phiên bản sơ cấp, có thể cảm nhận huyết dịch trong phạm vi rộng và thao túng lượng nhỏ huyết dịch. Tuy mới Kết Đan Sơ Kỳ nhưng huyết mạch đặc biệt cho phép sử dụng Huyết Khiên phòng thủ mạnh vượt cảnh giới. Đang cố gắng tìm cách tu luyện Huyết Ma Pháp mà không cần hút huyết người khác.",
        "- [[Cừu Huyết Thiên]] — Phụ thân, người mà cô vừa thương vừa sợ vì sự tàn nhẫn.\n- [[Nạp Lan Tiểu U]] — Bằng hữu duy nhất, người mà cô tin tưởng nhất.\n- [[Ma Chủ Vô Tên]] — Ma Chủ, sự tồn tại đáng sợ mà cô cố gắng tránh xa.",
        "Sinh ra là con gái của Đệ Nhất Ma Vương, mang trong mình huyết mạch Huyết Ma thuần khiết nhất. Nhưng trái với kỳ vọng của phụ thân, cô ghê sợ việc hút huyết và tàn sát. Phụ thân nhiều lần ép cô giết người tu luyện, cô đều lén lút tìm cách cứu nạn nhân. Sống trong mâu thuẫn giữa bản năng Huyết Ma và lương tâm, cô là ánh sáng hiếm hoi trong bóng tối Cửu U Ma Tông."
    ),
    "Mạc_Ám.md": (
        "Thiếu niên gầy gò, dung mạo tầm thường dễ bị lãng quên, mắt đen trầm lặng che giấu tham vọng sâu thẳm. Mặc nội môn hắc bào giản dị, di chuyển nhẹ nhàng như bóng. Tính cách bề ngoài khiêm tốn phục tùng, nhưng bên trong tính toán lạnh lùng, luôn quan sát và chờ thời cơ.",
        "Tu luyện tạp nhạp nhiều ma công cấp thấp, không chuyên tinh nhưng linh hoạt biến hóa. Sở trường ẩn giấu thực lực, khiến đối phương luôn đánh giá thấp. Tuy mới Trúc Cơ Viên Mãn nhưng chiến đấu thực tế ranh mãnh hơn nhiều kẻ cùng cảnh giới.",
        "- [[Nạp Lan Tiểu U]] — Sư muội chân truyền, kẻ mà hắn ngấm ngầm ghen tị vì thiên phú.\n- [[Cừu Huyết Nhi]] — Sư muội nội môn, mối quan hệ bình thường bề ngoài.\n- [[Lý Vô Ảnh]] — Ảnh Ma Viện Chủ, hắn bí mật muốn gia nhập Ảnh Ma Viện để tiến thân.",
        "Xuất thân bất minh, được Ma Tông thu nhận từ đám trẻ mồ côi ngoài biên cương. Không có thiên phú nổi bật, nhưng tồn tại trong Ma Tông bằng sự khôn ngoan và nhẫn nại phi thường. Âm thầm quan sát và học hỏi từ mọi người xung quanh, tích lũy kiến thức và kinh nghiệm. Mục tiêu bí mật là leo lên vị trí Ma Vương, chứng minh rằng kẻ không có thiên phú cũng có thể đứng trên đỉnh ma đạo."
    ),

    # ============================================================
    # FACTION 3: THIÊN KIÊU HỌC VIỆN
    # ============================================================
    "Hạo_Nhiên.md": (
        "Lão nhân cao lớn, tóc bạc phơ búi gọn, khuôn mặt hiền hòa với đôi mắt sáng ấm áp như mặt trời mùa đông. Mặc bạch bào viện trưởng thêu vân hạc, tay cầm phất trần trắng muốt, phong thái tiên nhân đạo cốt. Tính cách ôn hòa bao dung, coi trọng học trò như con cháu, nhưng khi cần thiết thì uy nghiêm không kém bậc đế vương.",
        "Tu luyện Hạo Nhiên Chính Khí — tuyệt học Nho đạo chính thống, linh lực hóa thành chính khí thuần dương áp chế mọi tà ma. Phất trần Thanh Vân là pháp khí truyền đời của Viện Trưởng, một nhát quét có thể tịnh hóa ma khí trong phạm vi trăm dặm. Là cường giả Hóa Thần Hậu Kỳ, thực lực đứng đầu Thiên Kiêu, có thể đối kháng cả Ma Vương cấp cường giả.",
        "- [[Lý Học Hải]] — Phó Viện Trưởng Học Thuật, đệ tử đắc ý nhất, cánh tay phải đáng tin cậy.\n- [[Vương Chiến]] — Phó Viện Trưởng Chiến Đấu, chiến hữu lâu năm, bổ sung lẫn nhau.\n- [[Lý Thiên Vũ]] — Càn Đế, mối quan hệ bình đẳng, cùng bảo vệ Thiên Trụ chính đạo.",
        "Là truyền nhân đời thứ chín của Thiên Kiêu Học Viện, tiếp nhận chức Viện Trưởng từ sư phụ tiền nhiệm hơn bốn trăm năm trước. Dưới thời ông, Thiên Kiêu trở thành học viện tu chân uy tín nhất Thiên Trụ, đào tạo vô số nhân tài. Từng cùng Càn Đế Lý Thiên Vũ chiến đấu trong loạn Thất Vương, bảo vệ kinh đô khỏi sụp đổ. Hiện tại ông lo lắng về thế hệ trẻ, tin rằng kiếp nạn lớn sắp đến và chỉ có thế hệ mới mới có thể vượt qua."
    ),
    "Lý_Học_Hải.md": (
        "Trung niên nho nhã, khuôn mặt thông tuệ với cặp kính ngọc bạch, tóc đen chải gọn gàng. Mặc thanh bào giáo sư, lưng thẳng, tay luôn cầm sách hoặc bút lông. Tính cách nghiêm cẩn, cầu toàn, đặt tiêu chuẩn rất cao cho bản thân và học trò, nhưng cũng biết khích lệ đúng lúc.",
        "Tu luyện Bác Học Đa Văn Thuật — công pháp dựa trên tri thức, càng hiểu biết rộng thì linh lực càng mạnh. Sở trường phân tích và giải mã pháp thuật, trận pháp, đan dược của bất kỳ hệ phái nào. Có thể dùng Vạn Quyển Thư Lâu — không gian lưu trữ tri thức trong thần thức — để tức thời tra cứu và phản chế kỹ thuật đối phương.",
        "- [[Hạo Nhiên]] — Viện Trưởng kiêm sư phụ, người mà hắn kính trọng nhất đời.\n- [[Vương Chiến]] — Phó Viện Trưởng Chiến Đấu, đồng liêu, văn võ bổ sung lẫn nhau.\n- [[Khổng Thư]] — Giáo sư lịch sử, đệ tử mà hắn đào tạo, kỳ vọng kế nhiệm.",
        "Xuất thân từ một gia đình thư hương, từ nhỏ đã đọc vạn quyển sách, được coi là thần đồng tri thức. Bái nhập Thiên Kiêu từ năm mười tuổi, là sinh viên xuất sắc nhất trong lịch sử bộ phận học thuật. Được Hạo Nhiên đích thân thu nhận làm đệ tử, truyền thụ và phát triển Bác Học Đa Văn Thuật. Trở thành Phó Viện Trưởng Học Thuật ở tuổi hai trăm, quản lý toàn bộ chương trình giảng dạy và nghiên cứu của học viện."
    ),
    "Vương_Chiến.md": (
        "Trung niên vạm vỡ, khuôn mặt vuông vức đầy nghị lực, cơ bắp cuồn cuộn dưới chiến phục xám. Cánh tay trái mang xăm hình hổ xuống núi, lưng đeo đại kiếm Hổ Khiếu. Tính cách hào sảng, nóng nảy, nói là làm, coi trọng thực lực hơn lý thuyết, là mẫu võ phu đáng mến.",
        "Tu luyện Mãnh Hổ Chiến Quyết — công pháp dương cương chí cường, mỗi đòn đánh mang sức mạnh bạo liệt như mãnh hổ. Kiếm pháp Hổ Khiếu phối hợp thể thuật, chuyên cận chiến áp chế đối thủ bằng sức mạnh thuần túy. Ngoài ra còn tinh thông huấn luyện chiến đấu, đào tạo ra nhiều thế hệ chiến đấu gia cho tu chân giới.",
        "- [[Hạo Nhiên]] — Viện Trưởng, sư phụ kiêm thượng cấp, người mà hắn tuyệt đối tin tưởng.\n- [[Lý Học Hải]] — Phó Viện Trưởng Học Thuật, đồng liêu, hay cãi nhau nhưng tôn trọng lẫn nhau.\n- [[Triệu Phong Vân]] — Chiến Đấu Viện Chủ, đệ tử đắc ý nhất, kế thừa tinh hoa chiến đấu.",
        "Xuất thân từ một gia tộc võ tướng, từ nhỏ đã rèn luyện thể xác và chiến đấu. Bái nhập Thiên Kiêu và nhanh chóng thống trị chiến đấu bộ phận, trở thành \"Chiến Vương\" huyền thoại trong sinh viên. Sau khi tốt nghiệp, được Hạo Nhiên mời ở lại làm giáo sư, rồi thăng chức Phó Viện Trưởng Chiến Đấu. Cùng Lý Học Hải tạo thành bộ đôi \"Văn Võ Song Tuyệt\" nổi tiếng Thiên Trụ, duy trì sự cân bằng của học viện."
    ),
    "Tôn_Thiên_Cơ.md": (
        "Trung niên gầy gò, mắt sáng tinh anh, ngón tay dài linh hoạt luôn bấm đốt tính toán. Mặc bạch bào viện chủ, lưng thêu hoa văn trận pháp phức tạp, eo thắt đai chứa bút trận và la bàn. Tính cách trầm tĩnh, mê trận pháp đến mức quên ăn quên ngủ, nhưng khi giảng dạy thì nhiệt tình bất tận.",
        "Tu luyện Thiên Cơ Trận Thuật — tuyệt học trận pháp biến hóa vô cùng, có thể tức thời thiết lập trận pháp phù hợp mọi tình huống. Sở trường kết hợp nhiều loại trận pháp chồng chéo, tạo ra hệ thống phòng thủ tấn công phức tạp mà đối phương không thể giải. Là chuyên gia trận pháp hàng đầu Thiên Kiêu, hệ thống phòng ngự học viện do hắn thiết kế.",
        "- [[Hạo Nhiên]] — Viện Trưởng, ân sư khai sáng cho hắn con đường trận đạo.\n- [[Lý Học Hải]] — Phó Viện Trưởng Học Thuật, thượng cấp trực tiếp, cung cấp tài liệu nghiên cứu.\n- [[Triệu Phong Vân]] — Chiến Đấu Viện Chủ, đối tác phối hợp trận pháp và chiến đấu.",
        "Xuất thân từ gia tộc trận sư, nhưng gia tộc sa sút, chỉ còn lại vài cuộn trận đồ cổ. Bái nhập Thiên Kiêu nhờ thiên phú trận pháp được Hạo Nhiên phát hiện, nhanh chóng trở thành chuyên gia trận đạo hàng đầu. Phát triển Thiên Cơ Trận Thuật dựa trên nền tảng gia truyền kết hợp tri thức học viện. Hiện quản lý Trận Chư Viện, đào tạo thế hệ trận sư mới và không ngừng nghiên cứu nâng cấp hệ thống phòng ngự Thiên Kiêu."
    ),
    "Triệu_Phong_Vân.md": (
        "Nữ tướng trung niên, dáng người cao ráo mạnh mẽ, mái tóc đen cột đuôi ngựa gọn gàng. Khuôn mặt sắc sảo với vết sẹo mỏng chéo qua sống mũi, đôi mắt sáng rực đấu chí. Tính cách thẳng thắn, cạnh tranh, luôn tìm cách vượt qua giới hạn bản thân, truyền tinh thần chiến đấu cho học trò.",
        "Tu luyện Cuồng Phong Kiếm Pháp — kiếm thuật dương cương tốc độ cao, mỗi kiếm chiêu tạo ra phong nhận sắc bén cắt qua mọi phòng ngự. Có thể triển khai Phong Vân Kiếm Trận đơn độc, biến mình thành tâm bão kiếm khí quét sạch đối thủ. Là chiến đấu gia mạnh nhất Thiên Kiêu sau Viện Trưởng và hai Phó Viện Trưởng.",
        "- [[Vương Chiến]] — Phó Viện Trưởng Chiến Đấu, sư phụ đã dạy dỗ cô thành chiến sĩ.\n- [[Tôn Thiên Cơ]] — Trận Chư Viện Chủ, đối tác phối hợp chiến đấu và trận pháp.\n- [[Trương Tinh Thần]] — Sinh viên xuất sắc nhất, đệ tử mà cô đặt nhiều kỳ vọng.",
        "Xuất thân bình dân, cha mẹ là tu sĩ cấp thấp ở ngoại thành. Nhờ thiên phú chiến đấu phi phàm được tuyển vào Thiên Kiêu, trở thành học trò xuất sắc nhất của Vương Chiến. Sau khi tốt nghiệp, từ chối nhiều lời mời từ quân đội và tông phái, chọn ở lại học viện dạy dỗ thế hệ sau. Trở thành Chiến Đấu Viện Chủ trẻ nhất lịch sử Thiên Kiêu, vẫn giữ phong độ chiến đấu đỉnh cao."
    ),
    "Lỗ_Bách_Nghệ.md": (
        "Trung niên nữ, dáng người tròn trịa phúc hậu, tay chai sạn đầy vết bỏng và vết cắt từ công việc. Mặc tạp dề da trên áo bào viện chủ, tóc búi gọn cài trâm sắt, mắt sáng nhiệt tình. Tính cách vui vẻ, phóng khoáng, mê sáng tạo, xưởng luyện khí của cô luôn ồn ào và đầy mùi kim loại nóng chảy.",
        "Tu luyện Bách Nghệ Tạo Hóa Công — công pháp chuyên về luyện khí, chế tạo pháp khí và phù lục. Có thể luyện chế pháp khí từ linh quặng, cải tạo và nâng cấp pháp khí cũ, sáng chế công cụ tu chân mới. Tuy chiến lực trực diện không nổi bật nhưng pháp khí do cô chế tạo có chất lượng hàng đầu Thiên Trụ.",
        "- [[Hạo Nhiên]] — Viện Trưởng, ân sư cho phép cô tự do sáng tạo trong học viện.\n- [[Tôn Thiên Cơ]] — Trận Chư Viện Chủ, đối tác thường xuyên — cô chế tạo vật liệu trận pháp cho hắn.\n- [[Hoàng Phủ Lạc Thiên]] — Giáo sư đan dược, bằng hữu thân thiết, thường trao đổi kỹ thuật.",
        "Xuất thân từ Lỗ gia — nhánh bên của gia tộc Lỗ Thiên Kiều (Công Bộ Thượng Thư), thừa hưởng thiên phú thủ công mỹ nghệ. Không thích quan trường, chọn bái nhập Thiên Kiêu để tự do nghiên cứu và sáng tạo. Phát triển Bách Nghệ Tạo Hóa Công kết hợp kỹ thuật gia truyền với phương pháp học viện. Hiện quản lý Bách Nghệ Viện, cung cấp pháp khí và công cụ cho toàn bộ học viện và cả hoàng triều."
    ),
    "Khổng_Thư.md": (
        "Nữ giáo sư trung niên, dung mạo đoan trang, khuôn mặt thanh nhã mang nét trí tuệ. Mặc nho phục xanh nhạt, tóc búi cao cài trâm sách, tay luôn cầm cuộn trúc giản cổ. Tính cách điềm đạm, nhẫn nại, giọng nói trầm ấm khiến sinh viên say mê nghe giảng hàng giờ không chán.",
        "Tu luyện Sử Giám Chân Kinh — công pháp dựa trên hiểu biết lịch sử, có thể dùng thần thức tái hiện sự kiện quá khứ tại một địa điểm. Sở trường phân tích và dự đoán dựa trên quy luật lịch sử, cung cấp góc nhìn chiến lược cho học viện. Trúc giản Sử Giám có thể tạo ảo ảnh lịch sử để giảng dạy, giúp sinh viên trải nghiệm trực tiếp sự kiện quá khứ.",
        "- [[Lý Học Hải]] — Phó Viện Trưởng Học Thuật, sư phụ đã đào tạo cô thành giáo sư.\n- [[Hạo Nhiên]] — Viện Trưởng, bậc tiền bối mà cô kính trọng sâu sắc.\n- [[Khổng Minh Đức]] — Lễ Bộ Thượng Thư, chú ruột bên ngoài học viện, thuộc Khổng gia.",
        "Là cháu gái của Khổng Minh Đức, thừa hưởng truyền thống Nho tu của Khổng gia. Nhưng khác với chú, cô không chọn quan trường mà đam mê nghiên cứu lịch sử tu chân giới. Bái nhập Thiên Kiêu theo lời giới thiệu của Lý Học Hải, nhanh chóng trở thành chuyên gia lịch sử hàng đầu. Đang nghiên cứu về thời kỳ thượng cổ, tin rằng lịch sử ẩn chứa manh mối về kiếp nạn sắp tới."
    ),
    "Hoàng_Phủ_Lạc_Thiên.md": (
        "Thanh niên nho nhã, dung mạo tuấn tú, luôn mang theo thoang thoảng mùi dược hương. Mặc bạch bào giáo sư, eo thắt dây đan lô nhỏ, ngón tay mảnh mai linh hoạt thường xuyên bào chế đan dược. Tính cách ôn nhu, kiên nhẫn, nói chuyện nhỏ nhẹ, nhưng đối với chất lượng đan dược thì cầu toàn đến mức khắc nghiệt.",
        "Tu luyện Lạc Thiên Đan Thuật — công pháp luyện đan kết hợp dược lý với linh lực tinh tế, đan dược luyện ra có hiệu quả vượt trội cùng cấp. Sở trường bào chế đan dược chữa thương, tăng tu vi, và giải độc, có thể tùy biến công thức theo tình trạng từng người. Đan lô tùy thân có thể luyện đan mọi lúc mọi nơi, là \"dược khố di động\" của học viện.",
        "- [[Hạo Nhiên]] — Viện Trưởng, ân sư cho phép hắn tự do nghiên cứu đan đạo.\n- [[Lỗ Bách Nghệ]] — Bách Nghệ Viện Chủ, bằng hữu thân thiết, thường trao đổi kỹ thuật.\n- [[Lâm Tĩnh]] — Giáo sư tâm pháp, đồng nghiệp, cung cấp tâm pháp hỗ trợ luyện đan.",
        "Xuất thân từ Hoàng Phủ gia — gia tộc dược sư nổi tiếng nhiều đời. Thừa hưởng thiên phú đan đạo gia truyền, từ nhỏ đã có thể phân biệt hàng trăm loại linh dược bằng mùi hương. Bái nhập Thiên Kiêu ở tuổi mười lăm, nhanh chóng vượt qua mọi giáo sư đan dược tiền nhiệm. Tuy tuổi đời trẻ nhất trong hàng giáo sư nhưng trình độ đan thuật không ai dám coi thường, đan dược của hắn được cả hoàng triều trọng dụng."
    ),
    "Lâm_Tĩnh.md": (
        "Nữ giáo sư trung niên, dung mạo thanh nhã tĩnh lặng, như hồ nước phẳng lặng không gợn sóng. Mặc bạch bào đơn giản, tóc dài buông tự nhiên, mắt nhắm hờ như đang nhập định. Tính cách ít nói, bình thản, không bao giờ nổi giận, sự hiện diện của cô khiến xung quanh trở nên yên tĩnh lạ thường.",
        "Tu luyện Tĩnh Tâm Minh Giác Thuật — công pháp chuyên về tâm pháp, thiền định và kiểm soát tinh thần. Có thể dùng thần thức trấn áp tâm ma, chữa trị tổn thương tinh thần cho tu sĩ bị tẩu hỏa nhập ma. Sở trường dạy sinh viên ổn định tâm tính, vượt qua tâm chướng — nền tảng quan trọng nhất của tu luyện.",
        "- [[Hạo Nhiên]] — Viện Trưởng, ân sư truyền dạy Tĩnh Tâm Thuật.\n- [[Hoàng Phủ Lạc Thiên]] — Giáo sư đan dược, đồng nghiệp, tâm pháp của cô hỗ trợ luyện đan.\n- [[Tiêu Mộng Dao]] — Nữ sinh viên xuất sắc, có thiên phú tâm pháp, đệ tử mà cô đặc biệt chú ý.",
        "Xuất thân từ một ngôi chùa nhỏ ở vùng núi hẻo lánh, từ nhỏ tu thiền cùng sư phụ. Sau khi sư phụ viên tịch, cô rời núi gia nhập Thiên Kiêu theo di nguyện. Thiên phú tâm pháp khiến cô nhanh chóng được chú ý, trở thành giáo sư chuyên trách thiền định và tâm tính tu luyện. Nhiều tu sĩ bị tẩu hỏa nhập ma trên khắp Thiên Trụ đều tìm đến cô chữa trị, danh tiếng \"Tĩnh Tâm Tiên Cô\" vang xa."
    ),
    "Trương_Tinh_Thần.md": (
        "Thiếu niên mười bảy tuổi, dung mạo anh tuấn sáng sủa, ánh mắt kiên định vượt tuổi. Mặc sinh viên bào trắng viền xanh, thắt lưng đeo kiếm ngắn Tinh Thần, dáng đi thẳng lưng đầy tự tin. Tính cách chính trực, cầu tiến, không ngại thử thách, luôn đứng đầu mọi bảng xếp hạng của học viện.",
        "Tu luyện Tinh Thần Kiếm Thuật — kiếm pháp kết hợp tinh thần lực với kiếm khí, mỗi kiếm chiêu mang theo ý chí kiên định. Tuy mới Kết Đan Sơ Kỳ nhưng chiến lực vượt cảnh giới nhờ tinh thần lực mạnh mẽ phi thường. Đang được Triệu Phong Vân đích thân kèm cặp, kỳ vọng trở thành chiến đấu gia thế hệ mới.",
        "- [[Triệu Phong Vân]] — Chiến Đấu Viện Chủ, sư phụ trực tiếp kèm cặp và huấn luyện.\n- [[Tiêu Mộng Dao]] — Đồng học, đối thủ cạnh tranh hạng nhất, mối quan hệ vừa ganh đua vừa tôn trọng.\n- [[Vương Chiến]] — Phó Viện Trưởng Chiến Đấu, sư tổ mà hắn ngưỡng mộ.",
        "Xuất thân từ gia đình bình thường ở ngoại thành, cha mẹ là nông dân không có tu vi. Được phát hiện có linh căn xuất sắc khi lên mười, tuyển vào Thiên Kiêu bằng học bổng. Từ sinh viên tầm thường, nhờ nỗ lực phi thường vươn lên đứng đầu, chứng minh rằng cần cù bù thiên phú. Là niềm tự hào của Chiến Đấu Viện, được coi là ứng cử viên sáng giá nhất cho danh hiệu \"Thiên Kiêu\" của thế hệ mới."
    ),
    "Tiêu_Mộng_Dao.md": (
        "Thiếu nữ mười sáu tuổi, dung mạo thanh lệ thoát tục, mái tóc dài đen mượt buông xõa đến eo. Mặc sinh viên bào trắng viền hồng, tay cầm tiêu trúc — nhạc khí kiêm pháp khí. Tính cách trầm tĩnh, nội tâm, ngoài mặt lạnh lùng nhưng bên trong giàu cảm xúc, biểu đạt tâm tư qua tiếng tiêu.",
        "Tu luyện Mộng Dao Tiêu Thuật — dùng âm thanh từ tiêu trúc tác động thần thức đối phương, tạo ảo giác hoặc trấn áp tinh thần. Tiếng tiêu có thể an thần chữa bệnh hoặc rối loạn tâm trí tùy ý, hiệu quả tăng mạnh theo tu vi. Tuy mới Trúc Cơ Viên Mãn nhưng âm công thiên phú vượt xa kỳ vọng, được Lâm Tĩnh đặc biệt chú ý.",
        "- [[Lâm Tĩnh]] — Giáo sư tâm pháp, người hướng dẫn đặc biệt, cô kính trọng như mẫu thân.\n- [[Trương Tinh Thần]] — Đồng học, đối thủ cạnh tranh, mối quan hệ phức tạp vừa ganh đua vừa ngưỡng mộ.\n- [[Hạo Nhiên]] — Viện Trưởng, bậc tiền bối mà cô tôn kính từ xa.",
        "Xuất thân từ gia tộc nhạc sư đã sa sút, chỉ còn lại cây tiêu trúc gia truyền. Mồ côi mẹ từ nhỏ, cha bệnh nặng, cô thi vào Thiên Kiêu để có cơ hội tu luyện cứu cha. Phát hiện thiên phú âm công khi vô tình thổi tiêu và kích phát linh lực, được Lâm Tĩnh nhận ra tiềm năng. Tuy tu vi còn thấp nhưng tiềm năng được đánh giá ngang Trương Tinh Thần, là ngôi sao nữ sáng nhất thế hệ mới của Thiên Kiêu."
    ),
}


def process_file(filename, sections, faction_dir):
    filepath = os.path.join(BASE, faction_dir, filename)
    # Handle macOS NFD normalization
    if not os.path.exists(filepath):
        filepath = unicodedata.normalize("NFD", filepath)
    if not os.path.exists(filepath):
        filepath = unicodedata.normalize("NFC", filepath)
    if not os.path.exists(filepath):
        print(f"  [SKIP] File not found: {os.path.join(BASE, faction_dir, filename)}")
        return False

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    sec_ii, sec_iii, sec_iv, sec_v = sections

    # We need to replace each section's placeholder.
    # The pattern is: "## II. NGOẠI HÌNH & TÍNH CÁCH\n*(Chưa xác định)*"
    # Replace with: "## II. NGOẠI HÌNH & TÍNH CÁCH\n<content>"

    replacements = [
        ("## II. NGOẠI HÌNH & TÍNH CÁCH\n*(Chưa xác định)*",
         f"## II. NGOẠI HÌNH & TÍNH CÁCH\n{sec_ii}"),
        ("## III. NĂNG LỰC & CHIẾN ĐẤU\n*(Chưa xác định)*",
         f"## III. NĂNG LỰC & CHIẾN ĐẤU\n{sec_iii}"),
        ("## IV. CÁC MỐI QUAN HỆ\n*(Chưa xác định)*",
         f"## IV. CÁC MỐI QUAN HỆ\n{sec_iv}"),
        ("## V. TIỂU SỬ & HÀNH TRÌNH\n*(Chưa xác định)*",
         f"## V. TIỂU SỬ & HÀNH TRÌNH\n{sec_v}"),
    ]

    changed = False
    for old, new in replacements:
        if old in content:
            content = content.replace(old, new)
            changed = True

    if changed:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  [OK] {filename}")
    else:
        print(f"  [NO CHANGE] {filename} — placeholders not found (already filled?)")

    return changed


def main():
    print("=" * 60)
    print("Filling character details for 3 Thiên Trụ factions")
    print("=" * 60)

    factions = {
        "Đại Càn Hoàng Triều": (FACTION_DIRS["Đại Càn Hoàng Triều"], [
            "Lý_Thiên_Vũ.md", "Trần_Bách_Tài.md", "Khổng_Minh_Đức.md",
            "Vương_Thiết_Kỵ.md", "Bao_Chính.md", "Lỗ_Thiên_Kiều.md",
            "Tôn_Hiền.md", "Mộ_Dung_Chiến.md", "Triệu_Vạn_Quân.md",
            "Tư_Mã_Tinh_Vân.md", "Hà_Thiên_Chiêu.md", "Lý_Thiên_Long.md",
            "Lý_Thiên_Phượng.md", "Lý_Nguyệt_Nhi.md", "Trương_Văn_Hàn.md",
            "Lưu_Phong_Thành.md",
        ]),
        "Cửu U Ma Tông": (FACTION_DIRS["Cửu U Ma Tông"], [
            "Ma_Chủ_Vô_Tên.md", "Cừu_Huyết_Thiên.md", "Âm_Phong.md",
            "Hồn_Diệt.md", "Nạp_Lan_U_Minh.md", "Lý_Cửu_Âm.md",
            "Mạc_U_Hồn.md", "Bạch_Cốt.md", "Diệp_Huyền_Minh.md",
            "Quỷ_Diện.md", "Lý_Vô_Ảnh.md", "Nạp_Lan_Tiểu_U.md",
            "Cừu_Huyết_Nhi.md", "Mạc_Ám.md",
        ]),
        "Thiên Kiêu Học Viện": (FACTION_DIRS["Thiên Kiêu Học Viện"], [
            "Hạo_Nhiên.md", "Lý_Học_Hải.md", "Vương_Chiến.md",
            "Tôn_Thiên_Cơ.md", "Triệu_Phong_Vân.md", "Lỗ_Bách_Nghệ.md",
            "Khổng_Thư.md", "Hoàng_Phủ_Lạc_Thiên.md", "Lâm_Tĩnh.md",
            "Trương_Tinh_Thần.md", "Tiêu_Mộng_Dao.md",
        ]),
    }

    total = 0
    updated = 0

    for faction_name, (faction_dir, files) in factions.items():
        print(f"\n--- {faction_name} ---")
        for fn in files:
            total += 1
            if fn in CHARS:
                if process_file(fn, CHARS[fn], faction_dir):
                    updated += 1
            else:
                print(f"  [SKIP] No data for {fn}")

    print(f"\n{'=' * 60}")
    print(f"Done: {updated}/{total} files updated.")
    print("=" * 60)


if __name__ == "__main__":
    main()
