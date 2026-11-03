---
tags: [manager-kb, source]
url: https://www.anthropic.com/engineering/claude-code-auto-mode
type: eng-blog
author: John Hughes
published: 2026-03-25
accessed: 2026-10-29
reliability: high (primary; reports own error rates honestly)
---
# How we built Claude Code auto mode
## Key claims
- Motivation: users accept 93% of permission prompts anyway (approval fatigue). Auto mode replaces `--dangerously-skip-permissions`-style trust with classifier-based approvals.
- Two layers: server-side probe screens tool outputs for prompt injection; a transcript classifier (Sonnet 4.6) reviews each action. Stage 1 fast yes/no tuned to over-block; stage 2 chain-of-thought only on flagged actions. Classifier is reasoning-blind: sees user messages and tool calls only, not assistant prose or tool results.
- Threat model: overeager behaviour (scope escalation, credential hunting, skipping deploy checks), honest mistakes, prompt injection, misalignment. Defence in all cases: block the action.
- Numbers: real traffic n=10,000 stage-1 FPR 8.5%, full pipeline FPR 0.4%; real overeager actions n=52 FNR 17% ("the honest number"); synthetic exfiltration n=1,000 FNR 5.7%. Misses often = danger recognised but prior approval judged to cover it.
- Subagents: classifier checks delegation (can deny) and reviews subagent output on return (warns only). "a subagent that was benign at delegation could be compromised mid-run by a prompt injection".
- Deny-and-continue: blocked actions return to the agent with guidance to find a safer path; 3 consecutive or 20 total denials escalate to human (ends process in headless mode).
## Quotable
> "in practice users accept 93% of them anyway"
> "The 17% false-negative rate on real overeager actions is the honest number."

## Used by
[[topic-agent-security]], [[topic-anthropic-agent-guidance]], [[topic-remote-mobile-ux]]
