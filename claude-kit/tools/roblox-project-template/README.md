# roblox-project-template

Starter layout for a Rojo project plus the static-check toolchain. No secrets, no personal paths.

- `default.project.json`, `src/server`, `src/client`, `src/shared`: Rojo layout (server -> ServerScriptService.Server, client -> StarterPlayerScripts.Client, shared -> ReplicatedStorage.Shared).
- `rokit.toml`: pinned tools (rojo, selene, stylua, luau-lsp, lune). Install Rokit from https://github.com/rojo-rbx/rokit/releases (or `winget install` / `brew install rokit`), then run `rokit install` in this folder or the project folder.
- `luau-check.sh <file-or-dir>`: stylua --check, selene (roblox.yml std), luau-lsp analyze (globalTypes.d.luau). Missing tools are reported as SKIPPED. Run it from anywhere: `bash luau-check.sh /abs/path/to/project/src`.
- `.mcp.windows.json` / `.mcp.macos.json`: optional. Studio's built-in MCP server (https://create.roblox.com/docs/studio/mcp). Copy the one for your OS to `.mcp.json` in the game project only if Studio is installed; it is not needed to build files.
- `roblox.yml` and `globalTypes.d.luau` are generated (selene Roblox std and luau-lsp Roblox definitions). Regenerate with `selene generate-roblox-std` and the luau-lsp release asset when Roblox updates its API.

Scaffold a new project: copy `default.project.json rokit.toml selene.toml stylua.toml .gitignore src/` into an empty folder; do not copy the two big generated files (the check script uses the ones here).
