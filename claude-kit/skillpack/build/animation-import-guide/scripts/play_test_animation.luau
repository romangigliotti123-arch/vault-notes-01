--!strict
local ANIMATION_ID = ""
local RIG: Model? = nil
local PLAY_SECONDS = 0.6

local function findAnimator(): Animator?
	if RIG then
		return RIG:FindFirstChildWhichIsA("Animator", true)
	end
	for _, inst in workspace:GetDescendants() do
		if inst:IsA("Animator") then
			return inst
		end
	end
	return nil
end

local function run(): string
	if ANIMATION_ID == "" then
		return "PLAY TEST: set ANIMATION_ID to the uploaded animation first (rbxassetid://<number>)"
	end
	local animator = findAnimator()
	if not animator then
		return "PLAY TEST: no Animator found. Run in play mode (server) with a rig in Workspace, or set RIG."
	end
	local anim = Instance.new("Animation")
	anim.AnimationId = ANIMATION_ID
	local ok, track = pcall(function()
		return animator:LoadAnimation(anim)
	end)
	if not ok then
		anim:Destroy()
		return `PLAY TEST: load failed ({tostring(track)}). Check the id, that the rig owner owns the animation, and that it is published.`
	end
	local keyframes: { string } = {}
	local conn = track.KeyframeReached:Connect(function(name: string)
		table.insert(keyframes, name)
	end)
	track:Play()
	local before = track.TimePosition
	task.wait(PLAY_SECONDS)
	local playing, after = track.IsPlaying, track.TimePosition
	local reached = if #keyframes > 0
		then table.concat(keyframes, ", ")
		else "none (normal if the clip has no named keyframes)"
	local lines = {
		`PLAY TEST: {ANIMATION_ID} on {animator:GetFullName()}`,
		`length={string.format("%.2f", track.Length)}s looped={track.Looped} priority={track.Priority.Name}`,
		`playing after {PLAY_SECONDS}s: {playing}; time advanced {string.format("%.2f", after - before)}s`,
		`keyframes reached: {reached}`,
	}
	if track.Length <= 0 then
		table.insert(lines, "PROBLEM: length 0, the asset is empty or not loaded")
	end
	if not playing and not track.Looped then
		table.insert(lines, "note: a non-looping clip shorter than the wait has already finished")
	end
	conn:Disconnect()
	track:Stop()
	track:Destroy()
	anim:Destroy()
	table.insert(lines, "test only: track stopped and destroyed, nothing saved")
	return table.concat(lines, "\n")
end

local report = run()
print(report)
return report
