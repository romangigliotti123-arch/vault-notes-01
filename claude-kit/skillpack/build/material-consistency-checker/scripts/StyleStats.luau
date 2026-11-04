--!strict
local StyleStats = {}

export type Sample = { material: string, color: string, count: number? }
export type Outlier = { key: string, count: number, share: number }
export type Report = {
	total: number,
	materials: { [string]: number },
	colors: { [string]: number },
	distinctMaterials: number,
	distinctColors: number,
	materialOutliers: { Outlier },
	colorOutliers: { Outlier },
	notes: { string },
}

function StyleStats.bucket(r: number, g: number, b: number, step: number?): string
	local s = step or 32
	local function q(v: number): number
		return math.min(255, math.floor(v / s + 0.5) * s)
	end
	return string.format("#%02X%02X%02X", q(r), q(g), q(b))
end

local function tally(samples: { Sample }, field: string): ({ [string]: number }, number)
	local counts: { [string]: number } = {}
	local total = 0
	for _, s in samples do
		local key = if field == "material" then s.material else s.color
		local n = s.count or 1
		counts[key] = (counts[key] or 0) + n
		total += n
	end
	return counts, total
end

local function outliers(counts: { [string]: number }, total: number, minShare: number): { Outlier }
	local out: { Outlier } = {}
	for key, n in counts do
		local share = if total > 0 then n / total else 0
		if share < minShare then
			table.insert(out, { key = key, count = n, share = share })
		end
	end
	table.sort(out, function(a, b)
		if a.count ~= b.count then
			return a.count < b.count
		end
		return a.key < b.key
	end)
	return out
end

function StyleStats.analyse(samples: { Sample }, minShare: number?): Report
	local share = minShare or 0.02
	local materials, total = tally(samples, "material")
	local colors = tally(samples, "color")
	local dm, dc = 0, 0
	for _ in materials do
		dm += 1
	end
	for _ in colors do
		dc += 1
	end
	local notes: { string } = {}
	if dm > 6 then
		table.insert(notes, `{dm} distinct materials: style guides keep a handful, check the rest`)
	end
	if dc > 12 then
		table.insert(notes, `{dc} distinct colour buckets: tighten the palette`)
	end
	local mo = if dm > 3 then outliers(materials, total, share) else {}
	local co = if dc > 5 then outliers(colors, total, share) else {}
	return {
		total = total,
		materials = materials,
		colors = colors,
		distinctMaterials = dm,
		distinctColors = dc,
		materialOutliers = mo,
		colorOutliers = co,
		notes = notes,
	}
end

return StyleStats
