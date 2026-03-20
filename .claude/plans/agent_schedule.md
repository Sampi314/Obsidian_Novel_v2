# Agent Schedule — Cố Nguyên Giới

> Tệp này là **nguồn chân lý duy nhất** cho tất cả agents (Claude, Jules, Gemini, hoặc bất kỳ agent nào).
> Mọi skills nằm tại `.claude/skills/[tên]/SKILL.md`.

---

## 📌 NHIỆM VỤ THEO ƯU TIÊN

### 🔴 1. Task 10: Populate Faction Rosters
> **Plan chi tiết:** `.claude/plans/populate_factions.md`
> **Work queue:** `WORK_QUEUE.md`
> **Skill:** `.claude/skills/nhan-vat/SKILL.md` (Chế Độ 1)

**Phân vùng gợi ý (tránh overlap qua WORK_QUEUE.md):**

| Slot | Khu Vực | Thế Lực Hạng Nhất |
|------|---------|-------------------|
| A | Đông Hoang | Cửu Hoa, Vân Tông, Thanh Đế Cung, Thái Ất, Huyết Sát Minh, Thần Khí Phường, Dược Vương Cốc, Vô Tranh Tự, Vạn Yêu Thành, Thiên Yêu Đình, Tinh Linh Vương Đình, Vũ Hoàng Các, Ảnh Nguyệt Uyển, Thiên Trụ Hộ Vệ Đoàn |
| B | Nam Cương | Vạn Độc Môn, Đan Hà Cốc, Huyết Ma Tông |
| C | Thiên Trụ | Đại Càn Hoàng Triều, Cửu U Ma Tông, Thiên Kiêu Học Viện, Bách Bảo Các, Thiên Mộc Thành, Lôi Trì, Trích Tinh Lâu, Thiên Môn Kính Đài |
| D | Vô Tận Hải | Hải Thần Cung, Long Cung, Phong Bạo Thương Đội |
| E | Bắc Băng | Huyền Băng Cung, Cực Quang Thần Điện, Bắc Hải Cự Yêu Hang |
| F | Tây Mạc | Kim Sa Tự, Thiên Sa Thương Hội |

**Mỗi phiên:** 1 thế lực, 10-100 chars tùy phase.

---

### 🟡 2. Task 9: Điền Chi Tiết Nhân Vật
> **Skill:** `.claude/skills/nhan-vat/SKILL.md` (Chế Độ 2)
> **Khi nào:** Song song với Task 10 hoặc sau khi Task 10 Phase 1-2 xong.

```bash
python3 scripts/find_unfilled_chars.py 3
```
Mỗi phiên điền 2-3 nhân vật có `*(Chưa xác định)*`.

---

### 🟢 3. Viết Chương (SAU Task 9+10 Phase 1-2)

#### Task 2: Catch-up Lâm Phong
- Viết chương 133+ cho Góc Nhìn Lâm Phong
- Skill: `.claude/skills/chuong-truyen/SKILL.md`

#### Task 5: Arc 2 Tuyến Khu Vực
| Khu Vực | Chương Cần Viết | Arc |
|---------|----------------|-----|
| Nam Cương | ch 21-28 | Arc 2 — Bão Lửa Sắp Đến |
| Bắc Băng | ch 11-16 | Arc 2 — Băng Giải Huyết Hàn |
| Đông Hoang | ch 11-16 | Arc 2 — Bước Chân Ra Ngoài |
| Vô Tận Hải | ch 11-16 | Arc 2 — Đại Dương Nổi Sóng |
| Tây Mạc | ch 11-16 | Arc 2 — Bão Cát Trỗi Dậy |

Tham khảo: `Đạo/Quy_Hoạch_Cốt_Truyện/QUY_HOẠCH_GÓC_NHÌN_PHỤ.md`

#### Task 6: Mở rộng chương 19 nhân vật phụ
Tất cả đã hoàn thành ch 7-10. Chờ Arc 2 trước khi viết tiếp.

---

## 📌 TIẾN ĐỘ CHƯƠNG TRUYỆN

### Nam Cương (12 POV)
| Góc Nhìn | Chương | Ghi Chú |
|-----------|:------:|---------|
| Nam Cương | 135 | Arc 6 — Băng Ngục Thành |
| Diệp Tĩnh Sương | 10 | Arc 1 |
| Lâm Phong | 132 | Catch-up |
| Lệ Vô Tâm | 152 | ✅ Bridge Arc xong |
| A Ngốc | 152 | ✅ Arc 14 xong |
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

---

## 📌 QUY TẮC CHUNG

- **Ngôn ngữ:** Vietnamese only (không English trong nội dung sáng tạo)
- **Tên:** Mỗi tên do AI đặt, có ý nghĩa xianxia. KHÔNG dùng chức danh làm tên.
- **Work Queue:** BẮT BUỘC claim trong `WORK_QUEUE.md` trước khi bắt đầu bất kỳ task nào
- **Locked Chapters:** Kiểm tra `locked_chapters.json` trước khi sửa chương
- **Skills:** Tất cả tại `.claude/skills/[tên]/SKILL.md`
- **Plans:** Tất cả tại `.claude/plans/`
