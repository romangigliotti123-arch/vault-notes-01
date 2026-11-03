---
type: research-source
id: web-c6e15e7b0e
title: "Blender manual: advanced/scripting/security"
source_type: "web"
creator: "docs.blender.org"
url: "https://projects.blender.org/blender/blender-manual/raw/branch/main/manual/advanced/scripting/security.rst"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0010
relevance: 2
density: medium
tags: ["research-source", "web", "bpy-scripting-headless", "claude-blender-mcp"]
---
# web-c6e15e7b0e

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Official Blender manual page on Python script security. Explains that blend-files can auto-run scripts (registered text-blocks, drivers), that auto-execution is off by default, and how to control it via the File Browser Trusted Source toggle, the Preferences Auto Run Python Scripts setting, and the --enable-autoexec / --disable-autoexec command-line flags for headless renders. Nothing on Roblox, MCP, or asset export.

## Claims
- c1: Blender auto-execution of blend-file scripts is disabled by default; some files need it to function, and a dialog offers Allow Execution or Ignore. *(doc, high; bpy-scripting-headless)*
- c2: Auto-run occurs via registered text-blocks (load on start) and animation drivers; Freestyle rendering and running a script in the Text editor run scripts only with user interaction. *(doc, high; bpy-scripting-headless)*
- c3: Background batch renders can override Preferences with --enable-autoexec (-y) or --disable-autoexec (-Y); example: blender --background --enable-autoexec my_movie.blend --render-anim. *(doc, high; bpy-scripting-headless)*
- c4: Running Claude-written or MCP-sent bpy code in a trusted session is a security consideration: Python does not restrict what a script can do, so only run scripts from trusted sources. *(doc, medium; claude-blender-mcp)*

## Techniques
- t1: **Headless autoexec override**: Run blender --background with --enable-autoexec to allow drivers/registered scripts during batch render; use --disable-autoexec (-Y) to block them. Command-line flags override Preferences.

### Code: Headless render allowing drivers and scripts to auto-run
```sh
blender --background --enable-autoexec my_movie.blend --render-anim
```

## Points to
- https://projects.blender.org/blender/blender-manual/raw/branch/main/manual/advanced/scripting/security.rst
