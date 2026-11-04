# Intent: what you promise about a placement

The intent is a plain table (JSON-able). `Placement.place` stores it on the model as the attribute `PlacementIntent`, so every later scan re-checks the same promises. A model with no stored intent gets `defaultIntent`, a kind inferred from its name (door, tree, npc, crate ...) or `ground` for Baseplate/Ground/Floor.

```lua
Placement.place(door, {
  kind = "door",
  at = { 40, 3.5, 12 },
  posGrid = 4,
  surfacePath = "Workspace.Map.House.Floor",
  face = { target = "Workspace.Map.House.Hall" },
  front = "Front",
  yawGrid = 90,
  expectedSize = { 4, 7, 0.5 },
  bounds = { min = { -512, -50, -512 }, max = { 512, 400, 512 } },
  allowOverlap = { "Workspace.Map.House.Wall" },
  connect = { { at = "front", to = "Workspace.Map.Stairs2", toAt = "back", tol = 0.1 } },
  pair = { with = "Workspace.Map.Gate.R", axis = "x", at = 0 },
  group = { name = "Fence", sameYaw = true },
  waive = { P4 = "doors on this ship face the corridor, checked by hand 2026-11-04" },
})
```

| field | meaning | default |
|---|---|---|
| `kind` | door, window, npc, player, sign, chair, table, lamp, crate, fence, wall, stairs, platform, tree, rock, bush, pickup, ground, prop | inferred from the name, else prop |
| `floating` | the object is meant to hover (air, decor, pickup): P2 is skipped | kind (pickup, ground) |
| `floatTol` `buryTol` `flatGround` | ground tolerances (studs); `flatGround` makes uneven ground a fail | 0.1, 0.25 (kind), false |
| `allowTilt` `maxTiltDeg` `tilt = {deg, tol}` `alignToSurface` | upright rules; alignToSurface compares with the ground normal under the centre | upright within 3 deg |
| `face` `front` `faceTol` | facing target; `face.tol` overrides the 15 deg tolerance | none |
| `yawGrid` `randomYaw` `yawTolDeg` | grid in degrees; randomYaw for organic props | project default 15 (only when no `face`), kind default |
| `at` `atTol` `posGrid` `posGridOrigin` `originOk` | position promises | none |
| `expectedSize` `sizeTol` `sizeSorted` `sizeAxes` | size promise | kind range |
| `bounds` | map bounds `{min, max}`, each a 3-vector (use `nil`-free numbers) | `Placement.config.core.bounds`, else unverified |
| `allowOverlap` `allowOverlapNames` | prefixes / lower-case name parts that may be intersected | kind hosts (door: wall, frame, doorway) |
| `terrainFillMax` | share of the volume allowed inside terrain | 0.15 (tree 0.4, rock 0.5) |
| `dynamic` | physics object: may be unanchored | false |
| `canCollide` `canTouch` `massless` `allowInvisible` | physics promises | kind (pickup: false) |
| `connect` `pair` `group` | P7 promises | none |
| `waive` | `{ P4 = "reason" }`, reason of at least 10 characters | none |

`surfacePath` is the instance (or a descendant) the model must rest on (P2). `face.target` is an instance path or `{x,y,z}` (also `{ dir }`, `{ awayFrom }`, `{ any = true }`); `front` is Front (LookVector), Back, Left or Right; `yawGrid` 0 turns the grid off. [cold:rbx-placement/intent-syntax.md] read only when you need the exact syntax of `expectedSize`, `connect`, `pair` or `group`.

Project-wide defaults go in `Placement.config.core` or per call in `opts`; rules by name pattern in `opts.rules`, by path in `opts.intents`; precedence (later wins): defaultIntent, ground name, inferred kind, rules, `opts.intents`, the stored attribute. [cold:rbx-placement/intent-defaults.md] read only when setting project-wide defaults or name-pattern rules for intents.
Attributes on a model: `PlacementIntent` (JSON), `PlacementKind` (shorthand), `PlacementObject = true` (treat a container Model as one object), `PlacementIgnore = true` with `PlacementIgnoreReason` (skip it in scans; counted against the 10% limit).
