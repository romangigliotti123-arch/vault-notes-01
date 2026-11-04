# Lighting presets (game-dev-lighting-qa)

One preset per genre in `scripts/presets.json`, each with three times of day (`day`, `golden`, `night`) and a mobile-safe variant. `LightingKit.apply(name, overrides)` builds exactly one Atmosphere, Sky, Bloom, ColorCorrection and (where listed) SunRays and DepthOfField under `Lighting`, sets the Lighting properties and stamps `Lighting:SetAttribute("LightingKitPreset", "<genre>:<time>[:mobile]")` so a later scan knows the genre.

Values are starting points from common Roblox practice. They were NOT render-verified in live Studio (Studio was not signed in when this was written): apply, look at the spawn screenshot, adjust with overrides, and keep the result inside the L-check ranges.

| Genre (aliases) | Default time | ClockTime | Sun Brightness | OutdoorAmbient | Atmosphere Density | Bloom Intensity / Size / Threshold | SunRays | DepthOfField |
|---|---|---|---|---|---|---|---|---|
| obby (parkour, obstacle) | day | 13.6 | 3.2 | 128/138/162 | 0.27 | 0.35 / 22 / 1.05 | yes | no |
| simulator (tycoon, sim, idle, clicker) | day | 14.2 | 2.8 | 136/144/168 | 0.22 | 0.4 / 24 / 1.0 | yes | no |
| tower_defense (td, tower defence) | day | 15.2 | 2.6 | 122/130/148 | 0.16 | 0.25 / 20 / 1.15 | no | no |
| horror (scary, spooky) | night | 0.5 | 1.2 | 34/40/58 | 0.5 | 0.5 / 28 / 0.95 | no | no |
| cartoony (anime, cartoon, cute, casual) | day | 14.6 | 2.7 | 146/150/178 | 0.18 | 0.5 / 26 / 0.98 | yes | no |
| open_world (adventure, rpg, openworld) | day | 15.0 | 3.0 | 116/128/150 | 0.36 | 0.3 / 24 / 1.1 | yes | yes (far 0.12) |
| sci_fi (scifi, space, cyberpunk, futuristic) | night | 21.5 | 1.8 | 60/72/112 | 0.3 | 0.8 / 30 / 0.85 | no | yes (far 0.1) |

Every preset: Technology `Future`, GlobalShadows on, EnvironmentDiffuseScale and SpecularScale 0.5-1.2, a mild ColorShift_Top for the sun colour, ColorCorrection with a near-neutral TintColor (so palette colours survive), Sky with the six default Roblox textures plus sun/moon sizes and a star count (replace the textures with an asset-library skybox as an override), Atmosphere with a haze colour matched to the sky.

Reference frames of what good looks like (third-party screenshots, internal comparison only): the vault's roblox-reference folder, INDEX.md categories `lighting-atmosphere` and `world-environment`, tag `lighting` (e.g. warm sunset path map for tower defense, moonlit forest and neon cave for horror and sci-fi, high-key pastel plazas for cartoony). Compare the spawn screenshot against two or three of the same genre before keeping an override.

## Why each genre looks like this
- **obby**: bright and crisp. Higher sun brightness and a slightly lower ShadowSoftness make platform edges and gaps readable from the run-up; moderate haze so the next section is visible.
- **simulator / tycoon**: friendly, evenly lit, saturated; low density so counters, pets and pads stay readable at any camera distance.
- **tower_defense**: the lowest haze and no DepthOfField or strong rays: the whole field must stay sharp and the path must stay separable from the grass.
- **horror**: low ambient, cold tint, dense haze (0.35-0.70), high exposure compensation so it is dark but never pitch black, a single readable light source. The `day` variant is a grey overcast, not a bright day.
- **cartoony / anime**: high-key, high saturation (0.35), soft shadows (ShadowSoftness 0.45), warm sun against a cool fill, gentle bloom.
- **open_world**: layered depth: medium density and haze, warm sun against cool shade, light DepthOfField on PC only (removed in the mobile variant).
- **sci_fi**: cool dusk or night, neon accents, strongest bloom of the set on emissive parts, a thin violet haze.

## Times of day
`day`: sun high, full ambient. `golden` (ClockTime 17.4): low warm sun, warm haze (Decay colour), stronger sun rays, tinted ambient, Brightness 2.6. `night` (ClockTime 23): Brightness 1.5, blue ambient, StarCount 4000, bloom 0.5, no sun rays. The genre's default time is its base; the others are the global patch for that time plus the genre's own patch (e.g. horror `day`, `golden`).

## Mobile-safe variant (`mobile = true`)
Technology `ShadowMap` (instead of Future), EnvironmentSpecularScale 0.5, ShadowSoftness 0.15, Bloom Size 18, no DepthOfField, no SunRays. Same palette, so the look stays recognisable; the cost drops from 6.75-8.75 to 3.75 points (budget 7 on a mobile target). Roblox itself lowers quality on weak devices, but the scene must also be cheap by design: offer the mobile variant to low-end clients (`UserSettings` / `UserInputService.TouchEnabled`) from a client script that applies the non-Technology parts, or ship the mobile variant as the default for a phone-first game (`CONFIG.platform = "mobile"` in the scan).

## Overrides
`LightingKit.apply("horror", { time = "night", mobile = false, lighting = { ExposureCompensation = 0.8 }, atmosphere = { Density = 0.6 }, bloom = { Intensity = 0.3 }, sunRays = false, sky = { SkyboxBk = "rbxassetid://<real id from the asset library>" } })`. A section set to `false` removes that effect; a table merges property by property; colours are `{ r, g, b }` 0-255.

## Tolerance bands per genre (what L6 / L8 judge against)
Generic: Density 0.12-0.55, Haze 0-3, mean luma 0.28-0.72. obby: Density 0.15-0.40, mean 0.34-0.74. simulator: Density 0.12-0.38, mean 0.36-0.76. tower_defense: Density 0.08-0.32, Haze 0-1.5, mean 0.34-0.72, SunRays <= 0.15, DepthOfField not allowed. horror: Density 0.35-0.70, Haze 1-4, mean 0.14-0.50 (night 0.06-0.34), crushed up to 45% (night 60%), Bloom <= 0.8. cartoony: Density 0.08-0.35, mean 0.38-0.78, Saturation 0-0.6, Contrast <= 0.35. open_world: Density 0.22-0.52, mean 0.30-0.70. sci_fi: Density 0.15-0.50, mean 0.14-0.60, Bloom up to 1.3 (threshold >= 0.6). Dusk and night relax the brightness bands (generic night mean 0.10-0.46). Exact numbers: `bands` in `presets.json`.
