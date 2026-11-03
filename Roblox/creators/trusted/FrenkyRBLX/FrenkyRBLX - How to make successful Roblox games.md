---
title: FrenkyRBLX - How to make successful Roblox games
tags: [roblox, frenkyrblx, playbook]
videos: 5
generated: 2026-10-29
credibility: trusted
credibility_score: 8.2
creator_trust: TRUSTED
creator_score: 8.2
---

> [!note] Trust: TRUSTED (credibility audit score 8.2): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# FrenkyRBLX - How to make successful Roblox games

Evidence covers only the build stage of Roblox UGC hair in Blender. Model strands from circle-to-curve paths fitted to the R6 block dummy, lower curve resolution, merge into one mesh, then cut triangles under the 4,000 limit using non-destructive cleanups (dissolve flat edges, delete hidden faces, merge by distance) before any Decimate. Check counts with the statistics overlay. Two of five videos have no transcript. No evidence was extracted for idea validation, growth, or live ops.

**Style:** Hands-on Blender tutorial creator focused on UGC hair and triangle-budget optimisation. Step-by-step, screen-recorded workflow with statistics-overlay checks at each stage. Suits beginners making accessories for the UGC marketplace. These five videos offer no business, marketing, or live-ops guidance.

## Playbook
1. **Idea: choose UGC hair as an accessory product** [[ugc-and-avatar-economy]]: Titles pitch UGC hair as a way to earn Robux (YpaHoWr7w8E, lymyB5wZpgo). Both transcripts were empty, so no demand, pricing, or earnings evidence was extracted. Treat the earnings claim as unverified.
2. **Import the R6 fitting guide** [[3d-modeling-rigging-and-animation]]: Export the R6 block avatar dummy from Studio via Avatar > Rig Builder, save-export selection as OBJ, and import it into Blender as a fitting guide (P9RpgVY8sN8).
3. **Model hair strands from curves** [[3d-modeling-rigging-and-animation]]: Create strands from circle-to-curve paths shaped over the guide. Before merging, lower curve resolution from 12 to 6 (P9RpgVY8sN8, rtF3uoHrqU4).
4. **Convert and merge into one mesh** [[building-art-and-assets]]: Mirror parts, convert curves to mesh, and merge vertices into a single mesh (P9RpgVY8sN8, rtF3uoHrqU4).
5. **Reduce triangles below 4,000** [[building-art-and-assets]]: Dissolve edges on flat surfaces, delete hidden back faces using X-ray and face select, then run merge by distance. Use Decimate only as a last resort (7__AKBlwYkk, rtF3uoHrqU4). Read the count from the statistics overlay after each pass.
6. **Check face orientation and set UVs** [[building-art-and-assets]]: Verify face orientation, then set up the UV and texture in the shader editor (P9RpgVY8sN8).
7. **Final count check before upload** [[ugc-and-avatar-economy]]: Confirm the final mesh is under 4,000 tris on the overlay. This is the marketplace limit cited across videos (7__AKBlwYkk, P9RpgVY8sN8, rtF3uoHrqU4).

## Key numbers
- 4,000 tris: UGC hair/accessory upload limit (7__AKBlwYkk, P9RpgVY8sN8, rtF3uoHrqU4)
- 19k tris: demo model before optimisation (7__AKBlwYkk)
- 66 vertices removed in one merge-by-distance pass on demo mesh (7__AKBlwYkk)
- Curve resolution lowered 12 -> 6 before merging (P9RpgVY8sN8, rtF3uoHrqU4)
- ~10,000 -> ~5,000 tris after strand resolution drop (rtF3uoHrqU4)
- 4,500 tris before back-face deletion (rtF3uoHrqU4)
- ~80 tris removed by merge by distance (rtF3uoHrqU4)
- Caveat: 4,500 minus ~80 is still above 4,000, and the source's ~90 tris remaining conflicts with this. Verify counts in Blender. The 4,56x figure in P9RpgVY8sN8 is garbled and was not used.

## Common mistakes
- Leaving strand curve resolution at 12, which roughly doubles triangle count (rtF3uoHrqU4)
- Using the Decimate modifier, which damages topology; the creator does not recommend it (7__AKBlwYkk)
- Deleting visible geometry when removing hidden faces; confirm selection in X-ray first (rtF3uoHrqU4)
- Running merge by distance without checking the result, since it can remove vertices unnoticed (7__AKBlwYkk)
- Skipping overlay checks between steps, so you cannot see which cleanup actually cut triangles (7__AKBlwYkk)
- Building hair without the R6 dummy guide, which makes fitting harder to verify (P9RpgVY8sN8)
- Trusting earnings claims in titles; the two videos with empty transcripts provide no support (lymyB5wZpgo, YpaHoWr7w8E)

## Launch checklist
- [ ] Final mesh under 4,000 tris on the statistics overlay
- [ ] Strand curve resolution set to 6 before merging
- [ ] Flat-surface edges dissolved
- [ ] Hidden back faces deleted and selection checked in X-ray
- [ ] Merge by distance run and result visually checked
- [ ] Face orientation verified
- [ ] UV and texture set up in the shader editor
- [ ] Fitted against the R6 dummy OBJ guide
- [ ] Decimate not used, or used only as a last resort

## Theme notes
- [[FrenkyRBLX - Studio & Scripting|Studio & Scripting]]
- FrenkyRBLX - Games Mentioned
- [[FrenkyRBLX - Numbers & Benchmarks]]
- [[FrenkyRBLX - Tools & Resources]]
- Cross-creator knowledge base: [[README]]

## All videos (oldest first)
- [[2025-03-29 - How To Make UGC Hair For Roblox (Blender Tutorial)|How To Make UGC Hair For Roblox (Blender Tutorial)]] (58,731 views, 2025-03-29): Title-only: 23:46 Blender UGC hair tutorial; no transcript, so content is unverified.
- [[2025-04-18 - How to Make UGC Hair in Roblox and EARN ROBUX! (Blender Tutorial )|How to Make UGC Hair in Roblox and EARN ROBUX! (Bl]] (32,531 views, 2025-04-18): Title-only: 15:37 Blender UGC hair tutorial pitched as a way to earn Robux; no transcript.
- [[2025-05-05 - How to LOWER TRIS COUNT in Your Roblox UGC|How to LOWER TRIS COUNT in Your Roblox UGC]] (8,841 views, 2025-05-05): Four ways to cut tris under 4,000; dissolve edges and merge by distance preferred, Decimate not recommended.
- [[2025-08-20 - How To Make Roblox UGC Hair Blender Step-By-Step Tutorial|How To Make Roblox UGC Hair [Blender Step-By-Step ]] (255,947 views, 2025-08-20): Full Blender UGC hair workflow: R6 dummy guide, strands, merge, under 4,000 tris, and UV setup.
- [[2025-12-24 - How to Optimize your Roblox Hair|How to Optimize your Roblox Hair]] (7,586 views, 2025-12-24): Hair optimisation: lower strand resolution, merge vertices, dissolve edges, delete back faces to hit 4,000.
