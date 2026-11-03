---
name: ad-policy-checker
description: "Check the ads a game shows (rewarded video, in-world ad units, sponsored billboards, the game as an ad) and the ads a creator runs for it against the advertising standards: content, clear disclosure, no third-party ad servers, per-player AreAdsAllowed gating, no fake impressions. Use before enabling any ad surface and before running a promotion campaign."
category: publish
tags: ads, advertising standards, rewarded video, AreAdsAllowed, PolicyService, disclosure, sponsored, compliance, promotion
kb: Roblox/roblox-kb/ads-and-sponsored-experiences.md, Roblox/roblox-kb/ads-stats-monetisation-playbook.md, Roblox/roblox-kb/age-ratings-moderation-and-tos.md, Roblox/roblox-kb/monetisation-other.md
related: tos-compliance-checker, rewarded-ad-planner, sponsored-ad-reviewer, regional-availability-checker, age-rating-prep, publish-readiness-gate
---

# ad-policy-checker

One job: keep ad surfaces inside the published advertising standards. It has two halves. Ads shown IN the game: `tos-compliance-checker/scripts/compliance_gap.py --focus ads` finds ad code with no `AreAdsAllowed` check and any third-party ad host named in code. Ads the creator runs ON Roblox for the game: reviewed by hand against the same page, with `sponsored-ad-reviewer` for the creative. The standards, property names and limits are `live-check`: policies change, so the page is opened first.

## When to use
Before adding rewarded video, ad billboards or any sponsored content to a game, when the whole game is an ad, and before buying promotion. Not for: planning where rewarded ads fit (`rewarded-ad-planner`), reviewing one creative's wording (`sponsored-ad-reviewer`), paid random items (`paid-random-compliance`).

## Inputs (max 2)
1. Project folder, or the list of ad surfaces. 2. Who the ads are for: own game's ad units, a partner's ad, or the game itself as an ad (default: own game's ad units).

## Procedure
1. Open the live advertising standards page (Evidence). Copy the current content rules, disclosure rules, data-privacy rule and integrity rules into the notes with the date.
2. Run `python -I ~/.claude/claude-kit/skillpack/publish/tos-compliance-checker/scripts/compliance_gap.py <project> --focus ads`. FAIL rows: ad code with no `AreAdsAllowed` read, or a named third-party ad host.
3. Gate by player: read `PolicyService:GetPolicyInfoForPlayerAsync` per player; when `AreAdsAllowed` is false hide, replace or block the ad for that player. If the whole game is an ad, block ineligible players at entry with a clear message.
4. Disclosure: every ad is labelled as advertising in the player's language and does not copy Roblox's own disclosure style (different font and colour). Use the localization tools for the label.
5. Content and data: only ad content you uploaded yourself; no calls to third-party ad servers (even for analytics); no phone numbers or other personal data in ads that lead off-platform; nothing that endangers children or shows violence beyond the rating.
6. Integrity: no bots or engagement campaigns to fake impressions, no wrong metadata to boost delivery, nothing that hides the disclosure. These risk suspension and payout loss per the page.
7. Run `age-rating-prep` again if ads change what a player can see.
8. Write `release/ad-policy.md`: ad surface table (surface, file:line, gated by AreAdsAllowed?, disclosed?, content reviewed?), page date, open items.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `script_grep` (`AreAdsAllowed`, ad unit classes) -> `start_stop_play` -> `execute_luau` (Server) to print the policy table for a test player -> `get_console_output`. A restricted account is needed to see the blocked branch; without one that row stays `untested`.

## Fallback
Run the script on the Rojo folder and review the creatives by hand. Actual ad delivery, reporting and billing are Creator Hub tasks and stay `untested`.

## Evidence
Official (live-check): `Roblox/docs/Videos/2026-10-28 - Docs production promotion comply-with-advertising-standards.md` (clear disclosure in the user's language, self-uploaded content only, no third-party ad servers, AreAdsAllowed per user, no fake impressions), `... Docs production promotion rewarded-video-ads.md`, `... Docs production ad-placements.md`. Pack: `Roblox/roblox-kb/ads-and-sponsored-experiences.md`, `Roblox/roblox-kb/ads-stats-monetisation-playbook.md`.

## Output
`release/ad-policy.md` and the script output.

## Acceptance checks
- [ ] `compliance_gap.py --focus ads` shows no FAIL (quote the lines).
- [ ] Every ad surface has gating, disclosure and content answers with a file:line.
- [ ] The live standards page date is recorded.
- [ ] No third-party ad host or analytics call appears.
- [ ] A restricted-player test is done or marked `untested`.

## Pitfalls
Checking `AreAdsAllowed` once at join but showing the ad to a different context later. Disclosure text only in English. Using an off-platform tracker "just for analytics". Copying the look of the platform's own ad label. Assuming a creative approved elsewhere meets the standards here.

## Related
`tos-compliance-checker`, `rewarded-ad-planner`, `sponsored-ad-reviewer`, `regional-availability-checker`, `age-rating-prep`.
