<!-- cold: rbx-use/map.md | read when: read only to locate a vault folder (kb, creators, Library, learned, Manager, Imported, Assets) that grep, kbq or vault-find did not reach. -->

## From skills/rbx-use/SKILL.md :: Where things are

- `Roblox/roblox-kb/`: ~30 topic files plus `case-studies-*.md`; `README.md` (task to topic table), `master-playbook.md`; `_tools/` quick sheets (DECISION-RULES, BENCHMARKS, PRICE-LADDER, AD-PLAYBOOK, CHECKLIST-launch, CHECKLIST-monetization, HOW-TO-USE, INDEX): cheapest place to start.
- `Roblox/creators/<tier>/<creator>/` (tier = trusted, mixed or unaudited; the Blender research is `Roblox/blender/`): per-creator playbooks (`<creator> - How to make successful Roblox games.md`, `Numbers & Benchmarks`, `Games Mentioned`, `Tools & Resources`); `Roblox/docs/` official Creator Docs notes (including genre playbooks); `Roblox/devforum/`; `Roblox/_Roblox-Home.md` hub.
- `Library/`: `_Home.md` hub, `PICKS.md` (best 1-3 items per job), `README.md`; `Library/skills/<category>/S--<source>--<name>.md` and `Library/agents/<category>/A--<source>--<name>.md` hold the full text of each skill or agent (own items use `own` as the source); `categories/cat-*.md` and `sources/src-*.md` are maps. Find an item by name: `ls Library/skills/*/ Library/agents/*/ | rg -i "<name>"` or `rg -i "<words>" Library/PICKS.md`.
- `learned/<topic>/`: curated findings contributed by agents (index `learned/README.md`; type `learned` in vault-find). Look here first for gotchas and fixes.
- `Manager/`: research on how to run and brief agents (`Manager-README.md`, `PROPOSALS.md`, `kb-conventions.md`, `src-*.md` source notes). Read `Manager-README.md` first.
- `Imported/`: public knowledge vaults (Roblox Creator docs, Luau site, game mechanics); start at `Imported/Imported-Vaults-INDEX.md`.
- `claude-kit/`: installer, agents, skills and tools for using all this (see its INSTALL.md).
- Assets are in `<vault>/Assets` (downloaded from the public vault-assets GitHub repos by /rbx-update, never in git; licences in THIRD-PARTY-NOTICES.md; fallbacks: env `ROBLOX_ASSETS`, `~/roblox-assets`) (`INDEX.md`, `catalog/`, `code/`, `3d-models/`, `audio/`, `textures/`, `hdris/`).
