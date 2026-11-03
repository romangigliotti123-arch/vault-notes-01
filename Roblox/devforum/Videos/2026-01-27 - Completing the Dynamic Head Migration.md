---
title: "Completing the Dynamic Head Migration"
url: https://devforum.roblox.com/t/completing-the-dynamic-head-migration/4301387
creator: Roblox DevForum
official: false
advice_density: low
date: 2026-01-27
views: 74988
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Completing the Dynamic Head Migration

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://devforum.roblox.com/t/completing-the-dynamic-head-migration/4301387) | Roblox DevForum | 74,988 views | 2026-01-27

## Summary
Roblox DevForum announcement from GeneralRelish on completing the migration of all Classic Heads and Faces into Dynamic Heads (unified avatar schema). Covers the March 23, 2026 rollout, Limited handling (same serials and copy counts), head-shape swapping via AvatarEditorService, API changes for experiences, and the facial animation toggle.

## Tips
- [page](https://devforum.roblox.com/t/completing-the-dynamic-head-migration/4301387) **[[ugc-and-avatar-economy]]** If your experience uses AvatarEditorService for Classic Heads/Faces, stop filtering for legacy AssetTypes; SearchCatalog and GetInventory return empty for "Face" and "Head" now.
- [page](https://devforum.roblox.com/t/completing-the-dynamic-head-migration/4301387) **[[scripting-and-performance]]** Call AvatarEditorService:ConformToAvatarRulesAsync() before presenting an avatar so legacy Classic assets are swapped for their Dynamic Head equivalents with the correct HeadShape.
- [page](https://devforum.roblox.com/t/completing-the-dynamic-head-migration/4301387) **[[ui-ux-design]]** Consolidate separate Classic Heads and Classic Faces UI categories into a single unified Heads category.
- [page](https://devforum.roblox.com/t/completing-the-dynamic-head-migration/4301387) **[[ugc-and-avatar-economy]]** Use GetHeadShapesAsync() to get a user's owned Classic head shapes, then apply them via BodyPartDescription.HeadShape on a Dynamic Head asset.

## Numbers
- [page](https://devforum.roblox.com/t/completing-the-dynamic-head-migration/4301387) Classic Head/Face combinations converted: **tens of thousands**
- [page](https://devforum.roblox.com/t/completing-the-dynamic-head-migration/4301387) Face decals with side-by-side comparisons: **around 500 of ~700**
- [page](https://devforum.roblox.com/t/completing-the-dynamic-head-migration/4301387) Initial V2 heads released for review: **50 top heads**
- [page](https://devforum.roblox.com/t/completing-the-dynamic-head-migration/4301387) Limited copies after migration: **same count as Classic Face (1:1 replacement, serials kept)**

## Tools
AvatarEditorService, HumanoidDescription, BodyPartDescription, Players:CreateHumanoidModelFromDescriptionAsync

## Topics
[[scripting-and-performance]] [[ugc-and-avatar-economy]] [[ui-ux-design]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
