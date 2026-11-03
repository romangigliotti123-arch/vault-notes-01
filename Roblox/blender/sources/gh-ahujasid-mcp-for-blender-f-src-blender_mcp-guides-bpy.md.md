---
type: research-source
id: gh-ahujasid-mcp-for-blender-f-src-blender_mcp-guides-bpy.md
title: "ahujasid/mcp-for-blender/src/blender_mcp/guides/bpy.md"
source_type: "github"
creator: "ahujasid"
url: "https://github.com/ahujasid/mcp-for-blender/blob/HEAD/src/blender_mcp/guides/bpy.md"
published: "2026-10-29"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0039
relevance: 3
density: high
tags: ["research-source", "github", "bpy-scripting-headless", "claude-blender-mcp", "common-mistakes-fixes", "creator-workflows"]
---
# gh-ahujasid-mcp-for-blender-f-src-blender_mcp-guides-bpy.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Guide for writing version-robust bpy scripts run inside a live Blender via blender-mcp. Covers RNA introspection for enums and sockets, Principled BSDF 4.0 input renames, EEVEE engine ID changes, slotted actions in 4.4 and fcurves removal in 5.0, preferring bpy.data over operators, temp_override for operators, and unit and scale habits. Does not cover Roblox export specifics.

## Claims
- c1: Scripts run in the user's live Blender whose version, language and add-ons are unknown; check blender_version from get_addon_status before version-specific calls. *(doc, high; bpy-scripting-headless)*
- c2: The mcp-for-blender guide names a get_addon_status tool that reports blender_version. *(doc, high; claude-blender-mcp)*
- c3: Find nodes by type rather than name because node names are localized. *(doc, high; bpy-scripting-headless)*
- c4: Principled BSDF in Blender 4.0 renamed many inputs (e.g. Emission Color, Subsurface Weight, Coat Weight, Sheen Weight, Transmission Weight); use inputs.get with fallback. *(doc, high; bpy-scripting-headless)*
- c5: scene.render.engine is a dynamic enum under-reported by RNA; assign inside try/except TypeError to get the accepted list. EEVEE is BLENDER_EEVEE_NEXT in 4.2-4.x and BLENDER_EEVEE before and after. *(doc, high; bpy-scripting-headless)*
- c6: In 5.0+ material.use_nodes is always on; material.diffuse_color only drives solid viewport, not shading. *(doc, high; bpy-scripting-headless)*
- c7: Blender 4.4 introduced slotted actions and 5.0 removed Action.fcurves; insert keys with obj.keyframe_insert and reach fcurves via bpy_extras.anim_utils.action_get_channelbag_for_slot on 4.4+. *(doc, high; bpy-scripting-headless)*
- c8: Prefer bpy.data and object properties over bpy.ops since they need no context and are faster; bmesh for editing. *(doc, medium; bpy-scripting-headless)*
- c9: Code run from a timer lacks a UI area; viewport operators need temp_override with area, region, active_object and selected_objects. *(doc, high; bpy-scripting-headless)*
- c10: mode_set needs an active, visible, selectable object; always return to OBJECT mode in try/finally. *(doc, high; common-mistakes-fixes)*
- c11: Apply scale (transform_apply or mesh data transform) before rigging, dependent modifiers, or export. *(doc, high; common-mistakes-fixes)*
- c12: obj.copy() shares mesh data and is cheap for repeated props; use obj.data.copy() only when the copy must differ. *(doc, high; creator-workflows)*
- c13: Blender units are metres; reference sizes: door about 2.1 m, table 0.75 m, person 1.7 m. *(doc, high; common-mistakes-fixes)*

## Numbers
- n1: **Reference object heights**: door 2.1 m, table 0.75 m, person 1.7 m 

## Techniques
- t1: **RNA introspection before coding**: List enum_items via bl_rna.properties[name].enum_items, list type properties, inspect operator args via get_rna_type(). Probe node sockets in a temporary node group, print enabled inputs, then remove the group.
- t2: **Operator override from timer**: Find VIEW_3D area and WINDOW region, then wrap the operator in bpy.context.temp_override(area, region, active_object, selected_objects).
- t3: **Safe mode switching**: Ensure object is active, visible and selectable; call mode_set; use try/finally to return to OBJECT mode.

### Code: Override context for a viewport operator run from a timer
```python
area = next(a for a in bpy.context.screen.areas if a.type == "VIEW_3D")
region = next(r for r in area.regions if r.type == "WINDOW")
with bpy.context.temp_override(area=area, region=region, active_object=obj, selected_objects=[obj]):
    bpy.ops.object.shade_smooth()
```

### Code: Keyframe insertion that works across versions and fcurve access on 4.4+
```python
obj.keyframe_insert("location", frame=f)
from bpy_extras.anim_utils import action_get_channelbag_for_slot
cb = action_get_channelbag_for_slot(action, obj.animation_data.action_slot)
```

## Quotes (brief, for attribution)
> Scripts run in the user's live Blender, whose version, language and add-ons you don't know.  (ahujasid)
> Find nodes by `type`, never by name: names are localized.  (ahujasid)
> Units are metres. A door is ~2.1 m tall, a table 0.75 m, a person 1.7 m.  (ahujasid)

## Points to
- https://github.com/ahujasid/mcp-for-blender
