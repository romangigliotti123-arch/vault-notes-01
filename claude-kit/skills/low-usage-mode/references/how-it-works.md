# low-usage-mode: how it works

## Pieces (all inside the skill folder, installed to `~/.claude/claude-kit/vault-mode/.claude/skills/low-usage-mode/`)
- `SKILL.md`: the slash command. Runs `scripts/lum run "<arg>"` through shell injection before Claude reads it, so the switch happens deterministically, then Claude replies from the result line.
- `scripts/lum`: tiny `sh` launcher. Finds the first working Python 3 (`python3`, `python`, `py`; skips the Windows Store stub) and runs `lum.py`; if none, runs `lum.ps1`. For `hook` it exits at once when the marker is absent (one file test).
- `scripts/lum.py`: the logic (on/off/status, hook output, settings.json merge/remove). Standard library only, no network.
- `scripts/lum.ps1`: PowerShell fallback for hook/on/off/status (install/remove of hooks needs Python). Its rules text must stay identical to `RULES` in `lum.py` (checked 2026-11-01: identical).
- Marker: `<config dir>/state/low-usage-mode.on` (config dir = `$CLAUDE_CONFIG_DIR`, else `~/.claude`). Present = on. Global per computer and user, not per project or per session.

## Commands
- `/low-usage-mode` or `/low-usage-mode on`: create the marker; the reply starts with `low usage mode enabled.`
- `/low-usage-mode off`: delete the marker; reply `low usage mode disabled.`; hooks go silent.
- `/low-usage-mode status`: mode and whether the hooks are installed.
- `/low-usage-mode install-hooks` / `uninstall-hooks`: merge or remove the two hook entries (also offered automatically, with a yes/no, when the mode is turned on and the hooks are missing).

## Hooks (merged into `~/.claude/settings.json` by `lum.py install-hooks`)
- `UserPromptSubmit` -> `sh "${CLAUDE_CONFIG_DIR:-$HOME/.claude}/skills/low-usage-mode/scripts/lum" hook UserPromptSubmit` (every prompt).
- `SessionStart`, matcher `startup|resume|compact` -> same command with `SessionStart`.
- The merge is JSON-aware: it keeps every other key and hook, writes a backup `settings.json.lum-bak-<timestamp>` first, does nothing if our entries exist, refuses to touch an invalid settings.json, and `uninstall-hooks` removes exactly our entries (tested: the file returns to its pre-install content).
- Installer flags (opt-in, never automatic on `/vault-update`): `install.ps1 -WithHooks | -RemoveHooks`, `install.sh --with-hooks | --remove-hooks`.
- Hooks load when a session starts (or via `/hooks`); a session that began before install gets the rules from the skill text until restarted.

## Limits
- It is an instruction, not enforcement: Claude can still miss the prefix on a very long or odd turn. The hook repeats the rules every message to make that rare.
- Windows needs Git Bash (Claude Code on Windows has it) for the `sh` hook command.
- `claude -p` headless needs the hooks too; set `CLAUDE_CONFIG_DIR` the same way.
- Turning the mode off mid-session leaves older reminders in the transcript; the skill's off reply tells Claude to ignore them (tested: replies lose the prefix immediately).

## Test record (2026-11-01, temp config, haiku, headless)
On via skill; 3 further prompts in the same session, each reply began `low usage mode enabled.`; `/compact` then another prompt, still prefixed (transcript: compact_boundary, then SessionStart and UserPromptSubmit attachments); a fresh session without the skill, prefixed by hooks alone; off, then two prompts without the prefix; PowerShell fallback output identical to Python's; hook merge/remove round-trip restores the original settings.json.
