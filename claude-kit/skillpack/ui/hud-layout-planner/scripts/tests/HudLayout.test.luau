--!nocheck
-- Run: lune run HudLayout.test.luau   (from the kit's systems folder, see check-scripts.sh)
local t = require("../../../../../systems/_check/harness")
local H = require("../HudLayout")

local ins = { left = 0.04, top = 0.06, right = 0.04, bottom = 0.05 }
local function el(name, x, y, w, h, p, lvl)
	return { name = name, rect = { x = x, y = y, w = w, h = h }, priority = p or "core", unlockLevel = lvl }
end

t.test("clean top-centre HUD has no issues", function()
	t.eq(H.check({ el("health", 0.35, 0.07, 0.3, 0.05), el("coins", 0.7, 0.07, 0.2, 0.05) }, { insets = ins }), {})
end)
t.test("element under the notch edge is outside the safe area", function()
	local issues = H.check({ el("menu", 0, 0.07, 0.1, 0.05) }, { insets = ins })
	t.eq(issues[1].kind, "outside-safe-area")
end)
t.test("core element in the thumb zone is flagged, optional is not", function()
	local a = H.check({ el("skill", 0.75, 0.6, 0.1, 0.1) }, { insets = ins })
	t.eq(a[1].kind, "in-control-zone")
	t.eq(H.check({ el("skill", 0.75, 0.6, 0.1, 0.1, "optional") }, { insets = ins }), {})
end)
t.test("overlap pair is reported once with both names", function()
	local issues = H.check({ el("a", 0.3, 0.1, 0.2, 0.1), el("b", 0.4, 0.1, 0.2, 0.1) }, { insets = ins })
	t.eq(#issues, 1)
	t.eq(issues[1].other, "b")
end)
t.test("coverage cap flags a crowded HUD", function()
	local issues = H.check({ el("big", 0.05, 0.1, 0.9, 0.4) }, { insets = ins, reserved = {} })
	t.eq(issues[1].kind, "too-much-screen")
end)
t.test("visibleAt gates by level", function()
	local list = { el("health", 0.4, 0.1, 0.1, 0.1), el("quests", 0.5, 0.2, 0.1, 0.1, "situational", 5) }
	t.eq(#H.visibleAt(list, 1), 1)
	t.eq(#H.visibleAt(list, 5), 2)
end)
t.done()
