# Plan: Điền Chi Tiết Nhân Vật (Section II-V)

## Mục Tiêu
Điền Section II-V cho TẤT CẢ nhân vật có placeholder `*(Chưa xác định)*`.
Bao gồm cả nhân vật cũ lẫn nhân vật mới tạo từ Task 01_populate.

## Skills Cần Đọc
> 📖 **Skill chính:** `.claude/skills/nhan-vat/SKILL.md` (Chế Độ 2: Điền Chi Tiết Nhân Vật Hiện Có)
> 📖 **Skill phụ:** `.claude/skills/the-luc/SKILL.md` (hiểu faction context)
> 📖 **Skill phụ:** `.claude/skills/chung-toc/SKILL.md` (nếu phi Nhân Tộc)

---

## Cách Tìm Nhân Vật Cần Điền

```bash
python3 scripts/find_unfilled_chars.py 3
```
Script trả về 2-3 nhân vật cùng phe phái có `*(Chưa xác định)*`.

---

## Quy Trình Mỗi Phiên (10-20 nhân vật)

### 1. Pull
```bash
git pull origin main
```

### 2. Cập nhật số liệu
```bash
python3 scripts/find_unfilled_chars.py 1
```
Script chỉ ĐỌC — không ghi đè nội dung AI đã làm. Dùng kết quả để cập nhật bảng PHẦN 2.

### 3. Tìm nhân vật
```bash
python3 scripts/find_unfilled_chars.py 3
```
Hoặc chọn thủ công:
```bash
grep -rl 'Chưa xác định' Đạo/Nhân_Vật/[Region]/ | head -20
```

### 4. Đọc context
- Đọc `.claude/skills/nhan-vat/SKILL.md` (Chế Độ 2)
- Đọc file thế lực: `Đạo/Thế_Lực/[Region]/[Faction].md`
- Đọc file chủng tộc: `Đạo/Chủng_Tộc/[Race].md` (nếu phi Nhân Tộc)
- Đọc nhân vật đã điền trong cùng thư mục để giữ nhất quán

### 5. Điền 4 sections cho mỗi nhân vật

⚠️ **KHÔNG thay đổi YAML frontmatter và Section I**

#### Section II — Ngoại Hình & Tính Cách (2-4 câu)
- Đặc điểm ngoại hình: thân hình, khuôn mặt, tóc, dấu hiệu đặc biệt, trang phục
- Tính cách: khí chất, thói quen, cách người khác nhìn nhận
- Phản ánh chủng tộc và cấp bậc
- Phàm nhân: mô tả ngoại hình bình thường, đặc điểm nghề nghiệp

#### Section III — Năng Lực & Chiến Đấu (2-3 câu)
- Tu sĩ: phong cách chiến đấu gắn với chuyên môn phe phái
- Kỹ thuật đặc trưng — đặt tên Tiếng Việt kèm Hán Tự (VD: *Băng Thiên Nhất Kiếm* (冰天一劍))
- Điểm mạnh và yếu
- Phàm nhân: đổi thành **"Kỹ Năng & Đời Sống"** — mô tả tay nghề, kinh nghiệm, điều đặc biệt

#### Section IV — Các Mối Quan Hệ (2-4 gạch đầu dòng)
- Format: `- **[Tên Nhân Vật]:** [mô tả quan hệ]`
- Ít nhất 1 quan hệ trong phe phái (sư phụ, đồng môn, cấp dưới, đối thủ)
- Quan hệ phải dùng tên nhân vật thật (kiểm tra thư mục cùng phe)
- Phàm nhân: quan hệ với chủ nhân, đồng nghiệp, hoặc tu sĩ quen biết

#### Section V — Tiểu Sử & Hành Trình (3-5 câu)
- Xuất thân: quê quán, gia đình, hoàn cảnh
- Cách gia nhập phe phái và lý do
- Sự kiện quan trọng định hình tính cách
- Mục tiêu, tham vọng, hoặc bí mật chưa tiết lộ
- Phàm nhân: câu chuyện đời thường nhưng có chiều sâu

### 6. Push
```bash
git add Đạo/Nhân_Vật/[Region]/[Faction]/ && git commit -m "docs: fill character details for [Faction]" && git push origin main
```

### 7. Cập nhật bảng tiến độ
Cập nhật cột **Xong** và **Chưa Điền** trong bảng PHẦN 2 → push.

---

## Checklist Mỗi Nhân Vật
- [ ] Section II có nội dung (không còn placeholder)
- [ ] Section III có nội dung (không còn placeholder)
- [ ] Section IV có ít nhất 1 quan hệ có tên thật
- [ ] Section V có nội dung (không còn placeholder)
- [ ] Tiếng Việt only
- [ ] Tính cách KHÁC với nhân vật cùng phe
- [ ] Năng lực phù hợp chuyên môn phe phái
- [ ] YAML và Section I KHÔNG bị thay đổi

---

# PHẦN 2: WORK QUEUE

> Cập nhật số liệu: `python3 scripts/find_unfilled_chars.py 1`
> Script chỉ ĐỌC — không ghi đè nội dung AI đã làm.
>
> **Quy trình:** Tìm hàng ⬜ đầu tiên → đổi 🔄 → ghi Đang Làm → push → điền 10-20 chars → push → Xong += Đang Làm → push.

| Khu Vực | Xong | Đang Làm | Chưa Điền | Tổng | Trạng Thái |
|---------|:----:|:--------:|:---------:|:----:|:----------:|
| Đông Hoang | 689 | 0 | 49 | 738 | ⬜ |
| Vô Tận Hải | 306 | 0 | 15 | 321 | ⬜ |
| Tây Mạc | 262 | 0 | 10 | 272 | ⬜ |
| Bắc Băng | 270 | 0 | 8 | 278 | ⬜ |
| Nam Cương | 134 | 0 | 0 | 134 | ✅ |
| Thiên Trụ | 137 | 0 | 0 | 137 | ✅ |
| Tán Tu | 7 | 0 | 0 | 7 | ✅ |

> **Lưu ý:** Cột "Chưa Điền" sẽ TĂNG khi Task 01_ tạo thêm stubs mới.
> Chạy `python3 scripts/find_unfilled_chars.py 1` để lấy số mới nhất.
> Khi TẤT CẢ khu vực = ✅ và `"remaining": 0` → task hoàn thành → xóa file này.
