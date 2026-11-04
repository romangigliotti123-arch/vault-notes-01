# Usage safety

Why: one session launched 7 workers plus 8 helpers and exhausted a shared 5-hour usage window, stopping everything.

## Before launching
1. Get the user's cap in one question: a usage line ("stop at 70% of the 5-hour window") and/or a dollar, time or agent-count cap. Write it in the ledger. No answer: default max 2 concurrent workers, no high-effort fan-out, ask again before a third.
2. Estimate: workers x effort x expected length. High effort and opus cost several times a medium sonnet. If the estimate may breach the cap, shrink first (fewer sources, medium effort, haiku for lookups).
3. A dollar budget has no live meter for you: convert it to a hard cap on workers, sources and turns up front (e.g. "$2" => 1 sonnet-medium worker, <= 12 sources, maxTurns 40, no fan-out), and say the conversion to the user. Workers cannot see spend either; caps are the control. Under a small dollar cap prefer ONE worker over parallel ones (each extra worker re-reads context and adds a brief and a report), your own tokens count too, and never use opus. If the work cannot fit the cap, say what you would drop and let the user decide; do not quietly exceed it.
4. Every brief carries a budget (searches/sources/time/turn cap) and "no subagents".

## While running
- Never exceed the cap; count every agent. Start no new workers when the user says usage is close.
- Keep your own context small: pipe tool output through `head`/`select -first 40`, no dumps over ~50 lines, reports to files.
- No polling or sleep loops; wait for completion notices.
- Never retry a rate-limited or limit-stopped step in a loop.

## Reading usage (you cannot see it yourself)
Ask the user to run `/usage` in Claude Code (or open claude.ai > Settings > Usage) and tell you: percent of the current 5-hour session window, percent of the weekly limit, and the reset time. Do not scrape pages or automate a browser for this. If the user is away, treat the cap as the smaller of their stated cap and 2 workers.

## On a usage-limit message

Stop launching, record running jobs in the ledger, tell the user in one line what stopped, what is saved and the reset time; never retry the limited step in a loop and never work around limits (other accounts, hiding work). [cold:rbx-manager/usage-limit-hit.md] read only after a usage-limit message appears (stop, ledger, pause/resume steps).

## Measure before changing, keep teams off

Read `/usage` attribution once before changing routing or caps; keep `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` unset or 0 (teammates cost about 7x tokens). [cold:rbx-manager/usage-measure-teams.md] read only before changing routing or caps, or when `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` is mentioned.