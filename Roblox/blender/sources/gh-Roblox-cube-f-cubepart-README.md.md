---
type: research-source
id: gh-Roblox-cube-f-cubepart-README.md
title: "Roblox/cube/cubepart/README.md"
source_type: "github"
creator: "Roblox"
url: "https://github.com/Roblox/cube/blob/HEAD/cubepart/README.md"
published: "2026-05-28"
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0324
relevance: 1
density: low
tags: ["research-source", "github", "procedural-generation", "rigging-animation"]
---
# gh-Roblox-cube-f-cubepart-README.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
README for Roblox's CubePart, an open-source multi-part 3D mesh decomposition model (DiT + shape VAE). Given a mesh and a list of part names, it outputs one mesh per part, exported as GLB via trimesh. Has no Blender, Claude, MCP, bpy or Roblox import content. Marginally relevant to text/AI-to-3D part splitting for rigging and animation.

## Claims
- c1: CubePart takes an input mesh plus a list of part names and outputs one mesh per part. The README says the parts assemble coherently and can be driven by animation, physics and scripts without manual post-processing (vendor claim). *(doc, medium; procedural-generation)*
- c2: Input mesh should be canonically aligned (+Y up, +Z forward). A watertight single-surface mesh is preferred. *(doc, high; procedural-generation)*
- c3: Meshes with duplicated inner/outer shells, common in some AI-generated meshes, often degrade decomposition quality. *(doc, high; procedural-generation)*
- c4: Weights are on Hugging Face (Roblox/cubepart): multi_part_dit.safetensors (~8.6 GB) and vae.safetensors (~1.3 GB). A Gradio demo accepts a .glb and part names. *(doc, high; procedural-generation)*
- c5: Per-part GLB outputs (part_00.glb etc.) could serve as separate rigid pieces for animation. The README only says they can be driven by animation scripts; it does not cover rigging. *(doc, low; rigging-animation)*

## Numbers
- n1: **surface samples**: 128,000 sample_surface num_samples for encoding input mesh
- n2: **guidance_scale / inference steps**: 7.5 / 50 example inference settings
- n3: **DiT checkpoint size**: ~8.6 GB multi_part_dit.safetensors
- n4: **VAE checkpoint size**: ~1.3 GB vae.safetensors

## Techniques
- t1: **Split a mesh into named parts with CubePart**: Install the package, download weights, load the mesh with load_mesh, sample 128k surface points, call encode_shape, then call input_to_part_shape with prompt=`[[part names]]`. Export each (vertices, faces) pair with trimesh as GLB.

### Code: Download CubePart weights
```bash
huggingface-cli download Roblox/cubepart --local-dir weights
```

### Code: Run part decomposition inference
```bash
export PYTHONPATH=.

python examples/run_inference.py \
    --config configs/shape_denoiser_multimesh.yaml \
    --checkpoint weights/multi_part_dit.safetensors \
    --vae-checkpoint weights/vae.safetensors \
    --mesh examples/inputs/jellyfish_car.glb \
    --parts "body, front right wheel, front left wheel" \
    --output outputs/jellyfish_car_parts
```

## Points to
- https://github.com/Roblox/cube
- https://huggingface.co/Roblox/cubepart
- https://arxiv.org/abs/2605.28763
- https://cubepart.github.io/
- https://github.com/wgsxm/PartCrafter
- https://github.com/Tencent/Hunyuan3D-2
- https://github.com/microsoft/TRELLIS
