---
title: "How Do You Make 'Impossible' Roblox Features?"
url: https://youtu.be/dd9QvPp6HQI
creator: ByteBlox
official: false
advice_density: low
date: 2024-10-24
views: 376722
transcript: auto-captions
confidence: high
tags: [roblox, byteblox100, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.1
---

> [!note] Trust: TRUSTED (credibility audit score 8.1): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# How Do You Make "Impossible" Roblox Features?

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Watch](https://youtu.be/dd9QvPp6HQI) | byteblox100 | 376,722 views | 2024-10-24

## Summary
Shows how to use ViewportFrames for Roblox optical illusions: transparent parts visible only via UI gradient, low-frame-rate character by cloning character into a ViewportFrame updated every 0.05-0.1s, and multi-viewport mirrored clones. Mostly experimental, not a business guide.

## Tips
- [1:01](https://youtu.be/dd9QvPp6HQI?t=61) **[[building-art-and-assets]]** ViewportFrames render any model inside them as UI, so they draw on top of the world and ignore walls; useful for unusual visual effects.
- [5:43](https://youtu.be/dd9QvPp6HQI?t=343) **[[scripting-and-performance]]** Rebuild ViewportFrame children each frame in a task.wait() loop, clearing old children except UIGradients, and set view.CurrentCamera to workspace.CurrentCamera.
- [8:53](https://youtu.be/dd9QvPp6HQI?t=533) **[[ui-ux-design]]** Use UIGradient transparency to make ViewportFrame content fade based on view angle, creating parts visible only when looked at.
- [12:42](https://youtu.be/dd9QvPp6HQI?t=762) **[[building-art-and-assets]]** Use a basic character with no accessories for ViewportFrame cloning; accessories break the clone setup.

## Numbers
- [0:41](https://youtu.be/dd9QvPp6HQI?t=41) Views: **Optical illusion video reached about 1 million views** (Creator's earlier low-frame-rate character video)
- [0:41](https://youtu.be/dd9QvPp6HQI?t=41) Views: **Second optical illusion video about to hit 1 million** (Creator's portal optical illusion video)
- [13:24](https://youtu.be/dd9QvPp6HQI?t=804) Update interval: **0.05-0.1 seconds** (Low-frame-rate character update interval)

## Tools
ViewportFrame, UIGradient, TweenService, Roblox Studio

## Topics
[[building-art-and-assets]] [[scripting-and-performance]] [[ui-ux-design]]

Back to [[byteblox100 - How to make successful Roblox games]]
