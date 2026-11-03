---
title: "Docs: production / publishing / vr-guidelines"
url: https://create.roblox.com/docs/production/publishing/vr-guidelines.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: production / publishing / vr-guidelines

[Open](https://create.roblox.com/docs/production/publishing/vr-guidelines.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox official VR guidelines: OpenXR platform support, Quest Auto Quality Mode targeting 72 FPS, comfort settings (Vignette, Stepped Rotation, 3rd Person Fixed Camera), default vs custom camera tradeoffs, and mobile VR performance best practices.

## Tips
- [page](https://create.roblox.com/docs/production/publishing/vr-guidelines) **[[building-art-and-assets]]** Target 72 FPS on Quest; frame drops cause discomfort. If visuals look poor under Auto Quality Mode, optimize the game further rather than accepting degraded output.
- [page](https://create.roblox.com/docs/production/publishing/vr-guidelines) **[[core-loops-and-game-design]]** Use Roblox default camera scripts (CameraModule child scripts) for VR; they receive ongoing updates and comfort-setting support, unlike custom cameras.
- [page](https://create.roblox.com/docs/production/publishing/vr-guidelines) **[[scripting-and-performance]]** Replace custom camera scripts only if necessary; custom cameras opt out of updates and require manual merging of VR camera fixes. Merge current VR camera scripts if using a custom one.
- [page](https://create.roblox.com/docs/production/publishing/vr-guidelines) **[[scripting-and-performance]]** Enable instance streaming so content streams in and out dynamically on the headset.
- [page](https://create.roblox.com/docs/production/publishing/vr-guidelines) **[[scripting-and-performance]]** Limit CPU-heavy operations such as raycasting.
- [page](https://create.roblox.com/docs/production/publishing/vr-guidelines) **[[scripting-and-performance]]** Use RunService.Heartbeat rather than task.wait() for frame-precise updates.
- [page](https://create.roblox.com/docs/production/publishing/vr-guidelines) **[[building-art-and-assets]]** Mobile VR is sensitive to draw call count: add detail where it matters, use lower detail elsewhere, and keep object count in scenes conservative.
- [page](https://create.roblox.com/docs/production/publishing/vr-guidelines) **[[building-art-and-assets]]** Keep custom meshes low-geometry for runtime efficiency.
- [page](https://create.roblox.com/docs/production/publishing/vr-guidelines) **[[building-art-and-assets]]** Minimize semi-transparent objects, partially transparent Decals, and Glass material; they cost performance.
- [page](https://create.roblox.com/docs/production/publishing/vr-guidelines) **[[building-art-and-assets]]** Keep SurfaceGuis few and simple; numerous or complex ones are costly for rendering and CPU.
- [page](https://create.roblox.com/docs/production/publishing/vr-guidelines) **[[scripting-and-performance]]** Use InputAction instead of keyboard-specific code so input bindings work across multiple sources.
- [page](https://create.roblox.com/docs/production/publishing/vr-guidelines) **[[playtesting-and-feedback]]** Test and iterate often on a real Quest 2 headset to confirm performance and visual quality.

## Numbers
- [page](https://create.roblox.com/docs/production/publishing/vr-guidelines) Target frame rate: **72 FPS minimum (Auto Quality Mode on Quest)**
- [page](https://create.roblox.com/docs/production/publishing/vr-guidelines) Minimum GPU for Oculus drivers: **NVidia GTX 1060 or equivalent**

## Tools
OpenXR, Auto Quality Mode, CameraModule, InputAction, Quest 2

## He points to
- VR Menus and Settings

## Quotes
- [page](https://create.roblox.com/docs/production/publishing/vr-guidelines) "Mobile VR is sensitive to a high number of draw calls."
- [page](https://create.roblox.com/docs/production/publishing/vr-guidelines) "doing so opts your game out of future script updates and you'll need to manually merge changes"

## Topics
[[building-art-and-assets]] [[core-loops-and-game-design]] [[playtesting-and-feedback]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
