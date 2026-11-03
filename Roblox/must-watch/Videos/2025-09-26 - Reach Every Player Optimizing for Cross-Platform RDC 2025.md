---
title: "Reach Every Player: Optimizing for Cross-Platform | RDC 2025"
url: https://youtu.be/R1gecdxghwE
creator: Roblox
official: true
advice_density: medium
date: 2025-09-26
views: 15520
transcript: auto-captions
confidence: high
tags: [roblox, mustwatch, youtube-learn]
---

# Reach Every Player: Optimizing for Cross-Platform | RDC 2025

[Watch](https://youtu.be/R1gecdxghwE) | MustWatch | 15,520 views | 2025-09-26

## Summary
RDC 2025 talk on cross-platform Roblox development. Presents three pillars (responsive layout, input abstraction, ergonomic UI) and new APIs: styling, input action system, preferred input, viewport display size, text size and size constraints. Walks through building an RPG HUD, then Q&A.

## Tips
- [9:45](https://youtu.be/R1gecdxghwE?t=585) **[[building-art-and-assets]]** Build each UI element responsive from the start: use scale properties (e.g. 0.8 icon scale) plus UIAspectRatioConstraint to keep square items.
- [10:27](https://youtu.be/R1gecdxghwE?t=627) **[[building-art-and-assets]]** Use UIListLayout or the new flex properties so repeated items line up with consistent padding at any screen size or item count.
- [13:39](https://youtu.be/R1gecdxghwE?t=819) **[[building-art-and-assets]]** Swap UI style tags instead of duplicating instances to rearrange HUD per orientation; style position and anchor point via the style editor.
- [14:06](https://youtu.be/R1gecdxghwE?t=846) **[[building-art-and-assets]]** Use the viewport display size API (small/medium/large) to decide content: expand minimap over viewport on large screens, fullscreen it on small ones.
- [16:12](https://youtu.be/R1gecdxghwE?t=972) **[[scripting-and-performance]]** Prefer PreferredInput over LastInputType for showing hints and controls; it is stable and avoids costly re-renders from every keystroke.
- [17:49](https://youtu.be/R1gecdxghwE?t=1069) **[[scripting-and-performance]]** Define actions in the input action system with bindings for touch, gamepad and keyboard, so game code connects once to the action regardless of hardware.
- [19:57](https://youtu.be/R1gecdxghwE?t=1197) **[[scripting-and-performance]]** Input action system is built on server authority: actions replicate and re-simulate on the server, so validate inputs there. Client beta available now.
- [22:18](https://youtu.be/R1gecdxghwE?t=1338) **[[building-art-and-assets]]** Use TextScaled plus UITextSizeConstraint (min/max) so text stays legible on mobile without becoming oversized on monitors.
- [23:01](https://youtu.be/R1gecdxghwE?t=1381) **[[building-art-and-assets]]** Use UISizeConstraint to enlarge hit targets on touch screens and allow smaller ones on mouse, keeping them easy to hit on every device.
- [23:43](https://youtu.be/R1gecdxghwE?t=1423) **[[building-art-and-assets]]** Define themes with the style system to support light/dark mode, seasonal event theming and high-contrast accessibility packs.
- [23:53](https://youtu.be/R1gecdxghwE?t=1433) **[[playtesting-and-feedback]]** Use Studio emulation to test most APIs (including VR and Xbox Ally) before production, so device bugs surface early.
- [27:27](https://youtu.be/R1gecdxghwE?t=1647) **[[common-mistakes]]** Avoid assuming device from capabilities: a PC can have touch, and a console may have keyboard and mouse attached. Don't hard-code device-specific control schemes.
- [3:46](https://youtu.be/R1gecdxghwE?t=226) **[[common-mistakes]]** Do not write bespoke keyboard-only code; hotkeys that do not map to gamepad or touch break on other devices. Test portrait mode layouts, which often collapse.
- [5:21](https://youtu.be/R1gecdxghwE?t=321) **[[core-loops-and-game-design]]** Design for independent input and form-factor dimensions rather than targeting PC, console or mobile separately, so new devices work automatically.
- [4:40](https://youtu.be/R1gecdxghwE?t=280) **[[analytics-metrics]]** Multi-device users reportedly spend over 2.5x more per hour and engage over 20% longer, so cross-platform support is a revenue lever.

## Numbers
- [4:40](https://youtu.be/R1gecdxghwE?t=280) Multi-device user spend per hour: **over 2.5x** (Speaker cites Raj's figure from prior day's keynote)
- [4:40](https://youtu.be/R1gecdxghwE?t=280) Multi-device user engagement: **over 20% longer** (Engagement duration versus single-device users, per keynote)
- [4:40](https://youtu.be/R1gecdxghwE?t=280) Roblox gaming market share goal: **over 10%** (Stated company goal for share of gaming market)
- [22:18](https://youtu.be/R1gecdxghwE?t=1338) UITextSizeConstraint example range: **min 24, max 64** (Example text size bounds shown in Studio properties panel)

## Games
- **Harvesting and planting simulator (example)**: Speaker's example game: dig holes, build houses, walls, roofs and doors; used to show multi-action input mapping.
- **RPG (example)**: Demo project used throughout the talk to show responsive HUD, item selector, minimap and input handling.

## Tools
Styling APIs (stylesheets, tokens, themes, no-code style editor), Input action system, PreferredInput API, ViewportDisplaySize API, UIListLayout and flex properties, TextScaled and UITextSizeConstraint, UISizeConstraint, Studio emulation

## He points to
- RDC 2025 device lab and creation support area
- QR code demo experience shown at end of talk

## Quotes
- [26:09](https://youtu.be/R1gecdxghwE?t=1569) "Build once, play everywhere will become even more powerful and easier to achieve."
- [28:08](https://youtu.be/R1gecdxghwE?t=1688) "The recommendation is to use preferred input over last input unless you really want to know for some reason that there was a mouse click or a specific keyboard stroke."
- [15:21](https://youtu.be/R1gecdxghwE?t=921) "Even experts get this wrong, like on something like the Xbox Ally. Our own UI didn't work at the beginning in our examples."

## On screen
Contact sheet shows Studio property panels for UIAspectRatioConstraint, UIListLayout, style tags (Styling/ViewportDisplaySize/AnchorPoint), a minimap expanding in a HUD, the input bindings code snippet (PreferredInput, GetImageForKeyCode), UITextSizeConstraint (min 24, max 64) and UISizeConstraint (min 80x80) on a phone/monitor mockup.

## Topics
[[analytics-metrics]] [[building-art-and-assets]] [[common-mistakes]] [[core-loops-and-game-design]] [[playtesting-and-feedback]] [[scripting-and-performance]]

Back to [[MustWatch - How to make successful Roblox games]]
