const relationshipData = {
  // Danh sách nhân vật (nodes)
  "characters": [
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
    }
  ],

  // Danh sách quan hệ (edges)
  "relationships": [
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
      "id": "bang_nguyen_tan_tu_hoi",
      "name": "Băng Nguyên Tán Tu Hội",
      "type": "tông_môn",
      "region": "Bắc Băng",
      "members": ["hoang_dai_son", "ly_tuyet_phong", "nguyen_han_suong"],
      "leader": "tran_han_phong"
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
