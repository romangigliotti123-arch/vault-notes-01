---
type: research-source
id: web-f6e9a31d0f
title: "DevForum thread 1566656"
source_type: "web"
creator: "devforum.roblox.com"
url: "https://devforum.roblox.com/raw/1566656"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0010
relevance: 2
density: low
tags: ["research-source", "web", "common-mistakes-fixes", "rigging-animation", "roblox-export-settings"]
---
# web-f6e9a31d0f

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Short 2021 DevForum thread: an FBX mesh imported into Roblox appears rotated 90 degrees. Replies blame Blender's Z-up versus Roblox's Y-up. The OP fixed it by fixing the object's origin rotation. One reply recommends OBJ over FBX, and another says OBJ drops the rig. No Claude, blender-mcp or bpy content.

## Claims
- c1: Blender is Z-up while Roblox is Y-up; imported meshes can appear lying on their side. Stated as a question by a reply, not verified. *(opinion, low; roblox-export-settings)*
- c2: OP's FBX rotation problem was fixed by rotating the whole object, then rotating the mesh back, which reset the origin's rotation. *(experience, medium; common-mistakes-fixes)*
- c3: OBJ is better than FBX for Roblox because it carries measurement data and imports at correct scale, rotation and position. *(opinion, low; roblox-export-settings)*
- c4: Exporting to OBJ removes the rig/armature from Blender, so OBJ cannot carry rigged meshes. *(opinion, medium; rigging-animation)*

## Techniques
- t1: **Origin rotation reset**: Rotate the whole object to a reference orientation, then rotate the mesh back to its original rotation so the origin's rotation is reset. Reported as working by the OP.

## Quotes (brief, for attribution)
> It seemed like the problem was the origin rotation of my mesh, I fixed this by rotating the entire object, then rotating the mesh back to its original rotation.  (devforum.roblox.com)
> Uploading it as an OBJ would remove the rig from blender  (devforum.roblox.com)

## Contradictions flagged
- OBJ is better than FBX for Roblox imports and keeps scale and position correct. (vs ThatLazyBucket reply: OBJ removes the rig, so FBX is needed for rigged assets.)
