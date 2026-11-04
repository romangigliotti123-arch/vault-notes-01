--!strict
local UiMotion = {}

export type Step = {
	name: string,
	role: string,
	duration: number,
	properties: { string },
	loops: boolean?,
	stoppable: boolean?,
}
export type Finding = { step: string, rule: string }

UiMotion.MAX_DURATION = { feedback = 0.2, transition = 0.35, reward = 1.2, ambient = 3 } :: { [string]: number }
UiMotion.MAX_CONCURRENT_LOOPS = 3

local MOTION_PROPERTIES = { Position = true, Size = true, Rotation = true, AnchorPoint = true }

function UiMotion.validate(plan: { Step }): { Finding }
	local out: { Finding } = {}
	local loops = 0
	for _, s in plan do
		local cap = UiMotion.MAX_DURATION[s.role]
		if cap == nil then
			table.insert(out, { step = s.name, rule = "unknown-role" })
		elseif s.duration > cap then
			table.insert(out, { step = s.name, rule = `too-slow-for-{s.role}` })
		end
		if s.duration < 0 then
			table.insert(out, { step = s.name, rule = "negative-duration" })
		end
		for _, p in s.properties do
			if p == "TextStrokeTransparency" then
				table.insert(out, { step = s.name, rule = "avoid-tweening-text-stroke" })
			end
		end
		if s.loops then
			loops += 1
			if s.stoppable ~= true then
				table.insert(out, { step = s.name, rule = "loop-not-stoppable" })
			end
		end
	end
	if loops > UiMotion.MAX_CONCURRENT_LOOPS then
		table.insert(out, { step = "(plan)", rule = "too-many-looping-tweens" })
	end
	return out
end

function UiMotion.reduced(plan: { Step }): { Step }
	local out: { Step } = {}
	for _, s in plan do
		if not s.loops then
			local keep = {}
			for _, p in s.properties do
				if not MOTION_PROPERTIES[p] then
					table.insert(keep, p)
				end
			end
			table.insert(out, {
				name = s.name,
				role = s.role,
				duration = if #keep > 0 then math.min(s.duration, 0.15) else 0,
				properties = keep,
				loops = false,
				stoppable = true,
			})
		end
	end
	return out
end

return UiMotion
