---
type: research-source
id: gh-ifBars-blender-agent-studio-f-plugins-blender-agent-studio-skills-blender-art-direction-in
title: "ifBars/blender-agent-studio/plugins/blender-agent-studio/skills/blender-art-direction-intake/SKILL.md"
source_type: "github"
creator: "ifBars"
url: "https://github.com/ifBars/blender-agent-studio/blob/HEAD/plugins/blender-agent-studio/skills/blender-art-direction-intake/SKILL.md"
published: "2026-10-25"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0012
relevance: 1
density: low
tags: ["research-source", "github", "creator-workflows"]
---
# gh-ifBars-blender-agent-studio-f-plugins-blender-agent-studio-skills-blender-art-direction-in

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Agent skill (SKILL.md) for clarifying a Blender creation brief before modeling. Covers which decisions need user input versus default assumptions, optional concept-image generation, and a hand-off working contract with evidence-mapped requirements. Not specific to Roblox export or blender-mcp; no pipeline steps, settings, or code.

## Claims
- c1: Skill asks only 1-3 highest-impact questions for consequential ambiguities; routine settings (names, preview resolution, folders) get default assumptions without a survey. *(doc, high; creator-workflows)*
- c2: Concept/mockup image generation is optional; a concept guides silhouette, materials, palette and camera but is not the final 3D asset and is not a prerequisite for geometry. *(doc, high; creator-workflows)*
- c3: Image generation does not guarantee manufacturable geometry, clean topology, rigging, or a usable texture set. *(doc, high; creator-workflows)*
- c4: Working contract maps each must-have to evidence (named view, motion phase, measured constraint, or export check) and marks requirements verified, failed, unclear or not tested. *(doc, high; creator-workflows)*
- c5: Requirement must never be marked verified from an object name alone. *(doc, high; creator-workflows)*
- c6: Questions must be asked when plausible answers change identity, silhouette, style, motion, simulation type, or deliverable (e.g., human vs creature, realistic vs cartoon, liquid vs smoke, static sculpt vs rigged avatar, single-view illusion vs full 3D asset). *(doc, high; creator-workflows)*

## Techniques
- t1: **Art-direction intake contract**: Resolve subject, style, platform, scale, export target, constraints from request and references; record assumptions; bundle 1-3 questions with recommended option; write working contract; map must-haves to evidence; then invoke smallest workflow.

## Quotes (brief, for attribution)
> A concept is not a prerequisite for geometry.  (ifBars)
> it will guide silhouette, materials, palette, and camera—not become the final 3D asset.  (ifBars)

## Points to
- references/astra-workflow.md
