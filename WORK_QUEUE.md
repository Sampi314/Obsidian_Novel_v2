# Work Queue — Cố Nguyên Giới

> Agent đọc file này để biết **task hiện tại** và **tiến độ**.
> Tất cả agents cùng làm chung 1 task cho đến khi xong.
> Sau khi xong mỗi phiên, agent cập nhật tiến độ ở đây → push.

---

## 🔴 Task Hiện Tại: Task 10 — Populate Faction Rosters

**Plan:** `.claude/plans/populate_factions.md`
**Skill:** `.claude/skills/nhan-vat/SKILL.md` (Chế Độ 1)

### Phase 1: Leadership (Thái Thượng → Phong Chủ)

| Thế Lực | Khu Vực | Hạng | Có | Cần | Trạng Thái |
|---------|---------|------|:--:|:---:|------------|
| Cửu Hoa Kiếm Tông | Đông Hoang | Nhất | 92 | ~35 leadership | ✅ Done |
| Thần Khí Phường | Đông Hoang | Nhất | 0 | ~20 | ⬜ Pending |
| Dược Vương Cốc | Đông Hoang | Nhất | 3 | ~20 | ⬜ Pending |
| Huyền Băng Cung | Bắc Băng | Nhất | 0 | ~20 | ⬜ Pending |
| Vân Tông | Đông Hoang | Nhất | 12 | ~15 | ⬜ Pending |
| Thanh Đế Cung | Đông Hoang | Nhất | 10 | ~15 | ⬜ Pending |
| Thái Ất Môn | Đông Hoang | Nhất | 10 | ~15 | ⬜ Pending |
| Vô Tranh Tự | Đông Hoang | Nhất | 10 | ~15 | ⬜ Pending |
| Vũ Hoàng Các | Đông Hoang | Nhất | 8 | ~15 | ⬜ Pending |
| Huyết Sát Minh | Đông Hoang | Nhất | 10 | ~15 | ⬜ Pending |
| Huyết Ma Tông | Nam Cương | Nhất | 10 | ~15 | ⬜ Pending |
| Vạn Độc Môn | Nam Cương | Nhất | 25 | ~10 | ⬜ Pending |
| Đan Hà Cốc | Nam Cương | Nhất | 20 | ~10 | ⬜ Pending |
| Kim Sa Tự | Tây Mạc | Nhất | 10 | ~15 | ⬜ Pending |
| Thiên Sa Thương Hội | Tây Mạc | Nhất | 11 | ~15 | ⬜ Pending |
| Hải Thần Cung | Vô Tận Hải | Nhất | 30 | ~10 | ⬜ Pending |
| Phong Bạo Thương Đội | Vô Tận Hải | Nhất | 9 | ~15 | ⬜ Pending |
| Đại Càn Hoàng Triều | Thiên Trụ | Nhất | 16 | ~15 | ⬜ Pending |
| Cửu U Ma Tông | Thiên Trụ | Nhất | 14 | ~10 | ⬜ Pending |
| Thiên Kiêu Học Viện | Thiên Trụ | Nhất | 11 | ~15 | ⬜ Pending |
| Bách Bảo Các | Thiên Trụ | Nhất | 7 | ~15 | ⬜ Pending |
| Thiên Mộc Thành | Thiên Trụ | Nhất | 8 | ~15 | ⬜ Pending |
| Lôi Trì Thánh Địa | Thiên Trụ | Nhất | 8 | ~15 | ⬜ Pending |
| Thiên Môn Kính Đài | Thiên Trụ | Nhất | 6 | ~15 | ⬜ Pending |
| Trích Tinh Lâu | Thiên Trụ | Nhất | 5 | ~10 | ⬜ Pending |
| Long Cung | Vô Tận Hải | Nhất | 17 | ~10 | ⬜ Pending |
| Bắc Hải Cự Yêu Hang | Bắc Băng | Nhất | 8 | ~10 | ⬜ Pending |
| Cực Quang Thần Điện | Bắc Băng | Nhất | 29 | ~10 | ⬜ Pending |
| Thiên Yêu Đình | Đông Hoang | Nhất | 33 | ~5 | ⬜ Pending |
| Tinh Linh Vương Đình | Đông Hoang | Nhất | 23 | ~10 | ⬜ Pending |
| Vạn Yêu Thành | Đông Hoang | Nhất | 20 | ~10 | ⬜ Pending |
| Thiên Trụ Hộ Vệ Đoàn | Đông Hoang | Nhất | 10 | ~15 | ⬜ Pending |
| Ảnh Nguyệt Uyển | Đông Hoang | Nhất | 10 | ~15 | ⬜ Pending |

### Phase 2-5: Chưa bắt đầu
_(Sẽ cập nhật khi Phase 1 hoàn thành)_

---

## ⏳ Task Queue (Chờ)

| Task | Plan File | Skill File | Ghi Chú |
|------|-----------|-----------|---------|
| Task 9: Điền nhân vật | `populate_factions.md` | `nhan-vat (Chế Độ 2)` | Chờ Task 10 |
| Task 11: Enrich Thế Lực | — | `the-luc` | Chờ |
| Task 12: Enrich Lore | — | `ky-vat, chung-toc, cong-phap...` | Chờ |
| Task 2: Catch-up Lâm Phong | — | `chuong-truyen` | Chờ |
| Task 5: Arc 2 | — | `chuong-truyen` | Chờ |

---

## ✅ Hoàn Thành

| Task | Ngày | Ghi Chú |
|------|------|---------|
| Task 48: Rename race chars | 2026-03-21 | 50 chars renamed across 8 races |
| Enrich 229 Thế Lực | 2026-03-20 | Fill YAML + 11 sections |
| Enrich Kỳ Vật, Chủng Tộc | 2026-03-20 | 41 kỳ vật + 8 races |
| Enrich Trận Pháp, Luyện Khí | 2026-03-20 | 7 + 8 files |
