import { expect, test } from 'claude-code/testing'

const PANE = {
  plugin: 'workflow-hud',
  component: 'Pane',
  requestId: 'workflow-hud',
  props: {
    title: 'Workflow',
    isFocused: false,
    bodyColumns: 44,
    placement: 'dock',
    scroll: { offset: 0, bodyRows: 20 },
    view: {},
  },
} as const

type A = {
  id: string
  description: string
  type: string
  status: 'running' | 'completed'
  parentId?: string
}

const T0 = 1_000_000

test('pane draws the tree, the 50% bar and the elapsed times', async ($, on) => {
  let now = T0
  let agents: A[] = []
  let opened = 0
  on('command.register', () => ({ value: { command: 'hud' } }))
  on('ui.open', () => {
    opened += 1
    return { value: { isPlaced: true } }
  })
  on('ui.panes', () => ({ value: [] }))
  on('session.start', (_, e) => ({ cwd: e.cwd }))
  on('tool.call', () => ({ result: {} }))
  on('clock.now', () => ({ value: now }))
  on('clock.every', () => ({ value: undefined }))
  on('agent.list', () => ({ value: agents }))
  on('fs.exists', () => ({ value: false }))

  await $.session.start({ cwd: '/', surface: 'terminal', isInteractive: true })

  // The model calls the game dev workflow: the pane opens.
  await $.tool.call({ tool: 'Skill', skill: 'game-dev-workflow' })
  expect(opened).toBe(1)

  // Three workers of the master, one nested under the first.
  agents = [
    { id: 'a', description: 'Build terrain', type: 'general-purpose', status: 'running' },
    { id: 'b', description: 'Write shop UI', type: 'general-purpose', status: 'running' },
    { id: 'c', description: 'Audit scripts', type: 'general-purpose', status: 'running' },
    { id: 'd', description: 'Place trees', type: 'general-purpose', status: 'running', parentId: 'a' },
  ]
  const todos = (done: number) =>
    [0, 1, 2].map(n => ({
      content: `step ${n}`,
      activeForm: `Doing step ${n}`,
      status: n < done ? ('completed' as const) : n === done ? ('in_progress' as const) : ('pending' as const),
    }))
  await $.tool.call({ tool: 'TodoWrite', todos: todos(0) })

  // c finishes after a minute.
  now = T0 + 60_000
  agents = agents.map(a => (a.id === 'c' ? { ...a, status: 'completed' as const } : a))
  await $.tool.call({ tool: 'TodoWrite', todos: todos(1) })

  // 3m12s in: 2 of 3 plan items done, 1 of 3 batch workers done = 3 of 6.
  now = T0 + 192_000
  await $.tool.call({ tool: 'TodoWrite', todos: todos(2) })

  for (const surface of ['terminal', 'desktop'] as const) {
    const ui = await $.ui.mount({ ...PANE, surface })

    const pctText = await ui.find({ type: 'Text', text: /%/ })
    expect(pctText?.text.trim()).toBe('50%')

    const branches = (await ui.findAll({ type: 'Text', text: /[├└]─/ })).map(t => t.text)
    expect(branches).toEqual(['├─ ', '│  └─ ', '├─ ', '└─ '])

    const times = (await ui.findAll({ type: 'Text', text: /^ \d+[ms]/ })).map(t => t.text.trim())
    expect(times).toEqual(['3m12s', '3m12s', '3m12s', '3m12s', '1m00s'])

    expect((await ui.find({ type: 'Text', text: /Build terrain/ }))?.text).toContain('Build terrain')
    expect((await ui.find({ type: 'Text', text: /1\/3 workers/ }))?.text).toContain('2/3 tasks')
    await ui.unmount()
  }
})

test('the one-line fallback shows the bar and the working count when no pane is placed', async ($, on) => {
  on('command.register', () => ({ value: { command: 'hud' } }))
  on('ui.open', () => ({ value: { isPlaced: false, reason: 'narrow' } }))
  on('ui.panes', () => ({ value: [] }))
  on('session.start', (_, e) => ({ cwd: e.cwd }))
  on('tool.call', () => ({ result: {} }))
  on('clock.now', () => ({ value: T0 }))
  on('clock.every', () => ({ value: undefined }))
  on('fs.exists', () => ({ value: false }))
  on('agent.list', () => ({
    value: [
      { id: 'a', description: 'Build terrain', type: 'general-purpose', status: 'running' },
      { id: 'b', description: 'Write shop UI', type: 'general-purpose', status: 'completed' },
    ],
  }))

  await $.session.start({ cwd: '/', surface: 'terminal', isInteractive: true })
  await $.tool.call({ tool: 'Skill', skill: 'game-dev-workflow' })
  // A plan of 2 items, 1 done, and 1 worker of the batch working: 1 of 3.
  await $.tool.call({
    tool: 'TodoWrite',
    todos: [
      { content: 'a', activeForm: 'Doing a', status: 'completed' },
      { content: 'b', activeForm: 'Doing b', status: 'in_progress' },
    ],
  })

  const ui = await $.ui.mount({
    plugin: 'workflow-hud',
    component: 'AbovePrompt',
    requestId: 'above',
    surface: 'terminal',
    props: { hasSurvey: false, isWorking: false, maxRows: 5, bodyColumns: 80 } as never,
  } as never)
  expect((await ui.find({ type: 'Text', text: /33%/ }))?.text.trim()).toBe('33%')
  expect((await ui.find({ type: 'Text', text: /agent.? working/ }))?.text).toBe('1 agent working')
  await ui.unmount()
})
