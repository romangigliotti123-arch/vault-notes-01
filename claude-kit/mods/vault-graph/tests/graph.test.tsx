import { expect, test } from 'claude-code/testing'

const PANE = {
  plugin: 'vault-graph',
  component: 'Pane',
  requestId: 'vault-graph',
  props: {
    title: 'Vault graph',
    isFocused: false,
    bodyColumns: 44,
    placement: 'dock',
    scroll: { offset: 0, bodyRows: 30 },
    view: {},
  },
} as const

// A fake 6-note vault. Sorted by path the notes are:
// 0 Mentor/Delta, 1 Mentor/Gamma, 2 README, 3 Roblox/Alpha, 4 Roblox/Beta, 5 claude-kit/Epsilon
const long = Array.from({ length: 30 }, (_, n) => `line ${n + 1}`)
long[0] = 'line 1 [[Delta|d]]'
const FILES: Record<string, string> = {
  '/vault/README.md': 'Home. [[Alpha]] and [[Beta#part]].',
  '/vault/Roblox/Alpha.md': '[[README]] and [[Gamma]]',
  '/vault/Roblox/Beta.md': 'no links',
  '/vault/Mentor/Gamma.md': '[[Alpha]]',
  '/vault/Mentor/Delta.md': '[[README]]',
  '/vault/claude-kit/Epsilon.md': long.join('\n'),
}
const DIRS: Record<string, string[]> = {
  '/vault': ['README.md', 'Roblox', 'Mentor', 'claude-kit'],
  '/vault/Roblox': ['Alpha.md', 'Beta.md'],
  '/vault/Mentor': ['Gamma.md', 'Delta.md'],
  '/vault/claude-kit': ['Epsilon.md'],
}

const norm = (p: string): string => p.split(String.fromCharCode(92)).join('/').replace(/^[A-Za-z]:/, '')

type On = Parameters<Extract<Parameters<typeof test>[1], (...a: never[]) => unknown>>[1]

function wire(hook: On): void {
  const store = new Map<string, unknown>()
  hook('command.register', () => ({ value: { command: 'graph' } }))
  hook('ui.open', () => ({ value: { isPlaced: true } }))
  hook('ui.panes', () => ({ value: [] }))
  hook('session.start', (_, e) => ({ cwd: e.cwd }))
  hook('env.get', (_, e) => ({ value: e.name === 'CLAUDES_VAULT' ? '/vault' : undefined }))
  hook('fs.exists', (_, e) => ({
    value: norm(e.path) in DIRS || norm(e.path) in FILES,
  }))
  hook('fs.list', (_, e) => ({
    value: (DIRS[norm(e.path)] ?? []).map(name => ({
      name,
      kind: `${norm(e.path)}/${name}` in DIRS ? 'dir' : 'file',
      size: 1,
      mtimeMs: 5,
      isLink: false,
    })),
  }))
  hook('fs.read', (_, e) => ({ value: FILES[norm(e.path)] ?? '' }))
  hook('store.get', (_, e) => ({ value: store.get(e.key) }))
  hook('store.set', (_, e) => {
    store.set(e.key, e.value)
    return { value: undefined }
  })
}

const texts = async (ui: { findAll: (q: { type: string }) => Promise<{ text: string }[]> }) =>
  (await ui.findAll({ type: 'Text' })).map(t => t.text)

for (const surface of ['terminal', 'desktop'] as const) {
  test(`graph centres, re-centres, searches and previews (${surface})`, async ($, on) => {
    wire(on)
    await $.session.start({ cwd: '/', surface, isInteractive: true })
    await $.command.run({ command: 'graph', args: '', origin: { kind: 'person' } } as never)

    const ui = await $.ui.mount({ ...PANE, surface })

    // Default centre is README: 2 links out (Alpha, Beta), 2 in (Alpha, Delta).
    expect((await ui.find({ type: 'Text', text: /^README$/ }))?.text).toBe('README')
    expect(await texts(ui)).toContain('links in 2 · links out 2 · notes 6')
    expect(await ui.find({ key: 'out:3' })).toBeDefined()
    expect(await ui.find({ key: 'out:4' })).toBeDefined()
    expect(await ui.find({ key: 'in:0' })).toBeDefined()

    // Clicking Beta re-centres on it: one link in (README), none out.
    await ui.press({ key: 'out:4' })
    expect(await texts(ui)).toContain('links in 1 · links out 0 · notes 6')
    expect((await ui.find({ type: 'Text', text: /^Beta$/ }))?.text).toBe('Beta')

    // Search jumps to Epsilon: none in, Delta out.
    await ui.input({ key: 'search', text: 'eps', kind: 'submit' })
    expect(await texts(ui)).toContain('links in 0 · links out 1 · notes 6')
    expect((await ui.find({ type: 'Text', text: /^Epsilon$/ }))?.text).toBe('Epsilon')

    // The preview shows the first 20 lines, then the toggle goes back.
    await ui.press({ key: 'toggle' })
    expect(await ui.find({ type: 'Text', text: /^line 20$/ })).toBeDefined()
    expect(await ui.find({ type: 'Text', text: /^line 21$/ })).toBeUndefined()
    await ui.press({ key: 'toggle' })
    expect(await ui.find({ type: 'Text', text: /^line 20$/ })).toBeUndefined()
    expect(await texts(ui)).toContain('links in 0 · links out 1 · notes 6')
    await ui.unmount()
  })
}

test('with no placed pane the line above the prompt says to widen the window', async ($, on) => {
  wire(on)
  await $.session.start({ cwd: '/', surface: 'terminal', isInteractive: true })
  await $.command.run({ command: 'graph', args: '', origin: { kind: 'person' } } as never)
  const ui = await $.ui.mount({
    plugin: 'vault-graph',
    component: 'AbovePrompt',
    requestId: 'above',
    surface: 'terminal',
    props: { hasSurvey: false, isWorking: false, maxRows: 5, bodyColumns: 80 } as never,
  } as never)
  expect((await ui.find({ type: 'Text', text: /widen the window/ }))?.text).toBe(
    'widen the window to see the graph',
  )
  await ui.unmount()
})
