# Prompt: Populate Faction Rosters

> Dán prompt này khi khởi động phiên làm việc cho bất kỳ agent nào.

---

## Nhiệm vụ

Tạo character stubs cho các thế lực trong dự án tiểu thuyết Cố Nguyên Giới.

## Trước khi bắt đầu — ĐỌC CÁC FILE NÀY THEO THỨ TỰ:

1. **Plan chi tiết:** `.claude/plans/populate_factions.md`
   - Phần 1: Cấu trúc theo loại thế lực (headcount, cấp bậc, tu vi)
   - Phần 2: Blueprint chi tiết từng thế lực Hạng Nhất
   - Phần 3: Schedule 5 Phase
   - Phần 5: Checklist

2. **Skill tạo nhân vật:** `.claude/skills/nhan-vat/SKILL.md`
   - Chế Độ 1: Tạo Nhân Vật Mới — template YAML + 5 sections body

3. **Work queue:** `WORK_QUEUE.md`
   - Kiểm tra thế lực nào đang được agent khác claim
   - Claim thế lực bạn sẽ làm → commit + push NGAY

4. **File thế lực:** `Đạo/Thế_Lực/[Region]/[Faction].md`
   - Xem divisions, members đã có, headcount, specialty

5. **File chủng tộc:** `Đạo/Chủng_Tộc/[Race].md`
   - Chỉ đọc nếu thế lực KHÔNG phải Nhân Tộc

6. **Nhân vật đã có:** `ls Đạo/Nhân_Vật/[Region]/[Faction]/`
   - Để tránh trùng tên và biết vị trí nào đã có người

## Quy trình mỗi phiên

```
1. git pull origin main
2. cat WORK_QUEUE.md
3. Chọn thế lực chưa ai claim → thêm claim → commit + push WORK_QUEUE.md
4. Đọc 5 file ở trên
5. Tạo 10-100 character stubs (tùy phase trong plan)
6. git add + commit + push
7. Cập nhật WORK_QUEUE.md (chuyển sang Hoàn Thành) → commit + push
```

## ⛔ QUY TẮC

- KHÔNG dùng script — mỗi tên do AI đặt, có ý nghĩa xianxia
- KHÔNG dùng chức danh làm tên (Vương, Trưởng Lão, Chiến Sĩ...)
- KHÔNG trùng tên trong cùng thế lực
- Tiếng Việt only trong nội dung
- BẮT BUỘC claim trong WORK_QUEUE.md trước khi bắt đầu
