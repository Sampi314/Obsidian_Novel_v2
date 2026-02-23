import os

def create_song_entry(title, meaning_theme, style_prompt, chinese_lyrics, hanviet_lyrics, meaning_lyrics):
    return f"""
## {title}

### I. NGUYÊN VĂN TIẾNG TRUNG (CHINESE LYRICS)
{chinese_lyrics}

### II. PHIÊN ÂM HÁN VIỆT (SINO-VIETNAMESE LYRICS)
{hanviet_lyrics}

### III. DỊCH SÁT NGHĨA (LITERAL TRANSLATION)
{meaning_lyrics}

### IV. THÔNG TIN BỔ SUNG
*   **Ý Nghĩa/Thông Điệp:**
    - **Chủ đề:** {meaning_theme}
*   **Suno AI Style Prompt:**
    > {style_prompt}

---
"""

activities_songs = [
    ("Đan Đạo Ca - Luyện Đan", "Luyện Đan.", "Mystical, Fire sounds.",
     "**(Verse 1)**\n金炉火起红烟飞，\n铅汞相投造化机。\n九转丹成惊鬼神，\n从此长生入紫微。",
     "**(Verse 1)**\nKim lô hỏa khởi hồng yên phi,\nDiên hống tương đầu tạo hóa cơ.\nCửu chuyển đan thành kinh quỷ thần,\nTòng thử trường sinh nhập tử vi.",
     "**(Verse 1)**\nLửa lò vàng nổi lên khói đỏ bay,\nChì và thủy ngân gặp nhau tạo nên cơ hội tạo hóa.\nĐan chín chuyển thành công kinh động quỷ thần,\nTừ nay trường sinh bước vào cung Tử Vi."),

    ("Khí Đạo Tụng - Luyện Khí", "Luyện Khí.", "Hammering sounds.",
     "**(Verse 1)**\n千锤百炼出深山，\n烈火焚烧若等闲。\n粉身碎骨浑不怕，\n要留清白在人间。",
     "**(Verse 1)**\nThiên chùy bách luyện xuất thâm sơn,\nLiệt hỏa phần thiêu nhược đẳng nhàn.\nPhấn thân toái cốt hồn bất phạ,\nYếu lưu thanh bạch tại nhân gian.",
     "**(Verse 1)**\nNgàn búa trăm luyện ra khỏi núi sâu,\nLửa mạnh thiêu đốt coi như thường.\nTan xương nát thịt cũng chẳng sợ,\nMuốn để lại sự trong trắng ở nhân gian."),

    ("Phù Lục Chú - Vẽ Bùa", "Vẽ Bùa.", "Paper sounds, Chant.",
     "**(Verse 1)**\n朱砂一点鬼神惊，\n笔走龙蛇气象生。\n借问苍天何处法，\n灵符一道镇妖精。",
     "**(Verse 1)**\nChu sa nhất điểm quỷ thần kinh,\nBút tẩu long xà khí tượng sinh.\nTá vấn thương thiên hà xứ pháp,\nLinh phù nhất đạo trấn yêu tinh.",
     "**(Verse 1)**\nMột điểm chu sa khiến quỷ thần kinh sợ,\nBút chạy như rồng rắn sinh ra khí tượng.\nXin hỏi trời xanh pháp thuật ở đâu,\nMột đạo linh phù trấn áp yêu tinh."),

    ("Trận Pháp Ca - Bày Trận", "Bày Trận.", "Complex, Mathematical.",
     "**(Verse 1)**\n八门金锁困蛟龙，\n十面埋伏绝路穷。\n变化无穷藏玄机，\n入此阵中万事空。",
     "**(Verse 1)**\nBát môn kim tỏa khốn giao long,\nThập diện mai phục tuyệt lộ cùng.\nBiến hóa vô cùng tàng huyền cơ,\nNhập thử trận trung vạn sự không.",
     "**(Verse 1)**\nKhóa vàng tám cửa nhốt giao long,\nMai phục mười mặt đường cùng tuyệt lộ.\nBiến hóa vô cùng ẩn chứa huyền cơ,\nVào trong trận này vạn sự đều hư không."),

    ("Linh Thực Ngâm - Trồng Cây", "Trồng Cây.", "Nature, Gentle.",
     "**(Verse 1)**\n锄禾日当午，\n汗滴禾下土。\n谁知盘中餐，\n粒粒皆辛苦。",
     "**(Verse 1)**\nSư hòa nhật đương ngọ,\nHãn tích hòa hạ thổ.\nThùy tri bàn trung Xan,\nLạp lạp giai tân khổ.",
     "**(Verse 1)**\nCày lúa giữa trưa nắng,\nMồ hôi nhỏ xuống đất dưới gốc lúa.\nAi biết thức ăn trong mâm,\nHạt nào cũng đều vất vả."),

    ("Ngự Thú Khúc - Nuôi Thú", "Nuôi Thú.", "Animal sounds.",
     "**(Verse 1)**\n心意相通若比邻，\n驾鹤乘龙入青云。\n灵兽护主生死共，\n不负当年一片恩。",
     "**(Verse 1)**\nTâm ý tương thông nhược tỷ lân,\nGiá hạc thừa long nhập thanh vân.\nLinh thú hộ chủ sinh tử cộng,\nBất phụ đương niên nhất phiến ân.",
     "**(Verse 1)**\nTâm ý thông nhau như hàng xóm,\nCưỡi hạc cưỡi rồng vào mây xanh.\nLinh thú bảo vệ chủ sống chết có nhau,\nKhông phụ ơn nghĩa năm xưa."),

    ("Thực Thần Ca - Nấu Ăn", "Nấu Ăn.", "Cooking sounds.",
     "**(Verse 1)**\n五味调和百味香，\n珍馐美味入愁肠。\n人间烟火气最暖，\n一碗清汤解凄凉。",
     "**(Verse 1)**\nNgũ vị điều hòa bách vị hương,\nTrân tu mỹ vị nhập sầu tràng.\nNhân gian yên hỏa khí tối noãn,\nNhất oản thanh thang giải thê lương.",
     "**(Verse 1)**\nNăm vị điều hòa trăm vị thơm,\nMón ngon vật lạ vào ruột sầu.\nKhói lửa nhân gian ấm áp nhất,\nMột bát canh trong giải nỗi thê lương."),

    ("Kỳ Đạo - Đánh Cờ", "Đánh Cờ.", "Strategy, Quiet.",
     "**(Verse 1)**\n闲敲棋子落灯花，\n一局残棋对晚霞。\n世事如棋局局新，\n黑白之间定天涯。",
     "**(Verse 1)**\nNhàn xao kỳ tử lạc đăng hoa,\nNhất cục tàn kỳ đối vãn hà.\nThế sự như kỳ cục cục tân,\nHắc bạch chi gian định thiên nhai.",
     "**(Verse 1)**\nNhàn rỗi gõ quân cờ làm rụng hoa đèn,\nMột ván cờ tàn đối diện với ráng chiều.\nChuyện đời như cờ ván nào cũng mới,\nGiữa đen và trắng định đoạt chân trời."),

    ("Tửu Tiên Ca - Uống Rượu", "Uống Rượu.", "Drunken, Fun.",
     "**(Verse 1)**\n对酒当歌，人生几何！\n譬如朝露，去日苦多。\n慨当以慷，忧思难忘。\n何以解忧？唯有杜康。",
     "**(Verse 1)**\nĐối tửu đương ca, nhân sinh kỷ hà!\nThí như triêu lộ, khứ nhật khổ đa.\nKhái đương dĩ khảng, ưu tư nan vong.\nHà dĩ giải ưu? Duy hữu Đỗ Khang.",
     "**(Verse 1)**\nTrước rượu nên hát, đời người bao lâu!\nVí như sương sớm, ngày qua khổ nhiều.\nKhí khái hào phóng, lo âu khó quên.\nLấy gì giải sầu? Chỉ có rượu ngon."),

    ("Thư Hương - Đọc Sách", "Đọc Sách.", "Scholarly.",
     "**(Verse 1)**\n书中自有黄金屋，\n书中自有颜如玉。\n男儿欲遂平生志，\n五经勤向窗前读。",
     "**(Verse 1)**\nThư trung tự hữu hoàng kim ốc,\nThư trung tự hữu nhan như ngọc.\nNam nhi dục toại bình sinh chí,\nNgũ kinh cần hướng song tiền độc.",
     "**(Verse 1)**\nTrong sách tự có nhà vàng,\nTrong sách tự có người đẹp như ngọc.\nNam nhi muốn thỏa chí bình sinh,\nNăm kinh cần cù đọc trước cửa sổ.")
]

creatures_songs = [
    ("Long Ngâm - Rồng Thiêng", "Rồng.", "Epic, Roaring.",
     "**(Verse 1)**\n潜龙勿用，飞龙在天。\n亢龙有悔，见龙在田。\n云从龙，风从虎，\n圣人作而万物睹。",
     "**(Verse 1)**\nTiềm long vật dụng, phi long tại thiên.\nKháng long hữu hối, kiến long tại điền.\nVân tòng long, phong tòng hổ,\nThánh nhân tác nhi vạn vật đổ.",
     "**(Verse 1)**\nRồng ẩn chớ dùng, rồng bay trên trời.\nRồng lên cao quá có hối tiếc, rồng hiện ở ruộng.\nMây theo rồng, gió theo hổ,\nThánh nhân làm việc mà vạn vật ngước nhìn."),

    ("Phượng Vũ - Phượng Hoàng Lửa", "Phượng Hoàng.", "High pitch, Graceful.",
     "**(Verse 1)**\n凤凰涅槃，浴火重生。\n百鸟朝凤，和鸣锵锵。\n非梧桐不栖，\n非练实不食。",
     "**(Verse 1)**\nPhượng hoàng niết bàn, dục hỏa trùng sinh.\nBách điểu triều phụng, hòa minh thương thương.\nPhi ngô đồng bất thê,\nPhi luyện thực bất thực.",
     "**(Verse 1)**\nPhượng hoàng niết bàn, tắm lửa tái sinh.\nTrăm chim chầu phượng, hót vang lanh lảnh.\nKhông phải cây ngô đồng không đậu,\nKhông phải quả trúc không ăn."),

    ("Lân Chân - Kỳ Lân", "Kỳ Lân.", "Mystical.",
     "**(Verse 1)**\n麒麟踏祥云，\n人间现瑞气。\n仁兽不履生虫，\n不折生草。",
     "**(Verse 1)**\nKỳ lân đạp tường vân,\nNhân gian hiện thụy khí.\nNhân thú bất lý sinh trùng,\nBất chiết sinh thảo.",
     "**(Verse 1)**\nKỳ lân đạp mây lành,\nNhân gian hiện khí tốt.\nThú nhân từ không giẫm lên côn trùng sống,\nKhông bẻ gãy cỏ sống."),

    ("Quy Thọ - Rùa Thần", "Quy.", "Slow, Ancient.",
     "**(Verse 1)**\n神龟虽寿，犹有竟时。\n腾蛇乘雾，终为土灰。\n养怡之福，可得永年。",
     "**(Verse 1)**\nThần quy tuy thọ, do hữu cánh thời.\nĐằng xà thừa vụ, chung vi thổ khôi.\nDưỡng di chi phúc, khả đắc vĩnh niên.",
     "**(Verse 1)**\nRùa thần tuy sống lâu, vẫn có lúc chết.\nRắn bay cưỡi sương mù, cuối cùng thành tro đất.\nNuôi dưỡng niềm vui tinh thần, có thể được sống lâu."),

    ("Hổ Khiếu - Chúa Sơn Lâm", "Hổ.", "Roaring, Powerful.",
     "**(Verse 1)**\n虎啸风生，威震山林。\n百兽震惶，无敢不从。\n独步天涯，王者之风。",
     "**(Verse 1)**\nHổ khiếu phong sinh, uy chấn sơn lâm.\nBách thú chấn hoàng, vô cảm bất tòng.\nĐộc bộ thiên nhai, vương giả chi phong.",
     "**(Verse 1)**\nHổ gầm sinh gió, uy chấn núi rừng.\nTrăm thú sợ hãi, không dám không theo.\nMột mình đi khắp chân trời, phong thái vương giả."),

    ("Hạc Minh - Tiên Hạc", "Hạc.", "Flute, Elegant.",
     "**(Verse 1)**\n鹤鸣于九皋，\n声闻于天。\n松鹤延年，\n仙风道骨。",
     "**(Verse 1)**\nHạc minh ư cửu cao,\nThanh văn ư thiên.\nTùng hạc diên niên,\nTiên phong đạo cốt.",
     "**(Verse 1)**\nHạc kêu ở đầm sâu,\nTiếng nghe tận trời.\nTùng hạc sống lâu,\nPhong thái tiên cốt cách đạo."),

    ("Lang Hào - Sói Hoang", "Sói.", "Howling, Fast.",
     "**(Verse 1)**\n月夜狼嚎，群起攻之。\n忍辱负重，只为生存。\n孤独是我的伴侣，\n荒野是我的家园。",
     "**(Verse 1)**\nNguyệt dạ lang hào, quần khởi công chi.\nNhẫn nhục phụ trọng, chỉ vi sinh tồn.\nCô độc thị ngã đích bạn lữ,\nHoang dã thị ngã đích gia viên.",
     "**(Verse 1)**\nĐêm trăng sói hú, bầy đàn cùng tấn công.\nNhẫn nhục chịu đựng, chỉ vì sinh tồn.\nCô độc là bạn lữ của ta,\nHoang dã là gia đình của ta."),

    ("Xà Ảnh - Rắn Độc", "Rắn.", "Hissing, Sneaky.",
     "**(Verse 1)**\n打草惊蛇，杯弓蛇影。\n人心不足蛇吞象，\n世事难料祸福依。",
     "**(Verse 1)**\nĐả thảo kinh xà, bôi cung xà ảnh.\nNhân tâm bất túc xà thôn tượng,\nThế sự nan liệu họa phúc y.",
     "**(Verse 1)**\nĐánh cỏ động rắn, bóng cung trong chén ngỡ là rắn.\nLòng người không đáy rắn nuốt voi,\nChuyện đời khó đoán họa phúc nương nhau."),

    ("Điểu Ngữ - Chim Hót", "Chim.", "Chirping.",
     "**(Verse 1)**\n几处早莺争暖树，\n谁家新燕啄春泥。\n乱花渐欲迷人眼，\n浅草才能没马蹄。",
     "**(Verse 1)**\nKỷ xứ tảo oanh tranh noãn thụ,\nThùy gia tân yến trác xuân nê.\nLoạn hoa tiệm dục mê nhân nhãn,\nThiển thảo tài năng một mã đề.",
     "**(Verse 1)**\nMấy chỗ chim oanh sớm tranh cây ấm,\nNhà ai chim yến mới mổ bùn xuân.\nHoa nở rối loạn dần làm mê mắt người,\nCỏ non mới che lấp móng ngựa."),

    ("Ngư Du - Cá Bơi", "Cá.", "Water sounds.",
     "**(Verse 1)**\n鱼戏莲叶东，\n鱼戏莲叶西。\n鱼戏莲叶南，\n鱼戏莲叶北。",
     "**(Verse 1)**\nNgư hí liên diệp đông,\nNgư hí liên diệp tây.\nNgư hí liên diệp nam,\nNgư hí liên diệp bắc.",
     "**(Verse 1)**\nCá đùa lá sen phía đông,\nCá đùa lá sen phía tây.\nCá đùa lá sen phía nam,\nCá đùa lá sen phía bắc.")
]

with open("Đạo/Âm_Nhạc/Tuyển_Tập_Sinh_Hoạt.md", "w") as f:
    f.write("# TUYỂN TẬP ÂM NHẠC: SINH HOẠT & NGHỀ PHỤ\n\n")
    f.write("Tổng hợp 10 bài hát về đời sống tu hành và các nghề phụ.\n\n")
    for song in activities_songs:
        f.write(create_song_entry(*song))

with open("Đạo/Âm_Nhạc/Tuyển_Tập_Linh_Thú.md", "w") as f:
    f.write("# TUYỂN TẬP ÂM NHẠC: LINH THÚ & YÊU TỘC\n\n")
    f.write("Tổng hợp 10 bài hát về các loài linh thú và sinh vật huyền bí.\n\n")
    for song in creatures_songs:
        f.write(create_song_entry(*song))

print("Batch 4 created successfully.")
