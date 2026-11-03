---
type: research-source
id: gh-ifBars-schedule-one-blender-readme
title: "ifBars/schedule-one-blender README: Bring-your-own-game tooling to reconstruct Schedule I's Main map as an editable Blender scene. No game a"
source_type: "github"
creator: "ifBars"
url: "https://github.com/ifBars/schedule-one-blender"
published: "2026-10-08"
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0278
relevance: 1
density: low
tags: ["research-source", "github", "automation-and-creator-workflows", "claude-blender-ai", "mesh-texture-limits", "other"]
---
# gh-ifBars-schedule-one-blender-readme

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
README for a Windows tool that rebuilds Schedule I's Main map as Blender scenes from a user's own Unity game install (UnityPy extraction, Blender 5.2 scene creation). It is about Unity-to-Blender, not Roblox or Claude/blender-mcp. It only offers an incidental example of a scripted headless Blender build pipeline with an agent-instructions file (AGENTS.md).

## Claims
- c1: The pipeline is driven by a PowerShell build.ps1 with a -Doctor preflight check. It creates a local Python venv, installs pinned dependencies, then builds both scenes. Game, Blender and Mono paths can be auto-detected or given explicitly. *(doc, high; automation-and-creator-workflows)*
- c2: Scene creation runs inside the user's installed Blender (scripted, headless-style). The repo includes an AGENTS.md with agent instructions and a validation contract. It shows no blender-mcp use. *(doc, medium; claude-blender-ai)*
- c3: The default editor .blend uses 512px textures and editable 64m reference chunks with Eevee. The full-detail master keeps original texture resolution, individual objects, hierarchy and LOD alternatives. Opening the full-detail file stays expensive. *(doc, high; mesh-texture-limits)*
- c4: The tool recovers transforms, meshes, material textures, terrain layers, forest placements and lighting from Unity assets using UnityPy. Blender cannot run compiled Unity shaders, so render parity is only approximate. *(doc, high; other)*
- c5: The repo runs unit tests with unittest discover and an audit_repo.py script. CI uses synthetic tests only and never downloads game assets. *(doc, high; automation-and-creator-workflows)*

## Numbers
- n1: **Blender version**: 5.2.x (tested 5.2.2) Required Blender version
- n2: **Python version**: 3.13 Required Python with py launcher
- n3: **Editor texture size**: 512px Default optimized editor scene
- n4: **Editor chunk size**: 64m Editable reference chunks
- n5: **Disk/RAM**: 15 GiB free disk, 32 GB RAM recommended Fresh build requirements
- n6: **Tested game/Unity**: 0.4.7f9 / 2022.3.62f2 Original tested versions

## Techniques
- t1: **Preflight then build script**: Run .\build.ps1 -Doctor to create the venv, install dependencies and check paths. Then run .\build.ps1, optionally with -GamePath, -ManagedPath, -BlenderPath and -OutputPath. Each step logs its progress and supports resume.

### Code: Preflight check and build
```powershell
.\build.ps1 -Doctor
.\build.ps1
```

### Code: Run tests and repo audit
```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
.\.venv\Scripts\python.exe scripts\audit_repo.py
```

## Points to
- https://github.com/K0lb3/UnityPy
- docs/BUILD.md
- AGENTS.md
- docs/ARCHITECTURE.md
