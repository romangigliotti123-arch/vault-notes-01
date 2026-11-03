--!nocheck
-- Run: lune run RequireGraph.test.luau   (from the kit's systems folder, see check-scripts.sh)
local t = require("../../../../../systems/_check/harness")
local RequireGraph = require("../RequireGraph")

t.test("extracts the common require shapes and ignores comments", function()
	local src = [==[
		local A = require(script.Parent.Alpha)
		local B = require(ReplicatedStorage.Shared:WaitForChild("Beta"))
		local C = require("./Gamma")
		-- local D = require(script.Parent.Delta)
		--[[ require(script.Parent.Echo) ]]
		local F = require(script.Parent.Alpha)
	]==]
	t.eq(RequireGraph.extractRequires(src), { "Alpha", "Beta", "Gamma" })
end)

t.test("build keeps only known modules and reports unknown ones", function()
	local g = RequireGraph.build({ A = "require(script.Parent.B) require(script.Parent.Zed)", B = "" })
	t.eq(g.edges.A, { "B" })
	t.eq(g.unknown.A, { "Zed" })
end)

t.test("finds a two-module cycle and a three-module cycle, not the acyclic part", function()
	local edges = { A = { "B" }, B = { "A" }, C = { "D" }, D = { "E" }, E = { "C" }, F = { "A" } }
	local cycles = RequireGraph.findCycles(edges)
	t.eq(#cycles, 2)
	t.eq(cycles[1], { "A", "B" })
	t.eq(cycles[2], { "C", "D", "E" })
end)

t.test("a self require is a cycle", function()
	t.eq(RequireGraph.findCycles({ A = { "A" } }), { { "A" } })
end)

t.test("no cycles in a clean graph", function()
	t.eq(RequireGraph.findCycles({ A = { "B" }, B = {}, C = { "B" } }), {})
end)

t.test("layers put leaves first and report the tangled modules", function()
	local r = RequireGraph.layers({ A = { "B", "C" }, B = { "C" }, C = {}, X = { "Y" }, Y = { "X" } })
	t.eq(r.layers, { { "C" }, { "B" }, { "A" } })
	t.eq(r.cyclic, { "X", "Y" })
end)

t.test("suggestBreak cuts at the module with fewest dependencies", function()
	local edges = { A = { "B", "C", "D" }, B = { "A" }, C = {}, D = {} }
	local from, to = RequireGraph.suggestBreak(edges, { "A", "B" })
	t.eq(from, "B")
	t.eq(to, "A")
end)

t.done()
