<!-- cold: rbx-placement/measure-definitions.md | read when: read only when you must judge whether a measured gap, yaw or overlap finding is correct. -->

## From skills/rbx-placement/references/checks.md :: What the numbers mean (so you can judge a finding)

- gap = lowest point minus the highest ray hit under the footprint (centre plus four corners inset 10%); positive floats, negative sinks. Rays start 4 studs above the lowest point and ignore the model itself and player characters.
- yaw = atan2(-front.x, -front.z) in degrees; the grid test uses the nearest multiple; facing offset = angle between the front and the direction to the target, both flattened to the ground plane.
- overlap depth = smallest overlap over the 15 separating axes of two oriented boxes; `move` is the translation of this model that separates it.
