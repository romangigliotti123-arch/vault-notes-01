---
title: "Docs: workspace / streaming / slim"
url: https://create.roblox.com/docs/workspace/streaming/slim.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: workspace / streaming / slim

[Open](https://create.roblox.com/docs/workspace/streaming/slim.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on SLIM, an automatic cloud-transcoded optimization for static models and R15 avatars under StreamingEnabled. Covers prerequisites, distance zones, enabling per model, avatar support and exclusions, limitations, debug tint modes, and troubleshooting.

## Tips
- [page](https://create.roblox.com/docs/workspace/streaming/slim) **[[building-and-level-design]]** Enable StreamingEnabled on Workspace first; SLIM only functions with streaming on, otherwise falls back to traditional LOD.
- [page](https://create.roblox.com/docs/workspace/streaming/slim) **[[titles-descriptions]]** Publish the place to Roblox and enable Team Create before testing; local .rbxl files produce no SLIM results.
- [page](https://create.roblox.com/docs/workspace/streaming/slim) **[[optimization-and-streaming]]** Set Model.LevelOfDetail to SLIM on static world models (buildings, props, vehicles, terrain features); avoid runtime part add/remove or property changes on them.
- [page](https://create.roblox.com/docs/workspace/streaming/slim) **[[optimization-and-streaming]]** Wait 1–2 minutes after first publish for cloud transcoding, then rejoin; transcoded assets persist on CDN.
- [page](https://create.roblox.com/docs/workspace/streaming/slim) **[[common-mistakes]]** Do not put Humanoid instances inside SLIM models; use SLIM avatars for animated characters instead.
- [page](https://create.roblox.com/docs/workspace/streaming/slim) **[[common-mistakes]]** Avoid models with zero Scale, and models that play animations, since they are excluded from SLIM processing.
- [page](https://create.roblox.com/docs/workspace/streaming/slim) **[[building-art-and-assets]]** Separate problematic PartOperation unions/negations into their own model or simplify CSG if they render missing or distorted in SLIM.
- [page](https://create.roblox.com/docs/workspace/streaming/slim) **[[building-art-and-assets]]** Move coplanar or overlapping parts apart by about 0.01 studs to eliminate Z-fighting on SLIM models.
- [page](https://create.roblox.com/docs/workspace/streaming/slim) **[[building-art-and-assets]]** Use SurfaceAppearance for important surfaces and group related parts in one model, since SLIM regenerates UVs and default material tiling may shift.
- [page](https://create.roblox.com/docs/workspace/streaming/slim) **[[client-server-and-remotes]]** For SLIM avatars, set Workspace.EnableSLIMAvatars to Enabled and do not modify the avatar after Player.CharacterAppearanceLoaded (tools, accessories, Highlights added later are excluded).
- [page](https://create.roblox.com/docs/workspace/streaming/slim) **[[common-mistakes]]** R6 avatars, NPCs, custom proportions, and body scaling are not eligible for SLIM avatars and fall back to default rendering.
- [page](https://create.roblox.com/docs/workspace/streaming/slim) **[[analytics-metrics]]** Use Developer Console DebugVisualizations > SlimTintMode (LOD or DataModelState) to verify SLIM status; Studio also offers TranscoderStatus while editing.
- [page](https://create.roblox.com/docs/workspace/streaming/slim) **[[testing-debugging-and-qa]]** Test SLIM avatars with Team Test using friends or alt accounts, or Server and Clients mode with at least 2 clients; single-player testing cannot show them.

## Numbers
- [page](https://create.roblox.com/docs/workspace/streaming/slim) Far-distance audience triangles: **SLIM ~170,000 vs disabled ~2,600,000** (Avatar audience far distance; client instances ~4,000 vs ~60,000)
- [page](https://create.roblox.com/docs/workspace/streaming/slim) Near-proximity audience triangles: **SLIM ~100,000 vs disabled ~670,000** (Avatar audience near proximity; client instances ~31,000 vs ~60,000)
- [page](https://create.roblox.com/docs/workspace/streaming/slim) Transcoding wait after first publish: **1–2 minutes** (Wait then rejoin before expecting SLIM model to appear)
- [page](https://create.roblox.com/docs/workspace/streaming/slim) Z-fighting separation: **0.01 studs** (Minimum offset to separate overlapping parts in SLIM model)

## Games
- **City People Cars SLIM Template**: Template showing world models with SLIM enabled.
- **SLIM Platform Avatars**: Demonstrates 200 animated avatars rendered with SLIM.

## Tools
Roblox Studio, Developer Console DebugVisualizations, Command Bar

## He points to
- Enum.SlimTintMode
- Enum.SlimTranscoderStatus
- Workspace.StreamingEnabled streaming properties

## Topics
[[analytics-metrics]] [[building-and-level-design]] [[building-art-and-assets]] [[client-server-and-remotes]] [[common-mistakes]] [[optimization-and-streaming]] [[testing-debugging-and-qa]] [[titles-descriptions]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
