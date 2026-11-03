---
title: "Docs: animation / events"
url: https://create.roblox.com/docs/animation/events.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: animation / events

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/animation/events.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on animation event markers: creating markers in the Animation Events bar of the timeline, attaching string parameters, detecting them in a LocalScript via GetMarkerReachedSignal, and duplicating events across an animation.

## Tips
- [page](https://create.roblox.com/docs/animation/events) **[[building-art-and-assets]]** Use animation event markers (e.g. FootStep) to trigger sounds or effects at exact animation frames instead of relying on timed waits.
- [page](https://create.roblox.com/docs/animation/events) **[[scripting-and-performance]]** Connect GetMarkerReachedSignal(name) on the AnimationTrack to react to a named keyframe; pass a Parameter string for per-marker data.
- [page](https://create.roblox.com/docs/animation/events) **[[building-art-and-assets]]** Events are available across the whole animation once created; copy and paste a marker to reuse it, e.g. FootStep for both left and right foot.
- [page](https://create.roblox.com/docs/animation/events) **[[building-art-and-assets]]** Enable Show Animation Events from the timeline settings icon to reveal the Animation Events bar.

## Tools
Animation Editor, Animation Events bar, AnimationTrack:GetMarkerReachedSignal

## Topics
[[building-art-and-assets]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
