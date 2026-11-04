<!-- cold: rbx-studio/setup-details.md | read when: read only when running or debugging the studio-setup scripts (what each of the five steps installs, pinned versions). -->

## From skills/rbx-studio/SKILL.md :: What it does, in order: (1) Rokit toolchain manager via wing

What it does, in order: (1) Rokit toolchain manager via winget `Rojo.Rokit` / `brew install rokit`; (2) `rokit install` in `claude-kit/systems` (pins rojo 7.7.1, selene 0.29.0, stylua 2.3.1, luau-lsp 1.70.1, lune 0.10.4 from their official GitHub releases; Wally with the flag); (3) `rojo plugin install` (Studio plugin); (4) `claude mcp add --scope user Roblox_Studio -- cmd.exe /c %LOCALAPPDATA%\Roblox\mcp.bat` (macOS: `/Applications/RobloxStudio.app/Contents/MacOS/StudioMCP`); (5) a verification table. Idempotent; `-DryRun` changes nothing; ends with exit 2 and the list of what is missing if something is.
