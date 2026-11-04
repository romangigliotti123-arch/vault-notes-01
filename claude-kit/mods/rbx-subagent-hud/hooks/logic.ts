import type { Eta, Hist, Item, Prompt, Rec, RecStatus, Turn } from '../types'

export const MAX_RECS = 60
export const MAX_PROMPTS = 50
export const MAX_PROMPT_CHARS = 20000
export const MAX_SAMPLES = 20
export const MAX_CLASSES = 40
export const FLOOR_MS = 10_000
export const DEFAULT_AGENT_MS = 120_000
export const DEFAULT_WRAP_MS = 20_000
export const MISSING_GRACE_MS = 3000

export const emptyHist = (): Hist => ({ v: 1, byClass: {}, byType: {}, wrap: [] })

export const isEnded = (s: RecStatus): boolean => s === 'done' || s === 'failed' || s === 'killed'
export const isActive = (s: RecStatus): boolean => s === 'running' || s === 'queued' || s === 'waiting'

export function toRecStatus(s: string): RecStatus {
  switch (s) {
    case 'pending':
      return 'queued'
    case 'running':
      return 'running'
    case 'waiting':
      return 'waiting'
    case 'completed':
    case 'idle':
      return 'done'
    case 'failed':
      return 'failed'
    case 'killed':
      return 'killed'
    default:
      return 'waiting'
  }
}

// 45s, 3m12s, 1h02m
export function fmt(ms: number): string {
  const s = Math.max(0, Math.floor(ms / 1000))
  if (s < 60) return `${s}s`
  const m = Math.floor(s / 60)
  if (m < 60) return `${m}m${String(s % 60).padStart(2, '0')}s`
  return `${Math.floor(m / 60)}h${String(m % 60).padStart(2, '0')}m`
}

export function fmtLeft(ms: number): string {
  const v = Math.max(0, ms)
  if (v < 60_000) return '<1 min'
  const m = Math.ceil(v / 60_000)
  if (m < 60) return `~${m} min`
  return `~${Math.floor(m / 60)}h ${String(m % 60).padStart(2, '0')}m`
}

export const clip = (s: string, n: number): string =>
  n <= 0 ? '' : n === 1 ? (s.length <= 1 ? s : '…') : s.length <= n ? s : s.slice(0, n - 1) + '…'

export function median(xs: readonly number[]): number {
  if (xs.length === 0) return 0
  const s = [...xs].sort((a, b) => a - b)
  const mid = Math.floor(s.length / 2)
  return s.length % 2 === 1 ? s[mid]! : Math.round((s[mid - 1]! + s[mid]!) / 2)
}

export function classOf(type: string, description: string): string {
  const words = description
    .toLowerCase()
    .replace(/[0-9]+/g, ' ')
    .split(/[^a-z]+/)
    .filter(w => w.length > 2)
    .slice(0, 3)
    .join(' ')
  return `${type}|${words}`
}

function pushSample(map: Record<string, number[]>, key: string, ms: number, maxKeys: number): void {
  const prior = map[key] ?? []
  delete map[key]
  map[key] = [...prior, ms].slice(-MAX_SAMPLES)
  const keys = Object.keys(map)
  for (const k of keys.slice(0, Math.max(0, keys.length - maxKeys))) delete map[k]
}

export function recordDuration(hist: Hist, rec: Pick<Rec, 'type' | 'name' | 'start' | 'end'>): Hist {
  if (rec.end === undefined) return hist
  const ms = rec.end - rec.start
  if (!(ms >= 1000) || ms > 6 * 3600_000) return hist
  const next: Hist = { v: 1, byClass: { ...hist.byClass }, byType: { ...hist.byType }, wrap: hist.wrap }
  pushSample(next.byClass, classOf(rec.type, rec.name), ms, MAX_CLASSES)
  pushSample(next.byType, rec.type, ms, 20)
  return next
}

export function recordWrap(hist: Hist, ms: number): Hist {
  if (!(ms >= 0) || ms > 30 * 60_000) return hist
  return { ...hist, wrap: [...hist.wrap, ms].slice(-MAX_SAMPLES) }
}

export type Typical = { ms: number; level: 'class' | 'type' | 'all' | 'none'; samples: number }

export function typicalFor(hist: Hist, rec: Pick<Rec, 'type' | 'name'>): Typical {
  const cls = hist.byClass[classOf(rec.type, rec.name)] ?? []
  if (cls.length > 0) return { ms: median(cls), level: 'class', samples: cls.length }
  const typ = hist.byType[rec.type] ?? []
  if (typ.length > 0) return { ms: median(typ), level: 'type', samples: typ.length }
  const all = Object.values(hist.byType).flat()
  if (all.length >= 3) return { ms: median(all), level: 'all', samples: all.length }
  return { ms: DEFAULT_AGENT_MS, level: 'none', samples: 0 }
}

export function counts(recs: readonly Rec[]): {
  total: number
  done: number
  running: number
  queued: number
  failed: number
} {
  let done = 0
  let running = 0
  let queued = 0
  let failed = 0
  for (const r of recs) {
    if (r.status === 'done') done++
    else if (r.status === 'failed' || r.status === 'killed') failed++
    else if (r.status === 'queued') queued++
    else running++
  }
  return { total: recs.length, done, running, queued, failed }
}

// Agents run in parallel: the master waits for the longest remaining one, then its own wrap-up.
export function estimate(recs: readonly Rec[], hist: Hist, now: number): Eta {
  const active = recs.filter(r => isActive(r.status))
  if (active.length === 0) return { kind: 'none', ms: 0, conf: 'none' }
  let longest = 0
  let isLow = false
  let hasHistory = false
  for (const r of active) {
    const t = typicalFor(hist, r)
    const elapsed = r.status === 'queued' ? 0 : Math.max(0, now - r.start)
    const left = r.status === 'queued' ? t.ms : Math.max(t.ms - elapsed, FLOOR_MS)
    if (t.level !== 'none') hasHistory = true
    if (t.level === 'none' || t.samples < 2 || elapsed > t.ms) isLow = true
    longest = Math.max(longest, left)
  }
  const hasWrap = hist.wrap.length > 0
  if (!hasWrap) isLow = true
  const ms = longest + (hasWrap ? median(hist.wrap) : DEFAULT_WRAP_MS)
  return { kind: hasHistory ? 'est' : 'estimating', ms, conf: isLow ? 'low' : 'ok' }
}

export function etaLabel(eta: Eta): string {
  if (eta.kind === 'none') return ''
  if (eta.kind === 'estimating') return `estimating... (${fmtLeft(eta.ms)}, low confidence)`
  return `${fmtLeft(eta.ms)} left (estimate${eta.conf === 'low' ? ', low confidence' : ''})`
}

export type ListedAgent = {
  id: string
  parentId?: string
  description: string
  type: string
  status: string
  name?: string
}

export type EndHint = { at: number; status: RecStatus }

// Merge the engine's live list into the kept records: the list drops an agent
// seconds after it ends, so a missing one is closed by its hint (or as done).
export function mergeRecs(
  prior: readonly Rec[],
  list: readonly ListedAgent[],
  now: number,
  turn: number,
  hints: Readonly<Record<string, EndHint>>,
): Rec[] {
  const byId = new Map(prior.map(r => [r.id, r]))
  const live = new Set<string>()
  for (const a of list) {
    live.add(a.id)
    const old = byId.get(a.id)
    const hint = hints[a.id]
    let status = toRecStatus(a.status)
    if (old !== undefined && isEnded(old.status) && !isEnded(status)) status = old.status
    if (hint !== undefined && status === 'running') status = hint.status
    const end = isEnded(status) ? (old?.end ?? hint?.at ?? now) : undefined
    byId.set(a.id, {
      id: a.id,
      parentId: a.parentId,
      name: a.description || a.name || a.type,
      type: a.type,
      model: old?.model,
      status,
      start: old?.start ?? now,
      end,
      turn: old?.turn ?? turn,
    })
  }
  for (const [id, r] of byId) {
    if (!live.has(id) && !isEnded(r.status)) {
      const hint = hints[id]
      if (hint !== undefined || now - r.start >= MISSING_GRACE_MS) {
        byId.set(id, { ...r, status: hint?.status ?? 'done', end: hint?.at ?? now })
      }
    }
  }
  return [...byId.values()].sort((a, b) => a.start - b.start).slice(-MAX_RECS)
}

export function addPrompt(list: readonly Prompt[], p: Prompt): Prompt[] {
  const text = p.text.length > MAX_PROMPT_CHARS ? p.text.slice(0, MAX_PROMPT_CHARS) : p.text
  const entry: Prompt = { ...p, text, chars: p.text.length, isTruncated: p.text.length > MAX_PROMPT_CHARS }
  const rest = list.filter(x => x.toolUseId !== p.toolUseId || p.toolUseId === '')
  return [...rest, entry].slice(-MAX_PROMPTS)
}

export function promptFor(list: readonly Prompt[], rec: Pick<Rec, 'id'>): Prompt | undefined {
  return list.find(p => p.id === rec.id)
}

export type Row = { rec: Rec; depth: number; index: number }

// Depth 1 = spawned by the master (or by an agent no longer shown); deeper
// levels are sub-subagents. Index counts from 1 in spawn order.
export function buildRows(recs: readonly Rec[]): Row[] {
  const ids = new Set(recs.map(r => r.id))
  const byId = new Map(recs.map(r => [r.id, r]))
  const depthOf = (r: Rec): number => {
    let d = 1
    let p = r.parentId === undefined ? undefined : byId.get(r.parentId)
    while (p !== undefined && d < 8) {
      d++
      p = p.parentId === undefined || !ids.has(p.parentId) ? undefined : byId.get(p.parentId)
    }
    return d
  }
  return recs
    .map((rec, i) => ({ rec, depth: depthOf(rec), index: i + 1 }))
    .sort((a, b) => a.depth - b.depth || a.index - b.index)
}

export type Phase = 0 | 1

export type LineStyle = {
  color: string
  isDim: boolean
  isFlashing: boolean
  isSolid: boolean
  glyph: string
}

const SPIN = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']

export function lineStyle(status: RecStatus, tick: number, isSelected: boolean): LineStyle {
  const phase: Phase = tick % 2 === 0 ? 0 : 1
  const cyan = isSelected
  switch (status) {
    case 'running':
      return {
        color: cyan ? 'cyan' : phase === 0 ? 'white' : 'gray',
        isDim: false,
        isFlashing: true,
        isSolid: cyan,
        glyph: SPIN[tick % SPIN.length]!,
      }
    case 'done':
      return { color: 'green', isDim: false, isFlashing: false, isSolid: cyan, glyph: '✓' }
    case 'failed':
      return { color: 'red', isDim: false, isFlashing: false, isSolid: cyan, glyph: '✗' }
    case 'killed':
      return { color: 'red', isDim: false, isFlashing: false, isSolid: cyan, glyph: '⊘' }
    case 'waiting':
      return { color: 'gray', isDim: false, isFlashing: false, isSolid: cyan, glyph: '…' }
    default:
      return { color: 'gray', isDim: true, isFlashing: false, isSolid: cyan, glyph: '○' }
  }
}

export function aggregateStatus(recs: readonly Rec[]): RecStatus {
  if (recs.some(r => r.status === 'running')) return 'running'
  if (recs.some(r => r.status === 'queued' || r.status === 'waiting')) return 'queued'
  if (recs.some(r => r.status === 'failed' || r.status === 'killed')) return 'failed'
  return recs.length === 0 ? 'queued' : 'done'
}

export function planItems(tasks: readonly Item[], todos: readonly Item[]): { done: number; total: number; current: string } {
  const items = [...tasks, ...todos]
  return {
    done: items.filter(i => i.status === 'done').length,
    total: items.length,
    current: items.find(i => i.status === 'active')?.label ?? '',
  }
}

export function grid<T>(items: readonly T[], perRow: number): T[][] {
  const n = Math.max(1, perRow)
  const rows: T[][] = []
  for (let i = 0; i < items.length; i += n) rows.push(items.slice(i, i + n))
  return rows
}

const esc = (s: string): string =>
  s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;')

type Pt = { x: number; y: number }

const SVG = {
  bg: '#0a1220',
  edge: '#164e63',
  cyan: '#22d3ee',
  cyanDim: '#155e75',
  greyHi: '#cbd5e1',
  greyLo: '#64748b',
  green: '#22c55e',
  red: '#ef4444',
  text: '#e2e8f0',
  muted: '#94a3b8',
  node: '#0f1b2e',
}

function lineAttrs(status: RecStatus, tick: number, isSelected: boolean): string {
  if (isSelected) return `stroke="${SVG.cyan}" stroke-width="2.2" stroke-opacity="1"`
  const dots = 'stroke-dasharray="1.5 4.5" stroke-linecap="round" stroke-width="1.8"'
  if (status === 'running') {
    return tick % 2 === 0
      ? `stroke="${SVG.greyHi}" stroke-opacity="1" ${dots}`
      : `stroke="${SVG.greyLo}" stroke-opacity="0.35" ${dots}`
  }
  if (status === 'done') return `stroke="${SVG.green}" stroke-opacity="1" ${dots}`
  if (status === 'failed' || status === 'killed') return `stroke="${SVG.red}" stroke-opacity="1" ${dots}`
  return `stroke="${SVG.greyLo}" stroke-opacity="0.45" ${dots}`
}

function curve(a: Pt, b: Pt): string {
  const d = Math.max(10, Math.abs(b.y - a.y) * 0.45)
  return `M${a.x} ${a.y} C${a.x} ${a.y + d} ${b.x} ${b.y - d} ${b.x} ${b.y}`
}

export type SvgInput = {
  width: number
  rows: readonly Row[]
  tick: number
  selectedId: string | null
  isMasterOn: boolean
}

export type SvgOut = { source: string; width: number; height: number; alt: string }

const R = 13
const CELL = 64
const ROW_H = 62

export function buildSvg(input: SvgInput): SvgOut {
  const W = Math.max(160, Math.round(input.width))
  const cx = W / 2
  const cols = Math.max(1, Math.floor((W - 16) / CELL))
  const hub: Pt = { x: cx, y: 62 }
  const pos = new Map<string, Pt>()
  let y = 92
  const depths = [...new Set(input.rows.map(r => r.depth))].sort((a, b) => a - b)
  for (const d of depths) {
    for (const row of grid(
      input.rows.filter(r => r.depth === d),
      cols,
    )) {
      row.forEach((r, i) => pos.set(r.rec.id, { x: (W - row.length * CELL) / 2 + CELL * i + CELL / 2, y: y + R }))
      y += ROW_H
    }
  }
  const H = Math.max(110, y + 6)
  const lines: string[] = []
  const nodes: string[] = []
  const rec = new Map(input.rows.map(r => [r.rec.id, r.rec]))

  const kids = input.rows.map(r => r.rec).filter(r => r.parentId === undefined || !rec.has(r.parentId))
  const trunkStatus = aggregateStatus(kids)
  if (input.rows.length > 0) {
    lines.push(`<path d="M${cx} 44 L${cx} ${hub.y}" fill="none" ${lineAttrs(trunkStatus, input.tick, false)}/>`)
  }
  for (const r of input.rows) {
    const to = pos.get(r.rec.id)!
    const parent = r.rec.parentId === undefined ? undefined : pos.get(r.rec.parentId)
    const from: Pt = parent === undefined ? hub : { x: parent.x, y: parent.y + R + 2 }
    const sel = input.selectedId === r.rec.id
    lines.push(
      `<path d="${curve(from, { x: to.x, y: to.y - R - 3 })}" fill="none" ${lineAttrs(r.rec.status, input.tick, sel)}/>`,
    )
  }
  for (const r of input.rows) {
    const p = pos.get(r.rec.id)!
    const s = r.rec.status
    const sel = input.selectedId === r.rec.id
    const ring = s === 'done' ? SVG.green : s === 'failed' || s === 'killed' ? SVG.red : s === 'running' ? SVG.greyHi : SVG.greyLo
    const g: string[] = []
    if (sel) g.push(`<circle cx="${p.x}" cy="${p.y}" r="${R + 5}" fill="none" stroke="${SVG.cyan}" stroke-width="1.6" filter="url(#glow)"/>`)
    g.push(`<circle cx="${p.x}" cy="${p.y}" r="${R}" fill="${SVG.node}" stroke="${ring}" stroke-width="1.8"/>`)
    if (s === 'running') {
      const rot = (input.tick * 60) % 360
      g.push(
        `<circle cx="${p.x}" cy="${p.y}" r="${R - 5}" fill="none" stroke="${SVG.cyan}" stroke-width="2" stroke-linecap="round" stroke-dasharray="14 40" transform="rotate(${rot} ${p.x} ${p.y})"/>`,
      )
    } else if (s === 'done') {
      g.push(`<path d="M${p.x - 5} ${p.y} L${p.x - 1.5} ${p.y + 4} L${p.x + 5.5} ${p.y - 4}" fill="none" stroke="${SVG.green}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>`)
    } else if (s === 'failed' || s === 'killed') {
      g.push(`<path d="M${p.x - 4.5} ${p.y - 4.5} L${p.x + 4.5} ${p.y + 4.5} M${p.x + 4.5} ${p.y - 4.5} L${p.x - 4.5} ${p.y + 4.5}" fill="none" stroke="${SVG.red}" stroke-width="2.2" stroke-linecap="round"/>`)
    } else {
      g.push(`<circle cx="${p.x}" cy="${p.y}" r="2.2" fill="${SVG.greyLo}"/>`)
    }
    g.push(
      `<text x="${p.x}" y="${p.y + R + 13}" text-anchor="middle" font-size="9" fill="${sel ? SVG.cyan : SVG.text}" font-family="system-ui,sans-serif">${r.index} ${esc(clip(r.rec.name, 9))}</text>`,
    )
    nodes.push(`<g>${g.join('')}</g>`)
  }
  const diamond = `${cx},${12} ${cx + 16},${28} ${cx},${44} ${cx - 16},${28}`
  const inner = `${cx},${20} ${cx + 8},${28} ${cx},${36} ${cx - 8},${28}`
  const c = counts(input.rows.map(r => r.rec))
  const master =
    `<polygon points="${diamond}" fill="${SVG.node}" stroke="${SVG.cyan}" stroke-width="1.8" filter="url(#glow)"/>` +
    `<polygon points="${inner}" fill="${input.isMasterOn ? SVG.cyan : SVG.cyanDim}"/>` +
    `<text x="${cx + 24}" y="26" font-size="10" font-weight="700" fill="${SVG.text}" font-family="system-ui,sans-serif">MASTER AGENT</text>` +
    `<text x="${cx + 24}" y="38" font-size="9" fill="${SVG.muted}" font-family="system-ui,sans-serif">(Orchestrator)</text>`
  const source =
    `<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}">` +
    `<defs><filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="2.2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>` +
    `<rect x="0.5" y="0.5" width="${W - 1}" height="${H - 1}" rx="10" fill="${SVG.bg}" stroke="${SVG.edge}"/>` +
    lines.join('') +
    nodes.join('') +
    master +
    `</svg>`
  const alt = `Master agent with ${c.total} subagents: ${c.done} done, ${c.running} running, ${c.queued} queued, ${c.failed} failed`
  return { source, width: W, height: H, alt }
}
