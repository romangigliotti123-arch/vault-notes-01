<!-- cold: rbx-placement/kind-scales.md | read when: read only to look up the default size range or per-kind exceptions of one kind. -->

## From skills/rbx-placement/references/checks.md :: Reference scale by kind (studs; `size` = sorted small, mid, large extents in the pivot frame)

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
