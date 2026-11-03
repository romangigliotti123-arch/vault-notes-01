---
name: privacy-data-checker
description: "Inventory what personal data a game stores or sends (DataStores, outbound HTTP, analytics, logs, webhooks) and check it can be deleted on a right-to-be-forgotten request: user id in store names/scopes/keys, deletion templates, webhook for complex cases, nothing personal leaving the platform. Use before publish and before adding any data feature."
category: publish
tags: privacy, personal data, right to be forgotten, RTBF, data stores, deletion templates, HTTP, analytics, compliance
kb: Roblox/roblox-kb/data-persistence.md, Roblox/roblox-kb/age-ratings-moderation-and-tos.md, Roblox/roblox-kb/anti-exploit-and-security.md, Roblox/roblox-kb/analytics-metrics.md
related: tos-compliance-checker, datastore-schema-builder, secrets-leak-scanner, post-launch-monitor, publish-readiness-gate, exploit-audit
---

# privacy-data-checker

One job: answer "what do we keep about players, and can we delete it?" Creators remain responsible for permanently deleting personal data when a user deletes their account. `scripts/rtbf_check.py` finds DataStore names, scopes and key expressions and checks the user id is present where a deletion template can match it; `tos-compliance-checker/scripts/compliance_gap.py --focus data` flags outbound HTTP writes and personal-data words on lines that send HTTP. Template syntax, limits and timelines are `live-check`: the Creator Docs pages change.

## When to use
Before publish, when adding a DataStore, leaderboard, analytics call, webhook, Discord logging or any external service, and when Roblox sends an RTBF message. Not for: designing the data schema (`datastore-schema-builder`), secrets in code (`secrets-leak-scanner`), asset privacy (images/meshes visibility, a Creator Hub task).

## Inputs (max 2)
1. Project folder (default: current). 2. Existing deletion templates as JSON, if any (default: none yet).

## Procedure
1. Open the live RTBF pages (Evidence) and copy the current template format, token spelling, template limit and the deletion deadline into the notes with the date.
2. Run `python -I ~/.claude/claude-kit/skillpack/publish/privacy-data-checker/scripts/rtbf_check.py <project>`. Read each store row: OK = user id in name/scope; WARN = it must be in every key; the key list shows expressions without a user id.
3. Fix keys that hold personal data but no user id: rename going forward (migrate with `datastore-schema-builder`), because entries without the id cannot be matched by automated deletion.
4. Write templates (`name_pattern`, `scope_pattern`, `key_pattern` with the exact case-sensitive id token from the live page) for every store holding user data, then run `rtbf_check.py <project> --templates templates.json`: a `FAIL` means a store no template covers. Keep within the template limit.
5. Run `python -I .../tos-compliance-checker/scripts/compliance_gap.py <project> --focus data`. Remove any personal data sent off-platform; webhooks that receive player ids need a deletion route.
6. Complex cases (custom logic, non-DataStore storage): plan a creator webhook for erasure requests per the page, with an owner and a daily inbox check; list what the webhook deletes.
7. Test end to end on a test game with a dummy account (the page recommends this): create data, request deletion, confirm removal within the deadline. This needs Roblox and stays `untested` until the owner runs it.
8. Write `release/privacy.md`: data inventory (what, where, id location, deletion route), template list, webhook plan, test status, page dates.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `script_grep` (`GetDataStore`, `GetOrderedDataStore`, `PostAsync`) -> `execute_luau` (Server) to list real key prefixes with `DataStore:ListKeysAsync` on a test universe only -> `get_console_output`. Never read live player data; use the Data Stores Manager for live comparison, as an owner action.

## Fallback
The scripts run on the Rojo folder. Templates are validated against code names only; the platform's own validation and the deletion test are `untested`.

## Evidence
Official (live-check): `Roblox/docs/Videos/2026-10-28 - Docs cloud-services data-stores right-to-be-forgotten.md` (templates with the exact id token, standard and ordered stores only, 100-template limit, verify within 30 days, publish carefully), `... Docs production publishing RTBF-and-creators.md` (creators stay responsible; daily inbox messages; webhook for complex cases). Pack: `Roblox/roblox-kb/data-persistence.md`, `Roblox/roblox-kb/age-ratings-moderation-and-tos.md`.

## Output
`release/privacy.md` and `templates.json`.

## Acceptance checks
- [ ] `rtbf_check.py` output is attached; no store row is `FAIL`.
- [ ] Every key holding personal data contains the user id (or has a webhook route).
- [ ] No personal data on outbound HTTP lines (`--focus data` clean).
- [ ] The live page date and template limit are recorded.
- [ ] `rtbf_check.py --selftest` prints `selftest ok`.

## Pitfalls
Using one global key for a table of players. Assuming the automation covers MemoryStores, files or Discord logs. Mistyping the id token's case. Logging emails or real names "for support". Forgetting the daily inbox check after launch.

## Related
`tos-compliance-checker`, `datastore-schema-builder`, `secrets-leak-scanner`, `post-launch-monitor`, `exploit-audit`.
