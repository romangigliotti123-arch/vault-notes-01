---
type: research-source
id: yt-hb14MxhZiOU
title: "How Server Authority works on Roblox"
source_type: "youtube"
creator: "Roblox Creators"
url: "https://www.youtube.com/watch?v=hb14MxhZiOU"
published: "2026-07-08"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0018
relevance: 1
density: low
tags: ["research-source", "youtube", "other"]
---
# yt-hb14MxhZiOU

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox Creators video (Ducks Yellow interviews Roblox senior engineer Jason) on Server Authority: server runs humanoid movement, client-side prediction hides latency, smoothing via linear interpolation (lerp). Off-topic for Blender/bpy/Claude pipeline; only tangential Roblox networking content.

## Claims
- c1: [0:28] Server authority runs humanoid movement on server; client sends only inputs; client-side prediction hides latency. *(doc, high; other)*
- c2: [3:28] With server authority enabled (one Studio workspace setting), speed/fly/jump hacks are blocked for humanoid movement. *(demo, medium; other)*
- c3: [7:31] Network ownership was the legacy way to give clients physics control; server-only physics causes roughly 100 ms lag on kicks. *(doc, medium; other)*
- c4: [11:48] Smoothing uses simple linear interpolation (lerp) between last server position and predicted position to hide jumps. *(doc, medium; other)*
- c5: [13:50] Open-source templates referenced: city, racing and FPS templates; docs searchable via 'server authority Roblox'. *(doc, low; other)*

## Numbers
- n1: **latency of server-only kick**: ~100 ms 
- n2: **player input latency range**: 50-100 ms 

## Techniques
- t1: **Client-side prediction**: Send player inputs to server; client immediately renders predicted result; reconcile with authoritative server state.
- t2: **Linear interpolation smoothing**: When server corrects a long-distance position jump, lerp from last shown position to new position over time.

## Quotes (brief, for attribution)
> you toggle one setting on the top of your workspace in Roblox Studio. And now all humanoid movement is going through this server authority system.  (at 5:17, Roblox Creators)

## Points to
- Roblox Studio workspace setting for server authority
- Roblox docs on server authority (search 'server 30 Roblox')
- City template, racing template, FPS template (open source)
