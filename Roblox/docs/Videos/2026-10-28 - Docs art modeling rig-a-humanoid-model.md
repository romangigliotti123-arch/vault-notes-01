---
title: "Docs: art / modeling / rig-a-humanoid-model"
url: https://create.roblox.com/docs/art/modeling/rig-a-humanoid-model.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: art / modeling / rig-a-humanoid-model

[Open](https://create.roblox.com/docs/art/modeling/rig-a-humanoid-model.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs guide on rigging an R15 humanoid model in Blender: importing a Lola reference model into a template, positioning bones symmetrically with X-Axis Mirror, parenting 15 meshes to an armature with empty groups, and assigning full vertex-group influence per mesh before skinning and testing in Pose mode.

## Tips
- [page](https://create.roblox.com/docs/art/modeling/rig-a-humanoid-model) **[[3d-modeling-rigging-and-animation]]** Enable X-Axis Mirror when editing bones so left and right bones stay symmetrical; asymmetry causes posing and animation issues.
- [page](https://create.roblox.com/docs/art/modeling/rig-a-humanoid-model) **[[3d-modeling-rigging-and-animation]]** Follow Studio's standard R15 bone hierarchy and naming conventions; modified or new bone structures must match them.
- [page](https://create.roblox.com/docs/art/modeling/rig-a-humanoid-model) **[[3d-modeling-rigging-and-animation]]** Center each bone within its corresponding mesh (e.g. Head bone inside Head_Geo) and verify with perspective views.
- [page](https://create.roblox.com/docs/art/modeling/rig-a-humanoid-model) **[[3d-modeling-rigging-and-animation]]** Do not assign influences to the Root or HumanoidRootNode bones; any added influences are dropped on import into Studio.
- [page](https://create.roblox.com/docs/art/modeling/rig-a-humanoid-model) **[[3d-modeling-rigging-and-animation]]** Assign each limb mesh's vertices fully to one corresponding bone before skinning; test in Pose mode after any influence change.
- [page](https://create.roblox.com/docs/art/modeling/rig-a-humanoid-model) **[[3d-modeling-rigging-and-animation]]** Expect to revisit bone positions after weight painting if a pose or animation does not work as intended.
- [page](https://create.roblox.com/docs/art/modeling/rig-a-humanoid-model) **[[3d-modeling-rigging-and-animation]]** Ensure the character model follows Studio's Avatar character specifications before rigging.

## Numbers
- [page](https://create.roblox.com/docs/art/modeling/rig-a-humanoid-model) R15 mesh objects per humanoid: **15**
- [page](https://create.roblox.com/docs/art/modeling/rig-a-humanoid-model) Blender version used in guide: **3.0**

## Tools
Blender, Rig_and_Attachments_Template.blend, Roblox Studio

## He points to
- Skin a humanoid model (Roblox docs)

## Topics
[[3d-modeling-rigging-and-animation]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
