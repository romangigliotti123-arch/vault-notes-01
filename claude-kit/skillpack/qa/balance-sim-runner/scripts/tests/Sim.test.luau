--!nocheck
local t = require("../../../../../systems/_check/harness")
local Sim = require("../Sim")

print("Sim")

t.test("same seed gives the same stream, different seeds differ", function()
	local a, b, c = Sim.rng(7), Sim.rng(7), Sim.rng(8)
	for _ = 1, 20 do
		t.eq(a(), b())
	end
	t.truthy(Sim.rng(7)() ~= c())
end)

t.test("rng stays in [0,1)", function()
	local r = Sim.rng(1)
	for _ = 1, 5000 do
		local v = r()
		t.truthy(v >= 0 and v < 1)
	end
end)

t.test("weighted pick matches the weights within 2 percentage points over 20000 rolls", function()
	local r = Sim.rng(42)
	local counts = { 0, 0, 0 }
	for _ = 1, 20000 do
		local i = Sim.pick(r, { 70, 25, 5 })
		counts[i] += 1
	end
	t.truthy(math.abs(counts[1] / 20000 - 0.70) < 0.02)
	t.truthy(math.abs(counts[2] / 20000 - 0.25) < 0.02)
	t.truthy(math.abs(counts[3] / 20000 - 0.05) < 0.02)
end)

t.test("stats percentiles on a known list", function()
	local s = Sim.stats({ 5, 1, 3, 2, 4, 10, 9, 8, 7, 6 })
	t.eq(s.min, 1)
	t.eq(s.max, 10)
	t.eq(s.p50, 5)
	t.eq(s.p90, 9)
	t.eq(s.mean, 5.5)
end)

t.test("a 1 percent drop takes about 100 rolls on average and pity caps the worst case", function()
	local plain = Sim.monteCarlo(4000, 3, function(r)
		return Sim.rollsToTarget(r, { 99, 1 }, 2)
	end)
	t.truthy(plain.mean > 80 and plain.mean < 120)
	t.truthy(plain.max > 300)
	local pity = Sim.monteCarlo(4000, 3, function(r)
		return Sim.rollsToTarget(r, { 99, 1 }, 2, 150)
	end)
	t.truthy(pity.max <= 150)
	t.truthy(pity.mean < plain.mean)
end)

t.test("time to kill without crits is exact", function()
	local r = Sim.rng(1)
	t.eq(Sim.timeToKill(r, 100, 10, 2), 5)
end)

t.test("crits shorten the kill on average", function()
	local base = Sim.monteCarlo(500, 5, function(r)
		return Sim.timeToKill(r, 1000, 10, 1)
	end)
	local crit = Sim.monteCarlo(500, 5, function(r)
		return Sim.timeToKill(r, 1000, 10, 1, 0.3, 2)
	end)
	t.truthy(crit.mean < base.mean)
end)

t.test("seconds to goal: no upgrades is goal / income, upgrades help, zero income never arrives", function()
	t.eq(Sim.secondsToGoal(1000, 10, 0, 0, 1), 100)
	t.truthy(Sim.secondsToGoal(1000, 10, 5, 50, 1.2) < 100)
	t.eq(Sim.secondsToGoal(10, 0, 0, 0, 1), math.huge)
end)

t.done()
