--!strict
local CodeBook = {}

export type Entry = {
	reward: string,
	startsAt: number?,
	expiresAt: number?,
	maxUses: number?,
	creator: string?,
}
export type State = { used: number, mine: { [string]: boolean } }
export type Result = { ok: boolean, reason: string?, code: string?, entry: Entry? }

function CodeBook.normalise(raw: any): string?
	if type(raw) ~= "string" then
		return nil
	end
	if #raw > 64 then
		return nil
	end
	local s = string.upper((string.gsub(raw, "%s+", "")))
	if s == "" then
		return nil
	end
	if string.find(s, "[^A-Z0-9%-]") then
		return nil
	end
	return s
end

function CodeBook.check(book: { [string]: Entry }, raw: any, state: State, now: number): Result
	local code = CodeBook.normalise(raw)
	if code == nil then
		return { ok = false, reason = "invalid" }
	end
	local entry = book[code]
	if entry == nil then
		return { ok = false, reason = "unknown" }
	end
	if entry.startsAt and now < entry.startsAt then
		return { ok = false, reason = "unknown" }
	end
	if entry.expiresAt and now >= entry.expiresAt then
		return { ok = false, reason = "expired" }
	end
	if state.mine[code] then
		return { ok = false, reason = "already_redeemed" }
	end
	if entry.maxUses and state.used >= entry.maxUses then
		return { ok = false, reason = "used_up" }
	end
	return { ok = true, code = code, entry = entry }
end

function CodeBook.validateBook(book: { [string]: Entry }): { string }
	local problems = {}
	for code, e in book do
		if CodeBook.normalise(code) ~= code then
			table.insert(problems, `{code}: not in normalised form (A-Z, 0-9, dash)`)
		end
		if type(e.reward) ~= "string" or e.reward == "" then
			table.insert(problems, `{code}: missing reward label`)
		end
		if e.startsAt and e.expiresAt and e.expiresAt <= e.startsAt then
			table.insert(problems, `{code}: expiresAt is not after startsAt`)
		end
		if e.maxUses and e.maxUses < 1 then
			table.insert(problems, `{code}: maxUses must be at least 1`)
		end
	end
	table.sort(problems)
	return problems
end

return CodeBook
