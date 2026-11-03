---
title: "Docs: effects / highlighting"
url: https://create.roblox.com/docs/effects/highlighting.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: effects / highlighting

[Open](https://create.roblox.com/docs/effects/highlighting.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on the Highlight instance: adding highlights (parenting or Adornee), customizing OutlineColor/FillColor/transparency/DepthMode/Enabled, the 255 client-side highlight limit, and performance guidance.

## Tips
- [page](https://create.roblox.com/docs/effects/highlighting) **[[building-art-and-assets]]** Keep the 255 simultaneous client-side Highlight limit in mind; extra highlights are silently ignored.
- [page](https://create.roblox.com/docs/effects/highlighting) **[[optimization-and-streaming]]** Adding or removing a Highlight causes geometry rebuilding, causing spikes and extra draw calls. Change properties or Enabled instead of re-creating.
- [page](https://create.roblox.com/docs/effects/highlighting) **[[optimization-and-streaming]]** Disabled highlights still consume one of the 255 slots. Delete permanently unused highlights rather than disabling them.
- [page](https://create.roblox.com/docs/effects/highlighting) **[[optimization-and-streaming]]** The first rendered highlight costs up to 1 ms GPU on mobile; additional highlights add no significant cost on any platform.
- [page](https://create.roblox.com/docs/effects/highlighting) **[[optimization-and-streaming]]** On mobile, highlight cost scales with screen coverage. Keep highlighted objects small on screen when targeting phones.
- [page](https://create.roblox.com/docs/effects/highlighting) **[[optimization-and-streaming]]** Avoid nesting objects with child Highlights inside other objects that also have child Highlights; keep them out of parent/child relationships.
- [page](https://create.roblox.com/docs/effects/highlighting) **[[ui-ux-design]]** Use highlights to signal that an object is important or interactable, or to show teammates' positions and status.
- [page](https://create.roblox.com/docs/effects/highlighting) **[[ui-ux-design]]** Use DepthMode AlwaysOnTop to keep important objects visible through walls; Occluded hides them behind obstructions.

## Numbers
- [page](https://create.roblox.com/docs/effects/highlighting) Max simultaneous client-side Highlights: **255** (Extra highlights are silently ignored beyond this limit)
- [page](https://create.roblox.com/docs/effects/highlighting) GPU cost of first rendered highlight on mobile: **up to 1 ms** (Additional highlights have no significant impact)
- [page](https://create.roblox.com/docs/effects/highlighting) Default highlight appearance: **white outline, red fill** (Default OutlineColor and FillColor when parented)

## Tools
Roblox Studio Explorer, Highlight instance

## He points to
- Roblox Creator Docs: Highlight class

## Topics
[[building-art-and-assets]] [[optimization-and-streaming]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
