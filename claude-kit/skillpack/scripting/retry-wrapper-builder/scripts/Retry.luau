--!strict
local Retry = {}

export type Options = {
	attempts: number?,
	base: number?,
	factor: number?,
	max: number?,
	jitter: number?,
	budget: number?,
	retryable: ((err: string) -> boolean)?,
	wait: ((seconds: number) -> ())?,
	random: (() -> number)?,
	onRetry: ((attempt: number, err: string, delay: number) -> ())?,
}

Retry.DATASTORE = { attempts = 5, base = 2, max = 32 } :: Options

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
