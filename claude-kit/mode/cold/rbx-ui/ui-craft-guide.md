<!-- cold: rbx-ui/ui-craft-guide.md | read when: designing or polishing any Roblox game UI (buttons, shop, inventory, rewards, chest or level-up, motion) or building a UI prototype, before choosing tokens or animation numbers. -->

# UI craft guide: what makes a Roblox / mobile game UI feel premium

Evidence level, said once: layout, colour and shape facts below were READ off screenshots (Roblox games and mobile references, listed at the end). Motion numbers are design heuristics gathered from UI-animation guidance and tuned by feel; no source measured them in a shipped game. Treat every number as a starting value and tune on a phone. Patterns only: never copy a game's art, icons, names or layout.

## 1. Principles (what the best screens share)
1. One focal point per screen: one big primary CTA (the yellow/gold or green one), everything else quieter. Clash Royale keeps yellow for the main action, green for buy/upgrade, red only for notification dots, blue for low-priority chrome.
2. Thick, soft, toy-like: fat dark outlines (about 1/12 of the button height), a coloured lip under every pressable thing, a bright top highlight, rounded corners. Flat rectangles read as cheap.
3. Text is a graphic: heavy rounded font, white (or cream) fill, dark outline in a darker shade of the surface behind it, plus a small hard drop copy. Prices green on cream, numbers tabular, titles larger than everything.
4. Consistent panel grammar: every window uses the same header, close button, inset card, tab and button styles (Bubble Gum Simulator, Pet Simulator 99, Adopt Me do this; mixed styles look amateur).
5. Rarity is colour + shape + motion, in that order: border colour, label word, corner ribbon, then glow and shimmer only for the top two tiers.
6. Popups are never fullscreen: dim the world, keep it visible, tap outside to close, close button top-right and square or round, red. Menu depth about one level.
7. Reward moments are choreographed, not instant: anticipation (shake), release (burst and flash), reveal (scale slam with overshoot), settle (count-up, fly to counter). Skippable and a fast mode for repeated opens.
8. Every number change animates (count-up, bump), every gained resource flies from its source to its counter (Royal Match does this for every resource).
9. Empty, locked, sold-out and disabled states are designed: desaturated, never hidden; locked shows the unlock condition.
10. Density differs by device: phone = one column of big cards or 2-col grid, tablet = 3-4 columns plus detail pane, landscape = side rails and two or three columns that really use the width.

## 2. Tokens (use as defaults, then theme)
Scale: spacing 4 / 8 / 12 / 16 / 24 (UIPadding, UIListLayout.Padding). Type scale (px at 390 wide, UIScale for others): caption 12, body 14-16, label 16-18, button 18-22, title 24-28, hero number 32-44.
Corner radius: small chip 6-8, button 10-14 (about 0.2-0.25 of height, or `UDim.new(0.2,0)`), card 14-18, panel 18-24, pill/round = 0.5 scale. DevForum UI tip: scale-based corners (about 0.2) keep the look on every device; fixed 20 px looks different per screen.
Stroke (UIStroke, Offset only): panel 4-5 px, button 3-4 px, card 2-3 px, chip 2 px, text outline 2-3 px at 18 px text. Colour = surface hue darkened 35-45 percent lightness, never pure black.
Lip (second Frame below): 6-8 percent of button height, hue darkened 25-30 percent. Pressed: lip shrinks to 2 percent, face moves down by the difference.
Highlight: top 40 percent strip, white, UIGradient transparency 0.55 (top) to 1 (bottom); inner shine line 2 px white 0.7 transparency on the top edge.
Shadows: Roblox has no soft shadow. Hard offset: duplicate Frame, black 0.7 transparency, offset (0, 4-6 px), same corner. Floating cards: 2 stacked offset frames.
Panel recipe (9-slice friendly): outer dark stroke 5 px, fill 2-stop vertical gradient, cream or tinted inset card (stroke 3 px darker), header band in accent colour with title text.

Palettes (eyeballed hex ranges from screenshots; adjust to your game):
| Genre | Base / frame | Surface | CTA | Positive | Danger | Premium |
|---|---|---|---|---|---|---|
| Pet / collector (PS99, Adopt Me) | sky blue #3ec1f0 to #1e7fd6 | white #ffffff / cream #fff6d8 | green #6fe02a to #3ba81a | green | red #ff4a4a | magenta #ff4fd8 / purple #9b4dff |
| Garden / farm (Grow a Garden) | wood brown #7a3f1d to #4a2410, grass green #55c23a header | dark brown rows #3a1d0e | green #29c42b | green | red #d22 | Robux purple #8a2be2 |
| Fashion (Dress to Impress) | pink #ff7ac8 to #ffb3e6 | translucent pink | hot pink #ff4fa8 | mint | red | gold stars #ffd23a |
| Puzzle / kingdom (Royal Match) | royal navy #1f3d99 with orange trim #f59a1a | cream #fdf3cf | glossy green #3fc13a with orange rim | green | red | gold |
| Tycoon / bakery (this kit's bar example) | night indigo #1d1b4c to #2d2a74 | cream #fff3d6 | honey #ffb81f | mint #3ddc84 | berry #ff5470 | orchid #b65cff |
Rarity (common to mythic): #b8c0cc grey, #5fd35f green, #3fa7ff blue, #b45cff purple, #ffb81f gold, #ff5fa2 pink or animated rainbow. Keep ONE table in code; name + colour + border + effect level.
Contrast: text over any surface at least 4.5:1; white text needs the dark outline; body text on cream uses #3b2a1a not black.

## 3. Typography in Roblox
Heavy rounded display: `Enum.Font.FredokaOne` (closest to the chunky pet-sim look), `Enum.Font.LuckiestGuy` (loud, short words only), `Enum.Font.GothamBlack`/`GothamBold` (clean numbers, small labels; the Font datatype maps Gotham to Gotham SSm weights and some old Gotham enums now map to Montserrat), `Enum.Font.Bangers` (comic bursts), newer families via `Font.fromName` (Builder Sans for body, Fredoka for headings). Pair: FredokaOne for titles, buttons and numbers; GothamMedium/BuilderSans for body and fine print. Never more than two families.
Outline: TextLabel plus UIStroke (ApplyStrokeMode Contextual, Thickness 2-3, dark shade) or TextStrokeTransparency 0; for the deep drop, a duplicate TextLabel offset (0, 2) behind. Numbers: tabular alignment needs a monospaced-digit font; with FredokaOne right-align counters and give them a fixed minimum width so count-ups do not jitter.
Web stand-ins in prototypes: "Arial Rounded MT Bold" / Trebuchet for FredokaOne, Impact for LuckiestGuy, Segoe UI for Gotham; use `font-variant-numeric: tabular-nums` and `-webkit-text-stroke` with `paint-order: stroke fill` for the outline.

## 4. Button anatomy and Roblox instance mapping
```
Button (ImageButton or TextButton, AutoButtonColor=false, BackgroundTransparency 1, AnchorPoint .5,.5)
 UIScale                      -- press/hover/breathing tweens go here, never on Size
 Lip     Frame  (Position y +6% , same size, UICorner 0.22, Color = dark shade)   ZIndex 1
 Face    Frame  (UICorner 0.22, UIStroke 3 dark shade, UIGradient top light -> bottom base)  ZIndex 2
   Gloss Frame  (top 40%, inset 6%, UICorner, white, UIGradient transparency .55 -> 1)
   Shine Frame  (rotated 20 deg, 18% width, white .6, UIGradient; ClipsDescendants on Face; tweened across)
   Row   Frame  UIListLayout Horizontal, Padding 6, Center   (icon + label lockup)
     Icon ImageLabel (UIAspectRatioConstraint 1)
     Label TextLabel (FredokaOne, UIStroke 2.5 dark shade) + LabelShadow TextLabel (offset 0,2, dark, behind)
 Badge  Frame (red circle 18 px, UIStroke 2 white, number label)  top-right, pops with a scale tween
```
Sizes (height at phone scale): small 40-44, medium 52-56, large 64-72; touch target at least 44 px including the lip; icon about 55 percent of the face height; padding 14-18 px horizontal. Five colours: primary (gold/honey), secondary (blue or cream), positive (green), danger (red), premium (purple/magenta with gem icon). One primary per screen.
States: idle (primary CTA breathes 1.00 to 1.04, 1.6 s sine in/out loop, plus a shine sweep every 3-4 s), hover (desktop: face brightens 8 percent, scale 1.04, lift 2 px, 0.12 s Quad Out), pressed (UIScale 0.94 in 0.07 s, lip shrinks), release (overshoot to 1.06 then 1.0 over 0.18 s Back Out), disabled (saturation 0, gradient grey, text 0.5 transparency, no breathing, a tap shakes it and toasts the reason), loading (spinner arc rotating 0.8 s linear, label replaced), success (tick draws in with scale 0 to 1 Back Out, face flips green, 0.9 s then restore).
Hold-to-confirm: ring or bar fills over 0.8-1.0 s while held (linear), release early drains in 0.2 s, completion = pop + haptic cue.
Components: toggle (track 52x28, knob slides 0.15 s Back Out, track colour crossfades grey to green), slider (fill + knob scales 1.2 on drag), stepper (minus/plus round buttons with the number bumping), segmented control and tabs (selected tab raised, accent fill, content slides 8 percent and crossfades), checkbox (tick draws with scale overshoot), notification badge (pop 0 to 1.25 to 1 in 0.25 s, red #ff3b4a, white stroke).

## 5. MOTION TABLE (event -> motion)
| Event | Duration / easing | Values | Stagger | Sound cue |
|---|---|---|---|---|
| Button press down | 0.07 s Quad Out | UIScale 0.94, lip -4 px | none | soft tick (hover higher pitch, click lower) |
| Button release | 0.18 s Back Out | 0.94 to 1.0 with 1.06 overshoot | none | click |
| Hover in / out | 0.12 / 0.15 s Quad Out | scale 1.04, lift 2 px, face +8% light | none | faint high tick (desktop only) |
| Idle breathing (primary CTA) | 1.6 s Sine InOut, loop | scale 1.00 to 1.04 | none | none |
| Shine sweep | 0.6 s Quad InOut every 3.5 s | gloss bar -30% to 130% x | none | none |
| Card entrance | 0.35 s Back Out (spring) | from y +16 px, scale 0.85, transparency 1 | 45-60 ms per card | tiny pop per 3rd card |
| Screen push (forward) | 0.30 s Quint Out | new from x +8% fade+scale .98 to 1; old to x -6% fade out | none | whoosh |
| Screen back | 0.24 s Quad In Out | reverse | none | whoosh low |
| Tab content swap | 0.22 s Quad Out | old fades 0.10 s, new slides 8% in with fade | cards 40 ms | tick |
| Modal open | 0.25 s Back Out | scale 0.8 to 1, dim 0 to 0.55 over 0.2 s | none | pop |
| Modal close | 0.15 s Quad In | scale 1 to 0.92, fade | none | soft close |
| Toast in / out | 0.3 s Back Out / 0.25 s Quad In, hold 2.2 s | y -120% to 0 | queue, one at a time | ping |
| Count-up number | 0.6-0.9 s Quad Out, tick every 3-5 units | value tween + bump scale 1.18 for 0.2 s at end | none | coin tick per step, rising pitch |
| Currency fly-to-counter | 0.7-0.9 s curved, Quad In on the way | 8-14 icons, curved path (bezier, control point up), scale 1 to 0.6, arrive then counter bumps | 40-60 ms per icon | coin clink per arrival |
| Progress bar fill | 0.5 s Quad Out; stripes move 1 s linear loop | gloss strip, end cap bump | none | rising pitch while filling |
| Rarity glow pulse (rare+) | 1.4 s Sine InOut loop | outline ring alpha .15 to .5 (UIStroke Transparency) | none | none |
| Legendary shimmer | 2.2 s linear loop | white bar sweeps the border/face | none | sparkle at reveal |
| Chest shake (anticipation) | 0.7-0.9 s, rotation +/-6 deg ramping, 6-8 shakes | scale 1.0 to 1.12 | none | rattle rising |
| Burst + flash | flash 0.12 s then 0.25 s fade; particles 0.8-1.2 s | 24-40 particles, gravity ~1800 px/s2, fade last 40% | 0 | boom + shimmer |
| Item reveal slam | 0.4 s Back Out | scale 2.2 to 1.0 with 1.08 overshoot, rays spin 20 s/rev | name 0.15 s after | big stinger |
| Rarity text slam | 0.3 s Back Out | scale 3 to 1, then rarity colour stroke | after item | whoosh + hit |
| Screen shake | 0.25-0.4 s | amplitude 6-10 px, decays, 3-5 oscillations (big rewards only) | none | low thump |
| Level-up | banner 0.5 s Back Out; fireworks 1.5 s | XP bar fills, flashes white, bursts at the bar end | bursts 150 ms apart | fanfare |
| Daily calendar claim | tile pop 0.3 s Back Out; tick draws 0.25 s | tile lifts, sparkles, reward flies to counter | next tile glows after | chime |
| Skeleton loading | 1.2 s linear loop | grey blocks with a moving light bar | none | none |
| List reorder | 0.3 s Quint Out | each item moves to its new slot (FLIP) | none | none |
Reduced motion: no shake, no flashes, no infinite loops, fades only, durations x0.5. Always provide it.
Performance: animate transform (Position, Size via UIScale, Rotation) and transparency only; pool particle frames (cap 40-60), recycle toasts, stop idle loops for hidden screens.

## 6. Screen-transition recipes
- Push (shop to item detail): shared element feel: the tapped card's art scales and moves to the detail art position while the list fades 0.2 s (clone the art as a ghost Frame, tween Position and Size 0.35 s Quint Out, swap to the real one).
- Tabs: selected tab rises 3 px and takes the accent; content out 0.1 s, in 0.22 s sliding 8 percent from the direction of the tab.
- Modal over screen: dim to 0.55 in 0.2 s, panel scale 0.8 to 1 Back Out 0.25 s; closing is faster (0.15 s) than opening.
- Rotate or resize: panels re-flow with UIGridLayout/UIListLayout; fade 0.25 s through the change, never let two states overlap.

## 7. Reward reveal recipe (crate / egg / chest): five beats
Research in one line: players want anticipation, a hard impact and a readable payoff; the build-up is the product, so rarity changes LENGTH and VFX, not just colour; repeated opens need a fast path.
| Beat | What happens | Time (common / rare / epic / legendary) |
|---|---|---|
| 1 Anticipation | crate drops with squash impact (scale 1.2 x .8 then settle), dust ring, small shake; idle glow breathes; prompt "Tap the crate"; 3 escalating taps = creak, shake harder, light leaks through the seams | until the player acts |
| 2 Build-up | escalating shake (+/-2 to +/-11 deg, scale to 1.12), rising tick pitch, rumble swell and riser, spark rate grows, rim light and halo grow; near-miss tease: in the last 45 percent the light flickers through LOWER tiers then settles on the real colour (keep the light generic warm white earlier: Overwatch found early coloured lights weakened suspense) | 0.7 / 1.0 / 1.4 / 2.0 s |
| 3 Impact | pull-back (squat, lid winds up 6 deg, latch click) 150 ms, then hit-stop 120 ms, slow-mo 0.35x for 150 ms, lid blast with overshoot (to -86 deg, back to -60), white or tier-tinted flash, shockwave rings, lens-flare streaks, speed lines, light beam, camera push 1.0 to 1.08 to 1.0, shake 10-26 px decaying, particles in rarity colours | 0.45 s |
| 4 Reveal | item rises from the mouth, flips (scale-x 1 to 0, swap face, 0 to 1 with overshoot: 100 + 240 ms), name card, rarity text slam (scale 3 to 1), stars fill one by one (130 ms apart), NEW ribbon, rays length and brightness scale with tier, confetti epic+, screen-wide fireworks and a longer hold for legendary | 0.9 / 1.4 / 1.8 / 2.5 s |
| 5 Payoff | value count-up with ticks, Collect (card flies to the Collection tab, badge pops), Again | player paced |
Total from tap to payoff about 1.6 / 2.4 / 3.2 / 4.5 s. Multi-open (x3): one short build-up (0.9 s) for the best tier, three cards flip 300 ms apart, Skip all. Skip must jump to the final state: finish running tweens, wipe particles, cancel decorative timers; never leave timers or particles behind. Never auto-close; the crate is committed when the build-up starts, so closing mid-way never loses an item.
Sound (layered, never single beeps): wood creak plus latch click on tap; rattle ticks rising in pitch; low rumble swell plus a filtered-noise riser into the hit; impact = sub boom plus noise burst plus a metallic clang; shimmer or chime arpeggio on reveal (2 to 6 notes by rarity, a choir-like pad for legendary); coin shower sprinkle; tick per count-up step; a quick flutter for the near-miss tease. Route through one compressor and a short reverb; keep stingers 1-2 s except legendary.
VFX: spotlight dim (everything but the crate), vignette pulse tinted by rarity, additive glow bloom behind the crate, god rays from the mouth, flare streaks, sparkle trails (streak particles), soft glow sprites on particles, floating embers, ground shadow and a light pool under the crate.
Crate art: chunky 3/4 view, layered planks with grain, metal bands with rivets, emblem on the lock, thick dark outline, rim highlight, one palette per tier (silver, gold, honey, teal with glowing runes, purple with a crown). In Roblox: stacked ImageLabels or Frames, lid as its own element pivoted with AnchorPoint and tweened Rotation.

## 8. Mistakes to avoid
- Pure black outlines and pure white fills everywhere (looks like a default theme); use shaded hues.
- Animating Size/Position of layout children (breaks UIListLayout): tween a UIScale or an inner frame.
- Hover-only affordances on a phone; touch targets under 44 px; buttons crowded at the bottom corners where thumbsticks sit.
- Everything glowing: effects only on the CTA, rare items and the reward moment.
- Long auto-playing sequences with no skip; shaking on every tap; flashes that cannot be turned off.
- Text without outline over busy art; tiny helper text (below 12 px) carrying key facts.
- Two button styles on one screen; red used for both danger and notifications without a rule; a primary button on every card.
- Counters that jump; currencies that vanish without a fly or bump; disabled buttons that give no reason.
- Not clearing tweens: cancel the running tween on MouseEnter/Leave and on destroy (DevForum, interrupted looping tweens).
- Emoji or stretched raster art in shipped UI: use authored icons (ImageLabel, ScaleType Fit) at 2x.
Sound: short and soft; separate hover and click; keep the reward stingers 1-2 s; honour the user's sound toggle (SoundService groups).

## 9. REFERENCE LIST (studied; paraphrased; no images shipped)
Screenshots viewed (copyrighted, study only, not copied):
- Pet Simulator 99 popups: fat white text with dark outline, sky-blue gradient header, big green buttons with dark outline and lip, square red close.
- Adopt Me "New Pet Discovered": polaroid-style framed card, green burst rays behind it, big pink name, small red Done / green Next buttons.
- Adopt Me mobile backpack and catalogue: cyan panel, tabs, rounded white cards with tiny rarity/age chips, red close, search field.
- Bubble Gum Simulator Infinity My Pets / Items: blue panel with pattern, rarity-bordered cards, diagonal LIMITED ribbon, notification dots on side tabs.
- Grow a Garden seed shop (phone): wood panel, green header with restock timer, rarity pills, green price + purple Robux buttons, red NO STOCK.
- Plants vs Brainrots seed shop: gold rows, rarity word under name, green cash + magenta gem + cyan gift buttons, consistent rows.
- Blox Fruits fruit spinner: horizontal card strip, rarity word coloured under the name, yellow pointer arrows.
- Dress to Impress picker and star rating: pink shared frame, category rail, stars filling one by one with sparkles.
- Tower Defense Simulator HUD and reward text: UI kept to edges, white outlined floating cash text, colour semantics green/red/orange.
- Royal Match (Wikipedia screenshot): navy frame with thin orange trim, cream inset panels, ribbon headers, round glossy green buttons with orange rim, outlined white text.
- Clash Royale and Brawl Stars (Wikipedia screenshots): thick outline, saturated flat colours, joystick buttons large and translucent.
Articles and docs:
- therookies.co Clash Royale UX breakdown: yellow primary / green secondary / red only for notifications, popups never fullscreen, tap outside to close, about one level of depth, two currencies, 6-item shops.
- funovus.com Royal Match lessons: every gained resource flies from its source to its container, spent resources fly out; animated task completion; animation communicates polish.
- Roblox DevForum "Designing UI - Tips and Best Practices" (devforum.roblox.com/t/3074034): Scale sizing, UICorner about 0.2 scale, UIStroke Offset only, HUD/popup/full-screen/toast hierarchy, safe areas, mobile first.
- DevForum button threads (devforum.roblox.com/t/2395076, /t/how-do-i-get-these-silky-smooth-button-animations/2917473, /t/help-creating-a-gui-effect/475051): UIScale child tween with AnchorPoint .5,.5, hover 1.1 in 0.3 s, tween down on MouseButton1Down and back on Up, cancel looping tweens.
- Roblox Creator Docs Font datatype and Enum.Font pages: FredokaOne, LuckiestGuy, Gotham SSm weights, Builder Sans, legacy enum mapping.
- Roblox Creator Docs UIStroke class: ApplyStrokeMode, LineJoinMode, Thickness, BorderStrokePosition, StrokeSizingMode.
- UI-animation guidance (skills.cat micro-interactions, playbooks.com gesture-responses): press scale 0.95-0.97, press response under 100 ms, release 150-300 ms with cubic-bezier(.34,1.56,.64,1), ripples 400-600 ms.
- Kotaku, loot-box opening (why it feels like Christmas): faint glow leaking from the seams as a teaser, signal rarity late, soft tactile sounds, camera and kinetic effects, keep animations short when people open many (Halo 5, Duelyst).
- Roblox DevForum "What makes a good loot box opening animation" (devforum.roblox.com/t/1999029): drop-and-slam with bounce, box punched open from inside, more dramatic animation for legendary, particle colours tied to rarity, more build-up.
- Game Wisdom / gurugamer / dotgg loot-box writeups: a rare item can flash past before the real result (near-miss-like presentation); Roblox hatch-script pages show players ask for skip because long hatch animations become a time sink.
- Rarity colour ladders (starship-survivors wiki, WoW-style tables): grey, green, blue, purple, orange/gold; glow and shape complexity rise with tier.
Not found (said honestly): no talk transcript for "Juice It or Lose It", no Material or Apple HIG page returned numbers; touch target minimums used (44 px Apple, 48 dp Material) are from general knowledge.
