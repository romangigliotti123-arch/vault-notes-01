--!strict
-- Consistency: find UI style values that are used rarely when the kit clearly has a dominant one (corner radius, stroke thickness,
-- font, text size, padding). Pure over flat records so it can be tested; `ui_scan.luau` collects the same records from Instances.
--   local report = Consistency.analyse(records, { "cornerRadius", "font", "textSize" })
--   report.cornerRadius.dominant -> 8 ; report.cornerRadius.outliers -> { { value = 6, paths = {...} } }
local Consistency = {}

export type Record = { path: string, [string]: any }
export type Outlier = { value: any, paths: { string } }
export type FieldReport = { dominant: any, dominantShare: number, distinct: number, outliers: { Outlier } }

-- A value is an outlier when it is not dominant, covers under `maxShare` of the records, and the dominant value covers over `minDominant`.
function Consistency.analyse(
	records: { Record },
	fields: { string },
	maxShare: number?,
	minDominant: number?
): { [string]: FieldReport }
	local lowShare = maxShare or 0.15
	local needDominant = minDominant or 0.5
	local report: { [string]: FieldReport } = {}
	for _, field in fields do
		local counts: { [string]: number } = {}
		local values: { [string]: any } = {}
		local paths: { [string]: { string } } = {}
		local total = 0
		for _, r in records do
			local v = r[field]
			if v ~= nil then
				local k = tostring(v)
				counts[k] = (counts[k] or 0) + 1
				values[k] = v
				paths[k] = paths[k] or {}
				table.insert(paths[k], r.path)
				total += 1
			end
		end
		local topKey: string? = nil
		local distinct = 0
		for k, n in counts do
			distinct += 1
			if topKey == nil or n > counts[topKey] or (n == counts[topKey] and k < topKey) then
				topKey = k
			end
		end
		local fr: FieldReport = { dominant = nil, dominantShare = 0, distinct = distinct, outliers = {} }
		if topKey ~= nil and total > 0 then
			fr.dominant = values[topKey]
			fr.dominantShare = counts[topKey] / total
			if fr.dominantShare >= needDominant then
				local keys = {}
				for k in counts do
					table.insert(keys, k)
				end
				table.sort(keys)
				for _, k in keys do
					if k ~= topKey and counts[k] / total < lowShare then
						table.insert(fr.outliers, { value = values[k], paths = paths[k] })
					end
				end
			end
		end
		report[field] = fr
	end
	return report
end

return Consistency
