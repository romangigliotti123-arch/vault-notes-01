--!strict
-- Palette: contrast, colour-blind and grayscale checks for a game palette. Pure logic (no Roblox API), unit-tested under Lune.
--   local issues = Palette.check({ { name = "wall", hex = "#C9B79C" }, { name = "trim", hex = "#8A6D4B" } }, { pairs = {{"wall","trim"}} })
-- Colour-blind simulation uses the Machado et al. 2009 matrices at full severity, applied in linear RGB (a screening aid, not a diagnosis).
local Palette = {}

export type RGB = { number } -- r, g, b in 0..255
export type Entry = { name: string, hex: string }
export type Issue = { kind: string, a: string, b: string, value: number, note: string }

local MATRICES: { [string]: { { number } } } = {
	protanopia = {
		{ 0.152286, 1.052583, -0.204868 },
		{ 0.114503, 0.786281, 0.099216 },
		{ -0.003882, -0.048116, 1.051998 },
	},
	deuteranopia = {
		{ 0.367322, 0.860646, -0.227968 },
		{ 0.280085, 0.672501, 0.047413 },
		{ -0.01182, 0.04294, 0.968881 },
	},
	tritanopia = {
		{ 1.255528, -0.076749, -0.178779 },
		{ -0.078411, 0.930809, 0.147602 },
		{ 0.004733, 0.691367, 0.3039 },
	},
}
Palette.KINDS = { "protanopia", "deuteranopia", "tritanopia" }

function Palette.parseHex(hex: string): RGB?
	local h = string.match(hex, "^#?(%x%x%x%x%x%x)$")
	if not h then
		return nil
	end
	return {
		tonumber(string.sub(h, 1, 2), 16) :: number,
		tonumber(string.sub(h, 3, 4), 16) :: number,
		tonumber(string.sub(h, 5, 6), 16) :: number,
	}
end

local function toLinear(c: number): number
	local s = c / 255
	if s <= 0.04045 then
		return s / 12.92
	end
	return ((s + 0.055) / 1.055) ^ 2.4
end

local function fromLinear(l: number): number
	local v = math.clamp(l, 0, 1)
	if v <= 0.0031308 then
		return v * 12.92 * 255
	end
	return (1.055 * v ^ (1 / 2.4) - 0.055) * 255
end

function Palette.luminance(c: RGB): number
	return 0.2126 * toLinear(c[1]) + 0.7152 * toLinear(c[2]) + 0.0722 * toLinear(c[3])
end

-- WCAG contrast ratio, 1..21. Normal text needs 4.5, large text and UI shapes 3.
function Palette.contrast(a: RGB, b: RGB): number
	local la, lb = Palette.luminance(a), Palette.luminance(b)
	if la < lb then
		la, lb = lb, la
	end
	return (la + 0.05) / (lb + 0.05)
end

function Palette.simulate(c: RGB, kind: string): RGB
	local m = MATRICES[kind]
	if not m then
		error("unknown colour-blind kind: " .. kind)
	end
	local lin = { toLinear(c[1]), toLinear(c[2]), toLinear(c[3]) }
	local out = {}
	for i = 1, 3 do
		out[i] = fromLinear(m[i][1] * lin[1] + m[i][2] * lin[2] + m[i][3] * lin[3])
	end
	return out
end

local function toLab(c: RGB): { number }
	local r, g, b = toLinear(c[1]), toLinear(c[2]), toLinear(c[3])
	local x = (0.4124564 * r + 0.3575761 * g + 0.1804375 * b) / 0.95047
	local y = 0.2126729 * r + 0.7151522 * g + 0.072175 * b
	local z = (0.0193339 * r + 0.119192 * g + 0.9503041 * b) / 1.08883
	local function f(t: number): number
		if t > 0.008856 then
			return t ^ (1 / 3)
		end
		return 7.787 * t + 16 / 116
	end
	local fx, fy, fz = f(x), f(y), f(z)
	return { 116 * fy - 16, 500 * (fx - fy), 200 * (fy - fz) }
end

-- CIE76 colour difference. About 2.3 is a just-noticeable difference; under ~12 two colours read as the same family.
function Palette.deltaE(a: RGB, b: RGB): number
	local la, lb = toLab(a), toLab(b)
	return math.sqrt((la[1] - lb[1]) ^ 2 + (la[2] - lb[2]) ^ 2 + (la[3] - lb[3]) ^ 2)
end

-- Grayscale value of a colour (0..255, luminance based), for the "view it in monochrome" check.
function Palette.gray(c: RGB): number
	return fromLinear(Palette.luminance(c))
end

export type Options = {
	pairs: { { string } }?, -- names that must stay distinguishable; nil = every pair
	minDeltaE: number?, -- default 12
	minGrayGap: number?, -- default 25 (of 255)
	textPairs: { { string } }?, -- { foregroundName, backgroundName } pairs that carry text; need contrast >= minContrast
	minContrast: number?, -- default 4.5
}

function Palette.check(entries: { Entry }, opts: Options?): ({ Issue }, { string })
	local o: Options = opts or {}
	local minDE, minGray, minContrast = o.minDeltaE or 12, o.minGrayGap or 25, o.minContrast or 4.5
	local byName: { [string]: RGB } = {}
	local issues: { Issue } = {}
	local errors: { string } = {}
	for _, e in entries do
		local rgb = Palette.parseHex(e.hex)
		if rgb then
			byName[e.name] = rgb
		else
			table.insert(errors, "bad hex for " .. e.name .. ": " .. e.hex)
		end
	end
	local pairList: { { string } } = {}
	if o.pairs then
		pairList = o.pairs
	else
		for i = 1, #entries do
			for j = i + 1, #entries do
				table.insert(pairList, { entries[i].name, entries[j].name })
			end
		end
	end
	for _, p in pairList do
		local a, b = byName[p[1]], byName[p[2]]
		if a and b then
			local gap = math.abs(Palette.gray(a) - Palette.gray(b))
			if gap < minGray then
				table.insert(
					issues,
					{ kind = "gray", a = p[1], b = p[2], value = gap, note = "same brightness in monochrome" }
				)
			end
			local normal = Palette.deltaE(a, b)
			for _, kind in Palette.KINDS do
				local de = Palette.deltaE(Palette.simulate(a, kind), Palette.simulate(b, kind))
				if de < minDE and normal >= minDE then
					table.insert(issues, {
						kind = kind,
						a = p[1],
						b = p[2],
						value = de,
						note = "distinct normally, confusable under " .. kind,
					})
				end
			end
		end
	end
	local textPairs: { { string } } = o.textPairs or {}
	for _, p in textPairs do
		local fg, bg = byName[p[1]], byName[p[2]]
		if fg and bg then
			local cr = Palette.contrast(fg, bg)
			if cr < minContrast then
				table.insert(
					issues,
					{ kind = "contrast", a = p[1], b = p[2], value = cr, note = "text contrast below " .. minContrast }
				)
			end
		end
	end
	return issues, errors
end

return Palette
