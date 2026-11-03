--!strict
-- UpdateRate: distance-based update rings and frame-staggered scheduling for NPCs/AI/animation, so only a slice of the crowd runs each frame. Pure logic, Lune-tested.
-- Vault (optimization KB, creators): "animate NPCs only near the camera focus (test value 100 studs, final 500); NPCs outside stay parked; visual-only movement on the client
-- kept network near zero in a 200-NPC demo"; serial AI for 72 deer cost about 50 ms vs about 16 ms in parallel; Dead Rails halved server CPU by anchoring/disabling idle animators.
-- The RING table below (Hz per distance band) is this skill's DEFAULT, a heuristic to be tuned by profiler captures; the vault gives only the 100/500 stud examples.
local UpdateRate = {}

export type Ring = { maxDist: number, hz: number } -- hz 0 = parked (no updates)

UpdateRate.DEFAULT_RINGS = {
	{ maxDist = 100, hz = 30 },
	{ maxDist = 250, hz = 10 },
	{ maxDist = 500, hz = 3 },
	{ maxDist = math.huge, hz = 0 },
} :: { Ring }

function UpdateRate.hzFor(distance: number, rings: { Ring }?): number
	for _, r in rings or UpdateRate.DEFAULT_RINGS do
		if distance <= r.maxDist then
			return r.hz
		end
	end
	return 0
end

-- shouldUpdate: staggered by id so that the work spreads evenly across frames instead of every NPC updating on the same frame.
function UpdateRate.shouldUpdate(frameIndex: number, id: number, hz: number, frameRate: number?): boolean
	if hz <= 0 then
		return false
	end
	local fps = frameRate or 60
	local step = math.max(1, math.floor(fps / hz + 0.5))
	return (frameIndex + id) % step == 0
end

-- load: expected NPC updates per frame for a crowd (distances in studs), for budgeting against a ms-per-update cost you measured.
function UpdateRate.updatesPerFrame(distances: { number }, rings: { Ring }?, frameRate: number?): number
	local fps = frameRate or 60
	local total = 0
	for _, d in distances do
		local hz = UpdateRate.hzFor(d, rings)
		if hz > 0 then
			total += math.min(hz, fps) / fps
		end
	end
	return total
end

-- unthrottledPerFrame: the baseline (everyone, every frame) to compare with.
function UpdateRate.savedPercent(distances: { number }, rings: { Ring }?, frameRate: number?): number
	if #distances == 0 then
		return 0
	end
	return (1 - UpdateRate.updatesPerFrame(distances, rings, frameRate) / #distances) * 100
end

return UpdateRate
