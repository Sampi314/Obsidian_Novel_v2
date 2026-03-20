# Kế Hoạch: Tạo Toàn Bộ Dân Số Thế Lực

## Mục Tiêu
Tạo nhân vật mới cho MỌI thế lực dựa trên cấp bậc (Hạng), bao gồm cả **phàm nhân**.

## Unified Skill Source
⚠️ **Mọi agent đều dùng chung 1 nguồn skill duy nhất:**
- **Nhân Vật:** `.claude/skills/nhan-vat/SKILL.md` (Chế Độ 1: Tạo Nhân Vật Mới)
- **Thế Lực:** `.claude/skills/the-luc/SKILL.md`
- **Chủng Tộc:** `.claude/skills/chung-toc/SKILL.md`

## Quy Mô Nhân Vật Theo Hạng

| Hạng | Target | Phân Bổ |
|------|--------|---------|
| **Nhất** | 35 | 5-8 leadership + 8-12 elite + 5-8 common + 5-10 phàm nhân |
| **Nhì** | 20 | 3-5 leadership + 5-8 elite + 3-5 common + 3-5 phàm nhân |
| **Ba** | 12 | 2-3 leadership + 3-5 elite + 2-3 common + 2-3 phàm nhân |
| **Tư** | 7 | 1-2 leadership + 2-3 elite + 1-2 common + 1-2 phàm nhân |
| **Năm** | 4 | 1 leadership + 1-2 members + 1 phàm nhân |
| **KXH** | 3 | 1 leader + 1-2 members |

## Work Queue System

### Nguyên Tắc Chống Trùng Lặp
Mọi agent **BẮT BUỘC** tuân thủ quy trình sau để tránh hai agent cùng làm 1 thế lực:

#### Bước 1: Pull mới nhất
```bash
git pull origin main
```

#### Bước 2: Kiểm tra Work Queue
```bash
cat WORK_QUEUE.md
```
Xem thế lực nào đang được agent khác claim. **KHÔNG được chọn thế lực đã có claim.**

#### Bước 3: Claim thế lực
Thêm dòng mới vào `WORK_QUEUE.md` phần `## Đang Làm`:
```
| [Tên Thế Lực] | [Khu Vực] | [Session ID/Thời gian] | claiming |
```
Rồi commit + push NGAY:
```bash
git add WORK_QUEUE.md && git commit -m "claim: [Tên Thế Lực]" && git push origin main
```

#### Bước 4: Tạo nhân vật
Làm việc bình thường — tạo 5-10 nhân vật cho thế lực đã claim.

#### Bước 5: Hoàn thành
Cập nhật `WORK_QUEUE.md`:
- Chuyển dòng từ `## Đang Làm` sang `## Hoàn Thành`
- Ghi số nhân vật đã tạo

Commit tất cả + push:
```bash
git add -A Đạo/Nhân_Vật/ WORK_QUEUE.md && git commit -m "docs: populate [Faction] with [N] new characters" && git push origin main
```

### Xử Lý Conflict
Nếu push bị reject (agent khác push trước):
```bash
git pull --rebase origin main
```
Nếu `WORK_QUEUE.md` bị conflict → kiểm tra ai claim trước, nhường cho họ, chọn thế lực khác.

## Quy Trình Tạo Nhân Vật

### 1. Xác Định Gap
```bash
python3 scripts/faction_population_gap.py [region]
```

### 2. Đọc Context
1. **Skill:** `.claude/skills/nhan-vat/SKILL.md` (Chế Độ 1)
2. **Thế lực:** `Đạo/Thế_Lực/[Region]/[Faction].md`
3. **Chủng tộc:** `Đạo/Chủng_Tộc/[Race].md` (nếu không phải Nhân Tộc)
4. **Nhân vật đã có:** `Đạo/Nhân_Vật/[Region]/[Faction]/`

### 3. Tạo Nhân Vật
- File mới: `Đạo/Nhân_Vật/[Region]/[Faction]/[Tên].md`
- YAML frontmatter theo `.claude/skills/nhan-vat/SKILL.md`
- 5 sections body (I-V), 7 sections nếu nhân vật quan trọng

### Loại Nhân Vật

#### Tu Sĩ (Cultivators)
- Cảnh giới phù hợp vị trí trong thế lực
- Công pháp/vũ khí phù hợp chuyên môn thế lực

#### Phàm Nhân (Mortals)
- **cultivation:** Phàm Nhân
- **stats:** [1-5, 1-5, 1-5, 1-5, 1-5, 1-5]
- **Archetype:** Đầu bếp, Thợ rèn, Hầu cận, Thương nhân, Nông dân, Tạp dịch
- **QUAN TRỌNG:** Có câu chuyện riêng, ước mơ, bí mật — KHÔNG phải NPC vô hồn

### Quy Tắc Đặt Tên
| Chủng Tộc | Họ (Family Name) |
|-----------|-------------------|
| Nhân Tộc | Họ Việt: Nguyễn, Trần, Lê, Phạm... |
| Yêu Tộc | Theo loài: Hổ, Lang, Xà, Hồ... |
| Cự Tộc | Nham, Thạch, Sơn |
| Hải Tộc | Theo loài biển: Kình, Giải, Chương, Triều... |
| Vi Tộc | Theo vi sinh: Nấm, Bào, Khuẩn, Phấn... |
| Tinh Linh Tộc | Theo nguyên tố: Diệp, Hoa, Mộc, Ám... |
| Vũ Tộc | Theo loài chim: Ưng, Hạc, Phượng, Yến... |

- Tên (given): 1-2 chữ, KHÔNG dùng chức danh (Vương, Trưởng Lão, Chiến Sĩ...)
- Phàm nhân: tên đời thường (Tiểu X, Lão X)

## Phân Vùng Gợi Ý

Để tránh overlap, mỗi session nên chọn 1 khu vực cố định:

| Khu Vực | Gap | Thế Lực |
|---------|-----|---------|
| Đông Hoang | ~539 | 61 |
| Vô Tận Hải | ~116 | 14 |
| Bắc Băng | ~169 | 18 |
| Tây Mạc | ~125 | 15 |
| Nam Cương | ~98 | 11 |
| Thiên Trụ | ~206 | 9 |

**Ưu tiên:** Chọn khu vực có gap lớn nhất mà chưa có agent nào claim trong `WORK_QUEUE.md`.

## Kiểm Tra Tiến Độ
```bash
python3 scripts/faction_population_gap.py all
```
Khi tất cả thế lực đạt target → hoàn thành.
