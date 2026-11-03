---
type: research-source
id: gh-ahujasid-mcp-for-blender-i111
title: "ahujasid/mcp-for-blender#111 Is there a way to disable using Hyper3D and PolyHaven?"
source_type: "github"
creator: "ahujasid"
url: "https://github.com/ahujasid/mcp-for-blender/issues/111"
published: "2025-05-13"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0027
relevance: 3
density: medium
tags: ["research-source", "github", "claude-blender-mcp", "common-mistakes-fixes"]
---
# gh-ahujasid-mcp-for-blender-i111

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
GitHub issue on ahujasid/mcp-for-blender: users using Blender MCP with Goose (Blender 4.4.3, macOS M1) find the agent still calls PolyHaven and Hyper3D tools even when both are disabled in the Blender UI. Maintainers say the behaviour is non-deterministic and suggest prompting for scripting. Workaround reported: naming execute_blender_code() explicitly in the prompt. No Roblox content.

## Claims
- c1: PolyHaven and Hyper3D integrations are disabled by default in blender-mcp and only enabled via checkboxes in the Blender UI panel. *(doc, high; claude-blender-mcp)*
- c2: Even with PolyHaven and Hyper3D disabled, the agent (Goose) still tries to call their tools; the reporter says the agent then ignores the MCP server and outputs scripts to copy-paste. *(experience, high; claude-blender-mcp)*
- c3: The asset_creation_strategy() MCP prompt in src/blender_mcp/server.py starts with integration checks (get_polyhaven_status) and did not mention execute_blender_code(), which may explain why the agent doesn't run scripts. *(opinion, medium; claude-blender-mcp)*
- c4: Maintainer ahujasid says behaviour is non-deterministic when both integrations are disabled and suggests asking the agent to write a script instead. *(opinion, medium; claude-blender-mcp)*
- c5: Prompt-only exclusion ('without using Hyper3D or PolyHaven') was unreliable; results varied across runs and the model often produced script text instead of executing it. *(experience, high; common-mistakes-fixes)*
- c6: Tested environment in the issue: MacBook Pro M1, Blender 4.4.3, Goose 1.0.22; the Goose tutorial predates the Hyper3D and PolyHaven additions. *(experience, medium; claude-blender-mcp)*

## Numbers
- n1: **Tested versions**: Blender 4.4.3, Goose 1.0.22, MacBook Pro M1 Versions reported by issue author

## Techniques
- t1: **Explicit tool naming in prompt**: Tell the agent to use only execute_blender_code() from the MCP tool set and to exclude Hyper3D/PolyHaven by name. Reported as a fix to try; success varied.

### Code: Prompt pattern suggested in thread to force scripting path via MCP tool
```text
Without using Hyper3D or Polyhaven, use only execute_blender_code() in the mcp tool set, build a scene ...
```

## Quotes (brief, for attribution)
> It should usually go back to scripting if both are disabled, is that not the case?  (ahujasid)
> Try asking it to write a script instead  (ahujasid)

## Contradictions flagged
- Goose tutorial as described by reporter implies PolyHaven/Hyper3D-style asset paths; issue shows they are off by default and the tutorial predates them. (vs Goose tutorial (as described by the reporter))

## Points to
- https://block.github.io/goose/docs/tutorials/blender-mcp/
- https://github.com/ahujasid/mcp-for-blender/blob/main/src/blender_mcp/server.py
