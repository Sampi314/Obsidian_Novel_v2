# Cố Nguyên Giới — Agent Instructions

## Locked Chapters

Before editing any chapter file in `Đạo/Chương_Truyện/`, check `locked_chapters.json` in the repo root.
If the chapter's file path is listed in `locked_chapters`, DO NOT modify it.
These chapters are approved for publication and must not be changed.
Do NOT modify `locked_chapters.json` itself — it is managed exclusively by the author through the web UI.

## Code Style

- `scripts/tts_player.js` — IIFE pattern, ES5 syntax (`var`, no arrow functions), CSS injected via JS string arrays
- Skill files (`.claude/skills/*/SKILL.md`) — YAML frontmatter (`name`, `description`), Vietnamese with diacritics for content, include `**Tham khảo:**` reference to a sample file in the corresponding `Đạo/` directory
- Skill output templates must match the Roman numeral section format (I, II, III...) used in actual `Đạo/` files

## VieNeu-TTS Integration

- Local server: `uv run vieneu-web` → port 8001
- Standard voices: `GET /stream?text=...&voice_id=...` → `audio/wav`
- Voice cloning: `POST /stream` with FormData (`text`, `ref_audio` file, `ref_text`) → `audio/wav`
- Cloned voice profiles stored in `localStorage` as base64 under key `tts_cloned_voices`
