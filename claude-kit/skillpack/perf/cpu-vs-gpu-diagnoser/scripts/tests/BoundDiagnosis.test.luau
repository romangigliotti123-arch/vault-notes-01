--!nocheck
local t = require("../../../../../systems/_check/harness")
local BoundDiagnosis = require("../BoundDiagnosis")

t.test("a frame inside the goal is not diagnosed", function()
	t.eq(BoundDiagnosis.diagnose({ frameMs = 14, jobsMs = 9, renderMs = 4, gpuWaitMs = 0 }).bound, "none")
end)

t.test("GPU wait over 2.5 ms wins even when Jobs is bigger", function()
	local d = BoundDiagnosis.diagnose({ frameMs = 30, jobsMs = 12, renderMs = 8, gpuWaitMs = 6 })
	t.eq(d.bound, "gpu")
	t.eq(d.colour, "red")
end)

t.test("Jobs bigger than Render is orange simulation cost", function()
	local d = BoundDiagnosis.diagnose({ frameMs = 25, jobsMs = 18, renderMs = 5, gpuWaitMs = 1 })
	t.eq(d.bound, "cpu-simulation")
	t.eq(d.nextSkills[1], "script-profiler")
end)

t.test("Render bigger than Jobs is blue render prep", function()
	local d = BoundDiagnosis.diagnose({ frameMs = 25, jobsMs = 4, renderMs = 17, gpuWaitMs = 2.5 })
	t.eq(d.bound, "cpu-render-prep")
	t.eq(d.colour, "blue")
end)

t.test("goal can be 30 FPS for phones and improvement is a percentage", function()
	t.eq(BoundDiagnosis.diagnose({ frameMs = 30, jobsMs = 10, renderMs = 5, gpuWaitMs = 0 }, 33.33).bound, "none")
	t.eq(
		BoundDiagnosis.improvement(
			{ frameMs = 40, jobsMs = 0, renderMs = 0, gpuWaitMs = 0 },
			{ frameMs = 30, jobsMs = 0, renderMs = 0, gpuWaitMs = 0 }
		),
		25
	)
end)

t.done()
