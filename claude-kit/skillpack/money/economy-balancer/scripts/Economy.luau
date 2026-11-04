--!strict
local Economy = {}

export type Flow = { name: string, perHour: number }
export type Config = {
	sources: { Flow },
	sinks: { Flow },
	hours: number,
	startBalance: number?,
	minSinkRatio: number?,
	maxUnmetShare: number?,
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

function Economy.hoursToEarn(price: number, incomePerHour: number, balance: number?): number
	assert(incomePerHour > 0, "incomePerHour must be > 0")
	return math.max(0, math.ceil((price - (balance or 0)) / incomePerHour))
end

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
