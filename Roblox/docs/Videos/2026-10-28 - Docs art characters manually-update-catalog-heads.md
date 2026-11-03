---
title: "Docs: art / characters / manually-update-catalog-heads"
url: https://create.roblox.com/docs/art/characters/manually-update-catalog-heads.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: art / characters / manually-update-catalog-heads

[Open](https://create.roblox.com/docs/art/characters/manually-update-catalog-heads.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs on manually fixing catalog heads that fail the updated dynamic head validation. Covers re-validating via a glTF export script, fixing the cage/rig/animation in Blender using Roblox cage templates, re-uploading as a Development Item, and submitting the new asset ID via the web form.

## Tips
- [page](https://create.roblox.com/docs/art/characters/manually-update-catalog-heads) **[[updates-live-ops]]** If a catalog head fails dynamic head validation, fix and reupload it; body bundle owners only need to update the head asset, not the body.
- [page](https://create.roblox.com/docs/art/characters/manually-update-catalog-heads) **[[building-art-and-assets]]** Delete the original cage and use a Roblox-provided cage template matching the head shape instead of editing the broken cage; this is usually faster.
- [page](https://create.roblox.com/docs/art/characters/manually-update-catalog-heads) **[[3d-modeling-rigging-and-animation]]** Disable 'Guess Original Bind Pose' on glTF import in Blender; rotate the asset 180 degrees on Z because Studio flips avatars on import.
- [page](https://create.roblox.com/docs/art/characters/manually-update-catalog-heads) **[[3d-modeling-rigging-and-animation]]** Heads must have a rig with FACS-mapped poses: eyes blink, mouth opens and closes, face expresses happy and sad.
- [page](https://create.roblox.com/docs/art/characters/manually-update-catalog-heads) **[[3d-modeling-rigging-and-animation]]** Remove vertex colors and vertex color shading nodes, and set the Blender animation start value to 0, before export.
- [page](https://create.roblox.com/docs/art/characters/manually-update-catalog-heads) **[[3d-modeling-rigging-and-animation]]** For FBX export, save each glTF-imported texture image to disk locally first, since Blender cannot export those textures to FBX by default.
- [page](https://create.roblox.com/docs/art/characters/manually-update-catalog-heads) **[[testing-debugging-and-qa]]** Verify validation by using Save to Roblox > Avatar Item > Head, then cancel the publish to avoid fees.
- [page](https://create.roblox.com/docs/art/characters/manually-update-catalog-heads) **[[updates-live-ops]]** Publish the fixed head as a Development Item (Model category, Public privacy), which carries no publishing fee; then submit the asset ID via the web form. Only your last submission counts.

## Numbers
- [page](https://create.roblox.com/docs/art/characters/manually-update-catalog-heads) Update workflow steps: **5** (Re-validate, export glTF, fix in Blender, import and validate, submit asset ID)
- [page](https://create.roblox.com/docs/art/characters/manually-update-catalog-heads) Publish fee on dev item save: **none** (Saving as Development Item incurs no publishing fees; avatar validation tests must be cancelled)

## Tools
Roblox Studio, glTF Export beta feature, Blender, FBX export, Roblox head cage templates

## He points to
- Dynamic head overview
- Head validation process
- Head validation video guide
- Avatar Setup
- Caging Best Practices

## Topics
[[3d-modeling-rigging-and-animation]] [[building-art-and-assets]] [[testing-debugging-and-qa]] [[updates-live-ops]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
