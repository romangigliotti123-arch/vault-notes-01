--!strict
-- JoinTimeline: turn timestamped join milestones into phase durations, find the long pole and the blocking calls. Pure logic, Lune-tested.
-- Marks come from join_marks.luau (client) as {name, t} with t in seconds since the client script started.
-- Vault: Creator Docs test-on-hardware: "time the full join-to-gameplay flow on the baseline device; if loads exceed a few seconds consider instance streaming" (official,
-- "a few seconds" is not a number); scripting KB: never block character loading on third-party calls (an analytics outage caused 30 s waits at 15,000 CCU, creator report).
-- So there is NO built-in pass/fail seconds: pass your own `budgetSeconds` (a heuristic you set from the baseline run) and compare release to release.
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

-- longPole: the phase that ends at the milestone that took longest to reach. Fix this first.
function JoinTimeline.longPole(phases: { Phase }): Phase?
	local best: Phase? = nil
	for _, p in phases do
		if best == nil or p.seconds > best.seconds then
			best = p
		end
	end
	return best
end

-- verdict: compares total with a budget and with a previous run (both optional). Regressions above `tolerance` (default 10 percent, heuristic) are flagged.
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

-- blocking: phases whose name contains one of the substrings (for example "analytics", "datastore", "http") and that take over `limit` seconds.
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
