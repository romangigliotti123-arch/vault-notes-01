--!strict
local Workspace = game:GetService("Workspace")
local Players = game:GetService("Players")

local BANDS = { 100, 250, 500 }

local focus = Vector3.zero
local player = Players:GetPlayers()[1]
if player and player.Character and player.Character.PrimaryPart then
	focus = player.Character.PrimaryPart.Position
end

local rigs, humanoids, withTracks, tracksTotal, idleAnimators = 0, 0, 0, 0, 0
local bands: { number } = { 0, 0, 0, 0 }
local worst: { { name: string, tracks: number } } = {}

for _, inst in Workspace:GetDescendants() do
	if inst:IsA("Animator") then
		rigs += 1
		local animator = inst :: Animator
		local model = animator:FindFirstAncestorOfClass("Model")
		local tracks = #animator:GetPlayingAnimationTracks()
		tracksTotal += tracks
		if tracks > 0 then
			withTracks += 1
			table.insert(worst, { name = animator:GetFullName(), tracks = tracks })
		else
			idleAnimators += 1
		end
		if model and model.PrimaryPart then
			local d = (model.PrimaryPart.Position - focus).Magnitude
			local idx = #BANDS + 1
			for i, limit in BANDS do
				if d <= limit then
					idx = i
					break
				end
			end
			bands[idx] += 1
		end
	elseif inst:IsA("Humanoid") then
		humanoids += 1
	end
end
table.sort(worst, function(a, b)
	return a.tracks > b.tracks
end)

local lines = {
	("Animators=%d Humanoids=%d  playing-tracks total=%d  animators with tracks=%d  idle animators=%d"):format(
		rigs,
		humanoids,
		tracksTotal,
		withTracks,
		idleAnimators
	),
	("ClientAnimatorThrottling=%s (docs/creators: enable for distant animators)"):format(
		tostring(Workspace.ClientAnimatorThrottling)
	),
	("Rigs by distance from focus: <=%d: %d  <=%d: %d  <=%d: %d  beyond: %d"):format(
		BANDS[1],
		bands[1],
		BANDS[2],
		bands[2],
		BANDS[3],
		bands[3],
		bands[4]
	),
	"Most tracks playing:",
}
for i = 1, math.min(6, #worst) do
	table.insert(lines, ("  %2d  %s"):format(worst[i].tracks, worst[i].name))
end
return table.concat(lines, "\n")
