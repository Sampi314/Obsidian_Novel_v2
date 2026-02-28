# HƯỚNG DẪN JULES TỔNG QUẢN — CỐ NGUYÊN STORY HUB

## Cách đọc Story Planner
File chính: `.Jules-Memory/story-planner.md`
- Đọc phần KANBAN STATE để biết trạng thái từng chapter
- Tìm các chapter có status `planned` và User Notes để ưu tiên làm
- Ghi Jules Notes vào từng task theo format: `**Jules Notes:** {nội dung}`
- Cập nhật JULES SYNC LOG mỗi lần bạn sửa file

## Cách cập nhật Wiki
- Các file trong `.Jules-Memory/wiki/` là nguồn truth
- Khi update wiki, set `lastEditedBy: jules` trong frontmatter
- Thêm comment `<!-- jules_update: {timestamp} — {mô tả thay đổi} -->` ở cuối
- App sẽ tự detect và hiển thị badge "Jules đã cập nhật"

## Cách giao tiếp với User qua Annotations
- Append vào `.Jules-Memory/annotations.md`
- Format: `## [{ISO timestamp}] Jules → User`
- Luôn ghi rõ **Context:** để user biết bạn đang nói về phần nào
- Giới hạn mỗi annotation trong 200 chữ, rõ ràng và actionable

## Workflow khi Jules nhận task mới từ User
1. Đọc `story-planner.md` → tìm chapters liên quan
2. Đọc wiki pages liên quan trong `.Jules-Memory/wiki/`
3. Thực hiện task
4. Cập nhật wiki page tương ứng
5. Ghi annotation trong `annotations.md` để báo cáo User
6. Cập nhật status chapter trong `story-planner.md` nếu cần
