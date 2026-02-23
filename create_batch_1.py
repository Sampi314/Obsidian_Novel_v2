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

realms_songs = [
    ("Luyện Khí Ca - Khởi Đầu Gian Nan", "Bước đầu tiên của tu hành, cảm nhận linh khí.", "Traditional Chinese, Flute intro, Peaceful.",
     """**(Verse 1)**\n引气入体洗凡尘，\n百窍通达始为真。\n吐纳天地浩然气，\n从此不再是凡人。\n\n**(Chorus)**\n炼气九层路漫漫，\n一步一印如登山。\n心如止水观自在，\n大道初成在此间。""",
     """**(Verse 1)**\nDẫn khí nhập thể tẩy phàm trần,\nBách khiếu thông đạt thủy vi chân.\nThổ nạp thiên địa hạo nhiên khí,\nTòng thử bất tái thị phàm nhân.\n\n**(Chorus)**\nLuyện khí cửu tầng lộ mạn mạn,\nNhất bộ nhất ấn như đăng sơn.\nTâm như chỉ thủy quán tự tại,\nĐại đạo sơ thành tại thử gian.""",
     """**(Verse 1)**\nDẫn khí vào cơ thể rửa sạch bụi trần,\nTrăm huyệt đạo thông suốt mới là thật.\nHít thở khí hạo nhiên của trời đất,\nTừ nay không còn là người phàm nữa.\n\n**(Chorus)**\nLuyện khí chín tầng đường dài dằng dặc,\nMột bước một dấu chân như leo núi.\nTâm như nước lặng quan sát sự tự tại,\nĐại đạo ban đầu hình thành ở nơi này."""),

    ("Trúc Cơ Ngâm - Xây Dựng Đạo Cơ", "Xây dựng nền móng vững chắc cho đại đạo.", "Orchestral build up, Guzheng, Determined.",
     """**(Verse 1)**\n百日筑基非等闲，\n精气神足汇丹田。\n铸就无上大道基，\n从此仙凡两重天。\n\n**(Chorus)**\n筑基不易毁基难，\n万丈高楼平地起。\n风雨不动安如山，\n他日飞升由此始。""",
     """**(Verse 1)**\nBách nhật trúc cơ phi đẳng nhàn,\nTinh khí thần túc hối đan điền.\nChú tựu vô thượng đại đạo cơ,\nTòng thử tiên phàm lưỡng trùng thiên.\n\n**(Chorus)**\nTrúc cơ bất dị hủy cơ nan,\nVạn trượng cao lâu bình địa khởi.\nPhong vũ bất động an như sơn,\nTha nhật phi thăng do thử thủy.""",
     """**(Verse 1)**\nTrăm ngày trúc cơ không phải chuyện thường,\nTinh khí thần đầy đủ tụ về đan điền.\nĐúc nên nền móng đại đạo vô thượng,\nTừ nay tiên và phàm là hai phương trời.\n\n**(Chorus)**\nTrúc cơ không dễ phá hủy càng khó,\nLầu cao vạn trượng khởi từ đất bằng.\nGió mưa không lay động vững như núi,\nNgày sau phi thăng bắt đầu từ đây."""),

    ("Kim Đan Khúc - Một Hạt Kim Đan", "Kết đan, sự chuyển hóa chất lượng linh lực.", "Epic, Drums, Powerful vocals.",
     """**(Verse 1)**\n一颗金丹吞入腹，\n我命由我不由天。\n碎丹成婴需九转，\n历尽劫波始成仙。\n\n**(Chorus)**\n金丹灿烂照紫府，\n寿元千载乐无边。\n纵横四海任遨游，\n不论沧海与桑田。""",
     """**(Verse 1)**\nNhất khỏa kim đan thôn nhập phúc,\nNgã mệnh do ngã bất do thiên.\nToái đan thành anh nhu cửu chuyển,\nLịch tận kiếp ba thủy thành tiên.\n\n**(Chorus)**\nKim đan xán lạn chiếu tử phủ,\nThọ nguyên thiên tải lạc vô biên.\nTung hoành tứ hải nhậm ngao du,\nBất luận thương hải dữ tang điền.""",
     """**(Verse 1)**\nMột viên kim đan nuốt vào bụng,\nMệnh ta do ta không do trời.\nVỡ đan thành anh cần chín lần chuyển hóa,\nTrải hết sóng gió kiếp nạn mới thành tiên.\n\n**(Chorus)**\nKim đan rực rỡ chiếu sáng tử phủ,\nTuổi thọ ngàn năm vui sướng vô biên.\nTung hoành bốn biển mặc sức dạo chơi,\nChẳng màng biển xanh hóa nương dâu."""),

    ("Nguyên Anh Ca - Phá Kén Hóa Bướm", "Nguyên Anh xuất thế, thần thức ly thể.", "Ethereal, High pitched flute, Mystical.",
     """**(Verse 1)**\n破壳而出显真容，\n元婴离体驾长风。\n瞬息千里游太虚，\n方知天地在心中。\n\n**(Chorus)**\n元婴不死身不灭，\n夺舍重生逆苍穹。\n三花聚顶五气朝，\n逍遥自在乐无穷。""",
     """**(Verse 1)**\nPhá xác nhi xuất hiển chân dung,\nNguyên anh ly thể giá trường phong.\nThuấn tức thiên lý du thái hư,\nPhương tri thiên địa tại tâm trung.\n\n**(Chorus)**\nNguyên anh bất tử thân bất diệt,\nĐoạt xá trùng sinh nghịch thương khung.\nTam hoa tụ đỉnh ngũ khí triều,\nTiêu dao tự tại lạc vô cùng.""",
     """**(Verse 1)**\nPhá vỏ chui ra hiện chân dung,\nNguyên anh rời khỏi cơ thể cưỡi gió dài.\nTrong nháy mắt đi ngàn dặm dạo chơi thái hư,\nMới biết trời đất nằm trong tim.\n\n**(Chorus)**\nNguyên anh không chết thân xác không diệt,\nĐoạt xác sống lại nghịch cả bầu trời.\nBa hoa tụ trên đỉnh đầu năm khí chầu về,\nTiêu dao tự tại vui sướng vô cùng."""),

    ("Hóa Thần Điệu - Thần Du Thái Hư", "Hóa Thần cảnh, dung hợp thiên địa.", "Deep, Ambient, Choir, Slow.",
     """**(Verse 1)**\n化神虚空悟真谛，\n天地与我共虽一。\n举手投足引天象，\n翻云覆雨念动希。\n\n**(Chorus)**\n神游太虚观万界，\n星辰陨落如尘泥。\n不问世间恩怨事，\n只求大道更相依。""",
     """**(Verse 1)**\nHóa thần hư không ngộ chân đế,\nThiên địa dữ ngã cộng tuy nhất.\nCử thủ đầu túc dẫn thiên tượng,\nPhiên vân phúc vũ niệm động hy.\n\n**(Chorus)**\nThần du thái hư quan vạn giới,\nTinh thần vẫn lạc như trần nê.\nBất vấn thế gian ân oán sự,\nChỉ cầu đại đạo canh tương y.""",
     """**(Verse 1)**\nHóa thần vào hư không ngộ ra chân lý,\nTrời đất với ta tuy hai mà một.\nGiơ tay nhấc chân dẫn động thiên tượng,\nLật mây che mưa chỉ cần ý niệm khẽ động.\n\n**(Chorus)**\nThần dạo chơi thái hư quan sát vạn giới,\nSao trời rơi rụng như bụi đất.\nKhông hỏi chuyện ân oán thế gian,\nChỉ cầu đại đạo càng thêm gắn bó."""),

    ("Luyện Hư Khúc - Phản Hư Quy Chân", "Luyện Hư cảnh, nhìn thấu hư thực.", "Mysterious, Bells, Whispering vocals.",
     """**(Verse 1)**\n炼虚合道返本源，\n看破红尘是与非。\n虚实之间随心变，\n万法皆空亦皆悲。\n\n**(Chorus)**\n虚怀若谷容天地，\n无牵无挂自清规。\n此时方觉修真苦，\n高处不胜寒风吹。""",
     """**(Verse 1)**\nLuyện hư hợp đạo phản bản nguyên,\nKhán phá hồng trần thị dữ phi.\nHư thực chi gian tùy tâm biến,\nVạn pháp giai không diệc giai bi.\n\n**(Chorus)**\nHư hoài nhược cốc dung thiên địa,\nVô khiên vô quải tự thanh quy.\nThử thời phương giác tu chân khổ,\nCao xứ bất thắng hàn phong xuy.""",
     """**(Verse 1)**\nLuyện hư hợp đạo trở về nguồn gốc,\nNhìn thấu đúng sai chốn hồng trần.\nGiữa hư và thực tùy tâm biến hóa,\nVạn pháp đều là không cũng đều là bi thương.\n\n**(Chorus)**\nLòng trống như hang núi chứa cả trời đất,\nKhông vướng bận tự có quy tắc trong sạch.\nLúc này mới thấy tu chân khổ,\nỞ nơi cao không chịu nổi gió lạnh thổi."""),

    ("Hợp Thể Ca - Thân Hợp Thiên Địa", "Hợp Thể cảnh, sức mạnh vô song.", "Grand, Orchestral, Powerful.",
     """**(Verse 1)**\n身与道合力无穷，\n拳破虚空震苍穹。\n法相天地高达丈，\n吼声如雷贯长虹。\n\n**(Chorus)**\n合体期成半步仙，\n纵横寰宇任西东。\n哪怕天劫终须渡，\n亦要笑着对天冲。""",
     """**(Verse 1)**\nThân dữ đạo hợp lực vô cùng,\nQuyền phá hư không chấn thương khung.\nPháp tướng thiên địa cao đạt trượng,\nHống thanh như lôi quán trường hồng.\n\n**(Chorus)**\nHợp thể kỳ thành bán bộ tiên,\nTung hoành hoàn vũ nhậm tây đông.\nNả phạ thiên kiếp chung tu độ,\nDiệc yếu tiếu trước đối thiên xung.""",
     """**(Verse 1)**\nThân thể và đạo hợp nhất sức mạnh vô cùng,\nNắm đấm phá vỡ hư không chấn động bầu trời.\nPháp tướng thiên địa cao ngàn trượng,\nTiếng gầm như sấm xuyên qua cầu vồng.\n\n**(Chorus)**\nKỳ Hợp Thể thành tựu đã là nửa bước tiên,\nTung hoành vũ trụ mặc sức đông tây.\nDù cho thiên kiếp cuối cùng phải vượt qua,\nCũng phải cười mà lao thẳng lên trời."""),

    ("Đại Thừa Hành - Tiêu Dao Cửu Thiên", "Đại Thừa cảnh, chuẩn bị phi thăng.", "Majestic, Guzheng solo, Serene.",
     """**(Verse 1)**\n大乘圆满近仙乡，\n只待天门开金光。\n洗尽凡胎换仙骨，\n从此长生伴君旁。\n\n**(Chorus)**\n回首凡尘多少事，\n一笑置之泪两行。\n大乘之道在于舍，\n舍得红尘得仙方。""",
     """**(Verse 1)**\nĐại thừa viên mãn cận tiên hương,\nChỉ đãi thiên môn khai kim quang.\nTẩy tận phàm thai hoán tiên cốt,\nTòng thử trường sinh bạn quân bàng.\n\n**(Chorus)**\nHồi thủ phàm trần đa thiểu sự,\nNhất tiếu trí chi lệ lưỡng hàng.\nĐại thừa chi đạo tại ư xả,\nXả đắc hồng trần đắc tiên phương.""",
     """**(Verse 1)**\nĐại thừa viên mãn gần quê hương của tiên,\nChỉ đợi cửa trời mở ra ánh sáng vàng.\nRửa sạch thai phàm đổi lấy cốt tiên,\nTừ nay trường sinh ở bên cạnh người.\n\n**(Chorus)**\nNgoảnh đầu nhìn lại biết bao chuyện phàm trần,\nCười một cái cho qua mà nước mắt hai hàng.\nĐạo của Đại Thừa nằm ở chỗ buông bỏ,\nBuông bỏ được hồng trần mới đắc được phương thuốc tiên."""),

    ("Độ Kiếp Nan - Sinh Tử Nhất Tuyến", "Độ kiếp phi thăng, hiểm nguy trùng trùng.", "Intense, Fast paced, Thunder sounds.",
     """**(Verse 1)**\n九重天劫落九天，\n雷霆万钧毁山川。\n生死由命不由己，\n只争一线在当前。\n\n**(Chorus)**\n渡得过时成真仙，\n渡不过时化灰烟。\n古往今来多少客，\n尽皆折戟在雷边。""",
     """**(Verse 1)**\nCửu trùng thiên kiếp lạc cửu thiên,\nLôi đình vạn cân hủy sơn xuyên.\nSinh tử do mệnh bất do kỷ,\nChỉ tranh nhất tuyến tại đương tiền.\n\n**(Chorus)**\nĐộ đắc quá thời thành chân tiên,\nĐộ bất quá thời hóa khôi yên.\nCổ vãng kim lai đa thiểu khách,\nTận giai chiết kích tại lôi biên.""",
     """**(Verse 1)**\nChín tầng thiên kiếp rơi từ chín tầng trời,\nSấm sét vạn cân phá hủy núi sông.\nSống chết do mệnh không do mình,\nChỉ tranh giành một tia hy vọng trước mắt.\n\n**(Chorus)**\nVượt qua được thì thành chân tiên,\nKhông vượt qua được thì hóa thành tro khói.\nXưa nay biết bao nhiêu vị khách,\nĐều gãy vũ khí bên cạnh tia sét."""),

    ("Tu Tiên Lộ - Tổng Kết", "Tổng kết con đường tu tiên.", "Orchestral, Inspiring.",
     """**(Verse 1)**\n修仙路漫漫其修远兮，\n吾将上下而求索。\n从练气到渡劫期，\n步步惊心步步奇。\n\n**(Chorus)**\n不求闻达于诸侯，\n只求长生傲九州。\n大道三千任我取，\n一剑光寒十九秋。""",
     """**(Verse 1)**\nTu tiên lộ mạn mạn kỳ tu viễn hê,\nNgô tương thượng hạ nhi cầu sách.\nTòng luyện khí đáo độ kiếp kỳ,\nBộ bộ kinh tâm bộ bộ kỳ.\n\n**(Chorus)**\nBất cầu văn đạt ư chư hầu,\nChỉ cầu trường sinh ngạo cửu châu.\nĐại đạo tam thiên nhậm ngã thủ,\nNhất kiếm quang hàn thập cửu thu.""",
     """**(Verse 1)**\nCon đường tu tiên dài đằng đẵng và xa xôi,\nTa sẽ tìm kiếm khắp trên dưới.\nTừ Luyện Khí đến kỳ Độ Kiếp,\nBước nào cũng giật mình bước nào cũng kỳ lạ.\n\n**(Chorus)**\nKhông cầu nổi tiếng với các chư hầu,\nChỉ cầu trường sinh ngạo nghễ chín châu.\nBa ngàn đại đạo mặc sức ta lấy,\nMột thanh kiếm sáng lạnh mười chín mùa thu.""")
]

weapons_songs = [
    ("Kiếm Đạo Ca - Vua Của Trăm Binh", "Ca ngợi Kiếm.", "Rock, Fast Guitar.",
     """**(Verse 1)**\n百兵之君是为剑，\n双刃开锋斩敌顽。\n刚柔并济藏锋锐，\n君子如玉剑如兰。""",
     """**(Verse 1)**\nBách binh chi quân thị vi kiếm,\nSong nhận khai phong trảm địch ngoan.\nCương nhu tịnh tế tàng phong nhuệ,\nQuân tử như ngọc kiếm như lan.""",
     """**(Verse 1)**\nVua của trăm loại binh khí chính là kiếm,\nHai lưỡi mở ra chém kẻ địch ngoan cố.\nCứng mềm kết hợp giấu đi mũi nhọn,\nNgười quân tử như ngọc, kiếm như hoa lan."""),

    ("Đao Pháp Ca - Bá Khí Tuyệt Luân", "Ca ngợi Đao.", "Heavy Metal, Drums.",
     """**(Verse 1)**\n刀如猛虎下山林，\n力劈华山鬼神惊。\n一往无前无退路，\n霸气冲天震古今。""",
     """**(Verse 1)**\nĐao như mãnh hổ hạ sơn lâm,\nLực phách Hoa Sơn quỷ thần kinh.\nNhất vãng vô tiền vô thoái lộ,\nBá khí xung thiên chấn cổ kim.""",
     """**(Verse 1)**\nĐao như hổ dữ xuống rừng núi,\nSức chém vỡ núi Hoa Sơn khiến quỷ thần kinh sợ.\nMột đi không trở lại không có đường lui,\nKhí thế bá đạo xung thiên chấn động xưa nay."""),

    ("Thương Hồn Khúc - Nhất Thương Phá Vạn Pháp", "Ca ngợi Thương.", "Orchestral, Trumpets.",
     """**(Verse 1)**\n一点寒芒先到，\n随后枪出如龙。\n长坂坡前谁敢挡，\n百万军中任纵横。""",
     """**(Verse 1)**\nNhất điểm hàn mang tiên đáo,\nTùy hậu thương xuất như long.\nTrường Bản pha tiền thùy cảm đáng,\nBách vạn quân trung nhậm tung hoành.""",
     """**(Verse 1)**\nMột điểm sáng lạnh đến trước,\nSau đó thương đâm ra như rồng.\nTrước dốc Trường Bản ai dám cản,\nGiữa trăm vạn quân mặc sức tung hoành."""),

    ("Cung Tiễn Hành - Bách Bộ Xuyên Dương", "Ca ngợi Cung.", "Folk, Rapid Plucking.",
     """**(Verse 1)**\n挽弓当挽强，\n用箭当用长。\n射人先射马，\n擒贼先擒王。""",
     """**(Verse 1)**\nVãn cung đương vãn cường,\nDụng tiễn đương dụng trường.\nXạ nhân tiên xạ mã,\nCầm tặc tiên cầm vương.""",
     """**(Verse 1)**\nKéo cung phải kéo cung mạnh,\nDùng tên phải dùng tên dài.\nBắn người trước hết bắn ngựa,\nBắt giặc trước hết bắt vua."""),

    ("Phiến Vũ - Quạt Giấy Phong Lưu", "Ca ngợi Quạt.", "Elegant, Flute.",
     """**(Verse 1)**\n羽扇纶巾笑谈间，\n强虏灰飞烟灭。\n看似风流藏杀机，\n一点朱唇染碧血。""",
     """**(Verse 1)**\nVũ phiến luân khăn tiếu đàm gian,\nCường lỗ khôi phi yên diệt.\nKhán tự phong lưu tàng sát cơ,\nNhất điểm chu môi nhiễm bích huyết.""",
     """**(Verse 1)**\nTay cầm quạt lông khăn buộc đầu cười nói,\nKẻ địch mạnh tan thành tro bụi.\nNhìn như phong lưu nhưng giấu sát cơ,\nMột điểm son môi nhuộm máu xanh."""),

    ("Cầm Âm Sát - Đàn Tranh Đoạt Mệnh", "Ca ngợi Đàn (Vũ khí).", "Guzheng, Fast.",
     """**(Verse 1)**\n一曲肝肠断，\n天涯何处觅知音。\n弦弦掩抑声声思，\n音波化刃斩鬼神。""",
     """**(Verse 1)**\nNhất khúc can tràng đoạn,\nThiên nhai hà xứ mịch tri âm.\nHuyền huyền yểm ức thanh thanh tư,\nÂm ba hóa nhận trảm quỷ thần.""",
     """**(Verse 1)**\nMột khúc đàn làm đứt ruột gan,\nChân trời góc bể tìm đâu ra tri âm.\nDây dây che giấu tiếng tiếng tư lự,\nSóng âm hóa thành lưỡi dao chém quỷ thần."""),

    ("Bút Nghiên Ca - Văn Khí Hóa Hình", "Ca ngợi Bút.", "Scholarly, Slow.",
     """**(Verse 1)**\n笔落惊风雨，\n诗成泣鬼神。\n挥毫泼墨画江山，\n点石成金化为真。""",
     """**(Verse 1)**\nBút lạc kinh phong vũ,\nThi thành khấp quỷ thần.\nHuy hào bát mặc họa giang sơn,\nĐiểm thạch thành kim hóa vi chân.""",
     """**(Verse 1)**\nHạ bút làm kinh động gió mưa,\nThơ thành khiến quỷ thần phải khóc.\nVung bút vẩy mực vẽ nên giang sơn,\nChấm đá thành vàng hóa thành sự thật."""),

    ("Chùy Pháp - Sức Mạnh Ngàn Cân", "Ca ngợi Chùy/Búa.", "Heavy Percussion.",
     """**(Verse 1)**\n双锤舞动风雷吼，\n一力降十会无穷。\n不管前方何阻挡，\n以此身躯破苍穹。""",
     """**(Verse 1)**\nSong chùy vũ động phong lôi hống,\nNhất lực hàng thập hội vô cùng.\nBất quản tiền phương hà trở đáng,\nDĩ thử thân khu phá thương khung.""",
     """**(Verse 1)**\nHai cây búa múa lên gió sấm gầm thét,\nMột sức mạnh hàng phục mười kẻ biết võ công.\nBất kể phía trước có gì ngăn cản,\nDùng thân xác này phá vỡ bầu trời."""),

    ("Tiên Sách - Roi Thần", "Ca ngợi Roi.", "Whip sounds, Fast.",
     """**(Verse 1)**\n长鞭一甩响云霄，\n软硬兼施意逍遥。\n缚龙困虎由心意，\n哪怕神魔也求饶。""",
     """**(Verse 1)**\nTrường tiên nhất súy hưởng vân tiêu,\nNhuyễn ngạnh kiêm thi ý tiêu dao.\nPhược long khốn hổ do tâm ý,\nNả phạ thần ma dã cầu nhiêu.""",
     """**(Verse 1)**\nRoi dài quất một cái vang tận mây xanh,\nMềm cứng thi rốt ý chí tiêu dao.\nTrói rồng nhốt hổ tùy theo ý muốn,\nDù là thần ma cũng phải xin tha."""),

    ("Đỉnh Lô - Luyện Hóa Thiên Địa", "Ca ngợi Đỉnh/Lò.", "Mystical, Low tones.",
     """**(Verse 1)**\n乾坤为鼎火为柴，\n炼化万物在怀胎。\n吞天噬地无穷尽，\n造化神奇任我裁。""",
     """**(Verse 1)**\nCàn khôn vi đỉnh hỏa vi sài,\nLuyện hóa vạn vật tại hoài thai.\nThôn thiên phệ địa vô cùng tận,\nTạo hóa thần kỳ nhậm ngã tài.""",
     """**(Verse 1)**\nLấy trời đất làm đỉnh lấy lửa làm củi,\nLuyện hóa vạn vật như đang mang thai.\nNuốt trời ăn đất không cùng tận,\nTạo hóa thần kỳ mặc sức ta cắt đặt.""")
]

with open("Đạo/Âm_Nhạc/Tuyển_Tập_Cảnh_Giới.md", "w") as f:
    f.write("# TUYỂN TẬP ÂM NHẠC: CẢNH GIỚI TU LUYỆN\n\n")
    f.write("Tổng hợp 10 bài hát tương ứng với các cảnh giới tu luyện và quá trình cầu đạo.\n\n")
    for song in realms_songs:
        f.write(create_song_entry(*song))

with open("Đạo/Âm_Nhạc/Tuyển_Tập_Binh_Khí.md", "w") as f:
    f.write("# TUYỂN TẬP ÂM NHẠC: BINH KHÍ VÀ PHÁP BẢO\n\n")
    f.write("Tổng hợp 10 bài hát ca ngợi các loại binh khí trong tu chân giới.\n\n")
    for song in weapons_songs:
        f.write(create_song_entry(*song))

print("Batch 1 created successfully.")
