---
type: research-source
id: web-d9b5fe5fb6
title: "Normalizing Vertex Group Weights in Blender"
source_type: "web"
creator: "hydroxide.dev"
url: "https://hydroxide.dev/articles/blender-bone-weight-normalization/"
published: "2026-09-14"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0014
relevance: 2
density: high
tags: ["research-source", "web", "common-mistakes-fixes", "other", "rigging-animation"]
---
# web-d9b5fe5fb6

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Blog post on Blender vertex-group weight normalization for bone deformation. Explains that without envelopes, distance is ignored; per-vertex weights are normalized to sum to 1.0, so single-bone painted falloffs are lost. Fix: add a constant-weight non-moving deform 'Root' normalization bone. Not about Roblox export, MCP, or bpy scripting.

## Claims
- c1: Without bone envelopes, a bone's influence on a vertex depends only on that vertex's group weight; distance from the bone is irrelevant in bone weight mode. *(demo, high; rigging-animation)*
- c2: Blender normalizes each vertex's deform weights to sum to 1.0, so a vertex weighted to only one deform bone ends up at full influence regardless of the painted value (0.1 or 0.9). *(demo, high; rigging-animation)*
- c3: To preserve painted falloff, each vertex must also carry a constant weight to another deform bone; the author's example gives 0.1/(0.1+1.0)=0.09 and 0.9/(0.9+1.0)=0.47. *(demo, high; rigging-animation)*
- c4: Recommended fix: add a non-moving 'normalization sink' bone (e.g. Root/NormalizationRoot) weighted on every vertex; it must have Deform checked or its weight is ignored. *(opinion, medium; rigging-animation)*
- c5: Source cites armature_deform.cc: contributions are summed then scaled by armature_weight / total, i.e. divided by the sum of weights. *(doc, high; rigging-animation)*
- c6: Source is a facial-rig weight-normalization write-up; it does not cover the Roblox export, Asset Manager, MCP or bpy scripting topics. *(opinion, high; other)*
- c7: Common mistake: a hand-painted weight falloff on a single-bone region appears to do nothing when posed, because of normalization. *(demo, medium; common-mistakes-fixes)*

## Numbers
- n1: **Normalized weight example**: 0.1/1.1=0.09 vs 0.9/1.9=0.47 
- n2: **Lip displacement ratio**: ~5x lip face vs near nose 

## Techniques
- t1: **Normalization sink bone**: Add a non-moving bone (Root). Assign every vertex a constant weight to it. Keep Deform checked. Painted weights on other bones then keep their falloff.

### Code: Normalization calculation for two vertices with UpperLip weights 0.1 and 0.9 plus LowerLip 1.0
```text
Weight_Va = 0.1 / (0.1 + 1.0) = 0.1 / 1.1 = 0.09
Weight_Vb = 0.9 / (0.9 + 1.0) = 0.9 / 1.9 = 0.47
```

## Quotes (brief, for attribution)
> Your hand-painted falloff will be completely ignored!  (hydroxide.dev)
> the distance of a vertex from a bone is irrelevant in bone weight mode  (hydroxide.dev)

## Points to
- https://hydroxide.dev/articles/blender-bone-weight-normalization/
- armature_deform.cc (Blender source)
