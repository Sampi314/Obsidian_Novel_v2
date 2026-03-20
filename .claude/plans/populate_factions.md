# Kế Hoạch: Tạo Toàn Bộ Dân Số Thế Lực

## Mục Tiêu
Tạo stub nhân vật cho MỌI thế lực dựa trên cấp bậc (Hạng), bao gồm cả **phàm nhân**.
Mỗi stub có tên có ý nghĩa + YAML + Section I (chức vụ, phong, tu vi).
Phần nội dung chi tiết (Section II-V) sẽ do agent khác điền sau.

## Unified Skill Source
⚠️ **Mọi agent đều dùng:** `.claude/skills/nhan-vat/SKILL.md` (Chế Độ 1: Tạo Nhân Vật Mới)

## ⛔ CẤM
- **KHÔNG dùng script** để tạo tên — mỗi tên phải do AI đặt, có ý nghĩa phù hợp văn hóa xianxia
- **KHÔNG dùng tên chức danh** làm tên riêng (Vương, Trưởng Lão, Chiến Sĩ...)
- **KHÔNG trùng tên** trong cùng 1 thế lực

---

## Cấu Trúc Tông Môn Chuẩn

### Cấp Bậc (Cao → Thấp)
```
Thái Thượng Đại Trưởng Lão > Thái Thượng Trưởng Lão > Hộ Pháp > Tông Chủ > Phó Tông Chủ
> Trưởng Lão/Phong Chủ > Thánh Tử/Nữ > Chân Truyền > Nội Môn > Ngoại Môn > Tạp Dịch
```

**Lưu ý quan trọng:**
- Tông Chủ = quản lý hành chính, KHÔNG nhất thiết mạnh nhất
- Hộ Pháp tu vi CAO HƠN Tông Chủ
- Ngoại Môn = pool chung, chưa phân phong
- Tạp Dịch/Phàm Nhân = pool chung phục vụ toàn tông

### Số Lượng Theo Hạng

| Vị Trí | Hạng Nhất | Hạng Nhì | Hạng Ba | Hạng Tư | Hạng Năm |
|--------|:---------:|:--------:|:-------:|:-------:|:--------:|
| Thái Thượng (Lão Tổ) | 5-10 | 2-5 | 1-2 | 0-1 | 0 |
| Tông Chủ | 1 | 1 | 1 | 1 | 1 |
| Phó Tông Chủ | 1-2 | 0-1 | 0 | 0 | 0 |
| Thánh Tử | 0-1 | 0-1 | 0 | 0 | 0 |
| Thánh Nữ | 0-1 | 0-1 | 0 | 0 | 0 |
| Hộ Pháp | 5-20 | 3-10 | 2-5 | 1-2 | 0-1 |
| Trưởng Lão / Phong Chủ | 5-20 | 3-10 | 3-5 | 2-3 | 1-2 |
| Chân Truyền (1-5/sư phụ) | 20-60 | 10-30 | 5-15 | 3-8 | 2-5 |
| **Nội Môn** (chung các phong) | **100** | **50** | **20** | **10** | **5** |
| **Ngoại Môn** (pool chung) | **200** | **100** | **50** | **20** | **10** |
| Ngoại Môn Trưởng Lão | 5-10 | 3-5 | 1-3 | 1 | 0 |
| **Phàm Nhân** (Hậu Cần chung) | **10,000** | **3,000** | **1,000** | **300** | **100** |
| **TỔNG DÂN SỐ** | **~10,000-18,000** | **~3,000-5,000** | **~1,000-2,000** | **~300-600** | **~100-200** |

### Quan Hệ Sư Đồ
- Mỗi Trưởng Lão/Phong Chủ nhận 1-5 Chân Truyền đệ tử
- Tông Chủ có thể nhận 1-3 Chân Truyền
- Lão Tổ/Hộ Pháp HIẾM KHI nhận đệ tử nhưng có thể có 0-1
- Mỗi Trưởng Lão quản lý 10-100 Nội Môn đệ tử (tùy phong)
- Ngoại Môn chưa được phân, do Ngoại Môn Trưởng Lão quản lý

---

## Quy Tắc Đặt Tên

### Tu Sĩ (Nhân Tộc)
| Loại | Họ | Tên | Ví dụ |
|------|-----|------|-------|
| Lãnh đạo | Họ Việt trang trọng | 2-3 chữ, uy nghiêm | Vân Thanh Hà, Đoàn Kiếm Sơn |
| Chân Truyền | Họ Việt | 2 chữ, khí phách | Lê Thiên Vũ, Phạm Liệt Hỏa |
| Nội Môn | Họ Việt | 2 chữ, trẻ trung | Hoàng Thanh Trúc, Mã Vân Sương |
| Ngoại Môn | Họ Việt | 1-2 chữ, giản dị hơn | Lý Phong, Nguyễn Hoa |

### Tu Sĩ (Phi Nhân Tộc)
| Chủng Tộc | Họ theo | Ví dụ |
|-----------|---------|-------|
| Yêu Tộc | Loài thú | Hổ Huyết Nha, Lang Tuyết, Hồ Nguyệt |
| Cự Tộc | Đá/núi | Nham Chấn Nhạc, Thạch Vĩnh Đông, Sơn Cương |
| Hải Tộc | Sinh vật biển | Kình Thiên Hải, Giải Thiết Giáp, Chương Mặc |
| Vi Tộc | Vi sinh | Nấm Độc Tâm, Bào Tử Linh, Khuẩn Minh |
| Tinh Linh | Nguyên tố | Diệp Phong, Hoa Ngọc Lan, Ám Dạ Hành |
| Vũ Tộc | Loài chim | Ưng Liệt Phong, Hạc Minh Nguyệt, Yến Phi |
| Long Tộc | Rồng/nước | Ngao Đình, Xích Viêm, Hắc Thiên |

### Phàm Nhân
| Loại | Cách đặt tên | Ví dụ |
|------|-------------|-------|
| Người có chức trách | Họ + tên giản dị | Nguyễn Đại Chùy (thợ rèn), Phạm Thị Lan (giặt giũ) |
| Người già | Lão + Họ | Lão Trương, Lão Lý |
| Trẻ em / thanh niên | Tiểu + tên | Tiểu Hoa, Tiểu Đậu |
| Phụ nữ | Họ + Thị + tên | Trần Thị Nấu, Lê Thị Mai |

### Nghề Phàm Nhân
Đầu bếp, Phụ bếp, Thợ rèn, Thợ mộc, Giặt giũ, Quét dọn, Gánh nước, Chăn ngựa,
Canh cổng, Trồng rau, Khuân vác, Dệt vải, Nấu rượu, Quản kho, Sửa chữa,
Hái thuốc, Đốn củi, Khâu vá, Chăm vườn, Nuôi linh thú, Giao hàng,
Đào giếng, Xây tường, Lợp mái, Làm gốm, Nung gạch, Đan rổ...

---

## Work Queue System

### Trước khi bắt đầu
```bash
git pull origin main
cat WORK_QUEUE.md  # Kiểm tra ai đang làm gì
```

### Claim thế lực
Thêm vào `WORK_QUEUE.md` → commit → push NGAY trước khi làm:
```bash
git add WORK_QUEUE.md && git commit -m "claim: [Tên Thế Lực]" && git push
```

### Sau khi xong
Chuyển sang `## Hoàn Thành` → commit tất cả → push.

---

## Schedule Chi Tiết — Cửu Hoa Kiếm Tông (Mẫu)

### Đã hoàn thành (92 nhân vật)
- 5 Thái Thượng ✓
- 1 Tông Chủ + 1 Phó Tông Chủ ✓
- 1 Thánh Tử + 1 Thánh Nữ ✓
- 6 Hộ Pháp ✓
- 7 Phong Chủ (Bạch/Hồng/Kim/Ngọc/Tử/Thanh/Huyền/Nguyệt Hoa) ✓
- 18 Chân Truyền (2 mỗi phong) ✓
- 27 Nội Môn (3 mỗi phong) ✓
- 15 Ngoại Môn ✓
- 10 Phàm Nhân ✓

### Còn thiếu
| Batch | Loại | Số Lượng | Ưu Tiên |
|-------|------|----------|---------|
| A | Ngoại Môn Trưởng Lão | 7 | 🔴 Cao |
| B | Chân Truyền bổ sung (3-5/phong thay vì 2) | ~20 | 🔴 Cao |
| C | Nội Môn bổ sung (đạt ~100 tổng) | ~70 | 🟡 Trung |
| D | Ngoại Môn bổ sung (đạt ~200 tổng) | ~185 | 🟡 Trung |
| E1-E100 | Phàm Nhân batch (100/phiên × 100 phiên) | ~10,000 | 🟢 Thấp |

---

## Schedule Tổng — Tất Cả Hạng Nhất (33 thế lực)

### Phase 1: Leadership (Batch 10-20 chars/phiên)
Mỗi phiên: chọn 1 thế lực → tạo toàn bộ Thái Thượng + Hộ Pháp + Tông Chủ/Phó + Thánh Tử/Nữ + Trưởng Lão/Phong Chủ.

| Phiên | Thế Lực | Khu Vực | Chars Cần |
|-------|---------|---------|-----------|
| 1 | Thần Khí Phường | Đông Hoang | ~20 leadership |
| 2 | Dược Vương Cốc | Đông Hoang | ~20 leadership |
| 3 | Huyền Băng Cung | Bắc Băng | ~20 leadership |
| 4 | Vân Tông | Đông Hoang | ~15 leadership |
| 5 | Thanh Đế Cung | Đông Hoang | ~15 leadership |
| 6 | Thái Ất Môn | Đông Hoang | ~15 leadership |
| 7 | Vô Tranh Tự | Đông Hoang | ~15 leadership |
| 8 | Vũ Hoàng Các | Đông Hoang | ~15 leadership |
| 9 | Huyết Sát Minh | Đông Hoang | ~15 leadership |
| 10 | Huyết Ma Tông | Nam Cương | ~15 leadership |
| 11 | Vạn Độc Môn | Nam Cương | ~10 leadership |
| 12 | Đan Hà Cốc | Nam Cương | ~10 leadership |
| 13 | Kim Sa Tự | Tây Mạc | ~15 leadership |
| 14 | Thiên Sa Thương Hội | Tây Mạc | ~15 leadership |
| 15 | Hải Thần Cung | Vô Tận Hải | ~10 leadership |
| 16 | Phong Bạo Thương Đội | Vô Tận Hải | ~15 leadership |
| 17 | Đại Càn Hoàng Triều | Thiên Trụ | ~15 leadership |
| 18 | Cửu U Ma Tông | Thiên Trụ | ~10 leadership |
| 19 | Thiên Kiêu Học Viện | Thiên Trụ | ~15 leadership |
| 20 | Bách Bảo Các | Thiên Trụ | ~15 leadership |
| 21 | Thiên Mộc Thành | Thiên Trụ | ~15 leadership |
| 22 | Lôi Trì Thánh Địa | Thiên Trụ | ~15 leadership |
| 23 | Thiên Môn Kính Đài | Thiên Trụ | ~15 leadership |
| 24 | Trích Tinh Lâu | Thiên Trụ | ~10 leadership |
| 25 | Long Cung | Vô Tận Hải | ~10 leadership |
| 26 | Bắc Hải Cự Yêu Hang | Bắc Băng | ~10 leadership |
| 27 | Cực Quang Thần Điện | Bắc Băng | ~10 leadership |
| 28 | Thiên Yêu Đình | Đông Hoang | ~5 (gần đủ) |
| 29 | Tinh Linh Vương Đình | Đông Hoang | ~5 (gần đủ) |
| 30 | Vạn Yêu Thành | Đông Hoang | ~10 leadership |
| 31 | Thiên Trụ Hộ Vệ Đoàn | Đông Hoang | ~15 leadership |
| 32 | Ảnh Nguyệt Uyển | Đông Hoang | ~15 leadership |
| 33 | Thần Khí Phường | Đông Hoang | ~15 leadership |

### Phase 2: Chân Truyền + Nội Môn (Batch 20-30/phiên)
Sau khi Phase 1 xong cho 1 thế lực → quay lại tạo Chân Truyền (2-5/Trưởng Lão) + Nội Môn notable.

### Phase 3: Ngoại Môn (Batch 50/phiên)
Tạo 200 ngoại môn cho mỗi Hạng Nhất. Mỗi phiên 50 tên = 4 phiên/thế lực.

### Phase 4: Phàm Nhân (Batch 100/phiên)
Tạo 10,000 phàm nhân cho mỗi Hạng Nhất. Mỗi phiên 100 tên = 100 phiên/thế lực.

**Ước tính tổng cho 33 Hạng Nhất:**
- Phase 1: ~33 phiên
- Phase 2: ~66 phiên (2 phiên/thế lực)
- Phase 3: ~132 phiên (4 phiên/thế lực)
- Phase 4: ~3,300 phiên (100 phiên/thế lực)
- **Tổng: ~3,500 phiên**

> **Với mỗi phiên Jules tạo 100 chars, chạy 10 phiên/ngày = 1,000 chars/ngày.**
> **Ước tính hoàn thành Hạng Nhất: ~350 ngày.**
> **→ Cần nhiều agents chạy song song để rút ngắn.**

---

## Quy Trình Mỗi Phiên (Step-by-Step)

### 1. Pull & Check Queue
```bash
git pull origin main
cat WORK_QUEUE.md
```

### 2. Chọn & Claim
```bash
# Chọn thế lực chưa ai claim, ưu tiên Hạng Nhất
# Thêm vào WORK_QUEUE.md
git add WORK_QUEUE.md && git commit -m "claim: [Tên]" && git push
```

### 3. Đọc Context
```
1. Đọc .claude/skills/nhan-vat/SKILL.md (Chế Độ 1)
2. Đọc Đạo/Thế_Lực/[Region]/[Faction].md (divisions, members, headcount)
3. Đọc Đạo/Chủng_Tộc/[Race].md (nếu phi Nhân Tộc)
4. Đọc nhân vật đã có: ls Đạo/Nhân_Vật/[Region]/[Faction]/
```

### 4. Tạo Stub Characters
Mỗi file theo template:
```yaml
---
type: character
name: [Tên có ý nghĩa]
hantu: ''
archetype: [Vai trò]
race: [Chủng tộc]
dao_tam: ''
age: [Tuổi hợp lý theo cảnh giới]
avatar: ''
arcs:
  - arc: 1
    status: Còn Sống
    cultivation: [Cảnh giới or "Phàm Nhân"]
    methods: []
    inventory: []
    stats: [0, 0, 0, 0, 0, 0]
    relationships: []
---

# [Tên]

## I. THÔNG TIN CƠ BẢN
- **Tên:** [Tên]
- **Chức Vụ:** [Vị trí] — [Phong/Viện/Đường]
- **Tu Vi:** [Cảnh giới]
- **Phe Phái:** [Tên thế lực]

## II. NGOẠI HÌNH & TÍNH CÁCH
*(Chưa xác định)*

## III. NĂNG LỰC & CHIẾN ĐẤU
*(Chưa xác định)*

## IV. CÁC MỐI QUAN HỆ
*(Chưa xác định)*

## V. TIỂU SỬ & HÀNH TRÌNH
*(Chưa xác định)*
```

**Phàm Nhân dùng:** `cultivation: Phàm Nhân` và Section III → `## III. KỸ NĂNG & ĐỜI SỐNG`

### 5. Commit & Push
```bash
git add Đạo/Nhân_Vật/[Region]/[Faction]/ WORK_QUEUE.md
git commit -m "docs: populate [Faction] — [N] new characters ([loại])"
git push origin main
```

### 6. Cập nhật WORK_QUEUE.md
Chuyển từ `## Đang Làm` sang `## Hoàn Thành`, ghi số chars tạo.

---

## Checklist Mỗi Phiên
- [ ] Pull mới nhất trước khi bắt đầu
- [ ] Đã claim trong WORK_QUEUE.md và push
- [ ] Mỗi tên có ý nghĩa, không trùng, không dùng chức danh
- [ ] Họ nhất quán theo chủng tộc
- [ ] Tuổi hợp lý (phàm nhân 8-80, tu sĩ theo cảnh giới)
- [ ] Section I có đủ: Tên, Chức Vụ (kèm phong), Tu Vi, Phe Phái
- [ ] Phàm nhân có ghi nghề cụ thể
- [ ] Không trùng tên với nhân vật đã có trong thư mục
- [ ] Đã cập nhật WORK_QUEUE.md sau khi xong
