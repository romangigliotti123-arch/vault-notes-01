# Roblox skill pack

300+ focused skills for Roblox development, kept as files so they cost no context until used. They are NOT installed into `~/.claude/skills`; the installer copies this folder to `.rbx/claude-kit/skillpack/` and one small router skill, `rbx`, opens a skill on demand.

- Use: `/rbx <name> [what you want]`, `/rbx list [category]`, `/rbx find <words>`. Example: `/rbx gamepass-maker for a pet simulator`.
- From a shell or another agent: `python .rbx/claude-kit/tools/skillpack.py list|find|path|lint|catalogue`, or `vault-find.py "<job>" --type skillpack`.
- Catalogue (every planned skill, status built/planned): [CATALOGUE.md](CATALOGUE.md). Quality bar and rubric: [QUALITY.md](QUALITY.md). Scores: [REVIEW.md](REVIEW.md).
- Layout: `<category>/<name>/SKILL.md`, optional `scripts/` (Luau, Python) and `scripts/tests/` (Lune). Categories: design, systems, scripting, build, ui, perf, money, marketing, liveops, qa, community, publish, workflow.
- Checks: `bash skillpack/check-scripts.sh` (stylua, selene, luau-lsp on every script, Lune on every test), `python tools/skillpack.py lint` (format and KB path check; set `CLAUDES_VAULT` to the vault folder to verify KB links).
- A planned skill still runs through `/rbx <name>`: the router does a best-effort job from its one-line purpose and the vault, and labels the result.
- How the pack plugs in: `rbx-workflow` and `rbx-mentor` name pack skills; pack skills use `rbx-studio` modes (Studio MCP, Rojo, hand code) and the kit's tested systems (`PlayerData`, `Shop`, `DailyRewards`, `Analytics`, `Admin`) instead of re-implementing them.
- Adding a skill: add a row to CATALOGUE.md (or use a planned one), write `<category>/<name>/SKILL.md` to the QUALITY.md shape, put substantive code in `scripts/` and check it, run `skillpack.py lint`, score it in REVIEW.md, then `skillpack.py catalogue --write`.
