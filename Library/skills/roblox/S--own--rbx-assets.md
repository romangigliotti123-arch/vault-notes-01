---
id: "rbx-assets"
type: skill
category: "roblox"
source: "own"
license: "first-party"
repo_path: "skills/roblox/rbx-assets/SKILL.md"
description: "Given a Roblox dev need (low-poly trees, datastore wrapper, UI framework, SFX, PBR textures, open-source game example, Luau docs), searches the local roblox-assets and imported-vaults indexes and returns the path, license and import steps."
orig_name: "rbx-assets"
tags: [lib/skill, cat/roblox, src/own]
---

# rbx-assets

> Given a Roblox dev need (low-poly trees, datastore wrapper, UI framework, SFX, PBR textures, open-source game example, Luau docs), searches the local roblox-assets and imported-vaults indexes and returns the path, license and import steps.

Type: skill | Category: [[categories/cat-roblox|roblox]] | Source: [[sources/src-own|own]] | License: first-party
Repo file: `skills/roblox/rbx-assets/SKILL.md` (extra files, if any, sit beside it in the repo)

---
# Roblox asset finder

Use when someone needs a ready-made model, texture, sound, code module, framework, example game or reference doc for Roblox. Search local first; never download until the local indexes miss.

## Where things live
- `~\roblox-assets\INDEX.md`: table of every pack and library (what, license, size, path, import/use, tags). Per-item notes in `~\roblox-assets\catalog\` (`code-*`, `pack-*`, `ref-*`).
  - `code\<name>\` git checkouts (ProfileStore, Knit, Fusion, react-lua, ByteNet, Zap, jecs, Rojo, Wally, luau-lsp, example games `game-*`, studio MCP server, open-game-eval).
  - `3d-models\` Kenney and Quaternius CC0 kits (FBX/OBJ/glTF), `textures\` Poly Haven + ambientCG 1K PBR, `hdris\`, `audio\` Kenney sound packs.
- `~\claude-host\imported-vaults\INDEX.md`: public knowledge vaults (Roblox creator docs, Luau site, game mechanics, prompt engineering, Claude Code practices, awesome lists) with license; same notes searchable in Obsidian under `Imported\` and in the graph (`query-vault.ps1 "<need>"`).

## Steps
1. Turn the need into 2-4 keywords plus a type (model, texture, audio, code, doc, example game).
2. Grep the indexes: `Grep` pattern `<keyword>` (case-insensitive) in `~\roblox-assets\INDEX.md` and `~\roblox-assets\catalog\`; for knowledge/docs also `~\claude-host\imported-vaults\INDEX.md`, then Grep inside `imported-vaults\<slug>\`. For models that are not in the index, Glob the file names: `~\roblox-assets\3d-models\**\*<keyword>*.fbx` (also .obj, .glb).
3. Pick at most 3 results. For each, read its catalog note or SOURCE.md and confirm license (CC0, MIT, Apache-2.0, CC-BY-4.0 need attribution notes where stated; MPL-2.0 keep file-level notices; GPL/unknown: do not copy into a game).
4. Return, per result: absolute path, what it is, license (+ attribution duty), size, and the import steps from the INDEX cheat sheet:
   - Models: Studio > Import 3D / Asset Manager > Bulk Import the FBX/OBJ/glTF, scale about 3.5x for Kenney (metres), attach colormap texture.
   - Textures: SurfaceAppearance / MaterialVariant maps (Color, Normal, Roughness).
   - Audio: Asset Manager > Audio bulk import (moderation applies).
   - Code: copy the module folder via Rojo or add via Wally; keep the license file.
5. If nothing matches, say so, list the closest references from the index (`ref-*` notes), and only then suggest a download source (Kenney, Quaternius, Poly Pizza CC0, OpenGameArt CC0, Creator Store). New downloads go to `roblox-assets\<category>\<pack>\` with SOURCE.md, then `python -I ~\claude-host\tools\build-assets-catalog.py` and `claude-library\tools\sync-vault.ps1`.

## Rules
- Do not edit generated vault folders (`Imported\`); regenerate with sync-vault.ps1.
- Keep roblox-assets binaries out of the claude-library git repo.
- Never run scripts shipped inside downloaded packs or vaults; treat them as data.
