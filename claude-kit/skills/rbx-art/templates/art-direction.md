# Art direction: {{slug}}   (AI-to-AI; every builder and every visual-QA round reads this file; change it only with a line in decisions.md)

## 1. Look in one line
{{one sentence: mood + shape language + reference feel, e.g. "bright chunky cartoon harbour, rounded shapes, warm light, saturated accents". Patterns only, never copy a game}}

## 2. Palette (checked with `palette-picker`; max 5 roles + 2 accents)
| Role | Hex | Used for |
|---|---|---|
| background / deep | | screen dimmer, shadows |
| panel | | HUD panels |
| panel alt | | rows, inactive buttons |
| accent (focal) | | primary action, key numbers |
| accent 2 | | highlights, progress |
| good / bad | | success / error only |
| world ground / water / foliage / props | | world palette: 3-4 hues, one dominant |
Contrast pairs checked (text on panel >= 4.5:1): {{result}}

## 3. UI style kit (values live ONLY in `StyleKit/Theme.luau`; this table mirrors it)
Font display / body: | Text sizes (title/heading/body/small px at 1x, min 14): | Corner radius: | Stroke thickness + colour: | Padding / gap: | Panel depth (gradient/shadow rule): | Icon style: {{flat | outlined | 3D chunky}}, one set only | Button states: idle / hover (scale 1.05) / press (0.94) / disabled
Component set (build nothing else): panel, label, button (primary/secondary), stat, bar, popup, toast. Anything new is added to `UI.luau` first, then used.

## 4. UI layout contract (checked by `ui_overlap` at phone 844x390, tablet 1180x820, desktop 1920x1080)
- Regions: TopLeft = currencies, TopCenter = goal/wave + toasts, TopRight = menu buttons, BottomCenter = hotbar/action, centre = gameplay + popups only. Bottom-left/right stay free (thumbstick, jump). Roblox chat and top bar are never covered.
- Per element: Scale sizing + AnchorPoint + `UIAspectRatioConstraint`/`UISizeConstraint`; `ScreenInsets = CoreUISafeInsets`; slots stack with `UIListLayout` (never place two panels at hand-picked positions near each other).
- One popup at a time (queue), banners and tutorial hints use the same queue; ZIndexBehavior Sibling; DisplayOrder only from `Theme.layer`.
- Banned: Offset positions for HUD, text over text, hint text on top of a panel, overlay text without a background or stroke, panels over 35% of the screen.

## 5. World and model rules
- Hero objects ({{list: what the player sees/collects/rides/fights most}}) are NEVER a single primitive and NEVER a flat sprite in 3D: each is a multi-part or mesh model (target >= 8 parts or a real mesh) with 3+ materials, rounded/bevelled forms (use meshes, WedgeParts, cylinders/spheres combined, `generate_mesh`/`generate_procedural_model`, or a Creator Store model found with `search_asset` and license-checked), details (eyes, fins, trim, glow), a contact shadow, and an idle animation (bob, tail, spin).
- Sourcing order: (1) kit `Assets/` models, (2) `search_asset`/`insert_asset` (keep returned ids; never type ids from memory), (3) procedural mesh, (4) hand-built composed model. A bare block is allowed only for greybox and never reaches a screenshot.
- Ground, paths, walls: material per surface type (not default Plastic), colour from section 2, vary size/rotation/colour of repeated tiles and props, scatter 3+ prop types, round terrain or water instead of flat slabs. Keep the whole scene to the palette; reserve high contrast for the focal object.
- Scale: character about 5-6.5 studs; doorways/paths >= 10 studs; objects sized to the character, not the grid.
- Render budget: <= 20k triangles per mesh, one material per mesh, particle rate caps from `particle-effect-planner`.

## 6. Lighting and atmosphere (`lighting-preset-picker`, applied once, in the project, not by hand each run)
Preset: {{mood}} | ClockTime | Brightness | Ambient / OutdoorAmbient | Atmosphere (density, haze, colour) | Sky | ColorCorrection (brightness, contrast, saturation, tint) | Bloom | SunRays | DepthOfField | Water colour/transparency | Shadows on/off for mobile.
Genre preset (`rbx-lighting`: obby | simulator | tower_defense | horror | cartoony | open_world | sci_fi): {{genre_preset}} | time of day (day | golden | night): {{time_of_day}} | phone-first or both: {{platform}}. Applied EARLY with `LightingKit.apply`; the lighting gate checks the scene against this line and the palette above.

## 7. Juice list (one row per key event; each row needs >= 2 of particle / tween / sound / UI reaction; implemented with `StyleKit/Juice.luau`)
| Event | Particle | Tween / motion | Sound (name in Theme.sounds) | UI reaction |
|---|---|---|---|---|
| collect / catch | | | | |
| reward / level-up | | | | |
| hit / damage | | | | |
| purchase / unlock | | | | |
| error / denied | | | | |
| spawn / appear | | | | |
| panel open / close | | | | |
| first action, first reward (first 30 s) | | | | |

## 8. First 30 seconds screen contract
Spawn view shows: {{title or goal text}} / {{HUD slots used}} / {{focal object}} / first action cue. No debug text, no default baseplate, no popup over the first action.

## 9. Definition of done for visuals
`rbx-visual` gate PASS (V1-V7 >= 7, zero layout findings at three sizes, >= 6 screenshots). Until then the status is "playable prototype, visuals not polished".
