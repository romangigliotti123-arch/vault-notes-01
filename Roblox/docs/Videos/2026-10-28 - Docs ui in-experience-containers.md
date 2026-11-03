---
title: "Docs: ui / in-experience-containers"
url: https://create.roblox.com/docs/ui/in-experience-containers.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: ui / in-experience-containers

[Open](https://create.roblox.com/docs/ui/in-experience-containers.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox official docs on in-experience UI containers: SurfaceGui renders UI onto a part face and accepts input when placed in StarterGui with CanQuery true. BillboardGui always faces the camera and suits name tags, health bars and markers. Covers Adornee, scale sizing, AlwaysOnTop, Brightness/LightInfluence and MaxDistance.

## Tips
- [page](https://create.roblox.com/docs/ui/in-experience-containers) **[[ui-ux-design]]** Use scale values (not offset) for size and position of SurfaceGui child objects so they fit the face regardless of its size.
- [page](https://create.roblox.com/docs/ui/in-experience-containers) **[[ui-ux-design]]** Place interactive SurfaceGui and BillboardGui containers inside StarterGui; buttons only receive input when parented to PlayerGui.
- [page](https://create.roblox.com/docs/ui/in-experience-containers) **[[ui-ux-design]]** Set the part's CanQuery to true, or interactive UI elements on a SurfaceGui will not receive input.
- [page](https://create.roblox.com/docs/ui/in-experience-containers) **[[building-art-and-assets]]** Use Show Orientation Indicator (right-click part) to pick the correct SurfaceGui Face before building.
- [page](https://create.roblox.com/docs/ui/in-experience-containers) **[[ui-ux-design]]** Add UIAspectRatioConstraint to SurfaceGui children to keep their aspect ratio across face sizes.
- [page](https://create.roblox.com/docs/ui/in-experience-containers) **[[ui-ux-design]]** Enable TextScaled on TextLabels inside a sized BillboardGui so text scales with camera distance.
- [page](https://create.roblox.com/docs/ui/in-experience-containers) **[[ui-ux-design]]** Set Adornee from a script at runtime to attach a BillboardGui to player characters or other dynamic parts.
- [page](https://create.roblox.com/docs/ui/in-experience-containers) **[[optimization-and-streaming]]** Set MaxDistance high enough for outdoor SurfaceGuis so pop-in and pop-out is less noticeable; default 1000 suits most cases.
- [page](https://create.roblox.com/docs/ui/in-experience-containers) **[[ui-ux-design]]** Use ZOffset to order multiple SurfaceGuis on the same face; ZOffset does not visually move the container off the surface.
- [page](https://create.roblox.com/docs/ui/in-experience-containers) **[[ui-ux-design]]** Brightness has no effect when LightInfluence is 1 or AlwaysOnTop is true; lower LightInfluence and raise Brightness (e.g. 10) for dark rooms.

## Numbers
- [page](https://create.roblox.com/docs/ui/in-experience-containers) SurfaceGui MaxDistance default: **1000 (0 = unlimited)** (Distance before SurfaceGui stops rendering)
- [page](https://create.roblox.com/docs/ui/in-experience-containers) Brightness range: **0 to 1000 (example 10)** (Scales emitted light on SurfaceGui and BillboardGui)
- [page](https://create.roblox.com/docs/ui/in-experience-containers) LightInfluence range: **0 to 1** (0 = lighting has no effect; 1 = full lighting control)
- [page](https://create.roblox.com/docs/ui/in-experience-containers) BillboardGui Size example: **UDim2.fromScale(10, 2) = 10:2 aspect** (Scale components set stud size in 3D space)
- [page](https://create.roblox.com/docs/ui/in-experience-containers) BillboardGui MaxDistance default: **inf (0 also unlimited)** (Distance before billboard stops rendering)

## Tools
Roblox Studio, Show Orientation Indicator

## He points to
- Roblox Creator Docs: In-game UI containers

## Topics
[[building-art-and-assets]] [[optimization-and-streaming]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
