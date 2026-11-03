--!strict
-- Ledger: server-side record of every currency source and sink, and a report that finds inflation and lopsided income.
-- Call Ledger.record at the ONE place each grant/spend happens (the same place that changes the balance), never from the client.
--   local ledger = Ledger.new()
--   Ledger.record(ledger, "source", "quest_reward", 150)
--   Ledger.record(ledger, "sink", "pet_upgrade", 120)
--   local report = Ledger.report(ledger)   -- report.flags lists problems in plain words
local Ledger = {}

export type Kind = "source" | "sink"
export type Ledger = { source: { [string]: number }, sink: { [string]: number }, count: number }
export type Row = { name: string, total: number, share: number }
export type Report = {
	sourceTotal: number,
	sinkTotal: number,
	ratio: number,
	sources: { Row },
	sinks: { Row },
	flags: { string },
}

function Ledger.new(): Ledger
	return { source = {}, sink = {}, count = 0 }
end

function Ledger.record(l: Ledger, kind: Kind, name: string, amount: number)
	assert(kind == "source" or kind == "sink", "kind must be source or sink")
	assert(type(name) == "string" and name ~= "", "name required")
	assert(type(amount) == "number" and amount > 0 and amount == amount, "amount must be a positive number")
	local bucket = l[kind]
	bucket[name] = (bucket[name] or 0) + amount
	l.count += 1
end

local function rows(bucket: { [string]: number }): ({ Row }, number)
	local sum = 0
	for _, v in bucket do
		sum += v
	end
	local out: { Row } = {}
	for name, v in bucket do
		table.insert(out, { name = name, total = v, share = if sum > 0 then v / sum else 0 })
	end
	table.sort(out, function(a, b)
		if a.total ~= b.total then
			return a.total > b.total
		end
		return a.name < b.name
	end)
	return out, sum
end

-- minRatio: sinks/sources below this = inflation risk (default 0.6, a heuristic). maxShare: one source above this share = fragile (default 0.6).
function Ledger.report(l: Ledger, minRatio: number?, maxShare: number?): Report
	local sources, sourceTotal = rows(l.source)
	local sinks, sinkTotal = rows(l.sink)
	local ratio = if sourceTotal > 0 then sinkTotal / sourceTotal else 0
	local flags: { string } = {}
	if sourceTotal == 0 then
		table.insert(flags, "no sources recorded: nothing to analyse")
	else
		if sinkTotal == 0 then
			table.insert(flags, "no sinks recorded: every unit earned is still in circulation")
		elseif ratio < (minRatio or 0.6) then
			table.insert(
				flags,
				`sink/source ratio {math.floor(ratio * 100)}% is low: inflation risk, add or strengthen sinks`
			)
		end
		if #sources > 1 and sources[1].share > (maxShare or 0.6) then
			table.insert(
				flags,
				`source "{sources[1].name}" is {math.floor(sources[1].share * 100)}% of income: one exploit or change there breaks the economy`
			)
		end
		if ratio > 1.05 then
			table.insert(
				flags,
				"sinks exceed sources in this window: balances are draining (check starting grants and refunds)"
			)
		end
	end
	return {
		sourceTotal = sourceTotal,
		sinkTotal = sinkTotal,
		ratio = ratio,
		sources = sources,
		sinks = sinks,
		flags = flags,
	}
end

return Ledger
