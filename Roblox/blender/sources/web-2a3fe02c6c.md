---
type: research-source
id: web-2a3fe02c6c
title: "DevForum thread 4115553"
source_type: "web"
creator: "devforum.roblox.com"
url: "https://devforum.roblox.com/raw/4115553"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0010
relevance: 3
density: medium
tags: ["research-source", "web", "common-mistakes-fixes", "rigging-animation", "roblox-import-pipeline"]
---
# web-2a3fe02c6c

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
DevForum bug report (2025-12-04): a custom Blender rig exported as FBX imports into Roblox with wrong Motor6D rotations, so Blender-made animations pose incorrectly. The reporter says the Roblox animation editor treats the FBX as one mesh, pushing it over the triangle limit, so the Roblox Animations Importer-Exporter plugin is used instead. Changing axes and bone Roll did not fully fix it. No forum solution was reported.

## Claims
- c1: FBX export of a custom Blender armature imports into Roblox with incorrect Motor6D rotations, causing animations to pose wrongly. *(experience, medium; rigging-animation)*
- c2: Roblox animation editor imports the FBX as one big mesh instead of separate parts, pushing triangle count over the limit. *(experience, medium; roblox-import-pipeline)*
- c3: Changing import/export axes and adjusting bone Roll in Blender did not fully fix Motor6D rotation errors; Roll fixes sometimes flipped the bone axis. *(experience, medium; rigging-animation)*
- c4: Roblox Animations Importer-Exporter Blender addon plus Roblox plugin can import keyframe animation data directly from Blender, bypassing the FBX animation path. *(doc, medium; rigging-animation)*
- c5: Reporter scaled the imported rig to mm during import; no verified fix was found and the issue was filed as a bug. *(experience, low; common-mistakes-fixes)*

## Numbers
- n1: **Import scale**: mm Reporter adjusted scale to mm in the 3D importer

## Techniques
- t1: **Bone Roll and axis adjustment test**: Pose each bone to test axis of movement in Blender, then try changing import/export axes or bone Roll. Reporter says this only partly worked.
- t2: **Keyframe import via Animations Importer-Exporter**: Use the Blender extension and Roblox plugin to move keyframe animation data straight from Blender into Studio, bypassing FBX animation import.

## Quotes (brief, for attribution)
> it appears this is because the Motor6D rotations are imported incorrectly.  (devforum.roblox.com)
> plug-ins must be used to import animations directly from blender as keyframe data.  (devforum.roblox.com)

## Points to
- https://extensions.blender.org/approval-queue/roblox-animations-importer-exporter/
- https://create.roblox.com/store/asset/16708835782/Blender-Animations-ultimate-edition
- https://devforum.roblox.com/t/4115552
