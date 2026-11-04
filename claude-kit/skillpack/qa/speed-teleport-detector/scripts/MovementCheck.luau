--!strict
local MovementCheck = {}
MovementCheck.__index = MovementCheck

export type Vec = { x: number, y: number, z: number }
export type Verdict = {
	kind: "ok" | "speed" | "fly" | "teleport" | "exempt",
	excess: number,
	resetTo: Vec?,
}

export type Config = {
	baseSpeed: number?,
	margin: number?,
	jumpSpeed: number?,
	teleportDistance: number?,
	maxAirtime: number?,
	minDt: number?,
	maxDt: number?,
}

type State = {
	pos: Vec,
	t: number,
	speed: number?,
	exemptUntil: number,
	airSince: number?,
}

export type MovementCheck = typeof(setmetatable({} :: { _c: Config, _s: { [any]: State } }, MovementCheck))

function MovementCheck.new(config: Config?): MovementCheck
	return setmetatable({ _c = config or {}, _s = {} }, MovementCheck)
end

local function copy(v: Vec): Vec
	return { x = v.x, y = v.y, z = v.z }
end

local function finite(v: Vec): boolean
	for _, n in { v.x, v.y, v.z } do
		if n ~= n or n == math.huge or n == -math.huge then
			return false
		end
	end
	return true
end

function MovementCheck.SetSpeed(self: MovementCheck, key: any, speed: number?)
	local st = self._s[key]
	if st then
		st.speed = speed
	end
end

function MovementCheck.Exempt(self: MovementCheck, key: any, seconds: number, now: number)
	local st = self._s[key]
	if st then
		st.exemptUntil = math.max(st.exemptUntil, now + seconds)
	end
end

function MovementCheck.Clear(self: MovementCheck, key: any)
	self._s[key] = nil
end

function MovementCheck.Sample(self: MovementCheck, key: any, pos: Vec, t: number, airborne: boolean?): Verdict
	local c = self._c
	local st = self._s[key]
	if not finite(pos) then
		return { kind = "teleport", excess = math.huge, resetTo = if st then copy(st.pos) else nil }
	end
	if st == nil then
		self._s[key] = { pos = copy(pos), t = t, exemptUntil = 0 }
		return { kind = "ok", excess = 0 }
	end
	local dt = t - st.t
	if dt < (c.minDt or 0.1) then
		return { kind = "ok", excess = 0 }
	end
	if t < st.exemptUntil or dt > (c.maxDt or 5) then
		st.pos, st.t, st.airSince = copy(pos), t, nil
		return { kind = "exempt", excess = 0 }
	end
	local margin = c.margin or 2
	local dx, dz = pos.x - st.pos.x, pos.z - st.pos.z
	local horizontal = math.sqrt(dx * dx + dz * dz)
	local rise = pos.y - st.pos.y
	local allowedH = (st.speed or c.baseSpeed or 16) * dt + margin
	local allowedUp = (c.jumpSpeed or 60) * dt + margin
	local kind: "ok" | "speed" | "fly" | "teleport" = "ok"
	local excess = 0
	if horizontal > (c.teleportDistance or 80) then
		kind, excess = "teleport", horizontal - allowedH
	elseif horizontal > allowedH then
		kind, excess = "speed", horizontal - allowedH
	elseif rise > allowedUp then
		kind, excess = "fly", rise - allowedUp
	end
	if airborne then
		local since = st.airSince or t
		st.airSince = since
		if kind == "ok" and t - since > (c.maxAirtime or 8) then
			kind, excess = "fly", t - since - (c.maxAirtime or 8)
		end
	else
		st.airSince = nil
	end
	if kind ~= "ok" then
		return { kind = kind, excess = excess, resetTo = copy(st.pos) }
	end
	st.pos, st.t = copy(pos), t
	return { kind = "ok", excess = 0 }
end

return MovementCheck
