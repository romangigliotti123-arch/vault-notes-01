<!-- cold: rbx-placement/intent-syntax.md | read when: you need the exact syntax of an intent field (face targets, front, yawGrid, expectedSize, connect, pair, group). -->

## From skills/rbx-placement/references/intent.md :: intent field syntax

`surfacePath` is the instance (or a descendant) the model must rest on (P2). `face.target` is an instance path or `{x,y,z}`; also `{ dir = {0,0,1} }`, `{ awayFrom = ... }`, `{ any = true }`. `front` is Front (LookVector), Back, Left or Right. `yawGrid` 0 turns the grid off. `expectedSize` is pivot-frame extents x y z (`sizeTol` 0.2). `connect` entries make my face meet another face (`toAt = "point"` takes `{x,y,z}`). `pair` mirrors a partner across the plane `axis = at`. `group` makes siblings with the same base name match in size, part count and yaw.
