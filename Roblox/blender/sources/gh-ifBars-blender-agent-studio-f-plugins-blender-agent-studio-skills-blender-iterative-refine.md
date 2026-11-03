---
type: research-source
id: gh-ifBars-blender-agent-studio-f-plugins-blender-agent-studio-skills-blender-iterative-refine
title: "ifBars/blender-agent-studio/plugins/blender-agent-studio/skills/blender-iterative-refinement/SKILL.md"
source_type: "github"
creator: "ifBars"
url: "https://github.com/ifBars/blender-agent-studio/blob/HEAD/plugins/blender-agent-studio/skills/blender-iterative-refinement/SKILL.md"
published: "2026-10-25"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0014
relevance: 1
density: medium
tags: ["research-source", "github", "claude-blender-mcp", "common-mistakes-fixes", "creator-workflows"]
---
# gh-ifBars-blender-agent-studio-f-plugins-blender-agent-studio-skills-blender-iterative-refine

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Agent-skill doc for an opt-in second refinement pass on a finished Blender deliverable. Covers freezing the candidate and invariants, a pass/fail/unclear visual critic ledger, one targeted durable-source repair, identical recheck, and retain-or-rollback decisions logged to iteration_review.json. Mentions blender_quality_report and blender_compare_scenes tools. No Roblox-specific content.

## Claims
- c1: Skill references MCP tools blender_quality_report and blender_compare_scenes; compare takes candidate as baseline and supports invariantObjects for parts allowed to change. *(doc, medium; claude-blender-mcp)*
- c2: Refinement pass is opt-in: only runs when user asks to critique/improve or a benchmark requires before/after evidence; it adds a critic, repair, and recheck on top of normal build stages. *(doc, high; creator-workflows)*
- c3: Aggregate scene.bounds.dimensions, not only the largest mesh, must satisfy any global size limit. *(doc, high; common-mistakes-fixes)*
- c4: Bounds overlap alone cannot prove mesh intersection; review_required from the compare tool is not a pass. *(doc, high; common-mistakes-fixes)*
- c5: Repair edits durable Python or editable Blender source and regenerates authored and exported artifacts; derived files are not hand-patched. *(doc, medium; creator-workflows)*
- c6: If primary subject or causal layout is wrong, rebuild that portion before doing cosmetic polish; retain repair only if no critical requirement or hard gate regresses. *(doc, medium; creator-workflows)*
- c7: Transmissive enclosures and emissive subjects are a coupled visibility problem; a valid shader graph is not enough if glass renders opaque or emission blooms to white. *(doc, medium; common-mistakes-fixes)*

## Techniques
- t1: **Evidence-backed critic-repair-recheck loop**: Freeze candidate source, export, metrics and hero/multiview renders. Write pass/fail/unclear ledger from images. Fix one smallest source cause. Re-render identically, compare side by side, retain only if no regressions; else restore candidate and log decision in iteration_review.json.

## Quotes (brief, for attribution)
> Aggregate scene.bounds.dimensions, not only the largest mesh, satisfies any global size limit.  (ifBars)
> review_required is not a pass, and bounds overlap alone cannot prove a mesh intersection.  (ifBars)

## Points to
- references/astra-workflow.md
- blender_quality_report
- blender_compare_scenes
- iteration_review.json
