---
type: research-source
id: yt-UBjgJM6D18A
title: "Building My Dream Game With AI - Characters & Animations"
source_type: "youtube"
creator: "Stefan 3D AI"
url: "https://www.youtube.com/watch?v=UBjgJM6D18A"
published: "2026-09-26"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0042
relevance: 1
density: low
tags: ["research-source", "youtube", "automation-and-creator-workflows", "avatar-ugc-accessories", "claude-blender-ai", "mesh-texture-limits", "other", "rigging-animation"]
---
# yt-UBjgJM6D18A

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Unity-based indie RTS dev vlog, not a Roblox pipeline. Relevant only for Blender-side AI workflow: GPT-6 driven through Blender MCP to animate a Tripo model, Mixamo rigs, and cost estimates. No Roblox export, scale, or MeshPart content. Mostly off-topic for the target topic.

## Claims
- c1: [7:13] Author opened Blender with Blender MCP, gave a Tripo textured model plus video references, and asked GPT-6 (X-High effort) to animate it; output was decent after a few feedback iterations, not fully perfect. *(experience, medium; claude-blender-ai)*
- c2: [7:13] Earlier Claude-to-Cascade MCP posing attempt for quadruped rig was abandoned; author called it a nightmare due to non-unified skeleton standards. *(experience, medium; claude-blender-ai)*
- c3: [10:01] For a scorpion, GPT-6 performed all rigging (legs, tail etc.) itself; author estimates a manual rig would take about half a day. *(experience, low; rigging-animation)*
- c4: [11:50] Author chose Mixamo auto-rig over Unreal rig for human skeletons because Mixamo skeleton is simpler with fewer bones, which keeps units optimized. *(experience, medium; rigging-animation)*
- c5: [13:12] Retargeting Mixamo/purchased animations to custom rigs was previously painful but GPT handled it with no issues after the agent was given the files. *(experience, medium; rigging-animation)*
- c6: [13:52] Unreal Engine 5.8 offers free markerless mocap animation; Quick Magic (paid) exports a Mixamo-compatible skeleton but outputs in Unreal-specific formats needing a pipeline to reach Blender/Unity. *(doc, medium; automation-and-creator-workflows)*
- c7: [14:32] Video-only AI reference clips with non-human skeletons were unusable for mocap; author converted them to human motion with Seedance 2.5 first. *(experience, low; rigging-animation)*
- c8: [23:32] Bought about four or five Mixamo-style animation packs on a marketplace at around $2 each; reused arm and leg movements rather than full clips. *(experience, medium; rigging-animation)*
- c9: [26:54] Bought a $19 horse animation pack made for Unreal on Fab; installed it in an Unreal sample project and asked GPT to export the animations as FBX for reuse with the horse rig. *(experience, medium; rigging-animation)*
- c10: [28:55] Built a pose-controller tool in the engine: user sets a rig pose, saves it as a reference, and the model recalculates the animation to match, instead of approximate degree-based feedback. *(experience, low; rigging-animation)*
- c11: [11:10] Per-unit polygon budget author stated was roughly 10,000–15,000 for characters; generals and knights slightly higher, horses higher still. *(opinion, low; mesh-texture-limits)*
- c12: [17:11] Concept image generation via GPT image 2.5 API cost about 4 cents per image; 40–50 iterations to pick one character is about $2.50–3. *(data, medium; other)*
- c13: [18:33] Tripo P2 via API costs about 80 cents per model for low-poly, texturing and UV; Tripo Studio about 60 cents; roughly 8 parts per character gives about $5–6. *(data, medium; mesh-texture-limits)*
- c14: [19:14] Seedance 2.5 video references for animation cost the most: 7–8 clips averaged $13–15 via true API; cheaper through third-party platforms. *(data, medium; automation-and-creator-workflows)*
- c15: [21:15] Estimated total per character about $20–25 (5–10% of weekly GPT subscription limit, which is 20x tier); author's own estimate, not an invoice. *(data, low; automation-and-creator-workflows)*
- c16: [17:52] Tripo P2 smart UV removed about one hour of manual unwrapping per character, per author. *(experience, low; mesh-texture-limits)*
- c17: [25:33] Interchangeable parts (flags, colors) handled by separating objects, baking one shared texture, then recoloring the bake via GPT image for team colors (blue, red, gray neutral). *(experience, medium; avatar-ugc-accessories)*

## Numbers
- n1: **budget per character**: ~10,000–15,000 (unit unspecified) author's stated target for RTS units, low-poly
- n2: **concept image cost**: $0.04 per image; ~$2.5–3 total GPT image 2.5 API, 40–50 images per character
- n3: **Tripo P2 API cost**: ~$0.80 per model low poly + texturing + UV; Studio ~$0.60
- n4: **parts per character**: ~8 models generated in parts and assembled in Blender
- n5: **Seedance video reference cost**: $13–15 for 7–8 clips used for animation references and mocap input
- n6: **per-character total**: ~$20–25 author estimate including GPT subscription share
- n7: **horse animation pack price**: $19 Unreal-format pack from Fab, exported to FBX
- n8: **mocap cost**: ~$3 for 3–4 clips via Quick Magic

## Techniques
- t1: **Blender MCP prompt-driven animation**: Open the model in Blender with Blender MCP connected. Give the model and video reference clips. Ask the LLM to animate. Iterate on feedback until acceptable.
- t2: **Part-based generation and recolor**: Generate each unit in parts in Tripo, assemble in Blender. Separate color-swappable objects, bake to one texture, recolor the bake via image model.
- t3: **Mixamo rig plus retargeted library clips**: Auto-rig with Mixamo for simpler bone count. Use purchased or Mixamo clips as bases, edit them, and let the agent retarget to weapons and proportions.
- t4: **Pose reference feedback loop**: Build a rig pose controller in the engine. Save a pose as reference, then send it with feedback so the model recalculates matching animation frames.

## Quotes (brief, for attribution)
> open Blender, give this model that I generated in Tripo, just put it there like textured model, open the Blender with Blender MCP and say like, look, bro, try to do this.  (at 7:13, Stefan 3D AI)
> All rigging was done by Chat GPT. All rigging, all legs, tail, et cetera, was done completely by Chat GPT.  (at 10:01, Stefan 3D AI)

## Contradictions flagged
- Video is about Blender-to-Roblox pipeline (vs Source is about a Unity game; no Roblox export, Studio import, or MeshPart content appears)

## Points to
- Tripo (Tripo P2, smart UV)
- Mixamo
- Quick Magic (mocap)
- Animate Anything
- Cascade (animation software)
- Seedance 2.5
- MiniMax H3
- Unreal Engine 5.8 markerless mocap
- Fab marketplace (horse animation pack)
