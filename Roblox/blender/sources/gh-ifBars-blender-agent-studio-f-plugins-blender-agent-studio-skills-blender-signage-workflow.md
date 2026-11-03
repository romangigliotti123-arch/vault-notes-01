---
type: research-source
id: gh-ifBars-blender-agent-studio-f-plugins-blender-agent-studio-skills-blender-signage-workflow
title: "ifBars/blender-agent-studio/plugins/blender-agent-studio/skills/blender-signage-workflow/SKILL.md"
source_type: "github"
creator: "ifBars"
url: "https://github.com/ifBars/blender-agent-studio/blob/HEAD/plugins/blender-agent-studio/skills/blender-signage-workflow/SKILL.md"
published: "2026-10-25"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0015
relevance: 1
density: low
tags: ["research-source", "github", "common-mistakes-fixes", "creator-workflows", "other", "texturing-baking-uv"]
---
# gh-ifBars-blender-agent-studio-f-plugins-blender-agent-studio-skills-blender-signage-workflow

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Agent skill doc for designing signs and surface graphics on Blender props: separate face and carrier, 2D layout trials, view-distance readability sizing, font/icon rights, and raster sizing. Not about Roblox, blender-mcp, or bpy scripting specifically. Mentions UV and export steps only by reference to other files.

## Claims
- c1: Sign face and physical carrier should be authored as separate assets; compose the graphic in a 2D tool, then integrate with the model and review in context. *(doc, high; texturing-baking-uv)*
- c2: Render vector-like graphics larger and downsample with a quality filter for clean edges; the original implementation used 3x, which is described as a choice, not a rule. *(doc, high; texturing-baking-uv)*
- c3: Size the raster to projected use, target texture budget and physical aspect ratio; power-of-two dimensions are not universal rules. *(doc, high; texturing-baking-uv)*
- c4: Do not silently shrink important text below useful viewing size; resolve overflow by editing layout or agreed copy. *(opinion, medium; creator-workflows)*
- c5: Do not substitute a closer camera, sharper texture or higher render resolution for an appropriately sized layout when text is weak. *(opinion, medium; creator-workflows)*
- c6: Keep exact text editable and deterministic (SVG, layered design file, or reproducible drawing script); verify generated text rather than trusting it. *(opinion, medium; creator-workflows)*
- c7: A board with default floating text is rarely a finished sign; check every required line at delivery resolution, not just a zoomed crop. *(opinion, medium; common-mistakes-fixes)*
- c8: Avoid relying on emoji or unverified symbol-font coverage; check font character coverage for every language including punctuation. *(opinion, medium; other)*

## Numbers
- n1: **supersampling factor**: 3x Original implementation renders vector-like graphics at 3x then downsamples

## Techniques
- t1: **Measured layout trial**: Compare two or three cheap flat layout candidates before housing build; vary line breaks, occupied width and type weight, not just palette. Measure glyph bounds and line widths.
- t2: **View-distance sizing pass**: Classify each line as identification, required action, or optional detail; size required text for the intended viewing distance. Referenced in linked file, not detailed here.
- t3: **Flat-face review at in-scene pixel size**: Open the flat face at full size and at estimated in-scene pixel size; review longest label and densest layout before producing the whole family.

## Quotes (brief, for attribution)
> A board with default floating text is rarely a finished sign.  (ifBars)
> Do not substitute a closer camera, sharper texture or higher render resolution for an appropriately sized layout.  (ifBars)

## Points to
- references/astra-workflow.md
- references/face-spec.md
- references/surface-integration.md
