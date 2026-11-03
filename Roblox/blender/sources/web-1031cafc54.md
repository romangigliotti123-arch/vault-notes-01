---
type: research-source
id: web-1031cafc54
title: "Blender Python API doc: info_advanced_blender_as_bpy"
source_type: "web"
creator: "docs.blender.org"
url: "https://raw.githubusercontent.com/blender/blender/main/doc/python_api/rst/info_advanced_blender_as_bpy.rst"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0027
relevance: 3
density: medium
tags: ["research-source", "web", "bpy-scripting-headless"]
---
# web-1031cafc54

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Blender Python API doc on running Blender as an importable bpy module. Covers pip bpy availability, differences from --background mode (binary_path, unsupported CLI flags, signal handling, default startup scene, factory settings), and limits (no importlib.reload, one .blend at a time). Relevant to headless bpy scripting, not Roblox-specific.

## Claims
- c1: bpy is available via PyPI (pip install bpy); it can also be compiled from source using Blender's build instructions. *(doc, high; bpy-scripting-headless)*
- c2: Using bpy as a module is largely equivalent to running a script with --background, with some differences. *(doc, high; bpy-scripting-headless)*
- c3: When bpy loads, it creates the default startup scene (cube, camera, light) rather than an empty file; use bpy.ops.wm.read_factory_settings(use_empty=True) for an empty scene. *(doc, high; bpy-scripting-headless)*
- c4: Module mode behaves as if --factory-startup was passed; user prefs and startup are ignored unless loaded via bpy.ops.wm.read_userpref() and bpy.ops.wm.read_homefile(). *(doc, high; bpy-scripting-headless)*
- c5: bpy.app.binary_path defaults to an empty string; it can be set manually after locating blender with shutil.which. *(doc, high; bpy-scripting-headless)*
- c6: Modules like gpu and mathutils must be imported after bpy or they will not be found. *(doc, high; bpy-scripting-headless)*
- c7: Reloading bpy via importlib.reload raises an exception; use bpy.ops.wm.read_factory_settings() to reset state instead. *(doc, high; bpy-scripting-headless)*
- c8: Command-line-only options such as --threads and --log have no Python API equivalent; Ctrl-C cancel handling and crash logs are not available in module mode. *(doc, high; bpy-scripting-headless)*
- c9: Only one .blend file can be edited at a time per bpy instance; parallel work should use multiple processes (multiprocessing), each with separate bpy state. *(doc, high; bpy-scripting-headless)*
- c10: Other Python modules using the GPU may prevent Blender/Cycles from accessing it. *(doc, medium; bpy-scripting-headless)*
- c11: bpy.data.temp_data offers a temporary data context to avoid modifying the current .blend; bpy.data.libraries load/write can move data between files. *(doc, medium; bpy-scripting-headless)*

### Code: Locate a blender executable and set bpy.app.binary_path
```python
import bpy
import shutil

blender_bin = shutil.which("blender")
if blender_bin:
   print("Found:", blender_bin)
   bpy.app.binary_path = blender_bin
else:
   print("Unable to find blender!")
```

### Code: Start from empty scene, or load user prefs/startup manually
```python
bpy.ops.wm.read_factory_settings(use_empty=True)

# or load user config explicitly:
bpy.ops.wm.read_userpref()
bpy.ops.wm.read_homefile()
```

## Quotes (brief, for attribution)
> Blender as a Python Module isn't provided on Blender's official download page.  (docs.blender.org)
> The user's startup and preferences are ignored to prevent your local configuration from impacting script behavior.  (docs.blender.org)

## Points to
- https://pypi.org/project/bpy/
- https://developer.blender.org/docs/handbook/building_blender/python_module/
