---
name: mobile-ui-audit
description: "Audit every screen of a Roblox game's UI for phones: static scan for Offset-only sizing, small touch targets, tiny text, unconstrained scaled text and images, safe-area risks and non-scaling scroll frames, then screenshot passes at several aspect ratios, with ranked fixes. Use before launch and after any UI change; most Roblox players are on phones."
category: ui
tags: ui, mobile, phone, touch, scale, offset, aspect ratio, safe area, text size, responsive, screengui, audit
kb: Roblox/roblox-kb/ui-ux-design.md, Roblox/roblox-kb/cross-platform-and-console.md, Roblox/roblox-kb/first-session-onboarding.md, Roblox/roblox-kb/localization-and-international.md
related: ui-scale-fixer, safe-area-checker, roblox-ui-responsive, gamepad-ui-navigator, accessibility-checker, localization-ready-checker, hud-layout-planner, first-minute-designer
---

# mobile-ui-audit

The kit skill `roblox-ui-responsive` teaches how to build responsive UI. This skill is the audit: find what is already broken, rank it, and fix or hand off. Roblox skews young and mobile; a UI that works only at the Studio default size is a launch bug.

## When to use
Before launch, after adding a screen, when reviews say "can't press the button". Not for: visual design taste (`ui-kit-consistency-checker`), controller navigation (`gamepad-ui-navigator`).

## Inputs (max 2)
1. Which screens (default: all ScreenGuis in StarterGui + any created at runtime, listed from code). 2. Target devices (default: small phone portrait and landscape, large phone, tablet, 16:9 desktop).

## Procedure
1. Static scan: run `scripts/ui_audit.luau` (Edit datamodel scans StarterGui; a Client playtest scans PlayerGui, which includes runtime UI). Save the output. It flags: Offset-only sizes, fixed widths over 300 px, touch targets under 44 px (an industry heuristic, not a Roblox number), TextSize under 14, `TextScaled` without `UITextSizeConstraint`, scaled images without `UIAspectRatioConstraint`, scroll frames with a layout but fixed canvas, `ScreenInsets = None`.
2. Layout rules to apply (vault ui-ux-design): size and position in Scale, Offset only for pixel-exact needs; aspect ratio and min/max constraints as DIRECT children of the object they constrain; do not set Position/Size on children of a UIGridLayout/UIListLayout (the layout owns them); use AutomaticSize/wrapping for variable and localised text; scroll frames with automatic canvas and relative sizing so children do not grow with the canvas; the real device aspect ratio matters more than Studio's preview.
3. Visual pass: for each screen, view it at several device emulations (Studio's Device Emulator: a small phone, a large phone, a tablet; portrait and landscape). Switching the emulated device is a manual Studio action, so ask the owner to switch and then take `screen_capture` of each (Studio MCP), or have them send screenshots. State exactly which sizes were viewed; if none, the report is "static only".
4. Check by hand-list: nothing important under notch/home-bar/rounded corners (core UI safe insets), thumb zones for primary actions (bottom corners), text readable at arm's length, popups close with a visible target, no screen covers the whole view without a close, no tiny close buttons.
5. Rank issues: BLOCKER (cannot press / cannot read core UI on a phone), MAJOR (clipped or overlapping), MINOR (looks off). Fix BLOCKER and MAJOR; for each give the exact property change.
6. Apply fixes (one screen at a time) and re-run the scan; compare counts.
7. Hand-offs: Offset-to-Scale conversion at scale `ui-scale-fixer`; localisation text overflow `localization-ready-checker`.

## Studio MCP path
`list_roblox_studios` -> `search_game_tree` (StarterGui) -> `execute_luau` (Edit) with `scripts/ui_audit.luau` -> property fixes via `execute_luau` -> `start_stop_play` + `execute_luau` (Client) to re-run the scan on PlayerGui -> `screen_capture`. Device emulation is a Studio UI setting: ask the owner.

## Fallback
Paste the script into the command bar; or review UI code/Rojo files for Offset usage with grep (`UDim2.fromOffset`, `UDim2.new(0, `). Visual claims are `untested` without screenshots.

## Evidence
`Roblox/roblox-kb/ui-ux-design.md` (Scale not Offset; real device aspect ratio; constraints as direct children; layouts own positioning; scroll frames; AutomaticSize for localised text), `Roblox/roblox-kb/cross-platform-and-console.md`, `Roblox/roblox-kb/first-session-onboarding.md` (UI clarity in the first minute), `Roblox/roblox-kb/localization-and-international.md`. The 44 px and 14 px thresholds are heuristics from general mobile UI practice, labelled as such in the script.

## Output
```
MOBILE UI AUDIT <game> <date>  screens N
[BLOCKER] Shop/Close: 28x28 px target -> size 0.12 scale with UIAspectRatioConstraint + min 44
[MAJOR] ... (ranked list, each with path and exact fix)
Viewed sizes: <list or "static only">   Scan before -> after: <counts>
```

## Acceptance checks
- [ ] Script output attached for before and after; counts match the report.
- [ ] Every BLOCKER/MAJOR has a path and an exact property change.
- [ ] The report says which device sizes were actually viewed, or "static only".
- [ ] Runtime-created UI was included (Client playtest scan or code review).
- [ ] No fix converted a layout-owned child's Position/Size.
- [ ] Sizes use Scale (Offset only for fixed padding or icons) with `UISizeConstraint` caps; scaled text sits in a Frame with `MinTextSize` 9 or higher; custom mobile buttons sit about 60 px from the screen sides and out of the bottom corners (mixed; Roblox/roblox-kb/_tools/DECISION-RULES.md, ui-ux-design).

## Pitfalls
Auditing only StarterGui and missing UI built in scripts. Trusting AbsoluteSize in Edit mode (it reflects the editor viewport). Using TextScaled everywhere (extreme sizes). Fixing sizes but not the touch target's hit area (a scaled-down image button with tiny hit area). Treating the heuristics as hard rules.

## Related
`roblox-ui-responsive`, `ui-scale-fixer`, `safe-area-checker`, `accessibility-checker`, `localization-ready-checker`, `hud-layout-planner`.
