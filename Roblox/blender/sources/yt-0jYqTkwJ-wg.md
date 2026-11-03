---
type: research-source
id: yt-0jYqTkwJ-wg
title: "Blender Python for Beginners: Importing Images as Planes"
source_type: "youtube"
creator: "CG Python"
url: "https://www.youtube.com/watch?v=0jYqTkwJ-wg"
published: "2023-01-23"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0023
relevance: 1
density: medium
tags: ["research-source", "youtube", "claude-blender-ai"]
---
# yt-0jYqTkwJ-wg

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Beginner bpy tutorial (18 min) that clears a scene, enables the "Import Images as Planes" add-on from script, and imports a PNG as an image plane. Covers addon_utils check/enable, select_all and delete operators, pathlib path building, and wrapping functions. No Roblox, blender-mcp, or export content.

## Claims
- c1: [5:23] addon_utils.check(name) returns (enabled_in_prefs, loaded); the script checks loaded state before enabling to avoid redundant work. *(demo, medium; claude-blender-ai)*
- c2: [6:43] Add-on module name is the preference name without .py (e.g. 'io_import_images_as_planes'), not the human-readable label. *(demo, medium; claude-blender-ai)*
- c3: [7:24] addon_utils.enable(name) is called with just the add-on module name to activate it from script. *(demo, medium; claude-blender-ai)*
- c4: [2:52] Clearing scene uses bpy.ops.object.select_all(action='SELECT') then bpy.ops.object.delete() with default parameters; it does not remove orphan data like collections or materials. *(demo, high; claude-blender-ai)*
- c5: [4:15] Operator-based deletion is insufficient for full cleanup; created collections and materials persist, so a separate data-removal step is needed (presenter defers this to another video). *(opinion, medium; claude-blender-ai)*
- c6: [8:46] Path.home() combined with 'tmp' and 'my_image.png' gives a cross-platform image path on Windows, Mac and Linux. *(demo, high; claude-blender-ai)*
- c7: [10:46] Check Path.exists() before calling the import operator to avoid an error on missing files. *(demo, high; claude-blender-ai)*
- c8: [12:15] The operator is bpy.ops.import_image.as_planes; its file path argument must be a str, so Path objects must be wrapped with str(). *(demo, high; claude-blender-ai)*
- c9: [10:19] Windows shows Python print output via Window > Toggle System Console; Mac and Linux need separate terminal steps. *(demo, medium; claude-blender-ai)*
- c10: [14:47] Docstrings in functions show in the interactive Python console via help or tab completion. *(demo, high; claude-blender-ai)*

## Numbers
- n1: **video length**: 18:08 
- n2: **views at capture**: 4409 (2023-01-23) 

## Techniques
- t1: **Enable add-on from script**: Import addon_utils; check(name) returns (enabled, loaded); if not loaded, call enable(name) with the module name.
- t2: **Scene clear via operators**: bpy.ops.object.select_all(action='SELECT'), then bpy.ops.object.delete(). Add separate cleanup for orphan data.
- t3: **Cross-platform path building**: pathlib.Path.home() / 'tmp' / 'my_image.png'; verify with .exists() then pass str(path) to the operator.
- t4: **Wrap steps into functions**: Put clear, enable_add_on, and import steps into functions under main(), add docstrings, call main() at bottom for reusable scripts.

### Code: Clear scene objects via operators
```python
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()
```

### Code: Enable add-on only if not loaded
```python
import addon_utils
name = 'io_import_images_as_planes'
if not addon_utils.check(name)[1]:
    addon_utils.enable(name)
```

### Code: Cross-platform image path and import with existence check
```python
from pathlib import Path
image_path = Path.home() / 'tmp' / 'my_image.png'
if image_path.exists():
    bpy.ops.import_image.as_planes(filepath=str(image_path))
```

## Quotes (brief, for attribution)
> I need to convert that object into a string, so I'm gonna wrap it in a string conversion.  (at 12:15, CG Python)
> if your script is creating collections or materials, this will not remove the data that is created by your script.  (at 4:15, CG Python)

## Points to
- Blender add-on: Import Images as Planes (io_import_images_as_planes)
- Blender addon_utils module
- pathlib documentation
