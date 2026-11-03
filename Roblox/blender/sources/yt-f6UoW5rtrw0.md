---
type: research-source
id: yt-f6UoW5rtrw0
title: "The Ultimate Guide to Reading and Writing JSON Files for Blender Python Beginners"
source_type: "youtube"
creator: "CG Python"
url: "https://www.youtube.com/watch?v=f6UoW5rtrw0"
published: "2023-01-30"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0044
relevance: 2
density: medium
tags: ["research-source", "youtube", "bpy-scripting-headless", "creator-workflows"]
---
# yt-f6UoW5rtrw0

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Beginner tutorial on Blender Python (bpy) for reading and writing mesh data to JSON. Builds a script that clears the scene, extracts verts, faces and object name/location from a mesh in edit mode via bmesh, dumps to a mesh.json file with indent=4, then reloads it and recreates the mesh. Does not cover Blender MCP, Claude, Roblox export or import.

## Claims
- c1: [2:08] Clearing scene: force object mode, select all objects, delete selected; does not clear collections, materials or geometry nodes data. *(demo, high; bpy-scripting-headless)*
- c2: [5:07] bmesh is used to read mesh data; the mesh must be put in edit mode first, and returned to object mode before finishing. *(demo, high; bpy-scripting-headless)*
- c3: [8:34] Developer Extras in Preferences > Interface shows vertex/face indices in edit mode, used to verify the face-to-vert index mapping. *(demo, high; bpy-scripting-headless)*
- c4: [14:25] Vertex coordinates are stored by pre-filling a list of None of len(verts) and assigning by index, rather than appending, so order matches vertex index. *(demo, medium; bpy-scripting-headless)*
- c5: [18:01] json.dump with indent=4 writes readable output; without indent the file is one unreadable line, though it loads the same. *(demo, high; bpy-scripting-headless)*
- c6: [17:19] Output path built with pathlib home folder, file name mesh.json in a temp folder; works on Windows, Mac, Linux. *(demo, medium; bpy-scripting-headless)*
- c7: [25:44] Load uses json.loads on file text; the script does not check file existence first, which would error if missing. *(demo, medium; bpy-scripting-headless)*
- c8: [32:41] Object location is saved as list(obj.location) (x,y,z) and applied to the recreated object after creation. *(demo, high; bpy-scripting-headless)*
- c9: [30:10] Same save/load pipeline works unchanged for a different primitive (icosphere): only the creation op changes. *(demo, medium; bpy-scripting-headless)*
- c10: [12:15] Pprint (pretty print) module used to make nested list output readable in the system console. *(demo, high; bpy-scripting-headless)*
- c11: [0:44] Author recommends starting from a blank scene every run so repeated script runs don't accumulate objects. *(opinion, medium; creator-workflows)*

## Numbers
- n1: **exercise location test value**: 5, 5, 5 (set via object location) Location set to a test value so the object is visibly off-centre

## Techniques
- t1: **Clear scene before run**: Set object mode if poll passes, select_all SELECT, then object.delete. Run at script start for a blank scene each time.
- t2: **Index-based vertex fill**: Create list of None with length of vert count, then assign each vert coord at its vert.index inside a bmesh loop.
- t3: **Dict to JSON round trip**: Build dict of name, location, face vert indices and vert coords; json.dumps with indent=4 and write; read text, json.loads to rebuild.

### Code: Clear all objects from the scene, forcing object mode first
```python
import bpy

def delete_all_objects():
    """Delete all objects in the scene"""
    if bpy.ops.object.mode_set.poll():
        bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()
```

### Code: Write mesh data to JSON with indent
```python
with open(path, 'w') as f:
    text = json.dumps(data, indent=4)
    f.write(text)
```

## Quotes (brief, for attribution)
> it's gonna put all that data in a single line unreadable, but it works  (at 18:01, CG Python)

## Points to
- CG Python channel (Victor Stepanov) - related Blender Python videos
- Mac/Linux system console tutorial (referenced, not linked)
