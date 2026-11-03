---
type: research-source
id: gh-ifBars-schedule-one-blender-f-docs-BUILD.md
title: "ifBars/schedule-one-blender/docs/BUILD.md"
source_type: "github"
creator: "ifBars"
url: "https://github.com/ifBars/schedule-one-blender/blob/HEAD/docs/BUILD.md"
published: "2026-10-08"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0013
relevance: 1
density: medium
tags: ["research-source", "github", "automation-and-creator-workflows", "claude-blender-ai", "mesh-texture-limits", "other"]
---
# gh-ifBars-schedule-one-blender-f-docs-BUILD.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Build guide for ifBars/schedule-one-blender, a tool that extracts the Schedule I game map into Blender. It covers Python 3.13 setup, a map.py doctor/build flow, three resumable phases, and common failures. It is not about Roblox, blender-mcp, or the Roblox asset pipeline; the only overlap is generic Blender scripting.

## Claims
- c1: Source targets Schedule I game map extraction into Blender, not Roblox Studio; off-topic for the Roblox pipeline. *(doc, high; other)*
- c2: Blender-side builds require Blender 5.2 series; earlier compositor APIs differ and future versions need validation first. *(doc, high; claude-blender-ai)*
- c3: Blender Python exceptions are surfaced with --python-exit-code 1; the runner checks nonzero exit codes per helper. *(doc, medium; claude-blender-ai)*
- c4: Build runs headless; no GUI session is required. Resume works via -Resume and completed phases are skipped. *(doc, high; automation-and-creator-workflows)*
- c5: A successful doctor run does not mean the map build completed; doctor only checks discovery, Main scene, Blender version and Mono schema folder. *(doc, high; other)*
- c6: A changed game install, script, schema DLL or completed output requires a new output directory rather than resuming. *(doc, high; automation-and-creator-workflows)*
- c7: Black terrain fix: control maps must keep RGBA channels independent and use Channel Packed alpha mode. *(doc, medium; mesh-texture-limits)*
- c8: Out-of-disk fix guidance: a generated .blend1 backup can consume space; never delete source game files to recover space. *(doc, medium; other)*

## Numbers
- n1: **Python version**: 3.13 
- n2: **Supported Blender version**: 5.2 series 
- n3: **Build phases**: 3 (extract, scene, editor) 

## Techniques
- t1: **Phased resumable build**: Run build with -Through extract to checkpoint, then -Resume into a fresh output dir. Completed phases are checked by SHA-256 and skipped; interrupted phase restarts from its clean predecessor.
- t2: **Headless build via venv**: Create py -3.13 venv, pip install requirements.txt, run map.py doctor then map.py build with --game path; no GUI needed.

### Code: Manual setup and build steps
```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe map.py doctor --game 'D:\Games\Schedule I'
.\.venv\Scripts\python.exe map.py build --game 'D:\Games\Schedule I'
```

## Quotes (brief, for attribution)
> A successful doctor run is not a completed map build.  (ifBars)

## Points to
- https://github.com/ifBars/schedule-one-blender
