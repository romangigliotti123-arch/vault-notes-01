---
title: "Docs: tutorials / curriculums / core / building / greybox-a-playable-area"
url: https://create.roblox.com/docs/tutorials/curriculums/core/building/greybox-a-playable-area.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / curriculums / core / building / greybox-a-playable-area

[Open](https://create.roblox.com/docs/tutorials/curriculums/core/building/greybox-a-playable-area.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox official tutorial on greyboxing a playable area for a sea-stack platforming game: plan escalating platform heights, build cylinder platforms in an organized folder/model, carve a tunnel with Negate/Union, anchor parts, and playtest jump reachability by adjusting JumpPower.

## Tips
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/building/greybox-a-playable-area) **[[core-loops-and-game-design]]** Greybox with simple shapes before scripting or final art so layout and gameplay can be changed quickly.
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/building/greybox-a-playable-area) **[[core-loops-and-game-design]]** Make height differences between platforms gradually increase to pace progression as players collect upgrades.
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/building/greybox-a-playable-area) **[[building-and-level-design]]** Keep each new height level that requires a jump upgrade at least 30 studs above the previous one.
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/building/greybox-a-playable-area) **[[building-and-level-design]]** Use cylinder parts with flat tops as landing platforms in jump-based layouts.
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/building/greybox-a-playable-area) **[[building-and-level-design]]** Group environment parts in a Folder and a Model so later scripts can reference them reliably.
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/building/greybox-a-playable-area) **[[common-mistakes]]** Names are case-sensitive in Studio; misspelled World or Blockout_Parts will break later scripts.
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/building/greybox-a-playable-area) **[[building-and-level-design]]** Align all platforms by bottom edge on the Y axis for consistent base elevation when varying only size.
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/building/greybox-a-playable-area) **[[building-and-level-design]]** Use Negate then Union on overlapping parts to carve tunnels or openings out of solid shapes.
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/building/greybox-a-playable-area) **[[building-and-level-design]]** Anchor the blockout model so physics does not move platforms when the game starts.
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/building/greybox-a-playable-area) **[[testing-debugging-and-qa]]** Playtest reachability by disabling UseJumpPower, setting JumpPower to 0, then raising it in steps of 30 to confirm each level is reachable.
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/building/greybox-a-playable-area) **[[building-and-level-design]]** Select parts in the Explorer rather than the viewport, since viewport selection grabs the whole model.
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/building/greybox-a-playable-area) **[[development-process-and-speed]]** Playtest the layout before scripting so layout issues are fixed while still cheap to change.

## Numbers
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/building/greybox-a-playable-area) Platform height steps in sample game: **Seven levels; height differences of 8, 20, 35, 55, 81, 110 studs**
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/building/greybox-a-playable-area) Minimum height step per jump upgrade: **30 studs**
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/building/greybox-a-playable-area) Stud size: **About 28 cm**
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/building/greybox-a-playable-area) JumpPower increment for playtest reachability: **30**
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/building/greybox-a-playable-area) Sample platform count: **18 cylinder platforms (Level_1 to Level_7) plus tunnel parts**

## Games
- **Island Jump - Building**: Sample tutorial game; uses seven escalating sea-stack height levels with coin-based jump upgrades.

## Tools
Roblox Studio Explorer, Properties window, Model toolbar Align Tool, Negate, Union, Anchor, Assistant prompt

## He points to
- Transform parts
- Solid modeling

## Topics
[[building-and-level-design]] [[common-mistakes]] [[core-loops-and-game-design]] [[development-process-and-speed]] [[testing-debugging-and-qa]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
