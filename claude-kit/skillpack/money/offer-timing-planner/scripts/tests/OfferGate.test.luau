--!nocheck
local t = require("../../../../../systems/_check/harness")
local G = require("../OfferGate")

local cfg = {}

t.test("never on join", function()
	local ok, why = G.canShow(cfg, G.newState(5), "A", "join", 100)
	t.falsy(ok)
	t.eq(why, "no sales on join")
end)

t.test("a moment of need passes for a returning player", function()
	t.truthy(G.canShow(cfg, G.newState(5), "A", "need", 100))
end)

t.test("unknown triggers (random pop-ups) are refused", function()
	t.falsy(G.canShow(cfg, G.newState(5), "A", "timer", 100))
end)

t.test("first session allows only a player-opened shop", function()
	local s = G.newState(1)
	t.falsy(G.canShow(cfg, s, "A", "need", 100))
	t.truthy(G.canShow(cfg, s, "A", "shopOpen", 100))
end)

t.test("no stacking and no interrupting play", function()
	local s = G.newState(5)
	s.modalOpen = true
	t.eq(select(2, G.canShow(cfg, s, "A", "need", 100)), "another modal is open (no stacking)")
	s.modalOpen = false
	s.canPause = false
	t.eq(select(2, G.canShow(cfg, s, "A", "need", 100)), "gameplay cannot pause here")
	t.truthy(G.canShow(cfg, s, "A", "shopOpen", 100))
end)

t.test("global and per-offer cooldowns", function()
	local s = G.newState(5)
	G.record(s, "A", 1000)
	t.eq(select(2, G.canShow(cfg, s, "B", "need", 1100)), "global cooldown")
	t.eq(select(2, G.canShow(cfg, s, "A", "need", 1400)), "offer cooldown")
	t.truthy(G.canShow(cfg, s, "B", "need", 1400))
	t.truthy(G.canShow(cfg, s, "A", "need", 2900))
end)

t.test("per-session cap, but the shop itself is never capped", function()
	local s = G.newState(5)
	for i = 1, 4 do
		G.record(s, "O" .. i, i * 1000)
	end
	t.eq(select(2, G.canShow(cfg, s, "Z", "need", 99999)), "session cap reached")
	t.truthy(G.canShow(cfg, s, "Z", "shopOpen", 99999))
end)

t.done()
