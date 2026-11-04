import type { Register } from 'claude-code'

const LINK = 'https://vault-hhmi60uo.netlify.app/#graph'

export const register: Register = on => {
  on('session.start', async ($, e, next) => {
    const result = await next(e)
    await $.command.register({ name: 'rbx-graph', description: 'Show the link to the vault graph site' })
    return result
  })

  on('command.run', { command: 'rbx-graph' }, () => ({ text: LINK }))
}
