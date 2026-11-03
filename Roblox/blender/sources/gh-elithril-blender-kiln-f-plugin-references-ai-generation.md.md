---
type: research-source
id: gh-elithril-blender-kiln-f-plugin-references-ai-generation.md
title: "elithril/blender-kiln/plugin/references/ai-generation.md"
source_type: "github"
creator: "elithril"
url: "https://github.com/elithril/blender-kiln/blob/HEAD/plugin/references/ai-generation.md"
published: "2026-10-29"
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0839
relevance: 2
density: high
tags: ["research-source", "github", "claude-blender-mcp", "common-mistakes-fixes", "creator-workflows", "procedural-generation", "roblox-mesh-limits"]
---
# gh-elithril-blender-kiln-f-plugin-references-ai-generation.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Reference from the blender-kiln Claude plugin on optional AI mesh generation alongside Claude-scripted Blender. It covers Blender MCP's Hunyuan3D and Rodin tools, HF Space backends (TRELLIS, TRELLIS.2, Hunyuan3D) via gradio_client, ZeroGPU quota limits, local TRELLIS.2 on Apple Silicon, licences, and the cleanup that raw AI meshes need. It has almost nothing on Roblox itself.

## Claims
- c1: Blender MCP addon ships generation tools only for Hunyuan3D (Tencent Cloud keys or local API) and Hyper3D Rodin (paid). Tools: get_*_status, generate_*, poll_*_job_status, import_generated_asset*. *(doc, high; claude-blender-mcp)*
- c2: Hunyuan3D and Rodin integrations are OFF by default. While off, the addon doesn't register their commands, so calls return 'Unknown command type' rather than 'disabled'. Call get_*_status() first. *(doc, high; claude-blender-mcp)*
- c3: Enable the integrations through checkboxes in the BlenderMCP panel of the 3D Viewport sidebar (press N): 'Use Tencent Hunyuan 3D model generation' and 'Use Hyper3D Rodin 3D model generation'. *(doc, high; claude-blender-mcp)*
- c4: Default is Claude scripting Blender, with no AI model. AI generation is offered only for organic or realistic forms, at the user's choice. *(opinion, medium; procedural-generation)*
- c5: Hunyuan3D licence (2.0 and 2.1) does not apply in the EU, UK or South Korea. This matters for commercial or UGC use from those regions. *(doc, high; procedural-generation)*
- c6: TRELLIS.2 Space background removal falls back to RMBG-2.0 (CC BY-NC 4.0) unless the input has an alpha channel. Send a transparent-PNG cut-out for commercial use. *(doc, high; procedural-generation)*
- c7: Hunyuan3D Space /generation_all (textured) failed server-side with NameError on 2026-09-29. /shape_generation worked, so texture in Blender afterwards. *(data, medium; procedural-generation)*
- c8: Free ZeroGPU quota is 2 min per day without an HF account and 3.5 min with one. It resets 24 h after the first use, not at midnight. A TRELLIS.2 call reserves 60–120 s, so roughly 1–2 generations a day. *(data, medium; procedural-generation)*
- c9: A Space call reserves its declared duration, not its actual run time. FLUX took 5.6 s but was refused with '90s requested vs. 0s left'. *(data, medium; procedural-generation)*
- c10: gradio_client sends the locally saved HF token by default. Use Client(space, token=False) for anonymous calls; token=None sends the saved token. *(data, medium; procedural-generation)*
- c11: Paused community Spaces still return HTTP 200, but gradio_client raises ValueError 'invalid state: PAUSED'. Check runtime.stage through the huggingface.co/api/spaces/<owner>/<name> endpoint. Prefer vendor-owned Spaces. *(data, high; procedural-generation)*
- c12: gradio_client 2.7.1 can return a dict ({'value': path}) instead of a string path. Unwrap it before shutil copies, or you get a TypeError. *(data, high; procedural-generation)*
- c13: Hunyuan3D Space's randomize_seed defaults to True, making runs non-reproducible. Set it False and fix the seed for batches. *(doc, high; procedural-generation)*
- c14: Raw TRELLIS.2 output is 160–190k triangles, one material, 1024² PBR, ~11 MB GLB. It is always 1 m tall and non-manifold with open edges, so it needs decimation and cleanup before any budgeted platform like Roblox. *(data, medium; roblox-mesh-limits)*
- c15: AI meshes are always 1 m tall, so set real size. Glass and metal come out as one material and must be split. Ink lines in concept art bake into the texture as black cracks. *(data, medium; common-mistakes-fixes)*
- c16: Decimating thin parts (wires, bails, loops) breaks them. Rebuild them as curves with a round bevel, taking the centreline from slice centroids and the radius from slice size. Decimate only solid bodies, then count open and non-manifold edges. *(experience, medium; common-mistakes-fixes)*
- c17: Best use of TRELLIS.2 output is as a measuring template for scripted modelling: take proportions from the mesh, build clean geometry from the measures, and take materials from the photo. *(opinion, medium; procedural-generation)*
- c18: TRELLIS.2 Space /extract_glb rejects a decimation_target under 100,000, so decimate in Blender afterwards. *(data, medium; procedural-generation)*
- c19: Local TRELLIS.2 on an M4 Pro with 24 GB takes 5–7 min per model, peaks at 19.5–22.5 GB, and needs 31 GB of weights (TRELLIS.2-4B 28 GB, DINOv3 2.3 GB, BiRefNet 0.8 GB). *(data, medium; procedural-generation)*
- c20: Local Hunyuan3D-2 Mini texture generation needs CUDA, while shape generation runs on MPS and CPU, 3–10x slower than CUDA. Variants: mini ~16 s, mini-fast ~12 s, mini-turbo ~8 s on CUDA. *(doc, medium; procedural-generation)*
- c21: To run TRELLIS.2 MIT-only, swap RMBG-2.0 for ZhengPeng7/BiRefNet (MIT) and cast it with .float(). Test with an opaque image, because alpha images skip removal. DINOv3 remains under Meta's gated licence. *(experience, medium; procedural-generation)*
- c22: FLUX.1-schnell HF Space (Apache-2.0) gave a 1024² concept image in 5.6 s but sometimes adds ground and shadow despite the prompt. It returns WebP, so convert to PNG for 3D Spaces. *(data, medium; procedural-generation)*
- c23: Fallbacks when quota is spent: the user's own image, a CC0 PolyHaven preview thumbnail (credit required), scripted modelling from the brief, or waiting for the reset. *(doc, medium; creator-workflows)*

## Numbers
- n1: **ZeroGPU daily quota**: 2 min anon / 3.5 min free account Per user, resets 24 h after first use
- n2: **TRELLIS.2 raw triangles**: 160–190k Local output, one material, 1024² PBR
- n3: **TRELLIS.2 local time/memory**: 5–7 min; 19.5–22.5 GB peak M4 Pro 24 GB via trellis-mac
- n4: **TRELLIS.2 weights**: 31 GB Plus a 1 GB venv; README says 15 GB
- n5: **Hunyuan3D Space defaults**: steps 30, guidance 5.0, octree 256, num_chunks 8000 13 parameters, all with defaults
- n6: **extract_glb min decimation_target**: 100,000 TRELLIS.2 Space
- n7: **FLUX.1-schnell time**: 5.6 s 1024×1024, 4 steps

## Techniques
- t1: **Check MCP generation integration before calling**: Call get_hunyuan3d_status() or get_hyper3d_status(). Show the remediation text from the message field. Have the user tick the checkbox in the BlenderMCP sidebar panel, then generate, poll the job and import.
- t2: **Check HF Space health**: curl huggingface.co/api/spaces/<owner>/<name> and read runtime.stage. Use it only if RUNNING, and skip PAUSED, SLEEPING and BUILD_ERROR.
- t3: **Inspect auto-generated Gradio API**: On a failed call, print client.view_api(return_format='dict')['named_endpoints'][endpoint] instead of guessing the arguments.
- t4: **Untextured shape then Blender texturing**: When /generation_all fails, call /shape_generation and texture the mesh in Blender.
- t5: **Rebuild thin parts as curves**: Slice the part along its length, take one centroid per slice for the centreline, and take the radius from the slice size. Build a curve with a round bevel. Decimate only the solid body.
- t6: **Mesh as measuring template**: Extract proportions from the AI mesh with a template-profile tool, then model a clean low-poly version by script and take materials from the photo.

### Code: Unwrap gradio_client results that may be dicts
```python
def gradio_path(x):
    if isinstance(x, dict):
        x = x.get("path") or x.get("value") or x.get("name")
        if isinstance(x, dict):
            return gradio_path(x)
    if not isinstance(x, str):
        raise TypeError(f"no file path in gradio result: {x!r}")
    return x
```

### Code: Hunyuan3D Space call via gradio_client
```python
client = Client("tencent/Hunyuan3D-2")
result = client.predict(
    image=handle_file("concept.png"),
    steps=30, guidance_scale=5.0, octree_resolution=256,
    check_box_rembg=True, randomize_seed=False, seed=1234,
    api_name="/generation_all",
)
mesh_path = gradio_path(result[0])
```

### Code: Check Space stage
```bash
curl -s https://huggingface.co/api/spaces/<owner>/<name> \
  | python3 -c "import json,sys; print(json.load(sys.stdin)['runtime']['stage'])"
```

## Contradictions flagged
- TRELLIS.2 weights need 31 GB of disk (vs The trellis-mac project README, which states 15 GB)

## Points to
- microsoft/TRELLIS.2
- trellis-community/TRELLIS
- tencent/Hunyuan3D-2
- shivampkumar/trellis-mac
- black-forest-labs/FLUX.1-schnell
- ZhengPeng7/BiRefNet
- huggingface/skills huggingface-zerogpu
- PolyHaven API
- Tencent-Hunyuan/Hunyuan3D-2
