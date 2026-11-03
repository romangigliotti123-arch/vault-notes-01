---
type: research-source
id: yt-pHlsKz0c-eQ
title: "Blender 2.90 is here! - Scripting Changes!!?"
source_type: "youtube"
creator: "Darkfall"
url: "https://www.youtube.com/watch?v=pHlsKz0c-eQ"
published: "2020-09-08"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0021
relevance: 1
density: low
tags: ["research-source", "youtube", "bpy-scripting-headless", "common-mistakes-fixes"]
---
# yt-pHlsKz0c-eQ

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Darkfall video (Sep 2020) on Blender 2.90 scripting-workspace changes: info-panel log formatting, Ctrl+T toolbar moved right, Highlight Line moved to View menu, and Noise Texture node socket changes that break old node-setup scripts. Shows enabling Developer Extras, Python Tooltips and Edit Source. No Roblox, Claude, MCP or export content.

## Claims
- c1: [0:25] Blender 2.90 Info editor log lines are reformatted with icons to distinguish operator lines, easier to read than prior versions. *(demo, medium; bpy-scripting-headless)*
- c2: [1:06] In 2.90 the Highlight Line option moved from the Text editor's bottom menu to View > Highlight Line. *(demo, medium; bpy-scripting-headless)*
- c3: [1:47] Enabling Developer Extras plus Python Tooltips in Preferences adds Edit Source to the F3 search, which jumps to the add-on script line behind a button. *(demo, high; bpy-scripting-headless)*
- c4: [4:02] In 2.90 the Noise Texture node swaps Color and Factor output positions, so older scripts linking by index are wrong; Roughness input added and Distortion moved down one slot. *(demo, high; bpy-scripting-headless)*
- c5: [4:45] Scripts and add-ons written for earlier Blender versions must be re-tested in 2.9x because node sockets and layout shifted. *(opinion, medium; bpy-scripting-headless)*
- c6: [3:22] A Stylized shader library material showed nothing in 2.90 due to a change; the author deferred the fix to a later video. *(demo, low; common-mistakes-fixes)*

## Techniques
- t1: **Enable Edit Source for script lookup**: Preferences > Add-ons: enable Development Icon Viewer. Preferences > Interface: enable Python Tooltips and Developer Extras. Hover a button, press F3 (or Space), type Edit Source to jump to its script line.

## Points to
- Blender 2.90 release blog (node comparison image referenced)
