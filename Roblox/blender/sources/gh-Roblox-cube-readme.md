---
type: research-source
id: gh-Roblox-cube-readme
title: "Roblox/cube README: Roblox Foundation Model for 3D Intelligence"
source_type: "github"
creator: "Roblox"
url: "https://github.com/Roblox/cube"
published: "2026-05-28"
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0451
relevance: 2
density: medium
tags: ["research-source", "github", "bpy-scripting-headless", "procedural-generation"]
---
# gh-Roblox-cube-readme

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
README for Roblox's open-source Cube 3D text-to-shape model (v0.1, v0.5) and CubePart (part-controllable generation, May 2026). Covers install, CLI/Python inference, hardware needs, and .obj output; Blender >=4.3 only used for turntable GIF rendering. No Claude, blender-mcp, or Roblox import pipeline content.

## Claims
- c1: Cube 3D is Roblox's open-source text-to-shape model (shape tokenizer + autoregressive generator); outputs an .obj file, with no texture generation yet (texture and scene layout listed as upcoming). *(doc, high; procedural-generation)*
- c2: v0.5 adds bounding-box conditioning and better text adherence; trained on ~2.8M additional synthetic 3D assets; VQ-VAE latent length raised from 512 to 1024. *(doc, high; procedural-generation)*
- c3: Failure mode: with extreme bounding boxes (e.g. a cat) the model can produce disconnected components or orient the object diagonally to fit the box. *(doc, high; procedural-generation)*
- c4: CubePart (May 2026) takes an input mesh plus a user-defined parts schema and outputs one mesh per schema element that assemble into the object; claimed to be usable in engines with animation/physics without manual post-processing (vendor claim). *(doc, medium; procedural-generation)*
- c5: Blender >= 4.3 must be on PATH for the --render-gif turntable option; Cube uses Blender from the command line for rendering. *(doc, high; bpy-scripting-headless)*
- c6: Hardware: recommend at least 24GB VRAM with --fast-inference and 16GB otherwise; tested on L40S, H100, A100 and Apple M2-4. --fast-inference does not work on macOS. *(doc, high; procedural-generation)*
- c7: Slow shape decoding can be sped up with --resolution-base; values 4.0 to 9.0 recommended, lower gives coarser mesh. *(doc, high; procedural-generation)*
- c8: The [meshlab] extra enables mesh simplification; installing without it (pip install -e .) improves compatibility but disables simplification. *(doc, high; procedural-generation)*

## Numbers
- n1: **Recommended VRAM with --fast-inference**: 24GB 16GB without fast inference
- n2: **Recommended resolution-base range**: 4.0-9.0 lower is faster, coarser
- n3: **VQ-VAE latent length**: 512 to 1024 v0.5 fidelity increase
- n4: **Extra training assets v0.5**: ~2.8M synthetic 3D assets
- n5: **Minimum Blender version for turntable GIF**: >=4.3 must be on PATH

## Techniques
- t1: **Run Cube 3D text-to-shape locally**: Clone Roblox/cube, pip install -e .[meshlab], download weights via huggingface-cli download Roblox/cube3d-v0.5 --local-dir ./model_weights, run python -m cube3d.generate with --prompt; get .obj output for import into Blender.
- t2: **Bounding box conditioning**: Pass --bounding-box-xyz X Y Z (e.g. 1.0 2.0 1.5) to set the global aspect ratio alongside the text prompt.

### Code: Generate a mesh with bounding box conditioning
```bash
python -m cube3d.generate \
            --gpt-ckpt-path model_weights/shape_gpt.safetensors \
            --shape-ckpt-path model_weights/shape_tokenizer.safetensors \
            --fast-inference \
            --prompt "A tall pagoda" \
            --bounding-box-xyz 1.0 2.0 1.5
```

### Code: Library usage, export to obj via trimesh
```python
mesh_v_f = engine_fast.t2s([input_prompt], use_kv_cache=True, resolution_base=8.0, top_p=0.9)
vertices, faces = mesh_v_f[0][0], mesh_v_f[0][1]
_ = trimesh.Trimesh(vertices=vertices, faces=faces).export("output.obj")
```

## Points to
- https://github.com/Roblox/cube
- https://huggingface.co/Roblox/cube3d-v0.5
- https://huggingface.co/Roblox/cubepart
- https://arxiv.org/abs/2503.15475
- https://arxiv.org/abs/2605.28763
- https://cubepart.github.io/
