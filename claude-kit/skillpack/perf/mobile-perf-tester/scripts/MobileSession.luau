--!strict
-- MobileSession: analyse a 10-15 minute on-device sample log (frame ms + memory MB) for averages, spikes, thermal decline and memory growth.
-- Pure logic, Lune-tested. Samples come from mobile_sampler.client.luau (or the Performance Stats overlay copied by hand).
-- Sources (vault): Creator Docs test-on-hardware: run a 10-15 minute session and watch for steady FPS decline (thermal throttling) (official);
-- frame budget 16.67 ms at 60 FPS, 33.33 ms at 30 FPS; judge spikes and consistency, not average FPS (optimization KB, creators);
-- a 10 ms PC frame can be about 40 ms on a low-end phone (scripting KB, creator report). The 25 percent thermal flag and 2x spike rule are heuristics.
local MobileSession = {}

export type Sample = { t: number, frameMs: number, memMB: number }
export type Report = {
	samples: number,
	minutes: number,
	avgMs: number,
	p95Ms: number,
	worstMs: number,
	overBudgetPct: number,
	spikes: number,
	thermalDeclinePct: number,
	memStartMB: number,
	memEndMB: number,
	memGrowthMBPerMin: number,
	flags: { string },
}

local function percentile(sorted: { number }, p: number): number
	if #sorted == 0 then
		return 0
	end
	local idx = math.max(1, math.min(#sorted, math.ceil(p * #sorted)))
	return sorted[idx]
end

local function mean(xs: { number }, from: number, to: number): number
	local sum, n = 0, 0
	for i = from, to do
		sum += xs[i]
		n += 1
	end
	return if n > 0 then sum / n else 0
end

function MobileSession.analyze(samples: { Sample }, budgetMs: number?): Report
	local budget = budgetMs or 33.33 -- default target for phones is 30 FPS; pass 16.67 for a 60 FPS goal
	local flags: { string } = {}
	local n = #samples
	local ms: { number } = {}
	local over, spikes = 0, 0
	for i, s in samples do
		ms[i] = s.frameMs
		if s.frameMs > budget then
			over += 1
		end
		if s.frameMs > budget * 2 then
			spikes += 1
		end
	end
	local sorted = table.clone(ms)
	table.sort(sorted)
	local third = math.max(1, n // 3)
	local early = mean(ms, 1, math.min(n, third))
	local late = mean(ms, math.max(1, n - third + 1), n)
	local decline = if early > 0 then (late - early) / early * 100 else 0
	local minutes = if n >= 2 then (samples[n].t - samples[1].t) / 60 else 0
	local memStart = if n > 0 then samples[1].memMB else 0
	local memEnd = if n > 0 then samples[n].memMB else 0
	local growth = if minutes > 0 then (memEnd - memStart) / minutes else 0
	local report: Report = {
		samples = n,
		minutes = minutes,
		avgMs = mean(ms, 1, math.max(1, n)),
		p95Ms = percentile(sorted, 0.95),
		worstMs = sorted[n] or 0,
		overBudgetPct = if n > 0 then over / n * 100 else 0,
		spikes = spikes,
		thermalDeclinePct = decline,
		memStartMB = memStart,
		memEndMB = memEnd,
		memGrowthMBPerMin = growth,
		flags = flags,
	}
	if minutes < 10 then
		table.insert(flags, "short-session: under 10 minutes cannot show thermal throttling")
	end
	if decline > 25 then
		table.insert(flags, "thermal-decline: late frames are slower than early frames by more than 25 percent")
	end
	if report.p95Ms > budget then
		table.insert(flags, "p95-over-budget")
	end
	if spikes > 0 then
		table.insert(flags, "spikes: " .. spikes .. " frames over twice the budget")
	end
	if growth > 1 then
		table.insert(flags, "memory-growth: over 1 MB per minute; run instance-leak-finder")
	end
	return report
end

return MobileSession
