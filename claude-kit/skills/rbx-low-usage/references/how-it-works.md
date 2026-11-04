# rbx-low-usage: how it works

## Pieces (all inside the skill folder, installed to `~/.claude/claude-kit/vault-mode/.claude/skills/rbx-low-usage/`)
- `SKILL.md`: the slash command. Runs `scripts/lum run "<arg>"` through shell injection before Claude reads it, so the switch happens deterministically, then Claude replies from the result line.
- `scripts/lum`: tiny `sh` launcher. Finds the first working Python 3 (`python3`, `python`, `py`; skips the Windows Store stub) and runs `lum.py`; if none, runs `lum.ps1`. For `hook` it exits at once when the marker is absent (one file test).
- `scripts/lum.py`: the logic (on/off/status, hook output, settings.json merge/remove). Standard library only, no network.
- `scripts/lum.ps1`: PowerShell fallback for hook/on/off/status (install/remove of hooks needs Python). Its rules text must stay identical to `RULES` in `lum.py` (checked 2026-11-01: identical).
- Marker: `<config dir>/state/rbx-low-usage.on` (config dir = `$CLAUDE_CONFIG_DIR`, else `~/.claude`). Present = on. Global per computer and user, not per project or per session.

## Commands
- `/rbx-low-usage` or `/rbx-low-usage on`: create the marker; the reply starts with `low usage mode enabled.`
- `/rbx-low-usage off`: delete the marker; reply `low usage mode disabled.`; hooks go silent.
- `/rbx-low-usage status`: mode and whether the hooks are installed.
- `/rbx-low-usage install-hooks` / `uninstall-hooks`: merge or remove the two hook entries (also offered automatically, with a yes/no, when the mode is turned on and the hooks are missing).

## Hooks (merged into `~/.claude/settings.json` by `lum.py install-hooks`)

`lum.py install-hooks` merges a `UserPromptSubmit` hook (every prompt) and a `SessionStart` hook (matcher `startup|resume|compact`), each running `scripts/lum hook <event>`; the merge keeps every other key and hook, backs up settings.json first, does nothing if present, refuses an invalid settings.json, and `uninstall-hooks` removes exactly our entries. Installer flags are opt-in (`install.ps1 -WithHooks | -RemoveHooks`, `install.sh --with-hooks | --remove-hooks`); hooks load at session start (or via `/hooks`). [cold:rbx-low-usage/hooks-detail.md] read only to debug or audit the settings.json hook entries.

## Limits
- It is an instruction, not enforcement: Claude can still miss the prefix on a very long or odd turn. The hook repeats the rules every message to make that rare.
- Windows needs Git Bash (Claude Code on Windows has it) for the `sh` hook command.
- `claude -p` headless needs the hooks too; set `CLAUDE_CONFIG_DIR` the same way.
- Turning the mode off mid-session leaves older reminders in the transcript; the skill's off reply tells Claude to ignore them (tested: replies lose the prefix immediately).

## Test record (2026-11-01, temp config, haiku, headless)

Tested 2026-11-01: on, three follow-up prompts, `/compact`, fresh session with hooks only, off, PowerShell fallback and hook merge/remove round-trip all behaved as specified. [cold:rbx-low-usage/test-record.md] read only to see what was tested when the mode was built.