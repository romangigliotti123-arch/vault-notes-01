---
type: research-source
id: yt-ZrN9w8SMFjo
title: "Blender Python Tutorial: Linking Objects Across .blend Files"
source_type: "youtube"
creator: "CG Python"
url: "https://www.youtube.com/watch?v=ZrN9w8SMFjo"
published: "2023-03-12"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0023
relevance: 2
density: medium
tags: ["research-source", "youtube", "claude-blender-ai", "other"]
---
# yt-ZrN9w8SMFjo

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Beginner bpy tutorial on linking data-blocks from another .blend file. Uses a context manager that loads a file with link=True, then moves objects into the scene collection. Shows that linked objects are read-only until link is set to False (copy). Covers removing libraries and wrapping logic in functions. Two exercises: link scenes, and link only a named material. Nothing on Roblox, FBX/glTF or MCP.

## Claims
- c1: [2:11] Linking via bpy library load with link on keeps data as a reference to the source .blend, not a copy. *(demo, high; claude-blender-ai)*
- c2: [6:31] Linked objects can't be entered into edit mode (Tab fails); setting link to False copies the data so it becomes editable. *(demo, high; claude-blender-ai)*
- c3: [8:37] Inside the load context manager, the loaded data-block lists contain plain name strings; they only become Blender objects after the with block exits. *(demo, high; claude-blender-ai)*
- c4: [10:43] Linked objects are added to the scene by linking them into scene.collection.objects after the load block. *(demo, medium; claude-blender-ai)*
- c5: [11:32] Linked libraries can be removed with a bpy library remove call run over the library list, which clears the Library entry from the file. *(demo, medium; claude-blender-ai)*
- c6: [3:09] Source .blend path built with pathlib from the home folder (Path.home()) plus a temp folder, cross-platform on Mac, Linux and Windows. *(demo, medium; other)*
- c7: [3:50] On Windows, print output needs the system console (Window > Toggle System Console); Mac and Linux print to terminal. *(experience, medium; other)*
- c8: [15:26] Data-blocks other than objects (scenes, materials) can be linked the same way; a material is filtered by checking 'blue' in its name before appending to data_to.materials. *(demo, medium; claude-blender-ai)*
- c9: [5:48] Exercise-style pattern: wrap linking in a function with a link=False default argument so the caller chooses reference vs copy. *(opinion, low; claude-blender-ai)*

## Numbers
- n1: **video length**: 20:02 
- n2: **libraries in test file**: 1 library per link run; code says it works for many 

## Techniques
- t1: **Link .blend data-blocks with context manager**: Open the source file with bpy.data.libraries.load(path, link=True) as (data_from, data_to). Assign the names you want to data_to.objects, data_to.scenes or data_to.materials, then read them after the block exits.
- t2: **Clean up library links before rerunning**: Iterate bpy.data.libraries and call bpy.data.libraries.remove on each before the next run so the file doesn't accumulate library entries.
- t3: **Copy instead of link**: Call the load with link=False so data is copied into the current file and becomes editable.
- t4: **Selective link by name**: Loop over data_from.materials and keep only names that contain a substring such as 'blue', then assign that list to data_to.materials.

## Quotes (brief, for attribution)
> You can see that it already has a library. So that is, remember that path that we defined.  (at 6:31, CG Python)
> Let's go ahead and run it. And now let's go ahead and view layer, and you can see that there is no link icon anymore.  (at 12:53, CG Python)

## Points to
- Blender Python API (bpy) via scripting workspace
- Victor Stepanov / CG Python channel
