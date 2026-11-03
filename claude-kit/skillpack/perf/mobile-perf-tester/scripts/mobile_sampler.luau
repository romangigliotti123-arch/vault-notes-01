--!strict
-- mobile_sampler.luau: CLIENT LocalScript for an on-device session (StarterPlayerScripts; remove before publishing). Once per second it records the average frame time
-- of the last second and total client memory, then prints one CSV line per sample ("t,frameMs,memMB") so the log can be copied from the device console / Developer Console (F9)
-- and fed to MobileSession.analyze (mobile-perf-tester/scripts/MobileSession.luau). Default length is 12 minutes, inside the docs' 10-15 minute thermal-test window.
-- Memory here is Stats:GetTotalMemoryUsageMb(): compare it with the Developer Console Memory tab (PlaceMemory) on the same device.
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
