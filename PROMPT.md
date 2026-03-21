# Agent Prompt — Cố Nguyên Giới

Bạn đang tham gia dự án tiểu thuyết tu tiên Cố Nguyên Giới.

## Quy trình mỗi phiên

### 1. Pull và giải quyết conflict
```bash
git pull origin main
```
Nếu có merge conflict → giải quyết → commit → push trước khi làm gì khác.

### 2. Đọc Schedule
Đọc `.claude/plans/agent_schedule.md` để biết:
- Task nào đang ưu tiên cao nhất (🔴 > 🟡 > 🟢)
- Plan file nào cần đọc
- Skill file nào cần dùng

Nếu không có task phù hợp → đọc `.claude/plans/daily_tasks.md`.

### 3. Đọc Plan + Claim
Mở plan file được chỉ định (ví dụ `.claude/plans/populate_factions.md`).
Trong plan có **bảng Work Queue** với trạng thái:
- ⬜ = Pending (chưa ai làm)
- 🔄 = Đang làm
- ✅ = Done

**Chọn 1 mục ⬜ → đổi thành 🔄 → commit + push NGAY:**
```bash
git add .claude/plans/[plan_file] && git commit -m "claim: [tên sub-task]" && git push origin main
```
⚠️ Push fail → pull lại → kiểm tra mục đó còn ⬜ không → nếu đã 🔄 thì chọn cái khác.

### 4. Đọc Skill + Context
Plan file ghi rõ skill nào cần đọc. Ví dụ:
> 📖 Đọc `.claude/skills/nhan-vat/SKILL.md` (Chế Độ 1)

Đọc thêm context mà plan yêu cầu:
- File thế lực, file chủng tộc, nhân vật đã có, cốt truyện, v.v.
- `locked_chapters.json` nếu liên quan đến chương truyện

### 5. Làm việc
Thực hiện theo hướng dẫn trong plan + skill.

### 6. Push kết quả
```bash
git add [files] && git commit -m "docs: [mô tả]" && git push origin main
```
Push reject → `git pull --rebase origin main && git push origin main`

### 7. Cập nhật tiến độ
Trong plan file, đổi mục từ 🔄 → ✅.
```bash
git add .claude/plans/[plan_file] && git commit -m "done: [tên sub-task]" && git push origin main
```

## Tóm tắt
```
Pull → Read schedule → Read plan → Claim ⬜→🔄 + Push
→ Read skill → Work → Push → Update ✅ + Push
```

## Quy tắc chung
- Tiếng Việt only trong nội dung sáng tạo
- Không dùng script tạo nội dung
- Tên nhân vật có ý nghĩa, không dùng chức danh làm tên
- Kiểm tra `locked_chapters.json` trước khi sửa chương
