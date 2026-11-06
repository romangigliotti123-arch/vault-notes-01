<!-- cold: rbx-studio/builtin-mcp.md | read when: connecting Claude Code to the built-in Studio MCP server, choosing between it and the older Rust server, or deciding which MCP tool to use for reading and editing scripts. -->

# Built-in Roblox Studio MCP first, older Rust server as fallback

STATUS: wording checked against the Roblox docs (create.roblox.com/docs/studio/mcp) and the Roblox/studio-rust-mcp-server README on 2026-11-05. NOT tested live in Studio by this vault: no Studio was run while writing this. Treat the first real connection as the test and report what you see.

## 1. Built-in server (use this first)
- Enable: in Studio open Assistant, then `...` > Manage MCP Servers, then turn on Enable Studio as MCP server. Restart Studio and the AI client.
- Windows client entry (`mcpServers.Roblox_Studio`): `command` = `cmd.exe`, `args` = `["/c", "%LOCALAPPDATA%\\Roblox\\mcp.bat"]`. CLI form: `cmd.exe /c %LOCALAPPDATA%\Roblox\mcp.bat`. Claude Code: `claude mcp add --scope user Roblox_Studio -- cmd.exe /c %LOCALAPPDATA%\Roblox\mcp.bat` (what `studio-setup.ps1` runs).
- macOS: `command` = `/Applications/RobloxStudio.app/Contents/MacOS/StudioMCP`.
- Every tool call takes `studio_id`; `list_roblox_studios` returns the ids.
- Tools (docs): scripts `script_read`, `multi_edit`, `script_search`, `script_grep`; data model `search_game_tree`, `inspect_instance`, `subagent` (explore or playtest); `execute_luau` (Edit, Client or Server); playtest `get_studio_state`, `start_stop_play`, `get_console_output`, `screen_capture`; input `character_navigation`, `user_keyboard_input`, `user_mouse_input`; assets `search_asset`, `insert_asset`, `generate_mesh`, `generate_material`, `generate_procedural_model`, `wait_job_finished`, `upload_image`, `store_image`; docs `http_get`, `skill`; session `list_roblox_studios`.

## 2. Use the tools cheaply
- Find before you read: `script_grep` for a pattern across all scripts, `script_search` for a script by name, `search_game_tree` for the instance hierarchy. Open a whole script with `script_read` only when the lines around a hit are not enough (it takes a line range).
- Change before you rewrite: `multi_edit` applies several edits to one script in one call; never re-send a whole script to change a few lines. If a Rojo session is connected the project files stay the source and Rojo syncs (see the Mode 1 loop in the skill).
- `screen_capture` and `get_console_output` are the evidence for looks and errors.

## 3. Older server (fallback only)
`Roblox/studio-rust-mcp-server` (MIT, last pushed 2026-04-03) says it is no longer actively developed and recommends the built-in server. Use it only when the installed Studio has no Manage MCP Servers setting. Its config: `command` = path to `rbx-studio-mcp.exe`, `args` = `["--stdio"]`; macOS: `claude mcp add --transport stdio Roblox_Studio -- '/Applications/RobloxStudioMCP.app/Contents/MacOS/rbx-studio-mcp' --stdio`. Its tools are fewer: `run_code`, `insert_model`, `get_console_output`, `start_stop_play`, `run_script_in_play_mode`, `get_studio_mode`. The vault never downloads or installs it for the user: tell the user where it lives and let them decide.

## 4. Safety (from the docs)
MCP clients can read and modify the open places; connect only trusted clients. Keep Studio version history or a copy of the place. Never publish or save over the user's place through these tools.
