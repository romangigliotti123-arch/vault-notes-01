---
type: research-source
id: gh-ifBars-blender-agent-studio-f-plugins-blender-agent-studio-skills-blender-procedural-workf
title: "ifBars/blender-agent-studio/plugins/blender-agent-studio/skills/blender-procedural-workflow/SKILL.md"
source_type: "github"
creator: "ifBars"
url: "https://github.com/ifBars/blender-agent-studio/blob/HEAD/plugins/blender-agent-studio/skills/blender-procedural-workflow/SKILL.md"
published: "2026-10-25"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0010
relevance: 1
density: medium
tags: ["research-source", "github", "other", "procedural-generation"]
---
# gh-ifBars-blender-agent-studio-f-plugins-blender-agent-studio-skills-blender-procedural-workf

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Agent skill doc for building reproducible Blender Geometry Nodes and procedural scenes. Covers a parameter contract, layered graph authoring, seeded randomness from stable IDs, instancing vs realization, and tests across default, min, max and seeded variations. Notes that GLB and other runtime formats drop Geometry Nodes behaviour. Not Roblox-specific.

## Claims
- c1: Geometry Nodes output must be realized or baked before export because GLB and other runtime formats do not preserve Geometry Nodes behaviour. *(doc, high; procedural-generation)*
- c2: Prefer instancing for repeated assets; realize instances only when an operation or export needs real geometry, and measure triangle counts and memory after realization. *(doc, high; procedural-generation)*
- c3: Random variation should derive from stable element IDs rather than evaluation order so instances stay stable across revisions. *(doc, high; procedural-generation)*
- c4: A graph that looks correct at one seed or density is not reusable; test default, min, max and at least one seeded variation, plus empty and dense inputs. *(opinion, medium; procedural-generation)*
- c5: Keep dependent constants in durable Python source so agents can regenerate node setups; name node groups, sockets, modifiers and collections semantically. *(doc, medium; procedural-generation)*
- c6: Completion gate requires source script, .blend file, parameter list, seed, input-asset requirements and test evidence. *(doc, medium; other)*

## Techniques
- t1: **Layered generator authoring**: Start with minimal graph proving main transform or placement, test from multiple views, then add variation and expose only meaningful group-interface controls with units, ranges and defaults.
- t2: **Terrain/scatter validation**: Check slope, normal alignment, collision or exclusion zones, density falloff, scale range, clipping and silhouette on evaluated output.

## Quotes (brief, for attribution)
> GLB and other runtime formats do not preserve Geometry Nodes behavior.  (ifBars)

## Points to
- references/astra-workflow.md
- $blender-agent-studio:blender-asset-validation
- $blender-agent-studio:blender-rendering-workflow
