--!strict
local TuneGuard = {}

export type Def = { min: number, max: number, maxStepPct: number?, cooldown: number? }
export type Change = { at: number, from: number, to: number }
export type Decision = { ok: boolean, reason: string?, value: number, stepPct: number }

local DEFAULT_STEP = 25
local DEFAULT_COOLDOWN = 3600

function TuneGuard.check(def: Def, current: number, proposed: number, history: { Change }, now: number): Decision
	assert(def.min <= def.max, "min > max")
	if type(proposed) ~= "number" or proposed ~= proposed or proposed == math.huge or proposed == -math.huge then
		return { ok = false, reason = "proposed value is not a finite number", value = current, stepPct = 0 }
	end
	local step = current ~= 0 and math.abs(proposed - current) / math.abs(current) * 100 or (proposed == 0 and 0 or 100)
	if proposed < def.min or proposed > def.max then
		return { ok = false, reason = "outside bounds", value = math.clamp(proposed, def.min, def.max), stepPct = step }
	end
	local maxStep = def.maxStepPct or DEFAULT_STEP
	if step > maxStep then
		local limit = math.abs(current) * maxStep / 100
		local value = math.clamp(current + (proposed > current and limit or -limit), def.min, def.max)
		return {
			ok = false,
			reason = `step {math.floor(step)}% is over the {maxStep}% limit`,
			value = value,
			stepPct = step,
		}
	end
	local last = history[#history]
	local cooldown = def.cooldown or DEFAULT_COOLDOWN
	if last and now - last.at < cooldown then
		return {
			ok = false,
			reason = `cooldown: last change {math.floor(now - last.at)}s ago, wait {cooldown}s`,
			value = current,
			stepPct = step,
		}
	end
	return { ok = true, value = proposed, stepPct = step }
end

function TuneGuard.stages(from: number, to: number, count: number): { number }
	assert(count >= 1, "count must be >= 1")
	local out = {}
	for i = 1, count do
		table.insert(out, math.floor((from + (to - from) * i / count) + 0.5))
	end
	return out
end

function TuneGuard.revertValue(history: { Change }): number?
	local last = history[#history]
	return last and last.from or nil
end

return TuneGuard
