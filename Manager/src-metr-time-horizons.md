---
tags: [manager-kb, source]
url: https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/
type: eng-blog
author: METR (Kwa, West et al.)
published: 2025-03-19 (page since updated)
accessed: 2026-10-29
reliability: high (primary eval org)
---
# Measuring AI Ability to Complete Long Tasks (METR time horizons)
## Key claims
- Time horizon = human-expert task length at which a model succeeds with x% probability (headline x=50%), from a logistic fit of success vs human task length. Claude 3.7 Sonnet 50% horizon about one hour.
- 50% horizon doubling approximately every 7 months over 6 years; on SWE-Bench Verified with separate human estimates doubling time under 3 months (page notes measurement caveats).
- Reliability collapses with task length: "almost 100% success rate on tasks taking humans less than 4 minutes" but "<10% of the time on tasks taking more than around 4 hours".
- Page notes later TH1.1 estimates exist and the static figures reflect March 2025 data.
## Page update (2026), from https://metr.org/time-horizons/ (fetched 2026-10-29)
- Page states "Measurements above 16 hrs are unreliable with our current task suite" and "This page is no longer actively updated" (September 8th, 2026 note). Newest models listed (dates = added to page): Claude Mythos Preview (early) May 8 2026; GPT-5.4 Apr 10 2026; Claude Opus 4.6 Feb 20 2026; Claude Sonnet 4.5 Sep 30 2025 (newest Sonnet). GPT-5 50% horizon "around 2 hours and 17 minutes". Per-model values live in a linked data file not fetched; secondary reports of 14.5 h (Opus 4.6) are unverified here.
- Two versions: Time Horizon 1.1 (current) and 1.0 (March 2025).
## Quotable
> "succeed <10% of the time on tasks taking more than around 4 hours"

## Used by
[[topic-brief-prompt-engineering]], [[topic-multi-agent-failure-modes]]
