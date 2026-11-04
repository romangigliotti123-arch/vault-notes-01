--!strict
local JoinTimeline = {}

export type Mark = { name: string, t: number }
export type Phase = { from: string, to: string, seconds: number, share: number }

function JoinTimeline.phases(marks: { Mark }): ({ Phase }, number)
	local sorted = table.clone(marks)
	table.sort(sorted, function(a, b)
		return a.t < b.t
	end)
	local out: { Phase } = {}
	if #sorted < 2 then
		return out, 0
	end
	local total = sorted[#sorted].t - sorted[1].t
	for i = 2, #sorted do
		local secs = sorted[i].t - sorted[i - 1].t
		table.insert(out, {
			from = sorted[i - 1].name,
			to = sorted[i].name,
			seconds = secs,
			share = if total > 0 then secs / total else 0,
		})
	end
	return out, total
end

function JoinTimeline.longPole(phases: { Phase }): Phase?
	local best: Phase? = nil
	for _, p in phases do
		if best == nil or p.seconds > best.seconds then
			best = p
		end
	end
	return best
end

function JoinTimeline.verdict(total: number, budgetSeconds: number?, previousTotal: number?, tolerance: number?): string
	local tol = tolerance or 0.1
	if budgetSeconds and total > budgetSeconds then
		return "over-budget"
	end
	if previousTotal and previousTotal > 0 and total > previousTotal * (1 + tol) then
		return "regressed"
	end
	if previousTotal and previousTotal > 0 and total < previousTotal * (1 - tol) then
		return "improved"
	end
	return "ok"
end

function JoinTimeline.blocking(phases: { Phase }, needles: { string }, limit: number): { Phase }
	local out: { Phase } = {}
	for _, p in phases do
		if p.seconds > limit then
			local label = string.lower(p.from .. " " .. p.to)
			for _, n in needles do
				if string.find(label, string.lower(n), 1, true) then
					table.insert(out, p)
					break
				end
			end
		end
	end
	return out
end

return JoinTimeline
