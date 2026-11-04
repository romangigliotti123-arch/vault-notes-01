--!strict
local CrashSignals = {}

export type Signal = { category: string, index: number, text: string }
export type Summary = {
	counts: { [string]: number },
	first: { [string]: number },
	timeline: { Signal },
	suspect: string,
	why: string,
}
export type Sample = { t: number, mb: number }

local RULES: { { string | { string } } } = {
	{ "memory", { "out of memory", "memory limit", "low memory", "memory warning" } },
	{ "script-timeout", { "exhausted allowed execution time", "script timeout" } },
	{ "datastore-throttle", { "added to queue", "keythrottled", "datastorethrottled", "http 429", "throttl" } },
	{ "datastore-error", { "datastore", "datastoreservice" } },
	{ "http-error", { "httpservice", "http 4", "http 5", "httprequest" } },
	{ "kicked", { "kicked", "you have been kicked" } },
	{ "disconnect", { "disconnected", "lost connection", "connection lost", "connection error" } },
	{ "infinite-yield", { "infinite yield possible" } },
	{ "script-error", { "attempt to ", "is not a valid member", "stack begin" } },
}

function CrashSignals.classify(line: string): string?
	local lower = string.lower(line)
	for _, rule in RULES do
		for _, frag in rule[2] :: { string } do
			if string.find(lower, frag, 1, true) then
				local cat = rule[1] :: string
				if
					cat == "datastore-error"
					and not (
						string.find(lower, "error", 1, true)
						or string.find(lower, "fail", 1, true)
						or string.find(lower, "can't", 1, true)
					)
				then
					break
				end
				return cat
			end
		end
	end
	return nil
end

local SUSPECT_ORDER = {
	"memory",
	"script-timeout",
	"datastore-throttle",
	"datastore-error",
	"http-error",
	"script-error",
	"infinite-yield",
	"kicked",
	"disconnect",
}
local WHY: { [string]: string } = {
	memory = "memory pressure came first: check the F9 memory tab on the real device and run the leak hunt (instance counts, heap snapshots over time)",
	["script-timeout"] = "a script ran too long without yielding: profile the loop named in the lines before it",
	["datastore-throttle"] = "DataStore calls are being queued or throttled: reduce save frequency, batch, and back off (see retry-wrapper-builder)",
	["datastore-error"] = "DataStore calls are failing: check pcall/retry and whether Studio API access or published place is the cause",
	["http-error"] = "HTTP calls are failing: check allowed domains, status codes and back-off",
	["script-error"] = "ordinary script errors precede the end of the log: triage them with output-error-triager",
	["infinite-yield"] = "a WaitForChild/require never resolved: check paths and load order",
	kicked = "players were removed by your own code: find the Kick call and what flagged them",
	disconnect = "the connection dropped with no earlier cause in this log: look at the other side (client log vs server log) and the time of day",
}

function CrashSignals.summarize(lines: { string }): Summary
	local counts: { [string]: number } = {}
	local first: { [string]: number } = {}
	local timeline: { Signal } = {}
	for i, line in lines do
		local cat = CrashSignals.classify(line)
		if cat then
			counts[cat] = (counts[cat] or 0) + 1
			if first[cat] == nil then
				first[cat] = i
				table.insert(timeline, { category = cat, index = i, text = line })
			end
		end
	end
	local endAt = math.huge
	for _, c in { "disconnect", "kicked" } do
		if first[c] and first[c] < endAt then
			endAt = first[c]
		end
	end
	local suspect, why =
		"none",
		"no crash-relevant message found: the log may be incomplete (get the other side's log and the device's F9 console)"
	local bestIndex = math.huge
	for _, c in SUSPECT_ORDER do
		local at = first[c]
		if at and at < endAt and at < bestIndex and c ~= "disconnect" and c ~= "kicked" then
			if suspect == "none" or at + 20 < bestIndex then
				suspect, why, bestIndex = c, WHY[c], at
			end
		end
	end
	if suspect == "none" then
		for _, c in { "kicked", "disconnect" } do
			if first[c] then
				suspect, why = c, WHY[c]
				break
			end
		end
	end
	return { counts = counts, first = first, timeline = timeline, suspect = suspect, why = why }
end

function CrashSignals.memoryTrend(
	samples: { Sample },
	leakMbPerMin: number?
): { slope: number, rising: boolean, leak: boolean }
	local n = #samples
	if n < 3 then
		return { slope = 0, rising = false, leak = false }
	end
	local sx, sy, sxx, sxy = 0, 0, 0, 0
	local ups = 0
	for i, s in samples do
		sx += s.t
		sy += s.mb
		sxx += s.t * s.t
		sxy += s.t * s.mb
		if i > 1 and s.mb >= samples[i - 1].mb then
			ups += 1
		end
	end
	local denom = n * sxx - sx * sx
	local slope = if denom == 0 then 0 else (n * sxy - sx * sy) / denom * 60
	local rising = slope > 0 and ups / (n - 1) >= 0.7
	return { slope = slope, rising = rising, leak = rising and slope >= (leakMbPerMin or 5) }
end

function CrashSignals.report(s: Summary): string
	local lines = { `CRASH SIGNALS: suspect {s.suspect}`, `  why: {s.why}` }
	for _, sig in s.timeline do
		table.insert(lines, `  line {sig.index} [{sig.category}] x{s.counts[sig.category]}: {sig.text}`)
	end
	return table.concat(lines, "\n")
end

return CrashSignals
