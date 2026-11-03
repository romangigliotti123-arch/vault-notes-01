--!nocheck
-- Run from the kit's systems folder: lune run ../skillpack/money/battle-pass-designer/scripts/tests/SeasonTrack.test.luau
local t = require("../../../../../systems/_check/harness")
local S = require("../SeasonTrack")

local DAY = 86400
local cfg = {
	tiers = 5,
	xpPerTier = 100,
	startsAt = 1000,
	endsAt = 1000 + 30 * DAY,
	free = { [1] = "Coins50", [3] = "Emote", [5] = "Hat" },
	premium = { [1] = "Skin1", [2] = "Skin2", [5] = "Aura" },
}
local NOW = 2000

t.test("a valid season has no problems; missing end date or empty track is reported", function()
	t.eq(#S.validate(cfg), 0)
	local bad = { tiers = 5, xpPerTier = 100, startsAt = 10, endsAt = 10, free = {}, premium = { [9] = "x" } }
	t.eq(#S.validate(bad), 3)
end)

t.test("claim needs the tier reached, then succeeds once only", function()
	local s = S.newState()
	t.eq(select(2, S.claim(cfg, s, "free", 1, NOW)), "tier not reached")
	S.addXp(cfg, s, 150, NOW)
	local ok, reward = S.claim(cfg, s, "free", 1, NOW)
	t.truthy(ok)
	t.eq(reward, "Coins50")
	local ok2, why = S.claim(cfg, s, "free", 1, NOW)
	t.falsy(ok2)
	t.eq(why, "already claimed")
end)

t.test("premium track needs the pass; the client cannot claim without it", function()
	local s = S.newState()
	S.addXp(cfg, s, 500, NOW)
	t.eq(select(2, S.claim(cfg, s, "premium", 1, NOW)), "premium pass not owned")
	s.premium = true
	t.truthy(S.claim(cfg, s, "premium", 1, NOW))
end)

t.test("buying mid-season unlocks premium rewards for tiers already earned", function()
	local s = S.newState()
	S.addXp(cfg, s, 250, NOW) -- tier 2
	t.eq(#S.claimable(cfg, s), 1) -- free tier 1 only (free tier 3 not reached)
	s.premium = true
	local c = S.claimable(cfg, s)
	t.eq(#c, 3) -- free1, premium1, premium2
	t.eq(c[1].tier, 1)
end)

t.test("no xp or claims outside the season window", function()
	local s = S.newState()
	t.eq(S.addXp(cfg, s, 100, 5), 0)
	S.addXp(cfg, s, 100, NOW)
	t.eq(select(2, S.claim(cfg, s, "free", 1, cfg.endsAt)), "season is not active")
end)

t.test("xp is capped at the last tier and junk xp is ignored", function()
	local s = S.newState()
	S.addXp(cfg, s, 99999, NOW)
	t.eq(s.xp, 500)
	t.eq(S.tierFor(cfg, s.xp), 5)
	S.addXp(cfg, s, -5, NOW)
	S.addXp(cfg, s, 0 / 0, NOW)
	t.eq(s.xp, 500)
end)

t.test("unknown track or empty tier is refused", function()
	local s = S.newState()
	S.addXp(cfg, s, 500, NOW)
	t.falsy(S.claim(cfg, s, "gold", 1, NOW))
	t.eq(select(2, S.claim(cfg, s, "free", 2, NOW)), "no reward at that tier")
end)

t.test("pacing warns when a casual player cannot finish", function()
	local days, warn = S.pacing(cfg, 10)
	t.eq(days, 50)
	t.truthy(warn)
	local d2, w2 = S.pacing(cfg, 100)
	t.eq(d2, 5)
	t.eq(w2, nil)
end)

t.done()
