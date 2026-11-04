--!nocheck
local t = require("../../../../systems/_check/harness")
local O = require("../Overlap")

local phone = { name = "phone", w = 844, h = 390 }

local function item(path, kind, x, y, w, h, order, extra)
	local it = { path = path, kind = kind, x = x, y = y, w = w, h = h, order = order }
	for k, v in extra or {} do
		it[k] = v
	end
	return it
end

local function rules(findings)
	local set = {}
	for _, f in findings do
		set[f.rule] = (set[f.rule] or 0) + 1
	end
	return set
end

t.test("a clean HUD has no findings", function()
	local items = {
		item("G.Coins", "panel", 20, 40, 160, 40, 1),
		item("G.Coins.Label", "text", 30, 45, 140, 30, 2, { textPx = 20 }),
		item("G.Wave", "panel", 360, 40, 120, 40, 1),
	}
	t.eq(O.analyse(items, phone, { topInset = 36 }), {})
end)
t.test("chat hint over the bait panel is an overlap (text over an unrelated panel)", function()
	local items = {
		item("G.Bait", "panel", 20, 300, 200, 60, 1, { opaque = true }),
		item("G.ChatHint", "text", 30, 320, 180, 20, 2, { textPx = 16 }),
	}
	t.eq(rules(O.analyse(items, phone)).overlap, 1)
end)
t.test("a banner behind an opaque HUD bar is hidden-behind", function()
	local items = {
		item("G.Banner", "text", 300, 20, 240, 40, 1, { textPx = 20 }),
		item("G.HudBar", "panel", 200, 10, 440, 60, 5, { opaque = true }),
	}
	t.eq(rules(O.analyse(items, phone))["hidden-behind"], 1)
end)
t.test("two popups at once", function()
	local items = {
		item("G.Popup1", "panel", 300, 100, 200, 100, 3, { popup = true }),
		item("G.Popup2", "panel", 700, 100, 100, 100, 4, { popup = true }),
	}
	t.eq(rules(O.analyse(items, phone))["popup-stack"], 1)
end)
t.test("related items (label inside its own panel) never overlap-flag", function()
	local items = {
		item("G.P", "panel", 0, 50, 100, 100, 1, { opaque = true }),
		item("G.P.L", "text", 10, 60, 80, 20, 2, { textPx = 16 }),
	}
	t.eq(O.analyse(items, phone), {})
end)
t.test("off-screen, small text and a button in the thumbstick zone", function()
	local items = {
		item("G.Far", "panel", 800, 40, 100, 40, 1),
		item("G.Tiny", "text", 400, 100, 60, 10, 1, { textPx = 9 }),
		item("G.Btn", "button", 10, 300, 80, 60, 1),
	}
	local r = rules(O.analyse(items, phone))
	t.eq(r["off-screen"], 1)
	t.eq(r["small-text"], 1)
	t.eq(r["touch-zone"], 1)
end)
t.test("contrast ratio: black on white is 21, grey on grey fails", function()
	t.eq(math.floor(O.contrast({ 0, 0, 0 }, { 1, 1, 1 }) + 0.5), 21)
	local items = {
		item("G.T", "text", 100, 100, 100, 20, 1, { textPx = 16, fg = { 0.5, 0.5, 0.55 }, bg = { 0.45, 0.45, 0.5 } }),
	}
	t.eq(rules(O.analyse(items, phone))["low-contrast"], 1)
end)
t.test("a panel that fills the screen is too big", function()
	local items = { item("G.Shop", "panel", 0, 0, 800, 380, 1) }
	t.eq(rules(O.analyse(items, phone))["panel-too-big"], 1)
end)
t.done()
