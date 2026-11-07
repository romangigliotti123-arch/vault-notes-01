---
name: tos-compliance-checker
description: "Check a game design and its code against the platform rules that show up in code and settings (maturity answers, paid random items, ads, chat and text filtering, personal data, third-party links) and produce one gap list that routes each gap to the skill that fixes it. Use before publish and after any feature that touches players' text, money, data or ads."
category: publish
tags: terms of service, community standards, compliance, policy, audit, PolicyService, text filtering, publish, gap list
kb: Roblox/roblox-kb/age-ratings-moderation-and-tos.md, Roblox/roblox-kb/monetisation-other.md, Roblox/roblox-kb/ads-and-sponsored-experiences.md, Roblox/roblox-kb/_tools/CHECKLIST-launch.md
related: age-rating-prep, paid-random-compliance, chat-compliance-checker, ad-policy-checker, ugc-moderation-checker, privacy-data-checker, regional-availability-checker, publish-readiness-gate
---

# tos-compliance-checker

One job: the umbrella audit. It does not read the legal text for you and does not decide what is allowed; it finds where the CODE lacks the hooks the official pages ask for, and sends each gap to the specialist skill. `scripts/compliance_gap.py` is the engine: it reuses `age-rating-prep/scripts/feature_scan.py` for the feature inventory and adds per-rule checks (PolicyService calls, text filtering, legacy chat, third-party ad hosts, personal data on outbound HTTP). All rule wording, thresholds and names are `live-check`: policies change, so the page is opened first and the script second.

## When to use
Before the first publish and before updates that add chat, user text or images, paid random items, trading, ads, outbound HTTP or a new audience. Not for: the maturity questionnaire answers (`age-rating-prep`), licence status of assets (`asset-license-checker`, `copyright-checker`), account moderation appeals (a Creator Hub support task).

## Inputs (max 2)
1. Project folder (default: current project). 2. One-line list of features players can use that might not be in code yet (default: none).

## Procedure
1. Run `python -I .rbx/claude-kit/skillpack/publish/age-rating-prep/scripts/feature_scan.py <project>` and keep the lead counts; they decide which rule pages apply.
2. Run `python -I .rbx/claude-kit/skillpack/publish/tos-compliance-checker/scripts/compliance_gap.py <project>`. Exit 1 means at least one FAIL. Each row is `[LEVEL] focus: message <- file:line`.
3. For every focus that has a FAIL or WARN, open the matching official page NOW (live-check; titles are in Evidence) and confirm the rule still reads the same. If the page differs from this skill, the page wins; note the difference.
4. Route each gap: paid_random -> `paid-random-compliance`; ads -> `ad-policy-checker`; chat -> `chat-compliance-checker`; ugc -> `ugc-moderation-checker`; data -> `privacy-data-checker`; region -> `regional-availability-checker`.
5. Add the features the owner listed in Inputs that the scan cannot see (Studio-side GUI text, uploaded images, external services) as manual rows marked `untested`.
6. Write `release/compliance.md`: gap table (focus, level, evidence line, owning skill, status), the pages checked with the date, and the manual rows.
7. Feed the result to `publish-readiness-gate` as the "Content rules" evidence line. A FAIL left open is a `fail` gate, not a waiver by default.
8. Self-test: `python -I .../compliance_gap.py --selftest` prints `selftest ok`.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `script_grep` (or `execute_luau` in Edit mode, read-only) for `GetPolicyInfoForPlayerAsync`, `TextChannel`, `FilterStringAsync` when no project folder exists -> `get_console_output`. The tools only read; no rule is "tested" until a play session with a restricted-policy test account shows the branch, and that stays `untested` without Studio.

## Fallback
Run the scripts on the Rojo folder, or grep by hand with the same keywords. Anything needing a running session (policy values for a real account, filter behaviour, ad delivery) stays `untested`; the Python self-test is the headless proof of the scan logic only.

## Evidence
Official Creator Docs notes in the vault (live-check every one): `Roblox/docs/Videos/2026-10-28 - Docs chat guidelines.md` (TextChatService, text filtering, rate-limited shared text), `... Docs production promotion content-maturity.md` (answer from the most mature content; PolicyService for paid random and trading), `... Docs production monetization paid-random-items.md`, `... Docs production promotion comply-with-advertising-standards.md`, `... Docs production publishing RTBF-and-creators.md`. Pack knowledge: `Roblox/roblox-kb/age-ratings-moderation-and-tos.md`, `Roblox/roblox-kb/monetisation-other.md`. Indie claims never override the official pages.

## Output
`release/compliance.md` plus the raw script output pasted under it.

## Acceptance checks
- [ ] `compliance_gap.py` ran on the project and its row list is attached (quote the exit code).
- [ ] Every FAIL/WARN row has an owning skill and a status; none is silently dropped.
- [ ] Each official page used is listed with the date it was checked.
- [ ] Manual (unscanned) features are listed as `untested`.
- [ ] `compliance_gap.py --selftest` prints `selftest ok`.

## Pitfalls
Treating "no hit" as clearance. Treating an OK row as proof the hook is correct (it only proves the call exists). Quoting a rule from memory instead of the live page. Auditing once and then adding chat or ads later.

## Related
`age-rating-prep`, `paid-random-compliance`, `chat-compliance-checker`, `ad-policy-checker`, `ugc-moderation-checker`, `privacy-data-checker`, `regional-availability-checker`, `publish-readiness-gate`.
