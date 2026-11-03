---
title: "Docs: tutorials / curriculums / gameplay-scripting / create-teams"
url: https://create.roblox.com/docs/tutorials/curriculums/gameplay-scripting/create-teams.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / curriculums / gameplay-scripting / create-teams

[Open](https://create.roblox.com/docs/tutorials/curriculums/gameplay-scripting/create-teams.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox official tutorial section on creating teams in the sample laser tag FPS. Covers assigning team colors via the Teams service (mint and carnation pink), team indicators (player, team, leaderboard, name tint), and disabling friendly fire in the blast handler.

## Tips
- [page](https://create.roblox.com/docs/tutorials/curriculums/gameplay-scripting/create-teams) **[[team-and-budget]]** Use the built-in Teams service for team sorting; it balances players, groups the leaderboard, tints name colors, and spawns teams at separate locations without extra scripting.
- [page](https://create.roblox.com/docs/tutorials/curriculums/gameplay-scripting/create-teams) **[[building-and-level-design]]** Pick complementary team colors (e.g. mint vs carnation pink) so players can quickly tell teams apart and orient themselves on the map.
- [page](https://create.roblox.com/docs/tutorials/curriculums/gameplay-scripting/create-teams) **[[ui-ux-design]]** Show team identity in multiple places: a custom on-screen player indicator, an in-game team indicator, the default leaderboard grouping, and name tints.
- [page](https://create.roblox.com/docs/tutorials/curriculums/gameplay-scripting/create-teams) **[[combat-and-gameplay-systems]]** Check team membership on the server before applying damage; return early when the tagged player is on the same team to disable friendly fire.
- [page](https://create.roblox.com/docs/tutorials/curriculums/gameplay-scripting/create-teams) **[[common-mistakes]]** Without custom spawn logic, team players spawn at the same random spawn zone and end up next to each other; restrict spawns per team.
- [page](https://create.roblox.com/docs/tutorials/curriculums/gameplay-scripting/create-teams) **[[client-server-and-remotes]]** Keep the damage and tagging logic on the server (LaserBlastHandler) and have clients only display state synced from the server.

## Games
- **Laser tag sample game (Roblox official tutorial)**: Team-based FPS sample: uses Teams service, friendly fire disabled, team-restricted spawns.

## Tools
Teams service, Team / Team.Color, ReplicatedStorage HUDGuiSetup, ServerScriptService LaserBlastHandler

## He points to
- UI Curriculum: Select a Color Theme
- UI Curriculum: Player Indicator
- UI Curriculum: Team Indicator

## Topics
[[building-and-level-design]] [[client-server-and-remotes]] [[combat-and-gameplay-systems]] [[common-mistakes]] [[team-and-budget]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
