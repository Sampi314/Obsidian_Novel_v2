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

seasons_songs = [
    ("Xuân Phong - Gió Xuân Ấm Áp", "Mùa Xuân.", "Lively, Birds.",
     "**(Verse 1)**\n春眠不觉晓，\n处处闻啼鸟。\n夜来风雨声，\n花落知多少。",
     "**(Verse 1)**\nXuân miên bất giác hiểu,\nXứ xứ văn đề điểu.\nDạ lai phong vũ thanh,\nHoa lạc tri đa thiểu.",
     "**(Verse 1)**\nGiấc ngủ xuân không biết trời sáng,\nĐâu đâu cũng nghe tiếng chim hót.\nĐêm nghe tiếng gió mưa,\nHoa rụng biết bao nhiêu."),

    ("Hạ Nhật - Nắng Hè Chói Chang", "Mùa Hạ.", "Cicada sounds, Hot.",
     "**(Verse 1)**\n力尽不知热，\n但惜夏日长。\n接天莲叶无穷碧，\n映日荷花别样红。",
     "**(Verse 1)**\nLực tận bất tri nhiệt,\nĐãn tích hạ nhật trường.\nTiếp thiên liên diệp vô cùng bích,\nÁnh nhật hà hoa biệt dạng hồng.",
     "**(Verse 1)**\nLàm việc hết sức không biết nóng,\nChỉ tiếc ngày hè dài.\nLá sen tiếp nối trời xanh vô cùng,\nHoa sen chiếu mặt trời đỏ đặc biệt."),

    ("Thu Nguyệt - Trăng Thu Sáng Tỏ", "Mùa Thu.", "Melancholic, Wind.",
     "**(Verse 1)**\n秋风萧瑟，洪波涌起。\n日月之行，若出其中。\n星汉灿烂，若出其里。",
     "**(Verse 1)**\nThu phong tiêu sắt, hồng ba dũng khởi.\nNhật nguyệt chi hành, nhược xuất kỳ trung.\nTinh hán xán lạn, nhược xuất kỳ lý.",
     "**(Verse 1)**\nGió thu hiu hắt, sóng lớn nổi lên.\nMặt trời mặt trăng đi, như từ trong đó ra.\nSông Ngân rực rỡ, như từ trong đó ra."),

    ("Đông Tuyết - Tuyết Đông Lạnh Giá", "Mùa Đông.", "Cold wind, Silence.",
     "**(Verse 1)**\n千山鸟飞绝，\n万径人踪灭。\n孤舟蓑笠翁，\n独钓寒江雪。",
     "**(Verse 1)**\nThiên sơn điểu phi tuyệt,\nVạn kinh nhân tung diệt.\nCô chu xoa lạp ông,\nĐộc điếu hàn giang tuyết.",
     "**(Verse 1)**\nNgàn núi chim bay hết,\nVạn đường dấu người mất.\nThuyền lẻ loi ông già nón lá áo tơi,\nCâu cá một mình trong tuyết sông lạnh.")
]

sects_songs = [
    ("Cửu Hoa Kiếm Ca - Kiếm Tông Hộ Sơn", "Cửu Hoa Kiếm Tông.", "Sword sounds, Heroic.",
     "**(Verse 1)**\n九华剑气冲斗牛，\n万剑归宗斩妖头。\n护我山门清净地，\n誓将热血洒春秋。",
     "**(Verse 1)**\nCửu hoa kiếm khí xung đẩu ngưu,\nVạn kiếm quy tông trảm yêu đầu.\nHộ ngã sơn môn thanh tịnh địa,\nThệ tương nhiệt huyết sái xuân thu.",
     "**(Verse 1)**\nKiếm khí Cửu Hoa xông thẳng lên sao Đẩu sao Ngưu,\nVạn kiếm quy tông chém đầu yêu quái.\nBảo vệ đất thanh tịnh nơi cửa núi ta,\nThề đem máu nóng tưới lên xuân thu."),

    ("Thiên Ma Vũ - Ma Tông Mê Hoặc", "Thiên Ma Tông.", "Seductive, Dark.",
     "**(Verse 1)**\n天魔缭乱舞众生，\n欲念横生道难成。\n借问何处是极乐，\n唯我魔宫任纵横。",
     "**(Verse 1)**\nThiên ma liễu loạn vũ chúng sinh,\nDục niệm hoành sinh đạo nan thành.\nTá vấn hà xứ thị cực lạc,\nDuy ngã ma cung nhậm tung hoành.",
     "**(Verse 1)**\nThiên ma múa may làm rối loạn chúng sinh,\nDục vọng nảy sinh đạo khó thành.\nXin hỏi nơi nào là cực lạc,\nChỉ có ma cung của ta mặc sức tung hoành."),

    ("Vạn Thú Hống - Thú Môn Uy Chấn", "Vạn Thú Môn.", "Beast roars, Tribal.",
     "**(Verse 1)**\n万兽奔腾震地摇，\n驾驭苍龙上九霄。\n人兽合一力无敌，\n踏破山河路迢迢。",
     "**(Verse 1)**\nVạn thú bôn đằng chấn địa dao,\nGiá ngự thương long thượng cửu tiêu.\nNhân thú hợp nhất lực vô địch,\nĐạp phá sơn hà lộ thiều thiều.",
     "**(Verse 1)**\nVạn thú chạy chồm làm rung chuyển đất,\nCưỡi rồng xanh lên chín tầng mây.\nNgười thú hợp nhất sức mạnh vô địch,\nĐạp vỡ núi sông đường xa thăm thẳm."),

    ("Thủy Nguyệt Tình - Am Môn Thanh Tịnh", "Thủy Nguyệt Am.", "Gentle, Water.",
     "**(Verse 1)**\n水中月影镜中花，\n一场空梦付烟霞。\n清修苦练求真道，\n不问红尘乱如麻。",
     "**(Verse 1)**\nThủy trung nguyệt ảnh kính trung hoa,\nNhất trường không mộng phó yên hà.\nThanh tu khổ luyện cầu chân đạo,\nBất vấn hồng trần loạn như ma.",
     "**(Verse 1)**\nBóng trăng trong nước hoa trong gương,\nMột giấc mộng không gửi vào khói ráng.\nTu hành thanh tịnh khổ luyện cầu chân đạo,\nKhông hỏi chuyện hồng trần rối như tơ vò."),

    ("Tán Tu Hành - Liên Minh Tự Do", "Tán Tu Liên Minh.", "Free, Folk.",
     "**(Verse 1)**\n无门无派一身轻，\n四海为家任我行。\n虽然路途多坎坷，\n逍遥自在乐平生。",
     "**(Verse 1)**\nVô môn vô phái nhất thân khinh,\nTứ hải vi gia nhậm ngã hành.\nTuy nhiên lộ đồ đa khảm kh_a,\nTiêu dao tự tại lạc bình sinh.",
     "**(Verse 1)**\nKhông môn không phái một thân nhẹ nhàng,\nBốn biển là nhà mặc sức ta đi.\nTuy rằng đường đi nhiều gập ghềnh,\nTiêu dao tự tại vui vẻ cả đời."),

    ("Thái Hư Nhạc - Tiên Giới Hư Vô", "Thái Hư/Tiên Giới.", "Ethereal, Holy.",
     "**(Verse 1)**\n太虚幻境渺无踪，\n只有仙音绕碧空。\n欲访神仙何处去，\n白云深处是仙宫。",
     "**(Verse 1)**\nThái hư huyễn cảnh miểu vô tung,\nChỉ hữu tiên âm nhiễu bích không.\nDục phỏng thần tiên hà xứ khứ,\nBạch vân thâm xứ thị tiên cung.",
     "**(Verse 1)**\nCảnh ảo thái hư mờ mịt không dấu vết,\nChỉ có tiếng tiên nhạc lượn lờ bầu trời xanh.\nMuốn tìm thần tiên đi nơi nào,\nNơi mây trắng sâu thẳm chính là cung tiên.")
]

with open("Đạo/Âm_Nhạc/Tuyển_Tập_Thời_Tiết.md", "w") as f:
    f.write("# TUYỂN TẬP ÂM NHẠC: THỜI TIẾT & MÙA\n\n")
    f.write("Tổng hợp 10 bài hát (4 mùa + 6 tông môn) về sự thay đổi của đất trời và các thế lực tu chân.\n\n")
    for song in seasons_songs:
        f.write(create_song_entry(*song))
    f.write("\n## CÁC BÀI HÁT TÔNG MÔN\n")
    for song in sects_songs:
        f.write(create_song_entry(*song))

print("Batch 5 created successfully.")
