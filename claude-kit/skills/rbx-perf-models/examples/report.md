# Performance pass (models): Fixture-Obby

Dry run. Nothing in your game was changed. Scan of `Workspace` taken 2026-11-07T13:55:17Z: 34 parts, 8 containers, 2 scripts (0 unreadable).

## Estimated effect of the SAFE tier (ESTIMATE in relative units, not milliseconds; measure with the MicroProfiler)

| metric | before | after SAFE | change |
|---|---|---|---|
| parts in scan | 34 | 30 | 12% |
| physics/query/touch cost units | 50.0 | 36.2 | 28% |
| collision memory units | 34.0 | 30.0 | 12% |
| draw batches proxy (distinct material/mesh/texture combos) | 2 | 2 | 0% |
| visible parts | 30 | 28 | 7% |
| shadow-casting visible parts | 30 | 28 | 7% |

Studio Stats at scan time: InstanceCount=50, memoryMb=123.5, streamingEnabled=False, streamingMinRadius=64, streamingTargetRadius=1024.

## SAFE tier (proven: no rendering property and no gameplay behaviour changes)

| rule | what | parts |
|---|---|---|
| S2 | CanQuery off on decorative non-colliding parts | 9 |
| S3 | CanTouch off on decorative parts | 16 |
| S4 | CanCollide off on parts fully hidden inside a bigger solid block | 1 |
| S5 | Move invisible, non-colliding, unreferenced leftover parts to ServerStorage.PerfPass_Removed | 2 |
| S6 | Move identical opaque duplicates (same place, same everything) to ServerStorage.PerfPass_Removed | 2 |

Kept as they are (not provably decorative): inside a scripted, character, tool, seat or tagged container: 7; tagged or has attributes: 2; has children WeldConstraint: 1; referenced by a weld, constraint, PrimaryPart or value: 1; class TrussPart: 1; class VehicleSeat: 1.

## REVIEW tier (might change the look or behaviour; never applied unless you approve each id)

- **RV-SHADOW** (19 parts, estimated gain 9.5 units): Turn off CastShadow on small parts (largest dimension 2 studs or less). Risk: visual: those parts stop casting shadows. Roblox docs: may leave visual artifacts on shadows; judge it in the view the player sees.
  e.g. `Gem`; `Beacon`; `Axle`
- **RV-ANCHOR** (1 parts, estimated gain 4.0 units): Anchor parts that are not anchored and have no joints, scripts or tags. Risk: gameplay: they no longer fall, slide or can be pushed. Cannot be proven static from edit-time data: a part that rests on the floor may still be a pushable crate or fall at runtime.
  e.g. `Crate`
- **RV-COLLIDE** (1 parts, estimated gain 1.0 units): Turn off CanCollide on small anchored decorative parts. Risk: gameplay: players walk through them. Walk-through foliage and trim are the usual candidates; walls, steps and rails are not.
  e.g. `Masonry/Edge`
- **RV-TEXTURES** (manual, no automatic change): 0 SurfaceAppearance, 0 Texture, 1 Decal. Downsizing images changes how surfaces look; open the largest ones in the Asset Manager and judge.
- **RV-LIGHTS** (manual, no automatic change): 1 lights (0 with Shadows on). Range, Brightness and Shadows are look decisions; each Shadows light is a real GPU cost.
- **RV-TRANSPARENT** (manual, no automatic change): 2 partly transparent parts. Overdraw cost; changing Transparency changes the look.

## Cannot be improved without changing how it looks

- 1 lights stay as they are (every change is a visible change).

## How to apply

1. Say yes to the SAFE tier. `perf_apply.luau` (next to this report) applies it, checks every rendering property again and puts everything back by itself if one differs.
2. Approve REVIEW items one by one by id (for example `--approve RV-FIDELITY-BOX`); each one is then included in a new `perf_apply.luau`.
3. Undo in one step: press Ctrl+Z in Studio (Edit > Undo 'PerfPass: applied'), or run perf_revert.luau from the same folder.

## Limits

- References from scripts are found by name (own name or any parent's name, also `Name1`/`Name2` style families). A script that finds parts some other way (by position, by child order, by string built at runtime) is only caught through the tag, attribute, joint and script-folder rules.
- If any script cannot be read, nothing is SAFE. If the scan was cut off (maxParts), nothing is SAFE.
- Runtime-created parts and parts in other services (ReplicatedStorage models spawned later) are not scanned; scan the Server datamodel during a playtest to cover spawned objects.
- Cost numbers are a relative proxy, not milliseconds. Real gain: compare MicroProfiler before and after.
- Removed parts are moved to ServerStorage.PerfPass_Removed, not destroyed; delete that folder when you are happy.
