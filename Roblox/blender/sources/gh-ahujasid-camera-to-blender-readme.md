---
type: research-source
id: gh-ahujasid-camera-to-blender-readme
title: "ahujasid/camera-to-blender README: Take a photo of real objects, and paste them in Blender"
source_type: "github"
creator: "ahujasid"
url: "https://github.com/ahujasid/camera-to-blender"
published: "2026-09-05"
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0228
relevance: 1
density: low
tags: ["research-source", "github", "claude-blender-mcp", "common-mistakes-fixes", "other", "procedural-generation"]
---
# gh-ahujasid-camera-to-blender-readme

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
README for a tool that turns a phone/webcam photo into a 3D model in Blender: photo, optional Gemini background removal, Tripo3D generation, then a WebSocket relay server pushes the model to a Blender add-on. Setup and troubleshooting only. Nothing about Claude, bpy scripting or Roblox export/import.

## Claims
- c1: Pipeline is photo → background removal (Gemini, optional) → Tripo3D image-to-3D → auto-import into Blender; takes about 30–60 seconds per model. *(doc, high; procedural-generation)*
- c2: Tripo3D API key is required for model generation. Gemini key is optional and only used for background removal; leaving it empty uses the photo as-is. *(doc, high; procedural-generation)*
- c3: Requires Python 3.10+ and Blender 3.0+. Phone use needs ngrok because phone cameras require HTTPS. A laptop webcam works at localhost without ngrok. *(doc, high; other)*
- c4: Blender connects through a custom WebSocket add-on (ws_import_addon.zip, N-panel 'WS Import' tab) to a FastAPI/uvicorn relay server. This is not MCP and has no Claude involvement. URL format is wss://<ngrok-host>/ws?client=blender. *(doc, high; claude-blender-mcp)*
- c5: Troubleshooting: 'Failed to send to Blender' means the add-on is not connected (check wss:// scheme and ?client=blender suffix). Free ngrok URLs change on every restart, so Blender must be reconnected. Background removal failures are usually Gemini quota or key problems. *(doc, high; common-mistakes-fixes)*

## Numbers
- n1: **generation time**: ~30–60 s wait after confirming photo before Send to Blender
- n2: **minimum versions**: Python 3.10+, Blender 3.0+ stated requirements
- n3: **default server port**: 8000 PORT env var default

## Techniques
- t1: **Photo-to-3D into Blender via relay**: Run uvicorn relay_server:app on port 8000, run ngrok http 8000, install the add-on zip, paste the wss:// URL with /ws?client=blender in the WS Import panel, click Connect, then take a photo on the phone and tap Send to Blender.

### Code: Start relay server
```bash
uvicorn relay_server:app --host 0.0.0.0 --port 8000
```

### Code: Repackage the Blender add-on after editing source
```bash
zip -r ws_import_addon.zip blender_addon -x "*/__pycache__/*" "*.pyc"
```

## Points to
- Tripo3D API (platform.tripo3d.ai)
- Gemini API (aistudio.google.com)
- ngrok
- ahujasid (author; also known for blender-mcp)
