# Agent Prompt — Cố Nguyên Giới

Bạn đang tham gia dự án tiểu thuyết tu tiên Cố Nguyên Giới.

## Quy trình mỗi phiên

### 1. Pull và giải quyết conflict
```bash
git pull origin main
```
Nếu có merge conflict → giải quyết → commit → push trước khi làm bất cứ gì.

### 2. Đọc Work Queue và Claim
```bash
cat WORK_QUEUE.md
```
- Tìm **Task Hiện Tại** (🔴)
- Xem sub-task nào đang ⬜ Pending → chọn 1 cái
- **Đổi ⬜ thành 🔄 → commit + push NGAY** trước khi làm bất cứ gì:
```bash
# Sửa WORK_QUEUE.md: ⬜ Pending → 🔄 Đang làm
git add WORK_QUEUE.md && git commit -m "claim: [tên sub-task]" && git push origin main
```
⚠️ Nếu push fail → pull lại → kiểm tra sub-task đó còn ⬜ không. Nếu đã bị 🔄 → chọn cái khác.

- Nếu không có Task Hiện Tại → đọc `.claude/plans/daily_tasks.md`

### 3. Đọc Plan
`WORK_QUEUE.md` ghi rõ plan file nào cần đọc. Ví dụ:
- **Plan:** `.claude/plans/populate_factions.md`

Đọc plan để hiểu quy trình chi tiết, blueprint, headcount, naming rules.

### 4. Đọc Skill
Plan file và `WORK_QUEUE.md` ghi rõ skill nào cần đọc. Ví dụ:
- **Skill:** `.claude/skills/nhan-vat/SKILL.md`

Đọc skill để biết template, format, quy tắc cụ thể.

### 5. Đọc Context
Tùy task, đọc thêm:
- File thế lực: `Đạo/Thế_Lực/[Region]/[Faction].md`
- File chủng tộc: `Đạo/Chủng_Tộc/[Race].md`
- Nhân vật đã có: `Đạo/Nhân_Vật/[Region]/[Faction]/`
- Cốt truyện: `Đạo/Quy_Hoạch_Cốt_Truyện/`
- Locked chapters: `locked_chapters.json`

### 6. Làm việc
Thực hiện theo hướng dẫn trong plan + skill.

### 7. Push kết quả
```bash
git add [files] && git commit -m "docs: [mô tả]" && git push origin main
```
Nếu push reject: `git pull --rebase origin main && git push origin main`

### 8. Cập nhật Work Queue
Trong `WORK_QUEUE.md`, đổi sub-task từ 🔄 sang ✅ Done.
```bash
git add WORK_QUEUE.md && git commit -m "done: [tên sub-task]" && git push origin main
```

## Quy tắc chung
- Tiếng Việt only trong nội dung sáng tạo
- Kiểm tra `locked_chapters.json` trước khi sửa chương
- Không dùng script tạo nội dung
- Tên nhân vật có ý nghĩa, không dùng chức danh làm tên
