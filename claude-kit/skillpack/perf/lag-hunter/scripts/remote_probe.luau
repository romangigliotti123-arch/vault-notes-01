--!strict
-- remote_probe.luau: SERVER-side. Counts how often each RemoteEvent is fired by clients for DURATION seconds and who fires it most,
-- by adding a second listener (the real handlers are untouched). Run during a playtest on the Server datamodel
-- (MCP `execute_luau` with datamodel_type Server) or paste into the command bar while a Studio server session runs.
-- Also samples server heartbeat time. Disconnects itself when done.
local DURATION = 20
local TOP = 8

local RunService = game:GetService("RunService")
local ReplicatedStorage = game:GetService("ReplicatedStorage")

if not RunService:IsServer() then
	return "remote_probe: run this on the Server datamodel during a playtest"
end

local counts: { [string]: { total: number, byPlayer: { [string]: number } } } = {}
local connections: { RBXScriptConnection } = {}

for _, inst in ReplicatedStorage:GetDescendants() do
	if inst:IsA("RemoteEvent") then
		local remote = inst :: RemoteEvent
		local key = remote:GetFullName()
		counts[key] = { total = 0, byPlayer = {} }
		table.insert(
			connections,
			remote.OnServerEvent:Connect(function(player: Player)
				local entry = counts[key]
				entry.total += 1
				entry.byPlayer[player.Name] = (entry.byPlayer[player.Name] or 0) + 1
			end)
		)
	end
end

local frames, slowest, sum = 0, 0, 0
local beat = RunService.Heartbeat:Connect(function(dt: number)
	frames += 1
	sum += dt
	if dt > slowest then
		slowest = dt
	end
end)

task.wait(DURATION)
beat:Disconnect()
for _, c in connections do
	c:Disconnect()
end

local rows = {}
for name, e in counts do
	if e.total > 0 then
		local topName, topN = "", 0
		for p, n in e.byPlayer do
			if n > topN then
				topName, topN = p, n
			end
		end
		table.insert(rows, { name = name, total = e.total, perSec = e.total / DURATION, top = topName, topN = topN })
	end
end
table.sort(rows, function(a, b)
	return a.total > b.total
end)

local lines = {
	`REMOTE PROBE {DURATION}s: heartbeat avg {string.format("%.1f", if frames > 0 then sum / frames * 1000 else 0)} ms, slowest {string.format(
		"%.1f",
		slowest * 1000
	)} ms over {frames} frames`,
}
if #rows == 0 then
	table.insert(lines, "no client->server remote traffic seen (the lag is not from RemoteEvents the clients fire)")
end
for i = 1, math.min(TOP, #rows) do
	local r = rows[i]
	table.insert(
		lines,
		`{r.name}: {r.total} calls ({string.format("%.1f", r.perSec)}/s), top sender {r.top} ({r.topN})`
	)
end
table.insert(
	lines,
	"Read: anything above ~10 calls/s per player from gameplay input deserves batching or a rate limit; the top sender being one player suggests an exploiter or a client bug."
)
local report = table.concat(lines, "\n")
print(report)
return report
