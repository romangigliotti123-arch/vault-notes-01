--!strict
local LoadMath = {}

export type Traffic = { name: string, perClientPerSec: number, bytesPerMessage: number }
export type Plan = {
	clients: number,
	traffic: { Traffic },
}
export type Totals = {
	messagesPerSec: number,
	bytesPerSec: number,
	perClientBytesPerSec: number,
	byRemote: { [string]: number },
}

function LoadMath.totals(plan: Plan): Totals
	local msgs, bytes = 0, 0
	local by: { [string]: number } = {}
	for _, tr in plan.traffic do
		local m = plan.clients * tr.perClientPerSec
		msgs += m
		bytes += m * tr.bytesPerMessage
		by[tr.name] = m
	end
	return {
		messagesPerSec = msgs,
		bytesPerSec = bytes,
		perClientBytesPerSec = if plan.clients > 0 then bytes / plan.clients else 0,
		byRemote = by,
	}
end

function LoadMath.worstCase(clients: number, limits: { [string]: number }): number
	local sum = 0
	for _, perSec in limits do
		sum += perSec
	end
	return clients * sum
end

function LoadMath.ramp(
	start: number,
	max: number,
	factor: number,
	holdSeconds: number
): { { clients: number, holdSeconds: number } }
	assert(factor > 1 and start >= 1 and max >= start, "ramp needs factor > 1 and 1 <= start <= max")
	local steps = {}
	local c = start
	while c < max do
		table.insert(steps, { clients = c, holdSeconds = holdSeconds })
		c = math.min(max, math.max(c + 1, math.floor(c * factor)))
	end
	table.insert(steps, { clients = max, holdSeconds = holdSeconds })
	return steps
end

export type Budget = { name: string, measured: number, limit: number, higherIsWorse: boolean? }
export type Verdict = { name: string, measured: number, limit: number, ok: boolean, headroom: number }

function LoadMath.verdicts(budgets: { Budget }): { Verdict }
	local out = {}
	for _, b in budgets do
		local worse = b.higherIsWorse ~= false
		local ok = if worse then b.measured <= b.limit else b.measured >= b.limit
		local headroom = if b.limit == 0
			then 0
			else (if worse then (b.limit - b.measured) / b.limit else (b.measured - b.limit) / b.limit)
		table.insert(out, { name = b.name, measured = b.measured, limit = b.limit, ok = ok, headroom = headroom })
	end
	return out
end

function LoadMath.safeCapacity(steps: { { clients: number, ok: boolean } }): number
	local safe = 0
	for _, s in steps do
		if not s.ok then
			break
		end
		safe = s.clients
	end
	return safe
end

function LoadMath.report(plan: Plan, tot: Totals): string
	local lines = { `LOAD PLAN: {plan.clients} clients` }
	table.insert(
		lines,
		`  messages/s {string.format("%.0f", tot.messagesPerSec)}, bytes/s {string.format("%.0f", tot.bytesPerSec)}, per client {string.format(
			"%.1f",
			tot.perClientBytesPerSec
		)} B/s`
	)
	for _, tr in plan.traffic do
		table.insert(lines, `  {tr.name}: {string.format("%.1f", tot.byRemote[tr.name])} msgs/s`)
	end
	return table.concat(lines, "\n")
end

return LoadMath
