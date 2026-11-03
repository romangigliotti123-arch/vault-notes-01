---
type: research-source
id: gh-elithril-blender-kiln-f-CONTRIBUTING.md
title: "elithril/blender-kiln/CONTRIBUTING.md"
source_type: "github"
creator: "elithril"
url: "https://github.com/elithril/blender-kiln/blob/HEAD/CONTRIBUTING.md"
published: "2026-10-29"
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0431
relevance: 2
density: medium
tags: ["research-source", "github", "bpy-scripting-headless", "claude-blender-mcp", "common-mistakes-fixes", "creator-workflows", "procedural-generation", "rigging-animation", "texturing-baking-uv"]
---
# gh-elithril-blender-kiln-f-CONTRIBUTING.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
CONTRIBUTING for blender-kiln, a Claude skill that drives Blender through blender-mcp. It isn't Roblox-specific. It teaches audit lessons: measure claims by running them, install the MCP addon via uvx, and verify headless in batch mode. It also lists failure modes: silent geometry-nodes export, outdated addon, pip PEP 668 failures, and scene-clear breaking integrations.

## Claims
- c1: Install the blender-mcp addon with `uvx blender-mcp install-addon`. `addon_utils.enable()` alone leaves property groups incomplete, and the resulting failures name nothing relevant. *(doc, high; claude-blender-mcp)*
- c2: An outdated MCP addon lacks commands. The errors name nothing relevant to the cause. `get_addon_status()` reports whether the addon is behind the server. *(doc, high; claude-blender-mcp)*
- c3: A batch runner's scene-clear disabled the integrations it depended on. This was one of fifteen bugs found by running the skill's documentation rather than reading it. *(experience, medium; bpy-scripting-headless)*
- c4: A geometry-nodes export wrote a 1 kB file and reported success. The only sign was a Blender warning, so warnings should be checked, not only errors. *(experience, high; procedural-generation)*
- c5: An export turned a 2,688-triangle scatter into 2 triangles. It was found only by running the export. *(experience, high; common-mistakes-fixes)*
- c6: A texturing workflow using a PolyHaven material lost four of the seven maps it downloaded. A material audit also fired on a harmless node while missing both real losses. *(experience, high; texturing-baking-uv)*
- c7: Six `pip install` lines failed on any PEP 668 (externally managed) Python. *(experience, high; bpy-scripting-headless)*
- c8: A rig validator raised three false alarms on a correct production rig. The FK/IK, twist-bone and facial sections need a real animated character and human review of the deformation. *(experience, medium; rigging-animation)*
- c9: AI-written checks produced four false positives. A regex that excluded digits silently truncated an AI-derived tool list. A rotation sign was wrong twice. Verify AI output by running it. *(experience, medium; creator-workflows)*
- c10: The Hunyuan3D, Hyper3D Rodin and Sketchfab paths were never exercised. The first two consume credits and the third needs an API key. *(doc, high; procedural-generation)*
- c11: The skill file `plugin/SKILL.md` costs about 15.7k tokens on invoke, up 50% over the audit. Moving the measured tables into lazily loaded references would cut that. *(data, medium; creator-workflows)*

## Numbers
- n1: **bugs found by running docs**: 15 found by running the skill; reading could not have found them
- n2: **Draco size example**: 435.1 kB to 43.9 kB example of a measured compression claim
- n3: **Blender versions**: developed on 5.0, CI on 5.2 LTS 4.x+ required
- n4: **SKILL.md token cost**: ~15.7k tokens on invoke, +50% since the audit
- n5: **gallery assets**: 15 reproduced by run_gallery.sh

## Techniques
- t1: **Headless Blender verification**: Run `blender --background --factory-startup --python-exit-code 1 --python plugin/tools/verify_blender.py`. The non-zero exit code on a Python error makes it usable in CI.
- t2: **Gallery regeneration**: Install `@gltf-transform/cli` and `gltfpack` with npm, plus cwebp from webp. Then run `cd examples/gallery && ./run_gallery.sh` to rebuild the assets and the metrics table.
- t3: **Check warnings and test both directions**: Read Blender warnings, not only errors. Add a regression case with every new check, covering both pass and fail, because a check that fires on correct input gets ignored.

### Code: headless Blender verification
```bash
blender --background --factory-startup --python-exit-code 1 --python plugin/tools/verify_blender.py
```

### Code: install the MCP addon
```bash
uvx blender-mcp install-addon
```

## Quotes (brief, for attribution)
> claims must be measured, not reasoned.  (elithril)
> do not submit a claim a model produced without running it.  (elithril)

## Points to
- https://github.com/ahujasid/blender-mcp
- @gltf-transform/cli
- gltfpack
- cwebp
- PolyHaven
- Hunyuan3D
- Hyper3D Rodin
- Sketchfab
