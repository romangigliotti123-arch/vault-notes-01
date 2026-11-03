---
name: support-macro-writer
description: "Write canned replies for common game support issues (lost items, failed purchases, bans and appeals, bugs, data loss, account safety) that are kind, short, truthful and safe: no personal data requests, no promises of compensation that were not agreed, a path to escalate. Lints every macro with a script. Use when the same support case keeps arriving or before launch."
category: community
tags: support, macros, replies, tickets, purchases, appeals, templates, tone, safety, discord
kb: Roblox/roblox-kb/community-and-discord.md, Roblox/roblox-kb/age-ratings-moderation-and-tos.md, Roblox/roblox-kb/ads-stats-monetisation-playbook.md
related: faq-writer, bug-intake-builder, toxicity-response-playbook, moderation-rules-writer, receipt-flow-tester, welcome-message-writer, hotfix-playbook
---

# support-macro-writer

Fast, consistent, honest replies keep trust. The vault: be transparent about changes and money, show odds and provide support for failed transactions, and after a monetisation bug notify affected players with an apology, fix and compensation. This builds the reusable replies and the rules for using them. It sends nothing and promises nothing for the owner.

## When to use
The same support question has come in several times, before launch, or after an incident that needs a standard reply. Not for: a public FAQ (`faq-writer`), bug intake (`bug-intake-builder`), or an incident playbook (`toxicity-response-playbook`).

## Inputs (max 2)
1. The top five or six support case types (default: lost progress, purchase did not arrive, banned or muted, bug report, exploit report, account safety). 2. What the owner can actually offer (default: apology, fix, explanation; compensation only if the owner decides).

## Procedure
1. For each case write: when to use it, the macro, what to check first, and the escalation. Keep every macro to 40-80 words: greeting, understanding, what happens next, thanks.
2. Purchase problems: the macro asks only for what the owner needs in the ticket (the item name and approximate time; the receipt id the game logged) and never asks for passwords, payment details, personal info or screenshots of account pages. Tell players real purchases are reconciled using the game's receipt log (see `receipt-flow-tester`) and that Roblox handles its own refunds and payment disputes through Roblox support; live-check the current Roblox support flow.
3. Bans and appeals: state the rule, the decision route, and the appeal path from `moderation-rules-writer`; never reveal another player's data or evidence; never argue.
4. Data loss and bugs: apologise once, say what is known, give the status vocabulary from `bug-intake-builder`, and promise only the next update time.
5. Compensation: write the macro only after the owner has chosen what to give; use a standard amount per severity, applied to everyone affected; log who got what.
6. Safety: no macro invites a DM; support happens in public support channels or tickets; staff do not accept off-platform payments or trades; a young user is never asked their age.
7. Lint all macros together: `python welcome-message-writer/scripts/text_lint.py macros.txt --max-words 90`; fix every FAIL, read every WARN, rerun to exit 0 (a macro that blames, e.g. "read the rules", is a WARN to rewrite).
8. Review them quarterly with real tickets: delete macros nobody used, add the new top case.

## Studio MCP path
Optional for facts: `list_roblox_studios` -> `get_studio_state` -> `script_grep` for the DataStore or purchase handler to confirm what is logged (receipt id, timestamp) before promising a lookup; do not invent log fields.

## Fallback
Plain text. Replies are posted by staff; nothing is sent by this skill.

## Evidence
`Roblox/roblox-kb/community-and-discord.md` (be transparent about changes and money; show odds and provide support for failed transactions; notify affected players with apology, fix and compensation; ignore trolls, respond publicly only for broken features). `Roblox/roblox-kb/age-ratings-moderation-and-tos.md` (safety, escalating enforcement). `Roblox/roblox-kb/ads-stats-monetisation-playbook.md` for monetisation trust context.

## Output
`community/macros.md`: a table (case, when to use, macro, check first, escalate to) of about six cases, plus the lint output. Under 70 lines.

## Acceptance checks
- [ ] `text_lint.py macros.txt --max-words 90` exits 0; output quoted.
- [ ] No macro requests passwords, payment details or personal data.
- [ ] No compensation is promised unless the owner has set it.
- [ ] Every macro names an escalation route.
- [ ] A quarterly review step is listed.

## Pitfalls
Robotic tone. Promising compensation nobody approved. Asking for account details. Replying in DMs to minors. Revealing why another player was banned.

## Related
`faq-writer`, `bug-intake-builder`, `toxicity-response-playbook`, `moderation-rules-writer`, `receipt-flow-tester`.
