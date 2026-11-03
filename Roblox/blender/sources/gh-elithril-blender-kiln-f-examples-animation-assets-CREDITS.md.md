---
type: research-source
id: gh-elithril-blender-kiln-f-examples-animation-assets-CREDITS.md
title: "elithril/blender-kiln/examples/animation/assets/CREDITS.md"
source_type: "github"
creator: "elithril"
url: "https://github.com/elithril/blender-kiln/blob/HEAD/examples/animation/assets/CREDITS.md"
published: "2026-10-29"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0007
relevance: 1
density: low
tags: ["research-source", "github", "bpy-scripting-headless", "other", "rigging-animation"]
---
# gh-elithril-blender-kiln-f-examples-animation-assets-CREDITS.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
CREDITS file for a Blender "kiln" example repo's animation showcase. Lists asset sources and licences: a kiln-built rigged villager (MIT), a Poly Pizza cat rigged by a script (CC BY 3.0), a Quaternius dragon (CC0), and Poly Haven wood/metal scans (CC0) downloaded at run time by chest.py. Says nothing about Roblox export or Claude/blender-mcp workflows.

## Claims
- c1: Asset licence attribution file: cat model is CC BY 3.0 (credit madtrollstudio); dragon and Poly Haven textures are CC0; villager is MIT. *(doc, high; other)*
- c2: Chest example script chest.py downloads Poly Haven textures (rough_wood, rusty_metal_04) at run time instead of shipping them in the repo. *(doc, high; bpy-scripting-headless)*
- c3: Cat model is rigged by a script (rig_cat.py) after import; lamp is modelled, rigged and animated from scratch by props.py. *(doc, high; rigging-animation)*

## Techniques
- t1: **Script-downloaded CC0 textures**: Keep third-party texture scans out of the repo; have the build script fetch them from Poly Haven at run time.

## Points to
- https://poly.pizza/m/YvVobPlTlQ
- https://poly.pizza/m/VBvzjFIYws
- https://creativecommons.org/licenses/by/3.0/
- https://polyhaven.com/a/rough_wood
- https://polyhaven.com/a/rusty_metal_04
- https://polyhaven.com
