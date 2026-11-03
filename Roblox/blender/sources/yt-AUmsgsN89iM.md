---
type: research-source
id: yt-AUmsgsN89iM
title: "Vtubing Using EEVEE/Cycles DLSS — BCON26"
source_type: "youtube"
creator: "Blender"
url: "https://www.youtube.com/watch?v=AUmsgsN89iM"
published: "2026-09-25"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0029
relevance: 1
density: low
tags: ["research-source", "youtube", "common-mistakes-fixes", "creator-workflows", "rigging-animation"]
---
# yt-AUmsgsN89iM

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
BCON26 talk by a Taiwanese VTuber-character studio (Holo Digital) on a Blender add-on, called "Yugo" in the transcript, that runs live VTubing inside Blender: VRM models, iFacial mocap, toon shading preset, Twitch/YouTube/Discord triggers, live-streamed from Taipei. No Roblox, Claude, blender-mcp or bpy content.

## Claims
- c1: [2:09] Speaker's stylized back-face-culling anime face looked correct in Blender but broke in Unity under different lighting, forcing either a custom Unity shader or abandoning the look. *(experience, medium; common-mistakes-fixes)*
- c2: [7:55] Add-on has three goals: drive VRM models, receive and combine body and face motion data, and run real-time physics, all editable while streaming. *(demo, medium; creator-workflows)*
- c3: [10:02] iFacial Mocap node supplies facial data; for upper-body VTube streaming this alone drives character reactions. *(demo, medium; creator-workflows)*
- c4: [10:43] VRM data is used as a shortcut for bone maps and expression maps so non-VRM characters can also be driven, and body parts such as neck or root can be hidden per source. *(demo, medium; rigging-animation)*
- c5: [12:05] Toon preset recreates popular Unity toon looks with rim lighting, object-drawn shadows, depth and ID passes, and environment colour blending; heavy load sits on the CPU. *(demo, medium; creator-workflows)*
- c6: [9:19] Audience input from Twitch, YouTube or Discord APIs can trigger scene events, and a lighter material preset is offered for performance. *(demo, medium; creator-workflows)*
- c7: [6:51] Timeline keyframes can trigger animations during a live stream without disrupting real-time motion capture. *(demo, medium; creator-workflows)*
- c8: [15:09] Sidebar controls in the 3D viewport target non-Blender users; the node system targets advanced users. *(doc, medium; creator-workflows)*
- c9: [15:50] Planned motion sources beyond VRM include Rokoko, Mocopi, Leap Motion and SteamVR; current build supports only VRM. *(doc, high; rigging-animation)*
- c10: [17:13] Speaker's opinion: Blender could become a real-time engine for virtual stage and live production. *(opinion, low; creator-workflows)*
- c11: [21:15] Live demo stalled from a crashed music program on the remote PC, which was restarted mid-session; live reliability was an issue. *(demo, high; common-mistakes-fixes)*
- c12: [27:09] Add-on is not yet public; GitHub repo was still private at the talk, and no QR code was available. *(doc, high; creator-workflows)*
- c13: [28:14] Speaker says the Warudo app already offers the same collision effect between Discord-driven objects and the VTuber model. *(opinion, low; creator-workflows)*

## Numbers
- n1: **Add-on goals**: 3 
- n2: **Supported motion sources at talk time**: 1 (VRM); 4 planned 

## Techniques
- t1: **VRM bone/expression mapping**: Load VRM data to auto-fill bone and expression maps, then drive non-VRM rigs by setting bone map and expression map values in nodes.
- t2: **Timeline-triggered events during live stream**: Set keyframes on the Blender timeline as triggers, then play the timeline while capture runs to fire events.
- t3: **Compositor toon stack**: Combine rim light, object-drawn shadows, depth and ID passes and environment colour blending in the compositor to fake Unity toon shading.

## Points to
- Warudo
- MMD Tools (Blender add-on)
- iFacial Mocap
- VRM format
- Rokoko
- Mocopi
- Leap Motion
- SteamVR
- Holo Digital website (named in talk)
