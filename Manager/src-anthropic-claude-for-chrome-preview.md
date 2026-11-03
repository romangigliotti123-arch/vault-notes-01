---
tags: [manager-kb, source]
url: https://www.anthropic.com/news/claude-for-chrome
type: eng-blog (product + safety)
author: Anthropic
published: 2025-08-26
accessed: 2026-10-29
reliability: high (first-party, numbers from internal red-team)
---
# Piloting Claude for Chrome
## Key claims
- Pilot with 1,000 Max users, "controlled testing"; asks testers without safety-critical setups; recommends trusted sites and avoiding financial/legal/medical sites.
- Red-team: 123 test cases / 29 attack scenarios; "Browser use without our safety mitigations showed a 23.6% attack success rate when deliberately targeted"; mitigations in autonomous mode cut it to 11.2%. Example attack: a fake "mailbox hygiene" email claiming "no additional confirmation required" made Claude delete emails without confirmation.
- Controls: site-level permissions (grant/revoke any time); action confirmations before high-risk actions like publishing, purchasing, sharing personal data, kept even in "autonomous mode"; blocked high-risk site categories (financial services, adult, pirated); classifiers for suspicious instruction patterns.
## Quotable
> Claude asks users before taking high-risk actions like publishing, purchasing, or sharing personal data. Even when users opt into our experimental autonomous mode, Claude still maintains certain safeguards for highly sensitive actions

## Used by
[[topic-personal-assistant-agents]], [[topic-remote-mobile-ux]]
