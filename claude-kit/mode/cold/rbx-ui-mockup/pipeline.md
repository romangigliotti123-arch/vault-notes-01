<!-- cold: rbx-ui-mockup/pipeline.md | read when: a step of rbx-ui-mockup fails, or the spec, the design sheet or the compare output is unclear. -->

# Pipeline detail (rbx-ui-mockup)

brief -> design sheet (HTML/CSS, real pixel frames) -> spec.json (browser layout, scale values) -> build through StyleKit -> compare (numeric rectangles + advisory image flags) -> fix (cap 3, shared with rbx-visual) -> assets.

## Why a local HTML/CSS sheet
No account, no key, no install: any Chrome/Edge/Chromium already on the machine renders it. The SAME file gives the exact spec: the page script writes getBoundingClientRect and computed style into the DOM and into a console marker; `--dump-dom` with a log file carries it out, because Chrome/Edge on Windows hand the page to a detached process and leave stdout empty (the tool polls the log, timeout 40 s). Exact numbers beat reading an image with vision. No browser found: HTML only, `spec.json` falls back to `source: model` (the rectangles the layout declares; the sheet is built from those percentages, so they agree within 0.1 px: `ui_spec.py check ui/design` proves it when a browser exists).

## Brief fields
`style.palette` (3-5 colours, max 8), `style.fonts` (real Roblox Enum.Font names: Legacy, Arial, SourceSans*, Gotham*, BuilderSans*, FredokaOne, Nunito, LuckiestGuy, Michroma, Jura, SciFi, Roboto, Ubuntu, Oswald, ...; the validator knows the full list read 2026-11-05), `corner` 0..0.5 of the smaller side, `stroke` px, `spacing` scale. `buttons[]` variants (fill, text_color, w, h); the sheet draws default / hover (lighter) / pressed (darker, 2 px down) / disabled (desaturated). `screens[].elements[]`: type panel|label|button|bar|chip|icon|grid, `rect [left, top, width, height]` as 0..1 fractions of the frame, `rect_desktop` override, `aspect` (UIAspectRatioConstraint behaviour), `parent`, `text`, `font`, `variant`, `value`, `gradient`, `grid {cols, rows, gap}` (cells are named `<Name>Cell<n>`).

## Frames
phone 844x390, tablet 1180x820, desktop 1920x1080 (the viewports rbx-visual measures). Guides drawn but not exported: Roblox top bar 36 px, thumbstick and jump corners (18% wide, 40% tall).

## Spec (ui_spec.py export)
`{version, game, source browser|model, tokens {palette, fonts, corner, stroke, spacing, buttons{variant{state{fill,text_color,offset_px}}}}, frames [{id "<Screen>.<kind>", kind, screen, w, h, elements [{name, type, frame, parent, state, variant, rect [l,t,w,h] scale, px [x,y,w,h], fill, stroke {px,color}, corner, text, font, font_px, color}]}]}`. Validation: scale 0..1, Roblox-safe unique names, real fonts, touch target >= 44 px at phone height 390 (about 11%), text >= 14 px, contrast >= 4.5:1, panel <= 35% of the frame, sibling overlap.

## Compare (ui_compare.py)
Built side = `UI-RECTS <viewport> [json]` lines printed by `rbx-visual/scripts/ui_overlap.luau` (path, kind, x, y, w, h, text per visible element, in viewport pixels). Elements match by Instance name (last path segment). Per element dx/dy/dw/dh as a fraction of the frame; tolerance 0.02; text must equal the spec; missing and extra elements are listed. Image layer (PNG only, 8-bit): 48x24 luminance grid inside the union of spec rectangles, mean abs diff, 6x3 heat grid, edge-map Pearson correlation, palette distance (top 5 colours), per-element region flags. Thresholds (edge >= 0.6, mad < 0.12, palette < 0.12, region 0.18) are untested guesses: advisory. The gate record `Games/<slug>/ui-design-qa/gate.json` is discovered by rbx-bench scorecard like any gate (weight 10, never required).

## Failure modes
Missing browser (HTML only; tell the user to open the file); browser launches but returns nothing (timeout, then model fallback); fonts not installed on the machine (generic sans fallback: sizes stay exact, glyph widths may differ a little); built UI not named like the spec (everything shows as missing: rename the Instances); a ui_overlap built before this change has no UI-RECTS lines (rebuild with `python scripts/build_inline.py`); the preview host places GUIs below the top bar inset when `IgnoreGuiInset` is false: positions are in full-viewport pixels.

