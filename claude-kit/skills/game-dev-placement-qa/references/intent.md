# Intent: what you promise about a placement

The intent is a plain table (JSON-able). `Placement.place` stores it on the model as the attribute `PlacementIntent`, so every later scan re-checks the same promises. A model with no stored intent gets `defaultIntent`, a kind inferred from its name (door, tree, npc, crate ...) or `ground` for Baseplate/Ground/Floor.

```lua
Placement.place(door, {
  kind = "door",                              -- reference scale, defaults (see checks.md)
  at = { 40, 3.5, 12 },                       -- where the pivot should be (P1, atTol 1 stud)
  posGrid = 4,                                -- x/z of the pivot on a 4 stud grid (optional)
  surfacePath = "Workspace.Map.House.Floor",  -- it must rest on this instance (or a descendant) (P2)
  face = { target = "Workspace.Map.House.Hall" },  -- front toward this instance or {x,y,z} (P4); also { dir = {0,0,1} }, { awayFrom = ... }, { any = true }
  front = "Front",                            -- which face of the model is its front: Front (LookVector), Back, Left, Right
  yawGrid = 90,                               -- yaw must be a multiple of 90 deg (kind default or 15 otherwise); 0 turns the grid off
  expectedSize = { 4, 7, 0.5 },               -- pivot-frame extents, x y z (or sorted with sizeSorted = true); sizeTol 0.2
  bounds = { min = { -512, -50, -512 }, max = { 512, 400, 512 } },
  allowOverlap = { "Workspace.Map.House.Wall" },   -- instances (prefix) this model may intersect
  connect = { { at = "front", to = "Workspace.Map.Stairs2", toAt = "back", tol = 0.1 } },   -- my face meets that face (or "point" = {x,y,z})
  pair = { with = "Workspace.Map.Gate.R", axis = "x", at = 0 },   -- mirrored partner across the plane x = 0
  group = { name = "Fence", sameYaw = true },                     -- siblings with the same base name must match in size, part count (and yaw)
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

Project-wide defaults go in `Placement.config.core` (floatTol, buryTol, defaultYawGrid, bounds ...) or per call in `opts`. Rules by name pattern: `opts.rules = { { pattern = "^lamp", intent = { kind = "lamp" } } }`; explicit by path: `opts.intents = { ["Workspace.Map.Door1"] = {...} }`. Precedence (later wins): defaultIntent, ground name, inferred kind, rules, `opts.intents`, the stored attribute.

Attributes on a model: `PlacementIntent` (JSON), `PlacementKind` (shorthand), `PlacementObject = true` (treat a container Model as one object), `PlacementIgnore = true` with `PlacementIgnoreReason` (skip it in scans; counted against the 10% limit).
