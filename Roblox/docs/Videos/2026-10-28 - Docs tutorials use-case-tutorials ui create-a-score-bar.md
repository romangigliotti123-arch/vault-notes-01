---
title: "Docs: tutorials / use-case-tutorials / ui / create-a-score-bar"
url: https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/create-a-score-bar.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / use-case-tutorials / ui / create-a-score-bar

[Open](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/create-a-score-bar.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Official Roblox docs tutorial showing how to build a gold score bar UI in Studio: ScreenGui with a top-center frame, UISizeConstraint and UIListLayout for legibility, a crown icon, score text, and testing across devices with Device Emulator.

## Tips
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/create-a-score-bar) **[[first-session-onboarding]]** Use icons instead of text labels where possible; a simple recognizable icon (gold crown) communicates the goal without cluttering the screen.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/create-a-score-bar) **[[ui-ux-design]]** Add a UISizeConstraint with MinSize (e.g. 0, 40) so UI frames never shrink below a legible pixel height on small screens.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/create-a-score-bar) **[[ui-ux-design]]** Add a UIListLayout (Horizontal, VerticalAlignment Center) to frames so child GuiObjects arrange inside the frame instead of spilling outside its perimeter.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/create-a-score-bar) **[[ui-ux-design]]** Use SizeConstraint RelativeYY on icons and text labels so they scale with frame height and keep their aspect ratio.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/create-a-score-bar) **[[ui-ux-design]]** Use large, high-contrast text (e.g. TextSize 30 on a semi-transparent dark background) so it stays readable over busy 3D scenes.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/create-a-score-bar) **[[ui-ux-design]]** Set TextXAlignment to Left so score text stays anchored next to the icon as the number grows from 0 to 1,000,000.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/create-a-score-bar) **[[playtesting-and-feedback]]** Test UI in Studio's Device Emulator with Actual Resolution across Phone, Tablet, Desktop and Console presets; the Studio viewport aspect ratio does not match player screens.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/create-a-score-bar) **[[ui-ux-design]]** Keep HUD elements from taking too much room; oversized UI can block the 3D view on small phone screens.

## Numbers
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/create-a-score-bar) Score bar Frame Size: **0.25 x 0.08 scale (25% width, 8% height)** (Top-center HUD frame, AnchorPoint 0.5,0, Position y 0.01)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/create-a-score-bar) UISizeConstraint MinSize: **0, 40 px** (Minimum frame height so contents stay legible on small screens)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/create-a-score-bar) Frame transparency: **BackgroundColor 0.6 black, BackgroundTransparency 0.6** (Semi-transparent dark background behind score bar)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/create-a-score-bar) Icon Size: **1.25 x 1 scale, SizeConstraint RelativeYY** (Crown ImageLabel widened beyond frame width to preserve aspect ratio)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/create-a-score-bar) Score TextSize: **30** (Gold text color 255,200,100 with GothamSSm font)

## Games
- **Gold Rush**: Sample place file used as the reference for building a gold score bar HUD with crown icon and score text.

## Tools
Roblox Studio Explorer, Roblox Studio Properties window, Device Emulator

## He points to
- Gold Rush .rbxl sample place file

## Topics
[[first-session-onboarding]] [[playtesting-and-feedback]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
