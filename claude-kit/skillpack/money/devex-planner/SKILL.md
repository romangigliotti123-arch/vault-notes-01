---
name: devex-planner
description: "Plan cashing out Robux through Developer Exchange: check the eligibility floor, estimate the gross payout by rate class, order the cash-out around the monthly limit, review waits, holds and tax paperwork, and keep a records template. Use when a game is earning and the owner asks about cashing out; it never submits a request."
category: money
tags: devex, developer exchange, cash out, earned robux, payout, tax, tipalti, rates, holds, records
kb: Roblox/roblox-kb/business-and-payouts.md, Roblox/roblox-kb/monetisation-other.md, Roblox/roblox-kb/studio-business-funding-and-publishing.md, Roblox/roblox-kb/roblox-platform-changes.md, Roblox/roblox-kb/_tools/CHECKLIST-monetization.md
related: premium-benefits-planner, subscription-planner, private-server-planner, ugc-item-planner, rbx-weekly
---

# devex-planner

One job: turn "can we cash out, how much and when" into a plan with dates and records. DevEx rules, rates and tax requirements change often and the cost of a mistake is real money and delays, so this skill estimates and plans; it never submits a request, enters tax data, or moves money. Everything below is from the vault's Roblox Creator Docs 2026-10 notes and must be live-checked on the DevEx pages the same day.

## When to use
Earnings are accumulating, a cash-out is being considered, or a budget needs real payout figures. Not for: pricing items, picking monetisation features, or advising on taxes (the owner needs an accountant; vault says to hire one and form an entity early for serious income).

## Inputs (max 3)
1. Earned Robux by class: balance from before the Sept 2025 rate change (`legacy`), purchases by eligible verified 18+ US players (`plus18`), everything else (`standard`) (default: read the Creator Dashboard; ask if the split is not shown). 2. Account facts: verified email, tax form status, age, group or individual (default: ask). 3. Planned cash-out month.

## Procedure
1. Read the rules: `python -I ~/.claude/claude-kit/tools/kbq.py section business-and-payouts rules --max-chars 6000`. List: eligibility floor, once per calendar month, review times, registration deadline, name rule, rates, holds.
2. Estimate: `python -I ~/.claude/claude-kit/skillpack/money/devex-planner/scripts/devex.py --legacy <n> --plus18 <n> --standard <n>`. Default rates come from the vault (0.0035 / 0.0054 / 0.0038 USD per Robux); override with `--legacy-rate`, `--plus18-rate`, `--standard-rate` after reading the DevEx page. Exit code 1 means below the 30,000 floor. The output is a gross estimate; fees, FX and taxes are not modelled.
3. Order matters: the vault says old-rate (legacy) balances are cashed first and spending Robux does not reduce them. Do not recommend spending Robux to "protect" a rate.
4. Timing plan: one request per calendar month, cannot be cancelled, Robux held during review; first approval takes about 10 business days and returning about 5 (vault); payment-method registration must finish within a week of the invite or the request is auto-declined and Robux are refunded; payment verification takes 5-8 business days. Lay the dates on a calendar with a buffer.
5. Holds and escrow: earned Robux have a 60-day holding period; local-currency earnings escrow at least 60 days and pay monthly; Creator Store sales escrow 30 days; ads pay on the 25th of the following month; subscription payouts differ by currency (vault). Show the owner what is pending versus releasable.
6. Paperwork checklist for the OWNER: exact legal name matching the payout account, tax form on file (W-9 for US, W-8 otherwise), a note that the vault lists a tax-information update deadline of Oct 31, 2026 (live-check whether it applies now), two-step verification before granting any payout permission, phishing warning (real forms only inside the official portal).
7. Records template: a spreadsheet row per cash-out (date requested, Robux by class, rate used, USD estimate, USD received, fees, notes) and a separate row for Creator Rewards, Premium and ad income (`premium-benefits-planner`).
8. Group games: split and permissions are decided in the group before any sale; document the split.

## Studio MCP path
Not applicable: DevEx lives on the website. Do not use Studio MCP for payouts.

## Fallback
The estimator script and the checklist; the owner does every portal step. All platform behaviour is `untested` by this skill.

## Evidence
`Roblox/roblox-kb/business-and-payouts.md` (eligibility floor, monthly limit, review times, registration deadlines, name rule, legacy and current rates, holds and escrow, tax and records, accountant advice, platform revenue split, Creator Rewards as income), `Roblox/roblox-kb/monetisation-other.md` (DevEx 18+ rate eligibility; Creator Store and subscription payouts), `Roblox/roblox-kb/roblox-platform-changes.md`. The vault notes the 100,000 Robux minimum and Premium requirement from older guides are outdated.

## Output
`design/devex-plan.md`: estimate table, timeline with dates, owner checklist, records template. Short.

## Acceptance checks
- [ ] `devex.py` was run and its output quoted, with rates shown.
- [ ] `python -I .../devex.py --selftest` prints "4 checks ok".
- [ ] Every rate, floor and deadline carries "live-checked on <date>" or "unverified".
- [ ] The plan places exactly one cash-out per calendar month and includes a review-time buffer.
- [ ] No tax or legal advice is given beyond "consult an accountant"; no portal step is performed.

## Pitfalls
Using the old 100k minimum. Assuming rates are stable. Ignoring holds so cash flow fails. Name mismatches that cause rejection. Resubmitting after a name-discrepancy rejection instead of contacting support. Sharing payout details in chat.

## Related
`premium-benefits-planner`, `subscription-planner`, `private-server-planner`, `ugc-item-planner`, `rbx-weekly`.
