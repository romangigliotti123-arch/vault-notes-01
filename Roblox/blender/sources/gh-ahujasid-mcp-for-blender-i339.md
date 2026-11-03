---
type: research-source
id: gh-ahujasid-mcp-for-blender-i339
title: "ahujasid/mcp-for-blender#339 Can't get blender mcp to work no matter what I do"
source_type: "github"
creator: "ahujasid"
url: "https://github.com/ahujasid/mcp-for-blender/issues/339"
published: "2026-08-29"
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0798
relevance: 3
density: medium
tags: ["research-source", "github", "claude-blender-mcp"]
---
# gh-ahujasid-mcp-for-blender-i339

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
GitHub issue on blender-mcp (ahujasid) where tool calls time out on Windows 11 with Blender 5.1+/5.2 and Claude Desktop. The addon accepts the connection but never answers. Commenters found the likely cause was a conflicting second MCP addon (BlenderLabs "MCP" 1.0.0) competing for port 9876. Others report that downgrading to Blender 5.0 or 4.5 worked. Includes diagnostic socket snippets and a Claude Desktop uvx config.

## Claims
- c1: Symptom: addon logs 'Connected to client' and 'Client handler started', then no command executes. Calls time out around 4 minutes in Claude Desktop while Blender stays responsive (Windows 11, Blender 5.1.1). *(experience, high; claude-blender-mcp)*
- c2: Reporter's hypothesis: README mentions length-prefixed JSON frames, but addon.py uses plain json.loads on the buffer, so a version mismatch between server and addon could cause the hang. Unconfirmed. *(opinion, low; claude-blender-mcp)*
- c3: laske185 reports blender-mcp works on Blender 4.5 LTS and 5.0.0, but breaks on 5.1.x and 5.2 with truncated responses (51 bytes after ~40s, 'Incomplete JSON response received'). Reinstalling the addon didn't help. Downgrading Blender did. *(experience, medium; claude-blender-mcp)*
- c4: laske185 later found the cause was a port conflict: both this blender-mcp and the official BlenderLabs MCP were running and competing for the same port. Uninstalling the BlenderLabs one fixed it. They noted this differs from the original reporter's cause. *(experience, medium; claude-blender-mcp)*
- c5: matejfric (Windows 11, Blender 5.2.0) fixed the timeout on get_addon_info by disabling a legacy add-on named 'MCP' (maintainer Blender Lab, v1.0.0) in Edit > Preferences > Add-ons. *(experience, medium; claude-blender-mcp)*
- c6: CJM2027 (Blender 5.2.1 LTS, fresh addon via uvx blender-mcp install-addon) saw every tool call take almost exactly 5:00 minutes, past Claude Desktop's ~4 minute timeout. A single PID listened on 9876. They also tried blocking the telemetry host (a supabase.co domain) via the hosts file; the outcome is cut off in the source. *(experience, medium; claude-blender-mcp)*
- c7: Ruled-out causes by the original reporter: unofficial blender-mcp.com extension, antivirus, Python 3.13 vs 3.11, uv first-run caching, localhost vs 127.0.0.1, a port conflict seen via netstat, and config JSON syntax. None resolved it. *(experience, high; claude-blender-mcp)*
- c8: Security note: an impersonating extension from an unofficial 'blender-mcp.com' site was found installed. Use only the official GitHub or PyPI addon. *(experience, medium; claude-blender-mcp)*

## Numbers
- n1: **default addon TCP port**: 9876 checked with netstat -ano | findstr 9876 for conflicts
- n2: **Claude Desktop tool timeout**: ~4 min observed client-side timeout; one report saw 5:00 server response
- n3: **truncated response size**: 51 bytes after ~40s reported on Blender 5.1.x/5.2

## Techniques
- t1: **Diagnose by raw socket fingerprint**: In Blender's Python console, open a socket to 127.0.0.1:9876, send {"type":"get_addon_info"} and recv. A timeout means the addon isn't answering. Check netstat for a single listener and disable duplicate MCP addons.
- t2: **List loaded MCP addons**: Use addon_utils.modules() filtered on 'mcp', and print bpy.context.preferences.addons.keys(), to find conflicting or legacy MCP addons.
- t3: **Pin uvx Python for Claude Desktop**: Set command uvx, args [--python, 3.11, blender-mcp], and env UV_PYTHON_PREFERENCE=only-managed and BLENDER_HOST=127.0.0.1. Install the addon with 'uvx blender-mcp install-addon' so versions match.

### Code: Maintainer's diagnostic to test whether the addon responds on port 9876
```python
import socket
s = socket.create_connection(("127.0.0.1", 9876), timeout=10)
s.sendall(b'{"type": "get_addon_info"}')
print(s.recv(8192))
```

### Code: Claude Desktop config used by the reporter
```json
{
  "mcpServers": {
    "blender": {
      "command": "uvx",
      "args": ["--python", "3.11", "blender-mcp"],
      "env": {
        "UV_PYTHON_PREFERENCE": "only-managed",
        "BLENDER_HOST": "127.0.0.1"
      }
    }
  }
}
```

## Contradictions flagged
- Original reporter suspects a length-prefix framing mismatch between addon and server (vs Later commenters traced the same symptom to a conflicting BlenderLabs/legacy MCP addon on the same port, not a framing issue)
- laske185 first blamed Blender 5.1+ socket/timer changes, since only a downgrade helped (vs laske185 later found a port conflict with the official BlenderLabs MCP addon)

## Points to
- https://github.com/ahujasid/blender-mcp
- https://github.com/ahujasid/mcp-for-blender/issues/339
- BlenderLabs official MCP addon
