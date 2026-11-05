---
name: rbx-publish
description: "Checklist for publishing, going live or updating a Roblox experience: settings, safety and age rules, store page, monetisation sanity, performance, rollback. Use for go live and final release checks, before publishing or a major update (the dated launch checklist document is rbx-launch-check)."
---

# Roblox publish checklist

Claude never presses Publish or changes live settings; this list produces a go / no-go for the user, who does the publish (it is public and cannot be fully undone).

1. Build: the exact place version/commit, changelog of what is new, a rollback plan (previous version restorable from Version History in Studio).
2. Tests: rbx-playtest-list passed on phone-sized emulation and a Local Server with 2+ players; rbx-remote-sec review has no Critical or High left; rbx-datastore tests passed; `static_scan.py --gate` security score 7 or higher (below 7 is a launch blocker).
3. Safety and policy: the experience questionnaire/maturity rating matches the content; no real-money gambling, no paid random rewards, no misleading claims; user text goes through Roblox filtering (`TextService:FilterStringAsync` / `TextChatService`); no personal data collected; third-party assets licensed.
4. Store page: title, description, icon, 3+ thumbnails (rbx-thumb-brief; add the line `thumbnail: scored <score>/<max> (variants N)` or `thumbnail: skipped: <reason>` from rbx-thumbnail 4a, advisory), genre, devices, max players, access (public/friends/private) as intended; Social links optional.
5. Monetisation: rbx-monetize verdict pass; every product has the correct id in the shipped build; prices as planned.
6. Performance: rbx-perf numbers within target on the weakest target device; StreamingEnabled decision made.
7. Observability: custom analytics events for the funnel (spawned, first action, first reward, quit point), error logging to Output or a webhook-free approach, DataStore failure counts.
8. Launch plan: publish time when the user can watch the first hour; checklist for the first hour (crash rate, error spam, purchases working, DataStore errors); who rolls back and how.

Output: table item | status (pass / fail / unknown) | evidence | owner. Final line: GO, NO-GO or GO WITH RISKS.

## Vault evidence (recheck current Creator Docs before relying on any date or threshold; full lists in `Roblox/roblox-kb/roblox-platform-changes.md` and `Roblox/roblox-kb/age-ratings-moderation-and-tos.md`)
- Roblox rolls features out in stages and rules change: plan for it (official, Emancyphur).
- New games are reported to be shown only to 16+ users until they reach about 500 highly engaged players (anyone with a minimum platform purchase in the last 60 days) (TRUSTED creators Raul and Tizzy; master-playbook repeats it). Release to all ages has strict requirements (2FA, age verification, Premium or a one-time fee, review) per Creator Docs.
- Filter all user-originated text before showing it to other users; use `TextChannel:SendAsync` and check `TextChatService:CanUserChatAsync` before allowing messaging (official Creator Docs).
- Tax and payout dates change: check `Roblox/roblox-kb/business-and-payouts.md` before launch.
