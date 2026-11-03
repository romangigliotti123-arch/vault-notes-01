---
type: research-source
id: yt-BSsjSj0iOaE
title: "Automating 360 Turntable Animations With a Python Script in Blender"
source_type: "youtube"
creator: "CG Python"
url: "https://www.youtube.com/watch?v=BSsjSj0iOaE"
published: "2023-04-09"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0035
relevance: 2
density: medium
tags: ["research-source", "youtube", "automation-and-creator-workflows", "claude-blender-ai", "other"]
---
# yt-BSsjSj0iOaE

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Blender Python tutorial (CG Python, 2023) building a turntable render script with bpy. It globs .blend files in a models folder, links objects from each file into the scene, filters by name substring, adds a light rig, a 360-degree rotating empty, and a camera with Track To constraint, then renders PNG stills and an MP4. Nothing on Claude, blender-mcp, or Roblox export.

## Claims
- c1: [0:37] Script workflow: paste helper code into Blender's Scripting workspace text editor, save as .py next to a models folder, and resolve paths relative to the script location. *(demo, high; claude-blender-ai)*
- c2: [5:05] Uses pathlib Path.glob('*.blend') to list .blend files; author notes glob dates to 1970s Linux. *(demo, high; claude-blender-ai)*
- c3: [7:46] Linking pattern: bpy.data.libraries.load with data_from/data_to, copy objects into bpy.context.scene collection, then return them. Objects must be both loaded and linked into a collection to appear. *(demo, high; claude-blender-ai)*
- c4: [10:59] Missing-file fallback: if the floor .blend path does not exist, create a 100-size plane, make a material, set diffuse colour, and assign it. *(demo, high; claude-blender-ai)*
- c5: [12:37] Light rig: vertices of a circle primitive position three lights; an Empty with Track To constraint keeps them aimed at centre. *(demo, medium; claude-blender-ai)*
- c6: [14:33] 360 rotation about Z is animated on an Empty; frame count is FPS times seconds, plus one so the loop's first and last frames differ. *(demo, medium; claude-blender-ai)*
- c7: [17:48] Camera is parented to the rotating Empty and gets a Track To constraint targeting it, and is set as scene.camera. *(demo, high; claude-blender-ai)*
- c8: [22:23] Filtering by name: linked objects are kept only if the name contains a substring (Target); author renamed model files to include 'Target' to pick one of two variants. *(demo, high; claude-blender-ai)*
- c9: [25:13] Model centre computed by averaging bounding-box corners in local space, then transformed by the world matrix; the focus Empty is placed there. *(demo, medium; claude-blender-ai)*
- c10: [26:31] Camera height set to twice the target's Z dimension; camera position then multiplied by 1.5 to pull back so model is framed. *(demo, medium; claude-blender-ai)*
- c11: [33:28] Animation output: scene render file format set to FFMPEG with MP4 container (codec transcribed as 'mpic4', likely MPEG-4); test renders at 10% resolution before full render. *(demo, medium; claude-blender-ai)*
- c12: [34:59] Between iterations, objects are unlinked from scene collection so models do not overlap; the loop then renders each model in turn. *(demo, high; claude-blender-ai)*
- c13: [36:15] Author's third-party 'BPI building blocks' package (pip or add-on) replaces boilerplate scene cleanup and resolution setup helpers with imports. *(opinion, low; claude-blender-ai)*
- c14: [32:37] Rendering from script via bpy.ops.render blocks the Blender UI until finished; no progress window appears. *(experience, medium; claude-blender-ai)*
- c15: [6:27] On Windows the system console toggle is available in Blender; on Mac/Linux a separate setup is needed to view print output. *(experience, medium; other)*
- c16: [1:48] Sample models are free Poly Haven assets (football, marble bust, potted plant), each in its own folder with textures. *(demo, high; automation-and-creator-workflows)*

## Numbers
- n1: **sample models**: 3 Poly Haven assets 
- n2: **fallback floor plane size**: 100 
- n3: **frame count**: FPS x seconds, plus 1 for loop 
- n4: **camera height multiplier**: 2x target Z dimension 
- n5: **camera pull-back multiplier**: 1.5x 
- n6: **test render resolution percentage**: 10 (full was 100) 

## Techniques
- t1: **Name-substring filter on linked objects**: Pass with_name to link function; append object to list only if name contains substring; return only filtered list.
- t2: **Bounding-box centre to world space**: Average the 8 bound_box corners locally, multiply by object world matrix, use as focus Empty location.
- t3: **Parent camera to rotating Empty plus Track To**: Animate Empty Z rotation over frame range; parent camera to Empty; add Track To constraint targeting Empty.
- t4: **Unlink between model iterations**: After each render, unlink linked objects from scene collection before linking the next model.
- t5: **Low-res preview then full render**: Set render percentage to 10, render animation to check loop, then restore to 100 and render full.

## Quotes (brief, for attribution)
> link the objects from that blend file into the current scene  (at 7:46, CG Python)
> we need to unlink model that's currently in the scene so we can link the next model for the next render  (at 34:59, CG Python)

## Points to
- https://polyhaven.com (source of sample models)
- BPI building blocks package by the author (pip or add-on), referenced in video
