---
id: "roblox-brain/roblox-gui"
type: skill
category: "src-roblox-brain"
source: "roblox-brain"
license: "MIT"
repo_path: "sources/roblox-brain/skills/gameplay/roblox-gui/SKILL.md"
description: "Use when building or fixing Roblox menus, HUDs, shops, dialogs, or UI that must work on phones, tablets, desktop and console."
orig_name: "roblox-gui"
orig_when_to_use: "Also when changing or reviewing any UI, or when UI overlaps, is cut off, too small, misplaced or unreadable on mobile, a phone, tablet, TV or with a controller."
orig_last_reviewed: "2026-10-14"
tags: [lib/skill, cat/src-roblox-brain, src/roblox-brain]
---

# roblox-brain/roblox-gui

> Use when building or fixing Roblox menus, HUDs, shops, dialogs, or UI that must work on phones, tablets, desktop and console.

Type: skill | Category: [[categories/cat-src-roblox-brain|src-roblox-brain]] | Source: [[sources/src-roblox-brain|roblox-brain]] | License: MIT
Repo file: `sources/roblox-brain/skills/gameplay/roblox-gui/SKILL.md` (extra files, if any, sit beside it in the repo)

---
# roblox gui

## When to Load

HUDs, menus, shops, dialogs, world UI, and layout bugs on phone, tablet, desktop or TV.

## Quick Reference

- Mobile first: design on the smallest landscape phone with touch controls, then grow (full.md §11).
- Reserve top bar, thumbstick, jump, chat; interactive UI in `CoreUISafeInsets`; place by measured `AbsolutePosition`/`AbsoluteSize`.
- Check every element pair that can show together; reflow, don't shrink.
- Gamepad: one `SelectedObject` owner, `SelectionGroup` bounds, restored focus, layered Back (§8).
- Console: TV-safe area, `ViewportDisplaySize`, no chat window.
- Layouts own repeated layout; UI shows server state; a button is not an authority boundary.
- Reactive UI: per-screen cleanup; repeat open/close to test leaks. Loading UI in `ReplicatedFirst`.
- TextBox submit, grids, truncation, RichText safety, deprecated APIs: full.md.

> Details: [references/full.md](references/full.md)
