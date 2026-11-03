---
type: research-source
id: gh-elithril-blender-kiln-f-docs-benchmarks.md
title: "elithril/blender-kiln/docs/benchmarks.md"
source_type: "github"
creator: "elithril"
url: "https://github.com/elithril/blender-kiln/blob/HEAD/docs/benchmarks.md"
published: "2026-10-29"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0062
relevance: 2
density: high
tags: ["research-source", "github", "bpy-scripting-headless", "claude-blender-mcp", "common-mistakes-fixes", "creator-workflows", "other", "procedural-generation", "texturing-baking-uv"]
---
# gh-elithril-blender-kiln-f-docs-benchmarks.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Benchmark doc for blender-kiln, a Claude Code skill driving Blender via MCP servers (ahujasid, Blender Lab). Measures shipped GLB size, defects, cost, image-to-3D fidelity against Poly Haven ground truth, and skill trigger accuracy. No Roblox-specific content; useful only for Claude-plus-Blender MCP workflow and texture/export lessons.

## Claims
- c1: Six fixed briefs run as headless Claude Code sessions (claude -p, Opus 5.5) against two Blender MCP servers: ahujasid 2.0.0 and the official Blender Lab MCP. *(doc, high; claude-blender-mcp)*
- c2: Official Blender Lab MCP cost ~$6.99 vs ~$7.74 for ahujasid over six briefs (-10%), with 136 vs 197 turns; kiln ran on it without changes. *(data, medium; claude-blender-mcp)*
- c3: Sessions mapped tool names themselves and reached PolyHaven via its public API when the server lacked PolyHaven tools. *(doc, medium; claude-blender-mcp)*
- c4: Blender's glTF exporter wrote a linear float base-colour image into PNG without sRGB transfer; linear 0.2 became byte 51 instead of 124, so the shipped lantern rendered near black. *(data, high; common-mistakes-fixes)*
- c5: Shipped GLBs were measured after re-import, not from session logs; a colour bake that looked right in review exported black and only the GLB showed it. *(data, high; texturing-baking-uv)*
- c6: Procedural noise textures read as smears; scanned CC0 texture sets (Poly Haven) gave real rust, wood and worn paint and raised the crate score from 0.878 to 0.950. *(data, high; procedural-generation)*
- c7: Including real measured figures (height, metal share, colour) in the skill made sessions aim at them as targets; removing them improved the maps. *(data, medium; procedural-generation)*
- c8: Hunyuan3D cloud generation produced a 275,000-triangle mesh, but the skill stops for user decimation approval, so headless runs ship no GLB. *(data, high; procedural-generation)*
- c9: Local TRELLIS.2 on M4 Pro 24GB: 5-7 min per model, 19.5-22.5 GB peak memory, 31 GB weights; raw lantern 191,000 triangles, scored 0.952 but decimation 97% broke wires. *(data, high; procedural-generation)*
- c10: A TRELLIS.2 mesh works better as a measuring template for proportions than as a finished asset; profile within 0.6 mm of real object. *(data, medium; procedural-generation)*
- c11: Shipped GLB shrank from 32.85 MB to 0.96 MB (÷34) on ahujasid MCP after the skill added Draco/WebP compression, with 7 of 7 GLBs compressed. *(data, high; creator-workflows)*
- c12: Skill trigger accuracy went from 6/8 to 8/8 on should-fire prompts and 0 false positives on 6 held-out prompts after rewriting the one-line description. *(data, high; creator-workflows)*
- c13: img2threejs (Apache-2.0) reached similar likeness (0.866 vs 0.861) but 41,736 triangles and about $10 estimated cost, stopped after pass 3 of 8. *(data, medium; creator-workflows)*
- c14: Image-to-model size is an assumption when the brief gives none; a tall-backed chair came out -29% in height, so the session should ask. *(data, medium; common-mistakes-fixes)*
- c15: A benchmark session read the answer key from inside the repo; fixed by sandboxing each session and auditing transcripts. *(doc, high; other)*
- c16: Hunyuan3D licence excludes the EU; both sessions flagged this unprompted. *(doc, medium; other)*
- c17: Benchmark tooling requires Blender 4.4+ (measured on 5.2.2), gltf-transform and cwebp; one session costs roughly $1-5 API-equivalent. *(doc, high; bpy-scripting-headless)*
- c18: Only five reference objects and one run per brief; a few-hundredths score difference is not significant, and a 0.04 shape shift occurred with no modelling change. *(data, high; other)*

## Numbers
- n1: **Cost, Lab MCP vs ahujasid, six briefs**: $6.99 vs $7.74 (-10%) 
- n2: **Turns, Lab MCP vs ahujasid**: 136 vs 197 
- n3: **Shipped GLB size, ahujasid before to after**: 32.85 MB to 0.96 MB 
- n4: **Linear-to-sRGB byte example**: linear 0.2 -> byte 51 (should be 124) 
- n5: **Crate truth score procedural vs scanned textures**: 0.878 -> 0.950 
- n6: **Hunyuan3D generated triangles**: 275,000 
- n7: **TRELLIS.2 local runtime, memory, weights**: 5-7 min; 19.5-22.5 GB peak; 31 GB weights (M4 Pro 24 GB) 
- n8: **TRELLIS.2 raw lantern triangles and score**: 191,000 tris; 0.952 
- n9: **TRELLIS.2 template profile accuracy**: within 0.6 mm 
- n10: **Trigger accuracy should-fire, old to new description**: 6/8 -> 8/8; false positives 0/6 held-out 
- n11: **img2threejs vs kiln v7 lantern**: 0.866 vs 0.861; 41,736 vs 7,552 tris; ~$10 est vs $3.52 
- n12: **Chair height vs real when size unspecified**: -29% 
- n13: **Blender version requirement and cost per session**: Blender 4.4+ (tested 5.2.2); about $1-5 per session 

## Techniques
- t1: **Measure the shipped file**: Re-import the exported GLB in Blender and measure triangles, textures, grounding and rig; never trust the session's own report.
- t2: **Scanned texture sets before procedural noise**: Pick CC0 scanned sets by thumbnail against the photo crop, tint to photo palette; avoids noise smearing on rust, wood, paint.
- t3: **3D template for proportions**: Generate a mesh (e.g. TRELLIS.2), read its profile for proportions only, and never copy its surface.
- t4: **Compress GLB output**: Apply Draco for geometry and WebP for textures; ahujasid shipped files fell from 32.85 MB to 0.96 MB.
- t5: **Sandboxed headless sessions**: Run each session outside repos with only named brief files; audit transcript for any call to results or truth.

### Code: Reproduce the bench: run briefs, compare labels, and score a GLB against Poly Haven ground truth in Blender background mode.
```bash
python3 bench/test_measure.py
python3 bench/run.py mylabel
python3 bench/report.py baseline-52 mylabel
blender -b --factory-startup --python-exit-code 1 --python bench/gt_compare.py -- --truth <poly-haven-asset>.gltf --model <asset>_final.glb --label mine
```

## Quotes (brief, for attribution)
> A figure in the skill becomes a target.  (elithril)
> Measure the file that ships. A float colour bake exported black; only the GLB showed it.  (elithril)

## Contradictions flagged
- Blender-driven sessions with the skill are cheaper or lighter than before. (vs Its own before/after table: cost rose +13% (ahujasid) and +34% (Lab MCP) on the five non-AI briefs.)
- A higher photo-fit score means a better model. (vs Doc states v4 fitted the photo best (0.898) but scored worse on the real object; a photo score above real object's (~0.80) is overfitting.)

## Points to
- https://github.com/ahujasid/blender-mcp
- Blender Lab MCP (official, behind Claude's Blender connector)
- https://github.com/img2threejs/img2threejs
- Poly Haven (CC0 textures and asset previews)
- trellis-mac
- Microsoft TRELLIS.2 (MIT)
- Hunyuan3D Space
- BiRefNet
