---
type: research-source
id: gh-ifBars-blender-agent-studio-readme
title: "ifBars/blender-agent-studio README: Free, open-source Blender AI plugin for the tools you already use. Codex and Claude Code installers, loc"
source_type: "github"
creator: "ifBars"
url: "https://github.com/ifBars/blender-agent-studio"
published: "2026-10-25"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0032
relevance: 2
density: medium
tags: ["research-source", "github", "bpy-scripting-headless", "claude-blender-mcp", "common-mistakes-fixes", "creator-workflows", "other", "procedural-generation", "rigging-animation", "texturing-baking-uv"]
---
# gh-ifBars-blender-agent-studio-readme

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
README for Blender Agent Studio, a free MIT plugin that lets Claude Code or Codex drive a local Blender via bundled skills and a local MCP server. Covers install, Blender discovery, a headless setup check, and paired evaluation results. Contains nothing on Roblox export, import, mesh limits, or UGC. Relevant only as a general Claude-to-Blender reference.

## Claims
- c1: Plugin installs into Claude Code via 'claude plugin marketplace add ifBars/blender-agent-studio' then 'claude plugin install blender-agent-studio@blender-agent-studio'; Codex uses the 'codex plugin' equivalents. *(doc, high; claude-blender-mcp)*
- c2: Requires Claude Code or Codex, Blender (5.2 LTS is the tested version) and Bun 1.3.5 or newer. No API key, subscription or extra service beyond the agent itself. *(doc, high; claude-blender-mcp)*
- c3: Ships twelve specialist skills and a local MCP server for inspection, rendering and asset downloads; the agent runs blender_check_setup to find Blender, save/reopen a tiny scene and render a preview. *(doc, high; claude-blender-mcp)*
- c4: Blender discovery order: tool blenderPath or --blender flag, then BLENDER_EXECUTABLE env var, then blender on PATH, then standard install locations; a wrong configured path is reported, not replaced. Env var must point to the executable, not its folder. *(doc, high; bpy-scripting-headless)*
- c5: 'bun run doctor' saves and reopens a tiny scene, renders a 128px Cycles CPU preview and a 64px EEVEE render; needs no GPU, downloads or Rust. EEVEE failure on headless Linux is a warning (OpenGL needed for studio views). *(doc, high; bpy-scripting-headless)*
- c6: Generated scenes come with Python source that records build steps, so the scene can be regenerated or edited later; output is an editable .blend plus the script. *(doc, high; claude-blender-mcp)*
- c7: Supports props, environments, characters and Geometry Nodes setups; rigging, animation and cloth/smoke simulations are listed as capabilities, with no Roblox-specific limits stated. *(doc, medium; procedural-generation)*
- c8: Downloads CC0 textures and HDRIs from Poly Haven at 1K, 2K, 4K or 8K via the MCP tools. *(doc, high; texturing-baking-uv)*
- c9: Can import downloaded Mixamo FBX animations into a new .blend via a browser handoff; retargeting limits are documented separately. *(doc, medium; rigging-animation)*
- c10: Paired evaluation (5 Codex pairs, lantern, lever press, drawbridge): plugin runs passed the technical gate 5/5 vs 5/5 failures for baseline; blinded judges preferred plugin asset in 4 of 5 pairs. Author states five pairs cannot give a reliable success rate. *(data, high; creator-workflows)*
- c11: Later Claude Code scene comparisons (Sonnet 5.5, Opus 5.5) are mixed; the README says the selected hero image does not establish a general visual advantage. Plugin used more reported tokens; some plugin runs took about twice as long. *(data, medium; creator-workflows)*
- c12: Renders a hero view plus fixed front, back, left, right and top views for checking; repairs can use two smaller views for faster feedback. *(doc, medium; common-mistakes-fixes)*
- c13: Opinion of author-facing framing: 'free' refers to plugin only; the agent subscription the user already pays for is still required. *(opinion, low; other)*

## Numbers
- n1: **Blender version tested**: 5.2 LTS 
- n2: **Bun minimum**: 1.3.5 
- n3: **Setup check preview sizes**: 128px Cycles CPU; 64px EEVEE 
- n4: **Bundled specialist skills**: 12 
- n5: **Initial paired comparison**: 5 pairs; technical gate plugin 5/5 pass vs baseline 5/5 fail; visual preference 4/5 
- n6: **Published gallery pairs**: 31 
- n7: **Poly Haven texture resolutions**: 1K, 2K, 4K, 8K 
- n8: **Plugin build time vs baseline**: about even on lantern (3 pairs); about 2x on press and drawbridge 

## Techniques
- t1: **Point the plugin at a specific Blender**: Set BLENDER_EXECUTABLE to the executable file (not its folder) in the same shell that launches the CLI agent, or pass --blender to bun run doctor. Restart the conversation if env changes are not inherited.
- t2: **Headless setup verification**: Run 'bun run doctor' from plugin checkout. It writes .blend, previews, logs and a JSON report to a new temp folder; nonzero exit means failure.
- t3: **Multi-view review loop**: Render hero view plus fixed front/back/left/right/top; ask agent to inspect images and repair; use two smaller views during repairs for speed.

### Code: Install the plugin into Claude Code
```bash
claude plugin marketplace add ifBars/blender-agent-studio
claude plugin install blender-agent-studio@blender-agent-studio
```

### Code: Set Blender executable for discovery (macOS example)
```bash
export BLENDER_EXECUTABLE="/Applications/Blender.app/Contents/MacOS/Blender"
```

### Code: Set Blender executable for discovery (Windows example)
```powershell
$env:BLENDER_EXECUTABLE = "C:\path\to\Blender\blender.exe"
```

### Code: Run setup check without an agent
```bash
bun run doctor
```

## Quotes (brief, for attribution)
> It runs your local Blender and needs no extra service, API key or subscription beyond the agent you already use.  (ifBars)
> Five pairs cannot give a reliable success rate for arbitrary prompts, models, or art styles.  (ifBars)

## Points to
- https://ifbars.github.io/blender-agent-studio/
- https://github.com/ifBars/blender-agent-studio
- https://ifbars.github.io/blender-agent-studio/bring-your-agent/
- https://skills.sh/ifbars/blender-agent-studio
- https://polyhaven.com
- https://code.claude.com
- https://www.blender.org/download/
