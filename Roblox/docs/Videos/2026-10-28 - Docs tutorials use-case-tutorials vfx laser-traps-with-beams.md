---
title: "Docs: tutorials / use-case-tutorials / vfx / laser-traps-with-beams"
url: https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/laser-traps-with-beams.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / use-case-tutorials / vfx / laser-traps-with-beams

[Open](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/laser-traps-with-beams.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs tutorial on building a laser beam blaster with Beam objects. Covers an invisible anchored CollisionBox with Touched detection, StartAttachment/EndAttachment for beam reach, Beam appearance properties (texture, color, LightEmission, width, TextureSpeed, FaceCamera), and a short script setting Humanoid.Health to 0 on touch.

## Tips
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/laser-traps-with-beams) **[[vfx-and-particles]]** Beam objects have no collision; pair them with an invisible anchored basic part and use its Touched event for detection.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/laser-traps-with-beams) **[[vfx-and-particles]]** Beams need two Attachments to render; without Attachment0 and Attachment1 the beam cannot function at all.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/laser-traps-with-beams) **[[vfx-and-particles]]** Set beam Width0 and Width1, TextureSpeed, LightEmission (e.g. 0.5 for faint glow) and enable FaceCamera so the beam is visible from any angle.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/laser-traps-with-beams) **[[vfx-and-particles]]** Make the collision part fully transparent (Transparency 1) so the beam texture is not obstructed.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/laser-traps-with-beams) **[[scripting-and-performance]]** Check for a Humanoid via FindFirstChildWhichIsA before modifying a touched part's character to avoid errors on non-character parts.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/laser-traps-with-beams) **[[building-art-and-assets]]** Reuse assets from your inventory via Toolbox Inventory tab after clicking Get Model on the Creator Store page.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/laser-traps-with-beams) **[[common-mistakes]]** Scripts and parts must match exact names (e.g. CollisionBox, script parented to the blaster model) or the trap silently fails.

## Numbers
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/laser-traps-with-beams) Beam Color: **255, 47, 137** (bright pink laser tint in tutorial)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/laser-traps-with-beams) LightEmission: **0.5** (faint glow setting)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/laser-traps-with-beams) Width0 / Width1: **4** (widened laser beam)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/laser-traps-with-beams) TextureSpeed: **2** (faster animation of laser texture)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/laser-traps-with-beams) Transparency: **1** (fully invisible collision box)

## Tools
Roblox Studio, Toolbox, Creator Store, Beam, Attachment, Script

## He points to
- Beams documentation
- Exporting Requirements

## Topics
[[building-art-and-assets]] [[common-mistakes]] [[scripting-and-performance]] [[vfx-and-particles]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
