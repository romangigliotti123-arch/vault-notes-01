--!strict
-- Weapons: server-side activation rules for tools and weapons: equipped, alive, cooldown (os.clock on the server), ammo and reload.
-- The client sends "I activated" (maybe with an aim hint); the server decides if a shot/swing happens, and the damage number comes
-- from this table, never from the client. Hit detection is hitbox-combat-builder; damage application is health-damage-builder.
--   local weapons = Weapons.new({ now = os.clock, defs = { Pistol = { cooldown = 0.25, damage = 12, mag = 8, reload = 1.5 },
--       Sword = { cooldown = 0.6, damage = 20 } } })
--   local ok, why, dmg = weapons:activate(userId, "Pistol", { equipped = "Pistol", alive = true })
local Weapons = {}
Weapons.__index = Weapons

export type Def = { cooldown: number, damage: number, mag: number?, reload: number? }
export type Config = { defs: { [string]: Def }, now: () -> number, latency: number? }
export type Player = { equipped: string?, alive: boolean }
type State = { last: number, ammo: number, reloadingUntil: number }
export type Weapons = typeof(setmetatable({} :: { _c: Config, _s: { [number]: { [string]: State } } }, Weapons))

function Weapons.new(config: Config): Weapons
	for name, d in config.defs do
		assert(d.cooldown > 0 and d.damage >= 0, `weapon {name}: cooldown > 0 and damage >= 0`)
		assert((d.mag == nil) == (d.reload == nil), `weapon {name}: mag and reload go together`)
	end
	return setmetatable({ _c = config, _s = {} }, Weapons)
end

local function state(self: Weapons, userId: number, name: string): State
	local per = self._s[userId]
	if per == nil then
		per = {}
		self._s[userId] = per
	end
	local s = per[name]
	if s == nil then
		s = { last = -math.huge, ammo = self._c.defs[name].mag or math.huge, reloadingUntil = 0 }
		per[name] = s
	end
	return s
end

-- returns ok, reason, damage. The latency allowance (default 0.05 s) lets a legitimate shot through that arrives slightly early.
function Weapons.activate(self: Weapons, userId: number, name: any, player: Player): (boolean, string, number?)
	local d = if type(name) == "string" then self._c.defs[name] else nil
	if d == nil then
		return false, "unknown weapon"
	end
	if not player.alive then
		return false, "dead"
	end
	if player.equipped ~= name then
		return false, "not equipped"
	end
	local s = state(self, userId, name)
	local now = self._c.now()
	if now < s.reloadingUntil then
		return false, "reloading"
	end
	if now - s.last < d.cooldown - (self._c.latency or 0.05) then
		return false, "cooldown"
	end
	if s.ammo <= 0 then
		return false, "empty"
	end
	s.last = now
	s.ammo -= 1
	return true, "ok", d.damage
end

function Weapons.reload(self: Weapons, userId: number, name: string): (boolean, string)
	local d = self._c.defs[name]
	if d == nil or d.mag == nil then
		return false, "cannot reload"
	end
	local s = state(self, userId, name)
	local now = self._c.now()
	if now < s.reloadingUntil then
		return false, "already reloading"
	end
	if s.ammo >= d.mag then
		return false, "full"
	end
	s.reloadingUntil = now + (d.reload :: number)
	s.ammo = d.mag
	return true, "ok"
end

function Weapons.ammo(self: Weapons, userId: number, name: string): number
	return state(self, userId, name).ammo
end

function Weapons.forget(self: Weapons, userId: number)
	self._s[userId] = nil
end

return Weapons
