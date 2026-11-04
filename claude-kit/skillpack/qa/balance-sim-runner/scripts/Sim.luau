--!strict
local Sim = {}

export type Rng = () -> number
export type Stats = { n: number, mean: number, min: number, max: number, p50: number, p90: number, p99: number }

function Sim.rng(seed: number): Rng
	local state = (math.floor(math.abs(seed)) % 2147483646) + 1
	return function()
		state = (state * 48271) % 2147483647
		return (state - 1) / 2147483646
	end
end

function Sim.pick(rng: Rng, weights: { number }): number
	local total = 0
	for _, w in weights do
		total += w
	end
	local r = rng() * total
	for i, w in weights do
		r -= w
		if r < 0 then
			return i
		end
	end
	return #weights
end

local function percentile(sorted: { number }, p: number): number
	if #sorted == 0 then
		return 0
	end
	local idx = math.clamp(math.ceil(p * #sorted), 1, #sorted)
	return sorted[idx]
end

Sim.percentile = percentile

function Sim.stats(samples: { number }): Stats
	local sorted = table.clone(samples)
	table.sort(sorted)
	local sum = 0
	for _, v in sorted do
		sum += v
	end
	return {
		n = #sorted,
		mean = if #sorted > 0 then sum / #sorted else 0,
		min = sorted[1] or 0,
		max = sorted[#sorted] or 0,
		p50 = percentile(sorted, 0.5),
		p90 = percentile(sorted, 0.9),
		p99 = percentile(sorted, 0.99),
	}
end

function Sim.monteCarlo(n: number, seed: number, trial: (rng: Rng) -> number): Stats
	local rng = Sim.rng(seed)
	local out = table.create(n)
	for i = 1, n do
		out[i] = trial(rng)
	end
	return Sim.stats(out)
end

function Sim.rollsToTarget(rng: Rng, weights: { number }, target: number, pity: number?, cap: number?): number
	local misses, rolls = 0, 0
	local limit = cap or 1000000
	while rolls < limit do
		rolls += 1
		local got = Sim.pick(rng, weights)
		if got == target or (pity ~= nil and misses + 1 >= pity) then
			return rolls
		end
		misses += 1
	end
	return rolls
end

function Sim.timeToKill(
	rng: Rng,
	hp: number,
	damage: number,
	hitsPerSecond: number,
	critChance: number?,
	critMult: number?
): number
	local dealt, hits = 0, 0
	while dealt < hp and hits < 100000 do
		hits += 1
		local crit = critChance ~= nil and rng() < critChance
		dealt += damage * (if crit then (critMult or 2) else 1)
	end
	return hits / hitsPerSecond
end

function Sim.secondsToGoal(
	goal: number,
	baseIncome: number,
	perUpgrade: number,
	upgradeCost: number,
	upgradeGrowth: number,
	capSeconds: number?
): number
	local cap = capSeconds or 86400 * 30
	local coins, income, cost, t = 0, baseIncome, upgradeCost, 0
	if income <= 0 then
		return math.huge
	end
	while coins < goal do
		t += 1
		coins += income
		if upgradeCost > 0 and perUpgrade > 0 and coins >= cost and cost / perUpgrade < (goal - coins) / income then
			coins -= cost
			income += perUpgrade
			cost = math.ceil(cost * upgradeGrowth)
		end
		if t >= cap then
			return math.huge
		end
	end
	return t
end

return Sim
