--!strict
-- RaceScheduler: deterministic interleaving explorer for join/leave/trade/purchase races. Pure logic, unit-tested in Lune.
-- Roblox code yields at DataStore calls, MarketplaceService calls, task.wait and remote round trips; a race is a bad ORDER of the pieces
-- between yields. Model each actor as a list of atomic steps (the code between two yields), then run every interleaving that keeps each
-- actor's own order and check an invariant after each. A failing schedule is a reproduction you can replay in Studio with task.wait().
local RaceScheduler = {}

export type Step = (state: any) -> ()
export type Actor = { name: string, steps: { Step } }
export type Failure = { schedule: string, message: string }
export type Result = { runs: number, failures: { Failure }, truncated: boolean }

-- number of distinct interleavings of actors with the given step counts (multinomial)
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

-- setup() returns a fresh state; invariant(state) returns nil when fine or a message when violated (checked after the last step).
-- maxRuns caps the exploration (the first maxRuns schedules in a fixed order); `truncated` says the cap was hit.
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
