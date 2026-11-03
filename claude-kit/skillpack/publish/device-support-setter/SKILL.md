---
name: device-support-setter
description: "Decide which devices the experience supports (phone, tablet, PC, console, VR) and prove it from the code and a device-by-device play list: input handling per device, UI scale, console navigation and chat rules, performance floor. Use before choosing supported devices in settings and before adding console or VR."
category: publish
tags: devices, mobile, console, gamepad, touch, VR, input, supported devices, cross-platform, settings
kb: Roblox/roblox-kb/cross-platform-and-console.md, Roblox/roblox-kb/ui-ux-design.md, Roblox/roblox-kb/_tools/CHECKLIST-launch.md, Roblox/roblox-kb/optimization-and-streaming.md
related: experience-settings-configurator, mobile-ui-audit, gamepad-ui-navigator, safe-area-checker, accessibility-checker, publish-readiness-gate
---

# device-support-setter

One job: turn "works on all devices" into a per-device yes/no with evidence. Supported devices are a setting the owner makes; the evidence is what the scripts handle (`scripts/device_scan.py` reports keyboard, touch, gamepad and abstract input-layer leads, console chat, large fixed pixel UI) and what a play on the device showed. Console and VR rules are `live-check`: the Creator Docs guidelines change.

## When to use
Before publish when picking supported devices, when adding gamepad, touch or VR, and when mobile or console players report being stuck. Not for: UI layout polish (`mobile-ui-audit`, `safe-area-checker`), gamepad menu navigation build (`gamepad-ui-navigator`), performance tuning (`mobile-perf-tester`).

## Inputs (max 2)
1. Project folder (default: current). 2. Devices the owner wants (default: phone and PC, then console if the scan and a play pass it).

## Procedure
1. Open the live console guidelines, cross-platform and input pages (Evidence) and copy the current rules (TV safe areas, D-pad navigation, chat on console, input action system) with the date.
2. Run `python -I ~/.claude/claude-kit/skillpack/publish/device-support-setter/scripts/device_scan.py <project>`. A FAIL is raw keyboard/mouse handling with no touch, no gamepad and no input-action layer.
3. For each device build a row: can the player start, move, act, buy, open every menu, exit? Evidence is a code lead and a play note. A device you cannot test stays `untested` and is NOT claimed as supported.
4. Prefer one input layer (Input Action System or `ContextActionService`) over per-device branches; show prompts that match the active input (`InputActionLabel` or the key-glyph APIs per the page).
5. Console specifics from the page: relative UI sizes, TV-safe areas, every element reachable with D-pad/select/back, few presses per key action, chat window handling.
6. Phone floor: run `mobile-ui-audit` and a frame/memory pass on the lowest device you can get; record the device model.
7. Decide the supported list: include a device only if its row is fully played. Record excluded devices and why (they are a deliberate choice, not a gap).
8. Write `release/devices.md` (device matrix, scan output, decisions) and pass the list to `experience-settings-configurator` as `devices`.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `start_stop_play` -> Studio device emulator and controller emulator are Studio UI features, not MCP tools: `execute_luau` (Client) can print `UserInputService.TouchEnabled`/`GamepadEnabled`/`PreferredInput` per emulated device -> `get_console_output`. Emulators approximate; a real device pass is separate.

## Fallback
Run the scan on the Rojo folder and test on real hardware by hand. Every device row not actually played is `untested`.

## Evidence
Official (live-check): `Roblox/docs/Videos/2026-10-28 - Docs production publishing console-guidelines.md` (relative UI, TV-safe areas, D-pad reachability, disable chat window on console, glyphs per device), `... Docs projects cross-platform.md` (Input Action System, `PreferredInput`, scale-based UI, `ViewportDisplaySize`), `... Docs input mobile.md`, `... Docs input gamepad.md`, `... Docs production publishing vr-guidelines.md`. Pack: `Roblox/roblox-kb/cross-platform-and-console.md`.

## Output
`release/devices.md` and the supported-devices list.

## Acceptance checks
- [ ] `device_scan.py` ran and exits 0 (quote the verdict lines).
- [ ] Each supported device has a play note, not only a code lead.
- [ ] Unplayed devices are listed as `untested` and not claimed.
- [ ] Console chat and TV-safe rules were checked against the live page.
- [ ] `device_scan.py --selftest` prints `selftest ok`.

## Pitfalls
Calling a game "mobile-friendly" because the emulator opened it. Detecting devices by capability instead of the primary input (a connected gamepad on a phone). Fixed pixel UI that fits a laptop and overflows a phone. Enabling console without a controller-only run through the whole purchase flow.

## Related
`experience-settings-configurator`, `mobile-ui-audit`, `gamepad-ui-navigator`, `safe-area-checker`, `accessibility-checker`.
