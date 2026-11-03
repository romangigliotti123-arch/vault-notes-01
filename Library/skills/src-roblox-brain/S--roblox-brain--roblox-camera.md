---
id: "roblox-brain/roblox-camera"
type: skill
category: "src-roblox-brain"
source: "roblox-brain"
license: "MIT"
repo_path: "sources/roblox-brain/skills/gameplay/roblox-camera/SKILL.md"
description: "Use when scripting or fixing Roblox camera behavior: CFrame placement, screen raycasts, first/third-person, shoulder views, cutscenes."
orig_name: "roblox-camera"
orig_when_to_use: "Also when the camera clips through walls, jitters, aims wrong on touch or gamepad, or needs a death cam or spectate view."
orig_last_reviewed: "2026-10-14"
tags: [lib/skill, cat/src-roblox-brain, src/roblox-brain]
---

# roblox-brain/roblox-camera

> Use when scripting or fixing Roblox camera behavior: CFrame placement, screen raycasts, first/third-person, shoulder views, cutscenes.

Type: skill | Category: [[categories/cat-src-roblox-brain|src-roblox-brain]] | Source: [[sources/src-roblox-brain|roblox-brain]] | License: MIT
Repo file: `sources/roblox-brain/skills/gameplay/roblox-camera/SKILL.md` (extra files, if any, sit beside it in the repo)

---
# Roblox Camera

## When to Load

Load when scripting custom camera behavior (cutscenes, third-person follow, custom rotation), manipulating `CFrame` for placement/rotation, raycasting from the screen, or building a non-default player view. Client-only.

## Quick Reference

**The Camera**: `workspace.CurrentCamera`: one per client. Set `CameraType = Scriptable` to disable defaults and take full control. Without it, defaults overwrite your CFrame every frame.

**CameraType**: `Fixed`, `Attach`/`Watch`/`Track`/`Follow` (subject-following), `Custom` (default), `Scriptable` (no default), `Orbital` (fixed Y, rotates around player). `CameraSubject` cannot be `nil`: setting it reverts.

**Key properties**: `CFrame`, `CameraSubject`, `FieldOfView` (deg), `FieldOfViewMode` (`Vertical`/`Diagonal`), `NearPlaneZ`, `ViewportSize`, `HeadLocked`, `HeadScale`, `Focus`.

**CFrame essentials**:

| Operation | Luau |
| --- | --- |
| Position only | `CFrame.new(position)` |
| Look at target | `CFrame.lookAt(position, target, upVector)` |
| XYZ rotation | `CFrame.Angles(rx, ry, rz)` |
| Local to world | `cf * Vector3.new(0, 0, 10)` |
| Interpolate | `cf:Lerp(goal, alpha)` |
| Unit axes | `cf.LookVector`, `cf.RightVector`, `cf.UpVector` |

**Custom camera loop**: always `PreRender`, never `Heartbeat`:

```luau
camera.CameraType = Enum.CameraType.Scriptable
RunService.PreRender:Connect(function(dt)
    local desired = CFrame.lookAt(head.Position - offset, head.Position)
    camera.CFrame = camera.CFrame:Lerp(desired, math.min(dt * 10, 1))
end)
```

**Raycasting from camera**: `camera:ScreenPointToRay(mx, my)` (accounts for GUI inset) vs `camera:ViewportPointToRay(mx, my)` (raw, NO inset). `ScreenPointToRay` returns a unit Ray (1 stud); multiply `Direction` by length for the actual raycast.

**Pitfalls**:
- Client-only. Server sets silently dropped.
- Without `Scriptable`, defaults overwrite your CFrame every frame.
- `PreRender` for camera (visual sync). `Heartbeat` adds 1-frame lag. `RenderStepped` still works but is superseded by `PreRender`.
- `Camera.CFrame` lacks VR head rotation; use `GetRenderCFrame()` for the true view.
- `SetRoll` is outdated; apply roll via `CFrame.Angles(0, 0, roll)` on CFrame.
- `CFrame.new(pos, lookAt)` is legacy (back-compat only); use `CFrame.lookAt(at, lookAt)` for new code.

See `references/full.md` for first/third-person recipes, cutscenes, screen shake, mouse-look, full API.
