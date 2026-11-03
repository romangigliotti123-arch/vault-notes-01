--!nocheck
-- Run: lune run Palette.test.luau   (from the kit's systems folder, see check-scripts.sh)
local t = require("../../../../../systems/_check/harness")
local Palette = require("../Palette")

t.test("parseHex accepts with and without #, rejects junk", function()
	t.eq(Palette.parseHex("#FF8000"), { 255, 128, 0 })
	t.eq(Palette.parseHex("00ff00"), { 0, 255, 0 })
	t.eq(Palette.parseHex("#FFF"), nil)
	t.eq(Palette.parseHex("zzzzzz"), nil)
end)

t.test("contrast of black on white is 21 and symmetric", function()
	local c = Palette.contrast({ 0, 0, 0 }, { 255, 255, 255 })
	t.truthy(math.abs(c - 21) < 0.01, "got " .. c)
	t.eq(Palette.contrast({ 255, 255, 255 }, { 0, 0, 0 }), c)
	t.truthy(math.abs(Palette.contrast({ 9, 9, 9 }, { 9, 9, 9 }) - 1) < 1e-9)
end)

t.test("white on yellow fails the text contrast check", function()
	local issues = Palette.check(
		{ { name = "text", hex = "#FFFFFF" }, { name = "bg", hex = "#FFE600" } },
		{ pairs = {}, textPairs = { { "text", "bg" } } }
	)
	t.eq(#issues, 1)
	t.eq(issues[1].kind, "contrast")
end)

t.test("simulation keeps grays gray and changes saturated reds", function()
	local g = Palette.simulate({ 128, 128, 128 }, "deuteranopia")
	t.truthy(math.abs(g[1] - 128) < 3 and math.abs(g[2] - 128) < 3 and math.abs(g[3] - 128) < 3, "gray moved")
	local r = Palette.simulate({ 255, 0, 0 }, "deuteranopia")
	t.truthy(math.abs(r[1] - 255) > 50, "red unchanged")
	t.eq(pcall(Palette.simulate, { 1, 2, 3 }, "nope"), false)
end)

t.test("red and green of similar brightness are flagged", function()
	local issues = Palette.check({ { name = "team_a", hex = "#C0392B" }, { name = "team_b", hex = "#4F8F2F" } })
	local kinds = {}
	for _, i in issues do
		kinds[i.kind] = true
	end
	t.truthy(kinds.deuteranopia or kinds.protanopia or kinds.gray, "no flag raised")
end)

t.test("a well separated palette passes", function()
	local issues = Palette.check(
		{ { name = "a", hex = "#0B1F3A" }, { name = "b", hex = "#F5E9C8" }, { name = "c", hex = "#E4572E" } },
		{ pairs = { { "a", "b" }, { "a", "c" } } }
	)
	t.eq(#issues, 0)
end)

t.test("bad hex is reported, not thrown", function()
	local _, errors = Palette.check({ { name = "x", hex = "nope" } })
	t.eq(#errors, 1)
end)

t.done()
