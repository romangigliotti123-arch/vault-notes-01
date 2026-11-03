---
type: research-source
id: web-5b1eabceab
title: "Blender manual: animation/armatures/skinning/parenting"
source_type: "web"
creator: "docs.blender.org"
url: "https://projects.blender.org/blender/blender-manual/raw/branch/main/manual/animation/armatures/skinning/parenting.rst"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0010
relevance: 2
density: medium
tags: ["research-source", "web", "common-mistakes-fixes", "rigging-animation"]
---
# web-5b1eabceab

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Blender manual page on Armature Deform parenting (Ctrl-P). Explains binding child meshes to an armature with three modes: Empty Groups (creates empty vertex groups named after deform bones for manual weighting), Automatic Weights (bone heat distance-based weights, may deform badly on complex meshes), and Envelope Weights (weights from bone envelopes, requires re-parenting after envelope changes). Not Roblox-specific.

## Claims
- c1: Armature Deform parenting: select children first, armature last, Ctrl-P, choose Armature Deform; each child gets an Armature Modifier pointing at the armature. *(doc, high; rigging-animation)*
- c2: Empty Groups option creates empty vertex groups named after each deforming bone only; bones must have Deform enabled in Bone properties. *(doc, high; rigging-animation)*
- c3: Automatic Weights uses bone heat algorithm based on vertex distance to bones; can produce unexpected deformation with complex armatures/overlaps, requiring manual weight edits. *(doc, high; rigging-animation)*
- c4: Envelope Weights computes weights from bone envelope volumes; new vertices or envelope changes are ignored until Armature Deform With Envelope Weights is reapplied. *(doc, high; rigging-animation)*
- c5: Existing vertex groups with same names as bones are fully overwritten by Automatic or Envelope weighting; use Empty Groups if weights already exist. *(doc, high; common-mistakes-fixes)*
- c6: Binding Armature Modifier to Bone Envelopes makes envelope settings take effect immediately. *(doc, medium; rigging-animation)*

## Techniques
- t1: **Armature Deform parenting (Ctrl-P)**: Select child meshes, then armature last; Ctrl-P > Armature Deform; pick Empty Groups, Automatic Weights, or Envelope Weights.

## Points to
- Armature Modifier manual page
- Vertex groups manual page
- Weight painting bones
