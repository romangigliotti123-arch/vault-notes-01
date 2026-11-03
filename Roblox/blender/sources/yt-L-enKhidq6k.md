---
type: research-source
id: yt-L-enKhidq6k
title: "How to Build Claude Editing Teams Better Than 99% of People"
source_type: "youtube"
creator: "Aidan Stanik"
url: "https://www.youtube.com/watch?v=L-enKhidq6k"
published: "2026-08-11"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0023
relevance: 0
density: low
tags: ["research-source", "youtube", "automation-and-creator-workflows", "blender-roblox-export-import", "claude-blender-ai", "other"]
---
# yt-L-enKhidq6k

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Transcript is a Claude Code video-editing agent project (silence, mistake, verify, motion graphics via HyperFrames, B-roll agents) with a free Whisper setup. It does not cover Blender, blender-mcp, bpy, or Roblox export. Relevance to the Blender-for-Roblox topic is near zero; only the general Claude-agent workflow pattern is reusable.

## Claims
- c1: [0:00] Video is about a Claude Code multi-agent video editing project ("editing OS"), not Blender or Roblox; no bpy, blender-mcp, or Roblox export content. *(doc, high; other)*
- c2: [2:15] Editing OS uses skills in a .claude directory; agents include cut silences, cut mistakes, verify cuts, motion graphics (HyperFrames, Remotion alternative), and insert B-roll. *(demo, high; automation-and-creator-workflows)*
- c3: [6:13] Setup is driven by telling Claude 'I want to set up my editing OS'; it checks environment, installs HyperFrames, and asks for API keys in a .env file. *(demo, medium; automation-and-creator-workflows)*
- c4: [7:35] Free alternative to ElevenLabs is local Whisper for transcription used by silence, mistake, and verify agents. *(demo, medium; automation-and-creator-workflows)*
- c5: [8:42] Editing a video is started by giving Claude the local file path (copied via right-click with Option on Mac) and asking to run the full editing pipeline. *(demo, medium; automation-and-creator-workflows)*
- c6: [9:24] Split-screen input (screen left, webcam right) is detected; output set to 1920x1080 for YouTube via HyperFrames. *(demo, medium; automation-and-creator-workflows)*
- c7: [12:22] On a 7:15 source, silence and mistake cuts reduced runtime to about 3:35 with six cuts approved. *(demo, medium; automation-and-creator-workflows)*
- c8: [13:15] Motion graphics agent analyzed 1,136 HyperFrames style cards from a style library; nine pre-installed styles are offered. *(doc, medium; automation-and-creator-workflows)*
- c9: [3:10] Pipeline order: silence cut, mistake cut, verify pass (run three times against a regenerated transcript), motion graphics, then optional B-roll. *(doc, medium; automation-and-creator-workflows)*
- c10: [4:32] B-roll scout pulls from Pinterest, Pixabay, and stock video/image sites, using the user's own API keys. *(doc, low; automation-and-creator-workflows)*
- c11: [0:00] Source gives no blender-mcp, bpy, or blender -b instructions; Blender is not mentioned in the transcript. *(doc, high; claude-blender-ai)*
- c12: [0:00] Source contains no Roblox Studio, FBX/glTF, MeshPart, or scale/axis guidance. *(doc, high; blender-roblox-export-import)*
- c13: [1:20] Author's opinion: using a Claude Code subscription with VS Code or Claude desktop app is the prerequisite; Codex is an alternative. *(opinion, medium; other)*

## Numbers
- n1: **Runtime after silence/mistake cuts**: ~3:35 from 7:15 (six cuts) 
- n2: **Style cards analyzed**: 1,136 
- n3: **Verify pass runs**: 3 
- n4: **Pre-installed motion styles**: 9 

## Quotes (brief, for attribution)
> It will then run this pass three separate times and challenge it against a transcript it generated off of your no silence and no mistake video.  (at 3:10, Aidan Stanik)
> That will then install Whisper on your computer for the agents to use for the cut silences, cut mistakes, and the verifying passing agent.  (at 7:35, Aidan Stanik)

## Points to
- HyperFrames
- Remotion
- ElevenLabs
- Whisper
- Higgsfield
- Pixabay
- Pexels
- Pinterest
- Creative AI Network
