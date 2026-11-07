# Handoff: Moonlit Bakery bar prototype -> Roblox ScreenGui

This prototype (`index.html`) is a browser mock-up and the quality bar for every future vault UI. It is not the game. Build the real UI with `/rbx-ui` from this file, `spec.json` and the guide (`[cold:rbx-ui/ui-craft-guide.md]`); run `rbx-visual` only after the real build. Numbers marked (tuned) are feel heuristics, not measured.

## Global
- `ScreenGui` "MoonlitBakery": `ResetOnSpawn=false`, `ScreenInsets=DeviceSafeInsets`, `ZIndexBehavior=Sibling`. DisplayOrder: screens 1, modals 5, reward stage 8, toasts 9, fx 10.
- Root `Frame` "Root" (Size 1,0,1,0) with one `UIScale`: `Scale = clamp(min(ViewportSize.X, ViewportSize.Y) / 390, 0.8, 1.75)`. The prototype sizes everything in em; 1 em = 14.4 px at phone scale (tablet 17, desktop 17.8). Use Scale for placement; Offset only for UIStroke thickness and corner radii (em x 14.4).
- Fonts: titles, buttons, numbers `FredokaOne`; body `BuilderSansBold` (or GothamMedium). Text outline = `UIStroke` (ApplyStrokeMode Contextual, Thickness 2-3, dark shade of the surface) plus a duplicate `TextLabel` offset (0,2) behind. Counters: fixed minimum width, right aligned.
- Palette (spec.json): night 1D1B4C, panel 3B3694, cream FFF3D6, honey FFB81F, mint 2FC455, berry F03E5B, orchid 9A4DFF. Rarity: common AAB4C8, uncommon 5FD35F, rare 3FA7FF, epic B45CFF, legendary FFB81F (one table in a ModuleScript).

## Button (the core component) and its states
```
Btn (TextButton, AutoButtonColor=false, BackgroundTransparency=1, AnchorPoint .5,.5)   child UIScale
 Lip   Frame  Position y +0.32em, UICorner 0.95em, colour = lip shade                          ZIndex 1
 Face  Frame  UICorner 0.95em, UIStroke 0.17em (outline shade), UIGradient Rotation 90 (top light -> bottom base)   ZIndex 2
  Gloss Frame top 38%, inset .3em, UICorner, white, UIGradient Transparency 0.4 -> 0.9
  Shine Frame Rotation 20, width 20%, white UIGradient (0 -> .3 -> 0 transparency); Face ClipsDescendants=true
  Row   Frame UIListLayout Horizontal Padding .4em Center: Icon ImageLabel (UIAspectRatioConstraint 1) + Label TextLabel + LabelShadow
 Badge Frame (red circle 1.55em, UIStroke white .14em) top-right, UIScale pops
```
| Variant | Face top / bottom | Lip | Outline |
|---|---|---|---|
| Primary | FFD45A / FFA81F | C46A0A | 7A3B06 |
| Secondary | 8FB8FF / 4D7BE6 | 2B4CAC | 1B2C78 |
| Positive | 86F5A4 / 2FC455 | 1A8A37 | 0E5A22 |
| Danger | FF8FA0 / F03E5B | A82040 | 6A1028 |
| Premium | DCA8FF / 9A4DFF | 6528B8 | 3D1580 |
Sizes (height at phone scale): s 44, m 52, l 63 px (min touch target 44 px including the lip).
| Behaviour | Roblox |
|---|---|
| press | `InputBegan`: UIScale 1 -> 0.94, `TweenInfo(0.07, Quad, Out)`; Lip shrinks to 0.08em and Face moves down 0.24em |
| release | UIScale 0.94 -> 1, `TweenInfo(0.18, Back, Out)` (prototype keys 1 -> 1.06 -> 1); click Sound |
| hover (desktop) | `MouseEnter`: Face lifts 0.12em, +8% light, `TweenInfo(0.12, Quad, Out)`; skip on touch |
| idle CTA | looping `TweenInfo(0.8, Sine, InOut, -1, true)` UIScale 1 -> 1.04 on a wrapper; shine Position loop every 3.6 s, `TweenInfo(0.6, Quad, InOut)` |
| disabled | grey gradient BCC0D2 / 8D92A9, text EC EE F7, no loops; tap: wobble (Position +/-0.4em, 0.28 s) + toast with the reason + `nope` cue |
| loading / success | spinner ImageLabel Rotation loop `TweenInfo(0.8, Linear, -1)`; then tick (ImageLabel scale 0 -> 1 Back Out 0.35 s), face turns green, restore after 1.1 s |
| ripple | ImageLabel ring, Size 0.6em -> 7x, Transparency 0 -> 1, `TweenInfo(0.5, Quad, Out)` |
| hold-to-confirm | fill 0 -> 1 over 0.9 s linear while held, drain 0.2 s on early release, completion pop + haptic |

## Other components
| HTML | Roblox tree | Values |
|---|---|---|
| currency pill | `Frame` (UICorner 1, UIStroke .14em, gradient 3B3694 -> 221F5E) + overlapping icon `ImageLabel` + count `TextLabel` + green plus `TextButton` | count-up: tween a `NumberValue` 0.6-0.9 s Quad Out, tick cue every 3-5 units; bump UIScale 1.14 for 0.3 s |
| level badge | star `ImageLabel` + number label | |
| XP / progress bar | track `Frame` ClipsDescendants + UICorner 1; fill `Frame` (same corner) slid by Position, `TweenInfo(0.5, Quint, Out)`; gloss strip; stripes = tiled ImageLabel scrolled `TweenInfo(1, Linear, -1)` | |
| panel | `Frame` UICorner 1.1em + UIStroke .2em + lip Frame + inset gradient | modal header band = honey Frame with title; close X = square red Button top-right, overlapping the corner |
| card | `Frame` UICorner 1em, UIStroke .17em (rarity dark), inner UIStroke .13em (rarity colour), art well Frame with UIGradient, ribbon, quantity badge | rare+: glow = 2 transparent UIStroke Frames pulsing Transparency .85 <-> .66, 1.6 s Sine; epic+: shimmer Frame loop 2.4 s |
| tabs | segmented `Frame`; selected indicator Frame slides, `TweenInfo(0.28, Back, Out)` | content: old fades 0.1 s, new slides 8% in 0.24 s Quint Out |
| nav (bottom or rail) | `Frame` UIListLayout Horizontal (portrait) or Vertical (landscape rail 5em wide) | selected: icon lifts 0.1em, scale 1.12 Back Out |
| toggle | track 3.8x2.1em + knob, `TweenInfo(0.18, Back, Out)` | track colour 9A8F80 -> mint |
| slider / stepper / segmented / checkbox | as in index.html, tick draw `0.2 s` | |
| skeleton | grey Frames + moving light bar, `TweenInfo(1.2, Linear, -1)` | shown 0.56 s on first visit of each shop tab |

## Screens and motion
| Event | Roblox | TweenInfo |
|---|---|---|
| card entrance | each card: Position +1.1em, scale .86, transparency 1 -> rest | `(0.38, Back, Out)`, delay 0.05 s x index |
| screen push | new body: Position +8%, scale .98, fade -> rest; old: -6%, fade out | `(0.30, Quint, Out)` / `(0.24, Quad, In)` |
| modal open / close | dim 0 -> 0.64, panel UIScale .8 -> 1 / 1 -> .92 | `(0.25, Back, Out)` / `(0.15, Quad, In)` |
| toast | Position y -160% -> 0, hold 2.2 s, out | `(0.3, Back, Out)` / `(0.25, Quad, In)`; one at a time |
| currency fly | 8-14 icon frames along a quadratic Bezier (control point above), scale 1 -> .6, then bump counter | `(0.78, Quad, In)` per icon, delay 0.055 s x index |
| chest sequence | shake: Rotation +/-9 deg ramp + scale 1 -> 1.12 over 0.85 s (6-8 swings); flash 0.38 s; burst 24-46 particles; item card scale 2.3 -> 1 `(0.5, Back, Out)`; rarity text scale 3 -> 1 `(0.4, Back, Out)` | see index.html section 10 |
| screen shake | Root Position decaying amplitude 6-14 px, 7 steps, 0.3-0.42 s | big rewards only |
| level up | fireworks at the bar end (4 bursts, 150 ms apart), flash, rays, badge slam | |
| quest claim | reorder: each row tweens from old to new Position `(0.42, Quint, Out)` | |
| detail | art ghost flies from the slot to the detail position, scale ratio, `(0.38, Quint, Out)` | |
Behaviours to wire: Free first Moon Crate, weighted rarity drop (table in DATA), duplicate converts to coins, daily calendar (7 days, claim once), quest progress from bake count / crates / collection / level, level curve 60 + 20 x level, text size and particles settings (Low/Med/High cap particle count), Reduce Motion (no shake, no flash > 0.25, no loops, durations ~0).

## Sound cue points (SoundService; prototype synthesises them)
click (release), tick (hover, counter step, tab), coin (each arriving icon), whoosh (screen push), pop (modal, badge, toast), rattle (chest shake), boom (burst), sparkle (rare reveal, claim), levelup, nope (disabled tap). Short and soft; one SoundGroup with a volume slider.

## Not buildable as-is (substitutes)
text-stroke + shadow copy -> UIStroke + duplicate label; repeating stripes -> tiled ImageLabel; skew shine -> rotated Frame; SVG hold ring -> two clipped half rings or sprite sheet or bar; canvas particles -> pooled Frames (40-60) or ParticleEmitter in a ViewportFrame; inline SVG art -> ImageLabel assets at 2x; box-shadow rings -> UIStroke / offset Frames; WebAudio -> Sounds.

Next step: `/rbx-ui` builds the real ScreenGui from `spec.json` and this file.
