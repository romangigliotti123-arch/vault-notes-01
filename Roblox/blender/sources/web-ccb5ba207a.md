---
type: research-source
id: web-ccb5ba207a
title: "Roblox docs: studio/material-generator"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/studio/material-generator.md"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0010
relevance: 1
density: low
tags: ["research-source", "web", "other"]
---
# web-ccb5ba207a

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox Studio doc on the Material Generator: type a text prompt, click Generate, pick a result, adjust Studs Per Tile and Organic toggle, choose a Base Material, then Save & Apply Variant to the Material Manager. Tips: use "close up"/"top down"/"texture" for close-ups, "simple"/"pattern"/"symmetrical"/"flat" for repeating patterns, "grayscale" to allow tinting. Does not cover Blender, bpy, blender-mcp, or FBX/mesh import.

## Claims
- c1: Material Generator creates material variants from text prompts inside Roblox Studio, not via Blender. *(doc, high; other)*
- c2: Saved generated materials go to the Material Manager; Base Material sets default physical properties. *(doc, high; other)*
- c3: Same keywords produce different results on every Generate click. *(doc, high; other)*

## Techniques
- t1: **Keyword prompting for materials**: Add 'close up', 'top down', or 'texture' for close-up patterns; 'simple', 'pattern', 'symmetrical', 'flat' for repeating patterns; 'photorealistic', 'cartoon', 'hand-drawn' for style; 'grayscale' so the result can be tinted later.

## Points to
- Roblox docs: parts/materials.md (Material widget, Material Manager, default physical properties)
