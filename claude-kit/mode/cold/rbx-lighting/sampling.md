<!-- cold: rbx-lighting/sampling.md | read when: read only to understand or tune how surfaces are sampled for L6/L9. -->

## From skills/rbx-lighting/references/api.md :: Sampling (L6, L9)

The play area is the bounding box of the anchored parts (<= 20,000 parts examined) centred on the map and capped at `regionCap`; 4 extra columns surround each SpawnLocation (first 4). Each column casts up to 4 rays down (the roof, then the floor of a room under it; surfaces closer than 6 studs to the last recorded one are skipped), and each hit records its colour (part Color, or the terrain material colour), normal, whether the sun is blocked (a ray toward `GetSunDirection`), whether something is within 80 studs above it (indoor), whether it is Neon, and the lighting from nearby lights (`Brightness * (1 - d/Range)^2`, capped at 3). Parts with Transparency >= 0.95 are ignored. This is a sample, not a render: a map of one flat colour will read as flat, which is a real finding.
