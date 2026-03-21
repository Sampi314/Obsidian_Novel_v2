# Agent Prompt — Cố Nguyên Giới

Bạn đang tham gia dự án tiểu thuyết tu tiên Cố Nguyên Giới.

## Quy trình

### 1. Pull và giải quyết conflict
```bash
git pull origin main
```
Có conflict → giải quyết → commit → push.

### 2. Đọc file ĐẦU TIÊN trong `.claude/plans/`
```bash
ls .claude/plans/
```
File có prefix số nhỏ nhất (01_, 02_...) = task hiện tại.
Đọc file đó và làm theo hướng dẫn bên trong.

Nếu không có file số → đọc `99_daily_tasks.md`.

### 3. Làm theo plan
Plan file ghi rõ:
- Skill nào cần đọc
- Context nào cần đọc
- Work queue (⬜/🔄/✅) để claim task
- Checklist kiểm tra

### 4. Claim → Push → Làm → Push
- Tìm ⬜ trong plan → đổi thành 🔄 → push
- Làm việc
- Push kết quả
- Đổi 🔄 → ✅ → push

### 5. Khi task hoàn thành
Nếu TẤT CẢ mục trong plan đều ✅ → xóa file plan đó → push.
File tiếp theo tự động trở thành task đầu tiên.

## Quy tắc
- Tiếng Việt only
- Không dùng script tạo nội dung
- Kiểm tra `locked_chapters.json` trước khi sửa chương
