---
name: rbx-ui-prototype
description: "Turn a UI mockup image (Gemini, Nano Banana, screenshot) into ONE clickable HTML prototype to open in a browser: working buttons, animations, screen navigation, fake coins, device switcher, plus a Roblox handoff. Use for 'prototype this mockup'. The real ScreenGui build is rbx-ui."
argument-hint: "[game slug] [image path(s)]"
---

# rbx-ui-prototype

Code comments: none by default (see rbx-luau, Comments).

A clickable stand-in for the game UI, made from a mockup picture, so the user can feel the buttons before anything is built in Studio. It is NEVER the game and never says so. One self-contained HTML file, no network, no installs, no server, no CDN. Called after `rbx-ui-mockup` mode on (Gemini image) or when the user drops any UI picture in the game folder and says "prototype this mockup".

## Steps
1. Input: image path(s) of screens of the same game UI (Read shows images), or a pasted screenshot; the game slug. Output folder `Games/<slug>/ui/prototype/`, or `./ui-prototype/` when there is no game. No image = ask once for it (or point to `rbx-ui-mockup` to get one made).
2. Read every image and write `ui/prototype/spec.json` in the `rbx-ui-mockup` brief schema (`ui_design.py init` shows it): palette, real Roblox font names, corner and stroke, buttons, screens, elements with rects as fractions (type panel, label, button, bar, chip, icon, grid). Add a `prototype` key: `source` (image names), `rect_source`, `placeholder_art`, `not_buildable`. Copy and text come from the image; anything not readable is a guess and goes in the fidelity panel.
3. Build `index.html` by copying the structure of `examples/index.html` (read it first; it is the template): sections 1-11 in order (tokens, page chrome, game UI CSS in em from one scale, DATA, VIEWS, one `render`, ACTIONS via `data-act="name:arg"`, press feel, keyboard, devices and safe areas, loop). Edit the data arrays and views, keep the rest: the page layout (top bar with device switcher, rotate button, safe-area toggle, Reset and Notes; centred device frame; notes drawer on the right) is the part the user likes and is not redesigned. Rules:
   - Real behaviour: hover, press (0.08 s to 0.92, release 0.15 s overshoot to 1.08), disabled, navigation between EVERY screen in the images (back, tabs, modals), fake state (coins/gems count up, inventory, equip, locked/unlocked, toasts, bars, cooldown ring), keyboard keys, device switcher with three devices (Phone, Tablet, Desktop) plus a rotate button (key R) that turns Phone and Tablet between portrait and landscape (Desktop: rotate disabled) and shows the current device and orientation ("Phone - Landscape"); the frame swaps width and height with a 0.25-0.3 s transition (phone 390x844 <-> 844x390, tablet 820x1180 <-> 1180x820), the choice lives in page state (not localStorage), every screen reflows per orientation (landscape: shop 4 columns, home and bag two columns, no overlap) and the safe-area overlay changes per orientation (notch and home indicator in portrait, side cutouts in landscape); `id="constraints"` badge list, `id="notbuildable"` note, `id="fidelity"` panel (matched vs guessed), visible banner "UI PROTOTYPE - not the game".
   - Only what Roblox can build: UICorner, UIStroke (inset 0-blur box-shadow), UIGradient (linear only), UIListLayout, UIGridLayout (fixed columns), UIAspectRatioConstraint, UIPadding, UIScale tweens. Hard offset shadows are a second Frame. NEVER blur, backdrop-filter, filter, blend modes, clip-path, masks, radial or conic gradients, soft shadows; if the image needs one, use the closest Roblox substitute and list it in the notbuildable note (the checker fails an unnamed one).
   - Art: emoji, CSS or SVG shapes as placeholders; say so in the fidelity panel. No fonts, images or scripts from the network. Data-driven JS, no framework, about 700 lines for 3 screens.
4. Write `ui/prototype/handoff.md` like `examples/handoff.md`: every component to a Roblox instance tree (Frame/ImageButton/UICorner/UIStroke/UIGradient/UIListLayout, Scale values, em to px rule, tweens), screens, behaviours to wire, the not-buildable substitutes, ending with the next step `/rbx-ui`.
5. Check: `python -I scripts/proto_check.py Games/<slug>/ui/prototype` prints PASS/FAIL lines. Fix every FAIL and rerun before telling the user it is done.
6. Tell the user (Reply format, bold footer): the file path, how to open it (double-click `index.html`; `start` on Windows, `open` on Mac, `xdg-open` on Linux; with the Artifact or a preview tool say "I can also open it here"), what the fidelity panel guessed, and offer to iterate ("change X": edit the data or the view, rerun the check). Next step is `/rbx-ui` (it builds the real ScreenGui from `spec.json` and `handoff.md`); run `rbx-visual` only after that real build. The prototype is not the game and is not visual-gate evidence.

## Rules
- Mockup images are style hints only; no copying other games' UI; no real brands.
- Never write into the real game place or Studio from this skill; it only writes under `ui/prototype/`.
- Changes the user asks for later: edit `index.html` and `spec.json` together, keep `handoff.md` in step, rerun the check.
