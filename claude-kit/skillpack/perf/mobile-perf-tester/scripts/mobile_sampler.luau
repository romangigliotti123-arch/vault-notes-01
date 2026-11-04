--!strict
local DURATION_SECONDS = 12 * 60

local RunService = game:GetService("RunService")
local Stats = game:GetService("Stats")

local started = os.clock()
local frames, accum = 0, 0
local worst = 0

print("[mobile] t,frameMs,memMB,worstFrameMs")
local conn: RBXScriptConnection
conn = RunService.RenderStepped:Connect(function(dt: number)
	frames += 1
	accum += dt
	worst = math.max(worst, dt)
end)

task.spawn(function()
	local second = 0
	while os.clock() - started < DURATION_SECONDS do
		task.wait(1)
		second += 1
		local frameMs = if frames > 0 then accum / frames * 1000 else 0
		print(("[mobile] %d,%.2f,%.1f,%.1f"):format(second, frameMs, Stats:GetTotalMemoryUsageMb(), worst * 1000))
		frames, accum, worst = 0, 0, 0
	end
	conn:Disconnect()
	print("[mobile] done: paste the lines into MobileSession.analyze")
end)
