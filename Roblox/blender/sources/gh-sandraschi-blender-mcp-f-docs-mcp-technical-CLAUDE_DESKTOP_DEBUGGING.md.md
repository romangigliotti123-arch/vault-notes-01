---
type: research-source
id: gh-sandraschi-blender-mcp-f-docs-mcp-technical-CLAUDE_DESKTOP_DEBUGGING.md
title: "sandraschi/blender-mcp/docs/mcp-technical/CLAUDE_DESKTOP_DEBUGGING.md"
source_type: "github"
creator: "sandraschi"
url: "https://github.com/sandraschi/blender-mcp/blob/HEAD/docs/mcp-technical/CLAUDE_DESKTOP_DEBUGGING.md"
published: "2026-10-25"
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0446
relevance: 1
density: medium
tags: ["research-source", "github", "claude-blender-mcp"]
---
# gh-sandraschi-blender-mcp-f-docs-mcp-technical-CLAUDE_DESKTOP_DEBUGGING.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Generic guide to debugging Claude Desktop MCP servers that start then get killed (from a nest-protect MCP). Causes: function-level imports, module-level config validation, missing dependencies, and async/sync misuse. Fixes: module-level imports, deferred config, stderr logging, startup validation, and a minimal FastMCP repro server. Nothing Blender- or Roblox-specific; it is only indirectly useful for debugging a blender-mcp server.

## Claims
- c1: Claude Desktop does not randomly kill MCP servers. The --kill/transport-closed log pattern follows a server crash or hang, typically during tools/list discovery, about 5-10 seconds after start. *(experience, medium; claude-blender-mcp)*
- c2: Imports inside tool functions, such as `from x import y` in a tool body, can crash the server with an unhandled ImportError. Move imports to module level, or check them at startup. *(experience, medium; claude-blender-mcp)*
- c3: A module-level config object with required Pydantic fields raises ValidationError. Give fields defaults or create the config lazily with a get_config() function. *(experience, medium; claude-blender-mcp)*
- c4: Wrapping blocking app.run() in `async def main` plus asyncio.run causes event-loop conflicts. Call app.run() directly from a synchronous main(). *(experience, medium; claude-blender-mcp)*
- c5: Log to sys.stderr (and optionally a file) so the output shows in Claude Desktop MCP logs. A bare 'Server disconnected' message means a hidden crash that needs better logging. *(experience, medium; claude-blender-mcp)*
- c6: Isolation plan: run a minimal FastMCP server with one tool in Claude Desktop. If it works, add tools one at a time until the server breaks. If it fails, the environment is the problem. *(experience, medium; claude-blender-mcp)*

## Numbers
- n1: **Claude Desktop unresponsive-server detection window**: 5-10 s Time before Claude Desktop sends --kill to a crashed server

## Techniques
- t1: **Minimal reproduction server**: Create a FastMCP app with a hello tool and a test_import tool that tries your problem import inside try/except. Run it from Claude Desktop. Then add real tools one at a time until it breaks.
- t2: **Startup validation**: Before app.run(), run validate_environment(). It checks imports, instantiates the config, and tests external connections. Any failure exits at startup with a logged error.
- t3: **Diagnostic MCP tools**: Expose test_imports and test_config tools that try __import__ on each module and return the results or a traceback to Claude.

### Code: Log to stderr and a file so output reaches Claude Desktop logs
```python
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(sys.stderr),
        logging.FileHandler("debug.log"),
    ],
)
```

### Code: Deferred config instantiation
```python
config = None

def get_config():
    global config
    if config is None:
        try:
            config = MyConfig()
        except ValidationError as e:
            config = MyConfig.default()
    return config
```

## Quotes (brief, for attribution)
> Claude Desktop NEVER randomly kills servers.  (sandraschi)

## Points to
- sandraschi/blender-mcp
- FastMCP
- Claude Desktop MCP logs
