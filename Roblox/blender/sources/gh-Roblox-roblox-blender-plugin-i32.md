---
type: research-source
id: gh-Roblox-roblox-blender-plugin-i32
title: "Roblox/roblox-blender-plugin#32 Bug. Can't Upload From Blender"
source_type: "github"
creator: "Roblox"
url: "https://github.com/Roblox/roblox-blender-plugin/issues/32"
published: "2023-11-14"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0010
relevance: 2
density: low
tags: ["research-source", "github", "automation-and-creator-workflows", "blender-roblox-export-import"]
---
# gh-Roblox-roblox-blender-plugin-i32

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
GitHub issue #32 on Roblox/roblox-blender-plugin (2023-11-14): upload from Blender fails on Blender 4.0 with AttributeError because context.selected_ids no longer exists. Users fixed it by changing it to selected_objects; maintainer says fixed in v1.0.2. Thin on Claude/MCP, bpy, or mesh/rig/avatar specifics.

## Claims
- c1: Roblox Blender plugin v4.0 incompatibility: get_selected_objects.py used context.selected_ids, which Blender 4.0 removed, causing AttributeError on upload. *(experience, high; blender-roblox-export-import)*
- c2: User-reported workaround: in lib/get_selected_objects.py replace 'context.selected_ids' with 'context.selected_objects', then restart Blender. Reported working by multiple commenters. *(experience, high; blender-roblox-export-import)*
- c3: Maintainer Nightriff states the issue was fixed in plugin v1.0.2; latest release is the recommended fix rather than manual edits. *(doc, high; blender-roblox-export-import)*
- c4: Blender 4.0 update removed the add-on on first launch, forcing a manual reinstall of the plugin before the error appeared. *(experience, medium; automation-and-creator-workflows)*

## Numbers
- n1: **Plugin version with fix**: v1.0.2 Maintainer comment stating issue fixed
- n2: **Blender version affected**: 4.0 Error appeared after Blender 4.0 update

## Techniques
- t1: **Manual hotfix for removed API attribute**: Open lib/get_selected_objects.py in the plugin folder under scripts/addons; replace context.selected_ids with context.selected_objects; save; restart Blender.

### Code: Line causing the Blender 4.0 crash (from traceback), and the commenter-reported fix
```python
for selected_object in context.selected_ids:
# fix: change 'selected_ids' to 'selected_objects'
for selected_object in context.selected_objects:
```

## Quotes (brief, for attribution)
> This issue was fixed in v1.0.2, thanks for reporting!  (Roblox)
> AttributeError: 'Context' object has no attribute 'selected_ids'. Did you mean: 'selected_bones'?  (Roblox)

## Contradictions flagged
- Commenter says the add-on was removed by the 4.0 update and reinstalled, but the issue title/body attribute the bug to 4.0.0 only as a suspicion ('I think') (vs Issue body hedges the cause; not confirmed by maintainers)

## Points to
- https://github.com/Roblox/roblox-blender-plugin/releases/latest
