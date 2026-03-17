const relationshipData = {
  // Danh sách nhân vật (nodes)
  "characters": [
    {
      "id": "linh_tham_nguyet",
      "name": "Linh Thâm Nguyệt",
      "title": "Trưởng Lão Quan Sát",
      "realm": "Kim Đan",
      "faction": "Thâm Hải Vi Linh",
      "region": "Vô Tận Hải",
      "role": "supporting",
      "pov": false,
      "avatar_color": "#1e3a8a"
    },
    {
      "id": "linh_tieu_uyen",
      "name": "Linh Tiểu Uyên",
      "title": "Đệ Tử Thâm Hải",
      "realm": "Luyện Khí",
      "faction": "Thâm Hải Vi Linh",
      "region": "Vô Tận Hải",
      "role": "supporting",
      "pov": false,
      "avatar_color": "#3b82f6"
    },
    {
      "id": "linh_tram_uyen",
      "name": "Linh Trầm Uyên",
      "title": "Thu Thập Viên",
      "realm": "Trúc Cơ",
      "faction": "Thâm Hải Vi Linh",
      "region": "Vô Tận Hải",
      "role": "supporting",
      "pov": false,
      "avatar_color": "#4338ca"
    },
    {
      "id": "a_ngoc",
      "name": "A Ngốc",
      "title": "Hồn Nhiên Tử",
      "realm": "Nguyên Anh Sơ Kỳ",
      "faction": "Tán Tu",
      "region": "Trung Tâm",
      "role": "protagonist",
      "pov": true,
      "avatar_color": "#c9a96e"
    },
    {
      "id": "le_vo_tam",
      "name": "Lệ Vô Tâm",
      "title": "Vạn Độc Thánh Tử",
      "realm": "Kim Đan Trung Kỳ",
      "faction": "Vạn Độc Môn",
      "region": "Trung Tâm",
      "role": "antagonist",
      "pov": true,
      "avatar_color": "#6b1c23"
    },
    {
      "id": "lam_phong",
      "name": "Lâm Phong",
      "title": "Truy Phong Khách",
      "realm": "Luyện Khí Viên Mãn",
      "faction": "Tán Tu",
      "region": "Đông Hoang",
      "role": "protagonist",
      "pov": true,
      "avatar_color": "#2d6a4f"
    },
    {
      "id": "diep_tinh_suong",
      "name": "Diệp Tĩnh Sương",
      "title": "Hàn Mai Kiếm",
      "realm": "Trúc Cơ Sơ Kỳ",
      "faction": "Cửu Hoa Kiếm Tông",
      "region": "Đông Hoang",
      "role": "protagonist",
      "pov": true,
      "avatar_color": "#d4cbbf"
    },
    {
      "id": "am_diep",
      "name": "Ám Diệp",
      "title": "Trưởng Lão Lưu Đày",
      "realm": "Trúc Cơ Viên Mãn",
      "faction": "Hắc Tinh Linh Lưu Đày",
      "region": "Đông Hoang",
      "role": "supporting",
      "pov": false,
      "avatar_color": "#2c3e50"
    },
    {
      "id": "am_da_hanh",
      "name": "Ám Dạ Hành",
      "title": "Ám Sát Đội Trưởng",
      "realm": "Trúc Cơ Viên Mãn",
      "faction": "Hắc Tinh Linh Lưu Đày",
      "region": "Đông Hoang",
      "role": "supporting",
      "pov": false,
      "avatar_color": "#34495e"
    },
    {
      "id": "am_huyet",
      "name": "Ám Huyết",
      "title": "Huyết Mạch Sư",
      "realm": "Trúc Cơ Trung Kỳ",
      "faction": "Hắc Tinh Linh Lưu Đày",
      "region": "Đông Hoang",
      "role": "supporting",
      "pov": false,
      "avatar_color": "#7f8c8d"
    },
    {
      "id": "hoang_dai_son",
      "name": "Hoàng Đại Sơn",
      "title": "Trưởng Trại Tuyết Thưa",
      "realm": "Trúc Cơ Hậu Kỳ",
      "faction": "Băng Nguyên Tán Tu Hội",
      "region": "Bắc Băng",
      "role": "supporting",
      "pov": false,
      "avatar_color": "#8c9fb0"
    },
    {
      "id": "ly_tuyet_phong",
      "name": "Lý Tuyết Phong",
      "title": "Trưởng Trại Hàn Phong",
      "realm": "Trúc Cơ Viên Mãn",
      "faction": "Băng Nguyên Tán Tu Hội",
      "region": "Bắc Băng",
      "role": "supporting",
      "pov": false,
      "avatar_color": "#b0c4de"
    },
    {
      "id": "nguyen_han_suong",
      "name": "Nguyễn Hàn Sương",
      "title": "Quản Sự",
      "realm": "Luyện Khí Đỉnh Phong",
      "faction": "Băng Nguyên Tán Tu Hội",
      "region": "Bắc Băng",
      "role": "supporting",
      "pov": false,
      "avatar_color": "#a8c0d8"
    },
    {
      "id": "nguyet_quang",
      "name": "Nguyệt Quang",
      "title": "Đàn Mẫu",
      "realm": "Trúc Cơ Sơ Kỳ",
      "faction": "Thủy Mẫu Trùng Đàn",
      "region": "Vô Tận Hải",
      "role": "supporting",
      "pov": false,
      "avatar_color": "#e0e0e0"
    },
    {
      "id": "trung_bach_quang",
      "name": "Trùng Bạch Quang",
      "title": "Phó Đàn",
      "realm": "Luyện Khí Đỉnh Phong",
      "faction": "Thủy Mẫu Trùng Đàn",
      "region": "Vô Tận Hải",
      "role": "supporting",
      "pov": false,
      "avatar_color": "#ffffff"
    },
    {
      "id": "trung_hong_diem",
      "name": "Trùng Hồng Diệm",
      "title": "Tiên Phong Dẫn Đường",
      "realm": "Luyện Khí Hậu Kỳ",
      "faction": "Thủy Mẫu Trùng Đàn",
      "region": "Vô Tận Hải",
      "role": "supporting",
      "pov": false,
      "avatar_color": "#ff4d4d"
    },
    {
      "id": "bao_hong_tan",
      "name": "Bào Hồng Tán",
      "title": "Tộc Trưởng",
      "realm": "Trúc Cơ Hậu Kỳ",
      "faction": "Bào Tử Mật Lâm Tộc",
      "region": "Đông Hoang",
      "role": "supporting",
      "pov": false,
      "avatar_color": "#ff6b6b"
    },
    {
      "id": "bao_huyet_tinh",
      "name": "Bào Huyết Tịnh",
      "title": "Chuyên Gia Huyết Độc",
      "realm": "Trúc Cơ Trung Kỳ",
      "faction": "Bào Tử Mật Lâm Tộc",
      "region": "Đông Hoang",
      "role": "supporting",
      "pov": false,
      "avatar_color": "#cc0000"
    },
    {
      "id": "bao_hac_lam",
      "name": "Bào Hắc Lâm",
      "title": "Trinh Sát",
      "realm": "Trúc Cơ Sơ Kỳ",
      "faction": "Bào Tử Mật Lâm Tộc",
      "region": "Đông Hoang",
      "role": "supporting",
      "pov": false,
      "avatar_color": "#333333"
    },
    {
      "id": "trung_bach",
      "name": "Trùng Bạch",
      "title": "Phường Chủ",
      "realm": "Trúc Cơ Trung Kỳ",
      "faction": "Ngọc Trai Sâu Phường",
      "region": "Đông Hoang",
      "role": "supporting",
      "pov": false,
      "avatar_color": "#ffffff"
    },
    {
      "id": "trung_ngoc_chau",
      "name": "Trùng Ngọc Châu",
      "title": "Thợ Chế Tác",
      "realm": "Trúc Cơ Sơ Kỳ",
      "faction": "Ngọc Trai Sâu Phường",
      "region": "Đông Hoang",
      "role": "supporting",
      "pov": false,
      "avatar_color": "#ffffff"
    },
    {
      "id": "trung_tieu_trai",
      "name": "Trùng Tiểu Trai",
      "title": "Nuôi Trồng Viên",
      "realm": "Luyện Khí Hậu Kỳ",
      "faction": "Ngọc Trai Sâu Phường",
      "region": "Đông Hoang",
      "role": "supporting",
      "pov": false,
      "avatar_color": "#ffffff"
    }
  ],

  // Danh sách quan hệ (edges)
  "relationships": [
    {
      "source": "Cung Tuyệt Trần",
      "target": "Tiễn Vô Song",
      "description": "Kính trọng Môn Chủ, luôn cố gắng rèn ra cây cung hoàn mỹ nhất cho người này để bảo vệ vùng Vọng Nguyệt Đỉnh.",
      "type": "positive"
    },
    {
      "source": "Cung Tuyệt Trần",
      "target": "Lý Xuyên Vân",
      "description": "Thường xuyên tranh cãi gay gắt với vị Trưởng Lão này về việc sử dụng linh cốt nào là tốt nhất, nhưng sâu thẳm lại rất nể phục tài bắn cung của đối phương.",
      "type": "neutral"
    },
    {
      "source": "Cung Tuyệt Trần",
      "target": "Lê Thiên Mục",
      "description": "Đánh giá cao nhãn lực thiên phú của tiểu bối này, thỉnh thoảng chỉ điểm vài kỹ xảo nhỏ để bảo quản cung tên khi hành tẩu sa mạc.",
      "type": "positive"
    },
    {
      "source": "Lý Xuyên Vân",
      "target": "Tiễn Vô Song",
      "description": "Tuyệt đối trung thành với Môn Chủ, là lưỡi dao sắc bén nhất ẩn giấu trong bóng tối của Thần Cung Môn.",
      "type": "positive"
    },
    {
      "source": "Lý Xuyên Vân",
      "target": "Cung Tuyệt Trần",
      "description": "Bằng hữu chí cốt nhưng hay khắc khẩu, thường xuyên nhờ đối phương chế tạo những mũi tiễn cốt đặc thù riêng cho những nhiệm vụ hiểm ác.",
      "type": "neutral"
    },
    {
      "source": "Lý Xuyên Vân",
      "target": "Lê Thiên Mục",
      "description": "Sư tôn nghiêm khắc, truyền thọ toàn bộ kinh nghiệm ngắm bắn và bí quyết ẩn nấp sinh tồn trên sa mạc khắc nghiệt cho đệ tử này.",
      "type": "positive"
    },
    {
      "source": "Lê Thiên Mục",
      "target": "Lý Xuyên Vân",
      "description": "Sư tôn đáng kính, người đã kiên nhẫn dạy y cách kìm nén sự kiêu ngạo tuổi trẻ để trở thành một thợ săn thực thụ trong Sa Mạc Cốt Linh.",
      "type": "positive"
    },
    {
      "source": "Phạm Nhất Tiễn",
      "target": "Tiễn Vô Song",
      "description": "Sư phụ đích thực, người đã nhặt hắn về từ bão cát và truyền dạy đạo lý \"Nhất tiễn\".",
      "type": "positive"
    },
    {
      "source": "Phạm Nhất Tiễn",
      "target": "Tiễn Phá Không",
      "description": "Vô cùng kính sợ vị Đại Trưởng Lão uy nghiêm này, luôn lấy sức mạnh phá hoại của ông làm mục tiêu phấn đấu.",
      "type": "positive"
    },
    {
      "source": "Phạm Nhất Tiễn",
      "target": "Lê Thiên Mục",
      "description": "Thường cùng tên đồng môn này thực hiện các nhiệm vụ săn bắn; một người tìm kiếm con mồi, một người tung đòn kết liễu.",
      "type": "positive"
    },
    {
      "source": "Tiễn Linh Phong",
      "target": "Tiễn Vô Song",
      "description": "Kính nể Môn Chủ, là cánh tay đắc lực phụ trách mạng lưới tai mắt cho tông môn.",
      "type": "positive"
    },
    {
      "source": "Tiễn Linh Phong",
      "target": "Tiễn Phá Không",
      "description": "Cực kỳ khó chịu với sự cứng nhắc của vị Đại Trưởng Lão, thường xuyên tranh cãi về chiến lược, nhưng khi cần lại phối hợp rất nhịp nhàng.",
      "type": "neutral"
    },
    {
      "source": "Tiễn Linh Phong",
      "target": "Lý Xuyên Vân",
      "description": "Tôn trọng cái nhìn đại cục của vị Trưởng Lão này, thường trao đổi thông tin về các thương đoàn để tối ưu hóa nguồn thu bảo kê của tông môn.",
      "type": "positive"
    },
    {
      "source": "Tiễn Phá Không",
      "target": "Tiễn Vô Song",
      "description": "Tôn sùng Môn Chủ nhưng thường có quan điểm khắt khe hơn về trừng phạt kẻ phản bội, luôn là chỗ dựa quân sự vững chắc nhất.",
      "type": "positive"
    },
    {
      "source": "Tiễn Phá Không",
      "target": "Tiễn Linh Phong",
      "description": "Thường mắng mỏ vị Chấp Sự Tình Báo này vì những cách hành động lén lút, nhưng lại dựa dẫm vào thông tin của ông ta để nhắm mục tiêu chuẩn xác.",
      "type": "neutral"
    },
    {
      "source": "Tiễn Phá Không",
      "target": "Phạm Nhất Tiễn",
      "description": "Khen ngợi sát khí của tên đệ tử này, thường xuyên huấn luyện khắc nghiệt với hắn để rèn giũa kỹ năng \"Nhất Tiễn\".",
      "type": "positive"
    },
    {
      "source": "Lê Thiên Mục",
      "target": "Cung Tuyệt Trần",
      "description": "Vô cùng biết ơn Viện Chủ vì đã ưu ái rèn riêng cho y một cây linh cung cốt xà vô cùng phù hợp với nhãn lực đặc thù.",
      "type": "positive"
    },
    {
      "source": "Lê Thiên Mục",
      "target": "Tiễn Vô Song",
      "description": "Sùng bái Môn Chủ, coi sức mạnh của ngài là đỉnh cao tiễn thuật mà bản thân luôn khao khát vươn tới.",
      "type": "positive"
    },
    {
      "from": "trung_bach",
      "to": "trung_ngoc_chau",
      "type": "đồng_minh",
      "subtype": "bảo_vệ",
      "desc": "Coi như con gái"
    },
    {
      "from": "trung_bach",
      "to": "trung_tieu_trai",
      "type": "đồng_minh",
      "subtype": "sư_đồ",
      "desc": "Dạy bài ca buồn"
    },
    {
      "from": "trung_ngoc_chau",
      "to": "trung_tieu_trai",
      "type": "đồng_minh",
      "subtype": "chăm_sóc",
      "desc": "Kể chuyện biển cả"
    },
    {
      "from": "a_ngoc",
      "to": "le_vo_tam",
      "type": "đồng_minh",
      "subtype": "bảo_vệ",
      "label": "Bảo vệ / Bạn đồng hành",
      "strength": 4,
      "status": "active",
      "since_chapter": 78,
      "bidirectional": false,
      "notes": "A Ngốc dùng Hỗn Độn Kim Đan cứu Lệ Vô Tâm và đi theo làm khiên bảo vệ."
    },
    {
      "from": "le_vo_tam",
      "to": "a_ngoc",
      "type": "đồng_minh",
      "subtype": "che_chở",
      "label": "Che chở bất đắc dĩ",
      "strength": 3,
      "status": "active",
      "since_chapter": 89,
      "bidirectional": false,
      "notes": "Lệ Vô Tâm dần thay đổi tâm tính vì sự thuần khiết của A Ngốc."
    },
    {
      "from": "lam_phong",
      "to": "diep_tinh_suong",
      "type": "đồng_minh",
      "subtype": "tri_kỷ",
      "label": "Đồng hành / Người bảo vệ",
      "strength": 4,
      "status": "active",
      "since_chapter": 18,
      "bidirectional": true,
      "notes": "Cùng thoát khỏi Rừng Huyết Độc và tiến vào Đông Hoang."
    },
    {
      "from": "hoang_dai_son",
      "to": "ly_tuyet_phong",
      "type": "đồng_minh",
      "subtype": "đồng_môn",
      "label": "Đồng đội",
      "strength": 4,
      "status": "active",
      "since_chapter": 1,
      "bidirectional": true,
      "notes": "Thường xuyên cãi vã nhưng là đồng đội sinh tử, phối hợp ăn ý."
    },
    {
      "from": "hoang_dai_son",
      "to": "nguyen_han_suong",
      "type": "ngờ_vực",
      "subtype": "bất_hòa",
      "label": "Cảnh giác",
      "strength": 2,
      "status": "active",
      "since_chapter": 1,
      "bidirectional": false,
      "notes": "Hoàng Đại Sơn không thích tính cách lươn lẹo của Hàn Sương."
    },
    {
      "from": "ly_tuyet_phong",
      "to": "nguyen_han_suong",
      "type": "đồng_minh",
      "subtype": "cấp_trên_cấp_dưới",
      "label": "Tín nhiệm",
      "strength": 3,
      "status": "active",
      "since_chapter": 1,
      "bidirectional": false,
      "notes": "Lý Tuyết Phong trọng dụng mưu trí của Hàn Sương."
    },
    {
      "from": "nguyet_quang",
      "to": "trung_bach_quang",
      "type": "đồng_minh",
      "subtype": "cấp_trên_cấp_dưới",
      "label": "Tín nhiệm",
      "strength": 4,
      "status": "active",
      "since_chapter": 1,
      "bidirectional": true,
      "notes": "Nguyệt Quang dựa vào Bạch Quang để ổn định bầy đàn."
    },
    {
      "from": "nguyet_quang",
      "to": "trung_hong_diem",
      "type": "đồng_minh",
      "subtype": "bảo_vệ",
      "label": "Bảo bọc",
      "strength": 4,
      "status": "active",
      "since_chapter": 1,
      "bidirectional": true,
      "notes": "Nguyệt Quang luôn phải trông chừng sự bốc đồng của Hồng Diệm."
    },
    {
      "from": "trung_bach_quang",
      "to": "trung_hong_diem",
      "type": "đồng_minh",
      "subtype": "đồng_môn",
      "label": "Quản giáo",
      "strength": 3,
      "status": "active",
      "since_chapter": 1,
      "bidirectional": false,
      "notes": "Bạch Quang thường xuyên phải dọn dẹp hậu quả cho Hồng Diệm."
    },
    {
      "from": "bao_hong_tan",
      "to": "bao_huyet_tinh",
      "type": "đồng_minh",
      "subtype": "cấp_trên_cấp_dưới",
      "label": "Tin tưởng/Kìm hãm",
      "strength": 4,
      "status": "active",
      "since_chapter": 1,
      "bidirectional": true,
      "notes": "Tộc trưởng tôn trọng khả năng nhưng phải kìm hãm sự ám ảnh nghiên cứu độc của Huyết Tịnh."
    },
    {
      "from": "bao_hong_tan",
      "to": "bao_hac_lam",
      "type": "đồng_minh",
      "subtype": "cấp_trên_cấp_dưới",
      "label": "Tai mắt",
      "strength": 4,
      "status": "active",
      "since_chapter": 1,
      "bidirectional": true,
      "notes": "Hắc Lâm là trinh sát tuyệt đối trung thành của Hồng Tán."
    },
    {
      "from": "bao_huyet_tinh",
      "to": "bao_hac_lam",
      "type": "đồng_minh",
      "subtype": "đồng_môn",
      "label": "Đối tác",
      "strength": 3,
      "status": "active",
      "since_chapter": 1,
      "bidirectional": true,
      "notes": "Hắc Lâm mang mẫu vật về cho Huyết Tịnh nghiên cứu."
    },
    {
      "from": "am_diep",
      "to": "am_da_hanh",
      "type": "đồng_minh",
      "subtype": "cấp_trên_cấp_dưới",
      "label": "Tuyệt đối trung thành",
      "strength": 5,
      "status": "active",
      "since_chapter": 1,
      "bidirectional": true,
      "notes": "Ám Dạ Hành là cánh tay phải đắc lực, tuyệt đối phục tùng mệnh lệnh bảo vệ cộng đồng."
    },
    {
      "from": "am_diep",
      "to": "am_huyet",
      "type": "đồng_minh",
      "subtype": "cấp_trên_cấp_dưới",
      "label": "Tín nhiệm",
      "strength": 4,
      "status": "active",
      "since_chapter": 1,
      "bidirectional": true,
      "notes": "Ám Diệp cung cấp tài nguyên để Ám Huyết nghiên cứu bí mật huyết mạch của Hắc Tinh Linh."
    },
    {
      "from": "am_da_hanh",
      "to": "am_huyet",
      "type": "đồng_minh",
      "subtype": "đồng_môn",
      "label": "Đồng đội",
      "strength": 3,
      "status": "active",
      "since_chapter": 1,
      "bidirectional": true,
      "notes": "Ám Huyết cung cấp độc dược và dược thảo để Ám Dạ Hành thực hiện các nhiệm vụ ám sát."
    },
    {
      "from": "lang_bach_suong",
      "to": "lang_bao_phong",
      "type": "đồng_minh",
      "subtype": "đồng_môn",
      "label": "Chữa Trị / Cằn Nhằn",
      "strength": 4,
      "status": "active",
      "since_chapter": 1,
      "bidirectional": true,
      "notes": "Bạch Sương thường xuyên dùng bạo lực y khoa răn đe Bạo Phong bớt liều lĩnh."
    },
    {
      "from": "lang_co_han",
      "to": "lang_bao_phong",
      "type": "đồng_minh",
      "subtype": "đồng_môn",
      "label": "Chiến Hữu / Bọc Hậu",
      "strength": 4,
      "status": "active",
      "since_chapter": 1,
      "bidirectional": true,
      "notes": "Cô Hàn dọn dẹp cạm bẫy giúp Bạo Phong yên tâm lao lên càn quét."
    }
  ],

  // Nhóm thế lực
  "factions": [
    {
      "id": "van_doc_mon",
      "name": "Vạn Độc Môn",
      "type": "tông_môn",
      "region": "Nam Cương",
      "members": ["le_vo_tam"],
      "leader": "doc_co_lao_quai"
    },
    {
      "id": "tan_tu",
      "name": "Tán Tu",
      "type": "tự_do",
      "region": "Khắp Nơi",
      "members": ["a_ngoc", "lam_phong"],
      "leader": null
    },
    {
      "id": "hac_tinh_linh_luu_day",
      "name": "Hắc Tinh Linh Lưu Đày",
      "type": "thế_lực_ẩn",
      "region": "Đông Hoang",
      "members": ["am_diep", "am_da_hanh", "am_huyet"],
      "leader": "am_diep"
    },
    {
      "id": "bang_nguyen_tan_tu_hoi",
      "name": "Băng Nguyên Tán Tu Hội",
      "type": "tông_môn",
      "region": "Bắc Băng",
      "members": ["hoang_dai_son", "ly_tuyet_phong", "nguyen_han_suong"],
      "leader": "tran_han_phong"
    },
    {
      "id": "bao_tu_mat_lam_toc",
      "name": "Bào Tử Mật Lâm Tộc",
      "type": "bộ_lạc",
      "region": "Đông Hoang",
      "members": ["bao_hong_tan", "bao_huyet_tinh", "bao_hac_lam"],
      "leader": "bao_hong_tan"
    }
  ],

  // Metadata
  "meta": {
    "last_updated": "2026-03-15",
    "total_characters": 7,
    "total_relationships": 7,
    "scanned_chapters": {
      "Góc_Nhìn_A_Ngốc": 132,
      "Góc_Nhìn_Lệ_Vô_Tâm": 152,
      "Góc_Nhìn_Lâm_Phong": 88,
      "Góc_Nhìn_Diệp_Tĩnh_Sương": 10
    }
  }
};

if (typeof window !== "undefined") {
  window.relationshipData = relationshipData;
}
if (typeof module !== "undefined") {
  module.exports = relationshipData;
}

// Hai Than Cung (Vo Tan Hai) Update
if (typeof relationships !== 'undefined') {
    relationships.push(
        { source: "Chương Hắc Triều", target: "Chương Thiên Cơ Huyền", type: "Cấp Dưới", description: "Bị kiềm chế bởi sự nghiêm khắc của Tế Tư." },
        { source: "Chương Hắc Triều", target: "Chương Thiên Nhãn", type: "Đồng Liêu", description: "Dựa vào mạng lưới tình báo để tìm con mồi." },
        { source: "Chương Thiên Cơ Huyền", target: "Chương Hắc Triều", type: "Cấp Trên", description: "Thường xuyên răn đe Hắc Triều vì sự bạo lực vô cớ." },
        { source: "Chương Thiên Nhãn", target: "Chương Hắc Triều", type: "Đồng Liêu", description: "Cung cấp tọa độ mục tiêu nhưng cũng âm thầm đề phòng." }
    );
}

if (typeof characterData !== 'undefined') {
    characterData["Chương Hắc Triều"] = {
        name: "Chương Hắc Triều",
        faction: "Hải Thần Cung",
        realm: "Kim Đan Viên Mãn",
        description: "Tây Bắc Tướng Quân, bạch tuộc đen tàn nhẫn và khát máu.",
        image: ""
    };
    characterData["Chương Thiên Cơ Huyền"] = {
        name: "Chương Thiên Cơ Huyền",
        faction: "Hải Thần Cung",
        realm: "Nguyên Anh Sơ Kỳ",
        description: "Đệ Tứ Tế Tư, lão giả bạch tuộc uyên bác nhưng bảo thủ.",
        image: ""
    };
    characterData["Chương Thiên Nhãn"] = {
        name: "Chương Thiên Nhãn",
        faction: "Hải Thần Cung",
        realm: "Trúc Cơ Viên Mãn",
        description: "Tình Báo Trưởng, bạch tuộc nhỏ bé với hàng ngàn con mắt.",
        image: ""
    };
}

// Han Doc Vi Trung Doan (Bac Bang) Update
if (typeof relationships !== 'undefined') {
    relationships.push(
        { source: "Băng Dực", target: "Vi Thanh", type: "Chủ-Tớ", description: "Tai mắt đắc lực, vô cùng trung thành giúp nắm bắt tình hình Bắc Băng." },
        { source: "Băng Dực", target: "Trùng Băng Châm", type: "Đồng Nghiệp", description: "Đối tác phối hợp ăn ý trong nhiệm vụ trinh sát và mở đường." },
        { source: "Băng Dực", target: "Trùng Bạch Lân", type: "Đồng Môn", description: "Cạnh tranh khả năng lẩn trốn trong bão tuyết." },
        { source: "Trùng Băng Châm", target: "Vi Thanh", type: "Chủ-Tớ", description: "Phó thủ trung thành bảo vệ quần thể quyết đoán." },
        { source: "Trùng Băng Châm", target: "Trùng Bạch Lân", type: "Đồng Nghiệp", description: "Cùng thực hiện nhiệm vụ xâm nhập nhưng ít hợp tính cách." },
        { source: "Trùng Bạch Lân", target: "Vi Thanh", type: "Chủ-Tớ", description: "Được tin tưởng để quan sát các thế lực ma đạo cực kỳ nguy hiểm." }
    );
}

if (typeof characterData !== 'undefined') {
    characterData["Băng Dực"] = {
        name: "Băng Dực",
        faction: "Hàn Độc Vi Trùng Đoàn",
        realm: "Kim Đan Trung Kỳ",
        description: "Chuồn chuồn băng siêu nhỏ, trinh sát tinh tường.",
        image: ""
    };
    characterData["Trùng Băng Châm"] = {
        name: "Trùng Băng Châm",
        faction: "Hàn Độc Vi Trùng Đoàn",
        realm: "Kim Đan",
        description: "Kim gai siêu nhỏ tàn độc, phục kích gây chết chóc bằng băng.",
        image: ""
    };
    characterData["Trùng Bạch Lân"] = {
        name: "Trùng Bạch Lân",
        faction: "Hàn Độc Vi Trùng Đoàn",
        realm: "Trúc Cơ",
        description: "Vảy tuyết trong suốt chuyên rải sương lạnh vô hình.",
        image: ""
    };
    characterData["Ám Diệp"] = {
        name: "Ám Diệp",
        faction: "Hắc Tinh Linh Lưu Đày",
        realm: "Trúc Cơ Viên Mãn",
        description: "Trưởng Lão Lưu Đày, dùng Ám Mộc Chi Lực bảo vệ cộng đồng.",
        image: ""
    };
    characterData["Ám Dạ Hành"] = {
        name: "Ám Dạ Hành",
        faction: "Hắc Tinh Linh Lưu Đày",
        realm: "Trúc Cơ Viên Mãn",
        description: "Ám Sát Đội Trưởng, như bóng ma trong đêm.",
        image: ""
    };
    characterData["Ám Huyết"] = {
        name: "Ám Huyết",
        faction: "Hắc Tinh Linh Lưu Đày",
        realm: "Trúc Cơ Trung Kỳ",
        description: "Huyết Mạch Sư nghiên cứu cơ thể Hắc Tinh Linh.",
        image: ""
    };

    // Hỏa Yêu Tàn Đoàn (Tây Mạc)
    characterData["Hỏa Nham Dung"] = {
        name: "Hỏa Nham Dung",
        faction: "Hỏa Yêu Tàn Đoàn",
        realm: "Luyện Khí Hậu Kỳ",
        description: "Thợ rèn mang thân hình nham thạch bán nung chảy, kiên nhẫn chế tạo vũ khí và khao khát rèn ra Hỏa Bảo.",
        image: ""
    };
    characterData["Hỏa Thiên Viêm Sơn"] = {
        name: "Hỏa Thiên Viêm Sơn",
        faction: "Hỏa Yêu Tàn Đoàn",
        realm: "Trúc Cơ Sơ Kỳ",
        description: "Phó đoàn trưởng, chiến binh khổng lồ với lớp giáp nham thạch, luôn có niềm tin bất diệt vào Hỏa Hạch truyền thuyết.",
        image: ""
    };
    characterData["Hỏa Tinh"] = {
        name: "Hỏa Tinh",
        faction: "Hỏa Yêu Tàn Đoàn",
        realm: "Luyện Khí Viên Mãn",
        description: "Đốm lửa nhỏ linh hoạt, trẻ con nhưng dũng cảm, mơ ước tiến ra thế giới tìm nguồn lửa mới cho bộ tộc.",
        image: ""
    };

    // Cổ Nham Bộ Lạc (Tây Mạc)
    characterData["Nham Tĩnh"] = {
        name: "Nham Tĩnh",
        faction: "Cổ Nham Bộ Lạc",
        realm: "Trúc Cơ Trung Kỳ",
        description: "Tế Tư trầm mặc, thiền định ngộ đạo từ sự im lặng của trầm tích nham.",
        image: ""
    };
    characterData["Xích Nham"] = {
        name: "Xích Nham",
        faction: "Cổ Nham Bộ Lạc",
        realm: "Trúc Cơ Hậu Kỳ",
        description: "Thủ Vệ Trưởng dũng mãnh, sử dụng Xích Luyện Thạch Phủ canh giữ con đường lên đỉnh thiêng.",
        image: ""
    };

    // Cự Linh Tông (Bắc Băng)
    characterData["Nham Chấn Nhạc"] = {
        name: "Nham Chấn Nhạc",
        faction: "Cự Linh Tông",
        realm: "Hóa Thần Sơ Kỳ",
        description: "Trưởng Lão bảo thủ, luyện thể bá đạo với Bá Thể Cự Thần Quyết.",
        image: ""
    };
    characterData["Nham Hồng Hoang"] = {
        name: "Nham Hồng Hoang",
        faction: "Cự Linh Tông",
        realm: "Luyện Hư Sơ Kỳ",
        description: "Thái Thượng Trưởng Lão ngủ vạn năm trong lõi núi Thần Chùy Phong, mang sức mạnh đại địa.",
        image: ""
    };
    characterData["Nham Kình Thiên"] = {
        name: "Nham Kình Thiên",
        faction: "Cự Linh Tông",
        realm: "Nguyên Anh Sơ Kỳ",
        description: "Chiến Cự Tử bốc đồng, muốn mở rộng ảnh hưởng của Cự Tộc.",
        image: ""
    };

    // Phiêu Miễu Băng Hải (Bắc Băng)
    characterData["Băng San Hô"] = {
        name: "Băng San Hô",
        faction: "Phiêu Miễu Băng Hải",
        realm: "Kim Đan Trung Kỳ",
        description: "Dược Sư Biển Băng trầm tĩnh, chuyên điều chế mộng dược và xóa bỏ tâm ma.",
        image: ""
    };
    characterData["Hàn Thanh Âm"] = {
        name: "Hàn Thanh Âm",
        faction: "Phiêu Miễu Băng Hải",
        realm: "Kim Đan Sơ Kỳ",
        description: "Nhạc Sư Huyễn Âm kiêu ngạo, dùng tiếng đàn Hải Thạch Đàn gieo rắc huyễn cảnh chết chóc.",
        image: ""
    };
    characterData["Hải Cung"] = {
        name: "Hải Cung",
        faction: "Phiêu Miễu Băng Hải",
        realm: "Hóa Thần Sơ Kỳ",
        description: "Cung Chủ thoát tục và lạnh lùng, nắm giữ bản nhạc Trần Thế Chủng để đối phó đại kiếp.",
        image: ""
    };
}

if (typeof relationships !== 'undefined') {
    relationships.push(
        { source: "Nham Chấn Nhạc", target: "Nham Hồng Hoang", type: "Tôn Kính", description: "Thường xuyên đến thỉnh giáo và xin lời khuyên từ Thái Thượng Trưởng Lão." },
        { source: "Nham Chấn Nhạc", target: "Nham Kình Thiên", type: "Sư Phụ", description: "Đích thân huấn luyện và truyền đạt Bá Thể Cự Thần Quyết." },
        { source: "Nham Kình Thiên", target: "Nham Chấn Nhạc", type: "Đệ Tử", description: "Kính trọng nhưng hay cãi lại quan điểm bảo thủ của sư phụ." },
        { source: "Nham Kình Thiên", target: "Triệu Thanh Hằng", type: "Kình Địch", description: "Từng giao thủ nhưng không phân thắng bại, luôn xem là đối thủ đáng gờm." },
        { source: "Nham Hồng Hoang", target: "Nham Chấn Nhạc", type: "Hướng Dẫn", description: "Âm thầm chỉ bảo để bảo vệ tông môn." }
    );
    relationships.push(
        { source: "Nham Tĩnh", target: "Bàn Thạch", type: "Kính Trọng", description: "Âm thầm ủng hộ và chia sẻ gánh nặng với Đại Tế Tư." },
        { source: "Nham Tĩnh", target: "Nham Linh", type: "Lắng Nghe", description: "Người duy nhất lắng nghe mọi ý tưởng điên rồ của nàng." },
        { source: "Nham Tĩnh", target: "Nham Cốt", type: "Đồng Liêu", description: "Tôn trọng lòng trung thành nhưng giữ khoảng cách với sự bảo thủ." },
        { source: "Xích Nham", target: "Bàn Thạch", type: "Trung Thành", description: "Thủ vệ trung thành nhất, thề nguyện bảo vệ bằng cả sinh mạng." },
        { source: "Xích Nham", target: "Nham Cốt", type: "Chiến Hữu", description: "Đồng tâm hiệp lực trong việc bảo vệ bộ lạc khỏi ngoại đạo." },
        { source: "Xích Nham", target: "Nham Linh", type: "Nghi Ngờ", description: "Cho rằng nàng quá yếu đuối và có nhiều ý nghĩ kỳ quái." }
    );
    relationships.push(
        { source: "Băng San Hô", target: "Hải Cung", type: "Kính Trọng", description: "Điều chế hương liệu đặc biệt giúp Cung Chủ duy trì minh mẫn." },
        { source: "Hàn Thanh Âm", target: "Hải Cung", type: "Ngưỡng Mộ", description: "Xem Cung Chủ là hiện thân của sự hoàn hảo và lòng trung thành tuyệt đối." },
        { source: "Hải Cung", target: "Hàn Thanh Âm", type: "Trọng Dụng", description: "Giao phó trọng trách kiểm soát tâm trí và huyễn thuật." },
        { source: "Hải Cung", target: "Băng San Hô", type: "Trọng Dụng", description: "Tin tưởng trong việc điều chế dược liệu bảo vệ thần thức." },
        { source: "Băng San Hô", target: "Hàn Thanh Âm", type: "Đồng Liêu", description: "Phối hợp ăn ý, dùng dược liệu gia tăng uy lực tiếng đàn." },
        { source: "Hàn Thanh Âm", target: "Sở Lăng Sương", type: "Khinh Thường", description: "Cho rằng lối đánh trực diện của Lăng Sương thiếu tinh tế nghệ thuật." },
        { source: "Hải Cung", target: "Lý Tuyết Ưng", type: "Cảnh Giác", description: "Nhận thấy ý chí rực cháy của Lý Tuyết Ưng có thể phá vỡ huyễn cảnh băng giá." }
    );
}
