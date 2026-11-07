# Imported vaults INDEX

Public knowledge bases imported into `~/claude-host/imported-vaults/<slug>/` (markdown + small images, each with SOURCE.md: URL, commit, license, date). Mirrored read-only into Obsidian under `Imported/<slug>/` by sync-vault.ps1 (mirror-imports.py); note names that collide with existing vault notes get a ` (<slug>)` suffix there.

## Accepted (license allows reuse)

| Slug | Notes | License | Source | What |
|---|---|---|---|---|
| awesome-gamedev-agent-skills | 195 | Apache-2.0 | https://github.com/gamedev-skills/awesome-gamedev-agent-skills @ 19d93f97c9 | 77 game-dev skills for AI coding agents (Godot, Unity, Unreal, Phaser, ...), Apache-2.0. |
| awesome-gamedev-calinou | 4 | CC-BY-SA-4.0 | https://github.com/Calinou/awesome-gamedev @ 9918eea4f1 | Free-software and free-culture resources for making games (CC-BY-SA). |
| awesome-gamedev-fronkon | 1 | MIT | https://github.com/FronkonGames/Awesome-Gamedev @ fc0f586ffe | Large curated list of game dev resources (MIT). |
| awesome-learn-gamedev | 3 | CC0-1.0 | https://github.com/dawdle-deer/awesome-learn-gamedev @ 28e61535a7 | Curated game development learning resources (CC0). |
| awesome-roblox | 3 | CC0-1.0 | https://github.com/awesome-roblox/awesome-roblox @ ac2d275801 | Curated list of Roblox open-source libraries, tools and games (CC0). |
| game-mechanics | 256 | MIT | https://github.com/saschb2b/game-mechanics @ cca7ec63d8 | Personal knowledge base of game mechanics, reward loops, world-building and design patterns (game design / live-ops thinking). |
| luau-site | 63 | MIT | https://github.com/luau-lang/site @ c0eb09dc75 | Official Luau language site: syntax, type system, performance, library reference, RFCs. |
| ro-engineer | 11 | MIT | https://github.com/excaldev/ro-engineer @ d86f0c04d9 | REFERENCE ONLY. Roblox/Luau engineering reference notes (architecture choice, pooling, cleanup/lifecycle, state, sharp-edges checklist, testing evidence, retention ethics). Young single-maintainer repo; unverified, modified (see its SOURCE.md); the vault's own skills are rewritten from these ideas and win on conflicts. |
| roblox-creator-docs | 1039 | CC-BY-4.0 | https://github.com/Roblox/creator-docs @ 02c23e6297 | Official Roblox Creator Hub documentation (en-us): Studio, Luau, engine API guides, monetisation, UGC, performance, publishing. Core Roblox reference. |

## Reference only (no reusable license, template-style or off-topic; NOT copied)

- BananaPix4613/Obsidian-Game-Dev-Vault: game development notes vault, no license.
- codevogel/ReggieNotes: game design notes vault, no license.
- ShieldedAsh/obsidian-notes: RIT game design student notes, no license.
- Taneelkins/claude-brain-starter: Obsidian vault + MCP setup that turns Claude Code into a Roblox dev partner; license NOASSERTION. Read on GitHub before building similar tooling.
- shinjiesk/roblox-dev-notes, Cubitaa/Luau-Roblox-Scripting-Guide, wxmvibes/StudioGuides: Roblox notes/guides, no license.
- EddieWing/gamedev-postmortem-atlas: gamedev postmortem collection, no license.
- anthropics/prompt-eng-interactive-tutorial and anthropics/courses: Anthropic tutorials (no/NOASSERTION license); read online.
- Huerte/Vault-of-Forbidden-Knowledge (MIT): general IT/gaming how-tos, judged off-topic, not imported.
- jaredrhod/ai-memory-vault (CC-BY-SA) and undefined-ui/second-brain-os (MIT): template/guide style, skipped.
- izzyfrm/roblox-ai: about 1 GB Roblox media library (game screenshots, UI/VFX/animation refs, 2,210 MP3 sound effects), no license (SFX folder claims CC0 without per-clip origins): index only, except 5 small image folders (ui-styles, style-refs, vfx, animations, cutscenes; 500 images) mirrored as reference-only images in vault-refs-01 (REFSIMPORT1). See Imported/roblox-ai-index/roblox-ai-INDEX.md.
- Pointer lists used to find more vaults: github.com/kmaasrud/awesome-obsidian, github.com/obsidian-pkm-vault/awesome-obsidian-vault, github.com/lyz-code/best-of-digital-gardens.

Search order for agents: this INDEX, then Grep inside the slug folder, then `query-vault.ps1 "<need>"` (the graph includes Imported notes).
