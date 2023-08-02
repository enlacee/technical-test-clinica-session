import { describe, it, expect } from 'vitest'

import { mount } from '@vue/test-utils'
import TheHeader from '../TheHeader.vue'

describe('TheHeader', () => {
  it('renders properly', () => {
    const wrapper = mount(TheHeader, { props: { msg: 'This is a title example' } })
    expect(wrapper.text()).toContain('This is a title example')
  })
})
