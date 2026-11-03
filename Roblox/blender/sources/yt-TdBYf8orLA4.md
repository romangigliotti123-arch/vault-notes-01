---
type: research-source
id: yt-TdBYf8orLA4
title: "Creating a Basic Material in Blender Using Python Code"
source_type: "youtube"
creator: "CG Python"
url: "https://www.youtube.com/watch?v=TdBYf8orLA4"
published: "2023-02-20"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0035
relevance: 2
density: medium
tags: ["research-source", "youtube", "bpy-scripting-headless", "common-mistakes-fixes", "texturing-baking-uv"]
---
# yt-TdBYf8orLA4

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Beginner bpy tutorial: create a material via bpy.data.materials.new, enable use_nodes, set Principled BSDF base color/metallic/roughness by input name, add an ico sphere, assign material, clear scene and orphan data each run, then refactor into functions. No Roblox, Claude, or MCP content.

## Claims
- c1: [2:33] New materials are created with bpy.data.materials.new(name); use_nodes must be enabled to get a Principled BSDF node tree. *(demo, high; bpy-scripting-headless)*
- c2: [5:19] Node inputs can be referenced by index (starting at 0) or by name string such as 'Base Color'; the name form is more readable. *(demo, high; bpy-scripting-headless)*
- c3: [7:13] Re-running a script that creates materials accumulates unused datablocks with zero users. *(demo, high; common-mistakes-fixes)*
- c4: [7:53] File > Clean Up > Recursive Unused Data-blocks can be copied as Python from the Info panel to purge orphan data in scripts. *(demo, high; bpy-scripting-headless)*
- c5: [9:59] Material is assigned to an object by appending to mesh.materials list. *(demo, high; texturing-baking-uv)*
- c6: [10:45] Clearing the scene by select-all and delete each run avoids duplicate ico spheres. *(demo, high; bpy-scripting-headless)*
- c7: [12:08] Presenter says the scene-clearing snippet does not handle objects in edit mode or modified world shaders. *(opinion, medium; bpy-scripting-headless)*
- c8: [14:20] random.uniform(0.1, 1) gives a random roughness value each run. *(demo, high; bpy-scripting-headless)*

## Numbers
- n1: **roughness random range**: 0.1 to 1 random.uniform(0.1, 1) used for roughness each run
- n2: **ico sphere subdivisions**: 5 set for smooth ico sphere before shade smooth

## Techniques
- t1: **Get Info panel copy-as-Python**: Perform action in UI, copy the generated bpy command from the Info panel, paste into script and replace hard-coded references with variables.
- t2: **Refactor into functions**: Wrap code in main(), clear_scene(), create_material(name), add_mesh(); call main() at bottom, otherwise nothing runs.

### Code: Create material, enable nodes, set Principled BSDF inputs by name
```python
import bpy
material = bpy.data.materials.new(name="MyMaterial")
material.use_nodes = True
bsdf = material.node_tree.nodes["Principled BSDF"]
bsdf.inputs["Base Color"].default_value = (0.8, 0.1, 0.1, 1.0)
bsdf.inputs["Metallic"].default_value = 1.0
bsdf.inputs["Roughness"].default_value = 0.3
```

### Code: Purge unused datablocks
```python
bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)
```

### Code: Clear scene each run before rebuilding
```python
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()
```

### Code: Assign material to mesh and random roughness
```python
import random
obj = bpy.context.active_object
obj.data.materials.append(material)
bsdf.inputs["Roughness"].default_value = random.uniform(0.1, 1)
```

## Quotes (brief, for attribution)
> If we run the script a hundred times, it's gonna have a hundred materials just floating around.  (at 7:13, CG Python)

## Points to
- CG Python channel (Victor Stepanov) hex-to-RGBA video referenced, not provided
