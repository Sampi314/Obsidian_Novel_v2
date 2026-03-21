# Agent Schedule — Cố Nguyên Giới

> **Cách dùng:** Agent đọc file này để biết task nào ưu tiên nhất.
> Mỗi task ghi rõ **plan file** và **skill file** cần đọc.
> Quy trình tổng: xem `PROMPT.md` tại repo root.
> Không có task phù hợp → xem `.claude/plans/daily_tasks.md`.

---

## 🔴 ƯU TIÊN CAO

### Task 10: Populate Faction Rosters
Tạo character stubs cho tất cả thế lực (leadership → chân truyền → nội/ngoại môn → phàm nhân).

| | File |
|---|---|
| **Plan chi tiết** | `.claude/plans/populate_factions.md` |
| **Skill chính** | `.claude/skills/nhan-vat/SKILL.md` (Chế Độ 1) |
| **Skill phụ** | `.claude/skills/the-luc/SKILL.md` (headcount schema) |
| **Skill phụ** | `.claude/skills/chung-toc/SKILL.md` (nếu phi Nhân Tộc) |
| **Coordination** | `WORK_QUEUE.md` |

### Task 9: Điền Chi Tiết Nhân Vật Có Placeholder
Điền Section II-V cho nhân vật có `*(Chưa xác định)*`.

| | File |
|---|---|
| **Plan chi tiết** | `.claude/plans/fill_all_characters.md` |
| **Skill chính** | `.claude/skills/nhan-vat/SKILL.md` (Chế Độ 2) |
| **Script tìm stub** | `python3 scripts/find_unfilled_chars.py 3` |

---

## 🟡 ƯU TIÊN TRUNG

### Task 11: Enrichen Thế Lực Mỏng
Mở rộng nội dung cho faction files dưới 130 dòng.

| | File |
|---|---|
| **Skill** | `.claude/skills/the-luc/SKILL.md` |
| **Tìm file mỏng** | `find Đạo/Thế_Lực -name "*.md" ! -name "index.md" -exec sh -c 'lines=$(wc -l < "$1"); if [ "$lines" -lt 130 ]; then echo "$lines $1"; fi' _ {} \| sort -n` |

### Task 12: Enrichen Kỳ Vật, Chủng Tộc, Công Pháp, Trận Pháp
Mở rộng nội dung cho các file world-building còn ngắn.

| Nội dung | Skill | Thư mục |
|----------|-------|---------|
| Kỳ Vật | `.claude/skills/ky-vat/SKILL.md` | `Đạo/Kỳ_Vật/` |
| Chủng Tộc | `.claude/skills/chung-toc/SKILL.md` | `Đạo/Chủng_Tộc/` |
| Công Pháp | `.claude/skills/cong-phap/SKILL.md` | `Đạo/Công_Pháp/` |
| Trận Pháp | `.claude/skills/tran-phap/SKILL.md` | `Đạo/Trận_Pháp/` |
| Đan Dược | `.claude/skills/dan-duoc/SKILL.md` | `Đạo/Đan_Dược/` |
| Luyện Khí | `.claude/skills/luyen-khi/SKILL.md` | `Đạo/Luyện_Khí/` |
| Tu Luyện | `.claude/skills/tu-luyen/SKILL.md` | `Đạo/Tu_Luyện/` |
| Phù Lục | `.claude/skills/phu-luc/SKILL.md` | `Đạo/Phù_Lục/` |
| Văn Hóa | `.claude/skills/van-hoa/SKILL.md` | `Đạo/Văn_Hóa/` |
| Thế Giới | `.claude/skills/the-gioi/SKILL.md` | `Đạo/Thế_Giới_Và_Thời_Gian/` |

### Task 13: Xây Dựng Quan Hệ Giữa Nhân Vật
Bổ sung mối quan hệ (Section IV) cho nhân vật đã có nội dung nhưng thiếu relationship.

| | File |
|---|---|
| **Skill** | `.claude/skills/quan-he/SKILL.md` |
| **Script** | `python3 scripts/sync_relationship_data.py` |

---

## 🟢 ƯU TIÊN THẤP (SAU KHI CÁC TASK TRÊN HOÀN THÀNH)

### Task 2: Catch-up Lâm Phong
Viết chương 133+ cho Góc Nhìn Lâm Phong.

| | File |
|---|---|
| **Skill** | `.claude/skills/chuong-truyen/SKILL.md` |
| **Context** | `Đạo/Chương_Truyện/Góc_Nhìn_Lâm_Phong/` |
| **Locked** | Kiểm tra `locked_chapters.json` trước khi sửa |

### Task 5: Viết Arc 2 Tuyến Khu Vực
| Khu Vực | Chương | Arc | Skill |
|---------|--------|-----|-------|
| Nam Cương | ch 21-28 | Bão Lửa Sắp Đến | `.claude/skills/chuong-truyen/SKILL.md` |
| Bắc Băng | ch 11-16 | Băng Giải Huyết Hàn | `.claude/skills/chuong-truyen/SKILL.md` |
| Đông Hoang | ch 11-16 | Bước Chân Ra Ngoài | `.claude/skills/chuong-truyen/SKILL.md` |
| Vô Tận Hải | ch 11-16 | Đại Dương Nổi Sóng | `.claude/skills/chuong-truyen/SKILL.md` |
| Tây Mạc | ch 11-16 | Bão Cát Trỗi Dậy | `.claude/skills/chuong-truyen/SKILL.md` |

**Cốt truyện:** `Đạo/Quy_Hoạch_Cốt_Truyện/QUY_HOẠCH_GÓC_NHÌN_PHỤ.md`

### Task 6: Mở Rộng Chương 19 Nhân Vật Phụ
Tất cả đã hoàn thành ch 7-10. Chờ Arc 2 trước khi viết tiếp.

| | File |
|---|---|
| **Skill** | `.claude/skills/chuong-truyen/SKILL.md` |
| **Context** | Từng thư mục `Góc_Nhìn_[Tên]/` trong `Đạo/Chương_Truyện/` |

### Task 14: Tạo Âm Nhạc & Thơ Ca
Sáng tác bài hát, thơ cho các faction và sự kiện.

| | File |
|---|---|
| **Skill Nhạc** | `.claude/skills/am-nhac/SKILL.md` |
| **Skill Thơ** | `.claude/skills/tho-ca/SKILL.md` |
| **Output** | `Đạo/Âm_Nhạc/`, `Đạo/Thơ_Ca/` |

### Task 15: Tạo Hình Ảnh AI Prompt
Tạo prompt cho AI image generation (nhân vật, cảnh, vật phẩm).

| | File |
|---|---|
| **Skill** | `.claude/skills/hoa-si/SKILL.md` |
| **Output** | `Đạo/Ảnh/` |

### Task 16: Quản Lý Timeline
Kiểm tra và cập nhật niên biểu, tránh paradox thời gian.

| | File |
|---|---|
| **Skill** | `.claude/skills/thoi-gian/SKILL.md` |
| **File chính** | `Đạo/Thế_Giới_Và_Thời_Gian/NIÊN_BIỂU_CHÍNH.md` |

### Task 17: Kiểm Duyệt Chất Lượng
Review logic, consistency, continuity của nội dung đã viết.

| | File |
|---|---|
| **Skill** | `.claude/skills/kiem-duyet/SKILL.md` |

---

## 📊 TIẾN ĐỘ CHƯƠNG TRUYỆN

### Nam Cương (12 POV)
| Góc Nhìn | Chương | Ghi Chú |
|-----------|:------:|---------|
| Nam Cương | 135 | Arc 6 — Băng Ngục Thành |
| Lâm Phong | 132 | Catch-up |
| Lệ Vô Tâm | 152 | ✅ Bridge Arc |
| A Ngốc | 152 | ✅ Arc 14 |
| Diệp Tĩnh Sương | 10 | Arc 1 |
| Đan Dương Tử | 10 | ✅ ch 7-10 |
| Diệp Thanh Y | 10 | ✅ ch 6-10 |
| Hàn Thanh Nguyệt | 10 | ✅ ch 7-10 |
| Lục Trần | 10 | ✅ ch 6-10 |
| Độc Cô Lão Quái | 7 | ✅ ch 4-7 |
| Hắc Hạt Ma Trùng | 10 | ✅ ch 7-10 |
| Ngô Công TL | 10 | ✅ ch 7-10 |
| Phương Vô Kỵ | 10 | ✅ ch 7-10 |

### Bắc Băng (3 POV)
| Góc Nhìn | Chương | Ghi Chú |
|-----------|:------:|---------|
| Bắc Băng | 10 | ✅ Arc 1 |
| Lý Tuyết Ưng | 10 | ✅ ch 7-10 |
| Sở Lăng Sương | 10 | ✅ ch 9-10 |
| Triệu Thanh Hằng | 10 | ✅ ch 6-10 |

### Đông Hoang (4 POV)
| Góc Nhìn | Chương | Ghi Chú |
|-----------|:------:|---------|
| Đông Hoang | 10 | ✅ Arc 1 |
| Lục Ly | 10 | ✅ ch 7-10 |
| Nguyệt Dao | 10 | ✅ ch 7-10 |
| Nham Thần | 10 | ✅ ch 7-10 |
| Lục Tiêu | 10 | ✅ ch 7-10 |

### Vô Tận Hải (2 POV)
| Góc Nhìn | Chương | Ghi Chú |
|-----------|:------:|---------|
| Vô Tận Hải | 10 | ✅ Arc 1+2 |
| Lệ Nhược Thủy | 10 | ✅ ch 7-10 |
| Ngao Đình | 10 | ✅ ch 6-10 |

### Tây Mạc (2 POV)
| Góc Nhìn | Chương | Ghi Chú |
|-----------|:------:|---------|
| Tây Mạc | 10 | ✅ Arc 1 |
| Hứa Nhược Thủy | 10 | ✅ ch 1-10 |
| Hứa Thanh Vân | 10 | ✅ ch 1-10 |

### Thiên Trụ
| Góc Nhìn | Chương | Ghi Chú |
|-----------|:------:|---------|
| Thiên Trụ | — | Chưa bắt đầu |
