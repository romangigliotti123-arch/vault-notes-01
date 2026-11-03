--!strict
-- Economy: hour-by-hour simulation of one average player's soft-currency balance from declared sources and sinks.
-- It answers "does this economy inflate or starve?" before you ship numbers; the inputs are YOUR assumptions, so label results as a model.
--   local r = Economy.simulate({ sources = { { name = "mining", perHour = 600 } }, sinks = { { name = "upgrades", perHour = 500 } }, hours = 20 })
--   print(r.verdict, r.sinkRatio, r.endBalance)
local Economy = {}

export type Flow = { name: string, perHour: number }
export type Config = {
	sources: { Flow },
	sinks: { Flow }, -- demand per hour: what the player WANTS to spend if they can afford it
	hours: number,
	startBalance: number?,
	minSinkRatio: number?, -- below this spent/income the economy is called inflating (default 0.6, a heuristic, tune it)
	maxUnmetShare: number?, -- above this unmet demand share the economy is called starved (default 0.3)
}
export type Result = {
	balances: { number },
	income: number,
	spent: number,
	unmet: number,
	sinkRatio: number,
	endBalance: number,
	verdict: "inflating" | "balanced" | "starved",
}

local function total(flows: { Flow }): number
	local sum = 0
	for _, f in flows do
		assert(type(f.perHour) == "number" and f.perHour >= 0, `flow {f.name} needs perHour >= 0`)
		sum += f.perHour
	end
	return sum
end

function Economy.simulate(cfg: Config): Result
	assert(cfg.hours >= 1 and cfg.hours == math.floor(cfg.hours), "hours must be a whole number >= 1")
	local perHourIncome = total(cfg.sources)
	local perHourDemand = total(cfg.sinks)
	local balance = cfg.startBalance or 0
	local balances: { number } = {}
	local income, spent, unmet = 0, 0, 0
	for _ = 1, cfg.hours do
		local spend = math.min(perHourDemand, balance + perHourIncome)
		unmet += perHourDemand - spend
		spent += spend
		income += perHourIncome
		balance = balance + perHourIncome - spend
		table.insert(balances, balance)
	end
	local sinkRatio = if income > 0 then spent / income else 0
	local demand = perHourDemand * cfg.hours
	local verdict: "inflating" | "balanced" | "starved" = "balanced"
	if demand > 0 and unmet / demand > (cfg.maxUnmetShare or 0.3) then
		verdict = "starved"
	elseif sinkRatio < (cfg.minSinkRatio or 0.6) then
		verdict = "inflating"
	end
	return {
		balances = balances,
		income = income,
		spent = spent,
		unmet = unmet,
		sinkRatio = sinkRatio,
		endBalance = balance,
		verdict = verdict,
	}
end

-- hours of play to afford `price` from `balance` at `incomePerHour` with no other spending (whole hours, rounded up)
function Economy.hoursToEarn(price: number, incomePerHour: number, balance: number?): number
	assert(incomePerHour > 0, "incomePerHour must be > 0")
	return math.max(0, math.ceil((price - (balance or 0)) / incomePerHour))
end

-- share of income per source, largest first
function Economy.shares(sources: { Flow }): { { name: string, share: number } }
	local sum = total(sources)
	local out = {}
	for _, f in sources do
		table.insert(out, { name = f.name, share = if sum > 0 then f.perHour / sum else 0 })
	end
	table.sort(out, function(a, b)
		return a.share > b.share
	end)
	return out
end

return Economy
