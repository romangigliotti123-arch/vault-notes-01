---
title: "Docs: effects / beams"
url: https://create.roblox.com/docs/effects/beams.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: effects / beams

[Open](https://create.roblox.com/docs/effects/beams.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox Creator Docs page on Beams: how a Beam renders a Texture between two Attachments, and how to configure color, transparency, width, texture length/mode, facing, and Bézier curve.

## Tips
- [page](https://create.roblox.com/docs/effects/beams) **[[vfx-and-particles]]** Beams need two Attachments assigned to Attachment0 and Attachment1; each must be a different Attachment object, or the beam stops rendering its texture.
- [page](https://create.roblox.com/docs/effects/beams) **[[vfx-and-particles]]** Enable Show Constraint Details in Studio's View menu to see attachment positions while building beams.
- [page](https://create.roblox.com/docs/effects/beams) **[[optimization-and-streaming]]** Review beam visuals at both lowest and highest Editor Quality Level (Studio Settings) because beam appearance changes with player graphics settings.
- [page](https://create.roblox.com/docs/effects/beams) **[[vfx-and-particles]]** Use a ColorSequence keypoint gradient for color changes along the beam span instead of a single constant color for effects like waterfalls.
- [page](https://create.roblox.com/docs/effects/beams) **[[vfx-and-particles]]** Use a NumberSequence for Transparency to make a beam fade over its length or over time.
- [page](https://create.roblox.com/docs/effects/beams) **[[building-art-and-assets]]** Use FaceCamera = true on flat beams so they remain visible from any camera angle, since a beam is a 2D projection in 3D space.
- [page](https://create.roblox.com/docs/effects/beams) **[[vfx-and-particles]]** Width0 and Width1 set per-endpoint width in studs; values below 0 are clamped to 0, so use this to taper or warp beam shape.
- [page](https://create.roblox.com/docs/effects/beams) **[[vfx-and-particles]]** With TextureMode Wrap or Static, repeats equal beam length divided by TextureLength; with Stretch, the texture repeats TextureLength times across the whole beam.
- [page](https://create.roblox.com/docs/effects/beams) **[[vfx-and-particles]]** Shape curves with CurveSize0 and CurveSize1 and attachment orientation; control points extend along the attachments' X axes (positive X for Attachment0, negative X for Attachment1).

## Numbers
- [page](https://create.roblox.com/docs/effects/beams) Transparency range: **0 (opaque) to 1 (fully clear)** (Beam Transparency value or NumberSequence keypoints)
- [page](https://create.roblox.com/docs/effects/beams) Texture repetitions (Wrap/Static): **beam length / TextureLength** (Beam TextureMode Wrap or Static)
- [page](https://create.roblox.com/docs/effects/beams) Texture repetitions (Stretch): **TextureLength** (Beam TextureMode Stretch, repeats across whole span)
- [page](https://create.roblox.com/docs/effects/beams) Negative width clamp: **0** (Width0/Width1 values below 0 are set back to 0)

## Tools
Roblox Studio, Beam, Attachment, Studio Settings Editor Quality Level

## He points to
- Roblox Creator Docs: Beams

## Topics
[[building-art-and-assets]] [[optimization-and-streaming]] [[vfx-and-particles]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
