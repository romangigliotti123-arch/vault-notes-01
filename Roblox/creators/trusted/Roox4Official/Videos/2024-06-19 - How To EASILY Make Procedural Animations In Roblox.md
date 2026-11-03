---
title: "How To EASILY Make Procedural Animations In Roblox"
url: https://youtu.be/DPpAsjUr278
creator: Roox4
official: false
advice_density: low
date: 2024-06-19
views: 347550
transcript: auto-captions
confidence: high
tags: [roblox, roox4official, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.1
---

> [!note] Trust: TRUSTED (credibility audit score 8.1): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# How To EASILY Make Procedural Animations In Roblox

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Watch](https://youtu.be/DPpAsjUr278) | Roox4Official | 347,550 views | 2024-06-19

## Summary
Four-step tutorial for procedural (IK-based) leg animation in Roblox: prep the model with humanoid root and non-colliding leg parts, rig joints with the Rig Edit plugin, set up IK controls with targets, raycast parts and pole attachments, then call a downloadable module's IK step function. Adds an AlignOrientation secret so the body tilts on terrain.

## Tips
- [0:15](https://youtu.be/DPpAsjUr278?t=15) **[[building-art-and-assets]]** Name all parts uniquely, put animated parts in one folder, and set CanCollide to false on them so they don't interfere with other physics.
- [0:58](https://youtu.be/DPpAsjUr278?t=58) **[[3d-modeling-rigging-and-animation]]** Rig parts in Studio with the free Rig Edit plugin: select parent then child part and press Create Joints, then move joint pivots to the rotation point.
- [2:21](https://youtu.be/DPpAsjUr278?t=141) **[[3d-modeling-rigging-and-animation]]** Lower Rig Edit step value gives more precise joint movement; tune it per model and test joints in the animation editor before continuing.
- [2:44](https://youtu.be/DPpAsjUr278?t=164) **[[scripting-and-performance]]** Set IK target parts to CanCollide, CanTouch and CanQuery off and Massless on; weld raycast parts to HumanoidRootPart and keep them unanchored.

## Numbers
- [2:44](https://youtu.be/DPpAsjUr278?t=164) IK controls: **one per leg (example model had 4)** (Creator's example model used four legs)
- [0:58](https://youtu.be/DPpAsjUr278?t=58) Rig Edit step value: **25 recommended starting point** (Suggested initial setting in the Rig Edit plugin)

## Tools
Roblox Studio, Rig Edit plugin (free), Animation editor, Procedural animation module (creator's download)

## Topics
[[3d-modeling-rigging-and-animation]] [[building-art-and-assets]] [[physics-pathfinding-and-npc-ai]] [[scripting-and-performance]]

Back to [[Roox4Official - How to make successful Roblox games]]
