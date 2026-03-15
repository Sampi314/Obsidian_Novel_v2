# 🌌 "Cố Nguyên" (Ancient Origin) Xianxia World-Building System

> [!IMPORTANT]
> **STATUS: PRIVATE REFERENCE ARCHIVE**
> This is a personal world-building project. This repository serves as a live database for creating and developing Xianxia content with AI assistance. **We do not accept external contributions (Pull Requests/Issues).**

---

## 📜 Introduction (Lore Summary)

"Cố Nguyên" is an ancient cultivation world where spiritual Qi originates from primordial chaos. This project systematizes the laws, entities, and history of this world—from profound cultivation realms to the intricate schemes of great sects.

The goal is to build a rigorous data ecosystem where AI agents and authors collaborate to produce novel chapters with high world-logic consistency.

---

## 📖 Interactive Reader

The system uses `reader.html` as the sole display engine. Based on the `type` field in the YAML frontmatter of each Markdown file, the reader automatically adjusts its interface:

- **`type: character`**: Displays Character Profiles with aptitude radar charts, realm timelines, and emotional status bars.
- **`type: faction`**: Displays Faction Sheets with division diagrams, diplomacy bars, and territory maps.
- **Chapter files**: A dedicated novel chapter reader with smart navigation and a TTS (Text-to-Speech) player.

**Themes:** Ink (Ink wash), Blood Moon, Green Bamboo, Snow, Dark.

**[👉 Access the Story Index](https://sampi314.github.io/Obsidian_Novel_v2/index.html)**

---

## 🗂️ World Taxonomy

All world knowledge is organized within the `Đạo/` (The Way) directory:

- **`Nhân_Vật/`**: Detailed profiles of cultivators, demons, and mortals.
- **`Thế_Lực/`**: Systems of sects, clans, and dynasties (over 200 entities).
- **`Công_Pháp/`**: Cultivation manuals, divine abilities, and techniques.
- **`Thế_Giới_Và_Thời_Gian/`**: Geography, history, and the ten-thousand-year timeline.
- **`Tu_Luyện/`**: Realm systems and the laws of the Heavenly Dao.
- ... and other categories such as Alchemy (Pills), Forging (Equipment), Formations, Talismans, Poetry, and Music.

---

## 🤖 Claude Code Skills (AI Integration)

The project integrates 21 specialized AI skills (Claude Code Skills) that help AI agents understand and create content according to the standards of the Cố Nguyên world.

Key skills include:
- `/the-gioi`: Design geography and ecosystems.
- `/nhan-vat`: Initialize characters with standardized YAML metadata.
- `/chuong-truyen`: Compose novel chapters based on established plots.
- `/kiem-duyet`: Review consistency and content quality.
- *(See details in `.claude/skills/`)*

---

## 🛠️ Technical Stack

- **Primary Language**: Vietnamese (for world content).
- **Metadata**: YAML Frontmatter for data structure.
- **Frontend**: HTML/Vanilla JS, CSS (Custom Reader).
- **Automation**: Python & Node.js scripts (`scripts/`) for data synchronization, link checking, and index management.
- **AI Tooling**: Claude Code, Jules Agents.

---

## 📖 Terminology Guide (Hán-Việt to English)

To preserve the nuance of the Xianxia setting, we use traditional Hán-Việt terms. Here is a brief guide for English readers:

| Hán-Việt Term | English Translation | Description |
| :--- | :--- | :--- |
| **Tiên Hiệp** | Xianxia | "Immortal Heroes" – A genre of Chinese fantasy focusing on cultivation. |
| **Linh Khí** | Spiritual Qi | The fundamental energy used by cultivators. |
| **Công Pháp** | Cultivation Method | Manuals or techniques used to harness Qi. |
| **Đan Dược** | Alchemy / Pills | Medicinal pellets created by Alchemists to aid cultivation. |
| **Tông Môn** | Sect | A martial arts or cultivation organization. |
| **Cảnh Giới** | Realm | Levels of power attained through cultivation. |
| **Pháp Bảo** | Dharma Treasure | Magical artifacts or weapons used by cultivators. |
| **Thế Lực** | Faction / Power | Any organized group like a clan, sect, or dynasty. |

---

## ⚠️ Notes for AI Maintenance

When performing data updates, AI agents **MUST** strictly follow:
1. Filenames must use Vietnamese with accents, with spaces replaced by underscores (`_`).
2. Always verify consistency with `HỒ_SƠ_THẾ_GIỚI.md` before adding new entities.
3. Update `public/wiki-index.json` after any file structure changes.

---
© 2026 Cố Nguyên Project. All rights reserved.
