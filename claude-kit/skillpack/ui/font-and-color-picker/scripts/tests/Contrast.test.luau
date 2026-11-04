--!nocheck
local t = require("../../../../../systems/_check/harness")
local C = require("../Contrast")

local function near(a, b, eps)
	t.truthy(math.abs(a - b) < (eps or 0.01), `expected ~{b}, got {a}`)
end

t.test("black on white is 21:1 and same colour is 1:1", function()
	near(C.ratio({ 0, 0, 0 }, { 255, 255, 255 }), 21)
	near(C.ratio({ 90, 90, 90 }, { 90, 90, 90 }), 1)
end)
t.test("known mid-grey pair: #767676 on white is just over 4.5", function()
	local r = C.ratio({ 118, 118, 118 }, { 255, 255, 255 })
	t.truthy(r >= 4.5 and r < 4.6, `got {r}`)
end)
t.test("needed ratio: large or bold-large text relaxes to 3", function()
	t.eq(C.neededRatio(16), 4.5)
	t.eq(C.neededRatio(24), 3)
	t.eq(C.neededRatio(19, true), 3)
	t.eq(C.neededRatio(19, false), 4.5)
	t.eq(C.neededRatio(12, false, true), 3)
end)
t.test("bestText picks white on dark and dark on light", function()
	t.eq(C.bestText({ 10, 10, 40 })[1], 255)
	t.eq(C.bestText({ 250, 240, 120 })[1], 20)
end)
t.test("checkPalette reports only failing pairs with the needed ratio", function()
	local f = C.checkPalette({
		{ name = "body", fg = { 255, 255, 255 }, bg = { 30, 30, 30 }, textPx = 16 },
		{ name = "hint", fg = { 150, 150, 150 }, bg = { 200, 200, 200 }, textPx = 14 },
	})
	t.eq(#f, 1)
	t.eq(f[1].name, "hint")
	t.eq(f[1].needed, 4.5)
end)
t.done()
