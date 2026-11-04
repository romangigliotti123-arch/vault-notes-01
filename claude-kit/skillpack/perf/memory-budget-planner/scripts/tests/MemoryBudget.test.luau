--!nocheck
local t = require("../../../../../systems/_check/harness")
local MemoryBudget = require("../MemoryBudget")

t.test("2 GB device ceiling is 66 percent and target is 450 MB", function()
	local tier = MemoryBudget.clientTier(2)
	t.eq(tier.ceilingMB, 1351)
	t.eq(tier.targetMB, 450)
end)

t.test("client assessment bands", function()
	local tier = MemoryBudget.clientTier(2)
	t.eq(MemoryBudget.assessClient(400, tier), "ok")
	t.eq(MemoryBudget.assessClient(600, tier), "over-target")
	t.eq(MemoryBudget.assessClient(1000, tier), "risk")
	t.eq(MemoryBudget.assessClient(1400, tier), "ejection-zone")
end)

t.test("server formula matches the docs example of 30 players", function()
	local gib = MemoryBudget.serverTotalMB(30) / 1024
	t.truthy(math.abs(gib - 9.18) < 0.01, "expected about 9.18 GiB, got " .. gib)
	t.eq(MemoryBudget.assessServer(MemoryBudget.serverTotalMB(30) * 0.6, 30), "over")
	t.eq(MemoryBudget.assessServer(MemoryBudget.serverTotalMB(30) * 0.45, 30), "warn")
	t.eq(MemoryBudget.assessServer(100, 30), "ok")
end)

t.test("breakdown sorts biggest first and shares add to one", function()
	local rows = MemoryBudget.breakdown({ PlaceMemory = 300, Sounds = 100, Scripts = 100 })
	t.eq(rows[1].name, "PlaceMemory")
	t.eq(rows[2].name, "Scripts")
	t.truthy(math.abs(rows[1].share + rows[2].share + rows[3].share - 1) < 1e-9)
end)

t.test("larger devices get larger targets", function()
	t.truthy(MemoryBudget.clientTier(4).targetMB > MemoryBudget.clientTier(2).targetMB)
end)

t.done()
