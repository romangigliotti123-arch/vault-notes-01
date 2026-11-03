---
type: research-source
id: yt-7NndTBpol5c
title: "Building KIDDO : Merging Polygonal Modeling, CAD, and Electronics — BCON26"
source_type: "youtube"
creator: "Blender"
url: "https://www.youtube.com/watch?v=7NndTBpol5c"
published: "2026-09-24"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0028
relevance: 1
density: low
tags: ["research-source", "youtube", "blender-roblox-export-import", "other"]
---
# yt-7NndTBpol5c

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
BCON26 talk on KIDDO, a 3D-printed articulated action figure built in Blender, SolidWorks and KiCad. Covers poly-modeling vs CAD tradeoffs, 3D scan cleanup, Blender-to-SolidWorks export by origin alignment, friction joints, and a Blender rig for renders. No Claude, blender-mcp, bpy, Roblox, or Roblox export content.

## Claims
- c1: [4:40] Speaker says 3D printers ignore smooth shading and use only mesh topology, so shade-smooth on a printed part gives no visible change. *(demo, medium; other)*
- c2: [11:18] Blender and SolidWorks use different coordinate systems; move the part to the Blender world origin before export so it imports oriented correctly. SolidWorks workflow, not Roblox. *(experience, low; blender-roblox-export-import)*
- c3: [13:58] Final toy has nearly 200 parts, assembly estimated around 50 minutes, no glue, uses M2 screws and friction joints. *(experience, low; other)*
- c4: [8:38] Speaker chose coin cell over LiPo battery to avoid battery risk for a child user; electronics designed in KiCad, wireless via CC1101. *(experience, medium; other)*
- c5: [9:58] Built-in Blender measure tool used to verify minimum part thickness of 1 mm for rigidity. *(experience, medium; other)*
- c6: [10:40] Used a cheap 3D scanner on a child's face, cleaned the scan in Blender, then retopologized it. *(experience, medium; other)*
- c7: [18:54] Finger poses made by rigging fingers in SolidWorks, saving each pose, and exporting separate prints; Blender pose library mentioned as the pose method. *(experience, low; other)*
- c8: [20:17] Retopologized the SolidWorks-exported mesh to mostly quads for Blender rigging and rendering, then applied materials to create a digital twin. *(experience, medium; other)*
- c9: [4:40] Speaker's PC is low-end by today's standards; speaker argues hardware should not limit the project. *(opinion, low; other)*

## Numbers
- n1: **coordinate alignment**: export at world origin (0,0,0) Blender-to-SolidWorks export; origin alignment, not Roblox
- n2: **minimum wall thickness**: 1 mm Checked with Blender measure tool for rigidity
- n3: **parts in assembly**: ~200 Approximate count for KIDDO toy
- n4: **assembly time**: ~50 minutes Estimated, no glue, friction joints
- n5: **Blender user since**: age 12 Speaker self-taught Blender

## Techniques
- t1: **Origin-aligned export to CAD**: Move mesh to Blender world origin, export with precise settings or a Python add-on, then open in SolidWorks; part arrives oriented as in Blender. Speaker's own workflow.
- t2: **3D scan to CAD-ready mesh**: Cheap 3D scan, import to Blender, clean and smooth, then retopologize before CAD remodeling.
- t3: **Quad-first retopology**: Retopologize CAD-exported messy mesh into mostly quads, avoiding triangles, for rigging and rendering.

## Quotes (brief, for attribution)
> blender solid works doesn't share the same coordinate system. So when you're exporting what you can do is just take your part move it to the world origin  (at 11:18, Blender)
> the 3D printer just don't care about it. it just care about the topology  (at 6:06, Blender)
