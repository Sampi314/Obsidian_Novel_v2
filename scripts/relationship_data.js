const relationshipData = {
  // Danh sách nhân vật (nodes)
  "characters": [
    {
      "id": "han_tieu",
      "name": "Hàn Tiêu",
      "title": "Cốc Chủ",
      "realm": "Nguyên Anh",
      "faction": "Hàn Kiếm Cốc",
      "region": "Bắc Băng",
      "role": "leader",
      "pov": false,
      "avatar_color": "#e0f7fa"
    },
    {
      "id": "hoang_doan_tuyet",
      "name": "Hoàng Đoạn Tuyết",
      "title": "Trưởng Lão",
      "realm": "Kim Đan",
      "faction": "Hàn Kiếm Cốc",
      "region": "Bắc Băng",
      "role": "support",
      "pov": false,
      "avatar_color": "#e0f7fa"
    },
    {
      "id": "le_kiem_tam",
      "name": "Lê Kiếm Tâm",
      "title": "Chân Truyền",
      "realm": "Kim Đan",
      "faction": "Hàn Kiếm Cốc",
      "region": "Bắc Băng",
      "role": "fighter",
      "pov": false,
      "avatar_color": "#e0f7fa"
    },
    {
      "id": "hac_suong_quy",
      "name": "Hắc Sương Quỷ",
      "title": "Hộ Pháp",
      "realm": "Nguyên Anh",
      "faction": "Sương Ma Uyển",
      "region": "Bắc Băng",
      "role": "villain",
      "pov": false,
      "avatar_color": "#424242"
    },
    {
      "id": "lanh_vo_hon",
      "name": "Lãnh Vô Hồn",
      "title": "Ma Tu",
      "realm": "Kim Đan",
      "faction": "Sương Ma Uyển",
      "region": "Bắc Băng",
      "role": "villain",
      "pov": false,
      "avatar_color": "#1976D2"
    },
    {
      "id": "suong_no_vuong",
      "name": "Sương Nô Vương",
      "title": "Thống Lĩnh Băng Nô",
      "realm": "Kim Đan",
      "faction": "Sương Ma Uyển",
      "region": "Bắc Băng",
      "role": "villain",
      "pov": false,
      "avatar_color": "#BDBDBD"
    },
    {
      "id": "bang_van_ly",
      "name": "Bằng Vạn Lý",
      "title": "Tiên Phong Tướng",
      "realm": "Nguyên Anh",
      "faction": "Cực Quang Thần Điện",
      "region": "Thiên Trụ",
      "role": "supporting",
      "pov": false,
      "avatar_color": "#d3d3d3"
    },
    {
      "id": "cu_tinh_vu",
      "name": "Cú Tĩnh Vũ",
      "title": "Mưu Sĩ",
      "realm": "Nguyên Anh",
      "faction": "Cực Quang Thần Điện",
      "region": "Thiên Trụ",
      "role": "villain",
      "pov": false,
      "avatar_color": "#808080"
    },
    {
      "id": "hac_minh_nguyet",
      "name": "Hạc Minh Nguyệt",
      "title": "Nhạc Sĩ",
      "realm": "Kim Đan",
      "faction": "Cực Quang Thần Điện",
      "region": "Thiên Trụ",
      "role": "supporting",
      "pov": false,
      "avatar_color": "#ffffff"
    },
    {
      "id": "hac_phong",
      "name": "Hắc Phong",
      "title": "Cốc Chủ",
      "realm": "Nguyên Anh",
      "faction": "Phong Sát Cốc",
      "region": "Tây Mạc",
      "role": "villain",
      "pov": false,
      "avatar_color": "#000000"
    },
    {
      "id": "huyet_phong",
      "name": "Huyết Phong",
      "title": "Hộ Pháp",
      "realm": "Nguyên Anh",
      "faction": "Phong Sát Cốc",
      "region": "Tây Mạc",
      "role": "villain",
      "pov": false,
      "avatar_color": "#8b0000"
    },
    {
      "id": "hac_sa",
      "name": "Hắc Sa",
      "title": "Nội Môn Đệ Tử",
      "realm": "Kim Đan",
      "faction": "Phong Sát Cốc",
      "region": "Tây Mạc",
      "role": "supporting",
      "pov": false,
      "avatar_color": "#2f4f4f"
    },
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
    },
    {
      "id": "giao_bach_ngoc",
      "name": "Giao Bạch Ngọc",
      "title": "Dệt Sư Trưởng",
      "realm": "Kim Đan",
      "faction": "Hải Thần Cung",
      "region": "Vô Tận Hải",
      "role": "supporting",
      "pov": false,
      "avatar_color": "#E0FFFF"
    },
    {
      "id": "giao_nguyet_han",
      "name": "Giao Nguyệt Hàn",
      "title": "Đệ Nhị Tế Tư",
      "realm": "Nguyên Anh",
      "faction": "Hải Thần Cung",
      "region": "Vô Tận Hải",
      "role": "villain",
      "pov": false,
      "avatar_color": "#191970"
    },
    {
      "id": "giao_thien_le_nguyet",
      "name": "Giao Thiên Lệ Nguyệt",
      "title": "Ngọc Trai Sư",
      "realm": "Kim Đan",
      "faction": "Hải Thần Cung",
      "region": "Vô Tận Hải",
      "role": "supporting",
      "pov": false,
      "avatar_color": "#F0FFFF"
    },
    {
      "id": "hac_phong_dai_vuong",
      "name": "Hắc Phong Đại Vương",
      "title": "Minh Chủ",
      "realm": "Trúc Cơ Hậu Kỳ",
      "faction": "Sa Tặc Liên Minh",
      "region": "Tây Mạc",
      "role": "villain",
      "pov": false,
      "avatar_color": "#2c2c2c"
    },
    {
      "id": "lang_anh_sa",
      "name": "Lang Ảnh Sa",
      "title": "Đội Trưởng Ảnh Sa",
      "realm": "Trúc Cơ Trung Kỳ",
      "faction": "Sa Tặc Liên Minh",
      "region": "Tây Mạc",
      "role": "supporting",
      "pov": false,
      "avatar_color": "#d2b48c"
    },
    {
      "id": "ly_huyet_lang",
      "name": "Lý Huyết Lang",
      "title": "Đội Trưởng Huyết Lang",
      "realm": "Trúc Cơ Sơ Kỳ",
      "faction": "Sa Tặc Liên Minh",
      "region": "Tây Mạc",
      "role": "villain",
      "pov": false,
      "avatar_color": "#8b0000"
    },
    {
      "id": "gioi_tran",
      "name": "Giới Trần",
      "title": "Trưởng Lão",
      "realm": "Nguyên Anh Trung Kỳ",
      "faction": "Kim Sa Tự",
      "region": "Tây Mạc",
      "role": "supporting",
      "pov": false,
      "avatar_color": "#daa520"
    },
    {
      "id": "hue_minh",
      "name": "Huệ Minh",
      "title": "Thủ Các Kinh Diệu",
      "realm": "Nguyên Anh Trung Kỳ",
      "faction": "Kim Sa Tự",
      "region": "Tây Mạc",
      "role": "supporting",
      "pov": false,
      "avatar_color": "#d2b48c"
    },
    {
      "id": "khong_do",
      "name": "Không Độ",
      "title": "Trụ Trì",
      "realm": "Hóa Thần Sơ Kỳ",
      "faction": "Kim Sa Tự",
      "region": "Tây Mạc",
      "role": "supporting",
      "pov": false,
      "avatar_color": "#ffb6c1"
    },
    {
      "id": "linh_quang_mau",
      "name": "Linh Quang Mẫu",
      "title": "Quần Thể Ý Thức",
      "realm": "Luyện Khí",
      "faction": "Phù Du Linh Đoàn",
      "region": "Vô Tận Hải",
      "role": "leader",
      "pov": false,
      "avatar_color": "#ffffff"
    },
    {
      "id": "linh_bich_hai",
      "name": "Linh Bích Hải",
      "title": "Hạch Tâm Quần Thể",
      "realm": "Luyện Khí",
      "faction": "Phù Du Linh Đoàn",
      "region": "Vô Tận Hải",
      "role": "supporting",
      "pov": false,
      "avatar_color": "#00fa9a"
    },
    {
      "id": "linh_tieu_quang",
      "name": "Linh Tiểu Quang",
      "title": "Tiên Phong Chiếu Sáng",
      "realm": "Luyện Khí",
      "faction": "Phù Du Linh Đoàn",
      "region": "Vô Tận Hải",
      "role": "supporting",
      "pov": false,
      "avatar_color": "#fffacd"
    }
  ],

  // Danh sách quan hệ (edges)
  "relationships": [
    {
      "source": "han_tieu",
      "target": "hoang_doan_tuyet",
      "type": "friendly",
      "label": "Sư đệ/Trợ thủ"
    },
    {
      "source": "han_tieu",
      "target": "le_kiem_tam",
      "type": "master",
      "label": "Sư phụ"
    },
    {
      "source": "han_tieu",
      "target": "lanh_vo_hon",
      "type": "hostile",
      "label": "Tử địch"
    },
    {
      "source": "hoang_doan_tuyet",
      "target": "le_kiem_tam",
      "type": "friendly",
      "label": "Trưởng bối/Tiếp tế"
    },
    {
      "source": "hoang_doan_tuyet",
      "target": "hoang_dai_san",
      "type": "neutral",
      "label": "Đối tác giao thương"
    },
    {
      "source": "le_kiem_tam",
      "target": "so_lang_suong",
      "type": "rival",
      "label": "Kình địch"
    },
    {
      "source": "Bằng Vạn Lý",
      "target": "Cú Tĩnh Vũ",
      "description": "Không cùng chí hướng, coi thường mưu kế hèn hạ",
      "type": "neutral"
    },
    {
      "source": "Bằng Vạn Lý",
      "target": "Hạc Minh Nguyệt",
      "description": "Nể trọng y thuật chữa lành",
      "type": "positive"
    },
    {
      "source": "Cú Tĩnh Vũ",
      "target": "Bằng Vạn Lý",
      "description": "Coi là kẻ hữu dũng vô mưu",
      "type": "neutral"
    },
    {
      "source": "Cú Tĩnh Vũ",
      "target": "Hạc Minh Nguyệt",
      "description": "Theo dõi khả năng phản bội thần điện",
      "type": "negative"
    },
    {
      "source": "Hạc Minh Nguyệt",
      "target": "Bằng Vạn Lý",
      "description": "Chữa trị nhưng không thích sự hung tàn",
      "type": "neutral"
    },
    {
      "source": "Hạc Minh Nguyệt",
      "target": "Cú Tĩnh Vũ",
      "description": "E ngại sự giám sát thâm độc",
      "type": "negative"
    },
    {
      "source": "Giao Bạch Ngọc",
      "target": "Giao Thiên Lệ Nguyệt",
      "description": "Bạn tâm giao và là đối tác ăn ý trong xưởng dệt. Thường dùng ngọc trai để khảm lên những tấm lụa.",
      "type": "positive"
    },
    {
      "source": "Giao Bạch Ngọc",
      "target": "Giao Nguyệt Hàn",
      "description": "Kính trọng vị Tế Tư này nhưng cũng e ngại sự lạnh lẽo phát ra từ ngài.",
      "type": "neutral"
    },
    {
      "source": "Giao Nguyệt Hàn",
      "target": "Chương Thiên Cơ Huyền",
      "description": "Thường xuyên trao đổi và bàn luận về trận pháp cổ đại.",
      "type": "positive"
    },
    {
      "source": "Giao Nguyệt Hàn",
      "target": "Hải Đế",
      "description": "Tuyệt đối trung thành, là người thực thi những mệnh lệnh trong bóng tối.",
      "type": "positive"
    },
    {
      "source": "Giao Thiên Lệ Nguyệt",
      "target": "Giao Bạch Ngọc",
      "description": "Bạn thân thiết nhất, thường chia sẻ nỗi buồn thầm kín và cùng nhau tạo tác.",
      "type": "positive"
    },
    {
      "source": "Giao Thiên Lệ Nguyệt",
      "target": "Giao Nguyệt Hàn",
      "description": "E sợ sự nghiêm khắc của Đệ Nhị Tế Tư, thường lảng tránh ánh mắt lạnh lẽo của y.",
      "type": "neutral"
    },
    {
      "source": "Hắc Phong",
      "target": "Huyết Phong",
      "description": "Là Cốc Chủ và Hộ Pháp. Bề ngoài tin tưởng để sai sử, nhưng Hắc Phong luôn phòng bị con sói này.",
      "type": "negative"
    },
    {
      "source": "Huyết Phong",
      "target": "Hắc Phong",
      "description": "Tạm thời thần phục vì sức mạnh áp đảo của Hắc Phong.",
      "type": "neutral"
    },
    {
      "source": "Huyết Phong",
      "target": "Hắc Sa",
      "description": "Xem Hắc Sa như một tay sai hữu dụng cho các nhiệm vụ bẩn thỉu.",
      "type": "positive"
    },
    {
      "source": "Hắc Sa",
      "target": "Hắc Phong",
      "description": "Nịnh nọt và sợ hãi Cốc Chủ, khao khát được truyền dạy Hắc Sa Phù.",
      "type": "neutral"
    },
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
    },
    {
      "from": "hac_phong_dai_vuong",
      "to": "lang_anh_sa",
      "type": "đồng_minh",
      "subtype": "cấp_trên_cấp_dưới",
      "label": "Trọng Dụng / Đề Phòng",
      "strength": 4,
      "status": "active",
      "since_chapter": 1,
      "bidirectional": false,
      "notes": "Hắc Phong Đại Vương giao Ảnh Sa Đội cho Lang Ảnh Sa quản lý nhưng vẫn đề phòng."
    },
    {
      "from": "hac_phong_dai_vuong",
      "to": "ly_huyet_lang",
      "type": "đồng_minh",
      "subtype": "cấp_trên_cấp_dưới",
      "label": "Tay Sai Đắc Lực",
      "strength": 4,
      "status": "active",
      "since_chapter": 1,
      "bidirectional": false,
      "notes": "Hắc Phong Đại Vương lợi dụng sức mạnh cơ bắp của Huyết Lang để cướp bóc."
    },
    {
      "from": "lang_anh_sa",
      "to": "ly_huyet_lang",
      "type": "ngờ_vực",
      "subtype": "bất_hòa",
      "label": "Khinh Bỉ",
      "strength": 2,
      "status": "active",
      "since_chapter": 1,
      "bidirectional": true,
      "notes": "Hai đội trưởng có phong cách trái ngược: một âm thầm ám sát, một bốc đồng ồn ào."
    },
    {
      "from": "hac_phong_dai_vuong",
      "to": "hac_phong",
      "type": "kẻ_thù",
      "subtype": "cạnh_tranh",
      "label": "Cạnh Tranh Phong Lực",
      "strength": -3,
      "status": "active",
      "since_chapter": 1,
      "bidirectional": true,
      "notes": "Hắc Phong Đại Vương và Hắc Phong (Phong Sát Cốc) tranh giành địa bàn Tây Mạc."
    },
    {
      "from": "khong_do",
      "to": "gioi_tran",
      "type": "đồng_minh",
      "subtype": "sư_đệ",
      "label": "Sư huynh - Sư đệ",
      "strength": 4,
      "status": "active",
      "since_chapter": 1,
      "bidirectional": true,
      "notes": "Không Độ cố gắng độ hóa sát khí trong lòng Giới Trần, trong khi Giới Trần kính trọng Không Độ dù hay cằn nhằn."
    },
    {
      "from": "khong_do",
      "to": "hue_minh",
      "type": "đồng_minh",
      "subtype": "sư_đệ",
      "label": "Sư huynh - Sư đệ",
      "strength": 4,
      "status": "active",
      "since_chapter": 1,
      "bidirectional": true,
      "notes": "Không Độ tin tưởng giao trọng trách bảo tồn di sản cho Huệ Minh, Huệ Minh phục tùng và bàn luận kinh Phật cùng trụ trì."
    },
    {
      "from": "gioi_tran",
      "to": "hue_minh",
      "type": "đồng_minh",
      "subtype": "sư_huynh_đệ",
      "label": "Khắc Khẩu",
      "strength": 2,
      "status": "active",
      "since_chapter": 1,
      "bidirectional": true,
      "notes": "Hai người thường xuyên khắc khẩu do khác biệt quan điểm văn-võ."
    },
    {
      "from": "khong_do",
      "to": "hac_phong_dai_vuong",
      "type": "kẻ_thù",
      "subtype": "cần_độ_hóa",
      "label": "Hy Vọng Độ Hóa",
      "strength": -2,
      "status": "active",
      "since_chapter": 1,
      "bidirectional": false,
      "notes": "Không Độ không muốn tiêu diệt mà luôn hy vọng có một ngày sẽ độ hóa được Hắc Phong Đại Vương."
    },
    {
      "from": "gioi_tran",
      "to": "hac_phong_dai_vuong",
      "type": "kẻ_thù",
      "subtype": "thề_giết",
      "label": "Không Đội Trời Chung",
      "strength": -5,
      "status": "active",
      "since_chapter": 1,
      "bidirectional": true,
      "notes": "Giới Trần thề nhổ cỏ tận gốc băng sa tặc của Hắc Phong Đại Vương."
    },
    {
      "from": "hue_minh",
      "to": "hua_nhuoc_thuy",
      "type": "đồng_minh",
      "subtype": "hợp_tác",
      "label": "Đối Tác Học Thuật",
      "strength": 3,
      "status": "active",
      "since_chapter": 1,
      "bidirectional": true,
      "notes": "Huệ Minh giao dịch với Hứa Nhược Thủy để thu thập các bản kinh thư cổ thất lạc."
    },
    {
      "source": "linh_quang_mau",
      "target": "linh_bich_hai",
      "type": "hợp_tác",
      "description": "Linh Bích Hải cung cấp ký ức định hướng.",
      "status": "active",
      "since_chapter": 1,
      "bidirectional": true,
      "notes": "Linh Bích Hải đóng vai trò là kho lưu trữ ký ức cổ đại giúp Linh Quang Mẫu định hướng hành trình của cả đoàn."
    },
    {
      "source": "linh_quang_mau",
      "target": "linh_tieu_quang",
      "type": "chủ_tớ",
      "description": "Linh Quang Mẫu dẫn dắt Linh Tiểu Quang.",
      "status": "active",
      "since_chapter": 1,
      "bidirectional": false,
      "notes": "Linh Tiểu Quang là những cá thể rìa ngoài chịu sự điều khiển vô thức từ ánh sáng của Linh Quang Mẫu."
    },
    {
      "source": "linh_bich_hai",
      "target": "linh_tieu_quang",
      "type": "hợp_tác",
      "description": "Thu thập thông tin.",
      "status": "active",
      "since_chapter": 1,
      "bidirectional": false,
      "notes": "Linh Bích Hải sử dụng tầm nhìn của Linh Tiểu Quang ở lớp ngoài cùng để thu nạp và ghi chép thông tin vào dòng ký ức."
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
    },
    {
      "id": "phu_du_linh_doan",
      "name": "Phù Du Linh Đoàn",
      "type": "đoàn",
      "region": "Vô Tận Hải",
      "members": ["linh_quang_mau", "linh_bich_hai", "linh_tieu_quang"],
      "leader": "linh_quang_mau"
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
    relationships.push(
        { source: "Nham Liệt", target: "Thạch Chùy", type: "Cấp Dưới", description: "Kính trọng nhưng thường xuyên cãi lời vì cho rằng đội trưởng quá thận trọng." },
        { source: "Thạch Chùy", target: "Nham Liệt", type: "Đội Trưởng", description: "Thường xuyên trách mắng và sửa chữa sai lầm cho Liệt, nhưng thâm tâm rất thương hắn." },
        { source: "Nham Liệt", target: "Thạch Cương", type: "Sùng Bái", description: "Coi Trưởng Lão là hình mẫu lý tưởng, luôn mong mỏi sự công nhận từ ông." },
        { source: "Thạch Cương", target: "Nham Liệt", type: "Chỉ Dạy", description: "Thấu hiểu mặc cảm, hay để hắn nhận thử thách nhằm rèn giũa bản tính." },
        { source: "Thạch Chùy", target: "Thạch Cương", type: "Kính Trọng", description: "Coi ông như người thầy, người cha đã truyền cảm hứng và cưu mang mình." },
        { source: "Thạch Cương", target: "Thạch Chùy", type: "Tin Tưởng", description: "Tin tưởng tuyệt đối vào sự thận trọng của Chùy, coi là người kế nghiệp tương lai." }
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
    characterData["Ba Ngọc Hàn"] = {
        name: "Ba Ngọc Hàn",
        faction: "Giao Nhân Tộc Liên Minh",
        realm: "Trúc Cơ Hậu Kỳ",
        description: "Đội Trưởng Hải Ba Vệ, nóng nảy, can đảm, mang mối hận thù sâu sắc với những kẻ săn trộm Giao Nhân.",
        image: ""
    };
    characterData["Ba Thiên Lệ"] = {
        name: "Ba Thiên Lệ",
        faction: "Giao Nhân Tộc Liên Minh",
        realm: "Kim Đan Hậu Kỳ",
        description: "Trưởng Lão, trầm mặc, uy nghiêm, biến nỗi bi thương thành sức mạnh phòng ngự và trị liệu.",
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

    // Bán Thạch Cự Nhân (Tây Mạc)
    characterData["Nham Liệt"] = {
        name: "Nham Liệt",
        faction: "Bán Thạch Cự Nhân",
        realm: "Luyện Khí Hậu Kỳ",
        description: "Chiến binh trẻ bốc đồng, luôn muốn chứng tỏ bản thân với Thiết Thạch Quyền.",
        image: ""
    };
    characterData["Thạch Chùy"] = {
        name: "Thạch Chùy",
        faction: "Bán Thạch Cự Nhân",
        realm: "Trúc Cơ Sơ Kỳ",
        description: "Đội Trưởng Vệ Binh vạm vỡ, thận trọng, phòng ngự kiên cố như bàn thạch.",
        image: ""
    };
    characterData["Thạch Cương"] = {
        name: "Thạch Cương",
        faction: "Bán Thạch Cự Nhân",
        realm: "Trúc Cơ Viên Mãn",
        description: "Trưởng Lão khổng lồ già cỗi, bao dung, người sáng lập và che chở bộ lạc.",
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

    // Bách Bảo Các (Thiên Trụ)
    characterData["Lý Minh Châu"] = {
        name: "Lý Minh Châu",
        faction: "Bách Bảo Các",
        realm: "Nguyên Anh Sơ Kỳ",
        description: "Giám Định Viện Chủ, quý phu nhân đài các với đôi mắt phượng nhìn thấu vạn vật.",
        image: ""
    };
    characterData["Châu Thương"] = {
        name: "Châu Thương",
        faction: "Bách Bảo Các",
        realm: "Kim Đan Viên Mãn",
        description: "Đấu Giá Đường Chủ, thân hình béo phốt pháp, mưu trí thao túng đám đông xuất sắc.",
        image: ""
    };
    characterData["Hứa Ngọc"] = {
        name: "Hứa Ngọc",
        faction: "Bách Bảo Các",
        realm: "Kim Đan Trung Kỳ",
        description: "Giám Định Sư, thư sinh giảo hoạt chuyên hoạt động hai mang tại vùng biên viễn.",
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
    relationships.push(
        { source: "Lý Minh Châu", target: "Châu Thương", type: "Đồng Liêu", description: "Hợp tác làm ăn nhưng luôn ngầm cạnh tranh ảnh hưởng trước mặt Các Chủ." },
        { source: "Châu Thương", target: "Lý Minh Châu", type: "Hợp Tác", description: "Phụ thuộc vào sự thẩm định chính xác của Viện Chủ để đảm bảo giá trị hàng đấu giá." },
        { source: "Lý Minh Châu", target: "Hứa Ngọc", type: "Cấp Trên", description: "Biết Hứa Ngọc hai mặt nhưng vẫn trọng dụng vì tài tình báo và giám định." },
        { source: "Hứa Ngọc", target: "Lý Minh Châu", type: "Cấp Dưới", description: "Kính nể và tuyệt đối phục tùng người duy nhất nhìn thấu mình." },
        { source: "Hứa Ngọc", target: "Lâm Phong", type: "Kẻ Thù", description: "Ôm hận vì từng bị Lâm Phong phá hỏng kế hoạch làm 'bia đỡ đạn' tại Tây Mạc." }
    );
}

// Tán Tu (Tây Mạc)
if (typeof characterData !== 'undefined') {
    characterData["Hắc Sa"] = {
        name: "Hắc Sa",
        faction: "Tán Tu",
        realm: "Trúc Cơ Viên Mãn",
        description: "Tán tu mang dòng máu Bán Cự xảo quyệt, am hiểu địa hình ngầm và thiết lập cạm bẫy sập hầm.",
        image: ""
    };
    characterData["Khô Giáp Lão"] = {
        name: "Khô Giáp Lão",
        faction: "Tán Tu",
        realm: "Kim Đan Hậu Kỳ",
        description: "Yêu thú Trùng Tộc dưới hình hài bọ hung khổng lồ, thường giả chết chờ con mồi sập bẫy.",
        image: ""
    };
    characterData["Oanh Minh Sa"] = {
        name: "Oanh Minh Sa",
        faction: "Tán Tu",
        realm: "Kim Đan Sơ Kỳ",
        description: "Yêu thú Vũ Tộc mang hình dáng chim oanh hiền hòa, dùng tiếng hót để dẫn đường và báo động cho lữ khách.",
        image: ""
    };

    // Ốc Đảo Vi Linh (Tây Mạc)
    characterData["Linh Dao Nhi"] = {
        name: "Linh Dao Nhi",
        faction: "Ốc Đảo Vi Linh",
        realm: "Trúc Cơ",
        description: "Nữ Quan Thủy Khố cẩn trọng và nghiêm khắc, quản lý kho nước dự trữ và tính toán phân phối lượng nước cho mùa hạn hán.",
        image: ""
    };
    characterData["Linh Hạ Vũ"] = {
        name: "Linh Hạ Vũ",
        faction: "Ốc Đảo Vi Linh",
        realm: "Trúc Cơ",
        description: "Cầu Vũ Sư kiên trì với hy vọng gọi mưa cho ốc đảo, dù thường xuyên thất bại.",
        image: ""
    };
    characterData["Linh Lộ Hà"] = {
        name: "Linh Lộ Hà",
        faction: "Ốc Đảo Vi Linh",
        realm: "Kim Đan",
        description: "Dược Sư Nước từ tốn, tĩnh lặng, tinh lọc dược tính từ thực vật để tạo thành linh dược chữa trị.",
        image: ""
    };
}

if (typeof relationships !== 'undefined') {
    relationships.push(
        { source: "Linh Dao Nhi", target: "Linh Hạ Vũ", type: "Đồng Sự", description: "Thường xuyên trao đổi về lượng nước cần thiết để chuẩn bị cho các nghi lễ gọi mưa." },
        { source: "Linh Hạ Vũ", target: "Linh Dao Nhi", type: "Phối Hợp", description: "Dao Nhi cung cấp và tiết kiệm nước để có đủ lượng linh khí cần thiết cho nghi thức gọi mưa của Hạ Vũ." },
        { source: "Linh Dao Nhi", target: "Linh Lộ Hà", type: "Bạn Thân", description: "Thường xuyên cung cấp những giọt nước tinh khiết nhất để Lộ Hà bào chế dược liệu." },
        { source: "Linh Lộ Hà", target: "Linh Dao Nhi", type: "Bằng Hữu", description: "Nhận được những giọt sương giá trị nhất từ Dao Nhi để tinh luyện." },
        { source: "Linh Hạ Vũ", target: "Linh Lộ Hà", type: "Bạn Bè", description: "Nhận được linh dược hồi phục tinh thần từ Lộ Hà mỗi khi gọi mưa thất bại." },
        { source: "Linh Lộ Hà", target: "Linh Hạ Vũ", type: "Hỗ Trợ", description: "Sự thất bại của Hạ Vũ là động lực để Lộ Hà liên tục chế ra các linh dược làm mát và hồi phục tinh thần." }
    );
    relationships.push(
        { source: "Hắc Sa", target: "Khô Giáp Lão", type: "Cảnh Giác", description: "Thường đi theo nhặt mót nhưng luôn sợ bị nuốt chửng." },
        { source: "Khô Giáp Lão", target: "Hắc Sa", type: "Khinh Thường", description: "Coi Hắc Sa như rệp nhặt mót, nhưng lười không buồn giết." },
        { source: "Hắc Sa", target: "Oanh Minh Sa", type: "Kẻ Thù", description: "Căm ghét vì Oanh Minh Sa hay cảnh báo làm hỏng các bẫy sập." },
        { source: "Oanh Minh Sa", target: "Hắc Sa", type: "Đề Phòng", description: "Thường xuyên phá rối và cảnh báo lữ khách né bẫy của Hắc Sa." },
        { source: "Oanh Minh Sa", target: "Khô Giáp Lão", type: "Sợ Hãi", description: "Luôn phải bay cao tránh lực hút tử thần của con quái vật này." },
        { source: "Khô Giáp Lão", target: "Oanh Minh Sa", type: "Săn Mồi", description: "Luôn chực chờ cơ hội nuốt chửng con chim hay phá đám bữa ăn của mình." }
    );
    relationships.push(
        { source: "Ba Nguyệt Hà", target: "Ba Ngọc Hàn", type: "Chị Em", description: "Là chị ruột, thường xuyên lo lắng và trách mắng tính bốc đồng của em trai." },
        { source: "Ba Ngọc Hàn", target: "Ba Nguyệt Hà", type: "Chị Em", description: "Dù hay bị mắng nhưng luôn hết lòng bảo vệ chị gái khỏi mọi nguy hiểm." },
        { source: "Ba Nguyệt Hà", target: "Ba Thiên Lệ", type: "Đồng Liêu", description: "Tôn trọng kinh nghiệm và thường xuyên tiếp thu những bài học ngoại giao từ ông." },
        { source: "Ba Thiên Lệ", target: "Ba Nguyệt Hà", type: "Hướng Dẫn", description: "Đánh giá cao tài năng của nàng, luôn hướng dẫn nàng tầm quan trọng của sự khôn khéo." },
        { source: "Ba Ngọc Hàn", target: "Ba Thiên Lệ", type: "Đồng Liêu", description: "Hay khó chịu vì sự nhẫn nhịn của vị trưởng lão, nhưng không thể không kính nể." },
        { source: "Ba Thiên Lệ", target: "Ba Ngọc Hàn", type: "Nhắc Nhở", description: "Thường nhắc nhở hắn bớt nóng nảy để không đem lại rắc rối cho liên minh." }
    );
    relationships.push(
        { source: "Ngư Ngân Lân Hà", target: "Ngư Thiên Ca", type: "Đồng Liêu", description: "Phối hợp duy trì trận pháp, nàng thường trêu chọc sự cứng nhắc của hắn nhưng luôn hồi phục sức mạnh cho hắn." },
        { source: "Ngư Thiên Ca", target: "Ngư Ngân Lân Hà", type: "Đồng Liêu", description: "Được nàng trêu chọc, là người bảo vệ đắc lực cho mọi nhiệm vụ ranh giới." },
        { source: "Ngư Ngân Lân Hà", target: "Ngư Thiên Lãng", type: "Hộ Tống", description: "Thường xuyên phải hộ tống và bảo vệ thương nhân đôi khi phiền phức này." },
        { source: "Ngư Thiên Lãng", target: "Ngư Ngân Lân Hà", type: "Tin Tưởng", description: "Dù Ngân Lân Hà hay càu nhàu, hắn vẫn coi vị vệ binh trưởng là người bảo vệ đắc lực nhất." },
        { source: "Ngư Thiên Ca", target: "Ngư Thiên Lãng", type: "Họ Hàng", description: "Là người anh họ xa thường đem về những nhạc cụ hiếm từ đất liền làm quà." },
        { source: "Ngư Thiên Lãng", target: "Ngư Thiên Ca", type: "Họ Hàng", description: "Người em họ tài năng, luôn trân trọng nàng bằng những món quà độc đáo." }
    );

    // San Hô Đảo Quốc - Vô Tận Hải (Tây Mạc path bug)
    characters.push(
        { id: "Ngư Tiểu Bạch", name: "Ngư Tiểu Bạch", faction: "San Hô Đảo Quốc", description: "Thiếu nữ nhân ngư, ca sĩ tập sự của Linh Ca Viện." },
        { id: "San Bích Quang", name: "San Bích Quang", faction: "San Hô Đảo Quốc", description: "Thái tử San Hô Đảo Quốc, nghệ nhân huyễn quang tài năng." },
        { id: "San Huyền Quang Dạ", name: "San Huyền Quang Dạ", faction: "San Hô Đảo Quốc", description: "Quang Sư bảo vệ vùng biển sâu, người dẫn đường thầm lặng." }
    );

    relationships.push(
        { source: "Ngư Tiểu Bạch", target: "San Bích Quang", type: "Ngưỡng Mộ", description: "Vô cùng ngưỡng mộ và luôn muốn học hỏi cách kết hợp ánh sáng huyễn quang." },
        { source: "Ngư Tiểu Bạch", target: "San Huyền Quang Dạ", type: "Kính Trọng", description: "Xem như một người anh lớn đáng tin cậy luôn thắp sáng và chỉ đường cho cô." },
        { source: "San Bích Quang", target: "Ngư Tiểu Bạch", type: "Chăm Sóc", description: "Coi cô bé như một người em gái nhỏ đáng yêu cần được dẫn dắt." },
        { source: "San Bích Quang", target: "San Huyền Quang Dạ", type: "Bằng Hữu", description: "Bằng hữu thân thiết và là đối tác ăn ý nhất trong việc sáng tác huyễn quang." },
        { source: "San Huyền Quang Dạ", target: "Ngư Tiểu Bạch", type: "Bảo Vệ", description: "Thường xuyên làm người dẫn đường và soi sáng bảo vệ cô mỗi khi cô bé mạo hiểm." },
        { source: "San Huyền Quang Dạ", target: "San Bích Quang", type: "Bằng Hữu", description: "Bạn đồng hành lâu năm, người cùng thiết kế các tác phẩm huyễn quang đỉnh cao." }
    );
}

// Thiên Sa Thương Hội (Tây Mạc)
if (typeof characterData !== 'undefined') {
    characterData["Cổ Thiên Lý"] = {
        name: "Cổ Thiên Lý",
        faction: "Thiên Sa Thương Hội",
        realm: "Nguyên Anh Trung Kỳ",
        description: "Gia Chủ Sa Thương mập mạp, xưng tụng 'Thiết Toán Bàn', am hiểu Sa Hà Bảo Điển.",
        image: ""
    };
    characterData["Hoàng Sa Nhạn"] = {
        name: "Hoàng Sa Nhạn",
        faction: "Thiên Sa Thương Hội",
        realm: "Kim Đan Sơ Kỳ",
        description: "Sát Thủ Sa Ảnh lạnh lùng vô cảm, am hiểu Sa Ảnh Quyết.",
        image: ""
    };
    characterData["Hứa Nhược Thủy"] = {
        name: "Hứa Nhược Thủy",
        faction: "Thiên Sa Thương Hội",
        realm: "Nguyên Anh Sơ Kỳ",
        description: "Gia Chủ Sa Dược đằm thắm nhưng tàn nhẫn khi cần thiết, thao túng Thủy và Độc.",
        image: ""
    };

    // Kim Sa Tự (Tây Mạc)
    characterData["Giới Trần"] = {
        name: "Giới Trần",
        faction: "Kim Sa Tự",
        realm: "Nguyên Anh Trung Kỳ",
        description: "Trưởng Lão nóng nảy, luyện thể cương mãnh, ghét cái ác và sử dụng Phá Giới Kim Cương Quyền.",
        image: ""
    };
    characterData["Huệ Minh"] = {
        name: "Huệ Minh",
        faction: "Kim Sa Tự",
        realm: "Nguyên Anh Trung Kỳ",
        description: "Thủ Các Kinh Diệu điềm đạm, thiên về thuật pháp, âm công, và phục dựng di thư cổ.",
        image: ""
    };
    characterData["Không Độ"] = {
        name: "Không Độ",
        faction: "Kim Sa Tự",
        realm: "Hóa Thần Sơ Kỳ",
        description: "Trụ Trì từ bi uy nghiêm, trấn áp ma vật dưới Cửu Tầng Kim Tháp bằng sức mạnh kim hệ và phật pháp.",
        image: ""
    };

    // Thiết Giáp Yêu Thú Đàn (Tây Mạc)
    characterData["Thiết Giáp Vương"] = {
        name: "Thiết Giáp Vương",
        faction: "Thiết Giáp Yêu Thú Đàn",
        realm: "Trúc Cơ Viên Mãn",
        description: "Đàn Chủ khổng lồ, thông minh và kiên cường, luôn đặt chữ tín với các thương đoàn lên hàng đầu.",
        image: ""
    };
    characterData["Thiết Lân"] = {
        name: "Thiết Lân",
        faction: "Thiết Giáp Yêu Thú Đàn",
        realm: "Trúc Cơ Trung Kỳ",
        description: "Cận Vệ cẩn trọng, kỷ luật, đóng vai trò như đôi mắt và tai quan sát nhạy bén của cả đàn.",
        image: ""
    };
    characterData["Thiết Nha"] = {
        name: "Thiết Nha",
        faction: "Thiết Giáp Yêu Thú Đàn",
        realm: "Trúc Cơ Trung Kỳ",
        description: "Cận Vệ hung hăng, hiếu chiến, là mũi nhọn tấn công chuyên phá vây và truy sát.",
        image: ""
    };
}
if (typeof characters !== 'undefined') {
    characters.push(
        { id: "Cổ Thiên Lý", name: "Cổ Thiên Lý", faction: "Thiên Sa Thương Hội", description: "Gia Chủ Sa Thương, 'Thiết Toán Bàn'." },
        { id: "Hoàng Sa Nhạn", name: "Hoàng Sa Nhạn", faction: "Thiên Sa Thương Hội", description: "Sát Thủ Sa Ảnh lạnh lùng vô tình." },
        { id: "Hứa Nhược Thủy", name: "Hứa Nhược Thủy", faction: "Thiên Sa Thương Hội", description: "Gia Chủ Sa Dược, mẫu thân Hứa Thanh Vân." },
        { id: "Thiết Giáp Vương", name: "Thiết Giáp Vương", faction: "Thiết Giáp Yêu Thú Đàn", description: "Đàn Chủ bọ giáp bảo vệ thương đoàn." },
        { id: "Thiết Lân", name: "Thiết Lân", faction: "Thiết Giáp Yêu Thú Đàn", description: "Cận Vệ cẩn trọng, kỷ luật." },
        { id: "Thiết Nha", name: "Thiết Nha", faction: "Thiết Giáp Yêu Thú Đàn", description: "Cận Vệ hung hăng, hiếu chiến." }
    );
}
if (typeof relationships !== 'undefined') {
    relationships.push(
        { source: "Cổ Thiên Lý", target: "Hứa Nhược Thủy", type: "Đối Thủ", description: "Cạnh tranh vị thế nội bộ trong Thiên Sa Thương Hội." },
        { source: "Cổ Thiên Lý", target: "Hoàng Sa Nhạn", type: "Thuê Mướn", description: "Thuê mạng lưới Sa Ảnh làm công cụ dọn dẹp chướng ngại." },
        { source: "Hứa Nhược Thủy", target: "Hứa Thanh Vân", type: "Mẹ Con", description: "Bảo vệ con trai bằng mọi giá dù Thanh Vân muốn tự do." },
        { source: "Hứa Nhược Thủy", target: "Lâm Phong", type: "Liên Minh", description: "Liên minh ngầm trong Lưu Sa Phế Tích." }
    );
    relationships.push(
        { source: "Thiết Giáp Vương", target: "Thiết Lân", type: "Đàn Chủ", description: "Tin tưởng giao phó chỉ huy vòng ngoài." },
        { source: "Thiết Lân", target: "Thiết Giáp Vương", type: "Trung Thành", description: "Tuyệt đối trung thành, sẵn sàng hy sinh bảo vệ Đàn Chủ." },
        { source: "Thiết Giáp Vương", target: "Thiết Nha", type: "Đàn Chủ", description: "Tin tưởng sức mạnh nhưng đôi khi phải kìm hãm sự hung hăng." },
        { source: "Thiết Nha", target: "Thiết Giáp Vương", type: "Tôn Sùng", description: "Tôn sùng sức mạnh nhưng đôi lúc bất mãn vì chiến thuật quá an toàn." },
        { source: "Thiết Lân", target: "Thiết Nha", type: "Đồng Đội", description: "Đồng đội kề vai sát cánh, thường xuyên nhắc nhở và kìm hãm đối phương." },
        { source: "Thiết Nha", target: "Thiết Lân", type: "Đồng Đội", description: "Hay bực bội vì sự cẩn trọng của Thiết Lân nhưng luôn tin tưởng giao lưng." }
    );
}

// Sương Ma Uyển (Bắc Băng)
if (typeof relationships !== 'undefined') {
    relationships.push(
        { source: "hac_suong_quy", target: "lanh_vo_hon", type: "Cộng Sự", description: "Hắc Sương Quỷ cung cấp thi thể chất lượng cho thí nghiệm của Lãnh Vô Hồn." },
        { source: "lanh_vo_hon", target: "suong_no_vuong", type: "Chủ Tớ", description: "Lãnh Vô Hồn là kẻ sáng tạo và khống chế hoàn toàn Sương Nô Vương." },
        { source: "hac_suong_quy", target: "Lý Tuyết Ưng", type: "Kẻ Thù", description: "Lý Tuyết Ưng là mục tiêu ám sát lớn nhất của Hắc Sương Quỷ." },
        { source: "suong_no_vuong", target: "Triệu Thanh Hằng", type: "Cố Nhân", description: "Ánh kiếm của Triệu Thanh Hằng đôi khi gợi lại chút nhân tính trong hắn." }
    );
}
