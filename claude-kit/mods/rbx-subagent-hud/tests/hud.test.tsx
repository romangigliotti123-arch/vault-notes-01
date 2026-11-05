import { expect, mock, test } from 'claude-code/testing'
import type { AgentStatus, On } from 'claude-code'

import type { Hist, Rec } from '../types'
import {
  MAX_PROMPTS,
  MAX_PROMPT_CHARS,
  addPrompt,
  buildRows,
  classOf,
  counts,
  emptyHist,
  estimate,
  etaLabel,
  dotOf,
  progressOf,
  typicalFor,
  mergeRecs,
  median,
  recordDuration,
  recordWrap,
} from '../hooks/logic'

const NAME = 'rbx-subagent-hud'
const T0 = 1_000_000

type Listed = { id: string; description: string; type: string; status: AgentStatus; parentId?: string }

const PANE = {
  plugin: NAME,
  component: 'Pane',
  requestId: NAME,
  props: {
    title: 'Subagents',
    isFocused: false,
    bodyColumns: 44,
    placement: 'dock',
    scroll: { offset: 0, bodyRows: 20 },
    view: {},
  },
} as const

const rec = (over: Partial<Rec> & { id: string }): Rec => ({
  name: over.id,
  type: 'general-purpose',
  status: 'running',
  start: T0,
  turn: 1,
  ...over,
})

const histOf = (samples: number[], wrap: number[], type = 'general-purpose', name = 'Build terrain'): Hist => ({
  v: 1,
  byClass: { [classOf(type, name)]: samples },
  byType: { [type]: samples },
  wrap,
})

test('tree: spawn, parallel spawn, finish, fail and nested agents', () => {
  const one = mergeRecs([], [{ id: 'a', description: 'Build terrain', type: 'general-purpose', status: 'running' }], T0, 1, {})
  expect(one.map(r => [r.id, r.status])).toEqual([['a', 'running']])

  const three: Listed[] = [
    { id: 'a', description: 'Build terrain', type: 'general-purpose', status: 'running' },
    { id: 'b', description: 'Write shop UI', type: 'general-purpose', status: 'running' },
    { id: 'c', description: 'Audit scripts', type: 'Explore', status: 'running' },
  ]
  const par = mergeRecs(one, three, T0 + 1000, 1, {})
  expect(counts(par)).toEqual({ total: 3, done: 0, running: 3, queued: 0, failed: 0 })

  const fin = mergeRecs(par, [{ ...three[0]!, status: 'completed' }, three[1]!], T0 + 61_000, 1, {
    c: { at: T0 + 60_500, status: 'failed' },
  })
  expect(fin.map(r => [r.id, r.status])).toEqual([
    ['a', 'done'],
    ['b', 'running'],
    ['c', 'failed'],
  ])
  expect(fin.find(r => r.id === 'a')?.end).toBe(T0 + 61_000)
  expect(fin.find(r => r.id === 'c')?.end).toBe(T0 + 60_500)
  expect(counts(fin)).toEqual({ total: 3, done: 1, running: 1, queued: 0, failed: 1 })

  const nested = mergeRecs(
    fin,
    [...three, { id: 'd', description: 'Place trees', type: 'general-purpose', status: 'running', parentId: 'a' }],
    T0 + 62_000,
    1,
    {},
  )
  expect(buildRows(nested).map(r => [r.rec.id, r.depth, r.index])).toEqual([
    ['a', 1, 1],
    ['b', 1, 2],
    ['c', 1, 3],
    ['d', 2, 4],
  ])
  expect(nested.find(r => r.id === 'a')?.status).toBe('done')
})

test('tree: an agent gone from the list is closed, a pending one is queued, an orphan child is a root', () => {
  const next = mergeRecs(
    [rec({ id: 'a' })],
    [{ id: 'q', description: 'later', type: 'Plan', status: 'pending', parentId: 'gone' }],
    T0 + 5000,
    1,
    {},
  )
  expect(next.find(r => r.id === 'a')).toMatchObject({ status: 'done', end: T0 + 5000 })
  expect(next.find(r => r.id === 'q')?.status).toBe('queued')
  expect(buildRows(next).map(r => r.depth)).toEqual([1, 1])
})

test('counter: done of total, running and failed', () => {
  const recs = [rec({ id: 'a', status: 'done' }), rec({ id: 'b', status: 'done' }), rec({ id: 'c' }), rec({ id: 'd', status: 'killed' })]
  expect(counts(recs)).toEqual({ total: 4, done: 2, running: 1, queued: 0, failed: 1 })
  expect(counts([])).toEqual({ total: 0, done: 0, running: 0, queued: 0, failed: 0 })
})

test('estimate: no history shows estimating with a default and low confidence', () => {
  const eta = estimate([rec({ id: 'a' })], emptyHist(), T0 + 30_000)
  expect(eta).toEqual({ kind: 'estimating', ms: 120_000 - 30_000 + 20_000, conf: 'low' })
  expect(etaLabel(eta)).toBe('estimating... (~2 min, low confidence)')
})

test('estimate: with history, parallel agents finish at the longest, plus the master wrap-up', () => {
  const hist = histOf([60_000, 80_000], [10_000, 14_000, 12_000])
  const now = T0 + 30_000
  const one = estimate([rec({ id: 'a', name: 'Build terrain 2' })], hist, T0 + 10_000)
  expect(one).toEqual({ kind: 'est', ms: 70_000 - 10_000 + 12_000, conf: 'ok' })
  expect(etaLabel(one)).toBe('~2 min left (estimate)')

  const par = estimate(
    [rec({ id: 'a', name: 'Build terrain' }), rec({ id: 'b', name: 'Build terrain', start: T0 + 20_000 })],
    hist,
    now,
  )
  expect(par.ms).toBe(70_000 - 10_000 + 12_000)
})

test('estimate: never negative, floors an overrun agent, ignores finished agents', () => {
  const hist = histOf([60_000, 60_000], [0])
  const late = estimate([rec({ id: 'a', name: 'Build terrain' })], hist, T0 + 500_000)
  expect(late.ms).toBe(10_000)
  expect(late.conf).toBe('low')
  expect(etaLabel(late)).toBe('<1 min left (estimate, low confidence)')

  const done = estimate([rec({ id: 'a', status: 'done' })], hist, T0 + 500_000)
  expect(done.kind).toBe('none')
  expect(etaLabel(done)).toBe('')
  expect(estimate([rec({ id: 'a' })], hist, T0).kind).toBe('est')
  expect(estimate([rec({ id: 'q', status: 'queued', name: 'Build terrain' })], hist, T0).ms).toBe(60_000)
})

test('history: rolling median is bounded and ignores bad durations', () => {
  let h = emptyHist()
  for (let i = 0; i < 30; i++) h = recordDuration(h, { type: 'Explore', name: `scan ${i}`, start: 0, end: 1000 + i * 1000 })
  expect(h.byType['Explore']?.length).toBe(20)
  expect(h.byClass[classOf('Explore', 'scan 1')]?.length).toBe(20)
  expect(median([3, 1, 2])).toBe(2)
  expect(median([1, 2, 3, 4])).toBe(3)
  expect(recordDuration(h, { type: 'Explore', name: 'x', start: 0, end: 10 })).toBe(h)
  expect(recordDuration(h, { type: 'Explore', name: 'x', start: 0, end: 7 * 3600_000 })).toBe(h)
  for (let i = 0; i < 60; i++) {
    h = recordDuration(h, { type: `t${i}`, name: `name${String.fromCharCode(97 + (i % 26))}${i}`, start: 0, end: 5000 })
  }
  expect(Object.keys(h.byClass).length).toBeLessThanOrEqual(40)
  expect(recordWrap(emptyHist(), 5000).wrap).toEqual([5000])
  expect(recordWrap(emptyHist(), 31 * 60_000).wrap).toEqual([])
})

test('dot: running pulses on theme keys, done and failed hold their colour, queued is hollow', () => {
  expect(dotOf('running', 0)).toMatchObject({ glyph: '●', color: 'text', isDim: false })
  expect(dotOf('running', 1)).toMatchObject({ color: 'text', isDim: true })
  expect(dotOf('running', 2).isDim).toBe(false)
  for (const tick of [0, 1, 2, 3]) {
    expect(dotOf('done', tick)).toMatchObject({ color: 'success', isDim: false })
    expect(dotOf('failed', tick)).toMatchObject({ color: 'error', isDim: false })
    expect(dotOf('killed', tick).color).toBe('error')
  }
  expect(dotOf('queued', 0)).toMatchObject({ glyph: '○', color: 'inactive' })
})

test('progress: ended is full, running follows the typical time (capped), unknown without history, queued empty', () => {
  const none = typicalFor(emptyHist(), { type: 'general-purpose', name: 'x' })
  const known = typicalFor(histOf([60_000, 60_000], []), { type: 'general-purpose', name: 'Build terrain' })
  expect(progressOf('done', 5, none)).toEqual({ frac: 1, isKnown: true })
  expect(progressOf('failed', 5, none)).toEqual({ frac: 1, isKnown: true })
  expect(progressOf('running', 30_000, known)).toEqual({ frac: 0.5, isKnown: true })
  expect(progressOf('running', 600_000, known).frac).toBe(0.95)
  expect(progressOf('running', 0, known).frac).toBe(0.03)
  expect(progressOf('running', 30_000, none).isKnown).toBe(false)
  expect(progressOf('queued', 0, known)).toEqual({ frac: 0, isKnown: true })
})

test('prompts: capped in number and length, newest kept, same call replaced', () => {
  let list: ReturnType<typeof addPrompt> = []
  for (let i = 0; i < 70; i++) {
    list = addPrompt(list, {
      id: `a${i}`,
      toolUseId: `t${i}`,
      text: 'x'.repeat(i === 69 ? 50_000 : 10),
      chars: 0,
      isTruncated: false,
      description: 'd',
      type: 't',
    })
  }
  expect(list).toHaveLength(MAX_PROMPTS)
  expect(list[0]?.id).toBe('a20')
  const last = list[list.length - 1]!
  expect(last.text.length).toBe(MAX_PROMPT_CHARS)
  expect(last.chars).toBe(50_000)
  expect(last.isTruncated).toBe(true)
  const again = addPrompt(list, { id: 'a69', toolUseId: 't69', text: 'short', chars: 0, isTruncated: false, description: 'd', type: 't' })
  expect(again).toHaveLength(MAX_PROMPTS)
  expect(again[again.length - 1]?.text).toBe('short')
})

function world(on: On, entries?: Record<string, unknown>, isPlaced = true) {
  const clock = mock.clock(on, { now: T0 })
  mock.store(on, entries)
  const w = { agents: [] as Listed[], opened: 0, spawned: 0, viewed: [] as (string | undefined)[] }
  on('command.register', () => ({ value: { command: NAME } }))
  on('ui.open', () => {
    w.opened += 1
    return { value: isPlaced ? { isPlaced: true as const } : { isPlaced: false as const, reason: 'narrow' } }
  })
  on('ui.panes', () => ({ value: [] }))
  on('ui.view', (_, e) => {
    w.viewed.push(e.agentId)
    return { value: {} }
  })
  on('session.start', (_, e) => ({ cwd: e.cwd }))
  on('tool.call', () => ({ result: {} }))
  on('fs.exists', () => ({ value: false }))
  on('agent.list', () => ({ value: w.agents }))
  on('agent.spawn', (_, e) => {
    w.spawned += 1
    const id = `ag${w.spawned}`
    w.agents = [...w.agents, { id, description: e.description, type: e.subagentType, status: 'running', parentId: e.parentAgentId }]
    return { agentId: id, model: 'sonnet' }
  })
  on('prompt.submit', (_, e) => ({ text: e.text }))
  on('turn.start', () => ({ turnId: 't' }))
  on('turn.complete', () => ({ text: '' }))
  return { clock, w }
}

const spawnArgs = (prompt: string, description: string, subagentType = 'general-purpose', extra: object = {}) => ({
  tool_use_id: `tu-${description}`,
  prompt,
  description,
  subagentType,
  provider: { plugin: 'engine', tier: 'core' as const },
  parentModel: 'opus',
  background: false,
  fork: false,
  ...extra,
})

const listed = (id: string, description: string, status: AgentStatus = 'running', parentId?: string): Listed => ({
  id,
  description,
  type: 'general-purpose',
  status,
  parentId,
})

test('master turn: counter 2/4 done, resets on a new turn, estimate and elapsed update every second', async ($, on) => {
  const { clock, w } = world(on, { hist: histOf([60_000, 80_000], [10_000]) })
  await $.session.start({ cwd: '/', surface: 'terminal', isInteractive: true })
  await $.turn.start({ text: 'build it', turnId: 'm1' })
  const names = ['Build terrain', 'Write shop UI', 'Audit scripts', 'Place trees']
  for (const n of names) await $.agent.spawn(spawnArgs(`do ${n}`, n))
  w.agents = names.map((n, i) => listed(`ag${i + 1}`, n))
  await clock.advance(1000)

  let ui = await $.ui.mount({ ...PANE, surface: 'terminal' })
  expect((await ui.find({ type: 'Text', text: /\/4 done/ }))?.text).toBe('0/4 done')
  expect((await ui.find({ type: 'Text', text: /left/ }))?.text).toMatch(/^~\d+ min left \(estimate/)
  expect((await ui.find({ type: 'Text', text: /working/ }))?.text).toBe('working')

  w.agents = w.agents.map((a, i): Listed => (i < 2 ? { ...a, status: 'completed' } : a))
  await clock.advance(1000)
  expect((await ui.find({ type: 'Text', text: /\/4 done/ }))?.text).toBe('2/4 done')
  expect((await ui.find({ type: 'Text', text: /running/ }))?.text).toBe('  2 running  0 failed')

  const before = (await ui.find({ type: 'Text', text: /^ \d+[ms]/ }))?.text
  await clock.advance(5000)
  expect((await ui.find({ type: 'Text', text: /^ \d+[ms]/ }))?.text).not.toBe(before)

  w.agents = w.agents.map((a): Listed => ({ ...a, status: 'completed' }))
  await clock.advance(1000)
  expect((await ui.find({ type: 'Text', text: /\/4 done/ }))?.text).toBe('4/4 done')
  expect((await ui.find({ type: 'Text', text: /left/ })) === undefined).toBe(true)
  await ui.unmount()

  await $.turn.complete({ answer: 'ok', durationMs: 1, isAborted: false, turnId: 'm1', reason: 'answer' })
  await $.prompt.submit({ text: 'next', wait: false, origin: { kind: 'composer' } })
  await $.turn.start({ text: 'next', turnId: 'm2' })
  ui = await $.ui.mount({ ...PANE, surface: 'terminal' })
  expect((await ui.find({ type: 'Text', text: /No subagents in this turn/ }))?.text).toBe('No subagents in this turn.')
  expect(await ui.find({ type: 'Text', text: /\/4 done/ })).toBeUndefined()
  await ui.unmount()
})

test('master turn: no running agents shows elapsed only, no estimate', async ($, on) => {
  const { clock } = world(on)
  await $.session.start({ cwd: '/', surface: 'terminal', isInteractive: true })
  await $.turn.start({ text: 'think', turnId: 'm1' })
  await clock.advance(65_000)
  const ui = await $.ui.mount({ ...PANE, surface: 'terminal' })
  expect((await ui.find({ type: 'Text', text: /^ \d+m/ }))?.text).toBe(' 1m05s')
  expect(await ui.find({ type: 'Text', text: /left|estimating/ })).toBeUndefined()
  await ui.unmount()
})

test('master turn: with no history the pane says estimating and low confidence', async ($, on) => {
  const { clock, w } = world(on)
  await $.session.start({ cwd: '/', surface: 'terminal', isInteractive: true })
  await $.turn.start({ text: 'go', turnId: 'm1' })
  await $.agent.spawn(spawnArgs('p', 'Build terrain'))
  w.agents = [listed('ag1', 'Build terrain')]
  await clock.advance(1000)
  const ui = await $.ui.mount({ ...PANE, surface: 'terminal' })
  expect((await ui.find({ type: 'Text', text: /estimating/ }))?.text).toBe('estimating... (~3 min, low confidence)')
  await ui.unmount()
})

test('finished agents feed the history that later estimates use', async ($, on) => {
  const { clock, w } = world(on)
  await $.session.start({ cwd: '/', surface: 'terminal', isInteractive: true })
  for (const turnId of ['m1', 'm2']) {
    await $.prompt.submit({ text: 'go', wait: false, origin: { kind: 'composer' } })
    await $.turn.start({ text: 'go', turnId })
    await $.agent.spawn(spawnArgs('p', 'Build terrain'))
    w.agents = [listed(`ag${w.spawned}`, 'Build terrain')]
    await clock.advance(1000)
    await clock.advance(40_000)
    w.agents = [listed(`ag${w.spawned}`, 'Build terrain', 'completed')]
    await clock.advance(1000)
    await $.turn.complete({ answer: 'ok', durationMs: 1, isAborted: false, turnId, reason: 'answer' })
  }
  await $.prompt.submit({ text: 'go', wait: false, origin: { kind: 'composer' } })
  await $.turn.start({ text: 'go', turnId: 'm3' })
  await $.agent.spawn(spawnArgs('p', 'Build terrain'))
  w.agents = [listed(`ag${w.spawned}`, 'Build terrain')]
  await clock.advance(2000)
  const ui = await $.ui.mount({ ...PANE, surface: 'terminal' })
  expect((await ui.find({ type: 'Text', text: /left/ }))?.text).toBe('<1 min left (estimate)')
  await ui.unmount()
})

test('pulsing dot: bright and dim alternate each tick while running, turn green and hold when done', async ($, on) => {
  const { clock, w } = world(on)
  await $.session.start({ cwd: '/', surface: 'terminal', isInteractive: true })
  await $.turn.start({ text: 'go', turnId: 'm1' })
  await $.agent.spawn(spawnArgs('p', 'Build terrain'))
  w.agents = [listed('ag1', 'Build terrain')]
  await clock.advance(500)
  const ui = await $.ui.mount({ ...PANE, surface: 'terminal' })
  const dot = async () => (await ui.find({ type: 'Text', text: '●' }))?.props
  const seen: unknown[] = []
  for (let i = 0; i < 4; i++) {
    seen.push((await dot())?.['dimColor'] === true)
    await clock.advance(500)
  }
  expect(seen[0]).not.toBe(seen[1])
  expect(seen[0]).toBe(seen[2])
  expect((await dot())?.['color']).toBe('text')
  w.agents = [listed('ag1', 'Build terrain', 'completed')]
  await clock.advance(1000)
  for (let i = 0; i < 4; i++) {
    const p = await dot()
    expect([p?.['color'], p?.['dimColor']]).toEqual(['success', false])
    await clock.advance(500)
  }
  await ui.unmount()
})

test('failed agent: red dot, queued agent hollow grey, failed count in the summary', async ($, on) => {
  const { clock, w } = world(on)
  await $.session.start({ cwd: '/', surface: 'terminal', isInteractive: true })
  await $.turn.start({ text: 'go', turnId: 'm1' })
  await $.agent.spawn(spawnArgs('p', 'Build terrain'))
  await $.agent.spawn(spawnArgs('p', 'Later task'))
  w.agents = [listed('ag1', 'Build terrain', 'failed'), listed('ag2', 'Later task', 'pending')]
  await clock.advance(1000)
  const ui = await $.ui.mount({ ...PANE, surface: 'terminal' })
  expect((await ui.find({ type: 'Text', text: '●' }))?.props['color']).toBe('error')
  expect((await ui.find({ type: 'Text', text: '○' }))?.props['color']).toBe('inactive')
  expect((await ui.find({ type: 'Text', text: /1 failed/ }))?.text).toContain('1 failed')
  await ui.unmount()
})

test('click: a subagent shows the prompt the master sent, again or close dismisses, show more expands', async ($, on) => {
  const { clock, w } = world(on)
  await $.session.start({ cwd: '/', surface: 'terminal', isInteractive: true })
  await $.turn.start({ text: 'go', turnId: 'm1' })
  const long = 'CONTEXT: ' + 'lorem ipsum '.repeat(120)
  await $.agent.spawn(spawnArgs(long, 'Build terrain', 'general-purpose', { model: 'haiku' }))
  await $.agent.spawn(spawnArgs('Short prompt', 'Write shop UI', 'Explore'))
  w.agents = [listed('ag1', 'Build terrain'), listed('ag2', 'Write shop UI')]
  await clock.advance(1000)
  const ui = await $.ui.mount({ ...PANE, surface: 'terminal' })
  expect(await ui.find({ type: 'Text', text: /PROMPT \(from Master Agent\)/ })).toBeUndefined()

  await ui.press({ key: 'agent:ag2' })
  expect((await ui.find({ type: 'Text', text: /SUBAGENT 2 PROMPT/ }))?.text).toBe('SUBAGENT 2 PROMPT (from Master Agent)')
  expect((await ui.find({ type: 'Text', text: 'Short prompt' }))?.text).toBe('Short prompt')
  expect(await ui.find({ key: 'card-more' })).toBeUndefined()

  await ui.press({ key: 'agent:ag2' })
  expect(await ui.find({ type: 'Text', text: /PROMPT \(from/ })).toBeUndefined()

  await ui.press({ key: 'agent:ag1' })
  const meta = await ui.find({ type: 'Text', text: /· running/ })
  expect(meta?.text).toContain('Build terrain · general-purpose · haiku · running')
  const preview = await ui.find({ type: 'Text', text: /^CONTEXT: lorem/ })
  expect(preview?.text.length).toBe(601)
  await ui.press({ key: 'card-more' })
  expect((await ui.find({ type: 'Text', text: /^CONTEXT: lorem/ }))?.text).toBe(long)
  await ui.press({ key: 'card-more' })
  expect((await ui.find({ type: 'Text', text: /^CONTEXT: lorem/ }))?.text.length).toBe(601)

  await ui.press({ key: 'agent:ag2' })
  expect((await ui.find({ type: 'Text', text: /SUBAGENT 2 PROMPT/ }))?.text).toContain('2')
  await ui.press({ key: 'card-close' })
  expect(await ui.find({ type: 'Text', text: /PROMPT \(from/ })).toBeUndefined()

  await ui.press({ key: 'agent:ag1' })
  await ui.press({ key: 'card-view' })
  expect(w.viewed).toEqual(['ag1'])
  await ui.unmount()
})

test('prompt capture is bounded in the pane: 60 long prompts keep the newest 50, 20000 chars each', async ($, on) => {
  const { clock, w } = world(on)
  await $.session.start({ cwd: '/', surface: 'terminal', isInteractive: true })
  await $.turn.start({ text: 'go', turnId: 'm1' })
  for (let i = 1; i <= 60; i++) await $.agent.spawn(spawnArgs('y'.repeat(30_000), `task ${i}`))
  w.agents = Array.from({ length: 60 }, (_, i) => listed(`ag${i + 1}`, `task ${i + 1}`))
  await clock.advance(1000)
  const ui = await $.ui.mount({ ...PANE, surface: 'terminal' })
  await ui.press({ key: 'agent:ag60' })
  await ui.press({ key: 'card-more' })
  const body = await ui.find({ type: 'Text', text: /^yyyy/ })
  expect(body?.text.length).toBe(MAX_PROMPT_CHARS)
  expect((await ui.find({ type: 'Text', text: /stored first 20000 of 30000/ }))?.text).toContain('30000')
  await ui.press({ key: 'agent:ag60' })
  await ui.press({ key: 'agent:ag5' })
  expect((await ui.find({ type: 'Text', text: /not captured/ }))?.text).toContain('not captured')
  await ui.unmount()
})

test('nested agents are drawn on a lower level, indented, with a rail', async ($, on) => {
  const { clock, w } = world(on)
  await $.session.start({ cwd: '/', surface: 'terminal', isInteractive: true })
  await $.turn.start({ text: 'go', turnId: 'm1' })
  await $.agent.spawn(spawnArgs('p', 'Build terrain'))
  await $.agent.spawn(spawnArgs('p', 'Place trees', 'general-purpose', { parentAgentId: 'ag1' }))
  w.agents = [listed('ag1', 'Build terrain'), listed('ag2', 'Place trees', 'running', 'ag1')]
  await clock.advance(1000)
  const ui = await $.ui.mount({ ...PANE, surface: 'terminal' })
  expect((await ui.find({ type: 'Text', text: /2\. Place trees/ }))?.text).toContain('2. Place trees')
  expect((await ui.find({ type: 'Text', text: /^├╴/ }))?.text).toBe('├╴\n│\n│')
  expect((await ui.find({ type: 'Text', text: /^╰╴/ }))?.text).toBe('╰╴\n \n ')
  await ui.unmount()
})

test('narrow pane: 24 columns keeps every row inside the width', async ($, on) => {
  const { clock, w } = world(on)
  await $.session.start({ cwd: '/', surface: 'terminal', isInteractive: true })
  await $.turn.start({ text: 'go', turnId: 'm1' })
  for (let i = 1; i <= 5; i++) await $.agent.spawn(spawnArgs('p', `A very long description number ${i}`))
  w.agents = Array.from({ length: 5 }, (_, i) => listed(`ag${i + 1}`, `A very long description number ${i + 1}`))
  await clock.advance(1000)
  const ui = await $.ui.mount({ ...PANE, props: { ...PANE.props, bodyColumns: 24 }, surface: 'terminal' })
  const buttons = await ui.findAll({ type: 'Button' })
  expect(buttons.length).toBe(5)
  for (const b of buttons) expect(b.text.length).toBeLessThanOrEqual(24 - 2)
  const bars = await ui.findAll({ type: 'Text', text: /^━+$/ })
  expect(bars.length).toBeGreaterThan(0)
  for (const t of bars) expect(t.text.length).toBeLessThanOrEqual(24)
  await ui.unmount()
})

test('every surface draws the same native layout: no Svg, a Button per subagent, prompt on click', async ($, on) => {
  const { clock, w } = world(on)
  await $.session.start({ cwd: '/', surface: 'desktop', isInteractive: true })
  await $.turn.start({ text: 'go', turnId: 'm1' })
  await $.agent.spawn(spawnArgs('Prompt text', 'Build terrain'))
  await $.agent.spawn(spawnArgs('p', 'Write shop UI'))
  w.agents = [listed('ag1', 'Build terrain'), listed('ag2', 'Write shop UI', 'completed')]
  await clock.advance(1000)
  for (const surface of ['desktop', 'vscode', 'mobile', 'terminal'] as const) {
    const ui = await $.ui.mount({ ...PANE, surface })
    expect(await ui.find({ type: 'Svg' })).toBeUndefined()
    expect(await ui.findAll({ type: 'Button', text: /\d\. / })).toHaveLength(2)
    expect((await ui.find({ type: 'Text', text: /1\/2 done/ }))?.text).toBe('1/2 done')
    expect((await ui.find({ type: 'Text', text: /^Master/ }))?.text).toBe('Master ')
    await ui.press({ key: 'agent:ag1' })
    expect((await ui.find({ type: 'Text', text: 'Prompt text' }))?.text).toBe('Prompt text')
    await ui.press({ key: 'agent:ag1' })
    await ui.unmount()
  }
})

test('re-render is stable: the same state draws the same tree', async ($, on) => {
  const { clock, w } = world(on)
  await $.session.start({ cwd: '/', surface: 'terminal', isInteractive: true })
  await $.turn.start({ text: 'go', turnId: 'm1' })
  await $.agent.spawn(spawnArgs('p', 'Build terrain'))
  w.agents = [listed('ag1', 'Build terrain', 'completed')]
  await clock.advance(1000)
  const ui = await $.ui.mount({ ...PANE, surface: 'terminal' })
  await $.turn.complete({ answer: 'ok', durationMs: 1, isAborted: false, turnId: 'm1', reason: 'answer' })
  await clock.advance(3000)
  const a = JSON.stringify(await ui.drawn())
  await ui.redraw()
  await ui.redraw()
  expect(JSON.stringify(await ui.drawn())).toBe(a)
  await clock.advance(5000)
  expect(JSON.stringify(await ui.drawn())).toBe(a)
  await ui.unmount()
})

test('reload: values an earlier version stored under another shape are declined, history in the store is kept', async ($, on) => {
  const { clock } = world(on, { hist: histOf([60_000, 80_000], [10_000]) })
  on('state.get', () => ({ value: { value: [{ tool: 'Bash' }], version: 1 } }))
  await $.session.start({ cwd: '/', surface: 'terminal', isInteractive: true })
  await clock.advance(1000)
  const ui = await $.ui.mount({ ...PANE, surface: 'terminal' })
  expect((await ui.find({ type: 'Text', text: /No subagents/ }))?.text).toBe('No subagents in this turn.')
  await ui.unmount()
})

test('plan bar: shown as a compact line when tasks or todos exist', async ($, on) => {
  world(on)
  await $.session.start({ cwd: '/', surface: 'terminal', isInteractive: true })
  await $.tool.call({
    tool: 'TodoWrite',
    todos: [
      { content: 'a', activeForm: 'Doing a', status: 'completed' },
      { content: 'b', activeForm: 'Doing b', status: 'in_progress' },
    ],
  })
  const ui = await $.ui.mount({ ...PANE, surface: 'terminal' })
  expect((await ui.find({ type: 'Text', text: /plan/ }))?.text).toBe(' 50% plan 1/2')
  expect(await ui.find({ type: 'Text', text: /^━+$/ })).toBeDefined()
  await ui.unmount()
})

test('the command opens the pane, and the line above the prompt shows the counter when no pane is placed', async ($, on) => {
  const { clock, w } = world(on, undefined, false)
  await $.session.start({ cwd: '/', surface: 'terminal', isInteractive: true })
  const run = await $.command.run({ command: NAME, args: '' } as never)
  expect(run).toMatchObject({ text: 'Subagent HUD opened.' })
  await $.turn.start({ text: 'go', turnId: 'm1' })
  await $.agent.spawn(spawnArgs('p', 'Build terrain'))
  w.agents = [listed('ag1', 'Build terrain')]
  await clock.advance(1000)
  const above = await $.ui.mount({
    plugin: NAME,
    component: 'AbovePrompt',
    requestId: 'above',
    surface: 'terminal',
    props: { hasSurvey: false, isWorking: false, maxRows: 5, bodyColumns: 80 } as never,
  } as never)
  expect((await above.find({ type: 'Text', text: /done/ }))?.text).toBe('0/1 done')
  await above.unmount()
})

test('background agents: the counter survives the continuation turns they cause, and the master shows as waiting', async ($, on) => {
  const { clock, w } = world(on, { hist: histOf([60_000, 80_000], [10_000]) })
  await $.session.start({ cwd: '/', surface: 'terminal', isInteractive: true })
  await $.prompt.submit({ text: 'build it', wait: false, origin: { kind: 'composer' } })
  await $.turn.start({ text: 'build it', turnId: 'm1' })
  await $.agent.spawn(spawnArgs('p', 'Build terrain'))
  await $.agent.spawn(spawnArgs('p', 'Write shop UI'))
  await $.turn.complete({ answer: 'started', durationMs: 1, isAborted: false, turnId: 'm1', reason: 'answer' })
  await clock.advance(20_000)
  const ui = await $.ui.mount({ ...PANE, surface: 'terminal' })
  expect((await ui.find({ type: 'Text', text: /waiting for agents/ }))?.text).toBe('waiting for agents')
  expect((await ui.find({ type: 'Text', text: /left/ }))?.text).toMatch(/^~\d+ min left/)
  expect((await ui.find({ type: 'Text', text: /\/2 done/ }))?.text).toBe('0/2 done')

  w.agents = w.agents.map((a, i): Listed => (i === 0 ? { ...a, status: 'completed' } : a))
  await $.prompt.submit({ text: '<agent-message>', wait: false, isMeta: true, origin: { kind: 'composer' } })
  await $.prompt.submit({ text: '<task-notification>', wait: false, origin: { kind: 'task-notification' } })
  await $.turn.start({ text: '<task-notification>', turnId: 'm2' })
  await clock.advance(2000)
  expect((await ui.find({ type: 'Text', text: /\/2 done/ }))?.text).toBe('1/2 done')
  expect((await ui.find({ type: 'Text', text: /working/ }))?.text).toBe('working')
  await ui.unmount()
})

test('wrap-up time after the last agent is recorded for later estimates', async ($, on) => {
  const { clock, w } = world(on)
  await $.session.start({ cwd: '/', surface: 'terminal', isInteractive: true })
  await $.prompt.submit({ text: 'go', wait: false, origin: { kind: 'composer' } })
  await $.turn.start({ text: 'go', turnId: 'm1' })
  await $.agent.spawn(spawnArgs('p', 'Build terrain'))
  await clock.advance(5000)
  w.agents = [listed('ag1', 'Build terrain', 'completed')]
  await clock.advance(1000)
  await clock.advance(90_000)
  await $.turn.complete({ answer: 'ok', durationMs: 1, isAborted: false, turnId: 'm1', reason: 'answer' })
  await $.prompt.submit({ text: 'again', wait: false, origin: { kind: 'composer' } })
  await $.turn.start({ text: 'again', turnId: 'm2' })
  await $.agent.spawn(spawnArgs('p', 'Build terrain'))
  w.agents = [...w.agents.filter(a => a.id === 'ag1'), listed('ag2', 'Build terrain')]
  await clock.advance(1000)
  const ui = await $.ui.mount({ ...PANE, surface: 'terminal' })
  expect((await ui.find({ type: 'Text', text: /left/ }))?.text).toBe('~2 min left (estimate, low confidence)')
  await ui.unmount()
})
