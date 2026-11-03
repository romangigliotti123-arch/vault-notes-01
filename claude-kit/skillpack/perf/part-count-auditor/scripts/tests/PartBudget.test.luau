--!nocheck
-- Run: lune run PartBudget.test.luau   (from the kit's systems folder, see check-scripts.sh)
local t = require("../../../../../systems/_check/harness")
local PartBudget = require("../PartBudget")

t.test("regions are ranked worst first with the worst metric named", function()
	local rows = PartBudget.evaluate({
		{ name = "Lobby", parts = 1000 },
		{ name = "City", parts = 9000, drawCalls = 400 },
		{ name = "Mall", parts = 2000, drawCalls = 1500 },
	})
	t.eq(rows[1].name, "City")
	t.eq(rows[1].status, "over")
	t.eq(rows[1].worst, "visibleParts")
	t.eq(rows[2].name, "Mall")
	t.eq(rows[2].worst, "drawCalls")
	t.eq(rows[3].status, "ok")
end)

t.test("warn band starts at 80 percent", function()
	local rows = PartBudget.evaluate({ { name = "A", parts = 4000 }, { name = "B", parts = 3999 } })
	t.eq(rows[1].status, "warn")
	t.eq(rows[2].status, "ok")
end)

t.test("combine sums the regions seen together", function()
	local c =
		PartBudget.combine({ { name = "a", parts = 3000, drawCalls = 100 }, { name = "b", parts = 2500 } }, "view")
	t.eq(c.parts, 5500)
	t.eq(c.drawCalls, 100)
	t.eq(PartBudget.excess(c), 500)
end)

t.test("mobile budget is stricter", function()
	local r = { { name = "A", parts = 1000, drawCalls = 600 } }
	t.eq(PartBudget.evaluate(r)[1].status, "ok")
	t.eq(PartBudget.evaluate(r, PartBudget.MOBILE)[1].status, "over")
end)

t.done()
