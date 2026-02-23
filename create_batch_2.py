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

elements_songs = [
    ("Kim Chi Ca - Sắc Bén Vô Song", "Hành Kim - Sự cứng rắn, sắc bén.", "Metallic, Sharp sounds.",
     "**(Verse 1)**\n金戈铁马气如虹，\n百炼精钢化神锋。\n宁折不弯真君子，\n一剑光寒破苍穹。",
     "**(Verse 1)**\nKim qua thiết mã khí như hồng,\nBách luyện tinh cương hóa thần phong.\nNinh chiết bất loan chân quân tử,\nNhất kiếm quang hàn phá thương khung.",
     "**(Verse 1)**\nGiáo vàng ngựa sắt khí thế như cầu vồng,\nThép tinh luyện trăm lần hóa thành mũi nhọn thần.\nThà gãy chứ không cong mới là trang quân tử,\nMột đường kiếm ánh sáng lạnh lẽo phá vỡ bầu trời."),

    ("Mộc Chi Sinh - Vạn Vật Sinh Sôi", "Hành Mộc - Sự sống, sinh trưởng.", "Flute, Forest sounds.",
     "**(Verse 1)**\n枯木逢春发新枝，\n生生不息意绵迟。\n扎根大地汲甘露，\n直到参天化龙时。",
     "**(Verse 1)**\nKhô mộc phùng xuân phát tân chi,\nSinh sinh bất tức ý miên trì.\nTrát căn đại địa cấp cam lộ,\nTrực đáo tham thiên hóa long thời.",
     "**(Verse 1)**\nCây khô gặp mùa xuân nảy cành mới,\nSự sống không ngừng ý chí dằng dặc.\nCắm rễ vào lòng đất hút sương ngọt,\nCho đến khi chọc trời hóa rồng."),

    ("Thủy Chi Nhu - Thượng Thiện Nhược Thủy", "Hành Thủy - Sự mềm mại, linh hoạt.", "Water sounds, Guzheng.",
     "**(Verse 1)**\n上善若水利万物，\n不争无为是真途。\n刚柔并济随形变，\n滴水穿石意如初。",
     "**(Verse 1)**\nThượng thiện nhược thủy lợi vạn vật,\nBất tranh vô vi thị chân đồ.\nCương nhu tịnh tế tùy hình biến,\nTích thủy xuyên thạch ý như sơ.",
     "**(Verse 1)**\nCái tốt nhất giống như nước làm lợi cho vạn vật,\nKhông tranh giành vô vi mới là con đường thật.\nCứng mềm kết hợp tùy hình dáng mà thay đổi,\nNước chảy đá mòn ý chí như ban đầu."),

    ("Hỏa Chi Liệt - Nhiệt Huyết Bùng Cháy", "Hành Hỏa - Sự nhiệt huyết, hủy diệt.", "Fast Drums, Intense.",
     "**(Verse 1)**\n烈火燎原势难挡，\n焚尽世间不正方。\n丹心一片如红日，\n照耀千秋万古长。",
     "**(Verse 1)**\nLiệt hỏa liệu nguyên thế nan đáng,\nPhần tận thế gian bất chính phương.\nĐan tâm nhất phiến như hồng nhật,\nChiếu diệu thiên thu vạn cổ trường.",
     "**(Verse 1)**\nLửa mạnh đốt đồng thế khó ngăn cản,\nThiêu rụi những nơi bất chính trên thế gian.\nTấm lòng son sắt như mặt trời đỏ,\nChiếu sáng ngàn thu muôn đời."),

    ("Thổ Chi Hậu - Đức Dày Tải Vật", "Hành Thổ - Sự vững chãi, bao dung.", "Low Bass, Heavy.",
     "**(Verse 1)**\n地势坤君子厚德，\n载物无言默如默。\n万丈高楼平地起，\n不动如山镇妖魔。",
     "**(Verse 1)**\nĐịa thế khôn quân tử hậu đức,\nTải vật vô ngôn mặc như mặc.\nVạn trượng cao lâu bình địa khởi,\nBất động như sơn trấn yêu ma.",
     "**(Verse 1)**\nThế đất là quẻ Khôn người quân tử lấy đức dày,\nChở vạn vật không lời nào im lặng như tờ.\nLầu cao vạn trượng khởi từ đất bằng,\nKhông lay động như núi trấn áp yêu ma."),

    ("Phong Chi Tự - Tiêu Dao Tự Tại", "Hành Phong - Gió, tốc độ, tự do.", "Wind instruments, Fast.",
     "**(Verse 1)**\n风起云涌天地宽，\n扶摇直上九重天。\n来去无踪影无定，\n只留清气在人间。",
     "**(Verse 1)**\nPhong khởi vân dũng thiên địa khoan,\nPhù dao trực thượng cửu trùng thiên.\nLai khứ vô tung ảnh vô định,\nChỉ lưu thanh khí tại nhân gian.",
     "**(Verse 1)**\nGió nổi mây cuộn trời đất rộng,\nBay thẳng lên chín tầng trời.\nĐến đi không dấu vết bóng dáng không cố định,\nChỉ để lại khí thanh khiết ở nhân gian."),

    ("Lôi Chi Phạt - Thiên Phạt Hủy Diệt", "Hành Lôi - Sấm sét, sự trừng phạt.", "Thunder sounds, Electric Guitar.",
     "**(Verse 1)**\n雷霆万钧震苍穹，\n除魔卫道显威风。\n一念生灭皆由我，\n代天刑罚灭奸雄。",
     "**(Verse 1)**\nLôi đình vạn cân chấn thương khung,\nTrừ ma vệ đạo hiển uy phong.\nNhất niệm sinh diệt giai do ngã,\nĐại thiên hình phạt diệt gian hùng.",
     "**(Verse 1)**\nSấm sét vạn cân chấn động bầu trời,\nTrừ ma bảo vệ đạo hiển lộ uy phong.\nMột ý niệm sinh diệt đều do ta,\nThay trời thi hành hình phạt tiêu diệt kẻ gian hùng."),

    ("Băng Chi Lãnh - Hàn Băng Vạn Dặm", "Hành Băng - Lạnh lẽo, vô tình.", "Crystal sounds, High pitch.",
     "**(Verse 1)**\n千里冰封万里雪，\n寒梅傲骨独自绝。\n心如止水情已断，\n只为大道守清越。",
     "**(Verse 1)**\nThiên lý băng phong vạn lý tuyết,\nHàn mai ngạo cốt độc tự tuyệt.\nTâm như chỉ thủy tình dĩ đoạn,\nChỉ vi đại đạo thủ thanh việt.",
     "**(Verse 1)**\nNgàn dặm đóng băng vạn dặm tuyết,\nHoa mai lạnh lùng kiêu hãnh một mình tuyệt sắc.\nTâm như nước lặng tình đã dứt,\nChỉ vì đại đạo mà giữ sự trong trẻo."),

    ("Quang Chi Thánh - Ánh Sáng Hy Vọng", "Hành Quang - Ánh sáng, chữa lành.", "Choir, Uplifting.",
     "**(Verse 1)**\n光明普照驱黑暗，\n慈悲为怀度众生。\n心有明灯常不灭，\n照亮迷途指归程。",
     "**(Verse 1)**\nQuang minh phổ chiếu khu hắc ám,\nTừ bi vi hoài độ chúng sinh.\nTâm hữu minh đăng thường bất diệt,\nChiếu lượng mê đồ chỉ quy trình.",
     "**(Verse 1)**\nÁnh sáng chiếu khắp xua tan bóng tối,\nLấy lòng từ bi cứu độ chúng sinh.\nTrong tim có ngọn đèn sáng mãi không tắt,\nChiếu sáng con đường mê lầm chỉ lối về."),

    ("Ám Chi Ảnh - Bóng Tối Vĩnh Cửu", "Hành Ám - Bóng tối, ẩn nấp.", "Whispering, Dark Ambient.",
     "**(Verse 1)**\n黑夜降临万物藏，\n如影随形在身旁。\n光明背后即是暗，\n吞噬一切归洪荒。",
     "**(Verse 1)**\nHắc dạ giáng lâm vạn vật tàng,\nNhư ảnh tùy hình tại thân bàng.\nQuang minh bối hậu tức thị ám,\nThôn phệ nhất thiết quy hồng hoang.",
     "**(Verse 1)**\nĐêm đen buông xuống vạn vật ẩn nấp,\nNhư bóng với hình ở bên cạnh.\nPhía sau ánh sáng chính là bóng tối,\nNuốt chửng tất cả trở về thuở hồng hoang.")
]

emotions_songs = [
    ("Hỉ Lạc Ca - Niềm Vui", "Cảm xúc Vui vẻ.", "Happy, Upbeat.",
     "**(Verse 1)**\n春风得意马蹄疾，\n一日看尽长安花。\n人生得意须尽欢，\n莫使金樽空对月。",
     "**(Verse 1)**\nXuân phong đắc ý mã đề tật,\nNhất nhật khán tận Trường An hoa.\nNhân sinh đắc ý tu tận hoan,\nMạc sử kim tôn không đối nguyệt.",
     "**(Verse 1)**\nGió xuân đắc ý vó ngựa chạy nhanh,\nMột ngày ngắm hết hoa ở Trường An.\nĐời người đắc ý phải vui tận hưởng,\nĐừng để chén vàng trống không đối diện với trăng."),

    ("Nộ Hỏa Ca - Cơn Giận", "Cảm xúc Giận dữ.", "Intense, Fast.",
     "**(Verse 1)**\n怒发冲冠凭栏处，\n仰天长啸壮怀烈。\n三十功名尘与土，\n八千里路云和月。",
     "**(Verse 1)**\nNộ phát xung quan bằng lan xứ,\nNgưỡng thiên trường khiếu tráng hoài liệt.\nTam thập công danh trần dữ thổ,\nBát thiên lý lộ vân hòa nguyệt.",
     "**(Verse 1)**\nTóc dựng ngược vì giận dựa vào lan can,\nNgửa mặt lên trời hú dài nỗi lòng bi tráng.\nBa mươi năm công danh như bụi và đất,\nTám ngàn dặm đường mây và trăng."),

    ("Ai Thương Khúc - Nỗi Buồn", "Cảm xúc Bi thương.", "Sad Erhu.",
     "**(Verse 1)**\n十年生死两茫茫，\n不思量，自难忘。\n千里孤坟，无处话凄凉。",
     "**(Verse 1)**\nThập niên sinh tử lưỡng mang mang,\nBất tư lượng, tự nan vong.\nThiên lý cô phần, vô xứ thoại thê lương.",
     "**(Verse 1)**\nMười năm sống chết hai bên đều mênh mông,\nKhông cố nhớ, nhưng tự nhiên khó quên.\nNgàn dặm nấm mộ cô đơn, không nơi nào kể nỗi thê lương."),

    ("Ái Tình Dao - Tình Yêu", "Cảm xúc Yêu đương.", "Romantic, Piano.",
     "**(Verse 1)**\n死生契阔，与子成说。\n执子之手，与子偕老。\n关关雎鸠，在河之洲。\n窈窕淑女，君子好逑。",
     "**(Verse 1)**\nTử sinh khế khoát, dữ tử thành thuyết.\nChấp tử chi thủ, dữ tử giai lão.\nQuan quan thư cưu, tại hà chi châu.\nYểu điệu thục nữ, quân tử hảo cầu.",
     "**(Verse 1)**\nSống chết khổ cực, cùng người thề hẹn.\nNắm lấy tay người, cùng người già đi.\nQuan quan tiếng chim thư cưu, ở bãi sông.\nCô gái yểu điệu thục nữ, người quân tử mong cầu."),

    ("Ố Hận Ca - Sự Ghét Bỏ", "Cảm xúc Ghét/Thù hận.", "Dark, Minor key.",
     "**(Verse 1)**\n此时相望不相闻，\n愿逐月华流照君。\n恨君不似江楼月，\n南北东西，南北东西。",
     "**(Verse 1)**\nThử thời tương vọng bất tương văn,\nNguyện trục nguyệt hoa lưu chiếu quân.\nHận quân bất tự giang lâu nguyệt,\nNam bắc đông tây, nam bắc đông tây.",
     "**(Verse 1)**\nLúc này nhìn nhau mà không nghe thấy nhau,\nNguyện đuổi theo ánh trăng chiếu rọi chàng.\nHận chàng không giống như trăng trên lầu sông,\nNam bắc đông tây (lúc nào cũng có nhau)."),

    ("Tâm Ma Chú - Sự Ám Ảnh", "Tâm Ma.", "Whispering, Scary.",
     "**(Verse 1)**\n心魔生暗鬼，\n夜半叩柴扉。\n欲念如野草，\n春风吹又生。",
     "**(Verse 1)**\nTâm ma sinh ám quỷ,\nDạ bán khấu sài phi.\nDục niệm như dã thảo,\nXuân phong xuy hựu sinh.",
     "**(Verse 1)**\nTâm ma sinh ra quỷ ám,\nNửa đêm gõ cửa gỗ.\nDục vọng như cỏ dại,\nGió xuân thổi lại mọc."),

    ("Cô Độc Hành - Sự Cô Đơn", "Cô Độc.", "Solo Flute.",
     "**(Verse 1)**\n独坐幽篁里，\n弹琴复长啸。\n深林人不知，\n明月来相照。",
     "**(Verse 1)**\nĐộc tọa u hoàng lý,\nĐàn cầm phục trường khiếu.\nThâm lâm nhân bất tri,\nMinh nguyệt lai tương chiếu.",
     "**(Verse 1)**\nNgồi một mình trong bụi tre tối,\nGảy đàn rồi lại hú dài.\nRừng sâu người không biết,\nTrăng sáng đến chiếu soi."),

    ("Ngộ Đạo Ca - Sự Giác Ngộ", "Giác Ngộ.", "Bells, Clear.",
     "**(Verse 1)**\n本来无一物，\n何处惹尘埃。\n明心见性后，\n方知我是谁。",
     "**(Verse 1)**\nBản lai vô nhất vật,\nHà xứ nhạ trần ai.\nMinh tâm kiến tính hậu,\nPhương tri ngã thị thùy.",
     "**(Verse 1)**\nVốn dĩ không có vật gì,\nNơi nào bám bụi trần.\nSau khi sáng lòng thấy tính,\nMới biết ta là ai."),

    ("Điên Cuồng Khúc - Sự Điên Loạn", "Điên Cuồng.", "Chaotic, Fast.",
     "**(Verse 1)**\n他人笑我太疯癫，\n我笑他人看不穿。\n不见五陵豪杰墓，\n无花无酒锄作田。",
     "**(Verse 1)**\nTha nhân tiếu ngã thái phong điên,\nNgã tiếu tha nhân khán bất xuyên.\nBất kiến Ngũ Lăng hào kiệt mộ,\nVô hoa vô tửu sô tác điền.",
     "**(Verse 1)**\nNgười khác cười ta quá điên khùng,\nTa cười người khác nhìn không thấu.\nKhông thấy mộ của hào kiệt ở Ngũ Lăng sao,\nKhông hoa không rượu bị cày thành ruộng."),

    ("Tĩnh Lặng Ca - Sự Bình Yên", "Bình Yên.", "Silence, Soft sounds.",
     "**(Verse 1)**\n人闲桂花落，\n夜静春山空。\n月出惊山鸟，\n时鸣春涧中。",
     "**(Verse 1)**\nNhân nhàn quế hoa lạc,\nDạ tĩnh xuân sơn không.\nNguyệt xuất kinh sơn điểu,\nThời minh xuân giản trung.",
     "**(Verse 1)**\nNgười nhàn rỗi hoa quế rơi,\nĐêm yên tĩnh núi xuân vắng lặng.\nTrăng lên làm kinh động chim núi,\nThỉnh thoảng hót trong khe suối xuân.")
]

with open("Đạo/Âm_Nhạc/Tuyển_Tập_Ngũ_Hành.md", "w") as f:
    f.write("# TUYỂN TẬP ÂM NHẠC: NGŨ HÀNH & NGUYÊN TỐ\n\n")
    f.write("Tổng hợp 10 bài hát về các nguyên tố tự nhiên và sức mạnh của chúng.\n\n")
    for song in elements_songs:
        f.write(create_song_entry(*song))

with open("Đạo/Âm_Nhạc/Tuyển_Tập_Cảm_Xúc.md", "w") as f:
    f.write("# TUYỂN TẬP ÂM NHẠC: CẢM XÚC & TÂM MA\n\n")
    f.write("Tổng hợp 10 bài hát về hỉ nộ ái ố và các trạng thái tâm lý của tu sĩ.\n\n")
    for song in emotions_songs:
        f.write(create_song_entry(*song))

print("Batch 2 created successfully.")
