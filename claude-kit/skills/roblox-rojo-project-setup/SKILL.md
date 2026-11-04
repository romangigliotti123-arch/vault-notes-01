---
name: roblox-rojo-project-setup
description: "Set up a file-based Roblox project (Rojo, Wally, Selene, StyLua, git) so Luau can be edited and reviewed as plain files. Use when starting a Roblox project that Claude should edit outside Studio."
---

# Roblox Rojo project setup

Code comments: none by default (see roblox-luau-style, Comments).

Faster path: `python ~/.claude/claude-kit/tools/games.py init <slug> --rojo` scaffolds this whole layout; Studio connection and the toolchain installer are in the `roblox-studio-connect` skill.

Goal: Luau lives in git as plain files, Studio syncs via the Rojo plugin, and Claude can read/edit/lint the code without Studio open.

## Steps
1. Install a toolchain manager (Rokit or Aftman) from its official releases page. Download and inspect the install step yourself; do not pipe an install script from the internet into a shell without the user's approval. On Windows prefer `winget`/release binaries.
2. Pin tools in `rokit.toml` (or `aftman.toml`): `rojo`, `wally`, `selene`, `stylua`. Prefer the pinned `rokit.toml` from the kit template (`~/.claude/claude-kit/tools/roblox-project-template/`).
3. `rojo init` then edit `default.project.json`: map `src/server` to `ServerScriptService`, `src/shared` to `ReplicatedStorage.Shared`, `src/client` to `StarterPlayer.StarterPlayerScripts`, packages to `ReplicatedStorage.Packages`.
4. Script file naming: `*.server.luau` (Script), `*.client.luau` (LocalScript), `*.luau` (ModuleScript), `init.luau` for folder modules.
5. Config files: `selene.toml` (std = roblox), `stylua.toml`, `wally.toml` for packages, `.gitignore` (Packages, `*.rbxl` autosaves, `sourcemap.json`).
6. Generate `sourcemap.json` (`rojo sourcemap default.project.json -o sourcemap.json`) so Luau LSP resolves requires.
7. Verify: `rojo build -o build.rbxl` succeeds, `selene src` and `stylua --check src` pass, open the place in Studio, run `rojo serve`, connect with the plugin, and confirm a test print appears in Output.
8. Commit with a README listing the commands (build, serve, lint, format).

Rules: assets (meshes, images, sounds) stay uploaded in Roblox and referenced by id in a constants module; do not commit binary place files except releases the user asks for.
