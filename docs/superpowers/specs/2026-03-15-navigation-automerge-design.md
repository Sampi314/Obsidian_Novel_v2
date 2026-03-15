# Design Document: Bilingual Documentation Navigation & AI Auto-Merge Refinement

**Date:** 2026-03-15  
**Author:** Gemini CLI  
**Status:** Approved  
**Topic:** Improving Documentation Accessibility and Automation Reliable-ness  

## 1. Objective
Refine the bilingual documentation suite ("Cố Nguyên") to provide seamless language navigation, ensure the primary Vietnamese versions are idiomatic (no English headers), and update the auto-merge list to include the Gemini CLI agent.

## 2. Success Criteria
*   **Navigation:** Every documentation file has a clear language toggle at the top (top-right style).
*   **Vietnamese-First:** `CODE_OF_CONDUCT.md` and other primary files (`.md`) use exclusively Vietnamese headers.
*   **Auto-Merge:** `.github/workflows/auto-merge.yml` includes `google-labs-gemini-cli[bot]`.
*   **Consistency:** All 8 files follow the same structure and link mapping.

## 3. Architecture & Structure

### 3.1. Language Navigation Header
The following links will be added at the very top of each file (Line 1):

*   **Vietnamese Files (`.md`):**
    ```markdown
    [ [ 🇺🇸 View English Version ] ](./[FILE].en.md)
    ```
*   **English Files (`.en.md`):**
    ```markdown
    [ [ 🇻🇳 Xem Bản Tiếng Việt ] ](./[FILE].md)
    ```

**File Mappings:**
- `README.md` <-> `README.en.md`
- `CONTRIBUTING.md` <-> `CONTRIBUTING.en.md`
- `SECURITY.md` <-> `SECURITY.en.md`
- `CODE_OF_CONDUCT.md` <-> `CODE_OF_CONDUCT.en.md`

### 3.2. Vietnamese Header Refinement
- **`CODE_OF_CONDUCT.md`:** 
    - Change `# 🤝 Bộ Quy Tắc Ứng Xử (Code of Conduct)` to `# 🤝 Bộ Quy Tắc Ứng Xử`.
    - Ensure all sub-headers are only in Vietnamese.
- **`README.md`:**
    - Change `# 🌌 Hệ Thống Kiến Tạo Thế Giới Tiên Hiệp "Cố Nguyên" (Ancient Origin)` to `# 🌌 Hệ Thống Kiến Tạo Thế Giới Tiên Hiệp "Cố Nguyên"`.
- **`SECURITY.md`:**
    - Change `## ⚠️ Cảnh Báo Về Script Tự Đỗ` to `## ⚠️ Cảnh Báo Về Script Tự Động`.
- **Other Primary Docs:** Review and remove any parenthetical English in headers (e.g., `(Security Policy)`).

### 3.3. Auto-Merge Workflow Update
- **File:** `.github/workflows/auto-merge.yml`
- **Action:** Add `github.actor == 'google-labs-gemini-cli[bot]'` to the `if:` condition list.
- **Existing Actors:** Keep all current actors (`Sampi314`, `google-labs-jules[bot]`, `claude[bot]`, `gemini[bot]`).

## 4. Implementation Strategy
1.  **Prep:** Verify current actor and push access (done).
2.  **Navigation:** Apply the navigation link to all 8 files.
3.  **Refinement:** Clean up headers in the 4 primary Vietnamese files.
4.  **Auto-Merge:** Update the GitHub Actions YAML.
5.  **Validation:** Verify all links and workflow syntax.

## 5. Risks & Mitigations
*   **Risk:** Link breakage due to incorrect relative paths.
*   **Mitigation:** Manual verification and link-checking script run after implementation.
*   **Risk:** Auto-merge workflow syntax error.
*   **Mitigation:** Use `gh workflow view` or similar to verify the action is active and valid.
