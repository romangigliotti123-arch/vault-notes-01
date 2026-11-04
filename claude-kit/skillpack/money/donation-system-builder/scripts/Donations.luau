--!strict
local Donations = {}

export type Config = {
	min: number,
	max: number,
	presets: { number }?,
}
export type Board = { totals: { [number]: number }, names: { [number]: string }, seen: { [string]: boolean } }

function Donations.validate(cfg: Config, fromUserId: number, toUserId: number, amount: any): (boolean, string)
	if type(amount) ~= "number" or amount ~= amount or amount ~= math.floor(amount) then
		return false, "amount must be a whole number"
	end
	if amount < cfg.min or amount > cfg.max then
		return false, `amount must be between {cfg.min} and {cfg.max}`
	end
	if cfg.presets and not table.find(cfg.presets, amount) then
		return false, "amount is not one of the offered choices"
	end
	if fromUserId == toUserId then
		return false, "you cannot donate to yourself"
	end
	return true, "ok"
end

function Donations.newBoard(): Board
	return { totals = {}, names = {}, seen = {} }
end

function Donations.add(board: Board, receiptId: string, userId: number, name: string, amount: number): boolean
	if board.seen[receiptId] then
		return false
	end
	assert(amount > 0, "amount must be positive")
	board.seen[receiptId] = true
	board.totals[userId] = (board.totals[userId] or 0) + amount
	board.names[userId] = name
	return true
end

function Donations.top(board: Board, n: number): { { userId: number, name: string, total: number } }
	local rows = {}
	for userId, total in board.totals do
		table.insert(rows, { userId = userId, name = board.names[userId] or "", total = total })
	end
	table.sort(rows, function(a, b)
		if a.total ~= b.total then
			return a.total > b.total
		end
		return a.userId < b.userId
	end)
	local out = {}
	for i = 1, math.min(n, #rows) do
		table.insert(out, rows[i])
	end
	return out
end

return Donations
