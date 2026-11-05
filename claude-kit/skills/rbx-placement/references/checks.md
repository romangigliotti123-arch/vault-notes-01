# Placement checks P1-P7 (the gate passes only when every check of every model is pass or skip, or waived with a reason)

Measured from the model's real geometry (parts, pivot, ray casts, neighbours), never from the code or the plan. Each check returns `pass | fail | skip` plus `measured` values, `tolerance`, `issues` and `fixes` (a concrete correction with numbers). `skip` = the intent says the check does not apply (a floating pickup is not grounded). `unverified` = nothing was declared to check against (the report lists it; a model full of unverified items is a weak pass, say so).

| Check | Fails when | Default tolerance | Fix returned |
|---|---|---|---|
| **P1 Pivot and size** | a Model has no `PrimaryPart`; the pivot lies outside the model's own bounding box; the pivot sits at world (0,0,0) (not declared with `originOk`/`at`); the pivot is more than `atTol` from `intent.at`; the position is off `intent.posGrid`; size is degenerate (< 0.05 studs) or > 2048; size differs from `expectedSize` (per axis, relative) or lies outside the reference range of its `kind` (table below, sorted small/mid/large so authoring axis order does not matter) | `atTol` 1.0 stud, `posGridTol` 0.05, `sizeTol` 0.2 | `setPrimaryPart`, `moveBy` |
| **P2 Grounded** | the lowest point is more than `floatTol` above the highest surface under the footprint (floating), more than `buryTol` below it (buried), nothing is below (void), it rests on a different surface than `intent.surfacePath`, or (with `flatGround`) the ground under it varies by more than `slopeTol`. Skipped when `floating` (or the kind is a pickup/ground). Uneven ground without `flatGround` is a warning | `floatTol` 0.1, `buryTol` 0.25 (tree 1.0, rock 1.5, bush 0.5), `slopeTol` 1.0 | `snapToGround` (dy) |
| **P3 Upright** | the pivot's UpVector is tilted from world up (or from the surface normal with `alignToSurface`) by more than `maxTiltDeg`; upside down is reported as such; with `tilt = {deg, tol}` the angle must match the intended lean. Skipped with `allowTilt` | `maxTiltDeg` 3, tilt `tol` 3 | `setUpright` (keeps the yaw) |
| **P4 Facing and yaw** | the model's front (`front` = Front/Back/Left/Right face, default Front = LookVector) points more than `faceTolDeg` away from the target (`face.target` point or path, `face.dir`, `face.awayFrom`); the yaw is not on the grid (`yawGrid`, kind default, or `defaultYawGrid` 15 when no facing is declared) unless the object is `randomYaw` (trees, rocks, bushes); a kind that needs facing (door, window, npc, player, sign, chair) with no `face` declared (declare `face = {any = true}` to say it truly does not matter); the front points up or down | `faceTolDeg` 15, `yawTolDeg` 1, `defaultYawGrid` 15 | `rotateYaw` (deltaDeg, snapped to the grid when that still faces the target) |
| **P5 Clearance** | the model leaves the map `bounds`; an oriented-box test (SAT) finds a colliding part of another object inside it by more than `overlapTol` (the surface it stands on may sink `buryTol`, hosts named wall/frame/doorway are allowed for doors, `allowOverlap` prefixes and non-colliding parts never count); two visible faces are coplanar, same facing, within 0.005 studs and overlap by more than 0.01 sq studs (z-fighting; downward faces are ignored); more than `terrainFillMax` of its volume is inside terrain | `overlapTol` 0.05, `terrainFillMax` 0.15 (tree 0.4, rock 0.5) | `nudge` (the separating translation), `offsetFace`, `raise` |
| **P6 Physics flags** | a part is neither Anchored nor welded into an anchored assembly (decor that will fall) unless `dynamic`; `canCollide` true but nothing collides (or false but something does); `canTouch` true but no part can be touched; `massless` mismatch; junk parts: zero size, or fully transparent AND non-colliding AND non-touchable AND with no effect/gui/script inside (unless `allowInvisible`) | none | `anchor`, `setCanCollide`, `removeParts` |
| **P7 Connections** | declared `connect` entries end more than `connectTol` from where the next piece starts (stairs, doors, paths, rails, fences: my face `at` front/back/left/right/top/bottom/center vs the target point or the face `toAt` of the instance `to`); a `pair` (mirrored partner across `axis`/`at`) is off, of a different size or does not face the mirrored direction; a `group` member differs from the group median in size or part count (or, with `sameYaw`, in yaw) | `connectTol` 0.1, `pairTol` 0.15, `cloneSizeTol` 5% | `moveBy` |

## Reference scale by kind (studs; `size` = sorted small, mid, large extents in the pivot frame)
Roblox default character about 5.5 tall; door about 4 x 7; stair step rise <= 1. Override per object with `expectedSize`, or per project by editing `Placement.Core.KINDS` (size ranges and defaults) once at startup.

| kind | small | mid | large | notes |
|---|---|---|---|---|
| door | 0.1-2 | 3-6 | 6-9 | needs facing, 90 deg grid, may overlap wall/frame/doorway |
| window | 0.1-2 | 2-8 | 2-8 | needs facing, 90 deg grid |
| npc, player | 1-4 | 1.5-4 | 4.5-7 | needs facing |
| sign | 0.05-2 | 1-12 | 1-16 | needs facing, 90 deg grid |
| chair | 1.5-4 | 1.5-4 | 2-5 | needs facing |
| table | 2-5 | 2-12 | 2-14 | |
| lamp | 0.5-4 | 0.5-4 | 5-25 | |
| crate | 1.5-8 | 1.5-8 | 1.5-8 | |
| fence | 0.2-2 | 2-10 | 2-20 | |
| wall | 0.2-4 | 4-60 | 4-300 | 90 deg grid |
| stairs | 1-60 | 2-40 | 3-40 | |
| platform | 0.2-6 | 4-400 | 4-400 | |
| tree | 1-20 | 1-30 | 5-80 | random yaw, bury 1.0, terrain fill 0.4 |
| rock | 0.5-20 | 0.5-30 | 0.5-30 | random yaw, bury 1.5, terrain fill 0.5 |
| bush | 0.5-8 | 0.5-8 | 0.5-8 | random yaw, bury 0.5 |
| pickup | 0.2-4 | 0.5-4 | 0.5-4 | floats on purpose, must not collide |
| ground | | | | the base surface itself (Baseplate, Floor): not asked to rest on anything |
| prop | | | | no kind: grounded, upright, on the grid, clear, anchored; size and facing are `unverified` |

## What the numbers mean (so you can judge a finding)
- gap = lowest point minus the highest ray hit under the footprint (centre plus four corners inset 10%); positive floats, negative sinks. Rays start 4 studs above the lowest point and ignore the model itself and player characters.
- yaw = atan2(-front.x, -front.z) in degrees; the grid test uses the nearest multiple; facing offset = angle between the front and the direction to the target, both flattened to the ground plane.
- overlap depth = smallest overlap over the 15 separating axes of two oriented boxes; `move` is the translation of this model that separates it.

## Waivers, ignores and honesty
- `intent.waive = { P4 = "reason of at least 10 characters" }` turns a fail into a recorded waiver. More than 10% of the models (minimum 2) with waivers, or ignores (`PlacementIgnore` attribute plus `PlacementIgnoreReason`), fails the gate: fix the models instead.
- Overlap, grounding and z-fight checks only know the parts the engine reports. Welded moving parts, mesh shapes (their box is used), terrain detail below the 4 stud voxel grid and runtime-spawned models need a scan in the right datamodel (Server during a playtest for runtime models). Say what was not covered.
- A hard fail is never "close enough": the tolerances are the tolerances. A deliberate exception is a waiver with a reason, not a wider tolerance on the fly.
