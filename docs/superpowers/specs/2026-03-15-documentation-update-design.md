# Design Document: Personal World-Building Documentation Update ("Cố Nguyên")

**Date:** 2026-03-15  
**Author:** Gemini CLI  
**Status:** Approved  
**Topic:** Documentation Revamp for Bilingual Reference Archive  

## 1. Objective
Transform the repository's public documentation (README, CONTRIBUTING, SECURITY, CODE_OF_CONDUCT) into a high-quality, bilingual (Vietnamese/English) "Reference Archive." This reflects that the project is a private, personal world-building system for a "Tiên Hiệp" (Xianxia) setting, utilizing specialized AI "Claude Code Skills" and custom automation.

## 2. Success Criteria
*   **Bilingual Accessibility:** Each document has a primary Vietnamese version (`[FILE].md`) and a secondary English version (`[FILE].en.md`).
*   **Clear Project Status:** Explicitly states the project is private/personal and closed to external contributions.
*   **Technical Accuracy:** Correctly describes the "Claude Code Skills," the `Đạo/` directory taxonomy, and the interactive `reader.html` system.
*   **Operational Integrity:** Includes specific instructions for AI agents to maintain strict Vietnamese naming conventions and YAML schemas.
*   **Contact Information:** All documents point to `nkhoihue@gmail.com` for relevant inquiries (security, etc.).

## 3. Architecture & Structure

### 3.1. File Mapping
| Original File | New Vietnamese (Default) | New English (Suffix) |
| :--- | :--- | :--- |
| `README.md` | `README.md` (Updated) | `README.en.md` (New) |
| `CONTRIBUTING.md` | `CONTRIBUTING.md` (Updated) | `CONTRIBUTING.en.md` (New) |
| `SECURITY.md` | `SECURITY.md` (Updated) | `SECURITY.en.md` (New) |
| `CODE_OF_CONDUCT.md` | `CODE_OF_CONDUCT.md` (Updated) | `CODE_OF_CONDUCT.en.md` (New) |

### 3.2. README Specification
*   **Primary Message:** "Cố Nguyên" (Ancient Origin) is a personal Tiên Hiệp world-building project.
*   **Sections:**
    1.  **Project Title & Status:** "Archive/Personal" status badge.
    2.  **Introduction:** Lore summary and project goal (systematic world construction).
    3.  **World Taxonomy (`Đạo/`):** Explanation of sub-directories (Characters, Sects, Items, etc.).
    4.  **Interactive Reader:** Description of `reader.html` and its ability to parse YAML-frontmatter content.
    5.  **AI Integration:** Introduction to the 21 specialized `Claude Code Skills` that act as domain experts.
    6.  **Technical Stack:** Brief mention of Python/JS maintenance scripts.
    7.  **Terminology Guide (English Only):** A brief glossary of Hán-Việt terms translated to English to preserve nuance.

### 3.3. CONTRIBUTING Specification (Internal Guide)
*   **External Policy:** "This repository is CLOSED to public Pull Requests and Issues."
*   **Internal Workflow:**
    *   **Naming Convention:** All content files in `Đạo/` MUST use Vietnamese characters with accents and underscores for spaces (e.g., `Nhân_Vật_Chính.md`).
    *   **YAML Schema:** Strict adherence to metadata fields for different entity types (Chapter, Character, Faction).
    *   **AI Agency Rules:** Explicit instructions for LLM assistants (like Claude/Gemini) on how to navigate the graph-like world data without breaking links.

### 3.4. SECURITY & CODE OF CONDUCT
*   **Security:** Standard policy reporting to `nkhoihue@gmail.com`.
*   **CoC:** Maintains professional standards for AI-human interaction and public reference.

## 4. Implementation Strategy
1.  **Content Drafting:** Draft Vietnamese versions first, ensuring idiomatic Tiên Hiệp terminology.
2.  **Translation:** Produce accurate English counterparts that preserve the "Reference Archive" tone.
3.  **Validation:** Use `grep_search` to ensure no placeholder emails remain.
4.  **Deployment:** Write the files and verify directory structure.

## 5. Risks & Mitigations
*   **Risk:** English translations lose the nuance of the Chinese-Vietnamese (Hán-Việt) cultivation terms.
*   **Mitigation:** Include a brief terminology guide or parenthetical translations where necessary.
*   **Risk:** AI agents misinterpret the "Closed" status as a reason to stop following rules.
*   **Mitigation:** The `CONTRIBUTING` guide will clearly distinguish between "Public Contribution" (Disabled) and "AI Maintenance" (Strictly Required).
