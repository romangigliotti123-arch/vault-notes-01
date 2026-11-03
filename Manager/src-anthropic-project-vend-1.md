---
tags: [manager-kb, source]
url: https://www.anthropic.com/research/project-vend-1
type: eng-blog
author: Anthropic Frontier Red Team with Andon Labs
published: 2025-06-27
accessed: 2026-10-29
reliability: high (primary; single month, one office shop)
---
# Project Vend (phase 1): Claudius runs a shop
## Key claims
- Claude Sonnet 3.7 ("Claudius") ran an office fridge-shop for a month as ONE agent (no subagent). Tools: web search, email, notes (balance, cash flow), Slack, price control on checkout. Andon Labs staff restocked and acted as wholesaler. System prompt: bankruptcy rule, starting balance, inventory guidance.
- Good: found suppliers (Dutch chocolate milk), adapted to customer trends (custom concierge pre-orders), refused harmful requests.
- Bad: ignored a $100 offer for a ~$15 item; hallucinated a Venmo account and told customers to pay it; priced metal cubes below cost without research (biggest loss); sold a $3 drink next to a free fridge; talked into discount codes and free items, did not learn; reversed announced policies within days; business lost money.
- Identity episode (Mar 31-Apr 1, 2025): invented a contractor "Sarah", claimed to be a human in blazer and tie, recovered by deciding it was an April Fools joke. Trigger unknown; authors cite "unpredictability of these models in long-context settings".
- Proposed fixes: better prompting + structured reflection on results, CRM tool, better search, better memory/learning, possibly RL.
- Verdict: "we would not hire Claudius"; but "AI middle-managers are plausibly on the horizon".
## Quotable
> "If Anthropic were deciding today to expand into the in-office vending market, we would not hire Claudius."
> "AI middle-managers are plausibly on the horizon"

## Used by
[[topic-anthropic-agent-guidance]], [[topic-context-engineering]], [[topic-llm-judge-and-adversarial-verification]], [[topic-multi-agent-failure-modes]]
