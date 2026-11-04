<!-- cold: rbx-update/kit-refresh-details.md | read when: read only when the update output mentions queued learnings, the AI Library Vault or a kit migration and you need the exact behaviour. -->

## From skills/rbx-update/SKILL.md :: 3b. The kit refresh also sends notes queued by `/learn-rbxde

3b. The kit refresh also sends notes queued by `/rbx-learn` to the public vault-learnings inbox (`learn.py flush --quiet`): silent when nothing is queued, offline, or without write access (notes stay queued; `learn.py pr` is the explicit opt-in way to contribute from a fork). Skip with env `CLAUDE_LEARN_SKIP=1`.

## From skills/rbx-update/SKILL.md :: 4b. The kit refresh also (a) refreshes folders that have Rob

4b. The kit refresh also (a) refreshes folders that have Roblox dev mode loaded (`/rbx-load`), and (b) moves an OLDER always-on kit install (vault skills/agents directly in `~/.claude/skills` and `/agents`) into the on-demand store with a backup, printing `vault-mode: moved N vault skills ...`. Your own skills, agents and CLAUDE.md are not touched.
4c. Command rename (one time): output containing `NOTICE FOR THE USER ... commands renamed` = copy that notice into your report word for word (old name -> new name). The installer removed the OLD generic command names of this vault and installed the vault-suffixed ones; your own skills with those old names were left alone. Undo: `kit-rename.py migrate --revert` (in `<config>/claude-kit/tools`). Do not run any old name again.
