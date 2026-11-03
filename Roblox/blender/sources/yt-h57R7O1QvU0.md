---
type: research-source
id: yt-h57R7O1QvU0
title: "How To Make Tools In Roblox Studio"
source_type: "youtube"
creator: "Kingkade 3D"
url: "https://www.youtube.com/watch?v=h57R7O1QvU0"
published: "2026-06-04"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0013
relevance: 1
density: low
tags: ["research-source", "youtube", "other", "rigging-animation"]
---
# yt-h57R7O1QvU0

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Beginner Roblox Studio tutorial on building a working Tool (pickaxe): Tool container, transparent Handle part, WeldConstraints to unanchored parts, grip adjustment via Tool Grip Editor plugin, CanCollide off, and placing the tool in StarterPack. Does not mention Blender, Claude, bpy, blender-mcp, or export/import pipelines. Off-topic for the target subject.

## Claims
- c1: Roblox Tool needs a part named Handle; without it the tool does not work. *(demo, high; other)*
- c2: [1:04] Parts inside a Tool are attached using WeldConstraint with Part0 set to Handle and Part1 set to each other part. *(demo, high; other)*
- c3: [2:27] Tool grip is adjusted with the Tool Grip Editor plugin; the author rotated the grip 90 degrees to hold the pickaxe properly. *(demo, high; rigging-animation)*
- c4: [3:55] Parts must be unanchored, otherwise the tool gets stuck in place when picked up. *(demo, high; other)*
- c5: [4:45] Set CanCollide off on all tool parts so the character does not get pushed upward or stand on the tool. *(demo, high; other)*
- c6: [4:45] Put the finished tool inside StarterPack so players spawn with it. *(demo, high; other)*
- c7: [4:05] Tool swing animation is not included; the author defers it to a separate video. *(doc, medium; rigging-animation)*

## Numbers
- n1: **grip rotation**: 90 degrees Grip rotated 90° in Tool Grip Editor so character holds pickaxe correctly

## Techniques
- t1: **Weld tool parts to Handle**: Add WeldConstraint to Handle; set Part0=Handle, Part1=each other part; duplicate weld and reassign Part1 to speed up.
- t2: **Grip adjustment with Tool Grip Editor**: Select Tool, click Edit Grip in the plugin, move/rotate the grip preview, then close editor and test.
- t3: **Disable CanCollide and use StarterPack**: Select all tool parts, turn CanCollide off, move the Tool into StarterPack.

## Quotes (brief, for attribution)
> You need a handle, otherwise it's just not going to work.  (at 0:41, Kingkade 3D)
> Make sure that the parts are unanchored, otherwise that will happen.  (at 3:55, Kingkade 3D)

## Points to
- Tool Grip Editor plugin
