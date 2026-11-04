--!strict
local LeakTrend = {}

export type Trend = { slopePerMinute: number, r2: number, first: number, last: number, verdict: string }
export type Delta = { class: string, before: number, after: number, delta: number }

function LeakTrend.analyze(series: { number }, dtSeconds: number, minSlopePerMinute: number?): Trend
	local n = #series
	if n < 4 then
		return { slopePerMinute = 0, r2 = 0, first = series[1] or 0, last = series[n] or 0, verdict = "too-few-samples" }
	end
	local sumX, sumY, sumXY, sumXX = 0, 0, 0, 0
	for i, y in series do
		local x = (i - 1) * dtSeconds / 60
		sumX += x
		sumY += y
		sumXY += x * y
		sumXX += x * x
	end
	local denom = n * sumXX - sumX * sumX
	local slope = if denom == 0 then 0 else (n * sumXY - sumX * sumY) / denom
	local intercept = (sumY - slope * sumX) / n
	local meanY = sumY / n
	local ssTot, ssRes = 0, 0
	for i, y in series do
		local x = (i - 1) * dtSeconds / 60
		local fit = intercept + slope * x
		ssTot += (y - meanY) ^ 2
		ssRes += (y - fit) ^ 2
	end
	local r2 = if ssTot == 0 then 0 else 1 - ssRes / ssTot
	local verdict = "flat"
	if slope >= (minSlopePerMinute or 1) and r2 >= 0.8 and series[n] > series[1] then
		verdict = "growing"
	elseif slope >= (minSlopePerMinute or 1) then
		verdict = "noisy-growth"
	elseif slope <= -(minSlopePerMinute or 1) then
		verdict = "shrinking"
	end
	return { slopePerMinute = slope, r2 = r2, first = series[1], last = series[n], verdict = verdict }
end

function LeakTrend.diff(before: { [string]: number }, after: { [string]: number }): { Delta }
	local out: { Delta } = {}
	local seen: { [string]: boolean } = {}
	for k, v in after do
		seen[k] = true
		local b = before[k] or 0
		if v > b then
			table.insert(out, { class = k, before = b, after = v, delta = v - b })
		end
	end
	for k in before do
		seen[k] = true
	end
	table.sort(out, function(a, b)
		if a.delta ~= b.delta then
			return a.delta > b.delta
		end
		return a.class < b.class
	end)
	return out
end

return LeakTrend
