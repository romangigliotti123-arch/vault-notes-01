---
type: research-source
id: yt-LasB_NMmvyA
title: "Mesh Editing in Blender with Python: I Wish I'd Learned THIS Sooner"
source_type: "youtube"
creator: "CG Python"
url: "https://www.youtube.com/watch?v=LasB_NMmvyA"
published: "2023-08-28"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0018
relevance: 1
density: medium
tags: ["research-source", "youtube", "claude-blender-ai", "other"]
---
# yt-LasB_NMmvyA

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Blender bpy/bmesh tutorial, not Roblox or Claude-specific. Shows wrapping bmesh setup and teardown (get BMesh, bevel, normals update, write back, free) in a contextlib @contextmanager that yields the BMesh. Also covers handling object vs edit mode via bpy.context.mode, and stepping through the script in VS Code with the Blender Development extension.

## Claims
- c1: [0:46] Bevel scripts are split into boilerplate setup, the operator call, and teardown; the teardown is the same every time, so it can be wrapped once. *(demo, high; claude-blender-ai)*
- c2: [2:08] A @contextlib.contextmanager function that yields the BMesh runs setup before the with-block and cleanup after it, so editing code sits inside the with block. *(demo, high; claude-blender-ai)*
- c3: [4:52] Teardown in the context manager updates normals, writes the BMesh back to mesh data, updates the scene, then frees the BMesh. *(demo, high; claude-blender-ai)*
- c4: [6:15] The same wrapper works for edit-mode objects if the single call to edit_mesh is moved into the wrapper. *(demo, medium; claude-blender-ai)*
- c5: [8:47] Mode can be checked from the Python console via bpy.context.mode, which prints OBJECT or EDIT_MESH. *(demo, medium; claude-blender-ai)*
- c6: [10:10] A merged context manager branches on mode: edit mode uses edit_mesh, object mode uses mesh data and a BMesh, and both paths run the same yield body. The author calls this approach not ideal. *(opinion, medium; claude-blender-ai)*
- c7: [11:30] Moving the context manager into a separate module (bmesh_utils) and importing it works after a script reload. *(demo, medium; other)*
- c8: [7:30] The Blender Development VS Code extension runs scripts inside Blender while editing them in VS Code, so breakpoints can be stepped through. *(demo, medium; other)*

## Numbers
- n1: **video length**: 11:58 

## Techniques
- t1: **contextlib context manager for bmesh edits**: Import contextlib. Decorate a function with @contextmanager. Get the BMesh, yield it, then after the with-block update normals, write back to mesh, update the scene, and free the BMesh. Use with ... as bm: around the edit ops.
- t2: **Mode-aware wrapper**: Check bpy.context.mode. In OBJECT mode use mesh data and BMesh. In EDIT_MESH use edit_mesh. Yield the same BMesh in both cases, then apply the matching write-back.

### Code: Context manager shape for bmesh setup and teardown (from the video's pattern, paraphrased structure)
```python
from contextlib import contextmanager

@contextmanager
def get_bmesh(mesh_object):
    # setup: create BMesh from mesh data
    ...
    yield bm
    # teardown: update normals, write back, free BMesh
    ...
```

## Points to
- Blender Development VS Code extension
