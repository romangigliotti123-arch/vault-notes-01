--!strict
local BillboardFade = {}

export type Candidate = { id: string, distance: number, priority: number? }
export type Options = { maxCount: number, maxDistance: number, previous: { [string]: boolean }?, slack: number? }

function BillboardFade.transparency(distance: number, fadeStart: number, fadeEnd: number): number
	if fadeEnd <= fadeStart then
		return if distance > fadeEnd then 1 else 0
	end
	return math.clamp((distance - fadeStart) / (fadeEnd - fadeStart), 0, 1)
end

function BillboardFade.select(candidates: { Candidate }, options: Options): ({ [string]: boolean }, { string })
	local slack = options.slack or 3
	local previous = options.previous or {}
	local eligible: { { id: string, rank: number, priority: number } } = {}
	for _, c in candidates do
		if c.distance <= options.maxDistance then
			local rank = c.distance - (if previous[c.id] then slack else 0)
			table.insert(eligible, { id = c.id, rank = rank, priority = c.priority or 0 })
		end
	end
	table.sort(eligible, function(a, b)
		if a.priority ~= b.priority then
			return a.priority > b.priority
		end
		if a.rank ~= b.rank then
			return a.rank < b.rank
		end
		return a.id < b.id
	end)
	local set: { [string]: boolean } = {}
	local list: { string } = {}
	for i = 1, math.min(options.maxCount, #eligible) do
		set[eligible[i].id] = true
		table.insert(list, eligible[i].id)
	end
	return set, list
end

function BillboardFade.changes(
	previous: { [string]: boolean },
	current: { [string]: boolean }
): ({ string }, { string })
	local enable, disable = {}, {}
	for id in current do
		if not previous[id] then
			table.insert(enable, id)
		end
	end
	for id in previous do
		if not current[id] then
			table.insert(disable, id)
		end
	end
	table.sort(enable)
	table.sort(disable)
	return enable, disable
end

return BillboardFade
