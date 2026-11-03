---
type: research-source
id: web-a6bc40d729
title: "fixing blender part 2 going deeper"
source_type: "web"
creator: "www.blenderguru.com"
url: "https://www.blenderguru.com/posts/fixing-blender-part-2-going-deeper"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0010
relevance: 0
density: low
tags: ["research-source", "web", "other"]
---
# web-a6bc40d729

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Andrew Price's essay (Part 2 of 'Fixing Blender') on UI principles: feedback timing thresholds (0.1 s click/cursor, 1 s hourglass, 3 s progress bar), error recovery (Ctrl+Z mode-specific), simplicity sub-categories, and goal-oriented design. Off-topic for Blender-Roblox, bpy, MCP, or asset pipeline work.

## Claims
- c1: Source is an Andrew Price (BlenderGuru) UI/UX essay on Blender usability principles; contains no Roblox, bpy, blender-mcp, or FBX/glTF pipeline content. *(doc, high; other)*
- c2: Feedback guideline: button clicks must be acknowledged within 0.1 s; moving/resizing must not lag cursor more than 0.1 s. *(doc, high; other)*
- c3: Feedback guideline: delays over 1 s should show hourglass busy cursor; delays longer than 3 s should show a progress bar. *(doc, high; other)*
- c4: Ctrl+Z in Blender is mode-specific, sometimes reversing data made in a different mode. *(opinion, medium; other)*
- c5: Crash recovery exists in Blender but could be improved with a dialog on reopening (author's mockup). *(opinion, medium; other)*
- c6: Author cites research finding feedback is the #1 influence on user satisfaction. *(doc, low; other)*
- c7: Simplicity has four sub-areas: hierarchy, structure (proximity/similarity), design (larger text, contrasting wireframes), vocabulary (avoid jargon, plain-English tooltips). *(doc, high; other)*
- c8: Goal-oriented design: good interfaces have a shallow 'gulf of execution' that users cross easily; bad ones have deep gulfs. *(doc, high; other)*

## Numbers
- n1: **Button click feedback deadline**: 0.1 s 
- n2: **Cursor lag tolerance for move/resize**: 0.1 s 
- n3: **Busy indicator threshold**: 1 s (hourglass) 
- n4: **Progress bar threshold**: 3 s 

## Quotes (brief, for attribution)
> Feedback is acknowledging users actions and letting them know when the program is busy.  (www.blenderguru.com)

## Points to
- https://www.blenderguru.com/posts/fixing-blender-part-1-why-its-broken
- New Blender UI Proposal (follow-up post)
