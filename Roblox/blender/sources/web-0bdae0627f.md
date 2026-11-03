---
type: research-source
id: web-0bdae0627f
title: "DevForum thread 2824027"
source_type: "web"
creator: "devforum.roblox.com"
url: "https://devforum.roblox.com/raw/2824027"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0010
relevance: 3
density: low
tags: ["research-source", "web", "common-mistakes-fixes", "rigging-animation", "roblox-export-settings", "roblox-import-pipeline"]
---
# web-0bdae0627f

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
DevForum thread (Feb 2024) where a user exports FBX from Blender to Roblox with mismatched scale/rotation; suspects unit scale (suggests 0.5 scale, MM import), reports Secondary bone not working, Motor6D use, and that bones parented to meshes (RootPart) break the rig. Adding missing modifiers reportedly helped; glTF imports fine but creates no Bones. A DevForum staffer asks for hierarchy and .blend to reproduce.

## Claims
- c1: User exports FBX from Blender and the model appears wrongly scaled/rotated in Roblox Studio; user proposes export scale 0.5 with MM import to keep Blender unit scale. *(experience, low; roblox-export-settings)*
- c2: Secondary bone had no visible effect in Roblox; user says bones are wrong after FBX import. *(experience, low; rigging-animation)*
- c3: User is unsure whether Roblox supports bones parented to meshes; RootPart reportedly breaks the rig. *(experience, low; rigging-animation)*
- c4: Adding the missing modifiers to the object reportedly fixed part of the issue (user's own guess, not confirmed). *(experience, low; common-mistakes-fixes)*
- c5: glTF import works without rotation issues in the user's test, but does not create Bones. *(experience, low; roblox-import-pipeline)*
- c6: Thread shows Motor6D being used by Roblox instead of expected bone setup. *(experience, low; roblox-import-pipeline)*
- c7: A DevForum staffer says the preview mesh looks strangely rotated and asks for hierarchy and .blend to reproduce. *(doc, medium; common-mistakes-fixes)*

## Numbers
- n1: **FBX export scale**: 0.5 User's suggested scale factor to get correct units on MM import

## Techniques
- t1: **Export via glTF instead of FBX**: User reports glTF imports with correct orientation but no Bones created; use when FBX rotates wrongly.
- t2: **Check modifiers before export**: User found the object lacked modifiers it needed; adding them reportedly resolved part of the problem.

## Quotes (brief, for attribution)
> Preferrably one can set the scale to 0.5 and then import it as MM so that one can keep the Unit Scale to Blender's original values.  (devforum.roblox.com)
> gltf works fine though. But it isn't creating the Bones.  (devforum.roblox.com)

## Points to
- https://devforum.roblox.com/raw/2824027
