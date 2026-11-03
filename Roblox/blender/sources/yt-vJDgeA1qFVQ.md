---
type: research-source
id: yt-vJDgeA1qFVQ
title: "Blender Python Tutorial: Why is it not Working? : Episode 2 [learn python for beginners]"
source_type: "youtube"
creator: "Darkfall"
url: "https://www.youtube.com/watch?v=vJDgeA1qFVQ"
published: "2021-02-18"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0011
relevance: 1
density: low
tags: ["research-source", "youtube", "automation-and-creator-workflows", "claude-blender-ai"]
---
# yt-vJDgeA1qFVQ

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Short Blender Python tutorial (5:10) on building custom N-panel UI in the Scripting workspace. Shows layout.prop with a bpy.data.particles reference, using tooltips to find data paths, and hiding options with an if statement. Nothing on Claude, blender-mcp, FBX/glTF export, or Roblox. Only tangentially relevant to the topic.

## Claims
- c1: [0:00] Video is a generic Blender Python tutorial on adding UI properties to a custom side panel (N-panel); it does not cover Claude, blender-mcp, or Roblox export. *(demo, high; automation-and-creator-workflows)*
- c2: [2:25] Panel code pattern: create a reference like p_data = bpy.data.particles['<name>'] then layout.prop(p_data, 'count') to expose a particle setting in a panel. *(demo, high; claude-blender-ai)*
- c3: [4:10] Conditional UI: wrap dependent layout.prop calls in 'if p_data.use_rotations == True:' so they hide when the checkbox is off. *(demo, high; claude-blender-ai)*
- c4: [1:56] Hovering a property shows a tooltip containing the equivalent bpy data path (e.g. bpy.data.particles[...].count), which is used to write the script; tooltips must be enabled in Preferences. *(demo, medium; automation-and-creator-workflows)*

## Numbers
- n1: **particle count example value**: 1000 

## Techniques
- t1: **Tooltip-to-bpy path lookup**: Hover a UI property, read the Python path in tooltip (bpy.data.particles[name].count), copy into script, use layout.prop with that data reference.
- t2: **Conditional panel rows**: Put dependent layout.prop lines under an if on the controlling boolean so they vanish when it is off.

### Code: Expose a particle setting in a custom panel and hide dependent options via an if statement
```python
p_data = bpy.data.particles['ParticleSettings']
layout.prop(p_data, 'count')
layout.prop(p_data, 'use_rotations')
if p_data.use_rotations == True:
    layout.prop(p_data, 'rotation_factor_random')
```

## Quotes (brief, for attribution)
> we have bpy.data.particles then the name of the particle system dot count equals 1000  (at 1:56, Darkfall)

## Points to
- Darkfall blog post (template script link, not provided in transcript)
