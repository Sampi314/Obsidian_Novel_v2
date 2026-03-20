# Kế Hoạch: Tạo Toàn Bộ Dân Số Thế Lực

## Mục Tiêu
Tạo nhân vật mới cho MỌI thế lực dựa trên cấp bậc (Hạng), bao gồm cả **phàm nhân** (tạp dịch, thường dân, thợ thủ công).

## Quy Mô Nhân Vật Theo Hạng

| Hạng | Named Characters Cần | Phân Bổ | Factions |
|------|----------------------|---------|----------|
| **Nhất** | 30-50 | 5-8 leadership + 8-12 elite + 5-8 common + 5-10 phàm nhân + 5-10 notable | ~33 |
| **Nhì** | 15-25 | 3-5 leadership + 5-8 elite + 3-5 common + 3-5 phàm nhân | ~15 |
| **Ba** | 8-15 | 2-3 leadership + 3-5 elite + 2-3 common + 2-3 phàm nhân | ~20 |
| **Tư** | 5-10 | 1-2 leadership + 2-3 elite + 1-2 common + 1-2 phàm nhân | ~35 |
| **Năm** | 3-5 | 1 leadership + 1-2 members + 1 phàm nhân | ~60 |
| **KXH** | 2-3 | 1 leader + 1-2 members | ~90 |

## Phân Công (3 Agents Đồng Thời)

### Claude (Anthropic Agent) — Đông Hoang + Tán Tu
- **Khu vực:** Đông Hoang (~91 thế lực), Tán Tu, Độc Lập
- **Phương thức:** Trực tiếp trong session, 5 agents song song
- **Ưu tiên:** Hạng Nhất → Nhì → Ba → Tư → Năm → KXH

### Jules (Google AI Agent) — Nam Cương + Thiên Trụ
- **Khu vực:** Nam Cương (~12 thế lực), Thiên Trụ (~9 thế lực)
- **Phương thức:** GitHub Issue, 5-10 nhân vật/phiên
- **Ưu tiên:** Hạng Nhất → Nhì → Ba → Tư → Năm → KXH

### Gemini (Google AI Agent) — Vô Tận Hải + Bắc Băng + Tây Mạc
- **Khu vực:** Vô Tận Hải (~37 thế lực), Bắc Băng (~29 thế lực), Tây Mạc (~30 thế lực)
- **Phương thức:** GEMINI.md task, 5-10 nhân vật/phiên
- **Ưu tiên:** Hạng Nhất → Nhì → Ba → Tư → Năm → KXH

## Quy Trình Tạo Nhân Vật Mới

### Bước 1: Xác Định Gap
```bash
python3 scripts/faction_population_gap.py [region]
```
Script trả về danh sách thế lực cần thêm nhân vật, sắp xếp theo ưu tiên.

### Bước 2: Đọc Context
1. Đọc file thế lực: `Đạo/Thế_Lực/[Region]/[Faction].md`
2. Đọc file chủng tộc nếu không phải Nhân Tộc: `Đạo/Chủng_Tộc/[Race].md`
3. Đọc các nhân vật đã có trong cùng thư mục
4. Đọc skill `.jules/Nhân_Vật.md` (Chế Độ 1: Tạo Nhân Vật Mới)

### Bước 3: Tạo Nhân Vật
Mỗi nhân vật cần:
- File mới trong `Đạo/Nhân_Vật/[Region]/[Faction]/[Tên].md`
- YAML frontmatter đầy đủ (type, name, hantu, archetype, race, age, arcs with cultivation/stats/methods/inventory/relationships)
- 5 sections body (I-V) hoặc 7 sections nếu nhân vật quan trọng

### Loại Nhân Vật Cần Tạo

#### Tu Sĩ (Cultivators)
- Cảnh giới phù hợp với vị trí trong thế lực
- Công pháp/vũ khí phù hợp chuyên môn thế lực
- Quan hệ với các nhân vật cùng phe

#### Phàm Nhân (Mortals) — MỚI
- **cultivation:** Phàm Nhân (không có cảnh giới)
- **stats:** [1-5, 1-5, 1-5, 1-5, 1-5, 1-5] (rất thấp)
- **Archetype:** Thường dân, Thợ thủ công, Đầu bếp, Hầu cận, Thương nhân, Nông dân
- **Đặc điểm:** Có câu chuyện riêng, ước mơ, bí mật — KHÔNG phải NPC vô hồn
- **Ví dụ:**
  - Đầu bếp của Tông Chủ biết hết bí mật vì phục vụ bữa ăn
  - Thợ rèn phàm nhân có tay nghề ngang luyện khí sư nhưng không có linh căn
  - Tạp dịch sinh viên cần tiền nên làm việc cho tông môn

### Quy Tắc Đặt Tên
1. **Họ (family name):** Nhất quán theo chủng tộc/phe phái
   - Nhân Tộc: họ Việt thông thường (Nguyễn, Trần, Lê, Phạm...)
   - Yêu Tộc: họ theo loài (Hổ, Lang, Xà, Hồ...)
   - Cự Tộc: họ Nham, Thạch, Sơn
   - Hải Tộc: họ theo loài biển (Kình, Giải, Chương...)
   - Vi Tộc: họ theo hệ vi sinh (Nấm, Bào, Khuẩn...)
2. **Tên (given name):** 1-2 chữ, có ý nghĩa, KHÔNG dùng chức danh
3. **Phàm nhân:** Tên đời thường hơn (Tiểu X, Lão X, tên giản dị)

## Kiểm Tra
```bash
python3 scripts/faction_population_gap.py all
```
Khi tất cả thế lực đạt target → hoàn thành.
