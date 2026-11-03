---
type: research-source
id: gh-sandraschi-blender-mcp-f-docs-blender-GUI_MODE.md
title: "sandraschi/blender-mcp/docs/blender/GUI_MODE.md"
source_type: "github"
creator: "sandraschi"
url: "https://github.com/sandraschi/blender-mcp/blob/HEAD/docs/blender/GUI_MODE.md"
published: "2026-10-25"
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0275
relevance: 2
density: low
tags: ["research-source", "github", "claude-blender-ai"]
---
# gh-sandraschi-blender-mcp-f-docs-blender-GUI_MODE.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Doc for sandraschi/blender-mcp describing headless vs GUI execution of Blender scripts via a Python BlenderExecutor, with bpy example and env var toggle. Nothing Roblox-specific (no export/import, limits, rigs). Useful only as a reference for running bpy scripts via CLI in background or GUI mode.

## Claims
- c1: This blender-mcp server runs Blender headless by default and can open the full GUI for visual debugging and previewing. *(doc, high; claude-blender-ai)*
- c2: Headless command is `blender.exe --background --factory-startup --python script.py`; GUI mode drops `--background`. Headless suits CI/CD, batch processing, Docker and servers. *(doc, high; claude-blender-ai)*
- c3: GUI mode is slower, needs a display, uses more memory, and is unsuitable for servers. Headless is faster but harder to debug visually. *(doc, medium; claude-blender-ai)*
- c4: The executor is a singleton; switching modes requires resetting `blender_executor._blender_executor_instance = None` before calling get_blender_executor again. *(doc, high; claude-blender-ai)*
- c5: Doc recommends headless for production, GUI for development, testing scripts in both modes, and longer timeouts in GUI mode. *(doc, medium; claude-blender-ai)*
- c6: The doc lists no Roblox, FBX or glTF export steps, so it says nothing about the Blender-to-Roblox pipeline. *(doc, high; claude-blender-ai)*

## Techniques
- t1: **Toggle GUI vs headless executor**: Call get_blender_executor(headless=False) or BlenderExecutor(headless=False) for GUI. Alternatively set env var BLENDER_GUI_MODE=true before getting the executor. Then await executor.execute_script(script, script_name=...).
- t2: **Batch bpy script via CLI**: Run `blender --background --factory-startup --python script.py` so a clean scene state is used with no UI, for automation or CI.

### Code: Get a GUI-mode executor and run a bpy script string
```python
from blender_mcp.utils.blender_executor import get_blender_executor

executor = get_blender_executor(headless=False)
await executor.execute_script(script, script_name="animated_cube")
```

### Code: Reset singleton to switch execution mode
```python
from blender_mcp.utils import blender_executor

blender_executor._blender_executor_instance = None
executor = get_blender_executor(headless=False)
```

## Points to
- sandraschi/blender-mcp README
- TOOL_REFERENCE.md
- examples/gui_mode_example.py
- examples/basic_client.py
