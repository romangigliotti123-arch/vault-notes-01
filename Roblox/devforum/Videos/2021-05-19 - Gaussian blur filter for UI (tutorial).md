---
title: "Gaussian blur filter for UI (tutorial)"
url: https://devforum.roblox.com/t/gaussian-blur-filter-for-ui-tutorial/1238701
creator: Roblox DevForum
official: false
advice_density: medium
date: 2021-05-19
views: 299
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Gaussian blur filter for UI (tutorial)

[Open](https://devforum.roblox.com/t/gaussian-blur-filter-for-ui-tutorial/1238701) | Roblox DevForum | 299 views | 2021-05-19

## Summary
Tutorial on faking a Gaussian blur behind UI in Roblox using Fractality's neon/glass ModularScript, a LocalScript bound to a frame, and a DepthOfField effect. Covers setup, subframe offsets to reduce edge bleed, and limits with rounded frames.

## Tips
- [page](https://devforum.roblox.com/t/gaussian-blur-filter-for-ui-tutorial/1238701) **[[ui-ux-design]]** Blur only works on 3D-space elements (decals, parts, SurfaceGuis); ScreenGui frames cannot be blurred directly.
- [page](https://devforum.roblox.com/t/gaussian-blur-filter-for-ui-tutorial/1238701) **[[building-art-and-assets]]** Set the ModularScript's p0.Material from 'Neon' to 'Glass' to get the glass-style blur part.
- [page](https://devforum.roblox.com/t/gaussian-blur-filter-for-ui-tutorial/1238701) **[[ui-ux-design]]** Use a subframe named 'Blur' with scale offsets around -3 and Visible off, and place the LocalScript inside it to reduce edge bleeding.
- [page](https://devforum.roblox.com/t/gaussian-blur-filter-for-ui-tutorial/1238701) **[[ui-ux-design]]** Tune DepthOfField settings during playtesting to minimise bleeding around frame edges.
- [page](https://devforum.roblox.com/t/gaussian-blur-filter-for-ui-tutorial/1238701) **[[ui-ux-design]]** Very rounded frames (circles, non-square ImageFrames) do not work well with this effect; UICorner with offset around 5 to 7 still looks acceptable.
- [page](https://devforum.roblox.com/t/gaussian-blur-filter-for-ui-tutorial/1238701) **[[ui-ux-design]]** Tweening, scaling and positioning of blurred frames work without breaking the effect.

## Numbers
- [page](https://devforum.roblox.com/t/gaussian-blur-filter-for-ui-tutorial/1238701) Frame BackgroundTransparency: **0.5** (Blur frame setup in step 3)
- [page](https://devforum.roblox.com/t/gaussian-blur-filter-for-ui-tutorial/1238701) Blur neon Transparency: **0.98** (Value passed to neon:BindFrame in LocalScript)
- [page](https://devforum.roblox.com/t/gaussian-blur-filter-for-ui-tutorial/1238701) Blur subframe scale offset: **-3** (Suggested offset to reduce edge bleed)
- [page](https://devforum.roblox.com/t/gaussian-blur-filter-for-ui-tutorial/1238701) UICorner offset for circles: **5 to 7** (Suggested range that still looks good with rounded frames)

## Tools
Fractality's neon ModularScript, DepthOfField (Lighting), LocalScript

## He points to
- Fractality (original ModularScript author)

## Topics
[[building-art-and-assets]] [[ui-ux-design]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
