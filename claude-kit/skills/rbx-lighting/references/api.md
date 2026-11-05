# LightingKit API (Luau) and the console protocol

Module `scripts/LightingKit.luau` (generated; copy to `src/shared/LightingKit.luau` or paste before your code) and the one-file runner `scripts/lighting_run.luau` for `execute_luau`. Both embed `LightingCore` and the preset data; no other file is needed.

```lua
local LightingKit = require(game.ReplicatedStorage.Shared.LightingKit)
LightingKit.apply("obby")
LightingKit.apply("horror", { time = "night", mobile = true, bloom = { Intensity = 0.3 } })
local scan = LightingKit.scan({ genre = "obby", platform = "both", game = "my-game", scorer = "builder" })
LightingKit.fix({ genre = "obby" })
```

| Function | Does |
|---|---|
| `LightingKit.apply(preset, overrides?)` | Resolves the preset (aliases ok: tycoon, anime, adventure, scifi ...), sets the Lighting properties, creates or reuses exactly one object per effect class under `Lighting`, destroys duplicates, removes effects the preset lists as `false`, stamps the attribute. Returns `{ preset, time, mobile, applied, skipped }`. `overrides.time` = day / golden / night, `overrides.mobile`, any section override. Errors on an unknown preset or time. Run it in Edit mode: `Lighting.Technology` is not writable from a game script at runtime and is then listed in `skipped`. |
| `LightingKit.snapshot(opts?)` | Reads Lighting (properties, `GetSunDirection`), every Atmosphere / Sky / BloomEffect / ColorCorrectionEffect / SunRaysEffect / DepthOfFieldEffect / BlurEffect under Lighting and Camera, all PointLight / SpotLight / SurfaceLight in Workspace (counts, shadow flags, key lights), large-part CastShadow share, and a grid of surface samples. Returns the plain `state`. |
| `LightingKit.verify(opts?)` | snapshot + `Core.verify`; returns the report. |
| `LightingKit.scan(opts?)` | snapshot + verify + the scan table (`references/gate-format.md`) and the console lines. `opts`: `genre`, `time`, `platform` (`both` / `pc` / `mobile`), `game`, `scorer` (`builder` / `critic`), `waive`, `theme` (default: read from `ReplicatedStorage.Shared.StyleKit.Theme`), `bands`, `emit = false` (no console output). |
| `LightingKit.applyFixes(report)` | Carries out the fixes of the failed checks. Whole-look failures apply the preset once (then lights and CastShadow fixes); the rest are single property changes or removals. Returns `{ applied, manual, skipped, rescan }`. Interior lights, genre choice and sky choice are `manual`. |
| `LightingKit.fix(opts?)` | scan, applyFixes, scan, up to `opts.passes` (3). |
| `LightingKit.Core` | `verify(state, cfg)`, `resolve(preset, time, mobile, overrides)`, `bands(genre, phase)`, `canon(name)`. Pure, no engine calls. |
| `LightingKit.config` | Sampling defaults: `grid` 8 (8x8 columns over the play area), `maxSamples` 96, `regionCap` 400 studs, `roofCheck` 80 studs. |

## Sampling (L6, L9)
The play area is the bounding box of the anchored parts (<= 20,000 parts examined) centred on the map and capped at `regionCap`; 4 extra columns surround each SpawnLocation (first 4). Each column casts up to 4 rays down (the roof, then the floor of a room under it; surfaces closer than 6 studs to the last recorded one are skipped), and each hit records its colour (part Color, or the terrain material colour), normal, whether the sun is blocked (a ray toward `GetSunDirection`), whether something is within 80 studs above it (indoor), whether it is Neon, and the lighting from nearby lights (`Brightness * (1 - d/Range)^2`, capped at 3). Parts with Transparency >= 0.95 are ignored. This is a sample, not a render: a map of one flat colour will read as flat, which is a real finding.

## Console protocol
`execute_luau` output is truncated per line, so the scan is printed as `LIGHTING_SCAN_PART i/n <json chunk>` lines (7000 characters each) plus `LIGHTING: PASS|FAIL x/12 checks pass; failing: L4,L7`. Save the console output to a file and run `python scripts/lighting_gate.py ingest <file> ...`; the gate reassembles the chunks. A missing chunk is an error, never a silent pass.

## Limits (read these)
- Not run in live Studio: the Luau runs under Lune with a mock world (ray casts over boxes, Instance properties on Lune Instances). The engine calls (`Workspace:Raycast`, `GetDescendants` over a real map, `Lighting:GetSunDirection`, `Lighting.Technology` writes, `Terrain:GetMaterialColor`, requiring the StyleKit Theme module, `HttpService:JSONEncode`) are exercised only by static analysis.
- `Lighting.Technology` is plugin-level: set it in Edit mode (`execute_luau` / plugin / command bar) so it is saved in the place file.
- Colours are read from `Part.Color` / terrain material colours; textures, decals, SurfaceAppearance and material albedo are not seen, so textured maps read slightly different from the estimate. Use screenshots.
- The state of `ClockTime` animations (day/night cycles) is the value at the moment of the scan: scan at the time of day the screenshots use, or set `CONFIG.time`.

## Runner CONFIG (lighting_run.luau)
`mode` scan | apply | fix; `scorer` builder | critic; `genre` (see presets.md, aliases ok); `time` day | golden | night (apply; a scan reads Lighting.ClockTime); `platform` both | pc | mobile; `preset` (apply only, defaults to genre); `mobile` (apply only, the mobile-safe variant); `overrides` (apply only, section overrides such as `{ bloom = { Intensity = 0.2 }, sunRays = false }`); `waive` (`{ L5 = "reason" }`, at least 10 characters).
