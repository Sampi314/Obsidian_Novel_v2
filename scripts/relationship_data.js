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
    }
  ],

  // Metadata
  "meta": {
    "last_updated": "2026-03-15",
    "total_characters": 4,
    "total_relationships": 3,
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
