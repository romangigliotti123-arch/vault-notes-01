--!nocheck
-- Run: lune run StrictPlan.test.luau   (from the kit's systems folder, see check-scripts.sh)
local t = require("../../../../../systems/_check/harness")
local StrictPlan = require("../StrictPlan")
local RequireGraph = require("../../../require-cycle-finder/scripts/RequireGraph")
local TypeScan = require("../../../luau-type-annotator/scripts/TypeScan")

local sources = {
	Leaf = "function M.a(x)\nend\nfunction M.b(y)\nend",
	Mid = "local Leaf = require(script.Parent.Leaf)\nfunction M.run(x)\nend",
	Top = "--!strict\nlocal Mid = require(script.Parent.Mid)\nlocal function go(a: number): number\n\treturn a\nend",
	Clean = "--!strict\nlocal function f(a: number): number\n\treturn a\nend",
	LoopA = "local B = require(script.Parent.LoopB)\nfunction M.a(x)\nend",
	LoopB = "local A = require(script.Parent.LoopA)",
}

t.test("leaves come before the modules that require them", function()
	local plan = StrictPlan.order(sources, RequireGraph, TypeScan)
	local position = {}
	for i, r in plan.rows do
		position[r.name] = i
	end
	t.truthy(position.Leaf < position.Mid)
end)

t.test("already strict and fully typed modules are listed as done, not planned", function()
	local plan = StrictPlan.order(sources, RequireGraph, TypeScan)
	t.eq(plan.done, { "Clean", "Top" })
end)

t.test("cycle members come last with a note", function()
	local plan = StrictPlan.order(sources, RequireGraph, TypeScan)
	local last = plan.rows[#plan.rows]
	t.truthy(last.name == "LoopA" or last.name == "LoopB")
	t.truthy(last.note ~= nil)
end)

t.test("inside a layer the lowest score goes first", function()
	local plan = StrictPlan.order({
		Big = "function M.a(x, y, z)\nend",
		Small = "function M.a(x): ()\nend",
	}, RequireGraph, TypeScan)
	t.eq(plan.rows[1].name, "Small")
	t.eq(plan.rows[2].name, "Big")
end)

t.test("effort buckets", function()
	t.eq(StrictPlan.effort(0), "small")
	t.eq(StrictPlan.effort(5), "small")
	t.eq(StrictPlan.effort(6), "medium")
	t.eq(StrictPlan.effort(21), "large")
end)

t.done()
