---
title: "Creating custom skyboxes using Blender & crafting stunning atmospheres"
url: https://devforum.roblox.com/t/creating-custom-skyboxes-using-blender-crafting-stunning-atmospheres/3134324
creator: Roblox DevForum
official: false
advice_density: medium
date: 2024-08-25
views: 47
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Creating custom skyboxes using Blender & crafting stunning atmospheres

[Open](https://devforum.roblox.com/t/creating-custom-skyboxes-using-blender-crafting-stunning-atmospheres/3134324) | Roblox DevForum | 47 views | 2024-08-25

## Summary
Tutorial on building a custom Roblox skybox in Blender: six-camera cubemap rendering at 90° FOV, color-ramp gradient, importing into Sky object, then adding dynamic Clouds (under Terrain) with an Atmosphere for visibility and GlobalWind for scroll speed.

## Tips
- [page](https://devforum.roblox.com/t/creating-custom-skyboxes-using-blender-crafting-stunning-atmospheres/3134324) **[[vfx-and-particles]]** Pair Roblox Clouds with an Atmosphere object in Lighting; without it clouds render very faintly.
- [page](https://devforum.roblox.com/t/creating-custom-skyboxes-using-blender-crafting-stunning-atmospheres/3134324) **[[building-art-and-assets]]** Render skybox images square at 1024 or 2048px; non-square images will not work.
- [page](https://devforum.roblox.com/t/creating-custom-skyboxes-using-blender-crafting-stunning-atmospheres/3134324) **[[building-art-and-assets]]** For a simple gradient skybox, render only Top, Bottom and Front views; Front is reused for Back, Left and Right.
- [page](https://devforum.roblox.com/t/creating-custom-skyboxes-using-blender-crafting-stunning-atmospheres/3134324) **[[building-art-and-assets]]** Set Blender View Transform to Standard under Color Management, otherwise skybox colours render darker or greyish.
- [page](https://devforum.roblox.com/t/creating-custom-skyboxes-using-blender-crafting-stunning-atmospheres/3134324) **[[building-art-and-assets]]** Name rendered skybox images by direction (e.g. Skybox_Name_Front) to simplify assigning them to Sky properties.
- [page](https://devforum.roblox.com/t/creating-custom-skyboxes-using-blender-crafting-stunning-atmospheres/3134324) **[[vfx-and-particles]]** Increase Atmosphere Haze and Glare and lower ClockTime so the sun sits low for bloom-like sunset skies.
- [page](https://devforum.roblox.com/t/creating-custom-skyboxes-using-blender-crafting-stunning-atmospheres/3134324) **[[vfx-and-particles]]** Raise EnvironmentalDiffuseScale and EnvironmentalSpecularScale in Lighting so skybox colours tint the environment.
- [page](https://devforum.roblox.com/t/creating-custom-skyboxes-using-blender-crafting-stunning-atmospheres/3134324) **[[vfx-and-particles]]** Use Workspace.GlobalWind to control how fast Roblox Clouds scroll across the sky.
- [page](https://devforum.roblox.com/t/creating-custom-skyboxes-using-blender-crafting-stunning-atmospheres/3134324) **[[sound-and-music]]** Clouds must be inserted directly under Workspace.Terrain; they do not work elsewhere in the hierarchy.

## Numbers
- [page](https://devforum.roblox.com/t/creating-custom-skyboxes-using-blender-crafting-stunning-atmospheres/3134324) Camera field of view for cubemap render: **90°** (Six Blender cameras, each rotated 90°, needed for seamless skybox stitching)
- [page](https://devforum.roblox.com/t/creating-custom-skyboxes-using-blender-crafting-stunning-atmospheres/3134324) Recommended skybox render resolution: **1024 or 2048 px, square** (Blender Output tab resolution for skybox images)
- [page](https://devforum.roblox.com/t/creating-custom-skyboxes-using-blender-crafting-stunning-atmospheres/3134324) Images needed for gradient skybox: **3 (Top, Bottom, Front)** (Front reused for back, left and right when horizon is uniform)

## Tools
Blender, Roblox Studio, Sky object, Atmosphere object, Clouds object

## He points to
- Skybox_Generating.blend template file
- CustomSkyboxExample.rbxl demo place

## Topics
[[building-art-and-assets]] [[sound-and-music]] [[vfx-and-particles]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
