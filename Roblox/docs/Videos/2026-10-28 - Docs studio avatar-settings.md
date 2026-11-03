---
title: "Docs: studio / avatar-settings"
url: https://create.roblox.com/docs/studio/avatar-settings.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: studio / avatar-settings

[Open](https://create.roblox.com/docs/studio/avatar-settings.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox Studio docs for the Avatar Settings window (File menu or Avatar tab). Covers preset selection, preview lineup, and per-tab controls for body scale/build, clothing and accessory limits, animation packs/clips, collision type, and the Character Controller Library. Warns that settings change hidden defaults and must be tested in preview and playtesting before publishing.

## Tips
- [page](https://create.roblox.com/docs/studio/avatar-settings) **[[common-mistakes]]** Avatar Settings changes hidden game defaults not visible in scripts; test with preview and playtesting before publishing to a live game.
- [page](https://create.roblox.com/docs/studio/avatar-settings) **[[development-process-and-speed]]** Use a single source of truth for Avatar Settings across teams and place files, since multi-place universes can cause hard-to-debug avatar behaviour.
- [page](https://create.roblox.com/docs/studio/avatar-settings) **[[genre-mechanics]]** Use the Consistent Gameplay preset (same height and box collider) when collision consistency matters, rather than Player Choice.
- [page](https://create.roblox.com/docs/studio/avatar-settings) **[[building-art-and-assets]]** Set Clothing Scale and Accessory Scale limit bounds to restrict oversized user items; 0% means strictly inside the body bounding box.
- [page](https://create.roblox.com/docs/studio/avatar-settings) **[[combat-and-gameplay-systems]]** Choose Single Collider for consistent hit detection, and set Hit & Touch Detection to colliders rather than parts if you need uniform hitboxes.
- [page](https://create.roblox.com/docs/studio/avatar-settings) **[[optimization-and-streaming]]** Leave Abilities on Legacy Humanoid unless you need Character Controller Library; the library can be toggled on or off at runtime.
- [page](https://create.roblox.com/docs/studio/avatar-settings) **[[client-server-and-remotes]]** Custom Clothing or Accessories with a blank Asset ID removes all player items in that slot; use this deliberately, not by accident.

## Numbers
- [page](https://create.roblox.com/docs/studio/avatar-settings) Classic avatar height: **around 5 studs**
- [page](https://create.roblox.com/docs/studio/avatar-settings) Humanoid avatar height: **around 6 to 6.5 studs**
- [page](https://create.roblox.com/docs/studio/avatar-settings) Limit bounds at 100%: **items can occupy up to three times body size**
- [page](https://create.roblox.com/docs/studio/avatar-settings) Limit bounds at 0%: **items must be strictly within body bounding box**

## Tools
Roblox Studio Avatar Settings window, Studio preview lineup (AvatarPreview folder), Character Controller Library

## He points to
- Roblox Studio Avatar Settings documentation

## Topics
[[building-art-and-assets]] [[client-server-and-remotes]] [[combat-and-gameplay-systems]] [[common-mistakes]] [[development-process-and-speed]] [[genre-mechanics]] [[optimization-and-streaming]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
