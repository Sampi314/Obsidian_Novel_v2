# Documentation Update Implementation Plan: "Cố Nguyên" Reference Archive

> **For agentic workers:** REQUIRED: Use superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Transform public documentation into a high-quality, bilingual (Vietnamese/English) "Reference Archive" for a private world-building project.

**Architecture:** 
- Each document has a primary Vietnamese file (`[FILE].md`) and an English counterpart (`[FILE].en.md`).
- Content follows the "Reference Archive" approach (private/personal status, AI-maintenance focus).
- No new technical systems; primarily content creation and structural updates.

**Tech Stack:** 
- Markdown for documentation.
- Custom Claude Code Skills (reference only).
- Python/JS Maintenance Scripts (reference only).

---

## Chunk 1: Drafting Vietnamese Documentation (Core)

**Files:**
- Modify: `README.md`
- Modify: `CONTRIBUTING.md`
- Modify: `SECURITY.md`
- Modify: `CODE_OF_CONDUCT.md`

### Task 1: Update README.md (Vietnamese)
- [ ] **Step 1: Draft the new README.md content**
Include:
- Project title: Hệ Thống Kiến Tạo Thế Giới Tiên Hiệp "Cố Nguyên"
- Private Status Badge/Notice
- Introduction with Lore summary and project goals
- Description of `Đạo/` directory taxonomy
- Explanation of `reader.html`
- Overview of AI Skills in `.claude/skills/`
- Technical Stack (Python/JS maintenance scripts, custom reader)

- [ ] **Step 2: Apply changes to README.md**
- [ ] **Step 3: Verify content for broken internal links**
Run: `python scripts/check_links.py`
Expected: Zero broken links within the updated documentation.

### Task 2: Update CONTRIBUTING.md (Vietnamese)
- [ ] **Step 1: Draft the new CONTRIBUTING.md content**
Include:
- Notice that project is CLOSED to public contributions.
- Strict Vietnamese naming convention guide (accents + underscores).
- Instructions for AI Agents:
    - YAML schema and link maintenance.
    - Leveraging the 21 specialized skills mentioned in README.
- Reference to maintenance scripts in `scripts/`.

- [ ] **Step 2: Apply changes to CONTRIBUTING.md**
- [ ] **Step 3: Commit Vietnamese Core Docs**
Run: `git commit -m "docs(vn): update core documentation to reference archive status"`

### Task 3: Update SECURITY.md & CODE_OF_CONDUCT.md (Vietnamese)
- [ ] **Step 1: Draft and update SECURITY.md**
Include: Contact `nkhoihue@gmail.com`.
- [ ] **Step 2: Draft and update CODE_OF_CONDUCT.md**
Include: Professional standards for AI-human interaction and public reference.
- [ ] **Step 3: Commit safety docs**
Run: `git commit -m "docs(vn): update security and conduct policies"`

---

## Chunk 2: English Translation and Terminology Guide

**Files:**
- Create: `README.en.md`
- Create: `CONTRIBUTING.en.md`
- Create: `SECURITY.en.md`
- Create: `CODE_OF_CONDUCT.en.md`

### Task 1: Create README.en.md with Terminology Guide
- [ ] **Step 1: Translate Vietnamese README to English**
Ensure "Tiên Hiệp" nuances are preserved.
- [ ] **Step 2: Add Terminology Guide section**
Include terms: Tiên Hiệp (Xianxia), Linh Khí (Spiritual Qi), Công Pháp (Cultivation Method), etc.
- [ ] **Step 3: Write README.en.md**
- [ ] **Step 4: Verify formatting**

### Task 2: Create CONTRIBUTING.en.md (English)
- [ ] **Step 1: Translate CONTRIBUTING.md to English**
Clearly state the PR/Issue policy for English-speaking visitors.
- [ ] **Step 2: Write CONTRIBUTING.en.md**

### Task 3: Create SECURITY.en.md & CODE_OF_CONDUCT.en.md (English)
- [ ] **Step 1: Create English versions of safety docs**
- [ ] **Step 2: Final Verification of all 8 files**
- [ ] **Step 3: Commit English Docs**
Run: `git commit -m "docs(en): add English versions and terminology guide"`
