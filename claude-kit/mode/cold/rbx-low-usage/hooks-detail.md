<!-- cold: rbx-low-usage/hooks-detail.md | read when: read only to debug or audit the settings.json hook entries. -->

## From skills/rbx-low-usage/references/how-it-works.md :: Hooks (merged into `~/.claude/settings.json` by `lum.py install-hooks`)

- `UserPromptSubmit` -> `sh "${CLAUDE_CONFIG_DIR:-$HOME/.claude}/skills/rbx-low-usage/scripts/lum" hook UserPromptSubmit` (every prompt).
- `SessionStart`, matcher `startup|resume|compact` -> same command with `SessionStart`.
- The merge is JSON-aware: it keeps every other key and hook, writes a backup `settings.json.lum-bak-<timestamp>` first, does nothing if our entries exist, refuses to touch an invalid settings.json, and `uninstall-hooks` removes exactly our entries (tested: the file returns to its pre-install content).
- Installer flags (opt-in, never automatic on `/rbx-update`): `install.ps1 -WithHooks | -RemoveHooks`, `install.sh --with-hooks | --remove-hooks`.
- Hooks load when a session starts (or via `/hooks`); a session that began before install gets the rules from the skill text until restarted.
