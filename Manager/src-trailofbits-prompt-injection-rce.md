---
tags: [manager-kb, source]
url: https://blog.trailofbits.com/2025/10/22/prompt-injection-to-rce-in-ai-agents/
type: eng-blog
author: Trail of Bits
published: 2025-10-22
accessed: 2026-10-29
reliability: high (security firm, concrete exploits; vendors unnamed)
---
# Prompt injection to RCE in AI agents (argument injection through "safe" commands)
## Key claims
- Agents auto-run "safe" commands (`find`, `grep`, `rg`, `git`, `go test`, `fd`) without validating flags, so injected arguments reach RCE in one shot: `go test -exec bash...`, `git show --format/--output` writing a file then `rg --pre bash` running it, `fd -x=python3`.
- Payloads can hide in code comments, rule files, repos, logs. Techniques catalogued in GTFOBins / LOLBAS.
- "Blanket blocking arguments would break essential functionality" so flag filtering is fragile; "safe" command allowlists without a sandbox are "fundamentally flawed".
- Defence: sandbox (containers, WASM, Seatbelt/Landlock); if building a facade, put `--` before user input, disable shell execution, validate inputs; log every command execution; re-involve the user on suspicious chains.
- Implication for this host: Windows has its own LOLBAS surface (powershell, certutil, bitsadmin, mshta, schtasks); pattern-based guards (hooks, ask rules) are speed bumps, not walls.
## Quotable
> Blanket blocking arguments would break essential functionality

## Used by
[[topic-agent-security]]
