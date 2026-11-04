# LightingKit API (Luau) and the console protocol

Module `scripts/LightingKit.luau` (generated; copy to `src/shared/LightingKit.luau` or paste before your code) and the one-file runner `scripts/lighting_run.luau` for `execute_luau`; both embed `LightingCore` and the preset data.

```lua
local LightingKit = require(game.ReplicatedStorage.Shared.LightingKit)
LightingKit.apply("obby")
LightingKit.apply("horror", { time = "night", mobile = true, bloom = { Intensity = 0.3 } })
local scan = LightingKit.scan({ genre = "obby", platform = "both", game = "my-game", scorer = "builder" })
LightingKit.fix({ genre = "obby" })
```

| Function | Does |
|---|---|
| `LightingKit.apply(preset, overrides?)` | Resolves the preset (aliases ok: tycoon, anime, adventure, scifi ...), sets Lighting properties, creates or reuses exactly one object per effect class under `Lighting`, destroys duplicates, removes effects the preset lists as `false`, stamps the attribute. Returns `{ preset, time, mobile, applied, skipped }`. `overrides.time` = day / golden / night, `overrides.mobile`, any section override. Errors on an unknown preset or time. Run in Edit mode: `Lighting.Technology` is not writable at runtime and is then listed in `skipped`. |
| `LightingKit.scan(opts?)` | snapshot + verify + the scan table (`references/gate-format.md`) and the console lines. `opts`: `genre`, `time`, `platform` (`both` / `pc` / `mobile`), `game`, `scorer` (`builder` / `critic`), `waive`, `theme` (default: read from `ReplicatedStorage.Shared.StyleKit.Theme`), `bands`, `emit = false` (no console output). |
| `LightingKit.applyFixes(report)` | Carries out the fixes of the failed checks. Whole-look failures apply the preset once (then lights and CastShadow fixes); the rest are single property changes or removals. Returns `{ applied, manual, skipped, rescan }`. Interior lights, genre choice and sky choice are `manual`. |
| `LightingKit.fix(opts?)` | scan, applyFixes, scan, up to `opts.passes` (3). |

`LightingKit.snapshot(opts?)` reads Lighting, effects, lights and surface samples into the plain `state`; `LightingKit.verify(opts?)` = snapshot + `Core.verify`. [cold:rbx-lighting/api-reference.md] read only when calling `snapshot`/`verify` directly or tuning `LightingKit.config` / `LightingKit.Core`. 
`LightingKit.Core` (pure `verify`, `resolve`, `bands`, `canon`) and `LightingKit.config` (sampling defaults). [cold:rbx-lighting/api-reference.md] read only when calling `LightingKit.Core` functions or changing `LightingKit.config` sampling defaults.

## Sampling (L6, L9)

Grid of ray-cast columns over the play area (`LightingKit.config`), a sample not a render. [cold:rbx-lighting/sampling.md] read only to understand or tune how surfaces are sampled for L6/L9.

## Console protocol
`execute_luau` output is truncated per line, so the scan is printed as `LIGHTING_SCAN_PART i/n <json chunk>` lines (7000 characters each) plus `LIGHTING: PASS|FAIL x/12 checks pass; failing: L4,L7`. Save the console output to a file and run `python scripts/lighting_gate.py ingest <file> ...`; the gate reassembles the chunks. A missing chunk is an error, never a silent pass.

## Limits (read these)
- Not run in live Studio: the Luau runs under Lune with a mock world; the engine calls (`Workspace:Raycast`, `GetDescendants` over a real map, `Lighting:GetSunDirection`, `Lighting.Technology` writes, `Terrain:GetMaterialColor`, requiring the StyleKit Theme module, `HttpService:JSONEncode`) are checked only by static analysis.
- `Lighting.Technology` is plugin-level: set it in Edit mode (`execute_luau` / plugin / command bar) so it is saved in the place.
- Colours come from `Part.Color` / terrain material colours; textures, decals, SurfaceAppearance and material albedo are not seen, so textured maps differ from the estimate. Use screenshots.
- The state of `ClockTime` animations (day/night cycles) is the value at the moment of the scan: scan at the time of day the screenshots use, or set `CONFIG.time`.

## Runner CONFIG (lighting_run.luau)
`mode` scan | apply | fix; `scorer` builder | critic; `genre` (see presets.md, aliases ok); `time` day | golden | night (apply; a scan reads Lighting.ClockTime); `platform` both | pc | mobile; `preset` (apply only, defaults to genre); `mobile` (apply only, the mobile-safe variant); `overrides` (apply only, section overrides such as `{ bloom = { Intensity = 0.2 }, sunRays = false }`); `waive` (`{ L5 = "reason" }`, at least 10 characters).
