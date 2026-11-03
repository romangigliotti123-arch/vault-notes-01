---
title: "Docs: production / publishing / accessibility"
url: https://create.roblox.com/docs/production/publishing/accessibility.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: production / publishing / accessibility

[Open](https://create.roblox.com/docs/production/publishing/accessibility.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox official accessibility guidelines: text size, color contrast, color non-reliance (symbols beside color), sound non-reliance (visual cues), and player preferences (PreferredTransparency, PreferredTextSize, ReducedMotionEnabled) plus volume controls, with code samples for each.

## Tips
- [page](https://create.roblox.com/docs/production/publishing/accessibility) **[[first-session-onboarding]]** Increase the size of smaller font labels so text is readable for low-vision players.
- [page](https://create.roblox.com/docs/production/publishing/accessibility) **[[building-art-and-assets]]** Pick text and background colors with sufficient contrast; avoid light-on-light or dark-on-dark text.
- [page](https://create.roblox.com/docs/production/publishing/accessibility) **[[building-art-and-assets]]** Don't rely on color alone; add symbols alongside colors so colorblind players can tell differences in gameplay and UI.
- [page](https://create.roblox.com/docs/production/publishing/accessibility) **[[building-art-and-assets]]** Don't convey game events only through sound; pair audio cues with visual indicators for hearing-impaired players.
- [page](https://create.roblox.com/docs/production/publishing/accessibility) **[[building-art-and-assets]]** Respect GuiService.PreferredTransparency by tagging UI backgrounds 'TransparentBack' and multiplying BackgroundTransparency by the preferred value.
- [page](https://create.roblox.com/docs/production/publishing/accessibility) **[[building-art-and-assets]]** Respect GuiService.PreferredTextSize; avoid TextScaled and fixed sizes where text should grow, and use AutomaticSize/TextWrapped so layouts adapt.
- [page](https://create.roblox.com/docs/production/publishing/accessibility) **[[building-art-and-assets]]** Check GuiService.ReducedMotionEnabled and set tween time to 0 or switch to a fade-in instead of positional motion.
- [page](https://create.roblox.com/docs/production/publishing/accessibility) **[[core-loops-and-game-design]]** Provide separate volume controls for music, sound effects, and speech so players can reduce noisy audio.

## Numbers
- [page](https://create.roblox.com/docs/production/publishing/accessibility) Share of people with some disability: **over 26% (cited in docs)**
- [page](https://create.roblox.com/docs/production/publishing/accessibility) Share of people with some color blindness: **over 5% worldwide**
- [page](https://create.roblox.com/docs/production/publishing/accessibility) Default UI tween time in example: **0.75 seconds (0 when reduced motion enabled)**

## Tools
GuiService, CollectionService, TweenService, TextService, UITextSizeConstraint, CanvasGroup

## He points to
- Roblox Creator Docs: Accessibility guidelines

## Topics
[[building-art-and-assets]] [[core-loops-and-game-design]] [[first-session-onboarding]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
