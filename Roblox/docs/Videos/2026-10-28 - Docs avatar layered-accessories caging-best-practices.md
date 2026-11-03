---
title: "Docs: avatar / layered-accessories / caging-best-practices"
url: https://create.roblox.com/docs/avatar/layered-accessories/caging-best-practices.md
creator: Roblox Creator Docs
official: true
advice_density: high
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: avatar / layered-accessories / caging-best-practices

[Open](https://create.roblox.com/docs/avatar/layered-accessories/caging-best-practices.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox official docs on layered accessory caging: how inner/outer cages and clothing mesh must be arranged so layered accessories stretch and stack correctly, plus common caging errors that trigger validation rejection.

## Tips
- [page](https://create.roblox.com/docs/avatar/layered-accessories/caging-best-practices) **[[building-art-and-assets]]** Always start caging from one of Roblox's provided caging templates; they include inner and outer cages with properly set UVs.
- [page](https://create.roblox.com/docs/avatar/layered-accessories/caging-best-practices) **[[building-art-and-assets]]** Do not edit cage UVs; editing them introduces visual artifacts.
- [page](https://create.roblox.com/docs/avatar/layered-accessories/caging-best-practices) **[[building-art-and-assets]]** Keep the clothing mesh fully between the inner and outer cage so the layering system deforms it correctly.
- [page](https://create.roblox.com/docs/avatar/layered-accessories/caging-best-practices) **[[building-art-and-assets]]** Move outer cage vertices outward along vertex normals and keep the outer cage as close to the clothing as possible.
- [page](https://create.roblox.com/docs/avatar/layered-accessories/caging-best-practices) **[[building-art-and-assets]]** Do not stack vertices or change the outer cage's vertex, edge, and face count from the starting template.
- [page](https://create.roblox.com/docs/avatar/layered-accessories/caging-best-practices) **[[building-art-and-assets]]** Keep outer cage spacing even across faces; uneven spacing causes artifacts and uneven deformation when other layers are added.
- [page](https://create.roblox.com/docs/avatar/layered-accessories/caging-best-practices) **[[building-art-and-assets]]** Align cage break lines with joint positions, e.g. elbow with the LowerArm joint, to improve animation and posing.
- [page](https://create.roblox.com/docs/avatar/layered-accessories/caging-best-practices) **[[building-art-and-assets]]** Only modify cage regions related to your accessory; for a t-shirt, leave lower leg cages untouched.
- [page](https://create.roblox.com/docs/avatar/layered-accessories/caging-best-practices) **[[building-art-and-assets]]** For bulky clothing, displace outer cage vertices along normals and keep neighbouring vertices moving in similar directions to avoid distortion.
- [page](https://create.roblox.com/docs/avatar/layered-accessories/caging-best-practices) **[[building-art-and-assets]]** For protrusions like puffy hoods or spikes, keep the outer cage below the protruding part so it stays visible when other layers are equipped.
- [page](https://create.roblox.com/docs/avatar/layered-accessories/caging-best-practices) **[[common-mistakes]]** Do not make the inner and outer cage identical; the system cannot determine the accessory and deformation breaks.
- [page](https://create.roblox.com/docs/avatar/layered-accessories/caging-best-practices) **[[common-mistakes]]** Do not place clothing inside the inner cage; it causes artifacts when layered over other clothing.
- [page](https://create.roblox.com/docs/avatar/layered-accessories/caging-best-practices) **[[common-mistakes]]** Do not let the outer cage sit inside the inner cage or leave cages missing heads or limbs; these are rejected during validation.
- [page](https://create.roblox.com/docs/avatar/layered-accessories/caging-best-practices) **[[common-mistakes]]** Avoid collapsed or overlapping cage vertices; they cause artifacts and are rejected during validation.
- [page](https://create.roblox.com/docs/avatar/layered-accessories/caging-best-practices) **[[common-mistakes]]** Keep the clothing mesh inside the outer cage; mesh outside the outer cage does not deform and is rejected during validation.
- [page](https://create.roblox.com/docs/avatar/layered-accessories/caging-best-practices) **[[common-mistakes]]** Avoid oversized gaps between clothing and outer cage; they cause severe deformation when combined with other layers.
- [page](https://create.roblox.com/docs/avatar/layered-accessories/caging-best-practices) **[[updates-live-ops]]** Roblox is enforcing stricter layered accessory validation rules; improperly caged items may be blocked from upload or removed from the catalog.

## Numbers
- [page](https://create.roblox.com/docs/avatar/layered-accessories/caging-best-practices) Validation: **Certain cage errors (overlapping vertices, missing limbs, outer cage inside inner cage, mesh outside outer cage) are rejected on upload** (Roblox docs on layered accessory caging)

## Tools
Roblox caging templates

## He points to
- Roblox Creator Docs: Layered accessory caging best practices

## Topics
[[building-art-and-assets]] [[common-mistakes]] [[updates-live-ops]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
