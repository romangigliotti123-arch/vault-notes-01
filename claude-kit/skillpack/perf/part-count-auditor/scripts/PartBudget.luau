--!strict
-- PartBudget: compare per-region render counts against a budget and rank the regions. Pure logic, Lune-tested.
-- Defaults and sources:
--   visibleParts 5000   vault optimisation KB: "target about 5k parts in the players' render area for 60 FPS" (creator test, 25-30 FPS at 9k). Indie.
--   drawCalls    1000   Roblox Creator Docs performance-optimization/design: example threshold on a baseline device (official).
--   triangles    1000000 same page (official). The scripting KB quotes ~500k triangles and ~500 draw calls for phones (indie): pass a stricter budget for mobile.
-- Counts come from count_regions.luau (parts per grid cell) or from Studio's Render/Summary stats; the budget applies to what is VISIBLE at once, not the map total.
local PartBudget = {}

export type Budget = { visibleParts: number, drawCalls: number, triangles: number }
export type Region = { name: string, parts: number, drawCalls: number?, triangles: number? }
export type Row = { name: string, worst: string, ratio: number, status: string, ratios: { [string]: number } }

PartBudget.DEFAULT = { visibleParts = 5000, drawCalls = 1000, triangles = 1000000 } :: Budget
PartBudget.MOBILE = { visibleParts = 5000, drawCalls = 500, triangles = 500000 } :: Budget -- indie phone figures (scripting KB)

local WARN_AT = 0.8 -- heuristic: flag regions at 80 percent of any budget

local function status(ratio: number): string
	if ratio > 1 then
		return "over"
	elseif ratio >= WARN_AT then
		return "warn"
	end
	return "ok"
end

-- regionsInView: the regions a player can see at the same time (for example a cell and its 8 neighbours). Their counts are summed first.
function PartBudget.combine(regionsInView: { Region }, name: string): Region
	local out: Region = { name = name, parts = 0, drawCalls = 0, triangles = 0 }
	for _, r in regionsInView do
		out.parts += r.parts
		out.drawCalls = (out.drawCalls or 0) + (r.drawCalls or 0)
		out.triangles = (out.triangles or 0) + (r.triangles or 0)
	end
	return out
end

function PartBudget.evaluate(regions: { Region }, budget: Budget?): { Row }
	local b = budget or PartBudget.DEFAULT
	local rows: { Row } = {}
	for _, r in regions do
		local ratios: { [string]: number } = { visibleParts = r.parts / b.visibleParts }
		if r.drawCalls then
			ratios.drawCalls = r.drawCalls / b.drawCalls
		end
		if r.triangles then
			ratios.triangles = r.triangles / b.triangles
		end
		local worstKey, worst = "visibleParts", -1
		for k, v in ratios do
			if v > worst or (v == worst and k < worstKey) then
				worstKey, worst = k, v
			end
		end
		table.insert(rows, { name = r.name, worst = worstKey, ratio = worst, status = status(worst), ratios = ratios })
	end
	table.sort(rows, function(a, b2)
		if a.ratio ~= b2.ratio then
			return a.ratio > b2.ratio
		end
		return a.name < b2.name
	end)
	return rows
end

-- plan: how many parts must go from a region to fit the budget (0 when it already fits).
function PartBudget.excess(region: Region, budget: Budget?): number
	local b = budget or PartBudget.DEFAULT
	return math.max(0, region.parts - b.visibleParts)
end

return PartBudget
