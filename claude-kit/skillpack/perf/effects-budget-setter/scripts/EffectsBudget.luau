--!strict
local EffectsBudget = {}

export type Emitter = {
	name: string,
	rate: number,
	lifeMin: number,
	lifeMax: number,
	enabled: boolean?,
	maxSize: number?,
}
export type Row = { name: string, live: number, share: number, suggestedRate: number }

EffectsBudget.CAPS = { low = 300, mid = 800, high = 2000 } :: { [string]: number }
EffectsBudget.HIGHLIGHT_CAP = 255

function EffectsBudget.live(e: Emitter): number
	if e.enabled == false then
		return 0
	end
	return e.rate * (e.lifeMin + e.lifeMax) / 2
end

function EffectsBudget.plan(emitters: { Emitter }, tier: string): ({ Row }, number, number)
	local cap = EffectsBudget.CAPS[tier]
	assert(cap ~= nil, "unknown tier " .. tier)
	local total = 0
	for _, e in emitters do
		total += EffectsBudget.live(e)
	end
	local scale = if total > cap then cap / total else 1
	local rows: { Row } = {}
	for _, e in emitters do
		local live = EffectsBudget.live(e)
		table.insert(rows, {
			name = e.name,
			live = live,
			share = if total > 0 then live / total else 0,
			suggestedRate = if live > 0 then math.max(1, math.floor(e.rate * scale)) else 0,
		})
	end
	table.sort(rows, function(a, b)
		if a.live ~= b.live then
			return a.live > b.live
		end
		return a.name < b.name
	end)
	return rows, total, cap
end

function EffectsBudget.highlightStatus(count: number): string
	if count > EffectsBudget.HIGHLIGHT_CAP then
		return "over-cap: extras are silently ignored"
	elseif count > EffectsBudget.HIGHLIGHT_CAP * 0.8 then
		return "near-cap"
	end
	return "ok"
end

return EffectsBudget
