# RELATIONSHIP AUDIT & FIX PLAN

> **Mục tiêu:** Đảm bảo MỌI mối quan hệ nhân vật trong `Đạo/Nhân_Vật/` là **hai chiều** (bidirectional).
> Nếu Nhân Vật A liệt kê Nhân Vật B trong quan hệ, thì B cũng PHẢI liệt kê A.

---

## VẤN ĐỀ HIỆN TẠI

- ~1,777 nhân vật trong `Đạo/Nhân_Vật/[Khu_Vực]/[Phe_Phái]/[Tên].md`
- Mỗi nhân vật có quan hệ trong 2 nơi:
  1. **YAML frontmatter** → `arcs[0].relationships[]` (có `feelings` scores)
  2. **Markdown Section VI** (QUAN HỆ) → mô tả chi tiết bằng văn xuôi
- Nhiều quan hệ chỉ **một chiều**: A→B có nhưng B→A không có
- Ví dụ: Lệ Vô Tâm liệt kê Diệp Tĩnh Sương là kẻ thù, nhưng Diệp Tĩnh Sương có thể không liệt kê Lệ Vô Tâm

---

## QUY TRÌNH THỰC HIỆN (Từng nhân vật)

### Bước 1: Chọn nhân vật để audit
- Ưu tiên nhân vật chính trước (Lâm Phong, Lệ Vô Tâm, Diệp Tĩnh Sương, A Ngốc, v.v.)
- Sau đó đến nhân vật phụ quan trọng
- Cuối cùng là nhân vật nền

### Bước 2: Đọc file nhân vật
- Đọc YAML `arcs[0].relationships[]` → ghi lại tất cả tên nhân vật được nhắc đến
- Đọc Section VI (QUAN HỆ) trong markdown → ghi lại tất cả tên nhân vật được nhắc đến
- So sánh 2 danh sách: nếu có tên trong markdown mà không có trong YAML → thêm vào YAML

### Bước 3: Kiểm tra từng nhân vật được nhắc đến
Với MỖI nhân vật B mà A nhắc đến:
1. Tìm file của B: `Đạo/Nhân_Vật/*/[Phe]/[Tên_B].md`
2. Đọc YAML relationships của B
3. Kiểm tra: B có liệt kê A không?
4. Nếu **KHÔNG** → Thêm A vào YAML relationships của B với feelings phù hợp

### Bước 4: Tạo feelings đối xứng (RECIPROCAL)
Khi thêm quan hệ ngược, feelings KHÔNG được copy y hệt — phải có logic:

| Loại quan hệ A→B | B→A feelings |
|-------------------|-------------|
| **Sư phụ → Đệ tử** | B: kinh 70-90, tin 60-80, on 50-70, so 10-30 |
| **Đệ tử → Sư phụ** | B: tin 50-70, yeu 10-30, kinh 0-10 |
| **Kẻ thù (mạnh → yếu)** | B: han 50-80, so 30-60, tin -60 to -90, on -50 to -100 |
| **Kẻ thù (ngang sức)** | B: han 60-90, kinh 10-30, tin -70 to -90, so 0-20 |
| **Đồng đội/Chiến hữu** | B: tin 50-80, kinh 20-40, on 10-30 (gần giống A) |
| **Gia đình (cha → con)** | B: yeu tương tự, kinh cao hơn, on cao hơn |
| **Thủ lĩnh → Thuộc hạ** | B: kinh 60-80, tin 60-80, so 10-20, on 30-50 |

### Bước 5: Cập nhật cả YAML và Section VI
- Thêm entry mới vào YAML `arcs[0].relationships[]`
- Thêm mô tả vào Section VI markdown (nếu chưa có)

---

## FORMAT YAML RELATIONSHIP (chuẩn Lệ Vô Tâm)

```yaml
arcs:
  - arc: 1
    relationships:
      - character: Tên Nhân Vật
        description: Mô tả quan hệ bằng Tiếng Việt (1-2 câu)
        feelings:
          yeu: 0      # Yêu/Ghét (-100 đến +100)
          han: 0      # Hận (-100 đến +100)
          kinh: 0     # Kính/Khinh (-100 đến +100)
          tin: 0      # Tin/Nghi (-100 đến +100)
          so: 0       # Sợ (-100 đến +100)
          on: 0       # Ơn/Oán (-100 đến +100)
```

---

## DANH SÁCH NHÂN VẬT CẦN AUDIT (Thứ tự ưu tiên)

### Tier 1 — Nhân Vật Chính (CẦN LÀM TRƯỚC)
- [ ] Lâm Phong (Tán Tu) — nhân vật chính
- [ ] Lệ Vô Tâm (Vạn Độc Môn) — phản diện chính ← **ĐANG LÀM**
- [ ] Diệp Tĩnh Sương (Cửu Hoa Kiếm Tông)
- [ ] A Ngốc (Tán Tu) — nhân vật đặc biệt
- [ ] Nam Cương (nhân vật chính khu vực)
- [ ] Độc Cô Lão Quái (Vạn Độc Môn)

### Tier 2 — Nhân Vật Phụ Quan Trọng (19 POV characters)
- [x] Đan Dương Tử (Đan Hà Cốc)
- [ ] Diệp Thanh Y
- [x] Hắc Hạt Ma Trùng
- [x] Hàn Thanh Nguyệt
- [ ] Lục Trần
- [ ] Ngô Công Trưởng Lão
- [ ] Phương Vô Kỵ
- [ ] Sở Lăng Sương
- [ ] Triệu Thanh Hằng
- [ ] Lục Ly
- [ ] Nguyệt Dao
- [ ] Nham Thần
- [ ] Lục Tiêu
- [ ] Lệ Nhược Thủy
- [ ] Ngao Đình
- [ ] Hứa Nhược Thủy
- [ ] Hứa Thanh Vân
- [ ] Lý Tuyết Ưng
- [ ] Bắc Băng (nhân vật chính khu vực)

### Tier 3 — Nhân Vật Nền (Theo phe phái)
- [ ] Hàn Dân Hộ Vệ Đội (Bắc Băng) — 6 nhân vật ← **ĐÃ LÀM MỘT PHẦN**
- [ ] Vạn Độc Môn (Nam Cương)
- [ ] Đan Hà Cốc (Nam Cương)
- [ ] Cửu Hoa Kiếm Tông
- [ ] Huyền Băng Cung (Bắc Băng)
- [ ] Hải Thần Cung (Vô Tận Hải)
- [ ] Long Cung (Vô Tận Hải)
- [ ] Đại Càn Hoàng Triều (Thiên Trụ)
- [ ] ... (tất cả các phe phái còn lại)

---

## VÍ DỤ THỰC TẾ

### Case: Lệ Vô Tâm → Diệp Tĩnh Sương

**Lệ Vô Tâm liệt kê:**
```yaml
- character: Diệp Tĩnh Sương
  description: Kẻ thù ám ảnh, muốn bắt làm Độc Nô
  feelings:
    yeu: -30
    han: 80
    kinh: 30
    tin: -80
    so: 0
    on: -100
```

**Diệp Tĩnh Sương CẦN liệt kê ngược:**
```yaml
- character: Lệ Vô Tâm
  description: Kẻ thù nguy hiểm nhất, tên độc tu tàn nhẫn luôn muốn bắt nàng làm Độc Nô
  feelings:
    yeu: -50
    han: 70
    kinh: 20
    tin: -90
    so: 30
    on: -80
```

Logic: Diệp Tĩnh Sương cũng ghét (han:70) nhưng có chút sợ (so:30) vì Lệ Vô Tâm dùng độc rất nguy hiểm. Nàng khinh hắn (kinh:20 thấp) nhưng không tin tưởng (tin:-90).

---

## QUY TẮC QUAN TRỌNG

1. **KHÔNG xóa** quan hệ hiện có — chỉ THÊM quan hệ thiếu
2. **KHÔNG thay đổi** feelings đã có — chỉ thêm feelings cho quan hệ mới
3. **Tên nhân vật** trong `character:` field phải khớp CHÍNH XÁC với field `name:` trong YAML của nhân vật đó
4. **Description** phải viết bằng Tiếng Việt
5. **Feelings** phải có logic — không random, phải phản ánh mối quan hệ thực tế trong cốt truyện
6. Sau khi sửa, chạy `python scripts/sync_relationship_data.py` để cập nhật `relationship_data.js` cho frontend

---

## CÁCH TÌM FILE NHÂN VẬT

```
Đạo/Nhân_Vật/
├── Nam_Cương/[Phe_Phái]/[Tên].md
├── Bắc_Băng/[Phe_Phái]/[Tên].md
├── Thiên_Trụ/[Phe_Phái]/[Tên].md
├── Đông_Hoang/[Phe_Phái]/[Tên].md
├── Vô_Tận_Hải/[Phe_Phái]/[Tên].md
├── Tây_Mạc/[Phe_Phái]/[Tên].md
└── Tán_Tu/[Loại]/[Tên].md
```

Dùng glob: `Đạo/Nhân_Vật/**/Tên_Nhân_Vật.md`
Tên file = tên nhân vật với `_` thay khoảng trắng (có dấu Tiếng Việt).

---

## TIẾN ĐỘ

> Cập nhật phần này mỗi khi hoàn thành audit cho một nhóm nhân vật.

| Ngày | Agent | Nhân Vật Đã Audit | Ghi Chú |
|------|-------|-------------------|---------|
| 2026-03-20 | Claude Code | Lệ Vô Tâm (đang làm) | Đang kiểm tra Độc Cô Lão Quái, Diệp Tĩnh Sương, Lâm Phong |
| 2026-03-20 | Claude Code | Nam Cương main cast (đang làm) | Lâm Phong, Diệp Tĩnh Sương, Đan Dương Tử, Diệp Thanh Y, Độc Cô Lão Quái |
| 2026-03-20 | Claude Code | Đan Dương Tử (DONE) | Checked 15 refs, fixed 13 missing bidirectional links (Đan Hà Cốc subordinates + Hứa Nhược Thủy + Liễu Như Yên) |
| 2026-03-20 | Claude Code | Hắc Hạt Ma Trùng (DONE) | Checked 6 refs, fixed 5 missing bidirectional links (Nguyệt Dao, Lục Tiêu, Âu Dương Vô Tích, Trùng Ám Ảnh, Trùng Xích Giác) |
| 2026-03-20 | Claude Code | Hàn Thanh Nguyệt (DONE) | Checked 1 ref (Diệp Tĩnh Sương), all bidirectional OK, no fixes needed |
