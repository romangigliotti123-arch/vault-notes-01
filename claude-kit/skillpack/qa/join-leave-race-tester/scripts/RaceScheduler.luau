--!strict
local RaceScheduler = {}

export type Step = (state: any) -> ()
export type Actor = { name: string, steps: { Step } }
export type Failure = { schedule: string, message: string }
export type Result = { runs: number, failures: { Failure }, truncated: boolean }

function RaceScheduler.count(lengths: { number }): number
	local total, result = 0, 1
	for _, n in lengths do
		for i = 1, n do
			total += 1
			result = result * total / i
		end
	end
	return math.floor(result + 0.5)
end

function RaceScheduler.explore(
	setup: () -> any,
	actors: { Actor },
	invariant: (state: any) -> string?,
	maxRuns: number?
): Result
	local limit = maxRuns or 20000
	local result: Result = { runs = 0, failures = {}, truncated = false }
	local pos: { number } = {}
	local order: { number } = {}
	local totalSteps = 0
	for i, a in actors do
		pos[i] = 0
		totalSteps += #a.steps
	end
	local function replay()
		local state = setup()
		local label = {}
		local seen: { number } = {}
		for i = 1, #actors do
			seen[i] = 0
		end
		local errorMsg: string? = nil
		for _, ai in order do
			seen[ai] += 1
			local actor = actors[ai]
			table.insert(label, `{actor.name}{seen[ai]}`)
			local ok, err = pcall(actor.steps[seen[ai]] :: (any) -> any, state)
			if not ok and errorMsg == nil then
				errorMsg = `{actor.name}{seen[ai]} errored: {tostring(err)}`
			end
		end
		result.runs += 1
		local msg = errorMsg or invariant(state)
		if msg ~= nil then
			table.insert(result.failures, { schedule = table.concat(label, " "), message = msg })
		end
	end
	local function recurse(depth: number)
		if result.runs >= limit then
			result.truncated = true
			return
		end
		if depth == totalSteps then
			replay()
			return
		end
		for i, a in actors do
			if pos[i] < #a.steps then
				pos[i] += 1
				order[depth + 1] = i
				recurse(depth + 1)
				pos[i] -= 1
				if result.runs >= limit then
					result.truncated = true
					return
				end
			end
		end
	end
	recurse(0)
	return result
end

function RaceScheduler.report(r: Result, maxShown: number?): string
	local lines = { `RACE: {r.runs} schedules run, {#r.failures} failing{if r.truncated then " (capped)" else ""}` }
	for i, f in r.failures do
		if i > (maxShown or 5) then
			table.insert(lines, `  ... {#r.failures - (maxShown or 5)} more`)
			break
		end
		table.insert(lines, `  FAIL {f.schedule}: {f.message}`)
	end
	return table.concat(lines, "\n")
end

return RaceScheduler
