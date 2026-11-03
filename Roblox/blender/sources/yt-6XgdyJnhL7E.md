---
type: research-source
id: yt-6XgdyJnhL7E
title: "SO MANY Quality of Life Improvements! — Blender Today LIVE #273"
source_type: "youtube"
creator: "Blender"
url: "https://www.youtube.com/watch?v=6XgdyJnhL7E"
published: "2026-01-20"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0056
relevance: 1
density: low
tags: ["research-source", "youtube", "claude-blender-ai", "other"]
---
# yt-6XgdyJnhL7E

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Blender Today #273 (Jan 2026) changelog walkthrough. Almost entirely off-topic for Roblox export and Claude/MCP workflows. Only bpy-relevant items: new bpy.app.cache_dir property (for remote asset libraries, targeted for 5.2) and a pre-exit Python handler. No Roblox, FBX/glTF, MCP, or Open Cloud content.

## Claims
- c1: [1:30:42] Blender 4.5.6 LTS and 4.2.17 LTS were released on the day of the stream (Jan 2026), with fixes; not yet announced publicly. *(doc, medium; other)*
- c2: [46:12] New bpy.app.cache_dir property added alongside bpy.app.tempdir, needed for the remote/online asset library system; not in 5.1, expected in 5.2 as experimental. *(doc, high; claude-blender-ai)*
- c3: [46:54] New Python handler exit_pre runs before Blender quits; presenter says the older Python atexit-style hook ran when Blender data was already invalid, so exit_pre is safer. *(doc, medium; claude-blender-ai)*
- c4: [1:32:48] Blender 5.1 release planned for March 17, 2026; 5.2 LTS planned for July; LTS releases get about 2 years of bug fixes. *(doc, medium; other)*
- c5: [17:36] Presenter's advice (opinion): a production starting on 4.5 LTS should move to 5.0 because it is more future-proof than staying on 4.5. *(opinion, low; other)*
- c6: [23:31] Blender 5.1 default compositor workspace changes to put a viewer/image editor in place of the large backdrop-and-dope-sheet layout. *(doc, medium; other)*
- c7: [5:15] Shape key evaluation roughly 2x faster in a simple high-poly test (about 19 ms to 8 ms), less gain with animation (9.8 to 9.3 ms). *(data, medium; other)*

## Numbers
- n1: **shape key evaluation time**: 19 ms -> 8 ms (simple high-poly test) Presenter's example; animated case 9.8 ms -> 9.3 ms
- n2: **LTS support length**: about 2 years Presenter's description of LTS bug-fix window
- n3: **Blender 5.1 release date**: March 17, 2026 (planned) Stated in closing; beta and 5.2 alpha expected Feb 3

## Points to
- blender.org extensions platform
- code.blender.org
- Blender Development Fund
