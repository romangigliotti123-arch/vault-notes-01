---
name: seasonal-calendar-builder
description: "Draft a year of seasonal and holiday content slots: computed holiday dates, Friday launch a week ahead, the 60/40 content split, scenery tail, quarterly major updates, season passes with UTC start and end, and clash flags. Use when planning the year or the next two seasons."
category: liveops
tags: seasonal, holiday, calendar, halloween, christmas, season pass, battle pass, year plan, schedule, utc
kb: Roblox/roblox-kb/updates-live-ops.md, Roblox/roblox-kb/events-and-seasonal-content.md, Roblox/roblox-kb/localization-and-international.md, Roblox/roblox-kb/monetisation-other.md
related: update-cadence-planner, event-planner, battle-pass-designer, ccu-forecaster, patch-notes-writer, limited-offer-designer, launch-teaser-planner
---

# seasonal-calendar-builder

Real-world events give a ready reason for content; the vault says save seasonal ideas for the right time, release holiday updates about a week before the holiday, and check the theme actually appeals to your players. This skill lays the year out so holidays, majors and season passes do not collide. One event's design is `event-planner`; the weekly rhythm is `update-cadence-planner`.

## When to use
Planning next year or the next two seasons, deciding whether a holiday is worth a slot, or setting season pass dates. Not for: designing the event content, or pricing a pass (`battle-pass-designer`).

## Inputs (max 3)
1. Year, hemisphere and main audience countries (default: current year + 1, northern, Western). 2. Number of major updates (default: 4, about quarterly). 3. Your own dates (anniversary, lore holiday) and holidays to skip.

## Procedure
1. Confirm the audience. Holidays differ by country (`localization-and-international.md`); look at your top countries in Creator Hub before keeping the default list, and replace entries that do not fit. Vault: create your own anniversary or lore holiday to stand out.
2. Run `python -I .rbx/claude-kit/skillpack/liveops/seasonal-calendar-builder/scripts/seasons.py --year 2027 --majors 4 --skip valentines --own "Anniversary:07-15"`. Easter and Thanksgiving are computed; each holiday gets a Friday launch about a week before, an announcement date, the 60 percent week-one / 40 percent next-three-weeks split and a scenery tail 10 days past the holiday. Majors are spread evenly and each seasonal slot within 21 days of one is marked CLASH. Announcements are pushed to at least 3 days apart. Stop condition: resolve every CLASH by moving the slot or the major.
3. Pick the content for each slot from the "reuse" rule: reskin existing pets, items or areas for the season (vault) and add one permanent piece so the slot leaves value behind. Rotate back to classic content after the event.
4. Season passes: set `startUtc` and `endUtc` explicitly (official season-pass package; a season of about 3 months is common, longer ones exist) so the countdown and the limited window are driven by data, and plan catch-up (double XP in the final week). Pass design and prices: `battle-pass-designer`.
5. Keep event length 7-30 days for featuring (official guidance), at most 10 published events ongoing or upcoming per experience, and the planned gap between large events about 2-3 months.
6. Add marketing beats from the plan (`launch-teaser-planner`, `social-post-calendar`) and capacity checks for the launches (`ccu-forecaster`).
7. Review quarterly: drop slots that returned little against the pre-event baseline (judge sustained baseline, not the spike).

## Studio MCP path
Not needed for the calendar. For the in-game side: `script_grep` for existing event config tables so dates are data (UTC), not code; `multi_edit` to add season entries to the config.

## Fallback
Python 3 prints the calendar; paste it into `liveops/calendar.md`. Dates are plan values; confirm each against the current year's calendar.

## Evidence
`Roblox/roblox-kb/updates-live-ops.md`: release holiday updates about a week before; 60 percent in week one, 40 percent over three weeks; seasons about 3 months; majors about quarterly; set startUtc and endUtc on every season (Roblox Creator Docs 2026-10); events of 7-30 days perform best for featuring; at most 10 events ongoing or upcoming; do not rush seasonal updates; check theme appeal; Today's Picks favours notable updates and seasonal tie-ins. `events-and-seasonal-content.md`: keep seasonal scenery 1-2 weeks past the event; rotate to classic content; reskin existing pets.

## Output
`liveops/calendar-<year>.md`: dated table (launch, kind, theme, announce, scenery until, season pass start/end UTC), clash notes, audience assumptions.

## Acceptance checks
- [ ] `seasons.py --selftest` prints "selftest ok (8 checks)".
- [ ] Every launch is a Friday; no CLASH remains; announcements at least 3 days apart.
- [ ] Holiday list matches the actual audience countries.
- [ ] Each slot has a reuse plan, a permanent leftover and a measurement date.
- [ ] Season entries have explicit UTC start and end.

## Pitfalls
Assuming everyone celebrates the same holidays. Shipping seasonal content under deadline pressure (vault: a rushed Halloween update drew mixed feedback). A new event with no history cannot sustain interest alone. Local-time countdowns.

## Related
`update-cadence-planner`, `event-planner`, `battle-pass-designer`, `ccu-forecaster`, `launch-teaser-planner`.
