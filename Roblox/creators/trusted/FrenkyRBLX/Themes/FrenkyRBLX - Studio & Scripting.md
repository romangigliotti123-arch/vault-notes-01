---
title: FrenkyRBLX - Studio & Scripting
creator: FrenkyRBLX
tags: [roblox, frenkyrblx, theme]
creator_trust: TRUSTED
creator_score: 8.2
---

> [!note] Trust: TRUSTED (credibility audit score 8.2): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# FrenkyRBLX: Studio & Scripting

All FrenkyRBLX tips on this theme, grouped by topic, oldest first. Cross-creator synthesis: see [[README]] in roblox-kb.

## [[building-art-and-assets]]
- 2025-05-05 [0:00](https://youtu.be/7__AKBlwYkk?t=0) UGC items must stay under 4,000 tris; check the Statistics overlay in Studio/Blender to see the count. ([[2025-05-05 - How to LOWER TRIS COUNT in Your Roblox UGC|How to LOWER TRIS COUNT in Your Roblox UGC]])
- 2025-05-05 [1:33](https://youtu.be/7__AKBlwYkk?t=93) Dissolve edges lying on flat surfaces (Alt-click edge, X, Dissolve Edges) to reduce polycount without changing shape. ([[2025-05-05 - How to LOWER TRIS COUNT in Your Roblox UGC|How to LOWER TRIS COUNT in Your Roblox UGC]])
- 2025-05-05 [4:45](https://youtu.be/7__AKBlwYkk?t=285) Delete hidden faces that players never see, such as parts poking inside other geometry, using X-ray and face select. ([[2025-05-05 - How to LOWER TRIS COUNT in Your Roblox UGC|How to LOWER TRIS COUNT in Your Roblox UGC]])
- 2025-05-05 [7:17](https://youtu.be/7__AKBlwYkk?t=437) Avoid the Decimate modifier; it badly damages topology. Use only as last resort when tris must drop fast. ([[2025-05-05 - How to LOWER TRIS COUNT in Your Roblox UGC|How to LOWER TRIS COUNT in Your Roblox UGC]])
- 2025-05-05 [8:37](https://youtu.be/7__AKBlwYkk?t=517) Use Merge by Distance (vertex select, A, M) to clean up very close vertices; often removes many vertices unnoticed. ([[2025-05-05 - How to LOWER TRIS COUNT in Your Roblox UGC|How to LOWER TRIS COUNT in Your Roblox UGC]])
- 2025-08-20 [0:13](https://youtu.be/P9RpgVY8sN8?t=13) Export the R6 block avatar dummy from Studio via Avatar > Rig Builder and save-export selection as OBJ to use as a fitting guide in Blender. ([[2025-08-20 - How To Make Roblox UGC Hair Blender Step-By-Step Tutorial|How To Make Roblox UGC Hair [Blender Step-By-Step ]])
- 2025-08-20 [18:08](https://youtu.be/P9RpgVY8sN8?t=1088) Convert curves to mesh, join parts, and merge verts at center so the hair has fewer tris and no holes before publishing. ([[2025-08-20 - How To Make Roblox UGC Hair Blender Step-By-Step Tutorial|How To Make Roblox UGC Hair [Blender Step-By-Step ]])
- 2025-08-20 [24:29](https://youtu.be/P9RpgVY8sN8?t=1469) Keep UGC hair under 4,000 triangles; check count via Overlays > Statistics and dissolve edges on flat surfaces to reduce it. ([[2025-08-20 - How To Make Roblox UGC Hair Blender Step-By-Step Tutorial|How To Make Roblox UGC Hair [Blender Step-By-Step ]])
- 2025-08-20 [23:38](https://youtu.be/P9RpgVY8sN8?t=1418) Disable the mirror modifier while building one half, then apply it after merging to halve the work. ([[2025-08-20 - How To Make Roblox UGC Hair Blender Step-By-Step Tutorial|How To Make Roblox UGC Hair [Blender Step-By-Step ]])
- 2025-08-20 [29:13](https://youtu.be/P9RpgVY8sN8?t=1753) Enable Face Orientation overlay to find inverted normals (red faces), then fix with Shift+N and recalculate. ([[2025-08-20 - How To Make Roblox UGC Hair Blender Step-By-Step Tutorial|How To Make Roblox UGC Hair [Blender Step-By-Step ]])
- 2025-08-20 [30:50](https://youtu.be/P9RpgVY8sN8?t=1850) If the hair texture appears flipped on the mesh, rotate all UVs 90 degrees in the UV editor. ([[2025-08-20 - How To Make Roblox UGC Hair Blender Step-By-Step Tutorial|How To Make Roblox UGC Hair [Blender Step-By-Step ]])
- 2025-12-24 [0:57](https://youtu.be/rtF3uoHrqU4?t=57) Lower curve resolution on hair strands (Curve Properties, resolution ~12 down to ~6) to cut triangles roughly from 10,000 to 5,000. ([[2025-12-24 - How to Optimize your Roblox Hair|How to Optimize your Roblox Hair]])
- 2025-12-24 [1:38](https://youtu.be/rtF3uoHrqU4?t=98) Convert hair curves to mesh, join strands, and merge vertices by center so no gaps remain in the hair mesh. ([[2025-12-24 - How to Optimize your Roblox Hair|How to Optimize your Roblox Hair]])
- 2025-12-24 [2:20](https://youtu.be/rtF3uoHrqU4?t=140) Dissolve edges that cannot be merged (Alt-select edge, Ctrl+X) to reduce triangle count. ([[2025-12-24 - How to Optimize your Roblox Hair|How to Optimize your Roblox Hair]])
- 2025-12-24 [4:09](https://youtu.be/rtF3uoHrqU4?t=249) Dissolve edges on flat, straight surfaces that add no topology value; repeat across the mesh to drop under 4,000 triangles. ([[2025-12-24 - How to Optimize your Roblox Hair|How to Optimize your Roblox Hair]])
- 2025-12-24 [4:49](https://youtu.be/rtF3uoHrqU4?t=289) Use G-G to slide edges so strands look smoother and more natural after dissolving edges. ([[2025-12-24 - How to Optimize your Roblox Hair|How to Optimize your Roblox Hair]])
- 2025-12-24 [5:51](https://youtu.be/rtF3uoHrqU4?t=351) Delete back faces of hair parts that are hidden under the head and never visible in game to save triangles. ([[2025-12-24 - How to Optimize your Roblox Hair|How to Optimize your Roblox Hair]])
- 2025-12-24 [6:47](https://youtu.be/rtF3uoHrqU4?t=407) Select all, press M, Merge by Distance to remove hidden overlapping geometry; this removed about 80 triangles in the example. ([[2025-12-24 - How to Optimize your Roblox Hair|How to Optimize your Roblox Hair]])
- 2025-12-24 [7:31](https://youtu.be/rtF3uoHrqU4?t=451) Keep the UGC accessory under 4,000 triangles, the limit to upload to the Roblox marketplace. ([[2025-12-24 - How to Optimize your Roblox Hair|How to Optimize your Roblox Hair]])

Up: [[FrenkyRBLX - How to make successful Roblox games]]
