---
title: "The Ultimate Guide to Custom Loading/Health Bars"
url: https://devforum.roblox.com/t/the-ultimate-guide-to-custom-loadinghealth-bars/1323459
creator: Roblox DevForum
official: false
advice_density: low
date: 2021-07-01
views: 215
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# The Ultimate Guide to Custom Loading/Health Bars

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://devforum.roblox.com/t/the-ultimate-guide-to-custom-loadinghealth-bars/1323459) | Roblox DevForum | 215 views | 2021-07-01

## Summary
Moonvane's DevForum tutorial on building custom rounded and image-based loading/health bars in Roblox UI. Covers the frame hierarchy (FrameBase, Clipping, Top) and a Luau function that resizes the bar by a ratio while keeping the inner Top frame's scale correct.

## Tips
- [page](https://devforum.roblox.com/t/the-ultimate-guide-to-custom-loadinghealth-bars/1323459) **[[ui-ux-design]]** Build a loading bar as nested frames: a rounded base, a clipping frame set to clip descendants, and a Top frame sized {1,0,1,0} inside it.
- [page](https://devforum.roblox.com/t/the-ultimate-guide-to-custom-loadinghealth-bars/1323459) **[[ui-ux-design]]** Scale the bar by setting Clipping width to the ratio and Top width to 1/ratio so the inner fill stays correctly sized.
- [page](https://devforum.roblox.com/t/the-ultimate-guide-to-custom-loadinghealth-bars/1323459) **[[scripting-and-performance]]** Guard the 1/ratio calculation against zero (use sizeRatio > 0 check) to avoid dividing by zero.
- [page](https://devforum.roblox.com/t/the-ultimate-guide-to-custom-loadinghealth-bars/1323459) **[[ui-ux-design]]** Darken the ImageBase color when building image-based bars so the difference between the two images is visible.

## Numbers
- [page](https://devforum.roblox.com/t/the-ultimate-guide-to-custom-loadinghealth-bars/1323459) Example clipping size ratio: **0.7** (Example ratio used to demonstrate scaling behavior in the tutorial)

## Tools
Roblox Studio, Luau

## Topics
[[scripting-and-performance]] [[ui-ux-design]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
