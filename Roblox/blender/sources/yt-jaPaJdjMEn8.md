---
type: research-source
id: yt-jaPaJdjMEn8
title: "Protecting Creative Momentum: When the 'Wrong' Way Is the Right Way — BCON26"
source_type: "youtube"
creator: "Blender"
url: "https://www.youtube.com/watch?v=jaPaJdjMEn8"
published: "2026-09-25"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0043
relevance: 1
density: low
tags: ["research-source", "youtube", "automation-and-creator-workflows", "avatar-ugc-accessories", "other", "rigging-animation"]
---
# yt-jaPaJdjMEn8

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Personal talk about an Akira-homage animation made in Blender with EEVEE, not Roblox. Covers burnout from a multi-app pipeline (Cycles, MetaHuman, Marvelous Designer, asset packs) and a simplified EEVEE-only return. Only tangential: MPFB, AutoRig Pro, Poly Hammer, and a cloth sim exported as Alembic-style cache. No blender-mcp, bpy, Roblox export, or Claude content.

## Claims
- c1: Source does not mention Claude, blender-mcp, bpy scripting, Roblox Studio, FBX/glTF export, or any Blender-to-Roblox pipeline steps. *(doc, high; other)*
- c2: [8:01] Speaker says a multi-app asset pipeline (decision tree, conversions, export paths) consumed his evenings and caused burnout; he calls this opinion-based experience, not a measured result. *(experience, medium; automation-and-creator-workflows)*
- c3: [6:38] Poly Hammer plugin imports MetaHuman characters from Unreal Engine into Blender; early in development, required GitHub token setup and manual export/import, and MetaHuman meshes were dense. *(experience, medium; avatar-ugc-accessories)*
- c4: [6:38] Speaker used MPFB (MakeHuman plugin for Blender) for characters and AutoRig Pro for rigging; both kept in final pipeline. *(experience, medium; rigging-animation)*
- c5: [27:23] Cloth sim made in Blender was exported as an Alembic-style cache (transcript says 'Olympic', likely a transcription error) and played back without lag with subdivision enabled. *(experience, low; other)*
- c6: [30:49] EEVEE light Influence panel lets per-light volume scatter and glossy be adjusted without changing light intensity or color; negative light values still work in the latest EEVEE build. *(demo, medium; other)*
- c7: [12:51] Speaker reports EEVEE took about 12 s per frame versus about 2 min per frame in Cycles for his scenes, so he rejected Cycles. *(experience, low; other)*

## Numbers
- n1: **render time per frame**: 12 s EEVEE vs 2 min Cycles Speaker's own scenes; reason for rejecting Cycles
- n2: **Marvelous Designer cost**: $40/month Speaker's stated subscription cost for cloth sims
- n3: **playback framerate**: 13 fps (cityscape shot, EEVEE) Playback in viewport for dense scene

## Techniques
- t1: **Light Influence panel tuning**: Keep light color and intensity fixed; reduce or zero Volume Scatter and Glossy in the light's Influence panel to control haze per light.
- t2: **Light-only lighting (no shadows)**: Disable shadows on scene lights to keep playback fast and art-direct light placement; shadows become the absence of light.
- t3: **Flat card debris**: Use stretched flat geometry with noise-to-alpha textures instead of particle sims; move cards toward camera for depth.

## Quotes (brief, for attribution)
> I started to realize just how much an all-in-one software protects against the flow state.  (at 8:01, Blender)
> sometimes doing things the wrong way is more fun or sometimes it gives you a better result  (at 41:42, Blender)

## Points to
- MPFB (MakeHuman plugin for Blender)
- AutoRig Pro
- Poly Hammer
- Marvelous Designer
- Infinite Fracture add-on
- Poly Haven
