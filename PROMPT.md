# Agent Prompt — Cố Nguyên Giới

Bạn là một agent tham gia dự án tiểu thuyết tu tiên Cố Nguyên Giới. Làm theo quy trình dưới đây.

---

## Bước 1: Giải quyết Merge Conflict (nếu có)

```bash
git pull origin main
```

Nếu có conflict:
```bash
# Xem file conflict
git status
# Giải quyết bằng cách giữ cả hai thay đổi (hoặc chọn phiên bản mới nhất)
# Sau đó:
git add [file] && git commit -m "resolve merge conflict" && git push origin main
```

---

## Bước 2: Đọc Work Queue

```bash
cat WORK_QUEUE.md
```

Kiểm tra:
- Thế lực / task nào đang được agent khác claim? → **KHÔNG được chọn**
- Thế lực / task nào đã hoàn thành? → bỏ qua
- Thế lực / task nào chưa ai claim? → chọn 1 cái

---

## Bước 3: Đọc Plan và nhận Task

Đọc `.claude/plans/agent_schedule.md` để biết:
- Task nào đang ưu tiên cao nhất (🔴 > 🟡 > 🟢)
- Task đó cần đọc plan chi tiết nào
- Task đó cần đọc skill nào

**Nếu không có Task cụ thể** → đọc `.claude/plans/daily_tasks.md` để nhận việc mặc định.

---

## Bước 4: Claim Task → Push NGAY

Thêm 1 dòng vào `WORK_QUEUE.md` phần `## Đang Làm`:

```markdown
| [Tên thế lực / task] | [Khu vực] | [Thời gian claim] | claiming |
```

Rồi push:
```bash
git add WORK_QUEUE.md && git commit -m "claim: [tên task]" && git push origin main
```

⚠️ **Push TRƯỚC khi bắt đầu làm việc** — để agent khác biết bạn đã claim.

---

## Bước 5: Đọc Skill và Context

Plan file sẽ ghi rõ cần đọc skill nào. Ví dụ:
- Tạo nhân vật → đọc `.claude/skills/nhan-vat/SKILL.md`
- Thế lực → đọc `.claude/skills/the-luc/SKILL.md`
- Chủng tộc → đọc `.claude/skills/chung-toc/SKILL.md`
- Viết chương → đọc `.claude/skills/chuong-truyen/SKILL.md`

Đọc thêm context files mà plan yêu cầu (file thế lực, file chủng tộc, nhân vật đã có...).

---

## Bước 6: Làm việc

Thực hiện task theo hướng dẫn trong plan + skill. Mỗi phiên tạo 10-100 files tùy task.

---

## Bước 7: Push kết quả

```bash
git add [files đã tạo/sửa] && git commit -m "docs: [mô tả ngắn]" && git push origin main
```

Nếu push bị reject:
```bash
git pull --rebase origin main && git push origin main
```

---

## Bước 8: Cập nhật Work Queue → Push

Chuyển task từ `## Đang Làm` sang `## Hoàn Thành` trong `WORK_QUEUE.md`:

```markdown
| [Tên task] | [Khu vực] | [Số chars/files tạo] | [Ngày] |
```

```bash
git add WORK_QUEUE.md && git commit -m "done: [tên task]" && git push origin main
```

---

## Tóm tắt

```
Pull → Resolve conflicts → Read WORK_QUEUE → Read plan → Claim → Push
→ Read skill → Do work → Push → Update queue → Push → Done
```
