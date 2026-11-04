--!nocheck
local t = require("../../../../../systems/_check/harness")
local F = require("../FocusNav")

local function it(id, x, y)
	return { id = id, x = x, y = y, w = 100, h = 40 }
end
local grid = { it("a", 0, 0), it("b", 150, 0), it("c", 0, 100), it("d", 150, 100) }

t.test("step moves along the axis", function()
	t.eq(F.step(grid, "a", "right"), "b")
	t.eq(F.step(grid, "a", "down"), "c")
	t.eq(F.step(grid, "d", "left"), "c")
	t.eq(F.step(grid, "d", "up"), "b")
end)
t.test("step returns nil at the edge and for unknown ids", function()
	t.eq(F.step(grid, "a", "left"), nil)
	t.eq(F.step(grid, "zzz", "left"), nil)
end)
t.test("off-axis candidates lose to in-line ones", function()
	local items = { it("from", 0, 0), it("near-diag", 120, 60), it("inline", 200, 0) }
	t.eq(F.step(items, "from", "right"), "inline")
end)
t.test("audit passes a connected grid with the back button reachable", function()
	local p = F.audit(grid, "a", "d")
	t.eq(p.unreachable, {})
	t.eq(p.noBack, false)
end)
t.test("audit reports a back button that focus cannot reach", function()
	local items = { it("a", 0, 0), it("b", 0, 100) }
	local p = F.audit(items, "a", "missing")
	t.eq(p.noBack, true)
end)
t.test("a lone item is not a dead end", function()
	t.eq(F.audit({ it("a", 0, 0) }, "a", "a").noExit, {})
end)
t.done()
