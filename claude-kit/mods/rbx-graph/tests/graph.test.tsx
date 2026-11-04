import { expect, test } from 'claude-code/testing'

const LINK = 'https://vault-hhmi60uo.netlify.app/#graph'

test('/rbx-graph replies with only the graph link and opens no pane', async ($, on) => {
  let opened = 0
  let registered = ''
  on('command.register', (_, e) => {
    registered = e.name
    return { value: { command: e.name } }
  })
  on('ui.open', () => {
    opened++
    return { value: { isPlaced: true } }
  })
  on('session.start', (_, e) => ({ cwd: e.cwd }))

  await $.session.start({ cwd: '/', surface: 'terminal', isInteractive: true })
  const r = await $.command.run({ command: 'rbx-graph', args: '', origin: { kind: 'person' } } as never)

  expect(registered).toBe('rbx-graph')
  expect(r.text).toBe(LINK)
  expect(opened).toBe(0)
})
