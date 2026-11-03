--!strict
-- Sim: seeded Monte Carlo helpers for economy and combat balance, runnable under Lune (no Roblox APIs). Same seed = same numbers,
-- so a balance change can be compared like for like. All inputs are YOUR design numbers; nothing here is a Roblox statistic.
local Sim = {}

export type Rng = () -> number -- uniform in [0, 1)
export type Stats = { n: number, mean: number, min: number, max: number, p50: number, p90: number, p99: number }

-- small deterministic generator (Park-Miller / Lehmer, modulus 2^31-1)
function Sim.rng(seed: number): Rng
	local state = (math.floor(math.abs(seed)) % 2147483646) + 1
	return function()
		state = (state * 48271) % 2147483647
		return (state - 1) / 2147483646
	end
end

-- index of the picked weight (weights need not sum to 1)
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

-- run `trial(rng)` n times with one seeded stream; returns the stats of its numeric result
function Sim.monteCarlo(n: number, seed: number, trial: (rng: Rng) -> number): Stats
	local rng = Sim.rng(seed)
	local out = table.create(n)
	for i = 1, n do
		out[i] = trial(rng)
	end
	return Sim.stats(out)
end

-- Rolls until the first hit of `target` (index into weights), with optional pity: after `pity` misses the next roll is forced.
-- Returns the number of rolls. Use for "how many hatches until the rare pet".
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

-- Time to kill in seconds for one fighter: hp / (damage per hit * crit factor) hits, at hitsPerSecond, with random crits.
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

-- Seconds to afford a goal when income per second grows by `growth` per purchase of an upgrade costing `upgradeCost` (0 = no upgrades).
-- Deterministic; income = base + upgrades * perUpgrade. Returns seconds, and gives up (returns math.huge) after capSeconds.
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
		-- buy an upgrade only when it pays for itself before the goal is reached at the current income
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
