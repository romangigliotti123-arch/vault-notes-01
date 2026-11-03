---
tags: [manager-kb, source]
url: https://code.claude.com/docs/en/interactive-mode.md
type: official-doc
author: Anthropic (Claude Code docs)
published: undated (v2.1.234+)
accessed: 2026-10-29
reliability: high (section "Wait for a usage limit to reset" read verbatim from saved fetch)
---
# Interactive mode: "Wait for a usage limit to reset"
## Key claims
- Automatic continue after a claude.ai usage limit is on by default in INTERACTIVE sessions with a subscription login (v2.1.234+). Continues at reset without resending the last message.
- "Claude Code doesn't start the wait on its own in these cases: Remote Control and agent team teammate sessions: a person at that terminal can still start one." Also reset > 24 h away (weekly limit), Opus/Sonnet limit while on another family. In an RC session run `/rate-limit-options` yourself.
- "Claude Code doesn't offer the wait at all" in background sessions and `-p` runs.
- If the computer slept >~30 min and the limit reset meanwhile, it asks to press Enter instead of continuing.
- If it hits the limit again it re-arms at most twice, then stops ("Automatic continue stopped after repeated usage-limit hits").
- The wait does not survive exiting Claude Code; resume does not restart it. The continuation still asks permissions as usual.
- StopFailure hook matchers include `rate_limit`, so a hook can observe the limit even though it cannot decide.

## Used by
[[topic-long-running-always-on-agents]], [[topic-model-effort-routing-cost]]
