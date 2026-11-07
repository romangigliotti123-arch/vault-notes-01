# Handoff: Candy Quarry prototype -> Roblox ScreenGui

This prototype (`index.html`) is a browser mock-up. It is not the game. Build the real UI with `/rbx-ui` from this file and `spec.json`; run `rbx-visual` only after the real build.

## Global
- `ScreenGui` "CandyQuarry": `ResetOnSpawn=false`, `ScreenInsets=DeviceSafeInsets`, `IgnoreGuiInset=false`, `ZIndexBehavior=Sibling`. Layers by `DisplayOrder`: screens 1, modal 5, toasts 9.
- One `UIScale` on the root Frame "Root" (Size 1,0,1,0): `Scale = clamp(min(ViewportSize.X, ViewportSize.Y) / 390, 0.8, 1.75)`. All sizes below are in em; 1 em = 14.4 px at that scale (design px = em x 14.4), so use Scale for placement and the em value x 14.4 Offset only for strokes and corners.
- Fonts: titles `FredokaOne` (TextScaled off, `TextSize = 1.5em`), body `BuilderSansBold`.
- Colours (spec.json): bg 1B2340, panel 2B3A67, accent FFC83D, ok 4DD6A0, warn E5484D.

## Reusable components
| HTML | Roblox tree | Values |
|---|---|---|
| `.btn` | `ImageButton` (or `TextButton`) "Btn" + child `Frame` "Lip" (behind, Y offset +0.25em, darker colour) + `UICorner` + `UIStroke` + `UIGradient` + `UIPadding` | height 3 em min, `UICorner` 0.7 em, `UIStroke` 0.12 em white at Transparency 0.7 (ApplyStrokeMode Border), `UIGradient` Rotation 90, colours top to bottom (variant: yellow FFD96B to FFB81F, green 7BF0C4 to 2FBF8C, blue 6F87D6 to 4A62B3, red FF7A7E to E5484D) |
| `.btn:hover` | `MouseEnter` tween: gradient to the hover pair, Position Y -0.1 em, 0.12 s Quad Out | skip on touch (no hover) |
| press / release | `InputBegan`: `UIScale` child of the button tweens to 0.92 in 0.08 s Quad Out; `InputEnded`/`Activated`: to 1.08 then 1 over 0.15 s Back Out | helper `Squish(btn)` in the StyleKit |
| `.btn:disabled` | `Active=false`, `AutoButtonColor=false`, gradient 6C7599 to 59628A, text C0C8E6 | |
| `.chip` | `Frame` "CoinChip"/"GemChip" + `UICorner` 1 (full) + `UIStroke` + `UIListLayout` Horizontal (Padding 0.45 em) + icon `Frame`/`ImageLabel` + `TextLabel` + plus `TextButton` | count-up: tween a `NumberValue`, set `Text` on `Changed`; pulse `UIScale` 1.15 and back (0.26 s) |
| `.coin` / `.gem` | `Frame` + `UICorner` 1 + `UIStroke` + `UIGradient`; gem = `Frame` Rotation 45 + `UICorner` 0.18 em | placeholder art: replace with ImageLabels |
| `.panel` | `Frame` + `UICorner` 1 em + `UIStroke` + `UIPadding` 0.8 em | |
| `.bar` | `Frame` (track) `ClipsDescendants=true` + `UICorner` 1 + child `Frame` fill, `Size` tween 0.35 s Back Out | |
| `.tabs` / `.tab` | `Frame` + `UIListLayout` Horizontal Fill, children `TextButton` 2.8 em high | active: accent fill, others bg 45% |
| `.grid` / `.card` | `ScrollingFrame` + `UIGridLayout` (portrait 2 columns, landscape 4: set `CellSize` Scale from `AbsoluteSize` on `GetPropertyChangedSignal`) ; card `Frame` + `UICorner` 0.9 em + `UIListLayout` Vertical | `.art` = `Frame` with `UIAspectRatioConstraint` 1.3 |
| `.lock` | `Frame` overlay BackgroundTransparency 0.38 + `TextLabel` "Level N" | |
| `.dim` | full-screen `TextButton` BackgroundTransparency 0.42 (this is a dim, not a blur) | |
| `.modal` | `Frame` max width 22 em (`UISizeConstraint`), pop: `UIScale` 0.8 to 1 over 0.15 s Back Out | |
| `.toast` | `Frame` in a top-centre `UIListLayout`, slide Position -150% to 0 in 0.2 s Back Out, remove after 2.2 s | queue, one at a time per `rbx-ui` rule 9 |
| switch (`.sw button`) | `TextButton` track + `UICorner` 1 + knob `Frame`, knob Position tween 0.15 s Back Out | |

## Screens
- **Home** (`Home` Frame): top row `UIListLayout` Horizontal [spacer, CoinChip, GemChip]; centre `Frame` hero with `TextLabel` "CANDY QUARRY" (duplicate TextLabel behind for the text shadow), `MineButton` (`ImageButton`, circle: `UICorner` 1 + `UIAspectRatioConstraint` 1, 9 em wide, 6.2 em in landscape), hint `TextLabel`; `XpBar` panel (Lv label, bar, xp text); row [GiftButton, SettingsButton]; row [ShopButton, BagButton]. Landscape: the same Frame switches to two columns (left: hero; right: XpBar, gift row, Shop/Bag row, vertically spread) by swapping the root `UIListLayout` for a left `Frame` and a right `Frame` (each with its own `UIListLayout`), toggled from the orientation handler below (`UIListLayout` Horizontal, equal Scale widths).
- **Shop** (`Shop` Frame): header row [BackButton, Title, CoinChip, GemChip]; tab row `TabPicks`/`TabBoosts`/`TabGems`; `ItemGrid` (cards: art, name, note, buy button). Locked: `.lock` overlay when `level < item.lvl`. Owned: button disabled "Owned". Buy: not enough currency = shake (Position X +-0.4 em, 0.26 s) + red toast; enough = confirm modal then deduct, toast. Gems tab uses `MarketplaceService:PromptProductPurchase` (the prototype fakes it).
- **Bag** (`Bag` Frame): header row; `SlotGrid` 8 slots (4 columns, filled slots `ImageButton`, empty dashed `Frame` with `UIStroke` Dashed is NOT available: use a faint solid `UIStroke` Transparency 0.78); `DetailPanel` with name, stat text, equip/unequip button.
- **Settings modal**: three switches (Music, Sfx, Haptics), Reset progress, Done.

## Portrait and landscape (phone and tablet rotate; desktop does not)
- The prototype rotates phone 390x844 <-> 844x390 and tablet 820x1180 <-> 1180x820. In Roblox: `ScreenGui.ScreenOrientation = Sensor` (rotates with the device; `LandscapeSensor` or `Portrait` to lock) and `ScreenInsets = DeviceSafeInsets`, so the notch, side cutouts and home indicator are inset for you; read `GuiService:GetGuiInset()` and `ScreenGui.AbsoluteSize` only for custom padding. Do not hard-code the prototype safe-area numbers (portrait T47/B34, landscape L47/R47/B21 are typical-phone guesses).
- Orientation = `AbsoluteSize.X >= AbsoluteSize.Y`. Listen on `Root:GetPropertyChangedSignal("AbsoluteSize")` (or `workspace.CurrentCamera:GetPropertyChangedSignal("ViewportSize")`), debounce one frame, then run one `ApplyLayout(isLandscape)` that sets: shop grid columns 2 -> 4, bag `invwrap` direction Vertical -> Horizontal, Home two-column swap, hero MineButton 9 em -> 6.2 em. Tween the change over 0.25 s (Quad Out) so the turn reads as a transition, not a pop.
- Keep the `UIScale` formula on `min(ViewportSize.X, ViewportSize.Y)` so em stays the same size in both orientations (the prototype does the same: `--u` is from the short side). Use `UIAspectRatioConstraint` on art and circles only, never on whole screens.
- `DeviceOrientation` of the player: `UserInputService.GetPropertyChangedSignal("DeviceOrientation")` is not needed when `ScreenOrientation = Sensor`; only read `UserInputService:GetDeviceRotation()` for tilt effects.
- Test in Studio Device Emulator at phone and tablet in both orientations and at 16:9, then run `rbx-visual`.

## Behaviour to wire
Navigation stack (go/back), Esc/back closes modal first. Keys (desktop/console only): 1 Home, 2 Shop, 3 Bag, [ ] shop tabs, S settings, Space mine. Cooldown: GiftButton ring shows `elapsed/15 s`; ready = claim +3 gems. Level: `need = 20 x level`; +5 gems per level; gold at level 2, crystal and Turbo at level 3. Mine: `round((power x 2 + sweet 1) x clover 1.2)`.

## Not buildable as-is (use the substitute)
- Gift cooldown ring (`conic-gradient`): ring `ImageLabel` + two half-circle clip Frames rotated by `UIGradient`, or a 24-frame ring sprite sheet.
- Logo text-shadow: second TextLabel offset behind.
- Emoji art: ImageLabels with uploaded assets (`rbx-ui-mockup` assets steps); emoji in `TextLabel` also renders.
- Dashed slot border: solid faint `UIStroke`.

## Next step
Run `/rbx-ui` in this game folder (it reads `ui/prototype/spec.json` and this file). Do not call the prototype the game.
