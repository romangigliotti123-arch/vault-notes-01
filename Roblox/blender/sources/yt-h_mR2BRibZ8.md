---
type: research-source
id: yt-h_mR2BRibZ8
title: "New Insane AI Animation Workflow with GPT-6 Astra"
source_type: "youtube"
creator: "Stefan 3D AI"
url: "https://www.youtube.com/watch?v=h_mR2BRibZ8"
published: "2026-09-14"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0024
relevance: 2
density: low
tags: ["research-source", "youtube", "claude-blender-ai", "mesh-texture-limits", "other", "rigging-animation"]
---
# yt-h_mR2BRibZ8

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Creator video on using GPT-6 "Astra" via Codex CLI with the official Blender MCP to rig and animate a non-humanoid scorpion for a Unity RTS game, not Roblox. Teaches part-based low-poly modeling in Tripo P2, video-AI animation references, and iterative feedback. No Roblox export, scale, or limit details.

## Claims
- c1: [0:48] Generating a creature in one shot from image yields one solid mesh that causes weighting problems; generate parts separately, then assemble in Blender. *(experience, medium; claude-blender-ai)*
- c2: [2:10] Logically organized, low-poly meshes are easier for the AI to rig; rigging is adding bones and distributing weights; excess polys and messy topology cause artifacts. *(opinion, medium; claude-blender-ai)*
- c3: [6:23] Video AI (Seedance 2.5 via API) generated reference clips; the GPT agent then used them frame by frame to pose and animate the rig. Needed about two iterations per animation. *(experience, medium; rigging-animation)*
- c4: [7:04] Seedance 2.5 minimum clip length cited as 3 to 4 seconds, so generate longer and rescale in time later. *(experience, medium; rigging-animation)*
- c5: [7:59] Codex CLI was run in the game project folder with permissions bypassed, so the agent sees project files and the MCP setup; Blender is driven via MCP, not computer use. *(experience, medium; claude-blender-ai)*
- c6: [7:59] Minimum setup is the official Blender MCP; other MCP servers giving full Blender access are alternatives. *(doc, medium; claude-blender-ai)*
- c7: [9:13] Agent ran repeated self-tests in Blender, similar to its Unity testing loop; first rig and animations were produced in about 30 minutes. *(experience, low; claude-blender-ai)*
- c8: [9:54] Feedback that worked: tail made temporarily bigger for a few frames at contact; screenshots plus text notes on leg symmetry and body posture. *(experience, medium; rigging-animation)*
- c9: [10:58] Total time for all animations was about two hours on GPT-6 Astra x-high; walk and run cycles loop cleanly, and idle was cut shorter for in-game pacing. *(experience, low; rigging-animation)*
- c10: [4:10] Parts were unwrapped and packed into a single texture atlas, to minimize texture maps for a small on-screen RTS unit. *(experience, medium; mesh-texture-limits)*
- c11: [3:30] Separate object and material was used for the team-color crest so its color can be swapped in-game. *(experience, medium; mesh-texture-limits)*
- c12: [12:44] Final rigged creature was imported into Unity (not Roblox) and tested in a playground scene; the workflow does not cover Roblox Studio or FBX export. *(experience, high; other)*

## Numbers
- n1: **Tripo low-poly generation**: ~500 polys per part (quad topology) 
- n2: **Animation iterations**: 2 per animation 
- n3: **Video-AI minimum clip length**: 3 to 4 seconds 
- n4: **Attack cadence in game**: 1.6 seconds 
- n5: **Total animation time**: ~2 hours 

## Techniques
- t1: **Part-based generation and assembly**: Generate each part (e.g., one leg) as a low-poly mesh, bring into Blender, assemble with proportional editing and elastic wrap, keep parts as separate objects.
- t2: **Video reference to agent animation**: Generate reference video with a video AI, pass it to the agent, have it pose the rig frame by frame, then give screenshot and text feedback and iterate.
- t3: **Exaggerate contact frames**: Temporarily scale a feature (e.g., tail) up for a few frames at impact to make hits read clearly.
- t4: **Trim idle loop for game pacing**: Ask the agent to cut the long animation to a shorter frame range that still loops well.

## Quotes (brief, for attribution)
> you can see I use Codec CLI. Many ask like why? Because it works in folder and it's much easier to manage all this MCP and stuff.  (at 7:59, Stefan 3D AI)
> when it is presented as one big mesh it will cause problems with weights.  (at 0:48, Stefan 3D AI)

## Points to
- Tripo P2 (Tripo 3D)
- Seedance 2.5
- Codex CLI
- official Blender MCP
- Unity
