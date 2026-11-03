--!strict
-- FloatingNumbers: the bookkeeping for damage/reward popups: merge rapid hits on one target, spread simultaneous numbers into lanes
-- so they do not stack, cap the live count, and expire by age. Pure; creating/recycling the actual labels is the caller's job (use
-- the pack's object-pool-builder Pool for the frames) and `active` tells it what to draw.
--   local f = FloatingNumbers.new({ mergeWindow = 0.25, maxActive = 24, lifetime = 0.9, lanes = 3 })
--   local ev = f:spawn("goblin1", 12, "damage", now)     -- ev.id, ev.total, ev.lane, ev.merged
--   f:tick(now)                                          -- removes expired; returns the active list
local FloatingNumbers = {}
FloatingNumbers.__index = FloatingNumbers

export type Number = {
	id: number,
	target: string,
	kind: string,
	total: number,
	born: number,
	lastHit: number,
	lane: number,
	crit: boolean,
}
export type Options = { mergeWindow: number?, maxActive: number?, lifetime: number?, lanes: number? }
export type Feed = typeof(setmetatable(
	{} :: {
		_merge: number,
		_max: number,
		_life: number,
		_lanes: number,
		_active: { Number },
		_nextId: number,
		_laneCounter: number,
	},
	FloatingNumbers
))

function FloatingNumbers.new(options: Options?): Feed
	local o: Options = options or {}
	return setmetatable({
		_merge = o.mergeWindow or 0.25,
		_max = o.maxActive or 24,
		_life = o.lifetime or 0.9,
		_lanes = math.max(1, o.lanes or 3),
		_active = {},
		_nextId = 1,
		_laneCounter = 0,
	}, FloatingNumbers)
end

-- Same target + kind inside the merge window adds into the existing number (it stays on screen, its clock extended from lastHit).
function FloatingNumbers.spawn(
	self: Feed,
	target: string,
	amount: number,
	kind: string,
	now: number,
	crit: boolean?
): (Number, boolean)
	for _, n in self._active do
		if n.target == target and n.kind == kind and now - n.lastHit <= self._merge then
			n.total += amount
			n.lastHit = now
			n.crit = n.crit or crit == true
			return n, true
		end
	end
	if #self._active >= self._max then
		table.remove(self._active, 1) -- drop the oldest rather than growing without limit
	end
	self._laneCounter += 1
	local n: Number = {
		id = self._nextId,
		target = target,
		kind = kind,
		total = amount,
		born = now,
		lastHit = now,
		lane = (self._laneCounter - 1) % self._lanes,
		crit = crit == true,
	}
	self._nextId += 1
	table.insert(self._active, n)
	return n, false
end

-- Horizontal offset (px) for a lane, centred: lanes 3, spacing 24 -> -24, 0, 24.
function FloatingNumbers.laneOffset(self: Feed, lane: number, spacing: number): number
	return (lane - (self._lanes - 1) / 2) * spacing
end

-- 0..1 life progress for animation (rise and fade).
function FloatingNumbers.progress(self: Feed, n: Number, now: number): number
	return math.clamp((now - n.born) / self._life, 0, 1)
end

function FloatingNumbers.tick(self: Feed, now: number): { Number }
	for i = #self._active, 1, -1 do
		if now - self._active[i].born >= self._life and now - self._active[i].lastHit >= self._merge then
			table.remove(self._active, i)
		end
	end
	return self._active
end

return FloatingNumbers
