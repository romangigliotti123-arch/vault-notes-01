---
type: research-source
id: gh-Roblox-roblox-blender-plugin-i57
title: "Roblox/roblox-blender-plugin#57 \"Add-on Error\" during upload: AttributeError: Calling operator \"bpy.ops.export_scene.fbx\" error, could not b"
source_type: "github"
creator: "Roblox"
url: "https://github.com/Roblox/roblox-blender-plugin/issues/57"
published: "2024-08-13"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0023
relevance: 3
density: medium
tags: ["research-source", "github", "blender-roblox-export-import", "other"]
---
# gh-Roblox-roblox-blender-plugin-i57

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
GitHub issue on Roblox's Blender plugin (Aug 2024) where upload shows "Add-on error" with bpy.ops.export_scene.fbx not found. Maintainer could not reproduce on Blender 4.1.1. Reporter says it was fixed without documenting how. A later reporter's cause was an object name containing "/", which the FBX exporter treated as a folder path. Useful as a troubleshooting reference: get the system console log, and name objects without slashes.

## Claims
- c1: Upload in Roblox Blender plugin shows 'Add-on error' in Upload Status; the reported cause was AttributeError: bpy.ops.export_scene.fbx operator could not be found (Blender 4.1). *(doc, high; blender-roblox-export-import)*
- c2: Maintainer could not reproduce the missing export_scene.fbx operator on Blender 4.1.1; the reporter's fix was never documented, and the issue was closed then reopened. *(doc, high; blender-roblox-export-import)*
- c3: Object name containing '/' (e.g. 'Eye/Gem') makes FBX export treat the part before it as a folder; export then fails with file not found. Fix: rename object without slash. *(doc, medium; blender-roblox-export-import)*
- c4: Maintainer said he would open an issue to sanitize exported file names so object names cannot form invalid file system paths. *(doc, medium; blender-roblox-export-import)*
- c5: To get console output on Windows: Window > Toggle System Console. On macOS, start Blender from a terminal to see logs. *(doc, high; blender-roblox-export-import)*
- c6: 'Token has been revoked' error on upload: refresh token revoked by Roblox after a fixed time or on logout; add-on should re-prompt login. Maintainer advised logout and login again; one reporter said this did nothing. *(doc, medium; other)*
- c7: Export writes a temp file at a system temp path named after the object (tmp<random>/<ObjectName>.fbx), so object names feed directly into file paths. *(doc, medium; blender-roblox-export-import)*
- c8: Plugin installs under Blender's scripts/addons/roblox-blender-plugin/ with lib/upload_operator.py and lib/oauth2_client.py, which handle upload and token refresh. *(doc, medium; blender-roblox-export-import)*
- c9: One log reported 'export finished in 0.0000 sec' before the upload error, suggesting the export step failed early. *(data, low; blender-roblox-export-import)*

## Numbers
- n1: **Blender version tested by maintainer**: 4.1.1 (no repro) 
- n2: **Blender versions in reports**: 4.1 and 4.2.2 
- n3: **Issue dates**: opened 2024-08-13; reopened later 

## Techniques
- t1: **Get console log for plugin errors**: Windows: Window > Toggle System Console. macOS: launch Blender from terminal. Run upload, copy traceback from console into the issue.
- t2: **Rename objects to avoid slashes**: If FBX export fails with file-not-found on an object name, rename the object to remove '/' and re-upload.
- t3: **Re-login to fix revoked token**: Log out of the plugin, then log in again to get a new refresh token. Reporter said this did not help in their case.

### Code: Traceback from the first report showing the upload_task failure path (token refresh step)
```text
File "...\scripts\addons\roblox-blender-plugin\lib\upload_operator.py", line 190, in upload_task
    await oauth2_client.refresh_login_if_needed()
File "...\scripts\addons\roblox-blender-plugin\lib\oauth2_client.py", line 245, in refresh_login_if_needed
    new_token_data = await se
```

## Quotes (brief, for attribution)
> the slash / in the object name causing a problem with the export because it thinks the Eye is a folder on the file system rather than part of the file name.  (Roblox)
> If you rename your object to not have a slash in it, it should export with no problem.  (Roblox)

## Contradictions flagged
- Reporter's 'Add-on error' with missing export_scene.fbx operator was resolved by an unnamed fix; a different reporter's error was a slash-in-name file-not-found, not an operator-missing error. (vs Issue title and maintainer framing that the operator-not-found error is the cause)
- Logging out and back in resolves the revoked token error. (vs Reporter says logout and login did nothing)

## Points to
- https://github.com/Roblox/roblox-blender-plugin/issues/57
- https://github.com/Roblox/roblox-blender-plugin
