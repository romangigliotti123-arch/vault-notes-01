---
type: research-source
id: gh-Roblox-roblox-blender-plugin-i35
title: "Roblox/roblox-blender-plugin#35 Plugin incompatible with Blender 4.0 - Upload fails with no errors, AttributeError: 'Context' object has no "
source_type: "github"
creator: "Roblox"
url: "https://github.com/Roblox/roblox-blender-plugin/issues/35"
published: "2023-11-23"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0017
relevance: 2
density: low
tags: ["research-source", "github", "automation-and-creator-workflows", "blender-roblox-export-import"]
---
# gh-Roblox-roblox-blender-plugin-i35

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
GitHub issue #35 for the Roblox Blender plugin (Nov 2023). A user reports uploads from Blender's N-panel taking 10-30 minutes and never appearing, with no error. On Blender 4.0 the plugin raised AttributeError: 'Context' object has no attribute 'selected_ids'. Maintainers pointed to v1.0.3 as the 4.0 fix. A later ModuleNotFoundError was fixed by reinstalling and tracked in #39. Nothing on blender-mcp, bpy, or Claude.

## Claims
- c1: Plugin upload from Blender (select collection, press N, Upload) on Blender 4.0 failed with AttributeError: 'Context' object has no attribute 'selected_ids'. *(experience, high; blender-roblox-export-import)*
- c2: Reported symptom: uploads took 10-30 minutes and the asset never appeared, with no error shown, to personal account or group. *(experience, medium; blender-roblox-export-import)*
- c3: Plugin v1.0.3 was stated by maintainer othomson-roblox to fix the Blender 4.0 issue. *(doc, medium; blender-roblox-export-import)*
- c4: Original reporter said the same upload problem persisted on the latest release and after renaming the file. *(experience, low; blender-roblox-export-import)*
- c5: After updating to v1.0.3 a different error appeared: ModuleNotFoundError: No module named 'roblox-blender-plugin-1'. *(doc, high; blender-roblox-export-import)*
- c6: Fix suggested for the ModuleNotFoundError: remove all copies of roblox-blender-plugin from the Blender Add-ons folder, then reinstall. *(doc, high; automation-and-creator-workflows)*
- c7: Blender 4 update led one user to see a bones-related message from the plugin; commenter suspected the plugin was too outdated for frequent Blender releases (opinion). *(opinion, low; blender-roblox-export-import)*
- c8: Issue closed as resolved by v1.0.3; remaining new-problem reports were redirected to issue #39. *(doc, high; automation-and-creator-workflows)*

## Numbers
- n1: **upload duration before giving up**: 10-30 minutes reported upload time with no visible result or error
- n2: **Blender version with bug**: 4.0 AttributeError on selected_ids; plugin fixed in v1.0.3
- n3: **fixed plugin release**: v1.0.3 maintainer-named release addressing Blender 4.0 issue

## Techniques
- t1: **Clean plugin reinstall**: Open Blender Add-ons folder, delete every copy of roblox-blender-plugin, then reinstall the add-on. Fixes ModuleNotFoundError for roblox-blender-plugin-1.

## Quotes (brief, for attribution)
> it takes 10-30 minutes to upload. By then, I'm out of patience and time... Just never shows up. No errors.  (Roblox)
> Can you download the latest release (which fixes the 4.0 issue) and confirm if you are still having problems?  (Roblox)

## Contradictions flagged
- Reporter says upload failure persists on the latest release. (vs Maintainer says v1.0.3 fixes the 4.0 issue and the issue was closed as resolved.)

## Points to
- https://github.com/Roblox/roblox-blender-plugin/releases/tag/v1.0.3
- https://github.com/Roblox/roblox-blender-plugin/issues/39
