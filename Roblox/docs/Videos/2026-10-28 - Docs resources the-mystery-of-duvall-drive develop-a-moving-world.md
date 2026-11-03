---
title: "Docs: resources / the-mystery-of-duvall-drive / develop-a-moving-world"
url: https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/develop-a-moving-world.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: resources / the-mystery-of-duvall-drive / develop-a-moving-world

[Open](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/develop-a-moving-world.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox developer docs case study from The Mystery of Duvall Drive on building a moving world: storm clouds via TweenService and LocalScript rotation, scripted lightning beams synced to audio/post FX, skinned tree animations shared across rigs, particle rain/fog, and tweened door/wall movement. Covers when to use physics, tweens, animations and particles.

## Tips
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/develop-a-moving-world) **[[core-loops-and-game-design]]** Decide which movement tool fits by need: physics for interactables, TweenService for scripted motion, animations for shared motion, particles for ambient effects.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/develop-a-moving-world) **[[optimization-and-streaming]]** Skinned meshes are not instanced; each adds memory cost, so use them sparingly and check current rigging docs for updates.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/develop-a-moving-world) **[[client-server-and-remotes]]** Run purely cosmetic rotation in a LocalScript to reduce client-server bandwidth and allow smoother movement.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/develop-a-moving-world) **[[scripting-and-performance]]** Use one LocalScript handling all CollectionService-tagged instances instead of many scripts to maintain.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/develop-a-moving-world) **[[data-persistence]]** Handle streaming: queue objects on GetInstanceAddedSignal and initialize on later frames until values/PrimaryPart are replicated.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/develop-a-moving-world) **[[client-server-and-remotes]]** Send randomized FX parameters from server to all clients in one payload so every client sees identical lightning.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/develop-a-moving-world) **[[player-psychology-and-game-feel]]** Gate visual/audio effects client-side by player location (indoors, game state) so hidden players don't get FX.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/develop-a-moving-world) **[[scripting-and-performance]]** Use point-in-box checks over pre-placed volumes rather than touch events, since seated players stop touching volumes.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/develop-a-moving-world) **[[vfx-and-particles]]** Use SurfaceAppearance with semi-transparency on stacked, differently-speed meshes to fake volumetric clouds.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/develop-a-moving-world) **[[optimization-and-streaming]]** Avoid forcing many large objects to stream in; it can negate streaming benefits. Use sparingly.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/develop-a-moving-world) **[[building-art-and-assets]]** Set final scene lighting early to see which surface details are actually visible and skip the rest.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/develop-a-moving-world) **[[building-art-and-assets]]** Bake high-poly sculpt normal maps onto low-poly spheres to keep detail without performance cost.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/develop-a-moving-world) **[[vfx-and-particles]]** Increase ParticleEmitter Size when raising Squash, or stretched particles become too thin.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/develop-a-moving-world) **[[vfx-and-particles]]** Use several same-size particle volumes in a grid for heavy rain rather than one emitter over the whole area.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/develop-a-moving-world) **[[3d-modeling-rigging-and-animation]]** Use generic joint names across rigs so one animation can be reused on different tree models.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/develop-a-moving-world) **[[3d-modeling-rigging-and-animation]]** Build secondary motion (primary, secondary, tertiary joints) so trunks, branches and leaves react with delay.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/develop-a-moving-world) **[[building-and-level-design]]** Use a generic tweened door/wall script driven by target parts and a trigger volume to reuse one script across many moving objects.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/develop-a-moving-world) **[[common-mistakes]]** Beams cannot be synced to audio via particle systems alone; script the timing when no sequencer exists in Studio.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/develop-a-moving-world) **[[ui-ux-design]]** Don't model detail players can't see; a distant image on a decal can convey depth cheaply.

## Numbers
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/develop-a-moving-world) Random lightning interval: **3.0 to 10.0 seconds** (Server waits random time between hero lightning strikes)
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/develop-a-moving-world) Squash example values: **3 and 20** (Squash 3 stretches slightly; 20 stretches much longer, needs larger Size)
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/develop-a-moving-world) Legacy rotation value scale: **12x** (Previous rotation system values differed by factor of 12)
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/develop-a-moving-world) Beam brightness at wipe: **10** (Lightning wipe sets beam brightness to 10 before tweening down)

## Games
- **The Mystery of Duvall Drive**: Storm built from layered semi-transparent cloud meshes, scripted lightning, animated trees and particle rain; movement serves atmosphere and hides detail.
- **The Mystery of Duvall Drive (expanding pantry)**: Corrupt-space pantry walls move via TweenService on trigger volume entry to create nightmare-like disorientation.

## Tools
TweenService, LocalScript, CollectionService, Animation Editor, Blender, Substance Painter, ParticleEmitter, Beam

## He points to
- Roblox Creator Docs: rigging and skinning documentation

## Topics
[[3d-modeling-rigging-and-animation]] [[building-and-level-design]] [[building-art-and-assets]] [[client-server-and-remotes]] [[common-mistakes]] [[core-loops-and-game-design]] [[data-persistence]] [[optimization-and-streaming]] [[player-psychology-and-game-feel]] [[scripting-and-performance]] [[ui-ux-design]] [[vfx-and-particles]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
