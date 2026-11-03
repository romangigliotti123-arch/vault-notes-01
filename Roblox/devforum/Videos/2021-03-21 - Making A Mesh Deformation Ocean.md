---
title: "Making A Mesh Deformation Ocean"
url: https://devforum.roblox.com/t/making-a-mesh-deformation-ocean/1122587
creator: Roblox DevForum
official: false
advice_density: medium
date: 2021-03-21
views: 428
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Making A Mesh Deformation Ocean

[Open](https://devforum.roblox.com/t/making-a-mesh-deformation-ocean/1122587) | Roblox DevForum | 428 views | 2021-03-21

## Summary
Tutorial on building a deformable mesh ocean in Roblox: create a subdivided plane, auto-rig each vertex to a bone via a Blender Python script, export FBX, import with the avatar importer as a Custom rig, then animate bones with a Gerstner wave formula on the client with synchronized time.

## Tips
- [page](https://devforum.roblox.com/t/making-a-mesh-deformation-ocean/1122587) **[[building-art-and-assets]]** Balance ocean mesh resolution against performance; the author's ~8k tris worked but was at the edge of performant.
- [page](https://devforum.roblox.com/t/making-a-mesh-deformation-ocean/1122587) **[[building-art-and-assets]]** Scale up the plane's UVs before export so textures repeat more and look smaller/clearer.
- [page](https://devforum.roblox.com/t/making-a-mesh-deformation-ocean/1122587) **[[3d-modeling-rigging-and-animation]]** Use the avatar importer plugin with the Custom rig option to import an FBX mesh with bones already set up.
- [page](https://devforum.roblox.com/t/making-a-mesh-deformation-ocean/1122587) **[[physics-pathfinding-and-npc-ai]]** Run wave formula calculations on the client; running them on the server is jittery and slows the server down.
- [page](https://devforum.roblox.com/t/making-a-mesh-deformation-ocean/1122587) **[[client-server-and-remotes]]** Synchronize the time variable across clients with a client/server clock synchronizer so waves match for everyone.
- [page](https://devforum.roblox.com/t/making-a-mesh-deformation-ocean/1122587) **[[optimization-and-streaming]]** Offset the time value by a small amount (e.g. C+/-1) to compensate for lag or travel time of body positions.
- [page](https://devforum.roblox.com/t/making-a-mesh-deformation-ocean/1122587) **[[common-mistakes]]** Deformable mesh water has no collisions and does not respond to raycasts; plan gameplay interaction around this.

## Numbers
- [page](https://devforum.roblox.com/t/making-a-mesh-deformation-ocean/1122587) triangle count: **~8k tris** (Plane subdivision level author found workable but at performance edge)
- [page](https://devforum.roblox.com/t/making-a-mesh-deformation-ocean/1122587) bones created: **~4k** (One bone per vertex after rigging script ran in Blender)

## Tools
Blender, Blender Python script (bone-per-vertex rigging), Roblox Studio avatar importer plugin, FBX export, Gerstner wave formula

## He points to
- Post on wave equation and scripting (linked by author, not named)
- FBXImportGeneric - Roblox (DevForum/docs link)

## Topics
[[3d-modeling-rigging-and-animation]] [[building-art-and-assets]] [[client-server-and-remotes]] [[common-mistakes]] [[optimization-and-streaming]] [[physics-pathfinding-and-npc-ai]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
