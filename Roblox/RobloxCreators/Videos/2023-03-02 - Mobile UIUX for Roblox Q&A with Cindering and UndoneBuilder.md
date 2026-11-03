---
title: "Mobile UI/UX for Roblox Q&A with Cindering and UndoneBuilder"
url: https://youtu.be/PjwJb_nSePY
creator: Roblox Creators
official: true
advice_density: high
date: 2023-03-02
views: 785
transcript: manual-subs
confidence: medium
tags: [roblox, robloxcreators, youtube-learn]
---

# Mobile UI/UX for Roblox Q&A with Cindering and UndoneBuilder

[Watch](https://youtu.be/PjwJb_nSePY) | RobloxCreators | 785 views | 2023-03-02

## Summary
Roblox Level Up roundtable Q&A on mobile UI/UX with Cindering and UndoneBuilder. Covers aspect-ratio constraints, portrait vs landscape, tooltips and button clarity, UI style vs function, controller/console support, UIGridLayout with ScrollFrame, keeping PC features on mobile, playtesting on devices, and handling small screens by moving content into the 3D world.

## Tips
- [0:30](https://youtu.be/PjwJb_nSePY?t=30) **[[building-art-and-assets]]** Learn UI constraints (UIAspectRatioConstraint, UISizeConstraint, etc.) instead of fixed offsets; they make UI scale across the hundreds of mobile aspect ratios.
- [2:22](https://youtu.be/PjwJb_nSePY?t=142) **[[common-mistakes]]** Don't build portrait mode for a new game; players expect landscape on mobile. Only consider it for very simple games or later, after a hit.
- [3:02](https://youtu.be/PjwJb_nSePY?t=182) **[[common-mistakes]]** Don't stylize UI so heavily that players can't tell what it does; clarity matters more than looks.
- [4:28](https://youtu.be/PjwJb_nSePY?t=268) **[[first-session-onboarding]]** Make button function clear at a glance with clear icons and text; don't rely on hover tooltips, which mobile players can't use.
- [4:28](https://youtu.be/PjwJb_nSePY?t=268) **[[core-loops-and-game-design]]** Long-press to reveal extra info is hidden; only put non-critical details behind it, and show critical info directly.
- [5:49](https://youtu.be/PjwJb_nSePY?t=349) **[[monetisation-gamepasses]]** Add a small info (i) or question-mark button next to monetization items to explain what a gamepass does.
- [6:40](https://youtu.be/PjwJb_nSePY?t=400) **[[building-art-and-assets]]** Prioritize readable, simple UI over ornate styling; top Roblox games use simple, functional UIs.
- [7:59](https://youtu.be/PjwJb_nSePY?t=479) **[[building-art-and-assets]]** Lay out buttons in a grid so controller cursor navigation is easy, and enable the Selectable property on UI buttons for console/controller support.
- [8:54](https://youtu.be/PjwJb_nSePY?t=534) **[[building-art-and-assets]]** Pair UIGridLayout with ScrollFrame and script the canvas size to fit contents; this makes dynamically sized grids easy.
- [9:48](https://youtu.be/PjwJb_nSePY?t=588) **[[core-loops-and-game-design]]** Keep PC features on mobile by merging menus rather than cutting them; only cut movement controls that don't apply to touch (e.g. slide).
- [11:00](https://youtu.be/PjwJb_nSePY?t=660) **[[playtesting-and-feedback]]** Playtest on as many devices as possible, including old phones for performance; use the device emulator when you lack hardware.
- [11:41](https://youtu.be/PjwJb_nSePY?t=701) **[[playtesting-and-feedback]]** Watch a new player who doesn't know the game play it; observe where they tap and what confuses them.
- [14:13](https://youtu.be/PjwJb_nSePY?t=853) **[[building-art-and-assets]]** Keep core UI within a safe central layout that fits all screens; move overflow content like leaderboards into the 3D world on a panel the camera can reach.
- [14:54](https://youtu.be/PjwJb_nSePY?t=894) **[[building-art-and-assets]]** Test every UI in the device emulator to confirm it fits on different screen sizes.

## Numbers
- [1:10](https://youtu.be/PjwJb_nSePY?t=70) Aspect ratios: **Hundreds of device aspect ratios, per speaker** (Speaker says dozens is an understatement)
- [3:02](https://youtu.be/PjwJb_nSePY?t=182) Player complaints: **Zero** (Speaker says no player complained about missing portrait support in almost a decade)

## Games
- **Natural Disaster Survival** [2:22](https://youtu.be/PjwJb_nSePY?t=142): Simple movement-and-avoid gameplay is one of the few cases where portrait mode is practical.
- **Adopt Me!** [6:40](https://youtu.be/PjwJb_nSePY?t=400): Cute, adorable UI that stays highly readable; a good model for balancing style and clarity.
- **War Sim** [9:48](https://youtu.be/PjwJb_nSePY?t=588): Sliding while sprinting exists on PC but was cut on mobile because it doesn't apply to touch controls.
- **Roblox High School** [13:41](https://youtu.be/PjwJb_nSePY?t=821): Original version predates constraints and scaling; the creator used tiny offset-based UIs to fit mobile.

## Tools
UIAspectRatioConstraint, UIGridLayout, ScrollFrame, Device emulator, Virtual cursor (Roblox gamepad)

## He points to
- Roblox Level Up YouTube channel
- Roblox Level Up Guilded server

## Quotes
- [0:30](https://youtu.be/PjwJb_nSePY?t=30) "I was really surprised how few developers when I spoke to them knew how to use them and they are just amazing."
- [6:40](https://youtu.be/PjwJb_nSePY?t=400) "It is understandable is far more important than it being stylized or pretty."
- [14:13](https://youtu.be/PjwJb_nSePY?t=853) "If it fits in that, it fits on mobile. Anything else goes in the physical world."

## Topics
[[building-art-and-assets]] [[common-mistakes]] [[core-loops-and-game-design]] [[first-session-onboarding]] [[monetisation-gamepasses]] [[playtesting-and-feedback]]

Back to [[RobloxCreators - How to make successful Roblox games]]
