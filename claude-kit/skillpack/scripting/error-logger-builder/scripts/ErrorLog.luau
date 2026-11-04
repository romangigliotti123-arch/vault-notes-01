--!strict
local ErrorLog = {}
ErrorLog.__index = ErrorLog

export type Entry = { name: string, message: string, trace: string, time: number, repeats: number }
export type Options = {
	clock: (() -> number)?,
	sink: ((entry: Entry) -> ())?,
	window: number?,
	capacity: number?,
	print: ((text: string) -> ())?,
}
export type Log = typeof(setmetatable(
	{} :: {
		_clock: () -> number,
		_sink: ((entry: Entry) -> ())?,
		_window: number,
		_capacity: number,
		_print: (text: string) -> (),
		_recent: { Entry },
		_seen: { [string]: { first: number, suppressed: number } },
		_total: number,
		_suppressed: number,
	},
	ErrorLog
))

function ErrorLog.new(options: Options?): Log
	local o: Options = options or {}
	return setmetatable({
		_clock = o.clock or os.clock,
		_sink = o.sink,
		_window = o.window or 10,
		_capacity = o.capacity or 50,
		_print = o.print or function(text: string)
			warn(text)
		end,
		_recent = {},
		_seen = {},
		_total = 0,
		_suppressed = 0,
	}, ErrorLog)
end

function ErrorLog.Report(self: Log, name: string, message: string, trace: string?): boolean
	self._total += 1
	local now = self._clock()
	local key = name .. "\0" .. message
	local seen = self._seen[key]
	if seen and now - seen.first < self._window then
		seen.suppressed += 1
		self._suppressed += 1
		return false
	end
	local repeats = if seen then seen.suppressed else 0
	self._seen[key] = { first = now, suppressed = 0 }
	local entry: Entry = { name = name, message = message, trace = trace or "", time = now, repeats = repeats }
	table.insert(self._recent, entry)
	if #self._recent > self._capacity then
		table.remove(self._recent, 1)
	end
	local suffix = if repeats > 0 then ` (+{repeats} repeats)` else ""
	self._print(`[{name}] {message}{suffix}`)
	if self._sink then
		pcall(self._sink :: (Entry) -> (), entry)
	end
	return true
end

function ErrorLog.Try(self: Log, name: string, fn: (...any) -> ...any, ...: any): (boolean, any)
	local results = table.pack(xpcall(fn, function(err: any): string
		return tostring(err) .. "\n" .. debug.traceback("", 2)
	end, ...))
	if results[1] then
		return true, results[2]
	end
	local text = tostring(results[2])
	local message, trace = string.match(text, "^(.-)\n(.*)$")
	self:Report(name, message or text, trace)
	return false, nil
end

function ErrorLog.Wrap(self: Log, name: string, fn: (...any) -> ...any): (...any) -> ()
	return function(...: any)
		self:Try(name, fn, ...)
	end
end

function ErrorLog.Recent(self: Log): { Entry }
	return table.clone(self._recent)
end

function ErrorLog.Stats(self: Log): { total: number, suppressed: number, distinct: number }
	local distinct = 0
	for _ in self._seen do
		distinct += 1
	end
	return { total = self._total, suppressed = self._suppressed, distinct = distinct }
end

return ErrorLog
