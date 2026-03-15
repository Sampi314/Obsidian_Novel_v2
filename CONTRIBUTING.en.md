<div align="right">[ [ 🇻🇳 Xem Bản Tiếng Việt ] ](./CONTRIBUTING.md)</div>

# 🛠️ Maintenance & Content Standards

> [!CAUTION]
> **PRIVATE PROJECT - NO PUBLIC CONTRIBUTIONS ACCEPTED**
> This repository is established for personal world-building and development with AI assistance. We **DO NOT** accept Pull Requests or Issues from the community. Any public contributions will be closed or ignored.

---

## 🤖 AI Agent Workflow

To maintain the consistency of the "Cố Nguyên" world, AI agents (Claude Code, Gemini, etc.) must strictly adhere to the following steps when performing maintenance or creation tasks:

### 1. Consistency Check
- Before adding any new entity (Character, Sect, Technique), the AI must read the master file `Đạo/HỒ_SƠ_THẾ_GIỚI.md`.
- Ensure new entities do not conflict with existing settings regarding realms, geography, or history.

### 2. Specialized AI Skills (Claude Code Skills)
Use the established skills in `.claude/skills/` for specific tasks. For example:
- Use `/nhan-vat` to create new character profiles with standardized YAML frontmatter.
- Use `/kiem-duyet` after writing chapters to ensure quality.
- Use `/quan-he` to update relationship charts when plot points change.

### ### 3. Naming & Storage Rules
- **REQUIRED**: Filenames MUST be in **Vietnamese with accents**.
- **SPACES**: Replace with underscores (`_`).
- **PATHS**: Save to the correct functional directories within `Đạo/`.
  - *Standard Example*: `Đạo/Công_Pháp/Thái_Cực_Kiếm_Phổ.md`
  - *Incorrect Example*: `Dao/Cong_Phap/thai cuc kiem pho.md`

### 4. Metadata Structure (YAML Frontmatter)
Every content file must have complete YAML frontmatter according to the entity's schema.
- `type`: `character`, `faction`, `chapter`, `item`, etc.
- `tags`: Classification keywords.
- `status`: Entity state (Active, Deceased, Hidden).

---

## 🔧 Maintenance Scripts

Use the scripts in the `scripts/` directory to automate maintenance:

- `python3 scripts/update_chapter_data.py`: Update chapter lists and index.
- `node scripts/generate_wiki_index.mjs`: Rebuild the search index for the wiki.
- `python3 scripts/check_links.py`: Verify the integrity of internal links.

---

## ⚙️ Git Configuration

To avoid display issues with Vietnamese filenames in the terminal:

```bash
git config core.quotePath false
```

---
*This document serves as an internal operational guide between the User and AI.*
