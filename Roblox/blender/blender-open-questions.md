---
type: research-open-questions
topic: "Blender 3D for Roblox Studio: using Claude with Blender (blender-mcp, bpy scripting) and the Blender-to-Roblox asset pipeline"
date: 2026-11-01
---
# Open questions and gaps: Blender 3D for Roblox Studio: using Claude with Blender (blender-mcp, bpy scripting) and the Blender-to-Roblox asset pipeline

## Questions the synthesis could not answer
- **Does any official source document using Claude or blender-mcp for a Roblox pipeline?** The notes find none, so the workflow is unverified end to end.
- **Which Blender versions does the Roblox plugin truly support (4.x versus 5.x)?** Sources conflict on 4.x.
- **What is the current accessory publishing cost?** Sources give different Robux figures.
- **Do the bpy API drift claims (Principled inputs, slotted actions) hold on current Blender?** They come from single, possibly outdated sources.
- **Is the glTF linear-image near-black bug real and still present?** It is a single, possibly outdated report on Blender 5.2.2.
- **Does the official Blender Lab MCP server share the stdin hang bug?** This is a reporter claim only.
- **What exact texture connection settings does Studio need for Blender materials?** They live on a separate page (assign-textures.md) not covered in the notes.
- **How should Scale Factor be handled for projects authored before the 2026-06-16 change?** Existing meter-authored assets may import at different sizes.

## Gaps noted per theme
- No official-source coverage of blender-mcp or Claude-driven bpy workflows in these notes.  ([[blender-topic-automation-and-creator-workflows|Open Cloud automation, plugins and what top creators do]])
- Whether the plugin itself uses the newer .rbxm/animation Open Cloud support is not confirmed (animations were pending as of v1.0.3).  ([[blender-topic-automation-and-creator-workflows|Open Cloud automation, plugins and what top creators do]])
- Unclear whether Reimport works with Blender-plugin packages end to end.  ([[blender-topic-automation-and-creator-workflows|Open Cloud automation, plugins and what top creators do]])
- Little detail on what top creators automate beyond batch rename/manifest runners.  ([[blender-topic-automation-and-creator-workflows|Open Cloud automation, plugins and what top creators do]])
- Rate limits and quotas for mesh/model uploads via API are not given.  ([[blender-topic-automation-and-creator-workflows|Open Cloud automation, plugins and what top creators do]])
- No coverage of how Claude or blender-mcp scripting automates cage, rig or attachment creation for avatar items.  ([[blender-topic-avatar-ugc-accessories|Avatar, UGC and accessories]])
- Exact Blender FBX/glTF export settings for each avatar item type are not given, only that they exist.  ([[blender-topic-avatar-ugc-accessories|Avatar, UGC and accessories]])
- Current Marketplace fees and price floors are inconsistent and lack an authoritative recent source.  ([[blender-topic-avatar-ugc-accessories|Avatar, UGC and accessories]])
- Details of classic 2D clothing (shirt/pants templates) are minimal, covered only by one video.  ([[blender-topic-avatar-ugc-accessories|Avatar, UGC and accessories]])
- The 19 attachment names for bodies are not enumerated.  ([[blender-topic-avatar-ugc-accessories|Avatar, UGC and accessories]])
- Exact thresholds in the UGC Validation and Asset Quality scoring are not given.  ([[blender-topic-avatar-ugc-accessories|Avatar, UGC and accessories]])
- No source gives the exact glTF export settings to use in Blender for Roblox. Most settings guidance is for FBX.  ([[blender-topic-blender-roblox-export-import|Blender to Roblox export, import and common mistakes]])
- The root cause of several plugin 'Unknown Error' and 'Add-on error' reports was never established.  ([[blender-topic-blender-roblox-export-import|Blender to Roblox export, import and common mistakes]])
- Whether the June 16, 2026 scale change shipped as planned is not verified. Sources are pre-announcements.  ([[blender-topic-blender-roblox-export-import|Blender to Roblox export, import and common mistakes]])
- There is no Blender-specific guidance on using blender-mcp or bpy scripts for export, and no Roblox export preset exists in the surveyed MCP tools.  ([[blender-topic-blender-roblox-export-import|Blender to Roblox export, import and common mistakes]])
- The Reimport YouTube demo comes from a source with insufficient credibility. Its claims are only corroborated by the official Reimport announcement.  ([[blender-topic-blender-roblox-export-import|Blender to Roblox export, import and common mistakes]])
- No source covers Claude-driven export from Blender to Roblox (FBX/glTF settings, scale, cages) in an automated flow; the Roblox export sources are manual-only.  ([[blender-topic-claude-blender-ai|Claude + Blender: MCP servers, bpy scripting, headless Blender, procedural and AI-assisted modelling]])
- No evidence on Roblox-specific constraints (triangle limits, mesh validation) applied through bpy or MCP.  ([[blender-topic-claude-blender-ai|Claude + Blender: MCP servers, bpy scripting, headless Blender, procedural and AI-assisted modelling]])
- Little first-party documentation on the Anthropic/Claude side. The Blender Lab MCP example uses llama.cpp.  ([[blender-topic-claude-blender-ai|Claude + Blender: MCP servers, bpy scripting, headless Blender, procedural and AI-assisted modelling]])
- The key addon claims (integrations off, scene-clear, API drift) rest on a single repo or skill docs and lack independent verification.  ([[blender-topic-claude-blender-ai|Claude + Blender: MCP servers, bpy scripting, headless Blender, procedural and AI-assisted modelling]])
- No benchmarks of AI-generated modelling quality beyond the single-source reference-image fidelity workflow.  ([[blender-topic-claude-blender-ai|Claude + Blender: MCP servers, bpy scripting, headless Blender, procedural and AI-assisted modelling]])
- No Roblox-specific texel-density or vertex-count guidance for non-avatar environment props beyond the 20k mesh cap.  ([[blender-topic-mesh-texture-limits|Mesh limits, UVs, textures, PBR and performance]])
- Unclear whether the 256 PBR accessory cap (2025-07) still holds after the 2k texture update (2026-02).  ([[blender-topic-mesh-texture-limits|Mesh limits, UVs, textures, PBR and performance]])
- No verified Blender shader setup details for PBR import; the DevForum post is referenced but not summarized.  ([[blender-topic-mesh-texture-limits|Mesh limits, UVs, textures, PBR and performance]])
- Whether Mesh Streaming Phase 2 default-on actually shipped is not confirmed.  ([[blender-topic-mesh-texture-limits|Mesh limits, UVs, textures, PBR and performance]])
- Generic platform budgets (VRChat etc.) are not Roblox-specific and don't give Roblox performance numbers.  ([[blender-topic-mesh-texture-limits|Mesh limits, UVs, textures, PBR and performance]])
- No source in this bucket gives concrete Roblox FBX/glTF export settings, scale, axis, or triangle/texture limits.  ([[blender-topic-other|other]])
- No evidence on how blender-mcp tools specifically map to the Roblox Studio import flow.  ([[blender-topic-other|other]])
- Few dated sources for the Blender-side Roblox plugin behavior beyond the token issue.  ([[blender-topic-other|other]])
- The reliability of several creator video claims is unchecked (cred=INSUFFICIENT), so none were used as key support.  ([[blender-topic-other|other]])
- Which blender-mcp variant each README or release note describes is often unclear.  ([[blender-topic-other|other]])
- No source documents blender-mcp Claude prompts that produce Roblox-compliant R15 rigs. The MCP rigging tools (S178, S184, S196) do not mention R15 or Motor6D.  ([[blender-topic-rigging-animation|Rigging and animation for Roblox]])
- Little detail on how to author AnimationConstraint-compatible rigs from Blender after the AJU change.  ([[blender-topic-rigging-animation|Rigging and animation for Roblox]])
- No hard numbers on animation import fidelity such as frame rate or scale factor values.  ([[blender-topic-rigging-animation|Rigging and animation for Roblox]])
- Dynamic head and FACS rigging from Blender is barely covered, and the S247 FACS bug is unresolved.  ([[blender-topic-rigging-animation|Rigging and animation for Roblox]])
- Several R15 doc sources are undated, so version currency is unclear.  ([[blender-topic-rigging-animation|Rigging and animation for Roblox]])
- Evidence for the vertex-count tiers comes from one author's tests (S55, S65, S72), which share a repository.  ([[blender-topic-rigging-animation|Rigging and animation for Roblox]])

## Not processed
| source | done | pending | skipped | failed |
|---|---|---|---|---|
| github | 205 | 0 | 628 | 0 |
| papers | 74 | 0 | 0 | 0 |
| reddit | 3 | 0 | 97 | 0 |
| web | 374 | 0 | 136 | 0 |
| youtube | 585 | 0 | 68 | 0 |

Skipped/failed reasons: pruned: repo (604), pruned: kw-web (102), pruned: kw-reddit (82), no captions and whisper fallback not allowed (57), too-short (30), pruned: nav (16), reddit unreachable (15), pruned: cube (12)
Largest unprocessed back-catalogues: none (everything selected was processed or skipped)
Unreachable or blocked: web devforum.roblox.com (no RSS/Atom feed found; will use sitemap if present); web create.roblox.com (no RSS/Atom feed found; will use sitemap if present); web docs.blender.org (no RSS/Atom feed found; will use sitemap if present); web blenderartists.org (no RSS/Atom feed found; will use sitemap if present); web www.blenderguru.com (no RSS/Atom feed found; will use sitemap if present); web github.khronos.org (no RSS/Atom feed found; will use sitemap if present); web blog.roblox.com (no RSS/Atom feed found; will use sitemap if present); reddit public JSON endpoints (HTTP 403; using Atom/RSS fallback); reddit Atom/RSS feeds (rate limited or blocked) (HTTP 429; paused Reddit for 10 minutes)

## Contradictions checked against current official sources (chunk 10, 2026-11-01)
1. **Texture limits (4096 vs 1024 vs 256 vs 2048): resolved by scope, not a real conflict.** Source: Roblox/creator-docs `content/en-us/art/modeling/texture-specifications.md` (last commit 2026-07-22) and `avatar/rigid-accessories/specifications.md`, `avatar/layered-accessories/specifications.md` (mirror read 2026-11-01). 4096x4096 = general upload ceiling ("Roblox supports up to 4096x4096 (4K)"); 1024x1024 = maximum of the PBR texture budget table and of the UV-space line; 256x256 = maximum budget for non-albedo maps of rigid accessories; 2048x2048 = Marketplace rigid and layered accessory texture cap (confirmed by the 2026-02-12 DevForum staff post). Rule of thumb for Blender work: avatar accessories 2048 max (256 non-albedo if rigid), general PBR assets 1024, only go to 4096 for non-avatar hero textures. Residual doubt: the docs page mixes scopes without labelling them; re-check before publishing a Marketplace asset.
2. **Blender version for the Roblox plugin (3.2+ vs 5.0/5.1): resolved, both are true for different releases.** Sources: github.com/Roblox/roblox-blender-plugin README (main branch, repo last pushed 2026-04-20) still says "Prerequisite: Blender version 3.2 or greater"; release v1.0.5 (2026-04-20) says it "Fixes critical issues with dependency install and blender 5.x api incompatibility. The plugin should now work with 5.0 and 5.1" and "may not be compatible with blender v4.x and under"; the creator-docs page `art/modeling/roblox-blender-plugin.md` (last commit 2025-02-28) gives no version at all. Newest issues (2026-03 to 2026-07) are login failures and 5.x install problems. Practical rule: Blender 5.0/5.1 -> use v1.0.5; Blender 4.x or older -> use the previous release v1.0.3 (2023-11-29), which is untested here. Not checked: whether v1.0.5 works on 4.x, because Blender is not installed on the research machine.
3. **YouTube transcripts partly unavailable.** The earlier HTTP 429 block cleared on 2026-11-01 (chunk 15): 41 queued new-channel videos were processed, 36 skipped for having no captions, and 32 queued Roblox Creators (official channel) videos were not processed. Retry with `process.py run --retry-skipped` if needed.
