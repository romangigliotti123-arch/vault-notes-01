--!nocheck
-- Run: lune run NetBudget.test.luau   (from the kit's systems folder, see check-scripts.sh)
local t = require("../../../../../systems/_check/harness")
local NetBudget = require("../NetBudget")

t.test("payload bytes follow the documented sizes", function()
	t.eq(NetBudget.payloadBytes({ "cframe" }), 20)
	t.eq(NetBudget.payloadBytes({ "vector3int16", "int16" }), 8)
	t.eq(NetBudget.payloadBytes({ "string", "boolean" }, 30), 31)
end)

t.test("switching CFrame to Vector3int16 cuts a 20 Hz stream by 70 percent", function()
	local rows = NetBudget.audit({
		{ name = "A", fields = { "cframe" }, hz = 20 },
		{ name = "B", fields = { "vector3int16" }, hz = 20 },
	}, 10)
	t.eq(rows[1].name, "A")
	t.truthy(math.abs(rows[2].bytes / rows[1].bytes - 0.3) < 1e-9)
end)

t.test("rows rank by total server send and per-client total drives the status", function()
	local rows, perClient = NetBudget.audit({
		{ name = "Chat", fields = { "string" }, hz = 1, receivers = 1 },
		{ name = "Pos", fields = { "vector3", "number" }, hz = 30 },
	}, 20)
	t.eq(rows[1].name, "Pos")
	t.eq(NetBudget.status(perClient), "ok")
	t.eq(NetBudget.status(51), "over")
	t.eq(NetBudget.status(31), "warn")
end)

t.test("unknown field types fail loudly", function()
	local ok = pcall(NetBudget.payloadBytes, { "matrix" })
	t.falsy(ok)
end)

t.test("batching reports calls saved", function()
	t.eq(NetBudget.batchedCalls(60, 10), 50)
	t.eq(NetBudget.batchedCalls(5, 10), 0)
end)

t.done()
