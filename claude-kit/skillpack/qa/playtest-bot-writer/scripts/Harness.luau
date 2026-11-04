--!strict
local Harness = {}
Harness.__index = Harness

export type Harness = typeof(setmetatable(
	{} :: {
		name: string,
		results: { { label: string, ok: boolean, detail: string } },
		wait: (seconds: number) -> (),
		clock: () -> number,
	},
	Harness
))

function Harness.new(name: string, wait: ((number) -> ())?, clock: (() -> number)?): Harness
	return setmetatable({
		name = name,
		results = {},
		wait = wait or task.wait,
		clock = clock or os.clock,
	}, Harness)
end

function Harness.check(self: Harness, label: string, condition: any, detail: string?): boolean
	local ok = condition and true or false
	table.insert(self.results, { label = label, ok = ok, detail = detail or "" })
	return ok
end

function Harness.checkEq(self: Harness, label: string, actual: any, expected: any): boolean
	return self:check(label, actual == expected, `expected {tostring(expected)}, got {tostring(actual)}`)
end

function Harness.waitFor(
	self: Harness,
	label: string,
	predicate: () -> any,
	timeout: number,
	interval: number?
): boolean
	local step = interval or 0.1
	local start = self.clock()
	while self.clock() - start < timeout do
		local ok, value = pcall(predicate)
		if ok and value then
			return self:check(label, true, `after {string.format("%.2f", self.clock() - start)}s`)
		end
		self.wait(step)
	end
	return self:check(label, false, `timed out after {timeout}s`)
end

function Harness.step(self: Harness, label: string, fn: () -> ()): boolean
	local ok, err = pcall(fn :: () -> any)
	if not ok then
		return self:check(label, false, `error: {tostring(err)}`)
	end
	return true
end

function Harness.failures(self: Harness): number
	local n = 0
	for _, r in self.results do
		if not r.ok then
			n += 1
		end
	end
	return n
end

function Harness.report(self: Harness): string
	local lines = { `PLAYTEST BOT: {self.name}: {#self.results - self:failures()}/{#self.results} checks passed` }
	for _, r in self.results do
		table.insert(
			lines,
			`  {if r.ok then "PASS" else "FAIL"} {r.label}{if r.detail ~= "" then " (" .. r.detail .. ")" else ""}`
		)
	end
	return table.concat(lines, "\n")
end

return Harness
