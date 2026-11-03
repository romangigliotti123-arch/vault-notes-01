--!strict
-- UiMotion: lint an animation plan and derive its reduced-motion variant. Pure data in, findings out; the tweening itself uses
-- the pack's tween-helper-builder (TweenKit) or TweenService directly. Duration limits are common UI practice, labelled heuristics.
--   local findings = UiMotion.validate(plan)
--   local calm = UiMotion.reduced(plan)
local UiMotion = {}

export type Step = {
	name: string,
	role: string, -- "feedback" | "transition" | "reward" | "ambient"
	duration: number,
	properties: { string }, -- e.g. { "Position", "Size", "GroupTransparency", "TextStrokeTransparency" }
	loops: boolean?,
	stoppable: boolean?, -- an ambient loop must be stoppable (screen closed, reduced motion)
}
export type Finding = { step: string, rule: string }

-- seconds; heuristic ceilings per role
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
				table.insert(out, { step = s.name, rule = "avoid-tweening-text-stroke" }) -- vault: fade a CanvasGroup instead
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

-- Reduced-motion variant: no looping, no movement/scale/rotation; fades stay but shortened. Returns a new plan.
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
