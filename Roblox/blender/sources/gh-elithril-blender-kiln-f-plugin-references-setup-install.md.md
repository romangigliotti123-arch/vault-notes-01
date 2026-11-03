---
type: research-source
id: gh-elithril-blender-kiln-f-plugin-references-setup-install.md
title: "elithril/blender-kiln/plugin/references/setup-install.md"
source_type: "github"
creator: "elithril"
url: "https://github.com/elithril/blender-kiln/blob/HEAD/plugin/references/setup-install.md"
published: "2026-10-29"
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0239
relevance: 1
density: low
tags: ["research-source", "github", "claude-blender-ai"]
---
# gh-elithril-blender-kiln-f-plugin-references-setup-install.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Setup doc from the blender-kiln Claude plugin for optionally installing a local Hunyuan3D-2 (mini) AI shape-generation backend. It is not needed by default (scripted modeling is the default). It covers model variants, venv install commands, Windows notes, and a validation script. It has nothing on Roblox export or on blender-mcp.

## Claims
- c1: blender-kiln's default is scripted modeling with no AI model. If the user picks AI, a free hosted Space is tried first. Local install is only for offline work. *(doc, high; claude-blender-ai)*
- c2: Hunyuan3D-2's licence does not apply in the EU, UK or South Korea, per the first line of its LICENSE. The plugin shows this and requires a yes before installing. A measured MIT alternative, TRELLIS.2 on Apple Silicon, is described in ai-generation.md. *(doc, high; claude-blender-ai)*
- c3: Three Hunyuan3D-2 mini DiT variants (v2-mini, -fast, -turbo) are each 0.6B params and need about 6 GB VRAM. Turbo is fastest at preview quality. *(doc, medium; claude-blender-ai)*
- c4: Bare pip3 fails on PEP 668 Pythons (Homebrew, most Linux distros). The doc creates a venv and calls venv/bin/pip and venv/bin/python explicitly. *(doc, high; claude-blender-ai)*
- c5: Texture generation needs CUDA extensions (custom_rasterizer, differentiable_renderer). Without CUDA (Mac, CPU), shape generation runs on mps or cpu and texturing is done in Blender in the skill's TEXTURING phase. *(doc, high; claude-blender-ai)*
- c6: On Windows the CUDA extensions may need Visual Studio Build Tools, and compile_mesh_painter.sh must be run via Git Bash or WSL. *(doc, medium; claude-blender-ai)*

## Numbers
- n1: **Hunyuan3D-2mini params / VRAM**: 0.6B / ~6 GB all three mini variants

## Techniques
- t1: **Local Hunyuan3D-2mini install in venv**: git clone Tencent/Hunyuan3D-2; python3 -m venv; venv pip install -r requirements.txt and -e .; snapshot_download('tencent/Hunyuan3D-2mini') via huggingface_hub; on CUDA only, build texgen extensions; validate by loading the turbo pipeline.

### Code: Download Hunyuan3D-2mini weights
```python
from huggingface_hub import snapshot_download
snapshot_download('tencent/Hunyuan3D-2mini', local_dir='{models_path}/Hunyuan3D-2mini')
```

### Code: Pick device for validation
```python
device = 'cuda' if torch.cuda.is_available() else ('mps' if torch.backends.mps.is_available() else 'cpu')
```

## Points to
- Tencent/Hunyuan3D-2
- tencent/Hunyuan3D-2mini (Hugging Face)
- TRELLIS.2
- ai-generation.md (in blender-kiln)
