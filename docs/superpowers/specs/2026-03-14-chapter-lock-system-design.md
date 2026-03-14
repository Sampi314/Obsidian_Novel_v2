# Chapter Lock System — Design Spec

## Overview

A chapter review/lock system for the Cố Nguyên Giới novel project. The author marks chapters as "approved" from either the index page or reader page, which commits a lock file to the GitHub repo. AI agents and GitHub Actions enforce that locked chapters are never modified.

## Components

### 1. Index Page (`index.html`)

**Login button:**
- "Login with GitHub" button in the navbar (and mobile hamburger menu)
- After login: shows GitHub avatar + "Logout" option
- Session expires after 3 hours (token timestamp in localStorage; also enforced by an in-page timer that clears the token at the 3-hour mark even without a page reload)
- On expiry: clears token, shows login button again

**Expandable chapter lists:**
- Each POV card gets an expand/collapse toggle (e.g., chevron icon)
- When expanded, loads individual chapters from `chapter_data.js` under the card
- Each chapter shows its title + a checkmark toggle (if logged in) or read-only ✓ (if locked and not logged in)
- **Path construction:** The full chapter path is derived by extracting the directory path from the POV card's `href` attribute (e.g., `Đạo/Chương_Truyện/Bắc_Băng/Góc_Nhìn_Bắc_Băng/`) and appending the chapter filename from `chapter_data.js`

**Chapter checkmarks (when logged in):**
- Subtle checkmark (✓) next to each chapter title
- Clicking toggles locked/unlocked state
- Commits updated `locked_chapters.json` via GitHub API (`PUT /repos/:owner/:repo/contents/locked_chapters.json`)
- UI waits for commit to succeed before updating checkmark (pessimistic update); reverts on error
- Brief loading indicator while committing
- Locked: ✓ in accent color
- Unlocked: faint outline or empty clickable area

**Chapter checkmarks (when not logged in):**
- Read-only display — locked chapters show ✓ but are not clickable
- Anyone can see which chapters are finalized

### 2. Reader Page (`reader.html`)

**Shared auth state:**
- Reads the same OAuth token from localStorage as the index page
- Shows login/logout button consistent with index page

**Chapter checkmarks in MỤC_LỤC view:**
- When viewing a MỤC_LỤC.md (table of contents), each chapter link gets a checkmark toggle
- Same behavior as index page: toggle commits to `locked_chapters.json`
- Read-only ✓ for non-authenticated visitors
- Checkmarks do NOT appear on individual chapter reading views — only on MỤC_LỤC listings

### 3. Lock File (`locked_chapters.json`)

Located in repo root. Format:

```json
{
  "locked_chapters": [
    "Đạo/Chương_Truyện/Bắc_Băng/Góc_Nhìn_Bắc_Băng/Chương_00001_Băng_Tâm_Vỡ_Nát.md",
    "Đạo/Chương_Truyện/Bắc_Băng/Góc_Nhìn_Bắc_Băng/Chương_00002_Ôn_Dịch_Và_Hàn_Liên.md"
  ],
  "last_updated": "2026-03-14T10:30:00Z",
  "updated_by": "Sampi314"
}
```

- Full file paths from repo root (including region directory, e.g., `Bắc_Băng/Góc_Nhìn_Bắc_Băng/`)
- Flat array — simple to read, write, and check
- `updated_by` sourced from the OAuth token's authenticated user

**First-use:** When `locked_chapters.json` does not yet exist, the first lock action creates it via the GitHub API (PUT without SHA creates a new file).

### 4. OAuth Proxy (Cloudflare Worker)

A small serverless function:

- **Endpoint:** `POST /api/auth/github`
- **Input:** OAuth `code` from GitHub redirect
- **Action:** Exchanges code for access token using client secret (stored as Worker env var)
- **Returns:** JSON response: `{ "access_token": "gho_xxxx" }`
- **CORS:** Returns `Access-Control-Allow-Origin` header for the GitHub Pages domain only. Handles `OPTIONS` preflight requests with `Access-Control-Allow-Methods: POST, OPTIONS` and `Access-Control-Allow-Headers: Content-Type`.

Free tier on Cloudflare Workers.

**OAuth scope:** `public_repo` (least-privilege for committing to a public repo).

**One-time setup:**
1. Create a GitHub OAuth App (GitHub Settings → Developer Settings → OAuth Apps)
   - Set redirect URI to the GitHub Pages URL: `https://sampi314.github.io/Obsidian_Novel_v2/`
   - This means OAuth login always redirects back to `index.html`. If login is initiated from `reader.html`, the user returns to the index page (token is stored in localStorage and shared across pages).
   - Note the Client ID
2. Create a free Cloudflare account + Worker
3. Add `CLIENT_ID` and `CLIENT_SECRET` as Worker environment variables

### 5. CLAUDE.md Instructions

A `CLAUDE.md` file in repo root with:

```markdown
## Locked Chapters

Before editing any chapter file in `Đạo/Chương_Truyện/`, check `locked_chapters.json` in the repo root.
If the chapter's file path is listed in `locked_chapters`, DO NOT modify it.
These chapters are approved for publication and must not be changed.
Do NOT modify `locked_chapters.json` itself — it is managed exclusively by the author through the web UI.
```

### 6. GitHub Action (`protect-locked-chapters.yml`)

- **Triggers on:** pull requests that touch files in `Đạo/Chương_Truyện/`
- **Reads:** `locked_chapters.json` from the base branch
- **Compares:** changed files in the PR against the locked list
- **If locked chapter modified:** PR check fails with error listing which locked chapters were touched

**Auto-merge integration:** The existing `auto-merge.yml` must be updated to wait for the lock-check status before merging. Change from immediate `gh pr merge` to `gh pr merge --auto --merge` so it respects required status checks. A branch protection rule on `main` must also be added requiring the `protect-locked-chapters` check to pass.

## Authentication Flow

```
User clicks "Login with GitHub" (on index.html or reader.html)
  → Browser redirects to GitHub OAuth consent page (scope: public_repo)
  → User authorizes the app
  → GitHub redirects back to index.html with ?code=xxx
  → Index page sends code to Cloudflare Worker (POST /api/auth/github)
  → Worker exchanges code for access token (using client secret)
  → Worker returns { "access_token": "gho_xxxx" }
  → Page calls GET /user to verify the authenticated user is the repo owner (login === "Sampi314")
  → If not the owner: token discarded, error message shown
  → If owner: token + timestamp stored in localStorage
  → User sees checkmark toggles next to chapters

After 3 hours (checked on page load AND via in-page timer):
  → Token expired → cleared from localStorage
  → User sees "Login with GitHub" button again
```

## Lock/Unlock Flow

```
User clicks checkmark next to a chapter
  → Frontend reads current locked_chapters.json via GitHub API (GET)
     → If 404 (first use): initialize empty locked_chapters structure, no SHA needed
     → If 200: parse content and note the SHA
  → Adds or removes the chapter path from the array
  → Updates last_updated and updated_by
  → Commits updated file via GitHub API (PUT with SHA for conflict detection)
     → If 409 (SHA conflict): re-fetch latest file, re-apply the toggle, retry PUT (max 3 retries)
     → If 401/403: token likely revoked/expired, clear session and prompt re-login
     → If other error: show error message to user
  → On success: UI updates checkmark state
  → On failure: checkmark remains unchanged
  → Loading indicator shown during commit
```

## Security

- **Owner-only access:** After OAuth login, the frontend calls `GET /user` and verifies `login === "Sampi314"`. Non-owners are rejected.
- Client secret never exposed in frontend code (lives in Cloudflare Worker env vars)
- GitHub API requires the authenticated token to commit — no anonymous writes
- 3-hour session expiry (enforced on page load and by in-page timer)
- GitHub Action provides server-side enforcement even if the lock file is bypassed
- Branch protection rule ensures locked chapter check must pass before merge
- `locked_chapters.json` is protected from agent modification via CLAUDE.md instructions

## Visual Design

- Minimal — checkmark only (✓), no badges or color coding
- Matches existing index page theme system (uses CSS variables)
- Login button styled consistently with existing navbar elements
- Mobile: login button included in hamburger menu overlay
- Expandable chapter lists use subtle animation (slide down)
