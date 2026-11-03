--!strict
-- Colorblind: simulate the three dichromacies and find colour pairs that stop being distinguishable. Machado et al. (2009) matrices
-- at full severity, applied in linear RGB: an APPROXIMATION for design review, not a medical tool. Colours are 0-255 {r, g, b}.
-- Distinctness is the Euclidean distance in 0-255 sRGB after simulation (threshold is a heuristic; tune with real users if you can).
--   Colorblind.simulate({220, 40, 40}, "deutan")
--   Colorblind.collisions({ {name="red team", color=...}, {name="green team", color=...} }) -> list of {a, b, kind}
--   Colorblind.colourOnly(indicators) -> names whose meaning is carried by colour alone
local Colorblind = {}

export type RGB = { number }
export type Swatch = { name: string, color: RGB }
export type Collision = { a: string, b: string, kind: string, distance: number }
export type Indicator = { name: string, colors: number, hasSecondaryCue: boolean } -- secondary cue: icon, shape, label, pattern

Colorblind.MIN_DISTANCE = 60 -- heuristic: below this two colours look alike in the simulation

local MATRICES: { [string]: { { number } } } = {
	protan = { { 0.152286, 1.052583, -0.204868 }, { 0.114503, 0.786281, 0.099216 }, { -0.003882, -0.048116, 1.051998 } },
	deutan = { { 0.367322, 0.860646, -0.227968 }, { 0.280085, 0.672501, 0.047413 }, { -0.011820, 0.042940, 0.968881 } },
	tritan = { { 1.255528, -0.076749, -0.178779 }, { -0.078411, 0.930809, 0.147602 }, { 0.004733, 0.691367, 0.303900 } },
}

local function toLinear(v: number): number
	local c = v / 255
	if c <= 0.04045 then
		return c / 12.92
	end
	return ((c + 0.055) / 1.055) ^ 2.4
end

local function toSrgb(l: number): number
	local c = math.clamp(l, 0, 1)
	if c <= 0.0031308 then
		return c * 12.92 * 255
	end
	return (1.055 * c ^ (1 / 2.4) - 0.055) * 255
end

function Colorblind.simulate(c: RGB, kind: string): RGB
	local m = MATRICES[kind]
	assert(m ~= nil, "kind must be protan, deutan or tritan")
	local r, g, b = toLinear(c[1]), toLinear(c[2]), toLinear(c[3])
	return {
		toSrgb(m[1][1] * r + m[1][2] * g + m[1][3] * b),
		toSrgb(m[2][1] * r + m[2][2] * g + m[2][3] * b),
		toSrgb(m[3][1] * r + m[3][2] * g + m[3][3] * b),
	}
end

function Colorblind.distance(a: RGB, b: RGB): number
	local dr, dg, db = a[1] - b[1], a[2] - b[2], a[3] - b[3]
	return math.sqrt(dr * dr + dg * dg + db * db)
end

function Colorblind.collisions(swatches: { Swatch }, minDistance: number?): { Collision }
	local limit = minDistance or Colorblind.MIN_DISTANCE
	local out: { Collision } = {}
	for i = 1, #swatches do
		for j = i + 1, #swatches do
			local normal = Colorblind.distance(swatches[i].color, swatches[j].color)
			for _, kind in { "protan", "deutan", "tritan" } do
				local d = Colorblind.distance(
					Colorblind.simulate(swatches[i].color, kind),
					Colorblind.simulate(swatches[j].color, kind)
				)
				-- only report pairs that were distinguishable normally but collapse under this condition
				if d < limit and normal >= limit then
					table.insert(
						out,
						{ a = swatches[i].name, b = swatches[j].name, kind = kind, distance = math.floor(d) }
					)
				end
			end
		end
	end
	return out
end

function Colorblind.colourOnly(indicators: { Indicator }): { string }
	local out = {}
	for _, i in indicators do
		if i.colors >= 2 and not i.hasSecondaryCue then
			table.insert(out, i.name)
		end
	end
	return out
end

return Colorblind
