--!strict
-- tick_sampler.luau: SERVER Script (or MCP `execute_luau` on the Server datamodel during a playtest). Samples Heartbeat delta time for DURATION seconds and prints a summary
-- (average FPS, p95/p99/worst frame ms, share over the 16.67 ms budget, longest run of frames over 33 ms) and the raw delta list for TickStats.summarise
-- (server-tick-analyzer/scripts/TickStats.luau). It also prints Stats heartbeat if available. Compare against the Performance dashboard's server heartbeat (60 FPS is the cap).
-- Run it twice: idle server and the busy scenario (many players/NPCs/effects) so the difference points at load, not at the sampler.
local DURATION = 30

local RunService = game:GetService("RunService")
if not RunService:IsServer() then
	return "tick_sampler: run this on the Server datamodel during a playtest"
end

local deltas: { number } = {}
local conn = RunService.Heartbeat:Connect(function(dt: number)
	table.insert(deltas, dt)
end)
task.wait(DURATION)
conn:Disconnect()

local n = #deltas
local ms: { number } = {}
local sum, over, run, longest = 0, 0, 0, 0
for i, d in deltas do
	ms[i] = d * 1000
	sum += ms[i]
	if ms[i] > 1000 / 60 + 0.1 then
		over += 1
	end
	if ms[i] > 33 then
		run += 1
		longest = math.max(longest, run)
	else
		run = 0
	end
end
table.sort(ms)
local function pct(p: number): number
	return ms[math.max(1, math.min(n, math.ceil(p * n)))] or 0
end
local avg = if n > 0 then sum / n else 0
print(
	("[tick] frames=%d avgFps=%.1f p95=%.1fms p99=%.1fms worst=%.1fms over16.7ms=%.1f%% longestRunOver33ms=%d"):format(
		n,
		if avg > 0 then 1000 / avg else 0,
		pct(0.95),
		pct(0.99),
		ms[n] or 0,
		if n > 0 then over / n * 100 else 0,
		longest
	)
)
local sample = {}
for i = 1, math.min(n, 600) do
	sample[i] = ("%.4f"):format(deltas[i])
end
print("[tick] first 600 deltas: { " .. table.concat(sample, ", ") .. " }")
return "tick_sampler done"
