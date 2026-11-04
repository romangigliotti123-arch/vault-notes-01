<!-- cold: rbx-lighting/why.md | read when: read only to learn why this gate exists or to argue for it. -->

## From skills/rbx-lighting/SKILL.md :: Why this exists: a generated map with the engine's default l

Why this exists: a generated map with the engine's default lighting (flat grey ambient, no Atmosphere, no tuned sky, no colour grading, shadows nobody checked) looks amateur no matter how good the models are. WORKS (no errors), GOOD (fun), LOOKS (screenshots) and PLACEMENT (geometry) all miss it, and `rbx-visual` V5 only scores it by eye after the fact. This gate sets the look at the START and measures it, every time. `rbx-critic` re-runs it independently and refuses GOOD without it.

## From skills/rbx-lighting/references/checks.md :: Why a model and not just rules

The brightness checks need a number for "dark" and "washed out" without a screenshot. The model (constants `model` in `presets.json`): sRGB albedo to linear, ambient term from Ambient or OutdoorAmbient plus a sky term scaled by EnvironmentDiffuseScale and the sun height, sun term from Brightness, sun height, the surface normal and the shade ray, point-light term from `lightE`, emissive surfaces, 2^ExposureCompensation, a Reinhard-style tone curve, display gamma, then the ColorCorrection contrast and brightness. It ranks scenes correctly (default grey vs preset, night vs day, blown vs crushed) but is NOT photometry: the bands are wide on purpose and screenshots (`--shots-from-visual`) decide when they disagree.

## From skills/rbx-lighting/references/presets.md :: Why each genre looks like this

- **obby**: bright and crisp. Higher sun brightness and a slightly lower ShadowSoftness make platform edges and gaps readable from the run-up; moderate haze so the next section is visible.
- **simulator / tycoon**: friendly, evenly lit, saturated; low density so counters, pets and pads stay readable at any camera distance.
- **tower_defense**: the lowest haze and no DepthOfField or strong rays: the whole field must stay sharp and the path must stay separable from the grass.
- **horror**: low ambient, cold tint, dense haze (0.35-0.70), high exposure compensation so it is dark but never pitch black, a single readable light source. The `day` variant is a grey overcast, not a bright day.
- **cartoony / anime**: high-key, high saturation (0.35), soft shadows (ShadowSoftness 0.45), warm sun against a cool fill, gentle bloom.
- **open_world**: layered depth: medium density and haze, warm sun against cool shade, light DepthOfField on PC only (removed in the mobile variant).
- **sci_fi**: cool dusk or night, neon accents, strongest bloom of the set on emissive parts, a thin violet haze.
