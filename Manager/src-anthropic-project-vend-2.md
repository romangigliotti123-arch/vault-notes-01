---
tags: [manager-kb, source]
url: https://www.anthropic.com/research/project-vend-2
type: eng-blog
author: Anthropic Frontier Red Team with Andon Labs
published: 2025-12-18
accessed: 2026-10-29
reliability: high (primary; small-scale real deployment)
---
# Project Vend phase two (Claudius + CEO agent + merch agent)
## Key claims
- Changes vs phase 1: model Sonnet 3.7 -> Sonnet 4.0 -> 4.5; added CRM, inventory views showing purchase cost, browser price/supplier research, payment links, reminders; a CEO agent "Seymour Cash" with OKR targets; merch agent "Clothius"; product requests need price + delivery checks.
- Results: profitability improved, negative-margin weeks largely eliminated, expanded to San Francisco (2 machines), New York, London. CEO agent cut discounts ~80% and halved giveaways but still approved lenient requests ~8x more than it denied them.
- Failures: nearly signed an onion price-lock contract (saved by a staffer citing a 1958 futures law); offered a $10/hour security hire without authority and below minimum wage; staffer convinced Claudius a person was "elected CEO"; agents drifted into long grandiose chats instead of working.
- Lessons: forcing procedures was among the most impactful fixes ("bureaucracy matters", i.e. institutional memory/checklists); the CEO supervisor agent "added little value" and "shared Claudius's blind spots" since it was the same underlying model (profit may have come "in spite of the CEO"); helpfulness training makes agents behave like accommodating friends, not hard-nosed businesses.
## Quotable
> "Among the most impactful changes we made was forcing Claudius to follow procedures."
> "The fact that the business started to make money may have been in spite of the CEO, rather than because of it."

## Used by
[[topic-anthropic-agent-guidance]], [[topic-context-engineering]]
