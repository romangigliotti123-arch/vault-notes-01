---
name: rbx-ui-mockup
description: "Design-first Roblox UI: design buttons and screens, export the spec, build, compare (mockup first; building a ScreenGui straight in Luau is rbx-ui)."
argument-hint: "[game slug or project folder]"
---

# rbx-ui-mockup

Code comments: none by default (see rbx-luau, Comments).

Design-first UI: no screen or button is built before it exists as a design with exact numbers. Called by `rbx-art` (step 4b) and `rbx-ui` (step 0). It NEVER asks the user anything mid-turn: it reads the stored preference and keeps going. Stdlib tools in `scripts/` (`py` or `python3 -I`), no network, no installs, no local image generation.

If `Games/<slug>/design-pack/ui.md` exists, the picked screens there (Figma frames or HTML versions) are the design: refine them into the spec, never redesign from scratch; new or changed screens go through `rbx-design-pack` (3 versions, pick). The Figma check below is the same one the design pack makes.

## Steps
1. Mode: `python -I .rbx/claude-kit/tools/ui_pref.py get` prints `off` (default, also when unset) = AUTOMATIC DESIGN-FIRST, or `on` = MANUAL Nano Banana 2.1 package (step 3b).
2. Figma check, once per game: look in your tool list (ToolSearch "figma" when tools are deferred) for a connector or MCP tool whose name contains `figma`, then run `python -I .rbx/claude-kit/tools/ui_pref.py figma --tools "<those names, or none>" --game Games/<slug>`. Show the ONE line it prints (nothing is printed on later calls for the same game). Not connected = say so in that line and continue with the local sheet; connected = use it ([cold:rbx-ui-mockup/figma.md] read when Figma is connected or the user asks how to connect it). Never ask for, store or enter a Figma token, never install or log in.
3. Brief: write `ui/brief.json` (`scripts/ui_design.py init` shows the schema): palette and fonts from `art-direction.md` (real Roblox font names only), every button variant, every screen with element rectangles as fractions and the exact copy. Element names are the Roblox Instance names. Assumptions go in `ui/brief.md`, not questions.
3a. Automatic (mode off): `python -I scripts/ui_design.py all ui/brief.json --out ui/design` = validate, `index.html` design sheet (tokens, each button in default/hover/pressed/disabled, one layout per screen as phone 844x390 + desktop 1920x1080 frames), PNGs when a headless Chrome/Edge is already installed (else HTML only: say so and tell the user to open `ui/design/index.html`), and `spec.json` exported from the browser layout (`source: browser`, else `model`). Fix every ERROR; read the WARN lines (touch target, text size, contrast, panel share, safe zones) and fix or justify.
3b. Manual (mode on): `python -I scripts/ui_design.py all ...` as above (the sheet is the layout reference), then `python -I scripts/ui_mock.py package --brief ui/brief.json --project . --design ui/design` builds `ui-mockup/` (prompts, references to upload, numbered Gemini-website steps, checklist). Tell the user once: "Follow ui-mockup/INSTRUCTIONS.md; drop the images in ui-mockup/results/". Then add: "when you have your Gemini image, drop it in the game folder and say: prototype this mockup" (`rbx-ui-prototype` turns it into a clickable HTML page to open in a browser). Do NOT wait: build from the spec, run `ui_mock.py status .` before each screen and at the end, and use arrived images for style only (colours, icon style); the spec rectangles and copy always win. [cold:rbx-ui-mockup/manual.md] read when the user asks about the manual mode or its Gemini steps.
4. Build from the spec only, through the StyleKit (`UI.panel/label/button/...`): `python -I scripts/ui_spec.py roblox ui/design/spec.json --frame <Screen>.phone` lists AnchorPoint/Position/Size scale, UICorner, UIStroke, font and text per element. Instance names = spec names; text strings from the spec, never from an image; Scale not Offset; states from `tokens.buttons`.
5. Compare (part of the `rbx-visual` rounds, cap 3 shared, no extra rounds): run `rbx-visual/scripts/ui_overlap.luau`; keep its `UI-RECTS <viewport> [json]` lines (built AbsolutePosition/AbsoluteSize per element) in a file, then `python -I scripts/ui_compare.py gate --spec ui/design/spec.json --frame <Screen>.phone --built <that file> [--design ui/design/png/<Screen>.phone.png --shot <screenshot>] --mode auto|figma|manual --write Games/<slug>`. Tolerance 0.02 of the frame; missing, off or text-different elements go back to step 4; luminance/edge/palette region flags are advisory leads, never a verdict. Remaining diffs go to `polish-backlog.md`.
6. Gate line in your report, ADVISORY until calibrated: `UI design: done (auto|figma|manual) / skipped: <reason>` (`python -I scripts/ui_compare.py line Games/<slug>` prints it). Allowed skips: no UI in this change, hotfix, user declined: record with `ui_compare.py skip --reason "..." --mode auto --write Games/<slug>`. `skipped` never blocks; the final status adds "(UI not checked against a design)".
7. Assets: prefer StyleKit shapes. Art files, names and the manual or Open Cloud upload steps: `scripts/ui_assets.py steps` [cold:rbx-ui-mockup/assets.md] read before any UI art file is made or imported. Nothing is uploaded without the user's yes.

## Rules
- Mockup images are style hints only; no copying other games' UI; no real brands in prompts or references; text and sizes come from the spec.
- Automatic image generation (Gemini through `rbx-thumbnail/scripts/gen_image.py`, the only client) is a quiet advanced path: [cold:rbx-ui-mockup/advanced.md] read only when the user explicitly asks for generated UI images.
- Pipeline detail, spec schema, failure modes: [cold:rbx-ui-mockup/pipeline.md] read when a step fails or the spec or compare output is unclear.
