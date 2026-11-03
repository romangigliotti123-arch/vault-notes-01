---
type: research-source
id: gh-ahujasid-mcp-for-blender-readme
title: "ahujasid/mcp-for-blender README: Community plugin to control Blender 3D with any LLM of your choice. Not affiliated with the official Blende"
source_type: "github"
creator: "ahujasid"
url: "https://github.com/ahujasid/mcp-for-blender"
published: "2026-10-29"
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.1140
relevance: 3
density: high
tags: ["research-source", "github", "claude-blender-mcp", "creator-workflows", "open-cloud-automation", "procedural-generation"]
---
# gh-ahujasid-mcp-for-blender-readme

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
README for mcp-for-blender (formerly blender-mcp): a socket-based addon plus MCP server letting Claude (Desktop/Code), Codex, Cursor etc. drive a live Blender via Python execution, viewport inspection and asset/AI-model generation. Covers install, config, env vars, safe mode, security warnings, and Poly Pizza/Poly Haven/Meshy/Tripo/Hunyuan integrations. No Roblox-specific content.

## Claims
- c1: Architecture: a Blender addon (addon.py) runs a socket server inside Blender; a Python MCP server (src/blender_mcp/server.py) connects to it. Protocol is JSON over TCP with type/params commands and status/result|message responses. *(doc, high; claude-blender-mcp)*
- c2: Package renamed from blender-mcp to mcp-for-blender on PyPI; `uvx blender-mcp` still works with no config change. *(doc, high; claude-blender-mcp)*
- c3: Requirements: Blender 3.0+, Python 3.10+, uv (use official installer, not pip install uv). Pin Python 3.11 with UV_PYTHON_PREFERENCE=only-managed to avoid conda/pyenv conflicts. *(doc, high; claude-blender-mcp)*
- c4: Nine tools: execute_blender_code, look, get_scene_info, generate_3d, search_assets, import_asset, get_addon_status, disable_telemetry, record_trajectory_feedback. The AI writes bpy itself for modelling, materials, animation, rigging, retopology. *(doc, high; claude-blender-mcp)*
- c5: The `look` tool gives visual feedback (viewport, camera, multi-angle sheet, animation frame strip; solid/material/rendered/wireframe/xray) so the AI can verify its own work. *(doc, high; claude-blender-mcp)*
- c6: Security: addon socket has no authentication or encryption; anyone reaching the port can run Python in Blender. Keep on localhost; use SSH tunnel for remote. execute_blender_code runs arbitrary code; always save work first. *(doc, high; claude-blender-mcp)*
- c7: BLENDER_MCP_SAFE_MODE=1 validates scripts before running and blocks direct file I/O, subprocesses, network access and persistent code installs; modeling, materials, rendering, saving, import/export still work. Blocked scripts return the reason to the AI to retry. *(doc, high; claude-blender-mcp)*
- c8: GUI-launched clients don't inherit terminal PATH, causing `spawn uvx ENOENT`. Fix: use the full uvx path as command, or on Windows wrap with cmd /c uvx; fully quit and relaunch client (Windows: from system tray). *(doc, high; claude-blender-mcp)*
- c9: Run only one MCP server instance (Cursor or Claude Desktop, not both). Multiple Blender instances need separate ports via --port and matching port in the addon panel. *(doc, high; claude-blender-mcp)*
- c10: Troubleshooting: timeouts fixed by simplifying/breaking requests into smaller steps; first command sometimes fails; restart both Claude and the Blender server. Poly Haven downloads block Blender's main thread; ask for 1k/2k since size grows ~4x per resolution step. *(doc, high; claude-blender-mcp)*
- c11: generate_3d supports Tripo, Hunyuan3D, Hyper3D Rodin and Meshy. Meshy models are sized to real-world height with origin at bottom; requesting an A-pose or T-pose gives a rig-ready character (own key requires paid Meshy plan). *(doc, medium; procedural-generation)*
- c12: Hunyuan3D official API: mainland accounts use AI3D (version 2025-05-13, ap-guangzhou); international accounts use `hunyuan` (2023-09-01, ap-singapore, PBR). Wrong region gives AuthFailure.SignatureFailure or ResourceUnavailable. *(doc, high; procedural-generation)*
- c13: Poly Pizza (~10,600 free low-poly models, single .glb each, triangle counts in search results) is described as best source for stylised game assets and lighter than Sketchfab. import_asset supports target_size (e.g. 1.0 m). *(doc, medium; creator-workflows)*
- c14: About 69% of Poly Pizza is CC-BY requiring credit; the addon writes polypizza_attribution, polypizza_id, polypizza_licence as custom properties on imported roots. Filter licence=CC0 to avoid attribution. Relevant for marketplace/UGC licensing. *(doc, high; creator-workflows)*
- c15: Poly Haven (~2,400 CC0 assets) models import from the authored .blend, since glTF/FBX/USD versions lose material detail; textures build a Principled material; HDRIs are packed into the file. *(doc, high; creator-workflows)*
- c16: For headless/CI use, API keys can be injected via env vars such as BLENDERMCP_MESHY_API_KEY, BLENDERMCP_TRIPO_API_KEY, BLENDERMCP_HYPER3D_API_KEY, BLENDERMCP_SKETCHFAB_API_KEY, BLENDERMCP_POLYPIZZA_API_KEY, BLENDERMCP_HUNYUAN3D_*. *(doc, high; open-cloud-automation)*
- c17: Telemetry: minimal anonymous usage is collected by default; prompts, code and screenshots only on opt-in. Disable entirely with DISABLE_TELEMETRY=true. *(doc, high; claude-blender-mcp)*

## Numbers
- n1: **default socket port**: 9876 BLENDER_PORT default; host localhost
- n2: **minimum Blender version**: 3.0 Prerequisite; Python 3.10+
- n3: **Poly Pizza catalogue size**: ~10,600 models free low-poly; ~69% CC-BY
- n4: **Poly Haven catalogue size**: ~2,400 assets all CC0
- n5: **update command minimum version**: 2.1.7 older releases lack the `update` command

## Techniques
- t1: **One-command setup**: Run `curl -LsSf https://www.mcp-for-blender.com/install.sh | sh` (or PowerShell irm install.ps1 | iex), or `uvx mcp-for-blender setup`. It detects clients, adds a blender entry with .bak backups, installs and enables the addon. Restart client.
- t2: **Manual Claude Code setup**: Install uv; run `claude mcp add blender uvx mcp-for-blender`; run `uvx mcp-for-blender install-addon`; enable Interface: MCP for Blender in Preferences > Add-ons; press N, open MCP tab, Start MCP Server.
- t3: **Upgrade**: Run `uvx mcp-for-blender@latest update` (--dry-run to preview), restart MCP client, then restart Blender or toggle the addon and click Start MCP Server.
- t4: **Docker server**: Build image; client command `docker run -i --rm mcp-for-blender`. On Linux add --network=host and -e BLENDER_HOST=localhost. Blender stays on host. Add -e BLENDER_MCP_SAFE_MODE=1 for safe mode.
- t5: **Low-poly asset import at target size**: search_assets(source="polypizza", query="chair", licence="CC0") returns licence and triangle count; then import_asset(source="polypizza", id=..., target_size=1.0).

### Code: Claude Desktop MCP config with pinned Python
```json
{
    "mcpServers": {
        "blender": {
            "command": "uvx",
            "args": ["--python", "3.11", "mcp-for-blender"],
            "env": { "UV_PYTHON_PREFERENCE": "only-managed" }
        }
    }
}
```

### Code: Register server with Claude Code
```bash
claude mcp add blender uvx mcp-for-blender
```

### Code: Windows workaround when uvx not found
```json
{
    "mcpServers": {
        "blender": {
            "command": "cmd",
            "args": ["/c", "uvx", "mcp-for-blender"]
        }
    }
}
```

## Quotes (brief, for attribution)
> the addon's socket server has no authentication or encryption, so anyone who can reach that port can run Python inside Blender.  (ahujasid)
> ALWAYS save your work before using it.  (ahujasid)

## Points to
- https://github.com/ahujasid/mcp-for-blender
- https://polyhaven.com/
- https://poly.pizza/
- https://www.meshy.ai/
- https://www.tripo3d.ai/
- https://docs.astral.sh/uv/
- https://www.mcp-for-blender.com/
