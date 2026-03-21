# Daily Tasks — Việc Mặc Định Khi Không Có Task Cụ Thể

> Nếu không có file `01_`, `02_`... nào trong `.claude/plans/`,
> hoặc tất cả hàng trong bảng Work Queue đang 🔄/✅, thì làm việc trong danh sách này.

---

## 1. Điền Chi Tiết Nhân Vật Còn Placeholder
> **Skill:** `.claude/skills/nhan-vat/SKILL.md` (Chế Độ 2)

```bash
python3 scripts/find_unfilled_chars.py 3
```
Chọn 2-3 nhân vật có `*(Chưa xác định)*` → điền Section II-V.

---

## 2. Enrichen Thế Lực Mỏng
> **Skill:** `.claude/skills/the-luc/SKILL.md`

```bash
find Đạo/Thế_Lực -name "*.md" ! -name "index.md" -exec sh -c 'lines=$(wc -l < "$1"); if [ "$lines" -lt 130 ]; then echo "$lines $1"; fi' _ {} \; | sort -n | head -5
```
Chọn file ngắn nhất → mở rộng 11 sections với nội dung chi tiết hơn.

---

## 3. Enrichen Kỳ Vật / Chủng Tộc / Công Pháp
> **Skills:**
> - `.claude/skills/ky-vat/SKILL.md`
> - `.claude/skills/chung-toc/SKILL.md`
> - `.claude/skills/cong-phap/SKILL.md`

Tìm file ngắn nhất trong `Đạo/Kỳ_Vật/`, `Đạo/Chủng_Tộc/`, `Đạo/Công_Pháp/` → mở rộng nội dung.

---

## 4. Kiểm Tra Chất Lượng
> **Skill:** `.claude/skills/kiem-duyet/SKILL.md`

Chọn 1 thế lực hoặc 1 nhóm nhân vật → kiểm tra tính nhất quán (tên, tu vi, quan hệ, chủng tộc).
