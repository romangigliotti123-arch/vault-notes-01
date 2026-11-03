---
title: "Blender rig exporter/animation importer"
url: https://devforum.roblox.com/t/blender-rig-exporteranimation-importer/34729
creator: Roblox DevForum
official: false
advice_density: medium
date: 2017-03-30
views: 5001
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Blender rig exporter/animation importer

[Open](https://devforum.roblox.com/t/blender-rig-exporteranimation-importer/34729) | Roblox DevForum | 5,001 views | 2017-03-30

## Summary
Developer Den_S announces a Roblox plugin plus Blender addon that exports any Roblox rig to Blender as an equivalent armature, lets animators keyframe in Blender (including IK), and re-exports the animation as Roblox animation data. Covers install, workflow, FBX/Mixamo import, bone mapping, and sampling parameters. Skinned meshes are unsupported.

## Tips
- [page](https://devforum.roblox.com/t/blender-rig-exporteranimation-importer/34729) **[[ai-and-tools]]** Use the latest plugin and addon versions; incompatible versions cause errors. An error mentioning object.name = partnames[-index] means the addon is outdated.
- [page](https://devforum.roblox.com/t/blender-rig-exporteranimation-importer/34729) **[[ai-and-tools]]** Check that the rig shows no warnings in the exporter plugin, and that it loads in the default Roblox Animation Editor, which gives clearer error messages.
- [page](https://devforum.roblox.com/t/blender-rig-exporteranimation-importer/34729) **[[building-and-level-design]]** Make rig Motor6Ds direct children of the parent part (typically Part0); otherwise the plugin may fail to find the joint.
- [page](https://devforum.roblox.com/t/blender-rig-exporteranimation-importer/34729) **[[3d-modeling-rigging-and-animation]]** Skinned meshes and bones are not supported; for skinned mesh animation use the built-in .fbx animation importer instead.
- [page](https://devforum.roblox.com/t/blender-rig-exporteranimation-importer/34729) **[[3d-modeling-rigging-and-animation]]** For high-quality animation, use frame step 1 at 30 fps. Frame step 2-5 often gives smoother results, depending on the animation.
- [page](https://devforum.roblox.com/t/blender-rig-exporteranimation-importer/34729) **[[3d-modeling-rigging-and-animation]]** Keep the generated __Rig armature when exporting to other tools; replacing it loses metadata. Map external armatures onto it by bone name instead.
- [page](https://devforum.roblox.com/t/blender-rig-exporteranimation-importer/34729) **[[3d-modeling-rigging-and-animation]]** Before mapping keyframes by bone name, set the scene frame range first; only frames inside the range are mapped.
- [page](https://devforum.roblox.com/t/blender-rig-exporteranimation-importer/34729) **[[3d-modeling-rigging-and-animation]]** Use the Create IK constraints tool in Pose mode by selecting end-of-chain bones (feet, hands); tune constraint parameters afterward.
- [page](https://devforum.roblox.com/t/blender-rig-exporteranimation-importer/34729) **[[3d-modeling-rigging-and-animation]]** Mixamo/FBX animations can be imported with the Import FBX button; the rig must contain one armature with animation data.
- [page](https://devforum.roblox.com/t/blender-rig-exporteranimation-importer/34729) **[[building-art-and-assets]]** Humanoid clothing is not auto-imported; export an OBJ from Studio and link meshes to the generated bones manually if needed.

## Numbers
- [page](https://devforum.roblox.com/t/blender-rig-exporteranimation-importer/34729) Recommended frame step: **1 at 30 fps (high quality); 2-5 for smoother** (Blender animation export sampling parameters)
- [page](https://devforum.roblox.com/t/blender-rig-exporteranimation-importer/34729) Post likes: **5001** (Den_S post on DevForum)

## Tools
Blender 2.80+ (addon), Blender 2.79 (legacy, no longer maintained), Roblox Animation Editor, Roblox Blender rig exporter/animation importer plugin, Mixamo

## He points to
- Santa_Root Blender tutorial video (Blender 2.97)
- XAXA modified addon for R15 constraints (Blender 2.79)

## Topics
[[3d-modeling-rigging-and-animation]] [[ai-and-tools]] [[building-and-level-design]] [[building-art-and-assets]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
