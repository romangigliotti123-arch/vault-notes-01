--!strict
local TextFit = {}

export type Entry = { key: string, text: string, maxChars: number, canWrap: boolean? }
export type Issue = { key: string, lang: string, estimated: number, maxChars: number }

TextFit.EXPANSION = {
	de = 1.35,
	fr = 1.25,
	es = 1.25,
	pt = 1.25,
	ru = 1.3,
	it = 1.2,
	id = 1.2,
	tr = 1.2,
	ja = 0.6,
	zh = 0.5,
	ko = 0.7,
} :: { [string]: number }

function TextFit.estimate(text: string, lang: string): number
	local len = utf8.len(text) or #text
	local factor = TextFit.EXPANSION[lang] or 1.3
	local out = len * factor
	if len <= 10 and factor > 1 then
		out += 3
	end
	return math.ceil(out)
end

function TextFit.capacity(widthPx: number, textSizePx: number, lines: number?): number
	local perLine = math.floor(widthPx / math.max(1, textSizePx * 0.5))
	return perLine * (lines or 1)
end

function TextFit.check(entries: { Entry }, langs: { string }): { Issue }
	local issues: { Issue } = {}
	for _, e in entries do
		for _, lang in langs do
			local est = TextFit.estimate(e.text, lang)
			if est > e.maxChars then
				table.insert(issues, { key = e.key, lang = lang, estimated = est, maxChars = e.maxChars })
			end
		end
	end
	return issues
end

function TextFit.looksHardcoded(text: string): boolean
	return string.find(text, "%a%a") ~= nil and string.find(text, "^[%w_%.]+$") == nil
end

return TextFit
