---
type: research-source
id: gh-ahujasid-camera-to-blender-i1
title: "ahujasid/camera-to-blender#1 Add-on fails to enable: \"No module named 'websocket'\""
source_type: "github"
creator: "ahujasid"
url: "https://github.com/ahujasid/camera-to-blender/issues/1"
published: "2026-09-05"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0009
relevance: 1
density: medium
tags: ["research-source", "github", "claude-blender-mcp", "common-mistakes-fixes"]
---
# gh-ahujasid-camera-to-blender-i1

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
GitHub issue on ahujasid/camera-to-blender: a Blender add-on fails to enable with "No module named 'websocket'". Cause: websocket-client installed via pip into system Python, not Blender's bundled Python. Workaround: install websocket-client with Blender's own python.exe into the user scripts/modules folder. Not about Roblox; little relevance to the Blender-to-Roblox pipeline.

## Claims
- c1: Blender add-on (camera-to-blender, WS Import) fails to enable with 'No module named websocket' because pip installs into system Python, not Blender's bundled Python. *(doc, high; claude-blender-mcp)*
- c2: Fix: run Blender's bundled python -m pip install --target into the user scripts/modules folder with websocket-client==1.7.0; no admin rights needed; reported working on Blender 5.2. *(experience, medium; common-mistakes-fixes)*
- c3: Reporter's environment: Blender 5.2 on Windows 11, bundled Python 3.13, add-on version 0.1.0. *(doc, high; claude-blender-mcp)*
- c4: README omits the step to install dependencies into Blender's Python; suggested fix is documenting the command or vendoring websocket-client in the add-on zip. *(opinion, medium; common-mistakes-fixes)*

## Numbers
- n1: **Blender version**: 5.2 (bundled Python 3.13) 
- n2: **Add-on version**: 0.1.0 
- n3: **websocket-client pinned version**: 1.7.0 

## Techniques
- t1: **Install deps into Blender's Python**: Run <blender>/python/bin/python.exe -m pip install --target <user scripts/modules> websocket-client==1.7.0, restart Blender, then enable the add-on.

### Code: Install websocket-client into Blender's bundled Python user modules folder (Windows workaround from issue)
```bat
"C:\Program Files\Blender Foundation\Blender 5.2\5.2\python\bin\python.exe" -m pip install --target "%APPDATA%\Blender Foundation\Blender\5.2\scripts\modules" websocket-client==1.7.0
```

## Points to
- https://github.com/ahujasid/camera-to-blender
