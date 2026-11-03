--!strict
-- Retry: run a yielding call that can fail for reasons outside your code (DataStore, MarketplaceService, HttpService) with
-- exponential backoff, jitter, a retry budget and an "is this worth retrying" test. Wait and random are injected for tests.
--   local ok, result, tries = Retry.run(function() return store:GetAsync(key) end, { attempts = 5, base = 0.5 })
--   if not ok then ... result is the last error message end
-- The kit's PlayerData system already retries its own saves and loads: do not wrap those calls again (retries multiply).
-- Use this for the calls the kit does not cover: MarketplaceService:GetProductInfo, HTTP, MemoryStore, extra DataStores.
local Retry = {}

export type Options = {
	attempts: number?, -- total tries including the first (default 4)
	base: number?, -- first delay in seconds (default 0.5)
	factor: number?, -- delay multiplier per attempt (default 2)
	max: number?, -- cap for one delay (default 8)
	jitter: number?, -- 0..1, fraction of the delay randomised either way (default 0.2)
	budget: number?, -- stop retrying once this many seconds of waiting have been spent (default no limit)
	retryable: ((err: string) -> boolean)?,
	wait: ((seconds: number) -> ())?,
	random: (() -> number)?, -- returns 0..1
	onRetry: ((attempt: number, err: string, delay: number) -> ())?,
}

-- the vault's official DataStore sample (Creator Docs 2026-10): 5 attempts, 2 s base, 32 s max delay. Live-check before shipping.
Retry.DATASTORE = { attempts = 5, base = 2, max = 32 } :: Options

-- delay before the retry that follows `attempt` (1 = after the first failure). jitter spreads herds of servers apart.
function Retry.delayFor(attempt: number, options: Options?): number
	local o: Options = options or {}
	local delay = math.min((o.base or 0.5) * (o.factor or 2) ^ (attempt - 1), o.max or 8)
	local jitter = o.jitter or 0.2
	local random: () -> number = o.random or function()
		return math.random()
	end
	local r = random()
	return math.max(0, delay * (1 + jitter * (2 * r - 1)))
end

-- heuristic by message text: throttling and transient network faults are worth retrying, bad input and permission errors are not
function Retry.classify(err: string): string
	local lower = string.lower(err)
	for _, needle in
		{ "403", "401", "400", "invalid", "not allowed", "permission", "not found", "forbidden", "studio access" }
	do
		if string.find(lower, needle, 1, true) then
			return "permanent"
		end
	end
	for _, needle in
		{
			"429",
			"throttl",
			"keythrottled",
			"datastorethrottled",
			"301",
			"302",
			"303",
			"304",
			"305",
			"306",
			"queue",
			"timed out",
			"timeout",
			"503",
			"502",
			"500",
			"unavailable",
			"internal",
			"http",
		}
	do
		if string.find(lower, needle, 1, true) then
			return "transient"
		end
	end
	return "unknown"
end

local function defaultWait(seconds: number)
	if task then
		task.wait(seconds)
	end
end

-- (ok, result or last error message, attempts used)
function Retry.run(fn: () -> any, options: Options?): (boolean, any, number)
	local o: Options = options or {}
	local attempts = o.attempts or 4
	local wait = o.wait or defaultWait
	local spent = 0
	local lastErr = "no attempt made"
	for attempt = 1, attempts do
		local ok, result = pcall(fn)
		if ok then
			return true, result, attempt
		end
		lastErr = tostring(result)
		local retryable = if o.retryable then o.retryable(lastErr) else Retry.classify(lastErr) ~= "permanent"
		if attempt == attempts or not retryable then
			return false, lastErr, attempt
		end
		local delay = Retry.delayFor(attempt, o)
		if o.budget and spent + delay > o.budget then
			return false, lastErr, attempt
		end
		spent += delay
		if o.onRetry then
			o.onRetry(attempt, lastErr, delay)
		end
		wait(delay)
	end
	return false, lastErr, attempts
end

return Retry
