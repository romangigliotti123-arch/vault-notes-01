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
| crate sequence | five beats, see the crate section below | per beat |
| screen shake | Root Position decaying amplitude 6-14 px, 7 steps, 0.3-0.42 s | big rewards only |
| level up | fireworks at the bar end (4 bursts, 150 ms apart), flash, rays, badge slam | |
| quest claim | reorder: each row tweens from old to new Position `(0.42, Quint, Out)` | |
| detail | art ghost flies from the slot to the detail position, scale ratio, `(0.38, Quint, Out)` | |
Behaviours to wire: tap the crate 3 times or press Open (both start the same sequence once), Open x3 (two more crates), Free first Moon Crate, weighted rarity drop (table in DATA), duplicate converts to coins, daily calendar (7 days, claim once), quest progress from bake count / crates / collection / level, level curve 60 + 20 x level, text size and particles settings (Low/Med/High cap particle count), Reduce Motion (no shake, no flash > 0.25, no loops, durations ~0).

## Crate opening: five beats (rarity-timed, total about 1.6 / 2.4 / 3.2 / 4.5 s)
Instance tree: `Stage` Frame (dim with a spotlight hole = big ImageLabel with a transparent centre, or 4 dim Frames around the crate), `Rays` Frame (14 thin rotated Frames, UIGradient fade), `Halo`/`Bloom` ImageLabels (soft glow texture, tinted, low transparency; a BloomEffect in Lighting for the screen-wide look), `Crate` Frame (UIScale + Rotation) with children `Shadow`, `Body` (ImageLabels per layer), `Seam` (white bar, Transparency = 1 - leak), `Lid` (own Frame, AnchorPoint at the hinge corner), `Mouth` glow; `Flash` Frame; `Card` Frame with `Back` and `Front` faces; `Stars` row.
| Beat | Roblox | TweenInfo |
|---|---|---|
| 1 drop | Crate Position y -14em -> 0, UIScale 0.9,1.1 -> 1.2,0.8 -> 1,1; dust ring (UIStroke circle) scale .3 -> 1.7, Transparency 0 -> 1; shake 5 px; thud cue | `(0.42, Quad, In)` then `(0.3, Back, Out)`; dust `(0.6, Quad, Out)` |
| 1 tap x3 | Rotation +/-3 deg per tap, Seam Transparency .88 -> .55 -> .2, creak cue (PlaybackSpeed 0.95 + .05 per tap) | `(0.26 + 0.06 n, Sine, InOut)` |
| 2 build-up | Rotation steps +/-2 -> +/-11 deg every 55 ms, UIScale 1 -> 1.12, Seam/Halo Transparency ramp, sparks (pool), tick cue PlaybackSpeed +0.04 per tick; rumble volume 0 -> .8; riser PlaybackSpeed .8 -> 1.6; tease: ImageColor3 of Seam/Halo flips through lower tiers every 0.1 s in the last 45 percent, settles on the tier colour 90 ms before impact | `(B, Linear)` B = .7 / 1 / 1.4 / 2 s |
| 2b pull-back | Body UIScale 1,1 -> 1.12,.9; Lid Rotation 0 -> 6; latch click | `(0.15, Quad, Out)` |
| 3 impact | hit-stop: pause all tweens and particles 0.12 s, then run at 0.35x for 0.15 s; Lid Rotation 6 -> -86 -> -52 -> -66 -> -60 (overshoot and bounce back); Crate squash 1.12,.9 -> .9,1.14 -> 1.04,.97 -> 1; Flash Transparency .3 -> 1; shockwave rings x2; flare Frames scale-x 0.1 -> 1 -> 1.15; speed lines (30 Frames); beam Frame; camera push Stage UIScale 1 -> 1.08 -> 1; screen shake; vignette ImageLabel pulse | lid `(0.56, Back, Out)` keyed; squash `(0.48, Quad, Out)`; flash `(0.38, Quad, Out)`; push `(0.52, Quad, Out)` |
| 4 reveal | Crate fades down (Transparency 1, Position +2.5em); Card rises from the mouth (Position +4.5em, scale .4 -> 1) then fake flip: UIScale X 1 -> 0 `(0.1, Quad, In)`, swap Back/Front, X 0 -> 1.1 -> 1 `(0.24, Quad, Out)`; stars scale 0 -> 1 Back Out delay 0.13 s x index; rarity text scale 3 -> 1; rays UIScale and Transparency by tier; confetti epic+, 4 fireworks bursts 0.42 s apart for legendary | rise `(0.38, Back, Out)` |
| 5 payoff | value NumberValue 0 -> total in 10 steps of 45 ms with tick cues; Collect: Card Position -> Collection button, UIScale .12, `(0.52, Quad, In)`; badge UIScale pop | |
Multi-open (x3): one build-up of 0.9 s using the best tier; cards in a UIListLayout row, flip delay 0.3 s x index; Skip all. Skip: complete every running tween (`tween:Cancel()` after setting the end values), clear the particle pool, disconnect all heartbeat and delay connections owned by the sequence.
Per-beat sound table (SoundService, all through one SoundGroup with a ReverbSoundEffect and a CompressorSoundEffect): drop: whoosh (vol .5), thud (.6); tap: creak (.5), latch click (.4); build-up: rattle loop, rumble swell (0 -> .8 over B), riser (PlaybackSpeed .8 -> 1.6), tick (+0.04 speed each), flutter (tease); impact: boom (1.0 = sub + noise), metal clang (.5), coin shower (.5); reveal: whoosh, chime ladder (2 to 6 notes by tier), choir pad (legendary, vol .4), sparkle; payoff: tick per count step (+0.03 speed), whoosh on collect, coin ping.

## Home hero scene (layered, all linear gradients)
Stacked `ImageLabel`s or `Frame`s back to front: Sky (gradient, twinkling star sparkles, 2 cloud bands drifting 22 px over 38-52 s Sine), Moon (disc + 4 crater ellipses + 2 glow rings), Hills x2 and village silhouette with lit windows, Street (cobblestone rows + curb), Lamp posts x2 (glow rings flicker 3 s), Storefront: side wall, front wall with timber beams, roof tile rows (shaded plane + side plane), chimney (brick lines), dormer window, bunting, hanging sign (Rotation +/-2.2 degrees, 3.6 s Sine, pivot at the top), striped awning with scalloped edge and shadow, display window (warm gradient back wall, 3 panes split by two mullions; two shelf planks with a front lip and brackets, plates under the shelf items, a bread basket, a glass dome over the tart, a cake stand with price tags; glass glints only in the top-left corner of each pane; flicker overlay Transparency .74 <-> .88 irregular 2.6 s), door with wreath, flower box, chalkboard, crate stack, cat on the roof (tail Rotation flick every 2.8 s). Showcase item: the chosen pastry stands centred on the cake stand at about 2x the shelf size and pops (scale 0 -> 1, Back Out 0.5 s) on every bake. Place every window item by its base: bottom of the ImageLabel on the plank top, an 8 percent dark ellipse as contact shadow, items 11-16 studs-equivalent tall, never over the door or frame. Smoke: 5 puffs, Position curve up and right, Transparency .4 -> 1, scale .5 -> 2.6, 3.6 s each, stagger 0.7 s. String lights: 10 bulbs, chase delay 0.2 s.

## Pastry icons (12, premium set)
Each icon is one 64x64 SVG: warm dark outline (1.5), coloured inner outline, 3-4 stop diagonal linear gradients, top-left light, rim light bottom-right, contact shadow. In Roblox bake each to one ImageLabel per layer (back to front) or ship the flattened PNG at 256 px plus the sparkle layer. Layers: roll 6 (shadow, body, cuts, highlight, rim, flour), croissant 6 (shadow, tips, mid lobes, centre lobe, folds, sheen), swirl 6 (shadow, side, top, spiral, icing, highlight), muffin 7 (shadow, cup, pleats, crown, berries, cracks, highlight), donut 7 (shadow, side, top, glaze, sprinkles, hole, gloss), tart 8 (shadow, crust, rim, custard, berries, leaf, highlights, rim light), macaron 7 (shadow, lower shell, filling, feet, upper shell, feet, gloss), eclair 6 (shadow, bun, cream, glaze, gloss, sparkles), cupcake 8 (shadow, liner, 3 frosting tiers, star, gloss, sparkles), baguette 6 (shadow, body, cuts, highlight, flour, sparkles), cake 9 (shadow, 2 tiers, layer bands, drips, candle, flame, stars, sparkles), pie 8 (shadow, wall, rim, filling, lattice, gloss, steam, sparkles). Epic and legendary icons carry 2-3 twinkle layers (scale .6 <-> 1, Transparency .35 <-> 0, 2.2 s Sine, staggered); the pie steam drifts 1.5 px, 2.6 s. Every icon must read at 28 px: keep outline 1.5 of 64, no detail under 1.1.

## Sound design notes (prototype synth and Roblox)
All pitched cues share C major pentatonic (C D E G A). Coins and chimes are FM bells (carrier:modulator 1:3.5, fast attack, exponential decay, small detuned twin for shimmer); coins climb the pentatonic scale one step per arriving coin. UI clicks are soft sine/triangle blips with a pitch drop plus a 14 ms band-passed noise tick; whoosh = band-passed noise with a smooth sweep and a pan move; creak = three detuned band-passed noise bursts plus a gliding triangle and a latch tick; impact = sub sine drop + filtered noise burst + short inharmonic metallic partials; legendary = formant-filtered saw choir pad + low swell + sparkle cascade. Every voice is randomised (+/-3 percent pitch, +/-2 dB). Level policy: peak <= -3 dBFS, active-region RMS about -18 dBFS (measured -26..-14 for all cues), one master compressor, no DC, no clicks (4 ms minimum attack). In Roblox record or synthesise each cue as an asset, keep the same loudness policy via `Sound.Volume`, add small random `PlaybackSpeed` (0.97-1.03) per play, ReverbSoundEffect on the magic cues, and tween PlaybackSpeed for the rising ticks and riser.

## Sound cue points (SoundService; prototype synthesises them)
click (release), tick (hover, counter step, tab), coin (each arriving icon), whoosh (screen push), pop (modal, badge, toast), rattle (chest shake), boom (burst), sparkle (rare reveal, claim), levelup, nope (disabled tap). Short and soft; one SoundGroup with a volume slider.

## Not buildable as-is (substitutes)
radial-gradient (spotlight, vignette, bloom, glow sprites) -> glow ImageLabels / BloomEffect / ColorCorrection; mix-blend-mode screen and canvas lighter -> glow ImageLabels with low Transparency; text-stroke + shadow copy -> UIStroke + duplicate label; repeating stripes -> tiled ImageLabel; skew shine -> rotated Frame; SVG hold ring -> two clipped half rings or sprite sheet or bar; canvas particles -> pooled Frames (40-60) or ParticleEmitter in a ViewportFrame; inline SVG art -> ImageLabel assets at 2x; box-shadow rings -> UIStroke / offset Frames; WebAudio -> Sounds.

Next step: `/rbx-ui` builds the real ScreenGui from `spec.json` and this file.
