---
name: rbx-launch-check
description: "Builds a phone-friendly launch checklist (HTML plus markdown) for one Roblox game from the knowledge base: relative due dates, priorities, owners, a source per item. Use for a launch checklist, pre-launch plan, 'am I ready to launch'. The go/no-go publish gate is rbx-publish."
---

# Roblox launch checklist

Output: `launch-checklist-<game>.html` (tick boxes, progress bar, filters, saved in the browser) and `.md`, tailored to the game, with every item sourced.

## Inputs (assume and state; do not block)

Game name and genre, stage (concept / alpha / soft launch / pre-launch / relaunch), launch date (default: 4 weeks from today's date), team size and owners, monetisation plan (passes / products / none yet), platforms (mobile-first default), audience age, whether ads and a Discord are planned, current D1/PTR if any.

## Procedure

1. Pull the merged base: read `<KB>/_tools/CHECKLIST-launch.md` (its `Must` items per phase) and, if monetisation is in scope, `CHECKLIST-monetization.md`. These are regenerated daily from the KB.
2. Add what is current and specific: 
   ```
   K="bash .rbx/claude-kit/tools/pyrun .rbx/claude-kit/tools/kbq.py"   # run `$K where` once to see VAULT/KB/ASSETS
   $K find "release requirements age rating questionnaire 16+ gate" -t roblox-platform-changes -n 6
   $K find "soft launch before ads D1 first play funnel" -t playtesting-and-feedback,ads-and-sponsored-experiences -n 6
   $K find "<genre> launch mistakes" -t common-mistakes -n 5
   $K docs "publish requirements thumbnails experience details" -n 5
   ```
3. Tailor: drop items that do not apply (for example Discord items when none planned; keep but mark `could`), keep the item text short and imperative, make vague items measurable ("D1 at or above 10% on a soft launch" with the benchmark flagged indie), add 3-6 game-specific items.
4. Schedule: set `due` relative to launch (T-28, T-14, T-7, T-1, T+0, T+3, T+7) and an `owner`; order within a phase by due date. Priority: `must` for items most widely agreed across KB topics or official requirements; `should` for solid practice; `could` for nice-to-have.
5. Write `items.json` (schema in `make_checklist.py`), then build:
   `bash ".rbx/claude-kit/tools/pyrun" ".rbx/claude-kit/vault-mode/.claude/skills/rbx-launch-check/make_checklist.py" items.json launch-checklist-<game>.html --md launch-checklist-<game>.md`
6. Verify: open the JSON count, confirm every `must` item has `source` and `flag`, and spot-check 3 sources against the KB output. Tell the calling session the file path; the calling session may publish the HTML as a private Artifact for phone use.

## Phases (use these names, in order)

1. Idea and validation · 2. Core loop and economy · 3. Build quality (scripting, security, performance) · 4. First session and onboarding · 5. Playtest and soft launch · 6. Packaging (icon, thumbnails, title, description) · 7. Monetisation setup · 8. Community and pre-launch marketing · 9. Compliance and platform requirements · 10. Launch week (ads, analytics, live ops)

Only include phases that apply to the stated stage.

## Rules

- Source every item: link from kbq output (youtu.be timestamp or create.roblox.com URL) and the flag official / indie / mixed / devforum. Official overrides indie.
- Indie numbers (D1 targets, budgets, CTR) are marked indie and described as typical, not required.
- Do not invent requirements; platform requirements (age rating, 16+ gate, tax, DevEx) come from `docs`/official rows only; if unsure write "verify in Creator Hub" and mark UNVERIFIED.
- No spending, publishing or posting; the checklist only lists them.

## Self-check

- [ ] 25-60 items, grouped in the phases above, each with priority and due.
- [ ] Every `must` has a source and flag; no invented numbers.
- [ ] HTML built and the item count matches the JSON.
- [ ] Items are tailored to the game, not a generic dump.
