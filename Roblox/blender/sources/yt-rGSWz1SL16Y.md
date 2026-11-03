---
type: research-source
id: yt-rGSWz1SL16Y
title: "Use THIS For Easy Blender Scripting"
source_type: "youtube"
creator: "CG Python"
url: "https://www.youtube.com/watch?v=rGSWz1SL16Y"
published: "2024-04-08"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0016
relevance: 1
density: low
tags: ["research-source", "youtube", "bpy-scripting-headless", "common-mistakes-fixes", "creator-workflows"]
---
# yt-rGSWz1SL16Y

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Video on using GitHub Copilot (in VS Code) to write and refactor Blender Python add-ons. Shows explaining code, generating a cube/icosphere operator, adding it to a pie menu, line comments, and splitting code into functions. Live reload via the Blender Development extension in Blender 4.1. No Claude, Roblox, or MCP content.

## Claims
- c1: [1:32] AI assistant generated a bpy operator that calls primitive cube add inside execute(); user then registered it and added it to a pie menu draw layout. *(demo, high; bpy-scripting-headless)*
- c2: [3:36] Generated operator poll required an active object, blocking execution on empty scene; user changed it to check for none so it runs with no active object. *(demo, high; common-mistakes-fixes)*
- c3: [0:16] Live workflow: VS Code with Blender Development extension connected to running Blender 4.1 lets you edit add-on code and reload it in Blender. *(demo, medium; bpy-scripting-headless)*
- c4: [5:18] Assistant commented every line of a light-rig script; user judged output accurate but wordy and undid it. *(demo, medium; bpy-scripting-headless)*
- c5: [6:40] Assistant split a light-rig script into a main function plus helper functions; it was more split than the user wanted, and the script still ran in Blender. *(demo, medium; bpy-scripting-headless)*
- c6: [6:40] Blender Development extension did not support a removed code part (the user had to delete it before running). *(demo, low; common-mistakes-fixes)*
- c7: [4:08] Assistant autocompleted the register call and the pie-menu line from context; the presenter called it better than any autocomplete he had used (opinion). *(opinion, low; bpy-scripting-headless)*
- c8: [7:28] Setup: GitHub account, Copilot free trial, VS Code, Copilot extension; presenter says Copilot is based on GPT-4. Presenter states no sponsorship. *(doc, medium; creator-workflows)*
- c9: [8:10] Presenter plans to restore an old add-on that fails in the latest Blender release using the assistant. *(demo, low; bpy-scripting-headless)*

## Numbers
- n1: **Blender version**: 4.1 
- n2: **Model behind assistant**: GPT-4 (per presenter) 

## Techniques
- t1: **Assistant-generated operator + pie menu registration**: Ask assistant for bpy operator creating cube; insert into add-on; register; add layout.operator line in pie draw(); save; reload add-ons in Blender.
- t2: **Refactor via selection prompts**: Select code, use inline assistant prompt (Ctrl+I) to comment lines or split into functions; accept or undo.

### Code: Operator added by the assistant (as described in the video, not shown verbatim)
```python

```

## Quotes (brief, for attribution)
> GitHub co-pilot is actually based on GPT 4 you can think of it as Chad GPT but really tailored for the coding problems  (at 8:10, CG Python)

## Points to
- GitHub Copilot
- Blender Development extension (VS Code)
- Visual Studio Code
