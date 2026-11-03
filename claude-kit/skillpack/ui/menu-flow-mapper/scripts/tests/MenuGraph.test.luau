--!nocheck
-- Run: lune run MenuGraph.test.luau   (from the kit's systems folder, see check-scripts.sh)
local t = require("../../../../../systems/_check/harness")
local G = require("../MenuGraph")

t.test("a clean map reports nothing", function()
	local r = G.audit({
		{ id = "hud", entry = true, opens = { "shop" } },
		{ id = "shop", back = "hud", opens = { "confirm" } },
		{ id = "confirm", back = "shop" },
	})
	t.eq(r.unreachable, {})
	t.eq(r.trapped, {})
	t.eq(r.brokenLinks, {})
	t.eq(r.deep, {})
	t.eq(r.depth.confirm, 2)
end)
t.test("orphan, trap and broken link are found", function()
	local r = G.audit({
		{ id = "hud", entry = true, opens = { "shop", "ghost" } },
		{ id = "shop" },
		{ id = "orphan", back = "hud" },
	})
	t.eq(r.unreachable, { "orphan" })
	t.eq(r.trapped, { "shop" })
	t.eq(r.brokenLinks, { "hud -> ghost" })
end)
t.test("closable screens are not traps", function()
	local r = G.audit({ { id = "hud", entry = true, opens = { "toast" } }, { id = "toast", closable = true } })
	t.eq(r.trapped, {})
end)
t.test("deep screens are flagged against the limit", function()
	local r = G.audit({
		{ id = "a", entry = true, opens = { "b" } },
		{ id = "b", back = "a", opens = { "c" } },
		{ id = "c", back = "b", opens = { "d" } },
		{ id = "d", back = "c" },
	}, 2)
	t.eq(r.deep, { "d" })
end)
t.test("a back target that does not exist is reported", function()
	local r = G.audit({ { id = "a", entry = true, opens = { "b" } }, { id = "b", back = "nowhere" } })
	t.eq(r.brokenLinks, { "b back-> nowhere" })
end)
t.done()
