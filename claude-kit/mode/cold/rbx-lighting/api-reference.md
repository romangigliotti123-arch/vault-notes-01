<!-- cold: rbx-lighting/api-reference.md | read when: read only when calling `snapshot`/`verify` directly or tuning `LightingKit.config` / `LightingKit.Core`. -->

## From skills/rbx-lighting/references/api.md :: | `LightingKit.snapshot(opts?)` | Reads Lighting (properties

| `LightingKit.snapshot(opts?)` | Reads Lighting (properties, `GetSunDirection`), every Atmosphere / Sky / BloomEffect / ColorCorrectionEffect / SunRaysEffect / DepthOfFieldEffect / BlurEffect under Lighting and Camera, all Point/Spot/SurfaceLight in Workspace, large-part CastShadow share, and a grid of surface samples. Returns the plain `state`. |
| `LightingKit.verify(opts?)` | snapshot + `Core.verify`; returns the report. |

## From skills/rbx-lighting/references/api.md :: | `LightingKit.Core` | `verify(state, cfg)`, `resolve(preset

| `LightingKit.Core` | `verify(state, cfg)`, `resolve(preset, time, mobile, overrides)`, `bands(genre, phase)`, `canon(name)`. Pure, no engine calls. |
| `LightingKit.config` | Sampling defaults: `grid` 8 (8x8 columns over the play area), `maxSamples` 96, `regionCap` 400 studs, `roofCheck` 80 studs. |
