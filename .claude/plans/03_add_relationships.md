# Plan: Thêm Quan Hệ Cho Nhân Vật Thiếu Relationship

## Mục Tiêu
Thêm `relationships` vào YAML frontmatter cho tất cả nhân vật có `relationships: []`.
Mỗi nhân vật cần ít nhất 5-unlimited relationships với feelings 6 trục.

## Skills Cần Đọc
> 📖 **Skill chính:** `.claude/skills/nhan-vat/SKILL.md` (phần Quy Tắc Relationships)
> 📖 **Skill phụ:** `.claude/skills/quan-he/SKILL.md` (xây dựng mạng quan hệ)

## ⛔ QUY TẮC
- KHÔNG dùng script — AI tự đọc từng file, tìm nhân vật cùng faction, tạo relationship thủ công
- Relationship phải hai chiều — nếu A ghi B là sư phụ, thì B cũng phải ghi A là đệ tử
- Feelings 6 trục: yeu, han, kinh, tin, so, on (-100 đến +100)
- Description bằng Tiếng Việt

## Quy Trình Mỗi Phiên (10-15 nhân vật)

### 1. Pull
```bash
git pull origin main
```

### 2. Chọn faction từ bảng Work Queue bên dưới
Tìm hàng ⬜ đầu tiên → đổi 🔄 → ghi Đang Làm → push.

### 3. Đọc context
- Đọc `.claude/skills/nhan-vat/SKILL.md` (phần Relationships)
- Liệt kê TẤT CẢ nhân vật trong faction: `ls Đạo/Nhân_Vật/[Region]/[Faction]/`
- Đọc file thế lực để hiểu cấu trúc sư đồ

### 4. Thêm relationships
Với mỗi nhân vật có `relationships: []`:
- Xác định vị trí trong faction (sư phụ → đệ tử, đồng môn, cấp trên/dưới)
- Thêm ít nhất 2-3 relationships vào YAML:
```yaml
relationships:
  - character: [Tên]
    description: [Mô tả Tiếng Việt]
    feelings:
      yeu: 0
      han: 0
      kinh: 0
      tin: 0
      so: 0
      on: 0
```
- Cập nhật file đối phương nếu cần (hai chiều)

### 5. Push
```bash
git add Đạo/Nhân_Vật/[Region]/[Faction]/ && git commit -m "docs: add relationships for [Faction]" && git push origin main
```

### 6. Cập nhật bảng
Xong += Đang Làm, Đang Làm = 0. Nếu Xong ≥ Cần → ✅. Push.

---

## Checklist Mỗi Nhân Vật
- [ ] Ít nhất 2 relationships (3+ cho leadership)
- [ ] Mỗi relationship có description Tiếng Việt
- [ ] Feelings 6 trục hợp lý (không để tất cả 0)
- [ ] Quan hệ hai chiều (A→B thì B→A)
- [ ] Tên nhân vật trong relationship phải tồn tại trong cùng faction folder

---

# WORK QUEUE

> **Mỗi phiên:** 10-15 nhân vật, 1 faction.
> Tìm ⬜ → đổi 🔄 → ghi Đang Làm → push → làm → Xong += Đang Làm → push.

## Đông Hoang (619 thiếu)

| Faction | Xong | Đang Làm | Thiếu | Trạng Thái |
|---------|:----:|:--------:|:-----:|:----------:|
| Cửu Hoa Kiếm Tông | 63 | 0 | 195 | 🔄 |
| Thần Khí Phường | 0 | 0 | 31 | ⬜ |
| Vân Tông | 0 | 0 | 27 | ⬜ |
| Thanh Đế Cung | 0 | 0 | 21 | ⬜ |
| Thái Ất Môn | 0 | 0 | 20 | ⬜ |
| Huyết Sát Minh | 0 | 0 | 20 | ⬜ |
| Vạn Yêu Thành | 0 | 0 | 19 | ⬜ |
| Thiên Yêu Đình | 0 | 0 | 18 | ⬜ |
| Tinh Linh Vương Đình | 0 | 0 | 17 | ⬜ |
| Vũ Hoàng Các | 0 | 0 | 16 | ⬜ |
| Vô Tranh Tự | 0 | 0 | 15 | ⬜ |
| Ảnh Nguyệt Uyển | 0 | 0 | 14 | ⬜ |
| Dược Vương Cốc | 0 | 0 | 13 | ⬜ |
| Thiên Trụ Hộ Vệ Đoàn | 0 | 0 | 12 | ⬜ |
| (Các faction nhỏ) | 0 | 0 | 138 | ⬜ |

## Vô Tận Hải (215 thiếu)

| Faction | Xong | Đang Làm | Thiếu | Trạng Thái |
|---------|:----:|:--------:|:-----:|:----------:|
| Hải Thần Cung | 0 | 0 | 30 | ⬜ |
| Long Cung | 0 | 0 | 17 | ⬜ |
| Phong Bạo Thương Đội | 0 | 0 | 15 | ⬜ |
| (Các faction khác) | 0 | 0 | 153 | ⬜ |

## Tây Mạc (147 thiếu)

| Faction | Xong | Đang Làm | Thiếu | Trạng Thái |
|---------|:----:|:--------:|:-----:|:----------:|
| Kim Sa Tự | 0 | 0 | 20 | ⬜ |
| Thiên Sa Thương Hội | 0 | 0 | 18 | ⬜ |
| (Các faction khác) | 0 | 0 | 109 | ⬜ |

## Thiên Trụ (88 thiếu)

| Faction | Xong | Đang Làm | Thiếu | Trạng Thái |
|---------|:----:|:--------:|:-----:|:----------:|
| Đại Càn Hoàng Triều | 0 | 0 | 16 | ⬜ |
| Cửu U Ma Tông | 0 | 0 | 14 | ⬜ |
| Thiên Kiêu Học Viện | 0 | 0 | 11 | ⬜ |
| (Các faction khác) | 0 | 0 | 47 | ⬜ |

## Bắc Băng (57 thiếu)

| Faction | Xong | Đang Làm | Thiếu | Trạng Thái |
|---------|:----:|:--------:|:-----:|:----------:|
| Huyền Băng Cung | 0 | 0 | 20 | ⬜ |
| Cực Quang Thần Điện | 0 | 0 | 10 | ⬜ |
| (Các faction khác) | 0 | 0 | 27 | ⬜ |

## Nam Cương + Tán Tu: ✅ (0 thiếu)

---

**Tổng: 1,126 nhân vật cần thêm relationships.**
**Ước tính: ~75-113 phiên (10-15 chars/phiên).**
**Khi tất cả ✅ → xóa file này.**
