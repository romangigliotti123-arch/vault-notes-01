---
type: research-source
id: gh-elithril-blender-kiln-rel-v1.1.1
title: "elithril/blender-kiln v1.1.1: v1.1.1 — the HuggingFace path, verified live"
source_type: "github"
creator: "elithril"
url: "https://github.com/elithril/blender-kiln/releases/tag/v1.1.1"
published: "2026-08-26"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0017
relevance: 1
density: medium
tags: ["research-source", "github", "common-mistakes-fixes", "procedural-generation"]
---
# gh-elithril-blender-kiln-rel-v1.1.1

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Patch note for elithril/blender-kiln v1.1.1, a tool that generates 3D models via a HuggingFace Spaces (Hunyuan3D) backend. Covers a paused default Space, a documented API flow that did not match the live endpoints, and a README install check that missed a bare pip install. Nothing on Roblox export or Claude-Blender control.

## Claims
- c1: Default HF Space jbowyer/Hunyuan3D-2.1 (community duplicate) returns HTTP 200 but gradio_client raises 'space is in the invalid state: PAUSED'. *(demo, high; procedural-generation)*
- c2: Default backend changed to vendor's tencent/Hunyuan3D-2 Space in v1.1.1. *(doc, high; procedural-generation)*
- c3: Documented two-step flow ending in /on_export_click does not exist in the Space API; live gradio_client 2.6.1 showed 12 named endpoints. *(demo, high; procedural-generation)*
- c4: /shape_generation (4 returns) and /generation_all (5 returns) both take the same 13 parameters, all defaulted. *(demo, high; procedural-generation)*
- c5: randomize_seed defaults to True, so Hunyuan runs are not reproducible unless set False and seed fixed; matters for batch re-runs. *(doc, high; procedural-generation)*
- c6: verify_docs.py exempted text inside backticks, so a bare 'pip install' in a README dependency table passed the audit. *(demo, high; common-mistakes-fixes)*
- c7: Removing the backtick exemption produced four false positives earlier; author judges silent misses costlier than false positives. *(doc, medium; common-mistakes-fixes)*
- c8: Per-file line-count check from v1.1.0 failed CI immediately when ai-generation.md dropped from 270 to 215 lines. *(demo, high; common-mistakes-fixes)*
- c9: Community duplicate Spaces depend on one person paying for GPU; this is why the old default died (author's view). *(opinion, medium; procedural-generation)*

## Numbers
- n1: **Endpoints in Space API**: 12 named Live read via gradio_client 2.6.1
- n2: **Parameters per generation endpoint**: 13, all defaulted /shape_generation and /generation_all
- n3: **Returns**: /shape_generation 4; /generation_all 5 Return value counts per endpoint
- n4: **Regression suite**: 13/13 verify_docs checker tests after fix
- n5: **ai-generation.md line count**: 270 to 215 Stale README caught by CI line-count check

## Techniques
- t1: **Check Space runtime stage before connecting**: Read the Space's runtime stage with a one-liner before calling gradio_client, since HTTP 200 does not mean the Space is running. Print the API with view_api() to get real endpoint signatures when the Space changes.
- t2: **Per-file line-count doc check in CI**: Compare each doc file's line count against a recorded value; fail CI when a doc changes size so stale docs are caught on the commit that makes them stale.

## Quotes (brief, for attribution)
> It answers HTTP 200 — the page looks fine — but gradio_client refuses  (elithril)
> a prescription in markdown is written in backticks  (elithril)

## Contradictions flagged
- The documented API flow ending in /on_export_click works as written. (vs Live Space API has no /on_export_click endpoint (v1.1.0 documentation))
- Community duplicate Space is a valid default backend. (vs Duplicate was PAUSED; vendor Space used instead in v1.1.1)

## Points to
- https://github.com/elithril/blender-kiln/releases/tag/v1.1.1
- https://huggingface.co/spaces/tencent/Hunyuan3D-2
- Jbowyer/Hunyuan3D-2.1 (HF community duplicate, paused)
- gradio_client 2.6.1
- CHANGELOG.md in elithril/blender-kiln
- v1.1.0 release of elithril/blender-kiln
