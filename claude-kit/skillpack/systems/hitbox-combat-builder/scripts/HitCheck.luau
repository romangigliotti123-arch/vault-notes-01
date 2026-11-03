--!strict
-- HitCheck: the server's yes/no on a claimed hit. Range with a lag allowance (a moving target may be further on the server than on the
-- attacker's screen), a facing-angle limit for non-area attacks, an optional wall check (injected raycast), and once-per-swing
-- de-duplication so one swing cannot hit the same target twice. Positions are plain {x,y,z}; look vectors are unit length.
--   local hits = HitCheck.new({ maxLag = 0.2, now = os.clock })
--   local ok, why = hits:check({ swingId = id, attacker = a, target = tg, look = look, range = 8, targetSpeed = 16, lag = 0.1, maxAngle = 70 })
local HitCheck = {}
HitCheck.__index = HitCheck

export type Pos = { x: number, y: number, z: number }
export type Claim = {
	swingId: string,
	attacker: Pos,
	target: Pos,
	look: Pos?, -- attacker's look direction (unit); nil for area attacks
	range: number,
	targetSpeed: number?, -- server-known speed of the target, studs/s
	lag: number?, -- attacker ping in seconds as measured by the server
	maxAngle: number?, -- degrees; default 90
	blocked: boolean?, -- result of the server raycast between them, if the glue ran one
}
export type Config = { maxLag: number, swingTtl: number?, now: () -> number }
export type HitCheck = typeof(setmetatable({} :: { _c: Config, _seen: { [string]: number } }, HitCheck))

function HitCheck.new(config: Config): HitCheck
	assert(config.maxLag >= 0 and config.maxLag <= 1, "maxLag must be 0..1 s (more is an exploit window)")
	return setmetatable({ _c = config, _seen = {} }, HitCheck)
end

local function sub(a: Pos, b: Pos): Pos
	return { x = a.x - b.x, y = a.y - b.y, z = a.z - b.z }
end

local function len(v: Pos): number
	return math.sqrt(v.x * v.x + v.y * v.y + v.z * v.z)
end

local function finite(p: Pos): boolean
	for _, n in { p.x, p.y, p.z } do
		if n ~= n or n == math.huge or n == -math.huge then
			return false
		end
	end
	return true
end

-- allowed distance: range plus what a target at its known speed could have moved during the (capped) lag
function HitCheck.allowedRange(self: HitCheck, range: number, speed: number?, lag: number?): number
	local l = math.min(math.max(lag or 0, 0), self._c.maxLag)
	return range + (speed or 0) * l
end

function HitCheck.check(self: HitCheck, c: Claim): (boolean, string)
	if not (finite(c.attacker) and finite(c.target)) then
		return false, "bad position"
	end
	local now = self._c.now()
	local ttl = self._c.swingTtl or 5
	for k, at in self._seen do
		if now - at > ttl then
			self._seen[k] = nil
		end
	end
	if self._seen[c.swingId] then
		return false, "swing already hit"
	end
	local delta = sub(c.target, c.attacker)
	local d = len(delta)
	if d > self:allowedRange(c.range, c.targetSpeed, c.lag) then
		return false, "out of range"
	end
	if c.look and d > 0.001 then
		local dot = (delta.x * c.look.x + delta.y * c.look.y + delta.z * c.look.z) / d
		local angle = math.deg(math.acos(math.clamp(dot, -1, 1)))
		if angle > (c.maxAngle or 90) then
			return false, "not facing"
		end
	end
	if c.blocked then
		return false, "blocked"
	end
	self._seen[c.swingId] = now
	return true, "hit"
end

return HitCheck
