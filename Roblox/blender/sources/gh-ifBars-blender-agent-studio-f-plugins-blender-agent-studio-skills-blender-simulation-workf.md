---
type: research-source
id: gh-ifBars-blender-agent-studio-f-plugins-blender-agent-studio-skills-blender-simulation-workf
title: "ifBars/blender-agent-studio/plugins/blender-agent-studio/skills/blender-simulation-workflow/SKILL.md"
source_type: "github"
creator: "ifBars"
url: "https://github.com/ifBars/blender-agent-studio/blob/HEAD/plugins/blender-agent-studio/skills/blender-simulation-workflow/SKILL.md"
published: "2026-10-25"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0010
relevance: 1
density: low
tags: ["research-source", "github", "bpy-scripting-headless", "other"]
---
# gh-ifBars-blender-agent-studio-f-plugins-blender-agent-studio-skills-blender-simulation-workf

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Agent-skill doc for Blender physics simulation workflow (fluid, smoke, rigid body, cloth, particles, hair). Covers simulation contracts, preview-before-final bakes, cache provenance, and validation gates. Does not mention Roblox, blender-mcp, or the Roblox export pipeline; mostly off-topic for this research target.

## Claims
- c1: Simulation is a cache-producing build step; a plausible single frame is not proof of stability. Preview cache must be inspected before costly final bake. *(doc, high; other)*
- c2: Final cache uses the Python enum ALL; UI labels are not necessarily enum identifiers. *(doc, high; bpy-scripting-headless)*
- c3: Never overwrite an approved bake without a new output location or explicit user approval; use project-local cache outside source control. *(doc, high; other)*
- c4: Reopen saved scene in a fresh Blender process and re-inspect frames before declaring a bake complete; a fluid modifier or replay cache is not a completed bake. *(doc, high; other)*

## Techniques
- t1: **Preview-then-final bake**: Run short coarse preview cache, inspect critical frames from two cameras, change one causal parameter group at a time, rebake smallest interval, then bake final and verify every cache file exists.

## Points to
- references/astra-workflow.md
- $blender-agent-studio:blender-rendering-workflow
