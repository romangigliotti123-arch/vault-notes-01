---
title: "Docs: resources / modules / social-interactions"
url: https://create.roblox.com/docs/resources/modules/social-interactions.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: resources / modules / social-interactions

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/resources/modules/social-interactions.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox developer docs for the SocialInteractions package module. Covers body orientation (neck/waist head-facing toward camera) and chat animations triggered by configurable word patterns. Explains installation, configure() options, setTriggerWordsForChatAnimation(), and the onChatAnimationPlayed event.

## Tips
- [page](https://create.roblox.com/docs/resources/modules/social-interactions) **[[client-server-and-remotes]]** Custom rigs must include Motor6D joints named Neck and Waist, or the body orientation feature will not work correctly.
- [page](https://create.roblox.com/docs/resources/modules/social-interactions) **[[ui-ux-design]]** Chat animations are enabled by default once the module is inserted; set useChatAnimations = false in configure() if you don't want them.
- [page](https://create.roblox.com/docs/resources/modules/social-interactions) **[[building-art-and-assets]]** Install SocialInteractions from the Creator Store Packages category and move it into ReplicatedStorage; it starts running automatically.
- [page](https://create.roblox.com/docs/resources/modules/social-interactions) **[[scripting-and-performance]]** Call configure() only from a LocalScript in StarterPlayerScripts; it cannot be called from a server script.

## Numbers
- [page](https://create.roblox.com/docs/resources/modules/social-interactions) waistOrientationWeight default: **0.5 (1 = all waist, 0 = all neck)**
- [page](https://create.roblox.com/docs/resources/modules/social-interactions) useBodyOrientation default: **true**
- [page](https://create.roblox.com/docs/resources/modules/social-interactions) useChatAnimations default: **true**
- [page](https://create.roblox.com/docs/resources/modules/social-interactions) Chat animation count (built-in): **7 (Wave, Applaud, Agree, Disagree, Shrug, Laugh, Sleep)**

## Tools
Roblox Studio, Creator Store (Packages), SocialInteractions module, Luau string patterns

## Topics
[[building-art-and-assets]] [[client-server-and-remotes]] [[events-and-seasonal-content]] [[luau-language-and-types]] [[scripting-and-performance]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
