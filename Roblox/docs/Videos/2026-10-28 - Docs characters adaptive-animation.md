---
title: "Docs: characters / adaptive-animation"
url: https://create.roblox.com/docs/characters/adaptive-animation.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: characters / adaptive-animation

[Open](https://create.roblox.com/docs/characters/adaptive-animation.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on Adaptive Animation: importing custom rigs as Custom Humanoid, creating HumanoidRigDescription and DigitsRigDescription objects, assigning the 15 required joints via the joint assignment tool, and building a T-pose baseline so custom characters can play R15 and compatible published animations.

## Tips
- [page](https://create.roblox.com/docs/characters/adaptive-animation) **[[building-art-and-assets]]** Import custom characters via 3D Importer with Rig Type set to Custom, then click Create in Remap Rig panel to generate HumanoidRigDescription and per-hand DigitsRigDescription objects.
- [page](https://create.roblox.com/docs/characters/adaptive-animation) **[[3d-modeling-rigging-and-animation]]** Map at least 15 character joints to Roblox's standard 15-joint skeleton; unassigned required joints show grey and block compatibility.
- [page](https://create.roblox.com/docs/characters/adaptive-animation) **[[3d-modeling-rigging-and-animation]]** Assign optional extra joints (in hands via DigitsRigDescription) when the rig supports them to improve animation quality.
- [page](https://create.roblox.com/docs/characters/adaptive-animation) **[[3d-modeling-rigging-and-animation]]** Set a standard T-pose baseline using Enforce T-pose, then fine-tune with symmetry and Rotate tools, for universal animation support.
- [page](https://create.roblox.com/docs/characters/adaptive-animation) **[[testing-debugging-and-qa]]** Test the rig's T-pose by playing an animation from the Adaptive Animation toolbar dropdown; remap or re-pose if it deforms incorrectly.

## Numbers
- [page](https://create.roblox.com/docs/characters/adaptive-animation) Required joints for standard skeleton: **15** (Minimum joints that must map to Roblox's standardized 15-joint skeleton)

## Tools
Studio 3D Importer, Adaptive Animation toolbar, Joint assignment tool, T-pose mode, Remap Rig panel

## He points to
- Class.HumanoidRigDescription
- Class.DigitsRigDescription
- Blender Studio Snow character

## Topics
[[3d-modeling-rigging-and-animation]] [[building-art-and-assets]] [[testing-debugging-and-qa]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
