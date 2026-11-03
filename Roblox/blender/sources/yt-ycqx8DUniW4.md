---
type: research-source
id: yt-ycqx8DUniW4
title: "How to Make a Boss Fight in Roblox Studio (Parry, Dodge, Stun & Rage Phase) – Beginner Tutorial"
source_type: "youtube"
creator: "MrWonderHow"
url: "https://www.youtube.com/watch?v=ycqx8DUniW4"
published: "2026-09-26"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0023
relevance: 0
density: low
tags: ["research-source", "youtube", "other", "rigging-animation"]
---
# yt-ycqx8DUniW4

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Beginner Roblox Studio tutorial building a crab boss fight: boss AI, parry/dodge/critical combat, awaken phase, VFX, HUD, R6/R15 support. Contains no Blender, bpy, blender-mcp, Claude, FBX/glTF export, or Roblox mesh-import content. Only tangential notes on animation event markers and rig naming.

## Claims
- c1: [0:13] Video covers Roblox Studio boss-fight scripting only; no Blender, Claude, blender-mcp, bpy, or Blender-to-Roblox export content. *(doc, high; other)*
- c2: [1:57] Animation event markers inside published animations trigger damage and VFX at the right moment; event names must match the scripts exactly. *(doc, high; rigging-animation)*
- c3: [2:54] Author says bones with attachments plus rigid constraints are used for glowing eye parts instead of welds, because welds do not follow moving bones. *(experience, medium; rigging-animation)*
- c4: [20:59] Setup breaks on naming: model must be named 'crab boss_rig' with 'crab boss' as primary part; VFX attachment, sound, and event names must match exactly. *(doc, high; other)*
- c5: [20:19] R6 testing: set game settings Avatar to R6 and replace the starter character with an R6 character. *(doc, medium; rigging-animation)*
- c6: [19:05] Game values in demo: parry gives 25 energy, dodge gives 35 energy, awaken triggers below 35% boss health, boss respawns 10 s after death. *(doc, medium; other)*

## Numbers
- n1: **parry energy reward**: 25 
- n2: **dodge energy reward**: 35 
- n3: **awaken threshold (boss health)**: below 35% 
- n4: **boss respawn delay after death**: 10 seconds 

## Techniques
- t1: **Animation event markers**: Add named event markers to the animation at the hit frame; server/client scripts listen for the event name and trigger damage or VFX. Publish the animation and copy its ID into a config module.
- t2: **Bone-attached part via rigid constraint**: Add an attachment to a body bone, add a second attachment in the part, connect them with a RigidConstraint so the part follows the animated bone.

## Quotes (brief, for attribution)
> Make sure the event names are spelled exactly as shown on screen.  (at 1:57, MrWonderHow)

## Contradictions flagged
- Video title promises Blender 3D with Claude and the Blender-to-Roblox pipeline. (vs Transcript is entirely Roblox Studio scripting for a boss fight; no Blender or Claude steps appear.)

## Points to
- Crab boss model and animations (linked in video description)
- R15 and R6 player animations (linked in video description)
- Roblox Toolbox 'VFX pack' (free)
