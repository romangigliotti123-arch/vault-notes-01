--!nocheck
-- Run from the kit's systems folder: lune run ../skillpack/qa/load-test-planner/scripts/tests/LoadMath.test.luau
local t = require("../../../../../systems/_check/harness")
local LoadMath = require("../LoadMath")

print("LoadMath")

t.test("totals add messages and bytes per remote", function()
	local plan = {
		clients = 50,
		traffic = {
			{ name = "Move", perClientPerSec = 10, bytesPerMessage = 24 },
			{ name = "Chat", perClientPerSec = 0.1, bytesPerMessage = 80 },
		},
	}
	local tot = LoadMath.totals(plan)
	t.eq(tot.messagesPerSec, 505)
	t.eq(tot.bytesPerSec, 50 * 10 * 24 + 50 * 0.1 * 80)
	t.eq(tot.byRemote.Move, 500)
	t.eq(tot.perClientBytesPerSec, (50 * 10 * 24 + 50 * 0.1 * 80) / 50)
	t.truthy(string.find(LoadMath.report(plan, tot), "50 clients", 1, true))
end)

t.test("worst case assumes every client at every limit", function()
	t.eq(LoadMath.worstCase(100, { Buy = 2, Move = 20 }), 2200)
end)

t.test("ramp grows by the factor and ends exactly on the maximum", function()
	local steps = LoadMath.ramp(2, 40, 2, 120)
	local counts = {}
	for _, s in steps do
		table.insert(counts, s.clients)
	end
	t.eq(counts, { 2, 4, 8, 16, 32, 40 })
	t.eq(steps[1].holdSeconds, 120)
	t.falsy(pcall(LoadMath.ramp, 5, 40, 1, 10))
end)

t.test("ramp still advances when the factor rounds to no growth", function()
	local steps = LoadMath.ramp(1, 4, 1.1, 10)
	t.eq(#steps, 4)
end)

t.test("verdicts handle lower-is-better and higher-is-better budgets", function()
	local v = LoadMath.verdicts({
		{ name = "heartbeat ms", measured = 12, limit = 16 },
		{ name = "memory MB", measured = 900, limit = 800 },
		{ name = "fps", measured = 45, limit = 30, higherIsWorse = false },
	})
	t.truthy(v[1].ok)
	t.falsy(v[2].ok)
	t.truthy(v[3].ok)
	t.truthy(v[1].headroom > 0.2 and v[1].headroom < 0.3)
	t.truthy(v[2].headroom < 0)
end)

t.test("safe capacity is the last step before the first failure", function()
	t.eq(
		LoadMath.safeCapacity({
			{ clients = 10, ok = true },
			{ clients = 20, ok = true },
			{ clients = 40, ok = false },
			{ clients = 80, ok = true },
		}),
		20
	)
	t.eq(LoadMath.safeCapacity({ { clients = 10, ok = false } }), 0)
end)

t.done()
