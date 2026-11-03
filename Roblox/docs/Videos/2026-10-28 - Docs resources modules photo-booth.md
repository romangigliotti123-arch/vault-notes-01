---
title: "Docs: resources / modules / photo-booth"
url: https://create.roblox.com/docs/resources/modules/photo-booth.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: resources / modules / photo-booth

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/resources/modules/photo-booth.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Official Roblox docs for the PhotoBooth developer module: installing it from the Creator Store, positioning the booth, configuring messages/camera/timing via configure(), connecting to printout/countdown/prompt events, controlling GUI visibility during photos, and setting custom backgrounds.

## Tips
- [page](https://create.roblox.com/docs/resources/modules/photo-booth) **[[development-process-and-speed]]** Install the free PhotoBooth package from Creator Store Packages, move it into ReplicatedStorage, and it runs automatically; customise later via configure().
- [page](https://create.roblox.com/docs/resources/modules/photo-booth) **[[building-and-level-design]]** Place the PhotoBooth model anywhere in Workspace; any part tagged 'PhotoBooth' (CollectionService) also works, so custom booth models are supported.
- [page](https://create.roblox.com/docs/resources/modules/photo-booth) **[[client-server-and-remotes]]** Call PhotoBooth.configure() only from a LocalScript; events can also only be connected in a LocalScript.
- [page](https://create.roblox.com/docs/resources/modules/photo-booth) **[[ui-ux-design]]** Mark your own ScreenGuis with attribute ShowInPhotoBooth=true and use hideOtherGuis/showOtherGuis callbacks to keep HUD elements visible or hide them during photos.

## Numbers
- [page](https://create.roblox.com/docs/resources/modules/photo-booth) Default maxActivationDistance: **10 studs** (Distance a character must be from booth for prompt to appear)
- [page](https://create.roblox.com/docs/resources/modules/photo-booth) Default fadeUiDelay: **3 seconds** (Frame message shown before fading; negative value never fades)
- [page](https://create.roblox.com/docs/resources/modules/photo-booth) Default countdownSeconds: **3** (Countdown length before photo is taken)
- [page](https://create.roblox.com/docs/resources/modules/photo-booth) Background image size: **1024×576 (16:9)** (Optimal aspect ratio for setBackgrounds images)

## Tools
PhotoBooth module (Creator Store package), Roblox Studio Toolbox, CollectionService

## Topics
[[building-and-level-design]] [[building-art-and-assets]] [[client-server-and-remotes]] [[development-process-and-speed]] [[player-psychology-and-game-feel]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
