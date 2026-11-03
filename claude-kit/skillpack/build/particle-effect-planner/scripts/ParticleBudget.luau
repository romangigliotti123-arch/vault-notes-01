--!strict
-- ParticleBudget: cost an effect before building it and judge a set of effects against a device tier. Pure logic, Lune-tested.
-- Vault (vfx KB, Creator Docs): max Rate per emitter 400/s desktop and 100/s mobile; default Rate 20/s; Lifetime above 20 s is
-- silently clamped; high emission with long lifetime and low speed is the classic overdraw trap; test at the lowest and highest
-- Editor Quality Level. The live-particle limits per tier below are THIS SKILL'S defaults (assumptions), tune them from a profile.
local ParticleBudget = {}

export type Effect = {
	name: string,
	rate: number, -- particles per second while emitting
	lifeMax: number, -- seconds (Lifetime.Max)
	burst: number?, -- particles per Emit() call
	bursts: number?, -- bursts that can overlap (e.g. 3 players hitting at once)
	emitters: number?, -- simultaneous copies in the scene
	loop: boolean?, -- true: emits continuously; false: one-shot bursts
}
export type Tier = "desktop" | "mobile"

ParticleBudget.RATE_CAP = { desktop = 400, mobile = 100 }
ParticleBudget.LIFE_CAP = 20
ParticleBudget.LIVE_BUDGET = { desktop = 2000, mobile = 500 } -- assumption: live particles across the whole scene

export type Cost = { name: string, live: number, issues: { string } }

-- Steady-state live particles of one effect (rate * lifetime), or burst * overlap for a one-shot.
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
