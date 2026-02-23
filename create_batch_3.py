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

nature_songs = [
    ("Sơn Nhạc Tụng - Núi Cao Hùng Vĩ", "Núi.", "Majestic, Drums.",
     "**(Verse 1)**\n泰山岩岩，鲁邦所瞻。\n高山仰止，景行行止。\n巍巍乎高哉，\n镇压万古气如虹。",
     "**(Verse 1)**\nThái Sơn nham nham, Lỗ bang sở chiêm.\nCao sơn ngưỡng chỉ, cảnh hành hành chỉ.\nNguy nguy hồ cao tai,\nTrấn áp vạn cổ khí như hồng.",
     "**(Verse 1)**\nNúi Thái Sơn sừng sững, là nơi nước Lỗ ngước nhìn.\nNúi cao thì ngước nhìn, việc lớn thì làm theo.\nCao vời vợi thay,\nTrấn áp vạn cổ khí thế như cầu vồng."),

    ("Giang Hà Vịnh - Sông Dài Cuồn Cuộn", "Sông.", "Flowing, Guzheng.",
     "**(Verse 1)**\n黄河之水天上来，\n奔流到海不复回。\n大江东去浪淘尽，\n千古风流人物。",
     "**(Verse 1)**\nHoàng Hà chi thủy thiên thượng lai,\nBôn lưu đáo hải bất phục hồi.\nĐại giang đông khứ lãng đào tận,\nThiên cổ phong lưu nhân vật.",
     "**(Verse 1)**\nNước sông Hoàng Hà từ trên trời rơi xuống,\nChảy ra biển không quay trở lại.\nSông lớn chảy về đông cuốn trôi hết,\nNhững nhân vật phong lưu ngàn đời."),

    ("Lâm Hải U - Rừng Sâu Bí Ẩn", "Rừng.", "Birds, Flute.",
     "**(Verse 1)**\n空山新雨后，\n天气晚来秋。\n明月松间照，\n清泉石上流。",
     "**(Verse 1)**\nKhông sơn tân vũ hậu,\nThiên khí vãn lai thu.\nMinh nguyệt tùng gian chiếu,\nThanh tuyền thạch thượng lưu.",
     "**(Verse 1)**\nNúi vắng sau cơn mưa mới,\nTiết trời buổi tối chớm thu.\nTrăng sáng chiếu qua rừng tùng,\nSuối trong chảy trên đá."),

    ("Hải Dương Ca - Biển Cả Mênh Mông", "Biển.", "Waves, Vast.",
     "**(Verse 1)**\n海上生明月，\n天涯共此时。\n长风破浪会有时，\n直挂云帆济沧海。",
     "**(Verse 1)**\nHải thượng sinh minh nguyệt,\nThiên nhai cộng thử thời.\nTrường phong phá lãng hội hữu thời,\nTrực quải vân phàm tế thương hải.",
     "**(Verse 1)**\nTrăng sáng mọc trên biển,\nChân trời cùng chung lúc này.\nGió dài phá sóng sẽ có lúc,\nTreo thẳng buồm mây vượt biển xanh."),

    ("Vân Vụ Khúc - Mây Mù Ảo Ảnh", "Mây.", "Ethereal, Soft.",
     "**(Verse 1)**\n云深不知处，\n只在此山中。\n白云千载空悠悠，\n闲云野鹤自去留。",
     "**(Verse 1)**\nVân thâm bất tri xứ,\nChỉ tại thử sơn trung.\nBạch vân thiên tải không du du,\nNhàn vân dã hạc tự khứ lưu.",
     "**(Verse 1)**\nMây sâu không biết nơi nào,\nChỉ ở trong núi này.\nMây trắng ngàn năm trôi lững lờ,\nMây nhàn hạc hoang tự đi ở."),

    ("Nguyệt Quang Dao - Trăng Sáng Soi Đêm", "Trăng.", "Night, Quiet.",
     "**(Verse 1)**\n床前明月光，\n疑是地上霜。\n举头望明月，\n低头思故乡。",
     "**(Verse 1)**\nSàng tiền minh nguyệt quang,\nNghi thị địa thượng sương.\nCử đầu vọng minh nguyệt,\nĐê đầu tư cố hương.",
     "**(Verse 1)**\nÁnh trăng sáng trước giường,\nNgỡ là sương trên mặt đất.\nNgẩng đầu nhìn trăng sáng,\nCúi đầu nhớ cố hương."),

    ("Tinh Thần Biến - Sao Trời Lấp Lánh", "Sao.", "Twinkling sounds.",
     "**(Verse 1)**\n天接云涛连晓雾，\n星河欲转千帆舞。\n昨夜星辰昨夜风，\n画楼西畔桂堂东。",
     "**(Verse 1)**\nThiên tiếp vân đào liên hiểu vụ,\nTinh hà dục chuyển thiên phàm vũ.\nTạc dạ tinh thần tạc dạ phong,\nHọa lâu tây bạn quế đường đông.",
     "**(Verse 1)**\nTrời nối sóng mây liền sương sớm,\nSông Ngân muốn chuyển ngàn buồm múa.\nSao đêm qua gió đêm qua,\nBên tây lầu vẽ phía đông nhà quế."),

    ("Tuyết Vũ - Tuyết Rơi Trắng Xóa", "Tuyết.", "Cold, Slow.",
     "**(Verse 1)**\n北国风光，千里冰封，万里雪飘。\n孤舟蓑笠翁，\n独钓寒江雪。",
     "**(Verse 1)**\nBắc quốc phong quang, thiên lý băng phong, vạn lý tuyết phiêu.\nCô chu xoa lạp ông,\nĐộc điếu hàn giang tuyết.",
     "**(Verse 1)**\nPhong cảnh phương bắc, ngàn dặm đóng băng, vạn dặm tuyết bay.\nThuyền lẻ loi ông già đội nón lá áo tơi,\nCâu cá một mình trong tuyết trên sông lạnh."),

    ("Vũ Lâm Linh - Mưa Rơi Tí Tách", "Mưa.", "Rain sounds.",
     "**(Verse 1)**\n夜来风雨声，\n花落知多少。\n清明时节雨纷纷，\n路上行人欲断魂。",
     "**(Verse 1)**\nDạ lai phong vũ thanh,\nHoa lạc tri đa thiểu.\nThanh minh thời tiết vũ phân phân,\nLộ thượng hành nhân dục đoạn hồn.",
     "**(Verse 1)**\nĐêm nghe tiếng gió mưa,\nHoa rụng biết bao nhiêu.\nTiết thanh minh mưa lất phất,\nNgười đi trên đường buồn đứt ruột."),

    ("Sương Mù - Mù Khơi Che Lối", "Sương.", "Misty, Ambient.",
     "**(Verse 1)**\n月落乌啼霜满天，\n江枫渔火对愁眠。\n烟笼寒水月笼沙，\n夜泊秦淮近酒家。",
     "**(Verse 1)**\nNguyệt lạc ô đề sương mãn thiên,\nGiang phong ngư hỏa đối sầu miên.\nYên lung hàn thủy nguyệt lung sa,\nDạ bạc Tần Hoài cận tửu gia.",
     "**(Verse 1)**\nTrăng lặn quạ kêu sương đầy trời,\nCây phong bên sông đèn chài đối diện giấc ngủ sầu.\nKhói bao trùm nước lạnh trăng bao trùm cát,\nĐêm đậu thuyền bến Tần Hoài gần quán rượu.")
]

relations_songs = [
    ("Sư Đồ Tình - Ân Sư Như Phụ", "Sư Đồ.", "Respectful.",
     "**(Verse 1)**\n一日为师终身为父，\n教诲谆谆铭心骨。\n传道受业解惑时，\n白发苍苍泪模糊。",
     "**(Verse 1)**\nNhất nhật vi sư chung thân vi phụ,\nGiáo hối truân truân minh tâm cốt.\nTruyền đạo thụ nghiệp giải hoặc thời,\nBạch phát thương thương lệ mô hồ.",
     "**(Verse 1)**\nMột ngày làm thầy cả đời làm cha,\nLời dạy ân cần khắc ghi xương tủy.\nLúc truyền đạo dạy nghề giải đáp thắc mắc,\nTóc bạc trắng nước mắt nhạt nhòa."),

    ("Huynh Đệ Nghĩa - Đồng Sinh Cộng Tử", "Huynh Đệ.", "Brotherhood.",
     "**(Verse 1)**\n落地为兄弟，\n何必骨肉亲。\n岂曰无衣？\n与子同袍。",
     "**(Verse 1)**\nLạc địa vi huynh đệ,\nHà tất cốt nhục thân.\nKhởi viết vô y?\nDữ tử đồng bào.",
     "**(Verse 1)**\nSinh ra đã là anh em,\nCần gì phải ruột thịt.\nSao nói không có áo?\nCùng chung áo chiến bào với anh."),

    ("Đạo Lữ Duyên - Sắt Cầm Hảo Hợp", "Đạo Lữ.", "Romantic Duet.",
     "**(Verse 1)**\n在天愿作比翼鸟，\n在地愿为连理枝。\n两情若是久长时，\n又岂在朝朝暮暮。",
     "**(Verse 1)**\nTại thiên nguyện tác tỷ dực điểu,\nTại địa nguyện vi liên lý chi.\nLưỡng tình nhược thị cửu trường thời,\nHựu khởi tại triêu triêu mộ mộ.",
     "**(Verse 1)**\nTrên trời nguyện làm chim liền cánh,\nDưới đất nguyện làm cây liền cành.\nNếu tình yêu hai ta lâu dài,\nThì đâu cần phải bên nhau sớm tối."),

    ("Kẻ Thù Hận - Bất Đội Trời Chung", "Kẻ Thù.", "Intense, Dark.",
     "**(Verse 1)**\n此仇不报非君子，\n誓杀汝头祭亡魂。\n拔剑四顾心茫然，\n唯有鲜血洗乾坤。",
     "**(Verse 1)**\nThử cừu bất báo phi quân tử,\nThệ sát nhữ đầu tế vong hồn.\nBạt kiếm tứ cố tâm mang nhiên,\nDuy hữu tiên huyết tẩy càn khôn.",
     "**(Verse 1)**\nMối thù này không báo không phải quân tử,\nThề lấy đầu ngươi tế vong hồn.\nRút kiếm nhìn quanh lòng mờ mịt,\nChỉ có máu tươi rửa sạch trời đất."),

    ("Tri Kỷ Ca - Cao Sơn Lưu Thủy", "Tri Kỷ.", "Guqin, Gentle.",
     "**(Verse 1)**\n高山流水遇知音，\n伯牙子期情义深。\n摔琴谢知己，\n从此无古琴。",
     "**(Verse 1)**\nCao sơn lưu thủy ngộ tri âm,\nBá Nha Tử Kỳ tình nghĩa thâm.\nSuất cầm tạ tri kỷ,\nTòng thử vô cổ cầm.",
     "**(Verse 1)**\nNúi cao nước chảy gặp tri âm,\nBá Nha Tử Kỳ tình nghĩa sâu.\nĐập đàn tạ tri kỷ,\nTừ nay không còn đàn cổ cầm."),

    ("Cố Nhân Tình - Người Cũ Gặp Lại", "Cố Nhân.", "Nostalgic.",
     "**(Verse 1)**\n少小离家老大回，\n乡音无改鬓毛衰。\n儿童相见不相识，\n笑问客从何处来。",
     "**(Verse 1)**\nThiếu tiểu ly gia lão đại hồi,\nHương âm vô cải mấn mao suy.\nNhi đồng tương kiến bất tương thức,\nTiếu vấn khách tòng hà xứ lai.",
     "**(Verse 1)**\nNhỏ rời nhà đi già mới về,\nGiọng quê không đổi tóc đã bạc.\nTrẻ con gặp mặt không quen biết,\nCười hỏi khách từ đâu đến."),

    ("Phụ Mẫu Ân - Công Cha Nghĩa Mẹ", "Phụ Mẫu.", "Touching.",
     "**(Verse 1)**\n慈母手中线，\n游子身上衣。\n临行密密缝，\n意恐迟迟归。",
     "**(Verse 1)**\nTừ mẫu thủ trung tuyến,\nDu tử thân thượng y.\nLâm hành mật mật phùng,\nÝ khủng trì trì quy.",
     "**(Verse 1)**\nSợi chỉ trong tay mẹ hiền,\nChiếc áo trên người con đi xa.\nSắp đi may thật kỹ,\nSợ con chậm trở về."),

    ("Gia Tộc Vinh - Vinh Quang Gia Tộc", "Gia Tộc.", "Pride.",
     "**(Verse 1)**\n光宗耀祖在此举，\n莫让门楣蒙尘灰。\n子孙满堂皆豪杰，\n千秋万代永不衰。",
     "**(Verse 1)**\nQuang tông diệu tổ tại thử cử,\nMạc nhượng môn mi mông trần khôi.\nTử tôn mãn đường giai hào kiệt,\nThiên thu vạn đại vĩnh bất suy.",
     "**(Verse 1)**\nLàm rạng rỡ tổ tông ở hành động này,\nĐừng để cửa nhà phủ bụi tro.\nCon cháu đầy nhà đều là hào kiệt,\nNgàn thu muôn đời mãi không suy."),

    ("Tông Môn Nghĩa - Sống Chết Vì Tông", "Tông Môn.", "Unity.",
     "**(Verse 1)**\n生是宗门人，\n死是宗门鬼。\n誓死守山门，\n共存亡进退。",
     "**(Verse 1)**\nSinh thị tông môn nhân,\nTử thị tông môn quỷ.\nThệ tử thủ sơn môn,\nCộng tồn vong tiến thoái.",
     "**(Verse 1)**\nSống là người tông môn,\nChết là ma tông môn.\nThề chết giữ cửa núi,\nCùng tồn vong tiến lui."),

    ("Chúng Sinh Nguyện - Cứu Độ Thế Nhân", "Chúng Sinh.", "Compassion.",
     "**(Verse 1)**\n安得广厦千万间，\n大庇天下寒士俱欢颜。\n先天下之忧而忧，\n后天下之乐而乐。",
     "**(Verse 1)**\nAn đắc quảng hạ thiên vạn gian,\nĐại tý thiên hạ hàn sĩ câu hoan nhan.\nTiên thiên hạ chi ưu nhi ưu,\nHậu thiên hạ chi lạc nhi lạc.",
     "**(Verse 1)**\nLàm sao có được ngàn vạn gian nhà rộng,\nChe chở cho kẻ sĩ nghèo trong thiên hạ đều vui vẻ.\nLo trước cái lo của thiên hạ,\nVui sau cái vui của thiên hạ.")
]

with open("Đạo/Âm_Nhạc/Tuyển_Tập_Thiên_Nhiên.md", "w") as f:
    f.write("# TUYỂN TẬP ÂM NHẠC: THIÊN NHIÊN & ĐỊA DANH\n\n")
    f.write("Tổng hợp 10 bài hát ca ngợi vẻ đẹp hùng vĩ của thiên nhiên.\n\n")
    for song in nature_songs:
        f.write(create_song_entry(*song))

with open("Đạo/Âm_Nhạc/Tuyển_Tập_Nhân_Duyên.md", "w") as f:
    f.write("# TUYỂN TẬP ÂM NHẠC: NHÂN DUYÊN & TÌNH NGHĨA\n\n")
    f.write("Tổng hợp 10 bài hát về các mối quan hệ tình cảm trong tu chân giới.\n\n")
    for song in relations_songs:
        f.write(create_song_entry(*song))

print("Batch 3 created successfully.")
