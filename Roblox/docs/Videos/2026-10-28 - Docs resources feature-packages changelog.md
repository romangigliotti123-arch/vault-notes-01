---
title: "Docs: resources / feature-packages / changelog"
url: https://create.roblox.com/docs/resources/feature-packages/changelog.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: resources / feature-packages / changelog

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/resources/feature-packages/changelog.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Changelog for Roblox Feature Packages (Core, Bundles, Missions, Season Passes) covering breaking changes to HUD button centralization in ModalManager, renamed RoundProgressBar, UITween/UITimer fixes, and example config updates.

## Tips
- [page](https://create.roblox.com/docs/resources/feature-packages/changelog) **[[code-architecture-and-frameworks]]** When upgrading packages, update all packages to use the new centralized HUD button locations in FeaturePackagesCore ScreenGui; old placement breaks.
- [page](https://create.roblox.com/docs/resources/feature-packages/changelog) **[[ui-ux-design]]** Use FeaturePackagesCore.ModalManager.getHudGui() to fetch the shared HUD ScreenGui, which holds two frames for HUD button placement.
- [page](https://create.roblox.com/docs/resources/feature-packages/changelog) **[[ui-ux-design]]** Reduced hover animation duration from 0.5 to 0.3 seconds for a snappier feel; UIHover now adjusts TextTransparency/BackgroundTransparency on text buttons instead of resizing them.
- [page](https://create.roblox.com/docs/resources/feature-packages/changelog) **[[scripting-and-performance]]** Base timers on Workspace:GetServerTimeNow() rather than DateTime.now() to keep client and server timers synchronized.

## Numbers
- [page](https://create.roblox.com/docs/resources/feature-packages/changelog) Hover animation duration: **0.5s -> 0.3s** (playPurchaseEffect UIHover animation, Feature Packages Core v5)
- [page](https://create.roblox.com/docs/resources/feature-packages/changelog) Animated ImageLabel ImageTransparency: **0** (playPurchaseEffect now always sets 0 for better visibility)
- [page](https://create.roblox.com/docs/resources/feature-packages/changelog) HUD ScreenGui frames: **2** (ModalManager.getHudGui() ScreenGui contains two frames for HUD button locations)

## Tools
FeaturePackages Core, ModalManager, UITimer, UITween

## Topics
[[code-architecture-and-frameworks]] [[common-mistakes]] [[development-process-and-speed]] [[scripting-and-performance]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
