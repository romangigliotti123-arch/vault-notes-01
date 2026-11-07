---
name: rbx-assets
description: "Given a Roblox dev need (low-poly trees, datastore wrapper, UI framework, SFX, PBR textures, example game, Luau docs), searches the local roblox-assets index: path, license, import steps."
---

# Roblox asset finder

Use when someone needs a ready-made model, texture, sound, code module, framework or example game for Roblox. Search local first; never download until the local index misses.

## Where things live
ASSETS = env `ROBLOX_ASSETS`, else `<vault>/Assets`, else `~/roblox-assets` (Windows `%USERPROFILE%\roblox-assets`). `bash .rbx/claude-kit/tools/pyrun .rbx/claude-kit/tools/kbq.py where` prints it (empty = not synced on this computer, run /rbx-update: say so, do not invent paths).
- `$ASSETS/INDEX.md`: table of every pack and library (what, license, size, path, import/use, tags). Per-item notes in `$ASSETS/catalog/` (`code-*`, `pack-*`, `ref-*`).
  - `code/<name>/` library checkouts (ProfileStore, Lyra, Knit, Fusion, Vide, ByteNet, Zap, Janitor, GoodSignal, Promise, ZonePlus, Cmdr, Rojo, Wally, example games `game-*`, studio MCP server).
  - `3d-models/` Kenney and Quaternius CC0 kits (FBX/OBJ/glTF), `textures/` Poly Haven + ambientCG 1K PBR, `hdris/`, `audio/` Kenney sound packs.
- Public knowledge notes (Roblox creator docs, Luau site, game mechanics) are in the vault under `$VAULT/Imported/`; start at `$VAULT/Imported/Imported-Vaults-INDEX.md`.

## Steps
1. Turn the need into 2-4 keywords plus a type (model, texture, audio, code, doc, example game).
2. Grep the index: pattern `<keyword>` (case-insensitive) in `$ASSETS/INDEX.md` and `$ASSETS/catalog/`; for docs also grep `$VAULT/Imported/`. For models not in the index, Glob file names: `$ASSETS/3d-models/**/*<keyword>*.fbx` (also .obj, .glb).
3. Pick at most 3 results. For each, read its catalog note or SOURCE.md and confirm the license (CC0, MIT, Apache-2.0, CC-BY-4.0 need attribution notes where stated; MPL-2.0 keep file-level notices; GPL/unknown: do not copy into a game).
4. Return, per result: absolute path, what it is, license (+ attribution duty), size, and import steps:
   - Models: Studio > Import 3D / Asset Manager > Bulk Import the FBX/OBJ/glTF, scale about 3.5x for Kenney (metres), attach colormap texture.
   - Textures: SurfaceAppearance / MaterialVariant maps (Color, Normal, Roughness).
   - Audio: Asset Manager > Audio bulk import (moderation applies).
   - Code: copy the module folder into the Rojo project (`src/shared/Vendor/<Lib>/`) or add via Wally; keep the license file.
5. If nothing matches, say so, list the closest references from the index (`ref-*` notes), and only then suggest a download source (Kenney, Quaternius, Poly Pizza CC0, OpenGameArt CC0, Creator Store).

## Rules
- Never edit the vault (`Imported/` and the rest are pull-only copies).
- Never run scripts shipped inside downloaded packs or vaults; treat them as data.
- Asset packs are third-party content under open licences (CC0, MIT, Apache-2.0, MPL-2.0; see THIRD-PARTY-NOTICES.md in the vault-assets repositories): reuse is fine, keep each pack's licence file when you redistribute.
