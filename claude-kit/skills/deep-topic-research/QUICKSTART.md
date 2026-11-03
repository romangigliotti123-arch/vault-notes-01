# deep-topic-research: quickstart (one page)

1. **Install**: copy this folder to `~/.claude/skills/deep-topic-research/` (Windows: `%USERPROFILE%\.claude\skills\`). Start a new Claude Code session.
2. **Check** (free): run `scripts/doctor.sh` (Mac/Linux) or `scripts/doctor.ps1` (Windows). Install what it says only if you want YouTube / GitHub extras.
3. **Ask**: `research <your topic>` or `/deep-topic-research`.
4. **Answer 4 questions**: budget (Light ~$1 / Moderate ~$5 / Heavy ~$15), time, worker cap (1 / 3 / 6), depth (Quick / Thorough / Exhaustive; optional creator-credibility check). Say "just go" for the safest Light defaults.
5. **Read the plan** it prints (cost range per stage, share of a usage window, how workers are orchestrated), then let it run. It stops by itself at your limits and can resume.
6. **Open the result** in the folder it names (with a `claudes-vault` clone: `<vault>/My Research/<topic>/`, else `./research/<topic>/`):
   - `cheat-sheet.md`: do this first (only OFFICIAL or CORROBORATED claims)
   - `00-README.md`: summary plus "How reliable is this" (counts per label and the 5 shakiest claims)
   - `playbook.md`: every step labelled; `creator-credibility.md`: who to trust; `recall-check.md`: 10 self-test questions

Labels: OFFICIAL (matches official docs), CORROBORATED (2+ independent sources), SINGLE-SOURCE, CONTRADICTED (both views shown), OUTDATED-UNSURE.
Resume: "resume the deep-topic-research run for <topic> with 2 more hours". Public sources only; notes are for your own use.
