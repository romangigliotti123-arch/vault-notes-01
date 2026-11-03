---
title: "Docs: avatar / animation-packs"
url: https://create.roblox.com/docs/avatar/animation-packs.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: avatar / animation-packs

[Open](https://create.roblox.com/docs/avatar/animation-packs.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Official docs on creating and publishing Roblox avatar animation packs: the seven locomotion states, R15/CurveAnimation/looping requirements, clip upload and property setup, Parent model name grouping, validation rules, pricing floor and fees, and how packs apply in experiences.

## Tips
- [page](https://create.roblox.com/docs/avatar/animation-packs) **[[building-art-and-assets]]** Author all animation clips on a standard R15 Block Avatar rig so they play on every supported avatar appearance.
- [page](https://create.roblox.com/docs/avatar/animation-packs) **[[building-art-and-assets]]** Convert clips to CurveAnimation before saving; conversion is irreversible and may break some third-party animation plugins, so verify data first.
- [page](https://create.roblox.com/docs/avatar/animation-packs) **[[building-art-and-assets]]** Keep every clip except Jump looping; enable Loop in Properties under ServerStorage > RBX_ANIMSAVES > [rig].
- [page](https://create.roblox.com/docs/avatar/animation-packs) **[[building-art-and-assets]]** Trim clips to 10 seconds or less and keep body parts within 1.5 studs of their start position per frame, or validation fails.
- [page](https://create.roblox.com/docs/avatar/animation-packs) **[[building-art-and-assets]]** Use the identical Parent model name string on every clip in a pack, or Studio creates separate models and validation fails.
- [page](https://create.roblox.com/docs/avatar/animation-packs) **[[ugc-and-avatar-economy]]** Only original work is allowed; packs that reuse default Roblox animations fail validation.
- [page](https://create.roblox.com/docs/avatar/animation-packs) **[[ugc-and-avatar-economy]]** Limit uploads to one animation pack per day per creator; the upload fee is 80 Robux per pack.
- [page](https://create.roblox.com/docs/avatar/animation-packs) **[[pricing]]** Marketplace price floor for animation packs is 300 Robux; this is the minimum selling price, not an extra fee.
- [page](https://create.roblox.com/docs/avatar/animation-packs) **[[ugc-and-avatar-economy]]** Check that all seven state groups (Fall, Swim, Jump, Walk, Climb, Idle, Run) show Validation Succeeded before clicking Pay & Submit.

## Numbers
- [page](https://create.roblox.com/docs/avatar/animation-packs) Clip count per pack: **8 or 9 (Idle 1-2, Swim 2, other states 1 each)** (Complete animation pack clip count)
- [page](https://create.roblox.com/docs/avatar/animation-packs) Upload fee: **80 Robux per pack** (Charged on Studio pack submission)
- [page](https://create.roblox.com/docs/avatar/animation-packs) Marketplace price floor: **300 Robux** (Minimum selling price for animation packs)
- [page](https://create.roblox.com/docs/avatar/animation-packs) Uploads limit: **1 pack per day per creator** (Pack upload rate limit)
- [page](https://create.roblox.com/docs/avatar/animation-packs) Max clip duration: **10 seconds** (Validation fails above this length)
- [page](https://create.roblox.com/docs/avatar/animation-packs) Max body part translation: **1.5 studs per frame from starting position** (Spatial bounds validation limit)
- [page](https://create.roblox.com/docs/avatar/animation-packs) Idle weight default: **1 (positive integer, blank defaults to 1)** (Relative selection weight between up to two Idle clips)

## Tools
Roblox Studio Avatar tab (Rig Builder, Clip Editor), Animation Editor Curve Editor, Creator Dashboard

## He points to
- Publish to Marketplace docs
- Marketplace fees and commissions docs
- UGC validation system docs
- Curve Editor docs
- Avatar Settings docs

## Topics
[[building-art-and-assets]] [[pricing]] [[ugc-and-avatar-economy]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
