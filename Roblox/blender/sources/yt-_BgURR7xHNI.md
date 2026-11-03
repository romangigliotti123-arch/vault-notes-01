---
type: research-source
id: yt-_BgURR7xHNI
title: "Faster COMPOSITOR! ✨ Blender Today LIVE #281"
source_type: "youtube"
creator: "Blender"
url: "https://www.youtube.com/watch?v=_BgURR7xHNI"
published: "2026-05-12"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0069
relevance: 1
density: low
tags: ["research-source", "youtube", "claude-blender-ai", "other"]
---
# yt-_BgURR7xHNI

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Blender Today live stream (May 2026) on Blender 5.2 changes. Only tangential to Blender-to-Roblox work. Relevant bits: how to add the online essentials asset library (remote asset library, online access setting), that appended materials get packed and need unpacking to tweak, and the CLI -X flag for factory startup. No Roblox, Claude, MCP or bpy-pipeline content.

## Claims
- c1: [2:30] Blender 5.2 feature window closes about three weeks after stream; beta follows, then 5.2 LTS about a month later. *(opinion, medium; other)*
- c2: [7:15] Online essentials asset library is added via Preferences > Asset Libraries > Remote asset library; in this build remote libraries sat under Experimental. *(demo, medium; other)*
- c3: [14:12] Remote asset library requires System > Online Access enabled; the URL returns Forbidden in a browser because Blender reads a JSON index from it. *(demo, medium; other)*
- c4: [11:25] Appended materials are packed into the scene; to change a material setting like scale, you must make it local or unpack it, since asset-exposed settings have no UI yet. *(demo, medium; other)*
- c5: [22:28] Command-line flag for factory startup changed from lowercase to -X (capital X); useful for running Blender with default settings from scripts. *(doc, medium; claude-blender-ai)*
- c6: [21:21] Single-threaded raycast replacing multi-threaded per-region raycast in polygon hole filling is about 44x faster on a test polygon with 99,000 edges. *(data, medium; other)*
- c7: [1:49] Essentials online assets were expected to change before 5.2 final, and the stream asked viewers to test server load by redownloading. *(opinion, low; other)*

## Numbers
- n1: **speedup**: ~44x single-thread vs old multi-thread raycast polygon fill with holes, 99,000 edges
- n2: **timeline**: ~3 weeks to 5.2 beta feature freeze per host

## Techniques
- t1: **Add remote asset library**: Preferences > Asset Libraries > remote asset library menu > paste library URL > Create. Requires online access enabled in System settings.
- t2: **Unpack material to tweak**: Appended material is packed. Make it local/duplicate or unpack it, then edit the exposed inputs such as scale factor.

## Points to
- Blender roadmap page on blender.org
- Online essentials asset library URL (shared in chat, not in transcript)
- Blender projects commit log (projects.blender.org)
