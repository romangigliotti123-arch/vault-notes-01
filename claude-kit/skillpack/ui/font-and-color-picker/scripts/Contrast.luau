--!strict
local Contrast = {}

export type RGB = { number }
export type Pair = { name: string, fg: RGB, bg: RGB, textPx: number, bold: boolean?, nonText: boolean? }
export type Failure = { name: string, ratio: number, needed: number }

local function channel(v: number): number
	local c = v / 255
	if c <= 0.03928 then
		return c / 12.92
	end
	return ((c + 0.055) / 1.055) ^ 2.4
end

function Contrast.luminance(c: RGB): number
	return 0.2126 * channel(c[1]) + 0.7152 * channel(c[2]) + 0.0722 * channel(c[3])
end

function Contrast.ratio(a: RGB, b: RGB): number
	local la, lb = Contrast.luminance(a), Contrast.luminance(b)
	local hi, lo = math.max(la, lb), math.min(la, lb)
	return (hi + 0.05) / (lo + 0.05)
end

function Contrast.neededRatio(textPx: number, bold: boolean?, nonText: boolean?): number
	if nonText then
		return 3
	end
	if textPx >= 24 or (bold == true and textPx >= 18.66) then
		return 3
	end
	return 4.5
end

function Contrast.bestText(bg: RGB): RGB
	local white, black = { 255, 255, 255 }, { 20, 20, 20 }
	if Contrast.ratio(white, bg) >= Contrast.ratio(black, bg) then
		return white
	end
	return black
end

function Contrast.checkPalette(pairs: { Pair }): { Failure }
	local failures: { Failure } = {}
	for _, p in pairs do
		local need = Contrast.neededRatio(p.textPx, p.bold, p.nonText)
		local got = Contrast.ratio(p.fg, p.bg)
		if got < need then
			table.insert(failures, { name = p.name, ratio = math.floor(got * 100) / 100, needed = need })
		end
	end
	return failures
end

return Contrast
