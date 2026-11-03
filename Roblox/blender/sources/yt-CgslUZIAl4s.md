---
type: research-source
id: yt-CgslUZIAl4s
title: "From Idea to Game in ONE Day with AI - Fastest Character Workflow"
source_type: "youtube"
creator: "Stefan 3D AI"
url: "https://www.youtube.com/watch?v=CgslUZIAl4s"
published: "2026-10-05"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0023
relevance: 1
density: low
tags: ["research-source", "youtube", "claude-blender-ai", "mesh-texture-limits", "other", "rigging-animation"]
---
# yt-CgslUZIAl4s

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
AI character workflow video (Stefan 3D AI), not Roblox-specific. Covers splitting a character into parts, generating models in Tripo with several poly-count variants, using Smart UV before AI texturing, generating normal/roughness/metallic maps from color maps with an agent, Mixamo rigging, and a Unity-based game integration. No blender-mcp, bpy, FBX/glTF or Roblox export details.

## Claims
- c1: [1:20] Tripo generation with Smart UV can return four outputs per run; author sets four different poly counts within a range to compare wireframe density. *(demo, medium; mesh-texture-limits)*
- c2: [2:00] Clean Smart UV layout is required before AI texturing; author says poor UV islands make AI-generated maps (normal, roughness, metallic, AO) fail or look wrong. *(opinion, medium; mesh-texture-limits)*
- c3: [2:41] For highly detailed wings, generating from a less-detailed image then texturing from it avoids the model turning every feather into geometry, giving cleaner wireframe. *(demo, low; mesh-texture-limits)*
- c4: [4:52] Part assembly in Blender took about 12 minutes; author says the same step could be done by an AI agent but is slower for him. *(experience, medium; other)*
- c5: [5:00] Author generates normal, roughness and sometimes metallic maps from the color map via an AI agent instead of high-poly sculpting and baking, which he says saves roughly 4-6 hours. *(experience, low; mesh-texture-limits)*
- c6: [6:21] AI-generated PBR maps may need several iterations (e.g., too shiny or reflective on metal parts) and guided prompts. *(experience, medium; mesh-texture-limits)*
- c7: [7:30] Body is rigged with Mixamo without hair or wings; hand fingers optional for an RTS unit; weights are adjusted manually to 100% on specific bones. *(experience, medium; rigging-animation)*
- c8: [9:12] Animations are authored in a Claude Code CLI session using a skills repo (version 4.14); reference sources include Mixamo and AI video generation, the latter used sparingly for cost. *(experience, low; rigging-animation)*
- c9: [10:34] Agent-built preview add-on lets the author switch animations, set poses, and save pose references that the agent reuses in later prompts. *(demo, low; claude-blender-ai)*
- c10: [10:50] VFX are planned via generated HTML visualizations, timed to animation length, then added to the game by a separate agent in Unity, not Roblox Studio. *(demo, low; other)*

## Numbers
- n1: **poly-count variants per Tripo generation**: 4 Four outputs per generation, each with a different poly count
- n2: **assembly time**: 12 minutes Part positioning and small fixes in Blender
- n3: **manual baking time avoided**: 4-6 hours Author's estimate for high-to-low poly baking workflow
- n4: **animation session time**: ~2 hours Full animation set via agent session
- n5: **skills version**: 4.14 Animation skills pack referenced by author

## Techniques
- t1: **Multi-density generation**: Pick a poly range, set four different target counts in Tripo, compare wireframes, keep the best density.
- t2: **Smart UV before AI texturing**: Run Smart UV on each part, generate four layouts, choose cleanest island layout, then texture so AI can map normal/roughness/metallic from color.
- t3: **Image-first wing generation**: Create a low-detail image of the wing, generate the 3D model from it, then texture from the same image to avoid feather geometry.
- t4: **Color-to-PBR map generation**: Feed color map to an image-capable model to produce normal, roughness, metallic; iterate prompts on reflectivity.
- t5: **Pose reference by example**: Pose the rig in a preview tool, save pose reference, and prompt the agent to match that pose instead of describing it in words.

## Quotes (brief, for attribution)
> nice UV allow you so much options. To do image editing on top.  (at 2:00, Stefan 3D AI)
> if the UV will suck, because again, like what you see, these islands is more or less readable for AI  (at 5:41, Stefan 3D AI)

## Points to
- Tripo (Tripo3D model generator)
- Mixamo
- Moondiff (texture tool, referenced)
- GitHub skills workspace (author's, free)
- Unity (game integration, not Roblox)
