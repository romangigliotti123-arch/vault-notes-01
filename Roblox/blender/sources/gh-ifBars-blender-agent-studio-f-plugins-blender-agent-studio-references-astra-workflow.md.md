---
type: research-source
id: gh-ifBars-blender-agent-studio-f-plugins-blender-agent-studio-references-astra-workflow.md
title: "ifBars/blender-agent-studio/plugins/blender-agent-studio/references/astra-workflow.md"
source_type: "github"
creator: "ifBars"
url: "https://github.com/ifBars/blender-agent-studio/blob/HEAD/plugins/blender-agent-studio/references/astra-workflow.md"
published: "2026-10-25"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0019
relevance: 1
density: low
tags: ["research-source", "github", "claude-blender-mcp", "common-mistakes-fixes", "creator-workflows", "texturing-baking-uv"]
---
# gh-ifBars-blender-agent-studio-f-plugins-blender-agent-studio-references-astra-workflow.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Agent-skill guidance (Codex/Claude Code, "Astra" model profile) for Blender modeling work. Covers gathering reference images before modeling, whole-asset review coverage, checkpoint files, and export/render gates. No Roblox-specific content; the bundled MCP is described only as a bounded batch evaluator.

## Claims
- c1: The bundled Blender MCP is described as a bounded batch evaluator and does not add Responses API async support. *(doc, medium; claude-blender-mcp)*
- c2: For new recognizable subjects, the workflow requires inspecting real reference images (roughly 3-6 useful views) before detailed modeling; generated concepts cannot verify unseen geometry. *(doc, high; creator-workflows)*
- c3: Compare graybox and final model against chosen references from similar angles and record concrete mismatches before repair. *(doc, high; creator-workflows)*
- c4: Map full review coverage (reverse sides, broad surfaces, top/underside) before polishing a hero view to avoid a dressed focal area surrounded by blank construction. *(doc, medium; creator-workflows)*
- c5: Trigger fresh export/import checks early for export-sensitive changes (topology, modifiers, transforms, hierarchy, skinning, materials, actions); at completion reproduce final source in a clean process. *(doc, medium; creator-workflows)*
- c6: Keep reference_notes.md (source URL, image path, angle, feature informed, uncertainty, license) and work_state.md (brief, accepted decisions, source hash, defects, next action) beside the source for resumable work. *(doc, medium; creator-workflows)*
- c7: Ask at most one to three focused clarifying questions only for consequential ambiguity; otherwise record defaults and continue. *(doc, medium; creator-workflows)*
- c8: Do not equate originality with rebuilding every texture procedurally; sourced scanned materials/HDRIs are acceptable for photoreal scenes if recorded and inspected. *(doc, low; texturing-baking-uv)*
- c9: Common humanoid failure patterns to check early: oversized boxy torsos and shoes, disconnected pelvis/limbs, unfitted garment details, oversized thumbs, inconsistent skin patches. *(opinion, medium; common-mistakes-fixes)*

## Numbers
- n1: **reference images for new subject**: roughly 3-6 
- n2: **clarifying questions allowed**: 1-3 

## Techniques
- t1: **Reference coverage by question**: Pick views by question: front for width, profile for depth, three-quarter for volume, close-ups for joints. Include whole-subject views. Label analogues, don't blend variants.
- t2: **Checkpoint files for long work**: Maintain work_state.md with brief, decisions, source hash, evidence paths, defects, pending jobs. Verify files and job state on resume.

## Points to
- https://github.com/ifBars/blender-agent-studio/blob/HEAD/plugins/blender-agent-studio/references/astra-workflow.md
- https://developers.openai.com/api/docs/guides/latest-model
