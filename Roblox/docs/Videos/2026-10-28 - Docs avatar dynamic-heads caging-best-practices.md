---
title: "Docs: avatar / dynamic-heads / caging-best-practices"
url: https://create.roblox.com/docs/avatar/dynamic-heads/caging-best-practices.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: avatar / dynamic-heads / caging-best-practices

[Open](https://create.roblox.com/docs/avatar/dynamic-heads/caging-best-practices.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on best practices for caging dynamic character heads (face, eyes, eyebrows, mouth, nose, ears, hairline, neck). Focuses on geometry alignment so Marketplace accessories, makeup transfer and Hidden Surface Removal work correctly.

## Tips
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/caging-best-practices) **[[building-art-and-assets]]** Keep cage geometry equidistant where possible to reduce texture and layered accessory distortion; note this isn't always achievable.
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/caging-best-practices) **[[building-art-and-assets]]** Align vertex-colored areas to lips, eyebrows and hairline so makeup transfer and hair/facial hair/eyelash accessories fit correctly.
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/caging-best-practices) **[[building-art-and-assets]]** Align non-vertex-colored areas (nose, eyes, ears) carefully for accurate makeup transfer and accessory fit.
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/caging-best-practices) **[[building-art-and-assets]]** Keep the cage middle axis at origin when possible for consistency.
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/caging-best-practices) **[[building-art-and-assets]]** Line neck cage parts up close to render mesh so Hidden Surface Removal hides the underlying surface under layered accessories; HSR is disabled on head but not body.
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/caging-best-practices) **[[building-art-and-assets]]** Make the cage barely cover the render mesh without intersecting it; close fit improves layered accessory fit and makeup accuracy.
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/caging-best-practices) **[[building-art-and-assets]]** For eyes, use three verts on upper eyelid and three on lower eyelid, equidistant, and enclose the open eye edge up to the eye mesh.
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/caging-best-practices) **[[building-art-and-assets]]** For eyebrows, establish head and tail first, then place three upper and three lower verts equidistant.
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/caging-best-practices) **[[building-art-and-assets]]** For missing eyebrows, use facial proportion rules and adjust for stylization and face shape.
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/caging-best-practices) **[[building-art-and-assets]]** Outline lips inside and outside; upper lip on green vertex color, lower lip on purple, equidistant spacing.
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/caging-best-practices) **[[building-art-and-assets]]** Start the nose bridge at inner eyes and end two faces above the lips.
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/caging-best-practices) **[[building-art-and-assets]]** For ears, use the triangle portion for the top and the quad for the bottom; keep hairline shape around the ear.
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/caging-best-practices) **[[building-art-and-assets]]** For sideburns, define shape in front of and around ears and decide where hairline ends at neck base to guide layered hair fit.
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/caging-best-practices) **[[building-art-and-assets]]** For faces missing features, use proportion guides: face thirds (hairline-brows, brows-nose bottom, nose bottom-chin), eyes halfway down head, head about five eyes wide, pupils aligned with mouth corners.

## Numbers
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/caging-best-practices) Eyelid vertex count: **3 upper + 3 lower verts per eye** (Equidistant eyelid verts in dynamic head cage)
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/caging-best-practices) Eyebrow vertex count: **3 upper + 3 lower verts** (Placed equidistant between established head and tail)
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/caging-best-practices) Nose bridge end: **two faces above the lips** (Nose bridge runs from inner eyes to two faces above lips)
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/caging-best-practices) Head proportion: **about five eyes wide** (Guideline for faces missing major features)
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/caging-best-practices) Face vertical thirds: **three equal parts** (Hairline-to-brows, brows-to-nose bottom, nose bottom-to-chin)

## Tools
Roblox dynamic head template (vertex-colored cage), Hidden Surface Removal (HSR), Auto-setup for neck cage

## He points to
- Layered accessory caging best practices

## Topics
[[building-art-and-assets]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
