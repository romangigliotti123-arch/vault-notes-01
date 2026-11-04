<!-- cold: rbx-studio/troubleshooting.md | read when: read only when Studio MCP tools are missing, `rokit` says not found in manifest, or the Rojo plugin shows no project. -->

## From skills/rbx-studio/SKILL.md :: Troubleshooting

`mcp__Roblox_Studio__*` tools missing: Studio closed, MCP toggle off, or Claude Code not restarted; `claude mcp get Roblox_Studio` shows the registration; `%LOCALAPPDATA%\Roblox\mcp.bat` must exist (written by Studio when the toggle is on). JSON config typos prevent loading. `rokit` commands "not found in manifest": run them inside a folder that has `rokit.toml` (`claude-kit/systems` or the project). Rojo plugin shows no project: `rojo serve` must be running in the project folder with the default port. Windows without winget: install Rokit from github.com/rojo-rbx/rokit/releases.
