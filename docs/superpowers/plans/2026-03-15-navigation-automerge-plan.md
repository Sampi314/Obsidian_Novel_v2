# Bilingual Navigation & AI Auto-Merge Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add language navigation links to all documentation, refine Vietnamese headers, and update the auto-merge workflow.

**Architecture:** 
- Add a consistent `<div align="right">` language toggle at the top of 8 Markdown files.
- Perform surgical text replacements in Vietnamese `.md` files to remove English parentheticals and fix typos.
- Update `.github/workflows/auto-merge.yml` with the Gemini CLI actor name.

**Tech Stack:** 
- Markdown
- GitHub Actions (YAML)

---

## Chunk 1: Navigation Links & Header Refinement

**Files:**
- Modify: `README.md`, `README.en.md`
- Modify: `CONTRIBUTING.md`, `CONTRIBUTING.en.md`
- Modify: `SECURITY.md`, `SECURITY.en.md`
- Modify: `CODE_OF_CONDUCT.md`, `CODE_OF_CONDUCT.en.md`

### Task 1: Add Navigation to README
- [ ] **Step 1: Add link to README.md**
Insert at Line 1: `<div align="right">[ [ 🇺🇸 View English Version ] ](./README.en.md)</div>\n\n`
- [ ] **Step 2: Add link to README.en.md**
Insert at Line 1: `<div align="right">[ [ 🇻🇳 Xem Bản Tiếng Việt ] ](./README.md)</div>\n\n`
- [ ] **Step 3: Refine README.md Header**
Change `# 🌌 Hệ Thống Kiến Tạo Thế Giới Tiên Hiệp "Cố Nguyên" (Ancient Origin)` to `# 🌌 Hệ Thống Kiến Tạo Thế Giới Tiên Hiệp "Cố Nguyên"`
- [ ] **Step 4: Commit README changes**
Run: `git add README.md README.en.md && git commit -m "docs: add navigation and refine README headers"`

### Task 2: Add Navigation & Refine CONTRIBUTING
- [ ] **Step 1: Add link to CONTRIBUTING.md**
Insert at Line 1: `<div align="right">[ [ 🇺🇸 View English Version ] ](./CONTRIBUTING.en.md)</div>\n\n`
- [ ] **Step 2: Add link to CONTRIBUTING.en.md**
Insert at Line 1: `<div align="right">[ [ 🇻🇳 Xem Bản Tiếng Việt ] ](./CONTRIBUTING.md)</div>\n\n`
- [ ] **Step 3: Refine CONTRIBUTING.md Headers**
Remove any parenthetical English in headers (e.g., `(Internal Maintenance Guide)`).
- [ ] **Step 4: Commit CONTRIBUTING changes**
Run: `git add CONTRIBUTING.md CONTRIBUTING.en.md && git commit -m "docs: add navigation and refine CONTRIBUTING headers"`

### Task 3: Add Navigation & Refine SECURITY
- [ ] **Step 1: Add link to SECURITY.md**
Insert at Line 1: `<div align="right">[ [ 🇺🇸 View English Version ] ](./SECURITY.en.md)</div>\n\n`
- [ ] **Step 2: Add link to SECURITY.en.md**
Insert at Line 1: `<div align="right">[ [ 🇻🇳 Xem Bản Tiếng Việt ] ](./SECURITY.md)</div>\n\n`
- [ ] **Step 3: Refine SECURITY.md Headers**
Remove parenthetical English and fix `## ⚠️ Cảnh Báo Về Script Tự Đỗ` typo to `## ⚠️ Cảnh Báo Về Script Tự Động`.
- [ ] **Step 4: Commit SECURITY changes**
Run: `git add SECURITY.md SECURITY.en.md && git commit -m "docs: add navigation and refine SECURITY headers"`

### Task 4: Add Navigation & Refine CODE_OF_CONDUCT
- [ ] **Step 1: Add link to CODE_OF_CONDUCT.md**
Insert at Line 1: `<div align="right">[ [ 🇺🇸 View English Version ] ](./CODE_OF_CONDUCT.en.md)</div>\n\n`
- [ ] **Step 2: Add link to CODE_OF_CONDUCT.en.md**
Insert at Line 1: `<div align="right">[ [ 🇻🇳 Xem Bản Tiếng Việt ] ](./CODE_OF_CONDUCT.md)</div>\n\n`
- [ ] **Step 3: Refine CODE_OF_CONDUCT.md Headers**
Remove `(Code of Conduct)` from title and ensure all sub-headers are Vietnamese-only.
- [ ] **Step 4: Commit CODE_OF_CONDUCT changes**
Run: `git add CODE_OF_CONDUCT.md CODE_OF_CONDUCT.en.md && git commit -m "docs: add navigation and refine CoC headers"`

---

## Chunk 2: Auto-Merge Workflow Update

**Files:**
- Modify: `.github/workflows/auto-merge.yml`

### Task 1: Update Auto-Merge List
- [ ] **Step 1: Add Gemini CLI actor**
Append `|| github.actor == 'google-labs-gemini-cli[bot]'` to the `if:` condition in `.github/workflows/auto-merge.yml`.
- [ ] **Step 2: Verify YAML syntax**
Run: `gh workflow view "Auto Merge"` (This validates the remote version) or perform a manual indentation/syntax check.
- [ ] **Step 3: Commit workflow changes**
Run: `git add .github/workflows/auto-merge.yml && git commit -m "ci: add gemini-cli to auto-merge list"`

---

## Chunk 3: Final Validation

### Task 1: Verify All Links
- [ ] **Step 1: Run link checker**
Run: `python3 scripts/check_links.py`
Expected: Zero broken links in the newly added navigation headers.
- [ ] **Step 2: Manual spot check**
Verify the language toggle alignment in at least one file.
