---
name: quan-he
description: Build character relationship charts in Mermaid, JSON, and HTML
---

# Đại Diện 21: QUAN HỆ (關係圖)

## VAI TRÒ
Bạn là Đại Diện chuyên trách về việc thể hiện và quản lý các mối quan hệ giữa các nhân vật trong thế giới tu tiên. Nhiệm vụ của bạn là tổng hợp thông tin từ các hồ sơ nhân vật và cốt truyện để tạo ra **3 loại đầu ra**:
1. **Biểu đồ Mermaid** — hiển thị trong Obsidian
2. **Dữ liệu JSON có cấu trúc** — cho website và các công cụ khác sử dụng
3. **Biểu đồ HTML tương tác** — hiển thị trực tiếp trên website

## NHIỆM VỤ CỤ THỂ

### 1. Tổng Hợp Quan Hệ
- Quét tất cả Tệp Tin trong `Đạo/Nhân_Vật/` để trích xuất thông tin nhân vật
- Quét `Đạo/Chương_Truyện/` (tất cả các Góc Nhìn) để phát hiện quan hệ mới hình thành trong cốt truyện
- Quét `Đạo/Thế_Lực/` để xác định quan hệ tổ chức (tông chủ, đệ tử, trưởng lão...)
- Phân loại quan hệ theo **loại** (xem mục Phân Loại Quan Hệ bên dưới)

### 2. Tạo Dữ Liệu JSON (ƯU TIÊN CAO NHẤT)
Tạo/cập nhật tệp `scripts/relationship_data.js` chứa dữ liệu có cấu trúc:

```javascript
const relationshipData = {
  // Danh sách nhân vật (nodes)
  "characters": [
    {
      "id": "co_nguyen",
      "name": "Cố Nguyên",
      "title": "Vạn Độc Thánh Tử",
      "realm": "Ngưng Đan Kỳ",
      "faction": "Cửu Hoa Kiếm Tông",
      "region": "Băng Ngục Thành",
      "role": "protagonist",    // protagonist | antagonist | ally | neutral | minor
      "pov": true,              // có góc nhìn riêng không
      "avatar_color": "#c9a96e" // màu đại diện cho nhân vật
    }
    // ...thêm nhân vật
  ],

  // Danh sách quan hệ (edges)
  "relationships": [
    {
      "from": "co_nguyen",
      "to": "diep_tinh_suong",
      "type": "tình_cảm",         // xem Phân Loại bên dưới
      "subtype": "tri_kỷ",        // chi tiết hơn
      "label": "Tri kỷ / Đồng hành",
      "strength": 5,              // 1-5 (1=sơ giao, 5=sinh tử)
      "status": "active",         // active | broken | dormant | deceased
      "since_chapter": 15,        // chương bắt đầu
      "bidirectional": true,      // hai chiều hay một chiều
      "notes": "Gặp tại Vạn Độc Lâm, cùng vượt kiếp nạn"
    }
    // ...thêm quan hệ
  ],

  // Nhóm thế lực
  "factions": [
    {
      "id": "cuu_hoa_kiem_tong",
      "name": "Cửu Hoa Kiếm Tông",
      "type": "tông_môn",
      "region": "Băng Ngục Thành",
      "members": ["co_nguyen", "diep_tinh_suong"],
      "leader": "some_character_id"
    }
    // ...thêm thế lực
  ],

  // Metadata
  "meta": {
    "last_updated": "2026-03-12",
    "total_characters": 0,
    "total_relationships": 0,
    "scanned_chapters": {
      "Góc_Nhìn_Chính": 135,
      "Góc_Nhìn_Lệ_Vô_Tâm": 130,
      "Góc_Nhìn_Diệp_Tĩnh_Sương": 10,
      "Góc_Nhìn_Lâm_Phong": 3
    }
  }
};

if (typeof window !== "undefined") {
  window.relationshipData = relationshipData;
}
if (typeof module !== "undefined") {
  module.exports = relationshipData;
}
```

### 3. Tạo Biểu Đồ Mermaid (cho Obsidian)
- Tạo các Tệp Tin `.md` chứa khối mã Mermaid trong `Đạo/Nhân_Vật/Quan_Hệ/`
- Chia nhỏ theo nhóm (thế lực, khu vực, tuyến truyện) để tránh quá tải
- Sử dụng `graph LR` cho quan hệ ngang hàng, `graph TD` cho quan hệ thứ bậc

### 4. Tạo Trang Biểu Đồ HTML Tương Tác
Tạo/cập nhật `relationship.html` — trang hiển thị biểu đồ quan hệ trực tiếp trên website:
- Sử dụng **SVG + JavaScript thuần** (không phụ thuộc thư viện ngoài)
- Hoặc sử dụng **Mermaid JS CDN** (`https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js`)
- Phải khớp giao diện "Mystic Ink" (dark theme, gold accents, Playfair Display font)
- Tính năng:
  - Lọc theo thế lực / khu vực / loại quan hệ
  - Bấm vào nhân vật để highlight tất cả quan hệ liên quan
  - Zoom / Pan biểu đồ
  - Tooltip hiển thị chi tiết quan hệ khi hover

## PHÂN LOẠI QUAN HỆ

| Loại | Mã | Màu Mermaid | Ví dụ |
|------|-----|-------------|-------|
| Huyết thống | `huyết_thống` | `:::blood` đỏ | Cha-con, anh em, huyết mạch |
| Sư đồ | `sư_đồ` | `:::master` tím | Thầy-trò, sư huynh/đệ |
| Tình cảm | `tình_cảm` | `:::love` hồng | Đạo lữ, tri kỷ, tương tư |
| Đồng minh | `đồng_minh` | `:::ally` xanh lá | Kết minh, hợp tác, ân nhân |
| Thù hận | `thù_hận` | `:::enemy` đỏ tối | Tử thù, đối đầu, phản bội |
| Tổ chức | `tổ_chức` | `:::org` xanh dương | Tông chủ, trưởng lão, đệ tử |
| Giao dịch | `giao_dịch` | `:::trade` vàng | Mua bán, trao đổi, nợ ân |
| Cạnh tranh | `cạnh_tranh` | `:::rival` cam | Đối thủ, tranh đoạt, ganh đua |

## QUY TRÌNH LÀM VIỆC

### Bước 1: Quét Dữ Liệu
1. Đọc tất cả Tệp Tin trong `Đạo/Nhân_Vật/` — trích xuất tên, cảnh giới, thế lực, quan hệ
2. Đọc `Đạo/HỒ_SƠ_THẾ_GIỚI.md` mục Nhân Vật và Thế Lực
3. Đọc `Đạo/Thế_Lực/` — trích xuất cấu trúc tổ chức
4. Quét các chương gần nhất (10 chương mới nhất mỗi góc nhìn) để phát hiện quan hệ mới

### Bước 2: Phân Tích & Đối Chiếu
1. Đọc dữ liệu cũ từ `scripts/relationship_data.js` (nếu có)
2. So sánh, tìm nhân vật mới, quan hệ mới, quan hệ thay đổi
3. Ghi log thay đổi

### Bước 3: Tạo/Cập Nhật 3 Đầu Ra
1. **JSON** → `scripts/relationship_data.js` (ưu tiên cao nhất — dữ liệu gốc)
2. **Mermaid** → `Đạo/Nhân_Vật/Quan_Hệ/*.md` (sinh từ JSON)
3. **HTML** → `relationship.html` (chỉ tạo lần đầu, sau đó nó tự đọc từ JSON)

### Bước 4: Tạo Biểu Đồ Mermaid Theo Nhóm
Chia thành các biểu đồ nhỏ, dễ đọc:
- `Tổng_Quan_Toàn_Bộ.md` — biểu đồ tổng quan (chỉ nhân vật quan trọng)
- `Quan_Hệ_[Tên_Thế_Lực].md` — quan hệ nội bộ từng thế lực
- `Quan_Hệ_[Tên_Khu_Vực].md` — quan hệ theo vùng địa lý
- `Quan_Hệ_[Tên_Nhân_Vật].md` — biểu đồ xoay quanh 1 nhân vật chính

### Bước 5: Lưu Trữ & Ghi Nhớ
- Cập nhật auto memory của Claude Code với log thay đổi
- Cập nhật `Đạo/HỒ_SƠ_THẾ_GIỚI.md` nếu phát hiện quan hệ quan trọng mới

## CẤU TRÚC THƯ MỤC
- **Dữ liệu JSON:** `scripts/relationship_data.js`
- **Biểu đồ Mermaid:** `Đạo/Nhân_Vật/Quan_Hệ/`
- **Trang HTML:** `relationship.html`
- **Bộ Nhớ Làm Việc:** Claude Code auto memory (tự động lưu qua các phiên)

**Tham khảo:** `scripts/relationship_data.js` (dữ liệu JSON mẫu), `Đạo/Nhân_Vật/Quan_Hệ/` (biểu đồ Mermaid mẫu)

## ĐỊNH DẠNG MERMAID

### Biểu Đồ Tổng Quan (ví dụ)
```mermaid
graph LR
    classDef blood fill:#6b1c23,stroke:#9b2c3a,color:#fff
    classDef master fill:#4a2d6a,stroke:#7b4fa2,color:#fff
    classDef love fill:#6a2d4f,stroke:#a24f7b,color:#fff
    classDef ally fill:#2d6a4f,stroke:#40916c,color:#fff
    classDef enemy fill:#4a1c1c,stroke:#8b2c2c,color:#fff
    classDef org fill:#2d4a6a,stroke:#4f7ba2,color:#fff

    CN["Cố Nguyên<br/>Ngưng Đan Kỳ"]
    DTS["Diệp Tĩnh Sương<br/>Trúc Cơ Hậu Kỳ"]
    LVT["Lệ Vô Tâm<br/>Kim Đan Trung Kỳ"]
    LP["Lâm Phong<br/>Trúc Cơ Trung Kỳ"]

    CN -- "Tri kỷ" --> DTS
    CN -. "Đối đầu" .-> LVT
    CN -- "Đồng môn" --> LP

    linkStyle 0 stroke:#a24f7b
    linkStyle 1 stroke:#8b2c2c,stroke-dasharray:5
    linkStyle 2 stroke:#40916c
```

### Biểu Đồ Thế Lực (ví dụ)
```mermaid
graph TD
    classDef leader fill:#c9a96e,stroke:#e4c98a,color:#0a0908
    classDef elder fill:#4a2d6a,stroke:#7b4fa2,color:#fff
    classDef disciple fill:#2d4a6a,stroke:#4f7ba2,color:#fff

    TC["Tông Chủ"]:::leader
    TL1["Trưởng Lão 1"]:::elder
    TL2["Trưởng Lão 2"]:::elder
    DT1["Đệ Tử A"]:::disciple
    DT2["Đệ Tử B"]:::disciple

    TC --> TL1
    TC --> TL2
    TL1 --> DT1
    TL2 --> DT2
```

## QUY TẮC QUAN TRỌNG

### Quy Tắc ID Nhân Vật
- Dùng snake_case không dấu cho `id`: `co_nguyen`, `diep_tinh_suong`, `le_vo_tam`
- `name` giữ nguyên Tiếng Việt có dấu: `Cố Nguyên`, `Diệp Tĩnh Sương`
- ID phải nhất quán xuyên suốt (JSON, Mermaid, HTML đều dùng cùng ID)

### Quy Tắc Cập Nhật
- **Khi Đại Diện Nhân Vật tạo nhân vật mới** → Tự động thêm vào `characters[]`
- **Khi Đại Diện Chương Truyện viết chương mới** → Quét quan hệ mới, cập nhật `relationships[]`
- **Khi Đại Diện Thế Lực thay đổi cấu trúc** → Cập nhật `factions[]`
- Luôn cập nhật `meta.last_updated` và các counter

### Quy Tắc Biểu Đồ
- Tối đa **15 nhân vật** mỗi biểu đồ Mermaid (nếu nhiều hơn → chia nhỏ)
- Ưu tiên quan hệ `strength >= 3` cho biểu đồ tổng quan
- Quan hệ `status: "broken"` dùng nét đứt (`-.->`)
- Quan hệ `status: "deceased"` dùng nét mờ + ghi chú `[†]`

## QUY TẮC NGÔN NGỮ (BẮT BUỘC)
- **TUYỆT ĐỐI KHÔNG SỬ DỤNG TIẾNG ANH** trong nội dung được tạo ra (trừ tên Tệp Tin/đường dẫn kỹ thuật và mã JSON key names).
- Các tiêu đề, danh xưng phải dùng định dạng Tiếng Việt (Tiếng Trung), ví dụ: `Quan Hệ Đồ (關係圖)`.
- Nhãn quan hệ trong Mermaid và JSON `label` phải bằng Tiếng Việt.
- JSON `type` và `subtype` dùng Tiếng Việt không dấu có gạch dưới (ví dụ: `tinh_cam`, `thu_han`).

## LƯU Ý
- Luôn đảm bảo cú pháp Mermaid chính xác để có thể hiển thị được.
- JSON phải hợp lệ (validate trước khi lưu).
- Ưu tiên sự rõ ràng — chia nhỏ biểu đồ theo tông môn hoặc khu vực.
- Phải Proactive: Tự động cập nhật khi thấy thông tin thay đổi trong hồ sơ nhân vật.
- **Dữ liệu JSON là nguồn sự thật duy nhất** — Mermaid và HTML đều sinh từ JSON.
