--!strict
-- Health: health, damage types, flat armor, percentage resistances, delayed regeneration and a single death event. Pure logic on a
-- state table; the glue copies hp to Humanoid.Health for display. All damage numbers are decided on the server.
--   local h = Health.new({ max = 100, armor = 2, resist = { Fire = 0.5 }, regenDelay = 5, regenPerSec = 2, now = os.clock })
--   local dealt, died = h:damage(state, 30, "Fire")   -- (30 * 0.5) - 2 armor = 13
local Health = {}
Health.__index = Health

export type Config = {
	max: number,
	armor: number?, -- flat reduction per hit, never below minDamage
	resist: { [string]: number }?, -- 0..1 fraction removed per damage type; "True" damage ignores armor and resist
	minDamage: number?, -- smallest damage a hit can do after reductions (default 1)
	regenDelay: number?,
	regenPerSec: number?,
	now: () -> number,
}
export type State = { hp: number, dead: boolean, lastHit: number }
export type Health = typeof(setmetatable({} :: { _c: Config }, Health))

function Health.new(config: Config): Health
	assert(config.max >= 1, "max must be >= 1")
	local resist: { [string]: number } = config.resist or {}
	for t, r in resist do
		assert(r >= 0 and r <= 1, `resist {t} must be between 0 and 1 (over 1 would heal)`)
	end
	return setmetatable({ _c = config }, Health)
end

function Health.newState(self: Health): State
	return { hp = self._c.max, dead = false, lastHit = -math.huge }
end

-- returns damage actually dealt and whether this hit killed (true only once)
function Health.damage(self: Health, s: State, amount: any, kind: string?): (number, boolean)
	if s.dead or type(amount) ~= "number" or amount ~= amount or amount <= 0 or amount == math.huge then
		return 0, false
	end
	local dmg = amount
	if kind ~= "True" then
		local resist: { [string]: number } = self._c.resist or {}
		dmg *= 1 - (resist[kind or ""] or 0)
		dmg -= self._c.armor or 0
		dmg = math.max(dmg, self._c.minDamage or 1)
	end
	dmg = math.min(dmg, s.hp)
	s.hp -= dmg
	s.lastHit = self._c.now()
	if s.hp <= 0 then
		s.hp, s.dead = 0, true
		return dmg, true
	end
	return dmg, false
end

function Health.heal(self: Health, s: State, amount: any): number
	if s.dead or type(amount) ~= "number" or amount ~= amount or amount <= 0 then
		return 0
	end
	local healed = math.min(amount, self._c.max - s.hp)
	s.hp += healed
	return healed
end

-- call once a second (or per Heartbeat with dt): regen starts regenDelay after the last hit
function Health.tick(self: Health, s: State, dt: number)
	local rate = self._c.regenPerSec or 0
	if s.dead or rate <= 0 or s.hp >= self._c.max then
		return
	end
	if self._c.now() - s.lastHit >= (self._c.regenDelay or 0) then
		s.hp = math.min(self._c.max, s.hp + rate * dt)
	end
end

function Health.revive(self: Health, s: State)
	s.hp, s.dead, s.lastHit = self._c.max, false, -math.huge
end

return Health
