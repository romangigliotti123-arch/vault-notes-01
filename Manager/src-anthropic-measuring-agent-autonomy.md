---
tags: [manager-kb, source]
url: https://www.anthropic.com/research/measuring-agent-autonomy
type: eng-blog (research)
author: Anthropic Societal Impacts
published: 2026-02-18
accessed: 2026-10-29
reliability: high (first-party telemetry, Claude-classified)
---
# Measuring AI agent autonomy in practice
## Key claims
- New Claude Code users (<50 sessions) use full auto-approve ~20% of sessions; >40% by ~750 sessions. Interrupt rate is 5% of turns at ~10 sessions vs ~9% for experienced users: "experienced users auto-approve more but interrupt more" = a shift from approving each action to monitoring and intervening.
- On the most complex tasks Claude Code asks for clarification more than twice as often as on minimal tasks, and more often than humans interrupt it (n=500k sessions).
- Why Claude stops itself: present a choice between approaches 35%; gather diagnostic info 21%; clarify a vague request 13%; request missing credentials/access 12%; get approval before acting 11%.
- Why humans interrupt: provide missing technical context/corrections 32%; Claude slow/hanging/excessive 17%; they got enough help 7%; want to do the next step themselves 7%; change requirements mid-task 5%.
- 99.9th percentile Claude Code turn ~42 min; median much shorter.
- Recommendation: "Oversight requirements that prescribe specific interaction patterns, such as requiring humans to approve every action, will create friction without necessarily producing safety benefits."
## Quotable
> effective oversight doesn't require approving every action but being in a position to intervene when it matters.

## Used by
[[topic-anthropic-agent-guidance]], [[topic-remote-mobile-ux]]
