--!strict
local ParticleBudget = {}

export type Effect = {
	name: string,
	rate: number,
	lifeMax: number,
	burst: number?,
	bursts: number?,
	emitters: number?,
	loop: boolean?,
}
export type Tier = "desktop" | "mobile"

ParticleBudget.RATE_CAP = { desktop = 400, mobile = 100 }
ParticleBudget.LIFE_CAP = 20
ParticleBudget.LIVE_BUDGET = { desktop = 2000, mobile = 500 }

export type Cost = { name: string, live: number, issues: { string } }

function ParticleBudget.live(e: Effect): number
	local life = math.min(e.lifeMax, ParticleBudget.LIFE_CAP)
	local copies = e.emitters or 1
	if e.loop == false then
		return (e.burst or 0) * (e.bursts or 1) * copies
	end
	return e.rate * life * copies
end

function ParticleBudget.assess(e: Effect, tier: Tier): Cost
	local issues: { string } = {}
	local cap = ParticleBudget.RATE_CAP[tier]
	if e.rate > cap then
		table.insert(issues, `rate {e.rate}/s above the {tier} cap of {cap}/s (engine clamps it)`)
	end
	if e.lifeMax > ParticleBudget.LIFE_CAP then
		table.insert(issues, `lifetime {e.lifeMax}s above {ParticleBudget.LIFE_CAP}s (clamped silently)`)
	end
	if
		e.loop ~= false
		and e.rate * math.min(e.lifeMax, ParticleBudget.LIFE_CAP) > ParticleBudget.LIVE_BUDGET[tier] / 4
	then
		table.insert(
			issues,
			"one effect uses over a quarter of the scene budget: lower rate or lifetime, raise size and speed"
		)
	end
	return { name = e.name, live = ParticleBudget.live(e), issues = issues }
end

export type Plan = { totalLive: number, budget: number, over: boolean, costs: { Cost }, heaviest: string? }

function ParticleBudget.plan(effects: { Effect }, tier: Tier): Plan
	local costs: { Cost } = {}
	local total, heaviest, heavyLive = 0, nil :: string?, -1
	for _, e in effects do
		local c = ParticleBudget.assess(e, tier)
		table.insert(costs, c)
		total += c.live
		if c.live > heavyLive then
			heaviest, heavyLive = e.name, c.live
		end
	end
	local budget = ParticleBudget.LIVE_BUDGET[tier]
	return { totalLive = total, budget = budget, over = total > budget, costs = costs, heaviest = heaviest }
end

return ParticleBudget
