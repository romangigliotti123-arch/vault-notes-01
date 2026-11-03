---
type: research-source
id: yt-NHv33D2g-yI
title: "I Built a Blender Add-on Using a 100% FREE AI Agent"
source_type: "youtube"
creator: "CG Python"
url: "https://www.youtube.com/watch?v=NHv33D2g-yI"
published: "2026-06-20"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0017
relevance: 1
density: low
tags: ["research-source", "youtube", "bpy-scripting-headless", "common-mistakes-fixes", "creator-workflows"]
---
# yt-NHv33D2g-yI

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Video showing a free-model AI agent (Gemma 431B in VS Code chat) writing a Blender Python script that creates a stack of cubes, wrapping it in an operator and panel, then packaging it as a Blender extension with blender_manifest.toml. Covers prompt-quality issues and manifest errors. Does not involve Claude, blender-mcp, or Roblox export.

## Claims
- c1: [2:44] Generated bpy script ran only after manually re-running it via VS Code Blender Development extension; first run did nothing, second run created cubes. *(demo, medium; bpy-scripting-headless)*
- c2: [7:31] Free model wrapped operator in legacy add-on format instead of blender_manifest.toml extension format; author attributes this to vague prompting. *(demo, medium; bpy-scripting-headless)*
- c3: [10:22] Blender extension failed to load with 'missing schema version' error; manifest lacked schema_version field. *(demo, high; common-mistakes-fixes)*
- c4: [11:45] Agent set manifest type to 'built-in' instead of 'add-on'; pasting the Blender docs manifest example fixed type and prompted a license field requirement. *(demo, high; common-mistakes-fixes)*
- c5: [11:04] Author's opinion: cheaper models need pasted documentation examples and explicit field lists in prompts; one-line prompts are insufficient. *(opinion, medium; creator-workflows)*
- c6: [8:58] Model got stuck repeating text in long chats; starting a new chat fixed it. *(demo, medium; creator-workflows)*
- c7: [13:07] Author estimates the free-model output gets roughly 95% of the way, needing hand-holding. *(opinion, low; creator-workflows)*

## Numbers
- n1: **model**: Gemma 4 31B (free, VS Code chat) 
- n2: **cubes in stack**: 3 (initial), count controlled by operator 

## Techniques
- t1: **Paste docs example into prompt**: Copy the Blender manifest example from the official docs into the agent chat along with the target file. Agent corrected type and identified missing license field.
- t2: **Fresh chat on loop**: When the agent repeats output, start a new chat and re-provide the file context.

### Code: Manifest fields the agent was missing (per video; exact values not shown in full)
```text
schema_version = "1.0.0"
type = "add-on"
license = [...]
# id, version, name, tagline, blender_version_min also required by the manifest format
```

## Points to
- Blender Development VS Code extension
- Blender manifest documentation (blender_manifest.toml)
