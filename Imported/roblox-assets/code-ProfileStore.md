---
tags: [roblox-assets, code, library]
---
# ProfileStore (library)

Session-locked DataStore saving (successor to ProfileService)

- Path: `~\roblox-assets\code\ProfileStore\`
- Source: https://github.com/MadStudioRoblox/ProfileStore @ `45c9847cbc`
- License: Apache-2.0
- Size: 0.2 MB
- Searchable as: datastore wrapper, player data, saving

## How it helps
Player data: load/save a profile table per player with session locking; the standard choice for inventories, currencies and progress.

## How to use
- Wally-compatible libraries: add to `wally.toml` or copy the module folder (usually `src/` or `lib/`) into the project via Rojo.
- Check the license terms (Apache-2.0) before shipping; keep the license file with copied code.
- Tools (Rojo, Wally, StyLua, Selene, Lune, luau-lsp, Rokit) are source checkouts; prefer installing releases with Rokit over building them.
