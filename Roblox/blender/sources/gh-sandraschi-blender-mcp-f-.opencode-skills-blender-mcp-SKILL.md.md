---
type: research-source
id: gh-sandraschi-blender-mcp-f-.opencode-skills-blender-mcp-SKILL.md
title: "sandraschi/blender-mcp/.opencode/skills/blender-mcp/SKILL.md"
source_type: "github"
creator: "sandraschi"
url: "https://github.com/sandraschi/blender-mcp/blob/HEAD/.opencode/skills/blender-mcp/SKILL.md"
published: "2026-10-25"
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0747
relevance: 3
density: high
tags: ["research-source", "github", "avatar-ugc-accessories", "bpy-scripting-headless", "claude-blender-mcp", "common-mistakes-fixes", "procedural-generation", "rigging-animation", "roblox-export-settings", "roblox-mesh-limits", "texturing-baking-uv"]
---
# gh-sandraschi-blender-mcp-f-.opencode-skills-blender-mcp-SKILL.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Agent skill doc for sandraschi's blender-mcp FastMCP server: headless-by-default execution (blender --background per call) plus optional live bridge addon, portmanteau tools with operation= enums, LLM script-generation with AST/security validation, and export presets targeting VRChat/Resonite/Unity. No Roblox-specific content; useful as a Claude-to-Blender MCP architecture reference and generic export hygiene.

## Claims
- c1: Server defaults to headless: spawns `blender --background --python script.py` per call; each script_execute is a fresh Blender process with no persistent selection or viewport state. *(doc, high; claude-blender-mcp)*
- c2: For stateful multi-step work use blender_workflow(operation='execute', steps=[...]) which runs in a single execution context. *(doc, high; claude-blender-mcp)*
- c3: Live mode uses a bridge addon (blender_bridge_addon.py) polling GET /api/v1/blender/pending and posting results to /api/v1/blender/result; needed for screenshot_viewport, which returns empty in headless. *(doc, high; claude-blender-mcp)*
- c4: Portmanteau design: one tool per domain with an operation= enum rather than dozens of separate tools; docs claim a 41-tool authoritative table. All tools return {success, message, ...data}. *(doc, high; claude-blender-mcp)*
- c5: Agentic tools (agentic_blender_workflow) require a sampling-capable client such as Claude Desktop; without sampling they error, and fallback is blender_workflow(execute). *(doc, high; claude-blender-mcp)*
- c6: LLM-generated bpy passes AST parse, security score 0-100 and whitelist before execution; scripts importing os/socket/subprocess are rejected and logged. construct_object iterates up to max_iterations (default 3). *(doc, high; bpy-scripting-headless)*
- c7: Blender is not bundled; requires 3.0+ and is located via BLENDER_EXECUTABLE (legacy BLENDER_PATH). Health check: `uv run blender-mcp --check-blender`. *(doc, high; bpy-scripting-headless)*
- c8: blender_ai_generate supports text/image-to-3D via backends tripo, rodin, hunyuan using external API keys (RODIN_*, TRIPO_*); returns a mesh URL to import. *(doc, medium; procedural-generation)*
- c9: Vision-refine loop: render, vision model critiques, regenerate. *(doc, medium; procedural-generation)*
- c10: Always apply_transform before export/physics or scale bakes wrong. Blender is Z-up, meters; Unity/VRChat expect scale 1.0, legacy pipelines 0.01. *(doc, medium; roblox-export-settings)*
- c11: FBX keeps rig+NLA but needs apply_modifiers + bake_action before export; glTF/GLB keeps PBR and animations. Validate preset before export. *(doc, medium; roblox-export-settings)*
- c12: UV first (smart_project quick; unwrap+pack for final), then bake and consolidate materials to atlases ≤2048 for mobile VR. Procedural textures should drive roughness/bump rather than albedo. *(doc, medium; texturing-baking-uv)*
- c13: VRChat preset limits: 70k tris, 256 bones, 8 materials; failure order: tris, bones, materials, missing humanoid mapping. Use add_decimate and optimize_draw_calls before export. Never export raw dyntopo sculpts. *(doc, medium; roblox-mesh-limits)*
- c14: Bone naming must match humanoid_mapping preset before Unity/VRChat export; bake_action bakes constraints; bake physics/particles to keyframes or sims won't travel with the file. *(doc, medium; rigging-animation)*
- c15: transfer_weights copies body weights to clothing; blender_validation validate_avatar checks platform limits before export. No Roblox-specific cages or attachments covered. *(doc, medium; avatar-ugc-accessories)*
- c16: Destructive ops (clear_scene, delete_object, apply_modifier) are irreversible in headless; confirm names first and save milestones via manage_object_repo. *(doc, medium; common-mistakes-fixes)*

## Numbers
- n1: **VRChat preset triangle limit**: 70,000 blender_export_presets VRCHAT
- n2: **VRChat bone limit**: 256 VRCHAT preset; RESONITE 512
- n3: **VRChat material limit**: 8 VRCHAT preset
- n4: **Atlas size cap for mobile VR**: ≤2048 bake/consolidate step
- n5: **Default ports**: 10848 dashboard, 10849 API/MCP, 10850 bridge config
- n6: **Minimum Blender version**: 3.0+ install requirement

## Techniques
- t1: **Headless-first agent loop**: blender_help list_tools, blender_status, build with portmanteau tools, verify with render_preview, validate_avatar, then export_with_preset. Use prefer_session=False for deterministic batch.
- t2: **Bridge addon setup**: Start HTTP MCP, blender_session(start), install blender_bridge_addon.py in Preferences > Add-ons, enable Blender MCP Bridge, Scene properties > Start Bridge.
- t3: **Export validate-then-export**: validate_export_preset for target platform, fix tris/bones/materials, then export_with_preset; use export_for_mcp_handoff for cross-tool handoff.

## Points to
- github.com/sandraschi/blender-mcp
- Claude Desktop
- Ollama
- LM Studio
- Tripo
- Rodin
- Hunyuan
- Poly Haven
- Sketchfab
