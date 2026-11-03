---
type: research-source
id: gh-ifBars-blender-agent-studio-f-plugins-blender-agent-studio-skills-blender-agent-benchmark-
title: "ifBars/blender-agent-studio/plugins/blender-agent-studio/skills/blender-agent-benchmark/SKILL.md"
source_type: "github"
creator: "ifBars"
url: "https://github.com/ifBars/blender-agent-studio/blob/HEAD/plugins/blender-agent-studio/skills/blender-agent-benchmark/SKILL.md"
published: "2026-10-25"
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0686
relevance: 1
density: medium
tags: ["research-source", "github", "claude-blender-mcp", "creator-workflows", "other"]
---
# gh-ifBars-blender-agent-studio-f-plugins-blender-agent-studio-skills-blender-agent-benchmark-

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
A skill doc for benchmarking Blender modeling agents, skills and MCP tools with paired isolated baseline-vs-plugin runs (Codex or Claude Code). Covers integrity rules, test suites, blinded judging, regression gates and a quick repair loop. Nothing on Roblox, export settings or the Roblox pipeline; only marginally relevant as Blender MCP evaluation methodology.

## Claims
- c1: To evaluate an MCP condition fairly under noninteractive Codex, pass --bypass-approvals to every compared condition, since MCP tool calls needing approval are cancelled; use isolated directories. *(doc, high; claude-blender-mcp)*
- c2: An available MCP tool that the agent never called cannot establish benefit; confirm actual tool use in the agent trace. The runner starts the snapshot's mcp/server.ts as bas_benchmark and checks its tool inventory. *(doc, high; claude-blender-mcp)*
- c3: benchmark_mcp.ts checks that MCP transport returns the same deterministic metrics as direct CLI evaluation. This proves transport correctness, not a modeling quality gain. *(doc, high; claude-blender-mcp)*
- c4: Fast repair loop: take one saved asset with a visible defect, make one local source repair, regenerate once, and render two fixed views at 256 resolution with blender_render_evidence. Keep the original if the repair doesn't help. Budget about five minutes. *(doc, medium; creator-workflows)*
- c5: Low triangle count must not compensate for a blockout-looking asset. Judge polished-smooth versus explicitly low-poly intent separately, and prefer blinded pairwise visual review over absolute aesthetic scores. *(opinion, medium; creator-workflows)*
- c6: The runner's --agent flag (codex default, or claude-code) selects the agent under test; launching the runner from Claude Code does not change this. Record the agent CLI and requested and observed model. *(doc, high; other)*
- c7: Benchmark integrity: isolate each condition and repetition, keep prompts identical except for explicit skill invocation, and record CLI version, model, effort, Blender build, duration, tool calls, failures and output hashes. Use at least three tasks and repeated runs before claiming a general gain. *(doc, high; other)*
- c8: The non-regression gate fails on missing baseline pairs, hard-gate loss, any per-task automated score decrease, a blinded visual majority loss, or a critical visual criterion flipping from majority-pass to fail. *(doc, high; other)*

## Numbers
- n1: **fire lantern task**: 360 frames, 24 fps, 15 s MP4 Required animation and video output for realistic_fire_lantern_showcase
- n2: **gauntlet score weights**: 60% deterministic, 25% task visual criteria, 15% multiview quality verifiedScores for gauntlet comparison
- n3: **gauntlet score caps**: 49 hard-gate fail; 84 critical criterion lost; 94 any criterion lost; 99 otherwise Caps on verified scores
- n4: **repair render resolution**: 256, two fixed views Evidence renders for before/after repair

## Techniques
- t1: **Targeted single-defect repair**: Copy source of a saved asset to a new dir, fix the top visible defect locally with one model call, regenerate once, render two fixed 256px views with identical framing before and after, and review for collateral loss.

### Code: Run the quick benchmark suite in baseline mode
```powershell
bun "<skill-root>\scripts\run_benchmark.ts" `
  --suite quick `
  --mode baseline `
  --output "<run-root>\baseline"
```

## Points to
- ifBars/blender-agent-studio
- blender_render_evidence tool
- codex exec --ignore-user-config
- ffprobe
