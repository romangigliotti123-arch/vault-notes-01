--!strict
-- TickStats: summarise server Heartbeat samples (delta times in seconds) into FPS, percentile frame times, over-budget share and stall runs. Pure logic, Lune-tested.
-- Sources: Creator Docs performance-optimization/identify (official): the server heartbeat is capped at 60 FPS (16.67 ms) and anything lower suggests a performance issue;
-- production/analytics/performance: server CPU under 16 ms per frame for 60 FPS, server memory under 50 percent and under 3 GB; docs examples P90 server heartbeat 59 FPS, P10 40 FPS.
-- Optimisation KB: judge spikes and consistency, not average FPS (one 410 ms frame among 59 at 10 ms feels bad).
-- The 33 ms "stall" threshold (two missed 60 FPS frames) and the run length of 3 are this skill's heuristics.
local TickStats = {}

export type Summary = {
	frames: number,
	avgFps: number,
	avgMs: number,
	p95Ms: number,
	p99Ms: number,
	worstMs: number,
	overBudgetPct: number,
	longestStallRun: number,
	verdict: string,
}

local BUDGET_MS = 1000 / 60

local function percentile(sorted: { number }, p: number): number
	if #sorted == 0 then
		return 0
	end
	return sorted[math.max(1, math.min(#sorted, math.ceil(p * #sorted)))]
end

function TickStats.summarise(deltas: { number }): Summary
	local n = #deltas
	local ms: { number } = {}
	local sum, over, run, longest = 0, 0, 0, 0
	for i, d in deltas do
		local m = d * 1000
		ms[i] = m
		sum += m
		-- the 0.1 ms slack keeps a clean 60 Hz clock (16.67 ms) from counting as over budget
		if m > BUDGET_MS + 0.1 then
			over += 1
		end
		if m > 33 then
			run += 1
			longest = math.max(longest, run)
		else
			run = 0
		end
	end
	local sorted = table.clone(ms)
	table.sort(sorted)
	local avgMs = if n > 0 then sum / n else 0
	local summary: Summary = {
		frames = n,
		avgFps = if avgMs > 0 then 1000 / avgMs else 0,
		avgMs = avgMs,
		p95Ms = percentile(sorted, 0.95),
		p99Ms = percentile(sorted, 0.99),
		worstMs = sorted[n] or 0,
		overBudgetPct = if n > 0 then over / n * 100 else 0,
		longestStallRun = longest,
		verdict = "ok",
	}
	if n < 60 then
		summary.verdict = "too-few-samples"
	elseif summary.avgFps < 58 then
		summary.verdict = "slow-average"
	elseif longest >= 3 then
		summary.verdict = "stalls"
	elseif summary.p99Ms > 33 then
		summary.verdict = "spiky"
	end
	return summary
end

return TickStats
