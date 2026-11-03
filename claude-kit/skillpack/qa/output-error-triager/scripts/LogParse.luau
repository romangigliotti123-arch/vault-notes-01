--!strict
-- LogParse: turns a pasted Output / Developer Console log into grouped, ranked problems. Pure string logic, unit-tested in Lune.
-- Impact is a transparent heuristic (see rank): server errors outrank client errors, repeats raise the score on a log curve, spam is called out.
-- It reads text only; it cannot tell you the cause. The top groups are where to look first.
local LogParse = {}

export type Line = {
	raw: string,
	text: string,
	kind: "error" | "warn" | "info",
	side: "server" | "client" | "unknown",
	stack: boolean,
}
export type Group = {
	key: string,
	kind: string,
	side: string,
	count: number,
	firstLine: number,
	example: string,
	score: number,
	spam: boolean,
}

local ERROR_MARKERS = {
	"attempt to ",
	"is not a valid member",
	"invalid argument",
	"error",
	"exception",
	"failed",
	"cannot ",
	"unable to ",
	"stack begin",
	"requested module experienced an error",
}
local WARN_MARKERS =
	{ "infinite yield possible", "deprecated", "warning", "added to queue", "throttl", "timed out", "retrying" }

local function stripTime(line: string): string
	local rest = string.match(line, "^%d+:%d+:%d+%.?%d*%s+(.*)$")
	return rest or line
end

function LogParse.classify(line: string): Line
	local text = stripTime(line)
	local lower = string.lower(text)
	local side: "server" | "client" | "unknown" = "unknown"
	if string.find(lower, "%-%s+server") or string.find(lower, "^server") then
		side = "server"
	elseif string.find(lower, "%-%s+client") or string.find(lower, "^client") then
		side = "client"
	end
	local kind: "error" | "warn" | "info" = "info"
	for _, m in WARN_MARKERS do
		if string.find(lower, m, 1, true) then
			kind = "warn"
			break
		end
	end
	for _, m in ERROR_MARKERS do
		if string.find(lower, m, 1, true) then
			kind = "error"
			break
		end
	end
	return {
		raw = line,
		text = text,
		kind = kind,
		side = side,
		stack = string.find(lower, "stack begin", 1, true) ~= nil,
	}
end

-- group key: drop the trailing "- Server/Client - Script:12" context, replace ids and counts, keep script:line (it is the location)
function LogParse.normalise(text: string): string
	local t = string.gsub(text, "%s+%-%s+[Ss]erver.*$", "")
	t = string.gsub(t, "%s+%-%s+[Cc]lient.*$", "")
	t = string.gsub(t, "0x%x+", "0x#")
	t = string.gsub(t, "(%a)%s*%-?%d+%.?%d*", function(letter: string)
		return letter .. " #"
	end)
	t = string.gsub(t, "%d%d%d%d%d+", "#")
	return t
end

local function baseWeight(kind: string, side: string): number
	local w = if kind == "error" then 2 elseif kind == "warn" then 0.5 else 0
	if side == "server" and kind ~= "info" then
		w *= 1.5 -- a server error affects everyone in that server
	end
	return w
end

function LogParse.parse(log: string): { Line }
	local out: { Line } = {}
	for raw in string.gmatch(log .. "\n", "([^\n]*)\n") do
		if string.match(raw, "%S") then
			table.insert(out, LogParse.classify(raw))
		end
	end
	return out
end

-- groups errors and warnings (info lines are ignored); stack lines are folded into the error above them
function LogParse.rank(lines: { Line }, spamAt: number?): { Group }
	local groups: { [string]: Group } = {}
	local order: { Group } = {}
	local last: Group? = nil
	for i, l in lines do
		if l.kind == "info" then
			last = nil
			continue
		end
		if l.stack or (last ~= nil and (string.find(l.text, "^Script '") or string.find(l.text, "^Stack End"))) then
			continue
		end
		local key = l.kind .. "|" .. l.side .. "|" .. LogParse.normalise(l.text)
		local g = groups[key]
		if g == nil then
			g = {
				key = key,
				kind = l.kind,
				side = l.side,
				count = 0,
				firstLine = i,
				example = l.text,
				score = 0,
				spam = false,
			}
			groups[key] = g
			table.insert(order, g)
		end
		g.count += 1
		last = g
	end
	for _, g in order do
		g.score = baseWeight(g.kind, g.side) * (1 + math.log(g.count, 2))
		g.spam = g.count >= (spamAt or 50)
	end
	table.sort(order, function(a, b)
		if a.score ~= b.score then
			return a.score > b.score
		end
		return a.firstLine < b.firstLine
	end)
	return order
end

function LogParse.report(groups: { Group }, top: number?): string
	local lines = { `LOG TRIAGE: {#groups} distinct problems` }
	for i, g in groups do
		if i > (top or 10) then
			table.insert(lines, `  ... {#groups - (top or 10)} more`)
			break
		end
		local flag = if g.spam then " SPAM" else ""
		table.insert(
			lines,
			`  {i}. [{g.kind} {g.side}] x{g.count}{flag} score {string.format("%.1f", g.score)} (first at line {g.firstLine}): {g.example}`
		)
	end
	return table.concat(lines, "\n")
end

return LogParse
