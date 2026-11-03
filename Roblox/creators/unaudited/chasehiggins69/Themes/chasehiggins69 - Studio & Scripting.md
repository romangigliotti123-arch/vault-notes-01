---
title: chasehiggins69 - Studio & Scripting
creator: chasehiggins69
tags: [roblox, chasehiggins69, theme]
creator_trust: INSUFFICIENT
---

> [!note] Trust: UNAUDITED (fewer than 4 checkable claims verified): credibility unknown, treat as unverified, not as bad; confirm before relying. See [[creator-credibility]].

# chasehiggins69: Studio & Scripting

All chasehiggins69 tips on this theme, grouped by topic, oldest first. Cross-creator synthesis: see [[README]] in roblox-kb.

## [[building-art-and-assets]]
- 2026-07-08 [5:39](https://youtu.be/p86bt9ROQfk?t=339) Mount declarative UI to Players.LocalPlayer.PlayerGui from a client script so the root ScreenGui is created on the client. ([[2026-07-08 - How PRO devs make UI in Roblox (Vide UI)|How PRO devs make UI in Roblox (Vide UI)]])
- 2026-07-08 [6:23](https://youtu.be/p86bt9ROQfk?t=383) Use the Codify plugin to export a Studio-built UI frame into Vide code in one click, then iterate in code. ([[2026-07-08 - How PRO devs make UI in Roblox (Vide UI)|How PRO devs make UI in Roblox (Vide UI)]])

## [[code-architecture-and-frameworks]]
- 2026-07-08 [1:04](https://youtu.be/p86bt9ROQfk?t=64) Use Vide's parentheses-less call style (table/string literal args) only if your team accepts it; StyLua in VS Code will force parentheses anyway. ([[2026-07-08 - How PRO devs make UI in Roblox (Vide UI)|How PRO devs make UI in Roblox (Vide UI)]])
- 2026-07-08 [10:07](https://youtu.be/p86bt9ROQfk?t=607) Define a typed Props table for each component (position, color, increment) and pass values in from the parent app to make components reusable. ([[2026-07-08 - How PRO devs make UI in Roblox (Vide UI)|How PRO devs make UI in Roblox (Vide UI)]])

## [[ui-ux-design]]
- 2026-07-08 [8:17](https://youtu.be/p86bt9ROQfk?t=497) Bind text properties to sources (state) so only the affected property updates instead of rebuilding the whole element on change. ([[2026-07-08 - How PRO devs make UI in Roblox (Vide UI)|How PRO devs make UI in Roblox (Vide UI)]])
- 2026-07-08 [9:11](https://youtu.be/p86bt9ROQfk?t=551) Use bind.effect to run side effects (prints, animations like Ripple) automatically whenever a source changes, instead of wiring them into click handlers. ([[2026-07-08 - How PRO devs make UI in Roblox (Vide UI)|How PRO devs make UI in Roblox (Vide UI)]])

## [[version-control-and-tooling]]
- 2026-07-08 [3:26](https://youtu.be/p86bt9ROQfk?t=206) Install Vide via Wally (search on wally.run), then ensure packages are listed in default.project.json before running rojo serve. ([[2026-07-08 - How PRO devs make UI in Roblox (Vide UI)|How PRO devs make UI in Roblox (Vide UI)]])
- 2026-07-24 [0:00](https://youtu.be/e9ElODFv8lo?t=0) Use the Luau LSP plugin with Rojo in Neovim to get autocomplete and types for Studio instances, including ones not saved to disk. ([[2026-07-24 - vim for roblox|vim for roblox]])
- 2026-07-24 [2:03](https://youtu.be/e9ElODFv8lo?t=123) After adding a Wally package in wally.toml and running wally install, restart Rojo serve and reconnect so the source map picks up the package. ([[2026-07-24 - vim for roblox|vim for roblox]])
- 2026-07-24 [33:51](https://youtu.be/e9ElODFv8lo?t=2031) Regenerate the Luau LSP source map (space LR in his config) when packages or new instances stop being referenced, instead of restarting everything. ([[2026-07-24 - vim for roblox|vim for roblox]])
- 2026-07-24 [36:10](https://youtu.be/e9ElODFv8lo?t=2170) Run Neovim in one tmux pane and Rojo serve in another so you can switch between them without losing context. ([[2026-07-24 - vim for roblox|vim for roblox]])
- 2026-07-24 [38:30](https://youtu.be/e9ElODFv8lo?t=2310) Install Rojo and Wally via Rokit, then run rojo init and wally init in a new project folder. ([[2026-07-24 - vim for roblox|vim for roblox]])

Up: [[chasehiggins69 - How to make successful Roblox games]]
