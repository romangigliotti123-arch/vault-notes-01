---
id: "rbx-publish"
type: skill
category: "roblox"
source: "own"
license: "first-party"
repo_path: "skills/roblox/rbx-publish/SKILL.md"
description: "Checklist for publishing, going live or updating a Roblox experience: settings, safety and age rules, store page, monetisation sanity, performance, rollback. Use for go live and final release checks, before publishing or a major update."
orig_name: "rbx-publish"
tags: [lib/skill, cat/roblox, src/own]
---

# rbx-publish

> Checklist for publishing, going live or updating a Roblox experience: settings, safety and age rules, store page, monetisation sanity, performance, rollback. Use for go live and final release checks, before publishing or a major update.

Type: skill | Category: [[categories/cat-roblox|roblox]] | Source: [[sources/src-own|own]] | License: first-party
Repo file: `skills/roblox/rbx-publish/SKILL.md` (extra files, if any, sit beside it in the repo)

Related: [[S--own--rbx-datastore]], [[S--own--rbx-monetize]], [[S--own--rbx-playtest-list]], [[S--own--rbx-remote-sec]], [[S--own--rbx-thumb-brief]]

---
# Roblox publish checklist

Claude never presses Publish or changes live settings; this list produces a go / no-go for Roman, who does the publish (it is public and cannot be fully undone).

1. Build: the exact place version/commit, changelog of what is new, a rollback plan (previous version restorable from Version History in Studio).
2. Tests: rbx-playtest-list passed on phone-sized emulation and a Local Server with 2+ players; rbx-remote-sec review has no Critical or High left; rbx-datastore tests passed; `static_scan.py --gate` security score 7 or higher (below 7 is a launch blocker).
3. Safety and policy: the experience questionnaire/maturity rating matches the content; no real-money gambling, no paid random rewards, no misleading claims; user text goes through Roblox filtering (`TextService:FilterStringAsync` / `TextChatService`); no personal data collected; third-party assets licensed.
4. Store page: title, description, icon, 3+ thumbnails (rbx-thumb-brief), genre, devices, max players, access (public/friends/private) as intended; Social links optional.
5. Monetisation: rbx-monetize verdict pass; every product has the correct id in the shipped build; prices as planned.
6. Performance: rbx-perf numbers within target on the weakest target device; StreamingEnabled decision made.
7. Observability: custom analytics events for the funnel (spawned, first action, first reward, quit point), error logging to Output or a webhook-free approach, DataStore failure counts.
8. Launch plan: publish time when Roman can watch the first hour; checklist for the first hour (crash rate, error spam, purchases working, DataStore errors); who rolls back and how.

Output: table item | status (pass / fail / unknown) | evidence | owner. Final line: GO, NO-GO or GO WITH RISKS.
