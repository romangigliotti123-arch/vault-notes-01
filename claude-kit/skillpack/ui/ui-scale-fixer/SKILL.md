---
name: ui-scale-fixer
description: "Convert Offset-based Roblox UI to Scale with size and aspect-ratio constraints, then sweep the result across phone, tablet and desktop viewports; output is per-object property changes and a sweep report. Use after mobile-ui-audit finds Offset-only sizes."
category: ui
tags: ui, scale, offset, constraints, uiaspectratioconstraint, uisizeconstraint, responsive, mobile, aspect ratio
kb: Roblox/roblox-kb/ui-ux-design.md, Roblox/roblox-kb/cross-platform-and-console.md
related: mobile-ui-audit, roblox-ui-responsive, safe-area-checker, localization-ready-checker, hud-layout-planner
---

# ui-scale-fixer

The fix-it companion to `mobile-ui-audit`: it takes objects sized in pixels at the designer's screen and makes them scale, while keeping their proportions and sane pixel limits. Pure maths is in `scripts/ScaleMath.luau` (Lune-tested); the Instance edits are small `execute_luau` steps.

## When to use
After an audit lists "Offset-only size" or "fixed width over 300 px"; when UI looks right in Studio and wrong on a phone. Not for choosing the layout (`hud-layout-planner`) or for notch handling (`safe-area-checker`).

## Inputs (max 2)
1. Which ScreenGuis (default: those the audit flagged). 2. The reference viewport the Offsets were designed at (default 1920x1080; if unknown, say so and use the Studio viewport size, labelled as a guess).

## Procedure
1. List flagged objects (audit output or a scan). Skip children of `UIListLayout`/`UIGridLayout`: the layout owns their Position/Size (vault); fix the layout's cell/padding instead.
2. For each remaining object compute `ScaleMath.convert(design, ref, { interactive = isButton })`. It returns scale X/Y, an aspect ratio, a max pixel size (the design size) and a touch floor for interactive objects.
3. Apply: set `Size` to the scale values; add `UIAspectRatioConstraint` (aspect) and `UISizeConstraint` (min/max) as DIRECT children of the object (vault: constraints must be direct children). Anchor with `AnchorPoint` and 0.5 anchors for centre or edge pinning.
4. Text: prefer `AutomaticSize` and a fixed `TextSize` for body text; use `TextScaled` only with a `UITextSizeConstraint` (min 14, max design size).
5. Sweep: `ScaleMath.sweep(plan, viewports)` over the real emulator sizes (the built-in list is illustrative). Stop condition: no "exceeds the viewport" and no "under the touch floor" for interactive objects.
6. Re-run the `mobile-ui-audit` scan and compare counts; screenshot at least phone landscape and portrait.

## Studio MCP path
`list_roblox_studios` -> `search_game_tree` -> `inspect_instance` (read Size) -> `execute_luau` (Edit) to write Size/constraints per object -> `start_stop_play` (Client) to re-run the audit scan on PlayerGui -> `screen_capture`. Switching Device Emulator size is a manual step for the owner.

## Fallback
Edit Rojo `.model.json`/script code: replace `UDim2.fromOffset(w, h)` with `UDim2.fromScale(w/refW, h/refH)` plus the constraints; everything visual stays `untested`.

## Evidence
`Roblox/roblox-kb/ui-ux-design.md` (size and position in Scale, not Offset; keep aspect ratio and cap or floor pixel size with constraints; keep constraints as direct children; let layouts own positioning; design for the real device aspect ratio). `Roblox/roblox-kb/cross-platform-and-console.md` (mobile-first: most sessions are on mobile). The 44 px floor is a touch-target heuristic; reference viewports are illustrative.

## Output
```
SCALE FIX <ScreenGui>   ref 1920x1080
Path | before | after (scale) | aspect | min/max px
sweep: N issues -> ...      audit counts: before X -> after Y
```

## Acceptance checks
- [ ] No layout-owned child had Position/Size changed.
- [ ] Every constraint is a direct child of its object.
- [ ] `ScaleMath.sweep` clean for the listed viewports; viewports named.
- [ ] Audit scan counts attached before and after.
- [ ] Lune test passes (`ScaleMath.test.luau`, 5 tests).

## Pitfalls
Converting with the wrong reference viewport (everything is slightly off). Scaling a button down until its hit area is tiny. Putting `UIAspectRatioConstraint` on a parent frame instead of the object. Using `TextScaled` without limits.

## Related
`mobile-ui-audit`, `roblox-ui-responsive`, `safe-area-checker`, `localization-ready-checker`, `hud-layout-planner`.
