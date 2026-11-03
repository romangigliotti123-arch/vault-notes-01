---
type: research-source
id: yt-k1gCIezKA8E
title: "Easily Install 3rd Party Python Modules Into Blender"
source_type: "youtube"
creator: "CG Python"
url: "https://www.youtube.com/watch?v=k1gCIezKA8E"
published: "2024-09-05"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0014
relevance: 2
density: medium
tags: ["research-source", "youtube", "avatar-ugc-accessories", "bpy-scripting-headless", "common-mistakes-fixes"]
---
# yt-k1gCIezKA8E

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Short CG Python video showing how to install third-party Python packages (example: pillow) into Blender's bundled interpreter. Uses pip with --target pointed at Blender's user scripts/modules folder, obtained via bpy.utils.user_resource('SCRIPTS', path='modules'). Avoids writing into the Blender install folder, which may be blocked on Windows. Does not cover blender-mcp or Roblox export.

## Claims
- c1: [0:51] By default pip installs packages into the folder of the Python interpreter; for Blender's bundled Python that is inside the Blender install folder, which the user may not be able to write to, especially on Windows with the official installer. *(demo, high; bpy-scripting-headless)*
- c2: [1:16] Workaround: pass pip's --target argument with a folder Blender's Python already searches, so no admin write access to the install folder is needed. *(demo, high; bpy-scripting-headless)*
- c3: [1:54] Get the target path inside Blender's Python console by running bpy.utils.user_resource('SCRIPTS', path='modules'); the path is machine-specific and must be copied from the output. *(demo, high; bpy-scripting-headless)*
- c4: [2:34] Symptom before fix: 'import PIL' (pillow) fails inside Blender's Python with a no-module error. *(demo, high; bpy-scripting-headless)*
- c5: [3:16] Command used: pip install pillow --target <path from user_resource>; it completed successfully and the package appeared in the modules folder, which was empty beforehand. *(demo, high; bpy-scripting-headless)*
- c6: [3:57] After installing to that folder, the import works in Blender with no extra code such as sys.path changes. *(demo, high; bpy-scripting-headless)*
- c7: [4:00] Installed packages are only available locally; shipping them with a Blender add-on is covered in a separate video, not in this one. *(doc, low; avatar-ugc-accessories)*
- c8: [0:26] A 'no module' error when importing third-party packages in Blender is the problem this method addresses; the video references another video on the same error. *(doc, medium; common-mistakes-fixes)*

## Numbers
- n1: **video length**: 4:22 
- n2: **views at capture**: 19644 views (dated 2024-09-05) 

## Techniques
- t1: **Install pip package into Blender's user modules folder**: 1) In Blender Scripting workspace, Python console, run bpy.utils.user_resource('SCRIPTS', path='modules') and copy the path. 2) In terminal run: pip install <package> --target "<path>". 3) Restart or re-import in Blender; import works without sys.path edits.

### Code: Get the Blender user modules folder path (run in Blender's Scripting > Python console); reconstructed from spoken command
```python
import bpy
path = bpy.utils.user_resource('SCRIPTS', path='modules')
print(path)
```

### Code: Install pillow into that folder so Blender's bundled Python can import it (path is machine-specific placeholder)
```shell
pip install pillow --target "<path-from-user_resource>"
```

## Quotes (brief, for attribution)
> you can use a special command line argument pass into pip and tell where pip should install this python package  (at 1:16, CG Python)

## Points to
- Video on 'no module' error (CG Python / Default Cube), referenced at 0:26
- Pillow (Python Imaging Library) package
