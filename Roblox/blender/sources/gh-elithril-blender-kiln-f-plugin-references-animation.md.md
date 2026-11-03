---
type: research-source
id: gh-elithril-blender-kiln-f-plugin-references-animation.md
title: "elithril/blender-kiln/plugin/references/animation.md"
source_type: "github"
creator: "elithril"
url: "https://github.com/elithril/blender-kiln/blob/HEAD/plugin/references/animation.md"
published: "2026-10-29"
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0535
relevance: 2
density: high
tags: ["research-source", "github", "claude-blender-ai", "rigging-animation"]
---
# gh-elithril-blender-kiln-f-plugin-references-animation.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Reference from the blender-kiln plugin on animating rigged assets from headless Blender (bpy) scripts. It covers choosing a route by subject (scripted quadruped cycles, UniMate text-to-motion, Mixamo, keyframed objects), seven rules for scripted animation, and measured UniMate prompt reliability and speed. It has little on Roblox export. Its only Roblox-adjacent content is the rig naming and the Mixamo retargeting pointer.

## Claims
- c1: Animation generators need a proper skeleton. A one-bone leg cannot fold a knee, and both MoCapAnything V2 and an early UniMate v2 checkpoint gave unusable motion on such rigs. *(data, medium; rigging-animation)*
- c2: Rig-to-route mapping: a quadruped walk or idle uses the scripted tools/quadruped.py. Biped or winged creatures use UniMate. Humanoids use Mixamo (~2,500 free clips). Articulated objects are keyframed by hand. Video-to-motion is unsupported. *(experience, medium; rigging-animation)*
- c3: Drive bones in their own rest frame. Local Y is not necessarily up: a cat's Hips bone lies along the body, so a Y bob moved it 1.8 cm forward and back and 1 mm up. *(data, high; rigging-animation)*
- c4: Solve the IK pole angle from the rest pose instead of guessing. A guessed -90° turned a cat's elbows forward, while the solved value was +90°. *(data, high; rigging-animation)*
- c5: Keep legs bent in scripted walks. The rejected walk peaked at 101% leg extension. The approved one peaked at 93%, with hips 15% of a leg lower and a stride of 11% of body length. *(data, medium; rigging-animation)*
- c6: Measure a rotation's sign by rotating +0.2 rad and watching a probe. Assumed signs tipped a cat nose-down in sit and attack. *(experience, high; rigging-animation)*
- c7: Loop exactly: a cycle of P frames keys frames 0..P-1. Keying frame P as well duplicates a pose and stutters at the seam. *(experience, high; rigging-animation)*
- c8: For articulated objects, weight each rigid part 100% to one bone with no blending. Use anticipation, overshoot and bounce beats. tools/bind_rigid_parts.py folds bone-parented parts into the skin before skin-only pipelines. *(experience, medium; rigging-animation)*
- c9: The animation tools run as headless Blender scripts: blender --background --factory-startup --python-exit-code 1 --python script.py -- args. This is a batch bpy pattern rather than blender-mcp. *(doc, high; claude-blender-ai)*
- c10: The quadruped tool bakes plain FK keys, shortens the stride or lowers the hips until legs stay at 95% extension or less, and reports the root speed the planted paws share (0.106 m/s on the cat) so game code can move the character without foot skating. *(data, medium; rigging-animation)*
- c11: UniMate reads skeleton topology and joint names, so the Animation-ready skeleton naming matters. Its checkpoints are CC BY-NC 4.0 (non-commercial) and the code is MIT. Warn the user before commercial use. *(doc, high; rigging-animation)*
- c12: UniMate prompts should begin with 'An object' and describe one motion. 'walks in place' worked 8/8 while 'walks forward' worked 0/8 (it slides). Generate at least 4 samples per prompt and keep the best. *(data, medium; rigging-animation)*
- c13: UniMate output GLBs are 2 s long, generated as 60 frames at 30 fps and carried as 48 at 24 fps. The --loop option cross-fades the best-looping window and cuts seam error from 2.1-9.7x to 0.5-1.2x the local frame step. *(data, medium; rigging-animation)*
- c14: For four-legged rigs, relabel the hind leg joints as Thigh/Shin/Fetlock/Foot (Foot becomes Fetlock, ToeBase becomes Foot) to match UniMate's training labels. *(doc, medium; rigging-animation)*

## Numbers
- n1: **UniMate setup disk size**: 3.2 GB (1.1 GB checkpoint) Code, Python 3.10 env with torch, checkpoint
- n2: **UniMate time per 2 s clip, M4 Pro**: CPU adaptive 247 s; CPU 50 Euler 30 s; MPS 50 Euler 18 s Solver and device comparison
- n3: **Walk leg extension, rejected vs approved**: 101% vs 93% Legs locked above ~95% read as too long
- n4: **Mixamo library size**: ~2,500 clips Free with an Adobe account
- n5: **Run-in-place prompt success**: walks in place 8/8; jumps forward 6/8; runs forward 5/8; crouches down 4/8; walks forward 0/8 26-bone cat, 8 samples per prompt
- n6: **UniMate end-to-end time**: 6.5 min for 2 prompts x 2 samples M4 Pro

## Techniques
- t1: **World offset to bone-local conversion**: Convert a world-space offset into the bone's rest frame with (arm.matrix_world.to_3x3() @ bone.matrix_local.to_3x3()).inverted() @ world_offset, then key that in the bone's local channels.
- t2: **Solve IK pole angle**: Put the IK target at rest, search for the pole angle that leaves the chain at its rest rotation, and use that value.
- t3: **Measure motion numerically**: Check leg extension, foot height and loop seams with numbers instead of contact sheets. Example: hip height rose 0.32 to 0.61 m in a jump that looked flat. Then watch the loop.
- t4: **Keep paws level**: Add a copy-rotation constraint to the rest orientation so paws stay flat through the stride.
- t5: **UniMate looped generation**: Run unimate.py animate --asset rig.glb --loop --prompt "An object ..." --reps 4. Review annotation.json, rerun with --annotation, then inspect the kept <prompt>.loop.glb.

### Code: Headless Blender run of scripted quadruped idle/walk animation
```bash
blender --background --factory-startup --python-exit-code 1 --python plugin/tools/quadruped.py -- \
    --asset SK_Cat_rigged.glb --out ./anim --motions idle,walk
```

### Code: Generate looped UniMate motions
```bash
python3 plugin/tools/unimate.py animate --asset SK_Dragon_rigged.glb --loop \
    --prompt "An object flaps its wings." "An object walks in place." --reps 4 --out ./anim
```

### Code: World offset to bone rest frame
```python
(arm.matrix_world.to_3x3() @ bone.matrix_local.to_3x3()).inverted() @ world_offset
```

## Points to
- https://github.com/Friedrich-M/UniMate
- Mixamo
- MoCapAnything V2
- references/characters.md (Animation-ready skeleton, Animation Retargeting)
- tools/quadruped.py
- tools/unimate.py
- tools/motion_loop.py
- tools/bind_rigid_parts.py
