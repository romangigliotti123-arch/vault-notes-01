---
title: "How many parts is too many?"
url: https://youtu.be/tmyowxxIv8M
creator: PineappleDev
official: false
advice_density: medium
date: 2025-09-28
views: 1445
transcript: auto-captions
confidence: medium
tags: [roblox, pineappledevv, youtube-learn]
creator_trust: TRUSTED
creator_score: 7.7
---

> [!note] Trust: TRUSTED (credibility audit score 7.7): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# How many parts is too many?

[Watch](https://youtu.be/tmyowxxIv8M) | pineappledevv | 1,445 views | 2025-09-28

## Summary
Stress-tests how many parts Roblox Studio can handle using a script that spawns cubes. Shows FPS drop with visible part count, a big hit from unanchored/physics parts (even off-screen), and a smaller hit from ball shapes. Concludes mobile devices and unanchored parts are the main limits.

## Tips
- [0:22](https://youtu.be/tmyowxxIv8M?t=22) **[[scripting-and-performance]]** Keep parts anchored whenever possible; unanchored physics parts cost far more FPS than anchored ones, even when off-screen.
- [4:38](https://youtu.be/tmyowxxIv8M?t=278) **[[optimization-and-streaming]]** Minimise unanchored parts for mobile players; physics-simulated parts destroyed frame rate in the test.
- [1:43](https://youtu.be/tmyowxxIv8M?t=103) **[[optimization-and-streaming]]** Test performance on mobile-level hardware if many players will use phones; a mid-to-high PC handles far more than mobile devices.
- [1:04](https://youtu.be/tmyowxxIv8M?t=64) **[[optimization-and-streaming]]** Reduce the number of parts visible to the player at once; visible part count drives FPS loss more than total parts in the map.
- [3:17](https://youtu.be/tmyowxxIv8M?t=197) **[[optimization-and-streaming]]** Part shape matters somewhat (balls were slightly worse than cubes), but anchoring and visibility matter far more.

## Numbers
- [1:04](https://youtu.be/tmyowxxIv8M?t=64) Part count: **125,000 parts ran smoothly on a mid-to-high PC** (Anchored cubes, test machine, visible in view)
- [1:04](https://youtu.be/tmyowxxIv8M?t=64) Part count: **1,000,000 parts caused notable FPS drop** (Visible in view; FPS recovered when looking away)
- [2:20](https://youtu.be/tmyowxxIv8M?t=140) Unanchored parts: **~1,000 unanchored parts caused severe lag** (Even on a strong computer; described as roughly a thousand times impact)
- [3:17](https://youtu.be/tmyowxxIv8M?t=197) Ball vs cube: **~100,000 ball parts slightly worse than cubes** (Shape change had a smaller effect than anchoring)

## Tools
Roblox Studio

## Topics
[[optimization-and-streaming]] [[scripting-and-performance]]

Back to [[pineappledevv - How to make successful Roblox games]]
