---
title: "Docs: characters / appearance"
url: https://create.roblox.com/docs/characters/appearance.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: characters / appearance

[Open](https://create.roblox.com/docs/characters/appearance.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on character appearance. Covers File > Avatar Settings for global avatar presets, and programmatic customization via HumanoidDescription (creating from character, outfit ID, or user ID; modifying properties; applying to single, all, or spawning characters). Also covers layered accessories caging requirements for non-R15 and custom rigs.

## Tips
- [page](https://create.roblox.com/docs/characters/appearance) **[[development-process-and-speed]]** Use File > Avatar Settings for global player character presets; they apply to all player characters joining the game.
- [page](https://create.roblox.com/docs/characters/appearance) **[[scripting-and-performance]]** Always fetch a fresh description with Humanoid:GetAppliedDescription() before modifying and reapplying; stale descriptions cause unexpected results.
- [page](https://create.roblox.com/docs/characters/appearance) **[[scripting-and-performance]]** Do not change assets on a character while also changing HumanoidDescription; this may lead to undefined behavior.
- [page](https://create.roblox.com/docs/characters/appearance) **[[scripting-and-performance]]** Set Players.CharacterAutoLoads = false before PlayerAdded to apply a custom HumanoidDescription on spawn via LoadCharacterWithHumanoidDescription.
- [page](https://create.roblox.com/docs/characters/appearance) **[[building-art-and-assets]]** Body scale properties (height, width, head, body type, proportion) have no effect on R6 body types.
- [page](https://create.roblox.com/docs/characters/appearance) **[[building-art-and-assets]]** Use SetAccessories with Order values for layered accessories rather than setting individual accessory strings.
- [page](https://create.roblox.com/docs/characters/appearance) **[[building-art-and-assets]]** Custom layered accessory cage implementations cannot be published to the Marketplace; use custom cage meshes only for in-game assets.
- [page](https://create.roblox.com/docs/characters/appearance) **[[building-art-and-assets]]** For non-R15 or Humanoid-less targets, add a Weld with Part0 as the accessory and Part1 as the parent part for layered accessories.
- [page](https://create.roblox.com/docs/characters/appearance) **[[building-art-and-assets]]** Layered accessory cages need matching UV maps: target outer cage and layer inner/outer cages must share corresponding vertex UVs.

## Tools
Roblox Studio, HumanoidDescription, Avatar Settings

## He points to
- Avatar Settings
- Layered accessories caging overview
- Layered accessories caging best practices
- Layered accessories cage mesh specifications
- Avatar body cage specifications

## Topics
[[building-art-and-assets]] [[development-process-and-speed]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
