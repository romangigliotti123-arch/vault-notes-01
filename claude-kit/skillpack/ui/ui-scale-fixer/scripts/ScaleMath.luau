--!strict
-- ScaleMath: convert pixel (Offset) sizes designed at a reference viewport into Scale + constraints, and sweep the result over
-- other viewports to see what a player would get. Pure arithmetic; applying it to Instances is the skill's Studio step.
--   local plan = ScaleMath.convert({ w = 300, h = 80 }, { w = 1920, h = 1080 }, { interactive = true })
--   local issues = ScaleMath.sweep(plan, ScaleMath.EXAMPLE_VIEWPORTS)
local ScaleMath = {}

export type Size = { w: number, h: number }
export type Viewport = { name: string, w: number, h: number }
export type Plan = {
	scaleX: number,
	scaleY: number,
	aspect: number, -- w / h, for a UIAspectRatioConstraint
	maxPx: Size, -- UISizeConstraint.MaxSize: never bigger than the design size
	minPx: Size, -- UISizeConstraint.MinSize: touch floor for interactive objects, else 0
}
export type Options = { interactive: boolean?, minTouchPx: number? }

-- Illustrative sizes only; read the real emulator list in Studio. Labelled heuristic.
ScaleMath.EXAMPLE_VIEWPORTS = {
	{ name = "small phone landscape", w = 667, h = 375 },
	{ name = "phone portrait", w = 375, h = 667 },
	{ name = "tablet", w = 1024, h = 768 },
	{ name = "desktop 16:9", w = 1920, h = 1080 },
} :: { Viewport }

function ScaleMath.convert(design: Size, ref: Size, options: Options?): Plan
	assert(ref.w > 0 and ref.h > 0 and design.h > 0, "sizes must be positive")
	local floor = 0
	if options and options.interactive then
		floor = options.minTouchPx or 44
	end
	return {
		scaleX = design.w / ref.w,
		scaleY = design.h / ref.h,
		aspect = design.w / design.h,
		maxPx = { w = design.w, h = design.h },
		minPx = { w = math.min(floor, design.w), h = math.min(floor, design.h) },
	}
end

-- Pixels the object ends up with at a viewport, after the size constraint (aspect ratio keeps width and recomputes height).
function ScaleMath.resolve(plan: Plan, viewport: Size): Size
	local w = math.clamp(plan.scaleX * viewport.w, plan.minPx.w, plan.maxPx.w)
	return { w = w, h = w / plan.aspect }
end

function ScaleMath.sweep(plan: Plan, viewports: { Viewport }): { string }
	local issues = {}
	for _, v in viewports do
		local px = ScaleMath.resolve(plan, v)
		if px.w > v.w or px.h > v.h then
			table.insert(issues, `{v.name}: {math.floor(px.w)}x{math.floor(px.h)} exceeds the viewport`)
		end
		if plan.minPx.h > 0 and px.h < plan.minPx.h then
			table.insert(issues, `{v.name}: height {math.floor(px.h)} px under the touch floor {plan.minPx.h}`)
		end
	end
	return issues
end

return ScaleMath
