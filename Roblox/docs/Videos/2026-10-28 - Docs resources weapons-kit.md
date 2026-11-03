---
title: "Docs: resources / weapons-kit"
url: https://create.roblox.com/docs/resources/weapons-kit.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: resources / weapons-kit

[Open](https://create.roblox.com/docs/resources/weapons-kit.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page for the prefab Weapons Kit: setup steps, the WeaponsSystem folder layout, and the configuration values that control weapon behaviour, effects, charging, bows and the weapons GUI.

## Tips
- [page](https://create.roblox.com/docs/resources/weapons-kit) **[[development-process-and-speed]]** Use the Weapons Kit prefab weapons from the Toolbox Inventory to build competitive combat quickly instead of coding weapons from scratch.
- [page](https://create.roblox.com/docs/resources/weapons-kit) **[[building-and-level-design]]** Move the WeaponsSystem folder into ServerScriptService on first use so it acts as the single shared system for all prefab weapons.
- [page](https://create.roblox.com/docs/resources/weapons-kit) **[[combat-and-gameplay-systems]]** Set BulletSpeed to about 20000 to simulate laser/raycast weapons; default 1000 gives projectile travel.
- [page](https://create.roblox.com/docs/resources/weapons-kit) **[[combat-and-gameplay-systems]]** Use StartupTime (default 0.2s) to stop players firing one shot from several weapons in quick succession.
- [page](https://create.roblox.com/docs/resources/weapons-kit) **[[combat-and-gameplay-systems]]** Set ShotCooldown for semi-auto/auto fire rate; default 0.1s, and it is also the time between automatic shots.
- [page](https://create.roblox.com/docs/resources/weapons-kit) **[[combat-and-gameplay-systems]]** Use NumProjectiles for multi-pellet weapons like shotguns; one shot still consumes exactly one ammo.
- [page](https://create.roblox.com/docs/resources/weapons-kit) **[[combat-and-gameplay-systems]]** Set GravityFactor to 1 for arcing projectiles like crossbow arrows; keep 0 for straight rockets.
- [page](https://create.roblox.com/docs/resources/weapons-kit) **[[combat-and-gameplay-systems]]** Tune damage falloff with FullDamageDistance (default 1000) and ZeroDamageDistance (default 10000).
- [page](https://create.roblox.com/docs/resources/weapons-kit) **[[genre-mechanics]]** Add a ChargeRate configuration value to make a weapon a charging weapon (e.g. Railgun or bow); DischargeRate defaults to 0.
- [page](https://create.roblox.com/docs/resources/weapons-kit) **[[combat-and-gameplay-systems]]** Set ExplodeOnImpact true with BlastRadius (default 8), BlastPressure (10000) and BlastDamage (100) for explosive projectiles.
- [page](https://create.roblox.com/docs/resources/weapons-kit) **[[ui-ux-design]]** Provide SmallTouchscreen and LargeTouchscreen AimButton/FireButton frames so the prefab weapons work on touch devices.
- [page](https://create.roblox.com/docs/resources/weapons-kit) **[[vfx-and-particles]]** Add optional muzzle flashes, particle trails, hit marks and casings to weapons for feedback; each is optional and configured per weapon.
- [page](https://create.roblox.com/docs/resources/weapons-kit) **[[ui-ux-design]]** Hit feedback: the HitMarker and directional indicators (e.g. red arc showing shot direction) help players read combat; damage billboards show only to the shooter.

## Numbers
- [page](https://create.roblox.com/docs/resources/weapons-kit) BulletSpeed: **default 1000; 20000 simulates raycast** (Projectile speed config for prefab weapons)
- [page](https://create.roblox.com/docs/resources/weapons-kit) AmmoCapacity: **30 shots per clip (ammo unlimited)** (Reload occurs after each clip)
- [page](https://create.roblox.com/docs/resources/weapons-kit) HitDamage: **10 default** (Damage per direct hit)
- [page](https://create.roblox.com/docs/resources/weapons-kit) ShotCooldown / StartupTime: **0.1s / 0.2s defaults** (Fire rate and weapon-switch startup delay)
- [page](https://create.roblox.com/docs/resources/weapons-kit) MaxDistance: **2000 default** (Projectile travel range before disappearing)
- [page](https://create.roblox.com/docs/resources/weapons-kit) FullDamageDistance / ZeroDamageDistance: **1000 / 10000** (Damage falloff range)
- [page](https://create.roblox.com/docs/resources/weapons-kit) RecoilMin / RecoilMax / TotalRecoilMax: **0.05 / 0.5 / 2** (Recoil per shot and cap)
- [page](https://create.roblox.com/docs/resources/weapons-kit) NumBurstShots: **3 default** (Shots per burst when FireMode is Burst)
- [page](https://create.roblox.com/docs/resources/weapons-kit) BlastRadius / BlastPressure / BlastDamage: **8 / 10000 / 100** (Explosion defaults for ExplodeOnImpact projectiles)
- [page](https://create.roblox.com/docs/resources/weapons-kit) ChargingParticlesRatePerCharge: **20 default** (At 10% charge each emitter emits 2 particles)
- [page](https://create.roblox.com/docs/resources/weapons-kit) Directional indicator distance step: **about 0.03 screen scale per level** (DistanceLevelFromCenter default 6)

## Tools
Roblox Weapons Kit (prefab weapons), Roblox Studio Toolbox, Roblox Studio

## He points to
- Roblox Limited Use License

## Topics
[[building-and-level-design]] [[combat-and-gameplay-systems]] [[development-process-and-speed]] [[genre-mechanics]] [[ui-ux-design]] [[vfx-and-particles]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
