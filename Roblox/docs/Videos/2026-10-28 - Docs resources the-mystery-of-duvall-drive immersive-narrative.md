---
title: "Docs: resources / the-mystery-of-duvall-drive / immersive-narrative"
url: https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/immersive-narrative.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: resources / the-mystery-of-duvall-drive / immersive-narrative

[Open](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/immersive-narrative.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on the immersive narrative system in Duvall Drive (Beyond the Dark-style demo). Covers four diegetic info techniques: visual cues, lore (fullscreen, highlighted objects), thought bubbles (BillboardGui near object), and announcements (fullscreen third-person to all players), plus implementation via ScreenGui, TextLabel RichText, and a shared StoryNote object.

## Tips
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/immersive-narrative) **[[core-loops-and-game-design]]** Decide what story/info to convey first, then choose how the world communicates it; keep diegetic over UI overlays to preserve immersion.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/immersive-narrative) **[[building-and-level-design]]** Visual cues must have an in-world reason to exist even when no player is present; avoid out-of-place instructional signs.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/immersive-narrative) **[[ui-ux-design]]** Use a full-screen invisible back button so players can click or tap anywhere to close overlays, avoiding distracting buttons across PC, console and mobile.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/immersive-narrative) **[[ui-ux-design]]** Use Scale-based positioning and TextScaled inside a Frame so overlay text and images rescale across devices.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/immersive-narrative) **[[common-mistakes]]** Don't highlight every interactable: the team's Highlight on all objects caused visual noise; restrict highlights to corrupted or dangerous items.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/immersive-narrative) **[[common-mistakes]]** Don't attach lore to everything: players couldn't tell important story from flavor, so the team removed much of it and relied on visual cues.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/immersive-narrative) **[[localization-and-international]]** Use TextLabels rather than text images in BillboardGui thought bubbles so text stays readable by Roblox and auto-localizes.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/immersive-narrative) **[[ui-ux-design]]** Reuse one ScreenGui/TextLabel (e.g., StoryNote) and inject text and RichText via script instead of creating many ScreenGuis per event.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/immersive-narrative) **[[ui-ux-design]]** Use RichText markup to style narration by speaker (color, font, size) and to interrupt sentences mid-line for entity intrusions.

## Games
- **Duvall Drive**: Uses visual cues, lore, thought bubbles and announcements so story is told in-world rather than through UI.
- **Beyond the Dark**: Referenced as the demo that inspired the diegetic-storytelling approach.

## Tools
Highlight, ScreenGui, BillboardGui, TextLabel, ImageLabel, Frame, RichText

## He points to
- Automatic translations (Roblox docs)

## Quotes
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/immersive-narrative) "We initially used Highlight for every object a player could interact with, but the visual noise was overwhelming."
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/immersive-narrative) "We originally had lore on everything you could click on! This wasn't helpful because players weren't sure what information was important."

## Topics
[[building-and-level-design]] [[common-mistakes]] [[core-loops-and-game-design]] [[localization-and-international]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
