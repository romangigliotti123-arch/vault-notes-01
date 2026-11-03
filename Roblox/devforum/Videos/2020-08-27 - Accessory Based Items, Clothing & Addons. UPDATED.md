---
title: "Accessory Based Items, Clothing & Addons. [UPDATED]"
url: https://devforum.roblox.com/t/accessory-based-items-clothing-addons-updated/744207
creator: Roblox DevForum
official: false
advice_density: medium
date: 2020-08-27
views: 200
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Accessory Based Items, Clothing & Addons. [UPDATED]

[Open](https://devforum.roblox.com/t/accessory-based-items-clothing-addons-updated/744207) | Roblox DevForum | 200 views | 2020-08-27

## Summary
Tutorial on attaching 3D models to Roblox characters. Covers static accessories (Accessory objects welded via Attachments, added with Humanoid:AddAccessory) and dynamic "pseudo-accessories" (Model plus Motor6D) that can be animated alongside the character. Includes setup checklists, attachment matching rules and a helper function.

## Tips
- [page](https://devforum.roblox.com/t/accessory-based-items-clothing-addons-updated/744207) **[[3d-modeling-rigging-and-animation]]** Use static Accessories (welds) for clothing and addons that never move; use Model plus Motor6D for weapons you animate with the character, like a gripped spear or spinning knife.
- [page](https://devforum.roblox.com/t/accessory-based-items-clothing-addons-updated/744207) **[[building-art-and-assets]]** Before converting a model to an accessory: weld all parts together, unanchor them, turn off collisions, name one part Handle, and add an Attachment inside the Handle.
- [page](https://devforum.roblox.com/t/accessory-based-items-clothing-addons-updated/744207) **[[common-mistakes]]** Attachment names must match exactly between Handle and body part. Mismatched names fail to weld, or attach to the wrong attachment.
- [page](https://devforum.roblox.com/t/accessory-based-items-clothing-addons-updated/744207) **[[common-mistakes]]** Do not give multiple attachments the same name; results may be unsatisfactory. Use concise, meaningful names.
- [page](https://devforum.roblox.com/t/accessory-based-items-clothing-addons-updated/744207) **[[3d-modeling-rigging-and-animation]]** Set the body and handle attachment WorldOrientation to (0,0,0) and copy matching WorldPosition/WorldOrientation so the accessory does not get an unwanted rotation offset.
- [page](https://devforum.roblox.com/t/accessory-based-items-clothing-addons-updated/744207) **[[common-mistakes]]** Roblox overrides any welds or motors you create on a real Accessory with its own. For custom-controlled attachments, wrap the parts in a Model instead.
- [page](https://devforum.roblox.com/t/accessory-based-items-clothing-addons-updated/744207) **[[scripting-and-performance]]** Give static accessories with Humanoid:AddAccessory(accessory:Clone()) inside CharacterAdded so they reapply on every respawn.
- [page](https://devforum.roblox.com/t/accessory-based-items-clothing-addons-updated/744207) **[[code-architecture-and-frameworks]]** Store pseudo-accessory Models in a folder inside the character model for organisation, since they do not need to be parented directly to the character.
- [page](https://devforum.roblox.com/t/accessory-based-items-clothing-addons-updated/744207) **[[3d-modeling-rigging-and-animation]]** Add custom attachment points on rig body parts with the Default Move tool when Roblox's built-in attachments are not enough; keep their orientation at (0,0,0).
- [page](https://devforum.roblox.com/t/accessory-based-items-clothing-addons-updated/744207) **[[3d-modeling-rigging-and-animation]]** Enable Constraint Details and Draw On Top in Studio to see attachments and constraints in 3D and select them easily.

## Tools
Roblox Studio, F3X plugin, Motor6D, Humanoid:AddAccessory, Default Build Tools

## Topics
[[3d-modeling-rigging-and-animation]] [[building-art-and-assets]] [[code-architecture-and-frameworks]] [[common-mistakes]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
