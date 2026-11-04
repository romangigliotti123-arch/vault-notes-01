--!strict
local UpdateRate = {}

export type Ring = { maxDist: number, hz: number }

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

function UpdateRate.shouldUpdate(frameIndex: number, id: number, hz: number, frameRate: number?): boolean
	if hz <= 0 then
		return false
	end
	local fps = frameRate or 60
	local step = math.max(1, math.floor(fps / hz + 0.5))
	return (frameIndex + id) % step == 0
end

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

function UpdateRate.savedPercent(distances: { number }, rings: { Ring }?, frameRate: number?): number
	if #distances == 0 then
		return 0
	end
	return (1 - UpdateRate.updatesPerFrame(distances, rings, frameRate) / #distances) * 100
end

return UpdateRate
