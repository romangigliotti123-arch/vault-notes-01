# Roblox benchmark table (curated from the KB; generated 2026-10-29 14:31)

Flag: official = Roblox docs/staff/sessions; indie = creator self-reported; mixed; devforum; none = KB gap. Compare numbers with `compare.py`; full tables in `_tools/BENCHMARKS.md`. Official method: your Creator Hub Similar Experience Benchmarks (50th-90th percentile).

| Metric | Bands | Flag |
|---|---|---|
| D1 retention (`--d1`) | 0-6 %: broken; 6-10 %: weak; 10-16 %: typical (indie); 16-100 %: strong (at or above the 90th percentile for same-genre per an official talk) | mixed |
| D7 retention (`--d7`) | 0-1.5 %: weak; 1.5-2 %: below typical; 2-4 %: typical (indie); 4-100 %: strong | indie |
| D30 retention (`--d30`) | KB GAP | none |
| Average session length (`--session`) | 0-5 min: really bad (DevForum author); 5-7 min: average; 7-9 min: good; 9-15 min: excellent; 15-inf min: very strong | mixed |
| Play-through rate (PTR/QPTR) (`--ptr`) | 0-2 %: low; 2-3 %: okay; 3-100 %: healthy (indie about 3%; official sample 3.5% qPTR) | mixed |
| Ad / thumbnail CTR (`--ctr`) | 0-1 %: replace the creative; 1-1.5 %: poor; 1.5-2.5 %: below average; 2.5-3.5 %: average to good; 3.5-100 %: exceptional | indie |
| Payer conversion (`--conv`) | 0-1 %: low; 1-2 %: okay (official sample 1.63%); 2-3 %: healthy (indie 2-3%); 3-100 %: strong | mixed |
| ARPPU (`--arppu`) | KB GAP | official |
| Median join time (`--join`) | 0-5 s: good; 5-10 s: okay; 10-inf s: not great, fix | official |
| First-session retention at 5 minutes (`--fs5`) | 0-30 %: weak (others 20-30%); 30-65 %: middling; 65-100 %: healthy (one indie example 65%) | indie |
| First-play bounce (`--bounce`) | KB GAP | none |
| Ad cost per play (`--cpp`) | 0-0.008 USD: at or better than indie day-one target; 0.008-0.013 USD: typical indie (about 1.3c down to under 1c); 0.013-inf USD: expensive: fix creative and CTR first | mixed |
| Rewarded-video opt-in rate (`--optin`) | 0-13 %: below official floor; 13-15 %: meets floor; 15-30 %: genre average range (15-25%); 30-100 %: best in class | official |
| Client frame rate (`--fps`) | 0-30 FPS: poor on mobile; 30-60 FPS: below target; 60-inf FPS: target met | official |

Note and Sources columns: [cold:rbx-metrics/benchmark-notes.md] read only to verify a band's source or caveat (Note and Sources columns), or when a number is challenged.
