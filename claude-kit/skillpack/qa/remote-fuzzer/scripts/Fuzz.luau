--!strict
-- Fuzz: bad-value corpus + runner for server handlers. Pure logic, unit-tested in Lune. Use ONLY in your own test place.
-- Handler contract: `call(args)` invokes the handler as the server would; `snapshot()` returns a comparable view of the state the handler
-- may change (currency, inventory, position...); `reset()` restores clean state. A bad value that changes the snapshot was ACCEPTED.
local Fuzz = {}

export type Case = { label: string, value: any }
export type Finding = { arg: number, label: string, outcome: "accepted" | "threw" }
export type Options = {
	call: (args: { any }) -> (),
	snapshot: () -> any,
	reset: () -> (),
	baseline: { any }, -- a valid argument list (the handler must accept it, or the run is meaningless)
	kinds: { string }, -- one per argument: "number" | "integer" | "string" | "boolean" | "table" | "instance" | "any"
	skipThrew: boolean?, -- when true an error inside the handler is not reported (default false: handlers should not throw on input)
}

local function cyclic(): any
	local a: any = {}
	a.self = a
	return a
end

local function deep(n: number): any
	local root: any = {}
	local cur = root
	for _ = 1, n do
		local nxt = {}
		cur.child = nxt
		cur = nxt
	end
	return root
end

local NUMBERS: { Case } = {
	{ label = "NaN", value = 0 / 0 },
	{ label = "+inf", value = math.huge },
	{ label = "-inf", value = -math.huge },
	{ label = "-1", value = -1 },
	{ label = "0", value = 0 },
	{ label = "0.5", value = 0.5 },
	{ label = "2^53", value = 2 ^ 53 },
	{ label = "1e308", value = 1e308 },
	{ label = "-1e308", value = -1e308 },
}
local STRINGS: { Case } = {
	{ label = "empty string", value = "" },
	{ label = "10k chars", value = string.rep("A", 10000) },
	{ label = "NUL byte", value = "a\0b" },
	{ label = "unicode", value = "\u{202E}\u{1F600}x" },
	{ label = "newline/markup", value = "<b>\n{{x}}" },
	{ label = "numeric text", value = "999999999" },
}
local OTHERS: { Case } = {
	{ label = "nil", value = nil },
	{ label = "true", value = true },
	{ label = "false", value = false },
	{ label = "empty table", value = {} },
	{ label = "cyclic table", value = cyclic() },
	{ label = "deep table (200)", value = deep(200) },
	{ label = "array of 5000", value = table.create(5000, 1) },
}

local function append(into: { Case }, from: { Case })
	for _, c in from do
		table.insert(into, c)
	end
end

-- values worth sending for one argument kind. The wrong-type values are always included: a number argument gets strings and tables too.
function Fuzz.corpus(kind: string): { Case }
	local out: { Case } = {}
	if kind == "number" or kind == "integer" then
		append(out, NUMBERS)
		append(out, STRINGS)
		append(out, OTHERS)
	elseif kind == "string" then
		append(out, STRINGS)
		append(out, NUMBERS)
		append(out, OTHERS)
	else
		append(out, OTHERS)
		append(out, NUMBERS)
		append(out, STRINGS)
	end
	return out
end

local function same(a: any, b: any, seen: { [any]: boolean }?): boolean
	if a ~= a and b ~= b then
		return true -- NaN counts as equal to NaN so an unchanged NaN is not a change
	end
	if type(a) ~= "table" or type(b) ~= "table" then
		return a == b
	end
	local s = seen or {}
	if s[a] then
		return true
	end
	s[a] = true
	for k, v in a do
		if not same(v, b[k], s) then
			return false
		end
	end
	for k in b do
		if a[k] == nil then
			return false
		end
	end
	return true
end

Fuzz.same = same

local function withArg(base: { any }, n: number, value: any, count: number): { any }
	local args = table.create(count)
	for i = 1, count do
		args[i] = base[i]
	end
	args[n] = value
	return args
end

-- Send each bad value in each argument position (one position at a time) and report what the handler accepted or threw on.
function Fuzz.run(o: Options): { Finding }
	local count = #o.kinds
	o.reset()
	local before = o.snapshot()
	local okBase = pcall(o.call, o.baseline)
	assert(okBase, "baseline call failed: the valid arguments must be accepted before fuzzing means anything")
	assert(
		not same(before, o.snapshot()),
		"baseline call changed nothing: pick a snapshot that shows the handler's effect"
	)
	local findings: { Finding } = {}
	for n = 1, count do
		for _, case in Fuzz.corpus(o.kinds[n]) do
			o.reset()
			local clean = o.snapshot()
			local ok = pcall(o.call, withArg(o.baseline, n, case.value, count))
			if not ok then
				if not o.skipThrew then
					table.insert(findings, { arg = n, label = case.label, outcome = "threw" })
				end
			elseif not same(clean, o.snapshot()) and not same(case.value, o.baseline[n]) then
				table.insert(findings, { arg = n, label = case.label, outcome = "accepted" })
			end
		end
	end
	o.reset()
	return findings
end

-- Fire `n` identical valid requests as fast as possible; returns how many changed state. Compare with the rate limit you configured.
function Fuzz.burst(o: Options, n: number): number
	o.reset()
	local accepted = 0
	local prev = o.snapshot()
	for _ = 1, n do
		pcall(o.call, o.baseline)
		local now = o.snapshot()
		if not same(prev, now) then
			accepted += 1
		end
		prev = now
	end
	o.reset()
	return accepted
end

function Fuzz.report(findings: { Finding }, kinds: { string }): string
	if #findings == 0 then
		return "FUZZ: 0 findings"
	end
	local lines = { `FUZZ: {#findings} findings` }
	for _, f in findings do
		table.insert(lines, `  arg {f.arg} ({kinds[f.arg]}): {f.label} -> {f.outcome}`)
	end
	return table.concat(lines, "\n")
end

return Fuzz
